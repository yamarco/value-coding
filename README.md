# Value Coding

**Vibe coding is mostly about you. Value coding is mostly about them.**

Value Coding is an open skill for any AI model or coding agent. It turns the assistant
that never says no into one that asks, before it builds anything, the question most
people skip: *who is this for?* It is the method from Marco Yammine's book on value
coding, written as rails an agent follows: a person with a name before an idea, a price
in front of strangers before code, one thing in progress, a daily question you cannot
skip, an altitude reading before every argument, and a named human who signs each
gate.

It is free, open source, and vendor-neutral. It is not a product and it does not sell
one.

## What it does

When the skill is active, the agent:

- **Looks before it asks.** It reads your repository, manifests, git history, docs,
  and deck, says what it can see and how it knows (developer or founder, solo or team,
  startup or established business, industry, geography, how many nines you have
  today), and asks only for what the evidence does not settle. Then it challenges the
  answers that are claims, once, with the evidence.
- **Asks which voice you want, and does not pick for you.** The book's own voice is
  explicit: sex is the metaphor for the whole method, on purpose, because it sticks.
  *Unfiltered* uses the book's words. *Filtered* asks the same questions in office-safe
  words. Both are blunt.
- **Onboards you the way the book works: climb, dive, climb.** One question at a time,
  with choices to pick from wherever they exist, then a piece of real work that uses
  the answers, then the next questions at the moment they bite. Never a wall of
  questions. First the voice and where you are, then the one real person it is
  for and what they need in their words, then what done looks like for them and when a
  stranger first sees a price. After that you have something in hand, and the stake,
  the humans who sign, the numbers with green and red lines, the nines, and the fear
  made specific three times come when the work reaches them. It will not build before
  the person and the outcome exist.
- **Keeps state in your repo** in plain Markdown: a `VALUE.md` at the root and a
  `value-coding/` folder with people, strangers' replies word for word, KPIs with green
  and red lines, the ten-slide menu, a journal, action items, the humans who sign,
  parked decisions, the research it found with sources, and its own backlog and
  roadmap. Any tool and any model can read them.
- **Plans before it builds, mostly on its own.** It derives a backlog and a roadmap
  from the person, the outcome, the nines, and the code: tickets with a name, a
  question, an altitude, a status, and the test that proves them; milestones with
  goals and dates. You correct the board instead of writing it.
- **Builds to the nines you chose, and no further.** The nines are a contract that
  caps the work. Whenever an outcome can be proven by an automated test, it is, and the
  test is named after the person's question. One repository, one language, one
  database, boring technology, no infrastructure ahead of retention, because
  everything created must be maintained.
- **Does the market research itself** when it has web access: competitors and their
  complaints, the price band, a bottom-up market size with the arithmetic shown, the
  regulation that applies in your geography, with sources and dates.
- **Lets you skip steps, and keeps score.** Refuse the stake, build before a stranger
  has seen a price, sign your own gate: it helps anyway, marks the rail as rogue in
  VALUE.md, and shows a value score out of twelve at the start of every session. No
  lecture; the number does the work.
- **Tags every answer with its altitude**: 🟩 40,000 ft, 🟦 30,000 ft, 🟨 20,000 ft,
  🟧 10,000 ft, 🟥 ground, in the book's colours where the surface can show them, so
  you always know whether you are arguing about the button or about whether the button
  should exist.
- **Enforces the rails in daily work**: the daily question, an altitude reading, a
  name and a question on every to-do, a weekly random-ticket test, flags on the word
  "viral", a feeling-first rewrite of any feature-first pitch, a price near the top of
  every plan, strangers-only evidence, and action items with a name and a date at the
  end of every session.
- **Sends you to a human at the right moments.** The agent does the hours and cannot
  be accountable for any of them. It will tell you, once and plainly, when a product
  person should read the plan, when an engineer who has done it before should check
  the architecture, when a salesperson should hear the price, when a lawyer should see
  the terms, and when the person who tells you you are wrong should make the call. The
  three gates, before the build, before the first release, and before scaling, need a
  named signature, and a gate signed by the person who wants to pass it is not a gate.

## Install

The skill is a folder with a `SKILL.md` and references, in the open Agent Skills
layout. Any tool that reads skill folders can use it directly.

**Claude Code**

```bash
git clone https://github.com/yamarco/value-coding ~/.claude/skills/value-coding
```

Or inside one project: clone into `.claude/skills/value-coding`. Then say "build me
something" and watch it ask who it is for.

**Codex, Cursor, Windsurf, Cline, Aider, and other agents that read repo
instructions**

Clone the repo somewhere in your project (for example `skills/value-coding`) and add
one line to the file your tool reads (`AGENTS.md`, `.cursorrules`,
`.windsurfrules`, `CONVENTIONS.md`):

```
Before any work, read skills/value-coding/SKILL.md and follow it.
```

**ChatGPT, Gemini, Claude.ai, Mistral, Llama, or any chat tool with custom
instructions**

Paste `prompts/system-prompt.md` into the custom or project instructions. It is the
short version. If the tool lets you upload files, upload the whole `references/`
folder as well.

**Any other LLM**

Put the contents of `SKILL.md` at the top of the system prompt and make the
`references/` files available for retrieval. Nothing in the skill depends on a
specific model or tool; it only needs the model to read and write Markdown files in
the project.

## What a session looks like

1. The agent reads `VALUE.md` and your action items, puts the person's name and
   sentence at the top of its reply, and asks the daily question if it has not asked
   today.
2. It gives an altitude reading of what you asked: "that is a 10,000 ft feature
   request; the 40,000 ft question is still open."
3. It helps, at the altitude you choose, pushing toward the smallest thing a stranger
   can be shown and pay for, and naming the human who should be in the room when the
   stakes call for one.
4. It ends with action items: one sentence, a name, a date, written to
   `value-coding/ACTIONS.md`.

## Layout

```
SKILL.md                 the skill: the rules, the rails, the files
references/              read by the agent when the moment calls for it
  evidence.md            look before you ask, challenge the answers, research yourself
  onboarding.md          the onboarding, climb by climb
  planning.md            the backlog and roadmap the agent keeps and mostly derives
  building.md            the nines as a contract, tests that prove outcomes, the stack
  principles.md          the method in one sitting
  altitudes.md           the five altitudes and the reading
  rails.md               the 39 steps, in order, and who signs
  rituals.md             standing behaviours by cadence
  humans.md              when to send the user to a human, and the gates
  menu.md                the ten-slide deck, in both voices
  metrics.md             KPIs, goals, vanity numbers, the one number
  voice.md               the two vocabularies
  state.md               the state files and how to keep them
templates/               VALUE.md and the value-coding/ files, empty
prompts/system-prompt.md the short version for tools without skills
evals/                   test prompts used to check the skill behaves
```

## The one number

Vibe-coding tools count tools built and users active. This skill counts one thing: of
what was built, how much is still used and still paid for a year later, by name.

## Attribution and licence

The Value Coding method, the principles, the altitudes, the Raptor Method, the menu,
and the action items are by **Marco Yammine**, from his book on value coding
(*Doing things that don't penetrate a market is just m\*sturbating*). This skill is
released under the MIT licence so that anyone can use, copy, adapt, and redistribute
it; keep the copyright notice, and tell people where it came from.

Contributions are welcome: better questions, better rails, translations, and real
reports of what happened when a stranger was asked to pay.
