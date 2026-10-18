# DESIGN.md — kyudokan-v3, mundo «Gusuku»

## Concepto

**Okinawa, no Japón-genérico.** El sitio son los muros de un *gusuku* — los castillos
de piedra coralina de Okinawa — encalados y pisados por tres siglos de sol de mar.
La isla es la prueba material del linaje: la escuela es el Karate-do de la familia
Higa, y nada de esto lo puede declarar un gimnasio vecino. El contenido del sitio
2001 se presenta verbatim, byte a byte: el archivo habla en su propia voz.

## Materiales

- **Encalado `--cal #E9E1D0`** — revoque calizo procedural (`tools/texturas_gusuku.py`:
  grano de llana + manchas + poros de coral, tileable). Nunca blanco plano de museo:
  el material tiene textura visible y temperatura.
- **Muro `--cal-2 #DBD1BE`** (`muro.jpg`, aclarado para legibilidad: peor caso de contraste ≥5:1) — el mismo revoque más oscuro y poroso;
  banda de la pared del linaje y del pie.
- **Teja `--teja #A63E1C`** (labels pequeños sobre muro usan teja-horno `#8F2F10`) — los techos rojos de Shuri. Aparece como curso de tejas
  escalopadas (SVG data-URI, jamás foto) coronando bandas y como flourish de secciones.
- **Mar Kerama `--mar #0E668C`** — el mar real de la isla: enlaces, banda *seigaiha*
  (olas concéntricas SVG procedural) bajo el curso de tejas.
- **Tinta `--tinta #2A2520` / hueso `--hueso #F6F1E6`** — texto casi negro cálido;
  paspartú de retratos y láminas.

## Motivos

- **Shisas guardianes** (`marca/shisa-izq/der.png`, recortados de los GIF 2001 sin
  teñir) flanquean «Bienvenidos» en el mismo renglón, a 2× nearest — presencia, no
  caricatura.
- **Fénix de Shuri** (`marca/fenix-shuri.png`, recortado del paño tejido del castillo)
  como fantasma a opacity 0.16 en la pared del linaje: identidad como agua de fondo,
  no como museo.
- **Caligrafía 空手道** (`kanji_kara_te_do_bu_do.JPG`) integrada con
  `mix-blend-mode: multiply` — el papel del JPG desaparece sobre el encalado, la tinta
  queda.
- **Sello del 70.º aniversario** (`marca/kyudokan-70.png`, del logo dorado sobre negro de
  la federación: alfa por luma, tinta negra pura como el crest, sin fondo) — par del crest
  en el masthead, mismo drop-shadow: crest a la izquierda, sello a la derecha.

## Reglas

1. **Contenido verbatim.** El texto de 2001 queda byte a byte (ortografía incluida);
   sólo `TITULO_FIXES` toca `<title>`/h1. Dead artifacts fuera (MatrixWay, To English,
   IE4+/800×600, Google Custom Search, afiliados).
2. **Fotos jamás teñidas.** Se montan como están, con paspartú hueso y hairline.
   Falta de foto = cartela `.falta` honesta con el nombre de archivo.
3. **Texturas procedurales.** Revoques de `tools/texturas_gusuku.py`; tejas y seigaiha
   son SVG; la caligrafía grande es el archivo real. Nada de gradientes planos como
   «material» (la banda de mar es gradiente de agua, no superficie de pared).
4. **Teja y mar funcionales.** La teja marca sellos, flourish, hover y foco; el mar,
   enlaces y la banda. Si no marca nada, no lleva acento.
5. **Movimiento mínimo**: reveal de láminas con IntersectionObserver + failsafe 3 s +
   `prefers-reduced-motion`.

## Estructura

Home: masthead (crest + nombre + ficha + sello 70.º) → riel de navegación → Bienvenidos (shisas) →
La Escuela (texto verbatim + tarjeta de Lugani en Shuri + 空手道) → banda de mar bajo
tejas → pared del linaje (retratos Higa + fénix) → pie de muro con tejas.
Internas: mismo masthead, riel con estación activa en teja, subnav de subsecciones bajo el
título, contenido y pie de muro con sitemap (El dojo / Historia y estilo / El dojo en Campana).
Mobile: crest y sello 70.º apilados a la izquierda del titular; riel sticky deslizable con fade
de affordance. FHD+: escala tipográfica +1.5px.

## Anti-referencias (mundos rechazados)

- **La Muestra/El Hilo** (main_opt-1): galería blanca lisa de museo — Gusuku es
  encalado texturado y cálido, con materialidad de piedra y sellos.
- **La Línea** (95be255): papel de notación índigo, «poco karateka» — Gusuku es la
  isla misma: tejas, mar, shisas, caligrafías reales.
- **El shomen del dojo** (main_opt-2): madera oscura y luz de nicho — Gusuku es claro,
  mineral y exterior: muro de sol, no tokonoma.
