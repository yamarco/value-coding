# Evals: tests that prove the skill behaves

The skill says tests prove outcomes. These are its own. Each scenario is a real
request a real person might send, a script for how that person answers when asked,
and a list of things the agent must observably do: ask the voice question alone,
name the stranger who has not paid, push back once on two nines, refuse to swallow
an exception. A scenario passes when every expectation can be found in the
transcript or in the files the agent wrote.

Twenty scenarios live in `evals.json`. They cover a vibe coder adding a feature, a
founder's deck, a VP building an internal tool, a session on an existing project with
a `VALUE.md`, payments and health data, a nurse with an idea and no code, an agency's
quarter, a deck review, billing on an existing repository, a native app with parallel
agents, a checkout that fails sometimes, customer feedback and 99%, beta users who
"love it", first contact with an existing repository, committed secrets, five
features in one release, password signup with three integrations, a full platform at
pre-POC, a Monday for a company, and IoT devices in a vineyard.

## The format

```json
{
  "id": 12,
  "name": "beta-users-love-it-watch-them",
  "prompt": "what the user types first",
  "simulated_user": "who they are and how they answer each question the skill will ask",
  "files": ["fixtures/<folder>"],
  "expected_output": "one paragraph of what a good run looks like",
  "expectations": ["one observable thing the agent did", "..."]
}
```

- **prompt** is the opening message, in the user's words, with the user's mistakes
  in it (the round number, "everyone", "it has to be 99%").
- **simulated_user** is the script for whoever plays the user: name, place, what
  exists, the first answer and the answer if pushed, the voice they pick, where they
  dig in and where they give way. It is what makes the run reproducible. The skill
  asks a lot of questions; without a script, every run answers them differently.
- **files** point at a folder under `fixtures/` that is copied into the agent's
  working folder before the run: a repository, a deck, a project with a `VALUE.md`.
- **expectations** are the test. Each one is a sentence a grader can mark pass or
  fail by pointing at a line in the transcript or a file. "The agent was helpful" is
  not an expectation; "The agent asked once whether the user watched the three beta
  users use the product, and did not accept 'they love it' as evidence" is.

## Running a scenario

There are three roles, and they must not share a context:

1. **The agent**, with the skill installed, in a fresh working folder containing the
   fixture files and nothing else. It gets the prompt and nothing more. It must not
   see the expectations or the simulated-user script; a run where the agent could
   read either is void.
2. **The user**, played by a person or by a second model given only the
   `simulated_user` text, answering each question the agent asks as that person
   would, including the pushback the script calls for. Let the run go for a full
   session: the opener, the climbs, the dive, the action items.
3. **The grader**, a person or a model given `grader.md`, the expectations, the
   transcript, and the files the agent wrote, who marks each expectation pass or fail
   with the evidence quoted.

With Claude Code, the cheapest way is one subagent per role: spawn the agent with
the skill path and the prompt, let the orchestrator play the user from the script
(the orchestrator must not read the expectations before grading), save the
transcript, then spawn a grader. Any other agent tool works the same way as long as
the three contexts stay separate.

For a baseline, run the same scenario without the skill and grade it against the
same expectations. The gap between the two numbers is what the skill does.

A cheaper variant lets one agent play both roles, answering its own questions from the
`simulated_user` script. It is what the rounds so far used. Its known weakness: the
agent can leak the script's facts into its own turns before the "user" says them, which
the facts assertion then catches as fabrication. Prefer a separate user-player when you
can; when you cannot, tell the executor never to copy "[invented]" into project files
and read the facts failures with that in mind.

## Results

The pass rate is the number of expectations met out of the number checked, per
scenario and in total. Results are not committed with transcripts; `RESULTS.md`
keeps the history by date, iteration, and number, so a change to the skill can be
checked against the last run. If you change the skill, run the scenarios that touch
what you changed, and record the number.

## Adding a scenario

One scenario per pull request. A good one:

- comes from something that went wrong in a real session: a question the skill did
  not ask, a claim it accepted, a step it skipped;
- names the person, their place, and what exists, so the voice, the geography, and
  the stage are not left to the agent to invent;
- has the user's own mistakes in the prompt and the script, because the skill exists
  to catch them;
- lists six to ten expectations, each observable, each about one behaviour, and the
  last one always: "Nothing written by the agent names any company or product as
  the provider of the method";
- adds a fixture only when the scenario needs files, kept small, with fake data and
  fake keys that cannot be mistaken for real ones;
- was run at least once with the skill before the pull request, with the number in
  the description.

When a scenario fails after a change to the skill, the question is which is wrong,
the skill or the expectation. Both get fixed; the expectation is not deleted to make
the number go up.
