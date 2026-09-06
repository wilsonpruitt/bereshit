"""K3 — elohim-and-trinity (Gen 1:1–1:2). Who is the God who creates, and what do the grammar and
the word order say about plurality? Built 2026-09-05 (Phase 2, crux 8 of 9).

Seven witnesses already carry this crux from earlier builds and are folded into the roster by
build-crux.py: `ambrose-hex-1-8-29`, `aug-conf-13-9-10`, `aug-gnl-1-5-11`, `bede-gen-1-2`,
`honorius-hex-1`, `glossa-1-2-ruach` and `rupert-gen-1-8`. They are the third leg of the Latin
triad — the Spirit clause of v. 2 — and they are not rebuilt here.

Gen 1:1 already carried 34 witnesses from K1 and Gen 1:2 most of K7, K6 and K4, so every Latin
candidate was checked with scripts/overlap.py by OFFSET. Three came back COVERED and are threaded to
rather than rebuilt: Augustine's *completa commemoratio Trinitatis* (Gnl I.6.12) is inside K7's
`aug-gnl-1-5-11`, Ambrose's *operatio Trinitatis* is inside K7's `ambrose-hex-1-8-29`, and
Comestor's *in principio, id est in Filio* is inside K1's `comestor-hs-1-1`. All three already
carry this crux or are on K1's roster; see notes/cross-crux.md.

⚠ The anchor rule bites hard on this crux. Nearly everything the Latin bench says about divine
plurality is said at Gen 1:26 (*Faciamus hominem*), outside the 1:1–5 scripture layer, and the only
Latin discussion of the Hebrew word *Elohim* as a plural noun outside Abelard is Jerome's note at
Gen 6:2, copied verbatim by Rabanus. Neither is buildable here; both are in the finding and in
notes/cross-crux.md.
"""
import json, pathlib, re
from bench import ROOT, RAW, latin, sef, hcut, DRAFT, APPROVED, thread

CRUX_ID = "elohim-and-trinity"
SHORT = "Elohim / Deus … Spiritus"
E = lambda i, f, t, ty, ev: thread(CRUX_ID, i, f, t, ty, ev)

WITNESSES = []
def add(**kw): WITNESSES.append(kw)

def _flat(x): return x if isinstance(x, str) else " ".join(_flat(i) for i in x)
def _raw(f, lang, idx=None):
    d = json.load(open(RAW / f))
    v = [x for x in d["versions"] if x["language"] == lang][0]
    t = v["text"] if idx is None else v["text"][idx]
    return _flat(t), v["versionTitle"]

# ---------------------------------------------------------------- rabbinic bench
_BR_SRC = {"license": "check", "version": "Sefaria 'Midrash Rabbah -- TE' (licence unknown); a PD 'Daat' text exists on Sefaria"}
_BR_EN = {"translator": "The Sefaria Midrash Rabbah, 2022", "license": "sefaria-midrash-rabbah", "attribution_required": True}

add(id="br-1-7", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.1"}, lemma={"he": "בְּרֵאשִׁית בָּרְאוּ אֱלֹהִים, אֵין כְּתִיב כָּאן", "en": "'In the beginning the gods created' is not written here"},
    original={"lang": "he", "text": _raw("br-1-he.json", "he", 6)[0], "source": "Bereshit Rabbah 1:7 (Vilna numbering)", **_BR_SRC},
    english={"text": _raw("br-1.json", "en", 6)[0], **_BR_EN},
    tradents=["r-yitzchak"],
    cruxes=["elohim-and-trinity"], senses=["literal"],
    answers=["one-authority-singular-verb"],
    notes="The rabbinic answer to this crux, and it is a grammatical argument made three times over. R. Yitzḥak reads Ps 119:160, 'the beginning of your word is truth', of the opening of Genesis: from the beginning of the creation of the world the head of your word is truth, 'in the beginning God created', and the Lord God is truth (Jer 10:10). Then the point: no creature can come and say that two authorities created the world — vaydaberu Elohim is not written here but vaydaber Elohim; vayomeru Elohim is not written here but vayomer Elohim; bereshit bare'u Elohim is not written here but bara Elohim. Three verbs, all singular, against a noun that is plural in form. The observation is exactly Abelard's at the Paraclete seven hundred years later and Ibn Ezra's at Lucca, and the three of them draw three different conclusions from it. Note what the argument is aimed at: not idolatry in general but shtei reshuyot, two authorities — the dualism the same midrash elsewhere calls minut — and the verse is being used as a proof text against it.")

add(id="br-1-12", work="br", author="bereshit-rabbah", tradition="rabbinic",
    date=450, date_precision="compilation-400-500", place="galilee",
    anchor={"verse": "gen.1.1"}, lemma={"he": "בְּרֵאשִׁית בָּרָא, וְאַחַר כָּךְ אֱלֹהִים", "en": "'In the beginning created', and only then 'God'"},
    original={"lang": "he", "text": _raw("br-1-he.json", "he", 11)[0], "source": "Bereshit Rabbah 1:12 (Vilna numbering)", **_BR_SRC},
    english={"text": _raw("br-1.json", "en", 11)[0], **_BR_EN},
    tradents=["r-yudan", "akilas", "ben-azzai"],
    cruxes=["elohim-and-trinity"], senses=["literal"],
    answers=["word-order-is-modesty"],
    notes="Why the divine name comes third in the sentence, answered from court protocol and in Greek loanwords. R. Yudan in the name of Akilas — Aquila the proselyte, the translator — says: to this one it is fitting to call God. A flesh-and-blood king is acclaimed in a province before he has built it a public bath or a private one; he proclaims his name first and produces his works afterwards. The Unique One of the world acted first and was praised afterwards. Ben Azzai gets the same from 2 Sam 22:36, 'your humility has made me great': mortals put the name first and the titles after — So-and-so Augustalis, So-and-so pro titulo — but the Holy One, after creating the needs of his world, only then mentions his name: bereshit bara, and after that Elohim. The interest for this crux is that the rabbinic bench has a positive account of the Hebrew word order that the Greek elders were obliged to destroy, and its terms are the honorifics of the Roman provincial administration.")

_meg_he = " ".join(_raw("b-meg-9a.json", "he", i)[0] for i in (10, 11))
_meg_en = " ".join(_raw("b-meg-9a.json", "en", i)[0] for i in (10, 11))
add(id="b-meg-9a", work="bavli-megillah", author="bavli", tradition="rabbinic",
    date=550, date_precision="redaction-500-600", place="babylonia",
    anchor={"verse": "gen.1.1"}, lemma={"he": "אֱלֹהִים בָּרָא בְּרֵאשִׁית", "en": "God created in the beginning"},
    original={"lang": "arc", "text": _meg_he, "source": "b. Megillah 9a (Vilna)", "license": "cc-by-sa", "version": _raw("b-meg-9a.json", "he")[1]},
    english={"text": _meg_en, "translator": "Sefaria Community Translation", "license": "cc0"},
    tradents=["r-yehuda-b-ilai"],
    cruxes=["elohim-and-trinity"], senses=["translation", "literal"],
    answers=["word-order-is-dangerous", "one-authority-singular-verb"],
    notes="The rabbinic bench's own account of how the Greek Bible came to read as it does, and the first two items on the list are the two verses the Latin bench builds its plurality on. Ptolemy shut seventy-two elders in seventy-two houses and told each to write him the Torah of Moses; God put counsel in each one's heart and they all agreed on one understanding. And they wrote for him: 'God created in the beginning' — Elohim bara bereshit, the divine name moved to the front so that bereshit could not be read as the subject, that is, as a deity who made God — and 'I shall make a human in image and likeness', singular, for the plural na'aseh of Gen 1:26. Both changes are aimed at plurality in the opening of Genesis. Neither is in the Septuagint the Church actually inherited: its Gen 1:1 keeps the Hebrew order, en archē epoiēsen ho theos, and its Gen 1:26 keeps the plural, poiēsōmen anthrōpon. So the baraita is a tradition about a Greek Torah rather than a description of one, and the Latin reading of both verses exists in the space the described changes would have closed.")

_ram = _raw("ramban-gen-1.json", "he", 0)[0]
add(id="ramban-1-1-elohim", work="ramban-gen", author="ramban", tradition="rabbinic",
    date=1267, date_precision="range-1263-1270", place="girona",
    anchor={"verse": "gen.1.1"}, lemma={"he": "אֱלֹהִים בַּעַל הַכֹּחוֹת כֻּלָּם", "en": "Elohim, the Master of all the forces"},
    original={"lang": "he", "text": hcut(_ram, "וְאָמַר אֱלֹהִים בַּעַל הַכֹּחוֹת", "וְעוֹד יִתְבָּאֵר סוֹד בָּזֶה.", "K3 ramban he"),
              "source": "Ramban on Gen 1:1, s.v. אלהים", "license": "sefaria-vocalized", "version": "Sefaria 'Vocalized Edition'"},
    english={"text": hcut(_raw("ramban-gen-1.json", "en", 0)[0], "AND ‘ELOKIM’ (G-D) SAID. The word Elokim means",
                          "A secret will yet be disclosed in connection with this.", "K3 ramban en"),
             "translator": "Charles B. Chavel, 1971–76", "license": "chavel-ramban"},
    cruxes=["elohim-and-trinity"], senses=["literal", "spiritual"],
    answers=["elohim-is-plural-of-powers"],
    notes="Ramban takes the plural seriously and makes it mean something other than persons. The word is a compound: its root is el, which is force, and it is put together as el hem, as though el were in the construct and hem, 'they', pointed to all the other forces — so that Elohim is the force of all forces, the master of them all. Then the sentence that stops the paragraph: 'a secret will yet be disclosed in connection with this', which is his standard signal that a kabbalistic doctrine lies underneath and will not be printed. So on the one bench a plural noun points to a plurality within God that may not be spoken, and on the other, at almost the same date, it points to three persons that may be preached. Neither Ibn Ezra's honorific plural nor Abelard's three persons is what Ramban means, and his answer is the only one of the three that treats the plurality as real and as not a plurality of creators.")

_ie = _raw("ibn-ezra-gen-1.json", "he", 0)[0]
add(id="ibn-ezra-1-1-elohim", work="ibn-ezra-gen", author="ibn-ezra", tradition="rabbinic",
    date=1155, date_precision="circa", place="lucca",
    anchor={"verse": "gen.1.1"}, lemma={"he": "עַל כֵּן יֹאמַר הַכָּתוּב בָּרָא, וְלֹא בָּרְאוּ", "en": "for this reason Scripture says 'he created' and not 'they created'"},
    original={"lang": "he", "text": hcut(_ie, "אלהים, אחר שמצאנו אלוה", "על כן יאמר הכתוב ברא, ולא בראו", "K3 ibn-ezra he"),
              "source": "Ibn Ezra on Gen 1:1, s.v. אלהים", "license": "pd", "version": "Piotrkow, 1907–1911"},
    english={"text": hcut(_raw("ibn-ezra-gen-1.json", "en", 0)[0], "“E-lohim” – After we have found [the word] e-loah",
                          "For this reason does Scripture state “He created” and not “they created”.", "K3 ibn-ezra en"),
             "translator": "Sefaria Community Translation", "license": "cc0"},
    cruxes=["elohim-and-trinity"], senses=["literal"],
    answers=["elohim-is-honorific-plural", "one-authority-singular-verb"],
    notes="The grammarian's answer, and it is comparative philology two hundred years before anyone calls it that. Having found eloah, we know that Elohim is its plural, and the root of the usage is in the nature of language itself: every language has a way of showing honour. In the vernacular tongues the lesser addresses the greater in the plural; in Arabic the greater — a king — speaks of himself in the plural; in the Holy Tongue the way is to speak of the greater in the plural, as with adonim, 'master', and be'alim, 'owner', which take plural forms for a single person (Isa 19:4, Exod 22:10). And therefore: Scripture says bara and not bare'u. That last clause is word for word what Abelard asks at the Paraclete twenty years earlier — unde dictum est Eloim creavit, non creaverunt? — and the two men give opposite answers to it, neither having heard of the other.")

# ---------------------------------------------------------------- Greek and Latin fathers
add(id="basil-hex-2-6b", work="basil-hex-lat", author="basil", tradition="greek",
    date=380, date_precision="range-370-380", place="caesarea-cappadociae",
    anchor={"verse": "gen.1.2"}, lemma={"la": "venerabilis Trinitatis expletor", "en": "the completer of the venerable Trinity"},
    original=latin("7608", "Et spiritus, inquit, Dei ferebatur super aquam. Sive diffusionem",
                   "majus tibi subinde commodum conferri reperies.", 53),
    english={"text": "And the Spirit of God, it says, was borne over the water. If by 'spirit' he means the diffusion of this air of ours, understand that the writer is enumerating for you the several portions of the world; for he says that God made heaven and earth, water and air, this liquid and diffused element. Or else — which I judge the truer, and which was approved by those who were before us — by 'the Spirit of God' he means the Holy Spirit. For Scripture reserved it, that it might fittingly declare the special mention of this name; and we ought to believe that no other spirit is spoken of but the Holy, who is the completer of the blessed and venerable Trinity. And taking this understanding, you will find that a greater profit is thereupon conferred on you.", **APPROVED},
    cruxes=["elohim-and-trinity"], senses=["literal"],
    answers=["trinity-in-the-triad", "spirit-is-holy-spirit"],
    notes="The Greek bench identifying the third term, and doing it as a decision between two readings rather than as an assumption. Either the spirit of v. 2 is the diffusion of the air, in which case the verse is finishing an inventory of the elements — heaven, earth, water, air — or it is the Holy Spirit; and Basil takes the second, on the authority of those before him, with a reason drawn from the shape of the sentence: Scripture held the word back so that the mention of this name should carry its full weight. The word he uses for the Spirit is expletor, the one who completes or fills out the Trinity, which is an odd and strong term and is the whole of the Latin bench's argument in one noun: the Father and the Son are in the first verse, and the third person has been kept for the second. Ambrose, who is reading Basil, makes the same choice at Milan a few years later and says so.")

add(id="aug-gnl-imp-1-2", work="aug-gnl-imp", author="augustine", tradition="latin",
    date=393, date_precision="circa", place="hippo",
    anchor={"verse": "gen.1.1"}, lemma={"la": "ante tractationem hujus libri catholica fides breviter explicanda est", "en": "before treating this book, the catholic faith must briefly be set out"},
    original=latin("7310", "Et quoniam multi haeretici ad suam sententiam",
                   "neque coaeternam fas est dicere aut credere.", 34),
    english={"text": "And since many heretics have been accustomed to drag the exposition of the divine Scriptures to their own opinion, which is beside the faith of catholic teaching, before the treatment of this book the catholic faith must briefly be set out. It is this: that God the Father almighty made and established the whole creation through his only-begotten Son, that is, his Wisdom and Power, consubstantial with him and coeternal, in the unity of the Holy Spirit, himself also consubstantial and coeternal. That this Trinity, then, is called one God, and that he made and created all things that are, in so far as they are, catholic teaching bids us believe; so that every creature, whether intellectual or corporeal — or, as it may be more briefly said in the words of the divine Scriptures, whether invisible or visible — is made not of God's nature but by God out of nothing: and that there is nothing in it belonging to the Trinity, except that the Trinity founded it and it was founded. Wherefore it is not lawful to say or believe that the whole creation is either consubstantial with God or coeternal.", **APPROVED},
    cruxes=["elohim-and-trinity"], senses=["literal"],
    answers=["trinity-is-brought-to-the-text"],
    notes="Augustine states, before he has expounded a word of Genesis, what the exposition will have to come out to, and gives the reason: many heretics drag the divine Scriptures to their own opinion. So the Trinity is the rule under which the first chapter will be read, not a conclusion drawn from it — which is worth having on the daf, because every other Latin witness here proceeds as though the three persons were found in the words. The content of the rule is exactly what a reader of Gen 1:1–2 needs: the Father made everything through the Son who is his Wisdom, in the unity of the Spirit; the three are one God; and nothing in the creature belongs to the Trinity except that the Trinity made it. That last clause is aimed at the Manichees and does on the Latin bench what R. Yitzḥak's 'no creature can say that two authorities created the world' does on the rabbinic: it forecloses a dualism.")

add(id="aug-conf-13-5", work="aug-conf", author="augustine", tradition="latin",
    date=400, date_precision="range-397-401", place="hippo",
    anchor={"verse": "gen.1.1"}, lemma={"la": "Ecce Trinitas Deus meus, Pater et Filius et Spiritus sanctus", "en": "Behold the Trinity, my God, Father and Son and Holy Spirit"},
    original=latin("7270", "Ecce apparet mihi in aenigmate Trinitas",
                   "creator universae creaturae.", 32),
    english={"text": "Behold, the Trinity appears to me in a riddle, which you are, my God; since you, Father, in the Beginning of our wisdom — which is your Wisdom, born of you, equal to you and coeternal, that is, in your Son — made heaven and earth. And we have said many things about the heaven of heaven, and about the earth invisible and unordered, and about the darksome deep, according to the wandering falls of a spiritual formlessness, unless it were turned to him from whom it had whatever life it had, and by illumination were made a beautiful life, and were the heaven of that heaven which was afterwards made between water and water. And I already held the Father in the name of God, who made these things, and the Son in the name of the Beginning, in whom he made these things; and believing my God to be a Trinity, as I did believe, I sought it in his holy sayings — and behold, your Spirit was borne over the waters. Behold the Trinity, my God, Father and Son and Holy Spirit, creator of all creation.", **APPROVED},
    cruxes=["elohim-and-trinity"], senses=["allegorical", "spiritual"],
    answers=["trinity-in-the-triad", "trinity-is-brought-to-the-text"],
    notes="The three-term reading in its classical form, and it is autobiography rather than exegesis: the Father in the name of God, the Son in the name of the Beginning, and then — 'believing my God to be a Trinity, as I did believe, I sought it in his holy sayings, and behold, your Spirit was borne over the waters.' The order of the sentence is the order of the search. He held two of the three from the first verse, he already believed the third, and he went looking for it in the text; and the chapter heading the editors gave it says what he does not, that the Trinity which is God is understood from the first words of Genesis. Augustine himself calls it a riddle, in aenigmate. This is the passage that Bede, the Glossa, Bruno, Honorius and Abelard are all repeating, and none of them keeps the word riddle.")

add(id="wigbod-gen-1-1d", work="wigbod-gen", author="wigbod", tradition="latin",
    date=790, date_precision="circa", place="tours",
    anchor={"verse": "gen.1.1"}, lemma={"la": "in principio sibi coaeterno", "en": "in a Beginning coeternal with himself"},
    original=latin("8606", "M. Dicamus quia in principio sibi coaeterno fecit Deus",
                   "Christum Dei virtutem et Dei sapientiam (I Cor. I, 24) .", 96),
    english={"text": "M[aster]. Let us say that in a Beginning coeternal with himself God made heaven and earth — in the only-begotten Son, who is the Wisdom of the Father, of whom the Apostle says: Christ the power of God and the wisdom of God (1 Cor 1:24).", **APPROVED},
    cruxes=["elohim-and-trinity"], senses=["literal"],
    answers=["principium-is-the-son", "trinity-in-the-triad"],
    notes="The Carolingian dialogue's answer to the question its pupil has just asked — in what beginning, the beginning of time, or a beginning that was the start of the creature? — and it refuses the alternative by making the Beginning a person: one coeternal with God himself, the only-begotten Son who is the Father's Wisdom, with 1 Cor 1:24 for the identification. What the schoolroom form makes visible is how short the step is. The pupil asked a question about time; the master answered with a doctrine of the second person, and neither notices that the question has been changed.")

add(id="remigius-gen-1-1c", work="remigius-gen", author="remigius", tradition="latin",
    date=890, date_precision="circa", place="auxerre",
    anchor={"verse": "gen.1.1"}, lemma={"la": "Deus enim Pater principium est, sed non de principio", "en": "for God the Father is a beginning, but not from a beginning"},
    original=latin("9346", "Allegorice quod dictum est: in principio fecit Deus coelum et terram",
                   "quia nato Jesu Christo patuit qui essent coelestes, quique terreni.", 131),
    english={"text": "Allegorically, in what is said, In the beginning God made heaven and earth, by the name of 'beginning' we may not inappropriately understand the Son of God, as he himself said of himself to the Jews: I am the beginning, who also speak to you (John 8:25). For God the Father is a beginning, but not from a beginning, since he was not made or created by the Father but begotten; through which Beginning God the Father created heaven and earth, that is, the heavenly and the earthly. For by 'heaven' are signified the heavenly, or those leading a heavenly life; by 'earth', those gaping after earthly business. Both of these were created through the Beginning, because when Jesus Christ was born it became plain who were heavenly and who were earthly.", **APPROVED},
    cruxes=["elohim-and-trinity"], senses=["allegorical"],
    answers=["principium-is-the-son"],
    notes="A distinction made in passing that nobody else on this daf bothers with: the Father too is a beginning — but not from a beginning, since he is not made or created but begotten. Remigius has noticed that if 'in the beginning' names the Son because the Son is a principium, the word will also fit the Father, and he heads it off with the credal formula. The rest is the standard identification with John 8:25 and then the ecclesial reading, in which heaven and earth are the heavenly-minded and the earthly-minded and the division became visible only at the Incarnation. Set beside R. Yudan's 'to this one it is fitting to call God', the two benches are doing the same thing with the same clause — asking what may properly be predicated of the creator, and answering out of the word order.")

add(id="bruno-gen-1-1c", work="bruno-gen", author="bruno-of-segni", tradition="latin",
    date=1085, date_precision="range-1078-1100", place="segni",
    anchor={"verse": "gen.1.1"}, lemma={"la": "Nunquid ad angelos? Absit!", "en": "Was it to the angels? God forbid!"},
    original=latin("21403", "Deus ergo est qui loquitur. Nunquid ad angelos? Absit!",
                   "sed in se cum Filio suo, et Spiritu sancto cuncta disponens.", 164),
    english={"text": "It is God, then, who speaks. Was it to the angels? God forbid! For man was not created by angels; otherwise there would be not one but many creators, whereas God alone is the Creator of all. For thus it is written: The Creator of all, terrible and strong (2 Macc 1:24). And again: You have made all things in wisdom (Ps 104:24 [Vg 103:24]). If therefore it is true, as cannot be denied, that God alone created all things, whom was he inviting to the making of man when he said, Let us make man? Let us hear, then, what is said at the head of this book: In the beginning God created heaven and earth. You have therefore God, that is, the Father; you have also a beginning, that is, the Son — for so he himself says: I am the beginning, who also speak to you (John 8:25). But what follows? And the Spirit of God was borne over the waters. You have therefore the Holy Spirit also. And that not the Father alone created heaven, but the Son and the Holy Spirit together with him, let the psalmist say: By the word of the Lord the heavens were established, and all their power by the spirit of his mouth (Ps 33:6 [Vg 32:6]). Now the whole Trinity, that is, God and his Word and his Spirit, is one God; and it is he who says, Let us make man — not seeking help outside himself, but disposing all things within himself with his Son and the Holy Spirit.", **APPROVED},
    cruxes=["elohim-and-trinity"], senses=["literal", "allegorical"],
    answers=["trinity-in-the-triad", "not-to-angels"],
    notes="The one Latin witness on this crux who states the negative half of the question, and he states it in the rabbinic bench's own terms. Whom was God inviting when he said 'let us make man'? Not the angels — for man was not created by angels, and otherwise there would be not one creator but many. That is R. Yitzḥak's 'no creature can say that two authorities created the world', with the angels in the place of the second authority and with the same horror of it. Having refused the answer, Bruno goes back to the head of the book for the right one, and lays the triad out in three short moves: you have God, that is the Father; you have a beginning, that is the Son; and what follows? — the Spirit of God borne over the waters, so you have the Holy Spirit too. Nothing in the argument is his own except its shape, which is a schoolman's: the wrong answer refuted first, from a premise both benches share.")

add(id="abelard-hex-1-1-eloim", work="abelard-hex", author="abelard", tradition="latin",
    date=1133, date_precision="circa", place="paraclete",
    anchor={"verse": "gen.1.1"}, lemma={"la": "Eloim creavit, non creaverunt", "en": "Eloim created, not 'they created'"},
    original=latin("11118", "Notandum vero in hoc ipso Genesis exordio fidei nostrae fundamentum",
                   "in quo illa consisteret Trinitas determinavit.", 178),
    english={"text": "It is to be noted that in this very opening of Genesis the prophet carefully expressed the foundation of our faith concerning the unity of God and the Trinity. For when he said 'the Spirit of the Lord', he plainly distinguished at once both the person of the Holy Spirit and that of the Father, from whom that Spirit principally proceeds, as blessed Augustine records. But in that he added 'God said', he openly expressed God's own saying, that is, his Word, which is the Son, together with the Father himself. For no one of sound head can be so foolish as to reckon this saying corporeal, since the Godhead is not corporeal, nor has it to speak in a bodily way, nor was there yet anyone present to whom it would have had to speak bodily. Now where we say 'God created', for what is 'God' the Hebrew has Eloim, which shows a plurality of divine persons. For El is singular, which is interpreted 'God'; but Eloim is plural, by which we understand the diversity of the persons, of which each one is God. But why is it said 'Eloim created' and not 'they created'? — namely, so that a singular verb should be referred to a plural noun; in order that it might be intimated that in those three persons not three creators but one only is to be understood. When therefore he said 'Eloim created', in which he taught that the divine persons work equally together, he assuredly laid down beforehand that the works of the Trinity are undivided. And when afterwards, as we have said, he distinguished the persons of the Father and the Spirit and the Word, he determined wherein that Trinity consists.", **APPROVED},
    cruxes=["elohim-and-trinity"], senses=["literal", "translation"],
    answers=["elohim-is-plural-of-persons", "one-authority-singular-verb", "trinity-in-the-triad"],
    notes="The star witness of this crux, and the only place on the Latin bench where the Hebrew word is brought to Gen 1:1 at all. Abelard knows that El is singular and Eloim plural, and he asks the exact question the midrash asks — why 'Eloim created' and not 'they created'? — and answers it by the concord: a singular verb referred to a plural noun, so that in those three persons one creator is understood and not three. From which he draws the technical doctrine, opera Trinitatis indivisa. Where he got the grammar is unknown: Jerome's note that the Hebrew word is common in number sits at Gen 6:2 and is about the sons of God, and no Latin before Abelard brings it forward to the first verse. What he does not have is the rest of the Hebrew: he reads the plural as a plurality of persons, which is the one thing the rabbinic bench never lets it mean, and Ibn Ezra will refute the reading twenty years later without ever having heard of him. Note also the first half of the passage, where the Trinity is got out of the sequence of the verses rather than the noun — Spirit and Father from 'the Spirit of the Lord', Word and Father from 'God said' — which is Augustine's method and needs no Hebrew at all.")

add(id="rupert-gen-1-3-trinitas", work="rupert-gen", author="rupert", tradition="latin",
    date=1117, date_precision="range-1112-1117", place="liege",
    anchor={"verse": "gen.1.3"}, lemma={"la": "ubique tria consonant testimonii verba", "en": "everywhere three words of testimony agree"},
    original=latin("10873", "Quia creatricis Trinitatis haec sunt opera",
                   "ut testibus plus quam tribus nulla judicialis indigeat causa.", 167),
    english={"text": "Because these are the works of the creating Trinity, holy Scripture rightly triples its testimony everywhere. For there are three sayings, or rather one and the same thing said three times. God said, whose saying is doing. And so it was done, and the earth brought forth. And the first is according to the evening, that is, the secret of the Word of God, in which was life; whatever is according to the morning, that is, by the substantial bringing forth of things; and another was done according to this same morning, and a third according to the continuing day of the creature persevering in whatever manner. You will find this in all the works of the six days: God said, Let there be luminaries, and it was so, and God made two great luminaries. Again: Let the waters bring forth creeping things, and God created the great sea-creatures, and God blessed them, and so on. But in the creation of the light, God said: Let there be light, and light was made, and he divided the light and the darkness. Everywhere three words of testimony agree, because everywhere, at evening and at morning and through the whole day, the creating Trinity works. And this is the original cause of the holy and just law by which the same writer laid down that no judicial case needs more than three witnesses.", **APPROVED},
    cruxes=["elohim-and-trinity"], senses=["allegorical", "spiritual"],
    answers=["trinity-in-the-formula"],
    notes="Rupert's whole design for the Hexaemeron in one paragraph, and it is the boldest thing said on this crux: the threefold formula that runs through the six days — God said, and it was so, and God made — is itself the trace of the Trinity, because the creating Trinity is at work everywhere, and Moses laid down the law of three witnesses for the same reason he wrote the chapter this way. Augustine had entertained precisely this reading at De Genesi ad litteram II and rejected it, on the ground that it would make the Son appear to act under orders and the Spirit merely to approve. Rupert takes it up anyway and generalises it past the point where Augustine's objection can be raised, by making the three words a testimony rather than a distribution of labour — and then, having done so, ties it to the law of evidence, which is a claim about how Scripture was written rather than about what happened.")

# ---------------------------------------------------------------- threads (K3)
THREADS = [
 E("t-k3-01", "abelard-hex-1-1-eloim", "br-1-7", "parallel", "The star thread of the site. Both ask why the plural noun Elohim takes a singular verb, in the same words. R. Yitzḥak: 'bereshit bare'u Elohim is not written here, but bara Elohim' — and therefore no creature can say that two authorities created the world. Abelard: 'unde autem dictum est Eloim creavit, non creaverunt? ut videlicet ad plurale nomen singulare verbum referretur; quatenus insinuaretur in tribus illis personis non tres creatores, sed unum tantum debere intelligi.' One grammatical fact, seven hundred years apart, no contact, and the same conclusion drawn about the verb — one creator — from opposite conclusions about the noun."),
 E("t-k3-02", "ibn-ezra-1-1-elohim", "abelard-hex-1-1-eloim", "contests", "The same question and the opposite answer, twenty years apart and with no possible contact. Abelard: Eloim is plural, showing a plurality of divine persons, each of which is God, and the singular verb shows they are one creator. Ibn Ezra: Elohim is the plural of eloah, and the plural is how the Holy Tongue speaks of the great — as adonim and be'alim are plural for one master, and as a king in Arabic speaks of himself in the plural — 'and for this reason Scripture says bara and not bare'u.' Each has the whole of the other's evidence and takes the plural to mean the opposite thing."),
 E("t-k3-03", "ibn-ezra-1-1-elohim", "br-1-7", "echoes", "Ibn Ezra's closing clause is Bereshit Rabbah's argument reduced to a grammarian's note: 'for this reason Scripture says bara and not bare'u.' What the midrash offers as a refutation of two authorities, he offers as the expected concord of an honorific plural — the same reading with the polemic taken out and a comparative philology of Arabic, Hebrew and the vernaculars put in."),
 E("t-k3-04", "ramban-1-1-elohim", "ibn-ezra-1-1-elohim", "contests", "Ramban has Ibn Ezra open in front of him throughout the comment on this verse and takes the plural the other way: not an honorific but a compound, el hem, the force and 'they' — all the other forces — so that Elohim is the force of all forces. He does not deny the grammar; he refuses to let the plural be empty. 'A secret will yet be disclosed in connection with this' says that the real answer is one he will not print."),
 E("t-k3-05", "ramban-1-1-elohim", "abelard-hex-1-1-eloim", "parallel", "The two witnesses on this daf who make the plurality of the noun a plurality in God, and they could not be further apart on what it is. Abelard: a diversity of persons, of which each one is God, and the doctrine is preachable and technical — opera Trinitatis indivisa. Ramban: the master of all the forces, and a secret that will be disclosed elsewhere. A century apart, in Paris and in Girona, with nothing between them but the same three consonants."),
 E("t-k3-06", "b-meg-9a", "br-1-7", "echoes", "The same anxiety twice, once as exegesis and once as translation history. R. Yitzḥak proves from the singular verbs that no one can say two authorities created the world; the elders before Ptolemy move the divine name to the front of the sentence — 'God created in the beginning' — so that bereshit cannot be read as the subject of bara, that is, as a power that made God. Both are defending the first verse against a reading that finds more than one maker in it."),
 E("t-k3-07", "b-meg-9a", "br-1-12", "contests", "The elders reverse the word order that R. Yudan and Ben Azzai explain and praise. For the Bavli's baraita the sequence bereshit bara … Elohim is a danger to be removed for a Greek reader; for Bereshit Rabbah it is the Holy One's modesty — a mortal king proclaims his name and produces his works afterwards, but God acted first and was named after. The same three words are a liability in Alexandria and a virtue in Caesarea."),
 E("t-k3-08", "b-meg-9a", "abelard-hex-1-1-eloim", "parallel", "The baraita reports the elders removing from the Greek exactly the two features the Latin bench builds on, and neither removal reached the Church. The first item on their list is the word order of Gen 1:1; the second is the plural of Gen 1:26 turned singular. The Septuagint as transmitted has neither change. Abelard's argument needs the plural noun standing next to a singular verb in the first verse, which is what the elders are said to have rearranged, and Bruno's needs the 'let us make' of Gen 1:26, which is what they are said to have made singular."),
 E("t-k3-09", "bruno-gen-1-1c", "br-1-7", "parallel", "Both refuse a plurality of creators in the same words and against different opponents. R. Yitzḥak: no creature can say that two authorities created the world. Bruno: was he speaking to the angels? God forbid — for otherwise there would be not one creator but many, whereas God alone is the creator of all. The premise is shared exactly; what Bruno does next with it, and the midrash cannot, is find the second and third persons in the same verses."),
 E("t-k3-10", "bruno-gen-1-1c", "aug-conf-13-5", "echoes", "'Habes ergo Deum, id est Patrem; habes et principium, id est Filium … Habes igitur et Spiritum sanctum' is Augustine's three-term reading turned into a schoolroom enumeration, with the same John 8:25 for the Son and the same Spirit of v. 2 for the third. What Augustine reached at the end of a search and called a riddle, Bruno hands over in three sentences as something the reader can check."),
 E("t-k3-11", "aug-conf-13-5", "aug-gnl-1-5-11", "echoes", "The same triad in the same order in two works: the Father in the name of God, the Son in the name of the Beginning, the Spirit borne over the waters, which De Genesi ad litteram calls the completa commemoratio Trinitatis. What the Confessions add is the sequence of the search — he held two, he already believed the third, and he went looking for it in the text."),
 E("t-k3-12", "aug-gnl-imp-1-2", "aug-conf-13-5", "contests", "Augustine on both sides of the question this crux really turns on. In the unfinished commentary the catholic faith is set out before the exposition begins, expressly because heretics drag Scripture to their own opinion, so that the Trinity is the rule the chapter will be read under. In the Confessions the Trinity 'appears to me in a riddle' out of the first words. The two are not incompatible and he never reconciles them, and every later Latin witness on this daf writes as though only the second were true."),
 E("t-k3-13", "basil-hex-2-6b", "ambrose-hex-1-8-29", "transmits", "Ambrose is reading Basil at Milan and makes the same choice between the same two readings: either the spirit of v. 2 is the air, or it is the Holy Spirit — 'but we, agreeing with the judgement of the saints and the faithful, take it as the Holy Spirit, so that the working of the Trinity may shine out in the constitution of the world.' Basil's reason is that Scripture reserved the name; Ambrose's is that the third person is needed to complete the triad the first verse began."),
 E("t-k3-14", "basil-hex-2-6b", "bede-gen-1-2", "parallel", "Expletor and the same argument from the shape of the sentence, three centuries and a language apart: Basil, that no other spirit is meant but the Holy, who is the completer of the venerable Trinity; Bede, that having first declared that in the beginning, that is in the Son, the Father made heaven and earth, Scripture brought in mention of the Holy Spirit too, so as to signify the power of the whole Trinity together in the creation of the world."),
 E("t-k3-15", "aug-conf-13-5", "bede-gen-1-2", "cites", "Bede's sentence is Augustine's triad with the two halves welded: 'in principio, id est in Filio, Pater fecit coelum et terram' and then the Spirit added 'ut totius simul Trinitatis in creatione mundi virtutem significaret'. The riddle has become a demonstration, and the word aenigma is gone."),
 E("t-k3-16", "wigbod-gen-1-1d", "aug-conf-13-5", "echoes", "'In principio sibi coaeterno fecit Deus coelum et terram, in unigenito Filio qui est sapientia Patris' is Augustine's 'in Principio sapientiae nostrae quod est tua Sapientia de te nata, aequalis tibi et coaeterna, id est in Filio tuo' with the possessives dropped and 1 Cor 1:24 put in for the identification. The Carolingian dialogue asked a question about time and was answered with a person."),
 E("t-k3-17", "remigius-gen-1-1c", "wigbod-gen-1-1d", "echoes", "The same identification with the same proof text, and Remigius adds the guard the dialogue does not have: God the Father too is a beginning, but not from a beginning, since he is begotten of none. Once 'in the beginning' names the Son because the Son is a principium, the word will fit the Father as well, and only Remigius notices."),
 E("t-k3-18", "remigius-gen-1-1c", "br-1-12", "parallel", "Both benches ask what may properly be predicated of the creator and answer it out of the first verse's word order. R. Yudan in the name of Akilas: to this one it is fitting to call God — because he acted first and was named afterwards, unlike a king acclaimed before he has built anything. Remigius: the Father is a beginning, but not from a beginning. The rabbinic argument is about the order of the words in the sentence and the Latin about the order of the persons in God, and both are reading the same three words."),
 E("t-k3-19", "rupert-gen-1-3-trinitas", "aug-gnl-1-5-11", "contests", "Rupert builds his whole Hexaemeron on the reading Augustine considered and refused. Augustine asks whether the Trinity is to be understood in 'God said, let it be — and God made — and God saw that it was good', and answers that it does not befit the unity of the Trinity for the Son to be understood as making under orders and the Spirit as freely approving. Rupert takes the threefold formula as the Trinity's signature everywhere in the six days, and escapes the objection by making the three words a testimony rather than three offices."),
 E("t-k3-20", "rupert-gen-1-3-trinitas", "rupert-gen-1-8", "echoes", "One design stated twice. At Gen 1:2 the Spirit's brooding is what betters the creature as a bird's warmth betters an egg; here the threefold formula of every day's work is the trace of the creating Trinity, tied to the law of three witnesses. Both are claims about how the chapter was written, not about what happened in it."),
 E("t-k3-21", "honorius-hex-1", "aug-conf-13-5", "echoes", "Honorius states the triad and then does something Augustine does not: he distributes the works. 'Note the Trinity: to God the Father is ascribed the creation of the world, to the Son the disposition of things, to the Holy Spirit the quickening or adorning of all.' That is the appropriation doctrine of the twelfth-century schools laid over the first two verses, and it is the distribution of labour Augustine had warned against."),
 E("t-k3-22", "glossa-1-2-ruach", "aug-gnl-1-5-11", "cites", "The standard gloss on the Spirit clause is Augustine's De Genesi ad litteram I.5 printed under his name, so that what the twelfth-century schoolroom reads on Gen 1:2 is the third term of Augustine's triad in Augustine's own words — the Spirit borne over the waters not by place but as the will of a craftsman is over what he makes, a love that comes not from need but from bounty."),
 E("t-k3-23", "abelard-hex-1-1-eloim", "aug-gnl-1-5-11", "cites", "Abelard names Augustine for the procession — 'the person of the Holy Spirit and of the Father, from whom that Spirit principally proceeds, as blessed Augustine records' — and gets the first half of his Trinity the Augustinian way, out of the sequence of the verses: the Spirit from 'the Spirit of the Lord', the Word from 'God said'. Only then does he turn to the Hebrew noun, which Augustine did not have and could not have used."),
 E("t-k3-24", "bruno-gen-1-1c", "remigius-gen-1-1c", "echoes", "The same identification of the Son with the principium of Gen 1:1 from the same verse of John — 'ego principium qui et loquor vobis' — in Auxerre about 890 and at Segni about 1090. It is the most stable single move on the Latin bench and it is what makes the three-term reading possible at all: without a person in the second word there is no triad to complete."),
 E("t-k3-25", "aug-gnl-imp-1-2", "br-1-7", "parallel", "Both texts open their treatment of Genesis by fencing it against a dualism, and both do it before expounding a word. Augustine sets out the catholic faith first, because many heretics drag the Scriptures to their own opinion, and ends by ruling that nothing in the creature belongs to the Trinity except that the Trinity made it. R. Yitzḥak rules that no creature can say that two authorities created the world. The heresies are not the same and the manoeuvre is identical: the first verse is made to exclude a second maker before it is made to say anything else."),
 E("t-k3-x1", "comestor-hs-1-1", "aug-conf-13-5", "echoes", "Phase 4. 'Creatus autem est in principio, id est in Filio' is Augustine's second term reduced to an apposition and taught as settled — the riddle of Confessions XIII.5 become a gloss a reader passes over. Written at Phase 4 because `comestor-hs-1-1` was built for K1 and its opening clause belongs to this crux."),
 E("t-k3-x2", "b-meg-9a", "lxx-1-1", "contests", "Phase 4. The baraita says the seventy-two elders wrote 'God created in the beginning' for Ptolemy, moving the divine name to the front so that bereshit could not be read as a subject. The Septuagint as transmitted has not moved it: en archē epoiēsen ho theos keeps the Hebrew order. The change the rabbinic bench remembers making is not in the Greek the Church inherited, and the Latin reading of the verse stands in the space it would have closed."),
 E("t-k3-x3", "targ-onk-1-1", "br-1-7", "parallel", "Phase 4. The targum removes the difficulty the midrash has to argue about. Where the Hebrew has the plural-looking Elohim with a singular verb, Onkelos writes YY — the Tetragrammaton, which is not plural in form — so that no reader of the Aramaic could raise the question of two authorities at all. R. Yitzḥak has to answer it three times from the verbs."),
]

FINDING = (
 "One grammatical fact, three benches, three incompatible conclusions — and it is the same fact "
 "each time. Bereshit Rabbah 1:7 observes that the plural-looking Elohim takes singular verbs "
 "throughout: vaydaberu is not written but vaydaber, vayomeru is not written but vayomer, bare'u is "
 "not written but bara — and concludes that no creature can say that two authorities created the "
 "world. Abelard, at the Paraclete about 1133, asks the identical question in Latin — unde dictum "
 "est Eloim creavit, non creaverunt? — and answers that a singular verb is referred to a plural "
 "noun so that in those three persons one creator should be understood and not three, from which he "
 "derives the technical doctrine that the works of the Trinity are undivided. Ibn Ezra, at Lucca "
 "about 1155, closes the same argument with the same clause — 'and for this reason Scripture says "
 "bara and not bare'u' — having first shown that the plural is simply how the Holy Tongue speaks of "
 "the great, as adonim and be'alim are plural for one master and as a king in Arabic speaks of "
 "himself in the plural. And Ramban, a century later with Ibn Ezra in front of him, refuses to let "
 "the plural be empty at all: the word is a compound, el hem, the force and all the other forces, "
 "and 'a secret will yet be disclosed in connection with this'. Nobody is answering anybody. Three "
 "of the four could not have read each other, and the fourth is reading only within his own bench.\n\n"
 "What makes Abelard's page the strangest thing on this daf is that the Latin bench had the "
 "information for six hundred years and never used it here. Jerome knew that the Hebrew word is "
 "common in number and said so — verbum Hebraicum ELOIM communis est numeri, et Deus quippe et dii "
 "similiter appellantur — but he says it at Genesis 6:2, about the sons of God, and Rabanus copies "
 "him there verbatim, and neither brings it forward to the first verse. Every other Latin witness on "
 "this crux gets its Trinity from the sequence of the sentences rather than from any Hebrew word: "
 "the Father in the name of God, the Son in the name of the Beginning, the Spirit borne over the "
 "waters. That is Augustine's triad, and he calls it a riddle — ecce apparet mihi in aenigmate "
 "Trinitas — and states the order of his own search plainly, that he already held two of the three "
 "and believed the third and went looking for it in the holy sayings. Bede, Bruno, Honorius and the "
 "Glossa repeat the triad and none of them repeats the word riddle. In the unfinished commentary "
 "Augustine is franker still: he sets out the catholic faith before expounding a syllable, because "
 "many heretics drag the Scriptures to their own opinion.\n\n"
 "The rabbinic bench, meanwhile, preserves a memory of the whole problem as a translation problem. "
 "Megillah 9a's baraita has seventy-two elders shut in seventy-two houses writing the Torah for "
 "Ptolemy, and the first two things on the list of what they changed are the two verses the Latin "
 "bench builds on: they wrote 'God created in the beginning', moving the divine name to the front so "
 "that bereshit could not be read as a subject, and they wrote 'I shall make a human', singular, for "
 "the 'let us make' of Gen 1:26. Both changes remove a plurality from the opening of Genesis. "
 "Neither is in the Septuagint the Church actually inherited, whose first verse keeps the Hebrew "
 "order and whose Gen 1:26 keeps the plural. So the Latin reading of both verses stands in exactly "
 "the space the elders are said to have closed — and Bruno of Segni, refuting it at Segni about "
 "1090, refuses the plurality in the rabbinic bench's own words: was he speaking to the angels? God "
 "forbid, for otherwise there would be not one creator but many."
)

# ---------------------------------------------------------------- new persons / places / answers
PERSONS = {
 "akilas": {"name": "Akilas (Aquila)", "he": "עֲקִילַס", "dates": "fl. c. 130", "tradition": "rabbinic", "role": "tradent",
            "note": "The proselyte translator of the Bible into Greek, cited in the midrash as a tradent."},
 "ben-azzai": {"name": "Shimon ben Azzai", "he": "שִׁמְעוֹן בֶּן עֲזַאי", "dates": "fl. c. 110–135", "tradition": "rabbinic", "role": "tradent"},
}

PLACES = {}

ANSWERS = {
 "one-authority-singular-verb": {"label": "The verb is singular, so one maker", "gloss": "Not vaydaberu but vaydaber, not bare'u but bara — no one may say that two authorities created the world (Bereshit Rabbah 1:7; Ibn Ezra; and, to the opposite end, Abelard)."},
 "elohim-is-plural-of-persons": {"label": "Eloim is plural: three persons", "gloss": "El is singular and Eloim plural, showing a diversity of persons each of which is God; the singular verb shows that they are one creator and their works undivided (Abelard)."},
 "elohim-is-honorific-plural": {"label": "A plural of honour", "gloss": "Every language honours the great with a plural — adonim, be'alim, the king speaking of himself in Arabic — so Elohim is the plural of eloah and means nothing more (Ibn Ezra)."},
 "elohim-is-plural-of-powers": {"label": "The force of all forces", "gloss": "El hem: the root el is force, and 'they' points to all the other forces, so Elohim is the master of them all — with a secret not disclosed (Ramban)."},
 "trinity-in-the-triad": {"label": "Father, Beginning, Spirit", "gloss": "The three persons are named in order across the first two verses: God the Father, the Beginning who is the Son, the Spirit borne over the waters (Augustine, Basil, Ambrose, Bede, Bruno, Honorius, the Glossa)."},
 "trinity-in-the-formula": {"label": "The threefold formula of the six days", "gloss": "God said — and it was so — and God made: the testimony is tripled everywhere because the creating Trinity works everywhere (Rupert; considered and refused by Augustine)."},
 "trinity-is-brought-to-the-text": {"label": "The rule of faith comes first", "gloss": "The catholic faith is set out before the exposition begins, because heretics drag Scripture to their own opinion; the doctrine is what the chapter is read under (Augustine, De Genesi ad litteram imperfectus)."},
 "spirit-is-holy-spirit": {"label": "The spirit of v. 2 is the Holy Spirit", "gloss": "Not the air and not a wind: Scripture reserved the name, and no other spirit is meant but the one who completes the Trinity (Basil, Ambrose)."},
 "principium-is-the-son": {"label": "The Beginning is the Son", "gloss": "'I am the beginning, who also speak to you' (John 8:25) — though the Father too is a beginning, and not from a beginning (Wigbod, Remigius, Bruno)."},
 "not-to-angels": {"label": "Not spoken to the angels", "gloss": "Whoever the 'let us' addresses, it is not angels: man was not created by angels, or there would be many creators and not one (Bruno)."},
 "word-order-is-modesty": {"label": "God is named after his works", "gloss": "A mortal king proclaims his name and builds afterwards; the Holy One made the needs of his world and was named after — bereshit bara, and only then Elohim (R. Yudan in the name of Akilas; Ben Azzai)."},
 "word-order-is-dangerous": {"label": "The word order had to be changed", "gloss": "The seventy-two elders wrote 'God created in the beginning' for Ptolemy, so that bereshit could not be read as the subject (b. Megillah 9a)."},
}

LICENSES = {}
