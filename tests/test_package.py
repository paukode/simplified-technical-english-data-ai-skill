"""The skill folder must load in Claude, Codex, Kiro, and Whisper Studio.

The rules come from the Agent Skills specification (agentskills.io), from the
skill loaders of these agents, and from the repository rules in AGENTS.md.
"""

import re
import unittest

from _support import REFERENCES, REPO, SKILL

ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
# Whisper Studio rewrites these bare relative paths to absolute paths.
WHISPER_REL_REF = re.compile(r"(?<![\w/.])((?:scripts|references|assets)/[\w./\-]+)")
EM_DASH = chr(0x2014)
TEXT_SUFFIXES = {".md", ".py", ".sh", ".txt", ".yaml", ".yml", ".json", ".toml", ""}


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, "SKILL.md must start with YAML front matter"
    data, current = {}, None
    for line in m.group(1).splitlines():
        if line.startswith("  ") and current:
            key, _, value = line.strip().partition(":")
            data[current][key.strip()] = value.strip()
            continue
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if value:
            data[key] = value
            current = None
        else:
            data[key] = {}
            current = key
    return data, text[m.end():]


class SkillPackage(unittest.TestCase):
    def setUp(self):
        self.text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.meta, self.body = frontmatter(self.text)

    def test_front_matter_keys(self):
        self.assertTrue(set(self.meta) <= ALLOWED_KEYS, set(self.meta) - ALLOWED_KEYS)

    def test_name(self):
        name = self.meta["name"]
        self.assertRegex(name, r"^[a-z0-9]+(-[a-z0-9]+)*$")
        self.assertLessEqual(len(name), 64)
        self.assertEqual(name, SKILL.name, "the name must match the folder name")

    def test_description(self):
        d = self.meta["description"]
        self.assertTrue(1 <= len(d) <= 1024, len(d))
        self.assertNotRegex(d, r"[<>]")
        self.assertNotIn(": ", d, "a colon and a space can break simple YAML parsers")

    def test_compatibility_and_metadata(self):
        self.assertLessEqual(len(self.meta["compatibility"]), 500)
        for key, value in self.meta["metadata"].items():
            self.assertRegex(value, r'^".*"$', f"metadata value {key} must be a quoted string")

    def test_body_size(self):
        self.assertLess(len(self.text.splitlines()), 500)

    def test_file_references_exist(self):
        refs = set(re.findall(r"`((?:references|scripts|assets)/[^`\s]+)`", self.body))
        self.assertGreater(len(refs), 20)
        for ref in refs:
            with self.subTest(ref=ref):
                self.assertTrue((SKILL / ref).exists())

    def test_whisper_path_rewrite_finds_real_paths(self):
        for ref in WHISPER_REL_REF.findall(self.body):
            with self.subTest(ref=ref):
                self.assertTrue((SKILL / ref).exists(), "Whisper Studio would rewrite this path to a missing file")

    def test_each_terms_file_and_examples_file_is_listed(self):
        for folder in ("terms", "examples"):
            for path in (REFERENCES / folder).glob("*.md"):
                with self.subTest(file=path.name):
                    self.assertIn(f"references/{folder}/{path.name}", self.body)

    def test_codex_metadata(self):
        text = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn("display_name:", text)
        self.assertIn("short_description:", text)

    def test_only_skill_files_in_the_skill_folder(self):
        allowed_top = {"SKILL.md", "LICENSE.txt", "agents", "assets", "references", "scripts"}
        names = {p.name for p in SKILL.iterdir() if p.name not in {"__pycache__", ".DS_Store"}}
        self.assertEqual(names - allowed_top, set())


class RepositoryText(unittest.TestCase):
    def test_no_em_dash(self):
        for path in REPO.rglob("*"):
            if ".git" in path.parts or "dist" in path.parts or not path.is_file():
                continue
            if path.suffix not in TEXT_SUFFIXES:
                continue
            with self.subTest(file=str(path.relative_to(REPO))):
                self.assertNotIn(EM_DASH, path.read_text(encoding="utf-8", errors="replace"))


if __name__ == "__main__":
    unittest.main()
