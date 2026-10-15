# State: the files you keep

Rails only work if they survive the session. State lives in the user's project in
plain Markdown so any tool, any model, and the human can read and edit it. `VALUE.md`
sits in the project root, where a README would; everything else sits in
`value-coding/`. Templates are in `templates/` next to this skill; copy them on first
use and fill them in.

Rules:

- **The files live in the repository and are committed with it.** `VALUE.md` and
  `value-coding/` are part of the project, not of the session: they go into version
  control like a README, so the next session, the next tool, and the next human
  find them. Commit them with the work they describe, never in a separate "AI
  files" commit, and never put them in `.gitignore`. When the project has an agent
  instructions file (`CLAUDE.md`, `AGENTS.md`, `.cursorrules`, or the host's
  equivalent), add one line to it on first use, so agents without this skill still
  read the context: "Read VALUE.md and value-coding/ before any work; they hold who
  this is for, the stage, the nines, and the open action items." When the project
  is not a repository (a deck, a plan, a company run from a folder), the files go in
  that folder, next to the deliverable.
- Create `VALUE.md` as soon as the voice is chosen in climb 1, even if the rest is
  empty. A crashed session should still leave the voice and the person behind. Create
  the other files the first time something belongs in them, not all at once.
- Nothing goes in these files that the user did not say or that the evidence does not
  show. A fact you guessed is written "[to confirm]"; a fact copied from another state
  file is written "[from VALUE.md]"; research you found is cited. Only the user's or a
  stranger's actual words go in quotation marks; words the user reports someone else
  said are written as reported. Green and red lines you propose are marked as
  proposals until the user confirms them.
- Update files as things happen, not at the end of the session.
- Never overwrite a line a human wrote without saying so. Append, date, and keep the
  old line when a value changes (monthly climbs and KPI readings are histories). An
  unfilled template placeholder is not a line a human wrote; fill it and say so.
- Keep the human-readable shape; these files are read by people on Monday mornings,
  not just by you.
- Quote strangers word for word. Paraphrasing a no is how founders lose the reason.
- Dates in ISO format (`2026-10-14`). Names in full.

## `VALUE.md` (project root)

The index and the 40,000 ft view. Sections, in order:

1. Title and one-line description of what is being built.
2. **Voice**: explicit or professional, with the date chosen.
3. **Building**: software, deck, company, running a company; what comes first.
4. **Stage**: the product stage (pre-POC, POC, MVP, PMF, scaling) and the phase and
   step on the rails, with the date it was reached, and the onboarding climbs still
   open (by number, with the moment each is waiting for). When the user runs a
   company, one row per initiative.
5. **The person**: name, age, where, one line of story, their sentence in quotes, who
   pays, who decides. The first person from `PEOPLE.md`.
6. **The outcome**: what done looks like for them, in their words afterwards.
7. **At stake**: the unround number in money and in evenings, the date (and the time
   only if the user gave it), the line not to be crossed, who has been told.
8. **The one number**: the primary KPI with green and red lines and today's value; the
   list of names still using and paying at twelve months.
9. **Altitude and focus**: the current altitude, the one thing in progress, how many
   nines and who gets hurt.
9b. **How it is built** (software only): where it runs, the one command that reads
   the logs, how people get in, what it is measured with, what is bought and why,
   and how many lanes of work are open (`engineering.md`).
10. **Value score**: the twelve-rail checklist, the rogue list with dates, and the
    history, one line per session (`score.md`).
11. **Open action items**: copied from `ACTIONS.md`, unchecked ones only.
12. **Standing rules**: instructions the user pasted that address "your human".
13. **Files**: links to the `value-coding/` files.

## `value-coding/PEOPLE.md`

One section per real person this is for: full name, age, where they live, story in two
lines, their sentence in quotes, picture (path or link), role (uses, pays, decides),
what they do today instead, how the user knows them, date added. The first one is the
face at the top of every screen; the top bar rotates through all of them.

## `value-coding/STRANGERS.md`

A table of every reply, in rounds: date, name, whether they are a stranger, a friend,
an investor, or "assumed, never asked" (a number the user counted on without asking),
what was shown (the offer and the price), the reply word for word, whether they
paid. Friends and investors stay in the table, flagged, and do not count.
Under it, "Reasons for no" grouped by reason, each pointing at the action item or
backlog ticket it became. Under that, interview notes, each marked with whether the user watched the person
(in person, screen shared) or only heard them: what they did step by step while
watched, where they stalled in the product, what is annoying, what takes too
long, what they do instead, what they are embarrassed to admit, the words they used.

## `value-coding/METRICS.md`

KPIs as in `metrics.md`: label, unit, green, red, lower-is-better, primary, vanity, and
dated readings with the step. Then goals: label, target, unit, due date, checkpoints
with dates and evidence.

## `value-coding/MENU.md`

Ten lines, numbered, one sentence each, with the slide name in the user's voice and
the step on the rails each came from. Then "Shown to": the stranger who saw it first
and what they did.

## `value-coding/JOURNAL.md`

Three sections. **Daily**: one line per day, date and the one-word answer, with a note
when three bad answers in a row changed the day. **Monthly, 40,000 ft**: one block per
month with the three answers (value proposition, why, who for) and a line on what
changed since last month and whether it was decided. **Rituals**: when each weekly and
monthly ritual last ran (random ticket test, name-and-question pass, ten names,
monthly climb, viral sweep). Also the fear and the kitten verdict from onboarding,
dated.

## `value-coding/ACTIONS.md`

Checklist. Each item: one sentence, one thing to do, a person's name, a date. Grouped
by session date. Done items get checked and kept; a partly done item is checked with a
note and its remainder carried as a new item with a new date. Items with no name or no
date are not action items; rewrite them before saving. The names are ones the user
gave; when a human was named in the session, at least one item is theirs.

## `value-coding/HUMANS.md`

The roster (role, name, how to reach them, what they have done before), the four gate
rows (first, build, release, scale) each in one of the states listed in `humans.md`,
the consult log (date, moment, who was named, outcome), and briefs written for humans.

## `value-coding/BACKLOG.md` and `value-coding/ROADMAP.md`

The board and the roadmap, as described in `planning.md`: tickets with a person, a
question, an altitude, nines, a status, a human, and a test; milestones with goals,
dates, gates, and the evidence that marks them done. Derived mostly by you, corrected
by the user, moved as the work moves.

## `value-coding/RESEARCH.md`

What the user fixed (geography, demographics, language, currency, channel, regulated)
and what you found yourself, each with a source and a date; estimates marked.

## `value-coding/DECISIONS.md`

Parked ideas with the date and the reason (altitude, ticket test, stress test), and
the condition that brings them back (three strangers asked, retention goal met). The
random ticket test results: date, the item drawn, the question asked, the user's
answer, what happened.
Stress-test results: the claim, who argued against it, whether it survived, open holes.
Decisions handed to the person who says the user is wrong: the options, what they
picked, what happened.
