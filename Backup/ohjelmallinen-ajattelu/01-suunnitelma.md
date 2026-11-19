# Computational Thinking — Course Plan (Sune, Gate #1)

Course: Computational Thinking (English)
Target: First-year vocational ICT students, ~15–17, no prior programming
Duration: 8 weeks x 3 lessons/week x 90 min = 24 lessons
Pipeline scope this run: Sune locks the full plan; Rasmus builds Lesson 1 only; Linnea/Wilhelm audit Lesson 1; Alfred packages a single-lesson Netlify release with course-level README pointing to this plan.

---

## Suunnitelma

### Course overview

The course answers one central question: **"How do I speak to a computer so that it understands what I want it to do?"** Students start from familiar everyday situations (instructions for a younger sibling, a recipe, getting to school) and gradually move toward a formal, step-by-step way of expressing instructions. By the end of week 6 students can write pseudocode that includes sequence, condition, and repetition. In weeks 7–8 the same pseudocode pattern is translated into a tiny, browser-based JavaScript program. Programming is treated as the *last* layer; computational thinking is the layer the course actually trains.

Pedagogical spine:
1. Everyday first, IT second, code last.
2. Each new concept is practiced first without code, then as a process description, then as pseudocode, then (in weeks 7–8) as JavaScript.
3. Errors and imprecision are surfaced early (Lesson 3 is explicitly built around imprecise instructions) so students learn that computers are literal, not stupid.
4. Three assessed tasks (AT1, AT2, AT3) are spaced so each rests on competencies the preceding weeks actually built.

### Learning objectives by Bloom stage

The course is mapped across Bloom's revised taxonomy. Earlier lessons live in the lower stages; later lessons require students to apply, analyze, and create.

| Bloom stage | What students do | Lessons that primarily live here |
|---|---|---|
| Remembering | Recall key vocabulary (algorithm, abstraction, sequence, condition, loop, variable, syntax). | 1, 2, 13, 16, 19, 20 |
| Understanding | Explain in own words why instructions must be precise; describe the role of decomposition, abstraction, conditions, loops. | 1, 2, 3, 4, 7, 8, 13, 14, 15, 17, 19 |
| Applying | Write step-by-step instructions, draw a simple flowchart, write pseudocode for a stated problem, write a first JavaScript snippet. | 2, 3, 5, 6, 7, 9, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23 |
| Analyzing | Compare multiple solutions to the same problem; identify dependencies; spot the cause of a bug. | 5, 10, 11, 12, 18, 24 |
| Evaluating | Apply criteria to judge which solution is better; give and receive peer feedback. | 11, 12, 24 |
| Creating | Decompose a real problem and produce an original process description (AT1); design a process with sequence + condition + repetition (AT2); produce a small original JavaScript program from own pseudocode (AT3). | 6, 12, 16–18, 22–24 |

Course-level objectives (summarized from brief):
- Understand computational thinking, algorithm, abstraction.
- Break a problem into smaller parts.
- Describe a process in logical order.
- Recognize sequence, condition, and repetition.
- Understand pseudocode and dry-run it.
- Translate pseudocode into a small JavaScript program.

### 24-lesson plan

Vocabulary previews below list the 3–6 core terms each lesson must define (Rasmus expands these in `vocabulary.md`).

| Wk | L# | Topic | Learning objectives (3–5) | Key vocabulary preview | Assessed-task link |
|----|----|------|---------------------------|------------------------|--------------------|
| 1 | 1 | What does computational thinking mean? Humans, computers, and interpreting instructions | (a) Define computational thinking in own words. (b) Explain that a computer follows instructions literally. (c) Give one everyday and one IT example of "speaking to a computer". (d) Recognize that ambiguity is a property of the *instruction*, not of the computer. | computational thinking, instruction, literal interpretation, ambiguity, computer (as instruction-follower); preview: algorithm | — |
| 1 | 2 | Algorithms in everyday life: step-by-step instructions without code | (a) Define algorithm. (b) Identify algorithms in everyday situations (recipe, route, morning routine). (c) Write a 5–10 step everyday algorithm in plain language. (d) Compare two algorithms for the same goal. | algorithm, step, input, output, goal; preview: precision | — |
| 1 | 3 | Precise and imprecise instructions: testing and improving instructions | (a) Identify ambiguous words in an instruction. (b) Rewrite an imprecise instruction to be unambiguous. (c) Test instructions by acting as the "literal computer". (d) Explain why testing reveals defects faster than re-reading. | precise, imprecise, ambiguity, test, edge case; preview: decomposition | — |
| 2 | 4 | Decomposing a problem: main task, subtasks, and goal | (a) Define decomposition. (b) Identify a main task and its subtasks. (c) State the goal of a task separately from its steps. (d) Decompose a familiar problem into 3–6 subtasks. | decomposition, main task, subtask, goal; preview: dependency | leads to AT1 |
| 2 | 5 | Order of steps and dependencies | (a) Recognize when step B depends on step A. (b) Reorder a scrambled set of steps into a valid sequence. (c) Spot impossible orderings. (d) Visualize dependencies as a simple list or arrows. | order, dependency, prerequisite, sequence; preview: IT process | leads to AT1 |
| 2 | 6 | Decomposing an IT-related task | (a) Apply decomposition to an IT scenario (e.g. setting up a workstation, onboarding a user). (b) Distinguish technical subtasks from human subtasks. (c) Produce a clean decomposed plan for **AT1**. | IT task, subtask, workflow, decomposition; preview: process description | **AT1 submitted at end of L6 / start of L7** |
| 3 | 7 | Describing a process: list, step-by-step structure, and simple flowchart | (a) Convert a list of steps into a flowchart with start/end and arrows. (b) Read a flowchart and explain what it does. (c) Choose between list and flowchart depending on complexity. | process, flowchart, node, arrow, start/end; preview: abstraction | — |
| 3 | 8 | Abstraction | (a) Define abstraction as "hide detail, keep what matters". (b) Identify abstractions in everyday life (a bus stop, an icon). (c) Rewrite a detailed process at a higher abstraction level. | abstraction, detail, level, generalization; preview: function | — |
| 3 | 9 | Reusable instructions and the idea of a function without code | (a) Recognize repeated instruction blocks. (b) Name a reusable block and call it by that name. (c) Explain why naming reduces error. | reuse, name, function (informal), parameter (informal); preview: alternative solutions | — |
| 4 | 10 | Same problem, multiple solutions | (a) Produce two different valid solutions for the same problem. (b) Explain that "correct" is not unique. (c) Identify trade-offs between solutions. | solution space, trade-off, alternative; preview: criteria | — |
| 4 | 11 | Criteria for evaluating solutions | (a) State 3 criteria for evaluating a solution (correctness, simplicity, speed, readability). (b) Apply criteria to compare two solutions. (c) Justify a choice with criteria, not preference. | criterion, correctness, simplicity, readability, efficiency; preview: peer feedback | — |
| 4 | 12 | Improving one's own solution and using peer feedback | (a) Give specific, criteria-based feedback to a peer. (b) Receive feedback without taking it personally. (c) Revise own solution based on feedback. | revision, peer feedback, iteration; preview: sequence | — |
| 5 | 13 | Sequence | (a) Define sequence. (b) Recognize that order of statements changes the outcome. (c) Trace a short sequence manually. | sequence, statement, order; preview: condition | foundation for AT2 |
| 5 | 14 | Conditions: if-then-else thinking | (a) Identify decisions in everyday processes. (b) Express decisions as if-then / if-then-else. (c) Combine two conditions with AND/OR informally. | condition, if, then, else, AND, OR; preview: repetition | foundation for AT2 |
| 5 | 15 | Repetition | (a) Spot repeated steps. (b) Express repetition as "repeat until …" or "for each …". (c) Distinguish bounded from unbounded repetition. | repetition, loop, repeat, until, for each; preview: pseudocode | foundation for AT2 |
| 6 | 16 | Pseudocode | (a) Define pseudocode. (b) Write pseudocode using sequence, condition, and repetition. (c) Read peer pseudocode and predict its behavior. | pseudocode, indent, keyword (informal); preview: variable | leads to AT2 |
| 6 | 17 | Input, processing, output, and the idea of a variable | (a) Identify input, processing, and output in a small program. (b) Use a variable to store a value. (c) Update a variable. | input, processing, output, variable, value; preview: dry run | leads to AT2 |
| 6 | 18 | Testing pseudocode: dry running | (a) Dry-run pseudocode with a trace table. (b) Find a bug in pseudocode. (c) Fix the pseudocode and re-run. | dry run, trace table, bug, fix; preview: programming language | **AT2 submitted around end of week 5 / during week 6** |
| 7 | 19 | Why are programming languages needed? Syntax, commands, JavaScript | (a) Explain why a computer needs a formal language. (b) Define syntax. (c) Recognize JavaScript as one of many programming languages. | programming language, syntax, command, JavaScript; preview: console.log | bridge to AT3 |
| 7 | 20 | First JavaScript commands: console.log, values, variables | (a) Open the browser console. (b) Run `console.log` with a value. (c) Declare a variable with `let` and print it. | console, console.log, let, value, variable (formal); preview: comparison operator | bridge to AT3 |
| 7 | 21 | Conditions in JavaScript: if, else, comparisons | (a) Write an `if` statement. (b) Add `else`. (c) Use `==`, `!=`, `<`, `>` correctly. | if, else, comparison, ==, !=, <, >; preview: loop | bridge to AT3 |
| 8 | 22 | Loops in JavaScript: for or while | (a) Write a `for` loop or a `while` loop with a counter. (b) Avoid infinite loops by ensuring termination. (c) Combine a loop with an `if`. | for, while, counter, infinite loop, termination; preview: AT3 brief | bridge to AT3 |
| 8 | 23 | Small practical assignment: from pseudocode to JavaScript | (a) Translate a piece of own pseudocode into working JavaScript. (b) Run it in the browser console. (c) Produce **AT3** draft. | translation, runtime, error; preview: debugging | **AT3 in progress** |
| 8 | 24 | Testing, debugging, presentation | (a) Read a console error message and locate its cause. (b) Apply one small fix and re-run. (c) Present own AT3 program orally in 2 minutes. | bug, debugging, error message, presentation; — | **AT3 submitted and presented** |

### Assessed tasks (locked from brief)

- **AT1** — end of week 2 / start of week 3 — *Decompose an everyday or IT-related task into steps.* Builds on lessons 4–6.
- **AT2** — end of week 5 / during week 6 — *Describe a process using sequence, condition, and repetition* (delivered as pseudocode or annotated flowchart). Builds on lessons 13–18.
- **AT3** — week 8 — *Translate own pseudocode into a small JavaScript program, run it in the browser, and present.* Builds on lessons 19–24.

All three assessed tasks are designed to be **AI-resilient**: each requires the student's own concrete context (their chosen task, their own decomposition, their own pseudocode), a screenshot or recording of their own execution, and/or a short oral presentation. See the AI-resilience rule under Hyväksymiskriteerit.

---

## Rajaukset

**Out of scope for this course (do not let Rasmus produce these):**
- No slide deck, no PowerPoint, no `.pptx`, no Google Slides, no Keynote, no Reveal.js, no "slides.md". The brief is explicit: **no slides.** If anything in the brief or external requests implies slides, treat as out of scope.
- No deep JavaScript: no DOM manipulation, no `npm`, no frameworks, no build tools, no modules, no async, no classes. Browser console + plain `<script>` only.
- No IDE setup beyond a browser and any plain text editor the student already has. No VS Code installation guide, no Node.js install.
- No formal computer-science theory: no Big-O, no Turing machines, no formal grammars, no recursion as a topic of its own (it may appear once, briefly, in lesson 9 as a side note at most).
- No coverage of programming languages other than JavaScript. Scratch / Blockly may be *optionally* mentioned as a sandbox, never required.
- No graded essays, no long written reports. Assessed tasks are artefact + short reflection.
- No external accounts that require email signup (no Replit account, no CodePen account). Browser DevTools console is sufficient.

**Language:** English throughout. **Börje (Finnish polishing gate) is skipped.** Rasmus writes in English; Alfred packages in English; the course-level README is in English.

**Pipeline scope this run:**
- Sune produces this plan (you are reading it).
- Rasmus builds **only Lesson 1** in the canonical 4-block format. No other lessons are produced in this run.
- Linnea and Wilhelm audit Lesson 1 only.
- Alfred packages a Netlify-compatible single-lesson release. The course-level README must reference this plan file (`01-suunnitelma.md`) as the source of truth for the full 24-lesson roadmap, and clearly mark lessons 2–24 as "planned, not yet built".

---

## Hyväksymiskriteerit

Wilhelm verifies Lesson 1 against these concrete, checkable criteria.

### Structural

1. **All 4 canonical blocks present, with exactly these filenames** (case-sensitive, lowercase, kebab-case):
   - `student/lesson-01/self-study.md`
   - `student/lesson-01/student-tasks.md`
   - `student/lesson-01/vocabulary.md`
   - `teacher/lesson-01/teacher-materials.md`
2. **No extra files** in `student/lesson-01/` or `teacher/lesson-01/` (no slides, no images directory unless content explicitly references images and Rasmus included them — none should be required for Lesson 1).
3. `teacher/lesson-01/teacher-led-tasks.md` is **optional** for Lesson 1 and **not required** (the brief does not need teacher-led group tasks at the very first lesson; the teacher-materials file is sufficient).

### Volume (roughly matching golden sample lesson-01)

Word counts are approximate brackets, not hard limits. Use them as sanity checks.

4. `self-study.md`: **800–1400 words**, with an `## Johdanto`-equivalent intro section ("Introduction") and **3–5 body H2 sections** plus a summary section. Must include **at least 2 reflection prompts** ("Pause for a moment:" style block quotes), mirroring the golden sample's `> **Pysähdy hetkeksi:**` pattern.
5. `student-tasks.md`: **400–900 words**, **1–2 tasks total**. If 2, one must be marked recommended and the other deepening (mirror the golden sample's 🟢 SUOSITELTU / 🟣 SYVENTÄVÄ split — Rasmus may translate the labels to English, e.g. "RECOMMENDED" and "DEEPENING").
6. `vocabulary.md`: **6–10 terms**, each with a 1–3 sentence definition. Must include **one "looking ahead" preview term** (e.g. *algorithm*) explicitly flagged as next-lesson preview.
7. `teacher-materials.md`: **800–1400 words**, with these required H2 sections (English equivalents of the golden sample):
   - Learning objectives for this lesson (mapped to Bloom stages — Remembering and Understanding only for Lesson 1).
   - Common misconceptions (at least 4, each with a "Correction:" subsection).
   - Teacher facilitation guide split into **Before class**, **During class**, **Answers to common student questions**.
   - A **realistic 90-minute lesson structure**, broken into time slots (e.g. 0–10 min warm-up, 10–25 min instructor input, 25–55 min activity, 55–75 min discussion, 75–90 min reflection + AT preview). Times must sum to 90 minutes.
   - Assessment tips (formative for Lesson 1; no summative assessment yet).

### Content

8. `self-study.md` contains **at least 2 concrete everyday examples** (e.g. giving directions, a recipe, a younger sibling following instructions literally) **AND at least 2 concrete IT examples** (e.g. a search query, a file-name rename, a wrong-path error message). Everyday examples must appear **before** IT examples in the text.
9. The central question of the lesson — *"How do I speak to a computer so that it understands what I want it to do?"* — must appear verbatim or near-verbatim in the introduction or summary of `self-study.md`.
10. The lesson must establish that **a computer interprets instructions literally**, and that ambiguity is a property of the instruction, not a fault of the computer.
11. **Bloom stage cap:** Lesson 1 may only target **Remembering and Understanding**. No "create / design / build" verbs in the learning objectives. (Applying first appears in Lesson 2.)

### Tasks (AI resilience)

12. `student-tasks.md` contains **1–2 tasks**, and **at least one task is AI-resilient**, meaning it cannot be trivially solved by pasting the prompt into an LLM. Acceptable resilience mechanisms (one or more must apply to the AI-resilient task):
    - Requires the student's own concrete context (a real instruction they wrote, a real situation in their life or workplace, a screenshot of their own screen).
    - Requires producing physical / observable evidence (e.g. acting out the instruction with a classmate, recording a short video, photographing a result).
    - Requires the student to **critique or improve** an AI-generated answer rather than produce one (the LLM is treated as a sparring partner the way the golden sample does).
13. If an LLM is used as a sparring partner inside a task, the task must include a sample prompt block (fenced code block) and explicit instruction not to accept the AI's output verbatim.

### Teacher block

14. `teacher-materials.md` includes:
    - Learning objectives mapped to Bloom (criterion 11 above).
    - At least 4 common misconceptions with corrections.
    - A 90-minute lesson structure whose slot times sum to exactly 90.

### Language and polish

15. **English throughout.** No Finnish words except possibly proper nouns. The course README header and section headings (`Suunnitelma`, `Rajaukset`, etc., in this plan) may remain Finnish in *this plan file* because they are part of the Sune template; **Rasmus's lesson outputs must be fully English**, including section headings.
16. **No slide deck files anywhere.** No reference to PowerPoint, Keynote, Reveal.js, Google Slides, or `slides.md`. If Wilhelm finds any, that is a hard fail.
17. Markdown is valid: every code fence closes, every table renders, no broken links.

---

## Briefing Rasmukselle

### Lesson 1 — full detailed briefing

**Topic (locked from brief):** "What does computational thinking mean? Humans, computers, and interpreting instructions"

**Central question of the lesson (must appear in the text):**
> *How do I speak to a computer so that it understands what I want it to do?*

**Bloom stage cap:** Remembering + Understanding only. Verbs to use in objectives: *define, describe, explain, recognize, identify, give an example of*. Verbs to **avoid**: *create, build, design, evaluate, analyze, apply, write a program*. Applying first appears in Lesson 2 (writing an everyday algorithm).

**Pedagogical lead:** everyday before IT, always. The first example in `self-study.md` must be something a 15-year-old already knows — giving a friend directions, telling a younger sibling how to make a sandwich, explaining a TikTok dance step-by-step. Only after that does the lesson pivot to IT examples (a search query that returns nothing because of a typo; a file the computer "can't find" because the path is wrong; an instruction in a chat bot that gets misinterpreted).

#### Block 1 — `student/lesson-01/self-study.md`

Required structure (mirror golden sample lesson-01):
- `# <Lesson title>` — a short, hooky title. Suggestion: *"Speaking to a computer — what does it actually hear?"* (Rasmus may improve.)
- `## Introduction` — opens with a familiar scene, names the central question verbatim, and tells the student what they will be able to do after the lesson.
- `## What is computational thinking?` — define computational thinking as *a way of thinking about problems so that a computer (or anyone following instructions literally) can solve them*. Keep the definition short and quotable. Mention that the four classic pillars (decomposition, pattern recognition, abstraction, algorithms) exist and will each get their own lessons — do not unpack them now.
- `## A computer takes you literally` — the heart of the lesson. Use **2 concrete everyday examples** to show literal interpretation: e.g. (i) telling a sibling "make a sandwich" and them putting the bread on the outside of the cheese, and (ii) giving someone directions like "turn at the big tree" when there are three big trees. Then **2 concrete IT examples**: e.g. a search for `pyhton tutorial` returning nothing useful, and a file path with a missing slash. The lead-in example must be everyday, not IT.
- `## Ambiguity is in the instruction, not the computer` — reframe the misconception "the computer is stupid" into "the instruction was ambiguous". This is the conceptual pivot of the lesson.
- `## Why this matters for an IT professional` — a short, vocational paragraph: in IT work you write instructions for machines, for other developers, and for end users; the skill of writing unambiguous instructions is what you spend your career building.
- `## Summary` — one paragraph that closes the loop on the central question and previews Lesson 2 (*algorithms in everyday life*).

Include **at least 2 reflection prompts** as block quotes in the body (mirror golden sample's `> **Pysähdy hetkeksi:**`). Use the English equivalent: `> **Pause for a moment:**`. Good prompt examples:
- *Pause for a moment: think of an instruction you gave today that someone misunderstood. What was ambiguous about it?*
- *Pause for a moment: when an app does "the wrong thing", is it broken, or did it follow your instruction exactly?*

Volume target: **800–1400 words**, comparable to golden sample lesson-01's self-study.

#### Block 2 — `student/lesson-01/student-tasks.md`

**1–2 tasks**, mirroring the golden sample's structure (one recommended task and optionally one deepening task).

Task ideas Rasmus should adapt:

**Task 1.1 — RECOMMENDED — "The literal robot game"** (AI-resilient by construction)
- Step 1: Student writes a 6–10 step instruction for a familiar task in plain English (e.g. "make a cup of tea", "log in to the school portal", "send a message on Discord"). Must be their own instruction, written from scratch.
- Step 2: Student gives the instructions to a classmate (or family member, or themselves recorded on video) who must follow them **literally**, doing exactly what is written and nothing else. No assumptions.
- Step 3: Student observes at least 3 places the literal follower got stuck, and notes which word or step was ambiguous.
- Step 4: Student rewrites the instructions to remove the ambiguity, and re-tests with the same follower.
- Step 5: Short reflection (3–5 sentences): what kind of ambiguity was hardest to remove? How is this related to "speaking to a computer"?
- AI-resilience: requires a real human follower or a self-recording, plus the student's own original instructions. Pasting this task into an LLM produces a fictional answer the teacher can easily spot.

**Task 1.2 — DEEPENING — "Spot the ambiguity"** (optional, lighter AI use as sparring partner)
- Student is given a short list of 5–6 ambiguous instructions (Rasmus writes these) such as *"Save the file in the usual place"*, *"Run the script after lunch"*, *"Make the button bigger"*. The student annotates each: what is ambiguous, and how would they make it precise?
- After their own pass, the student may paste their annotations into an LLM with a sparring-partner prompt (Rasmus provides a fenced code-block sample prompt, in the style of the golden sample) and ask the LLM to challenge their analysis, *not* to give answers.
- Final 3–5 sentence reflection.

Both tasks must include a short "Tip" block, in the golden-sample style, telling students they don't have to submit but should keep their notes — they will reuse them when the assessed task AT1 lands at end of week 2.

Volume target: **400–900 words**.

#### Block 3 — `student/lesson-01/vocabulary.md`

**6–10 terms.** Required terms (Rasmus may add 1–2 of their own if useful, but must not skip any of the required ones):

1. **Computational thinking** — a way of thinking about problems so they can be solved by following clear, literal instructions.
2. **Instruction** — a single, executable step a person or computer can follow.
3. **Algorithm** — a sequence of clear steps that solves a problem or completes a task. *(Flag as "looking ahead — central topic of Lesson 2".)*
4. **Literal interpretation** — doing exactly what is written, without filling in unstated assumptions.
5. **Ambiguity** — a property of an instruction that allows more than one reasonable interpretation.
6. **Precision** — the quality of an instruction that leaves no room for ambiguity.
7. **Computer (as instruction-follower)** — a machine that follows the instructions it is given, literally and without judgement.

Optional additions Rasmus may include: *programmer*, *user*, *input*, *output* (kept very short).

The looking-ahead preview term is **algorithm** — explicitly marked.

Volume target: roughly **150–350 words** total (golden sample lesson-01 vocabulary is about this length).

#### Block 4 — `teacher/lesson-01/teacher-materials.md`

Required H2 sections (mirror golden sample):

1. **Learning objectives for this lesson** — 3–5 objectives, each mapped to a Bloom stage (Remembering or Understanding only for Lesson 1).
2. **Common misconceptions** — at least 4. Suggested set:
   - "The computer is stupid / dumb." → Correction: the computer is *literal*, not stupid. Ambiguity is in the instruction.
   - "Computational thinking is just programming." → Correction: it is the thinking *behind* programming; it applies to recipes, instructions to a colleague, and writing a help-desk ticket.
   - "Algorithms are something only computer scientists write." → Correction: every recipe, route, and morning routine is an algorithm.
   - "If the computer did the wrong thing, it's broken." → Correction: it did what you told it to. Read your instruction again.
3. **Teacher facilitation guide**:
   - **Before class**: prepare 3–4 deliberately ambiguous instructions to act out in front of the class; consider whether the school has any literal-interpretation IT examples (e.g. an email filter that flagged the wrong message).
   - **During class**: start with the literal-robot demonstration (teacher acts out one of the student's ambiguous instructions); use the board to collect everyday vs. IT examples in two columns; ask questions before giving answers.
   - **Answers to common student questions** — at least 3 expected questions with answers (e.g. *"Is Google an algorithm?"*, *"Why doesn't autocorrect understand me?"*, *"Is this going to be on the assessed task?"*).
4. **90-minute lesson structure** — concrete time slots summing to 90. Suggested skeleton (Rasmus may adjust):
   - 0–10 min: warm-up — teacher demos a literal-robot moment from an ambiguous student instruction.
   - 10–25 min: short instructor input on the central question + definition of computational thinking.
   - 25–55 min: pair activity — students draft an instruction and a partner follows it literally (this is also the start of Task 1.1).
   - 55–75 min: whole-class debrief — where did literal interpretation break down? Build the "everyday vs. IT" board.
   - 75–85 min: introduction of the vocabulary (5 minutes max — kept light because Lesson 1 is Remembering/Understanding only).
   - 85–90 min: closing reflection prompt + preview of Lesson 2 (*algorithms in everyday life*).
5. **Assessment tips** — only formative for Lesson 1. Suggest 2–3 quick checks the teacher can run during class (e.g. exit ticket: "Write one ambiguous instruction you used today").

Volume target: **800–1400 words**.

#### Common pitfalls for Rasmus to avoid in Lesson 1

- Do not introduce flowcharts, pseudocode, variables, loops, or any code. All of those have their own lessons.
- Do not over-define "abstraction" — that is Lesson 8.
- Do not use the phrase "the computer is dumb / stupid". Reframe to "the computer is literal".
- Do not use code blocks for JavaScript in Lesson 1. Code fences are only for prompt examples (in the deepening task, if used) or ambiguous-instruction examples in plain text.
- Do not produce any slide deck, `slides.md`, or PowerPoint output. The brief explicitly forbids slides.
- Do not introduce vocational scenarios that require prior IT knowledge the student doesn't have (e.g. CI/CD, Linux permissions). Keep IT examples to things a first-year student has touched: file paths, search queries, app settings, chat bots, autocorrect.

---

### Lessons 2–24 — forward-looking stubs (one paragraph each)

These are not built in this run. They give Rasmus the trajectory so Lesson 1 lands cleanly.

**Lesson 2 — Algorithms in everyday life.** Builds directly on Lesson 1's central question. Now that students accept computers follow instructions literally, this lesson names the artefact: a clear sequence of literal steps is an *algorithm*. Examples remain everyday (recipes, morning routine, route to school). First time students *write* their own algorithm in plain language. Connects backward to Lesson 1's "instruction" and forward to Lesson 3's "precise vs. imprecise".

**Lesson 3 — Precise and imprecise instructions.** Stress-tests Lesson 2's algorithms. Students learn to find ambiguity (Lesson 1 vocabulary) inside their own algorithms (Lesson 2 artefacts) and rewrite them. Closes Week 1 with a clear payoff: students now write instructions a literal follower can execute.

**Lesson 4 — Decomposing a problem.** Pivot to the second pillar of computational thinking. Now that students can write small algorithms, they confront problems too big for one. Introduces main task / subtasks / goal. Starts the runway toward AT1 (end of Week 2).

**Lesson 5 — Order of steps and dependencies.** Decomposition is not enough if the order is wrong. Students learn dependencies (B needs A first) and practice rearranging scrambled steps. Introduces a precursor of *sequence*, which becomes formal in Week 5.

**Lesson 6 — Decomposing an IT-related task.** Switches the everyday-first / IT-second pattern: this is the first lesson where IT is the lead context. AT1 is submitted at the end of this lesson or start of Lesson 7. Vocational realism is critical here (workstation setup, onboarding a new user, ticket triage).

**Lesson 7 — Describing a process: list, step-by-step, simple flowchart.** Begins the *describing a process* week. Students learn to draw a simple flowchart with start/end and arrows. First visual representation in the course. Connects back to the algorithms of Week 1.

**Lesson 8 — Abstraction.** The third pillar of computational thinking. "Hide detail, keep what matters." Uses everyday abstractions (a bus stop, an icon, a username) before IT abstractions. Sets up Lesson 9.

**Lesson 9 — Reusable instructions and the idea of a function without code.** Students notice repeated blocks in their algorithms (Lessons 2, 6) and learn to name and reuse them. The word *function* appears for the first time, but only informally. No code. Bridges to Week 4's discussion of alternatives.

**Lesson 10 — Same problem, multiple solutions.** Breaks the "one right answer" assumption. Students produce two different valid solutions to the same problem. Sets up Lesson 11's criteria.

**Lesson 11 — Criteria for evaluating solutions.** Introduces correctness, simplicity, readability, speed as criteria. Students apply these to compare their own solutions from Lesson 10.

**Lesson 12 — Improving one's own solution and using peer feedback.** Closes Week 4. Students give and receive criteria-based feedback (Lesson 11) and revise their own work. Practices the iterative loop that returns in Week 8.

**Lesson 13 — Sequence.** First lesson of the *logic structures* week. Formalizes what Week 1 and Week 2 already practiced: statements execute in order, and order matters.

**Lesson 14 — Conditions: if-then-else thinking.** Decisions in everyday processes (if it rains, take an umbrella) become formal if-then-else. AND/OR introduced informally. Sets up the assessed task (AT2).

**Lesson 15 — Repetition.** Repeat-until and for-each. Bounded vs. unbounded. Last logic structure before pseudocode brings them all together in Lesson 16.

**Lesson 16 — Pseudocode.** The synthesis of Weeks 1–5. Students write pseudocode that uses sequence, condition, and repetition. AT2 begins to take shape here.

**Lesson 17 — Input, processing, output, and the idea of a variable.** Adds state to the pseudocode model. Students can now store and update a value. This is the last conceptual piece needed before code.

**Lesson 18 — Testing pseudocode: dry running.** Students dry-run pseudocode with a trace table, find a bug, fix it. AT2 is submitted around this lesson. This is the last code-free lesson.

**Lesson 19 — Why are programming languages needed? Syntax, commands, JavaScript.** The bridge into code. Explains why a formal language is necessary (a computer can't disambiguate the way a human can, see Lesson 1). Names JavaScript as one option among many.

**Lesson 20 — First JavaScript commands: console.log, values, variables.** Students open the browser console and run their first `console.log`. The pseudocode variable of Lesson 17 becomes `let`. Strictly browser-console scope.

**Lesson 21 — Conditions in JavaScript: if, else, comparisons.** Lesson 14's if-then-else now in JavaScript. Comparison operators introduced. Still browser console only.

**Lesson 22 — Loops in JavaScript: for or while.** Lesson 15's repetition in JavaScript. Infinite loops named as a risk and as a debug skill. AT3 brief released here.

**Lesson 23 — Small practical assignment: from pseudocode to JavaScript.** Students translate a piece of their *own* pseudocode (likely from AT2) into JavaScript. AT3 is in progress.

**Lesson 24 — Testing, debugging, presentation.** The course closes by returning to the iterative loop of Lesson 12, now in code. Students read a real error message, fix one bug, and present their AT3 program in 2 minutes. The course ends where Lesson 1 started: *speaking to a computer so it understands you* — and now they can.

---

## Avoimet kysymykset

1. **AT3 deliverable format.** The brief says "small JavaScript solution from pseudocode" and that Alfred packages a Netlify release. For AT3, is the deliverable (a) a `.js` file + screenshot of the console output, (b) a tiny `index.html` with an inline `<script>`, or (c) just a screenshot/recording of the console? Assumption used in this plan: (a) — `.js` file + console screenshot. Orchestrator please confirm.
2. **Peer review logistics in Lesson 12.** Lesson 12 requires peer feedback. Is the teaching context one classroom (in-person pairs feasible) or does the course need an asynchronous fallback (e.g. paired comments in a shared doc)? Plan currently assumes in-person.
3. **Scratch / Blockly status.** Brief lists them as "optional". This plan treats them as *mentionable but never required*. Confirm that no Lesson is allowed to *require* Scratch/Blockly.
4. **AT1 submission timing.** Brief says "end of week 2 / start of week 3". This plan locks it as *end of Lesson 6 / start of Lesson 7*. Confirm.
5. **Course-level README in Alfred's deliverable.** Alfred packages a single lesson but the README points at the full plan. Should the README also list the planned topics for lessons 2–24 (essentially copying the 24-lesson table from this plan), or just link to `01-suunnitelma.md`? Plan currently assumes the latter, but the former may be more useful for a reader landing on the Netlify page.
6. **Language register.** Target students are ~15 years old, vocational, possibly with support needs. Should Rasmus aim for a CEFR B1 reading level explicitly, or use the same register as the Finnish golden sample (which reads roughly B2)? Plan currently assumes B1–B2, leaning B1 in `self-study.md` and B2 in `teacher-materials.md`.
