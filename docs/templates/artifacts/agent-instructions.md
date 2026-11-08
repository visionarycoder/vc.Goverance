---
metadata-version: "1.0.0"
title: "Bounded architect instructions to agents template"
description: "Define the fields and approval route for bounded architect instructions to agents."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Bounded architect instructions to agents template

**Artifact type:** `agent-instructions`. **Decision route:** GOV-A23.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/agent-instructions.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `issuing_architect` | object | Identify the architect who issues the bounded instructions. |
| `work_assignment` | object | Reference the current Project Manager assignment. Include repository, identity, revision, path, and byte hash. |
| `upstream_constraints` | array | Reference the exact approved inputs that limit these instructions. Each entry is an exact revision-bound reference. |
| `instructions` | array | State the required worker actions within the supplied bounds. |
| `within_provided_bounds` | boolean | State whether the instructions preserve the supplied upstream constraints. |
| `impact_assessments` | array | Record affected domains, revisions, owners, consequences, and required decisions. |
| `required_decision_refs` | array | Reference the decisions required by the actual changes. Each entry is an exact revision-bound reference. |

## Review and approval

Accountable owner: `issuing-architect`. Approval route: `issuing-architect within upstream bounds; ceo for solution-architect decisions`.

Required review roles: use the prerequisites for the reviewed artifact or requested action.

Owner permits Application/Test Architects to adjust instructions within supplied bounds. SA obtains CEO approval. A changed upstream artifact retains its own required approval.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
