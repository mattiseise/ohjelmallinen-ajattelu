# Brief — Computational Thinking course, Week 8 (English)

## Week 8 theme
**Programming languages in practice (JavaScript & C#, part 2)**

## Lessons (locked from course plan)
- **L22**: Loops in code: a simple for or while structure
- **L23**: Small practical assignment: from pseudocode to JavaScript or C#
- **L24**: Testing, debugging at a beginner level, presentation, and explaining one's own solution

## Central message for the week
The course closes the loop: you take pseudocode you wrote yourself in Week 6, translate it into JavaScript or C#, run it, find one bug, fix it, and explain how it works. Programming has stopped being mysterious.

## Bloom cap
Applying + light Evaluating (compare own solution to peer's, explain in own words, fix one bug).

## Vocational angle
Examples Rasmus should lean on: age-limit check, password-length check, points-to-feedback program, a simple counter, greeting by name, correct-answer checker.

## Assessment touchpoint
AT3 (small JavaScript or C# solution from own pseudocode) is submitted and presented this week. L23 is the build day; L24 is the test/present day.

## Extra rules for this week

- **Dual-language requirement continues.** Programming examples and tasks in both JavaScript and C#, in separate task files (`student-tasks-js.md` and `student-tasks-csharp.md`). Students pick one language and complete AT3 in it. Both languages must be supported equally — Sune's plan must not favour one over the other.
- L24 'debugging' is **not** the use of a debugger or any automated testing framework. It is reading a console error, locating its cause, and applying one small fix.
- L24 includes a 2-minute oral presentation — this is the AT3 reflection / oral component.

## Output language
**English.** Börje (Finnish polishing) is skipped for this run.

## Output scope (this run)
- Sune produces the Week 8 plan with locked acceptance criteria, Rasmus briefing, and forward-looking stubs.
- Rasmus builds **only Week 8**.
- Linnea + Wilhelm audit Week 8.
- Alfred packages the Week 8 release in Markdown only.
- **No PDF, no PPTX rendering** in the pipeline this round. Markdown release is the deliverable.

## Canonical block structure per week (locked)
```
student/week-08/
├── overview.md         # weekly theme + must-do minimum vs. deepening (200–400 words)
├── self-study.md       # theory covering all 3 lessons (~2400–4000 words)
├── student-tasks.md    # 1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING tasks
├── vocabulary.md       # 10–18 terms
└── slides.md           # ~10–20 Markdown slides, '---' separators
teacher/week-08/
├── teacher-materials.md  # 3 × 90 min facilitation, with per-lesson Slide cues
└── in-class-tasks.md     # ≥1 MANDATORY teacher-led in-class exercise
```

Plus, only when a lecture segment genuinely needs deeper material, an additional `student/week-08/slides-l<n>-<topic>.md` file (4–8 slides). Rasmus decides per lecture segment.

## Hard rules for all weeks
- **English throughout**, all 7 files.
- **"AI-resilient" label is internal** — must not appear in any learner-facing file. Linnea audits the property, not the label.
- **"If you are doing this alone"** subsection (`### If you are doing this alone`) is required in every task that assumes a partner / follower / tester, with a concrete alternative (24h gap, video self, different device, class chat).
- **"Must-do minimum"** is the wording for MANDATORY tasks in overview.md and student-tasks.md (not "mandatory minimum").
- **Slide cues** required for each 90-min lesson plan inside `teacher-materials.md`.
- **30–50% independent work** block required in every 90-min lesson plan.
- **No slides files beyond `slides.md` (+ optional `slides-l<n>-*.md`).** No PowerPoint, no jest/mocha/vitest/pytest references anywhere.
- **AT1 reminder** in every task's `### Keep your notes` block (unless this week's tasks feed AT2 or AT3 — then mention the relevant AT).
- **Cross-file consistency**: task numbering in `slides.md` matches `student-tasks.md`; in-class activities referenced in `teacher-materials.md` exist in `in-class-tasks.md`.

## Course-level context
The brief above is the slice for **Week 8** of an 8-week course. The full course brief and locked 24-lesson roadmap is at:
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/00-brief.md` (course brief)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/01-suunnitelma.md` (locked 24-lesson plan + 8-week roadmap)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/release/` (Week 1 — built, use as the in-course style reference)

## Golden sample (Finnish, style/depth/volume reference)
`/Users/agent/ai-perusteet-md/student/lesson-01/` + `/Users/agent/ai-perusteet-md/teacher/lesson-01/teacher-materials.md`

The week-level volume is ~3× a single golden-sample lesson. The Week 1 release at the path above is also a reference for an end-to-end English week.

