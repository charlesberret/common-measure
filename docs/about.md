# About Common Measure

**Status:** draft public description · 2026-08

Common Measure is a small reference-data project. It turns **public web crawls** into **derived, domain-keyed measurements** that can be cited, compared, and (in some cuts) purchased.

The first corpus is **web font and CSS structure** as seen by [HTTP Archive](https://httparchive.org/): whether a site serves webfonts, from where, in what formats, with what CSS practice (`font-display`, `unicode-range`, metric overrides), and which writing scripts those files actually cover.

That is a lens, not a permanent fence. Type is treated as **infrastructure** — a structured trace of institutions, platforms, languages, and technical maturity — not as a foundry sales catalog.

## The gap

Most technographic products answer a shallow yes/no: *uses Google Fonts*, *uses WordPress*. They do not productize:

- font-file metadata (variable/color flags, format mix, size, observed family names)
- CSS structural practice
- script/cmap coverage
- joins from that structure to civic lists, language data, or other public registers

HTTP Archive already measures much of this in the open. What it does not do is ship a **packaged, domain-grained, versioned product** with a dictionary, a free aggregate tier, and a clear commercial cut for people who need microdata.

In 2026 there is also no Web Almanac edition, so the usual public synthesis layer is thin while the monthly crawl continues. Common Measure is **not** a private Almanac chapter. It is a separate manufacturing path. If the Almanac returns, the chapter remains editorial synthesis; this project remains tables, dictionaries, and access rules.

## One sentence, two registers

**For researchers and the public.** A shared yardstick for how the web is built, starting with type, published with methodology and free headline numbers.

**For buyers.** Derived feature tables keyed by domain (and aggregates), always citing HTTP Archive and the crawl date — not a cheaper install-flag subscription and not a crawl you can pretend to own.

## What we do not do

- Redistribute font binaries, glyph outlines, or a license to use any typeface
- Resell HTTP Archive wholesale as “our crawl”
- Broker contacts, emails, or personal data
- Offer legal compliance certification (civic charts are observational)
- Claim HTTP Archive or Web Almanac endorsement
- Run a real-time crawl competing on refresh cadence with commercial scanners

## Who it is for

The interesting users are **not only** type foundries and font CDNs. Those may buy. The product has to remain useful if they never do.

| Audience | Why the data exists |
|----------|---------------------|
| Researchers and libraries | Citable aggregates, open methodology, deposit |
| Civic / digital-service teams | How public-sector and education hosts actually load type |
| Journalism and policy | Hosting, sovereignty, and inclusion questions with a documented grain |
| Performance and platform teams | Font payload and CSS-practice structure (not causal CWV claims) |
| Localization / inclusion | Script coverage of *served files*, not marketing language-support claims |

## Lineage (conceptual)

```text
HTTP Archive monthly crawl (public)
        │
        ▼
materialize (font requests + font-relevant CSS)
        │
        ▼
Structure Index  (one row per host × client)
        │
        ├── free aggregates   → this repo, site, academic deposit
        ├── paid strata       → buyers (later)
        └── enrichment joins  → civic lists, script labels, …
```

## Name and surfaces

- **Prose name:** Common Measure (two words)
- **Candidate site:** [https://commonmeasure.io](https://commonmeasure.io)
- **This repository:** public materials and, later, release pointers
- **Related domains** (registered; roles not frozen): `commonmeasure.dev`, `commonmeasure.net`, `commonmeasuredata.com`

Until a single citation URL is locked, cite the dataset’s deposit (DOI when it exists) plus crawl month. Do not invent three competing canonical homes in a paper.

## People

Common Measure is started by [Charles Berret](https://charlesberret.net), who has authored the Web Almanac Fonts chapter in recent editions. That editorial work is separate. It is mentioned here for provenance, not as a claim of Almanac or HTTP Archive partnership.
