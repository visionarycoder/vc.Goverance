---
metadata-version: "1.0.0"
title: "Current Microsoft technical standard"
description: "Define current Microsoft-based coding policy and the owner’s naming choices."
document-type: "standard"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Current Microsoft technical standard

**Reviewed:** 2026-11-07. **Authority:** the human owner's request for Microsoft's latest coding and code-quality guidance, with no underscore prefixes. **Scope:** technical implementation within approved architecture. This does not select an application stack. The Method's architecture, contracts, project design, and lifecycle remain governing.

## Source precedence

Use current official Microsoft documentation for language, API, compiler, analyzer, and library implementation details. Historical books and archived samples remain supporting evidence. They do not establish current API compatibility. Preserve original reference files. Modernize implementations derived from them. Escalate any apparent conflict with The Method instead of silently changing architectural boundaries.

Microsoft's documentation-team conventions currently use underscore-prefixed instance fields and `s_`-prefixed static fields. These are configurable conventions. The owner explicitly chooses unprefixed names. This is a recorded local override, not a claim that Microsoft recently prohibited underscores. See [Microsoft identifier guidance](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/identifier-names).

## Standard Technical English rules

The [structured records](technical-rules.json) are separate from the existing Method rules. Sources are listed below; local policy choices are identified explicitly.

| ID | Condition | Instruction | Basis |
| --- | --- | --- | --- |
| TECH-01 | Implementing technical details | Consult current official Microsoft guidance for the approved technology. Treat historical examples as evidence rather than current API instructions. | Owner policy; S1, S7 |
| TECH-02 | Naming an owned C# identifier | Do not use underscore naming prefixes, including `_`, `__`, `m_`, `s_`, and `t_`. A standalone language discard is not a naming prefix. | Explicit owner override; S2 |
| TECH-03 | Naming private or internal non-constant fields | Use unprefixed camelCase for instance and static fields. Qualify instance-field access with `this.`; use the declaring type when static qualification is needed. | Framework convention; S2, S3 |
| TECH-04 | Naming other symbols | Use PascalCase for types, namespaces, methods, properties, events, and constants. Prefix interfaces with `I`. Use camelCase for parameters and ordinary locals. Preserve Method component semantics and suffixes. | Adapted convention; S2 |
| TECH-05 | Selecting SDK and language versions | Select supported stable tooling through the Solution Architect. Record the SDK and roll-forward policy in global.json. Use the target-framework-compatible language default or an explicit compatible version. Do not set LangVersion to latest or preview. | Framework policy; S5, S6 |
| TECH-06 | Writing C# | Use supported modern features when they improve clarity or correctness. Use braces, four-space indentation, and consistent formatting. | Adapted convention; S1 |
| TECH-07 | Defining reference-type intent | Enable nullable analysis. Annotate optional references. Resolve warnings instead of disabling analysis or adding unjustified null-forgiving operators. | Framework quality policy; S8 |
| TECH-08 | Handling errors | Validate arguments with appropriate supported APIs. Handle exceptions where recovery or approved boundary translation is possible. Preserve the original stack on rethrow. Do not silently swallow failures. | Adapted guidance; S9 |
| TECH-09 | Implementing asynchronous operations | Use async and await for asynchronous I/O. Return awaitable tasks except where event-handler signatures require async void. Avoid blocking with Wait or Result. Preserve reviewed contracts and cancellation semantics. | Adapted guidance; S10 |
| TECH-10 | Designing reusable local APIs | Apply current Microsoft library guidance inside approved boundaries. Local properties and events do not authorize property-like service operations or forbidden event publishers. | Scoped guidance; S7; Method constraints |
| TECH-11 | Configuring builds | Enable SDK analyzers, nullable checks, and build-time style checks. Use the recommended analysis mode for the pinned SDK. Make warnings fail the quality gate. Record diagnostic decisions. | Framework quality policy; S4, S11 |
| TECH-12 | Enforcing naming and formatting | Configure EditorConfig naming rules and explicit build severity for IDE1006. Run dotnet format with --verify-no-changes in addition to builds and tests. | Framework quality policy; S3, S12 |
| TECH-13 | Changing diagnostic configuration | Do not weaken rules, add blanket suppressions, mark owned code generated, or alter SDK/build settings to make work pass. Route justified exceptions through the responsible architect with QA review and revision-bound evidence. | Owner enforcement policy; S4 explains configuration mechanics |
| TECH-14 | Refreshing technical guidance | Recheck official sources at baseline creation, planned SDK upgrades, and pattern changes. Record review date and impact. Obtain Solution Architect approval for baseline changes. | Framework maintenance policy; S5, S6 |

Use `private readonly IClock clock;` and `this.clock = clock;`. Use unprefixed camelCase static fields and PascalCase constants. External API names and overrides that cannot be changed require a recorded compatibility decision; workers cannot use compatibility as a blanket exemption.

## Templates and controls

Adopt the [EditorConfig template](../templates/dotnet/.editorconfig) and [build-policy template](../templates/dotnet/Directory.Build.props) through the [adoption procedure](../templates/dotnet/README.md). They are reusable framework artifacts, not installed application settings.

`AnalysisLevel=latest` selects analyzers available in the pinned SDK. It does not fetch a future SDK. `AnalysisMode=Recommended` selects a Microsoft rule set rather than enabling every rule indiscriminately. Use explicit diagnostic severities and inspect configuration precedence. Some style preferences are not automatically build checks. Formatting, tests, and semantic reviews remain necessary. See S4 and S11.

The Solution Architect owns the technical baseline. The Application Architect owns detailed realization. QA reviews diagnostic exceptions and process quality. Protect EditorConfig, build properties, SDK selection, analyzer versions, generator inputs, and suppressions from worker amendment. The independent gate must assess effective settings, including nested files, project overrides, and command-line overrides. These documents do not deploy permissions or an independent gate.

## Verification

An isolated fixture using stable SDK 10.0.403 compiled an unprefixed `count` field with zero warnings and errors. `_count`, `s_count`, `m_count`, and `__count` each failed with IDE1006. This validates those field cases under that SDK, not every identifier or future tool version. No application target framework changed.

## Official sources

All sources below were checked on 2026-11-07. Review relevant sections again when adopting or upgrading a baseline. Do not infer that every linked API or recommendation has been exhaustively audited.

- S1: [Common C# conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions).
- S2: [Identifier naming](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/identifier-names).
- S3: [EditorConfig naming rules](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/style-rules/naming-rules).
- S4: [Code analysis configuration](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/configuration-options).
- S5: [C# language-version configuration](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/configure-language-version).
- S6: [SDK selection with global.json](https://learn.microsoft.com/en-us/dotnet/core/tools/global-json).
- S7: [Framework design guidelines](https://learn.microsoft.com/en-us/dotnet/standard/design-guidelines/).
- S8: [Nullable reference types](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/null-safety/nullable-reference-types).
- S9: [Exception practices](https://learn.microsoft.com/en-us/dotnet/standard/exceptions/best-practices-for-exceptions).
- S10: [Asynchronous programming scenarios](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/async-scenarios).
- S11: [SDK build properties](https://learn.microsoft.com/en-us/dotnet/core/project-sdk/msbuild-props).
- S12: [dotnet format](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-format).
