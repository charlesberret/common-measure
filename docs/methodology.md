# Methodology (draft)

**Status:** public working draft · not a citable methodology PDF  
**Companion:** [catalog.md](catalog.md) · [limitations.md](limitations.md) · [structure-index dictionary](../data/dictionaries/structure-index.md)

This page will be rewritten when the first Structure Index export and free aggregates actually ship. Until then it records **intent and known procedure**, not a frozen protocol.

## 1. What is measured

Common Measure measures **observed font and CSS structure on HTTP Archive root pages**, rolled up to the v0 **host × client** grain.

It does **not** measure:

- user behavior, sessions, or people
- private or authenticated pages
- the full internal page graph of a site
- language quality, design quality, or legal font licensing
- Core Web Vitals as caused by fonts (any CWV-adjacent product would need its own method)

A “webfont” here means a font file requested in the HA root-page context, classified by URL, MIME/extension, and (when parseable) font-table payload. A site with no webfont requests is still in the universe: `has_webfont = false`.

## 2. Source

| Item | Working rule |
|------|----------------|
| Source | [HTTP Archive](https://httparchive.org/) public crawl |
| First target month | July 2026 (`date = 2026-07-01` in HA partitions) |
| Clients | `desktop` and `mobile` as labeled by HA |
| Pages | HA **root pages**, not a full-site crawl |
| Rank | Bucketed CrUX-style popularity magnitude on HA root pages (not a dense rank). v0 does **not** pull a separate CrUX rank table. |

HTTP Archive documents its own sampling, device definitions, and coverage. Common Measure inherits those limits. See [limitations.md](limitations.md).

Exact HA table names used in manufacturing may change as extracts are ported. A released dictionary will name the intermediates that actually produced that file.

## 3. Manufacturing (how a month becomes tables)

The expensive work is done **once per crawl month**:

1. **Select** the HA partition for the month and both clients.
2. **Materialize** two working extracts:
   - **font requests** — request rows that are fonts, with payload fields needed for format, variable/color flags, family, scripts
   - **pruned CSS** — font-relevant CSS only (so later CSS-practice queries do not rescan the full parsed-CSS table)
3. **Export** the Structure Index: one row per host × client, with presence, hosting, format, binary flags, and (second pass) CSS-practice columns.
4. **Roll up** free aggregates from that index (and, where honest, from the same extracts).
5. **Enrich** later with lists that do not require another HA scan (civic TLDs, CLDR labels, optional country joins).

The public promise is not “we scanned the web.” It is: **we reduced a public crawl to a documented grain, once, and we say what we threw away.**

Cost discipline is part of method, not just ops: naive repeated scans of the full crawl tables are rejected. If a column is not worth a second full-table pass, it waits.

## 4. Grain

**v0 grain:** `host` × `client`, where `host` is the network host of the HA root-page URL.

Consequences, stated up front:

- `www.example.com` and `example.com` are different hosts unless later normalized.
- Shared hosts (`github.io`, app platforms, some CDNs) collapse many sites into one row.
- Multiple root pages on the same host are collapsed (`OR` for presence flags; quantiles for sizes; `MIN(rank)` among pages that carry the bucketed magnitude, because in HA a lower value is more popular).
- eTLD+1 (Public Suffix List) grain is a later refinement, not the first export.

If marketing copy says “origin,” map it carefully: HA pages are URLs; v0 keys are hosts.

## 5. Feature families

Defined in the [Structure Index dictionary](../data/dictionaries/structure-index.md). In short:

| Family | Examples | Source side |
|--------|----------|-------------|
| Presence & hosting | any webfont; self / Google / Adobe / Font Awesome; service mix | font requests + URL classifier |
| File / binary | variable, color, parseable, format, byte quantiles | font payload / response |
| CSS practice | `font-display`, `unicode-range`, metric overrides, IFT opt-in | pruned CSS |
| Differentiating | scripts present, top families, open-license flags | payload (later / optional in Lite) |
| Enrichment | civic flags, CLDR labels, country | joins after the index exists |

**Scripts present** means Unicode scripts observed in cmap coverage of served files. It is **not** “languages this site supports.”

**Service = self-hosted** includes unknown hosts. The classifier is a list, not omniscience.

## 6. Free aggregates vs microdata

| | Free aggregates | Microdata (paid, later) |
|--|-----------------|-------------------------|
| Grain | national / global / rank-band totals and distributions | host × client rows |
| Purpose | citation, teaching, legitimacy | buyer lists, custom cuts |
| Denominators | must be printed on every table | same dictionary as the index |
| Release | this repo + deposit (Zenodo/Dataverse TBD) | delivery to the buyer |

A public number and a paid table that disagree because they used different denominators is a defect. The dictionary must name the universe: all hosts in the month’s root-page set, including those with no webfonts, unless a table says otherwise.

Suppression rules for small cells are **not written yet**. If a civic or country cut can identify a tiny set of hosts, that cut does not ship until a rule exists.

## 7. Validation (intended)

Before calling an export a release:

- row counts vs materialize (every root-page host × client appears once)
- `has_webfont` vs a known population baseline from the same month
- rank null-rate QA complete per the frozen dictionary (2026-10-06); choosing Lite cutoff `N` remains separate
- sample domains checked by hand (self / Google / none)
- CSS columns isolated so their cost and error modes are visible
- every file meets the release contract in [data/README.md#when-a-file-appears](../data/README.md#when-a-file-appears)

What will **not** be claimed even after that:

- completeness of the public web
- correctness of every family name string
- that unparsed fonts were “not variable”
- legal license status of a file from a name-table string

## 8. Versioning and corrections

Working scheme (unfixed):

- **Release id** = product + crawl month + dictionary revision, e.g. `structure-index-2026-07-v0`
- Breaking column changes increment the dictionary revision and are listed in that release’s changelog
- Errata for a deposited file get a new version of the deposit, not a silent overwrite

This page itself is **not** versioned as a release until it is copied into `releases/<id>/`.

## 9. Reproducibility

HTTP Archive public BigQuery is, in principle, enough to rebuild *some* aggregates. Whether Common Measure publishes the exact export SQL with the free tier is an open decision: reproducibility is a legitimacy good; some query labor is also what the paid cut funds.

Until that is decided, treat this methodology as **descriptive**, not as a rebuild kit.

## 10. Relation to the Web Almanac Fonts chapter

Definitions should not silently drift from the Fonts chapter where both exist (webfont rate, WOFF2 unique-URL share, variable-font page share, and so on). If Common Measure uses a different denominator or a request-weighted instead of unique-URL metric, the dictionary must say so in the column, not in a footnote three pages later.

The chapter is a narrative. This project is a table. They may share ancestry in extraction SQL and still be cited as different works.
