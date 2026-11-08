---
metadata-version: "1.0.0"
title: "Weekly progress, effort, float, and forecast template"
description: "Define the fields and approval route for weekly progress, effort, float, and forecast."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Weekly progress, effort, float, and forecast template

**Artifact type:** `progress-report`. **Decision route:** GOV-A20.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/progress-report.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `period_start` | string | Record the first reporting date in ISO format. |
| `period_end` | string | Record the final reporting date in ISO format. |
| `selected_sdp` | object | Identify the accepted project-plan revision and selected option. Include repository, identity, revision, path, and byte hash. |
| `completed_phase_records` | array | Reference valid phase-exit records used to calculate progress. Each entry is an exact revision-bound reference. |
| `duration_weighted_progress` | number | Record progress using the Method’s estimated-duration weights. |
| `direct_cost_effort` | number | Record consumed direct cost divided by planned direct cost. |
| `rate_baseline` | object | Reference the exact approved resource-rate version. Include repository, identity, revision, path, and byte hash. |
| `near_critical_float` | array | Record remaining float and issues on near-critical chains. |
| `forecast` | string | State the projected completion date, cost, assumptions, and required decisions. |
| `requested_commitment_changes` | array | Reference proposed commitment changes; a forecast does not approve them. Each entry is an exact revision-bound reference. |

## Review and approval

Accountable owner: `project-manager`. Approval route: `project-manager`.

Required review roles: `solution-architect`.

PM tracks; architect assesses redesign; CEO accepts changed commitments within bounds.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
