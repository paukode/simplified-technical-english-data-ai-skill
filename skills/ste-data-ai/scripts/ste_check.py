#!/usr/bin/env python3
"""Check text against the writing rules of the ste-data-ai skill.

The script finds the errors that a program can find: sentence length,
paragraph length, verb forms, helping verbs, passive voice, contractions,
semicolons, phrasal verbs and jargon, human qualities for models and agents,
and words that are not in the vocabulary. It cannot find all errors. It does
not know the meaning of a sentence, and it cannot tell if a word has its
narrow meaning. A person must also read the text.

Usage:
    python3 ste_check.py [options] [FILE ...]
    cat draft.md | python3 ste_check.py --mode procedural

Options:
    --mode auto|procedural|descriptive|specification   (default: auto)
    --terms FILE      Read more technical names from FILE. You can repeat it.
    --strict          Report each word that is not in the vocabulary as an error.
    --no-vocabulary   Do not compare words with the vocabulary.
    --format text|json

The script also reads technical names from `ste-terms.md` in the current
folder, and from each file in the STE_TERMS environment variable.

Exit status: 0 = no errors, 1 = one or more errors, 2 = usage error.
The script needs Python 3.8 or later and no other packages.
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REFERENCES = SKILL_DIR / "references"
PROJECT_TERMS = "ste-terms.md"

LIMITS = {"procedural": 20, "descriptive": 25, "specification": 25}
PARAGRAPH_LIMIT = 6

ING_CORE = {"during", "existing", "incoming", "missing", "outgoing", "pending", "remaining"}
ING_NOT_VERB = {
    "anything", "bring", "ceiling", "everything", "king", "nothing", "ping", "ring",
    "sing", "something", "spring", "sting", "string", "swing", "thing", "wing",
}
MODALS = {"should", "would", "may", "might", "shall", "ought"}
RFC_MARKER = re.compile(r"\b(?:RFC\s?2119|RFC\s?8174|BCP\s?14)\b")
PREFIXES = {
    "anti", "auto", "bi", "co", "cross", "de", "inter", "intra", "micro", "mid", "multi",
    "non", "post", "pre", "re", "self", "semi", "sub", "super", "un",
}
MODEL_SUBJECTS = {
    "model", "models", "llm", "llms", "slm", "agent", "agents", "subagent", "subagents",
    "assistant", "assistants", "chatbot", "chatbots", "ai", "bot", "bots", "orchestrator",
    "claude", "gpt", "gemini", "llama", "copilot", "codex", "kiro",
}
CONDITION_WORDS = {"if", "when", "before", "after", "while", "until", "unless"}
NOT_IMPERATIVE = {"be", "can", "have", "must", "will"}
NOTICE_WORDS = {"warning", "caution", "note", "important", "step"}

# Past participles for the perfect-tense and passive-voice checks.
PARTICIPLE = (
    r"(?:[a-z]+ed|been|become|begun|bent|bound|broken|brought|built|bought|caught|chosen|come|"
    r"cut|done|drawn|driven|fallen|fed|felt|forgotten|found|frozen|given|gone|got|gotten|"
    r"grown|heard|held|hidden|hung|kept|known|laid|led|left|lit|lost|made|meant|met|"
    r"overridden|overwritten|paid|put|read|rebuilt|rerun|reset|run|said|seen|sent|set|"
    r"shaken|shown|shut|sold|spent|split|spread|spun|stolen|struck|stuck|taken|taught|"
    r"thought|thrown|told|torn|understood|undone|withdrawn|won|worn|written)"
)
PERFECT = re.compile(
    r"\b(?:has|have|had|having)\s+(?:not\s+|already\s+|just\s+|never\s+|also\s+|"
    r"recently\s+|always\s+)?(" + PARTICIPLE + r")\b(?!-)\s*([^\s,.;:!?)]*)",
    re.IGNORECASE,
)
PROGRESSIVE = re.compile(
    r"\b(?:am|is|are|was|were|be|been|being|isn['’]t|aren['’]t|wasn['’]t|weren['’]t)\s+"
    r"(?:not\s+|still\s+|currently\s+|now\s+|also\s+|always\s+)?([a-z]+ing)\b(?!-)",
    re.IGNORECASE,
)
PASSIVE_BY = re.compile(
    r"\b(?:is|are|was|were|be|been|being|get|gets|got)\s+(?:[a-z]+ly\s+)?"
    r"(" + PARTICIPLE + r")\s+by\b",
    re.IGNORECASE,
)
MODAL_PASSIVE = re.compile(
    r"\b(?:can|cannot|could|must|will|should|would|may|might|shall)\s+(?:not\s+)?"
    r"(?:[a-z]+ly\s+)?be\s+(" + PARTICIPLE + r")\b(?!-)",
    re.IGNORECASE,
)
IMPERSONAL = re.compile(
    r"\bit\s+(?:is|was)\s+(?:[a-z]+ly\s+)?(" + PARTICIPLE + r")\s+that\b", re.IGNORECASE
)
CONTRACTION = re.compile(
    r"\b[a-z]+n['’]t\b|\b[a-z]+['’](?:re|ll|ve|m|d)\b|"
    r"\b(?:it|that|there|what|let|who|here|he|she|where|how)['’]s\b",
    re.IGNORECASE,
)
MAKE_SURE = re.compile(r"\b(?:make|makes|made)\s+sure\b(?!\s+that\b)", re.IGNORECASE)

# Words that follow a participle when "has/have/had" is a helping verb.
# A noun after the participle usually means possession plus an adjective:
# "the table has nested fields" is correct.
OBJECT_START = {
    "a", "an", "the", "this", "these", "that", "those", "its", "their", "our", "your", "all",
    "each", "some", "any", "no", "to", "in", "on", "at", "for", "from", "with", "by", "into",
    "of", "over", "after", "before", "since", "during", "because", "it", "them", "you", "we",
    "they", "him", "her", "me", "us", "not", "yet", "already", "twice", "again", "code",
    "quoted", "url",
}

UNIT = (
    r"(?:%|ms|µs|us|ns|s|sec|min|h|hr|hrs|d|B|KB|MB|GB|TB|PB|KiB|MiB|GiB|TiB|PiB|bps|Kbps|"
    r"Mbps|Gbps|vCPUs?|RPUs?|DPUs?|OCUs?|RUs?|IOPS|QPS|RPS|TPM|RPM|x)"
)
NUMBER = re.compile(r"(?<![\w.$€£])[$€£]?\d[\d,]*(?:\.\d+)?(?:\s?" + UNIT + r")?(?![\w])")

TOKEN = re.compile(r"\.?[A-Za-z0-9][A-Za-z0-9_.+#@/&'’-]*")
TRAILING = ".-/'’&@_"
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
LIST_ITEM = re.compile(r"^(?:[-*+]|\d+[.)])\s+(.*)$")
RULE_LINE = re.compile(r"^(?:-{3,}|\*{3,}|_{3,})$")
SPLIT = re.compile(r"(?<=[.!?:])\s+(?=[A-Z0-9\"“'(\[])")
FULL_STOP = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"“'(\[])")
ENTRY = re.compile(r"^([A-Z][A-Z' .-]*?)\s+\(([a-z]+(?:,\s*[a-z]+)*)\)(?:\s+\[([^\]]*)\])?\s*$")
BULLET = re.compile(r"^\s*[-*]\s+(.*\S)\s*$")
ALIAS = re.compile(r"^(.*\S)\s*\(([^()]*)\)$")


def tokens(text):
    """Return (token, start, end) for each word-like token in text."""
    out = []
    for m in TOKEN.finditer(text):
        tok, end = m.group(0), m.end()
        while tok and tok[-1] in TRAILING:
            tok, end = tok[:-1], end - 1
        if tok:
            out.append((tok, m.start(), end))
    return out


def norm(tok):
    t = tok.lower().replace("’", "'")
    return t[:-2] if t.endswith("'s") else t


def plurals(word):
    if not word or not word[-1].isalpha():
        return []
    out = [word + "s"]
    if word.endswith(("s", "x", "z", "ch", "sh")):
        out.append(word + "es")
    if len(word) > 1 and word.endswith("y") and word[-2] not in "aeiou":
        out.append(word[:-1] + "ies")
    return out


class Vocabulary:
    """The permitted words, technical names, substitutions, and model words."""

    def __init__(self):
        self.words = set()
        self.verb_bases = set()
        self._terms = {}
        self._subs = {}
        self.model_words = {}

    @classmethod
    def load(cls, extra_terms=()):
        v = cls()
        v.load_entries(REFERENCES / "core-vocabulary.md")
        v.load_entries(REFERENCES / "technical-verbs.md")
        for path in sorted((REFERENCES / "terms").glob("*.md")):
            v.load_terms(path)
        for path in extra_terms:
            v.load_terms(path)
        v.load_substitutions(REFERENCES / "substitutions.md")
        v.finish()
        return v

    # Loading -----------------------------------------------------------

    def add_entry(self, head, pos, forms):
        head = head.lower()
        self.words.update(head.split())
        self.words.add(head)
        if "v" in pos:
            self.verb_bases.add(head.split()[0])
        for form in (forms or "").split(","):
            form = form.strip().lower()
            if form:
                self.words.add(form)
                self.words.update(form.split())
        if "n" in pos and " " not in head:
            self.words.update(plurals(head))

    def add_term(self, item):
        item = item.strip().rstrip(".")
        if not item:
            return
        names = [item]
        m = ALIAS.match(item)
        if m:
            names = [m.group(1), m.group(2)]
        for name in names:
            toks = tuple(norm(t) for t, _, _ in tokens(name))
            if not toks:
                continue
            variants = {toks} | {toks[:-1] + (p,) for p in plurals(toks[-1])}
            for var in variants:
                self._terms.setdefault(var[0], set()).add(var)
                if len(var) == 1:
                    self.words.add(var[0])

    def _lines(self, path):
        in_comment = False
        for line in Path(path).read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if in_comment:
                in_comment = "-->" not in s
                continue
            if s.startswith("<!--"):
                in_comment = "-->" not in s
                continue
            yield line, s

    def load_entries(self, path):
        for _line, s in self._lines(path):
            m = ENTRY.match(s)
            if m:
                self.add_entry(m.group(1), m.group(2), m.group(3))

    def load_terms(self, path):
        for line, s in self._lines(path):
            m = ENTRY.match(s)
            if m:
                self.add_entry(m.group(1), m.group(2), m.group(3))
                continue
            b = BULLET.match(line)
            if b:
                for item in b.group(1).split(", "):
                    self.add_term(item)

    def load_substitutions(self, path):
        header = None
        for _line, s in self._lines(path):
            if not s.startswith("|"):
                header = None
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            if header is None:
                header = cells[0].lower()
                continue
            if len(cells) < 3 or set(cells[0]) <= set("-: "):
                continue
            forms, replacement, rule = cells[0], cells[1], cells[2]
            for form in forms.split(", "):
                seq = tuple(norm(t) for t, _, _ in tokens(form))
                if not seq:
                    continue
                if header.startswith("do not write about"):
                    self.model_words[seq[0]] = (form, replacement, rule)
                elif header == "do not write":
                    self._subs.setdefault(seq[0], []).append((seq, form, replacement, rule))

    def finish(self):
        self._terms = {k: sorted(v, key=len, reverse=True) for k, v in self._terms.items()}
        for k in self._subs:
            self._subs[k].sort(key=lambda item: len(item[0]), reverse=True)

    # Matching ----------------------------------------------------------

    def term_spans(self, norms):
        """Return the (start, end) token ranges of the longest technical names."""
        spans, i = [], 0
        while i < len(norms):
            for cand in self._terms.get(norms[i], ()):
                if tuple(norms[i:i + len(cand)]) == cand:
                    spans.append((i, i + len(cand)))
                    i += len(cand)
                    break
            else:
                i += 1
        return spans

    def substitutions(self, norms):
        """Return (start, end, entry) for each phrase from substitutions.md."""
        found, i = [], 0
        while i < len(norms):
            for entry in self._subs.get(norms[i], ()):
                seq = entry[0]
                if tuple(norms[i:i + len(seq)]) == seq:
                    found.append((i, i + len(seq), entry))
                    i += len(seq)
                    break
            else:
                i += 1
        return found

    def is_known(self, tok):
        """True when the token is permitted, or is not a word to examine."""
        if any(c.isdigit() for c in tok) or tok.isupper() or any(c.isupper() for c in tok[1:]):
            return True
        lw = norm(tok)
        if lw in self.words or len(lw) < 2:
            return True
        parts = [p for p in re.split(r"[-/]", lw) if p]
        if len(parts) > 1:
            return all(
                p in self.words or (k < len(parts) - 1 and p in PREFIXES)
                for k, p in enumerate(parts)
            )
        return not re.fullmatch(r"[a-z']+", lw)


class Report:
    def __init__(self):
        self.findings = []
        self.unknown = {}
        self._seen = set()

    def add(self, level, location, rule, message):
        key = (location, rule, message)
        if key not in self._seen:
            self._seen.add(key)
            self.findings.append(
                {"level": level, "location": location, "rule": rule, "message": message}
            )

    @property
    def errors(self):
        return sum(1 for f in self.findings if f["level"] == "error")

    @property
    def warnings(self):
        return sum(1 for f in self.findings if f["level"] == "warning")


# Text preparation ----------------------------------------------------------


def _mask_snake(m):
    return " CODE " if re.search(r"[A-Za-z0-9]", m.group(0)) else m.group(0)


def mask_inline(s):
    """Replace the parts of a line that the rules do not control.

    Each replacement is one uppercase word. Thus it counts as one word, and the
    vocabulary check ignores it. The replacements never remove a line break.
    """
    s = re.sub(r"<!--.*?-->", " ", s)
    s = re.sub(r"`[^`\n]+`", " CODE ", s)
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<https?://[^>\s]+>", " URL ", s)
    s = re.sub(r"\b[a-z][a-z0-9+.-]*://\S+", " URL ", s)
    s = re.sub(r"\bwww\.\S+", " URL ", s)
    s = re.sub(r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b", " EMAIL ", s)
    s = re.sub(r"\barn:[\w:/.*+=,@-]+", " CODE ", s)
    s = re.sub(r"<[\w.-]+>", " CODE ", s)
    s = re.sub(r"</?[A-Za-z][\w-]*(?:\s[^<>\n]*)?>", " ", s)
    s = re.sub(r"\{\{[^}\n]*\}\}", " CODE ", s)
    s = re.sub(r"\$\{?[A-Za-z_][A-Za-z0-9_]*\}?", " CODE ", s)
    s = re.sub(r"[\"“][^\"”\n]*[\"”]", " QUOTED ", s)
    s = re.sub(r"(?<![\w/.~-])(?:~|\.{1,2})?/[\w.@~-]+(?:/[\w.@~-]*)*", " CODE ", s)
    s = re.sub(r"\b[\w.-]+/[\w./-]*\.[A-Za-z]\w*\b", " CODE ", s)
    s = re.sub(r"(?<![\w-])--?[A-Za-z][\w-]*", " CODE ", s)
    s = re.sub(r"\b\w*_\w*\b", _mask_snake, s)
    s = re.sub(r"\b[a-z][\w-]+(?:\.[\w-]+)+\b", " CODE ", s)
    s = re.sub(r"\*\*|__|\*", " ", s)
    return s


def blocks(text):
    """Yield (line, kind, text) for each prose paragraph and list item.

    The function skips front matter, code blocks, headings, tables, rules,
    and comments.
    """
    lines = text.splitlines()
    start = 0
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() in ("---", "..."):
                start = j + 1
                break
    out, cur, cur_line, cur_kind = [], [], 0, None
    fence, in_comment = None, False

    def flush():
        nonlocal cur, cur_kind
        if cur:
            out.append((cur_line, cur_kind, "\n".join(cur)))
        cur, cur_kind = [], None

    for i in range(start, len(lines)):
        raw = lines[i]
        s = raw.strip()
        if fence:
            if s.startswith(fence):
                fence = None
            continue
        m = FENCE.match(raw)
        if m:
            flush()
            fence = m.group(1)
            continue
        if in_comment:
            in_comment = "-->" not in s
            continue
        if s.startswith("<!--") and "-->" not in s:
            flush()
            in_comment = True
            continue
        if not s or s.startswith(("#", "|")) or RULE_LINE.match(s):
            flush()
            continue
        if s.startswith(">"):
            s = s.lstrip("> ").strip()
            if not s:
                flush()
                continue
        item = LIST_ITEM.match(s)
        if item:
            flush()
            cur, cur_line, cur_kind = [item.group(1)], i + 1, "item"
            continue
        if cur_kind == "item" and raw[:1] in (" ", "\t"):
            cur.append(s)
            continue
        if cur_kind == "item":
            flush()
        if not cur:
            cur_line, cur_kind = i + 1, "para"
        cur.append(s)
    flush()
    return out


def split_sentences(text):
    out, pos = [], 0
    for m in SPLIT.finditer(text):
        out.append((pos, text[pos:m.start()]))
        pos = m.end()
    out.append((pos, text[pos:]))
    return [(o, s) for o, s in out if re.search(r"[A-Za-z]", s)]


def count_words(sentence):
    s = re.sub(r"\([^()]*\)", " PAREN ", sentence)
    s = NUMBER.sub(" NUM ", s)
    return len(tokens(s))


def excerpt(sentence, size=60):
    s = " ".join(sentence.split())
    return s if len(s) <= size else s[: size - 3].rstrip() + "..."


# Checks ----------------------------------------------------------------------


class Checker:
    def __init__(self, vocab, mode="auto", strict=False, vocabulary=True):
        self.vocab = vocab
        self.mode = mode
        self.strict = strict
        self.vocabulary = vocabulary

    def check_text(self, text, name="text", report=None):
        report = report or Report()
        rfc = self.mode == "specification" or (
            self.mode == "auto" and bool(RFC_MARKER.search(text))
        )
        for line, kind, block in blocks(text):
            masked = "\n".join(mask_inline(part) for part in block.split("\n"))
            sentences = split_sentences(masked)
            # A colon ends a part of a sentence for the length check. For the
            # paragraph check, only a full stop, a question mark, or an
            # exclamation mark ends a sentence. Labels such as "T7." do not count.
            real = [s for s in FULL_STOP.split(masked) if count_words(s) > 2]
            if kind == "para" and len(real) > PARAGRAPH_LIMIT:
                report.add(
                    "error", f"{name}:{line}", "D2",
                    f"The paragraph has {len(real)} sentences. The limit is {PARAGRAPH_LIMIT}.",
                )
            for offset, sentence in sentences:
                loc = f"{name}:{line + masked[:offset].count(chr(10))}"
                self.check_sentence(" ".join(sentence.split()), loc, rfc, report)
        return report

    def is_instruction(self, sentence, toks):
        words = [norm(t) for t, _, _ in toks]
        if not words:
            return False
        if words[0] in CONDITION_WORDS:
            comma = sentence.find(",")
            if comma < 0:
                return False
            words = [norm(t) for t, _, _ in tokens(sentence[comma + 1:])]
            if not words:
                return False
        first = words[0]
        second = words[1] if len(words) > 1 else ""
        if (first, second) in (("do", "not"), ("make", "sure")):
            return True
        return first in self.vocab.verb_bases and first not in NOT_IMPERATIVE

    def check_sentence(self, sent, loc, rfc, report):
        toks = tokens(sent)
        if not toks:
            return
        head = excerpt(sent)

        # Length (P1, D1).
        if self.mode == "auto":
            kind = "procedural" if self.is_instruction(sent, toks) else "descriptive"
        else:
            kind = self.mode
        limit = LIMITS[kind]
        n = count_words(sent)
        if n > limit:
            rule = "P1" if kind == "procedural" else "D1"
            what = "an instruction" if kind == "procedural" else "a sentence of this type"
            report.add(
                "error", loc, rule,
                f"The sentence has {n} words. The limit for {what} is {limit}: \"{head}\"",
            )

        # Punctuation and contractions (T1, S3).
        if ";" in sent:
            report.add("error", loc, "T1", f"There is a semicolon. Write two sentences: \"{head}\"")
        m = CONTRACTION.search(sent)
        if m:
            report.add("error", loc, "S3", f"\"{m.group(0)}\" is a contraction. Write the full words.")

        # Verb forms (V2, V3, V5).
        for m in PERFECT.finditer(sent):
            participle, nxt = m.group(1).lower(), m.group(2).lower()
            if participle == "been" or not nxt or nxt[:1].isdigit() or nxt in OBJECT_START or nxt.endswith("ly"):
                report.add(
                    "error", loc, "V2",
                    f"\"{' '.join(m.group(0).split()[:2])}\": do not use \"has\", \"have\", or \"had\" "
                    "as a helping verb. Use the simple past tense.",
                )
        flagged_ing = set()
        for m in PROGRESSIVE.finditer(sent):
            word = m.group(1).lower()
            if word in ING_CORE or word in ING_NOT_VERB:
                continue
            flagged_ing.add(word)
            report.add(
                "error", loc, "V3",
                f"\"{m.group(0)}\" is a progressive form. Use the simple present or the simple past tense.",
            )
        for pattern, text in (
            (PASSIVE_BY, "is the passive voice. Make the agent the subject."),
            (MODAL_PASSIVE, "is the passive voice. Use the imperative, or make the agent the subject."),
            (IMPERSONAL, "is the passive voice. Name the person or the system that does the action."),
        ):
            m = pattern.search(sent)
            if m:
                report.add("error", loc, "V5", f"\"{m.group(0)}\" {text}")

        # Helping verbs (V4, R1).
        for i, (tok, _s, _e) in enumerate(toks):
            lw = tok.lower()
            if lw in MODALS:
                if lw == "may" and tok == "May" and i + 1 < len(toks) and toks[i + 1][0][:1].isdigit():
                    continue
                if rfc and tok.isupper():
                    if lw == "shall":
                        report.add("warning", loc, "R1", "Use MUST, not SHALL.")
                    continue
                note = " In a specification, write the RFC 2119 keyword in uppercase." if tok.isupper() else ""
                report.add(
                    "error", loc, "V4",
                    f"\"{tok}\" is not permitted. Use \"must\", \"can\", or \"will\", or remove it.{note}",
                )
            elif lw == "could":
                report.add("warning", loc, "V4", "Use \"could\" only as the past tense of \"can\".")

        if MAKE_SURE.search(sent):
            report.add("warning", loc, "S2", "Write \"make sure that\". Keep the word \"that\".")

        norms = [norm(t) for t, _, _ in toks]

        # Human qualities for models and agents (M1).
        for i, w in enumerate(norms):
            if w in MODEL_SUBJECTS:
                for j in range(i + 1, min(i + 7, len(norms))):
                    hit = self.vocab.model_words.get(norms[j])
                    if hit:
                        report.add(
                            "warning", loc, "M1",
                            f"\"{toks[j][0]}\" gives a human quality to a model or an agent. Write: {hit[1]}.",
                        )
                        break

        spans = self.vocab.term_spans(norms)
        in_term = [False] * len(toks)
        for a, b in spans:
            for k in range(a, b):
                in_term[k] = True

        # Substitutions (W1, W8, W9, W13, V6, V7).
        for a, b, (_seq, form, replacement, rule) in self.vocab.substitutions(norms):
            if any(sa <= a and b <= sb and (sb - sa) > (b - a) for sa, sb in spans):
                continue
            if rfc and all(t.isupper() for t, _, _ in toks[a:b]):
                continue
            text = " ".join(t for t, _, _ in toks[a:b])
            if replacement.startswith("(") and replacement.endswith(")"):
                advice = replacement[1:-1]
            else:
                advice = f"write {replacement}"
            report.add("warning", loc, rule, f"\"{text}\": {advice}.")

        # "-ing" words outside technical names (V3).
        for k, (tok, _s, _e) in enumerate(toks):
            lw = norm(tok)
            if in_term[k] or tok.isupper() or not lw.isalpha() or len(lw) < 5:
                continue
            if lw in self.vocab.words:
                continue
            if lw.endswith("ing") and lw not in ING_CORE | ING_NOT_VERB | flagged_ing:
                report.add(
                    "warning", loc, "V3",
                    f"\"{tok}\": use an \"-ing\" word only in a technical name.",
                )

        # Vocabulary (W1).
        if not self.vocabulary:
            return
        for k, (tok, _s, _e) in enumerate(toks):
            if in_term[k] or self.vocab.is_known(tok):
                continue
            word = norm(tok)
            entry = report.unknown.setdefault(word, {"count": 0, "location": loc})
            entry["count"] += 1
            if self.strict:
                report.add(
                    "error", loc, "W1",
                    f"\"{tok}\" is not in the vocabulary. Use a core word, a technical name, or a technical verb.",
                )


# Command line ----------------------------------------------------------------


def extra_term_files(paths):
    files = [Path(p) for p in paths]
    for p in os.environ.get("STE_TERMS", "").split(os.pathsep):
        if p.strip():
            files.append(Path(p.strip()))
    local = Path.cwd() / PROJECT_TERMS
    if local.is_file():
        files.append(local)
    return files


def print_text(report):
    for f in report.findings:
        print(f"{f['location']}: {f['level'].upper()} [{f['rule']}] {f['message']}")
    if report.unknown and not any(f["rule"] == "W1" for f in report.findings):
        words = sorted(report.unknown, key=lambda w: (-report.unknown[w]["count"], w))
        print()
        print(f"Words to examine (rule W1): {len(words)}. Each word must be a technical name or a technical verb.")
        for i in range(0, len(words), 8):
            chunk = words[i:i + 8]
            print("  " + ", ".join(f"{w} ({report.unknown[w]['count']})" for w in chunk))
    print()
    print(
        f"Result: {report.errors} errors, {report.warnings} warnings, "
        f"{len(report.unknown)} words to examine."
    )
    if not report.errors and not report.warnings:
        print("The text obeys the rules that this script can check. A person must also read the text.")


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Check text against the Simplified Technical English rules of the ste-data-ai skill."
    )
    ap.add_argument("files", nargs="*", help="files to check (default: standard input)")
    ap.add_argument(
        "--mode", choices=["auto", "procedural", "descriptive", "specification"], default="auto",
        help="type of text (default: auto)",
    )
    ap.add_argument("--terms", action="append", default=[], metavar="FILE",
                    help="a file with more technical names (you can repeat this option)")
    ap.add_argument("--strict", action="store_true",
                    help="report each word that is not in the vocabulary as an error")
    ap.add_argument("--no-vocabulary", action="store_true",
                    help="do not compare words with the vocabulary")
    ap.add_argument("--format", choices=["text", "json"], default="text")
    args = ap.parse_args(argv)

    term_files = extra_term_files(args.terms)
    for f in term_files:
        if not f.is_file():
            print(f"ste_check: cannot read the terms file {f}", file=sys.stderr)
            return 2
    vocab = Vocabulary.load(term_files)
    checker = Checker(vocab, args.mode, args.strict, not args.no_vocabulary)
    report = Report()
    if args.files:
        for name in args.files:
            path = Path(name)
            if not path.is_file():
                print(f"ste_check: cannot read the file {name}", file=sys.stderr)
                return 2
            checker.check_text(path.read_text(encoding="utf-8"), name, report)
    else:
        checker.check_text(sys.stdin.read(), "stdin", report)

    if args.format == "json":
        print(json.dumps({
            "result": {
                "errors": report.errors,
                "warnings": report.warnings,
                "words_to_examine": len(report.unknown),
            },
            "findings": report.findings,
            "words_to_examine": [
                {"word": w, "count": d["count"], "location": d["location"]}
                for w, d in sorted(report.unknown.items())
            ],
        }, indent=2))
    else:
        print_text(report)
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
