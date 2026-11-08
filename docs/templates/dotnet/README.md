---
metadata-version: "1.0.0"
title: "C# technical-policy templates"
description: "Define controlled adoption of reusable C# quality-policy templates."
document-type: "index"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# C# technical-policy templates

These templates implement the [technical standard](../../standards/microsoft-technical-standard.md), including the owner's no-underscore-prefix rule. They do not select an application technology stack.

1. Have the Solution Architect approve the stable SDK, target framework, language compatibility, analyzers, and scope.
2. Create a controlled application global.json with the approved SDK, preview exclusion, and roll-forward policy. Do not use LangVersion=latest.
3. Merge [.editorconfig](.editorconfig) and [Directory.Build.props](Directory.Build.props) into that baseline. Preserve stronger compatible controls. Review nested configuration and property precedence.
4. Restore approved dependencies, build relevant configurations, run the Test Architect's tests, and run `dotnet format <solution-or-project> --verify-no-changes`.
5. Test compliant and violating naming, including static fields, constants, and externally imposed names. Record compatibility decisions.
6. Protect the configuration and run checks under the independent integration identity. Workers cannot lower severity, change the SDK, or add suppressions to pass their own work.

The templates deliberately omit a target framework and SDK version. Recommended analyzers resolve against the pinned SDK. Warnings-as-errors is an adopted framework quality policy, not a claim that Microsoft requires it universally. Review mixed-language and legacy solutions before adopting this modern C# props template.

Original references and their sample files remain unchanged. Derived application implementations must satisfy the current approved technical baseline.
