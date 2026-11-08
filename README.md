---
metadata-version: "1.0.0"
title: "vc.Governance"
description: "Define the repository purpose and the primary governance reading path."
document-type: "overview"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# vc.Governance

vc.Governance defines how agent teams design, assign, write, review, test, integrate, and change software.

Juval Löwy's **The Method** governs system and project design. Appendix C of [Righting Software](<docs/references/Righting Software.pdf>) is the adopted design standard. The human owner's decisions define the role hierarchy and approval authority.

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

- [Table of contents](docs/toc.md): documents grouped by responsibility.
- [Topic index](docs/index.md): direct links for common governance questions.
- [Architecture decision records](docs/adr/README.md): decision context, approval structure, and trade-offs.
- [Repository-local agent skills](.agents/README.md): workflows for maintaining and reviewing governance documentation.
- [Reference index](docs/references/README.md): current local sources and supplementary web resources.

## Repository boundaries

vc.Governance owns the rules, process, decision rights, required evidence, and acceptance criteria. Reusable technical mechanisms belong in the distinct vc.Ifx repository. Agent orchestration belongs in its distinct repository; application business artifacts belong with the consuming application. See [repository ownership](docs/implementation/repository-ownership.md). Shared project access does not merge repository authority or authorize cross-repository edits.

## Status

The repository contains source-derived standards, Standard Technical English rule records, approval responsibilities, artifact contracts, lifecycle gates, and change-control requirements. [Review history](docs/research/source-review.md) records source coverage. [Validation evidence](docs/artifacts/lifecycle-validity-validation.json) identifies what was checked and the limits of those checks. These governance documents do not themselves deploy worker isolation, authenticated approvals, or an independent integration gate.

Retained coding constraints and implementation-reference notes are indexed separately in the table of contents. Removed technology-specific references are not restored; historical review records distinguish them from current source copies.

## Document quality

Every Markdown file uses the [frontmatter and Standard Technical English contract](docs/standards/markdown-authoring.md). Run `python tools/validate_markdown.py` to check metadata, headings, local file links, and selected wording rules. Run `python -m unittest discover -s tests -p test_markdown_validation.py` to check validator behavior.
