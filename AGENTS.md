# Rules for changes to this repository

This repository contains the `ste-data-ai` agent skill.
The skill must work in Claude, Codex, Kiro, Whisper Studio, and other agents that read `SKILL.md`.

## Commands

Run the tests before each commit:

```bash
python3 -m unittest discover -s tests
```

Check a file against the rules of the skill:

```bash
python3 skills/ste-data-ai/scripts/ste_check.py --strict FILE
```

## Rules

1. Write `SKILL.md`, the rules, the patterns, and the "After" text of each example in STE. The tests check these files in strict mode.
2. Use only the standard fields in the front matter of `SKILL.md`: `name`, `description`, `license`, `compatibility`, and `metadata`. Other agents can reject a field that they do not know.
3. Keep `SKILL.md` shorter than 500 lines. Put long text in `references/`.
4. Put each file of the skill in `scripts/`, `references/`, `assets/`, or `agents/`. Whisper Studio changes only the paths in `scripts/`, `references/`, and `assets/` to full paths.
5. Write each path in `SKILL.md` as inline code, and start it at the folder of the skill. Example: `references/writing-rules.md`.
6. Keep the check script in the standard library of Python 3.8.
7. Do not copy the official ASD-STE100 dictionary or the text of the specification into this repository.
8. Do not use em dashes in any file. Use a comma, a colon, a period, or parentheses.
9. When you add a word to `substitutions.md`, make sure that the vocabulary and the terms files do not contain it. A test finds each conflict.
10. When you add an example, give it a "Type" line, a "Before" block, an "After" block, and a "Changes" line. Use the format of the other examples.

## Commit messages

Write a short commit message that tells what changed.
Do not name a person, an email address, or an AI tool in a commit message.
