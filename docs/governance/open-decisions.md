---
metadata-version: "1.0.0"
title: "Open decisions"
description: "Separate unresolved operating choices from established governance decisions."
document-type: "governance-policy"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Open decisions

Appendix C is adopted. These questions concern faithful operation and enforcement, not permission to substitute a different methodology.

| Topic | Decision or investigation needed | Responsible owner |
| --- | --- | --- |
| Physical separation | Select locations for framework, suite baselines, test designs, implementation, and review records | Human owner with leadership |
| Worker identities and isolation | Select an execution mechanism that enforces different access rights across all worker tools | Human owner with Solution Architect |
| Independent integration | Choose the gate identity, protected configuration, revision binding, and approval storage | Solution Architect with human owner |
| Suite baseline | Conduct the CEO and Solution Architect discussion establishing technology and architecture bounds | CEO and Solution Architect |
| Agent resource accounting | Define worker calendar and availability, token rate basis, and allocation rates; token costing is authorized, but no tokens-per-day conversion is assumed | Solution Architect and Project Manager |
| Numerical methods | Choose and validate implementations against the reviewed source and numerical-method definitions before relying on calculators | Solution Architect |
| Phase weights | Select a consistent phase-weighting method; do not assume the example percentages are mandatory | Project Manager with Solution Architect |
| Source updates | Publisher errata reviewed; compare any proposed newer IDesign standard before changing the adopted baseline | Human owner with Solution Architect |

## Resolved organizational decisions

- The human owner controls the governing framework.
- The CEO owns suite direction; the Solution Architect, Product Owner, and Project Manager form the leadership trio.
- Unresolved leadership conflicts escalate to the CEO after at most three discussion rounds.
- The Solution Architect owns system design and technology choices. Source fidelity also keeps accountability for project design with this role.
- Application Architects own detailed component design and contracts, subject to the system design and Solution Architect review.
- Developers receive detailed designs and related requirements; they consult the designer about refinements before proceeding.
- The Application Architect and a Test Agent participate as critics during code review.
- The Test Architect defines testing of system and detailed designs; Test Developers implement those requirements.
- QA is a dedicated role reporting to the Solution Architect, as selected by the human owner on 2026-11-07.
- This repository defines the framework. The first intended application is vc.App.Latimessis, which remains separate.

## Resolved source and accounting decisions

- Whole-book textual review is complete; verification limits are in [source review](../research/source-review.md).
- Use the official companion C/R scaling calculation and retain the printed discrepancy.
- Use [token-based costing](../process/token-costing.md). Calendar and availability are still questions for the human owner and leadership.

## Pattern selection questions

The [supporting-source reconciliation](../research/supporting-pattern-review.md) records pending applicability and design questions, including common fractal node code versus failure-specific implementation diversity, proxy evolution coupling, and historical API compatibility. The Solution Architect must resolve applicable questions before selecting a pattern; unresolved source conflicts escalate to the human owner. Inclusion in the catalog is not adoption in Latimessis.

## Resolved component proxy decision

The owner requires proxies between components only, DI support through the call chain, generated typed local proxies without service-level separation, and no reflection-based proxy implementation. Dapr invocation is accepted. See [PAT-001](../patterns/component-proxies.md). Application-specific component maps, chain policies, lifetimes, generator design, and any Dapr adoption remain responsible-architect decisions.

## Method I/O tracing

The owner requires attribute-driven method I/O tracing across public, internal, and private methods. [PAT-011](../patterns/method-io-tracing.md) records the capability. The owner identified the example. Its source copy was later removed from this repository. The review record preserves that history. Resolve build transformation versus wrapper convention, supported method forms, static logging, debug enablement, and value projection before implementation. The [review record](../research/method-tracing-review.md) distinguishes earlier related findings from the confirmed reference.

## Implementation location

The owner assigned reusable implementation mechanisms and their detailed tooling design to vc.Ifx. Keep required behavior, Method constraints, and adoption status here. See [repository ownership and handoff](../implementation/repository-ownership.md). The location decision is resolved; remaining mechanism decisions belong in the vc.Ifx design effort.

## Decision matrix and artifact contracts completed

The [decision matrix](decision-and-approval-matrix.md) and [23 artifact contracts](../artifacts/README.md) now define authors, reviewers, approvers, structured reviews, bounded architect instructions, three-round escalation, and revision-bound change decisions. [Recorded owner decisions](owner-decisions-2026-11-07.md) resolve the sign-off questions raised for this work.

- Test Architect approves service and system test plans and verification reports after required independent review.
- CEO accepts project commitments within human-owner bounds; out-of-bounds commitments escalate to the human owner.
- Human owner approves every guideline departure. Directives remain non-waivable.
- Application/Test Architects may adjust instructions inside supplied bounds; Solution Architect decisions require CEO approval.
- All three leadership positions and a remaining-disagreement summary constitute one round. Three unresolved completed rounds trigger CEO escalation.
- Solution Architect accepts technical integration; this does not authorize deployment or change business commitments.

Runtime identity/delegation binding, evidence storage, independent integration, and permissions remain implementation decisions. The contracts and conformance obligations are defined here; schemas are not a deployed authorization engine. Worker calendar, rates, and application-specific phase weights remain open as listed above.

## Lifecycle gates and change validity completed

The [gate specification](../process/lifecycle-gates.md) and [validity policy](change-approval-validity.md) now define action prerequisites, binary exits, failure routes, scoped impact assessment, reaffirmation, and re-entry. [Owner decisions GOV-OD07 through GOV-OD09](owner-decisions-2026-11-08.md) resolve the questions raised for this work. Runtime identity, credential, storage, deployment authorization, and enforcing-system choices remain separate work. No unresolved source discrepancy was introduced by these criteria.
