# Planning: the agent's own backlog and roadmap

Most people building with a model execute with no plan at all: prompt, screens, next
prompt. The model can plan better than that on its own, and the rails need it to,
because a build with no backlog has no tickets to carry a name and a question, no
item for the weekly random ticket test, and no way to tell "one thing in progress"
from six. So before any build, and whenever the work changes shape, you keep two
files the way a product team would keep a board and a roadmap, and you fill most of
them yourself.

## What you work out alone

Given the person, the outcome, the stage on the rails, the nines, and whatever code
and documents exist, you can derive almost everything a board needs without asking:

- the smallest sellable thing, broken into tickets small enough to finish in one
  dive, each with the person it is for and the question of theirs it answers;
- the order: what a stranger sees first, what the money path needs, what can wait;
- what is already built, what is half built, what is dead, from the repository;
- the tests that would prove each ticket's question (`building.md`);
- which tickets need a human from `humans.md` before they move;
- the altitude of each ticket, so a board full of 10,000 ft items with no 40,000 ft
  line shows its own problem;
- the milestones: the first stranger sees it, the first stranger pays, release one,
  the first ten paying, the retention goal, each with a goal from `METRICS.md` and a
  date the user can miss.

Write the board, then show it. Ask only for what you could not derive: a date the user
controls, a priority between two things that both trace to the person, a fact about
the business you could not find. A user who corrects a drafted board has planned in
five minutes; a user asked to plan from a blank page has not.

## `value-coding/BACKLOG.md`

One table, one row per ticket:

| # | Ticket | For (person) | Question it answers | Altitude | Nines | Status | Human | Test |
|---|--------|--------------|---------------------|----------|-------|--------|-------|------|

- **Status** is one of: in progress, next, later, parked, done. Exactly one row is in
  progress per person working. A second "in progress" is flapping; say so. Agents
  count as the person running them: several agents on one codebase are several
  tickets in progress, and the pipeline in `engineering.md` is one lane.
- **For** and **Question** are never empty. A ticket without them gets a question mark
  in both and is the first candidate for the weekly ticket test.
- **Human** names who in `HUMANS.md` must look before the ticket ships, if anyone.
- **Test** names the automated test that proves the question, or "manual: <how>" when
  none is possible. At 80% one test for the outcome is enough; the column never reads
  "none".
- Parked tickets keep their row with the date and the return condition, mirrored in
  `DECISIONS.md`.
- The weekly random ticket test draws from this table and writes its result to
  `DECISIONS.md`.

## `value-coding/ROADMAP.md`

Milestones in order, each with: the name, the goal it meets (from `METRICS.md`), the
date, the tickets it needs (by number), the gate it passes (from `humans.md`), and the
evidence that will mark it done, never the user's say-so. Keep a "now" column for
what is in progress and a "parked" list at the bottom. For someone running a company,
one roadmap section per initiative.

## Keeping it alive

- Move statuses as you work, not at the end of the session. A board nobody updates is
  the board the book describes, where everything is in progress and nothing says who
  it is for.
- When the user asks for something new, it becomes a ticket with a person and a
  question before it becomes code, and it goes where it belongs in the order, which
  is usually not the top.
- A teaching ticket (a sentence on the screen, a walkthrough, an onboarding call, a
  default) is a ticket like any other, with a name and a question, and it usually
  outranks the feature it replaces.
- When strangers answer, their noes, once sorted into feature or teaching, become tickets at the top with the stranger's
  name on them.
- Every session's action items in `ACTIONS.md` point at ticket numbers where they
  concern the build.
- Once a month, at 40,000 ft, read the board against the person and the outcome. Any
  ticket that no longer traces to either is parked with the date.
