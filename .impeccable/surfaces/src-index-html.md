---
version: 1
slug: "src-index-html"
primary_target: "src/index.html"
related_targets: []
---

# Surface brief — home (src/index.html) — mundo «La Línea»

Scope: home + sistema visual que heredan las ~116 páginas internas (conversión con tools/restyle.py). Modo **Persuade** en la puerta de reclutamiento; el archivo interno opera como Read.

- **Audience / job:** prospecto de Campana/Zárate (adolescente o madre/padre) decidiendo si entrena en el dojo; secundario: comunidad karate/linaje interesada en los Higa.
- **Action:** una sola — WhatsApp «Sumate a la línea» (wa.me/543489431664, número legacy marcado en PRODUCT.md).
- **Proof/content:** sucesión real verificada del linaje (Yuchoku Higa fundador 10º Dan Shuri-te → Jintatsu Higa 1938 Argentina / 8º Dan Kyoshi → familia Higa → Cristian Lugani 2º Dan, sitio 2001, Campana), retratos reales del archivo, horarios 2001, kanjis de caligrafía del archivo.
- **Constraints:** estática (HTML+CSS, JS inline mínimo para el trazo); 100% del contenido legacy preservado (mandato del usuario); fotos jamás teñidas; foto faltante = tramo punteado rotulado, nunca relleno; sin misticismo zen de bazar; datos legacy marcados «sitio 2001».
- **Memorable moment:** la línea del embusen dibujándose sola sobre el papel al cargar; el punto de inicio de la línea enciende la CTA.

## Direction contract

THESIS: Una escuela de karate es una línea que no se corta; el diagrama de esa línea es el embusen. El sitio es la página de notación del dojo — el lenguaje con que los libros de karate dibujan cada forma: trazos, huellas, puntos de kiai — y esa única línea trazada es puerta y riel de todo el archivo. Rehusa la plantilla gym/SaaS, la galería blanca y la lona cruda.

OWN-WORLD: Papel cálido #F6F2E9, tinta #191613/#5A5347, acento índigo ai-iro #2F4B6E para la línea y la interacción; rojo sello #B33A26 SOLO como marca funcional (inicio, kiai, fecha), jamás decorativo. Tipo self-hosted: Shippori Mincho (display, cubre kanji) + Zen Kaku Gothic New (texto/UI). Componentes: riel de línea con estaciones, lámina (foto + numeral de figura + pie), tabla de notación (horarios), sello de fecha, tramo punteado rotulado (falta).

STORY: El prospecto ve la línea cruzar la portada y entiende que esta práctica viene de Shuri a Campana sin cortarse; recorre sus estaciones (quién enseña, horarios, cómo llegar) y actúa: WhatsApp.

FIRST VIEWPORT: papel; wordmark del dojo arriba; el embusen trazado en grande cruzando el viewport (SVG que se dibuja al cargar); h1 en mincho a escala pared; bajada; CTA «Sumate a la línea» sobre el punto de inicio de la línea; primera estación visible sin scrollear.

FORM: página de notación: la línea como riel lateral con estaciones (nav global), láminas registradas a la línea, tablas de notación para horarios, sellos chicos para fechas, numeración de figura en cada foto. El rojo nunca decora: sólo marca.

RAISES: De jackfield — línea ininterrumpida como estado: la ausencia es un tramo punteado rotulado con su nombre, jamás un relleno. De ukiyoe — keyline fija: la grilla no se mueve entre páginas; sellos chicos como único mobiliario rojo. De film — honestidad de época: el material 2001 se rotula como tal, las fotos no se modernizan. De marquesina — un solo punto encendido por página: la estación activa es el único elemento saturado.
