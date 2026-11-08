---
metadata-version: "1.0.0"
title: "Bounded work assignment and handoff template"
description: "Define the fields and approval route for bounded work assignment and handoff."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Bounded work assignment and handoff template

**Artifact type:** `work-assignment`. **Decision route:** GOV-A11.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/work-assignment.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `activity_id` | string | Identify the project-network activity. |
| `activity_kind` | requirements, design, exploration, construction, test-design, test-implementation, integration, testing, noncoding | Select the activity category that controls the handoff requirements. |
| `assigned_worker` | object | Identify the assigned worker and its role. |
| `assigned_by` | object | Identify the Project Manager who issued the assignment. |
| `component_id` | string or null | Identify the component governed by the artifact. Use null only when the contract permits a non-component scope. |
| `requirements` | array | List the exact requirement revisions that govern the work. Each entry is an exact revision-bound reference. |
| `system_design` | array | Identify the exact approved system-design revision. Each entry is an exact revision-bound reference. |
| `detailed_design` | array | Identify the exact reviewed component-design revision. Each entry is an exact revision-bound reference. |
| `design_review_decisions` | array | List the decisions that accepted the referenced design revisions. Each entry is an exact revision-bound reference. |
| `selected_sdp` | array | Identify the accepted project-plan revision and selected option. Each entry is an exact revision-bound reference. |
| `test_plan` | array | Identify the exact test-plan revision used for the work. Each entry is an exact revision-bound reference. |
| `test_plan_decisions` | array | List the decisions that accepted the referenced test-plan revisions. Each entry is an exact revision-bound reference. |
| `constraints` | array | State the limits that the assigned worker must preserve. |
| `permitted_outputs` | array | List the files, artifacts, or results the assignment permits. |
| `completion_criteria` | array | State the evidence required to complete the assignment. |
| `authorized_phase` | string | Name the lifecycle phase this assignment permits. |

## Review and approval

Accountable owner: `project-manager`. Approval route: `project-manager`.

Required review roles: use the prerequisites for the reviewed artifact or requested action.

Only PM assigns work; design review evidence is a prerequisite, not replaced by PM acceptance.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
