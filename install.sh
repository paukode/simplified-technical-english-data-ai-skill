#!/bin/sh
# Install the ste-data-ai skill with one command:
#
#   curl -fsSL https://raw.githubusercontent.com/paukode/simplified-technical-english-data-ai-skill/main/install.sh | sh -s -- claude
#
# Targets: claude, codex, kiro, whisper, or all. With no arguments, the
# script installs the skill for all four agents. The script gives each
# argument to tools/install.py, for example: --project PATH, --uninstall.
#
# The script downloads the repository to a temporary folder, runs
# tools/install.py, and then deletes the temporary folder.
set -eu

REPO="paukode/simplified-technical-english-data-ai-skill"
REF="${STE_SKILL_REF:-main}"
ARCHIVE="${STE_SKILL_ARCHIVE:-https://github.com/$REPO/archive/$REF.tar.gz}"

for tool in curl tar python3; do
  if ! command -v "$tool" >/dev/null 2>&1; then
    echo "ste-data-ai: the install needs $tool." >&2
    exit 1
  fi
done

for arg in "$@"; do
  if [ "$arg" = "--link" ]; then
    echo "ste-data-ai: --link needs a clone of the repository. Clone it, then run tools/install.py --link." >&2
    exit 1
  fi
done

if [ "$#" -eq 0 ]; then
  set -- all
fi

tmp=$(mktemp -d 2>/dev/null || mktemp -d -t ste-data-ai)
trap 'rm -rf "$tmp"' EXIT
trap 'exit 1' INT TERM

echo "ste-data-ai: download $REPO ($REF)"
curl -fsSL "$ARCHIVE" | tar -xzf - -C "$tmp" --strip-components 1
python3 "$tmp/tools/install.py" "$@"
