#!/usr/bin/env python3
"""Publica o próximo carrossel da fila no Instagram do Dr. Bernardo.

Uso:
  python3 bernardo/publicar.py status     # mostra a fila e quantos faltam (não publica)
  python3 bernardo/publicar.py publicar   # publica o próximo post pendente

Token: variável de ambiente INSTAGRAM_ACCESS_TOKEN (nunca imprimir).
Imagens: JPEG servidos pelo raw.githubusercontent.com do commit atual (precisa estar no GitHub).
Um post conta como publicado quando a 1ª linha da legenda já aparece numa mídia recente da conta,
então a fila não precisa guardar estado e rodar duas vezes não duplica.
"""
import json
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request

API = "https://graph.facebook.com/v21.0"
REPO = "douglasmonteiro907/instagram"
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILA = os.path.join(RAIZ, "bernardo", "fila.json")


def graph(metodo, caminho, **params):
    token = os.environ["INSTAGRAM_ACCESS_TOKEN"]
    dados = urllib.parse.urlencode(params).encode() if metodo == "POST" else None
    url = f"{API}/{caminho}"
    if metodo == "GET" and params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, data=dados, method=metodo,
                                 headers={"Authorization": f"Bearer {token}"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise SystemExit(f"Erro da API em {caminho}: {e.read().decode()[:500]}")


def primeira_linha(texto):
    return next((l.strip() for l in texto.splitlines() if l.strip()), "")


def ja_publicados(conta):
    midias = graph("GET", f"{conta}/media", fields="caption,timestamp,permalink", limit=100)
    return {primeira_linha(m.get("caption", "")): m for m in midias.get("data", [])}


def carregar():
    with open(FILA, encoding="utf-8") as f:
        fila = json.load(f)
    for p in fila["fila"]:
        with open(os.path.join(RAIZ, p["pasta"], "legenda.txt"), encoding="utf-8") as f:
            p["legenda"] = f.read().strip()
    return fila


def pendentes(fila):
    feitos = ja_publicados(fila["conta_instagram_id"])
    return [p for p in fila["fila"] if primeira_linha(p["legenda"]) not in feitos], feitos


def url_imagem(sha, pasta, n):
    return f"https://raw.githubusercontent.com/{REPO}/{sha}/{pasta}/slide_{n:02d}.jpg"


def esperar_pronto(container):
    for _ in range(30):
        st = graph("GET", container, fields="status_code,status").get("status_code")
        if st == "FINISHED":
            return
        if st in ("ERROR", "EXPIRED"):
            raise SystemExit(f"Container {container} falhou: {st}")
        time.sleep(5)
    raise SystemExit(f"Container {container} não ficou pronto a tempo")


def publicar(fila, post):
    conta = fila["conta_instagram_id"]
    sha = subprocess.check_output(["git", "-C", RAIZ, "rev-parse", "HEAD"], text=True).strip()
    for n in range(1, post["slides"] + 1):  # confere se as imagens estão públicas
        try:
            urllib.request.urlopen(urllib.request.Request(url_imagem(sha, post["pasta"], n), method="HEAD"), timeout=30)
        except Exception as e:
            raise SystemExit(f"Imagem não acessível no GitHub ({e}). O commit {sha[:7]} foi enviado?")
    filhos = []
    for n in range(1, post["slides"] + 1):
        r = graph("POST", f"{conta}/media", image_url=url_imagem(sha, post["pasta"], n), is_carousel_item="true")
        filhos.append(r["id"])
    for c in filhos:
        esperar_pronto(c)
    carrossel = graph("POST", f"{conta}/media", media_type="CAROUSEL",
                      children=",".join(filhos), caption=post["legenda"])["id"]
    esperar_pronto(carrossel)
    midia = graph("POST", f"{conta}/media_publish", creation_id=carrossel)["id"]
    link = graph("GET", midia, fields="permalink").get("permalink")
    return midia, link


def main():
    acao = sys.argv[1] if len(sys.argv) > 1 else "status"
    fila = carregar()
    falta, feitos = pendentes(fila)
    if acao == "publicar":
        if not falta:
            print("FILA VAZIA: nada para publicar.")
        else:
            post = falta.pop(0)
            midia, link = publicar(fila, post)
            print(f"PUBLICADO: {post['id']} -> {link} (media {midia})")
    else:
        for p in fila["fila"]:
            m = feitos.get(primeira_linha(p["legenda"]))
            print(f"{'publicado ' + m['timestamp'][:10] if m else 'pendente  '}  {p['id']}")
    print(f"PENDENTES: {len(falta)}")


if __name__ == "__main__":
    main()
