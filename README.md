# Salão de Jogos

Joguinhos para celular (Android e iPhone) que funcionam no navegador e podem ser instalados como app.

- **Busão Lotado**: tire os ônibus do estacionamento e leve cada passageiro no ônibus da sua cor.
- **Blocos de Madeira**: arraste as peças para o tabuleiro e complete linhas e colunas.
- **Chuva de Blocos**: gire e encaixe as peças que caem (no estilo Tetris).
- **Bombinha**: bombas, tijolos e monstrinhos num labirinto (no estilo Bomberman).
- **Cruzadinha**: palavras cruzadas em português, com dicas, teclado na tela e níveis que vão crescendo.

## Como instalar no celular

Abra https://sidneitrancoso.github.io/jogos/ e:

- **iPhone (Safari):** botão de compartilhar → "Adicionar à Tela de Início".
- **Android (Chrome):** menu ⋮ → "Instalar app" ou "Adicionar à tela inicial".

## Como o código está organizado

- `src/jogos.html`: todos os jogos (HTML, CSS e JavaScript num arquivo só).
- `build.py`: gera o `index.html` do site a partir de `src/jogos.html` (`python3 build.py`).
- `manifest.webmanifest`, `sw.js`, `icons/`: o que faz o site virar app instalável e funcionar sem internet.
  Ao publicar uma versão nova, aumente o número em `CACHE` no `sw.js`.
