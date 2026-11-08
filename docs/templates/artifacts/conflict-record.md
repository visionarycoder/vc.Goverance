---
metadata-version: "1.0.0"
title: "Leadership dispute and escalation template"
description: "Define the fields and approval route for leadership dispute and escalation."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Leadership dispute and escalation template

**Artifact type:** `conflict-record`. **Decision route:** GOV-A21.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/conflict-record.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `dispute` | string | State the decision on which the participants disagree. |
| `subject` | object | Identify the exact artifact revision governed by this record. Include repository, identity, revision, path, and byte hash. |
| `applicable_constraints` | array | Reference the source and baseline constraints that limit the available options. Each entry is an exact revision-bound reference. |
| `options` | array | Describe candidate project options, assumptions, networks, cost, and risk. |
| `rounds` | array | Record the three leadership positions and remaining disagreement for each completed round. |
| `resolution_status` | open, resolved, escalated | State whether the dispute is open, resolved, or escalated. |
| `escalation_owner` | ceo, human-owner | Name the CEO or human owner responsible for the unresolved decision. |
| `decision_refs` | array | Reference the decisions that resolve the recorded issue. Each entry is an exact revision-bound reference. |

## Review and approval

Accountable owner: `ceo`. Approval route: `ceo`.

Required review roles: `solution-architect`, `product-owner`, `project-manager`.

Three completed discussion rounds maximum before CEO escalation; source conflict or framework amendment goes to human owner.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
