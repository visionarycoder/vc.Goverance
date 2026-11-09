---
name: "governance-admin-assistant"
description: "Prepare project governance status briefs, decision-routing summaries, and escalation packets using existing authority and artifact contracts."
---

# Governance administrative assistance

Use for coordination, status preparation, session resume, and escalation-packet preparation. This is a support task, not a new leadership role, decision authority, or sole communication channel. The human owner requested migration to vc.Governance on 2026-11-08.

## Governing inputs

Read the repository [agent instructions](../../../AGENTS.md), [source authority](../../../docs/governance/source-authority.md), [decision matrix](../../../docs/governance/decision-and-approval-matrix.md), [artifact contracts](../../../docs/artifacts/README.md), and applicable [lifecycle gates](../../../docs/process/lifecycle-gates.md) and [approval validity rules](../../../docs/governance/change-approval-validity.md). Use existing formats and routes rather than creating a second policy.

## Status and session resume

Identify the assigned project and scope. Read actual repository state, branches, recent revisions, assignments, plans, review evidence, and unresolved decisions. Distinguish unmerged code from integrated work. If state changes during inspection, refresh affected observations rather than overwriting another writer's work.

Prepare a concise brief of verified completed phases, active assignments, blockers, the planned next action, pending decisions, and supporting evidence/revisions. Effort, commits, and attempted tests do not establish completion. Use the Project Manager's assignment and the project design; do not assign work or alter the critical path on that role's behalf.

## Routing and escalation support

Identify the subject, accountable owner, required decision, revisions, options, and unresolved disagreement. Follow the existing matrix. Distinguish the human owner from the CEO. Do not filter out a failed criterion, blocker, source conflict, or decision needing attention.

Prepare the question, originator, existing route, evidence, considered options, recorded positions, and requested decision. Use existing conflict and source-resolution rules for timing and recipients. Do not invent completed rounds or treat a copied message as authenticated authority.

Draft updates for the responsible owner. Preserve author, critic, and approver functions. A coordination note does not replace their artifact or decision. Send messages, create external board items, or change another repository only when authorized for those actions.

## Bootstrap and restart requests

Inventory surviving requirements, designs, plans, evidence, and assignments before proposing recovery. Preserve artifacts and revision history. Missing files do not establish permission to bypass a gate, choose a technology baseline, activate a role, or resume construction. Prepare the next bounded action for its owner rather than automatically scaffolding an application or recreating approved records as empty files.

## Results and checks

Return the status brief, routing/escalation draft, evidence, unresolved questions, and actual checks. This skill does not continuously monitor a board without a separately authorized execution mechanism. It does not install infrastructure or grant acceptance.

Follow the [Markdown authoring contract](../../../docs/standards/markdown-authoring.md) and run `python tools/validate_markdown.py` after repository changes. Source fidelity, identity, and applicability remain separate from writing checks. Historical provenance is tracked in vc.Agentic's migration inventory; the archived admin-assistant instruction is not governing authority.
