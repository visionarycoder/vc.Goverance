---
metadata-version: "1.0.0"
title: "Table of contents"
description: "List current governance documents by responsibility."
document-type: "index"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Table of contents

[Repository overview](../README.md) · [Topic index](index.md)

The primary documentation governs how code is designed, assigned, reviewed, tested, and changed. Retained implementation notes appear after governance and process documents. Only current repository files are linked.

## Authority and decision rights

- [Source authority](governance/source-authority.md)
- [Roles and decisions](governance/roles-and-decisions.md)
- [Decision and approval matrix](governance/decision-and-approval-matrix.md)
- [Architecture decision records](adr/README.md)
- [ADR 0001: Approval process structure](adr/0001-approval-process-structure.md)
- [Owner decisions: approvals and artifact contracts](governance/owner-decisions-2026-11-07.md)
- [Owner decisions: approval validity](governance/owner-decisions-2026-11-08.md)
- [Change and approval validity](governance/change-approval-validity.md)
- [Open decisions](governance/open-decisions.md)

## Development process

- [System and project design](process/system-and-project-design.md)
- [Service lifecycle](process/service-lifecycle.md)
- [Lifecycle gate criteria](process/lifecycle-gates.md)
- [Project tracking](process/project-tracking.md)
- [Token based costing](process/token-costing.md)

## Design and review standards

- [Design standard](standards/design-standard.md)
- [Standard Technical English rules](standards/rules.ste.md)
- [Numerical methods](standards/numerical-methods.md)

- [Markdown authoring and validation](standards/markdown-authoring.md)

## Artifact contracts and templates

- [Governance artifact contracts](artifacts/README.md)
- [Artifact templates](templates/artifacts/README.md)

## Repository-local documentation skills

- [Skill catalog](../.agents/README.md)
- [Workflow documentation](../.agents/skills/document-agentic-workflows/SKILL.md)
- [Artifact-contract documentation](../.agents/skills/document-governance-artifacts/SKILL.md)
- [Decision records](../.agents/skills/record-governance-decisions/SKILL.md)
- [Workflow documentation review](../.agents/skills/review-agentic-workflow-docs/SKILL.md)

## Repository and enforcement boundaries

- [Framework and implementation ownership](implementation/repository-ownership.md)
- [Enforcement boundaries](implementation/enforcement-boundaries.md)

## Source and reconciliation records

- [Reference index](references/README.md)
- [Source review](research/source-review.md)
- [Whole-book reconciliation](research/reconciliation.md)
- [Supporting-pattern review](research/supporting-pattern-review.md)
- [Existing method-tracing evidence](research/method-tracing-review.md)

- [Navigation reconciliation](research/navigation-reconciliation.md)

## Retained coding constraints and implementation notes

- [Current Microsoft technical standard](standards/microsoft-technical-standard.md)
- [Implementation pattern catalog](patterns/README.md)
- [Mandatory component proxies](patterns/component-proxies.md)
- [Attribute-driven method I/O tracing](patterns/method-io-tracing.md)
- [UI visualization pattern](patterns/ui-visualization.md)
- [C# technical-policy templates](templates/dotnet/README.md)

## Machine-readable governance records

- [Approval matrix](governance/approval-matrix.json).
- [Lifecycle gate criteria](process/lifecycle-gates.json).
- [Change and approval validity](governance/change-approval-validity.json).
- [Method rule records](standards/rules.json).
- [Artifact schema](artifacts/schemas/artifact.schema.json).
- [Operational conformance obligations](artifacts/conformance-checks.json).
- [Lifecycle/validity acceptance cases](artifacts/lifecycle-validity-cases.json).
- [Lifecycle/validity validation report](artifacts/lifecycle-validity-validation.json).
- [Current and historical source identities](references/supporting-sources.json).
