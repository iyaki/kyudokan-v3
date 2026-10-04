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

## SEO tradicional — por implementar

1. **h1 único por página**: el masthead baja de h1 a `p.razon-social` (mismos estilos) y `pagina-titulo`/`display` pasan a h1 (16 páginas + base.html).
2. **Meta descriptions** en las 15 páginas que no la tienen (solo index la tiene).
3. **Canonical**: `<link rel="canonical" href="{{ sitio.url }}{{ page.url }}">` en `base.html`.
4. **Titles con intención de búsqueda** (ej: contacto «Visitanos» → «Clases de karate en Campana | Horarios y sedes»).
5. **og:image 1200×630** propio (composición SVG→Inkscape: fondo encalado, wordmark, crest) + bloque og/twitter completo en `base.html` con `og:locale es_AR`.
6. **404.html** con permalink `/404.html`, estilo Gusuku, links al riel.
7. **Enlaces internos desde texto corrido** (patrón del «Okinawa» en `.nota`): Kobudo, escuela/estilo en primera mención por página.

Externo: **Perfil de Empresa en Google** (categoría «Escuela de artes marciales», las dos sedes, horarios idénticos al sitio, NAP igual al footer).

## GEO / AEO — informe pendiente

Redactar `docs/geo-aeo.md` con las recomendaciones: párrafo-definición de apertura en home, FAQ local + schema FAQPage, E-E-A-T nominal (schema Person), huella externa consistente (Wikidata, blog), comparación de estilos estructurada, frase-respuesta antes de la tabla de horarios, párrafos-respuesta en páginas temáticas, katas como lista HTML, mini-índice en páginas largas.

El **JSON-LD** ya está implementado en `/contacto/` (grafo de 12 nodos: instructores Cristian Lugani y Daniela Soledad Bustos, dos dojos con geo, horarios como Events con `eventSchedule`) — commit `10c674f`. Los datos factuales provienen del propio sitio (tabla completa de horarios, coordenadas de los embeds OSM, sedes por tipo de clase).

## Polish — menores pendientes

- Flourish de tejas del hero centrado bajo el título (hoy huérfano a la izquierda).
- Curso de tejas coronando las bandas seigaiha (token `--curso-teja` ya existe).
- h1 del masthead con tamaño propio en ≤760px (hoy 6 renglones en móvil).
- `loading="lazy"` en below-fold del home (caligrafía + 4 retratos del linaje).
- Franja de cierre conversional al pie del linaje («¿Te sumás? → Empezá hoy», sistema existente).
- Typeset: `max-width: 65ch` en `.nota` (hoy ~145 chars/línea) + uppercase reservado a labels cortas (`.rol`, `<b>` de figcaption), fuera de descripciones largas.

## Contenido pendiente del dueño

- Fotos reales para las cartelas `.falta` (nombran el archivo original esperado).
- Decidir aranceles/cuotas (no se publican hasta dato oficial — regla de fidelidad).
