# Changelog

The skill's version is in `VERSION` and in the `metadata.version` field of
`SKILL.md`. The agent writes the version it ran with into `VALUE.md`, so a project
can tell when the skill moved under it. Bump the minor number when a rail changes
what the agent does, the patch number for wording.

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
