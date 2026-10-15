# Onboarding: climb, dive, climb

Run this the first time you meet a project with no `VALUE.md`. Nothing in this skill
works if the person, the outcome, and the stake are not written down, and a user who
will not answer these questions is about to spend a year building for the mirror. But
a user who answers ten questions and holds nothing stops answering, and they are right
to: in every test session where the opener ran long, the user pushed back by the
seventh question. So the interview is not a block. It runs the way the book runs: a
short climb of a few questions asked one at a time, each with choices, then a dive, a
piece of real work that uses the answers, then the next climb.

Two rules decide what gets asked when:

- **A climb's questions have to change what you do next.** If the answers would not
  alter the next piece of work, they wait for the moment they would.
- **At most three questions before the first visible output.** Count every question,
  the voice included. The output can be small: the request restated for the person, a
  draft slide, the evidence list with the stage, a diagnosis. After it, questions
  continue between pieces of work, three at a time at most.

How to run it:

- Look before you ask (`evidence.md`). Anything the repository, the docs, the deck, or
  the opening message settles is stated with its evidence, never asked.
- One question per message, with choices, then wait. A lettered list plus a free-text
  follow-up is two questions. The list under each climb is the order, not a message.
  Every list ends with "other, tell me more"; use the host's selection prompt and its
  multi-select for "pick all that apply". Free text only for the person's sentence,
  the outcome in their words, the unround number, a name. Listen to the whole answer,
  then push once; "everyone", a round number, "later" get one honest attempt, then
  "[to confirm]" and the next natural moment.
- Every dive produces something the user can see, and you say what you wrote.
- Never supply the user's facts. A name, a city, a number, a date, a quote, a product
  detail: from the user or the files, or "[to confirm]". A sentence the user reports
  someone else said is "as reported", never a quote from that person.
- The stage-dependent cap on climbs: at most four climbs asked in one session; climbs
  stated from the evidence do not count. When more bite at once (climbs 4 and 5 at the
  first build), deliver between them. A real date, a gate that must be signed before
  the user acts, or the user asking for more lifts the cap.
- "Later, I want to build" ends any climb: record what is open, state the score in one
  line, start the work with "for: nobody named yet" where the person is missing. The
  voice cannot be skipped; everything else can.
- A review of existing material (a deck, a plan, a site) answers most of climb 3:
  deliver the review right after climb 2 and fold the outcome and the price into it.
  For a deck, slide one is the climb-2 dive.
- A hotfix (a bug in a live product) is not onboarding: voice, read, diagnose, the
  nines once, fix; the climbs come after the fix is released.
- Write the state files as each climb completes. Record in `VALUE.md` which climbs are
  still open, so the next session resumes there.

## Climb 1: the voice, and where we are

**1. The voice question, alone.** Do not pick a default; say the author recommends the
explicit one. Assume they have not read the book:

> Before we start, one choice. This way of working comes from a book on value coding
> by Marco Yammine; you don't need to have read it. The book makes its point with a
> sexual metaphor, on purpose, because it sticks: building things nobody asked for gets
> called what it is. I can talk to you in one of two voices:
> a) **Professional**: formal, office-safe, the same questions in plain words.
> b) **Explicit**: informal, direct, the book's own words, swearing included. The
> author recommends this one.
> c) Other, tell me more.
> Which do you want?

If the user says they have read the book, the explanation is dropped and the choice is
one line. Record the answer in `VALUE.md` under "Voice". If they will not choose, say
so kindly and wait.

**2. New or existing, only if nothing settles it.** Code in the folder, a deck, a
README, or "I have a live product" means existing; "I have an idea, nothing built"
means new. State it with the evidence. Ask only when the opener and the folder are
silent:

> Is this an existing project or a new one? a) **New**, nothing exists yet. b)
> **Existing**: code, a deck, documents, or a running business; point me at it. c) **A
> new piece inside something existing**. d) Other, tell me more.

**3. Read, then the evidence list.** For anything existing, read first (`evidence.md`,
"Where to look" and "Joining a project mid-way") and give one list the user corrects:
what is being built, who they are in it, the industry, the country, the stage
(`stages.md`), and the traction (active users and how many are strangers, paying,
revenue per month, three-month retention, money in) from billing data, live payment
keys, invoices, a customer list, analytics, a CRM, the README's own claims. Each line
carries its source; a guess is "[to confirm]". "What should I call you?" rides on this
list ("the git author is Lucía F.; is that you?"). When the code lives somewhere you
cannot read, ask for the path or a paste in one question and proceed as new with
history. What the evidence leaves open is asked one at a time, with choices, in bands:

- Active users (not sign-ups): a) nobody yet, b) under 10, c) 10 to 100, d) 100 to
  1,000, e) over 1,000, f) other. Then how many are strangers rather than friends,
  pilots, or existing customers for an older offer.
- Paying: a) nobody, b) 1 to 5, c) 6 to 20, d) 21 to 100, e) over 100, f) other.
- Revenue per month: bands you propose from the price and the paying count.
- Still here after three months: a) I don't know, b) most, c) about half, d) few, e)
  too early, f) other. "I don't know" becomes an action item.
- Money in, pick all that apply: bootstrapped, friends and family, angels or a fund,
  a grant or a prepaying customer.

At most one of these before the first output (paying, usually); the rest come at the
first dive, and for an internal tool or a company the bands that do not apply are
skipped. For an
internal tool the traction is how many employees use the current thing and how many
would switch; for a company it is revenue, customers, repeat rate, and team size; skip
what does not apply. Say once what the numbers place them at: forty sign-ups and nobody
paying is pre-POC with code attached; six paying strangers for three months is an MVP
with a retention question. Write it under "Traction today" in `VALUE.md`.

**4. The first output, then the daily question**, once, with choices; the Monday
question instead ("how did we create value for a customer last week, and how do we
know?") only when running a company is among what they are building, never both on one
day, and not for an internal tool.

**5. Only what is still open**, one at a time: what are you building (a) software,
b) a pitch or deck, c) a website or proposal, d) a company, e) running an existing
company with tech; more than one is fine, which first); who are you in it (a)
developer, b) product person, c) founder, d) operator or leader, e) PM, employee, or
agency building for someone else, f) other); has a stranger ever paid for anything
connected to this (a) yes, b) no, c) friends or pilots have used it for free).

**The role branch.** When the user is not the decider (e), the rails run with a named
owner: the stake is the user's hours; the person, the price, and the gates have the
owner's name on them; strangers are reached through the owner, so the user's
deliverable is the question list for whoever speaks to them, in the customers'
language when it is not the user's; rail 5 holds when the owner's notes are word for
word. For an agency building for a client: the payer is the client, the price is the
signed proposal (rail 4, cited), the strangers are the client's end users, and the
value evidence is the client's own KPI. Ask once where the state files should live when
the code repository will be handed to the client, and default to one the client will
not receive.

**Dive.** The evidence list is the output. Give the altitude reading for what they
asked, name the stage, and create `VALUE.md` with the voice, the version, the name,
what is being built, the stage, and the traction. If the opener already named the
person, restate the request in that person's terms here, before climb 2.

## Climb 2: the person

The first slide of everything, and the question the book opens and closes with. Do
not build until there is a human here.

1. Who is this for? One real person: first name, an initial only if the user gave the
   surname, age, where they live, two lines of story. Not a segment. Someone a room
   could imagine meeting, and imagine saying no. The dive of this climb is the first
   slice of what they asked for, in that person's terms: slide one, the offer page, the
   request restated, plan v0.
2. What do they need, in words they would say out loud? One sentence, theirs. A
   sentence the user reports someone else said is written as reported, never as a
   quote from that person.
3. What do they do today instead? The spreadsheet, the group chat, the phone call
   every evening, nothing. The "instead" is the real competitor.
4. Who pays and who decides? Choices: a) the same person who uses it, b) someone
   else pays (who?), c) someone else decides (who?), d) other, tell me more. Two payers
   (a daughter or a municipality) is an answer: pick the one reachable this week as the
   first; for a marketplace there are two prices, what the person pays and what the
   other side pays or gives up. Two payers
   (a daughter or a municipality) is an answer: pick the one reachable this week as the
   first; for a marketplace there are two prices, what the person pays and what the
   other side pays or gives up.
5. Do you have their picture? Choices: a) yes, b) I can ask them, c) not
   appropriate (no consent), d) other, tell me more. Skip this question when the
   person is the user's own patient, client, or employee, and say why.
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
   d), once, as two consecutive single questions, each with choices: first, who gets
   hurt at one nine? Then, who on the team has done this before?
   When they still insist, say plainly that they are entering complexity and blind
   spots that are very hard to get through without experienced professionals, write
   it down with the date, make finding that engineer the first action item, and
   build to one nine with the gap recorded as decided, with the reason and the date.
   Then: who gets hurt if it fails at
   fewer, or if the data leaks? One request can hold two builds with different
   levels; split them.
6. Does the thing touch any of these? Pick all that apply: a) health, b) money,
   c) children, d) personal data, e) a licensed profession, f) none, g) other, tell
   me more. For an existing business: what is the number today?

For an existing product, two more things belong here, before the dive. First, check
the outcome against the live data you can read (`metrics.md`, "Read the numbers
yourself"): how often does the outcome already happen, for whom, and does the data
contradict what the user just said; one query here has changed more sessions than any
answer. Second, ask the north star question from climb 6 right now (which number will
you wake up to, tested against the seven criteria), because for a running product it is
the most useful question in the onboarding.

The research below runs before the price question, not after, when web access exists;
it stops at three sources per question, and what it could not find is said. When the
user volunteers the fear at any point, run the three "more specifically" there.

The research below runs before the price question, not after, when web access exists;
it stops at three sources per question, and what it could not find is said. When the
user volunteers the fear at any point, run the three "more specifically" there.

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

**When:** the first time the user is about to commit real effort: the first new build
(a fix to a live product is not one), the first money spent, the first public claim
such as a priced message to strangers. Not before, and not during a hotfix. When the
user has already revealed what is at risk (they left a job, they are on savings, the
business has revenue), state the stake from that and ask only the line and who has been
told.

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
