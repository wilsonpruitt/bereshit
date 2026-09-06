"""K4 — ex-nihilo-or-matter (Gen 1:1–1:2). Was anything there before?
Built 2026-09-05 (Phase 2, crux 6 of 9). See PHASES.md for the spec-file contract.

K4 is anchored across the two most crowded verses on the site: K1 built 34 witnesses on Gen 1:1,
K6 and K7 between them most of 1:2. Every Latin slice below was checked against every existing
Latin slice on 1:1–1:2 by offset, not by column, before it was written (scratchpad cover.py, the
method note at the end of the K5 entry in notes/SOURCES-FINDINGS.md). Three candidates came back
covered and were dropped: the Glossa's first gloss on 1:2 at 113:69A (inside K1's `glossa-1-1`),
Comestor 198:1055B (inside K5's `comestor-hs-1-1b`), and Ambrose 14:136A (inside K6's
`ambrose-hex-1-7-25`).

Three witnesses already carry this crux from earlier builds — `abelard-hex-1-2` (K7),
`aug-gnl-5-18` and `bonaventure-sent-2-12-1-2` (K10) — and build-crux.py folds them into the
roster. They are not rebuilt here.
"""
import json, pathlib
from bench import ROOT, RAW, latin, sef, hcut, DRAFT, APPROVED, thread

CRUX_ID = "ex-nihilo-or-matter"
SHORT = "out of nothing?"
E = lambda i, f, t, ty, ev: thread(CRUX_ID, i, f, t, ty, ev)

WITNESSES = []
def add(**kw): WITNESSES.append(kw)

PERSONS = {
    "bar-kappara": {"label": "Bar Kappara", "dates": "fl. c. 200–220", "note": "Tanna/amora of the transitional generation; quoted here by Rav Huna."},
    "rabban-gamliel": {"label": "Rabban Gamliel", "dates": "fl. c. 90–110", "note": "Rabban Gamliel II of Yavneh, to whom the philosopher puts the question at Bereshit Rabbah 1:9."},
    "the-philosopher": {"label": "A philosopher", "dates": "unnamed", "note": "The unnamed philosopher of Bereshit Rabbah 1:9, who tells Rabban Gamliel that God found good materials. The rabbinic bench's only speaker for the position the whole Latin bench argues against."},
}

ANSWERS = {
    "de-nihilo": {"label": "Out of nothing", "gloss": "God made the world, and the matter of the world, from nothing whatever."},
    "matter-then-formed": {"label": "Matter first, then formed", "gloss": "Formless matter was created first — first in origin, not in time — and everything else made out of it."},
    "matter-is-coeval": {"label": "Matter was already there", "gloss": "God is a craftsman working on a material he did not make. Reported on both benches, held by neither."},
    "three-principles": {"label": "God, exemplar, matter", "gloss": "The philosophers' three principles without a principle, named as the position to be refuted."},
    "all-of-them-created": {"label": "Of every one of them, creation is written", "gloss": "Each thing the objector calls a pre-existing material has its own verse saying God created it."},
    "bara-is-not-ex-nihilo": {"label": "'Created' does not mean from nothing", "gloss": "The verb bara is used of the sea-creatures and of man, who were made from something."},
    "creare-vs-formare": {"label": "Created, not formed", "gloss": "Scripture keeps two verbs apart: what has no pre-existing matter is created, what is shaped out of matter is formed."},
    "hyle-is-tohu": {"label": "The hyle is tohu", "gloss": "The one created thing is a substance without form, which the Greeks call hyle and Scripture calls tohu."},
    "made-from-something-of-god": {"label": "From the light and the snow", "gloss": "Heaven from the light of his garment, earth from the snow beneath the Throne of Glory."},
    "craftsman-needs-matter": {"label": "A craftsman needs a material", "gloss": "Wood helps the carpenter, silver the silversmith — the analogy that makes creation from nothing unthinkable."},
    "silence-proves-nothing": {"label": "Scripture's silence proves nothing", "gloss": "That Genesis does not say when a thing was made does not make it coeternal with God."},
    "world-from-tohu": {"label": "The world was made out of tohu va-vohu", "gloss": "Said with embarrassment, and only because the verse says it."},
}

LICENSES = {}

# ================================================================ rabbinic bench
_BR_SRC = {"license": "cc-by-sa", "version": "Sefaria 'Wikisource Bereshit Rabbah' (CC BY-SA). Phase 6, 2026-09-05: moved off 'Midrash Rabbah -- TE', whose own site asserts all rights reserved"}
_BR_EN = {"translator": "The Sefaria Midrash Rabbah, 2022", "license": "sefaria-midrash-rabbah", "attribution_required": True}

add(id="br-1-5b", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.1"},
    lemma={"he": "מִנַּיִן הֵן", "en": "From what were they?"},
    original={"lang": "he", "text": hcut(sef("br-1", "he", 4)[0],
                                         "בְּנֹהַג שֶׁבָּעוֹלָם מֶלֶךְ בָּשָׂר וָדָם בּוֹנֶה פָּלָטִין",
                                         "וְהָאָרֶץ הָיְתָה תֹהוּ וָבֹהוּ.", "K4 br-1-5b he"),
              "source": "Bereshit Rabbah 1:5 (Vilna numbering), second half", **_BR_SRC},
    english={"text": hcut(sef("br-1", "en", 4)[0], "The way of the world is that when a flesh-and-blood king",
                          "“The earth was emptiness and disorder” (Genesis 1:2).", "K4 br-1-5b en"), **_BR_EN},
    tradents=["r-huna", "bar-kappara"],
    cruxes=["ex-nihilo-or-matter"], senses=["literal"],
    answers=["world-from-tohu", "matter-then-formed"],
    notes="The rabbinic bench saying the thing the Latin bench spends four centuries denying, and saying it with its eyes shut. The parable first: a king builds his palace over sewers, a refuse heap and a stinking place, and whoever comes and says 'this palace is built over sewers' has insulted him — so too whoever says 'this world was created out of emptiness and disorder' has insulted the King. Then Rav Huna in the name of bar Kappara, and the formula is the formula for saying what may not be said: were the matter not written explicitly it would not be possible to say it — 'In the beginning God created' — from what? 'The earth was emptiness and disorder.' The verse is read as an answer to the question the verse raises, and the answer is that the material was there. Four sections later the same work will make Rabban Gamliel refuse exactly that inference to a philosopher's face. Neither section knows the other is there; the first half of BR 1:5, which forbids expounding what is before the world at all, belongs to K2.")

add(id="br-1-9", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.1"},
    lemma={"he": "אֱלֹהֶיךָ צַיָּר גָּדוֹל הָיָה", "en": "Your God was a great artist"},
    original={"lang": "he", "text": sef("br-1", "he", 8)[0],
              "source": "Bereshit Rabbah 1:9 (Vilna numbering)", **_BR_SRC},
    english={"text": sef("br-1", "en", 8)[0], **_BR_EN},
    tradents=["the-philosopher", "rabban-gamliel"],
    cruxes=["ex-nihilo-or-matter"], senses=["literal"],
    answers=["matter-is-coeval", "all-of-them-created", "craftsman-needs-matter"],
    notes="Six lines, and they contain the whole crux. A philosopher tells Rabban Gamliel: your God was a great artist, but he found good materials to help him — emptiness, disorder, darkness, wind, water, the deeps. The answer is not an argument but a concordance: may that man's spirit depart, of every one of them creation is written. Tohu and bohu from Isaiah 45:7, 'who makes peace and creates evil'; darkness from the same verse; water from Psalm 148:4–5, 'for he commanded and they were created'; wind from Amos 4:13, 'he forms mountains and creates wind'; the deeps from Proverbs 8:24, 'when there were no deeps I was brought forth'. The list is exactly the list of BR 1:5's embarrassment, and the objection is exactly Augustine's fabri and Basil's smith and carpenter — the craftsman who cannot work without a material. The rabbinic bench meets it once, in a chreia, and answers by producing a verse for each item; the Latin bench meets it as a philosophical position and answers with a doctrine of omnipotence. Neither method would satisfy the other.")

add(id="pdre-3-7", work="pdre", author="pirkei-derabbi-eliezer", tradition="rabbinic",
    date=800, date_precision="range-750-850", place="palestine",
    anchor={"verse": "gen.1.1"},
    lemma={"he": "מִשֶּׁלֶג שֶׁתַּחַת כִּסֵּא הַכָּבוֹד", "en": "from the snow beneath the Throne of Glory"},
    original={"lang": "he", "text": [x for x in json.load(open(RAW / "pdre-3.json"))["versions"] if x["language"] == "he"][0]["text"][7],
              "source": "Pirkei de-Rabbi Eliezer 3", "license": "pd", "version": "Sefaria Vocalized Edition"},
    english={"text": "Whence was the earth created? He took of the snow (or ice) which was beneath His Throne of Glory and threw it upon the waters, and the waters became congealed so that the dust of the earth was formed, as it is said, “He saith to the snow, Be thou earth” (Job 37:6).",
             "translator": "Gerald Friedlander, 1916", "license": "pd"},
    cruxes=["ex-nihilo-or-matter"], senses=["literal"],
    answers=["made-from-something-of-god"],
    notes="A cosmogony on the rabbinic bench in which the question 'from what?' has an answer, and the answer is a substance. Heaven from the light of his garment (the preceding section, built at K8 as pdre-3-6); earth from the snow under the Throne of Glory, thrown on the waters and congealed, with Job 37:6 for proof — 'he says to the snow, be earth'. Nothing here is made out of nothing, and nothing here is embarrassed about it: the materials are simply divine ones, taken from what is already God's. The Latin bench has no answer of this shape at all, and could not have: once matter is the thing at issue, a material that belongs to God is still a material, and Basil's objection would fall on it as heavily as on Plato's hyle. The two benches are not disagreeing here; only one of them has heard the question.")

_ie = json.load(open(RAW / "ibn-ezra-gen-1.json"))
def _ie_text(lang, idx):
    v = [x for x in _ie["versions"] if x["language"] == lang][0]["text"][idx]
    return v if isinstance(v, str) else " ".join(v)

add(id="ibn-ezra-1-1c", work="ibn-ezra-gen", author="ibn-ezra", tradition="rabbinic",
    date=1155, date_precision="circa", place="lucca",
    anchor={"verse": "gen.1.1"},
    lemma={"he": "בָּרָא", "en": "created"},
    original={"lang": "he", "text": hcut(_ie_text("he", 0), "ברא רובי המפרשים אמרו", "והמשכיל יבין", "K4 ibn-ezra he"),
              "source": "Ibn Ezra on Gen 1:1, s.v. ברא", "license": "pd", "version": "Piotrkow, 1907–1911"},
    english={"text": hcut(_ie_text("en", 0), "Most commentators have said that creation means",
                          "and the enlightened will understand.", "K4 ibn-ezra en"),
             "translator": "Sefaria Community Translation", "license": "cc0"},
    cruxes=["ex-nihilo-or-matter"], senses=["literal", "translation"],
    answers=["bara-is-not-ex-nihilo"],
    notes="The crux settled by lexicography, against the whole weight of the doctrine. Most commentators, Ibn Ezra says, have held that bara means bringing forth something from nothing, and they cite Numbers 16:30, 'if the Lord create a creation'. But they have forgotten 'and God created the great sea-creatures' (Gen 1:21), and the three occurrences in one verse at Gen 1:27, 'God created man in his image' — and 'who creates darkness' (Isa 45:7), which is the privation of light, and light is something. The verb has two senses, and the second, from 2 Samuel 12:17, is to cut, to set a bounded edge; and the enlightened will understand. Three verses, and two of them are the two Rupert of Deutz answers in Liège forty years earlier — Gen 1:21 and Gen 1:27, in that order — to save the doctrine that Ibn Ezra is dismantling. Note also which verse Ibn Ezra does not need to reach for: Isaiah 45:7 is Rabban Gamliel's first proof text at BR 1:9, brought there to show that tohu and darkness were created; here 'who creates darkness' is brought to show that the verb does not mean what the doctrine requires.")

_ram = json.load(open(RAW / "ramban-gen-1.json"))
def _ram_text(lang):
    v = [x for x in _ram["versions"] if x["language"] == lang][0]["text"][0]
    return v if isinstance(v, str) else " ".join(v)

add(id="ramban-1-1c", work="ramban-gen", author="ramban", tradition="rabbinic",
    date=1267, date_precision="range-1263-1270", place="girona",
    anchor={"verse": "gen.1.1"},
    lemma={"he": "מֵאֲפִיסָה מֻחְלֶטֶת", "en": "from absolute non-existence"},
    original={"lang": "he", "text": hcut(_ram_text("he"), "וְעַתָּה שְׁמַע פֵּרוּשׁ הַמִּקְרָא עַל פְּשׁוּטוֹ נָכוֹן וּבָרוּר",
                                         "וְהַכֹּל נַעֲשִׂים מֵהֶם.", "K4 ramban he"),
              "source": "Ramban on Gen 1:1, s.v. בראשית (the hyle)", "license": "sefaria-vocalized", "version": "Sefaria 'Vocalized Edition'"},
    english={"text": hcut(_ram_text("en"), "Now listen to the correct and clear explanation of the verse in its simplicity.",
                          "they alone were created, and everything else was constructed from them.", "K4 ramban en"),
             "translator": "Charles B. Chavel, 1971–76", "license": "chavel-ramban"},
    cruxes=["ex-nihilo-or-matter"], senses=["literal"],
    answers=["de-nihilo", "hyle-is-tohu", "matter-then-formed"],
    notes="The rabbinic bench's fullest statement of creation out of nothing, and it is built on the Latin schools' distinction without naming them. The Holy One created all things from absolute non-existence; and there is no expression in the sacred tongue for bringing forth something from nothing except the word bara. Then the qualification that makes the doctrine survive the objection: nothing under the sun or above it was made from non-existence at the outset — what was brought forth from the utter nothing was a very thin substance, without corporeality, having a power of potency, fit to receive form and to pass from potentiality into act; the primary matter, which the Greeks call hyly. After the hyly he created nothing, but formed and made. Two substances only were created, one for the heavens and one for the earth, and everything else was constructed from them. That is Hugh of St Victor's chapter one — God not only made all things out of matter but created the matter of all things out of nothing — reached in Girona a century and a half later with the Greek word intact and no Latin in sight. And the first sentence is aimed at a named man: R. Abraham is Ibn Ezra, quoted and answered a few lines above, who had denied precisely that bara carries the sense Ramban here says it alone carries. Chavel's English shows on Sefaria as CC BY; licence key chavel-ramban is marked for checking before publication.")

# ================================================================ latin bench, patristic
add(id="basil-hex-2-2-materia", work="basil-hex-lat", author="basil", tradition="latin",
    date=400, date_precision="circa", place="caesarea-cappadociae",
    anchor={"verse": "gen.1.2"},
    lemma={"la": "Quam si dixerimus ingenitam, sine dubio coaequari Deo", "en": "If we call it unbegotten, it is beyond doubt made equal to God"},
    original=latin("7608", "Sed obtrectatores veritatis, sensu proprio Scripturas minime consequentes",
                   "Non enim schematum repertor est Deus, sed totius naturae creator.", 53),
    english={"text": "But the detractors of the truth, in no way following the Scriptures in their proper sense and dragging their interpretation to their own judgement, say that by words of this kind the matter of things is shown — matter which was as it were by nature invisible and unordered and formless, and deprived of every appearance and figure, which the craftsman took up and shaped according to his wisdom, and so through it made all the things that are seen. If we call this matter unbegotten, it is beyond doubt made equal to God when it is weighed in the honours it deserves, and it will be judged worthy of the same privileges as he. And what could be more wicked and more criminal than that a thing confused and utterly deformed should be judged endowed with a dignity equal to the wise and powerful and exceedingly good God, the founder of all? Then, if it is so great that it can take in the whole divine discipline, they will nonetheless be seen to make its substance equal to God's power — if indeed the earth is able of itself to measure out the whole wisdom of God. But if matter is less than the divine power, their argument is drawn into a still more atrocious blasphemy; for they try to assert that God is ineffectual and idle in his works because of a poverty of matter. It is the neediness of human nature that deceived them into thinking such things. For with us each art is exercised upon some matter brought to it — smithcraft upon iron, carpentry upon wood — and in these one thing is what underlies, another the form, another what is made out of the form: for matter is what is taken from outside, the form is what the art produces, and the finished thing is what is composed of both, that is, of the form and the matter. So they suppose it is with the divine working too: that the figure was brought to the world out of the wisdom of its founder, but the matter was subjected to the creator from outside; and that the whole world was so constructed, possessing its substance sought from elsewhere, but its figure and shape received from the power of God. […] But God, before the things that are seen came to be, embracing all things in his mind and willing to bring to birth the things that were not, considered what kind of world it ought to be, and generated along with it a matter suited to its form. To heaven he assigned the nature befitting it, and to the shape of the lands he furnished the substance owed to them. Fire and water and air he distinguished as he willed, and led into the order that the account of each demanded. […] Let them cease, then, to handle with fabulous inventions and with the wretched sense of their own thoughts a power incomprehensible to the mind and unspeakable in human words. God made heaven and earth, not each of them by half, but a whole heaven and a whole earth, that is, the very substance taken together with its form. For God is not the deviser of figures, but the creator of the whole nature.", **APPROVED},
    cruxes=["ex-nihilo-or-matter"], senses=["literal"],
    answers=["de-nihilo", "matter-is-coeval", "craftsman-needs-matter"],
    notes="The Greek bench's answer, and the argument it refutes is the philosopher's at Bereshit Rabbah 1:9 stated as a philosophy. Those who read 'invisible and unordered' as a description of an unbegotten matter make that matter God's equal in honour, since whatever is unbegotten shares his privilege; and if the matter is instead less than God, they have made God poor. Then the diagnosis, and it is the same analogy the philosopher used and Augustine will use: with us every art works on a material brought to it, smithcraft on iron and carpentry on wood, so that the finished thing is composed of a form supplied by the art and a substance supplied from outside — and they project this on the divine working, giving God the shape of the world and someone else the stuff of it. Basil's answer is that God generated the matter along with the form it was to have, and made not half of heaven and half of earth but the whole substance with its form: he is not the deviser of figures but the creator of the whole nature. The paragraph before this one is K6's basil-hex-2-4. Two elisions are marked in the English: at PL 53:881B, 'Hinc illis datur occasio … commoditatem nobis non parvam contulit', where Basil argues that the human arts came after their materials (wool before weaving, wood before the adze) and that God's making is the reverse; and at PL 53:881C, 'Totum autem mundum … permixtione mutua copulata credantur', on the bonds of concord that hold the unlike world together. The Latin excerpt is continuous.")

add(id="ambrose-hex-1-1-hyle", work="ambrose-hex", author="ambrose", tradition="latin",
    date=387, date_precision="circa", place="milan",
    anchor={"verse": "gen.1.1"},
    lemma={"la": "de materia, quam vocant hylen", "en": "out of the matter which they call hyle"},
    original=latin("6958", "Tantumne opinionis assumpsisse homines", "quod adoriundum putasset.", 14),
    english={"text": "Have men taken up so much opinion that some of them set up three principles of all things — God, and the exemplar, and matter — and asserted that these are incorruptible and uncreated and without beginning, as Plato and his disciples do; and that God made the world not as the creator of matter but as a craftsman looking to an exemplar, that is, to an idea, out of the matter which they call hyle, which is said to have given the causes of generation to all things; and thought the world itself too incorruptible, neither created nor made? Others also, as Aristotle with his followers thought fit to argue, laid down two principles, matter and form, and a third along with them, which is called operative, to which it should belong to bring about fitly what it had judged should be undertaken.", **APPROVED},
    cruxes=["ex-nihilo-or-matter", "why-begin-here"], senses=["literal"],
    answers=["three-principles", "matter-is-coeval"],
    notes="The opening sentence of the Hexaemeron, and the whole Latin bench's account of the opposition is settled in it. Plato: three principles, God and the exemplar and matter, all three incorruptible, uncreated and without beginning, with God a craftsman looking to an idea rather than the maker of the stuff — and the stuff is named, hyle. Aristotle: two principles, matter and form, with a third operative one. Every later Latin witness on this crux repeats one or both lists, usually without naming Ambrose: Remigius has the three at PL 131:53D (K1 sliced it), Hugh of St Victor has them as opifex, materia and forma, Comestor has all three philosophers with Epicurus added and hyle spelt ile. What none of them repeats is the reason Ambrose gives immediately afterwards for Moses' having written as he did — that passage is at PL 14:124B and was built for K1 as ambrose-hex-1-2, so this crux takes the doxography and leaves the answer where it stands.")

add(id="aug-conf-12-7", work="aug-conf", author="augustine", tradition="latin",
    date=398, date_precision="range-397-401", place="hippo",
    anchor={"verse": "gen.1.1"},
    lemma={"la": "unum prope te, alterum prope nihil", "en": "one near to you, the other near to nothing"},
    original=latin("7270", "Et unde utcumque erat, nisi esset abs te", "alterum, quo inferius nihil esset.", 32),
    english={"text": "And whence had it any being at all, unless it were from you, from whom are all things in whatever measure they are? Yet the further from you the more unlike — and not by places. And so you, Lord, who are not one thing at one time and another otherwise, but the selfsame and the selfsame and the selfsame, Holy, Holy, Holy, Lord God almighty (Isa 6:3): in the Beginning which is from you, in your Wisdom which was born of your substance, you made something, and made it out of nothing. For you made heaven and earth; not out of yourself, for then it would be equal to your Only-begotten and thereby to you, and it would in no way be just that what was not out of you should be equal to you. And there was nothing else besides you out of which you might make them, God, one Trinity and threefold Unity: and therefore you made heaven and earth out of nothing, a great something and a small something; since you are almighty and good, to make all things good, a great heaven and a small earth. You were, and there was nothing else out of which you made heaven and earth, two somethings: one near to you, the other near to nothing; one than which you alone were higher, the other than which nothing was lower.", **APPROVED},
    cruxes=["ex-nihilo-or-matter"], senses=["literal"],
    answers=["de-nihilo", "matter-then-formed"],
    notes="The doctrine argued as a dilemma with two horns and no third. Whatever is, is from God; but heaven and earth are not made out of God, for what is out of God is the Only-begotten and equal to him; and there was nothing else besides God out of which to make them; therefore they were made out of nothing. Then the phrase that the rest of Book XII turns on: two somethings, one near to God and one near to nothing — the heaven of heaven and the formless matter — one than which God alone is higher, one than which nothing is lower. Augustine will not say that the matter is nothing, and he will not say that it is something in its own right; prope nihil is a position built to be unavailable to both objections at once. Bereshit Rabbah 1:5 stands at the same place and does not have the phrase, and so has to say the thing plainly and apologise for it.")

add(id="aug-conf-12-22", work="aug-conf", author="augustine", tradition="latin",
    date=398, date_precision="range-397-401", place="hippo",
    anchor={"verse": "gen.1.2"},
    lemma={"la": "cur non informem quoque illam materiem … a Deo factam esse de nihilo", "en": "why should we not understand that the formless matter too was made by God out of nothing"},
    original=latin("7270", "Unde si aliquid Genesis tacuit Deum fecisse", "omiserit enuntiare ista narratio?", 32),
    english={"text": "Hence if Genesis has passed over in silence something that God made — which nevertheless neither sound faith nor sure understanding doubts that God made — no sober teaching will on that account dare to say that those waters are coeternal with God, merely because we have heard them mentioned in the book of Genesis but do not find where they were made. Why then should we not understand, with truth teaching us, that the formless matter also, which this Scripture calls the invisible and unordered earth and the dark deep, was made by God out of nothing, and is therefore not coeternal with him — although this narrative has omitted to state where it was made?", **APPROVED},
    cruxes=["ex-nihilo-or-matter"], senses=["literal"],
    answers=["de-nihilo", "silence-proves-nothing"],
    notes="The argument that had to be made because the doctrine has no verse. Genesis never says that God made the formless matter, and the objection from that silence is real; Augustine answers it with a second silence in the same chapter. The waters above the firmament are mentioned and their making is never narrated either, and nobody is willing to call them coeternal with God — so the silence cannot be what decides. It is exactly the ground the philosopher takes at Bereshit Rabbah 1:9, and Rabban Gamliel's answer is the opposite method: not an argument about what silence can prove, but a verse produced for each item on the list, tohu from Isaiah, darkness from Isaiah, the waters from the Psalm, the wind from Amos, the deeps from Proverbs. Augustine has the more general answer and Rabban Gamliel the more convincing one, and neither could have used the other's.")

add(id="aug-gnm-1-6-10", work="aug-gnm", author="augustine", tradition="latin",
    date=389, date_precision="range-388-389", place="thagaste",
    anchor={"verse": "gen.1.1"},
    lemma={"la": "cum considerant fabros et quoslibet opifices non posse aliquid fabricare, nisi habuerint unde fabricent",
           "en": "when they consider that craftsmen and workmen of any kind cannot make anything unless they have something to make it from"},
    original=latin("7303", "Et ideo Deus rectissime creditur omnia de nihilo fecisse", "quod sacrilegum est credere.", 34),
    english={"text": "And therefore God is most rightly believed to have made all things out of nothing: because even if all formed things were made out of that matter, that matter itself was made out of nothing at all. For we ought not to be like those who do not believe that almighty God could make anything out of nothing, when they consider that craftsmen and workmen of any kind cannot make anything unless they have something to make it from. For wood helps the craftsman, and silver helps the silversmith, and gold the goldsmith, and earth helps the potter to be able to finish his works. If they are not helped by that matter out of which they make something, they can make nothing, since they do not themselves make the matter. For the craftsman does not make the wood, but makes something out of wood: and so all other workmen of this kind. But almighty God had no need to be helped by any thing that he had not himself made, in order to bring about what he willed. For if some thing that he had not himself made helped him towards the things he willed to make, he was not almighty: which it is sacrilege to believe.", **APPROVED},
    cruxes=["ex-nihilo-or-matter"], senses=["literal"],
    answers=["de-nihilo", "craftsman-needs-matter", "matter-then-formed"],
    notes="The chapter Migne heads 'Formless matter out of nothing, and out of it all things', and the argument in it is the one this whole crux turns on. Augustine grants that everything formed was made out of the formless matter and then puts the doctrine one step further back: the matter itself was made out of nothing at all. The objection he answers is not a text but a habit of mind — people cannot believe God made anything out of nothing because they are watching craftsmen, and wood helps the carpenter, silver the silversmith, gold the goldsmith, earth the potter. It is the philosopher's sentence at Bereshit Rabbah 1:9 with the trades filled in, made in Thagaste sixty years before the Galilean compilation and independently of it; and the refutation turns on omnipotence rather than on Scripture — if anything God had not made helped him, he was not almighty. Wigbod copies this chapter to the last clause, and Angelomus rewrites it with the trades kept and the source dropped.")

add(id="bede-gen-1-2-materia", work="bede-gen", author="bede", tradition="latin",
    date=720, date_precision="range-717-725", place="jarrow",
    anchor={"verse": "gen.1.2"},
    lemma={"la": "vel de ipsis exordium naturae, vel sumpsere de nihilo", "en": "either took the beginning of their nature from these, or took it out of nothing"},
    original=latin("8466", "Ad haec tantum informis est illa materies", "unde formositatem haberent non erat.", 91),
    english={"text": "Only to this extent is that matter formless out of which Scripture testifies that the world was made, when it says in the praises of God: 'You who made the world out of formless matter' (Wis 11:17). For all the things which we are accustomed to see in the world along with the waters and the earth either took the beginning of their nature from these, or took it out of nothing; but the earth itself and the waters themselves have received the name of formless matter for this reason, that before they came into the light there was nothing from which they might have comeliness.", **APPROVED},
    cruxes=["ex-nihilo-or-matter"], senses=["literal"],
    answers=["matter-then-formed", "pair-is-formless-matter"],
    notes="Bede taking the sting out of the word. Wisdom 11:17 says the world was made out of formless matter, and the whole Latin difficulty is in that verse: it appears to concede the philosopher's point in Scripture's own voice. Bede's answer is a restriction — the matter is formless only to this extent, that the earth and the waters had nothing to give them comeliness until the light came — so that 'formless matter' names two visible things at a stage of their history, not a substrate. And the sentence that follows keeps both possibilities open without choosing: what we see either began from the earth and the waters, or was taken out of nothing. Rabanus copies this paragraph verbatim at PL 107:446C and the Glossa prints it condensed at 113:69D–70A, which is where most readers after 1150 met it.")

add(id="alcuin-int-19-20", work="alcuin-int", author="alcuin", tradition="latin",
    date=796, date_precision="circa", place="tours",
    anchor={"verse": "gen.1.1"},
    lemma={"la": "Quae creaturae de nihilo factae sunt?", "en": "Which creatures were made out of nothing?"},
    original=latin("21416", "Inter. 19. Quot modis est operatio divina?", "anima hominis.", 100),
    english={"text": "Question 19. In how many ways is the divine working? — Answer. Four. First, that in the dispensation of the Word of God all things are eternal. Second, that in formless matter he who lives for ever created all things at once (Sir 18:1). Third, that through the works of the six days he distinguished the various creatures. Fourth, that out of the primordial seeds natures do not arise unknown, but known ones are more often re-formed, lest they perish. Question 20. Which creatures were made out of nothing? — Answer. Heaven, earth, angels, light, air, water, and the soul of man.", **APPROVED},
    cruxes=["ex-nihilo-or-matter"], senses=["literal"],
    answers=["de-nihilo", "matter-then-formed", "simul"],
    notes="The crux turned into a list a pupil can memorise, and the list is the Latin bench's only counterpart to the rabbinic enumerations. Seven items made out of nothing: heaven, earth, angels, light, air, water, the soul of man. Set it beside Rav Yehudah in Rav's name at b. Chagigah 12a — ten things created on the first day: heaven and earth, chaos and desolation, light and darkness, wind and waters, the measure of the day and the measure of the night — and beside Pirkei de-Rabbi Eliezer 3's eight, and the shape of the answer is identical while the contents diverge exactly where the doctrines diverge. Alcuin's list has angels and the human soul on it, which no rabbinic list has; the rabbinic lists have tohu and bohu on them, which is the one thing Alcuin's question is designed to exclude. The four modes in question 19 are Augustine's, with Sirach 18:1 for the second, and they are what makes the list possible: 'created all things at once' in formless matter is the mode under which the seven are all made out of nothing together.")

# ================================================================ latin bench, Carolingian
add(id="wigbod-gen-1-1c", work="wigbod-gen", author="wigbod", tradition="latin",
    date=790, date_precision="circa", place="luxeuil",
    anchor={"verse": "gen.1.1"},
    lemma={"la": "Non enim faber facit lignum, sed de ligno aliquid facit", "en": "For the craftsman does not make the wood, but makes something out of wood"},
    original=latin("8606", "Et ideo Deus rectissime creditur omnia de nihilo fecisse", "quod sacrilegum est credere.", 96),
    english={"text": "And therefore God is most rightly believed to have made all things out of nothing: because even if all formed things were made out of that matter, that matter itself was made out of nothing. For we ought not to be like those who do not believe that almighty God could make anything out of nothing, when they consider that craftsmen and workmen of any kind cannot make anything unless they have something to make it from. For wood helps the craftsman, and silver helps the silversmith, and gold the goldsmith, and earth helps the potter to be able to finish his works. If they are not helped by that matter out of which they make something, they can make nothing, since they themselves do not make the matter. For the craftsman does not make the wood, but makes something out of wood: and so all other workmen. But almighty God had no need to be helped by any thing that he had not himself made, in order to bring about what he willed; for if some thing that he had not himself made helped him towards the things he willed to make, he was not almighty: which it is sacrilege to believe.", **APPROVED},
    cruxes=["ex-nihilo-or-matter"], senses=["literal"],
    answers=["de-nihilo", "craftsman-needs-matter"],
    notes="Wigbod copying Augustine, and this time he copies everything. At K1 his method was the interesting thing about him: he takes over Jerome's discussion of 'in the beginning' and drops precisely the sentence in which Jerome refutes the reading 'in the Son' from the Hebrew, so that the objection survives in the Carolingian schools and the answer does not. Here he takes over De Genesi contra Manichaeos I.6.10 without losing a clause — the four trades, the wood that the carpenter does not make, the argument from omnipotence, the word sacrilegium at the end. What he drops in the one place and keeps in the other is a fair index of what a Carolingian compiler thought was load-bearing: philology about a Hebrew word is expendable, an argument that secures omnipotence is not. He reads 'de nihilo facta est' where Augustine has 'de omnino nihilo'.")

add(id="angelom-gen-1-1c", work="angelom-gen", author="angelomus", tradition="latin",
    date=850, date_precision="circa", place="luxeuil",
    anchor={"verse": "gen.1.1"},
    lemma={"la": "Ista propterea dicunt, quia attendunt fabrum, et non Deum", "en": "They say these things because they attend to the craftsman and not to God"},
    original=latin("9032", "Deus enim ex nihilo condidit informem materiam", "ut quod volebat efficeret, alioquin Deus non esset.", 115),
    english={"text": "For God founded formless matter out of nothing, and out of it created all things, according to what is written in the book of Wisdom: 'For your hand, Lord, was not powerless, which created the world out of formless matter' (Wis 11:17). Whence the philosophers, as has already been said, not being able to penetrate how the divine Wisdom created the world out of nothing, reckoned the world to be coeternal. They say these things because they attend to the craftsman and not to God. For they say: wood helps the craftsman, and silver the silversmith, and gold the goldsmith. Yet although they need these, they cannot create. But the Lord needed none of these, and founded all things out of formless matter, not outside himself as a craftsman does — for the craftsman does not make the wood, but makes something out of wood. And the almighty had no need to be helped by any thing that he had not himself made in order to bring about what he willed; otherwise he would not be God.", **APPROVED},
    cruxes=["ex-nihilo-or-matter"], senses=["literal"],
    answers=["de-nihilo", "craftsman-needs-matter", "matter-then-formed"],
    notes="Augustine's argument rewritten, and the rewriting turns it into a report of a debate. Where Augustine says 'we ought not to be like those who…', Angelomus says 'they say these things because they attend to the craftsman and not to God' and then quotes them: aiunt enim, lignum adjuvat fabrum, et argentum argentarium, et aurum aurificem. The objection has become a speech with a speaker, which is the form it has at Bereshit Rabbah 1:9 and nowhere else on the Latin bench — and, as there, the speaker is a philosopher and is not named. Angelomus adds the diagnosis Augustine does not give: it is because they could not penetrate how Wisdom created the world out of nothing that they concluded the world is coeternal. The paragraph immediately before this one is his analogy of sound and song for how formless matter precedes the formed creature in origin only, not in time; the one immediately after is Augustine's question about why the verse does not say 'let there be', which K5 built as angelom-gen-1-1b.")

add(id="glossa-1-2-materia", work="glossa", author="glossa-ordinaria", tradition="latin",
    date=1120, date_precision="compilation-1110-1130", place="laon",
    anchor={"verse": "gen.1.2"},
    lemma={"la": "Ipsa autem terra et aqua informis dicuntur materia", "en": "But the earth itself and the water are called formless matter"},
    original=latin("8950", "(BEDA ubi supra.) « Tenebrae erant, »", "non erat unde formam haberent.", 113),
    english={"text": "(Bede, in the place cited.) 'There was darkness,' etc. Those are not to be listened to who say by way of reproach that God created darkness before light: for he made no darkness in the water or the air; but by a distinct order of providence he first created the waters together with heaven, and the earth, and adorned them with the grace of light when he willed. And note that with heaven two elements of the world were created, into which two others were inserted, namely water and earth, in which are fire and air. The waters covered the whole surface of the earth to such a height that they reached to those places where they still in part remain above the firmament. But the earth itself and the water are called formless matter, because all the things we see either took their beginning out of these, or out of nothing: and before they came into the light there was nothing from which they might have form.", **APPROVED},
    cruxes=["ex-nihilo-or-matter"], senses=["literal"],
    answers=["matter-then-formed", "pair-is-formless-matter"],
    notes="The third of the Glossa's marginal glosses on Gen 1:2, Bede again, and it is the only place in the Glossa on this verse where formless matter is defined. Bede's paragraph at PL 91:15C is here cut to its last two sentences and lightly rewritten — 'omnia quae videmus, vel ex istis sumpserunt exordium, vel ex nihilo' for Bede's 'cuncta quae cum aquis et terra videre solemus in mundo, vel de ipsis exordium naturae, vel sumpsere de nihilo' — and the qualification that made Bede's sentence careful, that the matter is formless only to this extent, is gone with the sentence that carried it. What a twelfth-century reader met in the margin, then, is the flat statement that earth and water are called formless matter, with the alternative 'or out of nothing' still attached and no longer doing any work. The first half of this gloss, on the darkness, belongs to K9; the two glosses printed before it on the same lemma are K6's glossa-1-2-terra and the Strabo gloss carried inside K7's glossa-1-2-ruach.")

# ================================================================ latin bench, twelfth century
add(id="rupert-gen-1-1c", work="rupert-gen", author="rupert", tradition="latin",
    date=1115, date_precision="range-1112-1117", place="liege",
    anchor={"verse": "gen.1.1"},
    lemma={"la": "Quod si quis objiciat hominem quoque, cum non de nihilo, sed de terra factus sit, creatum dici",
           "en": "But if anyone should object that man too, though made not out of nothing but out of the earth, is said to be created"},
    original=latin("10873", "Quod si quis objiciat hominem quoque", "subsecutus terram exprimit: Terra autem erat inanis et vacua.", 167),
    english={"text": "But if anyone should object that man too, though made not out of nothing but out of the earth, is said to be created — as it is written, 'And God created man to his own image; to the image of God he created him' (Gen 1:27); or again what is likewise said, 'And God created the great sea-creatures' (Gen 1:21) — we say to this that it is rightly said, but in this respect only, that the matter out of which those forms were produced or taken had already been created. And by these names, that is heaven and earth, as was said above, the whole creation visible and invisible together is signified. That nothing is excepted is proved from the apostolic creed also, in which we say: I believe in God the Father almighty, creator of heaven and earth — adding nothing of the creatures; we do not doubt that under these names we have taken in all things visible and invisible together. For in the other creed of the catholic faith no less, when we say: I believe in one God the Father almighty, maker of heaven and earth, at once, explaining what we have said by heaven and earth, we add: of all things visible and invisible. Therefore what is said, 'in the beginning God created heaven and earth', is the same as if it were said: through his Son, God the Father created the whole substance of all things visible and invisible, such as yet as the earth that follows expresses: 'But the earth was empty and void.'", **APPROVED},
    cruxes=["ex-nihilo-or-matter"], senses=["literal"],
    answers=["de-nihilo", "creare-vs-formare", "bara-is-not-ex-nihilo"],
    notes="A Latin abbot meeting the objection from usage and answering it with a distinction, forty years before Ibn Ezra meets the same objection from the same verses and lets it stand. The objection: Scripture uses creavit of man, who was made out of the earth (Gen 1:27), and of the sea-creatures (Gen 1:21) — so the verb cannot carry the sense the doctrine needs. Rupert's answer is that the word is rightly used there, but only in the respect that the matter from which those things were shaped had itself already been created; the verb reaches back through the shaping to the creation of the stuff. He then secures the scope of Gen 1:1 from the creeds rather than from Genesis: creatorem coeli et terrae in the apostolic creed adds nothing after it, and the other creed glosses the pair as visibilium omnium et invisibilium. Ibn Ezra brings Gen 1:21 and Gen 1:27 in that same order and concludes instead that bara simply has a second sense. The sentence immediately before this one, in which Rupert refuses the philosophers' coeval hyle by name, is inside the slice K1 built as rupert-gen-1-1.")

add(id="abelard-hex-1-1c", work="abelard-hex", author="abelard", tradition="latin",
    date=1130, date_precision="circa", place="paraclete",
    anchor={"verse": "gen.1.1"},
    lemma={"la": "creari proprie id dicitur, quod de non esse ita ad esse producitur, ut praejacentem non habeat materiam",
           "en": "that is properly said to be created which is so brought forth from non-being to being that it has no pre-existing matter"},
    original=latin("11118", "Bene autem de elementis dictum est, creavit, potius quam formavit", "tunc rectissime formari dicitur.", 178),
    english={"text": "And it is well said of the elements 'created' rather than 'formed', because that is properly said to be created which is so brought forth from non-being to being that it has no pre-existing matter, and did not first subsist in any state of nature. But when something is made out of matter already prepared, by the joining on of a form, that is rightly said to be formed — as is what is set down in what follows: 'The Lord God therefore formed man of the slime of the earth' (Gen 2:7). And again: 'All the animals of the earth therefore having been formed out of the ground' (Gen 2:19). For when a pre-existing matter is denoted — as when 'out of the ground' is put first, since it was to be formed into some appearance — then a thing is most rightly said to be formed.", **APPROVED},
    cruxes=["ex-nihilo-or-matter"], senses=["literal", "translation"],
    answers=["creare-vs-formare", "de-nihilo"],
    notes="The distinction stated as a rule about two Latin verbs, and the rule is exactly what Ibn Ezra denies about the one Hebrew verb underlying both. Creare is properly said of what is brought from non-being to being with no pre-existing matter and no prior state of nature; formare of what is made out of matter already prepared by the joining on of a form. The proof is the usage of Genesis itself: formavit hominem de limo terrae at 2:7, formatis de humo cunctis animantibus at 2:19 — where the material is named first, the verb is formavit. Abelard is reading a Latin translation, and the two verbs he separates render two different Hebrew verbs at 2:7 and 2:19 but not at 1:21 and 1:27, where the Hebrew has bara and the Latin has creavit of things made out of something. That is the gap Rupert closes with a distinction and Ibn Ezra widens into a lexical entry, and none of the three has read either of the others.")

add(id="hugh-sacr-1-1-nihilo", work="hugh-sacr", author="hugh-of-st-victor", tradition="latin",
    date=1134, date_precision="range-1130-1137", place="paris",
    anchor={"verse": "gen.1.1"},
    lemma={"la": "non solum ex materia fecit, sed materiam omnium ipse de nihilo creavit",
           "en": "he not only made them out of matter, but himself created the matter of all things out of nothing"},
    original=latin("11082", "In principio creavit Deus coelum et terram (Gen. I) . Quod creatum est de nihilo factum est.",
                   "sed materiam omnium ipse de nihilo creavit.", 176),
    english={"text": "'In the beginning God created heaven and earth' (Gen 1:1). What was created was made out of nothing. For what was made out of something was indeed made, but was not created, because it was not made out of nothing. God therefore made heaven and earth; and not only made but created, that is, made out of nothing. The philosophers of the gentiles laid down three principles of things without a principle: the workman, matter, and form — professing that all the things that were made were brought forth out of matter into form through the workman. But they professed God to be only a maker and not a creator. The true faith, however, confesses one only first principle, which always was; and through it alone it came about that what once was not should be. And the power of his unspeakable omnipotence, just as it could not have anything coeternal besides itself by which it might be helped in making, so it had at hand, when it willed, that what it willed and when and how much it willed should be created out of nothing. All things therefore that were made, God not only made out of matter, but himself created the matter of all things out of nothing.", **APPROVED},
    cruxes=["ex-nihilo-or-matter", "why-begin-here"], senses=["literal"],
    answers=["de-nihilo", "creare-vs-formare", "three-principles"],
    notes="The first chapter of the first book of De sacramentis, which is to say that when the Latin bench organises itself into a systematic theology this crux is where it starts. The chapter title is the thesis: that there is one principle from which all things were made out of nothing. Then the distinction as a definition — what was made out of something was made but not created — followed by the doxography Ambrose opened the Hexaemeron with, now compressed to three words, opifex, materia, forma, and given its precise consequence: those philosophers professed God to be a maker and not a creator. The move that closes it is Augustine's, that nothing coeternal could help him in the making. Ramban reaches the same last sentence in Girona a century and a quarter later — two substances only were created, and everything else was constructed from them — from the Hebrew of the verb and a Greek word for the matter, and with nothing of this in front of him.")

add(id="comestor-hs-1-1c", work="comestor-hs", author="comestor", tradition="latin",
    date=1170, date_precision="range-1169-1175", place="paris",
    anchor={"verse": "gen.1.1"},
    lemma={"la": "Cum vero dixit Moyses, creavit trium errores elidit", "en": "But when Moses said 'created', he struck down the errors of three men"},
    original=latin("11575", "Cum vero dixit Moyses, creavit trium errores elidit", "alios in aera, alios in ignem.", 198),
    english={"text": "But when Moses said 'created', he struck down the errors of three men: Plato, Aristotle, and Epicurus. Plato said that three things were from eternity, namely God, the ideas, and hyle, and that in the beginning of time the world was made out of hyle. Aristotle said two, the world and the workman, who worked out of two principles, namely matter and form, without a beginning, and works without an end. Epicurus said two, the void and the atoms: and in the beginning nature solidified certain atoms into earth, others into water, others into air, others into fire.", **APPROVED},
    cruxes=["ex-nihilo-or-matter"], senses=["literal"],
    answers=["three-principles", "matter-is-coeval"],
    notes="Ambrose's doxography at the end of its Latin life, in the textbook every thirteenth-century student read. Three named opponents now instead of two, with Epicurus added and given the void and the atoms; and the whole apparatus hangs on a single word of the verse — cum vero dixit Moyses, creavit. Plato's three are God, the ideas and hyle, which Migne prints ile. What follows immediately is the sentence K1 built as comestor-hs-1-1, in which Moses prophesied God alone eternal and the world created without pre-existing matter, so this crux and that one hold the two halves of one paragraph: the errors here, the answer there.")

# ================================================================ threads
THREADS = [
    # --- the craftsman argument, across three benches
    E("t-k4-01", "br-1-9", "aug-gnm-1-6-10", "parallel",
      "The philosopher: 'Your God was a great artist, but he found good materials that helped him.' Augustine: 'those who do not believe that almighty God could make anything out of nothing, when they consider that craftsmen and workmen cannot make anything unless they have something to make it from … wood helps the craftsman, silver the silversmith.' The same inference from the same analogy, and the verb is the same in both — the materials help. Thagaste 389, Galilee c. 450, no contact."),
    E("t-k4-02", "br-1-9", "basil-hex-2-2-materia", "parallel",
      "Basil diagnoses the position the philosopher states: 'with us each art is exercised upon some matter brought to it — smithcraft upon iron, carpentry upon wood … so they suppose it is with the divine working too.' Two trades where the midrash has none and Augustine has four, and the same conclusion drawn about God's poverty."),
    E("t-k4-03", "aug-gnm-1-6-10", "basil-hex-2-2-materia", "parallel",
      "Both answer the craftsman analogy by denying that God receives anything from outside: Basil, 'God is not the deviser of figures but the creator of the whole nature'; Augustine, 'if some thing that he had not himself made helped him, he was not almighty'. Augustine did not read Eustathius' Latin Basil in 389, and the arguments differ in kind — Basil's from the dignity of the unbegotten, Augustine's from omnipotence."),
    E("t-k4-04", "wigbod-gen-1-1c", "aug-gnm-1-6-10", "transmits",
      "Verbatim to the last clause, including the four trades and 'quod sacrilegum est credere'; Wigbod reads 'de nihilo facta est' where Augustine has 'de omnino nihilo'. Wigbod does not name Augustine here, though he names Jerome elsewhere in the same work."),
    E("t-k4-05", "angelom-gen-1-1c", "aug-gnm-1-6-10", "echoes",
      "'Aiunt enim: Lignum adjuvat fabrum, et argentum argentarium, et aurum aurificem … non enim faber facit lignum, sed de ligno aliquid facit' — Augustine's clauses reused without his name and recast as reported speech, with the potter dropped and a diagnosis added ('quia attendunt fabrum, et non Deum')."),
    # --- the doxography of the philosophers
    E("t-k4-06", "hugh-sacr-1-1-nihilo", "ambrose-hex-1-1-hyle", "echoes",
      "Ambrose: 'tria principia constituerent omnium, Deum, et exemplar, et materiam … de materia, quam vocant hylen'. Hugh: 'Philosophi gentilium tria quaedam rerum principia sine principio posuerunt: opificem, materiam et formam.' The same three-item list with the same qualification (without a principle / uncreated and without beginning), abbreviated to single words and unattributed."),
    E("t-k4-07", "comestor-hs-1-1c", "ambrose-hex-1-1-hyle", "echoes",
      "'Plato dixit tria fuisse ab aeterno, scilicet Deum ideas, ile' is Ambrose's 'Deum, et exemplar, et materiam … quam vocant hylen' with exemplar resolved into ideae, and Aristotle's two principles, materia et forma, follow in the same order. Epicurus is Comestor's addition."),
    E("t-k4-08", "basil-hex-2-2-materia", "ambrose-hex-1-1-hyle", "parallel",
      "The same position described from the two sides of the Latin/Greek divide within about fifteen years: Ambrose names it (Plato's three principles, hyle uncreated) and Basil argues against it without naming anyone ('if we call this matter unbegotten it is made equal to God'). Ambrose knew Basil's Greek Hexaemeron; this Latin Basil is Eustathius' later version, so the Latin words are not a source for Ambrose's."),
    # --- what the verb means
    E("t-k4-09", "ibn-ezra-1-1c", "rupert-gen-1-1c", "parallel",
      "The same objection from the same two verses, in the same order, answered in opposite directions. Rupert: 'if anyone should object that man too … is said to be created — as it is written, God created man to his own image … or again, God created the great sea-creatures'. Ibn Ezra: 'they have forgotten And God created the crocodiles (Gen 1:21), as well as three times in the same verse, God created man in his image (Gen 1:27)'. Rupert saves the doctrine with a distinction about the matter; Ibn Ezra concludes the verb has a second sense. Liège c. 1115, Lucca c. 1155, no possible contact."),
    E("t-k4-10", "ibn-ezra-1-1c", "abelard-hex-1-1c", "parallel",
      "Abelard secures ex nihilo on the difference between two Latin verbs — creavit of the elements, formavit of man at Gen 2:7 and the animals at 2:19 — where Ibn Ezra dissolves it by showing that the one Hebrew verb bara stands at 1:21 and 1:27 of things made out of something. The Latin distinction is available only because the translation supplies two words where the Hebrew has one at the decisive places."),
    E("t-k4-11", "abelard-hex-1-1c", "rupert-gen-1-1c", "parallel",
      "Two Latin answers to one difficulty within about fifteen years: Rupert grants that creavit is used of things shaped from matter and refers the word back to the creation of the matter; Abelard denies that it is properly so used at all and assigns those cases to formare. Neither cites the other, and the two answers are incompatible."),
    E("t-k4-12", "hugh-sacr-1-1-nihilo", "abelard-hex-1-1c", "parallel",
      "The same definition by contrast, in Paris within four years: Abelard, 'creari proprie id dicitur, quod de non esse ita ad esse producitur, ut praejacentem non habeat materiam'; Hugh, 'quod de aliquo factum est, factum quidem est sed creatum non est; quia de nihilo factum non est'. Neither names the other, and the school relations between them make silence the interesting fact."),
    # --- formless matter through the Latin bench
    E("t-k4-13", "glossa-1-2-materia", "bede-gen-1-2-materia", "transmits",
      "Migne prints the gloss under (BEDA ubi supra.). Bede: 'cuncta quae cum aquis et terra videre solemus in mundo, vel de ipsis exordium naturae, vel sumpsere de nihilo; ipsa autem terra et ipsae aquae propterea nomen sortitae sunt materiae informis, quia priusquam in lucem venirent, unde formositatem haberent non erat.' Glossa: 'Ipsa autem terra et aqua informis dicuntur materia, quia omnia quae videmus, vel ex istis sumpserunt exordium, vel ex nihilo: et priusquam in lucem venirent, non erat unde formam haberent.' The restriction that opened Bede's paragraph — 'Ad haec tantum informis est illa materies' — is not carried over."),
    E("t-k4-14", "bede-gen-1-2-materia", "aug-gnm-1-6-10", "parallel",
      "Both hang the difficulty on Wisdom 11:17, 'qui fecisti mundum de materia informi', and take opposite routes out of it: Augustine grants the formless matter and pushes creation one step behind it; Bede restricts the phrase to the earth and the waters before the light came, so that no substrate is conceded at all."),
    E("t-k4-15", "angelom-gen-1-1c", "bede-gen-1-2-materia", "parallel",
      "Wisdom 11:17 again, quoted in full by Angelomus in the form 'non enim erat manus tua, Domine, invalida, qua creasti mundum ex informi materia', and used to the opposite end: for Angelomus the verse proves that God made the matter and then made everything out of it, for Bede that 'formless matter' is only a name for the earth and waters in the dark."),
    E("t-k4-16", "alcuin-int-19-20", "aug-gnl-5-18", "echoes",
      "Alcuin's second mode of divine working — 'in materia informi qui vivit in aeternum, creavit omnia simul (Eccli. XVIII, 1)' — is Augustine's simul doctrine with Augustine's proof text, reduced to one clause and set in a list of four."),
    # --- the rabbinic bench arguing with itself
    E("t-k4-17", "br-1-5b", "br-1-9", "contests",
      "Four sections apart in one compilation, and the second answers the first. BR 1:5: 'were the matter not written explicitly it would not be possible to say it — In the beginning God created — from what? The earth was emptiness and disorder.' BR 1:9: the philosopher names emptiness, disorder, darkness, wind, water and the deeps as the materials God found, and Rabban Gamliel answers that of every one of them creation is written. The same list of six, read once as the stuff the world was made of and once as a list of created things."),
    E("t-k4-18", "pdre-3-7", "br-1-9", "contests",
      "Pirkei de-Rabbi Eliezer answers 'from what?' with substances — the earth from the snow beneath the Throne of Glory, congealed on the waters, with Job 37:6 for proof; the heavens, in the preceding section, from the light of his garment. Rabban Gamliel's answer to the same question is that nothing was found and everything was created. Neither text acknowledges the other, and both stand in the rabbinic bench's own tradition."),
    E("t-k4-19", "ramban-1-1c", "ibn-ezra-1-1c", "contests",
      "Ramban names R. Abraham a few lines above this passage and then writes 'there is no expression in the sacred tongue for bringing forth something from nothing other than the word bara' — which is the exact claim Ibn Ezra had refuted from Gen 1:21, Gen 1:27 and Isaiah 45:7. The contest is direct and is the reason the sentence is phrased as an exclusive."),
    E("t-k4-20", "ramban-1-1c", "hugh-sacr-1-1-nihilo", "parallel",
      "Hugh: 'omnia ergo quae facta sunt, Deus non solum ex materia fecit, sed materiam omnium ipse de nihilo creavit.' Ramban: 'the Holy One, blessed be He, created these two substances from nothing; they alone were created, and everything else was constructed from them.' The same two-stage doctrine — one creation out of nothing, everything afterwards made out of what was created — with the Greek word for the matter on the Hebrew side and not on the Latin."),
    E("t-k4-21", "ramban-1-1c", "br-1-5b", "cites",
      "Ramban's tohu is bar Kappara's difficulty resolved: BR 1:5 asks 'from what?' and answers 'the earth was tohu va-vohu', with an apology; Ramban makes tohu the name in the sacred tongue for the hyle, so that the verse now says the world was made out of the one thing that was created out of nothing. He quotes the rabbinic material of this section (and Sefer Yetzirah, 'he created substance from tohu') by name in the lines that follow."),
    # --- what Scripture does not say
    E("t-k4-22", "aug-conf-12-22", "br-1-9", "parallel",
      "One difficulty, two opposite methods. Augustine argues that Genesis' silence about when a thing was made cannot prove it coeternal, and makes the case with a second silence (the waters above the firmament). Rabban Gamliel meets the same objection by breaking the silence item by item: Isaiah 45:7 for tohu and darkness, Psalm 148:4–5 for the waters, Amos 4:13 for the wind, Proverbs 8:24 for the deeps."),
    E("t-k4-23", "aug-conf-12-22", "aug-conf-12-7", "echoes",
      "The same conclusion reached twice in one book by different routes — at XII.7 from the exhaustive dilemma (not out of God, and nothing else was there, therefore out of nothing), at XII.22 from the failure of the argument from Scripture's silence. The second is the defensive form of the first."),
    E("t-k4-24", "aug-conf-12-7", "aug-gnm-1-6-10", "echoes",
      "'De nihilo fecisti coelum et terram' restates in prayer what De Genesi contra Manichaeos argued nine years earlier, with the same two-stage structure — formed things out of the matter, the matter out of nothing — now expressed as 'unum prope te, alterum prope nihil'."),
    E("t-k4-25", "alcuin-int-19-20", "aug-gnm-1-6-10", "parallel",
      "Augustine's doctrine turned into an inventory: 'Quae creaturae de nihilo factae sunt? — Coelum, terra, angeli, lux, aer, aqua et anima hominis.' The list form has no Latin precedent on this crux and exact rabbinic counterparts (b. Chagigah 12a's ten things, PdRE 3's eight), and Alcuin's items are chosen so that no unformed substrate appears on it."),
 E("t-k4-x1", "ramban-1-2-tohu", "ramban-1-1c", "echoes", "Phase 4. One continuous argument that the crux boundaries split in two: having said that the Holy One created all things from absolute non-existence and that after the hyle he created nothing, Ramban goes straight on to name it — the substance the Greeks called hyly is what the sacred tongue calls tohu. The hyle and the tohu are the same thing, and the two witnesses are consecutive sentences."),
 E("t-k4-x2", "abelard-hex-1-1c", "vulgate-1-1", "cites", "Phase 4. Abelard's whole definition of creation rests on a distinction between two Latin verbs — created of what has no pre-existing matter, formed of what is shaped out of matter — and the distinction is available only because the translation supplies two verbs where the Hebrew has one at the places that matter. Ibn Ezra brings the same two verses (Gen 1:21, 1:27) to the opposite conclusion, that bara does not mean bringing forth from nothing, because in Hebrew there is no second verb to escape into."),
]

FINDING = (
    "Both benches meet the same objection, in the same words, from a craftsman. The philosopher tells "
    "Rabban Gamliel that his God was a great artist who found good materials — emptiness, disorder, "
    "darkness, wind, water, the deeps (BR 1:9); Augustine says we must not be like those who cannot "
    "believe God made anything out of nothing, because they are watching craftsmen, and wood helps the "
    "carpenter, silver the silversmith, gold the goldsmith, earth the potter (Gnm I.6.10); Basil says "
    "with us every art works on a material brought to it, smithcraft on iron and carpentry on wood, and "
    "that this is what they have projected on God. Three benches, one analogy, no contact — and three "
    "different kinds of answer. Basil answers from the dignity of the unbegotten, Augustine from "
    "omnipotence, and Rabban Gamliel with a concordance, producing a verse of creation for each of the "
    "six materials. The Latin answer is a doctrine and the rabbinic answer is a list of proof texts, and "
    "neither would have satisfied the other.\n\n"
    "The second finding is a philological objection raised three times in forty years by men who could "
    "not have read one another, from the same two verses. Scripture uses the creation verb of things "
    "made out of something: God created the great sea-creatures (Gen 1:21), God created man in his own "
    "image (Gen 1:27). Rupert of Deutz puts the objection to himself at Liège about 1115 and answers "
    "that the word is used rightly there because the matter had already been created. Abelard at the "
    "Paraclete about 1130 answers it by separating two Latin verbs — created of what has no pre-existing "
    "matter, formed of what is shaped out of matter, as at Gen 2:7 and 2:19. Ibn Ezra in Lucca about "
    "1155 brings the identical verses in the identical order and concludes that the commentators are "
    "simply wrong: bara does not mean bringing forth something from nothing. The Latin distinction is "
    "available only because the translation supplies two verbs where the Hebrew has one at the places "
    "that matter — and Ramban, who had Ibn Ezra in front of him and named him, closed the question a "
    "century later by asserting the exclusive Ibn Ezra had denied, in the same two-stage form Hugh of "
    "St Victor had given it in Paris: one thing was created out of nothing, and everything else was made "
    "out of that.\n\n"
    "And the position everyone refutes is held, on this site, by nobody — except in the two places where "
    "the rabbinic bench states it in its own voice and is uncomfortable about it. Bereshit Rabbah 1:5 "
    "asks 'from what?' and answers 'the earth was emptiness and disorder', with the formula reserved for "
    "saying what may not be said, and a parable about insulting a king by mentioning the sewers his "
    "palace stands on. Pirkei de-Rabbi Eliezer 3 answers 'from what?' with no embarrassment at all: the "
    "heavens from the light of his garment, the earth from the snow beneath the Throne of Glory. Nothing "
    "on the Latin bench has that shape, and nothing could have: once matter is the thing at issue, a "
    "material that belongs to God is still a material."
    " Two later witnesses widen the frame at both ends. Philo holds, without embarrassment, the position everyone on this daf refutes: there was a substance, of itself without order, quality or life, and God, being good, did not grudge it his own best nature — and he declines to say where the substance came from, which is exactly the clause Augustine adds at Confessions 12 to make the same description orthodox. Ambrose refutes the hyle of the philosophers by name and does not know that the book he is following most closely, the De opificio, is where the vocabulary comes from. And at the far end Paul of Burgos answers eight centuries of the question by ruling it out of order: the philosophers proceed only by opinion, as their disagreeing with each other shows and as geometers do not, so the sense of Scripture must not be made to vary with them — and he reads the whole Latin bench as having agreed with him, sancti doctores modicum curaverunt de huiusmodi opinionibus, which is a remarkable thing to say about a bench that spent eight hundred years on it."
)

# ---------------------------------------------------------------- threads (K4, Chalcidius block)
# The two Chalcidius witnesses on this crux are built in cruxes/beginning-of-what.py and
# cruxes/tohu-vabohu.py and carry `ex-nihilo-or-matter` in their own cruxes facet; only the
# threads belong here.
_E4 = lambda i, f, t, ty, ev: thread("ex-nihilo-or-matter", i, f, t, ty, ev)
THREADS.extend([
 _E4("t-k4-c1", "chalcidius-hebraei-versiones", "br-1-9", "parallel", "A Latin reporting the rabbinic position on this crux, correctly, and by name. Hebraei syluam generatam esse confitentur — the Hebrews confess that hyle was generated. At Bereshit Rabbah 1:9 a philosopher tells R. Gamliel that his God was a great artist but had good materials to hand — tohu and bohu, darkness, wind, water, the deeps — and is answered that Scripture says of every one of them that it was created. That is the rabbinic bench refusing coeval matter, which is exactly what Chalcidius says the Hebrews hold. He is a fourth-century Latin who knows the other bench's answer to this crux, states it accurately, and is read by nobody who argues the crux afterwards."),
 _E4("t-k4-c2", "chalcidius-hebraei-versiones", "ambrose-hex-1-1-hyle", "contests", "Ambrose sets up the hyle of the philosophers as the position a Christian must refuse, and Chalcidius had already reported the concession that dissolves it. For Ambrose, matter that the craftsman merely finds is a rival to God; for Chalcidius, the Hebrews grant that hyle itself was generated, so the Platonist account of the world's substance and the scriptural account of its origin are not in competition. Ambrose is refuting a Platonism that this Latin Platonist does not hold, forty years earlier and in the same language."),
 _E4("t-k4-c3", "chalcidius-terra-sylua", "aug-conf-12-7", "parallel", "The same doctrine reached from opposite directions. Augustine works down from God to a formless something 'near to nothing', and needs a page to say what it is not. Chalcidius works up from the Timaeus and has the definition ready: the receiver of all qualities has none of its own by nature, and is therefore called empty; being devoid of all things, it is called nothing. Augustine has the Bible and is short of the vocabulary; Chalcidius has the vocabulary and is using the Bible to confirm it."),
 _E4("t-k4-c4", "chalcidius-terra-sylua", "ramban-1-1c", "parallel", "The two witnesses on this daf who take the plain sense of the verse to be about matter and still hold that the matter was made. Ramban: bara means from absolute non-existence, and what was drawn out on the first day was a formless substance from which everything after was formed. Chalcidius: the earth of v. 2 is corporeal hyle, the old substance of the world before it took form — and the Hebrews, he has just said, confess it was generated. Girona 1267 and a Latin commentary on the Timaeus of about 350, agreeing on both halves of the crux."),
])

# ================================================================ Philo (Phase 6 part five, 2026-09-06)
# See scripts/philo.py. Primary crux for this witness; it also carries `tohu-vabohu`, whose roster
# picks it up as an extra when K6 is rebuilt.
import philo
from philo import BASE as _PH, PDRAFT
from bench import greek as _gk

PERSONS.update(philo.PERSONS)
LICENSES.update(philo.LICENSES)

add(**_PH, id="philo-opif-21-22",
    anchor={"verse": "gen.1.1"},
    lemma={"el": "ἦν μὲν γὰρ ἐξ αὑτῆς ἄτακτος ἄποιος ἄψυχος",
           "en": "for of itself it was without order, without quality, without life"},
    original=_gk(21, 22),
    english={"text": "And the world-making power too has for its spring the truly good. For if anyone should wish to search out the cause for the sake of which this all was fashioned, it seems to me he would not miss the mark in saying, as one of the ancients also said, that the Father and Maker is good; and for that reason he did not grudge his own most excellent nature to a substance which had nothing beautiful of itself, but was able to become all things. For of itself it was without order, without quality, without life, unlike itself, full of unevenness and of discord and of dissonance; but it admitted a turn and a change to the opposites and to the best things, to order, quality, ensoulment, likeness, sameness, the well-fitted, the concordant, all that belongs to the better idea.",
             **PDRAFT},
    tradents=[], cruxes=["ex-nihilo-or-matter", "tohu-vabohu"], senses=["literal", "spiritual"],
    answers=["matter-then-formed", "craftsman-needs-matter", "pair-is-formless-matter"],
    notes="The position the whole Latin bench spends eight centuries refusing, stated by a Jew in Greek before any of them, and stated without embarrassment. There is a substance; of itself it is without order, without quality, without life, unlike itself, full of unevenness and discord; and God, being good, did not grudge it his own best nature, so it took the turn to order, quality, ensoulment and likeness. Philo does not say where the substance came from, and he does not deny that God made it; what he does is decline to raise the question, which is what makes the passage so useful to read against Ambrose and Augustine, who cannot decline it. Ambrose knows the position by name as the hyle of the philosophers and refutes it; Augustine at Confessions 12 accepts a formless matter and insists in the same breath that God made it too; Chalcidius reports the Hebrews as confessing that hyle was generated, which is the concession Philo does not make. The vocabulary is one of the reasons the argument travelled: ataktos and apoios are the Greek behind the invisibilis et incomposita of the old Latin Gen 1:2, so what the Latin bench debates as a fact about the earth of the second verse, Philo has already stated as a doctrine about substance in general.")

THREADS.extend([
 thread("ex-nihilo-or-matter", "t-k4-p1", "philo-opif-21-22", "ambrose-hex-1-1-hyle", "contests", "Ambrose refutes this position by name and does not know he is refuting Philo, whom he is elsewhere copying. Ambrose: they say the world was made out of the matter they call hyle, and this is to make God a craftsman rather than a creator. Philo: the substance was of itself without order, without quality, without life, and God being good did not grudge it his own best nature. Every term Ambrose objects to is in the Greek, in that order, in the book his own Hexaemeron follows most closely."),
 thread("ex-nihilo-or-matter", "t-k4-p2", "philo-opif-21-22", "aug-conf-12-7", "parallel", "Augustine's near-nothing is Philo's substance with the one addition that makes it orthodox. Augustine: you made two things, one near to you and one near to nothing, and the formless matter is yours too, made by you out of nothing. Philo: the substance had nothing beautiful of itself but was able to become all things. The description matches almost word for word; what Augustine adds is the clause about where it came from, and that clause is exactly what Philo does not supply."),
 thread("ex-nihilo-or-matter", "t-k4-p3", "philo-opif-21-22", "chalcidius-terra-sylua", "parallel", "The one Latin here who had read Philo, describing hyle in Philo's terms: because it is the receiver of all qualities it has none of its own. That is Philo's apoios, without quality, and Philo's able to become all things. Chalcidius names Philo twice elsewhere in the commentary and does not name him here, which is the ordinary shape of this transmission: the doctrine crosses and the attribution does not."),
 thread("ex-nihilo-or-matter", "t-k4-p4", "philo-opif-21-22", "aug-gnm-1-6-10", "contests", "The craftsman argument, from both sides. Augustine reports the objection that craftsmen and workmen of any kind cannot make anything unless they have something to make it from, and answers that God is not a craftsman. Philo is the position Augustine is answering, and he holds it as a description of God's goodness rather than of God's limits: the maker is good, and goodness is what makes him give form to what has none. The Latin bench inherits the objection without the argument that made it worth holding."),
])

# ================================================================ Burgos (Phase 6 part six, 2026-09-06)
import lyra as _ly
PERSONS.update(_ly.PERSONS)
PLACES = dict(globals().get("PLACES", {})); PLACES.update(_ly.PLACES)
LICENSES.update(_ly.LICENSES)
ANSWERS = dict(globals().get("ANSWERS", {}))
ANSWERS.update({
 "philosophy-cannot-move-the-sense": {
   "label": "The philosophers only have opinions",
   "gloss": "The philosophers do not proceed demonstratively about matter, as is shown by their "
            "disagreeing with each other, so the sense of Scripture must not be made to vary with "
            "them; and this is why the holy doctors took little notice of such opinions "
            "(Paul of Burgos, against Lyra's introduction to Genesis 1)."},
})

add(**_ly.BURGOS, id="burgos-add-1",
    anchor={"verse": "gen.1.1"},
    lemma={"la": "non debet sensus scripture propter hoc variari",
           "en": "the sense of Scripture ought not to vary on this account"},
    original={"lang": "la",
      "text": "Ex quo presupposito infertur quod postillator minus convenienter se habet circa processum introductorium expositionis litteralis huius capituli. Dicit enim quod ex varietate opinionum de natura materie a philosophis positarum dependet intellectus operationis sex dierum, quod videtur inconvenienter dictum. Constat enim quod philosophi in hoc non demonstrative procedunt, alias non contingeret eos diversimode vel contraria opinari, sicut nec in geometricis et huiusmodi, sed solum procedunt opinative. Unde non debet sensus scripture propter hoc variari, et ideo sancti doctores modicum curaverunt de huiusmodi opinionibus variis in hac materia.",
      "source": "Koberger 1486-87, leaf n48, column 2, Additio i (archive.org biblia-sacra-lyra_202308, page/n48.jpg)",
      **_ly.SRC},
    english={"text": "From which presupposition it follows that the postillator conducts himself less fittingly in the introductory procedure of the literal exposition of this chapter. For he says that the understanding of the work of the six days depends on the variety of opinions about the nature of matter put forward by the philosophers, which seems unfittingly said. For it is agreed that the philosophers do not proceed demonstratively in this matter — otherwise it would not happen that they hold different or contrary opinions, as it does not in geometry and the like — but proceed only by opinion. Hence the sense of Scripture ought not to vary on this account; and this is why the holy doctors took little care about such various opinions in this matter.",
             **_ly.DRAFT},
    tradents=[], cruxes=["ex-nihilo-or-matter"], senses=["literal"],
    answers=["philosophy-cannot-move-the-sense", "silence-proves-nothing"],
    notes="Eight centuries of this crux answered by ruling it out of order. Every Latin witness before this one takes some position on the nature of the matter and argues it: Ambrose refutes the hyle of the philosophers, Augustine accepts a formless matter and insists God made it, Abelard defines what created properly means, Hugh distinguishes making from matter and creating the matter. Lyra opens his exposition of Genesis 1 by laying out the philosophers' opinions on matter and saying that the understanding of the six days' work depends on which is taken. Burgos says that is unfitting, and the reason he gives is a claim about what kind of knowledge natural philosophy is: the philosophers do not proceed demonstratively here, and the proof is that they disagree, which does not happen in geometry. Where a discipline yields only opinion, the sense of Scripture must not be made to move with it. He then reads the Latin bench's whole history on this crux as agreeing with him — sancti doctores modicum curaverunt de huiusmodi opinionibus — which is a striking thing to say about a bench that spent eight hundred years on the question, and is what makes the witness worth printing beside the men who did. This is his substantive addition on Gen 1:1, as against Additio iij, which is a quarrel about credit."
    )

THREADS.extend([
 thread("ex-nihilo-or-matter", "t-k4-b1", "burgos-add-1", "ambrose-hex-1-1-hyle", "parallel", "Ambrose and Burgos both want the philosophers' matter kept out of Genesis, and they want it for opposite reasons. Ambrose argues against the doctrine: they say the world was made out of the matter they call hyle, and that makes God a craftsman rather than a creator. Burgos argues against the genre: the philosophers proceed only by opinion, as their disagreeing shows, so nothing in Scripture may be made to depend on which of them is right. The first is a refutation and the second is a ruling about jurisdiction, and only the second could have been written after the schools had spent three centuries on Aristotle."),
 thread("ex-nihilo-or-matter", "t-k4-b2", "burgos-add-1", "chalcidius-hebraei-versiones", "contests", "The two ends of this edition's Latin bench on the same question. Chalcidius in the fourth century reports what the Hebrews hold about hyle in order to agree with it, and takes the philosophers' vocabulary into the exposition without apology. Burgos in the fifteenth, himself born a Jew, rules that the philosophers' opinions about matter have no business determining the sense of the chapter at all. A thousand years apart, and it is the convert who fences the text off from philosophy."),
 thread("ex-nihilo-or-matter", "t-k4-b3", "burgos-add-1", "aug-conf-12-22", "contests", "Augustine says that formless matter too was made by God and is not to be feared, and he reaches that by taking the philosophical question seriously enough to answer it. Burgos cites the holy doctors as having taken little care about such opinions, which is not what Confessions 12 looks like. The disagreement is about the Latin bench's own history: Burgos needs the fathers to have been uninterested in a question they in fact worked hard at, because his argument is that a Christian exposition should not have to wait on the philosophers."),
])
