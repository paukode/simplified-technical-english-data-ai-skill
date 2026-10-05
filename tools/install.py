#!/usr/bin/env python3
"""Install the ste-data-ai skill into one or more AI agents.

Usage:
    python3 tools/install.py claude codex kiro whisper
    python3 tools/install.py all
    python3 tools/install.py --link claude          (a symbolic link, not a copy)
    python3 tools/install.py --project PATH claude codex kiro
    python3 tools/install.py --uninstall all
    python3 tools/install.py --status

Targets:
    claude    Claude Code: ~/.claude/skills (or $CLAUDE_CONFIG_DIR/skills)
    codex     Codex, and other tools that read ~/.agents/skills
    kiro      Kiro IDE and Kiro CLI: ~/.kiro/skills
    whisper   Whisper Studio: ~/.whisper/skills (or $WHISPER_USER_DIR/skills)
    all       all the targets above

With --project PATH, the script installs the skill into the project folder:
PATH/.claude/skills, PATH/.agents/skills, and PATH/.kiro/skills.
Whisper Studio has no project folder for skills.

A copy is the default. A copy works on all systems. With --link, a change in
this repository shows immediately in the agent. Run the script again after
`git pull` to update a copy.

The script never deletes a folder that is not the ste-data-ai skill.
"""

import argparse
import os
import shutil
import sys
from pathlib import Path

NAME = "ste-data-ai"
REPO = Path(__file__).resolve().parent.parent
SOURCE = REPO / "skills" / NAME
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")
TARGETS = ("claude", "codex", "kiro", "whisper")
PROJECT_DIRS = {"claude": ".claude/skills", "codex": ".agents/skills", "kiro": ".kiro/skills"}
LABELS = {
    "claude": "Claude Code",
    "codex": "Codex (and other tools that read ~/.agents/skills)",
    "kiro": "Kiro",
    "whisper": "Whisper Studio",
}


def env_dir(var, default):
    value = os.environ.get(var, "").strip()
    return Path(value).expanduser() if value else default


def user_skill_dirs():
    home = Path.home()
    return {
        "claude": env_dir("CLAUDE_CONFIG_DIR", home / ".claude") / "skills",
        "codex": home / ".agents" / "skills",
        "kiro": home / ".kiro" / "skills",
        "whisper": env_dir("WHISPER_USER_DIR", home / ".whisper") / "skills",
    }


def skill_dirs(targets, project):
    if project is None:
        dirs = user_skill_dirs()
        return [(t, dirs[t]) for t in targets]
    out = []
    for t in targets:
        if t in PROJECT_DIRS:
            out.append((t, Path(project).expanduser().resolve() / PROJECT_DIRS[t]))
        else:
            print(f"Skip {LABELS[t]}: it has no project folder for skills.")
    return out


def is_ours(path):
    """True if path is a folder with a SKILL.md for this skill."""
    skill = path / "SKILL.md"
    if not skill.is_file():
        return False
    for line in skill.read_text(encoding="utf-8", errors="replace").splitlines()[:20]:
        if line.strip() == f"name: {NAME}":
            return True
    return False


def describe(dest):
    if dest.is_symlink():
        return f"link to {os.readlink(dest)}"
    if dest.is_dir():
        return "copy" if is_ours(dest) else "a different folder with the same name"
    return "not installed"


def install(skills_dir, link):
    dest = skills_dir / NAME
    if dest.exists() and not dest.is_symlink() and not is_ours(dest):
        raise RuntimeError(f"{dest} is not the {NAME} skill. Move or remove it, then run the script again.")
    skills_dir.mkdir(parents=True, exist_ok=True)
    if link:
        if dest.is_symlink():
            dest.unlink()
        elif dest.exists():
            shutil.rmtree(dest)
        dest.symlink_to(SOURCE, target_is_directory=True)
        return f"link to {SOURCE}"
    tmp = skills_dir / f".{NAME}.installing"
    if tmp.exists():
        shutil.rmtree(tmp)
    shutil.copytree(SOURCE, tmp, ignore=IGNORE)
    if dest.is_symlink():
        dest.unlink()
    elif dest.exists():
        shutil.rmtree(dest)
    tmp.rename(dest)
    return "copy"


def uninstall(skills_dir):
    dest = skills_dir / NAME
    if dest.is_symlink():
        dest.unlink()
        return "removed the link"
    if not dest.exists():
        return "not installed"
    if not is_ours(dest):
        raise RuntimeError(f"{dest} is not the {NAME} skill. The script did not remove it.")
    shutil.rmtree(dest)
    return "removed"


def main(argv=None):
    ap = argparse.ArgumentParser(description=f"Install the {NAME} skill into AI agents.")
    ap.add_argument("targets", nargs="*", help="claude, codex, kiro, whisper, or all")
    ap.add_argument("--project", metavar="PATH", help="install into a project folder")
    ap.add_argument("--link", action="store_true", help="make a symbolic link, not a copy")
    ap.add_argument("--uninstall", action="store_true", help="remove the skill")
    ap.add_argument("--status", action="store_true", help="show where the skill is installed")
    args = ap.parse_args(argv)

    targets = []
    for t in args.targets or (TARGETS if args.status else ()):
        if t == "all":
            targets.extend(TARGETS)
        elif t == "agents":
            targets.append("codex")
        elif t in TARGETS:
            targets.append(t)
        else:
            ap.error(f"unknown target: {t}. Use claude, codex, kiro, whisper, or all.")
    targets = list(dict.fromkeys(targets))
    if not targets:
        ap.error("give one or more targets, or use --status")
    if not (SOURCE / "SKILL.md").is_file():
        print(f"The skill folder is missing: {SOURCE}", file=sys.stderr)
        return 1

    status = 0
    for target, skills_dir in skill_dirs(targets, args.project):
        label = LABELS[target]
        try:
            if args.status:
                result = describe(skills_dir / NAME)
            elif args.uninstall:
                result = uninstall(skills_dir)
            else:
                result = install(skills_dir, args.link)
        except (OSError, RuntimeError) as e:
            print(f"{label}: {e}", file=sys.stderr)
            status = 1
            continue
        print(f"{label}: {skills_dir / NAME} ({result})")
    return status


if __name__ == "__main__":
    sys.exit(main())
