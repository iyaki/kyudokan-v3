# Repository Guidelines

## Project Overview

Official v3 site of the **Centro de Enseñanza de Karate Do — Estilo Shorinryu Kyudokan de Okinawa** (Filial Campana, Argentina). A full redesign of the 2001 site with the visual world «Gusuku» (Okinawan castle walls, tejas, mar Kerama). Content is Spanish, preserved verbatim from the 2001 legacy site.

- **Stack**: Eleventy 3 (Liquid templates) over plain HTML/CSS — no JS framework, no CSS framework
- **Sole runtime dependency**: `@11ty/eleventy` ^3.1.6; Python 3 for tooling scripts

## Architecture & Data Flow

```
src/*.html ──(front matter: layout/title/section)──▶ src/_includes/base.html
                                                        │  riel nav from src/_data/riel.json
                                                        │  aria-current = item.label == page.section
src/assets/, src/gusuku.css ──(passthrough copy)──────┐ │
                                                      ▼ ▼
                                              npm run build → _site/
                                              URL scheme: /foo/ → foo/index.html
```

- **20 content pages**: front matter + `<main>` content only; shell (head, masthead, riel, footer, scripts) lives entirely in the layout.
- **4 whole-document pages** (ex-`.shtml`: `nacionales`, `internacionales`, `institucion`, `todas_las_notic_`): complete HTML documents with their own shell, no `layout` front matter. They render as-is through Liquid.
- **Directory URLs everywhere**: Eleventy defaults (no permalink overrides). Internal links are root-absolute extensionless (`/presentacion/`, `/` for home); asset refs are root-absolute (`/assets/...`, `/gusuku.css`). Relative asset paths break from directory URLs — always use leading `/`.
- `page.url` normalization: Eleventy strips `/index.html` → `/`; `section` front matter (a riel label like `"Historia"`) drives `aria-current`, not URL comparison.

## Key Directories

| Directory | Purpose |
|---|---|
| `src/` | Eleventy input. All 24 page templates at root level (flat, no subdirs) |
| `src/_includes/` | `base.html` — the single shared shell/layout |
| `src/_data/` | `riel.json` — the 8-entry navigation array consumed by the layout loop |
| `src/assets/` | Fonts, favicon, marca (shisas, crest), fotos, texturas — passthrough-copied verbatim |
| `legacy/` | **Pristine 2001 site (ISO-8859-1), read-only reference — never edit** |
| `tools/` | Python scripts: 1 daily checker + historical one-shots |
| `.impeccable/` | Design system: `config.json` (detector ignores), `design.json` (Gusuku tokens), `surfaces/` |
| `resources/` | Recovered external assets (Koyu Higa portrait) — gitignored |

## Development Commands

```bash
npm run build              # rm -rf _site && eleventy → _site/
npm run serve              # dev server with watch (Eleventy built-in)
python3 tools/check_links.py   # verify all local href/src in src/*.html resolve (exit 1 on broken)
python3 tools/texturas_gusuku.py   # regenerate procedural wall textures → src/assets/texturas/
```

QA pattern (no CI yet): build → serve `_site/` with a static server → crawl all pages for broken refs → browser smoke (desktop + mobile).

## Code Conventions & Common Patterns

**Content fidelity rules (non-negotiable, see PRODUCT.md):**
- 2001 body text is preserved verbatim; only orthographic fixes via `ORTO_FIXES` in `tools/restyle.py` — never reword prose
- Missing photos render as honest `.falta` cartelas naming the original file — never fabricate images
- Never invent credentials, testimonials, dates, or news; undecided facts (schedule, phone) stay as legacy values until the owner supplies them

**Templates:**
- Front matter keys: `layout: base.html`, `title` (full `<title>` verbatim), `section` (optional riel label → `aria-current`), `description` (optional, index only)
- Liquid in page content is incidental — never introduce `{{`/`{%` in content
- New pages: create `src/foo.html` with front matter; URL becomes `/foo/` automatically; add inbound links (riel.json or footer in `base.html` or a subnav) or the page is an orphan

**CSS:** single `src/gusuku.css`, custom properties (`--teja`, `--mar`, `--tinta`, ...), BEM-ish Spanish class names (`pagina-titulo`, `sitemap-col`). Tokens of record in `.impeccable/design.json`.

**Style:** ESM everywhere; tabs in JS/JSON tooling; Spanish for all content, comments, and commit messages.

## Important Files

| File | Role |
|---|---|
| `.eleventy.js` | Input dir `src/`, passthrough `assets/` + `gusuku.css` |
| `src/_includes/base.html` | Shared shell — head, masthead, riel loop, footer sitemap, laminas/riel scripts |
| `src/_data/riel.json` | Navigation source of truth (8 entries, root-absolute URLs) |
| `src/gusuku.css` | The stylesheet (only one) |
| `PRODUCT.md` | Product record: users, constraints, fidelity rules, undecided facts — **read before content work** |
| `DESIGN.md` + `.impeccable/design.json` | Gusuku world rules and tokens — **read before design work** |
| `tools/check_links.py` | The daily verifier |
| `tools/restyle.py`, `tools/to_11ty.py` | **Historical one-shots — never re-run against `src/`** (they predate/consume the template form) |

## Runtime/Tooling Preferences

| Requirement | Value |
|---|---|
| Node | 24 (`engines.node`) |
| Package manager | npm (no lockfile preferences beyond package-lock.json) |
| Module system | ESM (`"type": "module"`) |
| Python | 3.x, stdlib only (tools/) |
| Formatter/linter | None configured |
| Git | Trunk-based on `main`; commits in Spanish, conventional-ish imperative subjects |

## Testing & QA

- **No formal test suite and no CI** — verification is manual and scripted:
  1. `npm run build` must emit 24 directory outputs with zero warnings
  2. `python3 tools/check_links.py` — 0 broken (resolves files, `/foo/` dirs with `index.html`, and extensionless → `foo.html`)
  3. HTTP crawl of `_site/` (any static server) — all pages 200, zero broken refs
  4. Browser smoke on changed surfaces (desktop + mobile viewport)
- The impeccable hook (`.impeccable/config.json`) runs design-detector checks on edits; its ignoreValues encode approved-world exceptions — don't widen them without a DESIGN.md-backed reason.
