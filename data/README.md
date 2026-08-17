# Data

No dataset files live here yet.

This directory is the **public shelf**: dictionaries now, pointers to released snapshots later. Bulk extracts (Parquet, SQLite, CSV dumps) are not committed to git.

| Path | What |
|------|------|
| [dictionaries/](dictionaries/) | Column definitions. [structure-index.md](dictionaries/structure-index.md) is the first draft. |
| [../releases/](../releases/README.md) | Frozen methodology + download links per published snapshot |

## When a file appears

A release should give you, at minimum:

- crawl month and clients
- product name and dictionary revision
- grain and universe / denominator
- license
- HTTP Archive attribution ([docs/attribution.md](../docs/attribution.md))
- a checksum
- a short known-limitations pointer

If a file is missing any of those, it is a preview, not a release.

## Formats (intent)

| Kind | Likely format |
|------|----------------|
| Free aggregates | CSV + a one-page PDF or markdown methodology |
| Structure Index | Parquet (and CSV if a buyer needs it) |
| Dictionaries | Markdown in this repo; frozen copy beside the files |

## Do not put here

- Font files
- Raw HTTP Archive exports
- Unredacted custom buyer lists
