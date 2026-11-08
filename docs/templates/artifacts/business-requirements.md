---
metadata-version: "1.0.0"
title: "Business requirements and acceptance criteria template"
description: "Define the fields and approval route for business requirements and acceptance criteria."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Business requirements and acceptance criteria template

**Artifact type:** `business-requirements`. **Decision route:** GOV-A03.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/business-requirements.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

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

Accountable owner: `product-owner`. Approval route: `product-owner`.

Required review roles: `solution-architect`, `project-manager`.

Product Owner resolves customer behavior and priorities, not architecture.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
