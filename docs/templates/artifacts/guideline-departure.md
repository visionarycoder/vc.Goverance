---
metadata-version: "1.0.0"
title: "Guideline departure request template"
description: "Define the fields and approval route for guideline departure request."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Guideline departure request template

**Artifact type:** `guideline-departure`. **Decision route:** GOV-A15.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/guideline-departure.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `rule_id` | C-SD-1.a, C-SD-1.b, C-SD-1.c, C-SD-1.d, C-SD-1.e, C-SD-2.a, C-SD-2.b, C-SD-2.c, C-SD-2.d, C-SD-2.e, C-SD-3.a, C-SD-3.b, C-SD-3.c, C-SD-3.d, C-SD-3.e, C-SD-3.f, C-SD-4.a, C-SD-4.b, C-SD-4.c, C-SD-4.c.i, C-SD-4.c.ii, C-SD-4.c.iii, C-SD-4.c.iv, C-SD-4.d, C-SD-5.a, C-SD-5.b, C-SD-5.c, C-SD-5.d, C-SD-6.a, C-SD-6.b, C-SD-6.c, C-SD-6.d, C-SD-6.e, C-SD-6.f, C-SD-6.g, C-SD-6.h, C-SD-6.i, C-PD-1.a, C-PD-1.b, C-PD-1.c, C-PD-1.d, C-PD-1.e, C-PD-1.f, C-PD-1.g, C-PD-2.a, C-PD-2.b, C-PD-2.c, C-PD-2.d, C-PD-2.e, C-PD-2.f, C-PD-2.g, C-PD-2.h, C-PD-3.a, C-PD-3.b, C-PD-4.a, C-PD-4.b, C-PD-4.c, C-PD-4.d, C-PD-4.e, C-PD-4.f, C-PD-4.g, C-PD-5.a, C-PD-5.b, C-PD-5.c, C-PD-5.d, C-PD-5.e, C-PD-5.f, C-PD-5.g, C-PD-5.h, C-PD-5.i, C-PD-5.j, C-PD-6.a, C-PD-6.b, C-PD-6.c, C-PD-6.d, C-PD-6.e, C-PD-6.f, C-PD-6.g, C-PD-7.a, C-PD-7.b, C-PD-7.c, C-PD-7.c.i, C-PD-7.c.ii, C-PD-7.d, C-PD-7.e, C-PD-7.f, C-PD-7.g, C-PD-7.h, C-PD-7.i, C-PT-1, C-PT-2, C-PT-3, C-PT-4, C-PT-5, C-PT-6, C-SC-1, C-SC-2, C-SC-2.a, C-SC-2.b, C-SC-2.c, C-SC-3, C-SC-4, C-SC-5, C-SC-6 | Identify the guideline for which a departure is requested. |
| `classification` | guideline | Preserve the source classification. This record cannot waive a directive. |
| `source_context` | string | State the source locator and conditions that govern the guideline. |
| `strong_unusual_justification` | string | Explain the strong and unusual reason for the proposed departure. |
| `conforming_alternatives_assessed` | array | Describe the conforming alternatives and why they do not meet the required constraints. |
| `consequences` | array | State the expected design, test, schedule, cost, and risk effects. |
| `bounded_scope` | string | Define the exact work and revisions covered by the requested departure. |
| `affected_inputs` | array | Reference the upstream revisions affected by the request. Each entry is an exact revision-bound reference. |
| `architect_assessment` | string | Record the responsible architect’s assessment of the departure. |
| `qa_review` | object | Reference the independent process-quality review. Include repository, identity, revision, path, and byte hash. |
| `human_owner_decision` | array | Reference the human-owner decision. An empty list does not authorize a departure. Each entry is an exact revision-bound reference. |

## Review and approval

Accountable owner: `human-owner`. Approval route: `human-owner`.

Required review roles: `solution-architect`, `qa`.

Human owner approves every strongly justified guideline departure. Directive and explicit absolute prohibitions cannot be waived.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
