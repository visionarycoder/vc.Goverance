---
metadata-version: "1.0.0"
title: "Design standard"
description: "Map every Appendix C directive and guideline to its source."
document-type: "standard"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Design standard

**Governing source:** [Righting Software](<../references/Righting Software.pdf>), Appendix C, printed pp. 425-430. Adopted by the human owner on 2026-11-07. Every numbered checklist item is mapped below in paraphrase. Read the source for exact wording and the chapters for context. See [source authority](../governance/source-authority.md).

Identifiers preserve the appendix's hierarchy: `C-D` for directives; `C-SD` for system design; `C-PD` for project design; `C-PT` for tracking; and `C-SC` for service contracts. An identifier ending in a letter or Roman numeral corresponds to that source subitem. Category headings do not create additional rules.

## Prime directive and directives

Source: p. 426. These are directives, not waivable guidelines.

| ID | Meaning to preserve |
| --- | --- |
| C-PRIME | Do not derive the architecture by mapping the requirements' functionalities into components. Analyze requirements to discover volatility and required behavior; do not ignore them. See also pp. 84-87. |
| C-D-1 | Reject functional decomposition. |
| C-D-2 | Use volatility as the basis of decomposition. |
| C-D-3 | Produce a design whose components compose to deliver the required behaviors. |
| C-D-4 | Deliver features through integration rather than feature-shaped implementation units. |
| C-D-5 | Iterate the design and construct the system incrementally. |
| C-D-6 | Engineer the project that will construct the system. |
| C-D-7 | Enable informed decisions through feasible alternatives trading schedule, cost, and risk. |
| C-D-8 | Construct according to the project's critical path. |
| C-D-9 | Maintain schedule commitments throughout execution. |

The prime directive does not prohibit satisfying requirements. Chapter 4 distinguishes the basis of decomposition from validation that the resulting composition supports the core use cases.

## System design guidelines

Source: pp. 426-427. All following items are guidelines under the definition on p. 425. A worker's preference or convenience is not authorization to depart from one.

### Requirements

| ID | Meaning to preserve |
| --- | --- |
| C-SD-1.a | Record the behavior required of the system rather than a list of functionalities. |
| C-SD-1.b | Express that behavior as use cases. |
| C-SD-1.c | Use activity diagrams for use cases with nested conditions. |
| C-SD-1.d | Remove proposed solutions disguised as requirements. |
| C-SD-1.e | Validate the architecture against every core use case. |

### Cardinality

| ID | Meaning to preserve |
| --- | --- |
| C-SD-2.a | In a system without subsystems, avoid exceeding five Managers. |
| C-SD-2.b | Keep the number of subsystems to a handful. |
| C-SD-2.c | Keep each subsystem to no more than three Managers. |
| C-SD-2.d | Seek the observed golden-ratio relationship between Engines and Managers. |
| C-SD-2.e | Permit a ResourceAccess component to serve multiple Resources where needed. |

The ratio is a design diagnostic, not a requirement to manufacture otherwise unnecessary Engines. Chapter 3, pp. 63 and 67-68 permits Managers with no Engines when activity volatility does not justify one.

The four questions and naming conventions on pp. 65-67 initiate and evaluate decomposition. They do not supersede volatility. Functional decomposition may help discover requirements (p. 22); the prohibition concerns using it as the architectural decomposition.

### Attributes

| ID | Meaning to preserve |
| --- | --- |
| C-SD-3.a | Expect less volatility toward the bottom of the architecture. |
| C-SD-3.b | Expect greater reuse toward the bottom. |
| C-SD-3.c | Do not design encapsulation around a change to the business's fundamental nature. |
| C-SD-3.d | Keep Managers almost expendable, rather than expensive monoliths or empty pass-throughs. |
| C-SD-3.e | Seek architectural symmetry. |
| C-SD-3.f | Keep public communication channels out of internal system interactions. |

### Layers

| ID | Meaning to preserve |
| --- | --- |
| C-SD-4.a | Avoid an open architecture. |
| C-SD-4.b | Avoid a semi-open or semi-closed architecture. |
| C-SD-4.c | Prefer a closed architecture, with the following constraints. |
| C-SD-4.c.i | Do not make upward calls. |
| C-SD-4.c.ii | Do not make sideways calls, with the specified queued Manager exception. |
| C-SD-4.c.iii | Do not skip downward across multiple layers. |
| C-SD-4.c.iv | Meet needs that would open the architecture through queued calls or asynchronous event publication. |
| C-SD-4.d | Extend through subsystems. |

Interpret layers together with the explicit permitted interactions below and Chapter 3, pp. 77-79. Managers and Engines occupy the business logic layer; a Manager-to-Engine call is permitted. The Utilities bar is an explicit cross-layer facility, not a label for bypassing the architecture.

### Permitted interactions

| ID | Meaning to preserve |
| --- | --- |
| C-SD-5.a | Every component may use Utilities. |
| C-SD-5.b | Managers and Engines may invoke ResourceAccess services. |
| C-SD-5.c | Managers may invoke Engines. |
| C-SD-5.d | A Manager may queue a call to another Manager. |

The source numbers this group as 5.a through 5.d; it contains four items.

### Interactions to avoid

| ID | Meaning to preserve |
| --- | --- |
| C-SD-6.a | A Client does not invoke several Managers to execute one use case. |
| C-SD-6.b | A Manager does not queue calls to several Managers in one use case. |
| C-SD-6.c | An Engine does not receive queued calls. |
| C-SD-6.d | ResourceAccess does not receive queued calls. |
| C-SD-6.e | Clients do not publish events. |
| C-SD-6.f | Engines do not publish events. |
| C-SD-6.g | ResourceAccess does not publish events. |
| C-SD-6.h | Resources do not publish events. |
| C-SD-6.i | Engines, ResourceAccess services, and Resources do not subscribe to events. |

Chapter 3, pp. 80-81 additionally makes the Client-to-Engine, Engine-to-Engine, and ResourceAccess-to-ResourceAccess prohibitions explicit. Their absence as separate Appendix C rows does not make those interactions permissible.

A Client request posted to a message bus is not necessarily a published business event. Chapter 5 uses Client requests through a bus while preserving the event-publication rules. Identify the message's semantics and the caller and recipient roles. Do not classify every message as an event. The bus does not authorize otherwise forbidden communication, including Client-to-Client interaction (p. 118).

## Project design guidelines

Source: pp. 427-429. The Solution Architect is accountable for project design with Project Manager input; the Project Manager executes and tracks the selected design. See Chapter 7, pp. 149-150 and 194.

### General

| ID | Meaning to preserve |
| --- | --- |
| C-PD-1.a | Avoid overengineering project design for perfect precision; make it sufficient for informed, feasible commitments. See p. 365. |
| C-PD-1.b | Do not design the project without an architecture that contains volatility. |
| C-PD-1.c | State and verify the assumptions underlying the plan. |
| C-PD-1.d | Follow the prescribed sequence for designing the project. |
| C-PD-1.e | Develop multiple options, including at least normal, compressed, and subcritical solutions. |
| C-PD-1.f | Communicate with management using Optionality. |
| C-PD-1.g | Complete the Software Development Plan review before the main work begins. |

Chapter 14, pp. 366-367 defines Optionality as succinctly presenting a selected set of viable options for objective management evaluation. It favors three options and warns against overwhelming decision makers with too many.

### Staffing

| ID | Meaning to preserve |
| --- | --- |
| C-PD-2.a | Avoid multiple accountable system architects. |
| C-PD-2.b | Establish the core team at the outset. |
| C-PD-2.c | Seek the minimum staffing that permits uninterrupted critical-path progress. |
| C-PD-2.d | Allocate resources according to float. |
| C-PD-2.e | Preserve the appropriate staffing distribution over the project. |
| C-PD-2.f | Plan earned value as a shallow S curve. |
| C-PD-2.g | Maintain one-to-one component and developer assignments. |
| C-PD-2.h | Preserve continuity between a resource's successive tasks where possible. |

For C-PD-2.g, pp. 153-155 explain that a developer works on one service at a time and a service has one developer at a time. Sequential assignments are permitted; pair programming is explicitly distinguished from parallel or serial subdivision. Independent reviewers and delegated detailed designers do not become additional concurrent implementation owners.

### Integration

| ID | Meaning to preserve |
| --- | --- |
| C-PD-3.a | Avoid large, mass integration events. |
| C-PD-3.b | Do not defer integration to the project's end. |

### Estimation

| ID | Meaning to preserve |
| --- | --- |
| C-PD-4.a | Avoid overestimating. |
| C-PD-4.b | Avoid underestimating. |
| C-PD-4.c | Prefer accuracy over numerical precision. |
| C-PD-4.d | Estimate activities in five-day quanta. |
| C-PD-4.e | Use a whole-project estimate to check, or help initiate, the detailed project design. |
| C-PD-4.f | Actively reduce estimation uncertainty. |
| C-PD-4.g | Use the correct estimation dialogue when eliciting estimates. |

The owner authorized [token based costing](../process/token-costing.md) for agent resource consumption. This does not replace the five-day planning quantum, establish a tokens-to-days conversion, or change weekly tracking. The worker calendar and availability still need an explicit planning assumption.

### Project network

| ID | Meaning to preserve |
| --- | --- |
| C-PD-5.a | Include resource dependencies as actual dependencies. |
| C-PD-5.b | Ensure each activity belongs to a chain that begins and ends on a critical path. |
| C-PD-5.c | Assign a resource to every activity. |
| C-PD-5.d | Avoid node network diagrams. |
| C-PD-5.e | Prefer arrow network diagrams. |
| C-PD-5.f | Avoid oversized god activities. |
| C-PD-5.g | Represent large projects through a network of networks. |
| C-PD-5.h | Handle near-critical chains as critical. |
| C-PD-5.i | Seek project cyclomatic complexity as low as 10-12. |
| C-PD-5.j | Use design by layers to reduce complexity. |

Project-network complexity is not code cyclomatic complexity. A service lifecycle diagram does not substitute for the project network or its arrow notation.

The full design procedure, dependency notation, alternative evaluation, and SDP decision are in [system and project design](../process/system-and-project-design.md). In an arrow project network, arrows represent activities and nodes represent instantaneous dependency events (pp. 195-198).

### Time and cost

| ID | Meaning to preserve |
| --- | --- |
| C-PD-6.a | First accelerate through clean, efficient engineering practices rather than compression. |
| C-PD-6.b | Do not commit to an option in the project's death zone. |
| C-PD-6.c | Prefer parallel work as a compression technique over reliance on top resources. |
| C-PD-6.d | Use top-resource compression cautiously. |
| C-PD-6.e | Avoid compressing by more than 30 percent. |
| C-PD-6.f | Avoid a project efficiency above 25 percent. |
| C-PD-6.g | Explore compression even when choosing a compressed option is unlikely. |

These metrics require the book's definitions. Do not interpret efficiency as CPU utilization or assume that starting more agents constitutes a valid compressed project design.

### Risk

| ID | Meaning to preserve |
| --- | --- |
| C-PD-7.a | Tailor criticality-risk category ranges to the project. |
| C-PD-7.b | Use activity risk to account for float outliers. |
| C-PD-7.c | Decompress the normal solution beyond the risk curve's tipping point. |
| C-PD-7.c.i | Aim toward 0.5 risk when decompressing. |
| C-PD-7.c.ii | Prefer the tipping point over adherence to a particular risk number. |
| C-PD-7.d | Avoid excessive decompression. |
| C-PD-7.e | Decompress design-by-layers options, potentially substantially. |
| C-PD-7.f | Keep normal options below 0.7 risk. |
| C-PD-7.g | Avoid risk below 0.3. |
| C-PD-7.h | Avoid risk above 0.75. |
| C-PD-7.i | Avoid options beyond either risk crossover boundary. |

Chapter 10, pp. 239-241 defines normalized risk as relative design fragility, not a probability of success or a model-confidence score. Targets above cannot be used without the relevant risk model and project assumptions.

Chapter 12, pp. 318-320 states that geometric activity risk generally does not conform to the arithmetic risk-value guidelines. Do not apply the 0.3/0.5/0.75 thresholds blindly across models. Decompression preserves activity estimates and staffing while adding float (pp. 249-250). See [numerical methods](numerical-methods.md).

## Project tracking guidelines

Source: pp. 429-430.

| ID | Meaning to preserve |
| --- | --- |
| C-PT-1 | Use binary completion criteria for the internal phases of an activity. |
| C-PT-2 | Apply phase weighting consistently across activities. |
| C-PT-3 | Track progress and effort every week. |
| C-PT-4 | Do not use features as the basis of progress reports. |
| C-PT-5 | Base progress reporting on integration points. |
| C-PT-6 | Monitor the float of near-critical chains. |

Appendix A, pp. 390-393 distinguishes progress from effort. Credit only completed phases, using their weights. Time spent, code committed, and tests attempted are not phase completion. The example phase percentages on p. 391 are not mandatory weights.

Keep duration-weighted progress distinct from direct-cost effort, particularly with variable token rates. Use the appropriate planned direct-cost curve when the simplifying one-resource assumption does not hold (p. 394). See [project tracking](../process/project-tracking.md).

## Service contract design guidelines

Source: p. 430; rationale in Appendix B, pp. 407-423.

| ID | Meaning to preserve |
| --- | --- |
| C-SC-1 | Design contracts for reuse. |
| C-SC-2 | Apply the service-contract design metrics below. |
| C-SC-2.a | Avoid a one-operation contract. |
| C-SC-2.b | Aim for three to five operations in a contract. |
| C-SC-2.c | Avoid a contract with more than twelve operations. |
| C-SC-2.d | Reject a contract with twenty or more operations. |
| C-SC-3 | Avoid operations that expose property-like access. |
| C-SC-4 | Keep a service to one or two contracts. |
| C-SC-5 | Avoid the junior handoff. |
| C-SC-6 | Entrust contract design to the architect or capable senior developers. |

Metrics evaluate a design; meeting them does not validate it. Appendix B, pp. 412-423 requires logically consistent, cohesive, independent, reusable facets and warns against designing merely to hit a metric.

Appendix B, p. 420 flags contracts with twelve or more operations as likely poor designs, while Appendix C says more than twelve. Preserve that distinction: twelve operations still calls for investigation under Appendix B. Do not silently alter the Appendix C threshold.

For twenty or more operations, p. 420 explicitly requires rejection and says there are no benign circumstances. Preserve both the Appendix C heading's guideline classification and that specific instruction; the guideline label does not grant a standing exception to this rejection.

The Application Architect assignment uses the senior-developer-as-junior-architect arrangement of Chapter 14, pp. 376-377. It does not require the Solution Architect to author every component's detailed design before construction can start.

## Applying the standard

Each application must provide evidence appropriate to the applicable item: requirements analysis, volatility rationale, architecture and interaction diagrams, reviewed detailed designs, project alternatives, calculations, phase exits, and integration results. The role allocation and evidence formats are operational choices recorded separately.

Automation may check structure and metrics, but cannot establish by itself that a decomposition truly encapsulates volatility, that a use case expresses the business correctly, or that a contract is cohesive. Those remain accountable design and review judgments.
