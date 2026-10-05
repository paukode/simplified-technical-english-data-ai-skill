import re
import unittest

from _support import REFERENCES, checker_module, vocabulary

ENTRY = re.compile(r"^([A-Z][A-Z' .-]*?)\s+\(([a-z]+)\)(?:\s+\[([^\]]*)\])?\s*$")
NO_FORMS = {"BE", "CAN", "MUST", "WILL"}


def entries(path):
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ENTRY.match(line.strip())
        if m:
            out.append((m.group(1), m.group(2), m.group(3)))
    return out


class CoreVocabulary(unittest.TestCase):
    def test_entries_are_sorted_and_unique(self):
        items = entries(REFERENCES / "core-vocabulary.md")
        self.assertGreater(len(items), 500)
        keys = [(h, p) for h, p, _ in items]
        self.assertEqual(len(keys), len(set(keys)))
        heads = [h.replace(" ", "") for h, _, _ in items]
        self.assertEqual(heads, sorted(heads))

    def test_verbs_have_three_forms_and_no_ing_form(self):
        for path in (REFERENCES / "core-vocabulary.md", REFERENCES / "technical-verbs.md"):
            for head, pos, forms in entries(path):
                with self.subTest(word=head):
                    if forms:
                        self.assertFalse(any(f.strip().endswith("ing") for f in forms.split(",")))
                    if pos == "v" and head not in NO_FORMS:
                        self.assertIsNotNone(forms)
                        self.assertGreaterEqual(len(forms.split(",")), 3 if head != "CAN" else 2)

    def test_technical_verbs_are_not_core_verbs(self):
        core = {h for h, p, _ in entries(REFERENCES / "core-vocabulary.md") if p == "v"}
        tech = {h for h, _, _ in entries(REFERENCES / "technical-verbs.md")}
        self.assertEqual(core & tech, set())


class Consistency(unittest.TestCase):
    def test_substitutions_do_not_forbid_permitted_words(self):
        v = vocabulary()
        conflicts = []
        for items in v._subs.values():
            for seq, form, _rep, _rule in items:
                if len(seq) == 1 and seq[0] in v.words:
                    conflicts.append(f"{form} (word)")
                if seq in v._terms.get(seq[0], []):
                    conflicts.append(f"{form} (technical name)")
        self.assertEqual(conflicts, [])

    def test_rule_ids_in_substitutions_and_examples_exist(self):
        rules_text = (REFERENCES / "writing-rules.md").read_text(encoding="utf-8")
        defined = set(re.findall(r"^\*\*([A-Z]\d+)\.\*\*", rules_text, re.M))
        self.assertGreater(len(defined), 50)
        cited = set(re.findall(r"\|\s*([A-Z]\d+)\s*\|", (REFERENCES / "substitutions.md").read_text(encoding="utf-8")))
        for path in (REFERENCES / "examples").glob("*.md"):
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.startswith("Changes:"):
                    cited |= set(re.findall(r"\b([A-Z]\d+)\b", line))
        self.assertEqual(cited - defined, set())

    def test_terms_files_parse(self):
        m = checker_module()
        for path in sorted((REFERENCES / "terms").glob("*.md")):
            with self.subTest(file=path.name):
                v = m.Vocabulary()
                v.load_terms(path)
                self.assertGreater(sum(len(x) for x in v._terms.values()), 100)
                for line in path.read_text(encoding="utf-8").splitlines():
                    if line.startswith("- "):
                        for item in line[2:].split(", "):
                            self.assertTrue(item.strip(), "empty item")
                            self.assertEqual(item.count("("), item.count(")"), item)


if __name__ == "__main__":
    unittest.main()
