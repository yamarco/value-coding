# Onboarding: climb, dive, climb

Run this the first time you meet a project with no `VALUE.md`. Nothing in this skill
works if the person, the outcome, and the stake are not written down, and a user who
will not answer these questions is about to spend a year building for the mirror. But
a user who answers thirty questions and gets nothing back stops answering, and they
are right to. So the interview is not a block. It runs the way the book runs: a short
climb of three or four questions, then a dive, a piece of real work that uses the
answers, then the next climb.

The rule that decides what gets asked when: **a batch of questions has to change what
you do next.** If the answers would not alter the next piece of work, the questions
wait for the moment they would. The voice is always first and alone. Nothing gets
built before the person and the outcome exist. Everything else moves to the moment it
earns.

How to run it:

- Three to five questions per climb, in the user's voice, then wait. Listen to the
  whole answer before pushing, then push once. Do not accept "everyone", "SMBs", a
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
2. What are you building: software, a pitch or deck, a company, or are you running an
   existing company and using tech inside it? Which comes first?
3. Where is it today: an idea, something built, something built several times, or a
   live business with customers?
4. Has a stranger ever paid for anything connected to this?

**Dive.** Read whatever exists in the project and say what you found. Give the
altitude reading for what they asked. If the answer to 3 was "built several times",
say the pattern out loud: each version better built than the last, none sold first.
Create `VALUE.md` with the voice, the name, what is being built, and the stage.

## Climb 2: the person

The first slide of everything, and the question the book opens and closes with. Do
not build until there is a human here.

1. Who is this for? One real person: full name, age, where they live, two lines of
   story. Not a segment. Someone a room could imagine meeting, and imagine saying no.
2. What do they need, in words they would say out loud? One sentence, theirs.
3. What do they do today instead? The spreadsheet, the group chat, the phone call
   every evening, nothing. The "instead" is the real competitor.
4. If the one who pays is not the one who uses it, who pays, and who decides?

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
2. Is that a problem they have now, or an opportunity they did not have? If neither
   can be named, say which bucket is left.
3. What is the price, and when does a stranger first see it? A number and a date. If
   there is neither, those are the first two action items.
4. For an existing business: what is the number today?

**Dive.** The first real deliverable, scoped to the smallest thing a stranger can be
put in front of and pay for: the opening of the deck, the first slice of the spec, the
plan skeleton with the price and the pay-now step near the top, the message to the
first stranger. For an internal tool, the stranger is a user who did not ask for it,
the price is the date they switch off the spreadsheet, and the pre-sell is their
written commitment. Write the outcome to `VALUE.md`. From here on the user has
something in hand, and the remaining climbs come at the moments they earn.

## Climb 4: the stake

**When:** the first time the user is about to commit real effort: the first build
session, the first money spent, the first public claim. Not before.

1. How much are you willing to lose for this one thing? Money if they have it, a real
   unround number; evenings if not. Round numbers are how people avoid looking at it;
   ask for the real one once.
2. Is there a line you will not cross, whatever happens?
3. Who have you told? A stake nobody knows about is a hobby.

If both numbers are zero, say what that means: not a business yet. Ask them to decide
today whether to raise the stakes or stop.

**Dive.** Write the stake, the line, and the date to `VALUE.md`. Continue the work.
Open `ACTIONS.md` with the first items, each with a name and a date.

## Climb 5: the humans

**When:** the first gate or the first risky decision comes into view: a build about to
start, money or personal data about to be touched, a decision the user has circled for
a session. Read `humans.md` first.

1. Who tells you, to your face, when you are wrong, and stays? If no name comes in ten
   seconds, that is the first action item.
2. Who has shipped something strangers paid for, and will read the person and the
   outcome before the build? If it is you, say so.
3. Who has built and run something like this before, and been woken up by it? If it
   is you, say what you have not done before.
4. Who sells, who does the money, who does the terms, and who has lived the problem?

**Dive.** Write the roster to `HUMANS.md`; if one name answers every question, write
"all roles" and say that every gate will carry a note that a second human was absent.
Write the brief for the human the current moment calls for, the gate row in its
state, and the consult log line. Mark on the deliverable where that human should look.

## Climb 6: the numbers

**When:** release one is being scoped, or a plan is being written for an existing
business.

1. Which handful of numbers would tell the truth about this idea? For each, a green
   line above which it is working and a red line below which it stops. One is
   primary, the number they will wake up to.
2. Numbers about them, not about you. Flag any vanity number they insist on, keep it,
   flagged, and ask what someone would do to hit it without creating the value.
3. The first goal they could miss, with a date.

**Dive.** Write `METRICS.md` and the primary KPI into `VALUE.md`. Put the KPIs and the
dated goals into the deliverable where they belong: the metrics section of the spec,
the parties and ask slides, the roadmap's "now" column.

## Climb 7: nines, altitude, and the fear

**When:** the thing is about to be shown to a stranger, or the user is stuck.

1. How many nines does this need, and who gets hurt if it fails at fewer? Three is a
   website, five is a bank, seven is a plane. One request can hold two builds with
   different nines; split them.
2. What altitude are you at right now, and should you be there? Give your reading
   first.
3. What is the one thing in progress? One. Six is flapping, not diving.
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
