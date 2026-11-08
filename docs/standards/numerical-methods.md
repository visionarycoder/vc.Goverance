---
metadata-version: "1.0.0"
title: "Numerical methods"
description: "Preserve the book’s planning calculations, assumptions, and model limits."
document-type: "standard"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Numerical methods

Source: [Righting Software](https://www.amazon.com/dp/0136524036), Chapters 7–13 and Appendix A. These definitions constrain future calculators; no planning engine is implemented here.

| Quantity | Required interpretation |
| --- | --- |
| Duration | Preserve activity estimates in five-day quanta and use an explicit work calendar. Tokens are not days. |
| Total float | Delay available without delaying project completion. Shared chain float is not independently spendable by every activity. |
| Free float | Delay available without disturbing the next activity's scheduled start. |
| Normal solution | Seek minimum staffing that allows uninterrupted critical-path progress. Minimum direct cost need not equal minimum total cost. |
| Cost | Model direct and indirect costs by their relationship to project value. Do not classify by job title alone or count fixed costs twice. |
| Total cost | Sum modeled direct and indirect costs. Do not independently regress total cost in a way that breaks that relationship. |
| Compression | Recalculate activities, resource dependencies, cost, critical paths, and complexity. More workers alone do not establish a feasible compressed option. |
| Decompression | Add float without padding activity estimates or reducing planned staffing. Prefer the risk tipping point over a fixed target. |
| Efficiency | Use the book's project-design definition. Do not substitute CPU utilization or token utilization. |
| Network complexity | Use E − N + 2P for the dependency network. P is one for a connected project network; networks of networks need their appropriate representation. This is not code complexity. |

## Risk model conditions

Chapters 10 and 12 distinguish criticality risk, Fibonacci criticality risk, arithmetic activity risk, and geometric alternatives. Identify the model and project-specific category boundaries with every value. Risk represents relative design fragility, not success probability.

For the illustrated four-category criticality model, R = (4Nc + 3Nr + 2Ny + Ng)/(4N). The categories and weights belong to that model. Do not silently transplant its boundaries to another project. Exclude dummy activities and instantaneous milestones from activity counts.

Arithmetic activity risk is R = 1 − sum(Fi)/(M × N), where Fi is activity total float and M is maximum float. The expression is undefined when M is zero. Use the appropriate alternative model rather than returning zero risk for an all-critical network. Apply any source-prescribed outlier cap to a risk-input copy, preserving the actual schedule and float. Chapter 13's example treatment does not establish a universal half-standard-deviation cap.

Geometric activity risk generally does not follow arithmetic risk thresholds such as 0.3, 0.5, and 0.75. Investigate oversized activities and decomposition before relying on geometric treatment to accommodate them. Model selection requires judgment, not whichever score permits a desired option.

## Precision and source correction

Use full-precision coefficients from the applicable model; round only the presentation. Do not assume coefficients in a worked example apply to the target project.

The owner approved the official companion calculation F = C(tmr)/R(tmr), preserving the contradictory printed p. 310 ratio as a discrepancy. See the [source-resolution record](../governance/source-authority.md). This scales risk into cost units to find crossover boundaries; it is not an authorization to alter raw risk scores.

For the official example, the companion calculation gives tmr ≈ 8.25385557, R(tmr) ≈ 0.85156504, C(tmr) ≈ 28.04401022, and F ≈ 32.93231726. The full-precision cubic risk model's inflection formula −b/(3a) gives approximately 10.61858004 months and risk 0.54996122. Rounded display equations do not reproduce these values reliably.

## Tracking

Duration-weighted progress is P = sum(Ei × Ai)/sum(Ei), where Ei is estimated activity duration and Ai is credited completed-phase fraction. Direct-cost effort is D = sum(Si)/sum(Ri), where Si is spent direct cost and Ri is planned direct cost. These quantities have different weights. Compare effort against the planned direct-cost curve when the simplifying equal-resource assumption does not apply. See [project tracking](../process/project-tracking.md) and [token costing](../process/token-costing.md).
