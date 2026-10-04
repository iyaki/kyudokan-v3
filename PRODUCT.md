# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Eleventy 3 (static site generator) over plain HTML/CSS. Pages are Liquid templates with front matter; shared shell in `src/_includes/base.html`, nav data in `src/_data/riel.json`. Build: `npm run build` → `_site/`; dev: `npm run serve`. Init confirmed plain static; migrated to Eleventy at owner request (2026-10-02, PR #4).

## Users

- **Primary (front door):** Prospective karate students in Campana / Zárate area (Buenos Aires, Argentina) and parents of kids — deciding whether to train at this dojo: what is Kyudokan, who teaches, when and where, how to start.
- **Secondary (layered underneath):** The wider karate / Kyudokan community — Okinawan Shorin-ryu practitioners and researchers interested in the Higa family lineage, history, and the dojo's documented activity (tournaments 1988–2000, exhibitions, kata, Hombu dojo visits).

## Product Purpose

Official site of the **Centro de Enseñanza de Karate Do — Estilo Shorinryu Kyudokan de Okinawa**, taught by Profesor **Cristian Lugani**, representative of the Kyudokan school in Campana, Buenos Aires, Argentina. It presents the dojo to recruit students and preserves the history and lineage of the school. Success: a local prospect contacts/visits the dojo; the lineage archive remains publicly accessible.

## Positioning

Direct local representation (sucursal Campana) of the Kyudokan school — the Karate-do of the **Higa family**, founded by **Yuchoku Higa** (10th Dan), rooted in the ancient Shorin / Shurite school of Okinawa. A neighboring gym cannot truthfully claim this unbroken Okinawan lineage, nor the dojo's decades of documented activity in Argentina.

## Operating Context

- Dojo address (legacy): Jean Jaures 983, Campana, Buenos Aires, Argentina. Tel. (54)(03489) 431664. Email: cristian@karatelugani.com.ar
- Training schedules, arrival directions, and class offering (kids / women / physical conditioning / sport & traditional karate) were published pages in the legacy site.
- Content language: Spanish (the legacy site offered machine translation to English; no confirmed commitment to maintained bilingual content).
- Affiliation context: Kyudokan hombu (Okinawa) and the Higa family (Yuchoku, Jintatsu, Minoru, Oscar, Benito Higa) appear throughout the content and photo archive.

## Capabilities and Constraints

- v3 is a **full redesign**: new visual world and modern UX; product truth preserved, the 2001 look treated as evidence only. Confirmed by user.
- **Legacy site is the source of truth** for text and photos, migrated where relevant. Confirmed by user.
- Dropped without replacement (dead artifacts): Flash applet banner, guestbook CGI (`cgi-sys/`), Google Custom Search form, martial-arts affiliate banner, "Designed by MatrixWay", "optimized for IE4+ / 800×600" claims.
- Legacy `html/` contains ~250 pages: dojo info (presentación, centro de enseñanza, horarios, cómo llegar, contacto), articles (qué es karate, karate y el niño / la mujer, karate deportivo vs tradicional, acondicionamiento físico, credo del samurái, pensamiento), history (síntesis histórica, árbol genealógico, biografía Jintatsu Higa, la familia Higa, Okinawa), photo/afiche galleries (torneos 1988–2000, exhibiciones, katas, Hombu, Okinawa), noticias (nacionales/internacionales), links.
- `src/` holds the v3 modernized site (world «Gusuku»): **Eleventy source tree since 2026-10-02** — pages are front-matter + content templates, shell lives in `src/_includes/base.html`. The original pass generated whole-HTML pages in place from the pristine `legacy/` sources via `tools/restyle.py`; that script predates the Eleventy conversion and must NOT be re-run against `src/` (it would clobber the template form). **Content fidelity rule (updated by owner, 2026-09-30): body text is corrected ORTHOGRAPHICALLY (missing 2001 tildes and genuine typos) via the `ORTO_FIXES` dictionary in tools/restyle.py — applied word-wide with case preservation. Prose is NOT reworded. Dead 2001 artifacts dropped (MatrixWay, To English, IE4+/800×600 claims, guestbook CGI). Pristine sources live in `legacy/` (iso-8859-1) — always restore before any future regeneration.**
- Wood textures are procedural, deterministic assets: regenerate with `python3 tools/texturas.py` → `src/assets/texturas/`.
- **Undecided / open facts (owner must supply; do not invent):** current schedule, current phone/email, any post-2001 news or activity. Owner-supplied (2026-09-30): rank of Cristian Lugani **8° Dan Kyoshi** (display «Sensei Cristian Lugani (8° Dan Kyoshi)»; legacy body still reads «Profesor Cristian Lugani (2do. Dan)», verbatim) and **Koyu Higa as current kaichou** of the Kyudokan (Minoru Higa fue kaichou hasta 2025 — dato del dueño, reflejado en el Linaje del home) — his portrait was recovered from Chris Willson's «Karate Masters Portrait Project» (travel67.com, `645z0921-le640.jpg`; fuente registrada aquí — el crédito visible fue retirado a pedido del dueño). Until the remaining facts are supplied, legacy values are the record and must not be embellished.

## Brand Commitments

- Name and identity bind to: **Kyudokan** (the school), **Higa family lineage**, **Cristian Lugani** (sensei), **Campana, Argentina** (location).
- Kanji calligraphy images exist in legacy assets (karate-do, makoto/sinceridad, shin, hara, fudochi, kyu-shin-ryu, do) and are candidate authentic assets.
- The 2001 visual identity (black/red base GIFs, shisa lion guardians, gold engraved nav buttons) is historical evidence, not a binding commitment — v3 replaces it.

## Evidence on Hand

- `legacy/` — complete 2001 site: all text content and ~250 pages.
- `legacy/assets/images/` — photo archive: portraits of the Higa masters (Yuchoku, Jintatsu, Minoru, Oscar, Benito), Chibana Chosin, Cristian Lugani; kanji calligraphy; tournament/exhibition/Okinawa/Hombu photos in `legacy/html/fotos_*.html` galleries; tournament posters (afiches).
- Absence that future work must not fabricate: no testimonials, no current news, no verified credentials beyond the legacy record.
- Owner decision (2026-10-04): in the unified `/contacto/`, the two missing 2001 map photos (`mapa_comollegar.jpg`, `mapa_comollegar2.jpg`) are replaced by an OpenStreetMap embed instead of `.falta` cartelas — standing exception to the placeholder policy for these two files.
- Pedro Fattore (cartela in `/presentacion/`): sourced from English Wikipedia, article «Shōrin-ryū Kyudōkan» — «Master Pedro Fattore was a great representative of the central dojo of Okinawa» in Argentina; photo provided by the owner (Instagram post DOtNw4LDu-_), cropped to cartela portrait at `src/assets/images/pedro_fattore.jpg`.
- **Photo archive recovery status (2026 pass):** of 196 locally-missing image references, 157 remain — the rest were restored: 16 more originals recovered this pass from Wayback Machine captures of `karatelugani.com.ar` (2001 snapshots, 8 more files inherited from the previous pass's recovery), plus 23 NOF thumbnails re-derived locally (ffmpeg) from recovered originals. Remaining references render as honest labeled placeholders (`.falta`), naming the original file; they are recoverable from the original server if it ever returns.

## Product Principles

1. **Lineage is credibility.** The Higa-family chain, Okinawan roots, and documented history are the core proof; they must stay prominent and accurate.
2. **The archive is an asset.** Two decades of photographed activity survive the redesign; a full redesign may not orphan or discard it silently.
3. **Recruitment is the front door.** A prospect must find who, what, where, when, and how to start within the first viewport or two.
4. **Sober truth over embellishment.** A traditional school speaks with restraint; never invent credentials, testimonials, dates, or history. Stale facts stay marked as legacy until the owner updates them.
