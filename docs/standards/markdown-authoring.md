---
metadata-version: "1.0.0"
title: "Markdown authoring and validation"
description: "Define Markdown metadata, Standard Technical English conventions, and validation."
document-type: "standard"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Markdown authoring and validation

Use this contract for every Markdown file in vc.Governance. It governs document structure and wording. It does not change Method rules, role authority, or the approval state of an artifact.

## Required frontmatter

Put one YAML frontmatter block at the start of each file. Use lowercase kebab-case keys. Use JSON double-quoted strings as YAML scalar values. This restricted YAML profile has no lists, nested objects, aliases, tags, comments, or multiline values. It allows deterministic validation with the Python standard library.

```yaml
---
metadata-version: "1.0.0"
title: "Document title"
description: "State the document's purpose in one sentence."
document-type: "governance-policy"
repository: "vc.Governance"
language: "Standard Technical English"
updated: "2026-11-08"
---

# Document title
```

| Key | Required content |
| --- | --- |
| metadata-version | The exact metadata contract version |
| title | The single level-one heading, with identical text |
| description | One short sentence that states the document's purpose |
| document-type | An allowed category from the schema |
| repository | vc.Governance |
| language | Standard Technical English |
| updated | The actual edit date in YYYY-MM-DD format |

Use the [metadata schema](markdown-frontmatter.schema.json) as the field contract. Do not add unknown owners, approval states, review dates, or status claims. Metadata identifies a document. It does not authorize its content. Keep the existing heading hierarchy, source locators, rule identifiers, and code blocks after the header.

## Skill entrypoint frontmatter

Only `.agents/skills/<skill-name>/SKILL.md` uses the skill profile. Other Markdown, including the skill catalog, keeps the seven-field document profile above. This format supports repository-local skill discovery without adding unsupported document keys to skill headers.

```yaml
---
name: "document-agentic-workflows"
description: "Create or revise governance workflow documentation in vc.Governance."
---

# Document agentic workflows
```

The [skill metadata schema](skill-frontmatter.schema.json) requires a nonblank name and description. The name must match the directory, contain at most 64 characters, and use lowercase letters, digits, and single separating hyphens. Descriptions contain at most 1024 characters and no angle brackets. Use only these two fields and the same double-quoted scalar syntax. Each skill body has exactly one level-one heading; it does not need to match the machine-readable name. Link and prose checks still apply.

This is a document-format distinction. It does not change Method rules, approval authority, or validation coverage. The repository validator selects the profile by file location; a normal document cannot opt out by adding a skill name.

## Standard Technical English

1. State the actor when responsibility could be unclear. Use the exact role name from the decision matrix.
2. Put a condition before its required action. Name the affected artifact or scope.
3. Use short sentences. Give each instruction one main action.
4. Use active verbs. Replace abstract phrases with the action the reader must perform.
5. Use one term for one concept. Preserve the book's technical terms and define abbreviations in context or link to their definition.
6. Preserve obligation strength. A directive is non-waivable. A guideline retains its source classification and human-owner departure route. Do not change `may` or `should` into `must` merely to simplify a sentence.
7. Replace open-ended wording with the controlling criterion. For example, name the approved impact assessment instead of saying `as needed`.
8. State an unresolved decision explicitly. Name the responsible owner and hold only dependent work. Do not use `TODO` or `TBD` as a final requirement.
9. Separate established requirements, owner decisions, proposals, and historical findings. Identify missing source copies as historical evidence.
10. Preserve formulas, thresholds, exceptions, examples, and printed source locators. Shorter wording must retain the same meaning.

The Project Manager assigns work. The Solution Architect owns system and project design. The Application Architect owns detailed component design. The Test Architect owns test design. The Product Owner owns business meaning. The CEO and human owner retain the decision rights stated in the [approval matrix](../governance/decision-and-approval-matrix.md). Do not replace these roles with an unspecified approver.

Source-derived tables can contain qualified guidance. Preserve a qualifier that carries source meaning. Explain its governing condition in the surrounding text rather than turning advice into an absolute rule. Original source titles and quoted code also retain their meaning.

## Run validation

Use Python 3.10 or later. From the repository root, run:

```text
python tools/validate_markdown.py
python -m unittest discover -s tests -p test_markdown_validation.py
```

To save the current result:

```text
python tools/validate_markdown.py --report docs/research/markdown-validation.json
```

The validator scans Markdown files, including files hidden by Git ignore rules. It excludes Git internals and dependency/cache directories. It checks frontmatter placement, allowed fields and values, dates, duplicate keys, the document heading, local file targets, unresolved placeholders, and selected open-ended prose phrases. Code blocks, inline code, and source tables are excluded from prose checks. Link checks still apply to tables.

The validator returns a nonzero exit code on failure. It does not correct files, change authority, verify remote URLs or link fragments, or prove that every sentence is unambiguous. A qualified reviewer must check meaning and source fidelity. Python validation here is documentation maintenance; reusable runtime enforcement remains in its separately owned repository.

Adding or editing frontmatter changes file bytes. Apply the [approval-validity policy](../governance/change-approval-validity.md) to any operational approval that references the changed document. Metadata does not transfer approval to the revised file.
