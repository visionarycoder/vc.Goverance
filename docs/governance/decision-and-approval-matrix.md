---
metadata-version: "1.0.0"
title: "Decision and approval matrix"
description: "Define authorship, review, and approval routes for each artifact type."
document-type: "governance-policy"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Decision and approval matrix

Version 1.0.0. Applies to vc.Governance contracts, not as an instruction to modify another repository. The [machine-readable matrix](approval-matrix.json) and [owner decisions](owner-decisions-2026-11-07.md) distinguish source responsibilities from organizational sign-offs. The source is [Righting Software](https://www.amazon.com/dp/0136524036), especially pp. 148–153, 374–377, 380–382, 388–390, 405, and Appendix C.

## Accountability and approval

An accountable owner retains responsibility for content and integrity. An author prepares it. Critics review it. An approver decides a specific action within delegated scope. These functions are not interchangeable. Review participants are named by identity in the record; the matrix lists logical roles. A title or a field in JSON does not authenticate an identity.

The Solution Architect owns both system and project design. Under the owner’s GOV-OD04 decision, its own decisions and baseline changes require CEO approval. This does not give the CEO authorship of architecture or remove the required architect review. Application Architects own detailed design within system bounds; Test Architects own test design within requirements/design bounds. The Project Manager alone assigns work and tracks execution.

## Artifact routes

| ID / artifact | Accountable owner | Permitted authors | Required review roles | Approval route |
| --- | --- | --- | --- | --- |
| GOV-A01 [Framework amendment](../templates/artifacts/governance-baseline.md) | Human owner | QA, Solution Architect | Solution Architect, Product Owner, Project Manager | Human owner |
| GOV-A02 [Suite vision and strategic bounds](../templates/artifacts/suite-vision.md) | CEO / Visionary | CEO / Visionary | Product Owner, Solution Architect, Project Manager | CEO / Visionary |
| GOV-A03 [Business requirements and acceptance criteria](../templates/artifacts/business-requirements.md) | Product Owner | Product Owner | Solution Architect, Project Manager | Product Owner |
| GOV-A04 [System requirements specification](../templates/artifacts/system-requirements.md) | Solution Architect | Solution Architect | Product Owner, Project Manager, Application Architect, Test Architect, Implementation Developer | CEO / Visionary |
| GOV-A05 [Service requirements specification](../templates/artifacts/service-requirements.md) | Solution Architect | Application Architect, Solution Architect | Solution Architect, Test Architect | Solution Architect |
| GOV-A06 [System design and technology baseline](../templates/artifacts/system-design.md) | Solution Architect | Solution Architect | Application Architect, Product Owner, Project Manager, Implementation Developer, Test Architect | CEO / Visionary |
| GOV-A07 [Component detailed design and contracts](../templates/artifacts/detailed-design.md) | Application Architect | Application Architect | Solution Architect, Test Architect | Solution Architect |
| GOV-A08 [System test plan and harness design](../templates/artifacts/system-test-plan.md) | Test Architect | Test Architect, Test Developer | Solution Architect, Product Owner, Project Manager, Application Architect, Implementation Developer, Test Agent | Test Architect |
| GOV-A09 [Service test plan](../templates/artifacts/service-test-plan.md) | Test Architect | Test Architect, Test Developer | Application Architect, Test Agent | Test Architect |
| GOV-A10 [Project alternatives and selected SDP](../templates/artifacts/software-development-plan.md) | Solution Architect | Solution Architect | Project Manager, Product Owner, Test Architect, QA | CEO / Visionary |
| GOV-A11 [Bounded work assignment and handoff](../templates/artifacts/work-assignment.md) | Project Manager | Project Manager | Target-specific prerequisites | Project Manager |
| GOV-A12 [Structured review and findings](../templates/artifacts/review-record.md) | target-owner | QA, Application Architect, Test Architect, Solution Architect | Target-specific prerequisites | target-owner |
| GOV-A13 [Revision-bound approval or rejection](../templates/artifacts/decision-record.md) | target-owner | Human owner, CEO / Visionary, Solution Architect, Product Owner, Project Manager, Application Architect, Test Architect | Target-specific prerequisites | target-owner |
| GOV-A14 [Requirement, design, or commitment change](../templates/artifacts/change-request.md) | affected-owner | Human owner, CEO / Visionary, Solution Architect, Product Owner, Project Manager, Application Architect, Test Architect, QA, Implementation Developer, Test Developer, Test Agent | Target-specific prerequisites | affected-owner |
| GOV-A15 [Guideline departure request](../templates/artifacts/guideline-departure.md) | Human owner | Human owner, CEO / Visionary, Solution Architect, Product Owner, Project Manager, Application Architect, Test Architect, QA, Implementation Developer, Test Developer, Test Agent | Solution Architect, QA | Human owner |
| GOV-A16 [Component code and white-box test submission](../templates/artifacts/implementation-submission.md) | Application Architect | Implementation Developer | Application Architect, Test Agent | Application Architect |
| GOV-A17 [Execution against reviewed test plan](../templates/artifacts/verification-report.md) | Test Architect | Test Agent | Application Architect | Test Architect |
| GOV-A18 [Integrated revisions and checks](../templates/artifacts/integration-record.md) | Solution Architect | Implementation Developer, Test Developer, Test Agent | Application Architect, Test Agent | Solution Architect |
| GOV-A19 [Binary phase completion record](../templates/artifacts/phase-exit.md) | Project Manager | Project Manager | Target-specific prerequisites | Project Manager |
| GOV-A20 [Weekly progress, effort, float, and forecast](../templates/artifacts/progress-report.md) | Project Manager | Project Manager | Solution Architect | Project Manager |
| GOV-A21 [Leadership dispute and escalation](../templates/artifacts/conflict-record.md) | CEO / Visionary | Project Manager | Solution Architect, Product Owner, Project Manager | CEO / Visionary |
| GOV-A22 [Prevention and root-cause finding](../templates/artifacts/qa-finding.md) | QA | QA | Solution Architect | QA |
| GOV-A23 [Bounded architect instructions to agents](../templates/artifacts/agent-instructions.md) | issuing-architect | Application Architect, Test Architect, Solution Architect | Target-specific prerequisites | issuing-architect within upstream bounds; ceo for solution-architect decisions |

`target-owner` means the accountable/approval route of the reviewed subject; it is not a new universal role. `affected-owner` routes each impacted domain separately. `issuing-architect` means the architect issuing instructions inside its bounds; Solution Architect instructions need CEO approval. An identity acting as a different role does not gain authority beyond its recorded delegation.

For service requirements, the architect’s SRS review remains required. When the Solution Architect authors its own SRS or other technical decision rather than reviewing a delegated deliverable, apply the CEO-approval rule. For system design and requirements, keep core-team and affected-developer reviews; an independent architectural critic must be competent to review the design.

Detailed design requires Solution Architect review before handoff (pp. 376–377). Component construction requires Application Architect and independent Test Agent critics, followed by leading-architect technical acceptance. Test-plan approval uses the Test Architect after the specified independent input. Integration acceptance remains a separate Solution Architect decision and cannot replace post-integration testing.

## Bounded instruction changes

An Application or Test Architect may issue or revise instructions to workers within the supplied bounds. Record the upstream revisions, the intended task, and the impact assessment. Such an instruction cannot change business requirements, component boundaries, technology choices, another owner’s detailed design, test expectations above its authority, or project commitments. The PM’s assignment remains in force.

A change to a higher-level input is a change request to its owner, not a local instruction update. A guideline departure always goes to the human owner with strong, unusual justification; no directive waiver exists. If scope, schedule, cost, dependencies, or resources change, the Solution Architect and PM assess project consequences before the CEO accepts changed commitments within owner bounds.

## Structured reviews

The review record names moderator, owner, scribe, and critics with findings and follow-up (p. 381). These are review functions, not additional leadership offices. The PM schedules and coordinates the review. The accountable owner selects competent technical participants; QA checks process quality and completeness. A contributing author cannot supply its own independent critic position.

A passed review needs resolved blocking findings. A separate authorized decision accepts the subject/action. Implementation Developers and Test Developers never accept their own deliverables. Apply independent critique wherever the subject's review obligations require it; an author cannot manufacture that critique by changing its role claim. Bounded Application/Test Architect instruction updates do not acquire a new CEO-approval gate merely because they are recorded. They retain any review obligations of the actual artifact being changed. The matrix does not require creating a second accountable system architect.

## Leadership conflict rounds

A round is complete only after the Solution Architect, Product Owner, and Project Manager record their positions on the same dispute and the remaining disagreement is summarized. The PM records the round. An incomplete discussion, silence, elapsed time, tool retry, or failed artifact review is not a completed round.

Use at most three completed rounds. If disagreement remains after round three, mark the conflict escalated and route it to the CEO. Earlier escalation is permitted when participants conclude a decision cannot be reached. The CEO decides within delegated bounds; framework/source conflicts or out-of-bounds commitments reach the human owner. Pending escalation does not authorize disputed affected work. Unaffected authorized work may continue.

Reviewing source ambiguity is not a three-round vote on whether to obey the book. Preserve both source locators and escalate unresolved source conflicts directly to the human owner.

## Evidence and validity

Apply the [artifact contracts](../artifacts/README.md). Decisions bind exact revisions and referenced inputs. Identity, delegation, required critics, findings disposition, scope, and evidence must be verified independently. A final document or schema-valid approval record is not by itself authorization.

The [conformance catalog](../artifacts/conformance-checks.json) specifies checks for the future enforcing system. No repository permission, credential boundary, or approval service is deployed by this matrix.

## Gate and approval applicability

Use [lifecycle gate criteria](../process/lifecycle-gates.md) to determine which actions the reviewed evidence permits, and [change/approval validity](change-approval-validity.md) to determine whether that evidence still applies. [Owner decisions on 2026-11-08](owner-decisions-2026-11-08.md) allow documented editorial reaffirmation, reject blanket time expiry, and define withdrawal/revocation authority. Existing artifact ownership and sign-off routes remain in force.
