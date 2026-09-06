// Port of scripts/render-daf.py's snippet/marking logic to TypeScript, so the Astro build produces
// the same markup the Python prototype did. Kept close to the original on purpose (Phase 5 spec:
// "pixel for pixel").
import type { Witness, Person, Place, Answer } from "./data";
import { dateLabel } from "./data";

export function escapeHtml(s: string | null | undefined): string {
  return String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c] as string));
}

const NIQQUD = /[\u0591-\u05C7\u05BE\s]*/;
export function hePattern(lemma: string): RegExp | null {
  const letters = [...lemma].filter((c) => c >= "א" && c <= "ת");
  if (!letters.length) return null;
  return new RegExp(letters.map((c) => c.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")).join(NIQQUD.source));
}

export function marked(raw: string, pattern: RegExp | null): string {
  let s = raw || "";
  if (pattern) {
    const m = pattern.exec(s);
    if (m) s = s.slice(0, m.index) + "\x01" + m[0] + "\x02" + s.slice(m.index + m[0].length);
  }
  return escapeHtml(s).replace(/\x01/g, "<mark>").replace(/\x02/g, "</mark>");
}

export function excerpt(s: string, n = 170): string {
  s = s.trim();
  if (s.length <= n) return s;
  const cut = s.slice(0, n);
  const sp = cut.lastIndexOf(" ");
  const trimmed = (sp > 0 ? cut.slice(0, sp) : cut).replace(/[,;:.\s]+$/, "");
  return trimmed + " …";
}

export interface Chip { id: string; short: string }

export interface SnippetVM {
  id: string;
  traditionClass: string;
  isSlot: boolean;
  sig: string;
  dhLang: "he" | "el" | "la";
  dhHtml: string;
  exText: string;
  eyebrow: string;
  authorName: string;
  sourceLabel: string;
  fullParas: string[];
  origLabel: string;
  origClass: "heb" | "grk" | "lat";
  origDir: "rtl" | "ltr";
  origHtml: string;
  notes: string;
  answerLabels: string[];
  credit: string;
  chips: Chip[];
}

export function buildSnippet(
  w: Witness,
  persons: Record<string, Person>,
  places: Record<string, Place>,
  answers: Record<string, Answer>,
  chips: Chip[] = []
): SnippetVM {
  const p = persons[w.author] || {};
  const pl = places[w.place || ""] || {};
  const lem = w.lemma || {};
  const dh = lem.he || (lem as any).arc || lem.la || lem.el || "";
  const dhLang: "he" | "el" | "la" = lem.he || (lem as any).arc ? "he" : lem.el ? "el" : "la";
  const o = w.original;
  const origClass: "heb" | "grk" | "lat" = o.lang === "he" || o.lang === "arc" ? "heb" : o.lang === "el" ? "grk" : "lat";
  const draft = w.english.translator === "claude-draft";
  const translator = w.english.translator || "";
  const credit = draft
    ? "Draft English (Claude), awaiting Wilson"
    : translator === "claude-draft-approved"
    ? "English: fresh draft (Claude), approved by Wilson Pruitt"
    : translator === "wilson-pruitt"
    ? "English: Wilson Pruitt"
    : "English: " + translator;
  return {
    id: w.id,
    traditionClass: w.tradition,
    isSlot: (w as any).status === "slot",
    sig: `${p.name || w.author} · ${dateLabel(w)}`,
    dhLang,
    dhHtml: escapeHtml(dh),
    exText: excerpt(w.english.text),
    eyebrow: `${w.tradition.replace(/-/g, " ")} · ${dateLabel(w)} · ${pl.name || w.place || ""}`,
    authorName: p.name || w.author,
    sourceLabel: o.source || "",
    fullParas: escapeHtml(w.english.text).split(/\n\n+/),
    origLabel: origClass === "heb" ? "Hebrew / Aramaic" : origClass === "grk" ? "Greek" : "Latin",
    origClass,
    origDir: origClass === "heb" ? "rtl" : "ltr",
    origHtml: escapeHtml(o.text).replace(/\n\n+/g, "<br><br>"),
    notes: escapeHtml(w.notes || ""),
    answerLabels: (w.answers || []).map((a) => answers[a]?.label || a),
    credit,
    chips,
  };
}

export function regionSort(ws: Witness[]): Witness[] {
  return [...ws].sort((a, b) => (a.date - b.date) || a.id.localeCompare(b.id));
}
