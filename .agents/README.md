---
metadata-version: "1.0.0"
title: "Repository-local agent skills"
description: "Route documentation tasks to focused skills within vc.Governance."
document-type: "index"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Repository-local agent skills

These skills support governance documentation in this repository. They use the existing Method standards, role hierarchy, artifact contracts, and approval routes. They do not instantiate leadership roles, authenticate approvals, enforce worker isolation, or authorize changes in sibling repositories.

The root [agent instructions](../AGENTS.md) remain the repository instructions. No nested override is required.

| Task | Skill |
| --- | --- |
| Write lifecycle, gate, feedback, and handoff documentation | [document-agentic-workflows](skills/document-agentic-workflows/SKILL.md) |
| Maintain artifact contracts, field descriptions, and fictional examples | [document-governance-artifacts](skills/document-governance-artifacts/SKILL.md) |
| Record decision context and adopted approval structure | [record-governance-decisions](skills/record-governance-decisions/SKILL.md) |
| Review Method fidelity, authority, and cross-document consistency | [review-agentic-workflow-docs](skills/review-agentic-workflow-docs/SKILL.md) |

Invoke a skill by its name, such as `$document-agentic-workflows`, in a client that discovers repository-local skills. Automatic selection depends on the client's skill support. If a skill is not discovered, read its linked instructions directly; do not claim it was installed globally.

Keep each skill focused on its documented task. Reference governing files instead of copying their rules into a competing source of truth. Skills use the [skill frontmatter profile](../docs/standards/markdown-authoring.md); other Markdown keeps the repository document profile.

From the repository root, run:

```text
python tools/validate_markdown.py
python -m unittest discover -s tests -p test_markdown_validation.py
```

These checks validate format, links, selected wording, and validator behavior. Review source fidelity and authority separately.
