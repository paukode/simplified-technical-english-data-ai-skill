import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from _support import SKILL, check, checker_module, rules

SCRIPT = SKILL / "scripts" / "ste_check.py"


class LengthRules(unittest.TestCase):
    def test_instruction_limit_is_20_words(self):
        long_step = "Restart " + " ".join(["the service"] * 10) + "."
        self.assertIn("P1", rules(check(long_step)))
        self.assertNotIn("P1", rules(check("Restart the service on the primary node.")))

    def test_description_limit_is_25_words(self):
        words = "The job reads data from the source table and writes the result to the target table"
        twenty_two = words + " for each day of the week at noon."
        self.assertNotIn("D1", rules(check(twenty_two)))
        self.assertIn("D1", rules(check(words + " " + words + ".")))

    def test_auto_mode_uses_the_limit_of_the_sentence_type(self):
        text = "The job reads the data from the source table and writes it to the target table in the warehouse each hour."
        self.assertEqual(rules(check(text, "descriptive"), "error"), [])
        self.assertIn("P1", rules(check(text, "procedural")))

    def test_condition_then_command_is_an_instruction(self):
        m = checker_module()
        sent = "If the job fails, restart the job."
        self.assertTrue(m.Checker(m.Vocabulary.load()).is_instruction(sent, m.tokens(sent)))

    def test_paragraph_limit_counts_sentences_not_labels(self):
        seven = " ".join(["The job reads the table."] * 7)
        self.assertIn("D2", rules(check(seven)))
        labels = "**T7.** Write the date. Write the time: \"14:30 UTC\". Write the unit: \"5 GB\"."
        self.assertNotIn("D2", rules(check(labels)))

    def test_numbers_with_units_count_as_one_word(self):
        m = checker_module()
        self.assertEqual(m.count_words("Set the limit to 300 ms."), 5)
        self.assertEqual(m.count_words("Use 2 vCPU and 512 MiB (the minimum)."), 5)


class GrammarRules(unittest.TestCase):
    def test_semicolon_and_contraction(self):
        r = rules(check("Stop the job; then don't restart it."))
        self.assertIn("T1", r)
        self.assertIn("S3", r)

    def test_perfect_tense_is_an_error(self):
        self.assertIn("V2", rules(check("The job has failed.")))
        self.assertIn("V2", rules(check("The team has deployed the release.")))
        self.assertIn("V2", rules(check("The data has been loaded.")))

    def test_possession_with_an_adjective_is_not_a_perfect_tense(self):
        self.assertNotIn("V2", rules(check("The table has nested fields.")))

    def test_progressive_form_is_an_error(self):
        self.assertIn("V3", rules(check("The consumer is reading the topic.")))

    def test_ing_words_in_technical_names_are_permitted(self):
        self.assertNotIn("V3", rules(check("The streaming job uses load balancing and partitioning.")))
        self.assertNotIn("V3", rules(check("The file is missing.")))
        self.assertIn("V3", rules(check("Run the command after checking the logs.")))

    def test_modal_verbs(self):
        self.assertIn("V4", rules(check("You should rotate the key.")))
        self.assertIn("V4", rules(check("The query may fail.")))
        self.assertIn("V4", rules(check("The test could fail."), "warning"))
        self.assertNotIn("V4", rules(check("The release is in May 2026.")))

    def test_rfc_keywords_only_in_a_specification(self):
        req = "DC-01: The producer SHOULD send the data before 06:00 UTC."
        self.assertIn("V4", rules(check(req, "procedural")))
        self.assertNotIn("V4", rules(check(req, "specification")))
        marker = "This document uses the keywords of RFC 2119.\n\n" + req
        self.assertNotIn("V4", rules(check(marker, "auto")))
        self.assertIn("V4", rules(check("The producer should send the data.", "specification")))
        self.assertIn("R1", rules(check("The producer SHALL send the data.", "specification")))

    def test_passive_voice(self):
        self.assertIn("V5", rules(check("The file is uploaded by the job.")))
        self.assertIn("V5", rules(check("The bucket must be encrypted.")))
        self.assertIn("V5", rules(check("It is recommended that you rotate the key.")))
        self.assertNotIn("V5", rules(check("The bucket is encrypted.")))
        self.assertNotIn("V5", rules(check("The replica can be read-only.")))

    def test_make_sure_that(self):
        self.assertIn("S2", rules(check("Make sure the file is available.")))
        self.assertNotIn("S2", rules(check("Make sure that the file is available.")))


class WordRules(unittest.TestCase):
    def test_phrasal_verbs_and_jargon(self):
        r = check("Set up the cluster and spin up a new instance in prod.")
        self.assertIn("V7", rules(r))
        self.assertIn("W9", rules(r))
        messages = " ".join(f["message"] for f in r.findings)
        self.assertIn("configure", messages)

    def test_a_technical_name_protects_its_words(self):
        self.assertNotIn("W10", rules(check("Edit the launch template of the Auto Scaling group.")))
        self.assertIn("W10", rules(check("Launch the job.")))

    def test_former_product_name(self):
        r = check("Add the user to Azure AD.")
        self.assertIn("W8", rules(r))
        self.assertIn("Microsoft Entra ID", " ".join(f["message"] for f in r.findings))

    def test_vague_words(self):
        self.assertIn("W13", rules(check("Increase the memory as needed, etc.")))

    def test_human_qualities_for_models_only(self):
        self.assertIn("M1", rules(check("The model thinks that the answer is correct.")))
        self.assertIn("M1", rules(check("The agent decided to delete the files.")))
        self.assertNotIn("M1", rules(check("The on-call engineer knows the procedure.")))

    def test_unknown_words(self):
        r = check("Restart the frobnicator.")
        self.assertIn("frobnicator", r.unknown)
        self.assertEqual(rules(r, "error"), [])
        self.assertIn("W1", rules(check("Restart the frobnicator.", strict=True), "error"))

    def test_comparative_forms_and_plurals(self):
        r = check("The new index is larger than the old index. The queries are faster.", strict=True)
        self.assertEqual(r.findings, [])

    def test_identifiers_quotes_and_code_are_not_checked(self):
        text = (
            "Load `stg_frobnicate` and fact_orders_daily into the table.\n\n"
            "```bash\nkubectl rollout undo deployment/frob -n prod\n```\n\n"
            "Click \"Frobnicate now\". Open https://example.com/frob and ~/.config/frob.yaml."
        )
        self.assertEqual(check(text, strict=True).findings, [])

    def test_extra_terms_file(self):
        m = checker_module()
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "ste-terms.md"
            p.write_text("# Terms\n\n- frobnicator, Frob Platform (FP)\n\nFROBNICATE (v) [frobnicates, frobnicated, frobnicated]\n")
            vocab = m.Vocabulary.load([p])
            r = m.Checker(vocab, strict=True).check_text("Frobnicate the frobnicator on the Frob Platform.", "t")
            self.assertEqual(r.findings, [])


class CommandLine(unittest.TestCase):
    def run_script(self, args, stdin=None, cwd=None):
        env = dict(os.environ)
        env.pop("STE_TERMS", None)
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args], input=stdin, capture_output=True,
            text=True, cwd=cwd, env=env,
        )

    def test_exit_status(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(self.run_script([], "Restart the service.\n", cwd=d).returncode, 0)
            self.assertEqual(self.run_script([], "You should restart it.\n", cwd=d).returncode, 1)
            self.assertEqual(self.run_script(["missing-file.md"], cwd=d).returncode, 2)

    def test_json_output_and_line_numbers(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "doc.md"
            p.write_text("# Title\n\nRestart the service.\n\nYou should stop the job.\n")
            out = self.run_script(["--format", "json", str(p)], cwd=d)
            data = json.loads(out.stdout)
            self.assertEqual(data["result"]["errors"], 1)
            self.assertTrue(data["findings"][0]["location"].endswith(":5"))

    def test_reads_ste_terms_from_the_current_folder(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d, "ste-terms.md").write_text("- frobnicator\n")
            out = self.run_script(["--strict"], "Restart the frobnicator.\n", cwd=d)
            self.assertEqual(out.returncode, 0, out.stdout)


if __name__ == "__main__":
    unittest.main()
