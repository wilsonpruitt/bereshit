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

**State: K10, K1, K8, K6, K5, K4 and K9 built (2026-09-05). Next up is K3 `elohim-and-trinity`, row 8.**

To start that session, paste: *"Build the crux `elohim-and-trinity` in ~/bereshit, following the
per-crux checklist in PHASES.md."* Much of K3's material has already been read and flagged in
`notes/cross-crux.md` with its locus: b. Megillah 9a (on disk, unpulled into any crux — the changes
the elders made for Ptolemy, beginning with the reversal of *bereshit bara Elohim*), BR 1:12 (R.
Yudan in the name of Akilas: the King acts first and names himself after), Bruno PL 164:157B
(*habes ergo Deum, id est Patrem; habes et principium, id est Filium*, on *Faciamus hominem*),
Augustine *Conf.* XIII.5 (PL 32:847), `aug-gnl-1-5-11` (K7) and `glossa-1-2-ruach` (K7), both of
which already carry `elohim-and-trinity` in their facets and will be folded into the roster by
build-crux.py, and Rupert's whole design (the Trinity works at every *dixit … fecit … vidit*, PL
167:230A, which K9 read and did not build).

⚠ **K3 is on Gen 1:1–1:2, the two most crowded verses on the site** — K1 built 34 witnesses on 1:1
and K7, K6 and K4 have taken most of 1:2. `scripts/overlap.py` by OFFSET before every slice, and for
the rabbinic bench `grep -l '<distinctive phrase>' data/witnesses/*.json`, which is what caught K8's
over-long BR 3:6 slice while K9 was being built (see notes/cross-crux.md). Expect to lose several
candidates to K1 and to leave them for Phase 4.

⚠ **Run the renderers with `python3` (3.14 on this machine), not `python3.11`**: `render-daf.py`
uses backslashes inside f-string expressions and raises a `SyntaxError` under 3.11 that reads like
a corrupt file. ⚠ **Check the witness id you are about to write does not already exist** for another
verse: K7's `rabanus-gen-1-1` is on Gen 1:2, and `build-crux.py` overwrites without warning.

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
| 8 | K3 `elohim-and-trinity` | Megillah 9a; Rupert's whole design; much already tagged from K7 | 12–15 |
| 9 | K2 `why-begin-here` | Rashi's R. Yitzchak; Ambrose I.1; prologues; smallest | 8–12 |

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

## Phase 3 — English review · **Wilson**, with **Opus** as second reader

- Wilson revises every `claude-draft` passage or approves it as is; set `translator` and clear `status`.
- An Opus pass afterward checks each approved passage against the frozen renderings above and flags drift (does not rewrite).
- The Glossa English keeps `translator: wilson-pruitt`; Wilson sets its licence in `data/licenses.json` (`wroot-glossa`).

## Phase 4 — Cross-crux pass · **Opus** · 1 session

Merge `notes/cross-crux.md`: edges between witnesses in different cruxes, witnesses that belong to more cruxes than tagged, duplicated witnesses across crux files (one witness file, many `cruxes`). Re-run `check.py` over all ten.

## Phase 5 — Astro site · **Sonnet** (Opus on second failure)

Spec is the prototype: `out/C-daf-ruach-hovering.html` is the crux view, pixel for pixel; `out/B-map-*.html` is the secondary map view; the stream (A) is retired. Build order per `PLAN.md` §7.8: crux (daf) view → dialogue view (`/dialogue/gen-1-<verse>`; use the daf grid with all cruxes' notes, crux chip on each note) → `/witnesses/<id>`, `/persons/<id>`, `/places/<id>` → colophon from `licenses.json` → Pagefind. Static JSON in, no client fetches beyond Pagefind. EB Garamond / Inter / Frank Ruhl Libre. Both themes.

## Phase 6 — Second-tier sources · **Opus** (vision work needs care)

Only after Phases 2–4: Origen/Rufinus Hom. in Gen. I (GCS Baehrens, archive.org, PD) for K1/K3; Lyra Gen 1 from the 1492 Venice *Biblia cum glossa* (transcription = vision OCR, follow `feedback_vision-ocr-discipline`); Paul of Burgos; Bonaventure II Sent. d.12–13 slices from `~/bonaventure-sentences/vol2/`; Etheridge Onkelos and Daat BR Hebrew by alternate fetch; Sefaria attribution string.

## Phase 7 — Deploy · **Haiku**

`git` push to a new Labs repo (Wilson's OK per push), Vercel project on the Labs team, Cloudflare DNS-only record for the subdomain Wilson names (open decision §9.1), production deploy on Wilson's per-action OK.

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
