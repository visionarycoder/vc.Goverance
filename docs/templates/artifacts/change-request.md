---
metadata-version: "1.0.0"
title: "Requirement, design, or commitment change template"
description: "Define the fields and approval route for requirement, design, or commitment change."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Requirement, design, or commitment change template

**Artifact type:** `change-request`. **Decision route:** GOV-A14.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/change-request.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `subjects` | array | List every artifact revision affected by the proposed change. Each entry is an exact revision-bound reference. |
| `reason` | string | State why the change or decision is required. |
| `proposed_change` | string | Describe the proposed behavior or artifact change. |
| `impact_assessments` | array | Record affected domains, revisions, owners, consequences, and required decisions. |
| `dependent_evidence_to_reassess` | array | List the downstream reviews, tests, approvals, or phase exits that need reassessment. Each entry is an exact revision-bound reference. |
| `implementation_disposition` | hold-affected-work, unaffected-work-may-continue | State whether affected work is held while authorized unaffected work continues. |
| `requested_decisions` | array | List the decisions needed before the proposed change can take effect. |

## Review and approval

Accountable owner: `affected-owner`. Approval route: `affected-owner`.

Required review roles: use the prerequisites for the reviewed artifact or requested action.

Route by changed authority domain; approval in one domain cannot approve changes in another.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
