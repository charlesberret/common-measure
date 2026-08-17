# Common Measure

**Draft.** This repository is the public home for materials about [Common Measure](https://commonmeasure.io) and its data. Nothing here is a finished release. Numbers, column names, licenses, and access rules will change before the first deposit.

> Common Measure builds **reference data about the visible and technical web**, beginning with global font and CSS structure observed in public crawls.

The first source is [HTTP Archive](https://httparchive.org/). Common Measure does not own that crawl. It manufactures **derived tables**, publishes **free aggregates** with methodology, and (later) sells **domain-level microdata** that brokers of install-flags do not carry.

HTTP Archive is not a partner or endorser of Common Measure.

## Status (2026-08)

| | |
|--|--|
| **Stage** | Founding / pre-release |
| **First crawl month** | July 2026 HTTP Archive |
| **First product** | [Structure Index](docs/catalog.md#structure-index) (domain × client feature table) |
| **First public data** | Free aggregates — not yet deposited |
| **This repo** | Draft documentation, dictionaries, and citation shapes |
| **Site** | [commonmeasure.io](https://commonmeasure.io) (candidate primary; landing still empty) |

If you arrived looking for a downloadable dataset, there is not one yet. Watch [releases/](releases/README.md) and this README.

## What lives here

```text
docs/                 public explanation and policy drafts
data/dictionaries/    column definitions (draft)
releases/             published snapshots, when they exist
```

Bulk extracts and manufacturing code stay out of this tree. This repo is the **face**: what the data is, how it was made, how to cite it, and (when ready) pointers to the files.

| Start here | For |
|------------|-----|
| [docs/about.md](docs/about.md) | What Common Measure is, and is not |
| [docs/methodology.md](docs/methodology.md) | How a release is built |
| [docs/catalog.md](docs/catalog.md) | Products and planned cuts |
| [docs/limitations.md](docs/limitations.md) | What the numbers cannot say |
| [docs/access.md](docs/access.md) | Free, academic, and paid access (draft) |
| [docs/citation.md](docs/citation.md) | How to cite HA and Common Measure |
| [docs/attribution.md](docs/attribution.md) | Required credit lines |
| [data/dictionaries/structure-index.md](data/dictionaries/structure-index.md) | Structure Index columns (draft) |

## Principles (short)

1. **Measure in the open; package the labor.** The crawl is public. The work is the validated extract, the dictionary, and the grain.
2. **Free aggregates earn the right to charge for microdata.** Headline facts should be citable without a invoice.
3. **Academics and libraries are constituents**, not an afterthought.
4. **Depth over breadth.** Win on font/CSS structure and joins that install-flag tools omit — not by being a cheaper BuiltWith.
5. **Always attribute HTTP Archive.** Never claim exclusivity over raw crawl data.
6. **No font files.** Products describe observed use and structure. They are not a license to any typeface.

## Name

**Common Measure** is two words. Handles and domains compress to `commonmeasure`. Do not write “CommonMeasure” in citations or papers.

In typography, a *measure* is the width of a line. In research, a measure is a shared standard of comparison. The name is meant to hold both: a common yardstick for how the public web is built, starting with type as infrastructure rather than as a foundry catalog.

## Contact

Charles Berret — [charles@charlesberret.net](mailto:charles@charlesberret.net)

This GitHub repository currently lives under the personal account `charlesberret`. It may move to a project organization later. Treat **Common Measure** as the public name either way.

## License

Documentation in this repository is offered under [CC BY 4.0](LICENSE). Published datasets will carry their own license line at release (lean: CC BY 4.0 on free aggregates). Unpublished drafts are still drafts: do not treat column lists or access rules as final terms.
