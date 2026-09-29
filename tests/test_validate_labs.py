import tempfile
import unittest
from pathlib import Path

from scripts.validate_labs import validate_file


VALID = """---
lab:
  title: 'Summarize support tickets with Python'
  description: 'Count synthetic support tickets by priority.'
  duration: 15
  level: 300
  islab: true
  status: in-development
  targetDate: '2026-09-29'
---
# Summarize support tickets with Python

This exercise should take approximately **15** minutes to complete.

In this exercise, you will summarize synthetic ticket data.

## Scenario

You support a service desk. Summarize its tickets to prioritize work.

## Prior knowledge

Basic Python.

## Summarize the tickets

1. Open the supplied files.
"""


class ValidateLabsTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.path = self.root / "Instructions" / "Exercises" / "01-tickets.md"
        self.path.parent.mkdir(parents=True)

    def check(self, text):
        self.path.write_text(text, encoding="utf-8")
        return validate_file(self.path, self.root)

    def test_valid_exercise(self):
        self.assertEqual([], self.check(VALID))

    def test_invalid_dates(self):
        for value in ("'2099-01-0'", "'2026-02-30'", "2026-09-29"):
            with self.subTest(value=value):
                self.assertTrue(self.check(VALID.replace("'2026-09-29'", value)))

    def test_boolean_duration_is_not_an_integer(self):
        self.assertTrue(self.check(VALID.replace("duration: 15", "duration: true")))

    def test_mismatched_title(self):
        self.assertTrue(self.check(VALID.replace("# Summarize support tickets", "# Count tickets")))

    def test_misplaced_duration(self):
        self.assertTrue(self.check(VALID.replace(
            "This exercise should take", "An extra paragraph.\n\nThis exercise should take"
        )))

    def test_required_sections(self):
        self.assertTrue(self.check(VALID.replace("## Prior knowledge", "## Prerequisites")))

    def test_local_links(self):
        asset = self.root / "Labfiles" / "data.csv"
        asset.parent.mkdir()
        asset.write_text("priority\nhigh\n", encoding="utf-8")
        self.assertEqual([], self.check(VALID + "\n[Data](../../Labfiles/data.csv)\n"))
        self.assertTrue(self.check(VALID + "\n[Data](../../Labfiles/missing.csv)\n"))
        self.assertTrue(self.check(VALID + "\n[Outside](../../../outside.csv)\n"))

    def test_code_examples_are_not_headings_or_links(self):
        self.assertEqual([], self.check(VALID + "\n```python\n#### comment\n'[x](missing.txt)'\n```\n"))

    def test_author_comments(self):
        self.assertTrue(self.check(VALID + "\n<!-- replace this -->\n"))

    def test_setup_sections(self):
        setup = """## Before you start

### Environment

### Tools

### Exercise assets

### Verify your setup

"""
        self.assertEqual([], self.check(VALID.replace("## Summarize", setup + "## Summarize")))
        self.assertTrue(self.check(VALID.replace(
            "## Summarize", setup.replace("### Tools", "### Requirements") + "## Summarize"
        )))

    def test_shared_setup_has_no_lab_metadata_requirement(self):
        self.path = self.path.with_name("00-setup.md")
        self.assertEqual([], self.check("# Configure the shared environment\n\n1. Check Python.\n"))

    def test_invalid_yaml(self):
        self.assertTrue(self.check(VALID.replace("  level: 300", "  level: [")))


if __name__ == "__main__":
    unittest.main()
