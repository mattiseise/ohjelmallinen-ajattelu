# Wilhelm — Week 1 audit, round 1

Auditor: Wilhelm (gate #4, quality gate).
Auditee: Rasmus.
Plan: `01-suunnitelma.md` (`## Hyväksymiskriteerit`, criteria 1–29).
Scope: 7 files under `materiaali/student/week-01/` and `materiaali/teacher/week-01/`.

## Päätös

**rejected**

Two required H2 sections in `teacher-materials.md` are missing or renamed (criterion 16), and one of the four tasks in `student-tasks.md` ends with a `### Keep your notes` block that does not remind the student of AT1 (criterion 13). Both are structural compliance gaps that the criteria treat as blocking. Everything else passes — including all word-count brackets, all 90-minute slot sums, all independent-work percentages, the verbatim central question in two locations, examples-first ordering, vocabulary coverage, AI-resilience labelling, fenced LLM prompt with explicit no-verbatim instruction, and English-throughout. Rasmus should be able to fix the rejection with a small, targeted edit pass — no rewrite needed.

## Blocking-löydökset

1. **Criterion 16 — required H2 `## Answers to common student questions` missing in `teacher-materials.md`.**
   The H2 list of `teacher-materials.md` is:
   ```
   ## Week 1 learning objectives (mapped to Bloom)
   ## Common misconceptions for Week 1
   ## Lesson 1 — 90-minute plan
   ## Lesson 2 — 90-minute plan
   ## Lesson 3 — 90-minute plan
   ## Facilitation tips
   ## Formative assessment
   ```
   The five required student questions exist as bullets, but they live inside `### Common student questions during class` (a *sub*-section of `## Facilitation tips`, at line 163), not as their own H2. Sune's criterion 16 explicitly lists `## Answers to common student questions` as a required H2. Fix: promote that subsection to its own H2 directly after `## Lesson 3 — 90-minute plan` (or before `## Facilitation tips`), retitled `## Answers to common student questions`.
   Evidence: `teacher/week-01/teacher-materials.md:147` (`## Facilitation tips`) and `teacher/week-01/teacher-materials.md:163` (`### Common student questions during class`).

2. **Criterion 16 — required H2 `## Formative assessment tips` is renamed.**
   File has `## Formative assessment` at line 173. Sune's criterion 16 names the H2 `## Formative assessment tips`. Word count and content are fine; only the heading text is off by one word. Fix: rename the H2 to `## Formative assessment tips`.
   Evidence: `teacher/week-01/teacher-materials.md:173`.

3. **Criterion 13 — Task 1.3's `### Keep your notes` does not remind the student that AT1 lands at end of Week 2.**
   Criterion 13: "Each task ends with a `### Tip` or `### Keep your notes` block reminding the student that AT1 lands at end of Week 2." Tasks 1.1, 1.2 and 1.4 each end with a `### Keep your notes` that mentions AT1. Task 1.3 (`Two algorithms, one goal`) ends with:
   > "Keep both algorithms and the comparison. **Week 4** will return to 'more than one correct answer' in a more formal way; your notes here will save you time."
   No AT1 mention. The reference to Week 4 is helpful but does not satisfy the criterion. Fix: add a one-sentence AT1 reminder to Task 1.3's `### Keep your notes` (the Week 4 line can stay).
   Evidence: `student/week-01/student-tasks.md:112–114`.

## Non-blocking-parannukset

1. **Slides task list contains broken IDs (criterion 29, valid markdown, internal consistency).**
   `slides.md:155–161` ("Tasks this week") lists `Task 1.1`, `Task 1.3`, `Task 1.4`, `Task 1.5`. The actual `student-tasks.md` ships `Task 1.1`, `Task 1.2`, `Task 1.3`, `Task 1.4`. The slide's IDs follow Sune's *plan menu* numbering (where 1.2 = "morning algorithm" was the alternative Rasmus dropped), not what Rasmus shipped. Fix: renumber the slide list to `1.1 / 1.2 / 1.3 / 1.4` to match what students will actually see in `student-tasks.md`.
   Evidence: `student/week-01/slides.md:157–160` vs. `student/week-01/student-tasks.md:13,45,93,118`.

2. **`self-study.md` cross-references Task 1.3 as the "literal robot" follower task, but Rasmus's Task 1.3 is "Two algorithms, one goal".**
   `self-study.md:143`: *"This is what Task 1.1 and Task 1.3 of the week's tasks are about. In Task 1.1 you write an instruction, hand it to a real follower..."* — Task 1.3 in `student-tasks.md` is the algorithms-comparison task, which does not involve a real follower. Likely Rasmus meant Task 1.4 (vocational help-desk, which does use a real tester) or just Task 1.1. Fix: change `Task 1.3` to `Task 1.4` (or drop the second reference).
   Evidence: `self-study.md:143` vs. `student-tasks.md:93,118`.

3. **Task H2 labelling order differs slightly from Sune's wording (criterion 13).**
   Sune said tasks should be "prefixed with `🟢 RECOMMENDED —` or `🟣 DEEPENING —`". Rasmus puts the label at the *end* of the H2 instead: `## Task 1.1 — The literal robot game 🟢 RECOMMENDED *(AI-resilient)*`. The label is present in every task H2, just not as a prefix. Not blocking (the label is unambiguous), but worth nudging closer to the spec if Rasmus is editing the file anyway.
   Evidence: `student/week-01/student-tasks.md:13,45,93,118`.

4. **"Stupid/dumb" phrase appears in the teacher's reference text on the misconception itself.**
   Criterion 23 says the phrase "the computer is stupid / dumb" must not appear; framing must be "the computer is literal". Strictly, the phrase does appear, but every occurrence is in the explicit pedagogical act of *naming the misconception so the teacher can correct it* (`teacher-materials.md:41,45,46,158,180` and `student-tasks.md:9` which says *"the computer is **literal**, not stupid"*). I read this as compliant with the criterion's *intent* (never endorsing the framing), but it is worth flagging because a strict grep-only audit would call it. No fix required.
   Evidence: `teacher-materials.md:41,45,46,158,180`, `student-tasks.md:9`.

5. **Naming Python in `self-study.md` Example 3.**
   Sune's Rajaukset section says "in Week 1 no programming language is named at all." `self-study.md:37` names Python. However, Sune's own briefing for File 2 (plan line 232) explicitly recommends "`pyhton tutorial` typo search" as the IT example for the literal-interpretation section. The plan therefore contradicts itself on this point, and Rasmus took the briefing's lead. I do not block on this, but the orchestrator may want to align the plan and the brief in a future round so this is not relitigated each week.
   Evidence: `self-study.md:37`; plan `01-suunnitelma.md:232`.

## Tarkistettu evidenssi

### File presence (criterion 1)
All 7 canonical files present, no extras:
```
student/week-01/overview.md
student/week-01/self-study.md
student/week-01/slides.md
student/week-01/student-tasks.md
student/week-01/vocabulary.md
teacher/week-01/in-class-tasks.md
teacher/week-01/teacher-materials.md
```
No `.pptx`, `deck.md`, `slides.key`, Reveal.js HTML or `media/` folder found.

### Word counts (criteria 4–10)
| File | Words | Bracket | Pass |
|---|---|---|---|
| overview.md | 398 | 200–400 | ✓ |
| self-study.md | 3692 | 2400–4000 | ✓ |
| student-tasks.md | 1643 | 800–1800 | ✓ |
| vocabulary.md | 813 (16 terms) | 10–18 terms | ✓ |
| slides.md | 772 (19 slides) | 10–20 slides | ✓ |
| teacher-materials.md | 3248 | 2400–4200 | ✓ |
| in-class-tasks.md | 1177 | 400–1200 | ✓ |

`wc -w` source values shown above; slide count is `grep -c '^---$' = 18` separators ⇒ 19 slides including the title slide.

### Required H2s (criteria 11–17)
- `overview.md`: ✓ — `## Week 1 theme`, `## What you will be able to do by the end of the week`, `## Core minimum vs. deepening`, `## How the three lessons fit together` (in order, lines 3/7/16/29).
- `self-study.md`: ✓ — `# Speaking to a computer — what does it actually hear?` (line 1), `## Introduction` (3), `## Lesson 1 — Speaking to a computer (literal interpretation and ambiguity)` (17), `## Lesson 2 — Algorithms in everyday life` (61), `## Lesson 3 — Precise and imprecise instructions` (109), `## Summary and what comes next` (161). 4 `> **Pause for a moment:**` prompts at lines 57, 85, 105, 157 (≥1 per lesson; ≥4 total) ✓.
- `student-tasks.md`: ✓ structurally — `## Overview of the week's tasks` (3) + 4 task H2s. Each task ends with `### Keep your notes` (lines 39, 87, 112, 138). AT1 reminder present in 3 of 4 (see Blocking #3 for Task 1.3 gap).
- `vocabulary.md`: ✓ — single H2 `## Week 1 vocabulary` (3), 16 H3 terms; `### Decomposition *(looking ahead — central topic of Week 2)*` at line 52.
- `slides.md`: ✓ — title slide at line 1, central-question slide at lines 9–11, recap slide at 174–176; `---` on its own line between all 19 slides; no `.pptx` references; no renderer-specific speaker-note syntax.
- `teacher-materials.md`: **partial fail** — 5 of 7 required H2s match; `## Answers to common student questions` missing (content under `### Common student questions during class`); `## Formative assessment` instead of `## Formative assessment tips`. See Blocking #1 and #2.
- `in-class-tasks.md`: ✓ — `## Overview` (3), `## Activity A — "Literal robot live" 🟢 MANDATORY` (14), `## Activity B — "Algorithm relay (pair work)" 🟣 OPTIONAL` (49), `## How these activities connect to teacher-materials.md` (82).

### 30–50% rule (criterion 18)
Time-slot arithmetic from the three lesson tables in `teacher-materials.md`:
- Lesson 1: 10 + 15 + 30 + 20 + 10 + 5 = **90 min** ✓; independent block 30 min = **33.3%** (in 27–45 min, in 30–50%) ✓.
- Lesson 2: 10 + 15 + 35 + 20 + 8 + 2 = **90 min** ✓; independent block 35 min = **38.9%** ✓.
- Lesson 3: 10 + 15 + 30 + 25 + 8 + 2 = **90 min** ✓; independent block 30 min = **33.3%** ✓.

### Common misconceptions (criterion 16)
`grep -c '^\*\*Misconception'` = **7** (≥6 required). Per-lesson distribution: L1 = 2, L2 = 2, L3 = 2, plus 1 bonus. Each has a `**Correction:**` line on the next line. ✓

### Common student questions (criterion 16)
`awk` over `### Common student questions during class` finds **5** bulleted Q/A pairs (≥5 required). Content fine; placement is the issue (see Blocking #1).

### Central question verbatim (criterion 20)
- `self-study.md`: 2 verbatim hits (line 11 in `## Introduction`; line 163 in `## Summary and what comes next`).
- `slides.md`: 2 verbatim hits (line 11 on `## The central question`; line 176 on `## Recap — the central question, one more time`).

### Examples-first principle (criterion 21)
- L1 — `### A computer takes you literally`: Example 1 (sandwich, everyday), Example 2 (big tree, everyday), then *"Now the IT side."*, Example 3 (typo search), Example 4 (missing slash). ✓
- L2 — `### Algorithms you already use`: three everyday algorithms (tea, route to school, morning routine), then *"The same shape appears in an IT context too"* and the help-desk-script example. ✓
- L3 — `### Hunting ambiguity`: four ambiguity patterns each illustrated with everyday example first, then *"The same four patterns show up in IT contexts almost word for word."* ✓

### Forbidden content scan (criteria 19, 22, 23)
- `.pptx | PowerPoint | jest | mocha | vitest | pytest | reveal.js | deck.md | slides.key` across all 7 files: **0 matches** ✓.
- Forbidden Bloom verbs (`create | build | design | develop | evaluate | judge | analyze | decompose | abstract | debug`) in objective bullets of `teacher-materials.md` (lines 14–34): **0 matches** ✓. The verbs do appear at line 11 in the explanatory text that *lists them as forbidden*, which is fine.
- `stupid | dumb`: 6 matches across `teacher-materials.md` and `student-tasks.md`. Every occurrence is in the explicit act of *naming the misconception so it can be corrected*; none endorses the framing. Treated as non-blocking (see Non-blocking #4).

### Tasks structure (criteria 13, 24)
- 1 🟢 RECOMMENDED + 3 🟣 DEEPENING (in 1–2 + 2–3 brackets) ✓.
- The RECOMMENDED task (`Task 1.1 — The literal robot game`) is explicitly tagged `*(AI-resilient)*` in its H2 ✓.
- 1 of 2 AI-resilient tasks total (Task 1.1 RECOMMENDED, Task 1.4 DEEPENING). Criterion 24 wants at least one AI-resilient RECOMMENDED task; satisfied ✓.

### LLM sparring prompt (criterion 25)
Task 1.2 contains a fenced code block at lines 67–81 with a sample LLM prompt, plus the explicit instruction at line 65 (*"**Do not accept the LLM's answer as the truth.**"*) and at line 83 (*"**decide for each suggestion whether to accept, modify or reject it.**"*). ✓

### In-class MANDATORY (criteria 17, 26)
`grep -inE 'MANDATORY' in-class-tasks.md` → 3 hits, including the H2 `## Activity A — "Literal robot live" 🟢 MANDATORY` at line 14. Activity A is cross-referenced from `teacher-materials.md:89` (L1 warm-up) and `teacher-materials.md:133,139` (L3 main slot). ✓

### English-throughout (criterion 27)
- `grep -oE '[äöå]'` across all 7 files: **0 matches** in every file.
- Spot-checks of common Finnish stop-words against full-line context: no Finnish sentences detected; matches on tokens like `is`, `on`, `tai` are all inside English sentences.
- `Avoimet kysymykset` and other Finnish H2s only exist in the *plan* file, which is excluded from the audit per Sune's note at plan line 101. ✓

### Markdown validity (criterion 29)
- Code fences: `student-tasks.md` has 2 backtick fences (1 balanced block). All other files have 0 fences. ✓
- All 18 `---` separators in `slides.md` are alone on their own line (verified by `grep -nE '^---$'`). ✓
- No broken section anchors or missing closing markup observed.

## Seuraava

**palauta Rasmukselle** — three blocking edits, all surgical:
1. Promote the student-questions subsection in `teacher-materials.md` to an H2 named `## Answers to common student questions`.
2. Rename `teacher-materials.md`'s `## Formative assessment` to `## Formative assessment tips`.
3. Add a one-sentence AT1 reminder to `student-tasks.md` Task 1.3's `### Keep your notes`.

Optional in the same pass: fix the four non-blocking inconsistencies (slide task IDs, self-study Task-1.3 reference, Task H2 label position, and — if the orchestrator agrees — clean up the "stupid" mentions to talk about "the 'computer is X' misconception" without quoting the bad framing).

Linnea's pedagogical audit was running in parallel; her non-blocking notes should be folded into Rasmus's next pass when they arrive (Wilhelm round 2 will carry them forward).
