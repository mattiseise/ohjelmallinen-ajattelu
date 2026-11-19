# Computational Thinking — Week 4

A first-year course for vocational ICT students (roughly 15–17 years old, no prior programming experience). The course runs for 8 weeks, with 3 lessons of 90 minutes per week. This release contains the **Week 4** package — three lessons grouped under one theme.

The whole course turns around one central question:

> **How do I speak to a computer so that it understands what I want it to do?**

## Week 4 theme

**Comparing solutions**

> More than one valid solution can solve the same problem. Picking between them is not a matter of taste — it is a matter of stated criteria.

## Lessons covered this week

- **Lesson 10**: Same problem, multiple solutions
- **Lesson 11**: Criteria for evaluating solutions: clarity, efficiency, repeatability, error-proneness
- **Lesson 12**: Improving one's own solution and using peer feedback

## Assessment touchpoint

No assessed task is submitted this week. Week 4 is the mid-course reflection point and feeds AT2 and AT3.

## Status

**This release contains only Week 4**. The other weeks live in their own releases under `material-pipeline/output/computational-thinking-en-week-XX/release/`. See the full 8-week roadmap below.

## Canonical block structure per week

```
student/week-04/
  overview.md          # one-page weekly overview: theme, must-do minimum vs. deepening
  self-study.md        # student-facing self-study text covering all three lessons
  student-tasks.md     # 1–2 MANDATORY + 2–3 DEEPENING tasks
  vocabulary.md        # 10–18 terms with English definitions
  slides.md            # ~10–20 Markdown slides separated by `---`
teacher/week-04/
  teacher-materials.md # learning objectives, misconceptions, three 90-min lesson plans, formative assessment
  in-class-tasks.md    # at least one MANDATORY teacher-led classroom activity
```

If a lecture segment in `teacher-materials.md` needs deeper material than the main slide deck provides, a supplementary deck `slides-l<n>-<topic>.md` is shipped in `student/week-04/`. The lesson's Slide cues subsection names the supplement.

## Week 4 files

| Week | Status | Files |
|---|---|---|
| 04 — Comparing solutions | **built** | [overview](student/week-04/overview.md) · [self-study](student/week-04/self-study.md) · [student-tasks](student/week-04/student-tasks.md) · [vocabulary](student/week-04/vocabulary.md) · [slides](student/week-04/slides.md) · [teacher-materials](teacher/week-04/teacher-materials.md) · [in-class-tasks](teacher/week-04/in-class-tasks.md) |

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
| [10](student/week-04/self-study.md) | Same problem, multiple solutions | **built** |
| [11](student/week-04/self-study.md) | Criteria for evaluating solutions: clarity, efficiency, repeatability, error-proneness | **built** |
| [12](student/week-04/self-study.md) | Improving one's own solution and using peer feedback | **built** |

### Week 5 — Logic structures

| L# | Topic | Status |
|----|------|--------|
| 13 | Sequence: a program proceeds step by step | planned |
| 14 | Conditions: if-then-else thinking and decision trees | planned |
| 15 | Repetition: doing the same thing multiple times | planned |

### Week 6 — From thinking to code

| L# | Topic | Status |
|----|------|--------|
| 16 | Pseudocode: from natural language to a more precise format | planned |
| 17 | Input, processing, output, and the idea of a variable | planned |
| 18 | Testing pseudocode: dry running (AT2 submitted) | planned |

### Week 7 — Programming languages in practice (JavaScript & C#, part 1)

| L# | Topic | Status |
|----|------|--------|
| 19 | Why are programming languages needed? Syntax, commands, JavaScript and C# | planned |
| 20 | First commands: console.log / Console.WriteLine, values, variables | planned |
| 21 | Conditions in code: if, else, comparisons | planned |

### Week 8 — Programming languages in practice (JavaScript & C#, part 2)

| L# | Topic | Status |
|----|------|--------|
| 22 | Loops in code: a simple for or while structure | planned |
| 23 | Small practical assignment: from pseudocode to JavaScript or C# (AT3 build day) | planned |
| 24 | Testing, beginner-level debugging, 2-minute presentation (AT3 submitted) | planned |

## Source of truth

- The week's locked plan: `../01-suunnitelma.md`
- The week's original brief: `../00-brief.md`
- Course brief and original 24-lesson plan: `../../computational-thinking-en-week-01/00-brief.md` and `../../computational-thinking-en-week-01/01-suunnitelma.md`

If anything in this release contradicts the plan, the plan wins. Send corrections back through the material pipeline.
