"""Shared metadata for the Nicholas of Lyra / Paul of Burgos witnesses. Phase 6 part six, 2026-09-06.

Source: Biblia Sacra cum postillis Nicolai de Lyra, Anton Koberger, Nuremberg 1486-87, part 1
(Genesis - 2 Chronicles), archive.org item `biblia-sacra-lyra_202308`. Transcribed from the page
images under the same scoped exception PHASES.md froze for Chalcidius: the text is not in the
Patrologia, so it cannot be sliced from the TEI; abbreviations are expanded silently and
consistently, and every witness names the leaf it came from in `source`.

⚠ This is a SUBSTITUTION. PLAN.md names the 1492 Venice Biblia cum glossa, which did not surface;
the colophon and every `source` cite the edition actually used.
"""
LYRA = dict(work="lyra-postilla", author="nicholas-of-lyra", tradition="latin",
            date=1330, date_precision="range-1322-1332", place="paris")
BURGOS = dict(work="burgos-additiones", author="paul-of-burgos", tradition="latin",
              date=1429, date_precision="circa", place="burgos")
DOERING = dict(work="doering-replicae", author="matthias-doering", tradition="latin",
               date=1440, date_precision="range-1429-1450", place="paris")
DRAFT = {"translator": "claude-draft", "license": "cc-by", "status": "draft-awaiting-approval"}
EDITION = ("Biblia Sacra cum postillis Nicolai de Lyra, additionibus Pauli Burgensis et replicis "
           "Matthiae Doering (Nuremberg: Anton Koberger, 1486-87), pars i")
SRC = {"license": "lyra-koberger-1487", "version": EDITION}

PERSONS = {
 "nicholas-of-lyra": {"name": "Nicholas of Lyra", "dates": "c. 1270-1349", "tradition": "latin",
   "role": "author",
   "note": "Franciscan of Paris, whose Postilla litteralis is the most widely copied and printed "
           "Latin commentary on the whole Bible. He read Hebrew and used Rashi constantly, by name, "
           "as Ra. Sa. -- which is what Paul of Burgos attacks him for, and the reason this edition "
           "prints him: he is the one Latin on this daf who reads the rabbinic bench, credits it, "
           "and is taken to task by another Latin for crediting it too much."},
 "paul-of-burgos": {"name": "Paul of Burgos", "dates": "c. 1351-1435", "tradition": "latin",
   "role": "author",
   "note": "Solomon ha-Levi of Burgos, rabbi, baptised in 1390 and afterwards bishop of Burgos and "
           "chancellor of Castile. His Additiones to Lyra's Postilla were printed inside the Latin "
           "Bible from the 1480s on. On this daf he is the sharpest instrument the edition has: a "
           "man who had read the rabbinic bench from the inside, writing as a Christian bishop, "
           "arguing about how much of the literal sense the Latins owe to Rashi."},
 "matthias-doering": {"name": "Matthias Doering", "dates": "c. 1390-1469", "tradition": "latin",
   "role": "author",
   "note": "Franciscan provincial of Saxony, whose Replicae (he called them Correctorium "
           "corruptorii Burgensis) defend Lyra against Burgos and are printed beside both."},
}
PLACES = {"burgos": {"name": "Burgos", "lat": 42.34, "lon": -3.70}}
LICENSES = {
 "lyra-koberger-1487": {
   "label": EDITION + " -- public domain",
   "note": "Transcribed from the page images of archive.org item biblia-sacra-lyra_202308, which "
           "carries no rights notice. A SUBSTITUTION, accepted by Wilson Pruitt on 2026-09-06: "
           "PLAN.md named the 1492 Venice Biblia cum glossa, which did not surface on archive.org; "
           "this Koberger folio carries the same three-layer apparatus (Postilla, Burgos's "
           "Additiones, Doering's Replicae) and is cited throughout as the edition actually used, "
           "as Chalcidius is cited from the Bade print of 1520 rather than from Waszink. Leaf numbers in `source` are the archive.org leaf "
           "index (page/nN.jpg), which is the only stable reference the item has: the scandata "
           "carries no printed folio numbers, and the hOCR page index is offset from the leaves by "
           "an amount that drifts along the volume. Expansion convention as frozen for Chalcidius: "
           "abbreviations expanded silently and consistently, u/v normalised, nothing else altered."}
}
