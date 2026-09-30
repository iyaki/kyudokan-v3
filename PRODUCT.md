# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Plain static HTML/CSS. No build tooling; legacy content stays flat files. Confirmed by user in init.

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
- `src/` holds the v3 modernized site (world «El shomen del dojo», 2026 pass on `main_opt-2`): hand-built home + ~115 internal pages generated in place from the pristine `legacy/` sources by `tools/restyle.py`. **Content fidelity rule (user mandate, tightened on the 2.ª vuelta): the original page content is presented VERBATIM, byte for byte — including the 2001 orthography ("Enseanza", "transmisin"). Nothing added, nothing reworded; only presentation changed. The only permitted transformations: `<title>`/h1 orthography dictionary (TITULO_FIXES) and dead 2001 artifacts dropped (MatrixWay, To English, IE4+/800×600 claims).**
- Wood textures are procedural, deterministic assets: regenerate with `python3 tools/texturas.py` → `src/assets/texturas/`.
- **Undecided / open facts (owner must supply; do not invent):** current rank of Cristian Lugani (legacy says 2nd Dan, 2001), current schedule, current phone/email, any post-2001 news or activity. Until supplied, legacy values are the record and must not be embellished.

## Brand Commitments

- Name and identity bind to: **Kyudokan** (the school), **Higa family lineage**, **Cristian Lugani** (sensei), **Campana, Argentina** (location).
- Kanji calligraphy images exist in legacy assets (karate-do, makoto/sinceridad, shin, hara, fudochi, kyu-shin-ryu, do) and are candidate authentic assets.
- The 2001 visual identity (black/red base GIFs, shisa lion guardians, gold engraved nav buttons) is historical evidence, not a binding commitment — v3 replaces it.

## Evidence on Hand

- `legacy/` — complete 2001 site: all text content and ~250 pages.
- `legacy/assets/images/` — photo archive: portraits of the Higa masters (Yuchoku, Jintatsu, Minoru, Oscar, Benito), Chibana Chosin, Cristian Lugani; kanji calligraphy; tournament/exhibition/Okinawa/Hombu photos in `legacy/html/fotos_*.html` galleries; tournament posters (afiches).
- Absence that future work must not fabricate: no testimonials, no current news, no verified credentials beyond the legacy record.
- **Photo archive recovery status (2026 pass):** of 196 locally-missing image references, 157 remain — the rest were restored: 16 more originals recovered this pass from Wayback Machine captures of `karatelugani.com.ar` (2001 snapshots, 8 more files inherited from the previous pass's recovery), plus 23 NOF thumbnails re-derived locally (ffmpeg) from recovered originals. Remaining references render as honest labeled placeholders (`.falta`), naming the original file; they are recoverable from the original server if it ever returns.

## Product Principles

1. **Lineage is credibility.** The Higa-family chain, Okinawan roots, and documented history are the core proof; they must stay prominent and accurate.
2. **The archive is an asset.** Two decades of photographed activity survive the redesign; a full redesign may not orphan or discard it silently.
3. **Recruitment is the front door.** A prospect must find who, what, where, when, and how to start within the first viewport or two.
4. **Sober truth over embellishment.** A traditional school speaks with restraint; never invent credentials, testimonials, dates, or history. Stale facts stay marked as legacy until the owner updates them.
