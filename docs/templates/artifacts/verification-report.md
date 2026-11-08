---
metadata-version: "1.0.0"
title: "Execution against reviewed test plan template"
description: "Define the fields and approval route for execution against reviewed test plan."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Execution against reviewed test plan template

**Artifact type:** `verification-report`. **Decision route:** GOV-A17.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/verification-report.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `test_plan` | object | Identify the exact test-plan revision used for the work. Include repository, identity, revision, path, and byte hash. |
| `test_plan_decision` | object | Identify the decision that accepted the referenced test plan. Include repository, identity, revision, path, and byte hash. |
| `implementation_snapshot` | object | Identify the exact implementation revision tested. Include repository, identity, revision, path, and byte hash. |
| `integration_record` | array | State the integration record that governs this artifact. Each entry is an exact revision-bound reference. |
| `results` | array | Record each required test case, its outcome, and its evidence. |
| `overall_result` | pass, fail, incomplete | Report pass, fail, or incomplete from the required case results. |
| `environment` | string | Identify the environment used for this verification. |
| `defects` | array | List observed defects without changing the approved test expectations. |

## Review and approval

Accountable owner: `test-architect`. Approval route: `test-architect`.

Required review roles: `application-architect`.

Report actual pass/fail evidence. Failure does not authorize changing test expectations.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
