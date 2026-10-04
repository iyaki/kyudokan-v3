---
version: 1
slug: "src-centro-de-ensenanza-html"
primary_target: "src/centro_de_ensenanza.html"
related_targets: []
---

# Surface brief — src/centro_de_ensenanza.html (+ CSS acotado en src/gusuku.css)

## Surface
Página interna «Centro de Enseñanza» (/centro_de_ensenanza/): la página de lectura larga del dojo — qué es enseñanza integral, Karate vs Karate-Do, y el cierre declarativo. Subnav propio (Horarios · Acondicionamiento · Mujer · Niño).

## Mode
**Read.** Página de prosa larga; el diseño sirve la lectura, las fotos son registro del archivo.

## Dirección
- Restaurar la composición 2001: las tres fotos flotadas alternadas (der/izq/der) dentro de la prosa — v3 las había apilado en bloques que cortan el ritmo. Float CSS nativo (media query los apaga en ≤760px: full-width centradas, max 320px).
- «Enseñanza Integral» (label colorado 2001) → label teja-horno espaciado (lenguaje `.rol`), scoped `.centro`.
- Cierre «Por esto y mucho más nosotros hacemos Karate-Do.» → declaración display: Shippori Mincho, centrada, teja-flourish encima (patrón del home). La máxima «Karate ni sente nashi» queda en su párrafo verbatim — no se reordena texto.
- CTA: botón-imagen GIF «Mapa: cómo llegar al Centro de Enseñanza» → sello real (borde teja, uppercase, hover fill) hacia /como_llegar/.

## Contenido y fidelidad
- Prosa 2001 verbatim con orto ya aplicada (camaradería, socializarse, basado…). No se reescribe nada.
- Alt de fotos descriptivos desde los nombres de galería documentados (seminario filial Campana; espectáculo callejero los niños primero; Lugani con niños en Japón).

## Artefactos 2001 eliminados
- Botón-imagen «Todas las Fotos» (sección fotos gateada por el dueño; muerto en v3).
- GIF botón «Mapa» → reemplazado por sello de texto real (mismo destino /como_llegar/).
- Links «Servicios» y «Cupon de Descuento» del subnav 2001: páginas jamás migradas — siguen fuera.

## Checks
build + check_links + floats medidos (texto envuelve, no overflow-x) en desktop y 390px + contraste hover del sello ≥4.5:1 + detector.
