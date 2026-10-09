#!/usr/bin/env python3
"""Publica o próximo carrossel da fila no Instagram @clinicasotre.

Tudo o que a publicação precisa mora neste repositório (pasta clinica-sotre/):
  fila.txt          uma pasta de carrosseis/ por linha, em ordem
  publicados.log    o que já foi publicado (nome, data, link)
  carrosseis/NOME/  slide_N.jpg + legenda.txt
Quando /mnt/project-files existe (sessões do projeto), a fila e os slides são
sincronizados de lá antes, e o log é copiado de volta.

Uso: python3 publicar.py            publica o próximo
     python3 publicar.py --teste    faz tudo menos o passo final de publicar
Token: variável INSTAGRAM_ACCESS_TOKEN (nunca é impressa).
"""
import json, os, re, shutil, subprocess, sys, time, urllib.error, urllib.parse, urllib.request
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parent
PROJETO = Path('/mnt/project-files/clinica-sotre')
IG = '17841473420265611'
G = 'https://graph.facebook.com/v21.0'
TOKEN = os.environ.get('INSTAGRAM_ACCESS_TOKEN')

def api(path, data=None, fields=None):
    url = f'{G}/{path}'
    if data is not None:
        req = urllib.request.Request(url, data=urllib.parse.urlencode(dict(data, access_token=TOKEN)).encode())
    else:
        req = urllib.request.Request(url + '?' + urllib.parse.urlencode({'fields': fields, 'access_token': TOKEN}))
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f'ERRO Meta API em {path.split("?")[0]}: {e.read().decode()[:300]}')

def git(*a):
    return subprocess.run(['git', '-C', str(REPO), *a], check=True, capture_output=True, text=True).stdout.strip()

def ler_fila(p):
    vistos, fila = set(), []
    for l in p.read_text().splitlines():
        l = l.strip()
        if l and not l.startswith('#') and l not in vistos:
            vistos.add(l); fila.append(l)
    return fila

def publicados():
    log = AQUI / 'publicados.log'
    return {l.split('\t')[0] for l in log.read_text().splitlines() if l.strip()} if log.exists() else set()

def sincronizar():
    """Copia fila, slides (PNG -> JPEG) e legendas do projeto para o repositório."""
    from PIL import Image
    fila = ler_fila(PROJETO / 'publicar' / 'fila.txt')
    (AQUI / 'fila.txt').write_text('\n'.join(fila) + '\n')
    for nome in fila:
        if nome in publicados():
            continue
        src = PROJETO / 'carrosseis' / nome
        dst = AQUI / 'carrosseis' / nome
        pngs = sorted((src / 'png-final').glob('slide_*.png'), key=lambda p: int(re.findall(r'\d+', p.stem)[0]))
        if not pngs or not (src / 'legenda.txt').exists():
            continue
        if dst.exists():
            shutil.rmtree(dst)
        dst.mkdir(parents=True)
        for i, s in enumerate(pngs, 1):
            Image.open(s).convert('RGB').save(dst / f'slide_{i}.jpg', quality=92)
        shutil.copy(src / 'legenda.txt', dst / 'legenda.txt')

def enviar(msg):
    git('add', 'clinica-sotre')
    if git('status', '--porcelain', 'clinica-sotre'):
        git('commit', '-qm', msg)
        for t in range(4):
            try:
                git('pull', '-q', '--rebase', '--autostash', 'origin', 'main'); git('push', '-q', 'origin', 'main'); break
            except subprocess.CalledProcessError:
                if t == 3: raise
                time.sleep(2 ** (t + 1))
    return git('rev-parse', 'HEAD')

def main():
    teste = '--teste' in sys.argv
    if not TOKEN:
        sys.exit('ERRO: INSTAGRAM_ACCESS_TOKEN não está definido')
    git('pull', '-q', '--rebase', '--autostash', 'origin', 'main')
    if PROJETO.exists():
        sincronizar()
    feitos = publicados()
    pend = [f for f in ler_fila(AQUI / 'fila.txt') if f not in feitos]
    if not pend:
        print('FILA VAZIA'); return
    nome = pend[0]; pasta = AQUI / 'carrosseis' / nome
    slides = sorted(pasta.glob('slide_*.jpg'), key=lambda p: int(re.findall(r'\d+', p.stem)[0]))
    if not 2 <= len(slides) <= 10 or not (pasta / 'legenda.txt').exists():
        sys.exit(f'ERRO: {nome} sem slides JPEG (2 a 10) ou sem legenda.txt no repositório')
    sha = enviar(f'Sincroniza fila da Clínica Sotre ({nome} é o próximo)')
    base = f'https://raw.githubusercontent.com/douglasmonteiro907/instagram/{sha}/clinica-sotre/carrosseis/{nome}'

    filhos = [api(f'{IG}/media', {'image_url': f'{base}/{s.name}', 'is_carousel_item': 'true'})['id'] for s in slides]
    c = api(f'{IG}/media', {'media_type': 'CAROUSEL', 'children': ','.join(filhos),
                            'caption': (pasta / 'legenda.txt').read_text().strip()})['id']
    for _ in range(30):
        st = api(c, fields='status_code').get('status_code')
        if st == 'FINISHED': break
        if st == 'ERROR': sys.exit(f'ERRO: o Instagram recusou as imagens do {nome}')
        time.sleep(5)
    else:
        sys.exit(f'ERRO: o Instagram não terminou de processar o {nome}')
    if teste:
        print(f'TESTE OK {nome}: {len(slides)} slides aceitos pelo Instagram, nada publicado | {len(pend)} na fila'); return

    pid = api(f'{IG}/media_publish', {'creation_id': c})['id']
    link = api(pid, fields='permalink').get('permalink', '')
    with (AQUI / 'publicados.log').open('a') as f:
        f.write(f'{nome}\t{time.strftime("%Y-%m-%d %H:%M")}\t{link}\n')
    enviar(f'Registra publicação do {nome} da Clínica Sotre')
    if PROJETO.exists():
        shutil.copy(AQUI / 'publicados.log', PROJETO / 'publicar' / 'publicados.log')
    print(f'PUBLICADO {nome} {link} | restam {len(pend) - 1} na fila')

if __name__ == '__main__':
    main()
