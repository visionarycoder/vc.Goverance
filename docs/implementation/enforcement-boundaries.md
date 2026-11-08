---
metadata-version: "1.0.0"
title: "Enforcement boundaries"
description: "Define the access and integration controls needed to preserve decision authority."
document-type: "governance-policy"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Enforcement boundaries

## Required outcome

The owner requires agents to be unable to change constraints or approvals owned above their role. Physical separation of framework, application baselines, and implementation is accepted as the starting point. Different permissions and an independently controlled integration gate are also accepted requirements.

These are mechanisms for enforcing the chosen authority model. They do not change The Method, choose an application architecture, or establish a new development lifecycle.

The source requirements for reviews, architecture preservation, and project control come from [Righting Software](<../references/Righting Software.pdf>). The permission mechanism is the owner's implementation choice, not a substituted design method.

## Separate controlled areas

| Area | Contents | Intended write authority |
| --- | --- | --- |
| Governing framework | Adopted source references, organizational rules, and reusable procedures | Human owner for framework amendments |
| Suite direction and business baseline | Vision, business requirements, and strategic decisions | CEO and Product Owner within their authority |
| System and project design baseline | Architecture, technology choices, project options, and selected plan | Solution Architect, with leadership collaboration and management decisions |
| Detailed component designs | Contracts, messages, internal design constraints, and review records | Application Architect within reviewed system bounds |
| Test design baseline | Test requirements, plans, harness requirements, and verification expectations | Test Architect within approved requirements and designs |
| Process-quality work | Preventive procedures, findings, root-cause analysis, and quality metrics | Dedicated QA role reporting to Solution Architect, within higher-level constraints |
| Implementation workspace | Assigned service code and white-box test client | Assigned implementation developer |
| Test implementation workspace | Test harnesses and automation implementing approved test design | Assigned Test Developer |
| Review and integration records | Review decisions, verification results, and integrated revisions | Independent reviewers and integration identity within their delegated scope |

The exact number of repositories or storage locations is not decided. Separate folders under an unrestricted identity do not enforce these boundaries.

## Execution boundary

Implementation workers must not possess credentials or write access that let them edit protected artifacts, alter permissions, impersonate approvers, modify the gate, or merge their own work. Restricting only the visible working directory is insufficient if a worker can reach a sibling repository through another tool or credential.

Application hosting can remain local. Worker isolation is a separate decision. Candidate execution environments must enforce the assigned filesystem, credential, process, and integration permissions across every tool available to the worker. No container, VM, account arrangement, or orchestration product is selected here.

Application Architects and Test Architects likewise cannot alter the bounds set by higher authorities. Leadership identities must not be silently available to developer tools. The human owner's ability to govern the system must not become a credential inherited by every worker.

## Integration behavior to implement

The independent gate must assess the exact submitted implementation revision against the applicable approved requirements and design versions. It must obtain review decisions from authorized identities and reject self-approval or alteration of governing inputs by the submitting worker.

An affected requirement or design change must trigger reassessment of the dependent work and prior evidence. The precise rules for determining which approvals must be renewed need definition; an unrelated change need not reopen the whole project.

The selected SDP and its current approved revisions are controlled inputs too. Protect the activity network, resource assignments, assumptions, phase weights, and cost baselines against worker changes. Scope adjustments must return to the business owner and the architect/Project Manager loop before changed commitments are accepted (pp. 194 and 405).

Protect the independent token-usage ledger and rate versions described in [token based costing](../process/token-costing.md). A worker cannot erase consumption, change a rate baseline, or count resource consumption as earned completion.

Structural checks can detect forbidden dependencies, contract changes, unsupported technology choices, and metric violations. Semantic reviews still determine whether the design encapsulates real volatility, represents the business correctly, and satisfies the approved requirements. A passing check cannot replace the responsible architect's judgment.

## Verification scenarios

Before claiming enforcement, demonstrate that:

1. A developer cannot write to the governing framework, approved system design, detailed contracts, or test requirements through any provided tool.
2. An Application Architect or Test Architect cannot modify an upstream architectural constraint.
3. A developer cannot change or disable the independent validation and integration configuration.
4. A worker cannot create an approval using another role's identity or approve its own work.
5. A revision without the required successful reviews and verification cannot enter the approved integration baseline.
6. A legitimate proposed change can reach the responsible decider, receive the required reviews, and return as an authorized revised input.
7. A developer can complete valid component work within the approved boundary without unnecessary escalation of ordinary implementation choices.

## Current state

These protections have not been deployed or tested. The current authoring session has broad local permissions. Repository instructions and this document communicate the desired boundaries. They do not create them. No changes to host permissions, repository protections, sibling applications, or execution environments have been made.

## Technical baseline controls

Protect the [technical standard](../standards/microsoft-technical-standard.md), adopted EditorConfig files, SDK selection, analyzer versions, build properties, generator policy, and diagnostic suppressions from worker amendment. Evaluate effective settings and approved revisions in independent integration, including nested files and invocation overrides. The [templates](../templates/dotnet/README.md) have field-naming fixture verification. They do not deploy the required permission boundary.

## Proxy-chain controls

Protect the [component proxy policy](../patterns/component-proxies.md), component boundary map, contracts, chain registrations, generator inputs, and analyzer configuration. Verify effective DI resolution and reject direct cross-component bypasses or reflection-based proxy mechanisms. Internal collaborator calls are outside this policy. Runtime composition and invocation tests supplement Roslyn checks. No proxy enforcement project or Dapr deployment has been implemented here.

## Governance record contracts

The [decision matrix](../governance/decision-and-approval-matrix.md) and [artifact contracts](../artifacts/README.md) now define the logical approval routes and revision-bound records. The [conformance catalog](../artifacts/conformance-checks.json) separates schema checks from identity authentication, delegation, repository access, reference/hash verification, independence, and permission enforcement. Runtime implementations must not treat a final or schema-valid record as sufficient authority.
