---
metadata-version: "1.0.0"
title: "Suite vision and strategic bounds template"
description: "Define the fields and approval route for suite vision and strategic bounds."
document-type: "template"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Suite vision and strategic bounds template

**Artifact type:** `suite-vision`. **Decision route:** GOV-A02.

Follow the [common artifact contract](../../artifacts/README.md) and [schema](../../artifacts/schemas/artifact.schema.json). Use the [fictional draft JSON](../../artifacts/examples/suite-vision.json) as a structure example. It does not authorize work. Replace all example values and references before issuing an operational record.

## Required payload fields

| Field | Type or allowed values | Required content |
| --- | --- | --- | --- |
| `vision` | string | State the intended business direction of the application suite. |
| `objectives` | array | List the business outcomes needed to realize the vision. |
| `mission` | string | Explain how the objectives lead to the system design. |
| `delegated_bounds` | array | State the limits delegated by the human owner. |
| `business_glossary` | object | Reference the agreed meanings of business terms. Include repository, identity, revision, path, and byte hash. |

## Review and approval

Accountable owner: `ceo`. Approval route: `ceo`.

Required review roles: `product-owner`, `solution-architect`, `project-manager`.

CEO decides suite direction within human-owner delegation.

Use the [decision matrix](../../governance/decision-and-approval-matrix.md) to resolve authority and independent review. An empty list in an example does not waive required operational evidence.
