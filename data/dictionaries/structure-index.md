# Structure Index v0 — data dictionary (draft)

**Status:** draft for the first export — **not** a published buyer dictionary  
**Release target:** HTTP Archive crawl month **2026-07**  
**Companions:** [catalog](../../docs/catalog.md) · [methodology](../../docs/methodology.md) · [limitations](../../docs/limitations.md)

Ship a frozen revision of this file with the first export. Change columns only with a changelog note.

---

## 1. Identity

| Field | Value |
|-------|--------|
| Product | Structure Index |
| Version | v0 (MVP column set) |
| Grain (proposed) | one row per **`host` × `client`** |
| Host definition | network host of the HTTP Archive root-page URL |
| Clients | `desktop`, `mobile` (HA labels) |
| Universe | all hosts present on HA root pages for the crawl date, **including sites with no webfonts** |
| Rank | HA popularity rank already on those pages — not a separate CrUX pull for v0 |

### Grain notes (open)

- **Host vs full page URL vs eTLD+1 (Public Suffix List).** v0 proposes host. Multi-tenant hosts (e.g. `github.io`) collapse many sites into one row — that is a documented bias. PSL registrable-domain grain is a later refinement.
- **Several root pages per host.** Presence flags use a logical OR; sizes use quantiles or sums; `rank` uses the minimum (in HA, lower = more popular).
- **“Origin.”** If prose says origin, map it to host (+ scheme later). HA `page` values are URLs.

---

## 2. Column set

Types are indicative (BigQuery-ish). A released Parquet schema may use equivalents.

### 2.1 Keys and crawl metadata

| Column | Type | Definition | Null / bias |
|--------|------|------------|-------------|
| `crawl_date` | date | HA crawl partition date | should be non-null for a release |
| `client` | string | `desktop` or `mobile` | — |
| `host` | string | network host of the root-page URL | empty host rare; filter or flag |
| `page_example` | string | one representative root-page URL for the host | **not** a stable identifier |
| `rank` | int | HA popularity rank on the root page(s); minimum if several pages | nulls possible; check before Lite cutoffs |
| `n_root_pages` | int | distinct root-page URLs collapsed into this host | usually 1 |

**Lite strata (later):** `rank IS NOT NULL AND rank <= N` (N not chosen).

### 2.2 Presence and hosting (request-side)

| Column | Type | Definition | Null / bias |
|--------|------|------------|-------------|
| `has_webfont` | bool | at least one root-page font request for this host×client | false when none (left join) |
| `uses_self_hosted` | bool | any font URL classified self-hosted | “self” includes unknown CDNs not on the service list |
| `uses_google` | bool | any Google Fonts / gstatic fonts URL | theme and plugin defaults inflate this |
| `uses_adobe` | bool | any Adobe Fonts / Typekit URL | — |
| `uses_fontawesome_cdn` | bool | any `fontawesome.com` font URL | icon fonts, not body text |
| `service_combo` | string | sorted distinct service labels, comma-separated | empty if no webfonts |
| `n_font_requests` | int | count of font request rows | 0 if none |
| `n_distinct_font_urls` | int | distinct font URLs | — |

### 2.3 File and binary flags (request-side)

| Column | Type | Definition | Null / bias |
|--------|------|------------|-------------|
| `has_variable_font` | bool | any font with variable tables (`gvar` / `CFF2`) | unparsed fonts → false negative |
| `has_color_font` | bool | any color font by table-size gates | very rare; expect mostly false |
| `has_parsed_font` | bool | any font with parseable table-size payload | — |
| `dominant_format` | string | mode of file format among font requests | null if no fonts; ties broken arbitrarily |
| `woff2_request_share` | float | share of **requests** that are WOFF2 | request-weighted |
| `woff2_unique_url_share` | float | share of **distinct URLs** that are WOFF2 | prefer this for YoY-style claims |
| `font_bytes_p50` | int | median response body size over font requests | null if no sizes; request-weighted |
| `font_bytes_sum` | int | sum of font body sizes (same client×host) | double-counts a URL requested twice |

### 2.4 CSS practice (second pass)

| Column | Type | Definition | Null / bias |
|--------|------|------------|-------------|
| `has_font_display_swap` | bool | any rule with `font-display: swap` | only font-relevant CSS is kept |
| `has_font_display_block` | bool | … `block` | — |
| `has_unicode_range` | bool | any `unicode-range` | — |
| `has_metric_override` | bool | metric-override properties as defined in the extract | sparse |
| `has_ift_tech_incremental` | bool | IFT `tech(incremental)` opt-in | expect near-zero; absence is the story |

CSS columns may ship in this table or in a sibling export so their cost stays visible. Not required for a request-side-only first dry-run.

### 2.5 Later differentiators (same extracts; not required for first dry-run)

| Column | Type | Definition | Notes |
|--------|------|------------|-------|
| `has_ofl_font` | bool | any font whose name-table / license field classifies as OFL (class TBD) | strings are messy |
| `scripts_present` | string or list | distinct Unicode scripts from cmap codepoints | **not** “languages spoken” |
| `top_family_1` … `top_family_k` | string | top-k family names by request count | cap *k*; Lite may omit |
| `has_preload_font` / `has_preconnect` | bool | resource hints | may need an extra page-level join |

### 2.6 Enrichments (not v0 manufacture columns)

| Flag / column | How | Dependency |
|---------------|-----|------------|
| `is_civic` / sector flags | host TLD + published lists | after the index exists; no new crawl |
| CLDR language / territory labels | join on `scripts_present` (± country) | script flags first |
| CrUX country | separate join | only if a national cut is needed |
| EDGAR / Wikidata | external domain lists | later |

---

## 3. Source map (conceptual)

```text
HA root pages     → universe, client, page, rank
font requests     → presence, hosting, binary flags, scripts, families
pruned CSS        → font-display, unicode-range, metric overrides, IFT
URL classifier    → service labels (Google, Adobe, self, …)
external (later)  → PSL, civic lists, CLDR, extra CrUX country
```

Exact warehouse table names belong in a release appendix, not in this living draft.

---

## 4. Disclose with every export

1. Root-page only — not a full-site crawl.
2. Popularity bias — HA / CrUX sampling, not all domains.
3. Service list incompleteness — unknown hosts → self-hosted.
4. Parse failures → false negatives on variable / color / script / license.
5. Host-grain collisions — shared hosts, CDNs, parkers.
6. Format metrics — request share ≠ unique-URL share; label which.
7. Scripts ≠ language support.
8. No font files shipped — observational metadata only.

---

## 5. v0 freeze checklist

- [ ] Confirm grain: host × client (this draft) vs page × client
- [ ] Confirm Lite cutoff on `rank` after null-rate check
- [ ] Freeze P0 column list for first delivery
- [ ] CSS columns: same table or sibling file
- [ ] Family columns: include / cap / omit in Lite
- [ ] Attribution + crawl date on every file
- [ ] Promote this file from draft → release dictionary when the first export ships

---

## 6. Change log

| Date | Change |
|------|--------|
| 2026-08-17 | Public draft, adapted from the internal v0 column list (2026-08-04). Warehouse identifiers and unpublished population rates omitted on purpose. |
