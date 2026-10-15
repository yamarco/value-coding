# Engineering: the coding half of value coding

Value coding is two words. The first half is the person, the stranger, and the price.
The second half is the code, and the code has rails of its own. They come from the
same place as the rest of the method: everything created must be maintained, speed to
a stranger beats polish, and the model is only as good as what it can see. This
reference is for the first build session and for every build session after it. Read
`building.md` first for the nines, the tests, and the smallest stack; this file is
what sits underneath them.

## The three questions at the first build

Ask these once, one at a time, with choices, at the first build session, after the
board (`planning.md`) has been shown and before the first line is written. Look first
(`evidence.md`): a repository usually answers two of the three. Write the answers to
`VALUE.md` under "How it is built". Do not re-ask them; when the stage changes, they
come back on their own.

1. **Where does it run?** Choices: a) in the browser, on any device (the default),
   b) a native app in the stores, c) hardware or a device in the field, d) already
   decided, here is what exists, e) other, tell me more. If they answer b, push back
   once (below).
2. **How do people get in?** Choices: a) no login yet, a link is enough, b) a code
   by email or SMS, c) sign in with Google, Apple, or Microsoft, d) a password, e)
   other, tell me more. If they answer d, say why not (below).
3. **What are you paying someone else to do?** Choices: a) nothing yet, b) payments,
   c) email or SMS delivery, d) a specific integration someone has asked for by name,
   e) other, tell me more. Anything beyond b and c gets the build-over-buy question.

Everything else in this file you decide yourself and say in one line; the user
corrects it.

## Web first, and the native app can wait

When someone asks for a native app before a stranger has paid, the honest answer is
almost always a website that behaves like an app: a progressive web app, installable
from the browser, working offline where it matters, with push notifications on the
platforms that allow them. Say why in the user's terms:

- In the early stages the thing that matters most is how fast a change reaches a
  stranger. A web app deploys in a minute and the stranger sees the fix on their
  next visit. A store app waits for a review, then waits for the stranger to update.
  Every early user error and every blind spot the user has not found yet gets fixed
  ten times faster on the web.
- A native app is two codebases, or one codebase and a framework, plus two stores,
  two review processes, two sets of certificates, and a developer account on each.
  All of that is maintenance ahead of retention.
- The stranger does not care where it runs. They care whether the outcome happens.
  "Will it be in the App Store" is a question the user asks; the person on slide one
  has not asked it.

Push back once, with the reasons, and ask the question that settles it: what does
the person on slide one need that a browser cannot do? Real answers exist: a sensor,
Bluetooth to a device, background location, a camera pipeline the browser cannot run,
a store presence that a paying customer has named as the way they buy. If the answer
is one of those, build native and write the reason in `DECISIONS.md`. If the answer is
"it feels more real" or "investors expect it", that is building for the mirror; say
so, build the web app, and park the native app with the condition that brings it back
(a stranger who paid asking for it, or a device that needs it).

The same applies to desktop apps, browser extensions, and anything else that puts a
store or an installer between a change and a stranger.

## Logs the agent can read

The single most useful thing a user can give their model is the ability to see what
the running thing is doing. A model that can read the logs finds the bug; a model
that cannot guesses, and the user pays for the guesses in tokens and evenings. So
from the first deploy:

- **One place for every log**, server and client, with one command the agent can run
  to read them: the last few minutes, a filter by a request id or a person, the
  errors only. Write the command in `VALUE.md` under "How it is built". A managed
  logging service with a command-line client is fine; a file the agent can tail is
  fine at 80%; logs that only a human can see in a web console are not accessible
  to the agent and do not count.
- **Structured, not prose.** One line per event, machine-readable, with a timestamp,
  a level, the request or session id, the person or account where that is allowed,
  and what happened. A model reads a thousand structured lines faster than a page of
  free text.
- **Every request gets an id**, and the id travels: into the response, into the
  client log, into the error the user sees ("something went wrong, reference
  ab12"). A stranger who writes "it broke" with a reference is a bug the agent can
  find in a minute.
- **The client logs too.** Browser errors, failed requests, and the steps that led
  there are sent to the same place, with the same ids. A failure a stranger saw and
  the server never heard about is the kind that costs a customer.
- **Native apps and devices.** When the thing runs on someone else's phone or on a
  device in the field, the logs are the only eyes the user has. Buffer locally, ship
  when there is a connection, never lose a crash. Every crash and every handled error
  reaches the same place as the server logs, with the device, the version, and the
  steps before it. A fleet of devices with no logs is a fleet of support calls.
- **Before you say "fixed", read the log.** The test proves the outcome; the log
  proves the fix reached the person. After a deploy, read the errors for the path
  you touched. "No new errors in the last hour on the payment path" is a sentence;
  "should be fine now" is a feeling.

When the agent cannot read the logs at all, that is a ticket at the top of the
backlog, before the feature that was asked for, because every later ticket is cheaper
once it exists.

## Exceptions are handled, never swallowed

Logs are only as good as what reaches them, and most of what never reaches them was
caught and thrown away. The rules:

- **Nothing is caught silently.** An empty catch block, a "pass", a swallowed promise
  rejection, a default value returned on failure without a log line: each one hides a
  bug from the agent and from the user until a stranger finds it. Every catch logs
  what happened, with the id and the context, before it decides what to do.
- **Fail at the boundary, with a plain message.** Validate what comes in from the
  outside (a form, an API, a device, a file) at the edge, once, and reject it with a
  message the person can act on. Inside the boundary, trust the data and let a
  surprise fail loudly rather than limping on with half a record.
- **The person sees a sentence and a reference, never a stack.** "We could not save
  your booking, reference ab12, nothing was charged." The stack goes to the log.
- **Unhandled is still logged.** A global handler on the server, in the browser, and
  on the device catches whatever nobody expected, logs it with everything it can,
  and tells the person something true. The handler is the first thing built after
  the log command exists.
- **Retries have a count, timeouts have a number.** A retry loop without a limit and
  a request without a timeout are the two bugs that take a system down at 3 a.m.
  with nothing in the log.
- **At 80% this is still the rule.** The 80% level skips handling for inputs nobody
  sends; it does not skip logging what actually happens. The difference is one line
  per catch, and it is the cheapest line in the codebase.

## Measure from the first stranger

The person on slide one will not tell the user what they did; the data will. Before
the first stranger sees it, not after:

- **Analytics on every page and every step that matters**, with a tool like Google
  Analytics or any similar one. The events are named after the tickets' questions:
  "address_form_abandoned", not "click_7". The primary KPI in `METRICS.md` should be
  readable from the analytics without a developer.
- **Session recordings**, with a tool like Hotjar or any similar one, from the first
  stranger. Watching ten strangers struggle with a form teaches more than a hundred
  survey answers, and it is the only way to see the blind spots the user cannot
  describe because they cannot see them.
- **Errors tied to sessions.** The log reference and the recording should meet: a
  recording where the stranger gave up at an error, and the log line that says why.
- **Privacy is a boundary, not an afterthought.** Mask what the person types into a
  field that holds personal or payment data, say in plain words on the site that
  recording happens, and ask the lawyer in `humans.md` when the geography or the data
  (health, children, finance) calls for it. Record behaviour, not secrets.

For an internal tool, the same applies with the employees as the strangers: the
first week of recordings is where the real workflow shows up, and it is never the
one in the spec.

## Login without a password

A password form is where strangers leave. It is also a data breach waiting for a
leak, and a support queue of resets the user will answer by hand. So:

- **No login until it is needed.** A link with a token, a code in an email: the
  first stranger can often get the outcome without an account at all.
- **When login is needed, it is passwordless.** A one-time code by email or SMS, a
  magic link, or sign in with Google, Apple, or Microsoft. Pick the one the person
  on slide one already uses every day: a phone number and a code for someone on the
  move or in a shop, a corporate sign-in for someone at a desk in a company that has
  one, a magic link for everyone else.
- **A password only when a stranger has asked for one** or a regulation requires it,
  and then alongside the passwordless option, never instead of it. Write the reason
  in `DECISIONS.md`.
- **The login is a step in the money path and is tested like one.** The test fills
  in the code the way the person would.

## Data model and migrations

The data model is the part of the codebase that is hardest to change later and the
one most often built for a future that never comes. Rules:

- **Model the outcome, not the industry.** Tables for what the person on slide one
  does and what they pay for. The entities a consultant would draw for the whole
  sector are parked until a stranger asks for them.
- **Fewer tables, plain names, one owner per fact.** Every table has a reason that
  traces to a ticket. Nothing is normalised for a case that does not exist yet.
- **Migrations are small, forward-only, and one at a time.** Each migration does one
  thing, has a name that says what, and is applied before the next one is written.
  Two migrations in flight at once from two lanes of work is the most common way a
  build lands in a day of reconciliation; the one-lane rule below exists partly for
  the schema.
- **Add, backfill, switch, remove: four steps, never one.** A column is added, the
  data is filled, the code switches, and only then is the old column dropped, each
  step released and logged separately, so that any step can be rolled back without
  losing a row.
- **The data outlives the code.** A backup that has been restored once, sized to the
  nines: at 80%, a nightly copy the user has seen come back; at one nine, a restore
  that has been rehearsed and timed; at two nines, the human in `humans.md` has signed
  the recovery plan.

## Build over buy, with the short list of exceptions

The old advice was to buy anything that was not the core of the business, because
building was expensive. With a model in the loop, building most things is cheaper
than integrating them, and the integration is the part that keeps costing: a vendor
that changes its API, a price that rises with usage, a webhook that fails silently,
an account that gets suspended, a feature the user needs that the vendor does not
have. Every integration is a dependency with a bill and a support queue attached, and
the user loses control of a piece of the product they will have to explain to a
customer.

So the default is to build and keep control, and to avoid integrations at the start.
The exceptions are short, and they are the things where building is both hard and
dangerous:

- **Payments.** Card handling, invoicing, tax: buy it, from the provider the user's
  geography trusts. Nobody builds this at any number of nines.
- **Email and SMS delivery.** Sending at scale, deliverability, phone-number
  verification: buy the pipe, keep the logic.
- **Sign-in with a provider** (Google, Apple, Microsoft) when the person already lives
  there; it is a login, not an integration.
- **A specific integration a paying stranger has named**: their calendar, their
  accounting tool, their practice management system. Then it is a ticket with their
  name on it and a question it answers, built after they have paid.
- **The thing that would get someone hurt if the user built it wrong**: encryption,
  certificates, a medical or financial rule engine. That is also a human in
  `humans.md`.

For everything else (a CRM, a CMS, a form builder, a scheduling tool, a chat widget,
a feature-flag service, a "platform" for anything) the question is the same as for a
feature: which person asked, and what is the question it answers. When the answer is
"it would be faster", say what the integration costs in control and maintenance over
a year, and offer the version that builds the 20% of it the person needs. Write the
decision down either way.

## One lane, not a swarm

People running many agents at once on one codebase believe they are going faster.
Most of the time they are not. Each agent builds on a version of the code that the
others are changing, the same file gets touched from three sides, the data model
forks, and the user spends the afternoon they thought they had saved reconciling
conflicts, re-reading code they did not write, and re-running tests that pass alone
and fail together. Parallel work in progress has the same cost as parallel ideas in
progress, and the method's answer is the same: one thing at a time.

The workflow is a pipeline, and it is sequential:

1. **One ticket in progress.** The board shows it; nothing else is being changed.
2. **Say what will change, in one line,** which files and which table, before
   touching them.
3. **Build it in the smallest step that can be tested.**
4. **Run the tests, read the logs,** and fix what they say, before moving on.
5. **Commit with the ticket's name and question**, so the history reads like the
   board.
6. **Move the ticket, pick the next.** The next one starts from the code as it is
   now, not as it was when the plan was written.

When the user wants to run several agents at once, push back once, with the cost
above, and ask what is being parallelised. The cases where parallel work is cheaper
than sequential are narrow: work that touches different repositories, or different
parts of one codebase with no shared files, no shared tables, and no shared
interfaces, each with its own ticket and its own tests. Research, reading, and
reviewing parallelise well; writing to the same codebase does not. When parallel
work goes ahead, give each lane a named owner, a disjoint set of files, and a merge
order, and say that the schema belongs to one lane only. When the user insists on
more than that, it is a rail skipped: note it in `VALUE.md` with the date and the
reconciliation time, so the cost is visible the next week.

The same discipline applies to the user's own habits: a feature started while the
previous one is half-tested, a refactor opened in the middle of a ticket, a second
branch to "try something". Each is a second thing in progress, and the board says
so.

## What goes in `VALUE.md`

Under "How it is built", one line each, filled by the agent from the evidence and
corrected by the user:

- **Runs on:** web (installable) by default; native or device only with the reason
  and the date.
- **Logs:** the one command that reads them, server and client.
- **Login:** none, code by email or SMS, provider sign-in; a password only with a
  reason.
- **Measured with:** the analytics tool and the recording tool, and the date they
  went live.
- **Bought:** the short list, each with the reason.
- **Lanes:** one, or the named exception with its reconciliation cost.
