---
metadata-version: "1.0.0"
title: "vc.Governance"
description: "Govern system and project design, owner architecture constraints, decision rights, and software delivery evidence."
document-type: "overview"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-09"
---

# vc.Governance

vc.Governance defines the reusable rules, architectural constraints, roles, review and approval responsibilities, and evidence contracts for agent-assisted software projects. It governs how teams design systems and projects, assign work, construct components, review results, test, integrate, and manage change.

Juval Löwy's **The Method**, including volatility-based decomposition, governs system and project design. Appendix C of [Righting Software](https://www.amazon.com/dp/0136524036) is the adopted design standard. The human owner's decisions define additional architecture and implementation constraints, the role hierarchy, and approval authority. Owner-selected constraints remain distinct from rules attributed to Löwy.

## Contents

- Source authority, design standards, and source-review records.
- Owner-selected technical constraints, including component proxy requirements and coding standards.
- Role responsibilities, decision routes, lifecycle gates, and change-control policies.
- Artifact schemas, templates, fictional examples, and validation tools.
- Repository-local skills for maintaining governance documentation.

## Start here

1. [Source authority](docs/governance/source-authority.md) — governing sources, interpretation, and directive/guideline distinctions.
2. [Roles and decision rights](docs/governance/roles-and-decisions.md) — accountability and escalation.
3. [Decision and approval matrix](docs/governance/decision-and-approval-matrix.md) — authors, critics, and sign-offs.
4. [System and project design](docs/process/system-and-project-design.md) — business understanding, architecture, project options, and commitments.
5. [Service lifecycle](docs/process/service-lifecycle.md) and [gate criteria](docs/process/lifecycle-gates.md) — handoffs, successful reviews, feedback, and phase exits.
6. [Change and approval validity](docs/governance/change-approval-validity.md) — affected scope, revalidation, reaffirmation, and revocation.
7. [Artifact contracts](docs/artifacts/README.md) and [templates](docs/templates/artifacts/README.md) — the evidence agents exchange.
8. [Open decisions](docs/governance/open-decisions.md) — unresolved operating and enforcement choices.

## Documentation navigation

- [Documentation guide](docs/README.md): reading order, ownership, source access, and maintenance.
- [Table of contents](docs/toc.md): documents grouped by responsibility.
- [Topic index](docs/index.md): direct links for common governance questions.
- [Architecture decision records](docs/adr/README.md): decision context, approval structure, and trade-offs.
- [Repository-local agent skills](.agents/README.md): workflows for maintaining and reviewing governance documentation.
- [Sources and bibliography](docs/sources.md): Amazon book links and supplementary web resources.

## Repository boundaries

| Repository or environment | Responsibility |
| --- | --- |
| vc.Governance | Method rules, owner constraints, roles, process, decision rights, artifact contracts, and acceptance criteria |
| vc.Agentic | Reusable agent skills, supporting task resources, templates, and illustrative component examples |
| vc.Ifx | Reusable runtime libraries, integrations, proxies, compiler tooling, and their executable tests |
| Consuming application | Its business requirements, accepted system and detailed designs, implementation, tests, and operational evidence |
| Selected execution platform | Worker isolation, authenticated identities, permissions, orchestration, and protected integration |

See [repository ownership](docs/implementation/repository-ownership.md) and [enforcement boundaries](docs/implementation/enforcement-boundaries.md). Shared project access does not merge repository authority or authorize cross-repository edits.

## Status

The repository contains source-derived standards, Standard Technical English rule records, approval responsibilities, artifact contracts, lifecycle gates, and change-control requirements. [Review history](docs/research/source-review.md) records source coverage. [Validation evidence](docs/artifacts/lifecycle-validity-validation.json) identifies what was checked and the limits of those checks. These governance documents do not themselves deploy worker isolation, authenticated approvals, or an independent integration gate.

Retained coding constraints and implementation-reference notes are indexed separately in the table of contents. Removed technology-specific references are not restored; historical review records distinguish them from current source copies.

## Document quality

Every Markdown file uses the [frontmatter and Standard Technical English contract](docs/standards/markdown-authoring.md). Run `python tools/validate_markdown.py` to check metadata, headings, local file links, and selected wording rules. Run `python -m unittest discover -s tests -p test_markdown_validation.py` to check validator behavior.

## License

Original repository material uses the [MIT License](LICENSE). Third-party material and referenced publications retain their existing terms. The repository license does not replace those terms or license the cited books and external standards.
