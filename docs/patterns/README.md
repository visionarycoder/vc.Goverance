---
metadata-version: "1.0.0"
title: "Implementation pattern catalog"
description: "Index pattern requirements and distinguish required policies from design candidates."
document-type: "index"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Implementation pattern catalog

This catalog connects supporting ideas to implementation specifications under [the governing standard](../standards/design-standard.md). It uses Standard Technical English. PAT-001 now carries a mandatory owner-selected component-boundary policy. Other entries remain candidates for selection by the responsible design owners. Inclusion does not make a pattern mandatory or select an application stack. [Structured records](catalog.json) retain conditions, constraints, implementation choices, verification, and unresolved questions.

## Selection and handoff

The Solution Architect determines applicability, system boundaries, and technology. The Application Architect selects the detailed realization within those bounds and obtains Solution Architect review before handoff. The Test Architect defines verification. The Project Manager includes design, implementation, review, and integration work in the project design. The Product Owner resolves business semantics. Workers receive the selected pattern version, related requirements, reviewed detailed design, permitted variation, and test obligations.

Pattern refinements follow the existing [service lifecycle](../process/service-lifecycle.md). A pattern is not a new approval path or permission to change a contract. Escalate a detailed-design adjustment to the Application Architect, a system-design adjustment to the Solution Architect, and unresolved source conflicts to the human owner. Preserve the established three-round leadership escalation to the CEO.

The JSON selection fields describe a proposed evidence format. They do not establish technical enforcement. Protect selected patterns, templates, and acceptance evidence through the [enforcement boundaries](../implementation/enforcement-boundaries.md). Workers cannot change their own constraints to obtain a passing result.

## PAT-001: Contract-mediated component access

**Mandatory owner policy:** every call between components uses a DI-capable proxy. Generate a typed local proxy where no service separation exists. Reflection-based proxies are prohibited. Dapr invocation is accepted. Internal collaborator calls are excluded. See the [complete requirement and verification plan](component-proxies.md).

**Status:** mandatory owner-selected boundary policy; application realization remains a design decision.

**Use when:** A call crosses an approved component boundary, including a boundary inside one process.

**Sources:**

- [Righting Software](https://www.amazon.com/dp/0136524036): Chapter 3; Appendix B; Appendix C; governing.

**Preserve:**

- Expose the approved contract. Keep implementation details behind the boundary.
- Apply all permitted and prohibited interactions in C-SD-4, C-SD-5, and C-SD-6.
- Use cohesive business operations. Do not expose property-like service operations.

**Detailed-design decisions:**

- Select an approved service invocation proxy or generate a typed local proxy. Do not replace the mandatory proxy with direct calls or reflection-based dispatch.
- Specify messages, failures, and lifecycle handling in the detailed design.

**Verification:**

- Review actual dependency edges, including indirect calls.
- Test contract behavior and failure paths through the boundary.
- Verify that callers do not require the concrete service implementation.

## PAT-002: Service contract inheritance with proxy chaining

**Status:** candidate; not selected for an application.

**Use when:** A reviewed contract has a justified inherited capability, and the selected technology supports the pattern.

**Sources:**

- SimpleProxy.cs (source copy removed from this repository): SimpleCalculatorClient declaration and Add; Lowy/IDesign sample.

- ScientificProxy.cs (source copy removed from this repository): IScientificCalculator and ScientificCalculatorClient; Lowy/IDesign sample.

- [Righting Software](https://www.amazon.com/dp/0136524036): Chapter 3; Appendix B; Appendix C; governing.

**Preserve:**

- Keep inheritance aligned with cohesive public capabilities. Do not grow a contract merely to reuse implementation code.
- Preserve the source sample attribution and license when using its code.
- Do not mistake proxy class inheritance for permission to change component dependency rules.

**Detailed-design decisions:**

- The sample chains the scientific proxy through the simple proxy; the simple proxy uses a channel typed to the scientific contract.
- Evaluate this channel coupling explicitly. Do not infer that the base proxy is independent of derived contracts.
- Treat the sample as historical evidence, not a production-ready runtime selection.

**Verification:**

- Test inherited and added operations through their intended public interfaces.
- Verify endpoint and contract compatibility, channel cleanup, and fault behavior.
- Evaluate contract metrics over the effective exposed operation set.

**Questions before selection:**

- Does the base-proxy dependence on the most-derived channel fit the intended contract evolution?

## PAT-003: Generated infrastructure around approved components

**Status:** candidate; not selected for an application.

**Use when:** Repeated infrastructure behavior has a stable, reviewed definition.

**Sources:**

- Metaprogramming in NET.pdf (source copy removed from this repository): Sections 7.1.1–7.1.2, printed pp. 200–202; PDF pp. 225–227; supporting technique.

- [Righting Software](https://www.amazon.com/dp/0136524036): Chapter 3; Appendix B; Appendix C; governing.

**Preserve:**

- Keep business decisions in the approved business components.
- Do not use generated infrastructure to add forbidden dependencies or silently change contracts.
- Keep generation inputs and templates outside implementation-worker amendment authority.

**Detailed-design decisions:**

- Compare generation, composition, decorators, interception, and rewriting under the approved baseline. No mechanism is selected by this catalog.
- Record generator version, approved input revision, and generated output ownership.
- Make regeneration reproducible and generated behavior inspectable. These controls are proposed framework mechanisms, not quotations from Lowy.

**Verification:**

- Regenerate from the same inputs and compare outputs.
- Test observable behavior, exception paths, and required infrastructure presence.
- Verify that disabling or replacing a generator cannot silently bypass integration checks.

## PAT-004: Explicit message-type registration

**Status:** candidate; not selected for an application.

**Use when:** An approved boundary transmits polymorphic message types.

**Sources:**

- Metaprogramming in NET.pdf (source copy removed from this repository): Section 2.3.2 and 2.4.1, printed pp. 50–55; PDF pp. 75–80; supporting technique.

- [Righting Software](https://www.amazon.com/dp/0136524036): Chapter 3; Appendix B; Appendix C; governing.

**Preserve:**

- Define the permitted message family in the contract design.
- Do not let discovery expand the public message surface without design approval.
- Treat runtime discovery as implementation of an approved type policy, not authority to invent that policy.

**Detailed-design decisions:**

- Compare explicit registration, generated registration, and constrained reflection.
- If discovery is selected, specify approved assemblies, permitted types, and failure behavior. These restrictions are framework proposals.

**Verification:**

- Round-trip each approved derived message through the real serializer.
- Reject unapproved or incompatible message types.
- Test missing registrations and deployment version combinations.

**Questions before selection:**

- The explanatory text on printed p. 55 shows an apparent duplicate IsAssignableFrom expression while describing a different comparison. Resolve it before copying that explanation into implementation rules.

## PAT-005: Failure containment at approved boundaries

**Status:** candidate; not selected for an application.

**Use when:** Availability requirements identify a risk of dependency failure propagation.

**Sources:**

- [Anti-fragile ICT Systems](https://www.amazon.com/dp/3319300687): Chapter 4, printed pp. 35–42; PDF pp. 50–57; supporting principle.

- [Righting Software](https://www.amazon.com/dp/0136524036): Chapter 3; Appendix B; Appendix C; governing.

**Preserve:**

- Retain volatility-based component decomposition.
- Specify business-correct failure behavior. Do not report fabricated success.
- Contain failures through existing permitted boundaries. Do not create architecture bypasses.

**Detailed-design decisions:**

- Evaluate weak links, bounded dependency behavior, fallback, and redundancy against explicit failure scenarios.
- The Solution Architect selects mechanisms and resource costs; developers cannot introduce new platform dependencies independently.

**Verification:**

- Inject the approved dependency failures in the designated test environment.
- Measure propagation, recovery, and contractual responses against explicit acceptance criteria.
- Test interactions of individually healthy components as well as isolated component failures.

## PAT-006: Controlled failure learning

**Status:** candidate; not selected for an application.

**Use when:** The system has approved failure-containment and recovery behavior.

**Sources:**

- [Anti-fragile ICT Systems](https://www.amazon.com/dp/3319300687): Section 4.5, printed p. 39; PDF p. 54; supporting principle.

- [Righting Software](https://www.amazon.com/dp/0136524036): Chapter 14, printed pp. 378–383; governing.

**Preserve:**

- Use findings to propose reviewed corrections. Do not let a learning loop rewrite architecture or policy.
- Keep experiments within approved environments and impact limits.
- Route fixes through the existing lifecycle and design owners.

**Detailed-design decisions:**

- The Test Architect specifies fault scenarios, containment preconditions, stopping conditions, and recovery checks.
- QA records recurring causes and proposes process improvements within the assigned authority.

**Verification:**

- Record the injected fault, observed impact, recovery, and resulting corrective work.
- Demonstrate that the same failure is detected after the correction.
- Do not label a system anti-fragile merely because it survives one experiment.

## PAT-007: Reusable fractal business nodes

**Status:** candidate; not selected for an application.

**Use when:** Business analysis establishes a recurring participant structure and canonical interaction.

**Sources:**

- [Fractal Architecture, Juval Löwy](https://www.idesign.net/Resources): Printed/PDF pp. 4–8; Figures 1 and 2 on p. 7; Lowy supplementary guidance.

- [Righting Software](https://www.amazon.com/dp/0136524036): Chapter 3; Appendix B; Appendix C; governing.

**Preserve:**

- Design the participant structure and canonical interaction before multiplying nodes.
- Keep regular Method constraints inside each node.
- Keep participation opt-in and specify behavior when a node operates alone or disconnects.
- Do not infer unrestricted component-level upward or sideways calls from business-level participant interactions.

**Detailed-design decisions:**

- Evaluate a common node implementation with differences expressed through approved resources and constrained behavior configuration.
- Model level-specific communication and legacy interoperability nodes.
- Treat configuration and simulation as designed capabilities; constrain who can amend behavior and which contracts it may invoke.

**Verification:**

- Simulate alternative structures and representative interactions before selecting a topology.
- Test identical node logic in different levels and participant configurations.
- Test disconnection, reconnection, and partial structures.
- Verify that configurable behavior cannot invoke unapproved dependencies.

**Questions before selection:**

- Is the target business sufficiently self-similar to justify a fractal?
- Which failure risks require diversity, and can they be addressed without conflicting with the common-node design?

## PAT-008: Traceable behavioral requirement records

**Status:** candidate; not selected for an application.

**Use when:** Business, system, or service requirements are recorded for design and test handoff.

**Sources:**

- [Writing Software Requirements Specifications.htm](https://techwhirl.com/writing-software-requirements-specifications/): Sections on requirement identifiers, source linking, traceability matrix, and language quality; supporting article: Donn Le Vie, Jr..

- [Righting Software](https://www.amazon.com/dp/0136524036): Chapter 4; Appendix A, printed pp. 388–390; C-SD-1; governing.

**Preserve:**

- Record behavior and its business source. Do not disguise a proposed design as a requirement.
- Distinguish system-level Software Requirements Specification from service-level SRS in the lifecycle.
- Preserve guideline modality in the framework. Do not replace every SHOULD with SHALL because a requirements-writing article discourages weak requirement language.

**Detailed-design decisions:**

- Use stable IDs, requirement scope, source, conditions, expected behavior, acceptance criteria, owner, and revision.
- Trace reviewed requirements to detailed designs, test plans, work items, and verification evidence.
- Maintain traceability as design and construction progress. Do not require all implementation links before design begins.

**Verification:**

- Check identifier uniqueness and valid revision links.
- Review business meaning and testability with the Product Owner and responsible architect.
- Check that service requirements and test plans refer to the same reviewed scope.

## PAT-009: Usable and consistent internal framework APIs

**Status:** candidate; not selected for an application.

**Use when:** An approved reusable library exposes an API to component developers.

**Sources:**

- [Framework Design Guidelines](https://www.amazon.com/dp/0321545613): Second edition, Chapter 1 pp. 1–3 and Chapter 2 pp. 12–14; PDF pp. 47–49 and 58–60; supporting library-design guidance.

- [Righting Software](https://www.amazon.com/dp/0136524036): Chapter 3; Appendix B; Appendix C; governing.

**Preserve:**

- Apply library API guidance within the approved component architecture.
- Do not convert local object properties into property-like service operations.
- Do not substitute scenario-shaped components for volatility-based system decomposition.

**Detailed-design decisions:**

- Have the Application Architect review representative caller code before finalizing the API.
- Favor consistent APIs that make approved usage straightforward and expose only reviewed extension points.
- Evaluate historical guidance against the selected runtime before choosing specific APIs or idioms.

**Verification:**

- Exercise normal and erroneous use through public library APIs.
- Review whether typical caller code follows the intended boundary naturally.
- Verify that extension points cannot override higher-level architecture or framework policy.

## Attribution and review limits

The proxy-chaining sample was reviewed as historical IDesign evidence. Its source and accompanying license are no longer distributed in this repository. The review summary does not constitute a production implementation.

The supporting books were reviewed selectively for these patterns. This catalog does not claim whole-book review of those books. See the [supporting-source review record](../research/supporting-pattern-review.md).

## PAT-010: Purpose-driven UI data visualization

Use the [UI visualization pattern](ui-visualization.md) when an approved UI requirement needs readers to understand or explore data. The [structured record](catalog.json) contains applicability, invariants, implementation choices, verification, and ownership. The owner approved this reference for UI usage; the application-specific realization still requires the existing design reviews.

## Current technical implementation baseline

Apply the [Microsoft technical standard](../standards/microsoft-technical-standard.md) to every selected technical pattern. Modern implementations use current supported Microsoft guidance and unprefixed names under the approved SDK baseline. Historical source samples remain unchanged; their APIs, syntax, naming, and configuration are not automatic production choices. The supporting books do not override this current technical policy.

## PAT-011: Attribute-driven method I/O tracing

[Specification](method-io-tracing.md) and [structured requirements](../standards/tracing-rules.json). The owner requires automatic input/output debugging statements on attributed methods, including public, internal, and private methods. This is distinct from service-proxy logging. Transparent instrumentation of existing bodies requires a build transformation; an ordinary generator alone is insufficient. The implementation mechanism remains a detailed-design decision.

## Implementation location

The owner assigned reusable implementation mechanisms and their detailed tooling design to vc.Ifx. Keep required behavior, Method constraints, and adoption status here. See [repository ownership and handoff](../implementation/repository-ownership.md). The location decision is resolved; remaining mechanism decisions belong in the vc.Ifx design effort.
