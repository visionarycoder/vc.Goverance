---
name: "document-governance-artifacts"
description: "Create or revise governance artifact contracts, templates, and fictional examples without issuing operational approvals."
---

# Document governance artifacts

## Read the contract before editing

Read the repository [agent instructions](../../../AGENTS.md), [source authority](../../../docs/governance/source-authority.md), [design standard](../../../docs/standards/design-standard.md), [artifact contract](../../../docs/artifacts/README.md), [core schema](../../../docs/artifacts/schemas/artifact.schema.json), [approval matrix](../../../docs/governance/approval-matrix.json), and affected [templates](../../../docs/templates/artifacts/README.md). Read the [conformance obligations](../../../docs/artifacts/conformance-checks.json) when a field depends on identity, authority, or external evidence.

## Maintain an artifact family

1. Identify the artifact type, accountable owner, permitted authors, critics, and approval route from the existing matrix. Reuse an existing type when it expresses the required evidence.
2. Define each field's type, allowed values, required content, and relationship to other records. Keep template field descriptions consistent with the schema and approval route.
3. Bind references to repository identity, artifact identity and type, immutable revision, repository-relative path, and the SHA-256 of stored bytes. Do not normalize bytes before hashing or substitute a moving latest alias.
4. Distinguish artifact status, review outcome, approval decision, and current applicability. A final record, passed review, or schema-valid role claim does not authorize work.
5. Keep examples explicitly fictional and in example mode. Do not turn sample identities, zero hashes, or empty evidence into operational authorization. Never fabricate a review, decision, delegation, or test result.
6. If changing the contract, assess version compatibility, dependent templates, examples, conformance checks, and acceptance fixtures. Do not silently change a published schema version's meaning. Route substantive contract changes through the existing authority process.

Read the affected [lifecycle gates](../../../docs/process/lifecycle-gates.md) before changing handoff or completion fields. Keep author, review critic, and decider distinct. Use the actual artifact route; generic target-owner and affected-owner fields resolve through the subject and scope, not a new universal approver. Do not add STP approval as a construction prerequisite or let integration acceptance replace successful verification.

Use [change and approval validity](../../../docs/governance/change-approval-validity.md) for affected revisions. Preserve independent critique and all upstream limits. Operational records belong in their distinct owning repositories; this skill does not authorize cross-repository writes.

## Verify and report

Follow the [Markdown authoring contract](../../../docs/standards/markdown-authoring.md) and run `python tools/validate_markdown.py`. For changed JSON artifacts, use JSON Schema 2020-12 validation with format checking. Check affected positive and rejection cases. If the required validator or evidence is unavailable, report the gap rather than declaring conformance.

Report which schemas, templates, and examples changed, the approval basis, actual validation results, and compatibility effects. Structural validation does not prove identity, hash resolution, semantic correctness, or runtime enforcement.
