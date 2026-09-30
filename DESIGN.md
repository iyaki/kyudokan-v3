---
name: Kyudokan Campana — El shomen del dojo
description: El sitio como el frente ceremonial del dojo — pared de madera nobla, tokonoma hundido, los maestros colgados y luz cálida de práctica vespertina.
colors:
  madera: "#1D140D"
  madera-2: "#261A11"
  marco: "#3D2B1B"
  marco-claro: "#55402A"
  hueso: "#EDE1CC"
  hueso-2: "#BCAB90"
  hinomaru: "#C2311F"
  lamina-papel: "#EFE6D4"
  lamina-texto: "#4A3E2C"
  caligrafia-papel: "#F2EADA"
  luz: "rgba(233, 186, 116, .30)"
typography:
  display:
    fontFamily: "'Shippori Mincho', 'Times New Roman', serif"
    fontSize: "clamp(1.4rem, 1rem + 1.9vw, 2.3rem)"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: ".06em"
  headline:
    fontFamily: "'Shippori Mincho', 'Times New Roman', serif"
    fontSize: "clamp(1.7rem, 1.2rem + 2vw, 2.6rem)"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: ".01em"
  body:
    fontFamily: "'Zen Kaku Gothic New', system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.75
  label:
    fontFamily: "'Zen Kaku Gothic New', system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 700
    letterSpacing: ".07em"
rounded:
  sm: "2px"
  md: "3px"
spacing:
  shomen-ancho: "1080px"
  maestros-ancho: "860px"
  cuerpo: "66ch"
components:
  placa-nav:
    backgroundColor: "transparent"
    textColor: "{colors.hueso-2}"
    rounded: "{rounded.sm}"
    padding: "9px 12px"
  placa-nav-activo:
    backgroundColor: "transparent"
    textColor: "{colors.hueso}"
  entrada-cta:
    backgroundColor: "{colors.madera-2}"
    textColor: "{colors.hueso}"
    rounded: "{rounded.sm}"
    padding: "13px 18px"
  entrada-cta-hover:
    backgroundColor: "#2E1D12"
    textColor: "{colors.hueso}"
  sello-dojo:
    backgroundColor: "{colors.hinomaru}"
    textColor: "#F5E9D5"
    rounded: "{rounded.sm}"
    padding: "8px 5px"
  lamina:
    backgroundColor: "{colors.lamina-papel}"
    textColor: "{colors.lamina-texto}"
    padding: "8px 8px 0"
  falta:
    backgroundColor: "rgba(0, 0, 0, .28)"
    textColor: "{colors.hueso-2}"
    padding: "20px 22px"
---

# Design System: Kyudokan Campana — El shomen del dojo

## Overview

**Creative North Star: "El shomen del dojo"**

El sitio es el shomen — el frente ceremonial del dojo de Campana. Una pared de madera nobla oscura donde la luz cálida de la práctica de la tarde cae desde arriba; en el centro, un nicho hundido estilo tokonoma enmarca el kakemono con la caligrafía 空�u624b�u9053 del archivo, colgado de su viga con cordón y sellado en rojo. Sobre el piso elevado del kamidana, los cuatro maestros cuelgan como retratos enmarcados en madera: Yuchoku Higa, Jintatsu Higa, la familia, Cristian Lugani. El contenido del sitio de 2001 se presenta verbatim, byte a byte — es el dojo mismo, no una restauración.

La densidad es la de un lugar construido, no de un producto: marcos gruesos de madera (`--marco`, 8–12px), mats de papel para cada foto, sombras que provienen de la luz y de la hondura del nicho. El movimiento es diegético y mínimo: el kakemono y los retratos *cuelgan* (caen 8px hasta asentarse, en cascada); nada más se anima.

**Key Characteristics:**
- Pared de madera procedural (texturas JPG de `tools/texturas.py`), nunca gradiente plano ni periódico.
- Luz de dojo: resplandor radial cálido arriba, sombras de nicho hacia adentro.
- Tokonoma hundido con kakemono + tokobashira (pilastras laterales) en la home.
- Rojo hinomaru exclusivamente funcional: sello del dojo, marca activa, CTA-hover, foco, selección.
- Fotos jamás teñidas: se montan como están, enmarcadas en madera con mat de papel.
- Falta = cartela honesta: tramo punteado rotulado con nombre de archivo, jamás relleno.

## Colors

Todo es madera en gradación cálida y hueso; el rojo es un sello que aparece dos veces por pantalla.

### Primary
- **Hueso** (`#EDE1CC`): el texto sobre la madera — títulos mincho, cuerpo, enlaces. Su hover sube a `#FFF6E6` (más luz sobre el papel).

### Secondary
- **Hinomaru** (`#C2311F`): SOLO marca funcional — sello vertical del kakemono, borde y subrayado de la placa activa del nav, hover/focus del CTA, foco visible (`outline`), selección de texto. Jamás decorativo, nunca en fondos grandes.

### Neutral
- **Madera** (`#1D140D`): fondo de la pared (bajo la textura).
- **Madera 2** (`#261A11`): superficie elevada — fondos de CTA, base de retratos, track de scrollbar.
- **Marco** (`#3D2B1B`): los marcos de madera — kakemono, retratos, láminas (bordes de 7–12px).
- **Marco claro** (`#55402A`): detalle noble — thumb de scrollbar, borde de CTA en reposo.
- **Hueso 2** (`#BCAB90`): texto secundario, pies de retrato, placas del nav, datos legacy.
- **Mat de lámina** (`#EFE6D4`): el papel dentro de cada marco; su texto de pie es `#4A3E2C`.
- **Papel de caligrafía** (`#F2EADA`): el soporte del kakemono.
- **Luz** (`rgba(233,186,116,.30)` y vecinas): resplandores radiales que bañan pared y nicho — luz, no color de superficie.

### Named Rules
**La Regla del Rojo Funcional.** El hinomaru sólo marca lo activo y lo autenticado: sello, placa activa, CTA-hover, foco, selección. Si no está marcando, no lleva rojo.
**La Regla Contenido Verbatim.** El texto del sitio 2001 se presenta byte a byte, sin restaurar ortografía. Lo que dice el archivo, dice la pared.

## Typography

**Display Font:** Shippori Mincho 600, self-hosted woff2 (fallback Times New Roman serif; cubre kanji)
**Body Font:** Zen Kaku Gothic New 400/700, self-hosted woff2 (fallback system-ui sans)

**Character:** Mincho serifada para lo que está *en* la madera — títulos, nombres de maestros, marca del dojo — con `text-shadow` sutil para despegarse de la pared. Gótica japonesa neutra para el cuerpo verbatim y la UI. El pairing mantiene autoridad de kanji sin misticismo de bazar.

### Hierarchy
- **Headline** (600, clamp 1.7–2.6rem, lh 1.2, `.01em`, balance, máx 26ch): h1 de páginas internas y del nicho, en hueso con sombra.
- **Display** (600, clamp 1.4–2.3rem, lh 1.4, `.06em`): título del dojo bajo el kakemono, marca de la barra.
- **Nombres** (600, 14px, lh 1.3, mincho): figcaption de cada maestro, en hueso-2.
- **Body** (400, 17px, lh 1.75, máx 66ch): cuerpo verbatim 2001 en hueso; 16px bajo 420px. 13px en pies de lámina, 12.5px legal.
- **Label** (700, 12px, `.07em`, uppercase): placas del nav en hueso-2; (700, 11.5px, `.09em`): encabezados de sitemap.
- **Numeral de figura**: `Fig. N — ` generado por contador CSS, bold, sobre el mat de lámina en `#4A3E2C`.

### Named Rules
**La Regla Contenido Verbatim.** Los h1/title se corrigen con TITULO_FIXES (acentos); el cuerpo de 2001 no se reescribe ni se moderniza.

## Layout

Una sola columna construida: `main` a `max-width: 1080px` centrado con padding lateral `clamp(18px, 4vw, 48px)`; todo se apoya sobre la pared. La home es una composición vertical ceremonial: pared → tokonoma (viga, kakemono, título) → estante del kamidana con los 4 retratos → datos del dojo → texto de la escuela (caja hundida a 66ch) → CTA de entrada → pie.

- **Shomen:** `.pared` con marco de 12px `#150C06` y outline interior de hueso al 22%; pilastras de 34px flanqueando (ocultas <760px); zócalo de tres franjas al pie del nicho.
- **Retratos:** grid de 4 columnas (`repeat(4, 1fr)`, gap `clamp(14px, 3vw, 34px)`) apoyado sobre el `.estante` de 34px; 2 columnas <760px.
- **Páginas internas:** `.barra` sticky de madera noble (marca + placas, borde inferior de 3px `#0F0905`); contenido a 1080px, cuerpo a 66ch; sitemap en tres columnas (1fr / 1.2fr / 1.2fr), 1 columna <760px.
- **Secuencias:** grid `auto-fill minmax(180px, 1fr)`, gap `30px 24px`.
- Tabla de notación: números tabulares, padding derecho 22px.

## Elevation & Depth

La profundidad es arquitectónica, no de UI: viene de la luz que entra y de los planos construidos — pared al fondo, nicho hundido, viga y marcos adelantados, piso elevado. Las sombras son grandes, negras y difusas (`rgba(0,0,0,.5–.85)`), como de habitación real; el sistema usa inset shadows para la hondura del nicho (techo y costados proyectando sombra adentro) y drop shadows para lo que cuelga.

### Shadow Vocabulary
- **Hondura del nicho** (`inset 0 26px 44px -16px rgba(0,0,0,.80)` + inset laterales + glow exterior `0 34px 70px -22px`): en `.pared`; el tokonoma se ve excavado.
- **Colgado** (`0 3px 6px rgba(0,0,0,.55), 0 30px 60px -14px rgba(0,0,0,.7)`): kakemono y caligrafía, que cuelgan de la viga.
- **Retrato** (`0 6px 10px -4px rgba(0,0,0,.7), 0 22px 34px -12px rgba(0,0,0,.6)`): cada maestro sobre el estante.
- **Lámina** (`0 4px 8px rgba(0,0,0,.45), 0 22px 44px -14px rgba(0,0,0,.6)`): foto enmarcada en páginas internas; en hover de galería la capa externa se tiñe levemente de rojo (`rgba(194,49,31,.25)`).

### Named Rules
**La Regla de la Luz, No del Tinte.** La variación tonal proviene de resplandores radiales y sombras de luz de dojo; las fotos nunca se tiñen para integrarse.

## Shapes

Silueta de carpintería: bordes rectos, marcos gruesos de madera (7px retratos, 8px láminas y caligrafía, 12px nicho), radios mínimos (2–3px sólo en sellos, foco y placas). Doble filo en cada marco: `outline` de 1px hueso al ~25% desplazado hacia adentro, como el canto biselado de un marco real. Lo lineal domina: reglas de 1–2px en hueso para tablas y fronteras, trazos de 1.5px para los ramales del índice. Lo faltante es punteado: `border: 2px dashed rgba(237,225,204,.45)`.

## Components

### Kakemono (caligrafía del home)
- Cordón vertical de 2px desde la viga; soporte `#F2EADA` con marco de 12px `--marco` y outline biselado; img máx 540px.
- **Sello del dojo** (`--hinomaru`): cuadrado vertical (`writing-mode: vertical-rl`) montado en la esquina inferior derecha, desbordando −14px; texto `#F5E9D5`, mincho 600 13px.

### Tokobashira (pilastras)
- Postes de 34px a cada lado del nicho, textura `noble.jpg` con luz de canto (línea cálida a la izquierda, sombra a la derecha); `box-shadow` de poste. Ocultas <760px.

### Estante del kamidana
- Tablón de 34px con textura `piso.jpg`, brillo superior de 2px, borde inferior de 3px `#0F0905`, sombra proyectada abajo + inset; los retratos se apoyan alineados a `align-items: end`.

### Placas de navegación (`.placa`)
- **Shape:** borde 1px, radio 2px, padding `9px 12px`.
- **Reposo:** hueso-2 sobre borde hueso al 28%, 700 12px uppercase `.07em`.
- **Hover:** borde y texto → hueso, transición .2s ease-out.
- **Activa:** borde `--hinomaru` + `box-shadow: inset 0 -2px 0 var(--hinomaru)` — el único elemento en rojo del nav.

### CTA de entrada (`.entrada-dojo a`)
- **Shape:** borde 1px `--marco-claro`, radio 2px, padding `13px 18px`.
- **Reposo:** fondo `--madera-2`, hueso, 700 13.5px uppercase `.08em`.
- **Hover / Focus:** borde → `--hinomaru`, fondo `#2E1D12` — el rojo aparece sólo como respuesta.

### Lámina (foto enmarcada)
- Mat `#EFE6D4`, marco de 8px `--marco`, outline biselado, padding `8px 8px 0`; img máx `72vh`.
- figcaption: hairline superior sobre el mat, 13px `#4A3E2C`, prefijo `Fig. N — ` bold.
- En `.secuencia`: hover levanta `translateY(-2px)` con sombra teñida de rojo; reveal al scrollear (12px translateY, .55s).

### Cartela `.falta` (tramo punteado rotulado)
- `border: 2px dashed hueso .45`, fondo negro al 28%, padding `20px 22px`, 14px hueso-2.
- `strong` del motivo en hueso; nombre de archivo en `code` mono 700 12px sobre negro al 35%. Nunca se reemplaza por relleno ni placeholder decorativo.

### Tabla de notación
- Bordes horizontales only en hueso al 22%: regla de 2px hueso arriba del thead y al cierre del tbody; th 700; números tabulares.

### Índice de ramales
- Lista sin viñetas: cada ítem lleva una línea horizontal de 1.5px hueso al 40% de 18px a la izquierda — ramales que salen de la pared.

### Footer sitemap
- Regla superior 1px hueso al 30%; tres columnas: El dojo / El archivo / El dojo en Campana; h2 label 11.5px uppercase hueso-2; enlaces 14.5px hueso-2 → hueso; legal 12.5px bajo hairline.

## Do's and Don'ts

### Do:
- **Do** usar texturas procedurales de `tools/texturas.py` (`pared/nicho/noble/piso.jpg`) para toda superficie de madera.
- **Do** montar cada foto como lámina: marco `--marco` de 8px, mat `#EFE6D4`, numeral `Fig. N`.
- **Do** reservar `--hinomaru` para sello, placa activa, CTA-hover, foco (`outline: 2px solid`) y selección.
- **Do** rotular cada ausencia con `.falta` (tramo punteado + nombre de archivo en `code`).
- **Do** presentar el cuerpo verbatim 2001 byte a byte; animar sólo el colgado/reveal, respetando `prefers-reduced-motion`.

### Don't:
- **Don't** teñir, filtrar o modernizar fotos del archivo; se enmarcan como están (PNG con transparencia → `object-fit: contain`).
- **Don't** generar madera con gradientes periódicos o planos: la textura viene de `tools/texturas.py`; la luz, del CSS.
- **Don't** usar rojo decorativamente — si no marca lo activo o lo autenticado, no lleva rojo.
- **Don't** rellenar una foto ausente con placeholder gráfico: siempre cartela honesta.
- **Don't** reescribir el cuerpo verbatim de 2001 (sólo TITULO_FIXES en h1/title).
- **Don't** sumar sombras suaves de UI (glows pastel, elevaciones Material): las sombras son de habitación — negras, grandes, con dirección de luz.
