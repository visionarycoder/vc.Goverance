---
metadata-version: "1.0.0"
title: "Service test plan template"
description: "Define the fields and approval route for service test plan."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Service test plan template

**Artifact type:** `service-test-plan`. **Decision route:** GOV-A09.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/service-test-plan.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `requirements` | array | List the exact requirement revisions that govern the work. Each entry is an exact revision-bound reference. |
| `designs` | array | Reference the exact system or detailed designs covered by this plan. Each entry is an exact revision-bound reference. |
| `test_cases` | array | Define each case, requirement, condition, action, expected outcome, and pass criterion. |
| `test_harness` | string | Describe the tools and test clients needed to execute the plan. |
| `regression_scope` | string | Name the behavior and interactions that regression tests must cover. |
| `environment_constraints` | array | State the environment conditions required for valid test results. |
| `unresolved_questions` | array | List unresolved questions, their responsible owners, and the affected work that must wait. |

## Review and approval

Accountable owner: `test-architect`. Approval route: `test-architect`.

Required review roles: `application-architect`, `test-agent`.

Human owner selected Test Architect approval after Application Architect and independent test reviewer input.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
