# Brief — Computational Thinking course, Week 7 (English)

## Week 7 theme
**Programming languages in practice (JavaScript & C#, part 1)**

## Lessons (locked from course plan)
- **L19**: Why are programming languages needed? Syntax, commands, and the role of JavaScript
- **L20**: First commands: console.log / Console.WriteLine, values, variables, simple calculations
- **L21**: Conditions in code: if, else, comparisons

## Central message for the week
A programming language is a way to make instructions precise enough for a computer to follow without guessing. The thinking is what we have been doing all course; the language is just the syntax it gets written in.

## Bloom cap
Understanding + Applying (run first commands, write a tiny if/else; no debugging frameworks).

## Vocational angle
Examples Rasmus should lean on: logging a value to the browser console; comparing two numbers (age check, password length check); printing a friendly greeting.

## Assessment touchpoint
Foundation for AT3 (translate own pseudocode into a small program). AT3 brief released in Week 8.

## Extra rules for this week

- **Dual-language requirement.** Lesson 19 is language-agnostic — explain *what* a programming language is and *what* syntax means before tying it to any specific language. Lessons 20 and 21 introduce concrete syntax in **both JavaScript and C#**, side by side.
- Split task files: produce `student-tasks-js.md` and `student-tasks-csharp.md` in addition to (or instead of) `student-tasks.md`. Use a brief `student-tasks.md` as an index pointing at the two language-specific files, OR skip `student-tasks.md` and use the two language files directly — Sune decides.
- Browser console (JavaScript) and a simple .NET interactive / online C# environment are the only execution targets. No IDE setup beyond browser/online tools.
- No automatic testing or debugging frameworks. Programming-task level is 'try it, run it, see what happens'.

## Output language
**English.** Börje (Finnish polishing) is skipped for this run.

## Output scope (this run)
- Sune produces the Week 7 plan with locked acceptance criteria, Rasmus briefing, and forward-looking stubs.
- Rasmus builds **only Week 7**.
- Linnea + Wilhelm audit Week 7.
- Alfred packages the Week 7 release in Markdown only.
- **No PDF, no PPTX rendering** in the pipeline this round. Markdown release is the deliverable.

## Canonical block structure per week (locked)
```
student/week-07/
├── overview.md         # weekly theme + must-do minimum vs. deepening (200–400 words)
├── self-study.md       # theory covering all 3 lessons (~2400–4000 words)
├── student-tasks.md    # 1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING tasks
├── vocabulary.md       # 10–18 terms
└── slides.md           # ~10–20 Markdown slides, '---' separators
teacher/week-07/
├── teacher-materials.md  # 3 × 90 min facilitation, with per-lesson Slide cues
└── in-class-tasks.md     # ≥1 MANDATORY teacher-led in-class exercise
```

Plus, only when a lecture segment genuinely needs deeper material, an additional `student/week-07/slides-l<n>-<topic>.md` file (4–8 slides). Rasmus decides per lecture segment.

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
The brief above is the slice for **Week 7** of an 8-week course. The full course brief and locked 24-lesson roadmap is at:
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/00-brief.md` (course brief)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/01-suunnitelma.md` (locked 24-lesson plan + 8-week roadmap)
- `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/release/` (Week 1 — built, use as the in-course style reference)

## Golden sample (Finnish, style/depth/volume reference)
`/Users/agent/ai-perusteet-md/student/lesson-01/` + `/Users/agent/ai-perusteet-md/teacher/lesson-01/teacher-materials.md`

The week-level volume is ~3× a single golden-sample lesson. The Week 1 release at the path above is also a reference for an end-to-end English week.

