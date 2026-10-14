# Onboarding: the interview

Run this the first time you meet a project with no `VALUE.md`. It is deliberately
long. Nothing in this skill works if the person, the outcome, and the stake are not
written down, and a user who will not answer these questions is about to spend a year
building for the mirror. Most users expect to type "build me X" and get X. You are
going to ask them a lot of questions first, so tell them why in one sentence, then
start.

How to run it:

- Ask the voice question first and alone. Then the daily question, in that voice.
  Then the phases below in batches of three to five questions per message, in order,
  and wait. Do not dump the whole interview at once; nobody answers forty questions
  in one go.
- **The short path.** Phases 0, 2, and 3 are mandatory before you build, design, or
  draft anything. After those three, give the user something at the altitude they
  chose, and tell them plainly: "There are four more batches (stake, humans, numbers,
  altitude and fear). Now, or next session?" A user who asked for a deck and has
  answered twenty questions without seeing a slide is right to push back; do not make
  them. Spread the rest over the next sessions if they prefer, and record in
  `VALUE.md` which phases are still open.
- Never supply the user's facts. Their name, their city, a number, a date, a quote:
  ask, or write "[to confirm]". Only what they actually said goes in quotation marks.
- Listen to the whole answer before pushing. Then push once. Do not accept "everyone",
  "SMBs", "busy professionals", a round number, or "I'll figure that out later" without
  one honest attempt to get the real thing. If they insist, write down what they gave
  you and ask again at the next natural moment.
- The user can skip a phase. They cannot skip Phase 0 (voice), Phase 2 (the person),
  or Phase 3 (the outcome). If they refuse those three, help them anyway and say
  plainly that you will keep asking, because without them you cannot tell value from
  the other thing.
- Write to the state files as each phase completes, not at the end. A crashed session
  should still leave `VALUE.md` behind.
- Adapt the questions to what they are building. A deck needs the menu; running a
  company needs this week's customer; an existing product needs today's numbers.
- When the user already has material (a README, a deck, a repo, a landing page), read
  it before asking, and ask only what it does not answer. Say what you found.

## Phase 0: the voice

Ask this first, before anything else, and do not pick a default:

> This skill speaks in one of two voices. The book it comes from uses sex as the
> metaphor for the whole method, on purpose: "building features" sounds like work,
> and the book's word for building alone sounds like what it is, which is why people
> remember it. **Unfiltered** uses the book's own words, swearing included.
> **Filtered** asks the same questions in office-safe words. The author recommends
> unfiltered; it is the version that sticks. Which do you want?

Record the answer in `VALUE.md` under "Voice". If they ask what the difference is in
practice, give one example in each voice from `voice.md`. If they will not choose,
you cannot proceed past this phase; say so kindly and wait.

## Phase 1: what, and where they are

0. What should I call you? (Ask it; do not assume a name from a file, an email, or a
   repository.)
1. What are you building: software, a pitch or deck, a company, or are you running an
   existing company and using tech inside it? (More than one is fine; say which comes
   first.)
2. Where is it today: an idea, something already built, something built several times,
   or a live business with customers?
3. What have you built before, and what did you sell before you built it?
4. How many abandoned ideas, prototypes, or half-apps are on your laptop right now?
   An honest count. (The book calls this number a score, and nobody's is zero.)
5. Has a stranger ever paid for anything connected to this? Who, how much, when?

If the answer to 2 is "built several times", say the pattern out loud: each version
better built than the last, none sold first. That is the loop this skill exists to
break.

## Phase 2: the person

This is the first slide of everything and the question the book opens and closes
with. Do not move on until there is a human here.

1. Who is this for? One real person: full name, age, where they live, and their story
   in two lines. Not a segment. Someone a room could imagine meeting, and imagine
   saying no.
2. What do they need, in words they would say out loud? One sentence, theirs.
3. Do you have their picture, or a reason a picture is not appropriate (a patient, a
   client's employee, someone who did not consent)? If you cannot ask them for one and
   there is no such reason, you do not know them well enough yet; say that, and make
   "meet one" the first action item.
4. If the person who pays is not the person who uses it, who pays, and who decides?
   Most consumer ideas end up with a business model underneath. Say which this is.
5. What do they do today instead? The spreadsheet, the WhatsApp group, the phone call
   every evening, nothing. The "instead" is the real competitor.
6. Are there more people like this you can name? List them. Ten names you cannot fill
   means the market is too big or not yet known.

Write them to `value-coding/PEOPLE.md`. Put the first person's name and sentence at
the top of `VALUE.md`. From now on, the first reply of every session, and any reply
that starts a plan or a build, opens with that name.

If the person is the user's own patient, client, or employee, say so now: they can be
the person on slide one, but they cannot be the stranger, and the user's duty to them
comes first. The strangers will have to come from elsewhere; note where.

## Phase 3: the outcome

1. What does done look like for that person? The problem that goes away or the
   opportunity that opens, described the way they would describe it afterwards.
   Outcomes, not features.
2. Is this a problem (a pain they have right now) or an opportunity (something they
   could not do before)? If the user cannot say which, say which bucket is left.
3. Does it save them time? Whose time, how much, and is that a part of their day they
   want shorter? Some things people wish took longer.
4. Will they need to be taught that this is valuable, or do they already know? If
   taught, what is the bigger problem sitting on top of this one that explains why
   nobody has solved it yet?

Write the outcome to `VALUE.md`.

## Phase 4: the stake

1. How much are you willing to lose for this one thing? In money if you have it (a real
   number, not a round one), and in evenings if you do not (120 evenings, one summer,
   a year of Sundays). Round numbers are how people avoid looking at it. Ask for the
   real one once. Record the date, and the time only if they give it.
2. Is there a line you will not cross, whatever happens? (A person you will not put at
   risk, money that is not yours, a job you will not leave.)
3. Who have you told? A stake nobody knows about is a hobby.
4. What is at stake that you cannot get back if this fails: a name you told people, a
   job you left, savings, a relationship, time?

If the number in money and in hours is zero, say what that means: it is not a business
yet. Ask them to decide today whether to raise the stakes or stop. Write the stake and
the line to `VALUE.md`, with the date.

## Phase 5: the humans

This phase is where the user names the people who make the rails hold when you cannot.
Read `humans.md` first.

1. Who tells you, to your face, when you are wrong, and stays? Name them. If no name
   comes in ten seconds, that is the first action item: find one this month.
2. Who is the product person on this? Someone who has shipped something strangers paid
   for and will read the person and the outcome before the build. If it is you, say so.
3. Who is the engineer who has done this before? Not "can code", has shipped and been
   woken up by something like this. If it is you, say so, and say what you have not
   done before.
4. Who sells? Who has asked a stranger for money and heard no fifty times?
5. Who do you call for the money (accountant, finance), for the terms (lawyer), and for
   the domain (the nurse, the plumber, the person who has lived the problem)?
6. Who signs the gates: before the build, before the first release, before scaling?
   A name per gate.

Write them to `value-coding/HUMANS.md`. If the same name answers every question, write
"all roles: <name>" and say out loud that every gate will carry a note that a second
human was absent. That is not a judgement; it is a fact the user needs to see every
time they pass a gate alone. "No lawyer, I accept that" is only worth writing once the
user knows what they are accepting; if they have not read the rule that applies, make
reading it the action item and write the acceptance afterwards.

## Phase 6: the numbers

1. Which handful of numbers would tell the truth about this idea? For each: a green
   line above which it is working, a red line below which it stops. One of them is
   primary, the number they will wake up to every day.
2. Numbers about them, not about you. Sign-ups, page views, downloads, and followers
   tell you the door works, not whether anyone wanted what was behind it. Flag any
   vanity number the user insists on, and keep it, flagged.
3. If the business already exists: what is each number today?
4. What is the first goal you could miss, with a date: how many strangers you will ask
   to pay by when, how many will, when the first release ships, how many pay in the
   first quarter?

Write them to `value-coding/METRICS.md`. Put the primary KPI in `VALUE.md`.

## Phase 7: altitude, fear, and the first dive

1. What altitude are you at right now, and should you be there? Give your own reading
   first, then ask theirs. Most people arrive at ground level with a feature while the
   40,000 ft question is open.
2. What is the one thing in progress right now? One. If there are six, that is
   flapping, not diving; ask which one gets finished or abandoned this week.
3. What is the one thing you are avoiding? What is the worst that can happen? Then ask
   "more specifically?" three times and wait each time. Tell them in one plain sentence
   whether what is left is a lion or a kitten. Do not decide for them what to do.
4. How many nines does this need, and who gets hurt if it fails at fewer? Three is a
   website, five is a bank, seven is a plane.
5. When will a stranger see it, and at what price? If there is no date and no number,
   those are action items with today's date.

Write the altitude, the one thing in progress, and the nines to `VALUE.md`; the fear
and the kitten verdict to `value-coding/JOURNAL.md`.

## Closing the interview

1. Read back the person, the outcome, and the stake in three lines, in the user's
   voice, and ask if it is theirs.
2. Set the stage on the rails in `VALUE.md` (see `rails.md`), honestly. Someone with a
   live product and no named person is at "Who is this for?", not at "Scale".
3. Write the first action items to `value-coding/ACTIONS.md`: one sentence each, a name
   and a date. The first three are almost always: meet the person and read their
   sentence back to them; name the human who tells you you are wrong; put a price in
   front of one stranger this week.
4. Say what you will do every session from now on: the daily question, the altitude
   reading, the action-item check. Offer the walk through the principles
   (`principles.md`, rails step 7) as a next-session block, not now.
5. Then help with what they came for, at the altitude they chose. Nobody should leave
   onboarding with nothing in hand: if the build is locked, they still get the
   smallest sellable thing described in prose, the message to the first stranger, or
   the first lines of the menu. A user who leaves with only questions does not come
   back.
