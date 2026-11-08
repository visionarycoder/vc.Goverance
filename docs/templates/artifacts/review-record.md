---
metadata-version: "1.0.0"
title: "Structured review and findings template"
description: "Define the fields and approval route for structured review and findings."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Structured review and findings template

**Artifact type:** `review-record`. **Decision route:** GOV-A12.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/review-record.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `subject` | object | Identify the exact artifact revision governed by this record. Include repository, identity, revision, path, and byte hash. |
| `review_kind` | requirements, architecture, detailed-design, test-plan, code, harness, sdp, process | Select the kind of artifact or decision being reviewed. |
| `moderator` | object | Identify the person or agent who directs the review. |
| `artifact_owner` | object | Identify the accountable owner of the reviewed subject. |
| `scribe` | object | Identify the person or agent who records findings and follow-up. |
| `critics` | array | List the independent reviewers, their relevant expertise, and their positions. |
| `findings` | array | Record each finding, severity, disposition, resolution, and evidence. |
| `outcome` | passed, changes-required, rejected | Select the recorded review or decision result. |
| `follow_up` | array | State the corrective actions and their accountable owners. |
| `follow_up_evidence` | array | Reference evidence that required corrective actions were completed. Each entry is an exact revision-bound reference. |

## Review and approval

Accountable owner: `target-owner`. Approval route: `target-owner`.

Required review roles: use the prerequisites for the reviewed artifact or requested action.

Acceptance of this record does not approve its target. Target decision uses that artifact matrix row.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
