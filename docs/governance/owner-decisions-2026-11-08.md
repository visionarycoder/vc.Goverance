---
metadata-version: "1.0.0"
title: "Owner decisions: approval validity"
description: "Record the human owner’s decisions on reaffirmation, freshness, and revocation."
document-type: "owner-decision"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Owner decisions: approval validity

Recorded 2026-11-08 for the [lifecycle gate criteria](../process/lifecycle-gates.md) and [change/approval policy](change-approval-validity.md).

| ID | Owner decision | Consequence |
| --- | --- | --- |
| GOV-OD07 | Permit documented no-impact reaffirmation for editorial changes | The authorized approver reviews the exact change and records a new revision-bound decision. The old decision remains attached to old bytes. |
| GOV-OD08 | Tie validity to exact revisions and authority; expire on relevant change, withdrawal, revocation, or explicit freshness limits | No blanket clock-based expiry. Evaluate freshness only where the approved artifact, test plan, or policy requires it. |
| GOV-OD09 | Responsible approval authority, or a higher authority explicitly delegated control, may withdraw/revoke; human-owner approvals remain reserved to the human owner | A worker may stop affected work and report the issue, but cannot revoke another role's approval. |

The [earlier approval assignments](owner-decisions-2026-11-07.md) remain in force. These decisions do not delegate guideline departures, authorize self-approval by implementation/test workers, or change Method review responsibilities.
