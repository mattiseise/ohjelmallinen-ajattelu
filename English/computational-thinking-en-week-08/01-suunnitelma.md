# Computational Thinking — Week 8 Plan (Sune, Gate #1)

Course: Computational Thinking (English)
Target: First-year vocational ICT students, ~15–17, no prior programming
Duration: 8 weeks × 3 lessons/week × 90 min = 24 lessons
Pipeline scope this run: Sune produces this Week 8 plan; Rasmus builds the full Week 8 package in the dual-language weekly structure; Linnea/Wilhelm audit Week 8; Alfred packages a Week 8 Markdown release. No PDF, no PPTX rendering.

Week 8 closes the course. AT3 (small JavaScript or C# program built from the student's own Week 6 pseudocode) is submitted and presented this week.

---

## Suunnitelma

### Where Week 8 sits

Week 8 closes the arc that Week 1 opened. Lesson 1 asked *"How do I speak to a computer so that it understands what I want it to do?"* Week 8 answers it concretely: the student writes a small program, runs it, sees a real error message, fixes the bug, and explains the program out loud to another human in two minutes. Programming is no longer a mystery — it is a 15-line file the student can read top to bottom and defend.

Week 7 introduced JavaScript and C# side by side (output, variables, comparisons, if/else). Students chose their language at the end of Week 7 and stuck with it for AT3. Week 8 layers in loops, then assembles all course concepts (sequence, condition, repetition, variables, input/output) into one tiny working program per student.

### Week 8 theme statement

Week 8 is the **synthesis week**: nothing genuinely new conceptually, but the first time everything the course has trained — decomposition, precise instructions, flowcharts, alternatives, logic structures, pseudocode — gets assembled in a real programming language and run on a real machine. Three lessons cover (L22) loops, (L23) one full build day where students translate a piece of their own Week 6 pseudocode into JavaScript or C#, and (L24) testing, fixing one bug, and presenting the result in a 2-minute oral. By the end of the week each student has submitted **AT3**: a small program plus a 2-minute presentation, in their chosen language.

### L22–L24 breakdown for Week 8

#### Lesson 22 — Loops in code: a simple for or while structure

- **Learning objectives** (Understanding + Applying):
  - (a) **Recognize** a loop in code and **name** the parts: condition, body, update. *(Understanding)*
  - (b) **Read** a small for/while loop and **predict** what it prints. *(Understanding)*
  - (c) **Write** a 3–6 line loop that runs a known number of times (count 1 to 5, print "Hello" three times). *(Applying)*
  - (d) **Map** a repeat-until pattern from Week 5/6 pseudocode to a working for/while loop. *(Applying)*
- **Key vocabulary preview:** loop, for, while, counter, condition (revisited), body, iteration, infinite loop.
- **Central message (one sentence):** A loop is the formal name for the *repeat-until* idea the course already taught — only now the computer, not a human, is doing the repeating.

#### Lesson 23 — Small practical assignment: from pseudocode to JavaScript or C#

- **Learning objectives** (Applying):
  - (a) **Select** one of their own Week 6 pseudocode snippets to translate. *(Applying)*
  - (b) **Translate** that pseudocode into a working JavaScript or C# program of ~10–25 lines. *(Applying)*
  - (c) **Run** the program in the browser console (JS) or an online .NET runner (C#) and confirm at least one expected output. *(Applying)*
  - (d) **Save** the source as a `.js` or `.cs` file (or a clearly labelled snippet pasted into the AT3 submission). *(Applying)*
- **Key vocabulary preview:** translation (pseudocode → code), source file, run, expected output, actual output.
- **Central message (one sentence):** Translating pseudocode into a programming language is mostly a matter of replacing English words with the language's syntax — the structure was already there.

#### Lesson 24 — Testing, debugging at a beginner level, presentation, and explaining one's own solution

- **Learning objectives** (Applying + light Evaluating):
  - (a) **Test** the program by running it with at least two different inputs/values. *(Applying)*
  - (b) **Read** a real error message (or unexpected output) and **locate** the line responsible. *(Applying)*
  - (c) **Apply** one small fix and re-run. *(Applying)*
  - (d) **Explain** the program to a peer or the class in **2 minutes**: what it does, how it does it, what went wrong, how it was fixed. *(light Evaluating — own work)*
  - (e) **Compare** one's own solution with a peer's in plain English (different choices, same goal). *(light Evaluating)*
- **Key vocabulary preview:** test, error message, bug, fix, presentation, peer feedback.
- **Central message (one sentence):** Debugging at this level means reading what the computer told you, finding the one line it was talking about, and making one small change — no special tools needed.

### Week 8 — must-do minimum vs. deepening

**Must-do minimum (every student must leave Week 8 able to):**
- Read a small for or while loop in their chosen language and predict its output.
- Translate one piece of their own Week 6 pseudocode into a small, working JavaScript or C# program.
- Run the program, see real output, and submit the source plus a screenshot as AT3.
- Trigger at least one error message on purpose or by accident, read it, and apply one small fix.
- Give a 2-minute oral presentation of the program (what it does, how, the bug, the fix).

**Deepening (optional extension, not required for AT3 pass):**
- Combine a loop with an if/else (e.g. count how many passwords in a list are long enough).
- Compare their JS version to a classmate's C# version of the same program (or vice versa) and write 3–5 sentences on the differences.
- Add input from `prompt()` (JS) or `Console.ReadLine()` (C#) and validate it.
- Extend the program with a second feature, written first as a pseudocode line and then translated.

### Dual-language structure (continues from Week 7)

Both languages are equally supported. The student chose JS or C# at the end of Week 7 and stays with that choice for AT3. Rasmus delivers **both** task files in full, both with the same number and shape of tasks, both with parallel AT3 briefs. No language is the "default" and no language is the "alternative".

```
student/week-08/
├── overview.md
├── self-study.md            # covers both languages side by side
├── student-tasks-js.md      # 1–2 MANDATORY + 2–3 DEEPENING, all in JavaScript
├── student-tasks-csharp.md  # 1–2 MANDATORY + 2–3 DEEPENING, all in C#
├── vocabulary.md            # terms language-neutral where possible
└── slides.md
teacher/week-08/
├── teacher-materials.md
└── in-class-tasks.md
```

The AT3 brief itself is one of the MANDATORY tasks **in each** of `student-tasks-js.md` and `student-tasks-csharp.md`. The two AT3 briefs are parallel: same scope, same deliverables, same word count, same submission format — only the language differs.

### Course closure: connecting Week 8 back to Week 1

Lesson 24 explicitly revisits the central question of the course. In the L24 plan and on a slide near the end of `slides.md`, the question appears verbatim once more — *How do I speak to a computer so that it understands what I want it to do?* — alongside an honest acknowledgement that the student now has a working answer.

---

## Rajaukset

**Out of scope for Week 8:**
- **No automatic testing or debugging frameworks.** No jest, mocha, vitest, pytest, xUnit, NUnit, MSTest, FsCheck. Stated explicitly. "Testing" in L24 means running the program by hand with different values. "Debugging" means reading a console error and applying one small fix.
- **No actual debugger tool.** No `debugger;` statement, no Chrome DevTools breakpoints, no Visual Studio breakpoints, no step-through. The L24 debugging exercise is reading text and changing one line.
- **No new programming-language features beyond loops.** No functions, no arrays in JS (a list-style loop may use one in C# only if the simplest example genuinely needs it; otherwise stick to counter loops), no objects, no classes, no modules, no async, no LINQ.
- **No npm, no Node.js install, no Visual Studio install.** JS runs in the browser console; C# runs in an online .NET runner (dotnetfiddle.net or similar) that needs no signup beyond an optional email.
- **No grading rubric beyond a simple checklist.** AT3 is pass / not-yet-pass on a small set of observable criteria (the program runs; the student can name what it does; at least one bug was fixed).
- **No long written report.** AT3 includes the source, a screenshot, and a 2-minute oral. No essay.
- **No PowerPoint, no PPTX, no Reveal.js, no Google Slides.** Rasmus produces `slides.md` only.
- **Bloom cap: Applying + light Evaluating.** Forbidden verbs in Week 8 objectives: *design, develop, build, create (as a Bloom verb), analyse, architect, optimize, refactor*. "Create" in the everyday sense ("create a file") is fine — it is the Bloom-level *Creating* verb that is forbidden.

**Language:** English throughout. Sune-template H2 headings (`Suunnitelma`, `Rajaukset`, `Hyväksymiskriteerit`, `Briefing Rasmukselle`, `Avoimet kysymykset`) stay Finnish in this plan file; all 7 Rasmus files are fully English.

**Pipeline scope this run:**
- Sune produces this Week 8 plan (you are reading it).
- Rasmus builds **only Week 8** in the dual-language weekly structure (7 mandatory files; optional supplementary `slides-l<n>-*.md` only if a lecture segment genuinely needs it).
- Linnea and Wilhelm audit Week 8 only.
- Alfred packages a Week 8 Markdown release.

---

## Hyväksymiskriteerit

Wilhelm verifies the Week 8 package against the following concrete, checkable criteria.

### Structural — files and folders

1. **All 7 canonical files present**, with exactly these filenames (case-sensitive, lowercase, kebab-case):
   - `student/week-08/overview.md`
   - `student/week-08/self-study.md`
   - `student/week-08/student-tasks-js.md`
   - `student/week-08/student-tasks-csharp.md`
   - `student/week-08/vocabulary.md`
   - `student/week-08/slides.md`
   - `teacher/week-08/teacher-materials.md`
   - `teacher/week-08/in-class-tasks.md`
2. **No `student-tasks.md`** at the top level of `student/week-08/`. The two language-specific files replace it. (An optional 5-line `student-tasks.md` *index* is allowed if Rasmus wants one, but is not required and must not contain task content.)
3. **No `.pptx`, `.key`, Reveal.js HTML, or other slide formats** anywhere. Hard fail if found.
4. **Optional supplementary slide deck** allowed: `student/week-08/slides-l24-presentation-rubric.md` (4–8 slides). Rasmus decides whether to include it.

### Volume (sanity-check brackets, not hard limits)

5. `overview.md`: **200–400 words**.
6. `self-study.md`: **2400–4000 words** (covers L22, L23, L24, both languages side by side).
7. `student-tasks-js.md`: **800–1800 words**. **1–2 MANDATORY + 2–3 DEEPENING** tasks, all in JavaScript.
8. `student-tasks-csharp.md`: **800–1800 words**. **1–2 MANDATORY + 2–3 DEEPENING** tasks, all in C#. **Parallel in count and shape** to `student-tasks-js.md`.
9. `vocabulary.md`: **10–18 terms**, language-neutral wording where possible; where a term needs both syntaxes (e.g. "loop keyword"), give the JS and C# form side by side.
10. `slides.md`: **~12–20 slides** (slightly higher than the 10–20 baseline because the week spans loops + AT3 + presentation).
11. `teacher-materials.md`: **2400–4400 words**. Contains **3 × 90-minute lesson plans** (L22, L23, L24), each summing to 90 with per-lesson **Slide cues**.
12. `in-class-tasks.md`: **400–1200 words**. **At least 1 MANDATORY** teacher-led in-class exercise.

### Required H2 sections per file

13. `overview.md` must contain (in this order):
    - `## Week 8 theme`
    - `## What you will be able to do by the end of the week`
    - `## Must-do minimum vs. deepening`
    - `## How the three lessons fit together`
    - `## Choosing your language (reminder from Week 7)`
14. `self-study.md` must contain:
    - `# <Week title>` (an inviting H1).
    - `## Introduction` — re-states the course's central question verbatim and previews AT3.
    - `## Lesson 22 — Loops in code` (or close variant), with **JS and C# subsections side by side**.
    - `## Lesson 23 — From pseudocode to a small program`.
    - `## Lesson 24 — Test, fix one bug, present`.
    - `## How AT3 is assessed` — checklist version of the AT3 criteria.
    - `## Summary — closing the loop on the central question`.
    - **At least 4 `> **Pause for a moment:**` reflection prompts** across the three lessons (at least 1 per lesson).
15. `student-tasks-js.md` and `student-tasks-csharp.md` must each contain:
    - `## Overview of the week's tasks`
    - One H2 per task, prefixed with `🟢 MANDATORY —` or `🟣 DEEPENING —`.
    - **One MANDATORY task per file is the AT3 brief itself.**
    - Each task ends with a `### Keep your notes` block that mentions **AT3 explicitly** (this week's submission), not AT1.
    - Each task that assumes a partner (peer reader, in-class presentation, classmate-as-tester) includes an `### If you are doing this alone` subsection with a concrete alternative (24h gap, video self, class chat, different device).
    - The phrase **"must-do minimum"** appears at least once in the overview or in the MANDATORY task descriptions.
16. `vocabulary.md` must contain a single H2 `## Week 8 vocabulary`. At least one term flagged as **"course wrap-up — revisited from earlier weeks"** (suggest *algorithm*, *pseudocode*, or *condition*).
17. `slides.md` must:
    - Start with a title slide.
    - Contain at least one slide that shows the course's central question verbatim (course-closure slide near the end).
    - Use `---` on its own line between slides.
    - Show **both JS and C# syntax side by side** on at least the loop-introduction slide and the if/else-with-loop slide (if present).
    - Reference task numbers consistent with both task files (e.g. *Task 8.1 (MANDATORY) — see your language's task file*).
18. `teacher-materials.md` must contain (in this order):
    - `## Week 8 learning objectives (mapped to Bloom)`
    - `## Common misconceptions for Week 8` (≥6 across the week, ≥2 per lesson, each with a *Correction:* line)
    - `## Lesson 22 — 90-minute plan` — with **Slide cues** subsection.
    - `## Lesson 23 — 90-minute plan` — with **Slide cues**.
    - `## Lesson 24 — 90-minute plan` — with **Slide cues**, **must include a 2-minute student presentation segment**.
    - `## Facilitation tips`
    - `## Answers to common student questions` (≥5 across the week)
    - `## Formative assessment tips`
19. `in-class-tasks.md` must contain:
    - `## Overview`
    - At least 1 H2 task labelled **MANDATORY** requiring genuine classroom interaction (pair work, show-and-tell, whole-class debrief). Cross-referenced from `teacher-materials.md`.

### Pedagogical rules

20. **30–50% rule**: in `teacher-materials.md`, for each of the three 90-min lesson plans, the time blocks visibly labelled *independent student work* sum to **27–45 minutes**. Wilhelm checks arithmetically.
21. **Bloom cap**: Week 8 learning objectives use only Applying verbs (*translate, write, run, test, apply, predict, read, locate, fix, compare, explain*) with light Evaluating in L24 (*compare own solution to peer's*, *explain own choice in own words*). Forbidden verbs in Week 8 objectives: *design, develop, build, architect, optimize, refactor, judge, critique, analyse* (as Bloom verbs).
22. **Central question** — *How do I speak to a computer so that it understands what I want it to do?* — appears **verbatim** in `self-study.md` (Introduction and Summary, or at least once total) **and** on at least one slide in `slides.md` (course-closure slide).
23. **Dual-language parity**: every concrete syntax example in `self-study.md` and `slides.md` that exists for JS also exists for C#, and vice versa. Wilhelm spot-checks 5 examples.
24. **L24 debugging framing**: "debugging" in any file refers to **reading a console error message and applying one small fix**. No reference to a debugger, breakpoints, step-through execution, or any automated testing tool.
25. **No testing/debugging frameworks**: the strings `jest`, `mocha`, `vitest`, `pytest`, `xunit`, `nunit`, `mstest`, `chai`, `assert` (as a framework name), `debugger;` (the JS statement), `Debug.WriteLine`, *breakpoint*, *step over*, *step into* do not appear in any of the 7 files. Wilhelm greps.
26. **Course-closure framing**: at least one paragraph in `self-study.md` and one slide in `slides.md` connect Week 8 back to Lesson 1 explicitly (mention "Week 1" or "Lesson 1" or "the central question we started with").

### Tasks (AI resilience and dual-language parity)

27. Each of `student-tasks-js.md` and `student-tasks-csharp.md` contains **1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING** tasks. **The AT3 brief is one of the MANDATORY tasks in each file.** The two AT3 briefs are parallel in scope, deliverables and word count.
28. **The AT3-brief MANDATORY task** is AI-resilient by construction: it requires the student's own Week 6 pseudocode (their own artefact from earlier in the course), a real run-and-screenshot, and a 2-minute oral presentation. An LLM cannot fake any of those without the teacher noticing.
29. If a DEEPENING task uses an LLM as a sparring partner (e.g. "ask the LLM to suggest one extension, then reject or revise"), it includes a fenced sample prompt and an explicit instruction not to paste the LLM's output verbatim.
30. The 2-minute oral presentation requirement is stated **inside the AT3-brief MANDATORY task** in both language files (not only in `teacher-materials.md`).

### In-class tasks

31. `in-class-tasks.md` contains **at least 1 MANDATORY** teacher-led in-class exercise that genuinely requires classroom interaction. The recommended default is **"Show-and-tell loops"** (see Briefing). It is cross-referenced from `teacher-materials.md` with the exact 90-min slot in L22 or L23.

### Language and polish

32. **English throughout**, no Finnish in any of the 7 files except clearly necessary proper nouns.
33. **Register**: `self-study.md`, `student-tasks-js.md`, `student-tasks-csharp.md`, `overview.md`, `vocabulary.md`, `slides.md` at CEFR ~B1; `teacher-materials.md` and `in-class-tasks.md` at CEFR ~B2.
34. **Valid Markdown**: every code fence closes (and is fenced as `js` or `csharp` appropriately), every table renders, no broken internal links, `---` separators in `slides.md` alone on their own line.

### AT3 acceptance criteria (locked, surfaced in `self-study.md` and both task files)

35. The student submits, in their chosen language:
    - the source code (file or clearly fenced snippet, language tag matching the chosen language);
    - a screenshot of the program running with at least one expected output;
    - a 3–5 sentence written reflection naming the **one bug** they found and the **one fix** they applied;
    - a 2-minute oral presentation delivered in class on L24.
36. The teacher's pass / not-yet-pass check is on:
    - the program runs (or there is a documented attempt at a fix that did not succeed, with the error message recorded);
    - the student can name in plain English what the program does;
    - at least one bug-and-fix pair is documented;
    - the 2-minute presentation was delivered.

---

## Briefing Rasmukselle

### Cross-cutting reminders (apply to all 8 files Rasmus may produce — 7 mandatory + optional rubric deck)

- **Closing the loop.** This is the last week. Lean on continuity: in every file, refer back to at least one earlier week's artefact (Week 6 pseudocode, Week 5 conditions, Week 1 central question).
- **Both languages are first-class.** Never write "the JavaScript version" before "the C# version" everywhere; alternate which language is shown first across examples. Both languages get equal real estate on every shared slide and in every shared self-study section.
- **"Debugging" is reading and fixing, not tooling.** Every time the word *debugging* appears in any file, the surrounding text must make clear that this means reading a console error message and changing one line. No debugger references. No breakpoint references.
- **AT3 in L24 includes a 2-minute oral presentation.** State the time limit explicitly (the words "2 minutes" or "two minutes").
- **"Must-do minimum"** is the wording for MANDATORY tasks in overview.md and the two student-tasks files (not "mandatory minimum").
- **"If you are doing this alone"** subsection is required in every task that assumes a partner (peer reader, presentation audience, classmate-as-tester). Alternatives include: leave a 24h gap and read your own program with fresh eyes, record yourself presenting on video, post to the class chat for peer comment, run the program on a different device.
- **No `.pptx` references.** Rasmus delivers `slides.md`; the orchestrator (not in scope this run) would convert. No PDF or PPTX produced this round.
- **No testing/debugging frameworks anywhere.**
- **Central question must appear verbatim** in `self-study.md` and on a slide in `slides.md`: *How do I speak to a computer so that it understands what I want it to do?*

---

### Programs students will actually build — both languages, ready-to-use sketches

Rasmus picks 4–6 of these as exemplar programs in `self-study.md` and as starter examples in the student-tasks files. All are small, all are translatable from Week 6 pseudocode patterns the students have already practised, all run in the browser console (JS) or an online .NET runner (C#).

**Program A — Age-limit check**
- *Pseudocode pattern (Week 6):* read an age, if age ≥ 18 print "allowed", else print "not allowed".
- *JavaScript:*
  ```js
  let age = 17;
  if (age >= 18) {
    console.log("allowed");
  } else {
    console.log("not allowed");
  }
  ```
- *C#:*
  ```csharp
  int age = 17;
  if (age >= 18) {
      Console.WriteLine("allowed");
  } else {
      Console.WriteLine("not allowed");
  }
  ```

**Program B — Password-length check**
- *Pseudocode pattern:* read a password, if length ≥ 8 print "strong enough", else print "too short".
- *JS:*
  ```js
  let password = "hi";
  if (password.length >= 8) {
    console.log("strong enough");
  } else {
    console.log("too short");
  }
  ```
- *C#:*
  ```csharp
  string password = "hi";
  if (password.Length >= 8) {
      Console.WriteLine("strong enough");
  } else {
      Console.WriteLine("too short");
  }
  ```

**Program C — Points-to-feedback**
- *Pseudocode pattern:* given a score, print one of three messages.
- *JS:*
  ```js
  let score = 72;
  if (score >= 80) {
    console.log("great work");
  } else if (score >= 50) {
    console.log("you passed");
  } else {
    console.log("try again");
  }
  ```
- *C#:*
  ```csharp
  int score = 72;
  if (score >= 80) {
      Console.WriteLine("great work");
  } else if (score >= 50) {
      Console.WriteLine("you passed");
  } else {
      Console.WriteLine("try again");
  }
  ```

**Program D — Simple counter (the loop exemplar for L22)**
- *Pseudocode pattern:* repeat 5 times: print the current number.
- *JS:*
  ```js
  for (let i = 1; i <= 5; i++) {
    console.log(i);
  }
  ```
- *C#:*
  ```csharp
  for (int i = 1; i <= 5; i++) {
      Console.WriteLine(i);
  }
  ```

**Program E — Greeting by name (loop variant)**
- *Pseudocode pattern:* repeat 3 times: print "Hello, NAME".
- *JS:*
  ```js
  let name = "Aino";
  for (let i = 0; i < 3; i++) {
    console.log("Hello, " + name);
  }
  ```
- *C#:*
  ```csharp
  string name = "Aino";
  for (int i = 0; i < 3; i++) {
      Console.WriteLine("Hello, " + name);
  }
  ```

**Program F — Correct-answer checker (loop + if)**
- *Pseudocode pattern:* ask up to 3 times; if the answer matches, stop; otherwise say "try again".
- *JS (counter loop version — keep it simple, no prompt():*
  ```js
  let answers = ["red", "green", "blue"];
  let correct = "blue";
  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === correct) {
      console.log("got it on try " + (i + 1));
      break;
    } else {
      console.log("try again");
    }
  }
  ```
- *C#:*
  ```csharp
  string[] answers = { "red", "green", "blue" };
  string correct = "blue";
  for (int i = 0; i < answers.Length; i++) {
      if (answers[i] == correct) {
          Console.WriteLine("got it on try " + (i + 1));
          break;
      } else {
          Console.WriteLine("try again");
      }
  }
  ```
  *(Program F is on the upper edge of complexity — Rasmus uses it as a DEEPENING example, not as the mandatory exemplar.)*

Rasmus uses Programs A–E in `self-study.md` and on slides; Programs A–D as starter examples in the MANDATORY tasks; Programs E and F as DEEPENING task seeds. The AT3-brief MANDATORY task is **not** prescriptive about which program — it tells the student to translate **their own** Week 6 pseudocode and offers A–F as fallback templates if their pseudocode is missing or too large.

---

### File 1 — `student/week-08/overview.md` (200–400 words)

**Required H2 structure (in order):**
1. `## Week 8 theme` — one short paragraph: this is the closing week; AT3 lands here; the course's central question gets a real answer.
2. `## What you will be able to do by the end of the week` — bullet list of 5–7 plain-English "can do" statements, mapped to the L22–L24 objectives but stated in student-facing language. At least one bullet references the 2-minute presentation.
3. `## Must-do minimum vs. deepening` — two-bullet-list contrast. Use the exact phrase **"must-do minimum"**.
4. `## How the three lessons fit together` — one short paragraph: L22 loops → L23 build → L24 test, fix, present.
5. `## Choosing your language (reminder from Week 7)` — one short paragraph: you picked JS or C# in Week 7; you stay with it for AT3. Both task files exist; you use the one matching your language.

---

### File 2 — `student/week-08/self-study.md` (2400–4000 words)

**Required structure (in order):**
- `# <Week title>` — suggestion: *"Closing the loop — your first real program"*. Rasmus may improve.
- `## Introduction` — recall the central question **verbatim**. Tell the student that AT3 (their first real program) lands this week, that they pick the program from their own Week 6 pseudocode, and that they will present it for 2 minutes on L24.
- `## Lesson 22 — Loops in code`
  - `### Why loops exist` — connect to the *repeat-until* pattern from Week 5 and the pseudocode loops from Week 6.
  - `### The shape of a for loop` — JS and C# **side by side** in a two-column code block or paired fenced blocks. Use Program D (simple counter).
  - `### The shape of a while loop` — JS and C# side by side. Short example: print "Hello" while a counter is below 3.
  - `### Counter, condition, body, update` — name the four parts of a for loop in both languages.
  - `### When a loop runs forever` — gentle intro to *infinite loop*, how to spot one (browser console hangs, .NET runner times out), what to change to stop it.
  - 1 `> **Pause for a moment:**` reflection prompt.
- `## Lesson 23 — From pseudocode to a small program`
  - `### Pick one piece of your Week 6 pseudocode` — concrete instructions: 6–20 lines is the sweet spot; bigger means split off only one part.
  - `### The translation table` — a 6–10 row table mapping common Week 6 pseudocode patterns to JS and C# syntax: *print X*, *if X then Y else Z*, *repeat N times*, *let X be Y*, *read X*, *increase X by 1*, *check if X equals Y*, etc.
  - `### Save, run, see output` — JS in the browser console; C# in an online .NET runner. Name **one** online .NET runner (dotnetfiddle.net is the default suggestion — if Rasmus prefers a different free one with no required signup, that's fine).
  - `### When the screen is empty / silent` — what to check first: did you actually run the file? Is there a typo in the print/Console.WriteLine call?
  - 1–2 `> **Pause for a moment:**` reflection prompts.
- `## Lesson 24 — Test, fix one bug, present`
  - `### Testing by hand` — running the program twice with two different values. Show both languages.
  - `### Reading a real error message` — show one JS error (e.g. `Uncaught ReferenceError: scre is not defined`) and one C# error (e.g. `CS0103: The name 'scre' does not exist in the current context`). For each, show the misspelled line and the fix.
  - `### One small fix, one re-run` — that's all "debugging" means here. Explicit: no debugger tool, no breakpoints, no testing framework. Read the message, find the line, fix the typo, run again.
  - `### Your 2-minute presentation` — a 4-bullet outline of what to say: what the program does, how it works (loop + if?), what went wrong, how it was fixed. Mention the time limit explicitly: **2 minutes**.
  - 1 `> **Pause for a moment:**` reflection prompt.
- `## How AT3 is assessed` — checklist version of criteria 35–36. Pass / not-yet-pass.
- `## Summary — closing the loop on the central question` — re-state the central question **verbatim**. One paragraph connecting back to Week 1.

---

### File 3 — `student/week-08/student-tasks-js.md` (800–1800 words)

**Required structure:**
- `## Overview of the week's tasks` — 2–4 sentences. State that 🟢 MANDATORY tasks are the **must-do minimum** and that 🟣 DEEPENING tasks are optional extension. Mention that AT3 is submitted this week.

**Four candidate tasks for Rasmus to pick from (he keeps 1–2 MANDATORY + 2–3 DEEPENING):**

**Task 8.1-JS — 🟢 MANDATORY — "AT3 brief: translate your Week 6 pseudocode into JavaScript"**
- Student selects one piece of their Week 6 pseudocode (6–20 lines). If they cannot find one or it is too large, they may use Program A, B, C, D, or E as a fallback template — but they must adapt the values to their own context.
- Student writes the JavaScript program in the browser console (or a `.js` file pasted into the submission).
- Student runs the program with at least **two different input values** (or two different starting variable values) and captures the output (screenshot of the console).
- Student deliberately or accidentally introduces one error, reads the error message, fixes it, re-runs.
- Student writes a 3–5 sentence reflection naming the bug and the fix.
- Student prepares a **2-minute oral presentation** for L24: what the program does, how it works (loop? if/else?), what went wrong, how it was fixed.
- `### If you are doing this alone` — if there is no audience on L24, record a 2-minute video of yourself presenting the program to the camera, or post the program + a 3-sentence summary in the class chat.
- `### Keep your notes` — this **is** AT3. Save the source file, the screenshot, and the reflection. Bring them to L24.

**Task 8.2-JS — 🟢 MANDATORY (alternative or in addition) — "Loop warm-up: count 1 to 5 in JS"**
- Student writes a 4–6 line `for` loop that prints 1 to 5 to the console. Then modifies it to print 5 to 1 (reverse). Then modifies it again to print "Hello, NAME" three times.
- Submission: 3 short snippets in a single file.
- `### Keep your notes` — these patterns will appear in your AT3 program.

**Task 8.3-JS — 🟣 DEEPENING — "Combine loop + if/else in JS"**
- Student writes a small JS program that loops through 5 password attempts (an array of 5 strings the student picks) and for each prints either "long enough" or "too short".
- Reflection: 3 sentences on what the program does and one thing they would add next.
- `### Keep your notes` — useful as an extension to the AT3 program if there's time.

**Task 8.4-JS — 🟣 DEEPENING — "Read a real error message and fix it (JS)"**
- Student is given 3 short JS snippets, each containing exactly one mistake (typo in variable name, wrong comparison operator `=` instead of `===`, missing closing brace). For each: paste into the console, read the error, name the line and the fix in plain English, then apply it.
- LLM sparring step (optional): paste the error message and the snippet into an LLM with a supplied prompt asking the LLM to explain the message **without giving the fix**, then reject the LLM's explanation if it gives the fix anyway. Sample prompt in a fenced block.

**Task 8.5-JS — 🟣 DEEPENING — "Compare with a C# classmate"**
- Find a classmate who used C# for AT3. Read each other's program. Write 3–5 sentences in plain English on the differences (semicolons, `Console.WriteLine` vs `console.log`, `int` vs `let`, etc.) and one thing that is the same (the loop structure, the if/else, the goal).
- `### If you are doing this alone` — read the C# version of one of Programs A–E from `self-study.md` and write the same 3–5 sentences.

**Default selection Rasmus should ship in `student-tasks-js.md`:**
- 🟢 MANDATORY: Task 8.1-JS (*AT3 brief*) — **required**. Optionally also Task 8.2-JS (*Loop warm-up*) as a second MANDATORY.
- 🟣 DEEPENING: Tasks 8.3-JS, 8.4-JS, and 8.5-JS.

---

### File 4 — `student/week-08/student-tasks-csharp.md` (800–1800 words)

**Required structure:** mirrors `student-tasks-js.md` exactly. Same task count, same task shape, parallel AT3 brief.

**Four candidate tasks for Rasmus to pick from:**

**Task 8.1-CS — 🟢 MANDATORY — "AT3 brief: translate your Week 6 pseudocode into C#"**
- Same scope and deliverables as Task 8.1-JS. The student writes the C# program in an online .NET runner (dotnetfiddle.net or similar), screenshots the run, fixes one bug, prepares a 2-minute oral presentation.
- `### If you are doing this alone` — same alternatives as 8.1-JS (recorded video, class chat post).
- `### Keep your notes` — this **is** AT3.

**Task 8.2-CS — 🟢 MANDATORY (alternative or in addition) — "Loop warm-up: count 1 to 5 in C#"**
- Same shape as 8.2-JS but in C#. Three short snippets in one file.

**Task 8.3-CS — 🟣 DEEPENING — "Combine loop + if/else in C#"**
- Same shape as 8.3-JS. C# array of 5 strings, loop, print "long enough" / "too short".

**Task 8.4-CS — 🟣 DEEPENING — "Read a real error message and fix it (C#)"**
- Same shape as 8.4-JS. Three short C# snippets, each containing exactly one mistake (typo in variable name, `=` instead of `==`, missing closing brace). Read the error, name the fix, apply it. Optional LLM sparring step with the same sample prompt.

**Task 8.5-CS — 🟣 DEEPENING — "Compare with a JS classmate"**
- Mirror of Task 8.5-JS. Find a JS classmate, read each other's programs, write 3–5 sentences on differences and one thing that is the same.
- `### If you are doing this alone` — read the JS version of one of Programs A–E in `self-study.md`.

**Default selection Rasmus should ship in `student-tasks-csharp.md`:**
- 🟢 MANDATORY: Task 8.1-CS (*AT3 brief*) — **required**. Optionally also Task 8.2-CS (*Loop warm-up*) as a second MANDATORY.
- 🟣 DEEPENING: Tasks 8.3-CS, 8.4-CS, and 8.5-CS.

**Parity check:** Rasmus must ensure that the number of MANDATORY tasks in the JS file matches the C# file, and the number of DEEPENING tasks matches. If 8.1-JS and 8.2-JS are both MANDATORY, then 8.1-CS and 8.2-CS are both MANDATORY.

---

### File 5 — `student/week-08/vocabulary.md` (10–18 terms)

**Required terms (Rasmus may add 1–4 of their own):**
1. Loop
2. for (loop keyword in both JS and C#)
3. while (loop keyword in both)
4. Counter
5. Iteration
6. Body (of a loop)
7. Infinite loop
8. Error message
9. Bug
10. Fix
11. Test (revisited from Week 1)
12. Source code
13. Run (a program)
14. Presentation
15. **Algorithm** — flagged as **"course wrap-up — revisited from Week 1"**.

Optional additions: *console* (revisited from Week 7), *console.log / Console.WriteLine* (revisited), *condition* (revisited from Week 5).

Each definition is 1–3 sentences, plain English, with a short example. Where a term has different forms in JS and C#, show both (e.g. *"length of a string: `password.length` in JS, `password.Length` in C#"*).

---

### File 6 — `student/week-08/slides.md` (~12–20 slides)

**Recommended slide outline (Rasmus may adjust within the spirit of the structure):**

1. `# Week 8 — Closing the loop`
2. `## What lands this week` — bullet list: loops, AT3 build, AT3 presentation.
3. `## Loops — the shape (JS and C# side by side)` — Program D in both languages on one slide.
4. `## Counter, condition, body, update` — name the four parts.
5. `## A while loop (JS and C# side by side)` — short example.
6. `## When a loop runs forever` — what an infinite loop looks like and how to stop it.
7. `## From your pseudocode to your program` — single sentence + a 3-row translation table snippet.
8. `## The translation table` — 4–6 rows: *print*, *if/else*, *repeat N times*, *let X be Y*.
9. `## Save, run, see output` — one slide per language tool (browser console / online .NET runner).
10. `## Reading a real error message (JS)` — one error and one fix.
11. `## Reading a real error message (C#)` — one error and one fix.
12. `## One small fix, one re-run` — that is debugging, at this level. (Explicit: no debugger tool, no breakpoints.)
13. `## Your 2-minute presentation` — bullet outline of what to say.
14. `## Must-do minimum vs. deepening` — two-column contrast.
15. `## Tasks this week (see your language's task file)` — 1 line per task with reference to both files.
16. `## How AT3 is assessed` — checklist.
17. `## Closing the loop — the central question, one more time` — central question **verbatim**.
18. `## Thank you and what comes next`

Aim 14–18 slides. Use `---` on its own line between every slide.

---

### File 7 — `teacher/week-08/teacher-materials.md` (2400–4400 words)

**Required H2 sections (in order):**

1. `## Week 8 learning objectives (mapped to Bloom)` — restate the L22–L24 objectives, grouped by Bloom stage. Applying dominant; light Evaluating in L24 (compare own to peer's, explain in own words, fix one bug).

2. `## Common misconceptions for Week 8` — at least 6 across the week (≥2 per lesson). Suggested set:
   - **L22**: *"A loop is a complicated thing only programmers understand."* → Correction: it is the formal name for the "repeat 3 times" pattern from Week 6 pseudocode. // *"You need `while`; `for` is more advanced."* → Correction: a `for` loop with a counter is usually simpler than a `while` loop for beginners.
   - **L23**: *"Pseudocode and code are completely different."* → Correction: most of the work is replacing English words with the language's syntax — the structure is already there. // *"If my program does not print anything, something is broken."* → Correction: more often, you simply did not run it, or there is a typo in the print line.
   - **L24**: *"Debugging needs a special tool."* → Correction: at this level, debugging is reading the console error and changing one line. // *"If the program runs, it is correct."* → Correction: running and being correct are not the same — test with at least two different values.

3. `## Lesson 22 — 90-minute plan` — with **Slide cues** subsection at the end. Time slots sum to 90, independent-work block 27–45 min. Suggested skeleton:
   - 0–10 min: warm-up — show two pseudocode "repeat 3 times" lines from Week 6 and ask students to predict what a loop will look like.
   - 10–25 min: instructor input — Program D in both languages, name the four parts.
   - 25–55 min: **INDEPENDENT WORK** (30 min) — students complete Task 8.2 in their chosen language (count 1 to 5; reverse; greet by name).
   - 55–75 min: **MANDATORY in-class activity** — "Show-and-tell loops" (see in-class-tasks.md): each pair runs their loop live for the class.
   - 75–85 min: whole-class debrief — what was easy, what looked weird.
   - 85–90 min: closing reflection + preview of L23.
   - **Slide cues:** slides 1–6.

4. `## Lesson 23 — 90-minute plan` — with **Slide cues**. Suggested:
   - 0–10 min: warm-up — each student names the Week 6 pseudocode they will translate.
   - 10–25 min: instructor input — the translation table; show one full translation (Program A or B).
   - 25–65 min: **INDEPENDENT WORK** (40 min) — students translate their pseudocode in their chosen language. Teacher circulates.
   - 65–80 min: pair check — show your partner your program and the output.
   - 80–88 min: whole-class debrief — typical pain points.
   - 88–90 min: preview of L24 (presentation tomorrow).
   - **Slide cues:** slides 7–9.

5. `## Lesson 24 — 90-minute plan` — with **Slide cues**. **Must include a 2-minute student presentation segment.** Suggested:
   - 0–10 min: warm-up — show one JS error and one C# error on the board; class disambiguates.
   - 10–25 min: instructor input — reading an error message, applying one small fix, the 2-minute presentation outline.
   - 25–55 min: **INDEPENDENT WORK** (30 min) — students test their program with two different values, deliberately or accidentally trigger one error, fix it, prepare the 2-minute presentation. Teacher circulates and signs off readiness.
   - 55–85 min: **AT3 presentations** — each student gives a **2-minute** presentation. With a class of 12, 30 min covers everyone; with a larger class, split into two simultaneous groups of ~6 with a co-teacher or rotate over two sessions. (Rasmus notes the larger-class adaptation.)
   - 85–90 min: course closure — re-read the central question; thank the class.
   - **Slide cues:** slides 10–18.

6. `## Facilitation tips` — practical tips: how to keep the 2-minute presentations on time (use a phone timer visible to all), how to handle a student whose program never ran (focus the presentation on the bug they could not fix and what they tried), how to handle the dual-language room (group JS and C# students at adjacent tables for easier pair-check), how to deal with the online .NET runner being slow (have a fallback link, allow late submission of the screenshot only).

7. `## Answers to common student questions` — at least 5. Suggested: *Can I use `console.log` inside my C# program by mistake? / Why does my C# program say "CS0103"? / What if my Week 6 pseudocode is too big? / Do I have to do the presentation if I am shy? / Can I use ChatGPT to write the program?*

8. `## Formative assessment tips` — 3–5 quick checks (exit ticket: name the four parts of a `for` loop; pair report-back: what was the one bug?; one-minute paper after L24: did the course answer its central question for you?).

Cross-reference `in-class-tasks.md` from L22 (show-and-tell loops) and optionally L23 (pair check).

---

### File 8 — `teacher/week-08/in-class-tasks.md` (400–1200 words)

**Required structure:**
- `## Overview` — 2–3 sentences naming the activities and where they fit in the week.
- At least 1 H2 task labelled **MANDATORY**.

**Two concrete activity ideas Rasmus should ship (default: both):**

**Activity A — MANDATORY — "Show-and-tell loops"** *(pair / whole-class, ~20 min, slotted in L22 between 55–75 min)*
- Each pair (or solo student) has just finished writing their loop snippets (Task 8.2 in their language).
- One by one, each pair walks to the front (or projects from their seat), runs their loop **live** in front of the class, and reads the output out loud.
- The class names the four parts of the loop (counter, condition, body, update) for at least one of the loops shown.
- Mixed JS and C# loops together — the point is that the *shape* is the same in both languages.
- **Why it requires the classroom:** the live run + the public naming is the whole point. Cannot be done as homework.
- Cross-reference: `teacher-materials.md` L22 slot 55–75 min.

**Activity B — MANDATORY — "AT3 presentations"** *(whole-class, ~30 min, slotted in L24 between 55–85 min)*
- Each student gives a **2-minute** presentation of their AT3 program (covered in detail in `teacher-materials.md` L24). This is the official AT3 oral component.
- Teacher uses a visible phone timer.
- Brief peer feedback question after each: *"Name one thing you noticed."*
- Cross-reference: `teacher-materials.md` L24 slot 55–85 min.

Optional Activity C — OPTIONAL — "Translation race" *(pair, ~15 min, can be slotted in L23 between 65–80 min)* — one pair translates the same Week 6 pseudocode into JS, the other into C#. After 10 min, compare line by line. Useful for classes that finish early.

---

### Optional supplementary deck — `student/week-08/slides-l24-presentation-rubric.md` (4–8 slides)

Rasmus may include this short deck for teachers to project on L24 between presentations as a reminder of the 2-minute structure.

Suggested outline:
1. `# 2-minute presentation rubric` (title slide)
2. `## What to say (4 beats)` — what the program does / how it works / what went wrong / how it was fixed.
3. `## Timing — 2 minutes` — roughly 30 seconds per beat.
4. `## Pass criteria` — checklist for teacher: program runs (or attempt documented) / student names what it does / one bug-and-fix described / 2 minutes delivered.
5. `## What is *not* required` — perfect code, fancy slides, memorised script.
6. `## After each presentation` — one short peer note: "name one thing you noticed".

This deck is **optional**. If Rasmus includes it, Wilhelm checks for the 4–8 slide count and the presence of the timing reminder.

---

## Avoimet kysymykset

1. **Online C# runner choice.** This plan suggests **dotnetfiddle.net** as the default with no required signup. If the school has a preferred environment (e.g. a self-hosted runner), Rasmus may substitute it. **Default assumption:** dotnetfiddle.net, names it in `self-study.md` L23 section.

2. **Whether to keep both MANDATORY tasks or just the AT3 brief.** The hard rule says 1–2 MANDATORY per language file, and the AT3 brief is one of them. Rasmus may also include the Loop warm-up (Task 8.2) as a second MANDATORY for students who arrive without finished Week 6 pseudocode. **Default assumption:** Rasmus ships **both** as MANDATORY (8.1 + 8.2 in each language file), giving students a shorter warm-up before the bigger AT3 task. Wilhelm accepts 1 or 2 MANDATORY tasks per file, as long as the AT3 brief is one of them.

3. **AT3 oral presentation length.** The brief locks **2 minutes**. **Default assumption:** Rasmus writes "2 minutes" exactly (not "1–3 minutes" or "around 2 minutes"). Wilhelm greps for the string.

4. **Class size and the L24 presentation slot.** A class of 12 fits in 30 min; a larger class needs adaptation. **Default assumption:** Rasmus writes the 90-min L24 plan for a class of ~12, plus one sentence in *Facilitation tips* on how to scale (split into two simultaneous groups; or extend into a second session).

5. **Whether the AT3 brief lives in both task files or also in `self-study.md`.** The hard rule places it in both `student-tasks-js.md` and `student-tasks-csharp.md` as a MANDATORY task. `self-study.md` also contains `## How AT3 is assessed`. **Default assumption:** the actionable brief is in the two task files; `self-study.md` only summarises the assessment criteria.

6. **Whether to mention infinite loops at all.** They are a common bug source. **Default assumption:** Rasmus mentions infinite loops in L22 self-study (one short subsection, no scary jargon) and on one slide. Not in tasks.

7. **C# array syntax in DEEPENING task 8.3-CS / Program F.** Arrays are technically a new feature beyond what Week 7 introduced. **Default assumption:** Rasmus uses arrays in DEEPENING tasks only, never in MANDATORY tasks, and explains the array literal in one line right where it first appears.

8. **Slide count.** This plan recommends 14–18 slides; the canonical brief says ~10–20. **Default assumption:** Rasmus targets 14–18; Wilhelm accepts anywhere in 12–20.

9. **Supplementary deck `slides-l24-presentation-rubric.md`.** **Default assumption:** Rasmus **includes** it (4–6 slides) — Week 8 is the only week with a graded oral, so the rubric deck is genuinely useful.

10. **Vocational angle.** The brief lists six example programs (A–F). **Default assumption:** Rasmus uses Programs A–E in `self-study.md` and as starter examples; Program F appears only in DEEPENING tasks because it combines loop + if + array indexing.

11. **Whether to allow `prompt()` / `Console.ReadLine()` in MANDATORY tasks.** These add complexity (user input) but make programs feel real. **Default assumption:** allowed in DEEPENING tasks only; MANDATORY tasks use hard-coded variable values to keep the bar low. Rasmus notes this explicitly in the AT3 brief.

12. **Whether `slides.md` shows both languages on every code slide.** **Default assumption:** every slide that shows code shows JS and C# **side by side** (paired fenced blocks or a two-column table). This is the parity rule from criterion #23.
