# Limitations

**Status:** draft · promote any addition that would change how a number may be cited

Common Measure inherits the shape of HTTP Archive and then adds its own grain. The following limits are **features of the method**, not temporary bugs. If a claim needs a limit not listed here, the claim is not ready.

## Inherited from HTTP Archive

1. **Root pages, not whole sites.** Features describe the HA root HTML context. A webfont used only on an interior template can be invisible. A webfont on the home page can overstate the rest of the site.
2. **Public, popular web.** Coverage and rank follow HA / CrUX sampling. This is not “every registered domain.”
3. **A monthly snapshot.** There is no real-time refresh and no claim of what a host did last Tuesday.
4. **Two clients, HA’s definitions.** `desktop` and `mobile` are crawl configurations, not a census of devices.

Read HA’s own documentation before treating a Common Measure number as a census of the web.

## Introduced by Common Measure’s grain

5. **Host collisions.** `NET.HOST(page)` merges tenants that share a host (`github.io`, some app platforms, some CDNs). It also splits `www` from apex.
6. **Collapse across root pages.** Presence flags OR together; sizes are quantiles or sums across pages on that host. A multi-brand host is one row.
7. **Service list incompleteness.** Unknown font hosts classify as self-hosted. New CDNs will be under-counted as third-party until the list is updated.
8. **Parse failures are false negatives.** Variable, color, script, license, and family fields are only as good as the parsed payload. “Not variable” on an unparsed file means *not observed*, not *proven static*.
9. **Request-weighted ≠ unique-URL.** Byte and format shares must say which. Chapter-style unique-URL WOFF2 share and request-weighted WOFF2 share are different series.
10. **Scripts ≠ languages.** A Latin+Han cmap is not “this site supports Chinese.”
11. **Family names are observational strings.** They are not a trademark search, not an authorization chain, and may be omitted or capped in Lite cuts.
12. **License fields in font tables are messy.** An OFL flag, if shipped, is a string class — not legal advice.

## What we refuse to claim

- HTTP Archive partnership or endorsement
- Ownership or exclusivity over the raw crawl
- That products include or license font files
- That civic aggregates are a compliance audit
- That font structure *causes* a Core Web Vital
- That a paid row is more “true” than the public aggregate of the same denominator

## Bias to remember in prose

| Easy sentence | Often false because |
|---------------|---------------------|
| “X% of the web uses Google Fonts.” | Universe may be HA root hosts, or webfont hosts, or requests — say which. Theme and plugin defaults inflate Google. |
| “Self-hosted is more sovereign.” | “Self” includes unidentified CDNs. |
| “Sites support script S.” | Files *contain* S. The page may not use it. |
| “Gov sites do Y.” | Inclusion list and false friends are not yet frozen. |

If you are writing from a future free-aggregate table, quote the denominator printed on that table, not this paragraph.
