---
metadata-version: "1.0.0"
title: "ADR 0001: Approval process structure"
description: "Record the adopted approval hierarchy, review sequence, and escalation rules."
document-type: "governance-policy"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# ADR 0001: Approval process structure

## Status

Accepted as a record of existing human-owner decisions. Recorded on 2026-11-08. This ADR does not issue an approval for any application artifact, change the governance baseline, or grant new authority.

## Context

Implementation agents need clear limits on what they may decide, change, and accept. An agent must not weaken requirements, designs, tests, or approval rules to simplify its implementation.

The human owner adopted Juval Löwy's The Method and Appendix C of [Righting Software](https://www.amazon.com/dp/0136524036). The book governs design and engineering responsibilities. The human owner's decisions assign logical roles and sign-offs. These organizational assignments are not claims that Löwy prescribed these role names or record formats.

The adopted structure separates accountable ownership, authorship, independent critique, approval, and work assignment. The [source authority](../governance/source-authority.md) and [design standard](../standards/design-standard.md) remain governing references. Relevant book discussions include pp. 148–153, 194, 374–377, 380–382, 388–390, 405, and Appendix C, pp. 425–430.

## Decision

### Authority and ownership

| Role | Decision responsibility | Approval boundary |
| --- | --- | --- |
| Human owner | Governing framework, delegation, and commitments beyond delegated bounds | Approves framework amendments and every allowable guideline departure; human-owner approvals remain reserved to the human owner |
| CEO / Visionary | Suite direction and management acceptance | Approves Solution Architect decisions and accepts the SDP and changed commitments within human-owner-approved bounds |
| Solution Architect | System requirements, system design, technology baseline, and project design | Obtains CEO approval for its own decisions; reviews delegated detailed designs and accepts technical integration |
| Product Owner | Business requirements and acceptance criteria | Approves business artifacts within suite bounds; cannot change architecture or project commitments through business acceptance |
| Project Manager | Work assignment, process execution, progress, and phase records | Is the sole assignment and project-status channel; cannot replace technical approval or accept changed management commitments |
| Application Architect | Detailed component design, contracts, and bounded implementation instructions | Obtains required Solution Architect review before design handoff; accepts implementation after required critique |
| Test Architect | System and service test plans, harness design, and verification acceptance | Approves test plans and verification reports after required review; cannot weaken upstream requirements or designs |
| QA | Defect prevention and process quality | Reports to the Solution Architect; identifies process defects without gaining authority to change upstream bounds |
| Implementation Developer, Test Developer, and Test Agent | Assigned construction, test development, verification, and critique | Work within approved inputs; implementation and test developers cannot accept their own deliverables |

The Solution Architect, Product Owner, and Project Manager form the leadership triumvirate. Collaboration does not divide whole-system architectural accountability among multiple owners. Role names in records do not authenticate an actor or create delegated authority.

Use the [decision and approval matrix](../governance/decision-and-approval-matrix.md) and its [machine-readable routes](../governance/approval-matrix.json) for all 23 artifact types. This ADR summarizes those routes; it does not create a second matrix.

### Review and approval sequence

1. The accountable owner identifies the subject, required inputs, applicable constraints, and authorized approval route.
2. The permitted author prepares a revision-bound artifact. The artifact identifies exact input revisions and supporting evidence.
3. The Project Manager coordinates the required review. The record identifies the owner, moderator, scribe, critics, findings, and follow-up.
4. Competent critics perform the required review. An author cannot supply its own independent critic position by assuming another role name.
5. The author resolves blocking findings. Failed reviews return the artifact to its preceding task. Corrections that affect another owner's input require that owner's change route.
6. The authorized approver records a separate decision for the exact subject revision, action, scope, inputs, and evidence. Successful critique alone does not authorize the action.
7. Before assigning or resuming the affected work, the Project Manager checks the assignment and prerequisites. The requested action must satisfy its current lifecycle gate and approval-validity rules.

Use the [artifact contracts](../artifacts/README.md) for record content, the [lifecycle gates](../process/lifecycle-gates.md) for permitted actions, and [change and approval validity](../governance/change-approval-validity.md) for continuing applicability.

### Lifecycle review points and feedback

Service requirements review opens two concurrent paths: test planning, and exploratory construction followed by detailed design. A reviewed service test plan is required for testing against that plan. It is not an added prerequisite for detailed design or full construction.

The Application Architect supplies the detailed design and contracts. The Solution Architect reviews them before handoff. The Project Manager's assignment includes the detailed design and related feature requirements. Exploratory construction can expose a refinement, but the developer must consult the Application Architect before proceeding under the changed design. Any change beyond that architect's bounds goes to the responsible upstream owner.

Code review includes the Application Architect and an independent Test Agent as critics. The Application Architect accepts the implementation. The Solution Architect separately accepts technical integration. Integration precedes testing against the reviewed service test plan. The Test Architect approves verification reports after required review. Integration acceptance does not replace testing or authorize deployment.

The [service lifecycle](../process/service-lifecycle.md) preserves the source workflow and correction loops. Phase completion is binary and depends on successful exit evidence. Effort spent or code committed does not complete a phase.

### Changes and approval validity

A proposed change identifies affected artifacts, exact revisions, transitive effects, and responsible domains. Each affected owner decides within its authority. The Solution Architect and Project Manager assess schedule, resource, dependency, and cost effects. The CEO accepts changed commitments within human-owner-approved bounds; changes beyond those bounds go to the human owner.

Application and Test Architects may revise worker instructions within their upstream bounds. Those revisions retain the review obligations of the actual artifact being changed. They cannot change higher-level requirements, designs, test expectations, or commitments. Solution Architect decisions require CEO approval.

An approval applies only to its recorded action, revisions, scope, inputs, authority, and relevant environment. Relevant changes require applicability reassessment. There is no blanket time expiry. Apply explicit freshness limits when the approved policy, artifact, or test plan requires them.

An editorial change may use documented no-impact reaffirmation by the authorized approver. The approver issues a new revision-bound decision. The earlier approval remains attached to the earlier bytes.

The authority responsible for an approval may withdraw or revoke it. A higher authority may do so only under explicit delegated control. Human-owner approvals remain reserved to the human owner. A worker may stop affected work and report a problem, but cannot revoke another role's approval. Preserve historical records and unaffected authorized work.

### Disputes and departures

1. Route a role-level disagreement to the responsible decision owner. Route a cross-domain leadership dispute to the triumvirate.
2. Count a discussion round only when the Solution Architect, Product Owner, and Project Manager each record a position on the same dispute and the remaining disagreement is summarized. The Project Manager records the round.
3. Escalate unresolved disagreement after three completed rounds to the CEO. Earlier escalation is permitted. Failed reviews, silence, retries, and elapsed time do not count as rounds.
4. The CEO decides within delegated bounds. Escalate out-of-bounds commitments and framework authority questions to the human owner. Escalate unresolved source conflicts directly to the human owner.
5. Hold disputed affected work while its authority is unresolved. Unaffected authorized work may continue.

Every allowable guideline departure requires strong, unusual justification and human-owner approval. Directives and explicit absolute source prohibitions cannot be waived. A leadership vote, code review, or schedule pressure does not create an exception.

## Consequences

- Workers receive bounded assignments with reviewed designs and explicit acceptance evidence.
- Design ownership remains stable while independent critics can identify defects and required refinements.
- Business acceptance, technical acceptance, project execution, and management commitments remain separate decisions.
- Review, evidence tracing, and change assessment add work. Project design must include that work instead of omitting it to meet a token or schedule budget.
- CEO approval of Solution Architect decisions can constrain throughput. The existing delegation must be followed until the human owner changes it.
- Documentation defines obligations but does not provide tamper resistance. Authenticated identities, protected inputs, independently controlled integration, and runtime approval checks require separate implementation. See [enforcement boundaries](../implementation/enforcement-boundaries.md).

## Alternatives

These alternatives explain the decision's trade-offs; they are not additional proposals approved by the owner.

| Alternative | Reason not selected |
| --- | --- |
| Let workers approve their own implementation or tests | Removes the independent acceptance boundary and allows the worker to change its assessment criteria |
| Require CEO approval for every bounded Application or Test Architect instruction update | Exceeds the adopted delegation and adds a gate the owner did not require |
| Let each component architect change system boundaries | Fragments system ownership and bypasses the Solution Architect's whole-system responsibility |
| Treat a passed review or valid JSON record as authorization | Does not establish authenticated authority, exact revision applicability, or approval of the requested action |
| Put all lifecycle activities in one serial approval chain | Removes the source workflow's parallel test-plan and detailed-design paths |
| Transfer an old approval automatically to an edited document | Breaks revision binding and omits the required impact assessment or reaffirmation |

## Related decisions and specifications

No earlier ADR exists in this repository. This record consolidates these existing decisions without superseding them:

- [GOV-OD01–GOV-OD06](../governance/owner-decisions-2026-11-07.md): approval owners, bounded instruction authority, and escalation rounds.
- [GOV-OD07–GOV-OD09](../governance/owner-decisions-2026-11-08.md): editorial reaffirmation, validity, and revocation.
- [Roles and decision rights](../governance/roles-and-decisions.md): hierarchy and responsibility limits.
- [Decision and approval matrix](../governance/decision-and-approval-matrix.md): complete artifact routes.
- [Change and approval validity](../governance/change-approval-validity.md): current-context approval rules.

If a future proposal changes these decisions, route it through the governing amendment and approval process before recording it as accepted. An unresolved source or authority question must reach the human owner; editing this ADR cannot resolve it by itself.
