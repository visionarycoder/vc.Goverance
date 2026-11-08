---
metadata-version: "1.0.0"
title: "Project alternatives and selected SDP template"
description: "Define the fields and approval route for project alternatives and selected sdp."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Project alternatives and selected SDP template

**Artifact type:** `software-development-plan`. **Decision route:** GOV-A10.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/software-development-plan.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `system_design` | object | Identify the exact approved system-design revision. Include repository, identity, revision, path, and byte hash. |
| `options` | array | Describe candidate project options, assumptions, networks, cost, and risk. |
| `selected_option_id` | string or null | Identify the management-selected option. Use null before selection. |
| `do_not_proceed_option` | string | Describe the option to cancel or decline the project. |
| `calendar_and_availability` | string | State the work calendar and actual resource availability assumptions. |
| `resource_basis` | string | State the resource estimates and costing assumptions. |
| `rate_baseline` | object | Reference the exact approved resource-rate version. Include repository, identity, revision, path, and byte hash. |
| `quality_activities` | array | List planned review, test, integration, regression, and prevention activities. |
| `phase_weight_basis` | string | State the method used to assign consistent phase weights. |
| `within_owner_bounds` | boolean | State whether the proposed action is within the human-owner delegation. |
| `management_decision` | array | Reference management acceptance of the selected option and commitments. Each entry is an exact revision-bound reference. |

## Review and approval

Accountable owner: `solution-architect`. Approval route: `ceo`.

Required review roles: `project-manager`, `product-owner`, `test-architect`, `qa`.

Architect designs the project; CEO chooses and accepts within human-owner bounds; beyond bounds requires human owner.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
