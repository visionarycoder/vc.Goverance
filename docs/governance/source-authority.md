---
metadata-version: "1.0.0"
title: "Source authority"
description: "Define governing sources and the rules for resolving source conflicts."
document-type: "governance-policy"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Source authority

## Governing basis

The human owner requires fidelity to Juval Löwy's The Method. Workers may be agents; the design philosophy, design responsibilities, and engineering standards are not replaced with a new agent methodology.

On 2026-11-07 the owner explicitly directed this framework to follow Appendix C, Design Standard. The repository's [item map](../standards/design-standard.md) covers that appendix. The surrounding chapters explain its rationale, scope, and application. The item map is a paraphrase, not a substitute for the source.

## Primary source

Juval Löwy, Righting Software: A Method for System and Project Design, Pearson / Addison-Wesley, copyright 2020, ISBN 978-0-13-652403-8.

Repository reference: [Righting Software](<../references/Righting Software.pdf>).

Verified file identity:

- 480 PDF pages.
- SHA-256: `b9b911aaa7700021644eca54433525c7e181f50b2158ed2dc678091aa9e20792`.
- Printed Arabic page n is PDF page n + 35, using one-based PDF page numbers.
- Appendix C: printed pp. 425-430; PDF pp. 460-465.
- Supplied lifecycle illustration: Figure A-2, printed p. 390; PDF p. 425.
- Lifecycle explanation and review retries: printed pp. 388-389; PDF pp. 423-424.

References such as RS C, System Design Guidelines 4.c refer to the printed heading and item in this edition. Repository identifiers such as `C-SD-4.c` are navigation identifiers, not Löwy's own identifiers.

The human owner supplied the repository copy. Its hash matches the PDF used for the review. Temporary extracted text and rendered research pages are not repository references.

## Three kinds of statements

| Kind | Authority | Examples |
| --- | --- | --- |
| Method standard | Löwy's source, adopted by the human owner | Volatility-based decomposition; project design; binary phase exits |
| Organizational assignment | Explicit human-owner decisions in this conversation | CEO; triumvirate; Application Architect; Test Architect; three-round escalation |
| Enforcement mechanism | A technical implementation of those assigned rights | Separate permissions; protected artifacts; independently controlled integration |

An enforcement mechanism must support the standard and the assigned decision rights. It cannot introduce a different design rule or silently alter the development workflow.

The CEO and triumvirate control application-suite decisions within their assigned authority. The human owner controls the governing framework and delegation of authority. Neither leadership status nor ownership of a detailed design permits departure from an adopted Method directive.

## Directives and guidelines

Appendix C, p. 425 distinguishes rules that must never be violated from advice that should be followed except with strong, unusual justification. Preserve that distinction rather than converting every guideline into either optional advice or an unconditional prohibition.

Workers cannot approve their own departures. A proposed guideline departure must reach its responsible authority, with the source context, justification, and consequences. Authorization must remain within higher-level constraints. The human owner has now reserved approval of every guideline departure. Use the [departure contract](../templates/artifacts/guideline-departure.md) and [decision matrix](decision-and-approval-matrix.md). There is no generic worker bypass. Directives and explicit absolute source prohibitions cannot be waived.

If chapter wording and the checklist appear different, retain both locators and investigate. Do not silently resolve an ambiguity in the direction that simplifies implementation. Verified errata or clarification by Löwy can resolve source questions; a conflict that remains unresolved goes to the human owner with the relevant passages.

## Supplementary primary sources

Use Löwy's own books, articles, interviews, and IDesign publications for clarification. Do not elevate third-party summaries, existing agent skills, or prevailing industry practice over this source.

- [IDesign Method Management Overview, February 2020](https://www.idesign.net/Download/IDesign-Method-Management-Overview.pdf), especially p. 5 on the distinction between architecture and detailed design. This supports the separation of those design scopes. It does not supply the owner's role names.
- [Righting Software Q&A with Juval Löwy, February 10, 2020](https://www.infoq.com/articles/book-review-righting-software/), a supplementary clarification source.
- [Official book page](https://www.idesign.net/Books/Righting-Software) for supporting resources.

Do not assume an undated online standard is identical to this edition's Appendix C. Compare versions before proposing an update to the adopted baseline.

## Verified companion sources and correction

The [official support archive](https://idesign.net/download/Righting-Software-Support-Files.zip) contains the author's planning examples. Its reviewed download has SHA-256 `a5ed6b4242d245b60691b5cd82506a9e04c570b894b3feb9eeaeaaad9971edd1`.

The [publisher errata dated 2021-01-18](https://www.informit.com/content/images/9780136524038/errata/9780136524038_errata_01-18-2021.docx) was reviewed. Its SHA-256 is `1b89023b3245edddb14bd8ec534136cc746079517ebe808c202ad22e5b07f169`. Its listed corrections do not change the adopted Appendix C rule meanings. Some corrections are graphical; extracted text alone does not represent all of them.

The printed ratio on p. 310 is `F = R(tmr) / C(tmr)`. Page 311 instead uses approximately 32.93. The official archive's `Chapter 12 - Advanced Techniques/Risk Crossover.xlsx`, worksheet `Risk Model to Scale`, cells F3:G5, identifies risk and cost and calculates G5 as `G4/G3`, or `C(tmr)/R(tmr)`. On 2026-11-07, the human owner authorized using the companion calculation and retaining this discrepancy. This is an explicit source-resolution decision; it is not an unrecorded change to The Method or a claim that the publisher errata contains the correction.

The companion `Decompression Target.xlsx` uses full-precision coefficients and `-b/(3*a)` to reproduce the 10.62-month result on p. 314. The rounded coefficients printed in the text are insufficient for reproducing all worked results. Use the appropriate full-precision model, not a transcription of rounded display equations.

## Supporting implementation ideas

The owner requested implementation patterns informed by the additional [local references](../references/README.md). The [pattern catalog](../patterns/README.md) records source scope, applicability, constraints, and verification. Supporting material from other authors supplies techniques to evaluate. It does not replace The Method. Löwy's later fractal paper supplies conditional supplementary guidance, not an automatically adopted replacement standard. Pattern records are separate from the 148 source-derived rule records. Architects must select and review any application realization before worker handoff.

## Current implementation guidance

On 2026-11-07 the human owner directed use of Microsoft’s latest coding and code-quality guidance, explicitly prohibiting underscore naming prefixes. The [technical standard](../standards/microsoft-technical-standard.md) governs implementation details within Method boundaries; historical technical books and sample APIs do not override it. The no-prefix rule is an owner-selected override of Microsoft’s documentation-team conventions. SDK and technology baseline changes remain Solution Architect decisions. Technical policies are separate from source-derived Method directives.

## Owner-selected proxy constraint

On 2026-11-07 the owner required DI-capable proxies for calls between components, clarified that internal collaborator calls are excluded, required generated proxies where no service-level separation exists, and prohibited reflection-based proxies. Dapr sidecar invocation is accepted as a realization. This [binding implementation constraint](../patterns/component-proxies.md) is distinct from a claim about Lowy’s source wording. It narrows implementation choices without changing Method interaction rules.

## Decision and artifact contracts

The [approval matrix](decision-and-approval-matrix.md), [recorded owner decisions](owner-decisions-2026-11-07.md), and [artifact contracts](../artifacts/README.md) formalize source responsibilities and owner-selected authority. The schema and record fields are governance format choices. They do not claim that Lowy prescribed JSON, these role titles, or runtime identity mechanics.

## Lifecycle gates and change validity

The [gate criteria](../process/lifecycle-gates.md) operationalize the adopted lifecycle without serializing its parallel branches. The [change-validity rules](change-approval-validity.md) combine the source feedback/project-redesign duties with [explicit owner decisions](owner-decisions-2026-11-08.md) on reaffirmation, freshness, and revocation. Predicate names and record formats are governance mechanisms; they are not new quotations or alternate engineering methods.
