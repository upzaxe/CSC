from pathlib import Path
import re, html

ROOT = Path(__file__).resolve().parent
COMP = ROOT / "components"
PRE = ROOT / "preview"
PRE.mkdir(exist_ok=True)

def part(name):
    return (COMP / (name + ".html")).read_text(encoding="utf-8")

names = [p.stem for p in sorted(COMP.glob("*.html"))]
styles = sorted((ROOT / "css").glob("*.css"))

def page(body, title="CANDLE 2026 | Cendekia Student Challenge", prefix=""):
    links = "\n".join(f'<link rel="stylesheet" href="{prefix}css/{p.name}">' for p in styles)
    scripts = "\n".join(f'<script src="{prefix}js/{name}.js"></script>' for name in ("navigation", "modal"))
    if prefix:
        body = body.replace('src="assets/', 'src="'+prefix+'assets/')
    return f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#e9f6fc"><title>{html.escape(title)}</title>
{links}
</head><body>{body}
{scripts}
</body></html>'''

nav, *sections, footer, modal = names
main = '<a class="skip" href="#about">Lewati navigasi</a>' + part(nav) + '<main>' + ''.join(map(part,sections)) + '</main>' + part(footer) + part(modal)
(ROOT / "index.html").write_text(page(main), encoding="utf-8")

for name in names:
    if name == modal:
        body = '<main class="section"><div class="wrap"><h2>Uji dialog</h2><div class="actions">' + ''.join(f'<button class="btn" data-modal="{i}">{label}</button>' for i,label in [("csc","CSC"),("mac","MAC"),("acr","ACR"),("csc-reg","Daftar CSC"),("mac-reg","Daftar MAC"),("flyer","Flyer")]) + '</div></div></main>' + part(modal)
    elif name == nav:
        body = part(nav) + '<main class="section"><div class="wrap"><p>Preview navigasi. Gunakan index.html untuk mencoba perpindahan antarbagiannya.</p></div></main>' + part(modal)
    else:
        body = part(name) + part(modal)
    (PRE / (name + ".html")).write_text(page(body, "Preview | " + name, "../"), encoding="utf-8")

print("index.html dan semua preview diperbarui.")
