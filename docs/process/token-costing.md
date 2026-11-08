---
metadata-version: "1.0.0"
title: "Token based costing"
description: "Define agent token costs without replacing Method schedule or progress measures."
document-type: "process"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Token based costing

## Authority and scope

The human owner directed token-based costing on 2026-11-07. This assigns a consumption measure to agent workers. It does not replace the design principles, project network, schedule, float, risk, or progress definitions in [Righting Software](<../references/Righting Software.pdf>).

The source separates measurable direct value from ongoing indirect value, models the total cost of each project option, and distinguishes consumed effort from earned progress. See pp. 184-187, 222-231, 364 and 392-395. The token ledger below is the framework's worker-cost implementation, not a claim that Löwy prescribed tokens.

## Record consumption

Record each model request exactly once, using a stable request or usage identifier. Associate it with a worker, application, project-design option, activity or overhead account, lifecycle phase, model, and usage source. Record the governing requirements and design versions through the work assignment.

Keep separate token classes when their cost treatment differs. At minimum, preserve reported input and output counts. Preserve cached input separately when available. If cached input is included in total input, derive uncached input by subtraction. Do not add both counts as independent inputs. If reasoning usage is reported as part of output, do not add it a second time. Provider-specific usage definitions must be verified when the technology baseline is selected.

Use reported consumption rather than planned limits as actual usage. Count repeated context when a later request actually consumes it. Count retries, unsuccessful attempts, reviews, and rework when they consume resources. Deduplicate repeated telemetry for the same request. If the usage source is missing, mark consumption unknown. Do not record a false zero.

An implementation agent cannot edit the authoritative consumption ledger, rate baseline, or prior usage records. Its reports are input evidence for independently recorded usage. Corrections preserve the original event and its correction history.

## Estimate and price

For each activity, estimate a token vector by model and usage class. Include the internal work required to finish the activity: construction, the white-box test client, reviews, corrections, integration, and testing required by the activity’s approved lifecycle. When project design extracts one of those phases as a separate activity, remove it from the original activity's budget to prevent double counting.

Let `T_i,m,k` be planned tokens for activity `i`, model `m`, and usage class `k`. Let `U_i,m,k(t)` be actual tokens consumed by time `t`. Let `r_m,k` be the approved rate per one million tokens, in a common cost unit.

```text
Planned direct cost for activity i:
    R_i = sum(T_i,m,k * r_m,k / 1,000,000)

Actual direct cost for activity i:
    S_i(t) = sum(U_i,m,k(t) * r_m,k / 1,000,000)

Activity effort:
    C_i(t) = S_i(t) / R_i

Project direct effort:
    D(t) = sum(S_i(t)) / sum(R_i)
```

Do not treat one input token, one cached token, and one output token as identical costs unless the approved rate basis makes them equal. Raw counts remain useful consumption measures; they are not a comparable scalar cost across different models and rate classes. A missing rate makes the corresponding cost unavailable, while the measured token count remains reportable.

Version the rate basis and its effective period. Use a common approved basis to compare project-design options. Preserve both the original budget basis and current forecast when rates or models change. Distinguish consumption variance from rate variance. Do not silently restate a budget to make an overrun disappear.

For a local model with no per-token invoice, record raw consumption. A conversion to comparable cost requires an approved allocation rate reflecting the selected resource arrangement. Do not invent a rate or report local inference as free merely because there is no token invoice.

## Classify direct and indirect cost

Classify the work by the value and activity it contributes, not merely by the worker's title. For example, architecture or a specific test-harness activity can be direct work. Ongoing leadership, routine process oversight, and recurring operations can be indirect work. The source's examples sometimes make explicit alternative planning assumptions about idle developers; record such an assumption instead of treating it as a universal accounting rule. See pp. 222-229, 263-264 and 342.

Each usage event has one cost allocation, or an explicit split whose parts total the event's full cost. Do not charge a review both inside a service activity and again as an independent activity. Aggregate approved indirect usage separately. Include non-token operational costs and fixed costs where they exist; token accounting does not remove them from total project cost.

```text
Project total cost = direct cost + indirect cost + applicable fixed cost
```

The source commonly absorbs fixed costs into the indirect curve. Use one convention consistently and do not include the same fixed cost twice. Measure direct and indirect token consumption explicitly. Do not assume tokens accrue at a constant rate merely because resource-time overhead is approximately linear in a source example.

## Preserve schedule and progress

Keep activity estimates in five-day quanta and progress/effort reporting weekly under C-PD-4.d and C-PT-3. Define the actual worker calendar and availability before calculating a schedule. Token budgets do not determine duration or remove resource dependencies. No conversion from tokens to days is authorized by this costing decision.

Earn progress only through successful binary phase exits, with the approved phase weights. Preserve the duration-weighted project progress formula on pp. 392-393. Do not replace its weights with token budgets. Compare actual direct cost with the appropriate planned direct-cost curve, since variable model rates invalidate the simplifying assumption that cost and duration weights are identical.

Do not use token utilization as the book's project-efficiency metric or tokens as float. Record resource time and the original metric definitions independently where required. A cross-model or local-hardware efficiency calibration remains an explicit planning question, not a worker-defined substitution.

## Worked accounting example

The following rates are synthetic arithmetic inputs, not vendor prices or a chosen technology baseline.

| Usage class | Planned tokens | Actual tokens | Synthetic cost units per million tokens |
| --- | ---: | ---: | ---: |
| Uncached input | 1,000,000 | 1,200,000 | 2 |
| Cached input | 500,000 | 400,000 | 0.5 |
| Output | 100,000 | 150,000 | 8 |

The planned activity direct cost is `2 + 0.25 + 0.8 = 3.05` cost units. Actual direct cost is `2.4 + 0.2 + 1.2 = 3.8` units. The activity has consumed `3.8 / 3.05 = 124.59%` of its direct-cost estimate. Its earned progress still depends only on completed phase exits.

## Responsibilities

The Solution Architect includes token estimates, rates, overhead assumptions, and any non-token cost in each project-design option. The Project Manager tracks the independent ledger and forecasts. QA checks measurement reliability and recurring variance causes. Leadership selects model and resource choices through the normal baseline and project-design decisions. Developers cannot select a cheaper unauthorized model or reduce test scope to fit a token budget.
