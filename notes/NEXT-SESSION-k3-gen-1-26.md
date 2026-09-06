# Next session — Gen 1:26 *Faciamus hominem* into K3

**Model: Opus.** Estimated ~60–100K: the bench survey is already done (below), so this is roster
judgement, slicing and drafting, not discovery. Run it **before** the Lyra session, per Wilson.

---

## ⛔ READ FIRST — a blocker Wilson must clear in one line

**The anchor rule as frozen does not actually license this crux, and `check.py` will refuse it.**

Two separate problems, discovered while setting this session up:

1. **The rule text is narrower than the consequence attributed to it.** PHASES.md now says a witness
   "may be anchored on a verse it does not quote **when its subject is whether that verse may be
   expounded**", and then asserts as a consequence that Gen 1:26 is admissible in K3. That does not
   follow: *Faciamus hominem* is about divine plurality, not about whether Gen 1:1 may be expounded.
   The consequence was stated in the question Wilson answered and in the ruling as written up, but
   the rule as drafted does not carry it. **My drafting error, flagged rather than quietly widened.**
2. **`data/scripture/gen-1.json` holds only gen.1.1–gen.1.5**, and `check.py` rule 5 requires every
   `anchor.verse` to resolve there. A witness anchored `gen.1.26` fails the build today.

**Three ways out. Recommend (b).**

- **(a) Extend the scripture data to gen.1.26** and anchor the witnesses honestly on the verse they
  comment on. Cleanest logically — no rule bends at all, because they *are* comments on 1:26. Cost:
  the dialogue view is per-verse and would gain a `/dialogue/gen-1-26/` page holding only this
  material, which misrepresents the edition's scope (Gen 1:1–5) to a reader browsing verses.
- **(b) Anchor on `gen.1.2`** — where *Elohim*'s plural form already sits in K3 — with a visible
  `⚠ Anchor note` on each, under a **second and explicitly stated** widening: *a witness may be
  anchored on a verse it does not quote when it argues the same philological question that verse
  raises.* Keeps the edition's five-verse scope, keeps the daf coherent, and keeps the bending
  visible. Requires Wilson to approve the second clause, since a new rule is not a builder's call.
- **(c) Don't build it.** K3 stays as it is and the finding keeps saying the Latin material is
  mostly elsewhere. Costs the richest seam on the bench (below).

---

## The Latin survey is done: `notes/k3-gen-1-26-survey.md`

`grep-bench.py "Faciamus hominem"` gives **107 hits across 23 works**, most on the image of God
rather than on plurality. The survey file narrows that to **46 candidates** — every occurrence with
at least two of {plural, numer, persona, Trinit, Iudae, angel, singulari} within 700 characters.
**It is a seeding list, not a roster.** Standouts already visible:

| witness | where | why |
|---|---|---|
| **Abelard**, `abelard-hex` | PL 178:760B | *"Sed cur pluraliter dicitur: faciamus hominem ad imaginem nostram, si nulla prorsus pluralitas in Deo sit"* — the same man who is K3's star witness on *Eloim*, asking the same question at the other verse. Signals: judae, persona, plural, singulari. **Build this one first.** |
| **Glossa**, `glossa` | PL 113:80B | *"Insinuatur pluralitas personarum Patris, et Filii, et Spiritus sancti, et statim unitas deitatis"* (attributed AUG.) — the school answer in its printed form. |
| **Glossa**, `glossa` | PL 113:114D | *"Ad angelos dixisse intelligitur"* — ⭐ **the angels reading, which is the rabbinic bench's own primary answer.** This is the contact point. |
| **Rupert**, `rupert-gen` | PL 167:250B | *"cur hoc totum dixerit idem Deus… cum dicere posset solummodo: Faciamus hominem"* — why the longer formula at all. 31 hits in Rupert; prune hard. |
| **Hugh**, `hugh-adnot` | PL 175:37B | the three progressions — work, informing word, counsel. |
| **Comestor**, `comestor-hs` | PL 198:1063C | *"loquitur Pater ad Filium, et Spiritum sanctum"* — the handbook settling it. |

⛔ **Run `overlap.py` on every candidate before slicing.** None of these were checked against
existing slices, because that check belongs to the session that writes the spec.

## The rabbinic loci — availability probed, licences resolved

| ref | Hebrew | licence | note |
|---|---|---|---|
| **Bereshit Rabbah 8** | ⛔ **`Daat Bereshit Rabbah`** | **Public Domain** | 13 segments. ⛔ **`Wikisource Bereshit Rabbah` does NOT cover chapter 8** — only Torat Emet and Daat do, and Torat Emet is out. **Daat, which failed for BR 1–3, works here.** So BR Hebrew in this edition will come from two versions by chapter; say so in the colophon. |
| Bereshit Rabbah 17 | `Daat Bereshit Rabbah` | Public Domain | 8 segments; secondary. |
| Sanhedrin 38b | `Wikisource Talmud Bavli` | CC BY-SA | the *minim* material again. **Davidson is CC BY-NC — barred.** |
| Rashi on Gen 1:26 | Silbermann | Public Domain | key `silbermann` |
| Ibn Ezra on Gen 1:26 | Piotrkow 1907–11 | Public Domain | |
| Ramban on Gen 1:26 | `Vocalized Edition` | CC BY | key `sefaria-vocalized` |
| Onkelos Gen 1:26 | `Onkelos Genesis` | Public Domain | |
| Targum Neofiti Gen 1:26 | Vatican MS | **unknown** | same open question as the existing two Neofiti witnesses |

**BR 8 is the crux.** Read segments 3, 5, 8 and 9 first:
- **8:3** — *ויאמר אלהים נעשה אדם. **במי נמלך?*** "With whom did he take counsel?" R. Yehoshua in
  R. Levi's name: with the work of heaven and earth.
- **8:5** — R. Simon: the ministering angels formed parties, some saying *let him not be created*.
- **8:8** — ⭐ R. Shmuel bar Naḥman in R. Yonatan's name: when Moses was writing the Torah and reached
  *na'aseh adam*, he said, *"Master of the world, why do you give an opening to the minim?"*
- **8:9** — ⭐ *שאלו המינים את רבי שמלאי: כמה אלהות בראו את העולם?* "The *minim* asked R. Simlai:
  how many divinities created the world?"

## ⚠ This crux will probably require amending K3's finding — escalate, don't just do it

K3's finding says: three benches, three conclusions, **no contact**. Gen 1:26 looks like the place
where that is false, and falsely in both directions at once:

- the rabbinic bench **knows exactly** what is being done with the plural and says so — BR 8:8 and
  8:9 name the *minim* and answer them;
- the Latin bench's alternative reading, *ad angelos dixisse intelligitur* (Glossa 113:114D), **is
  the rabbinic bench's own primary answer** at BR 8:3.

That is direct, mutual, named contact on the very question K3 says the benches never had. Amending a
`finding` is not a builder's call — write the evidence, state the case in
`notes/SOURCES-FINDINGS.md`, and put the amendment to Wilson, as Phase 6 did for K1.

## Checklist

1. Get Wilson's answer on the anchor/scripture blocker above. Nothing builds until then.
2. `pull-sefaria.py`: add BR 8 (and 17 if used) pinned to **`Daat Bereshit Rabbah`**, Sanhedrin 38b
   to **Wikisource Talmud Bavli**, and the Gen 1:26 commentators. Probe the actual ref, never trust
   a version title listed for the work.
3. `overlap.py` every Latin candidate. `grep -l '<distinctive phrase>' data/witnesses/*.json` for the
   rabbinic ones — `overlap.py` covers Latin only.
4. Write `cruxes/elohim-and-trinity.py` additions, `build-crux.py`, `check.py`, render, read the daf.
5. Fresh English uses **`DRAFT`**, not `APPROVED` — Phase 3's approval predates it.
6. Log what the plan got wrong in `notes/SOURCES-FINDINGS.md`.
