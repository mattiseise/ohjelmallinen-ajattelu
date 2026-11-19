# Computational Thinking — Week 8

A first-year course for vocational ICT students (roughly 15–17 years old, no prior programming experience). The course runs for 8 weeks, with 3 lessons of 90 minutes per week. This release contains the **Week 8** package — three lessons grouped under one theme.

The whole course turns around one central question:

> **How do I speak to a computer so that it understands what I want it to do?**

## Week 8 theme

**Programming languages in practice (JavaScript & C#, part 2)**

> The course closes the loop: you take pseudocode you wrote yourself in Week 6, translate it into JavaScript or C#, run it, find one bug, fix it, and explain how it works. Programming has stopped being mysterious.

## Lessons covered this week

- **Lesson 22**: Loops in code: a simple for or while structure (dual-language)
- **Lesson 23**: Small practical assignment: from pseudocode to JavaScript or C# (AT3 build day)
- **Lesson 24**: Testing, beginner-level debugging, 2-minute presentation (AT3 submitted and presented)

## Assessment touchpoint

AT3 (small JavaScript or C# solution from own pseudocode) is submitted in Lesson 23 and presented orally for 2 minutes in Lesson 24.

## Status

**This release contains only Week 8**. The other weeks live in their own releases under `material-pipeline/output/computational-thinking-en-week-XX/release/`. See the full 8-week roadmap below.

## Canonical block structure per week

```
student/week-08/
  overview.md          # one-page weekly overview: theme, must-do minimum vs. deepening
  self-study.md        # student-facing self-study text covering all three lessons
  student-tasks-js.md   # 1–2 MANDATORY + 2–3 DEEPENING tasks (JavaScript)
  student-tasks-csharp.md  # parallel pairs in C#
  vocabulary.md        # 10–18 terms with English definitions
  slides.md            # ~10–20 Markdown slides separated by `---`
teacher/week-08/
  teacher-materials.md # learning objectives, misconceptions, three 90-min lesson plans, formative assessment
  in-class-tasks.md    # at least one MANDATORY teacher-led classroom activity
```

If a lecture segment in `teacher-materials.md` needs deeper material than the main slide deck provides, a supplementary deck `slides-l<n>-<topic>.md` is shipped in `student/week-08/`. The lesson's Slide cues subsection names the supplement.

## Week 8 files

| Week | Status | Files |
|---|---|---|
| 08 — Programming languages in practice (JavaScript & C#, part 2) | **built** | [overview](student/week-08/overview.md) · [self-study](student/week-08/self-study.md) · [student-tasks-js](student/week-08/student-tasks-js.md) · [student-tasks-csharp](student/week-08/student-tasks-csharp.md) · [vocabulary](student/week-08/vocabulary.md) · [slides](student/week-08/slides.md) · [teacher-materials](teacher/week-08/teacher-materials.md) · [in-class-tasks](teacher/week-08/in-class-tasks.md) |

## Full 8-week roadmap

### Week 1 — Computational thinking

| L# | Topic | Status |
|----|------|--------|
| 01 | What does computational thinking mean? Humans, computers, and interpreting instructions | **built** |
| 02 | Algorithms in everyday life: step-by-step instructions without code | **built** |
| 03 | Precise and imprecise instructions: testing and improving instructions | **built** |

### Week 2 — Decomposing a problem

| L# | Topic | Status |
|----|------|--------|
| 04 | Decomposing a problem: main task, subtasks, and goal | **built** |
| 05 | Order of steps and dependencies | **built** |
| 06 | Decomposing an IT-related task (AT1 submitted) | **built** |

### Week 3 — Describing a process

| L# | Topic | Status |
|----|------|--------|
| 07 | Describing a process: list, step-by-step structure, simple flowchart | **built** |
| 08 | Abstraction | **built** |
| 09 | Reusable instructions and the idea of a function without code | **built** |

### Week 4 — Comparing solutions

| L# | Topic | Status |
|----|------|--------|
| 10 | Same problem, multiple solutions | **built** |
| 11 | Criteria for evaluating solutions: clarity, efficiency, repeatability, error-proneness | **built** |
| 12 | Improving one's own solution and using peer feedback | **built** |

### Week 5 — Logic structures

| L# | Topic | Status |
|----|------|--------|
| 13 | Sequence: a program proceeds step by step | **built** |
| 14 | Conditions: if-then-else thinking and decision trees | **built** |
| 15 | Repetition: doing the same thing multiple times | **built** |

### Week 6 — From thinking to code

| L# | Topic | Status |
|----|------|--------|
| 16 | Pseudocode: from natural language to a more precise format | **built** |
| 17 | Input, processing, output, and the idea of a variable | **built** |
| 18 | Testing pseudocode: dry running (AT2 submitted) | **built** |

### Week 7 — Programming languages in practice (JavaScript & C#, part 1)

| L# | Topic | Status |
|----|------|--------|
| 19 | Why are programming languages needed? Syntax, commands, JavaScript and C# | **built** |
| 20 | First commands: console.log / Console.WriteLine, values, variables | **built** |
| 21 | Conditions in code: if, else, comparisons | **built** |

### Week 8 — Programming languages in practice (JavaScript & C#, part 2)

| L# | Topic | Status |
|----|------|--------|
| [22](student/week-08/self-study.md) | Loops in code: a simple for or while structure | **built** |
| [23](student/week-08/self-study.md) | Small practical assignment: from pseudocode to JavaScript or C# (AT3 build day) | **built** |
| [24](student/week-08/self-study.md) | Testing, beginner-level debugging, 2-minute presentation (AT3 submitted) | **built** |

## Source of truth

- The week's locked plan: `../01-suunnitelma.md`
- The week's original brief: `../00-brief.md`
- Course brief and original 24-lesson plan: `../../computational-thinking-en-week-01/00-brief.md` and `../../computational-thinking-en-week-01/01-suunnitelma.md`

If anything in this release contradicts the plan, the plan wins. Send corrections back through the material pipeline.
