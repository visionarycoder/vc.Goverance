---
metadata-version: "1.0.0"
title: "Attribute-driven method I/O tracing"
description: "Define attributed method I/O tracing requirements and unresolved implementation choices."
document-type: "implementation-constraint"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Attribute-driven method I/O tracing

**Pattern:** PAT-011. **Authority:** explicit human-owner requirement on 2026-11-07. **Scope:** attributed methods of any accessibility, including public, internal, and private. This is method-body instrumentation, distinct from the mandatory proxy boundary between components. It does not require proxies between internal collaborators.

## Standard Technical English requirements

| ID | Condition | Required behavior |
| --- | --- | --- |
| TRACE-01 | A method has the designated tracing attribute | Automatically provide debugging statements for method inputs and outputs. Do not require handwritten tracing statements in each method. |
| TRACE-02 | Selecting methods for instrumentation | Include public, internal, and private methods. Do not restrict tracing to service contracts or proxy entry points. |
| TRACE-03 | Entering an instrumented method | Capture the declared input values once, subject to the reviewed value-projection policy. Do not evaluate caller arguments again. |
| TRACE-04 | Completing an instrumented method | Capture the returned value and successful ref/out results where applicable. For void methods, record completion without inventing a result. |
| TRACE-05 | Completing asynchronous work | Observe logical completion, failure, or cancellation. Do not report a returned Task or ValueTask object as the completed output. Do not consume a ValueTask twice. |
| TRACE-06 | Leaving through failure or cancellation | Record the agreed outcome and preserve the original failure, cancellation semantics, and stack information. Do not replace the outcome with a logging result. |
| TRACE-07 | Dispatching to the method body | Use explicit typed code. Do not use a reflection-based proxy, runtime reflection dispatch, or runtime-generated proxy to supply instrumentation. |
| TRACE-08 | Generating instrumentation | Preserve accessibility, signatures, business behavior, argument evaluation, and return semantics. Diagnose unsupported attributed methods rather than silently omitting them. |
| TRACE-09 | Connecting diagnostics | Use the approved logging abstraction and DI-compatible instance wiring. Define static-method logging explicitly; do not introduce hidden service-location calls into business code. |
| TRACE-10 | Emitting debug values | Apply the reviewed enablement and value-projection policy before formatting. Do not implicitly enumerate lazy results, invoke arbitrary getters, or serialize whole object graphs. |

TRACE-01 and TRACE-02 express the owner-selected capability. The remaining items define proposed correctness and verification constraints for its detailed design. The attribute name, event schema, sink, enablement policy, supported method forms, and build integration remain design decisions. No new application stack is selected.

## Roslyn constraint and proposed realization

A normal incremental source generator adds source; it cannot insert statements into an existing handwritten method body. Microsoft's LoggerMessage generator creates attributed partial logging methods. It does not automatically wrap arbitrary business methods. See [Roslyn generator design](https://github.com/dotnet/roslyn/blob/main/docs/features/source-generators.md) and [Microsoft generated logging](https://learn.microsoft.com/en-us/dotnet/core/extensions/logging/source-generation), checked 2026-11-07.

For the requested attribute-only experience on existing method bodies, the proposed realization is a build-time Roslyn source-instrumentation task. It reads the semantic model, creates instrumented compilation copies, and supplies those copies to compilation while leaving authored files unchanged. It is a separate build transformation, not an ordinary IIncrementalGenerator. Roslyn's [syntax-transformation APIs](https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/get-started/syntax-transformation) provide the transformation mechanisms, not a ready-made tracing tool. This realization requires detailed architectural review before implementation.

An ordinary generator can instead generate an instrumented method around an explicitly separated implementation body, using a reviewed partial/wrapper convention. That alternative changes the authoring model and must not be presented as transparent instrumentation of an unchanged method. A service proxy alone cannot cover private methods and self-calls inside the target.

Do not choose experimental call-site interceptors or a third-party rewriting package implicitly. Do not mistake a generated logging helper for proof that every attributed method actually calls it.

## Detailed-design decisions

- Attribute identity and permitted settings; define parameter/result exclusions and bounded value projections.
- Logging level and build/runtime enablement; debug-level logging and DEBUG-only compilation are different choices.
- Event identity, method identity, input/output names, correlation, completion/failure/cancellation records, and nested-call handling.
- Synchronous, async, static, generic, overloaded, expression-bodied, recursive, virtual, and interface method treatment.
- Ref/out, ref returns, ref structs, pointers, iterators, async iterators, and async-void support or explicit diagnostics. Iteration completion is different from returning an enumerable.
- Instance logger wiring and a deliberate static-method strategy without hidden service location.
- Diagnostic-sink failures, disabled-logging overhead, source mappings, debugger stepping, deterministic outputs, incremental build invalidation, and compatibility with other generators.
- Preservation of compiled analyzer checks and approved build settings; neither the worker nor generated-code markers may bypass required architectural verification.

The Application Architect owns the detailed mechanism within Solution Architect bounds. The Test Architect owns coverage and runtime equivalence tests. The Project Manager accounts for the transformation, generator interaction, diagnostics, and integration work.

## Verification required before delivery

Test actual entry, normal output, exception, and cancellation records for public, internal, and private methods. Include private self-calls, early returns, overloads, generics, nested calls, and asynchronous completion. Verify that inputs and business bodies execute once and that instrumentation does not change results, ref/out state, exception behavior, or lazy enumeration. Exercise disabled tracing, value exclusions, logger failures, static wiring, deterministic rebuilds, source mapping, and every claimed supported method form. An unsupported attributed form must yield a useful diagnostic.

No tracing generator, source-instrumentation task, runtime sink, or enforcement analyzer has been implemented by this pattern document. See the [existing-code review](../research/method-tracing-review.md) and [current technical standard](../standards/microsoft-technical-standard.md).

## Confirmed reference behavior

Use the owner's experimental proxy snapshot (source copy removed from this repository) as the implementation reference. Preserve its DI-resolved interceptor-chain concept, named input capture, correlation, lifecycle records, timing, and diagnostic-sink failure isolation where applicable. Replace DispatchProxy and runtime reflection with typed generated calls or reviewed build-time method instrumentation. Extend completion capture from result type to actual approved result values. Extend service-boundary observation to attributed private methods and internal self-calls. The reference does not by itself satisfy those additional requirements.

## Implementation location

The owner assigned reusable implementation mechanisms and their detailed tooling design to vc.Ifx. Keep required behavior, Method constraints, and adoption status here. See [repository ownership and handoff](../implementation/repository-ownership.md). The location decision is resolved; remaining mechanism decisions belong in the vc.Ifx design effort.
