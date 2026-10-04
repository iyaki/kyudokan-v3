# Pendientes — kyudokan-v3

Última actualización: 2026-10-04

## Despliegue en Cloudflare Pages

Ya commiteado: `.nvmrc`, `wrangler.toml`, `src/_headers`, `src/_redirects`, `.eleventy.js` (passthrough) — commit `b8a5204`; más `src/_data/sitio.json`, `src/robots.txt.liquid`, `src/sitemap.xml.liquid` y el JSON-LD de `/contacto/` — commit `10c674f`.

**Garantía de actualización en cada push a `main`:** con la Git integration de Cloudflare Pages, CADA push a la rama de producción (`main`) dispara build y deploy automáticos — no requiere CI ni workflows en el repo. La config ya vive en `wrangler.toml` (build `npm run build`, output `_site`). Un segundo canal de deploy (GitHub Action con wrangler) crearía divergencia: solo agregarlo si no se puede conectar el repo a Cloudflare.

Pasos manuales restantes (dashboard Cloudflare):

1. Workers & Pages → Create → Pages → **Connect to Git** → repo `iyaki/kyudokan-v3`, rama `main`. Confirmar build `npm run build` / output `_site`.
2. Custom domain: agregar `karatekyudokan.com.ar` al proyecto.
3. **Cutover DNS**: cambiar los nameservers en el registrar cuando se decida reemplazar el sitio 2001. Hasta entonces, validar en `kyudokan-v3.pages.dev`.
4. **Quitar el `noindex`** de `src/_includes/base.html` en el mismo push del cutover DNS — hasta entonces los motores no indexan el sitio.

Externo (SEO): dar de alta el dominio en Google Search Console y Bing Webmaster, enviar `https://karatekyudokan.com.ar/sitemap.xml`.

## SEO tradicional — implementado (commit `9990410`)

Hecho: h1 único por página, meta descriptions en las 16, canonical, titles con intención de búsqueda, og:image 1200×630 + bloque og/twitter, 404.html, informe en `docs/seo-geo-aeo.md`.

Pendiente: **enlaces internos desde texto corrido** en el resto de las páginas (solo el index tiene los 2 nuevos; falta Kobudo y primera mención por página, patrón del «Okinawa» en `.nota`).

Externo: **Perfil de Empresa en Google** (categoría «Escuela de artes marciales», las dos sedes, horarios idénticos al sitio, NAP igual al footer).

## GEO / AEO — informe escrito

Informe en `docs/seo-geo-aeo.md` (backlog GEO/AEO vivo ahí: FAQ + schema FAQPage, párrafo-definición, frase-respuesta, E-E-A-T, huella externa, katas como lista, mini-índice).

El **JSON-LD** ya está implementado en `/contacto/` (grafo de 12 nodos: instructores Cristian Lugani y Daniela Soledad Bustos, dos dojos con geo, horarios como Events con `eventSchedule`) — commit `10c674f`. Los datos factuales provienen del propio sitio (tabla completa de horarios, coordenadas de los embeds OSM, sedes por tipo de clase).

## Polish — menores pendientes

- Flourish de tejas del hero centrado bajo el título (hoy huérfano a la izquierda).
- Curso de tejas coronando las bandas seigaiha (token `--curso-teja` ya existe).
- h1 del masthead con tamaño propio en ≤760px (hoy 6 renglones en móvil).
- ~~`loading="lazy"` en below-fold del home~~ — hecho vía transform build-only (`.eleventy/production-tweaks.js`); el fuente no lleva atributo y el build agrega lazy salvo above-fold (`.crest`, `.shisa`).
- Franja de cierre conversional al pie del linaje («¿Te sumás? → Empezá hoy», sistema existente).
- Typeset: `max-width: 65ch` en `.nota` (hoy ~145 chars/línea) + uppercase reservado a labels cortas (`.rol`, `<b>` de figcaption), fuera de descripciones largas.

## Optimizaciones de producción — implementadas (port de iyaki.github.io)

- **`npm run build` = eleventy + `jampack ./_site`** con `jampack.config.js` (medición: 3.35 MB → 2.68 MB, sin issues).
- **`.eleventy/production-tweaks.js`** (build-only, `--serve` intacto): CSS vía postcss-preset-env + cssnano (`gusuku.css` compilado, ya no es passthrough), minify HTML con CSS inline y JS, lazy de imágenes (excluye above-fold), `rel="noopener noreferrer"` en `target="_blank"`, minify XML (sitemap).
- `@swc/core` fijado a `1.11.6` por `overrides` (combo probado de iyaki.github.io; 1.16.x falla con `ERR_SWC_NATIVE_CACHE` en este `.cache`).
- Postinstalls nativos aprobados: `npm install-scripts approve @swc/core esbuild sharp`.
- Observación: 23 `.JPG` (mayúscula, fotos legacy en `assets/`) no las comprime jampack por extensión; ~1 MB sin tocar.

## Contenido pendiente del dueño

- Fotos reales para las cartelas `.falta` (nombran el archivo original esperado).
- Decidir aranceles/cuotas (no se publican hasta dato oficial — regla de fidelidad).
- Logos para el footer: **Campana 30 años** y **Kyudokan 70 años** (¿se incluyen? faltan los archivos).

## Nuevos pendientes (2026-10-04)

- **GoatCounter**: analytics ligero; decidir instancia (SaaS goatcounter.com vs self-host) y el snippet en `base.html`.
- **Google Search Console / Bing Webmaster Tools**: ya anotado en Despliegue (enviar el sitemap en el cutover).
- **Optimizaciones con jampack** (`@divriots/jampack` sobre `_site/` como paso post-build).
- **FAQ** (¿página nueva + schema FAQPage?): temas — Qué, Por qué, Linaje, Kobudo, Aranceles, Servicios (Karate/Kobudo/Japonés/Yoga).
- **Meishi de Cristian en `/contacto/`** (tarjeta/presentación; falta el asset).
