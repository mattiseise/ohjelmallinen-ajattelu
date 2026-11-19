# Brief — Computational Thinking course, Week 5 (English)

## Week 5 theme
**Logic structures**

## Lessons (locked from course plan)
- **L13**: Sequence: a program proceeds step by step
- **L14**: Conditions: if-then-else thinking and decision trees
- **L15**: Repetition: doing the same thing multiple times

## Central message for the week
Almost any process can be described with three building blocks: sequence, condition, and repetition. Once you can name them in everyday tasks, you have the skeleton of every program.

## Bloom cap
Remembering + Understanding + light Applying (express conditions and loops in natural language).

## Vocational angle
Examples Rasmus should lean on: a password-validation rule (condition), an inbox sweep (repetition), a step-by-step deployment checklist (sequence).

## Assessment touchpoint
Foundation week for AT2 (process description with sequence + condition + repetition). AT2 lands at end of Week 5 / during Week 6.

## Output language
**English.** Börje (Finnish polishing) is skipped for this run.

## Output scope (this run)
- Sune produces the Week 5 plan with locked acceptance criteria, Rasmus briefing, and forward-looking stubs.
- Rasmus builds **only Week 5**.
- Linnea + Wilhelm audit Week 5.
- Alfred packages the Week 5 release in Markdown only.
- **No PDF, no PPTX rendering** in the pipeline this round. Markdown release is the deliverable.

## Canonical block structure per week (locked)
```
student/week-05/
├── overview.md         # weekly theme + must-do minimum vs. deepening (200–400 words)
├── self-study.md       # theory covering all 3 lessons (~2400–4000 words)
├── student-tasks.md    # 1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING tasks
├── vocabulary.md       # 10–18 terms
└── slides.md           # ~10–20 Markdown slides, '---' separators
teacher/week-05/
├── teacher-materials.md  # 3 × 90 min facilitation, with per-lesson Slide cues
└── in-class-tasks.md     # ≥1 MANDATORY teacher-led in-class exercise
```

Plus, only when a lecture segment genuinely needs deeper material, an additional `student/week-05/slides-l<n>-<topic>.md` file (4–8 slides). Rasmus decides per lecture segment.

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
The brief above is the slice for **Week 5** of an 8-week course. The full course brief and locked 24-lesson roadmap is at:
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/00-brief.md` (course brief)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/01-suunnitelma.md` (locked 24-lesson plan + 8-week roadmap)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/release/` (Week 1 — built, use as the in-course style reference)

## Golden sample (Finnish, style/depth/volume reference)
`/Users/agent/ai-perusteet-md/student/lesson-01/` + `/Users/agent/ai-perusteet-md/teacher/lesson-01/teacher-materials.md`

The week-level volume is ~3× a single golden-sample lesson. The Week 1 release at the path above is also a reference for an end-to-end English week.

