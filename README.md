# Value Coding

**Vibe coding is mostly about you. Value coding is mostly about them.**

Value Coding is an open skill for any AI model or coding agent. It turns the assistant
that never says no into one that asks, before it builds anything, the question most
people skip: *who is this for?* It is the method from Marco Yammine's book on value
coding, written as rails an agent follows: a person with a name before an idea, a price
in front of strangers before code, one thing in progress, a daily question you cannot
skip, an altitude reading before every argument, and a named human who signs each
gate (https://www.amazon.com/dp/B0HN4HLVD2).

It is free, open source, and vendor-neutral. It is not a product and it does not sell
one.

## What it does

When the skill is active, the agent:

- **Looks before it asks.** It reads your repository, manifests, git history, docs,
  and deck, says what it can see and how it knows (developer or founder, solo or team,
  startup or established business, industry, geography, how many nines you have
  today), and asks only for what the evidence does not settle. On an existing
  project it establishes the traction first, active users, strangers among them,
  paying customers, revenue, retention, money in, from billing and analytics where
  it can and in quick bands where it cannot, because that sets the stage. Then it
  challenges the answers that are claims, once, with the evidence.
- **Asks which voice you want, and does not pick for you.** *Professional* is formal
  and office-safe. *Explicit* is informal and direct, the book's own words, swearing
  included; the book makes its point with a sexual metaphor, on purpose, because it
  sticks. Both are blunt. It assumes you have not read the book and explains each term
  in plain words the first time, offering the book's version if you want it.
- **Onboards you the way the book works: climb, dive, climb.** One question at a time,
  always with choices to pick from, built from what it can already see, with "pick
  all that apply" where several are true, then a piece of real work that uses
  the answers, then the next questions at the moment they bite. Never a wall of
  questions, and almost never an open one. First the voice, then whether this is a
  new project or an existing one (if it exists, the agent reads it before asking
  anything else), then where you are, then the one real person it is
  for and what they need in their words, then what done looks like for them and when a
  stranger first sees a price. After that you have something in hand, and the stake,
  the humans who sign, the numbers with green and red lines, the nines, and the fear
  made specific three times come when the work reaches them. It will not build before
  the person and the outcome exist.
- **Keeps state in your repo** in plain Markdown: a `VALUE.md` at the root and a
  `value-coding/` folder with people, strangers' replies word for word, KPIs with green
  and red lines, the ten-slide menu, a journal, action items, the humans who sign,
  parked decisions, the research it found with sources, and its own backlog and
  roadmap. They are committed with the project, and a one-line pointer goes into
  the project's agent instructions file, so any tool and any model, with or without
  the skill, reads them before working.
- **Plans before it builds, mostly on its own.** It derives a backlog and a roadmap
  from the person, the outcome, the nines, and the code: tickets with a name, a
  question, an altitude, a status, and the test that proves them; milestones with
  goals and dates. You correct the board instead of writing it.
- **Knows which stage you are at, and when to stop coding.** Pre-POC, POC, MVP, PMF,
  scaling: placed by paying strangers rather than by how much code exists. At POC it
  codes until the outcome happens once and then sends you to a stranger; at MVP it
  codes only what the strangers' noes ask for; at PMF it codes for retention.
- **Builds to the reliability you chose, and no further.** 80% is the default and is
  enough for most things; one nine is for what strangers pay for daily; two nines gets
  pushed back on hard, after it tells you what 99% actually means (watched around
  the clock, paged when it breaks, backups restored, reviewed by someone who has done
  it, ten times the cost), and if you insist it says plainly that you are entering
  complexity and blind spots that need experienced professionals, and makes finding
  one the first action item. The number is a contract that caps the work. Whenever an outcome can be proven by an automated test, it is, and the
  test is named after the person's question. One repository, one language, one
  database, boring technology, no infrastructure ahead of retention, because
  everything created must be maintained.
- **Pushes you to watch customers, not just ask them.** A customer interview is
  sitting with a stranger, in person or with their screen shared, watching them do
  the task today and then try the product, listening without helping. When you
  report what a customer said, it asks once whether you watched them do it, and if
  not, the screen-shared interview becomes the next action item.
- **Asks whether value needs to be taught before it builds the feature.** When you
  bring what a customer said, it asks once whether they could not find it, did not
  know why it mattered, or whether it really does not exist. Most people give up on
  teaching and say yes to every customer; a sentence on the screen or a walkthrough
  reaches every future stranger, a feature serves the one who asked.
- **Takes the coding half seriously.** Web first: it pushes back once on a native app
  before a stranger has paid and proposes an installable web app, because early on
  speed to deployment is what lets you fix the errors and blind spots strangers
  find. Logs the agent can read: from the first deploy, server and client logs (native
  apps and devices included) land in one place it can read with one command, with
  request ids, and no exception is ever swallowed, so it can find the bug instead of
  guessing. Analytics and session recordings before the first stranger. Passwordless
  login. Build over buy, with payments and message delivery as the exceptions. And
  one lane of work at a time: it pushes back on a swarm of agents changing one
  codebase at once, and runs a sequential pipeline instead, with migrations one at a
  time. End-to-end tests in a real browser for the outcome and the money path.
  Releases of one ticket at a time, each with a build you can open and one sentence
  saying what to try, so you never face ten changes at once. Three isolated
  environments, local, staging, and production, each a replica deployed from one
  command. Secrets in a gitignored `.env`, and a secret manager in production.
- **Makes you pick a north star and reads it itself.** One primary number that
  measures the value for the person, leads rather than trails, moves when you act,
  is hard to game, and counts people; it says which test your candidate fails. With
  the first release it builds a way to read the number without you: a read-only
  query, an analytics or BI API, or a KPI command. It reads the KPIs weekly and the
  traction monthly, and quotes the number before it says anything worked.
- **Does the market research itself** when it has web access: competitors and their
  complaints, the price band, a bottom-up market size with the arithmetic shown, the
  regulation that applies in your geography, with sources and dates.
- **Lets you skip steps, and keeps score.** Say "later, I want to build" to any
  question, refuse the stake, build before a stranger has seen a price, sign your own
  gate: it helps anyway, marks what is open or rogue in VALUE.md, and shows a value
  score out of twelve at the start of every session. Answer the daily question with
  the bad word and it builds with you for the day without a form. No lecture; the
  number does the work.
- **Rates you now and then, 1 to 10.** Not every session and not on a day you can
  predict: roughly every fourth or fifth session, or when a stranger pays, a rail
  goes rogue, or a week goes by in the weeds, one line on how well you are value
  coding right now, the one reason, and the one thing that would raise it. The
  score counts rails in use; the rating judges the whole.
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

Any tool that reads skill folders in the open Agent Skills format can use it. One line
installs it for every coding agent on the machine (Claude Code, Codex, Gemini CLI,
Antigravity, Grok, Cursor, Windsurf, Cline, Copilot) and tells you what to do for Aider:

```sh
curl -fsSL https://raw.githubusercontent.com/yamarco/value-coding/main/install/install.sh | sh
```

Read the script first; it is forty lines, makes one clone under `~/.agents/skills` and
links it where the other tools look. `install/README.md` has the per-tool paths and
commands, verified against each tool's documentation, and the per-project variant.

**Claude Code only**

```bash
git clone https://github.com/yamarco/value-coding ~/.claude/skills/value-coding
```

Or inside one project: clone into `.claude/skills/value-coding`. Or as a plugin, which
gives you install and updates from inside Claude Code:

```
/plugin marketplace add yamarco/value-coding
/plugin install value-coding@yamarco
```

Updates then come from `/plugin` (Installed tab, "Update now"), or automatically if
you enable auto-update for the marketplace in the same place; it is off by default
for marketplaces outside Anthropic's own. Each release bumps the plugin version, so
an update appears when the skill changes, not on every commit.

**Tools without skill folders** (Aider, a chat product with a system prompt field):
paste `prompts/system-prompt.md` into the standing instructions. It is the short
version and carries its version on the first line.

**Updating**

The version is in `VERSION` and in the front matter of `SKILL.md`; `CHANGELOG.md`
says what changed. To see what you have and what is current:

```bash
cat ~/.claude/skills/value-coding/VERSION
curl -s https://raw.githubusercontent.com/yamarco/value-coding/main/VERSION
```

To update:

```bash
git -C ~/.claude/skills/value-coding pull
```

Plugin installs update from `/plugin` instead. The agent also writes the version it ran with into your `VALUE.md`, tells you in one
line when the installed skill is newer than the one your project last saw, and once
a month, when it has network access and the skill is a git clone, checks for a newer
version and asks whether to update. It never pulls without your answer. If you pasted
`prompts/system-prompt.md` into another tool, updating means pasting it again; the
file's first line carries its version.

Installed globally, the skill does not take over every conversation. When the agent
judges that a request is about building, planning, pitching, or running something,
and the project has no `VALUE.md` yet, it asks once whether you want to use Value
Coding here. "Not for this project" writes one line to the project's agent
instructions file so nobody asks again. Call it by name (`/value-coding`) and it
starts without asking.

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

## Privacy: what gets written into your repository

The skill writes real people into plain-text files that get committed: the person it
is for, with a name, an age, a place, and their words; strangers and what they said;
sometimes a link to a picture. Git history does not forget, so:

- **Keep the repository private while those files hold real people.** The agent says
  this once when the first person is written down, and asks before writing a real
  person into a public repository.
- **Only what the method needs.** A first name and an initial are enough for a
  stranger. Full names and pictures only with consent; pictures are linked, never
  copied in.
- **Regulated data never goes in.** Health, children, finance, or anything a law in
  your country covers is written as a reference ("patient 14, back pain"), never as
  the record. The record stays in the system that is allowed to hold it. If you paste
  such a record into the chat, the agent uses it and does not write it down.
- **Removal.** Someone who asks to be removed is removed from the files and from the
  history; the agent tells you how.
- **Your lawyer.** When the geography or the data calls for it, the agent sends you
  to one, once.

The skill also puts analytics and session recordings in front of your strangers
early. The same rules apply there: say on the site that recording happens, mask
personal and payment fields, and ask the lawyer when the data calls for it.

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
  engineering.md         web first, logs the agent can read, exceptions, analytics,
                         passwordless login, data model, build over buy, one lane,
                         end-to-end tests, one-ticket releases, three envs, secrets
  deliverables.md        decks, websites, proposals, plans, messages: person first
  score.md               the twelve rails, the value score, going rogue
  stages.md              POC, MVP, PMF, and when to stop coding at each
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
install/                 one-line install for every coding agent, and the per-tool paths
evals/                   twenty scenarios with simulated users and expectations,
                         the grader prompt, fixtures, and the results history
CONTRIBUTING.md          how to add a scenario or a rail
VERSION, CHANGELOG.md    the version the agent records in VALUE.md, and what changed
.claude-plugin/          the marketplace file for installing as a Claude Code plugin
scripts/check.py         the repository's own rules, run on every pull request
CODE_OF_CONDUCT.md       the line between the explicit voice and how people are treated
```

## Does it work

The skill is tested on twenty scenarios with a simulated user, graded against
observable expectations (`evals/`). Two rounds on 2026-10-15:

| Version | Expectations met | Without the skill, same scenarios |
|---|---|---|
| 1.0.0 | 193 of 236 (81.8%) | 52 of 200 (26.0%) |
| 1.1.0 | 226 of 279 (81.0%), on a harder set | same baseline |

The second round added two hard checks to every scenario (no fact written that the
user did not give; something in the user's hands within three questions) and split
compound checks, so the bar rose by about 40 expectations; raw passes rose in 19 of 20
scenarios. What still misses is in `evals/RESULTS.md`, and 1.1.1 is the patch for it.

## Contributing

The evals in `evals/` are the skill's own tests: twenty scenarios, each with a
simulated user and a list of things the agent must observably do, graded from the
transcript. The most useful contribution is a scenario from a session that went
wrong. `CONTRIBUTING.md` and `evals/README.md` have the format and the method.

## The one number

Vibe-coding tools count tools built and users active. This skill counts one thing: of
what was built, how much is still used and still paid for a year later, by name.

## Attribution and licence

The Value Coding method, the principles, the altitudes, the Raptor Method, the menu,
and the action items are by **Marco Yammine**, from his book on value coding
(*Doing things that don't penetrate a market is just m\*sturbating*), on Amazon at
https://www.amazon.com/dp/B0HN4HLVD2. This skill is
released under the MIT licence so that anyone can use, copy, adapt, and redistribute
it; keep the copyright notice, and tell people where it came from.

Contributions are welcome: better questions, better rails, translations, and real
reports of what happened when a stranger was asked to pay.
