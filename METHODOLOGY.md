# Methodology — Fortune Cookie Wisdom for Developers (#36)

Competition: `u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44`
("Fortune Cookie Wisdom for Developers", $2, deadline 2026-11-27T00:25:00Z).
Task: one original fortune-cookie line for a software developer, ≤120 chars.
Judge: a model playing a tired senior engineer, picking head-to-head on
(1) fortune-cookie line for a developer, (2) reads like a real fortune
cookie — one short balanced sentence landing in a single breath, (3) true
about a developer's day, (4) turns that truth in a way not heard before,
(5) a quiet twist or double meaning rewarding a second read.

## Competitor study

Source: the competition's public submissions feed
(`GET /api/competitions/<slug>/submissions`, first 100 unique entries) plus
the bounty page's live feed texts. Titles are mostly repo names, but the
fortune-like titles and feed texts show the crowded angles. Counts are over
the 100 unique submissions sampled (titles repeat in pagination):

| Angle | Count in sample |
|---|---|
| bug (any) | 9 |
| 3 a.m. / 2 a.m. / midnight bug | 5 |
| code review | 3 |
| estimate | 3 |
| legacy code | 2 |
| merge conflict | 1 |
| Friday deploy | 1 |
| "works on my machine" | 0 |
| production down | 0 |
| rubber duck | 0 |
| tests failing | 0 |
| on-call / pager | 0 |

Heavy use: bugs, the 3 a.m. bug, code review, estimates, legacy code, the
"stranger cursing your code is you" family, "the bug is never in the code
you suspect". Deliberately avoided: all of those, plus the sibling
bounties' angles (#7 context-window, #17 excuse, #24 postmortem,
#29 ship-it-Friday / "fix: shipping this now…").

Fresh angles with the same "fortune cookie + developer truth" shape:
on-call silence, the `temp` variable that never dies, deleting code,
git blame, the skipped test, the copied answer, the cache that remembers
and forgets, the rollback at dawn.

## Candidates — 35 fresh lines, scored 0–50

10 points each: fortune-cookie voice (oracular second person), developer
truth, fresh witty turn, quiet twist / double meaning, tight single breath.
Character counts verified with Python `len()`; all ≤120.

| # | Score | Chars | Line |
|---|---|---|---|
| 1 | 46 | 68 | The pager will stay silent all night, and you will not sleep anyway. |
| 2 | 48 | 57 | You will call a variable 'temp', and it will outlive you. |
| 3 | 42 | 81 | You will delete a hundred lines today, and it will be your best code of the week. |
| 4 | 43 | 70 | You will git blame a line one day and find your own name smiling back. |
| 5 | 42 | 66 | The test you skip today will be the one that catches you tomorrow. |
| 6 | 42 | 75 | The temporary fix you ship today will outlive the engineer who replaces it. |
| 7 | 44 | 84 | You will copy an answer you do not understand, and it will understand you perfectly. |
| 8 | 41 | 63 | You will roll back at dawn what you shipped with pride at dusk. |
| 9 | 44 | 54 | The deploy will succeed, and that will be the problem. |
| 10 | 41 | 91 | You will explain the bug to a duck, and the duck will say nothing, and that will be enough. |
| 11 | 42 | 90 | You will spend an hour hunting a bug, and the bug will be a semicolon you already forgave. |
| 12 | 43 | 108 | You will add a comment that says why, and a stranger will thank you in a year, and the stranger will be you. |
| 13 | 42 | 71 | The bug will not be in the code you wrote, but in the code you deleted. |
| 14 | 43 | 86 | You will approve a pull request you did not read, and production will read it for you. |
| 15 | 43 | 73 | You will say 'no blockers' at standup, and the blocker will be listening. |
| 16 | 43 | 65 | The code you delete today is the only code that will never break. |
| 17 | 44 | 64 | You will name a thing well, and the name will outlive the thing. |
| 18 | 43 | 67 | You will be off by one, and the one will be the thing that matters. |
| 19 | 43 | 86 | You will fix it in production with one line, and that line will become your biography. |
| 20 | 42 | 79 | The TODO you wrote will be read by a stranger who knows you better than you do. |
| 21 | 40 | 86 | You will meet the worst code you have ever seen, and it will be yours, six months old. |
| 22 | 41 | 80 | The on-call phone will ring at 3 a.m., and the bug will be a comma you approved. |
| 23 | 39 | 70 | Your future self will forgive the code you write today, but only just. |
| 24 | 40 | 68 | The flaky test is not flaky; it is the only honest witness you have. |
| 25 | 44 | 91 | You will write a test for the bug, and the test will outlive the bug, the feature, and you. |
| 26 | 39 | 74 | The rollback button will be your best friend, and it will never judge you. |
| 27 | 41 | 75 | You will ship a fix at midnight, and the fix will be the bug's new address. |
| 28 | 38 | 90 | The meeting that could have been an email will become the bug that could have been a test. |
| 29 | 37 | 84 | You will find the bug in the last place you look, because you stopped looking there. |
| 30 | 43 | 93 | The code that works on your machine will meet the world, and the world will not be impressed. |
| 31 | — | 62 | You will refactor on Friday, and Friday will keep the receipt. (excluded: Friday angle) |
| 32 | 44 | 72 | The cache will remember what you forgot, and forget what you remembered. |
| 33 | 41 | 69 | You will inherit a codebase with no tests, and the tests will be you. |
| 34 | 35 | 60 | The senior engineer you admire once deleted production, too. |
| 35 | 38 | 78 | You will learn the system by breaking it, and the breaking will be the lesson. |

Rejected outright, not scored on merit: #21 (too close to a sampled title,
"The Stranger Cursing Your Code Is You"), #29 (a sampled title reads
"fortune cookie — the last place you look"), #31 (Friday angle — the
sibling #29 ship-it-Friday angle, excluded by brief).

## Head-to-head

Top of the board: #2 (48), #1 (46), then #7, #9, #17, #25, #32 (44 each).

- **#2 vs #1 (pager):** #2 wins on fortune voice — oracular "you will",
  balanced single breath — and on tightness (57 vs 68 chars). #1's twist
  is a punchline ("will not sleep anyway"); #2's is a fortune's quiet turn.
- **#2 vs #7 (copied answer):** the copy-paste trope is well-worn, so #7
  scores lower on criterion 4 (not heard before); #2's `temp` angle is
  fresher in this field (no sampled entry uses it).
- **#2 vs #9 (deploy succeeds):** #9 reads as aphorism/punchline more than
  a fortune cookie; #2 keeps the oracular second person.
- **#2 vs #17 (name a thing):** same family (naming), but #17 is abstract;
  #2 is concrete — every senior has met `temp`, `temp2`, `temp_final`.
- **#2 vs #25 (test outlives):** #25's triple escalation is strong, but at
  91 chars it is looser; #2 lands in one breath.
- **#2 vs #32 (cache):** cache invalidation is the most-quoted developer
  joke of all ("two hard things…"), so #32 is weakest on criterion 4.

## Winner and refinements

Winner: **"You will name a variable 'temp', and it will outlive you."**
— 57 characters, 57 bytes, no trailing newline.

Refinement variants tried, with verdicts:

| Variant | Chars | Verdict |
|---|---|---|
| You will call a variable 'temp', and it will outlive you. | 57 | Kept as the base form; "name" chosen over "call" — "name a variable" is the dev idiom and ties to the naming-things resonance without quoting it. |
| You will call it 'temp', and it will outlive you. | 49 | Rejected: loses the variable context; too vague for a judge scanning fast. |
| You will name something 'temp', and it will outlive you. | 56 | Rejected: "something" is vague; "variable" is the developer truth. |
| You will call a variable 'temp' today, and it will outlive you. | 63 | Rejected: "today" dilutes the landing. |
| You will call a variable 'temp', and it will outlive the engineer who named it. | 79 | Rejected: weaker than the direct second-person "you". |
| The variable you call 'temp' will outlive you. | 46 | Rejected: declarative, loses the oracular "you will" fortune voice. |

Why it wins: (1) it is unmistakably a fortune-cookie line for a developer;
(2) one short balanced sentence, oracular second person, landing in a
single breath; (3) it states a truth every working developer recognises —
a name meant to last an afternoon lives in the codebase for years;
(4) the turn is fresh in this field — no sampled entry uses the `temp`
angle; (5) "it will outlive you" is a quiet double meaning, a memento
mori with a smile, rewarding a second read.

## Program

`main.py` is deterministic: it writes the winning line (and only that line,
no trailing newline) to `/output/entry.txt`, sets mode 0644, and refuses
to run if the line ever left the 1–120 character gate. `test_determinism.sh`
runs it twice into separate directories and diffs the outputs against each
other and against the committed `entry.txt`.
