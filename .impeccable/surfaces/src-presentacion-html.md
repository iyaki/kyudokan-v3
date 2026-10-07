---
version: 1
slug: "src-presentacion-html"
primary_target: "src/presentacion.html"
related_targets: []
---

# Surface brief — src/presentacion.html (+ CSS acotado en src/gusuku.css)

## Surface
Página interna «Presentación» (/presentacion/): la carta de presentación del dojo — la cadena de transmisión de la escuela en seis retratos con su ficha, y el representante local como cierre. Shell compartido de base.html (masthead, riel, pie); el trabajo es el área de contenido.

## Mode
**Read.** El visitante entiende quién respalda la escuela (Chibana → Yuchoku → Jintatsu → Minoru/Oscar/Benito → Lugani). No persuade con recursos: presenta el registro.

## Dirección
Restaurar la estructura semántica de la fuente 2001 — grilla de cartelas (foto arriba, ficha debajo, apareados) — en el mundo Gusuku: paspartú hueso (`.lamina` reutilizado), hairline, sombra suave, fotos jamás teñidas y sin recorte (object-fit nunca cover: son registro). Etiquetas de rol (FUNDADOR:, JAPÓN:, …) en teja-horno, pequeñas y espaciadas — la jerarquía que en 2001 hacía el subrayado 7pt.

## Contenido y fidelidad
- Texto del cuerpo 2001 verbatim (solo ortografía: «Sudamérica»). `<strong>` de nombres conserva la posición exacta de la fuente por ficha.
- Fotos autogen propias de la página (103–125px de ancho): son el registro; se despliegan acotadas (marco ~206px alto desktop, 2 columnas en mobile ≈ tamaño nativo) para no inflar el upscale.
- Jintatsu enlaza a /biografia_jintatsu_higa/ (como la fuente y la v3 previa); hover/focus de cartela en teja.

## Fuera de alcance
Mundo visual (Gusuku committed), riel, pie, masthead, otras páginas. No se agregan claims, ranks nuevos ni enlaces externos muertos de 2001 (oikko.org, yudokarate.com, translate.google ya estaban descartados).

## Artefactos 2001 eliminados (decisiones)
- Bullets GIF `a_Round_Rectangle*.gif` (15×12px) y sus captions «U»: scaffolding de layout, no contenido.
- Captions/alts «click para abrir ventana»: hints de popups que ya no existen.
- Botón-imagen «Todas las Fotos»: apuntaba a la sección de fotos, gateada por el dueño (2026-09-30); estaba muerto en v3.

## Checks
build limpio + check_links 0 rotos + captura desktop y 390px (imágenes con naturalWidth > 0) + contraste ficha ≥4.5:1 sobre hueso.
