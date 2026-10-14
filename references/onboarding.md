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
- One question per message, in the user's voice, then wait. A climb is three to five
  questions, but they go one at a time; the list under each climb is the order, not a
  message. Offer choices whenever the answer has a natural set of them (stage, role,
  what is being built, who pays, nines, which thing stays in progress), and every
  list ends with "other, tell me more"; use the host tool's selection prompt if it
  has one. Default to choices; fall back to free text only when no sensible set of
  options exists. Free text is for
  what only the user can say. Listen to the whole answer before pushing, then push
  once. Do not accept "everyone", "SMBs", a
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
- A user may refuse a climb. They cannot refuse the first three (voice, person,
  outcome) and still get a build; say so kindly and keep asking at the next moment.
  A refused later climb is recorded as open and comes back at its next moment.

## Climb 1: the voice, and where we are

Ask the voice question first and alone, and do not pick a default:

> This skill speaks in one of two voices. The book it comes from uses sex as the
> metaphor for the whole method, on purpose: "building features" sounds like work,
> and the book's word for building alone sounds like what it is, which is why people
> remember it. **Unfiltered** uses the book's own words, swearing included.
> **Filtered** asks the same questions in office-safe words. The author recommends
> unfiltered; it is the version that sticks. Which do you want?

Record the answer in `VALUE.md` under "Voice". If they will not choose, you cannot
proceed; say so kindly and wait. Then, in that voice, the daily question, once, and
the rest of the climb:

1. What should I call you?
2. What are you building? Choices: a) software, b) a pitch or deck, c) a company,
   d) running an existing company with tech inside it; more than one is fine, say
   which comes first.
3. Who are you in it? Choices: a) developer, b) product person, c) founder,
   d) operator or leader, e) something else.
4. Where is it today? Choices: a) an idea, b) something built, c) something built
   several times, d) a live business with customers. Then, free text: which industry,
   which country first.
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
   count as strangers, d) I don't know yet, e) other, tell me more. Then, free text:
   their age band, what they earn, the language they speak.

Ask for a picture, or the reason there is none (a patient, a client's employee,
someone who did not consent). If the person is the user's own patient, client, or
employee, say now that they can be the person on slide one but not the stranger, and
that the user's duty to them comes first.

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
3. What is the price, in which currency, and when does a stranger first see it? Free
   text: a number and a date. If there is neither, those are the first two action
   items.
4. Who tells you, to your face, when you are wrong, and stays? Free text, one name,
   now, because the first gate needs a signature before you act on any of this.
   Choices if they stall: a) a co-founder, b) a former boss, c) a friend in the
   trade, d) nobody comes to mind, e) other, tell me more.
5. How many nines does this need? Choices: a) two, a prototype a stranger can see,
   b) three, a website people pay for, c) five, money or personal data, d) seven, a
   life depends on it, e) other, tell me more. Then: who gets hurt if it fails at
   fewer, or if the data leaks? One request can hold two builds with different nines;
   split them.
6. Does the thing touch any of these? Choices: a) health, b) money, c) children,
   d) personal data, e) a licensed profession, f) none, g) other, tell me more. For an
   existing business: what is the number today?

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
2. Is there a line you will not cross, whatever happens? Free text.
3. Who have you told? Choices: a) a partner or family, b) a co-founder or boss,
   c) nobody, d) other, tell me more. A stake nobody knows about is a hobby.

If both numbers are zero, say what that means: not a business yet. Ask them to decide
today whether to raise the stakes or stop.

**Dive.** Write the stake, the line, and the date to `VALUE.md`. Continue the work.
Open `ACTIONS.md` with the first items, each with a name and a date.

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

1. Which number will you wake up to? Propose three candidates from the person and
   the outcome as choices (for example a) paying strangers, b) people who come back
   in month two, c) the outcome event itself, counted), plus d) other, tell me more.
   Then the green line and the red line for it, free text or proposed by you and
   marked as a proposal.
2. The rest of the handful, one at a time, the same way. Numbers about them, not about
   you. Flag any vanity number they insist on, keep it, flagged, and ask what someone
   would do to hit it without creating the value.
3. The first goal they could miss, with a date. Free text.

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
