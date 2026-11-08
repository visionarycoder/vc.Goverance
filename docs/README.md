---
metadata-version: "1.0.0"
title: "Documentation guide"
description: "Provide the reading path and ownership map for agentic development governance."
document-type: "overview"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Documentation guide

This documentation defines how agent teams design, assign, construct, review, test, integrate, and change software under Juval Löwy's The Method. It separates engineering standards, human-owner decisions, and proposed enforcement mechanisms.

## Read in this order

1. [Source authority](governance/source-authority.md) and [sources and bibliography](sources.md): governing edition, Amazon book links, source access, and review limits.
2. [Design standard](standards/design-standard.md): the adopted Appendix C directives and guidelines.
3. [Roles and decision rights](governance/roles-and-decisions.md), [approval matrix](governance/decision-and-approval-matrix.md), and [approval structure ADR](adr/0001-approval-process-structure.md): accountable owners, independent critics, deciders, and escalation.
4. [System and project design](process/system-and-project-design.md): business behavior, volatility, feasible project options, and accepted commitments.
5. [Service lifecycle](process/service-lifecycle.md) and [gate criteria](process/lifecycle-gates.md): parallel planning/design paths, bounded handoffs, correction loops, and binary phase exits.
6. [Change and approval validity](governance/change-approval-validity.md): revision binding, impact assessment, reaffirmation, and scoped resumption.
7. [Artifact contracts](artifacts/README.md) and [templates](templates/artifacts/README.md): required records and evidence.
8. [Repository-local skills](../.agents/README.md): instructions for writing and reviewing this documentation.

## Find the controlling document

Use the [table of contents](toc.md) for documents grouped by responsibility and the [topic index](index.md) for governance questions. [Architecture decision records](adr/README.md) explain adopted decisions. [Open decisions](governance/open-decisions.md) identify unresolved operating and enforcement choices. Research records preserve historical review findings; they do not issue approvals.

## Ownership and authority

vc.Governance owns Method rules, decision rights, process, required constraints, and acceptance criteria. Reusable implementation mechanisms belong in vc.Ifx. Orchestration and consuming application artifacts remain in their distinct owning repositories. See [repository ownership](implementation/repository-ownership.md).

Workers cannot change upstream constraints or approve their own implementation or tests. Every allowable guideline departure requires human-owner approval. Directives remain non-waivable. Documents, schemas, and skills do not deploy authenticated approvals or worker isolation; see [enforcement boundaries](implementation/enforcement-boundaries.md).

## Source access

The reference directory and its document copies were removed by the owner. Use [Amazon book links and external sources](sources.md). Do not restore removed PDFs to fix a link. Obtain authorized source access when verification requires the actual text. Preserve edition-specific printed locators and historical review limits.

## Maintain documentation

Use [Standard Technical English and frontmatter](standards/markdown-authoring.md). Keep Markdown, JSON rules, approval routes, gates, templates, and navigation consistent. Updated bytes do not inherit an old approval automatically.

From the repository root, run:

```text
python tools/validate_markdown.py
python -m unittest discover -s tests -p test_markdown_validation.py
```

Validation checks structure, local links, and selected wording. It does not prove source fidelity, authenticate evidence, or grant approval.
