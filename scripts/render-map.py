#!/usr/bin/env python3
"""Version B: the crux as a map. Same graph as the stream view, laid out on a plane; the organizing
dimension (answer family / time / place / sense) is switchable. Usage: render-map.py <crux-id> —
with no crux-id, renders every crux whose data/cruxes.json status is "built" and (re)writes
out/index.html listing them."""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

if len(sys.argv) <= 1:
    import subprocess
    from indexpage import write_index
    built = [c["id"] for c in json.load(open(ROOT / "data" / "cruxes.json")) if c.get("status") == "built"]
    for cid in built:
        subprocess.run([sys.executable, __file__, cid], check=True)
    write_index(ROOT)
    sys.exit(0)

crux_id = sys.argv[1]
crux = {c["id"]: c for c in json.load(open(ROOT / "data" / "cruxes.json"))}[crux_id]
threads = [t for t in json.load(open(ROOT / "data" / "threads.json")) if t["crux"] == crux_id]
persons = json.load(open(ROOT / "data" / "persons.json"))
places = json.load(open(ROOT / "data" / "places.json"))
answers = json.load(open(ROOT / "data" / "answers.json"))
SHORT = {"lxx-1-2": "Septuagint", "vulgate-1-2": "Vulgate", "targ-onk-1-2": "Onkelos", "targ-neof-1-2": "Neofiti",
 "targ-psj-1-2": "Ps.-Jonathan", "br-2-4": "Bereshit Rabbah 2:4", "b-chag-15a": "Chagigah 15a", "rashi-1-2b": "Rashi",
 "basil-hex-lat-2-6": "Basil (Eustathius)", "ambrose-hex-1-8-29": "Ambrose", "jerome-hq-1-2": "Jerome",
 "aug-gnm-1-5-8": "Augustine, c. Manich.", "aug-gnl-imp-4-16": "Augustine, imperf.", "aug-conf-13-9-10": "Augustine, Conf. XIII",
 "aug-gnl-1-18-36": "Augustine, Gn. litt. I", "isidore-quaest-1-3": "Isidore", "bede-gen-1-2": "Bede", "wigbod-gen-1-2": "Wigbod",
 "alcuin-int-29": "Alcuin", "rabanus-gen-1-1": "Rabanus", "angelom-gen-1-2": "Angelomus", "remigius-gen-1-2": "Remigius",
 "bruno-gen-1-2": "Bruno of Segni", "rupert-gen-1-8": "Rupert", "abelard-hex-1-2": "Abelard", "hugh-adnot-gen-1-2": "Hugh of St Victor",
 "honorius-hex-1": "Honorius", "comestor-hs-gen-1": "Comestor", "glossa-1-2-ruach": "Glossa (slot)"}
ws = []
for wid in crux["witnesses"]:
    w = json.load(open(ROOT / "data" / "witnesses" / f"{wid}.json"))
    pl = places.get(w["place"], {})
    prec = w.get("date_precision", "")
    if "-" in prec and prec.split("-", 1)[1][0].isdigit():
        kind, rng = prec.split("-", 1); datelabel = ("" if kind == "range" else kind + " ") + rng.replace("-", "–")
    else:
        datelabel = ("c. " if prec == "circa" else "") + (f"{-w['date']} BCE" if w["date"] < 0 else str(w["date"]))
    ws.append({"id": wid, "short": SHORT.get(wid, wid), "author": persons.get(w["author"], {}).get("name", w["author"]),
        "tradition": w["tradition"], "date": w["date"], "datelabel": datelabel, "place": pl.get("name", w["place"]),
        "lat": pl.get("lat"), "lon": pl.get("lon"), "answers": w.get("answers", []), "senses": w.get("senses", []),
        "lemma": w.get("lemma", {}), "en": w["english"]["text"], "translator": w["english"].get("translator", ""),
        "orig": w["original"]["text"], "olang": w["original"].get("lang"), "source": w["original"].get("source", ""),
        "notes": w.get("notes", ""), "slot": w.get("status") == "slot"})
data = {"crux": {"id": crux_id, "question": crux["question"], "summary": crux["summary"], "finding": crux.get("finding", "")},
        "witnesses": ws, "threads": threads, "answers": answers,
        "senses": {"literal": "Literal", "allegorical": "Allegorical", "spiritual": "Spiritual", "translation": "Translation"}}

TEMPLATE = r'''<title>Ruach Merahefet Map</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Inter:wght@400;500;600&family=Frank+Ruhl+Libre:wght@400;500&display=swap">
<style>
:root{--bg:#F3F4F1;--ink:#1A1E21;--mute:#5B615E;--rule:#CBCFC9;--card:#FAFAF7;--lat:#A0392A;--rab:#2B4A9C;--grk:#67762B;--hub:#1A1E21;--ring:#DDE0DA;
 --e-cites:#1A1E21;--e-echo:#7A807C;--e-contest:#A0392A;--e-par:#B4B9B4;--e-trans:#2B4A9C;
 --serif:"EB Garamond",Garamond,"Times New Roman",serif;--sans:Inter,system-ui,sans-serif;--heb:"Frank Ruhl Libre","Times New Roman",serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#151819;--ink:#E7E5DD;--mute:#9AA09B;--rule:#33393B;--card:#1C2022;--lat:#E28A73;--rab:#8EA6EC;--grk:#B9C66A;--hub:#E7E5DD;--ring:#24292B;--e-cites:#E7E5DD;--e-echo:#8A908C;--e-contest:#E28A73;--e-par:#4C5250;--e-trans:#8EA6EC}}
:root[data-theme="dark"]{--bg:#151819;--ink:#E7E5DD;--mute:#9AA09B;--rule:#33393B;--card:#1C2022;--lat:#E28A73;--rab:#8EA6EC;--grk:#B9C66A;--hub:#E7E5DD;--ring:#24292B;--e-cites:#E7E5DD;--e-echo:#8A908C;--e-contest:#E28A73;--e-par:#4C5250;--e-trans:#8EA6EC}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--serif);height:100vh;display:grid;grid-template-rows:auto 1fr;overflow:hidden}
.bar{display:flex;flex-wrap:wrap;gap:10px 22px;align-items:center;padding:12px 18px;border-bottom:1px solid var(--rule);font:13px var(--sans)}
.bar .t{font:500 15px var(--serif);margin-right:auto}
.bar .t small{font:500 11px var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--mute);margin-right:10px}
.modes{display:flex;border:1px solid var(--rule);border-radius:3px;overflow:hidden}
.modes button{font:500 12.5px var(--sans);background:none;border:0;border-right:1px solid var(--rule);color:var(--mute);padding:6px 12px;cursor:pointer}
.modes button:last-child{border-right:0}
.modes button[aria-pressed="true"]{background:var(--ink);color:var(--bg)}
.modes button:focus-visible,.f label:focus-within{outline:2px solid var(--rab);outline-offset:1px}
.f{display:flex;gap:12px;color:var(--mute)}
.f label{display:inline-flex;gap:5px;align-items:center;cursor:pointer}
.f i{display:inline-block;width:22px;border-top:2px solid var(--e-cites)}
.f .echoes i{border-top-style:dashed;border-color:var(--e-echo)} .f .contests i{border-color:var(--e-contest)} .f .parallel i{border-top-style:dotted;border-top-width:3px;border-color:var(--e-par)} .f .transmits i{border-color:var(--e-trans)}
.trad{display:flex;gap:12px;color:var(--mute)}
.trad span::before{content:"";display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:5px;vertical-align:-1px;background:var(--c)}
.main{display:grid;grid-template-columns:minmax(0,1fr) 360px;min-height:0}
#map{width:100%;height:100%;display:block;cursor:grab}
#map:active{cursor:grabbing}
.panel{border-left:1px solid var(--rule);overflow:auto;padding:20px 22px 40px;font-size:16.5px;line-height:1.5}
.panel .eyebrow{font:600 11px var(--sans);letter-spacing:.12em;text-transform:uppercase;color:var(--mute);margin:0 0 6px}
.panel h2{font:500 22px/1.2 var(--serif);margin:0 0 4px;text-wrap:balance}
.panel .meta{font:12.5px var(--sans);color:var(--mute);margin:0 0 12px}
.panel .lem{font-size:18px;margin:0 0 10px} .panel .lem .heb{font-family:var(--heb);font-size:19px} .panel .lem .lat{font-style:italic}
.panel .orig{margin:12px 0 0;padding:10px 12px;background:var(--card);border-left:1px solid var(--rule);font-size:15.5px}
.panel .orig.heb{font-family:var(--heb);direction:rtl;text-align:right;font-size:18px;line-height:1.8}
.panel .orig.lat{font-style:italic}
.panel .note{font-size:15px;color:var(--mute);margin:12px 0 0}
.panel .cred{font:12px var(--sans);color:var(--mute);margin-top:12px}
.panel .ans{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 0}
.panel .ans span{font:500 11px var(--sans);border:1px solid var(--rule);padding:2px 7px;border-radius:2px}
.panel .ev{border-top:2px solid var(--ink);padding-top:8px}
.panel .heb-q{font-family:var(--heb);direction:rtl;text-align:right;font-size:20px}
.panel .la-q{font-style:italic;font-size:19px}
.panel .hint{font:13px/1.5 var(--sans);color:var(--mute);margin-top:18px;border-top:1px solid var(--rule);padding-top:10px}
svg text{font-family:var(--sans);fill:var(--ink);pointer-events:none}
.lbl{font-size:11px} .lbl.dim{opacity:.35}
.hublbl{font-size:12px;font-weight:600;fill:var(--ink)} .hubsub{font-size:10.5px;fill:var(--mute)}
.ring{fill:none;stroke:var(--ring);stroke-width:1} .ringlbl{font-size:10px;fill:var(--mute);letter-spacing:.08em}
.placelbl{font-size:10px;fill:var(--mute);letter-spacing:.06em;text-transform:uppercase}
.edge{fill:none;stroke-width:1.4;cursor:pointer;transition:opacity .2s}
.edge.cites{stroke:var(--e-cites)} .edge.echoes{stroke:var(--e-echo);stroke-dasharray:5 4} .edge.contests{stroke:var(--e-contest);stroke-width:1.8} .edge.parallel{stroke:var(--e-par);stroke-dasharray:2 4;stroke-width:2} .edge.transmits{stroke:var(--e-trans)}
.edge.on{stroke-width:3.2} .edge.dim{opacity:.12} .edge.hidden{display:none}
.hublink{fill:none;stroke:var(--rule);opacity:.6}
.node{cursor:pointer;stroke:var(--bg);stroke-width:2}
.node.latin{fill:var(--lat)} .node.rabbinic{fill:var(--rab)} .node.greek-jewish{fill:var(--grk)}
.node.slot{fill:none;stroke:var(--mute);stroke-dasharray:2 2}
.node.dim{opacity:.25} .node.on{stroke:var(--ink);stroke-width:3}
.hub{fill:var(--bg);stroke:var(--hub);stroke-width:1.5;cursor:pointer}
@media (max-width:860px){.main{grid-template-columns:1fr;grid-template-rows:1fr 42vh}.panel{border-left:0;border-top:1px solid var(--rule)}}
@media (prefers-reduced-motion:reduce){.edge{transition:none}}
</style>
<div class="bar">
  <div class="t"><small>Bereshit / In Principio · K7 · map</small>Genesis 1:2 — the spirit that hovers</div>
  <div class="modes" role="group" aria-label="Arrange by">
    <button data-mode="answers" aria-pressed="true">Answers</button>
    <button data-mode="time" aria-pressed="false">Time</button>
    <button data-mode="place" aria-pressed="false">Places</button>
    <button data-mode="sense" aria-pressed="false">Senses</button>
  </div>
  <div class="f" id="filters">
    <label class="cites"><input type="checkbox" checked data-type="cites"><i></i>cites</label>
    <label class="echoes"><input type="checkbox" checked data-type="echoes"><i></i>echoes</label>
    <label class="contests"><input type="checkbox" checked data-type="contests"><i></i>contests</label>
    <label class="parallel"><input type="checkbox" checked data-type="parallel"><i></i>parallel</label>
    <label class="transmits"><input type="checkbox" checked data-type="transmits"><i></i>transmits</label>
  </div>
  <div class="trad"><span style="--c:var(--lat)">Latin</span><span style="--c:var(--rab)">Rabbinic</span><span style="--c:var(--grk)">Greek-Jewish</span></div>
</div>
<div class="main">
  <svg id="map" role="img" aria-label="Map of witnesses and threads"></svg>
  <aside class="panel" id="panel"></aside>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js" integrity="sha384-CjloA8y00+1SDAUkjs099PVfnY2KmDC2BZnws9kh8D/lX1s46w6EPhpXdqMfjK6i" crossorigin="anonymous"></script>
<script>
const D = __DATA__;
const svg = d3.select('#map'), panel = document.getElementById('panel');
const g = svg.append('g');
const gRings = g.append('g'), gHubLinks = g.append('g'), gEdges = g.append('g'), gHubs = g.append('g'), gNodes = g.append('g'), gLabels = g.append('g');
let W = 800, H = 600, mode = 'answers';
const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

const wn = D.witnesses.map(w => ({...w, kind: 'w'}));
const byId = Object.fromEntries(wn.map(n => [n.id, n]));
const ansKeys = Object.keys(D.answers), senseKeys = Object.keys(D.senses);
const hubsA = ansKeys.map(k => ({id: 'hub:' + k, kind: 'hub', key: k, label: D.answers[k].label, gloss: D.answers[k].gloss, facet: 'answers'}));
const hubsS = senseKeys.map(k => ({id: 'hub:' + k, kind: 'hub', key: k, label: D.senses[k], gloss: '', facet: 'sense'}));
const hubById = Object.fromEntries([...hubsA, ...hubsS].map(h => [h.id, h]));
const threads = D.threads.map(t => ({...t, source: byId[t.from], target: byId[t.to]})).filter(t => t.source && t.target);
const hubLinksA = wn.flatMap(w => w.answers.map(a => ({source: w, target: hubById['hub:' + a]})));
const hubLinksS = wn.flatMap(w => w.senses.map(s => ({source: w, target: hubById['hub:' + s]})));

let k = 1;
function applyScale() {
  nodeSel.attr('r', d => (d.slot ? 6 : 7) / k).attr('stroke-width', 2 / k);
  labelSel.attr('font-size', 11 / k + 'px').attr('dx', 10 / k).attr('dy', 4 / k);
  edgeSel.attr('stroke-width', d => (d.type === 'contests' ? 1.8 : d.type === 'parallel' ? 2 : 1.4) / k).attr('stroke-dasharray', d => d.type === 'echoes' ? `${5/k} ${4/k}` : d.type === 'parallel' ? `${2/k} ${4/k}` : null);
  if (hubSel) { hubSel.attr('r', 13 / k).attr('stroke-width', 1.5 / k); hubLblSel.selectAll('.hublbl').attr('font-size', 12 / k + 'px').attr('y', 30 / k); hubLblSel.selectAll('.hubsub').attr('font-size', 10.5 / k + 'px').attr('y', 43 / k); hubLinkSel.attr('stroke-width', 1 / k).attr('stroke-dasharray', `${1/k} ${3/k}`); }
  gRings.selectAll('text').attr('font-size', 10 / k + 'px'); gRings.selectAll('circle').attr('stroke-width', 1 / k);
}
svg.call(d3.zoom().scaleExtent([.5, 6]).on('zoom', e => { g.attr('transform', e.transform); if (e.transform.k !== k) { k = e.transform.k; applyScale(); } }));

// ---------- drawing
const edgeSel = gEdges.selectAll('path').data(threads).join('path').attr('class', d => 'edge ' + d.type)
  .on('mouseenter', (e, d) => showEdge(d, true)).on('mouseleave', (e, d) => showEdge(d, false)).on('click', (e, d) => { showEdge(d, true); e.stopPropagation(); });
const nodeSel = gNodes.selectAll('circle').data(wn).join('circle').attr('class', d => 'node ' + d.tradition + (d.slot ? ' slot' : '')).attr('r', d => d.slot ? 6 : 7)
  .on('click', (e, d) => { showWitness(d); e.stopPropagation(); }).on('mouseenter', (e, d) => focusNode(d, true)).on('mouseleave', (e, d) => focusNode(d, false))
  .call(d3.drag().on('start', (e, d) => { d.fx = d.x; d.fy = d.y; }).on('drag', (e, d) => { d.fx = e.x; d.fy = e.y; sim.alpha(.3).restart(); }).on('end', (e, d) => { d.fx = null; d.fy = null; }));
const labelSel = gLabels.selectAll('text').data(wn).join('text').attr('class', 'lbl').text(d => d.short);
let hubSel, hubLblSel, hubLinkSel;

const sim = d3.forceSimulation().on('tick', tick);
function tick() {
  edgeSel.attr('d', d => { const {source: s, target: t} = d; const dx = t.x - s.x, dy = t.y - s.y, dr = Math.hypot(dx, dy) * 1.4; return `M${s.x},${s.y}A${dr},${dr} 0 0,1 ${t.x},${t.y}`; });
  nodeSel.attr('cx', d => d.x).attr('cy', d => d.y);
  labelSel.attr('x', d => d.x).attr('y', d => d.y);
  if (hubSel) { hubSel.attr('cx', d => d.x).attr('cy', d => d.y); hubLblSel.attr('transform', d => `translate(${d.x},${d.y})`); hubLinkSel.attr('x1', d => d.source.x).attr('y1', d => d.source.y).attr('x2', d => d.target.x).attr('y2', d => d.target.y); }
}

function size() { const r = svg.node().getBoundingClientRect(); W = r.width; H = r.height; }

function layout() {
  size(); const cx = W / 2, cy = H / 2, R = Math.min(W, H) / 2 - 40;
  gRings.selectAll('*').remove(); gHubs.selectAll('*').remove(); gHubLinks.selectAll('*').remove(); hubSel = null;
  const labelR = d => d.kind === 'hub' ? 46 : 12 + d.short.length * 2.4;
  sim.nodes(wn).force('charge', null).force('link', null).force('x', null).force('y', null).force('hublink', null).force('collide', d3.forceCollide(labelR).strength(.9));
  if (mode === 'answers' || mode === 'sense') {
    const hubs = mode === 'answers' ? hubsA : hubsS, links = mode === 'answers' ? hubLinksA : hubLinksS;
    hubs.forEach((h, i) => { const a = -Math.PI / 2 + i * 2 * Math.PI / hubs.length; h.fx = cx + Math.cos(a) * R * .9; h.fy = cy + Math.sin(a) * R * .9; h.x = h.fx; h.y = h.fy; });
    sim.nodes([...wn, ...hubs]);
    sim.force('charge', d3.forceManyBody().strength(d => d.kind === 'hub' ? -80 : -320))
       .force('hublink', d3.forceLink(links).distance(mode === 'answers' ? 120 : 150).strength(.6))
       .force('link', d3.forceLink(threads).distance(120).strength(.04))
       .force('x', d3.forceX(cx).strength(.03)).force('y', d3.forceY(cy).strength(.03));
    hubLinkSel = gHubLinks.selectAll('line').data(links).join('line').attr('class', 'hublink');
    hubSel = gHubs.selectAll('circle').data(hubs).join('circle').attr('class', 'hub').attr('r', 13).on('click', (e, d) => { showHub(d); e.stopPropagation(); });
    hubLblSel = gHubs.selectAll('g').data(hubs).join('g');
    hubLblSel.append('text').attr('class', 'hublbl').attr('text-anchor', 'middle').attr('y', 30).text(d => d.label);
    hubLblSel.append('text').attr('class', 'hubsub').attr('text-anchor', 'middle').attr('y', 43).text(d => (mode === 'answers' ? hubLinksA : hubLinksS).filter(l => l.target === d).length + ' witnesses');
  } else if (mode === 'time') {
    const dates = wn.map(d => d.date), d0 = Math.min(...dates), d1 = Math.max(...dates);
    const rOf = d => 50 + (d - d0) / (d1 - d0) * (R - 50);
    [0, 500, 1000].forEach(y => { gRings.append('circle').attr('class', 'ring').attr('cx', cx).attr('cy', cy).attr('r', rOf(y)); gRings.append('text').attr('class', 'ringlbl').attr('x', cx + 4).attr('y', cy - rOf(y) - 4).text(y === 0 ? 'year 1' : y); });
    gRings.append('text').attr('class', 'ringlbl').attr('x', cx + R * .7).attr('y', cy + R + 26).text('LATIN →').attr('text-anchor', 'middle');
    gRings.append('text').attr('class', 'ringlbl').attr('x', cx - R * .7).attr('y', cy + R + 26).text('← RABBINIC').attr('text-anchor', 'middle');
    const groups = {'greek-jewish': [], latin: [], rabbinic: []}; wn.forEach(w => groups[w.tradition].push(w));
    Object.values(groups).forEach(a => a.sort((p, q) => p.date - q.date));
    groups['greek-jewish'].forEach(w => { w.tx = cx; w.ty = cy - rOf(w.date); });
    groups.latin.forEach((w, i, a) => { const t = -Math.PI * .42 + (i / Math.max(1, a.length - 1)) * Math.PI * .84; w.tx = cx + Math.cos(t) * rOf(w.date); w.ty = cy + Math.sin(t) * rOf(w.date); });
    groups.rabbinic.forEach((w, i, a) => { const t = Math.PI + Math.PI * .42 - (i / Math.max(1, a.length - 1)) * Math.PI * .84; w.tx = cx + Math.cos(t) * rOf(w.date); w.ty = cy + Math.sin(t) * rOf(w.date); });
    sim.force('x', d3.forceX(d => d.tx).strength(.6)).force('y', d3.forceY(d => d.ty).strength(.6)).force('collide', d3.forceCollide(d => 8 + d.short.length * 1.6).strength(.8));
  } else if (mode === 'place') {
    const lons = wn.map(d => d.lon).filter(Number.isFinite), lats = wn.map(d => d.lat).filter(Number.isFinite);
    const sx = d3.scaleLinear().domain([Math.min(...lons) - 2, Math.max(...lons) + 2]).range([60, W - 120]);
    const sy = d3.scaleLinear().domain([Math.min(...lats) - 1, Math.max(...lats) + 1]).range([H - 50, 50]);
    const seen = new Set();
    wn.forEach(w => { w.tx = sx(w.lon); w.ty = sy(w.lat); if (!seen.has(w.place)) { seen.add(w.place); gRings.append('text').attr('class', 'placelbl').attr('x', w.tx + 12).attr('y', w.ty - 12).text(w.place); } });
    sim.force('x', d3.forceX(d => d.tx).strength(.5)).force('y', d3.forceY(d => d.ty).strength(.5)).force('collide', d3.forceCollide(d => 8 + d.short.length * 1.6).strength(.8));
  }
  applyScale();
  sim.alpha(1).restart();
}

// ---------- panel
function showHome() {
  const q = D.crux.question;
  panel.innerHTML = `<p class="eyebrow">Crux · Genesis 1:2</p><h2>${esc(q.en)}</h2><p class="la-q">${esc(q.la)}</p><p class="heb-q">${esc(q.he)}</p>
  <p>${esc(D.crux.summary)}</p><p>${esc(D.crux.finding)}</p>
  <p class="hint"><b>Answers</b> gathers witnesses around the reading they give; a witness between two hubs holds both. <b>Time</b> is a clock: distance from the centre is the date, Latin to the right, rabbinic to the left. <b>Places</b> is a map. <b>Senses</b> sorts by literal, allegorical, spiritual, translation. Threads keep their meaning in every arrangement. Click a node or a hub; hover a line; drag to pull the graph apart; scroll to zoom: zooming spreads the graph while dots and labels keep their size.</p>`;
}
function showWitness(w) {
  const lem = Object.entries(w.lemma || {}).filter(([k]) => k !== 'en').map(([k, v]) => `<span class="${k === 'he' || k === 'arc' ? 'heb' : 'lat'}" dir="${k === 'he' || k === 'arc' ? 'rtl' : 'ltr'}">${esc(v)}</span>`).join(' ');
  const ocls = (w.olang === 'he' || w.olang === 'arc') ? 'heb' : 'lat';
  const ans = (w.answers || []).map(a => `<span>${esc(D.answers[a]?.label || a)}</span>`).join('');
  const ins = threads.filter(t => t.target === w), outs = threads.filter(t => t.source === w);
  const rel = [...outs.map(t => `→ ${t.type} · ${esc(t.target.short)}`), ...ins.map(t => `← ${t.type} · ${esc(t.source.short)}`)].join('<br>');
  panel.innerHTML = `<p class="eyebrow">${esc(w.tradition.replace('-', ' '))} · ${esc(w.datelabel)} · ${esc(w.place)}</p><h2>${esc(w.author)}</h2><p class="meta">${esc(w.source)}</p>
  <p class="lem">${lem}</p><p>${esc(w.en)}</p><div class="orig ${ocls}">${esc(w.orig)}</div><div class="ans">${ans}</div><p class="note">${esc(w.notes)}</p>
  <p class="cred">${w.translator === 'claude-draft' ? 'Draft English (Claude), awaiting Wilson' : 'English: ' + esc(w.translator)}</p>${rel ? `<p class="cred">${rel}</p>` : ''}`;
  panel.scrollTop = 0;
}
function showHub(h) {
  const links = (h.facet === 'answers' ? hubLinksA : hubLinksS).filter(l => l.target === h);
  panel.innerHTML = `<p class="eyebrow">${h.facet === 'answers' ? 'Answer family' : 'Sense'}</p><h2>${esc(h.label)}</h2><p>${esc(h.gloss)}</p>
  <p class="cred">${links.map(l => esc(l.source.short) + ' · ' + esc(l.source.datelabel)).join('<br>')}</p>`;
  nodeSel.classed('dim', d => !links.some(l => l.source === d)); labelSel.classed('dim', d => !links.some(l => l.source === d));
}
function showEdge(t, on) {
  edgeSel.classed('on', d => on && d === t);
  nodeSel.classed('on', d => on && (d === t.source || d === t.target));
  if (on) { panel.innerHTML = `<p class="eyebrow">${esc(t.type)} · ${esc(t.source.short)} → ${esc(t.target.short)}</p><div class="ev">${esc(t.evidence)}</div>`; }
}
function focusNode(w, on) {
  edgeSel.classed('dim', d => on && d.source !== w && d.target !== w);
  nodeSel.classed('dim', d => on && d !== w && !threads.some(t => (t.source === w && t.target === d) || (t.target === w && t.source === d)));
  labelSel.classed('dim', d => on && d !== w && !threads.some(t => (t.source === w && t.target === d) || (t.target === w && t.source === d)));
}
svg.on('click', () => { nodeSel.classed('dim', false).classed('on', false); labelSel.classed('dim', false); edgeSel.classed('dim', false).classed('on', false); showHome(); });
document.querySelectorAll('.modes button').forEach(b => b.addEventListener('click', () => { mode = b.dataset.mode; document.querySelectorAll('.modes button').forEach(x => x.setAttribute('aria-pressed', x === b)); layout(); }));
document.querySelectorAll('#filters input').forEach(c => c.addEventListener('change', () => { const off = new Set([...document.querySelectorAll('#filters input')].filter(i => !i.checked).map(i => i.dataset.type)); edgeSel.classed('hidden', d => off.has(d.type)); }));
window.addEventListener('resize', () => layout());
size(); wn.forEach(w => { w.x = W / 2 + (Math.random() - .5) * 200; w.y = H / 2 + (Math.random() - .5) * 200; });
showHome(); layout();
</script>
'''
out = ROOT / "out"; out.mkdir(exist_ok=True)
(out / f"B-map-{crux_id}.html").write_text(TEMPLATE.replace("__DATA__", json.dumps(data, ensure_ascii=False)))
print(f"wrote out/B-map-{crux_id}.html ({len(ws)} witnesses, {len(threads)} threads, {len(answers)} answer families)")
