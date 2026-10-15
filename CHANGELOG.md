# Changelog

The skill's version is in `VERSION` and in the `metadata.version` field of
`SKILL.md`. The agent writes the version it ran with into `VALUE.md`, so a project
can tell when the skill moved under it. Bump the minor number when a rail changes
what the agent does, the patch number for wording.

## 1.1.0 (2026-10-15)

After a graded round of twenty scenarios on 1.0.0 (81.8% with the skill, 26.0% without)
and two field reports from live sessions.

- First contact: at most three questions before the first visible output; one order
  (voice, new-or-existing only if not evident, read and evidence list with traction,
  daily or Monday question, climbs); the name rides on the evidence list; hotfix path.
- One question per message made strict: the nines pushback is two single questions,
  the book offer is a trailing sentence once per session, the daily and voice questions
  carry choices.
- "Their words only" strengthened: nothing from a git log, a profile, a persona, or
  inference is written as the user's statement; the person's sentence is "as reported"
  until heard directly, in every file.
- The score: held out of reached with the not-yet-reached count; four states (held,
  held by history, decided with reason and date, rogue); not-applicable rails.
- One definition of a stranger; the pay button at pre-POC defined; hosted checkout
  exception; secrets floor on a single box; app-wide error handler; device firmware as
  the allowed second language.
- Role branch for a PM, an employee, or an agency building for a client; existing
  frameworks used, not mirrored; live-data check and the north star right after the
  outcome for an existing product; pasted profiles rule; brief mode; state files in
  plain professional words; project rules win; where the files live.
- Deliverables beyond code: `references/deliverables.md` for websites, proposals,
  plans, and messages, with the ten-slide menu as the pattern.
- SKILL.md cut from 715 to under 500 lines; detail moved to the references.
- Evals: assertions rewritten for the new rules, a facts assertion and a
  time-to-first-output assertion on every scenario, the dental fixture gains the
  failing checkout route.

## 1.0.0 (2026-10-15)

First tagged version. Everything the skill does as of today:

- Onboarding that climbs and dives: the voice first and alone, then new or existing
  project, then traction for existing projects, then the person, the outcome, the
  stake, the humans, the numbers, the fear, each at its moment. One question per
  message, always with choices, "pick all that apply" where several are true.
- Opt-in prompt when installed globally and not invoked by name.
- Altitude tag on every answer; the value score out of twelve; the 1-to-10 rating
  every now and then.
- Stages pre-POC, POC, MVP, PMF, scaling, placed by paying strangers, with a
  stop-coding rule at each.
- Reliability: 80% default, one nine for daily-paid use, a hard stop on two nines.
- Value needs to be taught: feature or teaching on every customer ask.
- Watch them, do not take their word: screen-shared customer interviews.
- The north star tested on seven criteria; KPIs the agent reads itself; weekly
  numbers and monthly traction readings.
- The coding half: web first, logs the agent can read, exceptions never swallowed,
  analytics and session recordings, passwordless login, data model and migrations,
  build over buy, one lane, end-to-end tests, one-ticket releases, three isolated
  environments, secrets in `.env` and a secret manager.
- Humans and gates, the rails, the rituals, the menu, the state files committed with
  the project.
- Twenty eval scenarios with simulated users, a grader, fixtures, and a results
  history.
