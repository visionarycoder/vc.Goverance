---
metadata-version: "1.0.0"
title: "Existing method-tracing evidence"
description: "Preserve historical findings from the owner-identified proxy example."
document-type: "research"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Existing method-tracing evidence

**Current availability, 2026-11-08:** the owner removed the reference directory and earlier selected sample copies. This record preserves historical review findings. [Sources and bibliography](../sources.md) lists external source locations. No local source copy is supplied.

Read-only review on 2026-11-07. The owner-supplied directory was absent. A sibling repository named vc.App.Latimessis was found, along with service-proxy infrastructure in vc.Ifx. Neither repository was modified. This is an in-repository review record; no external filesystem document links are needed to understand the findings.

| Inspected item | Finding | SHA-256 |
| --- | --- | --- |
| LoggingInterceptor.cs | vc.Ifx: Ifx.Proxy.Interceptor/LoggingInterceptor.cs records request type, scope/correlation, elapsed time, cancellation, and exceptions. It explicitly avoids payload logging. | `b54c9bf073a8867a96053b6ed50b24a483488f5144488d3ac6e466c098eabe3d` |
| LoggingInterceptor.cs | vc.Ifx: Ifx.Proxy.Interceptor/Logging/LoggingInterceptor.cs records proxy-operation start, elapsed duration, success/failure, cancellation, and exceptions. It does not implement arbitrary private-method instrumentation. | `f38b037988143b0b90adf06b3c3db333d8a4c94ec957c8823c53d8512464a773` |
| Ifx.Generators.csproj | vc.App.Latimessis: Ifx.Generators.csproj declares netstandard2.0. No generator source was found under that project directory in the inspected checkout. | `df6c9f6ca1e7b911978fbe052f9ca468c52ad553c26ab5ebbded30001eb3aa3f` |

Latimessis also contains LoggerMessage-attributed partial logging methods in its worker code. That demonstrates generated logging helpers, not attribute-only method-body tracing. The owner subsequently identified the intended experimental example; see the confirmed reference below. These observations are not a code-quality audit or execution test.

The [method-tracing pattern](../patterns/method-io-tracing.md) records the owner capability and implementation limitations. It distinguishes source generation from build-time transformation and preserves the existing [proxy scope](../patterns/component-proxies.md). No sibling source was copied, refactored, built, or executed.

## Confirmed owner reference

The owner identified the experimental Proxies example. The selected in-repository snapshot (source copy removed from this repository) is now the intended implementation reference. Earlier vc.Ifx observations above are supplementary findings, not the reference the owner meant. Original external source files were not changed or executed.

| Examined behavior | Evidence | Consequence for PAT-011 |
| --- | --- | --- |
| DI-resolved interceptor chain | Registration (source copy removed from this repository) | Preserve explicit registration and injectable chain collaborators |
| Named input values and context | MethodContext (source copy removed from this repository) and proxy (source copy removed from this repository) | Generate method identity and typed argument capture without reflected invocation |
| Started, Completed, and Failed status | StatusInterceptor (source copy removed from this repository) | Preserve lifecycle and correlation; define cancellation distinctly in the new detailed design |
| Timing and debug completion logging | TelemetryInterceptor (source copy removed from this repository) | Retain useful timing and diagnostic behavior |
| Completion exposes result type only | StatusInterceptor (source copy removed from this repository) | Add returned-value capture to fulfill the new method I/O requirement |
| Name-based argument redaction | RedactionInterceptor (source copy removed from this repository) | Use as evidence for a reviewed value-projection design, not proof of complete sensitive-data coverage |
| Status sink failures are contained | StatusInterceptor (source copy removed from this repository) | Test that tracing failures do not replace the observed method's outcome |
| DispatchProxy, MethodInfo.Invoke, and reflective async adaptation | BoundaryProxy (source copy removed from this repository) | Do not reuse that dispatch mechanism under the no-reflection proxy constraint |
| Interface-bound interception | BoundaryProxy (source copy removed from this repository) | Private methods and internal self-calls require method-body instrumentation, not merely this proxy |

This was a targeted source review, not a build, runtime test, or whole-directory audit. Selected files were copied as reference evidence and checksummed; no application or original experimental source was modified.
