---
metadata-version: "1.0.0"
title: "System design and technology baseline template"
description: "Define the fields and approval route for system design and technology baseline."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# System design and technology baseline template

**Artifact type:** `system-design`. **Decision route:** GOV-A06.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/system-design.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `volatility_rationale` | array | Explain each identified volatility and the boundary that contains it. |
| `components` | array | Identify each component, its Method role, and its contained volatility. |
| `allowed_edges` | array | List each allowed caller, target, interaction type, and contract revision. |
| `core_use_case_validation` | array | Show how the components compose to satisfy every core use case. |
| `technology_bounds` | array | List the approved technology choices and restrictions. |
| `project_design_inputs` | array | Reference the architecture and constraints needed to design the project. Each entry is an exact revision-bound reference. |

## Review and approval

Accountable owner: `solution-architect`. Approval route: `ceo`.

Required review roles: `application-architect`, `product-owner`, `project-manager`, `implementation-developer`, `test-architect`.

Use an independently qualified architectural critic; no division of whole-system ownership. CEO joins changes to suite bounds. Human owner requires Solution Architect decisions to receive CEO approval; technical accountability remains with the Solution Architect.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
