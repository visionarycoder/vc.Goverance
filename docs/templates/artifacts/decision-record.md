---
metadata-version: "1.0.0"
title: "Revision-bound approval or rejection template"
description: "Define the fields and approval route for revision-bound approval or rejection."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Revision-bound approval or rejection template

**Artifact type:** `decision-record`. **Decision route:** GOV-A13.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/decision-record.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `subject` | object | Identify the exact artifact revision governed by this record. Include repository, identity, revision, path, and byte hash. |
| `action` | accept-artifact, select-project-option, assign-work, approve-phase-exit, approve-guideline-departure, authorize-change, accept-integration, accept-business, approve-instructions | Select the specific action this decision addresses. |
| `decider` | object | Identify the decision issuer and its authorized role. |
| `authority_basis` | array | Reference the recorded delegation and policy that authorize the decision. Each entry is an exact revision-bound reference. |
| `outcome` | pending, approved, rejected, changes-required | Select the recorded review or decision result. |
| `reason` | string | State why the change or decision is required. |
| `decided_at` | string or null | Record the decision timestamp with its timezone. A pending decision can use null. |
| `review_records` | array | List the exact independent-review records used as evidence. Each entry is an exact revision-bound reference. |
| `prerequisite_checks` | array | Record each prerequisite, its result, and its supporting evidence. |
| `within_owner_bounds` | boolean | State whether the proposed action is within the human-owner delegation. |
| `bound_inputs` | array | List the exact input revisions to which the decision applies. Each entry is an exact revision-bound reference. |

## Review and approval

Accountable owner: `target-owner`. Approval route: `target-owner`.

Required review roles: use the prerequisites for the reviewed artifact or requested action.

Issuer must be the authorized decider for the target and requested action. No universal approval role.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
