---
metadata-version: "1.0.0"
title: "System requirements specification template"
description: "Define the fields and approval route for system requirements specification."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# System requirements specification template

**Artifact type:** `system-requirements`. **Decision route:** GOV-A04.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/system-requirements.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `scope_statement` | string | State the behavior and boundaries covered by these requirements. |
| `behaviors` | array | Define required behavior with stable IDs, sources, conditions, and acceptance criteria. |
| `quality_requirements` | array | Define measurable quality requirements and their acceptance criteria. |
| `constraints` | array | State the limits that the assigned worker must preserve. |
| `exclusions` | array | List behavior explicitly outside the artifact scope. |
| `unresolved_questions` | array | List unresolved questions, their responsible owners, and the affected work that must wait. |

## Review and approval

Accountable owner: `solution-architect`. Approval route: `ceo`.

Required review roles: `product-owner`, `project-manager`, `application-architect`, `test-architect`, `implementation-developer`.

Product Owner reviews business fidelity; system reviews include core team and developers. Human owner requires Solution Architect decisions to receive CEO approval; technical accountability remains with the Solution Architect.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
