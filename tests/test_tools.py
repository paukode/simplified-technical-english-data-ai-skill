import os
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from _support import REPO

INSTALL = REPO / "tools" / "install.py"
BUILD = REPO / "tools" / "build.py"


def run(script, args, home):
    env = dict(os.environ, HOME=str(home))
    env.pop("CLAUDE_CONFIG_DIR", None)
    env.pop("WHISPER_USER_DIR", None)
    return subprocess.run([sys.executable, str(script), *args], capture_output=True, text=True, env=env)


class Installer(unittest.TestCase):
    TARGET_DIRS = [".claude/skills", ".agents/skills", ".kiro/skills", ".whisper/skills"]

    def test_install_update_and_uninstall_all_targets(self):
        with tempfile.TemporaryDirectory() as home:
            home = Path(home)
            out = run(INSTALL, ["all"], home)
            self.assertEqual(out.returncode, 0, out.stderr)
            for d in self.TARGET_DIRS:
                skill = home / d / "ste-data-ai"
                self.assertTrue((skill / "SKILL.md").is_file(), d)
                self.assertTrue((skill / "scripts" / "ste_check.py").is_file(), d)
                self.assertFalse((skill / "tests").exists())
            self.assertEqual(run(INSTALL, ["all"], home).returncode, 0)
            out = run(INSTALL, ["--uninstall", "all"], home)
            self.assertEqual(out.returncode, 0, out.stderr)
            for d in self.TARGET_DIRS:
                self.assertFalse((home / d / "ste-data-ai").exists(), d)

    def test_link_mode(self):
        with tempfile.TemporaryDirectory() as home:
            home = Path(home)
            self.assertEqual(run(INSTALL, ["--link", "codex"], home).returncode, 0)
            dest = home / ".agents" / "skills" / "ste-data-ai"
            self.assertTrue(dest.is_symlink())
            self.assertEqual(dest.resolve(), (REPO / "skills" / "ste-data-ai").resolve())
            self.assertEqual(run(INSTALL, ["codex"], home).returncode, 0)
            self.assertFalse(dest.is_symlink())

    def test_does_not_replace_a_different_folder(self):
        with tempfile.TemporaryDirectory() as home:
            home = Path(home)
            other = home / ".claude" / "skills" / "ste-data-ai"
            other.mkdir(parents=True)
            (other / "SKILL.md").write_text("---\nname: something-else\ndescription: x\n---\n")
            self.assertEqual(run(INSTALL, ["claude"], home).returncode, 1)
            self.assertEqual(run(INSTALL, ["--uninstall", "claude"], home).returncode, 1)
            self.assertIn("something-else", (other / "SKILL.md").read_text())

    def test_project_install(self):
        with tempfile.TemporaryDirectory() as home, tempfile.TemporaryDirectory() as project:
            out = run(INSTALL, ["--project", project, "all"], Path(home))
            self.assertEqual(out.returncode, 0, out.stderr)
            for d in (".claude/skills", ".agents/skills", ".kiro/skills"):
                self.assertTrue((Path(project) / d / "ste-data-ai" / "SKILL.md").is_file(), d)
            self.assertIn("Whisper Studio", out.stdout)


class Build(unittest.TestCase):
    def test_zip(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "skill.zip"
            self.assertEqual(run(BUILD, ["zip", "-o", str(out)], Path(d)).returncode, 0)
            names = zipfile.ZipFile(out).namelist()
            self.assertIn("ste-data-ai/SKILL.md", names)
            self.assertIn("ste-data-ai/scripts/ste_check.py", names)
            self.assertFalse(any("__pycache__" in n or n.startswith("tests/") for n in names))

    def test_prompt_with_fields(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "prompt.md"
            r = run(BUILD, ["prompt", "--fields", "aws,genai", "--examples", "-o", str(out)], Path(d))
            self.assertEqual(r.returncode, 0, r.stderr)
            text = out.read_text(encoding="utf-8")
            self.assertNotIn("name: ste-data-ai", text)
            self.assertIn("## File: references/writing-rules.md", text)
            self.assertIn("## File: references/terms/cloud-aws.md", text)
            self.assertIn("## File: references/examples/generative-ai.md", text)
            self.assertNotIn("references/terms/cloud-azure.md\n", text)

    def test_prompt_rejects_an_unknown_field(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertNotEqual(run(BUILD, ["prompt", "--fields", "mainframe"], Path(d)).returncode, 0)


if __name__ == "__main__":
    unittest.main()
