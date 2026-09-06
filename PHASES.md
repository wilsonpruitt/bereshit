# PHASES.md — Bereshit / In Principio, from K7 to launch

Written 2026-09-05 at the end of the Fable pilot session. This is the score; cheaper sessions play it.
Rule of thumb from the model-prudence rubric: **no crux build, translation draft, or site page is Fable work.**
Fable returns only for the items in Phase 7, or when Opus has failed twice on one specific problem.

State when written: `~/bereshit` scaffolded (no git yet). K7 `ruach-hovering` built end to end: 30 witnesses,
33 threads, three prototypes, **C (daf) chosen**. Glossa on Genesis finished and wired in. Nine cruxes remain.

---

## Frozen conventions (do not re-decide in later sessions)

### Data
- Schema is `PLAN.md` §4 exactly, plus two facets added in the pilot: `answers` (ids from `data/answers.json`, one file per crux family set) and `senses` (`literal | allegorical | spiritual | translation`). Every witness carries both.
- One witness = one continuous argument on the verse from one work. A work may yield several witnesses (Augustine has five on 1:2). Never merge distinct arguments to save a card.
- **The anchor rule, as widened by Wilson 2026-09-05 (Phase 6 session).** A witness is normally
  anchored on a verse it comments on. **A witness may also be anchored on a verse it does not quote
  when its subject is whether that verse may be expounded.** Nothing else bends: this licenses texts
  *about the act of expounding*, not texts merely adjacent in topic. Consequences, both intended:
  K2's four non-comment witnesses (m. Chagigah 2:1, Hugh's and Comestor's prologues) **stand**, and
  Gen 1:26 *Faciamus hominem* is **admissible in K3**, where most of the Latin material on divine
  plurality actually sits. Every witness admitted under this clause keeps a visible `⚠ Anchor note`
  in its `notes`, so a reader can see the edition bending its own rule and why.
- Latin is **sliced from the local TEI by anchor phrase** (`~/patrologia/sources/pl/tei/<idno>.xml`; ids in `data/latin-bench.json`). Never retype Latin. PL column is computed from the last `<pb>` before the start anchor. If an anchor fails, fix the anchor; do not paste text.
- Rabbinic text comes from `raw/sefaria/*.json` pulled by `scripts/pull-sefaria.py`, using only the versions pinned there (Wikisource Bavli CC BY-SA; Sefaria Midrash Rabbah 2022 CC BY; Silbermann Rashi PD; Etheridge PD; Guggenheimer Yerushalmi CC BY; Berman Tanchuma CC BY). Davidson/Steinsaltz is never embedded.
- Edges need `evidence` quoting the words that prove the dependency. A shared image without a citation is `parallel`. Direction later → earlier except `transmits`. When a witness names its source (`HIERON.`, `AUG.`), that is `cites`; verbatim reuse without a name is `echoes`.
- Compilations carry a range and a precision flag (`compilation-1110-1130`, `redaction-500-600`), never a fake year.
- Every English passage has a non-empty `translator`; fresh drafts are `claude-draft` with `status: draft-awaiting-approval` until Wilson approves, then `wilson-pruitt` (revised) or `claude-draft-approved`.

### English register for fresh drafts (Latin bench)
- Plain, literal, unhurried; keep the Latin sentence order where English allows. No archaism, no "thee."
- Fixed renderings: *ferebatur / superferebatur* = "was borne over / above"; *fovebat* = "was warming"; *incubabat* = "was brooding"; *vivificare* = "quicken"; *artifex / faber* = "craftsman"; *voluntas artificis* = "the will of a craftsman"; *informis materia* = "formless matter"; *inanis et vacua* = "empty and void"; *per spatia locorum* = "across spaces of place".
- Quote the Vulgate lemma in single quotes as the witness quotes it; keep *Spiritus Domini* vs *Spiritus Dei* as the witness has it (it is evidence).
- Scripture references in parentheses, modern numbering; add Vulgate numbering only where it differs (Ps 104:30 [Vg 103]).
- Mark elisions in the English with `[…]` and say in `notes` what was elided; the Latin excerpt is always continuous.
- Added for K10 (extends the list, does not re-decide it): *dies unus* = "one day" and never "the first day"; *dies primus* = "first day"; *vespera / vespere* = "evening", *mane* = "morning", *aurora* = "dawn"; *dies naturalis / artificialis* = "natural / artificial day"; *circuitus* = "circuit"; *cognitio matutina et vespertina* = "morning and evening knowledge"; *creavit omnia simul* = "he created all things at once"; *relativa* = "relatives"; *senarius dierum* = "a senary of days".

### English register for fresh drafts (rabbinic bench)
- "Our rabbis taught" for *tanu rabbanan*; "as it is said" for *she-ne'emar*; "as it is written" for *di-khtiv*; "the Holy One, blessed be He"; in targums the Tetragrammaton is "the LORD"; *min qodam* = "from before".
- Transliteration: merahefet, tohu va-vohu, Bereshit, ruach; ḥ for ח, no other diacritics.
- Tradents named as in the text (Rav Aḥa bar Yaakov, Mar Zutra); add `tradents` to the witness.
- Added for K10: *yom echad* = "one day", *yom rishon* = "first day", *yachid be-olamo* = "alone in his world"; "the work of creation" for *ma'aseh bereshit*; "it is taught" for *tanya*; "our rabbis taught" for *tanu rabbanan* (as above).

### Crux files
- Questions in three languages (`en`, `la`, `he`) as in `data/cruxes.json`; the Latin and Hebrew forms are the medieval question, not a translation of the English.
- `summary` = why it is a crux; `finding` = what the built data showed that the plan did not know. Write `finding` only after the threads exist.

---

## Phase 1 — Generalize the pipeline · **Sonnet** · ~1 session — **DONE 2026-09-05**

Built as specified, plus four things the spec did not name: `scripts/bench.py` (the shared TEI
slicer / Sefaria loader, imported by every crux spec), `scripts/grep-bench.py` (seeds a crux by
searching the bench TEI for lemma words and printing hits with computed PL columns — the
checklist's step 3, now one command), `scripts/indexpage.py`, and two extra fields in the
spec-file contract added while building K10: **ANSWERS** and **LICENSES** (merged like
PERSONS/PLACES, so a crux spec is self-contained) and **SHORT** (the crux's display name, which
removed the last K7 hardcoding from the renderers). `check.py` has six checks, not three: the
sixth (answer ids and licence keys must resolve) caught a real K7 licence-key bug on its first run.

File paths and the pattern are given, so this is Tier-1 work.

1. Turn `scripts/build-k7.py` into `scripts/build-crux.py <crux-id>` reading a per-crux spec file `cruxes/<id>.py` (witness dicts + threads, same shape as K7). Keep the TEI slicer, the Sefaria loader, the answers-merge, and the column computation unchanged.
2. `scripts/render-daf.py` and `render-map.py` already take a crux id; make them iterate all built cruxes and write an `out/index.html` listing them.
3. Add `scripts/check.py`: every thread endpoint exists; every witness in a crux has that crux in its `cruxes`; no `claude-draft` without `status`; no licence `check` in a witness marked `ships: true`; anchors resolve.
4. `git init`, first commit (**ask Wilson before pushing anywhere**).

Done when: `python3 scripts/build-crux.py ruach-hovering` reproduces today's K7 byte-for-byte and `check.py` is clean.

## Phase 2 — Build the nine remaining cruxes · **Opus**, one crux per session

**STATE: PHASES 1–5 COMPLETE (2026-09-05). All ten cruxes built, the cross-crux pass merged, and the English approved. **235 witnesses, 321 threads, `check.py` clean, ten dafs rendered, 176 passages at `claude-draft-approved`, 0 drafts outstanding.** **Phase 5 is done too.** `~/bereshit/site` is a working Astro static site: 363 pages (10 crux dafs, 5 dialogue pages, 235 witnesses, 84 persons, 26 places, colophon, search, index), `npm run build` succeeds clean (`astro check`: 0 errors), Pagefind indexed. The crux daf is byte-identical in rendered text to the Python prototype (`out/C-daf-*.html`); the dialogue view, witness/person/place pages, and colophon are new. **Next is Phase 6 (second-tier sources, Opus).**

Phase 2 is finished; nothing further starts from this section. The per-crux checklist below stands as the record of how the ten were built, and Phase 6 will use it again for the second-tier sources.

Order chosen by how much rabbinic material each has and how much it teaches the next one:

| # | crux | why this order | expected witnesses |
|---|---|---|---|
| ~~1~~ | ~~K10 `one-day-evening-first`~~ | **BUILT 2026-09-05** — 28 witnesses, 34 threads | 20–25 |
| ~~2~~ | ~~K1 `beginning-of-what`~~ | **BUILT 2026-09-05** — 34 witnesses, 44 threads | 25–30 |
| ~~3~~ | ~~K8 `first-light`~~ | **BUILT 2026-09-05** — 27 witnesses, 35 threads | 20–25 |
| ~~4~~ | ~~K6 `tohu-vabohu`~~ | **BUILT 2026-09-05** — 25 new witnesses (32 on the daf with K7's), 28 threads | 15–20 |
| ~~5~~ | ~~K5 `heaven-earth-order`~~ | **BUILT 2026-09-05** — 17 new witnesses (19 on the daf), 20 threads | 15–20 |
| ~~6~~ | ~~K4 `ex-nihilo-or-matter`~~ | **BUILT 2026-09-05** — 19 new witnesses (22 on the daf), 25 threads | 15–20 |
| ~~7~~ | ~~K9 `good-and-separated`~~ | **BUILT 2026-09-05** — 32 witnesses, 45 threads | 12–15 |
| ~~8~~ | ~~K3 `elohim-and-trinity`~~ | **BUILT 2026-09-05** — 13 new witnesses (20 on the daf), 25 threads | 12–15 |
| ~~9~~ | ~~K2 `why-begin-here`~~ | **BUILT 2026-09-05** — 10 witnesses, 15 threads; smallest, as predicted | 8–12 |

Per-crux checklist (paste into the Opus prompt):
1. Read `PLAN.md` §5 entry, this file's conventions, and `notes/SOURCES-FINDINGS.md`.
2. Rabbinic: read the pulled JSON for the loci listed; add pulls to `pull-sefaria.py` only for refs not yet on disk.
3. Latin: grep the bench TEI for the crux's lemma words (as `build-k7.py` was seeded by grepping *incubabat / fovebat / superferebatur*); list hits with columns; keep only continuous arguments on the verse.
4. Write `cruxes/<id>.py`; run `build-crux.py`; run `check.py`; render the daf; read the daf once.
5. Fill `finding` last. Log anything the plan got wrong in `notes/SOURCES-FINDINGS.md`.
6. Do **not** revise K7 or another crux's threads while building this one; note cross-crux edges in `notes/cross-crux.md` for the Phase 4 pass.

Escalate to Fable only if: a crux needs a new edge type, a new facet, or a witness that does not fit "one continuous argument".

**Added for K1** (extends the frozen renderings, does not re-decide them): *in principio /
initium* = "in the beginning", and *Principium* is capitalised only where it names the Son;
*creavit* = "created" and *fecit* = "made", kept apart, because which one a witness quotes says
which Latin text he had; Aquila's *in capitulo* = "in the head", so that Jerome's pun on *caput
librorum* and Ps 40:8's *in capite libri* survives; *vitium in superfluitate dictionis* = "a vice of
superfluity of expression"; *aeternus* = "eternal" but *sempiternus* = "everlasting" (Comestor
needs both in one sentence); *hyle* = "hyle"; *materia informis* = "formless matter" as at K7.
**[Corrected 2026-09-05, Wilson's ruling: this line originally read "unformed matter", which K7 does
not say. See the K4 note below and the Phase 3 list.]**
Rabbinic: *reshit*, *bereshit*, *amon*, *uman*, *be-ḥokhmah*, *ḥalla* transliterated; "the Holy One,
blessed be He"; Prov 8:22 rendered as the witness quotes it, "the Lord made me reshit of his way".

**Added for K4** (extends the frozen renderings, does not re-decide them): *de nihilo / ex nihilo* =
"out of nothing"; *praejacens materia* = "pre-existing matter"; *creare* = "create" and *formare* =
"form", kept rigidly apart, because the whole crux is about the difference; *opifex* = "workman",
against the frozen *artifex / faber* = "craftsman", so that Hugh's three principles (*opifex,
materia, forma*) and Augustine's *fabros et quoslibet opifices* stay distinguishable; *coaeternus* =
"coeternal" but *coaevus* = "coeval"; *species* = "form" where it is opposed to *materia* (Basil,
Abelard); *prope nihil* = "near to nothing"; *schema / figura* = "figure". ⚠ **"unformed matter" is struck** (Wilson's ruling,
2026-09-05): K7 froze *informis materia* = "formless matter"; the K1 addendum wrote "unformed
matter" and cited K7 for it, which K7 does not say, and K6 then propagated it citing K1. Both lines
are corrected above. **This is not cost-free**: the built English is 23 occurrences of "formless
matter" across 13 witnesses against 6 of "unformed matter" across 4, so striking the line leaves
four witnesses in drift. **Phase 3 must fix `glossa-1-1` (K1), `angelom-gen-1-2-tohu` and
`glossa-1-2-terra` (K6)** — all three are `claude-draft`, so this is a draft revision, not a
retranslation. **`bonaventure-sent-2-13-1-1` is Wilson's own English and is not to be touched
mechanically**; if it stays as it is, that is a deliberate exception and should be said so in the
colophon. Rabbinic: *yesh me-ayin* = "something from nothing", *afisah muchletet* = "absolute
non-existence", *hiyuli* transliterated "hyly" as Chavel has it where the English is Chavel's and
"hyle" in the editorial prose.

**Slicing vocalized Hebrew by anchor needs a skeleton match.** Sefaria's pointed text and any
anchor phrase retyped through a terminal differ in combining-mark order, so `str.find` fails on a
phrase that is plainly there. `cruxes/beginning-of-what.py` carries a `_cut` helper that strips
U+0591–U+05C7, matches on the consonants, and maps the offsets back. Lift it into `bench.py` when a
third crux needs it.

**Burn, measured on K10 (Opus, 2026-09-05): ~170K tokens of context for the whole crux** —
survey, extraction, 28 English drafts, 34 threads, the daf read, and the notes. That is inside the
150–250K estimate and at its low end, and K10 was chosen as the *richest* of the nine, so the
remaining eight should not exceed it. Two things held the number down and are worth repeating:
`grep-bench.py` replaced hand-reading TEI files, and every rabbinic locus K10 needed was already on
disk except one (Chullin 83a). A crux needing several new Sefaria pulls or vision work will cost more.

What actually took the time was not extraction but **deciding the roster** — the bench yielded far
more than 25 usable witnesses and the pruning is a judgement call each time. Budget for that.

## Phase 3 — English review · **DONE 2026-09-05**

Wilson approved the whole body of fresh English as it stood. `bench.py` now carries **`APPROVED`**
alongside `DRAFT`; all 176 passages are `translator: "claude-draft-approved"` with no status, and
`DRAFT` remains for anything drafted from here (Phase 6). The second-reader pass was run **before**
the flip rather than after, on the reasoning that approving unread drift defeats the purpose, and it
found six real violations of the frozen renderings — all in drafts, all fixed: *informis materia*
rendered "unformed matter" (`angelom-gen-1-2-tohu`, `glossa-1-1`); *invisibilis et incomposita*
rendered "invisible and unformed" instead of "unordered" (`aug-civ-11-32`, `aug-gnl-1-5-11`); and a
creature's *conversio* to its Creator rendered "conversion" instead of "turning" (`aug-gnl-1-5-11`,
`aug-gnl-1-3`). `bonaventure-sent-2-13-1-1` is Wilson's own English and was left untouched, as ruled.
`glossa-1-2-terra`, named in the original drift list, turned out clean.

**Still open and still Wilson's**: the Glossa English keeps `translator: wilson-pruitt` and its
licence key `wroot-glossa` is unset in `data/licenses.json`, as are `wroot-bonaventure` and
`chavel-ramban`. No witness is marked `ships: true`, so `check.py` does not yet enforce them.

✅ **RESOLVED 2026-09-05 (Wilson's ruling, Phase 6 session): *operator* = "worker".** It had been
rendered "workman" at `ambrose-hex-1-3` (*quam incomparabilis operator esset*) and `ambrose-hex-1-5`
(*dum opus videtur, praefertur operator*), colliding with the frozen *opifex* = "workman" (K4).
"workman" is now reserved for *opifex* alone. Changed in the spec files and rebuilt: two witness
passages, one `lemma.en`, two thread evidences, one crux-prose paragraph, and the answer label
`the-work-shows-the-maker` ("The work shows the worker"). The three surviving "workman"s in the
built English are all *opifex/opifici* — `comestor-hs-1-1c`, `hugh-sacr-1-1-nihilo`,
`remigius-gen-1-1` — and were verified against their Latin before the change, not assumed.
*artifex/faber* = "craftsman" is untouched.

## Phase 4 — Cross-crux pass · **DONE 2026-09-05**

Run as part of the same session. 16 facet edits, 17 new threads, 1 slice repair, all made in the
`cruxes/*.py` spec files so the merge survives a rebuild; three items deliberately not merged. The
full record is the top section of `notes/cross-crux.md`. The one structural question Phase 2 left
open — whether the graph can carry an edge between a doctrine settled at one crux and an answer
foreclosed at another, which K8, K4 and K9 each raised — is **escalated to Phase 8 as a Fable
decision**, per the standing rule that a new edge type is not a builder's call.

## Phase 5 — Astro site · **Sonnet** (Opus on second failure)

**DONE 2026-09-05.** `~/bereshit/site`, Astro 7, static output. Built in spec order: crux (daf)
view → dialogue view → witnesses/persons/places → colophon → Pagefind.

- **Crux view is pixel-for-pixel with the prototype**, verified by stripping tags from both
  `out/C-daf-ruach-hovering.html` and the Astro build's rendered output and diffing the text — the
  only differences are the two new elements added below the daf (a link to the dialogue view, the
  crux's `finding`). The CSS (`src/styles/daf.css`) and the hover/pin/wire-drawing script
  (`src/components/Daf.astro`) are direct ports of `render-daf.py`'s `<style>` and `<script>` blocks.
- **Data access is `src/lib/data.ts`**, reading `../data/*.json` relative to `process.cwd()` (not
  `import.meta.url` — Vite bundles that module to an unpredictable depth, which broke a
  path-relative-to-this-file approach on the first build attempt). No client-side fetching anywhere;
  Pagefind is the only thing that reads anything after the HTML ships.
- **The dialogue view** (`/dialogue/gen-1-<n>/`) collects every witness whose `anchor.verse` matches,
  across all ten cruxes, lays them out in the same daf grid, and gives each note a row of crux chips
  (linking to `/crux/<id>/`). Threads shown are the subset of `data/threads.json` whose *both*
  endpoints are on that verse's roster — a cross-verse thread would point off the page.
- **Colophon** groups every witness by its `original.license` and `english.license` keys against
  `data/licenses.json`, two sections (source texts, English texts), each witness linked.
- **Credit line for approved English**: Phase 3's flip to `claude-draft-approved` needed a reader-facing
  label the Python prototype never had to render (it predates the approval). `src/lib/render.ts`
  renders it as "fresh draft (Claude), approved by Wilson Pruitt" — a site-building decision, not a
  correction; flag if a different phrasing is wanted before this goes live.
- **Not built**: the secondary map view (B) — PHASES.md calls it secondary and Phase 5's order didn't
  reach it; a theme-toggle control (the CSS already supports both themes via
  `prefers-color-scheme` and a `data-theme` override, just no UI to flip it).
- `npm run build` = `astro build && pagefind --site dist`. `npm run dev` for local editing.
  EB Garamond / Inter / Frank Ruhl Libre via Google Fonts, both themes.

## Phase 6 — Second-tier sources · **Opus** (vision work needs care)

Only after Phases 2–4: Origen/Rufinus Hom. in Gen. I (GCS Baehrens, archive.org, PD) for K1/K3; Lyra Gen 1 from the 1492 Venice *Biblia cum glossa* (transcription = vision OCR, follow `feedback_vision-ocr-discipline`); Paul of Burgos; Bonaventure II Sent. d.12–13 slices from `~/bonaventure-sentences/vol2/`; Etheridge Onkelos and Daat BR Hebrew by alternate fetch; Sefaria attribution string.

## Phase 7 — Deploy · **Haiku**

**Open decision §9.1 is answered: the site is `bereshit.wrootpress.com`.** Wilson added the CNAME on
2026-09-05, ahead of the build — there is nothing to deploy until Phase 5 exists, and the repo has
never been pushed anywhere.

⚠ **The subdomain is `wrootpress.com`, not `wrootlabs.com`**, which puts the edition under the Press
imprint rather than Labs. That is a licensing and colophon fact, not only a DNS one: Wroot Press
publishes under CC BY-NC 4.0 on English and encoding with the source PD. **Confirm with Wilson
before the colophon is written** whether the site takes the Press licence, and note that this entry
previously said "Vercel project on the Labs team" — a Press subdomain served by a Labs Vercel
project is fine technically but the two should be a deliberate choice, not a leftover.

Remaining: `git` push to a new repo (Wilson's OK per push), Vercel project, Cloudflare record is
DNS-only (already added), production deploy on Wilson's per-action OK.

## Phase 8 — Fable, once

One session, after everything above: read all ten daf pages; write the editorial introduction and the ten `finding` paragraphs into a single voice; decide whether any Phase-2 view (time scrubber, lemma view, invertible centre, authority map) is worth building; rule on the "one translation, one home" question for the Glossa and Bonaventure text this site re-hosts.

**Burn, measured on K1 (Opus, 2026-09-05): ~200K tokens**, against K10's ~170K — survey, extraction,
34 witnesses with 30 fresh English drafts, 44 threads, the daf read, and the notes. Two things cost
more than K10: the roster was larger (34 against 28, because Augustine alone yields five continuous
arguments on 1:1 and Ambrose and Bruno two each), and three of the greps had to be re-run against
the raw TEI because `grep-bench.py` does not know the Glossa (its `latin-bench.json` entry still had
`idno: null` although PL 113 = TEI 8950 is on disk and K7 sliced it). **Fixed in this session**, so
K8 onward can grep the Glossa like any other work.

**Added for K8** (extends the frozen renderings): *lux / lumen* both "light", but keep *lux* and
*lumen* distinct where a witness contrasts them; *lux corporalis* = "bodily light" and *lux
spiritualis* = "spiritual light"; *diluculum* = "dawn"; *accidens* = "an accident" and *substantia*
= "a substance" (Rupert's argument is unintelligible if these are softened); *nubes lucida* =
"luminous cloud"; *vice et loco solis* = "in the sun's stead and place"; *conversio* of a creature
to its Creator = "turning", not "conversion". Rabbinic: *ganaz* = "stored away", *or ha-ganuz* =
"the stored light"; *tzaddikim* = "the righteous"; *le-atid lavo* = "in the time to come".

**Burn, measured on K8 (Opus, 2026-09-05): ~170K tokens.** Back to the K10 figure, and for the
reason `notes/cross-crux.md` predicted: every rabbinic locus was already on disk and had been read
once, so the session cost was the Latin survey and the drafting. The Latin side was bigger than the
table's 20–25 estimate suggested — the twelfth century alone yields six witnesses — but Latin
witnesses are cheaper than rabbinic ones, because the slicer does the work.

**Added for K6** (extends the frozen renderings, does not re-decide them). The crux turns on two
Latin texts of one clause, so both lemmas are fixed: *inanis et vacua* = "empty and void" (as at
K7) and *invisibilis et incomposita* = "invisible and unordered" — **never** "formless", which is
reserved for *informis*; *materia informis / informis materia* = "formless matter" (as at K7;
this line read "unformed matter (as at K1)" until Wilson's ruling of 2026-09-05) but
*informitas* = "formlessness"; Angelomus' *invisa* = "unseen", to keep his variant visible.
*inutilis, infructuosa et incomposita* = "useless, unfruitful, and unordered", which is **Wilson's
own wording** in the Glossa chunk and must not drift, since Remigius, the Glossa and Comestor all
carry the phrase. Further: *ornatus* = "adornment" and *exornare* = "to furnish"; *machina
mundialis* = "the world-machine"; *germen* = "shoot", *semina* = "seeds", *animantia* = "living
things"; *conjunctio adversativa* = "adversative conjunction"; *chaos* = "chaos"; *spectator* =
"beholder"; *arida* = "dry land"; *hyle* = "hyle" (as at K1). Rabbinic: *tohu va-vohu*, *toheh
u-voheh*, *reikut*, *tzadya ve-reikanya*, *betohe*, *bo hu*, *kav yarok* transliterated; "the
Holy One, blessed be He"; Rashi's Old French *estordison* is printed as the text has it. Note that
K6's rabbinic English is **all embedded and licensed** (Sefaria Midrash Rabbah, Silbermann, Chavel,
two community translations) — the fresh drafts on this crux are Latin only, and the community
translation of Ibn Ezra leaves *mefulamot* untranslated and is kept as it stands.

**Burn, measured on K6 (Opus, 2026-09-05): ~135K tokens**, the cheapest of the four so far against
K10's ~170K, K1's ~200K and K8's ~170K. Three reasons, and two of them will not repeat: every
rabbinic locus was already on disk (BR 2, Rashi, Chagigah 12a, Ibn Ezra, Ramban, the targums), the
rabbinic English needed **no drafting at all** because every text had a licensed translation, and
`grep-bench.py` on a four-alternative regex laid out the whole Latin bench — both lemmas, 87 hits
across 23 works — in one call, which is what turned "which witnesses exist" into a reading problem
rather than a search problem. **A crux whose lemma has two Latin forms should be grepped for both
in one regex from the start**; doing so is what made this crux's finding visible in the first five
minutes rather than at the end.

The roster ran over the table's 15–20 estimate (25 new, 32 on the daf) and the overrun is real
rather than sloppy: the two-text split doubles the number of Latin witnesses that say something
distinct, and Bereshit Rabbah 2 alone yields four continuous arguments on the pair. Honorius,
Rabanus and BR 2:5 were read and dropped to `notes/cross-crux.md`.

**Added for K5** (extends the frozen renderings). *coelum et terra* = "heaven and earth" (not "the
heavens"), so that the Latin pair and the Hebrew *ha-shamayim ve-et ha-aretz* stay visibly
different; *coelum empyreum* = "the empyrean heaven" and *igneum non ab ardore sed a splendore* =
"fiery not from burning but from brightness" — the qualification is the whole content of the
gloss and must not be smoothed; *firmamentum* = "the firmament"; *elementa* = "the elements" and
*levia / gravia* = "light / heavy"; *continens et contentum* = "the container and the thing
contained"; *praerogativa* = "prerogative" and *privilegio primogenitae creaturae* = "by the
privilege of being the firstborn creature"; *non ordinis sed dignitatis causa* = "not for the sake
of order but of dignity"; *universaliter … per partes* = "universally … in its parts"; *mundus
sensibilis* = "the sensible world" and *regio sublunaris* = "the region below the moon";
*microcosmus* = "microcosm". Rabbinic: *bet shammai / bet hillel* = "Beit Shammai / Beit Hillel";
*sham mayim*, *et*, *ribbuyin*, *mi'utin* transliterated; *ke-kadera ve-khisuyah* = "like a stewpot
and its lid".

**Burn, measured on K5 (Opus, 2026-09-05): ~125K tokens**, the cheapest yet — but the number is
misleading and should not be used to estimate K2 or K3. It is low because **every rabbinic text was
on disk and licensed** (as at K6) *and* because the Latin survey was short: the crux's vocabulary
(`coeli et terrae nomine`, `empyre`) is distinctive enough that two greps found the whole bench.
What K5 spent instead of survey tokens was the **K1-overlap check**, which is a fixed cost on every
remaining crux and cost about 8K here.

The overlap is the thing to plan for. Gen 1:1 already carried 34 witnesses when K5 started, and
three of eleven Latin candidates — Bruno 147B, the Glossa's VERS. 1, Rabanus 444B — were inside a
K1 slice and had to be dropped to `notes/cross-crux.md`. **K2 and K3 are both on 1:1–1:2 and will
lose more.** Neither is a reason to widen a slice or to rebuild another crux's witness: the Phase 4
pass exists for exactly this, and the cross-crux table now carries the edges it will need.

**Added for K9** (extends the frozen renderings, does not re-decide them). The crux turns on which
Latin text a witness had, so the two forms are kept rigidly apart in the English as in the Latin:
*divisit inter lucem et tenebras* = "divided between the light and the darkness" (the Old Latin,
following the Greek's doubled *ana meson*) and *divisit lucem a tenebris* = "divided the light from
the darkness" (Jerome); *discrevit* = "distinguished" and *separavit* = "separated", never levelled
to "divided"; *distinctio* = "distinction" and *divisio* = "division". Further: *privatio* =
"privation" and *absentia lucis* = "the absence of light"; **_ordinare_ = "to order" / "to set in
order", held rigidly apart from *facere* = "to make"**, because Augustine's whole answer is that God
did not make the darkness but ordered it, and any English that blurs the pair destroys the argument;
*ordinator* = "orderer"; *tenebrae* = "darkness", but "darknesses" wherever a witness counts kinds
or has *tenebrae* as a plural subject beside a plural *lux* (Hugh); *vidit … quod esset bona/bonum*
= "saw … that it was good", and *vidit* is always "saw", never "judged" or "approved" — *approbare*
= "approve" and *comprobare* = "confirm" are separate words and Ambrose uses both; *judicium* =
"judgement" and *meritum* = "merit" (Hugh's *divisit per judicium; et per meritum nominavit* = "he
divided by judgement, and by merit he named"); *lux incommutabilis / commutabilis* = "the
unchangeable / changeable light"; *informis* = "unformed" **only** in the pair *res formata ab
informi* = "the formed thing from the unformed", where "formless" would collide with the frozen
*informis materia* = "formless matter"; *umbra ex objectione corporum* = "the shadow made by bodies
set against the light"; *essentia* = "an essence". The LXX's *καλόν* is rendered "beautiful", not
"good", so that the difference from the Hebrew *ki tov* is visible on the page.
Rabbinic: *va-yavdel*, *havdala*, *havdala mamash* (= "a real separating"), *hivdilo lo* (= "he
separated it for himself"), *ki tov*, *tzaddikim*, *reshaim* transliterated where the English keeps
them; *istratigin* = "generals"; "the Holy One, blessed be He"; *le-atid lavo* = "in the time to
come" (as at K8); *ma'aseihen shel tzaddikim* = "the deeds of the righteous". Note that K9's
rabbinic English is **all embedded and licensed** — Sefaria Midrash Rabbah for BR, Chavel for
Ramban, Friedlander for Pirkei de-Rabbi Eliezer, Etheridge for Pseudo-Jonathan, a community
translation for Ibn Ezra — so the fresh drafts on this crux are Latin, Greek and Onkelos only.

**Burn, measured on K9 (Opus, 2026-09-05): ~110K tokens**, the cheapest of the seven. The reasons,
and the one that generalises, are in the K9 entry of `notes/SOURCES-FINDINGS.md`: every rabbinic
locus was on disk and most had been read at K8 or K6; the Latin survey was two `grep-bench.py` calls
plus one direct read of Alcuin, whose *Interrogationes* do not answer a lemma grep because they are
organised as questions; and **on a crux with a small, sharply distinguished set of answers the
roster prunes itself**, which is the opposite of K10's experience and worth knowing before K3 and K2
are budgeted. The roster still ran to 32 against the table's 12–15 — the fifth overrun in a row.
**The table's numbers should be read as floors, not estimates.**

**Added for K3** (extends the frozen renderings, does not re-decide them). *Trinitas* = "the
Trinity" and *trinus* = "threefold"; *personae* = "persons" and *tres personae* = "three persons",
never "three beings"; *substantia / essentia* = "substance / essence", kept apart; *consubstantialis*
= "consubstantial" and *coaeternus* = "coeternal" (as at K4); *unigenitus* = "only-begotten";
*genitus, non factus nec creatus* = "begotten, not made or created" (Remigius is quoting the creed
and the English must let the reader hear it); *principium* = "beginning" throughout, capitalised
**Principium** only where it names the Son (as frozen at K1), and *in principio sibi coaeterno* = "in
a Beginning coeternal with himself"; *expletor* = "completer" — Basil's term for the Spirit, odd and
strong, and not to be softened to "fulfiller"; *aenigma* = "riddle", never "mystery" or "figure",
because Augustine's hedge is the point; *opera Trinitatis indivisa* = "the works of the Trinity are
undivided"; *appropriare* = "ascribe" where the twelfth century distributes the works. **The Hebrew
word is transliterated as the witness has it**: Abelard's *Eloim* and *El* stay as he spells them,
Jerome's *ELOIM* likewise, and the editorial prose uses *Elohim*.
Rabbinic: *Elohim*, *eloah*, *bara* / *bare'u*, *vayomer* / *vayomeru*, *adonim*, *be'alim*
transliterated; *shtei reshuyot* = "two authorities", never "two powers", so that the midrash's own
term stays visible; "the Holy One, blessed be He"; *yechido shel olam* = "the Unique One of the
world"; Akilas kept as *Akilas* in the midrash and *Aquila* in editorial prose; the Greek loanwords
of BR 1:12 (*dimosiot*, *privtaot*, *agostoli*) are given as the Sefaria translation has them.

**Burn, measured on K3 (Opus, 2026-09-05): ~85K tokens**, the cheapest of the eight. Two reasons and
both are structural rather than lucky: **seven witnesses were already tagged with this crux by the
K7 session and came onto the roster for free**, three of them load-bearing; and the anchor rule cuts
out Gen 1:26, where most of the Latin material on divine plurality actually is, so the survey was
short because the crux is small. **The pre-tagging is the transferable lesson: when a crux reads a
passage that plainly belongs to an unbuilt crux, add the facet then rather than writing a
cross-crux row.** K3 is also the first crux to land inside the table's estimate.

**Added for K2** (extends the frozen renderings, does not re-decide them). *opus conditionis* = "the
work of foundation" and *opus restaurationis* = "the work of restoration", **never** "creation" for
*conditio*, because Hugh's whole division depends on the pair being two technical terms and not a
description; *materia* here = "matter" in the scholastic sense of subject-matter, distinct from the
*materia* = "matter" of K4 (context disambiguates and no gloss is added); *historia / allegoria /
tropologia* = "history / allegory / tropology", untranslated as school terms, with Comestor's
*annalis, kalendaria, ephimera* as "annals, calendars, day-books"; *testis* = "witness" (Ambrose on
Moses) and must not become "eyewitness"; *specimen divinae operationis* = "a specimen of the divine
working"; *simulatoriae disputationes* = "counterfeit disputations"; *ornato politoque sermone* =
"with ornate and polished speech" against *rebus manifestis* = "with plain facts"; *imperiti /
indocti* = "the less skilled / the unlearned", kept apart because Augustine uses both in one
paragraph. Rabbinic: *ma'aseh bereshit* = "the work of creation" (as at K10) and *merkavah* = "the
Chariot"; *listim* = "robbers"; *te'alamna* rendered as the Sefaria translation has it; *berakhah*
and *arirah* transliterated in the *bet*/*alef* derashah; "it were fitting for him that he had not
come into the world" for *ra'ui lo she-lo ba la-olam*, kept identical across m. Chagigah 2:1 and its
echoes so the reader can see the formula repeat.

**Burn, measured on K2 (Opus, 2026-09-05): ~70K tokens**, the cheapest of the nine, and the crux is
also the smallest — 10 witnesses against a table estimate of 8–12, the second in a row to land
inside the estimate. The survey was short because K2's Latin material is *prologues*, which are
findable by name rather than by lemma, and because the rabbinic side is four passages of Bereshit
Rabbah 1 that K1 and K4 had already read.

**Three slice defects caught at build time and worth naming, because two of them fail silently:**
(1) `latin()` takes the FIRST match of the start anchor, and Hugh's *De sacramentis* prints its
chapter titles twice — once in the table of contents at PL 176:173 and once at the chapter itself —
so the first build produced a 20,115-character witness spanning the whole table. **Use
`occurrence=1` on any work with a printed table of contents.** (2) A slice that precedes the first
`<pb>` in its TEI gets `col. ?` from `latin()`; Augustine's *De Genesi contra Manichaeos* CAPUT
PRIMUM is such a slice, and the column has to be supplied by hand. (3) The Sefaria English for
m. Chagigah 2:1 is the **William Davidson Edition**, which is NC and is never embedded on this site
(the frozen data rule names Davidson/Steinsaltz for the Bavli; it applies to the Mishnah too) — the
English there is a fresh draft from the Hebrew.
