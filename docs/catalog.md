# Data catalog (draft)

**Status:** planned products · no files published yet  
**See also:** [methodology.md](methodology.md) · [access.md](access.md)

This is the public list of what Common Measure intends to make from the HTTP Archive crawl. It is not an inventory of downloadable files. When a snapshot exists, it will be listed in [../releases/](../releases/README.md) and linked from here.

## Structure Index

**Role:** master domain-keyed feature table. Other paid cuts are filters or enrichments of this table.  
**Grain (proposed):** one row per `host` × `client` (`desktop` / `mobile`).  
**Universe:** hosts present on HTTP Archive root pages for the crawl month, **including** hosts with no webfonts.  
**First target:** July 2026.

Feature families (detail in the [dictionary](../data/dictionaries/structure-index.md)):

- webfont presence
- hosting / service mix (self, Google, Adobe, Font Awesome CDN, combinations)
- format mix and byte summaries
- variable / color / parseable flags
- CSS practice (`font-display`, `unicode-range`, metric overrides, IFT)
- optional: script bitset, capped family names, rank for Lite strata

**Packaging (later, names not frozen):**

| Cut | Intent |
|-----|--------|
| Lite | rank-bounded panel + dictionary |
| Full | broader panel |
| Custom | buyer-supplied domain list, left-joined |

No Lite cutoff is published until rank null-rate is checked.

## Free aggregates

**Role:** the public tier. Totals and distributions that can be cited without buying microdata.

Likely first tables (short on purpose):

- webfont adoption by client
- service mix (self vs Google vs hybrid vs none)
- `font-display` distribution
- variable-font adoption
- later: script-coverage headlines, civic-cut headlines

Every aggregate must print its **denominator**. “Percent of hosts with a webfont” and “percent of font-requesting hosts using Google” are different sentences.

**License lean:** [CC BY 4.0](../LICENSE) on the tables and the methodology that ships with them, plus HTTP Archive attribution. Not final until the first deposit.

**Distribution lean:** this repository, [commonmeasure.io](https://commonmeasure.io), and an academic deposit (Zenodo or Dataverse — not chosen).

## Civic cut

**Role:** Structure Index restricted to public-sector and education-relevant hosts.  
**Why it is not a type-industry product:** digital-service teams, civic tech, journalists, accessibility consultants.

Working inclusion: `.gov`, `.mil`, `.edu`, selected national government TLDs, and published civic domain lists. Inclusion rules and false friends (commercial `.edu`, parked lookalikes) will be documented before any civic file is called a release.

- **Free:** national aggregate charts, carefully worded. Not a compliance certificate.
- **Paid:** domain-level civic panel.

## Script and language coverage atlas

**Role:** which Unicode **scripts** appear in served font files, optionally labeled with CLDR.  
**Why:** digital inclusion, localization, CJK/IFT narrative — questions install-flag tools do not ask.

Working split:

- **Free:** country- or rank-band cubes
- **Paid:** domain-level script vectors

**Do not read this as language support.** Cmap coverage is not typography quality, is not UI language, and is not a localization audit.

## Later (not commitments)

These appear in internal founding notes. They are listed so the catalog is honest about the horizon — not so they can be sold today.

| Working name | Only if |
|--------------|---------|
| Hosting / sovereignty view | Service-mix inference limits are stated |
| Variable-font maturity panel | Distinct from Structure Index columns |
| Public-company (EDGAR) join | Entity resolution notes exist |
| CWV-adjacent font risk | No causal overclaim; own method page |
| Foundry / license map | Remains optional; does not recenter the ICP on foundries |
| Newsroom fingerprint clusters | **Ethics-gated**; no public demo until a checklist exists |

## What you will never find in the catalog

- Font files
- Raw HAR or wholesale HA dumps branded as a Common Measure crawl
- Email / contact enrichment
- A live “does this domain use X, updated hourly” scanner
