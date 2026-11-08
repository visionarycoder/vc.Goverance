---
name: "review-agentic-workflow-docs"
description: "Review workflow documentation for Method fidelity, approval boundaries, artifact consistency, and actionable handoffs."
---

# Review agentic workflow documentation

## Review scope

Read the repository [agent instructions](../../../AGENTS.md), [source authority](../../../docs/governance/source-authority.md), [design standard](../../../docs/standards/design-standard.md), and the requested documents. Read the affected [approval routes](../../../docs/governance/decision-and-approval-matrix.md), [gates](../../../docs/process/lifecycle-gates.md), [validity rules](../../../docs/governance/change-approval-validity.md), and [artifact contracts](../../../docs/artifacts/README.md). Follow relevant source locators when a finding depends on the book's meaning.

This skill supports review. Using it does not create an independent actor, confer a review appointment, or grant acceptance authority. Do not relabel an author's self-check as independent critique. Perform a read-only review unless the user also requests corrections.

## Assess meaningful failure paths

- Check front-end baseline and selected SDP readiness against [system and project design](../../../docs/process/system-and-project-design.md). Preserve volatility-based decomposition, validation against core use cases, one accountable system/project architect, feasible alternatives, CEO acceptance within owner bounds, critical-path construction, and incremental integration. Do not demand all detailed designs before project design.
- Trace a normal service change from requirements through handoff, construction, review, integration, and testing. Check explicit actors, inputs, authorized decisions, feedback routes, and binary exits. Preserve parallel test planning and detailed design.
- Check a developer-proposed detailed-design refinement. The developer must reach the Application Architect before proceeding under the change. Upstream changes must reach their owners, and detailed-design handoff retains Solution Architect review.
- Check full construction includes the developer's white-box test client, Test Architect input to detailed-design review, and a current PM assignment. Distinguish Application Architect implementation acceptance, Test Architect test-plan/verification acceptance, and Solution Architect integration acceptance. Integration phase credit needs both integration and successful verification of the same context. Milestone acceptance needs required project tests and Product Owner acceptance; it does not authorize deployment. Apply project-designed criteria to noncoding activities.
- Check a failed review and a leadership dispute separately. Corrections return to the preceding task. A leadership round requires all three positions and a disagreement summary; after three unresolved completed rounds, escalate to the CEO.
- Check scope, schedule, resource, dependency, and cost changes receive Solution Architect/PM assessment and CEO acceptance within owner bounds, with escalation beyond those bounds. Check current fail/blocked/pass semantics and GATE-RESUME before affected work resumes.
- Check stale input revisions, editorial reaffirmation, revocation, and explicit freshness limits. Confirm scoped holds, immutable decision history, and reassessment of affected evidence without automatically reopening unrelated work.
- Check attempted self-approval, example evidence used operationally, missing authority, and a guideline departure. Reject claims that metadata, a schema result, a role name, or an ADR supplies authorization.
- Compare changed Markdown, JSON routes, schemas, templates, examples, navigation, and stated validation reports. Do not assume a dated report validates later revisions.

Do not invent application technology choices or runtime permissions to close a documentation gap. Escalate unresolved source conflicts and reserved decisions to the human owner. Describe implementation gaps as gaps; documentation alone does not enforce isolation.

## Report findings

For each actionable finding, identify the affected file and location, controlling source or owner decision, concrete failure, and required correction or decider. Distinguish a contradiction, missing evidence, unresolved choice, and optional wording improvement. State when no actionable findings remain and identify verification limits.

Run `python tools/validate_markdown.py` from the repository root. If validation code changes, run `python -m unittest discover -s tests -p test_markdown_validation.py`. Automated results supplement semantic review; they do not replace it or issue acceptance.
