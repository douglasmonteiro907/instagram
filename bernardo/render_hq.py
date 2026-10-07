# Monta as HQs (layout v2) em PNG 1080x1350 a partir das ilustrações originais do Canva.
# Uso: python3 render_hq.py <pasta_artes> <pasta_saida> [HQ01 ...]
# <pasta_artes>/<slot>_s<n>.(jpg|png) = ilustração do slide n (sem texto). Textos e cores vêm de hq_data_v2.py.
import sys, os, base64, html, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hq_data_v2 import HQS
from playwright.sync_api import sync_playwright

W = os.path.dirname(os.path.abspath(__file__))
ARTES, OUT = sys.argv[1], sys.argv[2]
SO = set(sys.argv[3:])
e = html.escape
def b64(p):
    mime = 'image/png' if p.endswith('.png') else 'image/jpeg' if p.endswith(('.jpg', '.jpeg')) else 'font/ttf'
    return f"data:{mime};base64," + base64.b64encode(open(p, 'rb').read()).decode()
FONTE = b64('/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf')  # métrica do Arial Bold, como no Canva

CSS = f"""
@font-face{{font-family:LatoBlack;src:url({FONTE})}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;font-family:LatoBlack,sans-serif}}
.page{{width:1080px;height:1350px;position:relative;overflow:hidden}}
.quadro{{position:absolute;left:112px;top:277px;width:856px;height:1066px}}
.arte{{position:absolute;left:120px;top:285px;width:840px;height:1050px;object-fit:cover}}
.balao{{position:absolute;top:22px;background:#fff;border:5px solid #111;border-radius:44px;
  display:flex;align-items:center;justify-content:center;text-align:center;color:#111;
  padding:30px 44px;line-height:1.2;text-transform:uppercase}}
.rabo{{position:absolute;width:0;height:0}}
.tarja{{position:absolute;left:120px;top:1160px;width:840px;height:175px;display:flex;flex-direction:column;
  align-items:center;justify-content:center;text-align:center}}
.tarja .c{{font-size:68px;line-height:1}} .tarja .a{{font-size:30px;color:#fff;margin-top:14px}}
"""

def balao(texto, left, width, fs, rabo_x):
    # altura cresce com o texto; o rabicho fica preso na borda de baixo via JS
    return (f'<div class="balao" data-rabo="{rabo_x}" style="left:{left}px;width:{width}px;font-size:{fs}px;padding:{30 if width < 600 else 26}px {30 if width < 600 else 40}px">{e(texto)}</div>')

def pagina(hq, n, arte):
    p = hq['paleta']
    corpo = [f'<div class="quadro" style="background:{p["quadro"]}"></div>', f'<img class="arte" src="{b64(arte)}">']
    if n == 1:
        corpo.append(balao(hq['capa'], 31, 1018, 52, 495))
    elif n in (2, 3, 4):
        pac, doc = hq['dialogo'][n - 2]
        corpo.append(balao(pac, 31, 500, 46 if len(pac) < 40 else 38, 350))
        corpo.append(balao(doc, 549, 500, 30 if len(doc) < 110 else 27, 720))
    else:
        corpo.append(balao(hq['cta'], 31, 1018, 50, 623).replace('padding:26px 40px', 'padding:26px 150px'))
        corpo.append(f'<div class="tarja" style="background:{p["tarja"]}"><div class="c" style="color:{p["palavra"]}">'
                     f'COMENTE "{hq["tema"]}"</div><div class="a">AQUI EMBAIXO</div></div>')
    js = """<script>
for (const b of document.querySelectorAll('.balao')) {
  // reduz a fonte até caber acima do quadro; o rabicho desce da borda do balão até o quadro
  let fs = parseFloat(b.style.fontSize);
  while (b.offsetHeight > 290 && fs > 18) { fs -= 1; b.style.fontSize = fs + 'px'; }
  const y0 = b.offsetTop + b.offsetHeight - 6, x = +b.dataset.rabo, h = Math.max(30, 292 - y0), w = Math.min(64, Math.max(40, h * 0.7));
  b.insertAdjacentHTML('afterend', `<svg style="position:absolute;left:${x - w/2}px;top:${y0}px" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">
    <path d="M2.5 0 L${w/2} ${h-3} L${w-2.5} 0" fill="#fff" stroke="#111" stroke-width="5" stroke-linejoin="round"/>
    <rect x="5" y="0" width="${w-10}" height="6" fill="#fff"/></svg>`);
}
</script>"""
    return f'<html><head><style>{CSS}</style></head><body><div class="page" style="background:{p["fundo"]}">{"".join(corpo)}</div>{js}</body></html>'

with sync_playwright() as pw:
    br = pw.chromium.launch(executable_path='/opt/pw-browsers/chromium') if os.path.exists('/opt/pw-browsers/chromium') else pw.chromium.launch()
    pg = br.new_page(viewport={'width': 1080, 'height': 1350})
    for hq in HQS:
        if SO and hq['slot'] not in SO:
            continue
        d = os.path.join(OUT, hq['id']); os.makedirs(d, exist_ok=True)
        for n in range(1, 6):
            arte = (glob.glob(f'{ARTES}/{hq["slot"]}_s{n}.*') or [None])[0]
            if not arte:
                print('sem arte:', hq['slot'], n); continue
            pg.set_content(pagina(hq, n, arte)); pg.wait_for_timeout(150)
            pg.screenshot(path=f'{d}/slide_{n:02d}.png')
        print(hq['id'])
    br.close()
