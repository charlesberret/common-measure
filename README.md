# Common Measure

Reference data on how the public web is built, beginning with type.

[HTTP Archive](https://httparchive.org/) publishes monthly crawls of the web. Common Measure turns those crawls into **derived measurements**: documented tables of font and CSS structure, with a grain and a dictionary you can cite.

This is not a second crawl, not a resale of HTTP Archive, and not an archive of font files.

## Direction

The first product is a **[Structure Index](docs/catalog.md#structure-index)** — one row per host and client for a crawl month, covering webfont presence, hosting mix, formats, and CSS practice.

Public methodology and aggregates will ship from that table. This repository is the record: what the data is, how it was made, and where to find a release when one exists.

## Repository

```text
docs/                 explanation, method, limits, citation
data/dictionaries/    column definitions
releases/             published snapshots, when they exist
```

| | |
|--|--|
| [About](docs/about.md) | What this project is |
| [Methodology](docs/methodology.md) | How a release is built |
| [Limitations](docs/limitations.md) | What the numbers cannot say |
| [Citation](docs/citation.md) | How to cite HTTP Archive and this work |
| [Structure Index dictionary](data/dictionaries/structure-index.md) | Column definitions |

A first snapshot is being prepared from the **July 2026** crawl. Nothing has been deposited yet; [releases/](releases/README.md) will list files when they exist.

## Source

Measurements described here are derived from HTTP Archive public data. HTTP Archive is not a partner or endorser of Common Measure.

The public name is **Common Measure** (two words). The site is [commonmeasure.io](https://commonmeasure.io).

## Contact

Charles Berret — [charles@charlesberret.net](mailto:charles@charlesberret.net)

## License

Documentation in this repository is offered under [CC BY 4.0](LICENSE). Released datasets will carry their own license line.
