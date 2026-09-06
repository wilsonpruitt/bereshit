# Bereshit / In Principio — site (Phase 5)

Astro static site built from `../data/*.json`. No client fetches beyond Pagefind — everything is
read at build time (`src/lib/data.ts`, `DATA_ROOT = ../data` relative to this directory) and baked
into static HTML.

```
npm install
npm run dev      # http://localhost:4321
npm run build    # astro build && pagefind --site dist
npm run preview  # serve dist/ locally
```

## Pages

- `/` — index of the ten built cruxes
- `/crux/<id>/` — the daf view (spec: `../out/C-daf-*.html`, pixel for pixel; see `src/components/Daf.astro`)
- `/dialogue/gen-1-<n>/` — every crux's witnesses on one verse, daf grid, crux chips per note
- `/witnesses/<id>/`, `/persons/<id>/`, `/places/<id>/`
- `/colophon/` — every source and translation, grouped by licence
- `/search/` — Pagefind UI

## Design

Fonts: EB Garamond / Inter / Frank Ruhl Libre (Google Fonts, loaded in `Layout.astro`). Both light
and dark themes via `prefers-color-scheme` and a `data-theme` override (see `src/styles/daf.css`
`:root` blocks) — no toggle control is wired up yet.

## Known gaps (see PHASES.md Phase 5 note for the full list)

- The map view (Version B, `../out/B-map-*.html`) was not ported — PHASES.md calls it secondary.
- No theme-toggle UI control.
- `build-crux.py`'s witness-id collision guard (flagged at K2) is unrelated to the site and still open.
