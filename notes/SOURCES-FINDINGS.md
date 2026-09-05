# Source findings — 2026-09-05 (first session)

What the plan assumed vs. what the sources actually are. Read before extraction.

## Latin bench (all local: `~/patrologia/sources/pl/tei/<idno>.xml`, index `~/patrologia/data/cc-pl-index.json`)

Resolved ids in `data/latin-bench.json`. Every PL work on the bench is on disk. Two are not in PL at all:

- **Origen, Hom. in Gen. (Rufinus)** — PG 12, not in the PL harvest. Source separately (Baehrens GCS is PD; archive.org) or defer.
- **Claudius of Turin on Genesis** — not in PL. Drop from pilot.

Aliases: Bede *In Genesim* = "Hexaemeron (Beda)" idno 8466 · Bruno of Segni = "Bruno Astensis, Expositio in Pentateuchum" 21403 · Wigbod = "Wicbodus" 8606 · Basil = "Eustathius, Metaphrasis Latina Hexaemeri" 7608 · Rupert *In Genesim* is inside *De Trinitate* 10873 (661K words; slice the first ~150K chars).

Column anchors: the TEI `<pb n="0939A"/>` marks resolve to PL columns; `scripts/build-k7.py` computes them. Sample-check against the Migne scan before trusting (per `~/patrologia/CLAUDE.md`: Corpus Corporum departs from Migne ~3 sites/page).

## Rabbinic bench (Sefaria v3 API; pulls in `raw/sefaria/`)

Licence surprises — the plan's "Aramaic is CC0" is wrong for the Bavli:

| Work | Original | English |
|---|---|---|
| Bavli (Chag 12a, 15a, Meg 9a, RH 10b–11a) | Davidson vocalized Aramaic is **CC BY-NC**. Use **"Wikisource Talmud Bavli" (CC BY-SA)**. | Davidson/Steinsaltz NC → never embed. "Sefaria Community Translation" is CC0 but patchy (RH: 1 segment). Translate fresh. |
| Bereshit Rabbah 1–3 | Default "Midrash Rabbah -- TE" licence *unknown*; a **"Daat Bereshit Rabbah" PD** version exists but did not return by title (try per-section). | **Sefaria Midrash Rabbah 2022, CC BY** — embed with attribution. |
| Rashi Gen 1 | Silbermann Hebrew, PD | Silbermann English, PD |
| Onkelos | "Onkelos Genesis" PD | Default English is Metsudah (**NC**). Etheridge (PD) is listed but didn't return by version title; fetch from archive.org. |
| Pseudo-Jonathan | PD | Etheridge 1862 PD — returned fine |
| Neofiti | Vatican MS transcription, licence *unknown* (whole of 1:1–5 as one segment) | Community translation CC0 |
| Yerushalmi Chag 2:1 | **Guggenheimer edition + translation both CC BY** on Sefaria → **resolves open decision §9.4: include, no fresh translation needed.** Verify the licence claim on Sefaria's version page. | |
| Mishnah Chag 2:1 | Torat Emet PD | default English is Davidson NC; use Kulp or translate |
| PdRE 3 | PD | Friedlander 1916 PD |
| Tanchuma Bereshit 1 | ref is `Midrash_Tanchuma,_Bereshit.1` (comma). Torat Emet PD | Berman **CC BY** (plan feared NC — it isn't) |
| Ibn Ezra Gen 1 | Piotrkow 1907 PD | Community CC0 (14 of 18 segs); Strickman–Silver is NC |
| Ramban Gen 1 | Vocalized ed. CC BY | **Chavel shows as CC BY on Sefaria** — surprising for a 1971 Shilo text; verify before embedding, else fresh. |
| Gen 1:1–5 Hebrew | Miqra according to the Masorah, CC BY-SA | JPS gender-sensitive is NC → use WEB (pulled, `raw/web-gen-1-1-5.json`). **WEB prints 1:5 as "the first day"** — a K10 datum. |

## K7 (ruach-hovering) — what extraction found that the plan didn't list

- **Rupert of Deutz** has the warmed egg (PL 167:205C) with no Syrian — image already naturalized.
- **Wigbod** quotes Jerome verbatim under the label HIERONYMUS (96:1116C) and Augustine Gnm (96:1112D): a Carolingian catena showing both Latin lines side by side.
- **Angelomus** splices Augustine's "non localiter sed potentialiter" onto Jerome's bird, unnamed, as "alia translatio" (115:116A).
- **Abelard** reports "Hebraicum habet volitabat" (178:735B) — against Jerome's incubabat and on the rabbinic side of the verb. Source unknown [CHECK].
- **Comestor** fuses Jerome's Hebrew + Basil's Syriac and turns the bird against Plato's world-soul (198:1057A).
- **Rashi's la'az acoveter** = Jerome's incubabat. Same vernacular sense, no contact.
- **Rashi's dove** is the Bavli's (yonah, Chag 15a), not BR 2:4's unspecified bird — settles the `cites` edge.
- **Bede has no bird** on 1:2; Trinitarian only (K3). Rabanus copies him verbatim (107:447C).
- Hugh *De sacramentis* and Rupert `fovebat` grep hits were false positives; Hugh's 1:2 is in the *Adnotationes* (175:36A).

## Still open

- Glossa on Gen 1:2 — Wilson's edition in progress; slot `glossa-1-2-ruach` reserved.
- Etheridge Onkelos, Daat BR Hebrew: fetch by alternate route.
- Sefaria attribution string for Midrash Rabbah: paste exact text into `data/licenses.json`.
- Bonaventure II Sent. d.12–13 files: `~/bonaventure-sentences/vol2/bon-sent-II-d12-*.md`, `-d13-*.md` (K4/K8/K10, not K7).
