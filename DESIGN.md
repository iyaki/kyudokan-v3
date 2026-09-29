---
name: Kyudokan Campana — La Línea
description: El sitio como página de notación de karate — papel, tinta y la línea del embusen que no se corta.
colors:
  papel: "#F5F1E8"
  papel-2: "#EDE7D8"
  lamina-papel: "#FCFAF4"
  tinta: "#1B1712"
  tinta-2: "#5D5546"
  linea: "#2E4D6B"
  sello: "#B33A26"
  cta-arrow: "#E8B4A8"
  hairline: "rgba(27, 23, 18, .18)"
  hairline-fuerte: "rgba(27, 23, 18, .42)"
  linea-suave: "rgba(46, 77, 107, .38)"
typography:
  display:
    fontFamily: "'Shippori Mincho', 'Times New Roman', serif"
    fontSize: "clamp(2rem, 1.2rem + 2.6vw, 3.1rem)"
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-.01em"
  display-hero:
    fontFamily: "'Shippori Mincho', 'Times New Roman', serif"
    fontSize: "clamp(2.5rem, 1.4rem + 3.6vw, 4.4rem)"
    fontWeight: 600
    lineHeight: 1.15
  headline:
    fontFamily: "'Shippori Mincho', 'Times New Roman', serif"
    fontSize: "clamp(1.5rem, 1.1rem + 1.4vw, 2.2rem)"
    fontWeight: 600
    lineHeight: 1.2
  body:
    fontFamily: "'Zen Kaku Gothic New', system-ui, sans-serif"
    fontSize: "16.5px"
    fontWeight: 400
    lineHeight: 1.7
  label:
    fontFamily: "'Zen Kaku Gothic New', system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 700
    letterSpacing: ".09em"
rounded:
  sm: "2px"
  md: "3px"
  pill: "50%"
spacing:
  bloque: "clamp(44px, 7vw, 96px) clamp(22px, 5vw, 72px)"
  pagina: "clamp(30px, 5vw, 68px) clamp(22px, 5vw, 72px) clamp(48px, 6vw, 88px)"
  riel-ancho: "218px"
components:
  cta-primary:
    backgroundColor: "{colors.linea}"
    textColor: "{colors.papel}"
    rounded: "{rounded.md}"
    padding: "15px 26px 15px 20px"
    typography: "{typography.body}"
  cta-primary-hover:
    backgroundColor: "{colors.tinta}"
    textColor: "{colors.papel}"
  sello-fecha:
    backgroundColor: "transparent"
    textColor: "{colors.sello}"
    rounded: "{rounded.md}"
    padding: "7px 11px"
  falta:
    backgroundColor: "transparent"
    textColor: "{colors.tinta-2}"
    padding: "22px 24px"
  lamina:
    backgroundColor: "{colors.lamina-papel}"
    textColor: "{colors.tinta-2}"
    padding: "10px 10px 0"
  estacion:
    backgroundColor: "transparent"
    textColor: "{colors.tinta-2}"
    padding: "7px 0 7px 26px"
---

# Design System: Kyudokan Campana — La Línea

## Overview

**Creative North Star: "La página de notación del dojo"**

Una escuela de karate es una línea que no se corta; el diagrama de esa línea es el embusen. Todo el sitio se comporta como la página de un libro de karate que notación dibuja cada forma: trazos, huellas, puntos de kiai, numerales de figura. Papel cálido, tinta económica, un solo trazo índigo que cruza la portada y se convierte en riel de navegación para las ~116 páginas del archivo. El material de 2001 se rotula como tal — nunca se moderniza ni se disimula.

La densidad es editorial, no de producto: títulos mincho a escala pared, cuerpos a 68ch, fotos montadas como láminas numeradas (`Fig. N`) y tablas de horarios con reglas de tinta en lugar de tarjetas. El movimiento es mínimo y diegético: la línea se traza sola al cargar y las láminas aparecen; nada más se anima.

**Key Characteristics:**
- Papel cálido + tinta sepia + un único acento índigo (ai-iro) para línea e interacción.
- Rojo sello exclusivamente funcional: inicio de kata, kiai, fechas, estación activa.
- Nav global = riel lateral de estaciones sobre una línea dibujada; una sola estación saturada por página.
- Ausencia honesta: foto faltante = tramo punteado rotulado (`.falta`), jamás relleno.
- Grilla keyline fija que no se mueve entre páginas; footer sitemap de tres columnas.

## Colors

Paleta de cuatro roles: papel, tinta, línea y sello. La característica es la contención — casi todo es papel y tinta; el índigo guía, el rojo marca.

### Primary
- **Línea índigo / ai-iro** (`#2E4D6B`): el color de la línea misma — embusen, riel de navegación, hover de enlaces, CTA, foco visible, selección de texto. Interacción = trazo.

### Secondary
- **Sello rojo** (`#B33A26`): SOLO marca funcional — punto de inicio del kata, marcas de kiai, sello de fecha «sitio 2001», año del linaje, punto de la estación activa. Jamás decorativo, nunca en fondos grandes.

### Neutral
- **Papel** (`#F5F1E8`): fondo de página y riel.
- **Papel 2** (`#EDE7D8`): fondo alterno (track de scrollbar, chips de código en `.falta`).
- **Papel de lámina** (`#FCFAF4`): pase de foto, más claro que la página, como montaje de archivo.
- **Tinta** (`#1B1712`): texto principal, reglas fuertes de tablas, hover de CTA.
- **Tinta 2** (`#5D5546`): texto secundario, pies de figura, etiquetas.
- **Hairlines** (`rgba(27,23,18,.18)` y `.42`): todas las fronteras; la fuerte para bordes punteados y marcadores.
- **Línea suave** (`rgba(46,77,107,.38)`): tramo de línea de fondo (riel, índice, linaje) bajo la estación activa.

### Named Rules
**La Regla del Punto Encendido.** Un solo elemento saturado por página: la estación activa del riel (punto rojo + tinta bold) — o en el home, la CTA encendida por el punto de inicio de la línea.
**La Regla del Rojo Funcional.** El rojo sólo marca: inicio, kiai, fecha. Si no rotula un dato o un hito, no lleva rojo.

## Typography

**Display Font:** Shippori Mincho 600, self-hosted woff2 (fallback Times New Roman serif; cubre kanji)
**Body Font:** Zen Kaku Gothic New 400/700, self-hosted woff2 (fallback system-ui sans)

**Character:** Mincho serifada de lectura vertical japonesa para títulos — autoridad de imprenta; gótica japonesa neutra para cuerpo y UI — legibilidad de archivo. El pairing evita tanto lo corporativo como lo místico.

### Hierarchy
- **Display** (600, clamp 2–3.1rem, lh 1.15, `-.01em`, balance, máx 24ch): h1 de páginas internas.
- **Display Hero** (600, clamp 2.5–4.4rem): h1 de la apertura del home, a escala pared.
- **Headline** (600, clamp 1.5–2.2rem, lh 1.2, máx 26ch): h2 de bloques del home.
- **Nombres** (600, 19.5px, lh 1.3): h3 del linaje, centrado.
- **Body** (400, 16.5px, lh 1.7, máx 68ch): cuerpo de texto, verbatim del sitio 2001. 15.5px en tablas, 15px en footer, 13.5px en pies.
- **Label** (700, 12px, `.09em`, uppercase): encabezados de sitemap; (700, 11.5–12px, `.09em`): sellos y años.
- **Numeral de figura**: `Fig. N — ` generado por contador CSS, bold tinta, en cada figcaption.

### Named Rules
**La Regla del Cuerpo Verbatim.** Los títulos se corrigen con TITULO_FIXES (acentos); el cuerpo del texto de 2001 no se reescribe.

## Layout

Modelo de página de notación con riel: nav fija izquierda de `--riel-ancho: 218px` (borde derecho hairline, logo + ol de estaciones conectadas por línea vertical de 1.5px); `main`, header y footer corren con `margin-left: 218px`. Contenido editorial a `max-width: 68ch`; bloques del home a 1160px; sitemap a 1060px en tres columnas (1fr / 1.2fr / 1.2fr). El ritmo lo dan las fronteras hairline entre bloques, no el espaciado.

- **Apertura del home:** grid `minmax(380px, 44%) 1fr`, h1 + bajada + CTA a la izquierda, SVG del embusen (máx 620px, 82vh) justificado a la derecha; min-height 100vh.
- **≥1000px:** riel vertical fijo. **<1000px:** el riel se vuelve strip horizontal sticky (logo arriba, estaciones en scroll-x con la línea debajo); apertura a una columna, embusen centrado (44vh); linaje a 2 columnas; sitemap a 1 columna.
- **<540px:** CTA full-width, cuerpo 15.5px.
- Tabla de notación: números tabulares, padding derecho 22px.

## Elevation & Depth

Sistema plano con una sola sombra de montaje. La profundidad no viene de capas sino del papel: la lámina es un papel más claro (`#FCFAF4`) montado sobre el papel de página con borde hairline — profundidad de archivo, no de UI.

### Shadow Vocabulary
- **Montaje de lámina** (`0 1px 2px rgba(27,23,18,.05), 0 14px 34px -16px rgba(27,23,18,.22)`): estático en `.lamina` y fotos del linaje.
- **Hover de secuencia** (`0 18px 40px -16px rgba(46,77,107,.35)`): la misma sombra teñida de índigo, sólo en hover de galerías, transición .25s ease-out.

### Named Rules
**La Regla Keyline.** La grilla no se mueve entre páginas; las fronteras son hairlines de tinta, no sombras.

## Shapes

Esquinas casi cuadradas: radios de 2–3px sólo en CTA, sellos y foco — el papel no tiene bolas. El lenguaje de forma es lineal: hairlines de 1px, reglas de tinta de 2px (thead, cierre de tabla, footer), trazos de 1.5–3px en SVG. Puntos circulares sólo donde la notación los exige: marcadores de estación (8px), huellas del embusen, diamantes rotados 45° del linaje. Los sellos (`anio`, `sello-fecha`) rotan levemente (−2°/−2.5°) como estampado a mano. Lo faltante es punteado: `border: 2px dashed`.

## Components

### CTA «Sumate a la línea»
- **Shape:** radio 3px, `▶` como prefijo en `#E8B4A8`.
- **Primary:** fondo `{colors.linea}`, texto `{colors.papel}`, padding `15px 26px 15px 20px`, 700 16.5px.
- **Hover / Focus:** fondo → tinta, `translateY(-1px)`, transición .2s ease-out.
- **Secundaria:** `.cta-sec`, sólo texto bold 15.5px sin caja.

### Riel de estaciones (nav global)
- Línea vertical 1.5px `linea-suave` conectando marcadores circulares 8px (fondo papel, borde hairline-fuerte).
- Enlace `.estacion`: 14.5px, tinta-2, padding `7px 0 7px 26px`; hover → índigo.
- **Activa:** punto relleno de sello (rojo) + texto bold tinta — único elemento saturado.
- <1000px: strip horizontal sticky con línea inferior y scroll-x oculto.

### Lámina (figura de notación)
- Papel `#FCFAF4`, borde hairline, padding `10px 10px 0`, máx 560px, sombra de montaje, contador CSS.
- figcaption: hairline superior, 13.5px tinta-2, prefijo `Fig. N — ` bold tinta.
- En `.secuencia`: grid auto-fill minmax(170px, 1fr), reveal al scrollear (12px translateY, .55s).

### Tramo punteado `.falta` (cartela de ausencia)
- `border: 2px dashed hairline-fuerte`, padding `22px 24px`, 14.5px tinta-2.
- `strong` "Falta en el archivo" en tinta; nombre de archivo en `code` (700 12.5px mono, fondo papel-2). Nunca se reemplaza por relleno ni placeholder decorativo.

### Tabla de notación
- Bordes horizontales only: hairline por fila, regla 2px tinta arriba del thead y al cierre del tbody; th 700; números tabulares.

### Sello de fecha / año
- Texto rojo `{colors.sello}` 700 12px `.09em`, borde 1.5–2px currentColor, radio 2–3px, rotación −2°/−2.5°. Marca datos legacy «sitio 2001».

### Embusen (SVG del home)
- Trazo índigo 3px round-cap que se dibuja solo (2s, cubic-bezier(.25,.6,.3,1), respeta prefers-reduced-motion); huellas (papel/índigo 1.5px), kiai en rojo con aro, texto 700 13px gótica.

### Footer sitemap
- Regla superior 2px tinta; tres columnas: El dojo / El archivo / El dojo en Campana; h2 label 12px uppercase tinta-2; legal 13px bajo hairline.

## Do's and Don'ts

### Do:
- **Do** usar `{colors.linea}` (#2E4D6B) para toda interacción: hover, foco (`outline: 2px solid`), selección, CTA.
- **Do** marcar cada foto como lámina con numeral `Fig. N` y pie en tinta-2.
- **Do** rotular datos 2001 con `.sello-fecha` y nombres de archivos faltantes con `.falta code`.
- **Do** mantener la estación activa como único elemento saturado por página.
- **Do** respetar `prefers-reduced-motion`: sin trazo animado ni reveal.

### Don't:
- **Don't** usar rojo `#B33A26` decorativamente — sólo inicio, kiai, fecha, estación activa.
- **Don't** teñir, filtrar o modernizar fotos del archivo; se montan como están.
- **Don't** rellenar una foto ausente con placeholder gráfico: siempre `.falta` (tramo punteado rotulado).
- **Don't** reescribir el cuerpo verbatim de 2001 (sólo TITULO_FIXES en h1/title).
- **Don't** mover la keyline entre páginas ni sumar sombras más allá del montaje de lámina.
