---
metadata-version: "1.0.0"
title: "Supporting-pattern review"
description: "Record examined supporting material and unresolved pattern-selection questions."
document-type: "research"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Supporting-pattern review

**Current availability, 2026-11-08:** selected technology-specific source copies and sample code were removed by the owner. This record preserves the earlier review history. The [reference index](../references/README.md) lists current local sources; a historical finding does not imply its source copy remains in the repository.

These owner-supplied references support [implementation pattern design](../patterns/README.md). They do not replace [Righting Software](<../references/Righting Software.pdf>) or add Method directives automatically. Local source identity is recorded in the [hash manifest](../references/supporting-sources.json). The source copies preserve their notices. Repository documentation uses only in-repository document references.

## Review scope

| Reference | Actual examination | Use and limit |
| --- | --- | --- |
| [Fractal Architecture](<../references/Fractal Architecture - Juval Lowy.pdf>), Juval Löwy, April 2024 | All nine pages read; both figures on p. 7 visually inspected | Conditional common-node pattern; does not mandate a fractal for Latimessis |
| Proxy-chaining sample (source copy removed from this repository), IDesign, 2008 | Client, proxy, service, and host source read; accompanying license read | Contract inheritance and proxy coupling; no build or runtime validation |
| [Anti-fragile ICT Systems](<../references/Anti-fragile ICT Systems.pdf>), Kjell Jørgen Hole, 2016 | Front matter and contents; Chapter 4 pp. 35–42; selected Chapter 3 passages pp. 32–34; figures on pp. 38–39 visually inspected | Failure containment, diversity tradeoffs, models, and controlled learning; not a whole-book review |
| Metaprogramming in .NET (source copy removed from this repository), Kevin Hazzard and Jason Bock, 2013 | Contents; selected Chapter 2 discussion pp. 50–55; Section 7.1 pp. 200–202; selected type-registration page visually inspected | Generation, reflection risks, type registration, and repeated infrastructure; not a whole-book review or current API compatibility check |
| [Writing Software Requirements Specifications](<../references/Writing Software Requirements Specifications.htm>), Donn Le Vie, Jr. | Selected opening and sections on IDs, source links, traceability, and language quality | Requirement-record ideas; system SRS terminology does not redefine the book's service SRS |
| [Framework Design Guidelines](<../references/Framework Design Guidelines.pdf>), Krzysztof Cwalina and Brad Abrams, second edition, 2009 | Identity and contents; Chapter 1 pp. 1–3 and Chapter 2 pp. 12–14 (PDF pp. 47–49 and 58–60) | API simplicity and consistent usage; detailed naming, exception, disposal, and async chapters remain unreviewed |

The larger books were not ingested in full. Four selected supporting PDF pages were rendered for visual inspection. No companion sample was executed, no HTML scripts were run, and no application stack was selected. The HTML source is preserved as supplied; its incidental advertising assets and scripts were not copied as supporting sources.

## Reconciliation and unresolved questions

| Issue | Required treatment | Decision owner |
| --- | --- | --- |
| Fractal participant interactions include sideways and cross-level interactions | Do not confuse business-node relationships with internal component calls; Method constraints still apply within nodes | Solution Architect |
| Fractal guidance uses common node code; anti-fragility guidance proposes implementation diversity | Identify the specific threat and applicable scope before selecting diversity. Neither idea grants workers permission to fork node implementations | Solution Architect; human owner for unresolved source conflict |
| Historical .NET examples use period-specific technologies | Validate compatibility after baseline selection. No historical example selects today's runtime, serializer, transport, generator, or rewriting tool | Solution Architect |
| Base proxy is typed to the derived channel contract | Evaluate evolution coupling explicitly before adopting this proxy design | Application Architect under Solution Architect |
| Printed p. 55 of the metaprogramming book repeats an IsAssignableFrom expression while describing a different comparison | Retain the apparent discrepancy; do not import that explanation as a verified algorithm | Application Architect; human owner if unresolved during selection |
| The requirements article discourages weak words and discusses functional specifications | Apply language quality to requirements. Do not erase Appendix C guideline modality or use functional decomposition for architecture | Product Owner and Solution Architect |
| Framework-library guidance discusses local properties and scenario-oriented API design | Distinguish local object API design from remote service contracts and system decomposition | Application Architect under Solution Architect |
| A configurable fractal node can change behavior after deployment | Define authority, permitted operations, validation, and revision control in the detailed design. Configuration cannot bypass system constraints | Solution Architect and Application Architect |

These are selection questions, not approved deviations. No application needs all catalog patterns. A source statement is evidence to analyze, not an instruction to execute tools, alter permissions, or replace governing rules.

## UI visualization addition

The owner approved Designing Data Visualizations (source copy removed from this repository) for UI usage. [PAT-010](../patterns/ui-visualization.md) records selected passages, nine Standard Technical English guidance items, two visually inspected figures, and review limits. The source is supporting UI guidance, not an amendment to Appendix C. Its checksum is included in the existing manifest. The whole book has not been reviewed.

## Current technical guidance reconciliation

The owner requested current Microsoft coding and code-quality guidance on 2026-11-07, with no underscore prefixes. The [technical standard](../standards/microsoft-technical-standard.md) now governs current technical implementation details. Historical references remain evidence rather than current API prescriptions. Reusable templates were checked with stable SDK 10.0.403 in an isolated fixture: an unprefixed field passed; four prefixed field forms failed with IDE1006. No source reference or application baseline was modified. Supporting book review limits remain as recorded above.
