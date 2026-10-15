# The value score

Users skip steps. They will refuse the stake, build before a stranger has seen a price,
sign their own gate, leave tickets without a name. The skill lets them; it is a
reminder, not a gate, and a user who is blocked stops using it. But a user who skips
a rail should see it every time they sit down, in one line, as a number, the way the
daily question is one word. That is the value score.

## Twelve rails, one point each

| # | Rail | Held when |
|---|------|-----------|
| 1 | The person | `PEOPLE.md` has one real person with a sentence in their words |
| 2 | The outcome | `VALUE.md` has the outcome in the person's terms, supplied by the user, as they would describe it afterwards |
| 3 | The stake | an unround number in money or evenings, a line not to cross, dated |
| 4 | A price in front of strangers | at least one stranger has seen a number, dated, in `STRANGERS.md` |
| 5 | Strangers' words | at least three replies from strangers recorded word for word |
| 6 | Numbers that tell the truth | KPIs with green and red lines, one north star that passes the tests in `metrics.md`, in `METRICS.md`, and once anything is released, a read path (a query, an API, a command) by which the agent reads the north star itself |
| 7 | A human who signs | the one who says they are wrong is named, and the current gate is signed by someone other than the user, or pending with a named human actually asked; "signed alone", "unsigned", and "not yet asked" do not hold it; "passed before the rails" holds it for that gate |
| 8 | One thing in progress | `BACKLOG.md` shows exactly one ticket in progress per person |
| 9 | A name and a question on every ticket | no ticket in progress or next has a question mark in both columns; later and parked tickets may carry one |
| 10 | Tests prove outcomes | every ticket marked done (released to staging or production with its test green) at one nine or more has a test, and every ticket at 80% has one test for the outcome or "manual: how"; once anything is deployed, the agent can read its logs with the one command in `VALUE.md`; show which half is missing when one is; code that was live before the rails holds it "by history" |
| 11 | The daily question | answered today, and the last three answers are not all the bad one |
| 12 | Action items with names and dates | last session ended with them, and yesterday's were checked |

## Reached, held, decided, rogue

The score is **held out of reached**, with the number not yet reached beside it:
"7/9 · 3 not yet reached". A rail is reached when its moment has passed:

| Rail | Reached when |
|------|--------------|
| 1, 2 | climb 2 and 3 have been asked, or the user said "later" to them |
| 3 | the first new build, money spent, or public claim (climb 4's moment) |
| 4 | a plan, a deck, a page, or a build exists that a stranger could see |
| 5 | a stranger has seen the price or the thing |
| 6 | release one is scoped, or an existing business is being planned |
| 7 | any gate has come into view |
| 8, 9 | a backlog exists |
| 10 | a ticket is done |
| 11, 12 | the second session |

Each reached rail is in one of four states:

- **Held.** The condition in the table above is met now.
- **Held by history, cited.** A running business meets it with evidence that predates
  the rails: paying customers hold rail 4, a signed proposal holds it for a client
  build, code live with tests holds rail 10. Write the source next to it. The score
  does not treat a running company like day one.
- **Decided, with reason and date.** The user consciously overrode the rail and gave a
  reason you wrote down: a round stake with the accountant's number due on a date; one
  nine accepted after the two-nines pushback; ops-first for a dated absence. Neither
  open nor rogue; it comes back when the reason expires, and it is listed as "decided"
  not "rogue".
- **Rogue.** Declined after the moment arrived, with no reason, or a reason that has
  expired. Listed by name with the date and the moment it returns.

A climb skipped with "later, I want to build" leaves its rails open, not rogue. For a
deck-only, document-only, retention, or client-build session, rails that cannot apply
(a stranger who sees a price in a pure retention initiative) are "not applicable", said
once, and left out of both numbers. The score is first shown at the end of the first
session, not in the opener of first contact. The display in `VALUE.md` matches: held,
reached, not reached, decided (with reasons), rogue.

## The rating: how well are you value coding, 1 to 10

The score counts rails in use. It says nothing about whether the user is actually
doing the thing: talking to strangers, building from their noes, staying out of the
weeds, selling on selling days. So every now and then, not on a schedule the user
can predict, give them a rating from 1 to 10 of how well they are value coding right
now, in one line, with the one reason and the one thing that would raise it:

> How you're value coding right now: 4/10. Three weeks of building, no stranger has
> seen the price since the 2nd. One thing: send the three messages in `ACTIONS.md`.

What it weighs, roughly: are strangers being watched and asked (the biggest weight);
does what is being built trace to their noes; is the user at the altitude and stage
the evidence calls for, or in the weeds; is the one number moving; are the rails
held. A 9 or 10 is a user with paying strangers, building from their words, out of
the weeds, with the score high; a 2 is a month of code and nobody asked. Say it in
the voice; in the explicit voice the book's framing is allowed, once.

Cadence: not every session and not on a fixed day. Roughly every fourth or fifth
session, and additionally when something notable happens: a stranger pays, a rail
goes rogue, a week passes in the weeds, a stage changes. Never twice in a week,
never less than once a month. Write each rating in `JOURNAL.md` with the date, so
you can check both limits and show the trend when the user asks. If the rating
dropped two points since the last one, say so and say why. It is a reminder, said
once, with no lecture after it; the number and the one thing are the whole message.

- **The opener, every session, one line**, right after the altitude tag:
  "Value score 7/9 · 3 not yet reached · decided: the stake (accountant's number due
  2026-10-31) · rogue: the build gate (since 2026-10-02)."
  In the explicit voice the book's word is allowed once: a low score is a
  masturbation score, and the user chose it.
- **`VALUE.md`**, under its own heading, with the twelve rails as a checklist, the
  rogue list, and the history: one line per session with the date and the score, so
  the user sees it move.
- **At every gate** and whenever the user skips another rail: the new score, the rail
  that just went rogue, and nothing else. No lecture. The number is the lecture.
- **When it rises**: say so, once, in one line. People keep rails they can see
  holding.

## What it is not

It is not a gate and not a grade of the user. It is a count of how much of the method
is currently in use, so that "I'll do that later" has a visible cost. A score of 4/12
with a product that strangers pay for is a founder who is winning despite the method,
and you say that too. A score of 12/12 with no paying stranger is a dossier, and the
one number at the top of `VALUE.md` still reads zero; the score never replaces it.
