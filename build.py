"""Gera o index.html do site (GitHub Pages) a partir de src/jogos.html.

src/jogos.html é a página do jogo sem <head>; aqui ela ganha o cabeçalho de app instalável
(manifesto, ícones, modo tela cheia) e o registro do service worker para funcionar offline.
Uso: python3 build.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
body = (ROOT / "src" / "jogos.html").read_text(encoding="utf-8")

# Tira do corpo as tags que precisam ir no <head>.
head_bits = []
for pattern in (r"<title>.*?</title>\n?", r"<meta [^>]*>\n?", r"<link [^>]*>\n?", r"<style>.*?</style>\n?"):
    for m in re.findall(pattern, body, flags=re.S):
        if "claude:" in m:
            body = body.replace(m, "", 1)
            continue
        head_bits.append(m.strip())
        body = body.replace(m, "", 1)

head = "\n".join([
    '<meta charset="utf-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, user-scalable=no">',
    '<link rel="manifest" href="manifest.webmanifest">',
    '<link rel="icon" href="icons/icon-192.png" type="image/png">',
    '<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">',
    '<meta name="apple-mobile-web-app-capable" content="yes">',
    '<meta name="mobile-web-app-capable" content="yes">',
    '<meta name="apple-mobile-web-app-title" content="Salão de Jogos">',
    '<meta name="apple-mobile-web-app-status-bar-style" content="default">',
    "<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
    "body{margin:0;font-size:14px}img{max-width:100%}[hidden]{display:none!important}</style>",
    *head_bits,
])

sw = """<script>
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {}));
}
</script>"""

head = head.replace("<title>Busão Lotado</title>", "<title>Salão de Jogos</title>")
html = f"<!doctype html>\n<html lang=\"pt-BR\">\n<head>\n{head}\n</head>\n<body>\n{body.strip()}\n{sw}\n</body>\n</html>\n"
(ROOT / "index.html").write_text(html, encoding="utf-8")
print("index.html gerado")
