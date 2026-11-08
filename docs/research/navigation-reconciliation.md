---
metadata-version: "1.0.0"
title: "Navigation reconciliation"
description: "Record documentation scope changes and navigation corrections."
document-type: "research"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Navigation reconciliation

Reviewed 2026-11-08 after the owner removed selected technology-specific source copies and narrowed the repository focus to governing how code is written.

## Findings and resolution

| Priority | Finding | Resolution |
| --- | --- | --- |
| High | Local links and active source indexes referenced removed sample code, metaprogramming material, and visualization material | Removed broken active links; retained clearly labeled historical review findings and source identities |
| High | Generic build-output ignore rules hid governance artifact contracts and their templates from Git | Added narrow exceptions for docs/artifacts and docs/templates/artifacts; preserved other owner ignore settings |
| Medium | README reading path gave detailed implementation topics prominence over process and authority | Rewrote the overview around governance, ownership, reviews, lifecycle gates, and change control |
| Medium | No explicit documentation table of contents or topic index existed | Added a grouped table of contents and a governance topic index; retained separate secondary coding/reference notes |
| Medium | Lifecycle work in progress needed links into the existing process and authority documents | Linked gate/validity policies, owner decisions, acceptance cases, and validation records without changing core artifact-schema version |

## Scope and remaining decisions

Canonical ownership remains vc.Governance for rules/process, vc.Ifx for reusable implementation mechanisms, and the other repositories for their separately owned work. No application source, orchestration project, release workflow, solution, or package target was modified. There is no application build in this governance repository to run for a navigation change.

The remaining files are indexed as they exist. Retained technology constraints are not silently revoked by removal of a supporting book or sample. Their implementation remains in the distinct owning repository. No deleted source copy was recreated.

Runtime enforcement and adoption decisions remain in [open decisions](../governance/open-decisions.md). See the [table of contents](../toc.md), [topic index](../index.md), and [reference index](../references/README.md). Validation checks local links, index targets, active manifest entries, JSON parsing, policy cases, and the existing artifact examples. It does not validate runtime identities or permissions.
