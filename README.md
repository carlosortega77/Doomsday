# DOOMSDAY · Dojo de Cálculo Mental

App web autocontenida para entrenar cálculo mental. Funciona como **PWA**: se puede instalar y usar offline.

## Demo

https://carlosortega77.github.io/Doomsday/

## Instalar en iPhone (offline)

1. Abre la URL en **Safari** (no Chrome).
2. Toca el botón **Compartir** → **"Añadir a pantalla de inicio"**.
3. La primera vez que la abras desde el icono, el service worker cachea todo.
4. Después funciona sin internet. Cuando haya conexión, se auto-actualiza.

## Instalar en escritorio

Chrome / Edge / Brave: en la barra de URL aparece un icono de instalar (⊕) cuando el manifest se detecta.

## Uso local sin servidor

Abre `index.html` en cualquier navegador. Service worker NO se registra desde `file://`, pero el HTML funciona igual offline.

## Stack

- `index.html` — single-file app (HTML + JS embebido)
- `manifest.webmanifest` — metadatos PWA
- `sw.js` — service worker, cache-first
- `icon-{180,192,512}.png` — iconos
- `_gen_icons.py` — script para regenerar iconos (PIL)
