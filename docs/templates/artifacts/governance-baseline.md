---
metadata-version: "1.0.0"
title: "Framework amendment template"
description: "Define the fields and approval route for framework amendment."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Framework amendment template

**Artifact type:** `governance-baseline`. **Decision route:** GOV-A01.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/governance-baseline.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `method_source` | object | Reference the governing book edition and its exact file identity. Include repository, identity, revision, path, and byte hash. |
| `rule_sets` | array | Reference the adopted rule-set revisions. Each entry is an exact revision-bound reference. |
| `delegations` | array | Reference the recorded role delegations and authority limits. Each entry is an exact revision-bound reference. |
| `repository_boundaries` | array | Name each repository and the artifacts it owns. |
| `amendment_reason` | string | Explain why the human owner must change the governing framework. |

## Review and approval

Accountable owner: `human-owner`. Approval route: `human-owner`.

Required review roles: `solution-architect`, `product-owner`, `project-manager`.

Human owner controls framework amendments. Method directives remain non-waivable.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
