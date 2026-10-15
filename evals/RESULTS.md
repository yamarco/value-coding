# Results

One line per run of the full set. The number is expectations met out of expectations
checked, with the skill and without it on the same scenarios. Transcripts are not
committed; the method is in `README.md`.

| Date | Skill version | Scenarios | With skill | Without skill | Notes |
|------|---------------|-----------|------------|---------------|-------|
| 2026-10-14 | first draft | 0 to 7 | 95.6% | 28.7% | first clean run; an earlier batch was void because the agent could read the expectations |
| 2026-10-14 | second draft | 0 to 7 | 84% | not rerun | harder bar: the simulated user pushed back on every challenge |
| 2026-10-14 | third draft (commit 2b6e3ac) | 0 to 8 | 85% (119/140) | 27.6% | scenario 8, the existing repository: 14/16 with the skill, 3/16 without. Recurring misses: a fact stated before the user gave it, the altitude tag missing on the voice-acknowledgement turn, semicolon-chained slides. All three were folded into the skill |
| | | 9 to 19 | not yet run | | added 2026-10-15 for the engineering rails, teaching before features, two nines, watching strangers, secrets, small releases, first contact with a repository, running a company, and devices |
