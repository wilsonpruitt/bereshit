import type { APIRoute } from "astro";
import {
  getBuiltCruxes, getAllWitnesses, getPersons, getPlaces, getScripture,
} from "../lib/data";

const STATIC_PAGES = ["/", "/introduction", "/map", "/search", "/colophon", "/export"];

export const GET: APIRoute = ({ site }) => {
  const base = site?.href.replace(/\/$/, "") ?? "https://bereshit.wrootpress.com";
  const urls: string[] = [...STATIC_PAGES];

  for (const c of getBuiltCruxes()) urls.push(`/crux/${c.id}`);
  for (const w of getAllWitnesses().values()) urls.push(`/witnesses/${w.id}`);
  for (const id of Object.keys(getPersons())) urls.push(`/persons/${id}`);
  for (const id of Object.keys(getPlaces())) urls.push(`/places/${id}`);
  for (const v of getScripture().verses) urls.push(`/dialogue/${v.ref.replace(/\./g, "-")}`);

  const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls.map((u) => `  <url><loc>${base}${u}/</loc></url>`).join("\n")}
</urlset>
`;
  return new Response(body, { headers: { "Content-Type": "application/xml" } });
};
