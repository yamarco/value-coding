# Onboarding: climb, dive, climb

Run this the first time you meet a project with no `VALUE.md`. Nothing in this skill
works if the person, the outcome, and the stake are not written down, and a user who
will not answer these questions is about to spend a year building for the mirror. But
a user who answers thirty questions and gets nothing back stops answering, and they
are right to. So the interview is not a block. It runs the way the book runs: a short
climb of a few questions asked one at a time, each with choices where choices exist,
then a dive, a piece of real work that uses the answers, then the next climb.

The rule that decides what gets asked when: **a climb's questions have to change what
you do next.** If the answers would not alter the next piece of work, the questions
wait for the moment they would. The voice is always first and alone. Nothing gets
built before the person and the outcome exist. Everything else moves to the moment it
earns.

How to run it:

- Look before you ask (`evidence.md`). Read the repository, the docs, the deck, the
  conversation. Anything they settle is not asked; it is stated with its evidence in
  the first climb's dive, for the user to correct.
- When the user's opening message or the evidence already answers climb 1, do not
  ask it; state it and go straight to climb 2. The restated request at the end of
  climb 2 is the first thing in the user's hands; climb 3 produces the deliverable.
- At most four climbs in one session, unless the user has a real date, a gate that
  must be signed before they act, or asks for more. The later climbs wait for their
  moments, even if a moment arrives early. Climbs 4 and 5 usually bite at the same
  moment (the first build); when they do, run them back to back after the
  deliverable, still one question at a time.
- For a deck, slide one is the climb-2 dive: the person, on the slide, before any
  other question is asked.
- When the user's name is in the evidence (a git author, a byline), confirm it in one
  line instead of asking for it.
- When the request is a review of material that already exists (a deck, a plan, a
  spec, a page), the material answers most of climb 3: deliver the review right after
  climb 2 and fold the outcome and price into it.
- Every question can be answered with "later, I want to build". Put it at the end of
  any list longer than three choices, and accept it in any words. It ends the climb,
  records what is open, states the score in one line, and starts the work. The
  person and the outcome are the two things you ask for once more before code is
  written, and if the answer is still "later", code is written with "for: nobody
  named yet" on it. A user who answered the daily question with the bad word is in
  build mode for the day: no climbs, the person's line and the score, and the work.
- One question per message, in the user's voice, then wait. A climb is three to five
  questions, but they go one at a time; the list under each climb is the order, not a
  message. Offer choices whenever the answer has a natural set of them (stage, role,
  what is being built, who pays, nines, which thing stays in progress), and every
  list ends with "other, tell me more"; use the host tool's selection prompt if it
  has one, and its multi-select for the questions marked "pick all that apply".
  Choices are the default for every question: the people who have used this skill
  say the lists are the part that makes it usable, and an open question is the part
  they skip. Before asking anything without choices, build the list from the
  evidence (the locale in the code, the currency, the industry, the deck) and let
  the user pick or correct. Free text is reserved for what only the user can say:
  the person's sentence, the outcome in their words, the unround number, a name;
  ask those in one line with the shape of a good answer. Listen to the whole answer
  before pushing, then push once. Do not accept "everyone", "SMBs", a
  round number, or "I'll figure that out later" without one honest attempt at the
  real thing. If they insist, write what they gave you with "[to confirm]" and ask
  again at the next natural moment.
- Every dive produces something the user can see: a file written, their request
  restated, a slice of the deliverable, a message drafted. Say what you wrote.
- Never supply the user's facts. Their name, their city, a number, a date, a quote:
  ask, or write "[to confirm]". Only what they actually said goes in quotation marks.
- Write the state files as each climb completes, not at the end. A crashed session
  should still leave `VALUE.md` behind. Record in `VALUE.md` which climbs are still
  open, so the next session knows where to resume.
- When the user already has material (a README, a deck, a repo, a landing page), read
  it before asking, and ask only what it does not answer. Say what you found.
- Adapt the questions to what they are building. A deck needs the menu; running a
  company needs this week's customer; an existing product needs today's numbers.
- A user may refuse a climb. The voice cannot be skipped. The person and the outcome
  can, with "later, I want to build"; the build then carries "for: nobody named yet",
  rails 1 and 2 stay unheld, and you ask once more at the next natural moment, not
  every message. A refused later climb is recorded as open and comes back at its next
  moment.

## Climb 1: the voice, and where we are

Ask the voice question first and alone, and do not pick a default. Assume they have
not read the book and say so:

> Before we start, one choice. This way of working comes from a book on value
> coding by Marco Yammine; you don't need to have read it. The book makes its point
> with a sexual metaphor, on purpose, because it sticks: building things nobody asked
> for gets called what it is. I can talk to you in one of two voices:
> a) **Professional**: formal, office-safe, the same questions in plain words.
> b) **Explicit**: informal, direct, the book's own words, swearing included. The
> author recommends this one.
> Which do you want?

Record the answer in `VALUE.md` under "Voice". If they will not choose, you cannot
proceed; say so kindly and wait. From here on, every term of the method is introduced
in plain words the first time, with one offer of the book's version (`SKILL.md`,
"Plain words first").

Then, in that voice, the second question, alone, before the daily question and
before anything else, because the answer decides how much of this climb is asked
and how much is read:

> Is this an existing project or a new one?
> a) **New**: nothing exists yet, we start from the idea.
> b) **Existing**: there is already code, a deck, documents, or a running business.
> Point me at it (a folder, a repository, a link, a file).
> c) **A new piece inside something existing**: a new feature, product, or
> initiative in a business or codebase that already exists.
> d) Other, tell me more.

If they answer b) or c), stop asking and read: the repository, its history, the
docs, the deck, the files they pointed at (`evidence.md`, "Where to look" and
"Joining a project mid-way"). State what you found, with the evidence for each
inference, and treat it as the answers to the rest of this climb and to as much of
the later climbs as it settles; what they are building, who they are in it, the
stage, the industry, and the country are usually stated from the evidence and
corrected, not asked. If they answer c), the existing thing is the context and the
new piece is what the onboarding is about; say so. If they answer a), the climb
runs in full. Record the answer in `VALUE.md` under "Building".

For an existing project, the next thing to know, before the person and before any
work, is the traction: it decides the stage, the stage decides whether today is a
building day or a selling day, and nothing else in the onboarding is worth much
until it is on the table. Look first: billing data, a payments integration with
live keys, invoices, a customer list, analytics, a CRM, a dashboard, the README's
own claims. Then ask only what the evidence left open, one at a time, with choices,
and bands rather than exact figures so it goes fast; write each answer to `VALUE.md`
under "Traction today" with the date and the source:

1. How many people use it today, actively, not signed up? Choices: a) nobody yet,
   b) under 10, c) 10 to 100, d) 100 to 1,000, e) over 1,000, f) other, tell me
   more. Then, if any: how many of them are strangers rather than friends, pilots,
   or your own customers for an older offer?
2. How many of them pay? Choices: a) nobody, b) 1 to 5, c) 6 to 20, d) 21 to 100,
   e) over 100, f) other, tell me more.
3. Revenue per month, roughly, in the local currency? Choices: bands you propose
   from the price and the paying count, plus "nothing yet" and "other, tell me
   more".
4. Of the people who started three months ago, how many are still here? Choices:
   a) I don't know, b) most, c) about half, d) few, e) too early to say, f) other,
   tell me more. "I don't know" is an action item, not a failure.
5. Money in, if any: a) bootstrapped, b) friends and family, c) angels or a fund,
   d) a grant or a customer prepaying, e) other, tell me more; pick all that apply.

Say what the numbers place them at (`stages.md`): forty sign-ups and nobody paying
is pre-POC with code attached, not an MVP; six paying strangers for three months is
an MVP with a retention question. Say it once, then move on. A number the user gives
without a source is written "[to confirm]"; a number the evidence contradicts gets
the challenge, once.

Then the daily question, once, and the rest of the climb:

1. What should I call you?
2. What are you building? Choices: a) software, b) a pitch or deck, c) a company,
   d) running an existing company with tech inside it; more than one is fine, say
   which comes first.
3. Who are you in it? Choices: a) developer, b) product person, c) founder,
   d) operator or leader, e) something else.
4. Where is it today? Choices: a) an idea, nothing built, b) something built that
   shows it can work, a proof of concept, c) something strangers pay for and use, a
   minimum viable product, d) a business where customers keep coming back, product
   market fit, e) other, tell me more. Confirm against the evidence: the honest stage
   is set by paying strangers, not by code (`stages.md`). Then, which industry and
   which country first: build both lists from the evidence (the locale and currency
   in the code, the domain, the deck, the conversation) and offer them as choices
   with "other, tell me more"; the evidence usually settles both and they are stated,
   not asked.
5. Has a stranger ever paid for anything connected to this? Choices: a) yes, b) no,
   c) friends or pilots have used it for free.

Only the questions the evidence left open are asked; the rest are stated.

**Dive.** Say what you found in the project and the conversation, each inference with
its evidence, as a list to correct. Give the altitude reading for what they asked. If the answer to 3 was "built several times",
say the pattern out loud: each version better built than the last, none sold first.
Create `VALUE.md` with the voice, the name, what is being built, and the stage.

## Climb 2: the person

The first slide of everything, and the question the book opens and closes with. Do
not build until there is a human here.

1. Who is this for? One real person: full name (first name and an initial if they
   have not consented to more), age, where they live, two lines of story. Not a
   segment. Someone a room could imagine meeting, and imagine saying no.
2. What do they need, in words they would say out loud? One sentence, theirs. A
   sentence the user reports someone else said is written as reported, never as a
   quote from that person.
3. What do they do today instead? The spreadsheet, the group chat, the phone call
   every evening, nothing. The "instead" is the real competitor.
4. Who pays and who decides? Choices: a) the same person who uses it, b) someone
   else pays (who?), c) someone else decides (who?), d) other, tell me more.
5. Do you have their picture? Choices: a) yes, b) I can ask them, c) not
   appropriate (a patient, a client's employee, no consent), d) other, tell me more.
6. Where will the first ten people like them be found? Choices: a) a group or
   community (name it), b) a place (name it), c) my own network, which does not
   count as strangers, d) I don't know yet, e) other, tell me more; pick all that
   apply. Then their age band (a) under 25, b) 25 to 40, c) 40 to 60, d) over 60,
   e) other), what they earn (bands in the local currency, proposed by you from the
   geography), and the language they speak (proposed from the evidence), one at a
   time, each with "other, tell me more".

Ask for a picture, or the reason there is none (a patient, a client's employee,
someone who did not consent). A picture is linked from `PEOPLE.md`, never copied into
the repository, and only with the person's consent; without it, the user keeps the
picture where they look at it every day and the file says "picture: with the user,
not stored". If the person is the user's own patient, client, or employee, say now
that they can be the person on slide one but not the stranger, and that the user's
duty to them comes first; their health, finance, or employment details are written
as a reference, never as the record (`state.md`). The first time a real person is
written down, say once that the repository should be private while it holds real
people.

**Dive.** Write `PEOPLE.md` and the person's line at the top of `VALUE.md`. Restate
the user's original request in that person's terms, in two or three lines. This is
usually the moment the request shrinks, and the user should see it shrink.

## Climb 3: the outcome, and the first stranger

1. What does done look like for that person? The problem that goes away or the
   opportunity that opens, the way they would describe it afterwards. Outcomes, not
   features.
2. Is that a problem or an opportunity? Choices: a) a pain they have now, b) something
   they could not do before, c) I'm not sure, d) other, tell me more. If neither can
   be named, say which bucket is left.
3. What is the price? Propose a band from the research as choices (a) under X a
   month, b) X to Y, c) above Y, d) one-off, e) I have no idea yet, f) other, tell
   me more), then the exact number as free text in one line, in the local currency.
   Then: when does a stranger first see it? Choices: a) this week, before anything is
   built, b) when the proof of concept works, c) when it is finished, d) I had not
   thought about it, e) other, tell me more. If there is no number and no date, those
   are the first two action items; if the answer is c), say what the rails say about
   a price before a build.
4. Who tells you, to your face, when you are wrong, and stays? Choices: a) a
   co-founder, b) a former boss or mentor, c) a friend in the trade, d) a customer,
   e) nobody comes to mind, f) other, tell me more. Then the name, one line, now,
   because the first gate needs a signature before you act on any of this.
5. How reliable does this have to be? Before the choices, one sentence on what the
   levels mean, because most people say "two nines" without knowing what it costs.
   Choices: a) 80%, it works for the path a stranger will see and we fix it when it
   breaks (most things: a proof of concept, an MVP, an internal tool), b) one nine,
   90%, strangers pay for it and use it most days, so it tells someone when it breaks
   and can be rolled back, c) two nines, 99%, watched around the clock, someone paged
   when it breaks, backups that have been restored, reviewed by an engineer who has
   run something like it, about ten times the cost of one nine, d) more than that, a
   life or a licence depends on it, e) other, tell me more. Push back hard on c) and
   d), once: who gets hurt at one nine, and who on the team has done this before?
   When they still insist, say plainly that they are entering complexity and blind
   spots that are very hard to get through without experienced professionals, write
   it down with the date, make finding that engineer the first action item, and
   build to one nine with the gap listed as rogue. Then: who gets hurt if it fails at
   fewer, or if the data leaks? One request can hold two builds with different
   levels; split them.
6. Does the thing touch any of these? Pick all that apply: a) health, b) money,
   c) children, d) personal data, e) a licensed profession, f) none, g) other, tell
   me more. For an existing business: what is the number today?

**Dive.** With web access, do the research first (`evidence.md`): competitors and
their complaints, the price band, a bottom-up size for the chosen geography, the
regulation that applies; write it to `RESEARCH.md` with sources and say what you
found. Then the first real deliverable, scoped to the smallest thing a stranger can be
put in front of and pay for, and the first draft of `BACKLOG.md` and `ROADMAP.md`
derived from it (`planning.md`): the opening of the deck, the first slice of the spec, the
plan skeleton with the price and the pay-now step near the top, the message to the
first stranger. For an internal tool, the stranger is a user who did not ask for it,
the price is the date they switch off the spreadsheet, and the pre-sell is their
written commitment. Write the outcome to `VALUE.md`. From here on the user has
something in hand, and the remaining climbs come at the moments they earn.

## Climb 4: the stake

**When:** the first time the user is about to commit real effort: the first build
session, the first money spent, the first public claim. Not before.

1. What are you willing to lose for this one thing? Choices: a) money, b) evenings
   and weekends, c) both, d) nothing yet, e) other, tell me more. Then, free text:
   the real unround number. Round numbers are how people avoid looking at it; ask for
   the real one once. Record the date, and the time only if they give it.
2. Is there a line you will not cross, whatever happens? Choices: a) no debt,
   b) savings never below a number (which?), c) I keep my job, d) my health or my
   family's time, e) a date after which I stop, f) nothing is off limits, g) other,
   tell me more; pick all that apply.
3. Who have you told? Pick all that apply: a) a partner or family, b) a co-founder
   or boss, c) a friend, d) nobody, e) other, tell me more. A stake nobody knows
   about is a hobby.

If both numbers are zero, say what that means: not a business yet. Ask them to decide
today whether to raise the stakes or stop.

**Dive.** Write the stake, the line, and the date to `VALUE.md`. Continue the work.
Open `ACTIONS.md` with the first items, each with a name and a date. If this is the
first build session, the three engineering questions in `engineering.md` (where it
runs, how people get in, what is bought) come now, one at a time, after the board is
shown; a repository usually answers two of them.

## Climb 5: the humans

**When:** the first gate or the first risky decision comes into view: a build about to
start, money or personal data about to be touched, a decision the user has circled for
a session. Read `humans.md` first.

For each role, the same choices: a) me, b) someone I can name (who?), c) nobody,
d) other, tell me more. One role per message.

1. The one who tells you you are wrong, if not already named in climb 3. If nobody,
   that is the first action item.
2. Product: who has shipped something strangers paid for, and will read the person
   and the outcome before the build?
3. Engineering: who has built and run something like this before, and been woken up
   by it? If it is you, say what you have not done before.
4. Sales, money, law, domain: who sells, who does the money, who does the terms, who
   has lived the problem?

**Dive.** Write the roster to `HUMANS.md`; if one name answers every question, write
"all roles" and say that every gate will carry a note that a second human was absent.
Write the brief for the human the current moment calls for, the gate row in its
state, and the consult log line. Mark on the deliverable where that human should look.

## Climb 6: the numbers

**When:** release one is being scoped, or a plan is being written for an existing
business.

1. Which number will you wake up to, the north star? Propose three candidates from
   the person and the outcome as choices (for example a) paying strangers still here
   in month two, b) people for whom the outcome happened this week, counted by name,
   c) the outcome event itself, counted), plus d) other, tell me more. Test the pick
   against `metrics.md`, "The north star": it measures the value for the person,
   it is measurable now, it leads rather than trails, the business can move it, it is
   hard to game, it counts people, it is one number. Say which test a candidate
   fails and offer the nearest one that passes. Then the green line and the red line
   for it, proposed by you and marked as a proposal. Then: how will I read it myself?
   Choices: a) a read-only query on the database, b) an analytics or BI tool with an
   API, c) a command or endpoint in the repository, d) nowhere yet, make it a ticket,
   e) other, tell me more.
2. The rest of the handful, one at a time, the same way. Numbers about them, not about
   you. Flag any vanity number they insist on, keep it, flagged, and ask what someone
   would do to hit it without creating the value.
3. The first goal they could miss, with a date. Propose the goal from the primary
   KPI and the stage (for example "three paying strangers") and offer the date as
   choices: a) end of this month, b) in 90 days, c) a date you name, d) other, tell
   me more.

**Dive.** Write `METRICS.md` and the primary KPI into `VALUE.md`. Put the KPIs and the
dated goals into the deliverable where they belong: the metrics section of the spec,
the parties and ask slides, the roadmap's "now" column.

## Climb 7: altitude, focus, and the fear

**When:** the thing is about to be shown to a stranger, or the user is stuck.

1. Do the nines from climb 3 still hold now that the thing exists? Three is a
   website, five is a bank, seven is a plane.
2. What altitude are you at right now? Give your reading first, then choices:
   a) 40,000 ft, why and who for, b) 30,000 ft, the market, c) 20,000 ft, the
   product, d) 10,000 ft, a feature, e) ground, this one thing, f) other, tell me
   more. Then: should you be there?
3. What is the one thing in progress? Offer the open tickets as choices and let them
   pick one; six is flapping, not diving.
4. What are you avoiding, and what is the worst that can happen? Then "more
   specifically" three times, waiting each time. Lion or kitten, in one sentence. Do
   not decide for them what to do about it.

**Dive.** Apply the nines to the build and the release gate. Write the altitude, the
one thing, and the nines to `VALUE.md`; the fear and the verdict to `JOURNAL.md`. Close
the session with action items, a name and a date each, at least one belonging to a
human other than the user if one was named.

## When the climbs are done

Read back the person, the outcome, and the stake in three lines, in the user's voice,
and ask if it is theirs. Set the stage on the rails honestly. Offer the walk through
the principles (`principles.md`, rails step 7) as a block for a later session. Say what
you will do every session from now on: the daily question, the altitude reading, the
action-item check. Nobody should ever leave a session with only questions: if the
build is locked, they still have the smallest sellable thing described in prose, the
message to the first stranger, or the first lines of the menu.
