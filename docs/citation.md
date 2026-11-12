# How to cite

**Status:** shapes for later · not final bibliographic policy  
Prefer HTTP Archive’s own recommended citation for the raw crawl. Do not invent one here.

## This project, before a data release

If you need to mention Common Measure as a project (not a dataset):

> Charles Berret. *Common Measure* (draft public materials). https://github.com/charlesberret/common-measure

There is **no DOI** yet. Do not mint a fake one.

## HTTP Archive (raw crawl)

Use whatever [httparchive.org](https://httparchive.org/) / HA docs currently recommend.

Placeholder only:

> HTTP Archive. Public crawl data, July 2026.

Always name the **crawl month**. “HTTP Archive” without a date is not a reproducible source.

## Common Measure free aggregates (once deposited)

```text
Common Measure. “[Dataset title].” [Version / crawl month]. [DOI or URL].
License: [e.g. CC BY 4.0]. Derived from HTTP Archive.
```

Example (fictional — do not copy into a paper):

> Common Measure. “Webfont adoption aggregates.” 2026-07 / v0. https://example.invalid. License: CC BY 4.0. Derived from HTTP Archive.

## Structure Index / paid microdata (once sold)

```text
Common Measure. Structure Index ([SKU], [crawl month]). Delivered [date].
```

If you publish **aggregates you computed** from paid rows, say so, name the crawl month, and do not redistribute the microdata file. The exact clause will live in the paid license; this paragraph is not that license.

## In-file footer (every future CSV / Parquet / PDF)

1. Crawl month and client(s)
2. “Derived from HTTP Archive public data”
3. Common Measure product name + version
4. License line (free vs paid)
5. “HTTP Archive is not a partner or endorser of Common Measure”

## Citation File Format

A machine-readable [CITATION.cff](../CITATION.cff) sits at the repository root. It will be updated when the first dataset is deposited. Until then its `version` is `draft`.
