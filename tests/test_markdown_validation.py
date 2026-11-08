"""Check Markdown metadata and link rejection cases."""

import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from validate_markdown import SCHEMA_PATH, markdown_files, metadata_errors, parse_frontmatter, validate_file


class MarkdownValidationTests(unittest.TestCase):
    def setUp(self):
        self.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.metadata = {
            "metadata-version": "1.0.0",
            "title": "Example document",
            "description": "Describe an example document.",
            "document-type": "governance-policy",
            "repository": "vc.Governance",
            "language": "Standard Technical English",
            "updated": "2026-11-08",
        }

    def document(self, body="# Example document\n\nState the required action.\n"):
        return "---\n" + "\n".join(f"{k}: {json.dumps(v)}" for k, v in self.metadata.items()) + "\n---\n\n" + body

    def validate(self, body):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "example.md"
            path.write_text(self.document(body), encoding="utf-8")
            return validate_file(path, root, self.schema)

    def test_valid_document(self):
        self.assertEqual(self.validate("# Example document\n\nName the responsible owner.\n"), [])

    def test_missing_header(self):
        with self.assertRaises(ValueError):
            parse_frontmatter("# No metadata\n")

    def test_header_must_start_at_line_one(self):
        with self.assertRaises(ValueError):
            parse_frontmatter("\n" + self.document())

    def test_unclosed_header(self):
        with self.assertRaises(ValueError):
            parse_frontmatter('---\ntitle: "Unclosed"\n')

    def test_duplicate_key(self):
        with self.assertRaises(ValueError):
            parse_frontmatter(self.document().replace('title: "Example document"', 'title: "Example document"\ntitle: "Duplicate"'))

    def test_unknown_key(self):
        self.metadata["approved"] = "true"
        self.assertTrue(metadata_errors(self.metadata, self.schema))

    def test_uppercase_markdown_extension(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "UPPER.MD"
            path.write_text(self.document(), encoding="utf-8")
            self.assertEqual(markdown_files(root), [path])

    def test_wrong_document_type(self):
        self.metadata["document-type"] = "unknown-category"
        self.assertTrue(metadata_errors(self.metadata, self.schema))

    def test_bom_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_frontmatter("\ufeff" + self.document())

    def test_missing_required_description(self):
        del self.metadata["description"]
        self.assertTrue(metadata_errors(self.metadata, self.schema))

    def test_empty_description(self):
        self.metadata["description"] = "   "
        self.assertTrue(metadata_errors(self.metadata, self.schema))

    def test_invalid_date(self):
        self.metadata["updated"] = "2026-02-30"
        self.assertTrue(metadata_errors(self.metadata, self.schema))

    def test_unsupported_version(self):
        self.metadata["metadata-version"] = "2.0.0"
        self.assertTrue(metadata_errors(self.metadata, self.schema))

    def test_wrong_repository(self):
        self.metadata["repository"] = "vc.Ifx"
        self.assertTrue(metadata_errors(self.metadata, self.schema))

    def test_complex_yaml_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_frontmatter('---\ntitle: ["One", "Two"]\n---\n')

    def test_alias_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_frontmatter('---\ntitle: *other\n---\n')

    def test_duplicate_frontmatter_block(self):
        with self.assertRaises(ValueError):
            parse_frontmatter(self.document('---\ntitle: "Second"\n---\n'))

    def test_heading_mismatch(self):
        self.assertTrue(self.validate("# Wrong title\n"))

    def test_multiple_document_headings(self):
        self.assertTrue(self.validate("# Example document\n\n# Another title\n"))

    def test_missing_local_link(self):
        self.assertTrue(self.validate("# Example document\n\n[Missing](missing.md)\n"))

    def test_outside_repository_link(self):
        self.assertTrue(self.validate("# Example document\n\n[Outside](../outside.md)\n"))

    def test_absolute_local_link(self):
        self.assertTrue(self.validate("# Example document\n\n[Outside](E:/outside.md)\n"))

    def test_remote_link_is_not_fetched(self):
        self.assertEqual(self.validate("# Example document\n\n[Source](https://example.invalid/source)\n"), [])

    def test_unresolved_placeholder(self):
        self.assertTrue(self.validate("# Example document\n\nTBD: select the owner.\n"))

    def test_open_ended_prose(self):
        self.assertTrue(self.validate("# Example document\n\nReview the code as needed.\n"))

    def test_code_and_source_tables_preserve_terms(self):
        body = "# Example document\n\n```text\n# Example code\nTODO\n```\n\n| Source | Text |\n| --- | --- |\n| Rule | Review as needed. |\n"
        self.assertEqual(self.validate(body), [])

    def validate_skill(self, metadata=None, body="# Example skill\n\nName the responsible owner.\n", location=None):
        metadata = metadata if metadata is not None else {
            "name": "example-skill", "description": "Maintain example workflow documents."
        }
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / (location or ".agents/skills/example-skill/SKILL.md")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("---\n" + "\n".join(f"{k}: {json.dumps(v)}" for k, v in metadata.items())
                            + "\n---\n\n" + body, encoding="utf-8")
            return validate_file(path, root, self.schema)

    def test_valid_skill_profile(self):
        self.assertEqual(self.validate_skill(), [])

    def test_skill_profile_cannot_bypass_document_metadata(self):
        self.assertTrue(self.validate_skill(location="docs/example.md"))

    def test_skill_missing_description(self):
        self.assertTrue(self.validate_skill({"name": "example-skill"}))

    def test_skill_name_must_match_directory(self):
        self.assertTrue(self.validate_skill({"name": "other-skill", "description": "Describe the task."}))

    def test_skill_invalid_name(self):
        self.assertTrue(self.validate_skill({"name": "Example--Skill", "description": "Describe the task."}))

    def test_skill_blank_description(self):
        self.assertTrue(self.validate_skill({"name": "example-skill", "description": " "}))

    def test_skill_unknown_authority_field(self):
        self.assertTrue(self.validate_skill({"name": "example-skill", "description": "Describe the task.",
                                             "approved": "true"}))

    def test_skill_links_and_prose_are_checked(self):
        errors = self.validate_skill(body="# Example skill\n\nReview as needed. [Missing](missing.md)\n")
        self.assertEqual({error["rule"] for error in errors}, {"link", "ste"})

    def test_skill_requires_one_heading(self):
        self.assertTrue(self.validate_skill(body="State the required action.\n"))


if __name__ == "__main__":
    unittest.main()
