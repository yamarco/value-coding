#!/bin/sh
# Install the Value Coding skill for every coding agent on this machine.
#
# One clone at ~/.agents/skills/value-coding, which Codex, Gemini CLI, Cursor,
# Windsurf/Devin, GitHub Copilot, and Grok scan on their own, plus a link into the
# folders of the tools that do not scan it (Claude Code, Cline, Antigravity CLI).
#
#   sh install.sh            install or update
#   sh install.sh --check    show what is installed where, change nothing
#
# Aider does not read skill folders: add `read: [~/.agents/skills/value-coding/SKILL.md]`
# to .aider.conf.yml, or start it with --read on that file.
set -eu
REPO="https://github.com/yamarco/value-coding"
CANON="$HOME/.agents/skills/value-coding"
LINKS="$HOME/.claude/skills $HOME/.cline/skills $HOME/.gemini/antigravity-cli/skills"
CHECK="${1:-}"

status() {
  printf '%-48s %s\n' "$1" "$2"
}

if [ "$CHECK" = "--check" ]; then
  if [ -d "$CANON/.git" ]; then status "$CANON" "clone, version $(cat "$CANON/VERSION" 2>/dev/null || echo '?')"; else status "$CANON" "missing"; fi
  for d in $LINKS; do
    t="$d/value-coding"
    if [ -L "$t" ]; then status "$t" "link -> $(readlink "$t")"
    elif [ -d "$t" ]; then status "$t" "copy or clone, version $(cat "$t/VERSION" 2>/dev/null || echo '?')"
    else status "$t" "missing"; fi
  done
  exit 0
fi

mkdir -p "$(dirname "$CANON")"
if [ -d "$CANON/.git" ]; then
  echo "Updating $CANON"; git -C "$CANON" pull -q --ff-only
else
  echo "Cloning into $CANON"; git clone -q "$REPO" "$CANON"
fi

for d in $LINKS; do
  mkdir -p "$d"
  t="$d/value-coding"
  if [ -L "$t" ] || [ ! -e "$t" ]; then
    ln -sfn "$CANON" "$t" && echo "Linked $t"
  else
    echo "Left $t alone: it exists and is not a link (update it yourself, or remove it and rerun)"
  fi
done

echo
echo "Installed Value Coding $(cat "$CANON/VERSION"). Restart your tools, then say 'build me something'."
echo "Aider: add  read: [$CANON/SKILL.md]  to .aider.conf.yml."
