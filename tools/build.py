#!/usr/bin/env python3
"""Build files to share the ste-data-ai skill.

Usage:
    python3 tools/build.py zip [-o FILE]
    python3 tools/build.py prompt [--fields LIST] [--examples] [--vocabulary] [-o FILE]

zip     A ZIP file with the skill folder. Upload it to Claude.ai or to any
        tool that installs a skill from a ZIP file.
        Default output: dist/ste-data-ai.zip

prompt  One Markdown file with the instructions and the reference files.
        Use it as a system prompt, as custom instructions, or as a Kiro steering
        file in a tool that does not read SKILL.md.
        Default output: dist/ste-data-ai-prompt.md

Fields for --fields (separate them with a comma, or use "all"):
    it, aws, gcp, azure, snowflake, redshift, opensearch, vector,
    data-engineering, data-architecture, ml, genai, agentic
"""

import argparse
import re
import sys
import zipfile
from pathlib import Path

NAME = "ste-data-ai"
REPO = Path(__file__).resolve().parent.parent
SKILL = REPO / "skills" / NAME
DIST = REPO / "dist"
SKIP_PARTS = {"__pycache__", ".DS_Store"}

# Field key: (file in references/terms, file in references/examples)
FIELDS = {
    "it": ("it-and-software.md", "it-operations.md"),
    "aws": ("cloud-aws.md", "cloud-aws.md"),
    "gcp": ("cloud-google-cloud.md", "cloud-google-cloud.md"),
    "azure": ("cloud-azure.md", "cloud-azure.md"),
    "snowflake": ("snowflake.md", "snowflake.md"),
    "redshift": ("redshift.md", "redshift.md"),
    "opensearch": ("opensearch.md", "opensearch.md"),
    "vector": ("vector-databases.md", "vector-databases.md"),
    "data-engineering": ("data-engineering.md", "data-engineering.md"),
    "data-architecture": ("data-architecture.md", "data-architecture.md"),
    "ml": ("machine-learning.md", "machine-learning.md"),
    "genai": ("generative-ai.md", "generative-ai.md"),
    "agentic": ("agentic-ai.md", "agentic-ai.md"),
}


def skill_files():
    for path in sorted(SKILL.rglob("*")):
        if path.is_file() and not SKIP_PARTS & set(path.parts) and path.suffix != ".pyc":
            yield path


def build_zip(output):
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in skill_files():
            arcname = Path(NAME) / path.relative_to(SKILL)
            info = zipfile.ZipInfo(arcname.as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o755 if path.suffix == ".py" else 0o644) << 16
            zf.writestr(info, path.read_bytes())
    return output


def body_of_skill():
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    m = re.match(r"^---\n.*?\n---\n", text, re.S)
    return text[m.end():].lstrip() if m else text


def parse_fields(value):
    if not value:
        return []
    if value == "all":
        return list(FIELDS)
    keys = [k.strip() for k in value.split(",") if k.strip()]
    unknown = [k for k in keys if k not in FIELDS]
    if unknown:
        raise SystemExit(f"Unknown field: {', '.join(unknown)}. Use: {', '.join(FIELDS)}, or all.")
    return keys


def build_prompt(output, fields, examples, vocabulary):
    parts = [
        f"# {NAME}: Simplified Technical English for IT, data, and AI\n",
        "This file contains the instructions and the reference files of the "
        f"`{NAME}` skill. Each section that starts with \"File:\" is one file of the skill. "
        "When the instructions refer to a file, use the section with the same name. "
        "If a file is not in this prompt, use the rules that are in this prompt.\n",
        "---\n",
        "## File: SKILL.md\n",
        body_of_skill(),
    ]
    files = ["references/writing-rules.md", "references/substitutions.md"]
    if vocabulary:
        files += ["references/core-vocabulary.md", "references/technical-verbs.md"]
    for key in fields:
        files.append(f"references/terms/{FIELDS[key][0]}")
    if examples:
        for key in fields:
            files.append(f"references/examples/{FIELDS[key][1]}")
    for rel in files:
        parts += ["---\n", f"## File: {rel}\n", (SKILL / rel).read_text(encoding="utf-8")]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(p.rstrip() + "\n" for p in parts), encoding="utf-8")
    return output


def main(argv=None):
    ap = argparse.ArgumentParser(description=f"Build files to share the {NAME} skill.")
    sub = ap.add_subparsers(dest="command", required=True)
    z = sub.add_parser("zip", help="a ZIP file of the skill folder")
    z.add_argument("-o", "--output", type=Path, default=DIST / f"{NAME}.zip")
    p = sub.add_parser("prompt", help="one Markdown file for a system prompt")
    p.add_argument("--fields", default="", help="comma-separated fields, or all")
    p.add_argument("--examples", action="store_true", help="add the examples of the fields")
    p.add_argument("--vocabulary", action="store_true", help="add the core vocabulary and the technical verbs")
    p.add_argument("-o", "--output", type=Path, default=DIST / f"{NAME}-prompt.md")
    args = ap.parse_args(argv)

    if args.command == "zip":
        out = build_zip(args.output)
    else:
        out = build_prompt(args.output, parse_fields(args.fields), args.examples, args.vocabulary)
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
