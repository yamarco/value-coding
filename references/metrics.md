# Metrics: KPIs, goals, and the one number

Opinions are cheap and everyone has one. Numbers are expensive because to get one you
have to count something real: how many strangers said yes, how many paid, how many
came back. Most ideas die without anyone counting, so nobody learns why. Every idea
gets its KPIs before it gets a line of code.

## KPIs

Each KPI in `METRICS.md` has:

- a label, in the user's words;
- a unit;
- a **green line**: at or beyond this it is working;
- a **red line**: at or beyond this, in the wrong direction, the idea stops;
- whether lower is better;
- whether it is **primary**: the one number the user wakes up to, shown at the top of
  `VALUE.md`;
- whether it is **vanity**: a number about the user, not about the person. Shown, never
  trusted, never used to open a gate;
- readings, dated, with the step on the rails they came from.

Numbers about them: interviews confirming the pain, pitch-to-deposit conversion,
active households, daily check-ins answered, churn, margin per customer, strangers who
paid at the real price, still paying at twelve months. Numbers about you: sign-ups,
page views, downloads, followers, waitlist, story points, tickets closed. The second
kind tells you the door works, not whether anyone wanted what was behind it.

## Goals

Goals are numbers the user can miss, with dates: strangers asked by week three,
strangers who paid, interviews recorded, letters signed, deposits paid, customers live
in release one, paying customers by month three, renewals. They go on the roadmap and
get checked off by evidence, never by the user. When a goal is missed, that is data,
not a verdict; ask what the strangers said.

## The cobra warning

Pick a number that is not the value, hand it to smart people, and they will optimise
it with total commitment. A bounty on dead cobras produced cobra farms. Sign-ups when
the value is people who come back; story points when the value is a customer who
noticed; tickets closed when the value is the thing working; speed when the value is
the other person getting there. Every dashboard has a cobra in it somewhere. When the
user proposes a KPI, ask what someone would do to hit it without creating the value,
and if the answer is easy, it is a cobra.

## Validation is not feedback

Feedback is information about the thing. Validation is information about the user.
They feel the same and do opposite jobs. Point every piece of feedback at the intended
value for the named person: did this do that for them, yes or no, and what did they do
next? If it lands on the value, it is data. If it lands on the founder, it is
validation or an attack, and neither says what to build.

## The question behind every feature

Every feature comes with a question about a specific human: "will Rebecca stop
abandoning at the address form", not "will engagement go up". Ship the smallest thing
that answers it, watch what she does, not what she says in the survey, then adjust.
If the question cannot be named, the dashboard is open and nobody is in the room.

## The one number

Of what was built, how much is still used and still paid for a year later, by name.
Not how many started; how many survived twelve months in a market. It is not a number,
it is a list of people who paid and are still there. Keep it at the top of `VALUE.md`
and add names only when the twelve months have passed.

## Data on day one

Before building anything for an existing business, ask for access to the data and
look. Within an hour of real numbers you will usually find three things the user has
been telling you the opposite of, and each is a feature about to not be built. Put the
chart next to the person and read both; the dashboard says you doubled, the humans say
they are tired, and both are true.
