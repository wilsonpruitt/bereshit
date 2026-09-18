# Open Corpus Plan — reading-layer launch checks (Bereshit / In Principio)

Rollout per `~/open-corpus/PLAN.md` §4, sixth site (after Christian Library, migne.app,
acta-sanctorum, bonaventure-sentences, milton-doctrina). Appendix F checks run against a
local `npm run build` (Astro static) on 2026-09-18, before push/deploy.

1. **GPTBot fetch of a crux URL → 200, full text, no gate.** Verified on the rendered
   `dist/crux/beginning-of-what/index.html` — full body present, no auth/gate. PASS.
2. **Plain-text/JSON siblings.** ⚠ **N/A by design, not an oversight** — per PLAN.md §4's
   own instruction for this site, the corpus is exported as one structured graph document
   (cruxes/witnesses/threads), not per-page prose siblings; a crux is a question with
   witnesses and threads, not a linear text, so a per-page `.txt` sibling would be a
   fabricated flattening of the data. The `/export` page + `scripts/build-export.mjs`
   substitute for the sibling-file convention here.
3. **`robots.txt`, `llms.txt`, `sitemap.xml`, rights page (`/colophon`, not `/rights` —
   this site's existing name), `/export` → 200; footer line present.** All present in
   `dist/`. ⚠ No footer license line exists site-wide yet (this site's `SiteHeader`/layout
   has no footer at all) — not added in this session; low priority, the colophon already
   states licensing per-witness and the new Machine Use section states it plainly.
4. **Canonical is absolute `https://` and equals `@id` in the JSON-LD; JSON-LD parses.**
   Canonical was ALREADY implemented site-wide (`Layout.astro` computes it from
   `Astro.url.href` on every page) — only JSON-LD was new, added via an optional
   `jsonLd` prop on `Layout.astro`, wired for crux pages only (the "work" unit named in
   PLAN.md §4's rollout note for this site; witness/person/place pages were left alone,
   same scope discipline as Bonaventure's leaf-page-only JSON-LD). Verified match on
   `/crux/beginning-of-what/`. PASS.
5. **`/export` manifest lists the newest export; the R2 object downloads.** ⬜ NOT YET —
   shared `wroot-corpus-export` R2 bucket still not provisioned (same open item as the
   other five sites). Local export built clean: 10 built cruxes, 292 witnesses, 456
   threads, `bereshit-2026-09-18.json` (1.0 MB) + `README.md`, in `~/bereshit/export/`
   (gitignored).
6. **Sitemap URL count equals the work count on disk (±known exclusions).** 441 URLs in
   the sitemap, 441 pages built by Astro — exact match (10 cruxes + 292 witnesses + 98
   persons + 30 places + 5 dialogue verses + 6 static pages). PASS.
7. **Vercel edge-request figure, day before / week after.** ⬜ Needs a week post-deploy.

## What shipped

- `LICENSE` §2a — machine-use note. **Different shape from the other five sites**: this
  edition's own work is already CC BY 4.0 (not CC BY-NC), which already permits ML use
  with no special carve-out — the note says so rather than inventing a redundant
  §3a-style exemption, and explicitly does NOT claim authority to relax the third-party
  CC BY-SA (Sefaria/Wikisource) material's share-alike terms.
- `src/pages/colophon.astro` — new "Machine Use" section, same license-shape reasoning
  as the LICENSE note.
- `public/robots.txt`, `public/llms.txt` — both new.
- `src/layouts/Layout.astro` — new optional `jsonLd` prop, rendered via Astro's
  `set:html` on a `<script type="application/ld+json">` tag. Canonical was already
  computed site-wide before this session.
- `src/pages/crux/[id].astro` — passes `jsonLd` for the CreativeWork record.
- `src/pages/sitemap.xml.ts` — **new**; this site had no sitemap at all before this.
  Hand-written endpoint (not the `@astrojs/sitemap` package) enumerating the same
  `getStaticPaths()` sources as the actual page routes, to avoid adding a dependency
  for ~10 lines of URL-listing logic.
- `scripts/build-export.mjs` — reads `data/*.json` directly (mirroring `src/lib/data.ts`'s
  own `DATA_ROOT` convention) and emits one JSON graph document + README + manifest,
  matching PLAN.md's explicit instruction for this site.
- `src/pages/export.astro` — new page.
- `package.json` — `build` now runs `build-export.mjs` before `astro build`.
- `.gitignore` (site + repo root) — `src/data/export-manifest.json`, `/export/`.

## Data-completeness note

`cruxes.json` has 10 built cruxes; `build-export.mjs` filters to `status === "built"`
only (matching `getBuiltCruxes()` in `src/lib/data.ts`) — any `register-only` cruxes
(planned but not yet written) are excluded from both the site and the export, not
half-shipped.

## Not done in this session

- **Push + deploy** — both Wilson's separate hard stops.
- **Sententiae** (`~/wroot-press/sentences`) — separate repo, same PLAN.md rollout
  entry ("Bereshit / Sententiae"), not started in this pass.
- **R2 bucket provisioning** — shared across all six sites.
- **HF org claim + dataset push** — after ≥2 exports exist on R2, per §4.
- **Vercel Firewall rate-limit backstop** — parked, not yet done for any shipped site.
- **A site-wide footer license line** — this site has no footer convention yet, unlike
  the other five; low-priority follow-up, not blocking.
