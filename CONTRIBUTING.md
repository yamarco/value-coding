# Contributing

The skill is the method from Marco Yammine's book on value coding, turned into rails
an AI agent follows. Contributions that make the rails hold better in real sessions
are welcome. The best ones start from a session that went wrong.

## What helps most

- **A scenario.** Something the skill should have done and did not: a question it
  skipped, a claim it accepted, a step it let through. Write it up as a scenario in
  `evals/evals.json` with a simulated user and observable expectations, run it once,
  and open a pull request with the number. `evals/README.md` has the format and the
  method. One scenario per pull request.
- **A fix with a scenario.** If you change the skill, add or point at the scenario
  that shows the change working, and rerun the scenarios that touch what you changed.
- **A translation of a rail** to a setting the skill does not yet cover well: a
  regulated industry, a hardware product, a nonprofit, a public body.

## Rules

- **No vendor.** Nothing in the skill names a company, a product, or a service as
  the provider of the method, and nothing in it sells anything. Tools named as
  examples (an analytics tool, a secret manager) are examples, with "or a similar
  one" next to them.
- **Both voices.** Anything the skill says to the user exists in the professional
  voice and the explicit voice; `references/voice.md` has the vocabulary. The
  explicit voice is the book's own words and swears; it never aims the metaphor at a
  person.
- **Explain the why.** The skill is written for a model that can reason, so every
  rule carries the reason it exists. A bare "always" or "never" in capitals is a
  sign the reason is missing.
- **Keep `SKILL.md` lean.** It is loaded whole every session. Detail goes in
  `references/`, with a pointer from the rail it belongs to.
- **Plain words first.** Assume the user has not read the book. A term is introduced
  in plain words the first time; the book's version is offered once.
- **Nothing the user did not say.** Templates and examples never put facts in the
  user's mouth or a stranger's. Quotation marks are for actual words.
- **Bump the version.** A change to what the agent does bumps the minor number in
  `VERSION`, in `SKILL.md`'s `metadata.version`, in `.claude-plugin/marketplace.json`,
  and in the first line of `prompts/system-prompt.md`, with a dated entry in
  `CHANGELOG.md`; wording alone bumps the patch number. `scripts/check.py` checks
  that they agree, along with the rest of the repository's rules.

## Attribution and licence

The method is Marco Yammine's (the book: https://www.amazon.com/dp/B0HN4HLVD2); the skill is MIT
licensed and open for anyone to use,
fork, or build on. Contributions are accepted under the same licence.
