# Building: the nines, the tests, and the stack

Value coding does not stop at the gate. The build itself has rails, and they come from
the same principles: 20% of the effort carries 80% of the value, everything created
must be maintained, nobody promises 100%, and the only proof is a person who paid and
stayed. This reference is for the moment the user says "build it".

## The nines are a contract, and the contract caps the work

The nines are decided before the build (`SKILL.md`, "How many nines") and they are the
most useful number in the project, because they tell you when to stop. The scale
starts lower than people think. Eighty percent is the book's unit of "good enough":
one round of 80% is what most things need, and most of what gets built with a model
is a prototype, a tool for a few people, or a website. Each nine costs roughly ten
times the one before it, and a model that builds an 80% thing to two-nines standards
burns the user's time and tokens on quality nobody asked for.

So the default is 80%, and anything above it needs a reason the user can say out
loud:

| Level | What it is for | What done means | What you do not do |
|---|---|---|---|
| **80%** (the default: a POC, an MVP for a handful of strangers, an internal tool, a demo) | It runs the path a stranger will see and produces the outcome; the known gaps are listed in one place. | One test for the outcome, or "manual: how". | No test suite, no abstraction for a case that does not exist, no error handling for inputs nobody sends, no polish. |
| **One nine, 90%** (strangers pay for it and use it most days) | It works for the paths people actually take; it tells someone when it breaks; it can be rolled back. | The outcome and the money path have tests; it deploys from one command. | No multi-region, no load tests, no coverage targets, no rewrite for elegance. |
| **Two nines, 99%** (money moving, personal data, a business that stops when it stops) | Push back first. Ask who gets hurt at one nine, and whether there is a team that has done this before and a budget for it. Without both, the honest answer is one nine with the dangerous part parked or handed to a human. With both: an engineer who has done it before reviews it; the risky paths have tests; failures are visible before customers report them; data can be recovered. | Everything in one nine, plus the review. | No heroics; the human in `humans.md` signs the release. |
| **Three nines and up** (a bank, a hospital, a plane) | Not something to build with a model and a founder. A team, a budget, regulation, and rounds of 80% with real incidents behind them. | | |

The book's reference points for the top of the scale still stand (five nines is a
bank, seven is a plane); they are there to show how far away they are, not as
targets. When the user asks for two nines, say what it costs and ask the two
questions. When they insist, write it down, build to one nine, and mark the gap
rogue.

Write the chosen nines and what done means at that level at the top of the plan, so
every later decision can be checked against it. When the user asks for more polish
than the nines call for, say what it costs and which nine it buys. When the stakes
change (money starts moving, health data arrives), the nines change, and so does the
contract.

## Tests prove outcomes

Every feature carries the question of a named person it answers (`SKILL.md`, "A name
and a question on every to-do"). Whenever that question can be turned into an
automated test, it is. "Will Rebecca stop abandoning at the address form" becomes a
test that fills the form the way Rebecca does and checks that the order goes through.
The test is the claim made checkable; without it, "it works" is an opinion the user
will repeat to a stranger.

Rules:

- **If it can be proven automatically, prove it automatically.** Acceptance tests for
  the outcome, unit tests for the logic the outcome depends on, a smoke test for the
  deploy. Prefer the test closest to what the person does.
- **The question is the test's name.** A test file that reads like the person's
  question tells the next human why it exists.
- **No test, no claim.** If something cannot be tested automatically, say so and say
  how it will be checked instead (a human, a stranger, a log), and write that down.
- **Tests are maintained like everything else.** A flaky or dead test is deleted, not
  skipped; the weekly ticket test applies to tests too.
- **Match the nines.** At 80%, one test for the outcome a stranger will see. At one
  nine, the outcome and the money path. At two nines, every path a human in
  `humans.md` would lose sleep over, reviewed by that human.
- **Run them before you say done.** A model that reports "done" without running the
  tests has reported a feeling.

## The smallest stack

Everything you create is something the user has to maintain, explain to the next hire,
and pay rent on every week. Pick the stack by that rule.

- **One repository, one language, one database, one deploy target** unless the user
  is already working across several and asks you to. A second language or service is
  a feature nobody asked for; it needs a name and a question like any other ticket.
- **Boring technology.** The tool with ten years of answered questions over the one
  with the best launch video. The managed service over the self-hosted one until the
  bill says otherwise. The framework's defaults over a custom layer.
- **No infrastructure ahead of retention.** Microservices, queues, caches, multi-region,
  a design system, an internal platform: parked in `DECISIONS.md` until the
  retention goal is met and a number says they are needed.
- **A monolith is a feature.** One process the user can run on a laptop, read in an
  afternoon, and deploy with one command, is worth more at three nines than any
  architecture diagram.
- **Dependencies are promises.** Each one is a future upgrade, a future breach notice,
  a future afternoon lost. Add them for the 20%, not for convenience in the 80%.
- **Delete.** Dead code, unused flags, the abandoned v2 directory, the feature a
  paying customer would not miss. The random ticket test applies to the codebase.
- **Work in the user's stack.** If a stack exists, the question is never "should we
  rewrite"; a rewrite that changes nothing for the person is building for the mirror.

When you depart from any of these, say why in one line, with the person and the
question that justify it, and write it in `DECISIONS.md`.

## Releasing

The first release goes to the strangers who paid, ugly, before it feels ready, as a
question and not an answer. Before it goes:

- the release gate in `humans.md` is in a named state;
- the outcome test passes, and the deploy is one command;
- there is a way to know it broke and a way to roll it back, sized to the nines;
- the question the release asks the strangers is written down, and so is when the
  user will go back and ask it in person.

Then the release note goes to the strangers, the answers go into `STRANGERS.md` word
for word, and the next dive starts from what they did, not what they said.
