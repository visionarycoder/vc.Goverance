---
metadata-version: "1.0.0"
title: "Project tracking"
description: "Define progress, effort, float monitoring, forecasts, and corrective decisions."
document-type: "process"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Project tracking

Source: [Righting Software](<../references/Righting Software.pdf>), Appendix A, printed pp. 387-405; Chapters 7-8. The Project Manager tracks execution. The Solution Architect redesigns the project with the Project Manager when the observed situation requires it.

## Keep the measurements distinct

Let `w_j` be a phase weight, `A_i(t)` an activity's completion at time `t`, `E_i` its estimated duration, `S_i(t)` its accumulated direct cost, and `R_i` its estimated direct cost. Use the following source definitions:

| Measure | Calculation | Source |
| --- | --- | --- |
| Activity progress | Sum the weights of completed phases only. | pp. 389-392 |
| Project progress | `P(t) = sum(E_i * A_i(t)) / sum(E_i)` | pp. 392-393 |
| Activity effort | `C_i(t) = S_i(t) / R_i` | p. 392 |
| Project effort | `D(t) = sum(S_i(t)) / sum(R_i)` | p. 394 |
| Planned earned value | Sum the estimated durations of activities planned complete by `t`; divide by the total estimated duration. | pp. 187-188 |

Progress is earned completion. Effort is consumed direct cost relative to its estimate. Spending 150 percent of a budget can coexist with only 60 percent progress. Neither time spent nor tokens consumed constitutes completion.

Use consistent phase-weighting methods. A phase earns its weight only after its binary exit condition succeeds. The example percentages in Table A-1 do not prescribe a universal weighting method. Track an activity's internal phases. Do not confuse them with overlapping project phases such as infrastructure or testing. See pp. 264 and 389-393.

The source's simple comparison between effort and the planned earned-value curve assumes one planned resource per activity. When resource quantities or costs differ, track effort against its corresponding planned direct-cost curve. Do not assume those two curves are identical. This matters when implementing [token-based costing](token-costing.md). See p. 394.

## Track and project

Track progress and effort weekly. Plot plan, actual progress, and actual effort. Project the observed trends to completion. The progress projection reaches 100 percent at the projected completion date. Evaluate the effort projection at that projected date to estimate direct-cost overrun. Account separately for indirect cost when reporting the total cost. See pp. 394-398 and C-PT-3.

Monitor total float on noncritical chains, particularly near-critical chains. A delayed upstream activity consumes downstream total float. Free float identifies how much delay can occur without disturbing another activity; it is distinct from total float. Do not add the shared float of chain activities as though each had an independent reserve. See pp. 199-206 and C-PT-6.

Report integration achievements to management. Do not substitute feature counts, commits, passing checks, or consumed token budgets for integrated progress. See pp. 146-147 and C-PT-4 through C-PT-5.

## Correct the cause

| Observed pattern | Source interpretation | Response to assess with the responsible owners |
| --- | --- | --- |
| Progress and effort follow the plan. | No corrective intervention is indicated. | Continue tracking; do not disrupt a healthy plan. |
| Progress is below plan; effort is above plan. | Likely underestimation. | Redesign commitments through revised estimates, reduced scope, or a justified combination. Do not add workers reflexively. |
| Progress and effort are below plan; progress is below effort. | Possible resource leak. | Escalate cross-project priority and resource commitments to the manager who owns both projects. |
| Progress is above plan, with excess effort. | Possible overestimation, excess staffing, or unplanned parallel work. | Reassess estimates and staffing. The source favors releasing excess resources when the project analysis supports that choice. Assess the consequences before changing deadlines or scope. |

These patterns identify hypotheses to investigate, not automatic diagnoses. Choose a corrective response using actual projections and a revised project design. The source allows early-project movement to an already designed compressed alternative. It does not justify indiscriminate late staffing. See pp. 398-404.

Scope changes require quantified schedule and cost consequences. Management accepts the new commitments or declines the change. Keep the approved history and the current plan distinct; an updated plan is a working control document, not a reason to erase evidence of the change. See pp. 387, 399 and 405.
