import re
import unittest

from _support import EXAMPLE, MODES, REFERENCES, REPO, SKILL, check


class Examples(unittest.TestCase):
    def test_each_example_file_parses(self):
        files = sorted((REFERENCES / "examples").glob("*.md"))
        self.assertGreaterEqual(len(files), 13)
        for path in files:
            text = path.read_text(encoding="utf-8")
            headings = re.findall(r"^## ", text, re.M)
            found = list(EXAMPLE.finditer(text))
            with self.subTest(file=path.name):
                self.assertGreaterEqual(len(found), 4)
                self.assertEqual(len(found), len(headings), "each heading must be one complete example")
                for m in found:
                    self.assertIn(m.group("type"), MODES)

    def test_after_obeys_the_rules_and_before_does_not(self):
        for path in sorted((REFERENCES / "examples").glob("*.md")):
            for m in EXAMPLE.finditer(path.read_text(encoding="utf-8")):
                mode = MODES[m.group("type")]
                with self.subTest(file=path.name, example=m.group("title")):
                    after = check(m.group("after"), mode, strict=True)
                    self.assertEqual(
                        after.findings, [], "\n".join(f"{f['rule']} {f['message']}" for f in after.findings)
                    )
                    before = check(m.group("before"), mode)
                    self.assertTrue(before.findings or before.unknown, "the Before text must show problems")


class SkillTextObeysItsOwnRules(unittest.TestCase):
    FILES = [
        SKILL / "SKILL.md",
        REFERENCES / "writing-rules.md",
        REFERENCES / "document-patterns.md",
        REFERENCES / "substitutions.md",
        REPO / "README.md",
        REPO / "AGENTS.md",
    ]

    def test_strict_check_is_clean(self):
        for path in self.FILES:
            with self.subTest(file=path.name):
                r = check(path.read_text(encoding="utf-8"), strict=True)
                self.assertEqual(r.findings, [], "\n".join(f"{f['location']} {f['rule']} {f['message']}" for f in r.findings))

    def test_example_files_have_no_errors_or_warnings(self):
        for path in sorted((REFERENCES / "examples").glob("*.md")):
            with self.subTest(file=path.name):
                r = check(path.read_text(encoding="utf-8"))
                self.assertEqual(r.findings, [])


if __name__ == "__main__":
    unittest.main()
