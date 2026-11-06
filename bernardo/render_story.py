import sys, os, base64, html, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_d = importlib.import_module(os.environ.get('STORY_DATA', 'story_data'))  # STORY_DATA=story_data_lote02 para o lote 02
POSTS, REV = _d.POSTS, _d.REV
from playwright.sync_api import sync_playwright
W = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
FOTOS = '/mnt/project-files/bernardo/fotos'
def b64(p, mime): return f"data:{mime};base64," + base64.b64encode(open(p,'rb').read()).decode()
AV = b64(f'{W}/avatar.png','image/png')
F = {k: b64(f'{W}/fonts/{v}','font/ttf') for k,v in {'400':'S6uyw4BMUTPHvxk.ttf','700':'S6u9w4BMUTPHh6UVew8.ttf','900':'S6u9w4BMUTPHh50Xew8.ttf'}.items()}
e = html.escape
CSS = f"""
@font-face{{font-family:Lato;font-weight:400;src:url({F['400']})}}
@font-face{{font-family:Lato;font-weight:700;src:url({F['700']})}}
@font-face{{font-family:Lato;font-weight:900;src:url({F['900']})}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;font-family:Lato,'Noto Color Emoji',sans-serif;color:#fff;overflow:hidden}}
.page{{width:1080px;height:1350px;position:relative;overflow:hidden}}
.dark{{background:radial-gradient(circle at 85% 10%,#22262c 0,#151618 45%,#101112 100%)}}
.navy{{background:linear-gradient(160deg,#0d2347 0%,#0b1b36 55%,#081428 100%)}}
.hi{{color:#1EB6F2}}
.badge{{display:flex;align-items:center;gap:18px}}
.badge img{{width:84px;height:84px;border-radius:50%;border:3px solid #cfd6de}}
.badge .n{{font-weight:700;font-size:28px;line-height:1.15}} .badge .u{{font-size:23px;color:#aab3bd}}
.swipe{{font-size:24px;letter-spacing:1px;color:#e6e9ec;font-weight:700}}
.swipe:after{{content:' ⊙';color:#9aa3ad;font-weight:400}}
/* cover */
.cover img.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.cover .shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,12,20,.05) 0%,rgba(8,12,20,.15) 35%,rgba(8,12,20,.88) 62%,rgba(8,12,20,.97) 100%)}}
.cover .top{{position:absolute;left:70px;top:64px;text-shadow:0 2px 10px rgba(0,0,0,.85)}} .cover .top .u{{color:#e8edf2}}
.cover .bottom{{position:absolute;left:70px;right:70px;bottom:90px}}
.pills{{display:flex;gap:14px;margin-bottom:26px}}
.pill{{font-size:22px;font-weight:700;padding:8px 18px;border-radius:30px}}
.pill.a{{background:#1EB6F2;color:#fff}} .pill.b{{background:#fff;color:#0b1b36}}
.cover h1{{font-size:78px;line-height:1.08;font-weight:900;letter-spacing:-.5px;margin-bottom:22px}}
.cover .sub{{font-size:40px;font-style:italic;color:#dfe5ea;margin:-6px 0 26px}}
/* card */
.cardwrap{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center}}
.card{{width:930px;background:linear-gradient(180deg,#26282c,#1c1d20);border:2px solid #3a3d42;border-radius:44px;padding:64px 62px 56px;position:relative;box-shadow:0 0 0 1px #000}}
.card:before,.card:after{{content:'';position:absolute;left:22%;right:22%;height:5px;border-radius:5px;background:#1EB6F2;box-shadow:0 0 28px 8px rgba(30,182,242,.55)}}
.card:before{{top:-3px}} .card:after{{bottom:-3px}}
.card .badge{{margin-bottom:40px}}
.card .pre{{font-size:44px;line-height:1.3;color:#f2f4f6;margin-bottom:12px}}
.card .big{{font-size:66px;line-height:1.12;font-weight:900;color:#1EB6F2;letter-spacing:-.3px}}
.card .post{{font-size:44px;line-height:1.3;color:#f2f4f6;margin-top:14px}}
.card .foot{{font-size:22px;color:#8e979f;margin-top:26px;font-style:italic}}
.card .swipe{{margin-top:40px}}
.card .ititle{{font-size:68px;font-weight:900;color:#1EB6F2;line-height:1.1;margin-bottom:22px}}
.card .ibody{{font-size:46px;line-height:1.3;color:#f2f4f6}}
/* review */
.rv{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:0 70px}}
.rv .lbl{{font-size:34px;font-weight:700;color:#cfe9f7;margin-bottom:34px;letter-spacing:.5px}}
.rcard{{background:#fff;color:#1d2125;border-radius:40px;padding:56px 56px 52px;width:100%}}
.rhead{{display:flex;align-items:center;gap:20px;margin-bottom:12px;flex-wrap:wrap}}
.ini{{width:78px;height:78px;border-radius:50%;background:#f7c6d9;color:#fff;font-size:38px;font-weight:700;display:flex;align-items:center;justify-content:center}}
.rname{{font-size:36px;font-weight:700}}
.ver{{font-size:20px;font-weight:900;color:#0f8a5f;background:#d9f6e9;padding:7px 14px;border-radius:8px;letter-spacing:.5px}}
.stars{{color:#f5b301;font-size:40px;letter-spacing:4px;margin:14px 0 6px}}
.rmeta{{font-size:24px;color:#6d757d;margin-bottom:24px}}
.rtext{{font-size:39px;line-height:1.38}}
.rv .src{{font-size:22px;color:#9fb3c8;margin-top:28px}}
.rv .swipe{{margin-top:36px}}
/* cta */
.cta{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 90px}}
.cta .badge{{margin-bottom:46px}}
.cta .q{{font-size:38px;color:#aab3bd;margin-bottom:20px;font-weight:700}}
.cta .main{{font-size:78px;line-height:1.12;font-weight:900}}
.cta .swipe{{margin-top:44px}}
.cta .swipe:after{{content:' ⊙'}}
"""
def badge(): return f'<div class="badge"><img src="{AV}"><div><div class="n">Dr. Bernardo Mercante</div><div class="u">@drbernardomercante</div></div></div>'
def slide_html(post, s):
    t = s['t']
    if t == 'cover':
        ph = b64(f"{FOTOS}/{post['photo']}", 'image/jpeg')
        title = e(s.get('pre','')) + f'<span class="hi">{e(s["hi"])}</span>' + e(s.get('post',''))
        sub = f'<div class="sub">{e(s["sub"])}</div>' if s.get('sub') else ''
        body = f'''<div class="page cover"><img class="bg" src="{ph}" style="object-position:{post['pos']}"><div class="shade"></div>
<div class="top">{badge()}</div>
<div class="bottom"><div class="pills"><span class="pill a">CRM: 83593-5</span><span class="pill b">RQE: 296734</span></div>
<h1>{title}</h1>{sub}<div class="swipe">ARRASTA PARA O LADO</div></div></div>'''
    elif t in ('card','item'):
        if t == 'card':
            inner = (f'<div class="pre">{e(s["pre"])}</div>' if s.get('pre') else '') + f'<div class="big">{e(s["hi"])}</div>' + (f'<div class="post">{e(s["post"])}</div>' if s.get('post') else '') + (f'<div class="foot">{e(s["foot"])}</div>' if s.get('foot') else '')
        else:
            inner = f'<div class="ititle">👉 {e(s["title"])}</div><div class="ibody">{e(s["body"])}</div>'
        body = f'<div class="page dark"><div class="cardwrap"><div class="card">{badge()}{inner}<div class="swipe">ARRASTA PARA O LADO</div></div></div></div>'
    elif t == 'review':
        r = REV[s['r']]
        body = f'''<div class="page navy"><div class="rv"><div class="lbl">O que os pacientes dizem</div><div class="rcard">
<div class="rhead"><div class="ini">{e(r["ini"][0])}</div><div class="rname">{e(r["ini"])}</div><div class="ver">CONSULTA VERIFICADA ✓</div></div>
<div class="stars">★★★★★</div><div class="rmeta">{e(r["date"])} · {e(r["local"])}</div>
<div class="rtext">{e(r["text"])}</div></div><div class="src">Avaliação real publicada no Doctoralia</div><div class="swipe">ARRASTA PARA O LADO</div></div></div>'''
    elif t == 'cta':
        body = f'<div class="page dark"><div class="cta">{badge()}<div class="q">{e(s["q"])}</div><div class="main"><span class="hi">{e(s["hi"])}</span>{e(s["post"])}</div><div class="swipe">LEIA A LEGENDA</div></div></div>'
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'
only = sys.argv[2] if len(sys.argv)>2 else None
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    pg = b.new_page(viewport={'width':1080,'height':1350})
    for post in POSTS:
        if only and post['id']!=only: continue
        d = os.path.join(OUT, post['id']); os.makedirs(d, exist_ok=True)
        for i, s in enumerate(post['slides'], 1):
            pg.set_content(slide_html(post, s)); pg.wait_for_timeout(150)
            pg.screenshot(path=os.path.join(d, f'slide_{i:02d}.png'))
        open(os.path.join(d,'legenda.txt'),'w').write(post['caption'].strip()+'\n')
        print(post['id'], len(post['slides']))
    b.close()
