# Brief — Computational Thinking course (English)

## Working title
Computational Thinking

## Purpose
Give beginning vocational IT students (~15 years old) a conceptual understanding of how programming works, before they learn an actual programming language in depth. The core question of the course is: *How do I speak to a computer so that it understands what I want it to do?*

## Target group
- First-year vocational ICT students, age ~15–17
- No prior programming competence assumed; basic ICT skills only
- May include students with support needs, low school motivation, or difficulty with abstract concepts
- Vocational upper secondary — practical relevance is critical

## Output language
**English** — full course in English. Börje (Finnish polishing gate) is skipped for this run.

## Course duration
8 weeks × 3 lessons per week × 90 min = 24 lessons total.

## Test scope (this pipeline run)
- **Sune**: lock the full 24-lesson plan + acceptance criteria + Rasmus briefing for Lesson 1.
- **Rasmus**: build **only Week 1 / Lesson 1** ("What does computational thinking mean? Humans, computers, and interpreting instructions") in full canonical 4-block format.
- **Linnea / Wilhelm**: audit Lesson 1 only.
- **Alfred**: package the single lesson as a Netlify-compatible release with course-level README pointing at the full plan.

## Canonical block structure per lesson (locked)
```
student/lesson-XX/
├── self-study.md
├── student-tasks.md
└── vocabulary.md
teacher/lesson-XX/
└── teacher-materials.md
```
**No slides.** If anything in the brief implies slides, treat them as out of scope.

## General course objectives
- Understand computational thinking, algorithm, abstraction.
- Break a problem into smaller parts.
- Describe a process in logical order.
- Recognize sequence, condition, repetition.
- Understand pseudocode.
- Move from natural language to formal instructions.
- Get a first introduction to JavaScript through practical examples (weeks 7–8 only).

## Pedagogical principles
- Highly practical, vocational-realistic.
- Everyday examples first, IT examples second.
- Programming concepts practiced without code before code.
- Errors treated as natural; many concrete exercises.
- Concepts revisited in multiple forms (everyday → process → pseudocode → JavaScript).
- Support for low-motivation / weak-abstraction students: templates, model answers, structured options.

## Weekly themes (from brief)
1. Computational thinking
2. Decomposing a problem
3. Describing a process
4. Comparing solutions
5. Logic structures
6. From thinking to code
7–8. Programming languages in practice: JavaScript

## Lesson-by-lesson topics (from brief PDF, locked)
| Wk | L# | Topic |
|----|----|----|
| 1 | 1 | What does computational thinking mean? Humans, computers, and interpreting instructions |
| 1 | 2 | Algorithms in everyday life: step-by-step instructions without code |
| 1 | 3 | Precise and imprecise instructions: testing and improving instructions |
| 2 | 4 | Decomposing a problem: main task, subtasks, and goal |
| 2 | 5 | Order of steps and dependencies |
| 2 | 6 | Decomposing an IT-related task |
| 3 | 7 | Describing a process: list, step-by-step structure, and simple flowchart |
| 3 | 8 | Abstraction |
| 3 | 9 | Reusable instructions and the idea of a function without code |
| 4 | 10 | Same problem, multiple solutions |
| 4 | 11 | Criteria for evaluating solutions |
| 4 | 12 | Improving one's own solution and using peer feedback |
| 5 | 13 | Sequence |
| 5 | 14 | Conditions: if-then-else thinking |
| 5 | 15 | Repetition |
| 6 | 16 | Pseudocode |
| 6 | 17 | Input, processing, output, and the idea of a variable |
| 6 | 18 | Testing pseudocode: dry running |
| 7 | 19 | Why are programming languages needed? Syntax, commands, JavaScript |
| 7 | 20 | First JavaScript commands: console.log, values, variables |
| 7 | 21 | Conditions in JavaScript: if, else, comparisons |
| 8 | 22 | Loops in JavaScript: for or while |
| 8 | 23 | Small practical assignment: from pseudocode to JavaScript |
| 8 | 24 | Testing, debugging, presentation |

## Assessed components (locked)
- **AT1** — End of week 2 / start of week 3 — decomposing an everyday or IT-related task into steps.
- **AT2** — End of week 5 / during week 6 — process description with sequence, condition, and repetition.
- **AT3** — Week 8 — small JavaScript solution from pseudocode.

## Tools (allowed)
Browser + console, text editor, paper, optional flowchart tool, optional Scratch/Blockly. No complicated setup.

## Golden sample (style, structure, content volume — same for all gates)
`/Users/agent/ai-perusteet-md/` — Tekoälyn perusteet (Business College Helsinki, 27 lessons, Finnish, deployed to Netlify via GitHub).
- Style/structure/volume reference for each lesson: `/Users/agent/ai-perusteet-md/student/lesson-01/` and `/Users/agent/ai-perusteet-md/teacher/lesson-01/teacher-materials.md`.
- Reference is for **style, depth, and content volume** — do not copy content. Output language is English; reference is Finnish.
