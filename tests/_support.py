"""Shared helpers for the tests. The tests use only the standard library."""

import importlib.util
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL = REPO / "skills" / "ste-data-ai"
REFERENCES = SKILL / "references"

_module = None
_vocab = None


def checker_module():
    global _module
    if _module is None:
        spec = importlib.util.spec_from_file_location("ste_check", SKILL / "scripts" / "ste_check.py")
        _module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_module)
    return _module


def vocabulary():
    global _vocab
    if _vocab is None:
        _vocab = checker_module().Vocabulary.load()
    return _vocab


def check(text, mode="auto", strict=False):
    m = checker_module()
    return m.Checker(vocabulary(), mode, strict=strict).check_text(text, "t")


def rules(report, level=None):
    return [f["rule"] for f in report.findings if level is None or f["level"] == level]


EXAMPLE = re.compile(
    r"^## (?P<title>.+?)\n.*?^Type: (?P<type>\w+)\n.*?^Before:\n\n~~~text\n(?P<before>.*?)\n~~~\n.*?"
    r"^After:\n\n~~~text\n(?P<after>.*?)\n~~~\n",
    re.S | re.M,
)
MODES = {"procedure": "procedural", "description": "descriptive", "specification": "specification", "mixed": "auto"}
