# Common Measure

Reference data about **how the public web is built**, starting with **font and CSS structure** observed in [HTTP Archive](https://httparchive.org/) crawls.

Common Measure does not run its own crawl. It publishes **derived, domain-keyed measurements**: documented reductions of the public crawl into tables you can cite, compare, and join to other registers. The first table line is the **Structure Index**—host-level webfont presence, service mix, format and byte summaries, and font-related CSS practice (`font-display`, `unicode-range`, and related signals). A draft column dictionary lives in this repository.

Status is pre-release. There is no dataset to download yet.

## Who it is for

People who need **reproducible structure** on how sites load type—not a shallow install flag and not a private copy of the crawl:

- research, libraries, and policy work that cites a defined grain and denominator
- journalism and civic technology asking hosting, inclusion, and practice questions with a documented universe
- performance and platform teams studying font payload and CSS structure (not causal performance claims)

Type foundries and CDNs may use the same tables; they are not the only audience.

## Boundaries

- **Not a second crawl.** Observations come from HTTP Archive’s public monthly crawl; we name the month on every output.
- **Not crawl resale.** We do not redistribute HTTP Archive wholesale or imply ownership of the underlying logs.
- **Not font files.** Family names and metadata in the tables are evidence of what was **served**, not a license to use those fonts or a redistribution of font binaries.

HTTP Archive is the **source**; Common Measure is the methodology, grain, and dictionary. **HTTP Archive is not a partner or endorser** of Common Measure.

## How to use this repository

| Path | Role |
|------|------|
| [`docs/`](docs/README.md) | Working methodology, limitations, attribution, and citation |
| [`data/dictionaries/`](data/dictionaries/) | Field definitions (Structure Index draft) |
| [`releases/`](releases/README.md) | Published snapshots—crawl month, license, checksums, and links |

When a snapshot is listed under `releases/`, treat that README as the entry point: grain, universe, license, and checksum before you cite numbers. Until then, treat figures in `docs/` as illustrative planning copy, not as a Common Measure release.

Contact Charles Berret at charles@charlesberret.net

Documentation in this repository is offered under [CC BY 4.0](LICENSE).
