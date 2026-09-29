---
name: Kyudokan Campana — La Muestra
description: La home como galería de museo blanca — una muestra histórica del linaje Kyudokan donde las fotos de época cuelgan chicas, con paspartú y marco, y el blanco carga la escala.
colors:
  papel: "#FDFCFA"
  papel-2: "#F4F2EE"
  tinta: "#141311"
  tinta-2: "#57534B"
  hairline: "rgba(20,19,17,.16)"
  rojo: "#C8331F"
  rojo-hondo: "#9A2415"
typography:
  display:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(38px, 4.8vw, 64px)"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.025em"
  sala-h2:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(30px, 4.4vw, 54px)"
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.02em"
  wall-text:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(17px, 1.6vw, 20px)"
    fontWeight: 400
    lineHeight: 1.7
  caption:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.6
  nav:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "12.5px"
    fontWeight: 500
    letterSpacing: "0.08em"
    textTransform: "uppercase"
  scale: [11.5, 12, 12.5, 13, 14, 14.5, 15, 15.5, 16, 17, "clamp(17, 2vw, 21)", 19, "clamp(17, 1.6vw, 20)", "clamp(19, 2.2vw, 25)", "clamp(30, 4.4vw, 54)", "clamp(38, 4.8vw, 64)", "clamp(40, 6.4vw, 88)"]
  dateline:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 500
  dojo-direccion:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "15.5px"
    fontWeight: 400
  obra-nombre:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 600
  num-badge:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 800
  horarios:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "14.5px"
    fontWeight: 400
  cita:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "16.5px"
    fontWeight: 400
  subtitulo:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(19px, 2.2vw, 25px)"
    fontWeight: 400
  indice-item:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(17px, 2vw, 21px)"
    fontWeight: 600
  sala-final-h2:
    fontFamily: "Archivo, system-ui, sans-serif"
    fontSize: "clamp(40px, 6.4vw, 88px)"
    fontWeight: 800
    letterSpacing: "-0.025em"
rounded:
  cta: "6px"
  obra: "0"
  num-badge: "50%"
spacing:
  sala-y: "clamp(70px, 10vh, 120px)"
  obra-mat: "14px"
components:
  cta:
    backgroundColor: "{colors.rojo}"
    textColor: "{colors.papel}"
    fontWeight: 600
    fontSize: "17px"
    rounded: "{rounded.cta}"
    padding: "15px 30px"
  num-badge:
    backgroundColor: "transparent"
    textColor: "{colors.tinta-2}"
    fontWeight: 800
    fontSize: "15px"
    border: "1px solid {colors.hairline}"
    size: "40px"
---

# Design System: Kyudokan Campana — La Muestra

## Overview

**Creative North Star: "La Muestra" — la home como galería de exhibición histórica.**

La página NO ilustra el linaje: lo cuelga. La home es una muestra de museo — salas numeradas en romanos (I–V), obras de época matadas en blanco, textos de pared, y un índice de recorrido al archivo. La restricción que fundó el mundo: las fotos del archivo son diminutas en su resolución nativa (~120–460px). En lugar de agrandarlas y destruir su autoridad, la escala la carga el blanco y la tipografía: las fotos cuelgan chicas, con paspartú blanco de 14px y marco, exactamente como en una muestra histórica real. La acción es única y roja — el botón «Sumate al dojo» (WhatsApp) — el único calor de toda la sala.

El mundo rehúsa explícitamente: la estética gym-fitness, el misticismo zen de bazar, las stock photos y el afiche de película. La autoridad no se declara: se demuestra con fechas exactas (1938, 1940), retratos reales del archivo jamás teñidos, y datos legados marcados «sitio 2001».

**Key Characteristics:**
- Estructura de exposición real: título de muestra → salas I–IV → recorrido del archivo → sala final.
- El blanco y la tipografía cargan la escala; las fotos cuelgan pequeñas y matadas, nunca agrandadas.
- Un único acento en todo el sistema: rojo #C8331F, solo en la acción.
- Hairlines (tinta al 16%) como único recurso de separación: sin grises plenos, sin sombras de bloque.
- Una sola animación: la entrada discreta de las obras, degradable sin JS y con `prefers-reduced-motion`, con failsafe de 3s.

## Colors

Paleta de sala blanca: pared, tinta de cartel, y un solo acento de acción. Nada más.

### Primary
- **Rojo** (`#C8331F`): único acento. Exclusivo de la acción y sus ecos: CTA, hover de nav/enlaces, focus ring, selección de texto. Hover del CTA: `#9A2415`. Nunca decorativo.

### Neutral
- **Papel** (`#FDFCFA`): pared de la sala (fondo de página) y texto sobre rojo.
- **Papel 2** (`#F4F2EE`): fondo secundario (track de scrollbar, fondo detrás de imágenes mientras cargan).
- **Tinta** (`#141311`): texto primario, titulares.
- **Tinta 2** (`#57534B`): texto secundario, epígrafes, nav, captions.
- **Hairline** (`rgba(20,19,17,.16)`): todas las líneas — bordes de topbar, salas, obras, filas de tabla, índice. La única "escala tonal" del sistema.

### Named Rules
**The One Accent Rule.** El rojo aparece solo donde se puede actuar. Si algo es rojo, lleva a algún lado.
**The Untinted Photo Rule.** Las fotos del archivo se muestran con `filter: grayscale(.12) contrast(1.03)`. Jamás se teñiden, nunca duotono, nunca overlay de color.

## Typography

**Única familia: Archivo** (Google Fonts, pesos 400/500/600/800, fallback system-ui). Sin display serif ni mono: la voz es la cartela de museo, no el cartel.

**Character:** la escala tipográfica reemplaza a la fotográfica. Los titulares son enormes y apretados (tracking negativo); los epígrafes de obra, discretos a 13px. El contraste entre ambos ES el recorrido.

### Hierarchy
- **Título de muestra / H1** (800, `clamp(38px, 6.2vw, 84px)`, line-height 1.02, `-.025em`, máx 18ch, `text-wrap: balance`): solo la frase de apertura.
- **Sala H2** (800, `clamp(30px, 4.4vw, 54px)`, `-.02em`): título de cada sala, junto al numeral romano.
- **Sala final** (800, `clamp(40px, 6.4vw, 88px)`, line-height 1, `-.025em`, máx 14ch): declaración de cierre.
- **Texto de pared** (400, `clamp(17px, 1.6vw, 20px)`, line-height 1.7, máx 52ch): la prosa curada de cada sala.
- **Caption de obra** (13px, tinta 2; el nombre en 15px/600 tinta): la cartela bajo cada foto.
- **Nav / fecha de muestra** (12.5–14px, 500, mayúsculas, tracking amplio).

### Named Rules
**The Dated Source Rule.** Cada dato legado lleva su fuente a la vista: «2º Dan (dato del sitio 2001)», «Horarios (sitio 2001 — confirmar por WhatsApp)». Nunca se actualiza por conjetura.

## Layout

Mobile-first, columna única de lectura de galería con máximos de 1200px.

- **Topbar**: wordmark «KYUDOKAN CAMPANA» (800, 16px, tracking .12em) + nav mayúscula 12.5px; borde inferior hairline.
- **Título de muestra**: generoso margen vertical (`clamp(90px,14vh,180px)` arriba) — como entrar a la sala.
- **Salas**: borde superior hairline, padding `clamp(70px,10vh,120px)`, cabecera con numeral romano en badge circular de 40px + H2.
- **Cuerpo de sala**: grid `auto 1fr` (obra a la izquierda, texto de pared a la derecha); colapsa a 1 columna <760px.
- **Salón de la familia**: tres obras colgadas en fila (`flex`, alineadas por base, como cuadros a distinta altura de marco).
- **Recorrido**: índice numerado con reglas horizontales hairline, máx 760px.
- Fluido de 360 a 1600px; `clamp()` en toda la tipografía, `min()` en anchos de obra.

## Elevation & Depth

Depth de papel sobre pared, mínimo y físico. Sombras solo en las obras.

- **Obra** (`0 14px 30px rgba(20,19,17,.10), 0 2px 6px rgba(20,19,17,.06)`): marco colgado con doble sombra — caída suave + contacto cercano.
- **CTA** (`0 2px 4px rgba(20,19,17,.18), 0 10px 24px rgba(154,36,21,.22)`): sombra teñida de rojo; al `:active` se reduce a contacto (`0 1px 2px`) y el botón baja 1px.
- Todo lo demás es plano: hairlines, no sombras.

### Named Rules
**The Pressed Button Rule.** El CTA responde como un botón físico: hover levanta 1px, `:active` baja y aprieta su sombra.

## Shapes

Bordes rectos de 1px hairline en toda superficie (obras, tabla, índice). Solo dos excepciones: el CTA (6px, para leerse como botón) y el badge del numeral (círculo de 50%). Las obras NO tienen border-radius: son marcos.

## Components

### CTA (único componente de acción)
`<a>` rojo pleno, 17px/600, `padding: 15px 30px`, radius 6px, flecha decorativa (`aria-hidden`). Hover: fondo `#9A2415` + 1px arriba. Active: baja 1px, sombra de contacto. Siempre `<a>` real, nunca div-botón.

### Sala (estructura)
`section.sala` con borde superior hairline. Cabecera: badge circular de 40px con numeral romano (800, 15px, tinta 2) + H2 display. Cuerpo: grid obra/texto.

### Obra (componente central)
`figure.obra`: fondo blanco, borde 1px hairline, paspartú de 14px (12px abajo), doble sombra de marco. La imagen dentro lleva `grayscale(.12) contrast(1.03)` y `width` al tamaño nativo (~200–460px) — nunca escalada más allá. Caption: nombre fuerte 15px/600 + datos 13px tinta 2.

### Texto de pared
`.texto-pared`: máx 52ch, `clamp(17px,1.6vw,20px)`, line-height 1.7. La voz curatorial de cada sala.

### Horarios (tabla)
`table.horarios`: máx 380px, 14.5px, `tabular-nums`; caption superior mayúscula con nota «sitio 2001 — confirmar por WhatsApp»; filas separadas por hairline, sin bordes verticales, sin última regla.

### Índice de recorrido
`ol.indice`: lista numerada del archivo, reglas horizontales hairline (arriba y abajo de la lista). Cada ítem: `<a>` flex con título 600 (`clamp(17px,2vw,21px)`) + años en `small` tabular. Hover: el ítem corre 14px a la derecha, pasa a rojo y aparece una flecha `→` alineada a la derecha. Transición 180ms.

### Topbar
Wordmark 800/16px tracking .12em mayúsculas; nav 12.5px/500 mayúsculas tinta 2, hover a rojo. Borde inferior hairline.

## Motion

Una sola animación en todo el mundo: **la entrada de las obras**.

- Solo si `prefers-reduced-motion: no-preference` Y JS activo: las obras arrancan en `.pre` (`opacity: .001; translateY(14px)`) y transicionan a visibles en 700ms `cubic-bezier(.16,1,.3,1)`.
- Un IntersectionObserver (threshold .1) revela cada obra al entrar; al salir de vista se desregistra.
- Failsafe de 3s (`setTimeout`) remueve `.pre` de todas: nada queda oculto, pase lo que pase.
- Sin JS: cero `.pre`, todo visible. La animación se añade encima, nunca es requisito.
- El resto del mundo es estático: las transiciones son solo estados de hover/active (180ms ease).

## Do's and Don'ts

### Do:
- **Do** usar el rojo (`#C8331F`) solo en acciones: CTA, hover de enlace, focus ring (`outline: 2px solid; outline-offset: 3px`), selección.
- **Do** colgar toda foto de época en `.obra`: fondo blanco, paspartú 14px, borde hairline, doble sombra, caption de cartela.
- **Do** mostrar las fotos a su escala nativa o menor: la escala la cargan el blanco y la tipografía.
- **Do** separar con hairlines; usar `tabular-nums` en años y horarios; marcar datos heredados «sitio 2001».
- **Do** mantener la animación de obras degradable: sin JS y con `prefers-reduced-motion`, todo visible.

### Don't:
- **Don't** introducir un segundo acento, gradiente de color o duotono sobre fotos.
- **Don't** agrandar las fotos del archivo más allá de su resolución nativa, ni teñirlas.
- **Don't** añadir sombras fuera del vocabulario obra/CTA, ni grises plenos en lugar de hairlines.
- **Don't** inventar grados, roles o fechas fuera de las fuentes del legado.
- **Don't** recurrir a estética gym-fitness, zen de bazar, stock photos o afiche de película.
