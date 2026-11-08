---
metadata-version: "1.0.0"
title: "Owner decisions: approvals and artifact contracts"
description: "Record the human owner’s decisions on artifact authority and approval."
document-type: "owner-decision"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Owner decisions: approvals and artifact contracts

These decisions record the human owner's answers during construction of the [decision matrix](decision-and-approval-matrix.md). They are organizational assignments; the source requirements remain in [Righting Software](https://www.amazon.com/dp/0136524036).

| ID | Owner decision | Consequence |
| --- | --- | --- |
| GOV-OD01 | Test Architect approves a service test plan with Application Architect and independent test reviewer input | TA sign-off; AA and independent Test Agent critique recorded |
| GOV-OD02 | CEO accepts the SDP and changed commitments within human-owner-approved bounds; beyond those bounds escalates to human owner | Management acceptance is separate from architect project-design ownership |
| GOV-OD03 | Human owner approves every guideline departure | No delegated worker or architect exception route; directives remain non-waivable |
| GOV-OD04 | Application/Test Architects can adjust instructions within their supplied guidelines; Solution Architect gets CEO approval | Bounded instruction authority below the system design; SA decisions require CEO approval |
| GOV-OD05 | A round includes all three leadership positions on the same dispute and a summary of the remaining disagreement | Three completed unresolved rounds trigger CEO escalation |
| GOV-OD06 | Test Architect approves system test plans and verification reports; Solution Architect approves technical integration acceptance | Preserve independent review; neither sign-off grants deployment or changed-commitment authority |

Operational interpretation of GOV-OD04: authorship alone never creates independent critique. Preserve the established Solution Architect review of detailed design before handoff and the mandatory Application Architect/Test Agent code-review critics. An instruction change that alters an upstream input must use that input's approval route.

These decisions resolve the questions raised for this matrix. Runtime identities, credentials, evidence storage, and enforcement implementation remain separate open decisions; they are not implied by the named logical roles.
