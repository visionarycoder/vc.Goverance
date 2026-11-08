---
metadata-version: "1.0.0"
title: "UI visualization pattern"
description: "Record supporting UI visualization guidance and its architectural limits."
document-type: "reference"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# UI visualization pattern

**Pattern:** PAT-010. **Scope:** data visualization within an application's UI. The owner approved [Designing Data Visualizations](https://www.amazon.com/dp/1449312284) (source copy removed from this repository), Noah Iliinsky and Julie Steele, O’Reilly, 2011, as a supporting reference for UI usage. It does not replace the governing Method or establish a general UI standard. No chart library or application stack is selected.

## Standard Technical English guidance

These records are supporting design guidance for pattern selection. They are not additional Appendix C directives. Apply them within the [existing ownership hierarchy](../governance/roles-and-decisions.md).

| ID | Condition | Design action | Source, printed pages |
| --- | --- | --- | --- |
| UI-VIZ-01 | Before choosing a chart or tool | State what the reader needs to learn or decide. | 21–22 |
| UI-VIZ-02 | When defining the audience | Record reader knowledge, vocabulary, context, available time, and required detail. | 15–16; 91 |
| UI-VIZ-03 | Before selecting visual encodings | Identify relevant dimensions, relationships, data types, ranges, and ordering. | 16–17; 25–29 |
| UI-VIZ-04 | When choosing displayed information | Include information that supports the stated goal. Remove distracting dimensions and decoration. | 23–24 |
| UI-VIZ-05 | When representing ordered values | Use an ordered visual property. Do not assume hue has a natural order. Distinguish hue from brightness and saturation. | 25–26 |
| UI-VIZ-06 | When encoding multiple values | Check that readers can distinguish the required values. Consider redundant encoding when it improves comprehension. | 28–29 |
| UI-VIZ-07 | When defining layout | Evaluate position for important relationships. Make direction, grouping, and proximity reflect the intended meaning. | 91–92 |
| UI-VIZ-08 | When labeling a visualization | Use vocabulary the intended reader can understand. Label important information and remove unnecessary labels. | 92 |
| UI-VIZ-09 | Across related views | Keep membership, ordering, placement, and encoding meanings consistent. | 93 |

Appendix B's shorthand warning about color and quantity must be read with Chapter 4: unordered hue differs from ordered brightness and saturation. Do not convert the shorthand into an unconditional ban on all quantitative color scales. The source's permission to depart intentionally from visualization guidance does not authorize a worker to depart from the approved detailed design or Method constraints.

## Detailed-design handoff

The following evidence format is a framework proposal, not wording attributed to the supporting authors:

- Requirement ID and user information need, accepted by the Product Owner.
- Audience, context, display conditions, and expected reader task.
- Data source contract, dimension definitions, units, ordering, and any aggregation or filtering semantics.
- Encoding map, labels, interaction behavior, and permitted visual variation.
- Required empty, loading, unavailable, partial, and extreme-data behavior.
- Test cases and comprehension criteria defined with the Test Architect.
- Reviewed detailed-design revision and the applicable system-design revision.

The Application Architect owns the detailed realization within Solution Architect bounds. UI code does not gain direct resource access or prohibited cross-component calls because data is needed for a chart. Escalate contract or boundary changes through the existing lifecycle. This pattern does not add a separate review gate.

## Review scope

The reference has 110 PDF pages. Printed Arabic page n is one-based PDF page n + 14. Reviewed material comprises identity and contents, selected preface passages, Chapter 2 pp. 15–17, Chapter 3 pp. 21–24, Chapter 4 pp. 25–26 and 28–29, and Appendix B pp. 91–93. Figures 4-3 and 4-4 on pp. 28–29 were rendered and visually inspected. This is a targeted review, not a whole-book review, accessibility certification, or exhaustive UI testing specification.
