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
- `src/` currently holds an identical copy of `legacy/` as the v3 working directory.
- **Undecided / open facts (owner must supply; do not invent):** current rank of Cristian Lugani (legacy says 2nd Dan, 2001), current schedule, current phone/email, any post-2001 news or activity. Until supplied, legacy values are the record and must not be embellished.

## Brand Commitments

- Name and identity bind to: **Kyudokan** (the school), **Higa family lineage**, **Cristian Lugani** (sensei), **Campana, Argentina** (location).
- Kanji calligraphy images exist in legacy assets (karate-do, makoto/sinceridad, shin, hara, fudochi, kyu-shin-ryu, do) and are candidate authentic assets.
- The 2001 visual identity (black/red base GIFs, shisa lion guardians, gold engraved nav buttons) is historical evidence, not a binding commitment — v3 replaces it.

## Evidence on Hand

- `legacy/` — complete 2001 site: all text content and ~250 pages.
- `legacy/assets/images/` — photo archive: portraits of the Higa masters (Yuchoku, Jintatsu, Minoru, Oscar, Benito), Chibana Chosin, Cristian Lugani; kanji calligraphy; and small content thumbnails in `assets/images/autogen/`.
- **Known gap:** the gallery pages (`legacy/html/fotos_*.html`, afiches) reference ~66 full-size photos (`assets/images/*.JPG`, posters, tournament photos) that are **not present** in the copied archive — only 13 files (772K) survived the 2001-era scrape. The gallery pages are broken until those files are recovered (original server or Wayback Machine). Do not substitute stock imagery for them (PRODUCT principle: no stock).
- `resources/` — **new assets supplied by the owner** (2025): larger master portraits (`Higa_Yuchoku_-_photo.jpg` 256×390, `jintatsu_higa.jpg` 297×400, `minoru.jpg`), vertical calligraphy scrolls (`kyudokan_1/2.jpg` 932×2200 極道館, `mugen.jpg` 526×2218 究道無限), Shuri castle illustration set (AI-generated styles), school emblem, favicons (`favicon_io/`). The home now uses the portraits, scrolls, castle (labeled «ilustración») and favicons via `src/assets/images/nuevas/` + `src/assets/favicon/`. Unused-but-available: `dojo-campana.webp` (dōjō lettering), emblem patch, enso-with-bell (鐘 Campana pun — not used: enso is a banned cliché).
- Absence that future work must not fabricate: no testimonials, no current news, no verified credentials beyond the legacy record.

## Product Principles

1. **Lineage is credibility.** The Higa-family chain, Okinawan roots, and documented history are the core proof; they must stay prominent and accurate.
2. **The archive is an asset.** Two decades of photographed activity survive the redesign; a full redesign may not orphan or discard it silently.
3. **Recruitment is the front door.** A prospect must find who, what, where, when, and how to start within the first viewport or two.
4. **Sober truth over embellishment.** A traditional school speaks with restraint; never invent credentials, testimonials, dates, or history. Stale facts stay marked as legacy until the owner updates them.
