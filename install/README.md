# Installing Value Coding in any coding agent

The skill is a folder in the open Agent Skills format: a `SKILL.md` with its
`references/`, `templates/`, and `prompts/` beside it. Most coding agents now read that
format directly; the only differences are where each one looks. This page was verified
against each tool's documentation on 2026-10-15; paths change, so when a row fails,
check the linked page.

## The one-line install

```sh
curl -fsSL https://raw.githubusercontent.com/yamarco/value-coding/main/install/install.sh | sh
```

Or clone first and run it from the folder. It makes one clone at
`~/.agents/skills/value-coding`, which Codex, Gemini CLI, Cursor, Windsurf, Copilot,
and Grok scan on their own, and links it into the folders of the tools that do not scan
that path (Claude Code, Cline, Antigravity CLI). Run it again to update. Run it with
`--check` to see what is installed where. Read it before you run it; it is forty lines.

A community alternative that installs into every detected agent in one command is the
`skills` CLI from Vercel Labs (`npx skills add yamarco/value-coding -g --all`). It is not
maintained by any of the tool vendors or by this project; check its paths against the
table below before relying on it.

## Per tool

| Tool | Reads skill folders | Where it looks (user level, then project level) | Install |
|------|---------------------|--------------------------------------------------|---------|
| **Claude Code** | Yes | `~/.claude/skills/<name>/`; `.claude/skills/<name>/`; plugins. Does not scan `~/.agents/skills`. | `git clone https://github.com/yamarco/value-coding ~/.claude/skills/value-coding`, or as a plugin: `/plugin marketplace add yamarco/value-coding` then `/plugin install value-coding@yamarco` (updates from `/plugin`) |
| **OpenAI Codex** (CLI, IDE, desktop) | Yes | `~/.agents/skills/`; `.agents/skills/` in the repo or its parents; `/etc/codex/skills`. Follows symlinks. Invoke with `$value-coding` or `/skills`. | `git clone https://github.com/yamarco/value-coding ~/.agents/skills/value-coding`, then restart Codex |
| **Google Gemini CLI** | Yes | `~/.gemini/skills/` or `~/.agents/skills/`; `.gemini/skills/` or `.agents/skills/`. Consent prompt on first use; `/skills list`. | `gemini skills install https://github.com/yamarco/value-coding --consent` (add `--scope workspace` for one project) |
| **Google Antigravity CLI** (`agy`) | Yes | `~/.gemini/antigravity-cli/skills/<name>/`; `<repo>/.agents/skills/<name>/`. Skills become slash commands. | `git clone https://github.com/yamarco/value-coding ~/.gemini/antigravity-cli/skills/value-coding` |
| **xAI Grok Build** (`grok`) | Yes | `~/.grok/skills/`, `~/.agents/skills/`; `.grok/skills/` walked up to the repo root; extra paths in `~/.grok/config.toml`. | `git clone https://github.com/yamarco/value-coding ~/.grok/skills/value-coding` |
| **Cursor** | Yes | `~/.agents/skills/`, `~/.cursor/skills/`; `.agents/skills/`, `.cursor/skills/`; also reads `.claude/skills/`. Shown under Customize, Skills. | `git clone https://github.com/yamarco/value-coding ~/.cursor/skills/value-coding` |
| **Windsurf / Devin Desktop** (Cascade) | Yes | `~/.codeium/windsurf/skills/<name>/` or `~/.config/devin/skills/<name>/`; `.devin/skills/` (legacy `.windsurf/skills/`); `.agents/skills/` and `~/.agents/skills/` always. | `git clone https://github.com/yamarco/value-coding ~/.codeium/windsurf/skills/value-coding` |
| **Cline** | Yes | `~/.cline/skills/`; `.cline/skills/`, `.clinerules/skills/`, `.claude/skills/`. Does not scan `.agents/skills`. Toggle in the Skills tab; `/value-coding`. | `git clone https://github.com/yamarco/value-coding ~/.cline/skills/value-coding` |
| **GitHub Copilot** (CLI, cloud agent, VS Code and JetBrains agent mode) | Yes | `~/.copilot/skills` or `~/.agents/skills`; `.github/skills`, `.claude/skills`, `.agents/skills` in the repo. | `gh skill install yamarco/value-coding value-coding --scope user` (gh 2.90 or later), or clone into `.github/skills/` for one repo |
| **Aider** | No | Reads files listed with `--read` or in `.aider.conf.yml`. | `aider --read ~/.agents/skills/value-coding/SKILL.md`, or `read: [~/.agents/skills/value-coding/SKILL.md]` in `.aider.conf.yml`. Aider does not follow the links to `references/`; list the ones you want. |
| **Anything else** | | Reads a standing-instructions file: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursor/rules/*.mdc`, `.clinerules/`, `.github/copilot-instructions.md`, a system prompt field. | Paste `prompts/system-prompt.md` into it. It is the short version of the skill and carries its version on the first line; paste again when the version moves. |

Not verified at the time of writing, so treat as unknown: whether Codex still reads the
older `~/.codex/skills` path, Grok's project-level `.agents/skills`, Copilot's install
scopes other than `user`, and whether Claude Code and Cline follow a symlinked skill
folder (the script links; if a tool does not list the skill, replace the link with a
copy).

## Per-project instead of per-user

Clone into the project-level folder from the table (`.agents/skills/value-coding` covers
most tools; `.claude/skills/value-coding` for Claude Code; `.github/skills/` for the
Copilot cloud agent) and commit it, or add it as a git submodule, so the whole team gets
the same version. The agent still asks once whether to use the skill in a project that
has no `VALUE.md`.

## Updating

The one-line install updates the clone and keeps the links. By hand:
`git -C ~/.agents/skills/value-coding pull`. The version is in `VERSION`; what changed is
in `CHANGELOG.md`. Inside a session the agent compares the installed version with the one
recorded in your `VALUE.md`, tells you in one line when it moved, and once a month asks
whether to pull a newer one; it never pulls without your answer.
