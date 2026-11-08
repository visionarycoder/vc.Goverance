---
metadata-version: "1.0.0"
title: "Change and approval validity"
description: "Define when changes require approval reassessment, reaffirmation, or revocation."
document-type: "governance-policy"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Change and approval validity

Version 1.0.0, reviewed 2026-11-08. This policy governs how work remains authorized when requirements, designs, code, plans, or evidence change. It follows [Righting Software](https://www.amazon.com/dp/0136524036), especially pp. 194, 376–377, 388–391, and 405, and the owner's [approval assignments](decision-and-approval-matrix.md) and [validity decisions](owner-decisions-2026-11-08.md). The [23 STE rules](change-approval-validity.json) are the machine-readable policy.

## Evaluate a decision in context

An approval is usable only for its stated action, exact subject and bound-input revisions, scope, adopted governance baseline, and relevant environment. Check authentic authority, required independent reviews, prerequisite evidence, and applicable revocation, withdrawal, freshness, and change effects. A final artifact, passed field, or valid JSON structure is not sufficient authority.

| Derived state | Meaning for the requested action |
| --- | --- |
| usable | Required current-context evidence and authority are verified |
| not-approved | Decision is pending, rejected, changes-required, or does not authorize this action |
| stale-for-context | Subject, inputs, environment, or assumptions changed and applicability is not yet re-established |
| revoked | An authorized effective revocation or withdrawal covers this scope |
| expired | An explicit applicable freshness or validity limit has been exceeded |
| unresolved | Required reference, identity, impact, or authority evidence cannot be verified |

These states are derived for the requested use. Preserve the issued decision and earlier reports as immutable history. A new revision does not retroactively erase the old review, and an old approval does not approve new bytes. A superseded revision may remain usable in an explicitly retained, authorized baseline unless withdrawn, revoked, expired, or otherwise made inapplicable. Do not silently select a latest alias.

## Assess the change before adopting it

1. Identify the old and proposed artifact revisions and exact hashes. Describe the requested behavior and authority domains, not just the files edited.
2. Trace affected inputs, outputs, dependencies, tests, integration evidence, assignments, phase exits, and commitments. Include transitive effects. Do not reopen unrelated work without cause.
3. Route each domain to its owner. Hold affected actions whose approval is uncertain. Unaffected authorized work can continue.
4. Obtain the required design/requirement decisions, independent reviews, management acceptance, or guideline-departure decision.
5. Perform the regeneration, build, review, integration, and test work required by the recorded impact assessment. Bind new evidence to the actual revised context.
6. Have the PM recheck the affected assignment and its dependencies before resuming work. A local design decision does not approve changed schedule or cost commitments.

The Solution Architect and PM assess project consequences together (p. 194). Changed scope requires evaluating duration and cost and presenting the new commitments for management acceptance (p. 405). The CEO accepts within human-owner bounds; changes beyond those bounds reach the human owner.

## Change-to-evidence routing

| Changed subject | Assessment and approval route | Evidence to reassess |
| --- | --- | --- |
| Business behavior or acceptance criteria | Product Owner; SA/PM assess technical and project effects | Requirements, core use-case composition, designs, tests, commitments |
| System requirements, component boundaries, interactions, or technology bounds | Solution Architect retains design ownership; CEO approval for its decisions | Detailed designs/contracts, allowed edges, generated outputs, test plans, project design |
| Detailed design or service contract | Application Architect; required Solution Architect review before handoff | Callers, proxies, implementation, white-box client, STP, integration and regression evidence |
| Test plan, harness expectations, or test environment | Test Architect; escalate changed upstream requirements/design to their owner | Coverage, test implementation, prior runs and dependent phase exits |
| Code, generator output, package, registration, or runtime dependency | Applicable architect and existing implementation-review route | Build, code review, integration, runtime tests and affected interactions |
| Bounded architect instruction | Issuing Application/Test Architect inside supplied bounds; SA decisions obtain CEO approval | Assignment applicability, instructions and the actual artifacts being changed |
| Schedule, resources, scope, dependencies, rates, or cost commitments | SA/PM assess and redesign; CEO/human owner accepts changed commitments | Selected SDP, assignments, rate baseline, forecasts and reporting context |
| Framework rules, authority delegation, or adopted governance baseline | Human owner controls amendments; apply recorded adoption/effectivity scope | Required decisions, gate eligibility, bounded exceptions and affected permissions |

A change in one domain does not confer approval in another. Application/Test Architects cannot revise higher-level guidelines by issuing new instructions. No ordinary acceptance waives a directive or an explicit absolute source prohibition. Every allowable guideline departure requires human-owner approval.

## Editorial no-impact reaffirmation

The owner permits a bounded no-impact review; it is not automatic approval transfer.

1. Record a change request with the exact old/new revisions and diff, affected scope, and proposed editorial classification.
2. Have the authorized approver assess meaning and downstream effects. The author or worker cannot self-certify no impact in place of that assessment.
3. Record a review of the new revision and the no-impact rationale. Identify exactly which earlier findings, tests, or other evidence remain applicable and why.
4. Issue a new decision through the artifact's existing approval route, bound to the revised subject and current inputs. Use the appropriate existing decision action; a special bypass role is not introduced.
5. For dependent unchanged artifacts whose bound inputs changed, record their applicability assessment and any necessary new decision. Preserve all prior decisions as history.

Changed requirements, operation names, signatures, defaults, ordering, allowed dependencies, test expectations, rates, project assumptions, generated behavior, or authority are not presumed editorial. If impact cannot be established, use the normal affected review and test path. A documented no-impact result can avoid repeating unrelated tests; it cannot fabricate a test run against different bytes.

Reaffirmation does not remove CEO approval for SA-authored decisions or human-owner control of guideline departures. Required independent critique remains applicable to the actual artifact change. A bounded AA/TA instruction update does not acquire a new CEO gate merely because it is versioned.

## Withdrawal, revocation, and freshness

The authority responsible for an approval may withdraw or revoke it. A higher authority may do so only where explicitly delegated control over that approval. Human-owner approvals remain reserved to the human owner. A worker may stop its affected work and report a problem; it cannot revoke another role's approval. The PM coordinates holds without rewriting technical acceptance.

Use immutable change, review, and decision records to identify the affected approval/artifact revisions, authorized actor and delegation, effective time, reason, scope, and recovery requirements. Bind the authorized decision to the described change. An unapproved request to revoke is not a revocation. Re-evaluate the relevant gates when the decision takes effect; preserve the historical issuance and earlier gate results.

There is no universal time-to-live. Enforce an explicit freshness or expiry limit only when the approved policy, artifact, or test plan requires it. Freshness requirements must be recorded before claiming evidence satisfies them. Do not invent an expiry after observing an inconvenient result, or ignore an expired requirement because an older test passed.

Verify authority at issuance and continuing applicability under the adopted policy. Routine replacement of an agent or completion of an assignment is not, by itself, an implicit retroactive revocation. An explicit authority expiry or revocation is evaluated for its stated scope and effect. Staffing changes do not erase legitimate historical critique.

## Gate and progress consequences

A known failed criterion fails the action; missing or unverified approval evidence blocks it. Stale evidence requires reassessment before the affected action resumes. A past gate result is not a permanent permission token. Apply the [gate criteria](../process/lifecycle-gates.md) for the requested context each time authority matters.

PM reporting preserves history and consumed cost. The current applicable completion state must exclude unsupported phase credit and reflect required rework. Do not rewrite old reports or erase spent tokens. Use consistent phase weights and the actual selected project baseline. Failed reviews and test retries remain correction loops, not leadership discussion rounds.

## Record and implementation scope

Use existing [artifact contracts](../artifacts/README.md): change-request for impact/scope, review-record for no-impact or substantive findings, decision-record for authorized acceptance/change, and assignment/verification/phase records for the resulting work and evidence. This policy does not change the existing core schema or add a universal approval role.

The [acceptance fixtures](../artifacts/lifecycle-validity-cases.json) and [validation report](../artifacts/lifecycle-validity-validation.json) document policy checks, not a deployed identity or permission system. Runtime implementations must resolve evidence and authority independently; a fixture or a role claim cannot authorize real work.
