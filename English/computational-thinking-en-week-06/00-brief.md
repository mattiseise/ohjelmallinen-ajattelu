# Brief — Computational Thinking course, Week 6 (English)

## Week 6 theme
**From thinking to code**

## Lessons (locked from course plan)
- **L16**: Pseudocode: from natural language to a more precise format
- **L17**: Input, processing, output, and the idea of a variable
- **L18**: Testing pseudocode: dry running and finding errors (AT2 submitted around this lesson)

## Central message for the week
Pseudocode is the bridge between everyday English and real code. It is precise enough for a computer to follow if it had to, but readable enough to share with a non-programmer.

## Bloom cap
Understanding + Applying (write pseudocode, dry-run with a trace table, fix a bug in pseudocode).

## Vocational angle
Examples Rasmus should lean on: pseudocode for a help-desk reply triage, for a password-strength check, for a daily backup routine.

## Assessment touchpoint
AT2 submitted around L18. Tasks this week feed directly into AT2. No code yet — only pseudocode.

## Extra rules for this week

- Absolutely no JavaScript or any real programming language this week. Pseudocode only.
- No testing frameworks (jest, mocha, vitest, pytest). Testing here means dry-running with a trace table on paper.

## Output language
**English.** Börje (Finnish polishing) is skipped for this run.

## Output scope (this run)
- Sune produces the Week 6 plan with locked acceptance criteria, Rasmus briefing, and forward-looking stubs.
- Rasmus builds **only Week 6**.
- Linnea + Wilhelm audit Week 6.
- Alfred packages the Week 6 release in Markdown only.
- **No PDF, no PPTX rendering** in the pipeline this round. Markdown release is the deliverable.

## Canonical block structure per week (locked)
```
student/week-06/
├── overview.md         # weekly theme + must-do minimum vs. deepening (200–400 words)
├── self-study.md       # theory covering all 3 lessons (~2400–4000 words)
├── student-tasks.md    # 1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING tasks
├── vocabulary.md       # 10–18 terms
└── slides.md           # ~10–20 Markdown slides, '---' separators
teacher/week-06/
├── teacher-materials.md  # 3 × 90 min facilitation, with per-lesson Slide cues
└── in-class-tasks.md     # ≥1 MANDATORY teacher-led in-class exercise
```

Plus, only when a lecture segment genuinely needs deeper material, an additional `student/week-06/slides-l<n>-<topic>.md` file (4–8 slides). Rasmus decides per lecture segment.

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
The brief above is the slice for **Week 6** of an 8-week course. The full course brief and locked 24-lesson roadmap is at:
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/00-brief.md` (course brief)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/01-suunnitelma.md` (locked 24-lesson plan + 8-week roadmap)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/release/` (Week 1 — built, use as the in-course style reference)

## Golden sample (Finnish, style/depth/volume reference)
`/Users/agent/ai-perusteet-md/student/lesson-01/` + `/Users/agent/ai-perusteet-md/teacher/lesson-01/teacher-materials.md`

The week-level volume is ~3× a single golden-sample lesson. The Week 1 release at the path above is also a reference for an end-to-end English week.

