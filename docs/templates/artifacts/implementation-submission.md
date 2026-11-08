---
metadata-version: "1.0.0"
title: "Component code and white-box test submission template"
description: "Define the fields and approval route for component code and white-box test submission."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Component code and white-box test submission template

**Artifact type:** `implementation-submission`. **Decision route:** GOV-A16.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/implementation-submission.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `work_assignment` | object | Reference the current Project Manager assignment. Include repository, identity, revision, path, and byte hash. |
| `source_snapshot` | object | Identify the exact submitted source revision and byte hash. Include repository, identity, revision, path, and byte hash. |
| `requirements` | array | List the exact requirement revisions that govern the work. Each entry is an exact revision-bound reference. |
| `detailed_design` | object | Identify the exact reviewed component-design revision. Include repository, identity, revision, path, and byte hash. |
| `white_box_test_evidence` | array | Reference the developer test client and its recorded results. Each entry is an exact revision-bound reference. |
| `changes_from_design` | array | List every proposed or accepted departure from the supplied detailed design. |
| `proposed_review` | string | Identify the review requested for this submission. |

## Review and approval

Accountable owner: `application-architect`. Approval route: `application-architect`.

Required review roles: `application-architect`, `test-agent`.

Application Architect is delegated leading technical reviewer; submitting developer cannot approve own deliverable.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
