---
metadata-version: "1.0.0"
title: "System and project design"
description: "Define business analysis, system design, project alternatives, and SDP acceptance."
document-type: "process"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# System and project design

Source: [Righting Software](<../references/Righting Software.pdf>), Chapters 1-14. Appendix C governs; the chapter discussions supply its context. The Solution Architect is accountable for both designs. The Product Owner supplies the business view. The Project Manager supplies execution constraints and manages the selected design.

## Establish the business basis

Agree on the vision before itemizing business objectives. Include objectives needed to realize that vision and reject unrelated objectives. State the mission that connects the objectives to the architecture. Maintain bidirectional traceability between business objectives and architectural decisions. Compile a glossary before decomposition so that participants use the same terms with the same meanings. These requirements follow Chapter 5, pp. 108-112.

Requirements analysis identifies core use cases and candidate volatilities. Use both axes: one customer over time, and different customers at the same time. Examine competitors, historical changes, and the intended system lifespan. Record why each candidate is volatile and what consequence its change would have. Distinguish ordinary variability, speculative changes to the nature of the business, and volatility outside this system's scope. A volatility can be contained by a component, operational concept, or external service; the mapping need not be one-to-one. See Chapters 2 and 5, pp. 30-53 and 113-116.

## Design and validate the system

Use the service semantics, layers, and permitted interactions in [the standard](../standards/design-standard.md). A name ending in Manager, Engine, or Access does not establish that the component contains the appropriate volatility. Check the semantics and call patterns, not just names or folders.

Produce the smallest adequate set of composable components. Demonstrate support for each core use case through call-chain or sequence diagrams. Use sequence diagrams where order, concurrent participants, or timing matters. Preserve the source notation: solid black arrows for synchronous calls and dashed gray arrows for queued calls; layer colors are consistent across diagram types. Activity diagrams describe required behavior; call-chain and sequence diagrams validate its architectural realization. See Chapters 3-5, pp. 55-93 and 124-135.

Architecture is broad in scope and limited in design effort. Component contracts, messages, internal class designs, UX, and implementation details have narrower scope and can take much longer. Do not require all component details to be completed before project design or turn requirements discovery into a demand for an exhaustive final requirements set. See pp. 5, 84-90 and 372-377.

The TradeMe message bus, Message Is the Application pattern, workflow tool, Abstract Manager, and specific service counts are case-specific decisions. Do not copy them as mandatory template elements. Justify any corresponding choice through the application's objectives, volatilities, constraints, and team capabilities. The system design example explicitly warns against copying its architecture dogmatically. See pp. 95, 108-123 and 336-337.

## Design the project

Continue from system design into project design as one design effort. Plan the design effort itself using its dependencies. Chapter 14, pp. 370-372 lists the following 21 activities. Their numbering is a source checklist, not a requirement that independent activities execute strictly in that order; Figure 14-2 supplies the dependency network.

| Source step | Design activity |
| --- | --- |
| 1 | Identify core use cases. |
| 2 | Design the system; identify components and validating call chains. |
| 3 | Identify noncoding work. |
| 4 | Estimate every activity's duration and resource needs. |
| 5 | Estimate the whole project independently. |
| 6 | Design the normal solution. |
| 7 | Examine constrained resource availability. |
| 8 | Determine the subcritical option. |
| 9 | Investigate compression with better resources. |
| 10 | Investigate compression through parallel work. |
| 11 | Investigate compression by changing activities. |
| 12 | Determine the minimum feasible duration. |
| 13 | Evaluate throughput, efficiency, and execution complexity. |
| 14 | Model time and cost. |
| 15 | Decompress the normal solution for risk. |
| 16 | Rebuild the time-cost model with the decompression results. |
| 17 | Compare the model with the independent whole-project estimate. |
| 18 | Quantify and model risk. |
| 19 | Determine acceptable and excluded risk regions. |
| 20 | Identify viable alternatives. |
| 21 | Prepare the Software Development Plan review. |

For each candidate solution, pp. 371-372 requires discovering assumptions; stating staffing needs; revising activities, estimates, and resources; deriving dependencies; accommodating constraints; reducing network complexity; assigning resources and updating the network; drawing the network; evaluating earned value and staffing; revisiting assumptions; calculating cost elements; analyzing float; and calculating risk. A list of tasks or a Gantt chart alone does not constitute project design.

## Build the activity network

Include structural coding, nonstructural coding, and noncoding activities. Include implicit infrastructure dependencies, resource dependencies, reviews, detailed design, test engineering, training, migration, integration, deployment, and release work required by the approved project scope. Do not copy the example activity durations or staffing assumptions into a new application. See pp. 165-176, 255-264 and 335-342.

Use an arrow network: arrows are activities and nodes are instantaneous dependency events. Use zero-duration dummy activities where required to express dependencies. Identify start, completion, critical paths, and milestones. Consolidate inherited dependencies only when their removal preserves the same dependency relationship. Do not mistake dependency arrows for runtime calls. See Chapter 8 and pp. 258-262.

Staff available work from lowest to highest total float. Use resource dependencies to reflect the actual staffing arrangement. Seek minimum staffing that does not impede critical-path progress. Check staffing elasticity, task continuity, phase-in and phase-out, specialist availability, and the expected shallow S curve. Include resources needed between explicit activities. See pp. 171-194 and 263-275.

## Evaluate alternatives

The normal option, compressed options, and subcritical option reveal different combinations of schedule, cost, and risk. A subcritical option demonstrates under-resourcing consequences; it is not automatically a viable recommendation. The TradeMe example presents a decompressed subcritical fallback only after making it feasible. See pp. 215-233, 272-275 and 353-360.

Compression changes the project, not merely its promise. For parallel construction against a simulated dependency, include contract design, simulator work, and explicit reintegration and retesting against the real service. Update estimates, assignments, critical paths, cost, throughput, and execution complexity. Completing a client against a simulator does not complete integration with the service. See pp. 211-214, 278-289 and 346-350.

Decompression creates float without padding the original activity estimates. Retain the planned staffing. Do not consume the new float to remove resources and defeat its purpose. Analyze the risk curve's behavior, inclusion boundaries, and tipping point. For design by layers, account for its increased design risk and stronger decompression needs. See pp. 249-253, 295-303, 308-320 and 332-334.

Reduce oversized activities or treat them as deliberately designed subprojects. For very large projects, discover and compare feasible networks of networks before construction. Each subnetwork still needs its own design and management. Preserve system design integrity rather than duplicating independent architectural authority. See pp. 307-308 and 324-334.

## Decide at the SDP review

Present a small set of feasible alternatives with duration, total cost, risk, complexity, resource requirements, and assumptions. Communicate in business terms. Show impractical alternatives when needed to explain why they should not be selected, and identify them as such. Include the option not to proceed. Management selects an option and signs the SDP before the main work begins. The Project Manager then assigns actual workers against the selected design. See pp. 151-153, 171, 303-305, 359-360 and 366-367.

The normal starting point is construction after SDP review. Chapter 11, p. 279 discusses a bounded, architect-designed possibility of moving infrastructure and Client design into the front end, with explicit risks to the proceed-or-cancel decision. It is not a worker exemption from approval, and it does not authorize premature implementation of business features.

## Execute and improve

Use the [service lifecycle](service-lifecycle.md) within the project design. Use [project tracking](project-tracking.md) to detect and correct deviations early. Reassess project commitments when scope or constraints change. Debrief projects, subsystems, and milestones, including successful ones, and act on recurring problems. QA addresses prevention, SOPs, standards, training, and root causes; testing alone is not QA. See pp. 378-383 and Appendix A.
