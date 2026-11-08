---
metadata-version: "1.0.0"
title: "Governance artifact contracts"
description: "Define the structure, evidence, and approval semantics of governance artifacts."
document-type: "artifact-contract"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Governance artifact contracts

Version 1.0.0. These contracts implement the owner's role hierarchy and the adopted [Method](../governance/source-authority.md). Their JSON structure is a governance format choice, not a format prescribed by Löwy. Work remains in vc.Governance; orchestration, implementation tooling, and application artifacts retain their separate repository ownership.

The [decision matrix](../governance/decision-and-approval-matrix.md) determines authority. The [artifact schema](schemas/artifact.schema.json) specifies structure. [Templates](../templates/artifacts/README.md) and [fictional examples](examples) cover 23 artifact types. The examples contain placeholders and zero hashes; they must never authorize real work.

## Common envelope

| Field | Meaning |
| --- | --- |
| schema_version | The exact artifact contract version, currently 1.0.0 |
| record_mode | example or operational; examples are ineligible as operational evidence |
| artifact_id and artifact_type | Stable identity and the matrix-defined artifact category |
| revision | Immutable revision identifier within the artifact's owning repository |
| title and scope | Document purpose, suite, project, and component scope when the artifact governs a component |
| creator | Author identity and role claim; authentication is a separate requirement |
| created_at | Timestamp including timezone |
| status | draft, submitted, final, superseded, or withdrawn; final means the record is complete, not that its subject is approved |
| inputs | Exact revisions on which the artifact depends |
| source_basis | Printed book locators, recorded owner decisions, and governance-contract references |
| payload | Type-specific content, constrained by the schema |

Every artifact reference includes repository identity, artifact identity/type, immutable revision, repository-relative path, and SHA-256 of the referenced file's exact bytes. Paths use forward slashes. Hash the stored bytes without normalizing whitespace or line endings. Do not use a moving branch name, a latest alias, or an unbound URL as an approved input. An external build result or code snapshot may be referenced through a separately controlled evidence manifest; a JSON claim alone does not establish that manifest's authenticity.

Repository identities express boundaries, not permission to read or change another repository. Governing documents here use in-repository document links. Operational application records may identify artifacts in their distinct owning repositories; the validator must use separately authorized access to resolve them.

## Content and review

Use the least content sufficient to state the behavior, constraints, and review evidence. A service SRS may remain brief: the book explicitly permits a few paragraphs or pages (p. 389). These contracts do not require exhaustive requirements or all component details before project design. Do not invent content to fill a field; record an unresolved question and hold only dependent work.

For a structured review, name the moderator, artifact owner, scribe, critics, findings, outcome, and follow-up. These are review functions, not new authority roles. The Project Manager schedules the review. Choose competent critics for the subject; record an independent actor rather than allowing an author to relabel itself as a critic. System-level reviews include the core team and affected developers, as required on p. 381. Application Architect and Test Agent critics remain required for component code review.

Only a passed review with resolved blocking findings supplies successful review evidence. A recommendation needs a recorded disposition and rationale; an owner may reject it on reasoned grounds within their authority. A review record does not itself approve its target. A separate authorized decision identifies the exact subject revision and the review evidence.

## Handoffs preserve the lifecycle

After a successful service SRS review, test planning and exploratory/detailed-design work may proceed concurrently. Do not require a passed STP review to begin construction merely because both records exist. Construction requires the reviewed detailed design, related requirements, selected SDP, and a PM assignment. Testing against the STP requires its successful review. Failed reviews return the preceding task for correction; they are not one of the three leadership discussion rounds. See the [service lifecycle](../process/service-lifecycle.md).

An architect instruction record refines an assigned task; it cannot assign a different worker, change the component boundary, alter project commitments, or amend upstream inputs. The PM remains the sole assignment channel. Instructions and their input bounds are versioned so that a worker can identify exactly which instructions apply.

## Approval semantics

1. A decision names its subject revision, requested action, authenticated decider, delegation basis, prerequisite results, and the input revisions it binds.
2. A pending, rejected, or changes-required decision grants no authority. A structurally valid approved decision also grants no authority until its role, scope, evidence, and reference integrity are verified.
3. The responsible owner must approve the requested action. A technical approval does not establish business acceptance, deployment authority, or management acceptance of changed commitments.
4. The Solution Architect obtains CEO approval for its own decisions and baseline changes. The architect remains accountable for system and project design and performs the required technical review of delegated detailed designs. CEO approval does not replace architectural review.
5. Application and Test Architects may revise agent instructions inside their provided bounds. A changed higher-level input goes to its owner. A detailed-design revision retains Solution Architect review before handoff; the within-bounds instruction rule is not a design-review bypass.
6. Implementation and Test Developers cannot approve their own deliverables. An authorized design owner can issue bounded instructions without adding a new CEO gate for Application/Test Architect updates. Preserve the changed artifact's required reviews; an author's role change does not manufacture independent critique.
7. CEO commitment decisions must remain inside recorded human-owner bounds. Outside those bounds, escalate to the human owner. Test Architect approval of a plan cannot authorize a weaker upstream requirement.
8. Every guideline departure needs strong, unusual justification and explicit human-owner approval. Directives and the source's explicit absolute prohibitions cannot be waived. Twenty-operation contracts remain rejected; the guideline heading does not create an exception route.

## Change handling

A change request identifies affected artifact revisions and authority domains, proposed changes, impact assessments, and evidence requiring reassessment. Route business behavior to the Product Owner, system/technology changes to the Solution Architect and CEO approval, detailed design to the Application Architect with required architectural review, test design to the Test Architect, and project consequences to the Solution Architect/PM and management decision.

An accepted change creates new revisions. Preserve old decisions as history. They do not automatically approve new bytes. Reassess affected downstream evidence and obtain the applicable new approvals before using the changed input. Do not reopen unrelated work automatically. Do not continue disputed affected work using an assumed future approval. Appendix A p. 405 requires evaluating changed duration and cost before management accepts changed commitments.

## Structural validation versus operational conformance

The schema uses [JSON Schema 2020-12](https://json-schema.org/draft/2020-12/json-schema-core). Use a validator supporting that dialect and enable date/time format checking. It checks envelope/payload structure, enumerations, required references, construction handoff fields, false phase credit, failed test results presented as passing, unresolved blocking review findings, and selected approval-role conditions.

The schema cannot authenticate identities, fetch artifacts, check their hashes against real files, compare role claims across records, prove a design's business correctness, or enforce permissions. The [conformance catalog](conformance-checks.json) defines those additional obligations for future independent validation. This repository contains contracts and examples, not a production authorization engine. No generated runtime, agent orchestration, or vc.Ifx implementation is added here.

The consumer must reject unknown contract versions, unresolved references, example records used as real evidence, mismatched revisions/hashes, missing authority, and contradictory prerequisite records. Absence of a negative check result is not positive evidence of approval.

## Lifecycle and approval use

Apply the [gate criteria](../process/lifecycle-gates.md) and [approval-validity rules](../governance/change-approval-validity.md) when consuming these records. [Abstract acceptance cases](lifecycle-validity-cases.json) cover parallel branches, missing evidence, changed inputs, reaffirmation, revocation, and explicit freshness. [Validation results](lifecycle-validity-validation.json) separate those checks from runtime enforcement. The existing version 1.0.0 core schema is unchanged.
