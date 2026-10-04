# SEO tradicional, GEO y AEO — kyudokan-v3

Informe del lote de SEO tradicional implementado en `karatekyudokan.com.ar` y
cola de mejoras para motores generativos (GEO) y respuestas directas (AEO).
Sin datos inventados: todo lo listado como hecho está en el repo; lo pendiente
queda como backlog.

## 1. Implementado en este lote

|Punto|Detalle|Archivo|
|---|---|---|
|Un `h1` por página|El `h1` del masthead bajó a `p.razon-social`; cada página interna promueve su `h2.pagina-titulo` a `h1`; el home promueve `h1.display`. Jerarquía resultante: h1 página → h2 secciones → h3|`src/_includes/base.html`, `src/gusuku.css`, 16 páginas|
|Titles con keyword|Los 16 `<title>` reescritos con la palabra «karate» y sufijo de marca `— Karate Kyudokan Campana` (corto cuando el tema ya lidera)|front matter `title` de las 16 páginas|
|Meta descriptions|Las 16 páginas con `description` propia (140-160 chars), templada sin condicional|front matter + `src/_includes/base.html`|
|Canonical|`<link rel="canonical">` absoluto con dominio de producción en todas las páginas|`src/_includes/base.html`|
|Open Graph / Twitter|`og:site_name`, `og:type`, `og:url`, `og:title`, `og:description`, `og:locale es_AR` y `twitter:card summary_large_image`|`src/_includes/base.html`|
|og:image|`og-image.png` 1200×630 (68 KB): kanjis 完進館 verticales sobre encalado + «Karate Dojo Campana»|`src/assets/marca/og-image.png`|
|Página 404|`/404.html` con layout, mensaje honesto y vuelta al inicio; excluida de colecciones (no entra al sitemap)|`src/404.html`|
|Enlaces internos contextuales|«Karate-do Shorinryu Kyudokan de Okinawa» → `/escuela_estilo/` y «Shurite» → `/sintesis_historica/` desde prosa del home|`src/index.html`|
|robots.txt + sitemap.xml|robots referencia el sitemap absoluto; sitemap dinámico sobre `collections.all` con dominio de producción (infra previa de esta sesión)|`src/robots.txt.liquid`, `src/sitemap.xml.liquid`, `src/_data/sitio.json`|
|JSON-LD|Grafo Organization + 2 SportsActivityLocation + 2 Person + Event de la expo anual (infra previa de esta sesión)|`src/contacto.html`|

## 2. Pasos manuales externos (SEO)

Cosas que no se pueden automatizar desde el repo:

1. **Perfil de Empresa en Google** con categoría «Escuela de artes marciales»,
   las dos sedes (Rawson 327 y Jean Jaurés 983, Campana), horarios idénticos a
   la tabla de `/contacto/` y NAP igual al footer del sitio.
2. **Google Search Console y Bing Webmaster Tools**: dar de alta
   `https://karatekyudokan.com.ar` y enviar `https://karatekyudokan.com.ar/sitemap.xml`.
3. **Cuando existan fotos reales** para reemplazar cartelas `.falta`: nombrar
   los archivos con contexto local (p. ej. `karate-ninos-campana.jpg`) y usar
   `alt` descriptivos. Mientras tanto, las cartelas siguen honestas.

## 3. Backlog GEO (motores generativos)

- **Párrafo-definición de apertura**: 2-3 frases «qué es …» al inicio de cada
  página temática, como contenido nuevo arriba de la prosa 2001 (sin tocarla).
- **JSON-LD**: ya implementado en contacto (grafo con Organization, sedes,
  senseis y evento). Extender el patrón a otras páginas si hace falta.
- **FAQ con schema FAQPage**: preguntas locales reales («¿dónde hay clases de
  karate en Campana?», «¿a qué edad puede empezar un niño?») con respuestas
  verificables contra el contenido del sitio.
- **E-E-A-T nominal**: el schema `Person` de los senseis ya existe; falta línea
  de responsabilidad de contenido visible en el footer («responsable del
  contenido: …»).
- **Huella externa consistente**: ficha de Wikidata de la escuela, el blog
  Blogspot histórico enlazando al sitio nuevo, directorios deportivos
  argentinos. Mismo NAP en todos.
- **Comparación estructurada de estilos** en «Escuela y estilo»: tabla
  Shorinryu vs otros estilos con fuentes del contenido existente.

## 4. Backlog AEO (respuestas directas)

- **Frase-respuesta de 40-60 palabras** antes de la tabla de horarios en
  contacto (responde «¿cuándo y dónde entrena el Kyudokan en Campana?»).
- **Primer párrafo-respuesta** en cada página temática, arriba de la prosa
  2001, sin reescribirla.
- **Lista de katas como lista HTML real** si hoy vive en prosa: los motores
  extraen listas mejor que párrafos.
- **Mini-índice con anclas** en las páginas largas (síntesis histórica,
  katas) para salto directo a cada sección.
