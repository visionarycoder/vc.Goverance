---
name: "record-governance-decisions"
description: "Write ADRs and decision documentation that distinguish adopted owner decisions from proposals and artifact approvals."
---

# Record governance decisions

## Establish the decision basis

Read the repository [agent instructions](../../../AGENTS.md), [source authority](../../../docs/governance/source-authority.md), [design standard](../../../docs/standards/design-standard.md), [ADR index](../../../docs/adr/README.md), [approval structure ADR](../../../docs/adr/0001-approval-process-structure.md), [decision matrix](../../../docs/governance/decision-and-approval-matrix.md), and relevant owner decisions linked from those documents.

Determine whether the request records an existing authorized decision, proposes a new decision, or requests an operational artifact approval. An ADR explains a decision; it does not replace the revision-bound decision artifact or authenticate the decider.

## Write the record

1. Allocate the next unused four-digit ADR number from the existing directory. Use a descriptive kebab-case filename.
2. Include status, context, decision, consequences, alternatives, and related decisions. Use Standard Technical English and the [Markdown metadata contract](../../../docs/standards/markdown-authoring.md).
3. Identify the source constraint, organizational assignment, or enforcement choice. Cite in-repository source locators and actual owner decisions. Attribute only supported Method guidance to Löwy.
4. Mark a new unresolved decision as proposed. Record accepted status only when an actual authorized decision supports it; cite that basis. A request to document a process does not manufacture approval of a new rule.
5. Preserve authority boundaries, independent critique, exact-revision applicability, and the distinction between technical, business, project, and management acceptance. Do not turn a diagram of relationships into a new universal approval chain.
6. Preserve prior decision history when recording a replacement. Link a successor only when the authorized decision establishes supersession. Describe the actual trade-offs; do not invent a history of deliberation.

When an ADR concerns gates or changed approvals, read the affected [gate criteria](../../../docs/process/lifecycle-gates.md) and [validity policy](../../../docs/governance/change-approval-validity.md). Preserve action-specific applicability, parallel lifecycle branches, and the distinction between technical acceptance, verification, phase credit, and milestone acceptance. No ADR or lifecycle gate grants deployment authority.

If source meaning or decision authority remains unresolved, present the question and relevant evidence to the human owner. A guideline departure requires the human owner's decision. No ADR can waive a directive.

## Publish within the repository

Update the [ADR index](../../../docs/adr/README.md), [table of contents](../../../docs/toc.md), and [topic index](../../../docs/index.md). Update existing specifications only within the authorized scope; an ADR is not a second approval matrix.

Run `python tools/validate_markdown.py` from the repository root. Report the record, status basis, related specifications, validation result, and any pending approval. Do not commit, publish externally, or modify another repository unless the user authorized that action.
