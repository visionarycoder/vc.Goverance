---
metadata-version: "1.0.0"
title: "Binary phase completion record template"
description: "Define the fields and approval route for binary phase completion record."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Binary phase completion record template

**Artifact type:** `phase-exit`. **Decision route:** GOV-A19.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/phase-exit.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `activity_id` | string | Identify the project-network activity. |
| `phase` | requirements, detailed-design, test-plan, construction, integration, noncoding | Select the activity phase being assessed. |
| `criterion` | string | State the binary phase-exit condition. |
| `completed` | boolean | Set true only when the required current evidence satisfies the exit condition. |
| `evidence` | array | Reference the records that establish the stated result. Each entry is an exact revision-bound reference. |
| `credited_fraction` | number | Record the completed phase credit. An incomplete phase receives zero. |
| `weight_baseline` | object | Reference the approved phase-weighting basis. Include repository, identity, revision, path, and byte hash. |
| `recorded_by` | object | Identify the Project Manager who records completion. |

## Review and approval

Accountable owner: `project-manager`. Approval route: `project-manager`.

Required review roles: use the prerequisites for the reviewed artifact or requested action.

PM records phase completion from successful reviews/tests, not from time or commits.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
