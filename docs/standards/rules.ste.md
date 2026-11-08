---
metadata-version: "1.0.0"
title: "Standard Technical English rules"
description: "Provide source-linked Standard Technical English rule records."
document-type: "standard"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Standard Technical English rules

Standard Technical English (STE) extraction of [Righting Software](<../references/Righting Software.pdf>). The [JSON records](rules.json) contain stable identifiers, source locators, classification, context, decision ownership, and exception policy. The source governs. Organizational assignments are separate from source rules.

Read applicable records together. Preserve explicit interaction exceptions. Guidelines require strong, unusual justification through the responsible authority; workers cannot approve departures. Directives cannot be waived. The twenty-operation contract rejection has no standing exception. The records assist review. They do not prove semantic compliance or enforce permissions.

## Rules

| ID | Class | Controlled instruction | Printed source pages |
| --- | --- | --- | --- |
| C-PRIME | directive | Do not derive the architecture by mapping the requirements' functionalities into components. Analyze requirements to discover volatility and required behavior; do not ignore them. See also pp. 84-87. | 426 |
| C-D-1 | directive | Reject functional decomposition. | 426 |
| C-D-2 | directive | Use volatility as the basis of decomposition. | 426 |
| C-D-3 | directive | Produce a design whose components compose to deliver the required behaviors. | 426 |
| C-D-4 | directive | Deliver features through integration rather than feature-shaped implementation units. | 426 |
| C-D-5 | directive | Iterate the design and construct the system incrementally. | 426 |
| C-D-6 | directive | Engineer the project that will construct the system. | 426 |
| C-D-7 | directive | Enable informed decisions through feasible alternatives trading schedule, cost, and risk. | 426 |
| C-D-8 | directive | Construct according to the project's critical path. | 426 |
| C-D-9 | directive | Maintain schedule commitments throughout execution. | 426 |
| C-SD-1.a | guideline | Record the behavior required of the system rather than a list of functionalities. | 426–427 |
| C-SD-1.b | guideline | Express that behavior as use cases. | 426–427 |
| C-SD-1.c | guideline | Use activity diagrams for use cases with nested conditions. | 426–427 |
| C-SD-1.d | guideline | Remove proposed solutions disguised as requirements. | 426–427 |
| C-SD-1.e | guideline | Validate the architecture against every core use case. | 426–427 |
| C-SD-2.a | guideline | In a system without subsystems, avoid exceeding five Managers. | 426–427 |
| C-SD-2.b | guideline | Keep the number of subsystems to a handful. | 426–427 |
| C-SD-2.c | guideline | Keep each subsystem to no more than three Managers. | 426–427 |
| C-SD-2.d | guideline | Seek the observed golden-ratio relationship between Engines and Managers. | 426–427 |
| C-SD-2.e | guideline | Permit a ResourceAccess component to serve multiple Resources where needed. | 426–427 |
| C-SD-3.a | guideline | Expect less volatility toward the bottom of the architecture. | 426–427 |
| C-SD-3.b | guideline | Expect greater reuse toward the bottom. | 426–427 |
| C-SD-3.c | guideline | Do not design encapsulation around a change to the business's fundamental nature. | 426–427 |
| C-SD-3.d | guideline | Keep Managers almost expendable, rather than expensive monoliths or empty pass-throughs. | 426–427 |
| C-SD-3.e | guideline | Seek architectural symmetry. | 426–427 |
| C-SD-3.f | guideline | Keep public communication channels out of internal system interactions. | 426–427 |
| C-SD-4.a | guideline | Avoid an open architecture. | 426–427 |
| C-SD-4.b | guideline | Avoid a semi-open or semi-closed architecture. | 426–427 |
| C-SD-4.c | guideline | Prefer a closed architecture, with the following constraints. | 426–427 |
| C-SD-4.c.i | guideline | Do not make upward calls. | 426–427 |
| C-SD-4.c.ii | guideline | Do not make sideways calls, with the specified queued Manager exception. | 426–427 |
| C-SD-4.c.iii | guideline | Do not skip downward across multiple layers. | 426–427 |
| C-SD-4.c.iv | guideline | Meet needs that would open the architecture through queued calls or asynchronous event publication. | 426–427 |
| C-SD-4.d | guideline | Extend through subsystems. | 426–427 |
| C-SD-5.a | guideline | Every component may use Utilities. | 426–427 |
| C-SD-5.b | guideline | Managers and Engines may invoke ResourceAccess services. | 426–427 |
| C-SD-5.c | guideline | Managers may invoke Engines. | 426–427 |
| C-SD-5.d | guideline | A Manager may queue a call to another Manager. | 426–427 |
| C-SD-6.a | guideline | A Client does not invoke several Managers to execute one use case. | 426–427 |
| C-SD-6.b | guideline | A Manager does not queue calls to several Managers in one use case. | 426–427 |
| C-SD-6.c | guideline | An Engine does not receive queued calls. | 426–427 |
| C-SD-6.d | guideline | ResourceAccess does not receive queued calls. | 426–427 |
| C-SD-6.e | guideline | Clients do not publish events. | 426–427 |
| C-SD-6.f | guideline | Engines do not publish events. | 426–427 |
| C-SD-6.g | guideline | ResourceAccess does not publish events. | 426–427 |
| C-SD-6.h | guideline | Resources do not publish events. | 426–427 |
| C-SD-6.i | guideline | Engines, ResourceAccess services, and Resources do not subscribe to events. | 426–427 |
| C-PD-1.a | guideline | Avoid overengineering project design for perfect precision; make it sufficient for informed, feasible commitments. See p. 365. | 427–429 |
| C-PD-1.b | guideline | Do not design the project without an architecture that contains volatility. | 427–429 |
| C-PD-1.c | guideline | State and verify the assumptions underlying the plan. | 427–429 |
| C-PD-1.d | guideline | Follow the prescribed sequence for designing the project. | 427–429 |
| C-PD-1.e | guideline | Develop multiple options, including at least normal, compressed, and subcritical solutions. | 427–429 |
| C-PD-1.f | guideline | Communicate with management using Optionality. | 427–429 |
| C-PD-1.g | guideline | Complete the Software Development Plan review before the main work begins. | 427–429 |
| C-PD-2.a | guideline | Avoid multiple accountable system architects. | 427–429 |
| C-PD-2.b | guideline | Establish the core team at the outset. | 427–429 |
| C-PD-2.c | guideline | Seek the minimum staffing that permits uninterrupted critical-path progress. | 427–429 |
| C-PD-2.d | guideline | Allocate resources according to float. | 427–429 |
| C-PD-2.e | guideline | Preserve the appropriate staffing distribution over the project. | 427–429 |
| C-PD-2.f | guideline | Plan earned value as a shallow S curve. | 427–429 |
| C-PD-2.g | guideline | Maintain one-to-one component and developer assignments. | 427–429 |
| C-PD-2.h | guideline | Preserve continuity between a resource's successive tasks where possible. | 427–429 |
| C-PD-3.a | guideline | Avoid large, mass integration events. | 427–429 |
| C-PD-3.b | guideline | Do not defer integration to the project's end. | 427–429 |
| C-PD-4.a | guideline | Avoid overestimating. | 427–429 |
| C-PD-4.b | guideline | Avoid underestimating. | 427–429 |
| C-PD-4.c | guideline | Prefer accuracy over numerical precision. | 427–429 |
| C-PD-4.d | guideline | Estimate activities in five-day quanta. | 427–429 |
| C-PD-4.e | guideline | Use a whole-project estimate to check, or help initiate, the detailed project design. | 427–429 |
| C-PD-4.f | guideline | Actively reduce estimation uncertainty. | 427–429 |
| C-PD-4.g | guideline | Use the correct estimation dialogue when eliciting estimates. | 427–429 |
| C-PD-5.a | guideline | Include resource dependencies as actual dependencies. | 427–429 |
| C-PD-5.b | guideline | Ensure each activity belongs to a chain that begins and ends on a critical path. | 427–429 |
| C-PD-5.c | guideline | Assign a resource to every activity. | 427–429 |
| C-PD-5.d | guideline | Avoid node network diagrams. | 427–429 |
| C-PD-5.e | guideline | Prefer arrow network diagrams. | 427–429 |
| C-PD-5.f | guideline | Avoid oversized god activities. | 427–429 |
| C-PD-5.g | guideline | Represent large projects through a network of networks. | 427–429 |
| C-PD-5.h | guideline | Handle near-critical chains as critical. | 427–429 |
| C-PD-5.i | guideline | Seek project cyclomatic complexity as low as 10-12. | 427–429 |
| C-PD-5.j | guideline | Use design by layers to reduce complexity. | 427–429 |
| C-PD-6.a | guideline | First accelerate through clean, efficient engineering practices rather than compression. | 427–429 |
| C-PD-6.b | guideline | Do not commit to an option in the project's death zone. | 427–429 |
| C-PD-6.c | guideline | Prefer parallel work as a compression technique over reliance on top resources. | 427–429 |
| C-PD-6.d | guideline | Use top-resource compression cautiously. | 427–429 |
| C-PD-6.e | guideline | Avoid compressing by more than 30 percent. | 427–429 |
| C-PD-6.f | guideline | Avoid a project efficiency above 25 percent. | 427–429 |
| C-PD-6.g | guideline | Explore compression even when choosing a compressed option is unlikely. | 427–429 |
| C-PD-7.a | guideline | Tailor criticality-risk category ranges to the project. | 427–429 |
| C-PD-7.b | guideline | Use activity risk to account for float outliers. | 427–429 |
| C-PD-7.c | guideline | Decompress the normal solution beyond the risk curve's tipping point. | 427–429 |
| C-PD-7.c.i | guideline | Aim toward 0.5 risk when decompressing. | 427–429 |
| C-PD-7.c.ii | guideline | Prefer the tipping point over adherence to a particular risk number. | 427–429 |
| C-PD-7.d | guideline | Avoid excessive decompression. | 427–429 |
| C-PD-7.e | guideline | Decompress design-by-layers options, potentially substantially. | 427–429 |
| C-PD-7.f | guideline | Keep normal options below 0.7 risk. | 427–429 |
| C-PD-7.g | guideline | Avoid risk below 0.3. | 427–429 |
| C-PD-7.h | guideline | Avoid risk above 0.75. | 427–429 |
| C-PD-7.i | guideline | Avoid options beyond either risk crossover boundary. | 427–429 |
| C-PT-1 | guideline | Use binary completion criteria for the internal phases of an activity. | 429–430 |
| C-PT-2 | guideline | Apply phase weighting consistently across activities. | 429–430 |
| C-PT-3 | guideline | Track progress and effort every week. | 429–430 |
| C-PT-4 | guideline | Do not use features as the basis of progress reports. | 429–430 |
| C-PT-5 | guideline | Base progress reporting on integration points. | 429–430 |
| C-PT-6 | guideline | Monitor the float of near-critical chains. | 429–430 |
| C-SC-1 | guideline | Design contracts for reuse. | 430 |
| C-SC-2 | guideline | Apply the service-contract design metrics below. | 430 |
| C-SC-2.a | guideline | Avoid a one-operation contract. | 430 |
| C-SC-2.b | guideline | Aim for three to five operations in a contract. | 430 |
| C-SC-2.c | guideline | Avoid a contract with more than twelve operations. | 430 |
| C-SC-2.d | guideline | Reject a contract with twenty or more operations. | 430 |
| C-SC-3 | guideline | Avoid operations that expose property-like access. | 430 |
| C-SC-4 | guideline | Keep a service to one or two contracts. | 430 |
| C-SC-5 | guideline | Avoid the junior handoff. | 430 |
| C-SC-6 | guideline | Entrust contract design to the architect or capable senior developers. | 430 |
| RS-01 | contextual_rule | Use functional decomposition only to discover requirements. Do not use it to decompose the architecture. | 22–31 |
| RS-02 | contextual_rule | Examine volatility across time and across customers. Distinguish volatility from variability. | 30–42 |
| RS-03 | contextual_rule | Do not add Engines solely to obtain a target Manager-to-Engine ratio. | 63–68 |
| RS-04 | contextual_rule | Treat Managers and Engines as members of the business logic layer. Permit the explicit Manager-to-Engine interaction. | 77–79 |
| RS-05 | contextual_rule | Reject Client-to-Engine, Engine-to-Engine, and ResourceAccess-to-ResourceAccess calls. | 80–81 |
| RS-06 | contextual_rule | Classify a message as a request or an event before applying event rules. A bus does not authorize forbidden interactions. | 118–123 |
| RS-07 | contextual_rule | Distinguish architectural symmetry from symmetry inside component implementations. | 82 |
| RS-08 | contextual_rule | Do not adopt the example message bus or workflow technology without application-specific justification. | 95–123 |
| RS-09 | contextual_rule | Establish vision, objectives, mission, and architecture. Trace objectives and architecture in both directions. | 108–112 |
| RS-10 | contextual_rule | Keep one architect accountable for system and project design. Delegate support without dividing that accountability. | 148–194 |
| RS-11 | contextual_rule | Assign one developer to one service at a time. Permit sequential assignments. Evaluate pair programming separately. | 153–155 |
| RS-12 | contextual_rule | Represent activities as arrows. Represent instantaneous dependency events as nodes. Give dummy activities zero duration. | 195–198 |
| RS-13 | contextual_rule | Include resource dependencies in the network. Assign available work in increasing order of total float. | 171–176 |
| RS-14 | contextual_rule | For simulated dependencies, plan contract design, simulator work, integration with real services, and retesting. | 211–289 |
| RS-15 | contextual_rule | Decompress by adding float. Preserve activity estimates and planned staffing. | 249–250 |
| RS-16 | contextual_rule | Interpret normalized project risk as relative design fragility. Do not interpret it as a probability of success. | 239–241 |
| RS-17 | contextual_rule | Do not apply arithmetic risk thresholds directly to geometric activity risk. | 318–320 |
| RS-18 | contextual_rule | Use full-precision model coefficients for calculations. Round displayed results only. | 301–314 |
| RS-19 | contextual_rule | Measure project-network complexity separately from source-code complexity. | 320–322 |
| RS-20 | contextual_rule | Follow the project-design dependency network. Do not serialize independent design activities merely because the checklist is numbered. | 370–372 |
| RS-21 | contextual_rule | Review delegated detailed designs before handoff. Require developers to consult the designer about refinements. | 374–377 |
| RS-22 | contextual_rule | Distinguish defect-prevention QA from test engineering and test execution. | 378–382 |
| RS-23 | contextual_rule | Define the review moderator, owner, scribe, critics, and follow-up responsibilities. | 380–382 |
| RS-24 | contextual_rule | Use SRS for Service Requirements Specification. Use STP for Service Test Plan. | 388–390 |
| RS-25 | contextual_rule | After successful SRS review, permit test planning and detailed-design work to proceed on parallel paths. | 388–390 |
| RS-26 | contextual_rule | Repeat the preceding activity after a failed review. Require successful STP review before plan-based testing. | 388–390 |
| RS-27 | contextual_rule | Retain the developer white-box test client during construction. Perform plan-based black-box testing after integration. | 388–390 |
| RS-28 | contextual_rule | Credit completed phases only. Keep duration-weighted progress separate from resource-cost effort. | 390–394 |
| RS-29 | contextual_rule | When resource costs differ, compare actual direct cost with the planned direct-cost curve. | 394 |
| RS-30 | contextual_rule | Project direct cost at the projected completion date. Assess schedule-related indirect cost separately. | 395–405 |
| RS-31 | contextual_rule | Assess duration and cost changes after a scope change. Obtain management acceptance of revised commitments. | 405 |
| RS-32 | contextual_rule | Evaluate contract cohesion, consistency, independence, and reuse. Do not treat operation counts as design validation. | 412–423 |
| RS-33 | contextual_rule | Investigate a contract with twelve operations. Reject a contract with twenty or more operations. | 420 |
