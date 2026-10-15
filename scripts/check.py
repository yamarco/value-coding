#!/usr/bin/env python3
"""The repository's own rules, checked on every pull request.

Run locally with: python3 -I scripts/check.py
"""
import json, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
problems = []

def fail(msg):
    problems.append(msg)

# 1. evals.json parses and every scenario is complete
try:
    evals = json.loads((root / "evals/evals.json").read_text())["evals"]
    ids = [e["id"] for e in evals]
    if len(ids) != len(set(ids)):
        fail("evals.json: duplicate ids")
    for e in evals:
        for key in ("name", "prompt", "simulated_user", "expectations"):
            if not e.get(key):
                fail(f"evals.json: scenario {e.get('id')} is missing {key}")
        for f in e.get("files", []):
            if not (root / "evals" / f).exists():
                fail(f"evals.json: scenario {e.get('id')} points at missing fixture {f}")
except Exception as exc:  # noqa: BLE001
    fail(f"evals.json: {exc}")

# 2. versions agree
version = (root / "VERSION").read_text().strip()
skill = (root / "SKILL.md").read_text()
m = re.search(r'^\s*version:\s*"?([0-9]+\.[0-9]+\.[0-9]+)"?', skill, re.M)
if not m or m.group(1) != version:
    fail(f"SKILL.md metadata.version does not match VERSION ({version})")
prompt_first = (root / "prompts/system-prompt.md").read_text().splitlines()[0]
if version not in prompt_first:
    fail(f"prompts/system-prompt.md first line does not carry version {version}")
if f"## {version}" not in (root / "CHANGELOG.md").read_text():
    fail(f"CHANGELOG.md has no entry for {version}")
mp = json.loads((root / ".claude-plugin/marketplace.json").read_text())
if mp["plugins"][0].get("version") != version:
    fail(f".claude-plugin/marketplace.json plugin version does not match VERSION ({version})")

# 3. no vendor named as the provider of the method
vendor_words = [w for w in (root / "scripts/vendor-words.txt").read_text().split() if w]
for path in list(root.glob("*.md")) + list((root / "references").glob("*.md")) + list((root / "templates").rglob("*.md")) + list((root / "prompts").glob("*.md")):
    text = path.read_text().lower()
    for w in vendor_words:
        if w.lower() in text:
            fail(f"{path.relative_to(root)}: contains forbidden vendor word {w!r}")

# 4. SKILL.md stays loadable
lines = skill.count("\n")
limit = 750  # lowered to 520 once the SKILL.md diet lands
if lines > limit:
    fail(f"SKILL.md is {lines} lines; the limit is {limit}. Move detail into references/.")

# 5. frontmatter present
if not skill.startswith("---\nname: value-coding\n"):
    fail("SKILL.md must start with the frontmatter and name: value-coding")

# 6. fixtures carry no key that looks real
for env in (root / "evals/fixtures").rglob(".env"):
    for line in env.read_text().splitlines():
        if re.search(r"(sk_live_|sk_test_|AKIA)[0-9A-Za-z]{20,}", line):
            fail(f"{env.relative_to(root)}: a key that matches a real pattern")

if problems:
    print("\n".join(problems))
    sys.exit(1)
print(f"ok: {len(evals)} scenarios, version {version}, SKILL.md {lines} lines")
