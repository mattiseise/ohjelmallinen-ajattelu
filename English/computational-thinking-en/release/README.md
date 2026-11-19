# Computational Thinking

A first-year course for vocational ICT students (roughly 15–17 years old, no prior programming experience). The course runs for 8 weeks, with 3 lessons of 90 minutes per week — 24 lessons in total. It begins with everyday instructions a teenager already gives every day, gradually moves through decomposition, abstraction, sequence, condition and repetition, and only in the last two weeks translates that thinking into a tiny browser-based JavaScript program. Programming is treated as the last layer; the thinking is what the course actually trains.

The whole course turns around one central question:

> **How do I speak to a computer so that it understands what I want it to do?**

## Status

**This release contains only Lesson 1.** The full 24-lesson plan is locked in `01-suunnitelma.md` at the project root, and lessons 2–24 will be produced in later pipeline runs. The folder layout below is already in its final shape, so each future lesson can be dropped into `student/lesson-XX/` and `teacher/lesson-XX/` without restructuring anything else.

## Canonical block structure per lesson

Every lesson in this course is delivered as four Markdown files in two folders. Filenames are exact, lowercase, kebab-case:

```
student/lesson-XX/
  self-study.md        # student-facing self-study text (800–1400 words)
  student-tasks.md     # 1–2 tasks, at least one AI-resilient (400–900 words)
  vocabulary.md        # 6–10 terms, at least one looking-ahead preview term
teacher/lesson-XX/
  teacher-materials.md # objectives, misconceptions, 90-min plan, assessment (800–1400 words)
```

A fifth file — `teacher/lesson-XX/teacher-led-tasks.md` — is **optional** and only added when a lesson genuinely needs a separate teacher-led group activity. Lesson 1 does not.

## Lesson index

| Lesson | Title | Files |
|---|---|---|
| 01 | Speaking to a computer — what does it actually hear? | [self-study](student/lesson-01/self-study.md) · [student-tasks](student/lesson-01/student-tasks.md) · [vocabulary](student/lesson-01/vocabulary.md) · [teacher-materials](teacher/lesson-01/teacher-materials.md) |

## Full 24-lesson roadmap

The course is grouped by week. Only Lesson 01 is built in this release; the rest are **planned** and will be produced in later pipeline runs. Three assessed tasks (AT1 in week 2/3, AT2 around weeks 5/6, AT3 in week 8) are all designed to be AI-resilient: each one requires the student's own context, their own artefact, and a short oral or recorded element.

### Week 1 — Computational thinking

| L# | Topic | Status |
|----|------|--------|
| [01](student/lesson-01/self-study.md) | What does computational thinking mean? Humans, computers, and interpreting instructions | **built** |
| 02 | Algorithms in everyday life: step-by-step instructions without code | planned |
| 03 | Precise and imprecise instructions: testing and improving instructions | planned |

### Week 2 — Decomposing a problem

| L# | Topic | Status |
|----|------|--------|
| 04 | Decomposing a problem: main task, subtasks, and goal | planned |
| 05 | Order of steps and dependencies | planned |
| 06 | Decomposing an IT-related task (AT1 submitted) | planned |

### Week 3 — Describing a process

| L# | Topic | Status |
|----|------|--------|
| 07 | Describing a process: list, step-by-step structure, and simple flowchart | planned |
| 08 | Abstraction | planned |
| 09 | Reusable instructions and the idea of a function without code | planned |

### Week 4 — Comparing solutions

| L# | Topic | Status |
|----|------|--------|
| 10 | Same problem, multiple solutions | planned |
| 11 | Criteria for evaluating solutions | planned |
| 12 | Improving one's own solution and using peer feedback | planned |

### Week 5 — Logic structures

| L# | Topic | Status |
|----|------|--------|
| 13 | Sequence | planned |
| 14 | Conditions: if-then-else thinking | planned |
| 15 | Repetition | planned |

### Week 6 — From thinking to code

| L# | Topic | Status |
|----|------|--------|
| 16 | Pseudocode | planned |
| 17 | Input, processing, output, and the idea of a variable | planned |
| 18 | Testing pseudocode: dry running (AT2 submitted) | planned |

### Week 7 — Programming languages in practice (JavaScript, part 1)

| L# | Topic | Status |
|----|------|--------|
| 19 | Why are programming languages needed? Syntax, commands, JavaScript | planned |
| 20 | First JavaScript commands: console.log, values, variables | planned |
| 21 | Conditions in JavaScript: if, else, comparisons | planned |

### Week 8 — Programming languages in practice (JavaScript, part 2)

| L# | Topic | Status |
|----|------|--------|
| 22 | Loops in JavaScript: for or while | planned |
| 23 | Small practical assignment: from pseudocode to JavaScript | planned |
| 24 | Testing, debugging, presentation (AT3 submitted and presented) | planned |

## Source of truth

- `../01-suunnitelma.md` — the locked course plan: full 24-lesson table, learning objectives by Bloom stage, assessment design, scope boundaries, and the 17 acceptance criteria every lesson must meet.
- `../00-brief.md` — the original brief from which the plan was derived.

If anything in this release contradicts the plan, the plan wins. Send corrections back through the material pipeline.
