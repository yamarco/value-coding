# Look before you ask

Most of what onboarding asks, a model with access to the project can already see.
Asking a developer whether they are a developer, after reading their repository, is
the kind of question that makes a skill feel like a form. So the first move on any
project, before the first climb, is to read what is there, say what it tells you and
how you know, and ask only for what the evidence does not settle. The user corrects
you; that is faster than answering from scratch, and it shows them you looked.

The rule: **infer when you have evidence, state the evidence, and ask when you do
not.** An inference without evidence is a guess, and a guess written into `VALUE.md`
is the fabrication problem in a nicer coat. "You seem to be a solo developer: one
author in the git log, 212 commits since March, no CI" is evidence. "You seem
technical" is not.

## Where to look

Read these when they exist, in roughly this order, and stop when the picture is clear:

- **The conversation so far**, including anything the tool gave you about the user
  (an email domain, a project name, earlier sessions).
- **`VALUE.md` and `value-coding/`**, if they exist: that is the whole picture, and
  you are not onboarding.
- **README, docs, a deck, a landing page, a pitch, a one-pager** in the project. The
  product, the market, the industry, the geography, the claims about customers.
- **Package manifests and lockfiles** (`package.json`, `pyproject.toml`, `go.mod`,
  `Gemfile`, `Cargo.toml`, `composer.json`, and their equivalents): languages,
  frameworks, how many of each, how old the dependencies are, whether there are test
  runners and linters, whether there is a payments, auth, or analytics SDK.
- **The repository shape**: one repo or several, one language or several, services or
  a monolith, a `tests/` directory and how full it is, CI configuration, deploy
  configuration, infrastructure files, migrations, feature flags.
- **Git history**: how many authors, how long it has been going, commit cadence,
  whether commits mention customers, tickets, or only features; whether anything was
  ever tagged or released.
- **Data and analytics**, if the user gives access: real numbers about what people do
  beat every answer in the interview (see `metrics.md`, "Data on day one").
- **Tests and monitoring**: how many nines the thing already has, in practice, is
  visible in whether anything proves it works.

## Joining a project mid-way

Most people will switch this skill on in the middle of something, not at the start.
A project that has been going for months has already answered many of the questions
the climbs ask; it just answered them in commits, tickets, docs, and deleted code
instead of in `VALUE.md`. Treat that history as answers, cite it, and let the user
correct it, instead of asking a person with a year of work behind them to start from
"who is this for".

- **Decisions already made**: a changelog, architecture notes, a `docs/` folder, an
  ADR directory, commit messages that say why. Each becomes a line in
  `DECISIONS.md` with its date and source, not a new question.
- **The person and the outcome**: customer names in testimonials, support threads,
  interview notes, a persona document, the words on the landing page, the first
  commit message. State the best candidate with its source and ask only whether it
  still holds.
- **Stage on the rails**: pricing pages, payment integrations with live keys, invoices,
  signed contracts, a customer list, analytics with real users. Place the project by
  that evidence and list the steps the history skipped as open holes.
- **The backlog and roadmap**: an issue tracker export, GitHub or GitLab issues, a
  `TODO.md`, a Trello or Notion board, a roadmap slide. Migrate what exists into
  `BACKLOG.md` and `ROADMAP.md`, keep the original identifiers, add the person and the
  question to each item (or a question mark), and do not start a second board.
- **The strangers**: reviews, support tickets, churned users, sales call notes, a CRM.
  Their words, with dates and sources, go in `STRANGERS.md` as what the history
  already heard.
- **The numbers**: analytics, billing data, a dashboard, a spreadsheet. The current
  values of the KPIs, and the one number, come from there before anyone is asked.
- **The humans**: authors in git, reviewers, names in docs, the contractor's invoices.
  The roster starts from who is already there.
- **Pivots and dead ends**: renamed features, deleted directories, an abandoned
  rewrite, a branch nobody merged. Each is a lesson the rails would otherwise have to
  re-teach; name them.

Say, in the first dive, "this project has already answered these, here is where", and
spend the user's time on what the history left open. A user who sees a year of their
own decisions read back correctly trusts the next question.

## What the evidence tells you

| Question in onboarding | Evidence that can answer it |
|---|---|
| Developer, product person, founder, operator? | Who authored the code; whether the docs are product or technical; whether there is a deck but no code, or code but no README; how the user phrases the request. |
| Solo or a team? | Authors in git, reviewers in CI, names in docs. |
| Startup, established business, running a company with tech? | Age of the repo, presence of customers or contracts in docs, invoices or pricing pages, a company name with a history you can check. |
| Industry, product category, geography, language, currency | README and landing page, locale files, currency symbols in code, regulatory words (HIPAA, GDPR, PCI, a national health or tax authority), addresses, time zones. |
| Stage on the rails | Any stranger evidence in the repo (testimonials, pricing page with a buy button, a payments integration with real keys configured, a waitlist); or none. |
| Nines achieved today | Test count and coverage, CI passing or absent, monitoring, error tracking, a changelog, uptime history. |
| Built several times before? | Abandoned branches, a `v2/`, an old repo linked from the README, a rewrite commit. |
| What they do today instead | Spreadsheets in the repo, exports, an import script from another tool, a competitor's name in the code. |

Present the inferences as a short list the user can correct, each with its evidence,
before the first climb's questions: "Here is what I can see. Tell me where I am
wrong." That list is one message with one question at the end of it (is this right?),
not a list of questions. Then ask what is still open, one at a time. A user who confirms five inferences has
answered five questions in one word.

## Challenge the answers

The interview is not a form to be filled. When an answer is a claim, test it against
the evidence you have, once, and say what you found:

- "Everyone", "SMBs", "busy professionals": a body with no face. Ask for the one.
- A market number with no source: ask where it came from, and offer to find the real
  one (see below).
- "Nobody else does this": name the competitor you found in two minutes, or the
  "instead" (the spreadsheet, the phone call) that is the real competitor.
- "It has to be perfect", "two nines": say what two nines costs in plain words, then
  name the person who gets hurt at one nine and the engineer who has done it before.
- "They loved it", "they said they would use it": did you watch them do it, on
  their screen or in the room? If not, it is "said, not watched" until an interview
  with the screen shared, which is the next action item.
- "A customer asked for X", "they did not use Y": feature or teaching? Ask which,
  with choices; most of the time the stranger could not find it or did not know why
  it mattered, and that is closed with a sentence or a walkthrough, not a ticket.
- "It will spread on its own": who makes the first call.
- "I will do sales later": the build stays locked until a stranger commits.
- "I'm the PM and the dev and the sales": written down, and said out loud at every
  gate.
- A round number for the stake: ask for the real one.
- A claim that contradicts the repo (they say there are tests; there are none; they
  say it is a monolith; there are six services): say so, with the file.

Once each, with the evidence, then move on. Challenge is friction; the empathy that
carries it is the reason you give.

## Research you can do yourself

A model with web access can do in minutes what founders spend a week guessing at. Do
it before asking the user, say what you found and where, and mark estimates as
estimates. Never present a number you found as a number the user gave you.

- **Competitors and alternatives**: who else is at this, what they charge, what their
  customers complain about in reviews and forums, and what people use instead.
  Complaints about a competitor are evidence of the pain, not evidence that the
  user's thing solves it.
- **Pricing**: the price band the person on slide one already pays in, for this or
  for the "instead".
- **Market size, bottom-up**: how many people like the person on slide one exist in
  the chosen geography, from public statistics, times what one of them will part
  with. Prefer a small real number to a large imaginary one, and show the arithmetic.
- **Regulation and data**: what rules apply to the data, the money, or the people
  involved in the chosen geography (health, financial, personal data, consumer
  protection, licensing). This feeds the lawyer moment in `humans.md`.
- **Timing**: what changed recently in the market, the platforms, the law, or the
  cost of building, and whether the user is standing in it or reading about it.
- **The field**: is this the boring 80% (energy, shelter, health, transport,
  infrastructure, safety, education) or the crowded 20%? Who else is over this field?

Research is not stranger evidence. It tells the user where the field is; it does not
tell them whether one person will pay. Ten strangers still have to be asked.

## The questions research needs

Research needs the user to fix a few things first, so these join the climbs:

- **Geography**: which country or city first, and why that one. A product for Norway
  is not a product for Europe.
- **Who, demographically**: age band, role, income band, language, where they live,
  what they already pay for; derived from the person on slide one, not instead of
  them.
- **Language and currency** of the product, the price, and the first strangers.
- **Channel**: where the first ten strangers will be found, by name of the place.
- **Regulated?** Does the thing touch health, money, children, personal data, or a
  licensed profession.

Write what is fixed to `VALUE.md` under the person and the market; write the research
to `value-coding/RESEARCH.md` with sources and dates, so nobody has to find it twice.
