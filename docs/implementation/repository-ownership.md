---
metadata-version: "1.0.0"
title: "Framework and implementation ownership"
description: "Assign governance and implementation artifacts to their distinct repositories."
document-type: "governance-policy"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Framework and implementation ownership

**Owner decision:** 2026-11-07. Implement reusable technical mechanisms in the repository named `vc.Ifx`. This repository, `vc.Governance`, remains responsible for The Method, leadership authority, development process, and required implementation constraints.

## Responsibilities

| Artifact or responsibility | Owning repository |
| --- | --- |
| Source authority, Method rules, role hierarchy, decision rights, lifecycle, and project controls | vc.Governance |
| Required proxy behavior, tracing capability, technical quality constraints, and acceptance obligations | vc.Governance |
| Reusable Roslyn analyzers, code fixes, generators, and build-time instrumentation | vc.Ifx |
| Reusable DI-capable proxies, interceptor infrastructure, diagnostic sinks, and registrations | vc.Ifx |
| Executable tests and package delivery for those reusable mechanisms | vc.Ifx |
| Application business requirements, component contracts, detailed designs, and approved adoption | The consuming application repository |
| Protected integration and permission provisioning | The selected execution platform, under the approved governance design |

Keep requirements and authority here; place detailed tooling design, implementation plans, source code, and executable verification for reusable mechanisms in vc.Ifx. Do not treat a local reference snapshot as a second production implementation. Source evidence and rule identifiers remain available here for traceability.

## Technical handoff

The following existing specifications are inputs to vc.Ifx detailed design and implementation:

- [Current Microsoft technical standard](../standards/microsoft-technical-standard.md) and [TECH records](../standards/technical-rules.json): coding and quality constraints, including unprefixed names.
- [Mandatory component proxies](../patterns/component-proxies.md) and [PROXY records](../standards/proxy-rules.json): DI-capable component boundaries, generated typed local proxies, no reflection-based proxies, and Dapr as an accepted service-invocation realization.
- [Attributed method I/O tracing](../patterns/method-io-tracing.md) and [TRACE records](../standards/tracing-rules.json): automatic diagnostics across method accessibilities, with the generator-versus-transformation decision still requiring detailed design.
- [Pattern catalog](../patterns/README.md): remaining reusable techniques, with each pattern's adoption status preserved.
- [Enforcement boundaries](enforcement-boundaries.md): independent integration and protection against worker amendment.

Use these stable identifiers in tooling requirements, diagnostics, tests, and verification evidence. The vc.Ifx design must map existing projects and capabilities before creating new ones. Reuse suitable existing mechanisms. Do not infer that every catalog pattern is mandatory, that all business/UI code belongs in vc.Ifx, or that implementing an analyzer establishes permission enforcement.

The Solution Architect remains accountable for technical boundaries. The Application Architect creates the detailed tooling design; the Test Architect defines verification; the Project Manager plans and assigns the work. Unresolved design choices remain visible until the correct owner decides them.

## Current state

This decision establishes repository ownership. It does not claim that a generator, source transformation, proxy, or independent integration gate has been delivered. Application adoption remains subject to its reviewed requirements and designs. Reusable mechanism implementation work continues in vc.Ifx; process and governance work continues here.
