// Estrategia: stale-while-revalidate.
// Sirve cache instantáneo y, en paralelo, actualiza la cache desde red.
// La siguiente visita ya recibe el contenido fresco — sin tocar este archivo
// cuando cambia el contenido del sitio.
const CACHE = 'doomsday-v3';
const ASSETS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icon-180.png',
  './icon-192.png',
  './icon-512.png',
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') return;
  e.respondWith(
    caches.open(CACHE).then((cache) =>
      cache.match(e.request).then((cached) => {
        const networkFetch = fetch(e.request)
          .then((res) => {
            if (res && res.status === 200 && res.type === 'basic') {
              cache.put(e.request, res.clone());
            }
            return res;
          })
          .catch(() => cached);
        // waitUntil extiende la vida del SW hasta que termine la revalidación
        // en background, aunque ya hayamos respondido con la versión cacheada.
        if (cached) {
          e.waitUntil(networkFetch);
          return cached;
        }
        return networkFetch;
      })
    )
  );
});
