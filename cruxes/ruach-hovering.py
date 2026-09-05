"""K7 — ruach-hovering (Gen 1:2). The pilot crux; ported verbatim from build-k7.py during the
Phase 1 generalization. See PHASES.md for the spec-file contract (WITNESSES, THREADS, FINDING,
PERSONS, PLACES)."""
import json, pathlib
from bench import ROOT, RAW, latin, sef, DRAFT, thread

CRUX_ID = "ruach-hovering"
E = lambda i, f, t, ty, ev: thread(CRUX_ID, i, f, t, ty, ev)

WITNESSES = []
def add(**kw): WITNESSES.append(kw)

# ---------------------------------------------------------------- scripture-level witnesses
add(id="lxx-1-2", work="lxx", author="lxx-translators", tradition="greek-jewish",
    date=-250, date_precision="circa", place="alexandria",
    anchor={"verse": "gen.1.2"}, lemma={"el": "πνεῦμα θεοῦ ἐπεφέρετο ἐπάνω τοῦ ὕδατος", "en": "a spirit of God was borne upon the water"},
    original={"lang": "el", "text": "ἡ δὲ γῆ ἦν ἀόρατος καὶ ἀκατασκεύαστος, καὶ σκότος ἐπάνω τῆς ἀβύσσου, καὶ πνεῦμα θεοῦ ἐπεφέρετο ἐπάνω τοῦ ὕδατος.", "source": "LXX Gen 1:2 (Rahlfs)", "license": "pd"},
    english={"text": "But the earth was unsightly and unfurnished, and darkness was over the deep, and the Spirit of God moved over the water.", "translator": "Brenton 1851", "license": "pd"},
    cruxes=["ruach-hovering", "tohu-vabohu"], senses=["translation"],
    notes="ἐπεφέρετο ('was borne upon') is the reading every Latin 'ferebatur / superferebatur' descends from. The Greek already drops the bird: the verb is motion-over, not brooding.")

add(id="vulgate-1-2", work="vulgate", author="jerome", tradition="latin",
    date=392, date_precision="circa", place="bethlehem",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Spiritus Dei ferebatur super aquas", "en": "the Spirit of God was borne over the waters"},
    original=latin("7204", "Terra autem erat inanis et vacua", "ferebatur super aquas.", 28),
    english={"text": "But the earth was empty and void, and darkness [was] upon the face of the deep, and the Spirit of God was borne over the waters.", **DRAFT},
    cruxes=["ruach-hovering", "tohu-vabohu"], senses=["translation"],
    notes="Jerome's own Vulgate keeps the Old Latin/LXX 'ferebatur' even though his Hebrew Questions (same decade) insist the Hebrew means brooding. The Latin bench inherits the verb he declined to change. PL 28 prints Jerome's text without 'erant' and flags the Vulgate's addition.")

# ---------------------------------------------------------------- rabbinic bench
onk_he, _, onk_lic = sef("targ-onk", "he", 1)
add(id="targ-onk-1-2", work="targ-onk", author="onkelos", tradition="rabbinic",
    date=200, date_precision="circa", place="babylonia",
    anchor={"verse": "gen.1.2"}, lemma={"arc": "וְרוּחָא מִן קֳדָם יְיָ מְנַשְּׁבָא", "en": "and a wind from before the LORD was blowing"},
    original={"lang": "arc", "text": onk_he, "source": "Sefaria, 'Onkelos Genesis'", "license": {"public domain": "pd"}.get(onk_lic.lower(), onk_lic.lower().replace(" ", "-"))},
    english={"text": "And the earth was waste and empty, and darkness was spread over the face of the deep, and a wind from before the LORD was blowing over the face of the waters.", **DRAFT},
    cruxes=["ruach-hovering", "tohu-vabohu"], senses=["translation"],
    notes="Onkelos makes two decisions at once: ruach is a wind, not a spirit, and 'from before the LORD' keeps God at a remove; merahefet becomes menashva, 'blowing'. No bird, no hovering. Etheridge's PD English exists on Sefaria but did not return by version title; fetch from archive.org.")

neof_he, _, _ = sef("targ-neof", "he", 0)
neof_en, neof_ver, neof_lic = sef("targ-neof", "en", 0)
add(id="targ-neof-1-2", work="targ-neof", author="targum-neofiti", tradition="rabbinic",
    date=300, date_precision="range-100-400", place="palestine",
    anchor={"verse": "gen.1.2"}, lemma={"arc": "וְרוּחַ דְּרַחֲמִין מִן קֳדָם יְיָ הֲוָה מְנַשְּׁבָא", "en": "and a spirit of mercy from before the LORD was blowing"},
    original={"lang": "arc", "text": neof_he, "source": "Sefaria, Vatican MS Neofiti 1 (whole of 1:1–5 in one segment)", "license": "check"},
    english={"text": "In the beginning, with wisdom, the Word of the LORD created and perfected the heavens and the earth. And the earth was waste and empty, desolate of human and beast, empty of all tillage of plants and of trees; and darkness was spread over the face of the deep, and a spirit of mercy from before the LORD was blowing over the face of the waters.", **DRAFT},
    cruxes=["ruach-hovering", "beginning-of-what", "tohu-vabohu"], senses=["translation"],
    notes="'Spirit of mercy' answers the wind/spirit question in a third way: neither the weather nor the Holy Spirit but a divine disposition. Neofiti's 1:1 'with wisdom' is the K1 anchor. Hebrew licence on Sefaria is 'unknown' — the MS transcription is PD in substance; confirm before embedding.")

psj_he, _, _ = sef("targ-psj", "he", 1)
psj_en, psj_ver, psj_lic = sef("targ-psj", "en", 1)
add(id="targ-psj-1-2", work="targ-psj", author="targum-pseudo-jonathan", tradition="rabbinic",
    date=750, date_precision="range-600-800", place="palestine",
    anchor={"verse": "gen.1.2"}, lemma={"arc": "וְרוּחַ רַחֲמִין מִן קֳדָם יְיָ מְנַתְבָא", "en": "and a spirit of mercies from before the LORD breathed"},
    original={"lang": "arc", "text": psj_he, "source": "Sefaria, 'Targum Jonathan on Genesis'", "license": "pd"},
    english={"text": psj_en, "translator": "Etheridge 1862", "license": "pd"},
    cruxes=["ruach-hovering", "tohu-vabohu"], senses=["translation"],
    notes="Same 'spirit of mercies' as Neofiti; the verb menatva ('breathed / blew') keeps the Onkelos line. Etheridge embedded verbatim (PD).")

br_he, _, _ = sef("br-2", "he", 3, he_file="br-2-he.json")
br_en, br_ver, br_lic = sef("br-2", "en", 3)
cut_he = br_he.find("וְרוּחַ אֱלֹהִים מְרַחֶפֶת")
cut_en = br_en.find("“And the spirit of God was hovering”")
add(id="br-2-4", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.2"}, lemma={"he": "וְרוּחַ אֱלֹהִים מְרַחֶפֶת", "en": "and the spirit of God was hovering"},
    original={"lang": "he", "text": br_he[cut_he:], "source": "Bereshit Rabbah 2:4 (Vilna numbering; Theodor–Albeck differs)", "license": "check", "version": "Sefaria 'Midrash Rabbah -- TE' (licence unknown); a PD 'Daat' text exists on Sefaria"},
    english={"text": br_en[cut_en:], "translator": "The Sefaria Midrash Rabbah, 2022", "license": "cc-by", "attribution_required": True},
    tradents=["resh-lakish", "r-hagai", "r-pedat", "ben-zoma", "r-yehoshua-b-hananya"],
    cruxes=["ruach-hovering"], senses=["allegorical", "literal"],
    notes="Two answers in one section. Resh Lakish: the ruach is the spirit of the King Messiah (Isa 11:2), brought by repentance-as-water. Then the Ben Zoma story: 'blowing' is not written but 'hovering' — like a bird beating its wings, touching and not touching. Note the bird is an unspecified 'of' and the claim is touching-and-not-touching; the Bavli's version has a dove and no touching at all.")

chag_he3, chag_ver, chag_lic = sef("b-chag-15a", "he", 2)
chag_he4, _, _ = sef("b-chag-15a", "he", 3)
add(id="b-chag-15a", work="bavli-chagigah", author="bavli", tradition="rabbinic",
    date=550, date_precision="redaction-500-600", place="babylonia",
    anchor={"verse": "gen.1.2"}, lemma={"he": "כְּיוֹנָה שֶׁמְּרַחֶפֶת עַל בָּנֶיהָ וְאֵינָהּ נוֹגַעַת", "en": "like a dove that hovers over her young and does not touch"},
    original={"lang": "arc", "text": chag_he3 + " " + chag_he4, "source": "b. Chagigah 15a (Vilna)", "license": "cc-by-sa", "version": chag_ver},
    english={"text": "Our rabbis taught: It once happened that Rabbi Yehoshua ben Ḥananya was standing on a step on the Temple Mount, and Ben Zoma saw him and did not rise before him. He said to him: From where and to where, Ben Zoma? He said to him: I was gazing between the upper waters and the lower waters, and between the one and the other there are only three fingerbreadths, as it is said, 'and the spirit of God was hovering over the face of the waters' (Gen 1:2) — like a dove that hovers over her young and does not touch them. Rabbi Yehoshua said to his disciples: Ben Zoma is still outside. — Now, 'the spirit of God was hovering over the face of the waters': when was that? On the first day. But the dividing was on the second day, as it is written, 'and let it divide water from water' (Gen 1:6). And how much [lies between them]? Rav Aḥa bar Yaakov said: a hair's breadth. The rabbis say: like the gap between the planks of a bridge. Mar Zutra, or some say Rav Ashi, said: like two cloaks spread one over the other; and some say, like two cups tipped one upon the other.", **DRAFT},
    tradents=["ben-zoma", "r-yehoshua-b-hananya", "rav-aha-b-yaakov", "mar-zutra"],
    cruxes=["ruach-hovering", "heaven-earth-order"], senses=["literal"],
    notes="The Bavli's Ben Zoma reads merahefet as a physical fact about distance: hovering measures the gap between upper and lower waters. The anonymous continuation then argues the gap into a hair's breadth. Steinsaltz/Davidson English is CC BY-NC and is NOT embedded; this is a fresh draft against the Wikisource Aramaic.")

rashi_he, _, _ = sef("rashi-gen-1", "he")
rashi_en, rashi_ver, rashi_lic = sef("rashi-gen-1", "en")
d = json.load(open(RAW / "rashi-gen-1.json"))
he_v = [v for v in d["versions"] if v["language"] == "he"][0]["text"][1]
en_v = [v for v in d["versions"] if v["language"] == "en"][0]["text"][1]
add(id="rashi-1-2b", work="rashi-gen", author="rashi", tradition="rabbinic",
    date=1090, date_precision="range-1080-1105", place="troyes",
    anchor={"verse": "gen.1.2"}, lemma={"he": "כְּיוֹנָה הַמְרַחֶפֶת עַל הַקֵּן", "en": "as a dove hovering over the nest"},
    original={"lang": "he", "text": he_v[-1], "source": "Rashi on Gen 1:2, s.v. ורוח אלהים מרחפת", "license": "pd"},
    english={"text": en_v[-1], "translator": "Rosenbaum–Silbermann 1929–34", "license": "pd"},
    cruxes=["ruach-hovering"], senses=["literal"],
    notes="Rashi's dove over the nest is the Bavli's dove (Chagigah 15a), not Bereshit Rabbah's unspecified bird. The Old French gloss acoveter means 'to cover, to brood' — which is exactly Jerome's incubabat. Rashi and Jerome, seven centuries apart, gloss the same Hebrew verb with the same vernacular sense from opposite sides. The Throne of Glory standing in the air is from a different source [CHECK: PdRE / Midrash Konen].")

# ---------------------------------------------------------------- latin bench
add(id="basil-hex-lat-2-6", work="basil-hex-lat", author="basil", tradition="latin",
    date=400, date_precision="circa", place="caesarea-cappadociae",
    anchor={"verse": "gen.1.2"}, lemma={"la": "fovebat et vivificabat aquarum naturam, ad similitudinem gallinae cubantis", "en": "warmed and quickened the nature of the waters, like a hen sitting"},
    original=latin("7608", "Quomodo ergo hic spiritus aquis superferebatur?", "genitali potentia Spiritus sanctus caret.", 53),
    english={"text": "How, then, was this Spirit borne above the waters? I will tell you not my own account but that of a certain man, a Syrian by birth, who was as far from the wisdom of this age as he was reckoned near to true doctrine. He used to say that the Syrian tongue is the more expressive, and that because of its kinship with Hebrew it comes closer to the idiom of the Scriptures. The sense of his saying, then, is this: 'was borne above,' he says, means that the Spirit warmed and quickened the nature of the waters, in the likeness of a hen sitting on her eggs, putting a living power into the things that were being warmed. So the reason for the phrase 'was borne above' is explained thus: he was driving the nature of the waters toward being quickened. From this the point that some so insistently demand can be sufficiently proved: that the Holy Spirit does not lack generative power.", **DRAFT},
    cruxes=["ruach-hovering"], senses=["literal"],
    notes="Basil, Hexaemeron II.6, delivered in Greek in 378; the Latin bench read it in Eustathius' version (c. 400). The unnamed Syrian is the source of the whole Latin 'warming' line: Ambrose, Augustine, Rupert, Abelard, Comestor all descend from this paragraph. Basil's bird is a hen (gallina); Jerome's, independently, is a generic volucris.")

add(id="ambrose-hex-1-8-29", work="ambrose-hex", author="ambrose", tradition="latin",
    date=387, date_precision="circa", place="milan",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Syrus … sic habet: Et Spiritus Dei fovebat aquas", "en": "the Syriac has: And the Spirit of God warmed the waters"},
    original=latin("6958", "maxime cum sequatur: Et spiritus Dei superferebatur super aquas", "Spiritus divinus qui fecit me (Job. XXXIII, 4) .", 14),
    english={"text": "…especially since there follows: 'And the Spirit of God was borne above the waters.' Some take this as the air, others as the breath we draw and take in, the breath of this life-giving atmosphere; but we, agreeing with the judgment of the saints and the faithful, take it as the Holy Spirit, so that in the founding of the world the working of the Trinity may shine out. […] Finally the Syriac, which is neighbor to the Hebrew and in most things agrees and chimes with it in wording, has it thus: 'And the Spirit of God warmed the waters,' that is, quickened them, so as to gather them into new creatures and by his warmth bring them alive. For we also read that the Holy Spirit is creator, Job saying, 'The divine Spirit who made me' (Job 33:4).", **DRAFT},
    cruxes=["ruach-hovering", "elohim-and-trinity"], senses=["literal"],
    notes="Ambrose is reading Basil's Greek directly (Milan, 387; Eustathius' Latin is later). He carries the Syriac 'warmed' but drops the hen. The Latin excerpt here spans two columns; the middle (Ps 33:6 on Word and Spirit) is elided in the English.")

add(id="jerome-hq-1-2", work="jerome-hq", author="jerome", tradition="latin",
    date=391, date_precision="circa", place="bethlehem",
    anchor={"verse": "gen.1.2"}, lemma={"he": "מְרַחֶפֶת", "la": "incubabat, sive confovebat", "en": "was brooding, or warming"},
    original=latin("7160", "Et Spiritus Dei ferebatur super aquas. Pro eo quod", "Spiritum tuum, et creabuntur (Psal. CIII, 30) .", 23),
    english={"text": "'And the Spirit of God was borne over the waters.' For what our copies have as 'was borne,' the Hebrew has MERAHEFET, which we may render 'was brooding' or 'was warming,' in the likeness of a bird quickening her eggs with her heat. From this we understand that it is not said of the spirit of the world, as some suppose, but of the Holy Spirit, who is himself called the giver of life to all things from the beginning. And if giver of life, then consequently creator; and if creator, then God. 'Send forth,' he says, 'your Spirit, and they shall be created' (Ps 104:30).", **DRAFT},
    cruxes=["ruach-hovering"], senses=["literal"],
    notes="Jerome claims the bird from the Hebrew verb itself, not from the Syrian. His bird broods and warms (incubare, confovere); Ben Zoma's hovers and does not touch. Same verb, opposite physical picture. The star thread's Latin end.")

add(id="aug-gnm-1-5-8", work="aug-gnm", author="augustine", tradition="latin",
    date=389, date_precision="range-388-389", place="thagaste",
    anchor={"verse": "gen.1.2"}, lemma={"la": "non per spatia locorum … sed per potentiam invisibilis sublimitatis suae", "en": "not across spaces of place, but by the power of his invisible loftiness"},
    original=latin("7303", "Quod autem scriptum est, Et Spiritus Dei superferebatur super aquam, sic solent Manichaei", "superferatur voluntas fabri.", 34),
    english={"text": "As for what is written, 'And the Spirit of God was borne above the water,' the Manichees are in the habit of carping at it thus: 'So the water was the dwelling of the Spirit of God, and it contained the Spirit of God?' They try to twist everything with a perverse mind, and are blinded by their own malice. When we say 'the sun is borne above the earth,' do we mean by this that the sun lives in the earth and that the earth contains the sun? And yet the Spirit of God was not borne above the water the way the sun is borne above the earth, but in another way, which few understand. For that Spirit was not borne above the water across the spaces of place, as the sun is borne above the earth, but by the power of his invisible loftiness. Let these people tell us how the will of a craftsman is borne above the things that are to be made.", **DRAFT},
    cruxes=["ruach-hovering"], senses=["literal"],
    notes="Augustine's first answer, against the Manichees: the verb is about power, not position. The craftsman's will (voluntas fabri) is born here and becomes the Carolingian bench's stock answer.")

add(id="aug-gnl-imp-4-16", work="aug-gnl-imp", author="augustine", tradition="latin",
    date=393, date_precision="circa", place="hippo",
    anchor={"verse": "gen.1.2"}, lemma={"la": "sicut superfertur voluntas artificis ligno", "en": "as the will of a craftsman is borne above the wood"},
    original=latin("7310", "Et Spiritus Dei superferebatur super aquam. Non ita superferebatur sicut oleum aquae", "quae ad operandum movet.", 34),
    english={"text": "'And the Spirit of God was borne above the water.' He was not borne above it as oil is above water, or water above earth, that is, as though he were contained; but, if examples are to be taken from visible things for this, as the light of the sun or moon is borne above the bodies it illuminates on earth: for it is not contained in them, but, while it is contained by the sky, it is borne above them. Likewise we must take care not to think the Spirit of God is borne above matter as though across spaces of place, but by a certain effecting and fashioning force, so that what he is borne above is effected and fashioned; as the will of a craftsman is borne above the wood, or above whatever thing is set under him to be worked, or even above the very limbs of his own body, which he moves in order to work.", **DRAFT},
    cruxes=["ruach-hovering"], senses=["literal"],
    notes="The craftsman image sharpened: will over wood, will over one's own limbs. Remigius, Bruno and Hugh's 'artifex' all come from here.")

add(id="aug-conf-13-9-10", work="aug-conf", author="augustine", tradition="latin",
    date=400, date_precision="circa", place="hippo",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Cur solus Spiritus sanctus superferebatur super aquas", "en": "Why only the Holy Spirit was borne above the waters"},
    original=latin("7270", "Numquid aut Pater aut Filius non superferebatur super aquas?", "loca sua petunt.", 32),
    english={"text": "Was not the Father, or the Son, borne above the waters too? If we mean by place, as a body is, then neither was the Holy Spirit; but if we mean the eminence of unchangeable Godhead over everything changeable, then Father and Son and Holy Spirit were borne above the waters. Why then is this said only of your Spirit? Why of him alone? As if there were a place there, where there is no place, for him alone of whom it is said that he is your gift. In your gift we rest; there we enjoy you. Our rest is our place. Love lifts us there, and your good Spirit raises our lowliness from the gates of death. In good will is our peace. A body by its weight strives toward its own place. Weight is not only toward what is lowest, but toward its own place. Fire tends upward, a stone downward. They are driven by their weights; they seek their places.", **DRAFT},
    cruxes=["ruach-hovering", "elohim-and-trinity"], senses=["literal", "spiritual"],
    notes="The question turned inward: not what 'above' means but why the Spirit alone is said to be above. Answer: because the Spirit is gift, and love is weight. 'Pondus meum amor meus' follows a few lines on.")

add(id="aug-gnl-1-18-36", work="aug-gnl", author="augustine", tradition="latin",
    date=410, date_precision="range-401-415", place="hippo",
    anchor={"verse": "gen.1.2"}, lemma={"la": "sicut ova foventur ab alitibus", "en": "as eggs are warmed by birds"},
    original=latin("7302", "Sed ante omnia meminerimus", "per quemdam in suo genere dilectionis affectum.", 34),
    english={"text": "But before all else let us remember, as we have already said at length, that God does not work by temporal motions, as it were of his mind or body, as a man or an angel works, but by the eternal, unchangeable and stable reasons of his Word, coeternal with himself, and by a certain — if I may so put it — brooding warmth of his Holy Spirit, equally coeternal. For even what is said in Greek and in Latin of the Spirit of God, that he 'was borne above the waters,' according to the sense of the Syriac tongue, which is neighbor to Hebrew (for this is reported to have been explained by a certain learned Syrian Christian), is held to mean not 'was borne above' but rather 'was warming.' Not as swellings or wounds in the body are warmed with water, whether cold or tempered to a fitting heat; but as eggs are warmed by birds, where that heat of the mother's body in a way assists even the forming of the chicks, through a certain affection of love after its kind.", **DRAFT},
    cruxes=["ruach-hovering"], senses=["literal"],
    notes="Augustine's mature answer joins his own 'power not place' to the Syrian's warming and adds the mother-bird's love. He cites the Syrian at one remove ('fertur'), almost certainly through Ambrose.")

add(id="isidore-quaest-1-3", work="isidore-quaest", author="isidore", tradition="latin",
    date=620, date_precision="circa", place="seville",
    anchor={"verse": "gen.1.2"}, lemma={"la": "super cor nostrum tenebrosum et fluidum, quasi super aquas", "en": "over our dark and fluid heart, as over waters"},
    original=latin("21433", "Et spiritus Dei ferebatur super aquas. Spiritus autem Dei super cor nostrum", "cujus unda ablueremur.", 83),
    english={"text": "'And the Spirit of God was borne over the waters.' The Spirit of God was already being borne over our dark and fluid heart, as over waters: that standing in him we might find rest, be quickened by his breath, and be washed in his wave.", **DRAFT},
    cruxes=["ruach-hovering"], senses=["allegorical"],
    notes="Isidore does not answer the physical question at all; the waters are the heart. The allegorical reading the Glossa will carry in its margin.")

add(id="bede-gen-1-2", work="bede-gen", author="bede", tradition="latin",
    date=720, date_precision="circa", place="jarrow",
    anchor={"verse": "gen.1.2"}, lemma={"la": "totius simul Trinitatis in creatione mundi virtutem", "en": "the power of the whole Trinity together in the creation of the world"},
    original=latin("8466", "Bene autem cum in principio Deum, id est, in Filio Patrem", "cooperatam esse signaret.", 91),
    english={"text": "And rightly, having first declared that in the beginning, that is, in the Son, the Father made heaven and earth, he brought in mention of the Holy Spirit too by adding, 'And the Spirit of God was borne above the waters,' so as to signify that the power of the whole Trinity together worked in the creation of the world.", **DRAFT},
    cruxes=["ruach-hovering", "elohim-and-trinity"], senses=["literal"],
    notes="Bede has no bird and no Syrian on this verse: his 1:2 is Trinitarian (K3). Included here because Rabanus copies this sentence verbatim and it becomes the Glossa's spine.")

add(id="wigbod-gen-1-2", work="wigbod-gen", author="wigbod", tradition="latin",
    date=790, date_precision="circa", place="aachen",
    anchor={"verse": "gen.1.2"}, lemma={"la": "HIERONYMUS. … in Hebraeo habetur merephet", "en": "JEROME: in the Hebrew it is merephet"},
    original=latin("8606", "D. Quomodo spiritus Dei ferebatur super aquas, edissere?", "vivificator omnium a principio dicitur.", 96),
    english={"text": "Disciple: Explain how the Spirit of God was borne over the waters. — JEROME. Master: For what our copies have as 'was borne,' the Hebrew has merephet, which we may render 'was brooding' or 'was warming,' in the likeness of a bird quickening her eggs with her heat. From this we understand that it is not said of the spirit of the world, as some suppose, but of the Holy Spirit, who is himself called the giver of life to all things from the beginning.", **DRAFT},
    cruxes=["ruach-hovering"], senses=["literal"],
    notes="A Carolingian question-and-answer catena that labels its sources. Jerome quoted verbatim under his name at col. 1116C; Augustine's sun-over-earth (Gnm I.5) quoted at col. 1112D. The first witness that shows the two Latin lines (Hebrew bird, power-not-place) sitting side by side as authorities.")

add(id="alcuin-int-29", work="alcuin-int", author="alcuin", tradition="latin",
    date=796, date_precision="circa", place="tours",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Non pervagatione, sed potestate", "en": "Not by wandering over, but by power"},
    original=latin("21416", "Inter. 29. Quid est: Spiritus Domini ferebatur super aquas", "aquae nomine significatur", 100),
    english={"text": "Question 29. What is 'The Spirit of the Lord was borne over the waters'? — Answer: Not by wandering over them, but by power and a ruler's command, to form and quicken the formless matter which in this place is signified by the name of water.", **DRAFT},
    cruxes=["ruach-hovering"], senses=["literal"],
    notes="Augustine compressed to one sentence for the schoolroom. Note 'Spiritus Domini' (Old Latin) not 'Spiritus Dei' (Vulgate) — the Vetus Latina lingers in Alcuin's lemma.")

add(id="rabanus-gen-1-1", work="rabanus-gen", author="rabanus", tradition="latin",
    date=822, date_precision="circa", place="fulda",
    anchor={"verse": "gen.1.2"}, lemma={"la": "in similitudinem videlicet fabri, cujus voluntas … solet superferri", "en": "like a craftsman, whose will is borne above the things to be made"},
    original=latin("8885", "Et Spiritus Dei ferebatur super aquas. Non est opinandum pueriliter", "solet superferri.", 107),
    english={"text": "'And the Spirit of God was borne over the waters.' It is not to be supposed childishly that the creator Spirit, of whom it is written 'The Spirit of the Lord has filled the whole earth' (Wis 1:7), was borne above the things to be created by position in place. Rather it is to be understood that by divine power he excelled the creatures, holding in his own power when he would illumine the abyss of waters, when he would part them into one place so that the dry land might appear, when and how he would dispose the other creatures at his nod — in the likeness, that is, of a craftsman, whose will is accustomed to be borne above the things that are to be made.", **DRAFT},
    cruxes=["ruach-hovering"], senses=["literal"],
    notes="Augustine's craftsman in Rabanus' own words at col. 446D; then at 447C he copies Bede's Trinity sentence verbatim. Rabanus is the bridge by which both lines reach the Glossa.")

add(id="angelom-gen-1-2", work="angelom-gen", author="angelomus", tradition="latin",
    date=850, date_precision="circa", place="luxeuil",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Unde bene alia translatio dicit: Incumbebat, seu confovebat", "en": "Hence another translation well says: was lying upon, or warming"},
    original=latin("9032", "Sed ferebatur non localiter, sed potentialiter", "sicut haeretici putaverunt.", 115),
    english={"text": "But he was borne not by place but by power, ruling and sustaining that formless matter, as the will of a craftsman is borne above the things to be made. Hence another translation well says 'was lying upon,' or 'was warming,' in the likeness of a bird quickening her eggs with her heat, so that it may be plainly understood of the Holy Spirit and not of the spirit of this world, as the heretics thought.", **DRAFT},
    cruxes=["ruach-hovering"], senses=["literal"],
    notes="Angelomus splices the two Latin lines into one sentence: Augustine's 'not by place but by power' and Jerome's bird, the latter presented as 'another translation' and unnamed. Jerome's 'nonnulli' (some suppose) has hardened into 'haeretici'.")

add(id="remigius-gen-1-2", work="remigius-gen", author="remigius", tradition="latin",
    date=900, date_precision="circa", place="auxerre",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Sicut mens vel sapientia alicujus artificis superfertur operi", "en": "As the mind or wisdom of a craftsman is borne above his work"},
    original=latin("9346", "Spiritus Dei ferebatur super aquas. Sicut mens vel sapientia", "qualiter facere vellet.", 131),
    english={"text": "'The Spirit of God was borne over the waters.' As the mind or wisdom of some craftsman is borne above the work he is going to make, so that he may make it as he wills, so too the Holy Spirit was borne above, fore-ordaining and as it were arranging what, and in what manner, he willed to make.", **DRAFT},
    cruxes=["ruach-hovering"], senses=["literal"],
    notes="Augustine's craftsman, now with 'wisdom' — the Spirit as the plan before the work. Remigius also gives a moral reading at col. 55D (the fluid hearts of men).")

add(id="bruno-gen-1-2", work="bruno-gen", author="bruno-of-segni", tradition="latin",
    date=1100, date_precision="circa", place="segni",
    anchor={"verse": "gen.1.2"}, lemma={"la": "ut bonus artifex … jam tunc facere disponebat", "en": "like a good craftsman, was even then arranging to make"},
    original=latin("21403", "Dei. vero Spiritus ferebatur super aquas, quia ut bonus artifex", "atque alia aliis officiis destinamus.", 164),
    english={"text": "But the Spirit of God was borne over the waters, because, like a good craftsman, he was even then arranging to make this so manifold variety of creatures that we see. So we too, for example, when about to build a house, looking over the timber with eye and mind, assign some pieces to beams, some to columns, and others to other uses.", **DRAFT},
    cruxes=["ruach-hovering"], senses=["literal"],
    notes="The craftsman becomes a house-builder sorting timber. The digitization reads 'Dei. vero' — the PL plate should be checked for the stop.")

add(id="rupert-gen-1-8", work="rupert-gen", author="rupert", tradition="latin",
    date=1114, date_precision="circa", place="liege",
    anchor={"verse": "gen.1.2"}, lemma={"la": "melioratur ovum in eo quod calore volucris animatur et pullum producit", "en": "an egg is bettered in that it is quickened by a bird's warmth and brings forth a chick"},
    original=latin("10873", "Deinceps namque creaturae ejusdem formatio vel exornatio succedit", "Patri Filioque consubstantialem.", 167),
    english={"text": "For next follows the forming or adorning of that same creature, and it receives from the attention of the Spirit of God as great a bettering and as great a supplying of its poverty as, in its own small measure, an egg is bettered in that it is quickened by a bird's warmth and brings forth a chick. And what do we think this spirit is, but the goodness and love of God — a love not of feelings but substantial; love, I say, and life, and living power abiding in the Son and the Father, or proceeding from both, consubstantial with Father and Son.", **DRAFT},
    cruxes=["ruach-hovering", "elohim-and-trinity"], senses=["literal", "spiritual"],
    notes="Rupert has the egg but not the Syrian: the image arrives already naturalized. His 'love' is Confessions XIII.9 turned Trinitarian. Not found by the plan's search; surfaced by grepping the TEI for the bird vocabulary.")

add(id="abelard-hex-1-2", work="abelard-hex", author="abelard", tradition="latin",
    date=1130, date_precision="circa", place="paraclete",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Hebraicum habet, volitabat super faciem aquarum", "en": "the Hebrew has, was fluttering over the face of the waters"},
    original=latin("11118", "Et Spiritus Domini ferebatur super aquas. Hebraicum habet", "quatuor elementa comprehendun", 178),
    english={"text": "'And the Spirit of the Lord was borne over the waters.' The Hebrew has 'was fluttering over the face of the waters.' One translation has 'was warming the waters,' another 'was borne over the waters,' as does the present one we have in hand, which first comes to us to be expounded. […] Another translation, as we said, also has 'and the Spirit of the Lord was warming the waters,' after the manner of a bird that sits upon an egg to warm and quicken it; whence we rightly call the Holy Spirit the giver of life. And that confused mass is well compared to an egg not yet quickened or formed, in which, as in an egg containing four things in itself, the four elements are comprised…", **DRAFT},
    cruxes=["ruach-hovering", "ex-nihilo-or-matter"], senses=["literal"],
    notes="The one Latin witness who reports the Hebrew as 'fluttering' (volitabat) — which is what merahefet means in Deut 32:11 and what Ben Zoma and Rashi hear — rather than Jerome's 'brooding'. He keeps 'warming' only as 'a certain translation'. Where did Abelard get volitabat? Not from Jerome. A Jewish informant is possible [CHECK]. The excerpt spans cols 735B–735D; the middle is elided in the English.")

add(id="hugh-adnot-gen-1-2", work="hugh-adnot", author="hugh-of-st-victor", tradition="latin",
    date=1130, date_precision="circa", place="paris",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Spiritum Dei vocat ejus intentionem", "en": "He calls 'the Spirit of God' his intention"},
    original=latin("11054", "Et spiritus Dei ferebatur super aquas. Spiritum Dei vocat", "modo aquas propter mobilitatem appellat.", 175),
    english={"text": "'And the Spirit of God was borne over the waters.' He calls 'the Spirit of God' his intention, who like a craftsman presided over the work to be formed; 'the waters' he calls that mist, on account of its mobility; and so he names the same thing now 'abyss' for its depth, now 'darkness' for the absence of light, now 'waters' for its mobility.", **DRAFT},
    cruxes=["ruach-hovering", "tohu-vabohu"], senses=["literal"],
    notes="The most physical Latin reading: the waters are a mist of mixed elements, the Spirit is God's intention. Hugh's Adnotationes are the literal school; his De sacramentis treats the same verse theologically. The TEI reads 'praecerat' for 'praeerat'.")

add(id="honorius-hex-1", work="honorius-hex", author="honorius", tradition="latin",
    date=1140, date_precision="circa", place="regensburg",
    anchor={"verse": "gen.1.2"}, lemma={"la": "vel aquas fovebat, id est cuncta de aquis procreanda animabat", "en": "or was warming the waters, that is, giving life to all that was to come from them"},
    original=latin("10991", "Et Spiritus Domini ferebatur super aquas, vel aquas fovebat", "omnium vivificatio, vel ornatio.", 172),
    english={"text": "'And the Spirit of the Lord was borne over the waters,' or 'was warming the waters,' that is, was giving life to all that was to be brought forth from the waters. And note the Trinity: to God the Father is ascribed the creation of the world, to the Son the disposing of things, to the Holy Spirit the quickening, or adorning, of all.", **DRAFT},
    cruxes=["ruach-hovering", "elohim-and-trinity"], senses=["literal"],
    notes="By 1140 'vel aquas fovebat' is offered as a bare variant reading, no Syrian, no bird: the image has become a lemma.")

add(id="comestor-hs-gen-1", work="comestor-hs", author="comestor", tradition="latin",
    date=1170, date_precision="circa", place="paris",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Hebraeus habet pro super ferebatur, incubabat, vel Syra lingua, fovebat, sicut avis ova", "en": "The Hebrew has 'was brooding', or in Syriac 'was warming', as a bird her eggs"},
    original=latin("11575", "Hebraeus habet pro super ferebatur, incubabat", "Emitte Spiritum tuum, et creabuntur (Psal. CIII) .", 198),
    english={"text": "The Hebrew has, for 'was borne above,' 'was brooding,' or in the Syriac tongue 'was warming,' as a bird her eggs. In this, too, the whole beginning of the world being born is noted, together with its governance. Plato misunderstood this passage, thinking it was said of the world-soul. But it is said of the Holy Spirit creating, of whom we read, 'Send forth your Spirit, and they shall be created' (Ps 104:30).", **DRAFT},
    cruxes=["ruach-hovering"], senses=["literal"],
    notes="The textbook of the schools fuses Jerome's Hebrew and Basil's Syriac into one sentence and adds a new opponent: Plato's world-soul, i.e. William of Conches and the Chartres reading of the Spirit as anima mundi. The bird has become a proof against philosophers.")

add(id="aug-gnl-1-5-11", work="aug-gnl", author="augustine", tradition="latin",
    date=401, date_precision="range-401-415", place="hippo",
    anchor={"verse": "gen.1.2"}, lemma={"la": "non ex indigentia, sed ex beneficentia veniens amor", "en": "a love that comes not from need but from bounty"},
    original=latin("7302", "Propterea priusquam scriberetur, Dixit Deus, Fiat lux", "per abundantiam beneficentiae Deus amare putaretur?", 34),
    english={"text": "Therefore, before it was written 'God said, Let there be light,' Scripture went before it, saying, 'And the Spirit of God was borne above the water.' For whether by the name of water he meant the whole of corporeal matter, so as to intimate by that means whence all the things we can now distinguish in their kinds were made and formed (calling it water because we see everything on earth formed and grown together out of a moist nature through its various species), or a kind of spiritual life, floating as it were before the form of its conversion: in either case the Spirit of God was borne above, because whatever it was that he had begun, to be formed and perfected, lay beneath the good will of the Creator; so that when God said in his Word, 'Let there be light,' what was made might abide in his good will, that is in his good pleasure, after the measure of its kind; and so it is right that it pleased God, Scripture saying, 'And light was made; and God saw the light, that it was good.' […] But why, after the creature had first been mentioned, imperfect as it was, is the Spirit of God mentioned afterwards, Scripture first saying 'But the earth was invisible and unformed, and darkness was over the abyss,' and then bringing in 'And the Spirit of God was borne above the water'? Is it because a needy and destitute love so loves that it is subjected to the things it loves; and therefore, when the Spirit of God was mentioned, in whom his holy benevolence and love are understood, he was said to be borne above, lest God should be thought to love the works he was to make out of the necessity of want rather than out of the abundance of bounty?", **DRAFT},
    cruxes=["ruach-hovering", "elohim-and-trinity"], senses=["literal"], answers=["power-not-place", "love-gift", "trinity"],
    notes="The passage the Glossa quotes in its margin on 1:2 (as 'lib. I de Gen. ad lit., c. 5'). Two answers at once: water is matter or formless spiritual life, and the Spirit is 'above' because divine love is not needy. The middle chapter, which finds the Trinity in the verse, is elided in the English.")

_gl_la = (ROOT / "raw" / "latin" / "glossa-8950-gen-1-2-la.md").read_text().strip().split("\n")
_gl_en = (ROOT / "raw" / "latin" / "glossa-8950-gen-1-2-en.md").read_text().strip().split("\n")
add(id="glossa-1-2-ruach", work="glossa", author="glossa-ordinaria", tradition="latin",
    date=1120, date_precision="compilation-1110-1130", place="laon",
    anchor={"verse": "gen.1.2"}, lemma={"la": "Et Spiritus Domini ferebatur super aquas", "en": "And the Spirit of the Lord was borne over the waters"},
    original={"lang": "la", "text": "\n\n".join(l for l in _gl_la if l.strip()), "source": "PL 113, col. 70A–70D (marginal glosses on 1:2, in the order printed; the 'inanis et vacua' gloss from 69D appended)", "license": "pd", "cc_idno": "8950"},
    english={"text": "\n\n".join(l for l in _gl_en if l.strip()), "translator": "wilson-pruitt", "license": "wroot-glossa", "edition": "migne.app/glossa, Liber Genesis (8950), chunk 0"},
    cruxes=["ruach-hovering", "tohu-vabohu", "elohim-and-trinity"], senses=["literal", "allegorical"], answers=["power-not-place", "brooding-warmth", "trinity", "heart"],
    notes="Four glosses stand on the verse in the margin: Augustine Gn. litt. I.5 (water as matter; love not from need; 'not in place but by a power surpassing all'); Jerome's merahephet, cited by PL column; an unlabelled sentence that is Bede's Trinity gloss via Rabanus ('Tota ergo Trinitas hic operata'); and one Migne marks 'ISID. in Gen.?' (the floating hearts, which is Isidore's moral reading in Augustine's wording). The lemma reads 'Spiritus Domini', the Old Latin, not the Vulgate's 'Spiritus Dei' — Wilson's [var:] flags it. The bird enters the Glossa through Jerome only; the Syrian and the craftsman are both absent.")

# ---------------------------------------------------------------- threads (K7)
THREADS = [
 E("t-k7-01", "vulgate-1-2", "lxx-1-2", "transmits", "Vulgate 'ferebatur' renders LXX ἐπεφέρετο, not the Hebrew merahefet; the Latin bench inherits a Greek verb of motion."),
 E("t-k7-02", "ambrose-hex-1-8-29", "basil-hex-lat-2-6", "cites", "'Syrus, qui vicinus Hebraeo est … fovebat aquas, id est vivificabat' reproduces Basil Hex. II.6's Syrian and his gloss 'warmed and quickened'. Ambrose read Basil's Greek; Eustathius' Latin is the bench's later access to the same source."),
 E("t-k7-03", "aug-gnl-1-18-36", "basil-hex-lat-2-6", "cites", "'a quodam docto christiano syro fertur expositum … non superferebatur sed fovebat' names Basil's Syrian at one remove ('fertur'); 'sicut ova foventur ab alitibus' extends the gallina cubans."),
 E("t-k7-04", "aug-gnl-1-18-36", "ambrose-hex-1-8-29", "echoes", "Augustine's access to the Syrian is most plausibly Ambrose's Hexaemeron (heard in Milan 386–7); the 'vivificatio' motif matches Ambrose's 'vivificabat … animaret ad vitam'."),
 E("t-k7-05", "jerome-hq-1-2", "b-chag-15a", "parallel", "Both derive a bird from merahefet. Jerome: incubabat/confovebat, a bird warming eggs. Ben Zoma: a dove hovering over her young and NOT touching. Same verb, opposite physical claim. No citation either way; Jerome's 'in Hebraeo' points at the word, not at a rabbinic informant."),
 E("t-k7-06", "wigbod-gen-1-2", "jerome-hq-1-2", "cites", "Wigbod prints Jerome's paragraph verbatim under the label HIERONYMUS (PL 96:1116C)."),
 E("t-k7-07", "wigbod-gen-1-2", "aug-gnm-1-5-8", "cites", "Wigbod prints Augustine's sun-over-earth paragraph verbatim (PL 96:1112D)."),
 E("t-k7-08", "angelom-gen-1-2", "jerome-hq-1-2", "echoes", "'alia translatio dicit: Incumbebat seu confovebat, in similitudine volucris, ova calore animantis' is Jerome's wording, unnamed and re-labelled as a translation variant."),
 E("t-k7-09", "angelom-gen-1-2", "aug-gnl-imp-4-16", "echoes", "'non localiter sed potentialiter … sicut superfertur rebus fabricandis voluntas artificis' is Augustine's craftsman (Gnl imp. §16 / Gnm I.5)."),
 E("t-k7-10", "rabanus-gen-1-1", "aug-gnl-imp-4-16", "echoes", "'in similitudinem fabri, cujus voluntas his quae fabricandae sunt rebus solet superferri' restates Augustine's voluntas artificis; 'positione loci' = 'spatia locorum'."),
 E("t-k7-11", "rabanus-gen-1-1", "bede-gen-1-2", "cites", "PL 107:447C copies Bede's 'totius simul Trinitatis in creatione mundi virtutem cooperatam esse signaret' verbatim."),
 E("t-k7-12", "alcuin-int-29", "aug-gnm-1-5-8", "echoes", "'Non pervagatione, sed potestate' compresses 'non per spatia locorum … sed per potentiam'."),
 E("t-k7-13", "remigius-gen-1-2", "aug-gnl-imp-4-16", "echoes", "'mens vel sapientia alicujus artificis superfertur operi' = voluntas artificis, with 'sapientia' added."),
 E("t-k7-14", "bruno-gen-1-2", "aug-gnl-imp-4-16", "echoes", "'ut bonus artifex … disponebat' with the house-builder sorting timber elaborating Augustine's 'voluntas artificis ligno'."),
 E("t-k7-15", "hugh-adnot-gen-1-2", "aug-gnl-imp-4-16", "echoes", "'quasi artifex operi formando praeerat'; Hugh keeps the craftsman but replaces will with 'intentio'."),
 E("t-k7-16", "rupert-gen-1-8", "aug-gnl-1-18-36", "echoes", "'ovum … calore volucris animatur et pullum producit' is Augustine's 'ova foventur ab alitibus … formandis pullis'; the Syrian is gone."),
 E("t-k7-17", "rupert-gen-1-8", "aug-conf-13-9-10", "echoes", "'bonitatem amoremque Dei … amorem et vitam' develops Conf. XIII.9's Spirit-as-gift-and-love reading of the same verse."),
 E("t-k7-18", "abelard-hex-1-2", "aug-gnl-1-18-36", "echoes", "'more avis quae ovo incumbit, ut ipsum foveat atque vivificet' = Augustine's warming bird; 'quaedam translatio fovebat' = the Syriac variant as transmitted by Augustine."),
 E("t-k7-19", "abelard-hex-1-2", "jerome-hq-1-2", "contests", "Abelard reports 'Hebraicum habet volitabat' against Jerome's 'in Hebraeo … incubabat'. He does not name Jerome, but the claim about the Hebrew is contradictory and deliberate."),
 E("t-k7-20", "abelard-hex-1-2", "rashi-1-2b", "parallel", "Abelard's 'volitabat' (flutter) is the sense Rashi's 'dove hovering over the nest' gives merahefet. Abelard consulted Jews on Hebrew elsewhere; no citation here. [CHECK for a documented channel]"),
 E("t-k7-21", "honorius-hex-1", "aug-gnl-1-18-36", "echoes", "'vel aquas fovebat, id est … animabat' offers the Syriac 'warmed' as a bare variant; the wording 'animabat' follows Ambrose/Augustine's vivificatio."),
 E("t-k7-22", "comestor-hs-gen-1", "jerome-hq-1-2", "cites", "'Hebraeus habet pro superferebatur incubabat' is Jerome's rendering, attributed to 'the Hebrew'."),
 E("t-k7-23", "comestor-hs-gen-1", "basil-hex-lat-2-6", "cites", "'vel Syra lingua fovebat, sicut avis ova' is Basil's Syrian, via Augustine Gnl I.18."),
 E("t-k7-24", "rashi-1-2b", "b-chag-15a", "cites", "Rashi's 'like a dove (yonah) hovering over the nest' follows the Bavli's dove (Chagigah 15a), not Bereshit Rabbah's unspecified bird ('of); the dove settles which source he is quoting."),
 E("t-k7-25", "rashi-1-2b", "br-2-4", "echoes", "The Ben Zoma story is in both BR 2:4 and Chagigah 15a; Rashi's wording is the Bavli's, but Rashi elsewhere cites BR by name on 1:1–5."),
 E("t-k7-26", "b-chag-15a", "br-2-4", "parallel", "Same Ben Zoma story, two redactions. BR: bird beating its wings, touching-and-not-touching. Bavli: dove over her young, not touching, three fingerbreadths. Compiled independently from a shared Palestinian tradition."),
 E("t-k7-27", "targ-psj-1-2", "targ-neof-1-2", "parallel", "Both render ruach Elohim as 'a spirit of mercy/mercies from before the LORD'; the Palestinian targum tradition shared the phrase."),
 E("t-k7-29", "glossa-1-2-ruach", "aug-gnl-1-5-11", "cites", "Labelled 'AUG., lib. I de Gen. ad lit., c. 5' in the margin; reproduces 'sive totam corporalem materiam aquam appellavit … sive spiritualem vitam … quasi fluitantem' and 'ne … per necessitatem indigentiae quam per abundantiam beneficentiae … amare putaretur' from PL 34:250–251."),
 E("t-k7-30", "glossa-1-2-ruach", "jerome-hq-1-2", "cites", "Labelled 'HIERON. in Gen. t. III, col. 939' — the Glossa (as printed by Migne) cites the very column; 'incubabat vel fovebat, more volucris ova calore animantis' is Jerome's sentence lightly recast."),
 E("t-k7-31", "glossa-1-2-ruach", "bede-gen-1-2", "echoes", "'Tota ergo Trinitas hic operata intelligitur, Deus, Pater scilicet; principium, Filius; Spiritus Dei, Spiritus sanctus' compresses Bede's 'totius simul Trinitatis in creatione mundi virtutem cooperatam' (PL 91:16C) as relayed by Rabanus (107:447C); unlabelled in the margin."),
 E("t-k7-32", "glossa-1-2-ruach", "isidore-quaest-1-3", "cites", "'In quo subsistentes requiesceremus flatu ejus vivificati, et unda baptismi abluti' is Isidore's 'in quo subsistentes requiesceremus, cujusque vivificaremur flatu, et cujus unda ablueremur' (PL 83:209C); a second gloss is labelled 'ISID. in Gen.?' by Migne."),
 E("t-k7-33", "glossa-1-2-ruach", "alcuin-int-29", "parallel", "Both carry the Old Latin lemma 'Spiritus Domini' against the Vulgate's 'Spiritus Dei'; no citation, but a shared Carolingian text-form."),
 E("t-k7-28", "jerome-hq-1-2", "rashi-1-2b", "parallel", "Jerome's incubabat and Rashi's Old French acoveter ('to cover, brood') give the same vernacular sense to merahefet, 700 years apart, with no possible contact. The only place on this crux where the two benches reach the same word."),
]

FINDING = "Rashi's Old French acoveter and Jerome's incubabat are the same word for the same Hebrew, with no contact. Abelard is the one Latin who reports the Hebrew as 'fluttering' (volitabat), on the rabbinic side of the verb."

# ---------------------------------------------------------------- persons / places this crux uses
PERSONS = {
 "lxx-translators": {"name": "The Seventy", "dates": "3rd c. BCE", "tradition": "greek-jewish"},
 "jerome": {"name": "Jerome", "la": "Hieronymus Stridonensis", "dates": "c. 347–420", "tradition": "latin"},
 "onkelos": {"name": "Targum Onkelos", "dates": "2nd c. (redaction 3rd–4th)", "tradition": "rabbinic"},
 "targum-neofiti": {"name": "Targum Neofiti", "dates": "1st–4th c.", "tradition": "rabbinic"},
 "targum-pseudo-jonathan": {"name": "Targum Pseudo-Jonathan", "dates": "7th–8th c. (older strata)", "tradition": "rabbinic"},
 "bereshit-rabbah": {"name": "Bereshit Rabbah", "dates": "compiled 400–500", "tradition": "rabbinic"},
 "bavli": {"name": "Babylonian Talmud", "dates": "redacted 500–600", "tradition": "rabbinic"},
 "rashi": {"name": "Rashi", "he": "רש״י", "dates": "1040–1105", "tradition": "rabbinic"},
 "ben-zoma": {"name": "Shimon ben Zoma", "he": "בן זומא", "dates": "fl. c. 110–135", "tradition": "rabbinic", "role": "tradent"},
 "r-yehoshua-b-hananya": {"name": "R. Yehoshua ben Ḥananya", "dates": "fl. c. 90–130", "tradition": "rabbinic", "role": "tradent"},
 "resh-lakish": {"name": "R. Shimon ben Lakish", "dates": "c. 200–275", "tradition": "rabbinic", "role": "tradent"},
 "r-hagai": {"name": "R. Ḥaggai", "tradition": "rabbinic", "role": "tradent"},
 "r-pedat": {"name": "R. Pedat", "tradition": "rabbinic", "role": "tradent"},
 "rav-aha-b-yaakov": {"name": "Rav Aḥa bar Yaakov", "tradition": "rabbinic", "role": "tradent"},
 "mar-zutra": {"name": "Mar Zutra", "tradition": "rabbinic", "role": "tradent"},
 "basil": {"name": "Basil of Caesarea", "la": "Basilius Magnus (tr. Eustathius)", "dates": "c. 330–379", "tradition": "greek-christian-in-latin"},
 "syrian-informant": {"name": "The Syrian", "la": "vir quidam genere Syrus", "dates": "before 378", "tradition": "syriac", "role": "informant", "note": "Basil's unnamed source; often identified with Ephrem, without proof."},
 "ambrose": {"name": "Ambrose", "la": "Ambrosius Mediolanensis", "dates": "c. 339–397", "tradition": "latin"},
 "augustine": {"name": "Augustine", "la": "Augustinus Hipponensis", "dates": "354–430", "tradition": "latin"},
 "isidore": {"name": "Isidore of Seville", "dates": "c. 560–636", "tradition": "latin"},
 "bede": {"name": "Bede", "dates": "c. 673–735", "tradition": "latin"},
 "wigbod": {"name": "Wigbod", "la": "Wicbodus", "dates": "fl. c. 790", "tradition": "latin"},
 "alcuin": {"name": "Alcuin", "dates": "c. 735–804", "tradition": "latin"},
 "rabanus": {"name": "Rabanus Maurus", "dates": "c. 780–856", "tradition": "latin"},
 "angelomus": {"name": "Angelomus of Luxeuil", "dates": "d. c. 855", "tradition": "latin"},
 "remigius": {"name": "Remigius of Auxerre", "dates": "c. 841–908", "tradition": "latin"},
 "bruno-of-segni": {"name": "Bruno of Segni", "la": "Bruno Astensis", "dates": "c. 1045–1123", "tradition": "latin"},
 "glossa-ordinaria": {"name": "Glossa ordinaria (school of Laon)", "dates": "c. 1110–1130", "tradition": "latin", "note": "Not Walafrid Strabo."},
 "rupert": {"name": "Rupert of Deutz", "dates": "c. 1075–1129", "tradition": "latin"},
 "abelard": {"name": "Peter Abelard", "dates": "1079–1142", "tradition": "latin"},
 "hugh-of-st-victor": {"name": "Hugh of St Victor", "dates": "c. 1096–1141", "tradition": "latin"},
 "honorius": {"name": "Honorius Augustodunensis", "dates": "c. 1080–1154", "tradition": "latin"},
 "comestor": {"name": "Peter Comestor", "dates": "c. 1100–1178", "tradition": "latin"},
}
PLACES = {
 "alexandria": {"name": "Alexandria", "lat": 31.20, "lon": 29.92},
 "bethlehem": {"name": "Bethlehem", "lat": 31.70, "lon": 35.20},
 "babylonia": {"name": "Babylonia (Sura / Pumbedita)", "lat": 32.5, "lon": 44.4},
 "palestine": {"name": "Palestine", "lat": 32.0, "lon": 35.3},
 "galilee": {"name": "Galilee (Tiberias / Sepphoris)", "lat": 32.79, "lon": 35.53},
 "troyes": {"name": "Troyes", "lat": 48.30, "lon": 4.08},
 "caesarea-cappadociae": {"name": "Caesarea in Cappadocia", "lat": 38.72, "lon": 35.49},
 "milan": {"name": "Milan", "lat": 45.46, "lon": 9.19},
 "thagaste": {"name": "Thagaste", "lat": 36.29, "lon": 7.95},
 "hippo": {"name": "Hippo Regius", "lat": 36.88, "lon": 7.75},
 "seville": {"name": "Seville", "lat": 37.39, "lon": -5.99},
 "jarrow": {"name": "Jarrow", "lat": 54.98, "lon": -1.49},
 "aachen": {"name": "Aachen", "lat": 50.78, "lon": 6.08},
 "tours": {"name": "Tours", "lat": 47.39, "lon": 0.69},
 "fulda": {"name": "Fulda", "lat": 50.55, "lon": 9.68},
 "luxeuil": {"name": "Luxeuil", "lat": 47.82, "lon": 6.38},
 "auxerre": {"name": "Auxerre", "lat": 47.80, "lon": 3.57},
 "segni": {"name": "Segni", "lat": 41.69, "lon": 13.02},
 "laon": {"name": "Laon", "lat": 49.56, "lon": 3.62},
 "liege": {"name": "Liège", "lat": 50.63, "lon": 5.57},
 "paraclete": {"name": "The Paraclete (Nogent-sur-Seine)", "lat": 48.49, "lon": 3.50},
 "paris": {"name": "Paris", "lat": 48.86, "lon": 2.35},
 "regensburg": {"name": "Regensburg", "lat": 49.02, "lon": 12.10},
}
SHORT = "Ruach merahefet"
