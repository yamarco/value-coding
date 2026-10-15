# Results

One line per run of the full set. The number is expectations met out of expectations
checked, with the skill and without it on the same scenarios. Transcripts are not
committed; the method is in `README.md`.

| Date | Skill version | Scenarios | With skill | Without skill | Notes |
|------|---------------|-----------|------------|---------------|-------|
| 2026-10-14 | first draft | 0 to 7 | 95.6% | 28.7% | first clean run; an earlier batch was void because the agent could read the expectations |
| 2026-10-14 | second draft | 0 to 7 | 84% | not rerun | harder bar: the simulated user pushed back on every challenge |
| 2026-10-14 | third draft (commit 2b6e3ac) | 0 to 8 | 85% (119/140) | 27.6% | scenario 8, the existing repository: 14/16 with the skill, 3/16 without. Recurring misses: a fact stated before the user gave it, the altitude tag missing on the voice-acknowledgement turn, semicolon-chained slides. All three were folded into the skill |
| 2026-10-15 | 1.0.0 | 0 to 19 | 81.8% (193/236) | 26.0% (52/200) | first full round on twenty scenarios; baselines 0 to 8 reused from the third-draft round, 9 to 19 run fresh. Strongest: the existing-project session (18/18), the vibe coder (14/15), the vineyard devices (8/9), the Monday plan (7/8). Weakest: integrations (4/8), the hotfix (4/6), customer feedback and two nines (5/8). The misses were structural: 8 to 12 questions before the first output in 18 of 20 runs; questions bundled in one turn in 15; facts from the persona or a git log written as the user's in 8; the score denominator read two ways in every run. All folded into 1.1.0 |
| | 1.1.0 | 0 to 19 | pending | same | rerun of the with-skill runs on the revised skill |
