#!/usr/bin/env python3
"""Pull the rabbinic bench from Sefaria v3 API, pinning FREE versions only.

⛔ Bereshit Rabbah Hebrew is "Wikisource Bereshit Rabbah" (CC BY-SA), NOT "Daat Bereshit Rabbah"
and NOT "Midrash Rabbah -- TE". Daat is listed on Sefaria's index for the work but returns ZERO
versions for chapters 1-3; Torat Emet ("Midrash Rabbah -- TE") returns text but its own site prints
כל הזכויות שמורות. A version title in api/texts/versions/<work> is a claim about the WORK, not the
passage — always probe the actual ref. (Phase 6, 2026-09-05.)
Writes raw/sefaria/<slug>.json with he + en text arrays and the version/license actually returned."""
import json, urllib.request, urllib.parse, time, pathlib, sys
OUT = pathlib.Path(__file__).resolve().parent.parent / "raw" / "sefaria"
OUT.mkdir(parents=True, exist_ok=True)
# (slug, ref, hebrew version title, english version title or None)
PULLS = [
 ("b-chag-12a", "Chagigah.12a", "Wikisource Talmud Bavli", "Sefaria Community Translation"),
 ("b-chag-15a", "Chagigah.15a", "Wikisource Talmud Bavli", "Sefaria Community Translation"),
 ("b-meg-9a", "Megillah.9a", "Wikisource Talmud Bavli", "Sefaria Community Translation"),
 ("b-rh-10b-11a", "Rosh_Hashanah.10b-11a", "Wikisource Talmud Bavli", "Sefaria Community Translation"),
 ("m-chag-2-1", "Mishnah_Chagigah.2.1", None, None),
 ("y-chag-2-1", "Jerusalem_Talmud_Chagigah.2.1", "The Jerusalem Talmud, edition by Heinrich W. Guggenheimer. Berlin, De Gruyter, 1999-2015", "The Jerusalem Talmud, translation and commentary by Heinrich W. Guggenheimer. Berlin, De Gruyter, 1999-2015"),
 ("br-1", "Bereshit_Rabbah.1", "Wikisource Bereshit Rabbah", "The Sefaria Midrash Rabbah, 2022"),
 ("br-2", "Bereshit_Rabbah.2", "Wikisource Bereshit Rabbah", "The Sefaria Midrash Rabbah, 2022"),
 ("br-3", "Bereshit_Rabbah.3", "Wikisource Bereshit Rabbah", "The Sefaria Midrash Rabbah, 2022"),
 ("rashi-gen-1", "Rashi_on_Genesis.1.1-5", None, "Pentateuch with Rashi's commentary by M. Rosenbaum and A.M. Silbermann, 1929-1934"),
 ("targ-onk", "Targum_Onkelos_Genesis.1.1-5", "Onkelos Genesis", "J.W. Etheridge. The Targums of Onkelos and Jonathan Ben Uzziel on the Pentateuch. London: Longmans, Green, 1862"),
 ("targ-psj", "Targum_Jonathan_on_Genesis.1.1-5", "Targum Jonathan on Genesis", "The Targum of Jonathan ben Uzziel, trans. J. W. Etheridge, London, 1862"),
 ("targ-neof", "Targum_Neofiti.Genesis.1.1-5", None, "Sefaria Community Translation"),
 ("pdre-3", "Pirkei_DeRabbi_Eliezer.3", None, "Pirke de Rabbi Eliezer, trans. Rabbi Gerald Friedlander, London, 1916"),
 ("tanch-ber-1", "Midrash_Tanchuma.Bereshit.1", "Midrash Tanchuma -- Torat Emet", "Townsend 1989 translation of Midrash Tanhuma, S. Buber Recension, edited and supplemented by R. Francis Nataf"),
 ("ibn-ezra-gen-1", "Ibn_Ezra_on_Genesis.1.1-5", "Piotrkow, 1907-1911", "Sefaria Community Translation"),
 ("ramban-gen-1", "Ramban_on_Genesis.1.1-5", "Vocalized Edition", "Commentary on the Torah by Ramban (Nachmanides). Translated and annotated by Charles B. Chavel. New York, Shilo Pub. House, 1971-1976"),
 ("gen-1-he", "Genesis.1.1-5", "Miqra according to the Masorah", None),
 # K10 (one-day-evening-first): the halakhic derivation that the day follows the night
 ("b-chull-83a", "Chullin.83a", "Wikisource Talmud Bavli", "Sefaria Community Translation"),
]
# Optional slug filter: pull-sefaria.py <slug> [slug ...] re-pulls only those (default: all).
if len(sys.argv) > 1:
    want = set(sys.argv[1:])
    PULLS = [p for p in PULLS if p[0] in want]
    if not PULLS: sys.exit(f"no such slug(s): {' '.join(sorted(want))}")
manifest = json.load(open(OUT / "_manifest.json")) if (OUT / "_manifest.json").exists() and len(sys.argv) > 1 else []
manifest = [m for m in manifest if m["slug"] not in {p[0] for p in PULLS}]
for slug, ref, he, en in PULLS:
    q = []
    q.append("version=" + urllib.parse.quote("hebrew|" + he if he else "hebrew"))
    q.append("version=" + urllib.parse.quote("english|" + en if en else "english"))
    url = f"https://www.sefaria.org/api/v3/texts/{ref}?" + "&".join(q) + "&return_format=text_only"
    try:
        with urllib.request.urlopen(url, timeout=40) as r:
            d = json.load(r)
    except Exception as e:
        print(f"FAIL {slug}: {e}"); manifest.append({"slug": slug, "ref": ref, "error": str(e)}); continue
    rec = {"slug": slug, "ref": ref, "title": d.get("title"), "versions": []}
    for v in d.get("versions", []):
        t = v.get("text")
        def count(x):
            return sum(count(i) for i in x) if isinstance(x, list) else (1 if x else 0)
        rec["versions"].append({"lang": v.get("language"), "versionTitle": v.get("versionTitle"), "license": v.get("license"), "segments": count(t)})
    (OUT / f"{slug}.json").write_text(json.dumps(d, ensure_ascii=False, indent=1))
    print(f"ok   {slug:16} " + " ; ".join(f"{x['lang']}={x['versionTitle'][:38]!r} [{x['license']}] {x['segments']}seg" for x in rec["versions"]))
    manifest.append(rec)
    time.sleep(0.5)
(OUT / "_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1))
