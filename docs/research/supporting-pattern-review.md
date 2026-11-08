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

**Current availability, 2026-11-08:** the owner removed the reference directory and earlier selected sample copies. This record preserves historical review findings. [Sources and bibliography](../sources.md) lists Amazon book links and external article locations. No local source copy is supplied.

These owner-supplied references support [implementation pattern design](../patterns/README.md). They do not replace [Righting Software](https://www.amazon.com/dp/0136524036) or add Method directives automatically. Historical source-copy identity is recorded in the [identity manifest](source-identities.json). Book citations now use Amazon links; articles use external source locations. A citation does not imply current access to the text.

## Review scope

| Reference | Actual examination | Use and limit |
| --- | --- | --- |
| [Fractal Architecture](https://www.idesign.net/Resources), Juval Löwy, April 2024 | All nine pages read; both figures on p. 7 visually inspected | Conditional common-node pattern; does not mandate a fractal for Latimessis |
| Proxy-chaining sample (source copy removed from this repository), IDesign, 2008 | Client, proxy, service, and host source read; accompanying license read | Contract inheritance and proxy coupling; no build or runtime validation |
| [Anti-fragile ICT Systems](https://www.amazon.com/dp/3319300687), Kjell Jørgen Hole, 2016 | Front matter and contents; Chapter 4 pp. 35–42; selected Chapter 3 passages pp. 32–34; figures on pp. 38–39 visually inspected | Failure containment, diversity tradeoffs, models, and controlled learning; not a whole-book review |
| [Metaprogramming in .NET](https://www.amazon.com/dp/1617290262) (source copy removed from this repository), Kevin Hazzard and Jason Bock, 2013 | Contents; selected Chapter 2 discussion pp. 50–55; Section 7.1 pp. 200–202; selected type-registration page visually inspected | Generation, reflection risks, type registration, and repeated infrastructure; not a whole-book review or current API compatibility check |
| [Writing Software Requirements Specifications](https://techwhirl.com/writing-software-requirements-specifications/), Donn Le Vie, Jr. | Selected opening and sections on IDs, source links, traceability, and language quality | Requirement-record ideas; system SRS terminology does not redefine the book's service SRS |
| [Framework Design Guidelines](https://www.amazon.com/dp/0321545613), Krzysztof Cwalina and Brad Abrams, second edition, 2009 | Identity and contents; Chapter 1 pp. 1–3 and Chapter 2 pp. 12–14 (PDF pp. 47–49 and 58–60) | API simplicity and consistent usage; detailed naming, exception, disposal, and async chapters remain unreviewed |

The larger books were not ingested in full. Four selected supporting PDF pages were rendered for visual inspection. No companion sample was executed, no HTML scripts were run, and no application stack was selected. The saved HTML source was also removed. Its earlier review did not execute scripts or copy incidental advertising assets.

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

The owner approved [Designing Data Visualizations](https://www.amazon.com/dp/1449312284) (source copy removed from this repository) for UI usage. [PAT-010](../patterns/ui-visualization.md) records selected passages, nine Standard Technical English guidance items, two visually inspected figures, and review limits. The source is supporting UI guidance, not an amendment to Appendix C. Its checksum is included in the existing manifest. The whole book has not been reviewed.

## Current technical guidance reconciliation

The owner requested current Microsoft coding and code-quality guidance on 2026-11-07, with no underscore prefixes. The [technical standard](../standards/microsoft-technical-standard.md) now governs current technical implementation details. Historical references remain evidence rather than current API prescriptions. Reusable templates were checked with stable SDK 10.0.403 in an isolated fixture: an unprefixed field passed; four prefixed field forms failed with IDE1006. No source reference or application baseline was modified. Supporting book review limits remain as recorded above.
