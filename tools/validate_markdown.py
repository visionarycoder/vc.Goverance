"""Validate the repository's scalar YAML frontmatter and Markdown conventions."""

from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote


SCHEMA_PATH = Path(__file__).resolve().parents[1] / "docs/standards/markdown-frontmatter.schema.json"
SKILL_SCHEMA_PATH = SCHEMA_PATH.with_name("skill-frontmatter.schema.json")
EXCLUDED_DIRECTORIES = {".git", ".venv", "node_modules", "__pycache__"}
LINK = re.compile(r"\[[^\]]*\]\((<[^>]+>|[^)\n]+)\)")
AMBIGUOUS = re.compile(r"\band/or\b|\bas needed\b|\bas appropriate\b|\bwhere appropriate\b|\betc\.", re.I)
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD)\b")


def issue(path: Path, line: int, rule: str, message: str) -> dict:
    return {"path": str(path), "line": line, "rule": rule, "message": message}


def parse_frontmatter(text: str) -> tuple[dict, str, int]:
    """Read the documented YAML subset: lowercase keys and JSON scalar values."""
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("Place the opening --- delimiter on line 1, without a BOM.")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValueError("Add the closing --- delimiter.") from error
    metadata = {}
    for number, line in enumerate(lines[1:end], 2):
        match = re.fullmatch(r"([a-z][a-z0-9-]*):\s*(.+)", line)
        if not match:
            raise ValueError(f"Line {number}: use a lowercase kebab-case key and a JSON scalar value.")
        key, raw = match.groups()
        if key in metadata:
            raise ValueError(f"Line {number}: duplicate key {key}.")
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as error:
            raise ValueError(f"Line {number}: double-quote string values; YAML aliases and complex values are not supported.") from error
        if isinstance(value, (dict, list)):
            raise ValueError(f"Line {number}: metadata values must be scalars.")
        metadata[key] = value
    body = "\n".join(lines[end + 1 :])
    if body.lstrip().startswith("---"):
        raise ValueError("Use one frontmatter block, followed by the document heading.")
    return metadata, body, end + 2


def metadata_errors(metadata: dict, schema: dict) -> list[str]:
    errors = []
    properties = schema["properties"]
    for key in schema["required"]:
        if key not in metadata:
            errors.append(f"Missing required key {key}.")
    for key, value in metadata.items():
        if key not in properties:
            errors.append(f"Unknown metadata key {key}.")
            continue
        rule = properties[key]
        if not isinstance(value, str):
            errors.append(f"{key} must be a string.")
            continue
        if "const" in rule and value != rule["const"]:
            errors.append(f"{key} must equal {rule['const']}.")
        if "enum" in rule and value not in rule["enum"]:
            errors.append(f"{key} is not an allowed value.")
        if "pattern" in rule and not re.search(rule["pattern"], value):
            errors.append(f"{key} does not match its required pattern.")
        if len(value.strip()) < rule.get("minLength", 0):
            errors.append(f"{key} must contain nonblank text.")
        if len(value) > rule.get("maxLength", sys.maxsize):
            errors.append(f"{key} exceeds its maximum length.")
        if rule.get("format") == "date":
            try:
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                    raise ValueError
                date.fromisoformat(value)
            except ValueError:
                errors.append(f"{key} must be a real ISO date in YYYY-MM-DD format.")
    return errors


def content_lines(body: str):
    fence = None
    for number, line in enumerate(body.splitlines()):
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None and not line.startswith(("    ", "\t")):
            yield number, line


def validate_file(path: Path, root: Path, schema: dict) -> list[dict]:
    errors = []
    try:
        metadata, body, offset = parse_frontmatter(path.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError) as error:
        return [issue(path, 1, "frontmatter", str(error))]
    relative = path.relative_to(root)
    is_skill = (len(relative.parts) == 4 and relative.parts[:2] == (".agents", "skills")
                and relative.name == "SKILL.md")
    active_schema = json.loads(SKILL_SCHEMA_PATH.read_text(encoding="utf-8")) if is_skill else schema
    errors.extend(issue(path, 1, "metadata", message) for message in metadata_errors(metadata, active_schema))
    if is_skill and metadata.get("name") != path.parent.name:
        errors.append(issue(path, 1, "metadata", "The skill name must match its directory name."))
    headings = []
    for number, line in content_lines(body):
        location = offset + number
        if line.startswith("# "):
            headings.append(line[2:].strip())
        for match in LINK.finditer(line):
            target = unquote(match.group(1).strip("<>"))
            if target.startswith(("https://", "http://", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            if re.match(r"(?:[A-Za-z]:|/|\\|file:)", target):
                errors.append(issue(path, location, "link", "Use a repository-relative document path."))
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                errors.append(issue(path, location, "link", f"Missing or out-of-repository target: {target}"))
        if line.startswith("|"):
            continue  # Preserve source-derived rules, titles, and reference tables.
        prose = re.sub(r"`[^`]*`", "", line)
        prose = LINK.sub("", prose)
        if PLACEHOLDER.search(prose):
            errors.append(issue(path, location, "ste", "Replace the unresolved placeholder with an explicit question or required decision."))
        if AMBIGUOUS.search(prose):
            errors.append(issue(path, location, "ste", "Name the condition, scope, or action instead of using an open-ended phrase."))
    if len(headings) != 1:
        errors.append(issue(path, offset, "heading", "Use exactly one level-one document heading."))
    elif not is_skill and metadata.get("title") != headings[0]:
        errors.append(issue(path, offset, "heading", "The metadata title must match the level-one heading."))
    return errors


def markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() == ".md"
                  and not EXCLUDED_DIRECTORIES.intersection(p.relative_to(root).parts))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    files = markdown_files(args.root)
    errors = [error for path in files for error in validate_file(path, args.root, schema)]
    if not files:
        errors.append(issue(args.root, 0, "inventory", "No Markdown files were found."))
    report = {"files_checked": len(files), "errors": errors, "passed": not errors,
              "limits": "Checks the scalar YAML profile, metadata, headings, local file targets, and selected prose phrases. Does not prove semantic clarity, validate remote URLs or fragments, or grant approval."}
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    for error in errors:
        print(f"{error['path']}:{error['line']}: {error['rule']}: {error['message']}")
    print(f"Checked {len(files)} Markdown files; {len(errors)} errors.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
