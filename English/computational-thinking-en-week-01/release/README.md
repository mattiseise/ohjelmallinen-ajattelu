# Computational Thinking

A first-year course for vocational ICT students (roughly 15–17 years old, no prior programming experience). The course runs for 8 weeks, with 3 lessons of 90 minutes per week — 24 lessons in total. It begins with everyday instructions a teenager already gives every day, gradually moves through decomposition, abstraction, sequence, condition and repetition, and only in the last two weeks translates that thinking into a tiny browser-based JavaScript program. Programming is treated as the last layer; the thinking is what the course actually trains.

The whole course turns around one central question:

> **How do I speak to a computer so that it understands what I want it to do?**

## Status

This release contains only **Week 1** (Lessons 1–3). The full 24-lesson plan is locked in `01-suunnitelma.md` at the project root; weeks 2–8 will be produced in later pipeline runs. The folder layout below is already in its final shape, so each future week can be dropped into `student/week-XX/` and `teacher/week-XX/` without restructuring anything else.

## Canonical block structure per week

Every week in this course is delivered as seven Markdown files in two folders. Filenames are exact, lowercase, kebab-case:

```
student/week-XX/
  overview.md          # one-page weekly overview: theme, can-do statements, core vs. deepening
  self-study.md        # student-facing self-study text covering all three lessons
  student-tasks.md     # 1–2 MANDATORY + 2–3 DEEPENING tasks
  vocabulary.md        # 10–18 terms with English definitions, including a look-ahead preview term
  slides.md            # ~10–20 Markdown slides separated by `---`; orchestrator converts to PPTX
teacher/week-XX/
  teacher-materials.md # learning objectives, misconceptions, three 90-min lesson plans, formative assessment
  in-class-tasks.md    # at least one MANDATORY teacher-led classroom activity, plus optional extras
```

Slides are delivered as Markdown only (`slides.md`); PPTX conversion happens downstream from this release.

## Week index

| Week | Status | Files |
|---|---|---|
| 01 — Computational thinking | **built** | [overview](student/week-01/overview.md) · [self-study](student/week-01/self-study.md) · [student-tasks](student/week-01/student-tasks.md) · [vocabulary](student/week-01/vocabulary.md) · [slides](student/week-01/slides.md) · [teacher-materials](teacher/week-01/teacher-materials.md) · [in-class-tasks](teacher/week-01/in-class-tasks.md) |

## Full 8-week roadmap

The course is grouped by week. Only Week 1 is built in this release; the rest are **planned** and will be produced in later pipeline runs. Three assessed tasks (AT1 at the end of Week 2, AT2 around Week 6, AT3 in Week 8) are each anchored in the student's own context, their own artefact, and a short oral or recorded element.

### Week 1 — Computational thinking

| L# | Topic | Status |
|----|------|--------|
| [01](student/week-01/self-study.md) | What does computational thinking mean? Humans, computers, and interpreting instructions | **built** |
| [02](student/week-01/self-study.md) | Algorithms in everyday life: step-by-step instructions without code | **built** |
| [03](student/week-01/self-study.md) | Precise and imprecise instructions: testing and improving instructions | **built** |

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

- `../01-suunnitelma.md` — the locked Week 1 plan and the course context Sune used to scope this run: per-week breakdown of Week 1 (L1–L3 objectives, vocabulary, core minimum vs. deepening), forward-looking stubs for Weeks 2–8, scope boundaries, and the 29 acceptance criteria every weekly package must meet.
- `../00-brief.md` — the original brief from which the plan was derived.

If anything in this release contradicts the plan, the plan wins. Send corrections back through the material pipeline.
