---
metadata-version: "1.0.0"
title: "Prevention and root-cause finding template"
description: "Define the fields and approval route for prevention and root-cause finding."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Prevention and root-cause finding template

**Artifact type:** `qa-finding`. **Decision route:** GOV-A22.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/qa-finding.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `observed_problem` | string | Describe the observed defect or process failure. |
| `evidence` | array | Reference the records that establish the stated result. Each entry is an exact revision-bound reference. |
| `root_cause_analysis` | string | Explain the evidence-based cause of the observed process failure. |
| `preventive_action` | string | State the proposed action to prevent recurrence. |
| `affected_owner_roles` | array | List the roles responsible for the affected artifacts or process. |
| `requires_framework_amendment` | boolean | State whether the proposal changes the governing framework. |
| `follow_up` | string | State the corrective actions and their accountable owners. |

## Review and approval

Accountable owner: `qa`. Approval route: `qa`.

Required review roles: `solution-architect`.

QA reports to SA. QA finding does not amend governing process or another owner’s design.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
