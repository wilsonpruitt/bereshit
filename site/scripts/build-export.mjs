/**
 * Bulk export: the structured graph (cruxes, witnesses, threads), one JSON
 * document, not per-page siblings — this corpus is structured argument, not
 * running prose (~/open-corpus/PLAN.md §4's own note for this site). Builds
 * locally into export/ at the repo root; hosting is the shared Cloudflare
 * R2 bucket `wroot-corpus-export`, prefix `bereshit/`, per PLAN.md item 8.
 *
 * Run: node scripts/build-export.mjs (from site/)
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SITE_DIR = path.resolve(__dirname, "..");
const REPO_ROOT = path.resolve(SITE_DIR, "..");
const DATA_ROOT = path.join(REPO_ROOT, "data");
const EXPORT_DIR = path.join(REPO_ROOT, "export");

const SITE_URL = "https://bereshit.wrootpress.com";
const today = new Date().toISOString().slice(0, 10);

function readJSON(rel) {
  return JSON.parse(fs.readFileSync(path.join(DATA_ROOT, rel), "utf-8"));
}

const cruxes = readJSON("cruxes.json").filter((c) => c.status === "built");
const threads = readJSON("threads.json");
const persons = readJSON("persons.json");
const places = readJSON("places.json");
const answers = readJSON("answers.json");
const licenses = readJSON("licenses.json");

const witnesses = {};
for (const file of fs.readdirSync(path.join(DATA_ROOT, "witnesses"))) {
  if (!file.endsWith(".json")) continue;
  const w = JSON.parse(fs.readFileSync(path.join(DATA_ROOT, "witnesses", file), "utf-8"));
  witnesses[w.id] = w;
}

const graph = {
  site: "bereshit",
  url: SITE_URL,
  generated: today,
  license_own_work: "CC BY 4.0",
  license_note:
    "Public-domain source texts are not claimed. This edition's own English translations, apparatus, and encoding are CC BY 4.0. Some source texts carry their own third-party licence (CC BY-SA via Sefaria/Wikisource) — see each witness's own license field and https://bereshit.wrootpress.com/colophon for the per-witness breakdown.",
  cruxes: cruxes.map((c) => ({
    id: c.id,
    url: `${SITE_URL}/crux/${c.id}/`,
    verse: c.verse,
    question: c.question,
    summary: c.summary,
    finding: c.finding || null,
    witnesses: c.witnesses,
  })),
  witnesses: Object.values(witnesses).map((w) => ({
    id: w.id,
    url: `${SITE_URL}/witnesses/${w.id}/`,
    author: persons[w.author]?.name || w.author,
    tradition: w.tradition,
    date: w.date,
    original: w.original,
    english: w.english,
    cruxes: w.cruxes,
  })),
  threads: threads.map((t) => ({ id: t.id, from: t.from, to: t.to, type: t.type, evidence: t.evidence, crux: t.crux })),
  persons,
  places,
  answers,
  licenses,
};

fs.mkdirSync(EXPORT_DIR, { recursive: true });
const fileName = `bereshit-${today}.json`;
fs.writeFileSync(path.join(EXPORT_DIR, fileName), JSON.stringify(graph, null, 2));

const readme = `# Bereshit / In Principio — bulk export

Generated ${today}. ${graph.cruxes.length} built cruxes, ${graph.witnesses.length}
witnesses, ${graph.threads.length} threads — the structured argument graph, not
running prose.

## Files

- \`${fileName}\` — one JSON document: cruxes, witnesses (original + English text
  inline, per-witness license), threads, persons, places, answers, and the license
  table. This is structured argument data — a crux is a question with witnesses and
  threads, not a linear text — treat it as a graph, not a corpus of documents.

## License

Public-domain source texts are not claimed. This edition's own work (English
translations, apparatus, encoding) is [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/),
attribution "bereshit.wrootpress.com (Wilson Pruitt, Wroot Press)". Full terms:
https://bereshit.wrootpress.com/colophon

**Per-witness licensing is mixed** — check each witness's own \`original.license\` /
\`english.license\` field against the \`licenses\` table in this export before reusing a
specific witness's text; some third-party Hebrew/Aramaic material is CC BY-SA
(attribution + share-alike), via Sefaria/Wikisource.

## Hosting

Served from the shared Cloudflare R2 bucket \`wroot-corpus-export\`
(prefix \`bereshit/\`), not baked into any deploy — see \`~/open-corpus/PLAN.md\` item 8.
`;
fs.writeFileSync(path.join(EXPORT_DIR, "README.md"), readme);

const manifest = {
  generated: today,
  cruxes: graph.cruxes.length,
  witnesses: graph.witnesses.length,
  threads: graph.threads.length,
  files: [
    {
      name: fileName,
      description: "The structured graph: cruxes, witnesses, threads, persons, places, answers, licenses.",
      size_bytes: fs.statSync(path.join(EXPORT_DIR, fileName)).size,
    },
    {
      name: "README.md",
      description: "Schema, license, and changelog.",
      size_bytes: fs.statSync(path.join(EXPORT_DIR, "README.md")).size,
    },
  ],
};
fs.writeFileSync(path.join(EXPORT_DIR, "manifest.json"), JSON.stringify(manifest, null, 2));

// Copy for the /export page to import at Astro build time.
fs.mkdirSync(path.join(SITE_DIR, "src", "data"), { recursive: true });
fs.writeFileSync(
  path.join(SITE_DIR, "src", "data", "export-manifest.json"),
  JSON.stringify(manifest, null, 2)
);

console.log(
  `Built export: ${graph.cruxes.length} cruxes, ${graph.witnesses.length} witnesses, ${graph.threads.length} threads -> ${EXPORT_DIR}`
);
