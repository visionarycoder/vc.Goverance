---
metadata-version: "1.0.0"
title: "Integrated revisions and checks template"
description: "Define the fields and approval route for integrated revisions and checks."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Integrated revisions and checks template

**Artifact type:** `integration-record`. **Decision route:** GOV-A18.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/integration-record.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `input_snapshots` | array | List the exact component revisions used for integration. Each entry is an exact revision-bound reference. |
| `code_review_decisions` | array | Reference the successful technical reviews for the integrated revisions. Each entry is an exact revision-bound reference. |
| `integrated_snapshot` | object | Identify the exact integrated source revision. Include repository, identity, revision, path, and byte hash. |
| `integration_environment` | string | Identify the environment and dependency realization used for integration. |
| `actual_dependency_checks` | array | Reference checks of the required real dependencies. Each entry is an exact revision-bound reference. |
| `test_results` | array | Reference the recorded execution results. Each entry is an exact revision-bound reference. |
| `authorized_identity` | object | Identify the actor authorized to record this integration. |
| `remaining_tests` | array | List required verification that is not yet complete. |

## Review and approval

Accountable owner: `solution-architect`. Approval route: `solution-architect`.

Required review roles: `application-architect`, `test-agent`.

A delegated authorized integration identity records exact revisions; review and STP-based testing still required.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
