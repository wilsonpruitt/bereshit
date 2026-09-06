"""Shared metadata for the Philo of Alexandria witnesses. Phase 6 part five, 2026-09-06.

Philo's De opificio mundi is sliced by Cohn's printed section number out of the First1KGreek TEI
(see bench.greek). He goes in on the `greek-jewish` bench, beside the LXX, which is where the
schema already had room for him -- no new tradition, no schema change.

Every Philo witness is defined in exactly ONE crux spec, its primary crux, and lists any further
cruxes in its own `cruxes` facet; build-crux.py folds it into the other rosters as an extra. That
is the Chalcidius pattern from Phase 6 part four.
"""
from bench import greek, yonge  # noqa: F401  (yonge is for checking a draft, never embedded)

# Common to every witness. Philo's floruit is fixed by the embassy to Gaius in 39/40 CE; De
# opificio is undated within his life and the edition dates him at the middle of it.
BASE = dict(work="philo-opif", author="philo", tradition="greek-jewish",
            date=40, date_precision="floruit-30-45", place="alexandria")

# Fresh English, drafted from Cohn's Greek. DRAFT, not APPROVED: Wilson's Phase 3 approval covered
# the body as it then stood, and everything drafted after it carries the draft status (PHASES.md).
PDRAFT = {"translator": "claude-draft", "license": "cc-by", "status": "draft-awaiting-approval"}

PERSONS = {
 "philo": {"name": "Philo of Alexandria", "dates": "c. 20 BCE - c. 50 CE", "tradition": "greek-jewish",
           "role": "author",
           "note": "The one Hellenistic-Jewish reader of Gen 1:1-5 in this edition, and the head of "
                   "streams that both other benches are the tail of. He was built at Phase 6 part "
                   "five; before that he was in this edition only as a name Chalcidius cites. The "
                   "transmission is this edition's own thesis in mirror: the rabbinic bench does "
                   "not cite him once and did not preserve him, while Ambrose's Hexaemeron is "
                   "substantially his and rarely says so, and Cohn's own prolegomena open by "
                   "saying that Philo's memory, neglected by Jews no less than by pagans, hangs "
                   "wholly on the Christian church. He was recovered for Judaism only in the "
                   "sixteenth century, by Azariah dei Rossi."}}

LICENSES = {
 "first1k-greek": {
   "label": "Cohn's Greek text of Philo, TEI edition by OpenGreekAndLatin/First1KGreek - CC BY-SA 4.0",
   "attribution": "Philo, De opificio mundi, ed. Leopold Cohn, Philonis Alexandrini opera quae "
                  "supersunt i (Berlin: Reimer, 1896). TEI text tlg0018.tlg001.1st1K-grc1 from "
                  "OpenGreekAndLatin/First1KGreek (University of Leipzig / Perseus, Digital Divide "
                  "Data), licensed CC BY-SA 4.0.",
   "note": "Cohn's 1896 text is itself in the public domain and this edition holds that a faithful "
           "transcription of a public-domain text creates no new right. What is licensed here is "
           "the file actually used, including its correction and encoding, and the site already "
           "carries CC BY-SA components under per-component licensing (Wikisource Talmud Bavli, "
           "Wikisource Bereshit Rabbah, Miqra according to the Masorah). This key does the same. "
           "The critical apparatus that the file carries inside its section divisions is not "
           "reproduced; it is stripped in the loader, and where a reading matters the variant is "
           "recorded in the witness notes."}}
