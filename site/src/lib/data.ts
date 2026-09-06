// Reads the project's data/*.json at build time. No client fetches — Astro inlines everything
// into static HTML at build. Path is relative to this file: ~/bereshit/data.
import fs from "node:fs";
import path from "node:path";

// Vite/Astro bundles this module into build chunks at arbitrary depths, so import.meta.url is not
// a stable anchor. process.cwd() is the Astro project root (~/bereshit/site) for both `astro dev`
// and `astro build`, invoked from there; the data directory is its sibling.
export const DATA_ROOT = path.resolve(process.cwd(), "../data");

function readJSON<T>(rel: string): T {
  return JSON.parse(fs.readFileSync(path.join(DATA_ROOT, rel), "utf-8")) as T;
}

export interface Verse {
  ref: string;
  he: { text: string; source: string; license: string; tokens: { id: string; t: string }[] };
  la: { text: string; source?: string; license?: string };
  en: { text: string; source?: string; license?: string };
}
export interface Scripture { book: string; chapter: number; verses: Verse[] }

export interface Crux {
  id: string;
  verse: string;
  question: { en: string; la: string; he: string };
  lemma: Record<string, string>;
  summary: string;
  witnesses: string[];
  status: "built" | "register-only";
  finding?: string;
  short?: string;
}

export interface Witness {
  id: string;
  work: string;
  author: string;
  tradition: string;
  date: number;
  date_precision?: string;
  place?: string;
  anchor: { verse: string };
  lemma?: Record<string, string>;
  original: { lang: string; text: string; source?: string; license?: string; cc_idno?: string; version?: string };
  english: { text: string; translator?: string; license?: string; status?: string; attribution_required?: boolean; edition?: string; };
  tradents?: string[];
  cruxes: string[];
  senses?: string[];
  answers?: string[];
  notes?: string;
  status_field?: string;
}

export interface Thread { id: string; from: string; to: string; type: string; evidence: string; crux: string }
export interface Person { name: string; he?: string; dates?: string; tradition?: string; role?: string; note?: string }
export interface Place { name: string; lat?: number; lon?: number }
export interface Answer { label: string; gloss: string }
export interface License { label: string; note?: string; attribution?: string
  home?: string;
}

let _witnessCache: Map<string, Witness> | null = null;

export function getScripture(): Scripture {
  return readJSON<Scripture>("scripture/gen-1.json");
}
export function getCruxes(): Crux[] {
  return readJSON<Crux[]>("cruxes.json");
}
export function getBuiltCruxes(): Crux[] {
  return getCruxes().filter((c) => c.status === "built");
}
export function getThreads(): Thread[] {
  return readJSON<Thread[]>("threads.json");
}
export function getPersons(): Record<string, Person> {
  return readJSON<Record<string, Person>>("persons.json");
}
export function getPlaces(): Record<string, Place> {
  return readJSON<Record<string, Place>>("places.json");
}
export function getAnswers(): Record<string, Answer> {
  return readJSON<Record<string, Answer>>("answers.json");
}
export function getLicenses(): Record<string, License> {
  return readJSON<Record<string, License>>("licenses.json");
}
export function getAllWitnesses(): Map<string, Witness> {
  if (_witnessCache) return _witnessCache;
  const dir = path.join(DATA_ROOT, "witnesses");
  const m = new Map<string, Witness>();
  for (const f of fs.readdirSync(dir).sort()) {
    if (!f.endsWith(".json")) continue;
    const w = JSON.parse(fs.readFileSync(path.join(dir, f), "utf-8")) as Witness;
    m.set(w.id, w);
  }
  _witnessCache = m;
  return m;
}
export function getWitness(id: string): Witness {
  const w = getAllWitnesses().get(id);
  if (!w) throw new Error(`no witness ${id}`);
  return w;
}

export function dateLabel(w: Witness): string {
  const prec = w.date_precision || "";
  if (prec.includes("-") && /\d/.test(prec.split("-", 2)[1]?.[0] || "")) {
    const [kind, ...rest] = prec.split("-");
    const rng = rest.join("-");
    return (kind === "range" ? "" : kind + " ") + rng.replace("-", "–");
  }
  const circa = prec === "circa" ? "c. " : "";
  return circa + (w.date < 0 ? `${-w.date} BCE` : String(w.date));
}

export const BOOKS: Record<string, string> = { gen: "Genesis" };
export function verseLabel(ref: string): string {
  const [b, c, v] = ref.split(".");
  return `${BOOKS[b] || b} ${c}:${v}`;
}
