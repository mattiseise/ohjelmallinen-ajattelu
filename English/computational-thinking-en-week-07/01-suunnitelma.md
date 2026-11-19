# Computational Thinking — Week 7 Plan (Sune, Gate #1)

Course: Computational Thinking (English)
Target: First-year vocational ICT students, ~15–17, with six weeks of computational-thinking foundations already in place (Weeks 1–6).
Week 7 in the 8-week arc: **the bridge into code.** Six weeks of pseudocode, sequence, condition, repetition, dry-running and decomposition now meet real syntax — in two languages, JavaScript and C#, side by side.
Pipeline scope this run: Sune produces this Week 7 plan; Rasmus builds Week 7 in the canonical week-XX structure (with the dual-language task-file split); Linnea and Wilhelm audit Week 7; Alfred packages a **Markdown-only** Week 7 release (no PDF, no PPTX).

---

## Suunnitelma

### Where Week 7 sits in the course arc

The course's central question — *"How do I speak to a computer so that it understands what I want it to do?"* — has been answered conceptually since Week 1. Students already know that a computer follows instructions literally, that ambiguity is a property of the instruction, that an algorithm is the everyday name for a clear sequence of literal steps, that flowcharts, abstraction, alternative solutions, logic structures (sequence, condition, repetition) and pseudocode with dry-running all exist as tools.

Week 7 finally puts that conceptual machinery in front of a real interpreter. The week answers: *"If a computer literally cannot guess, what does an instruction look like that it can actually run?"* The answer is **syntax** — a small, strict, exact way of writing instructions. The week introduces two concrete languages, JavaScript and C#, in parallel, so students see that *the thinking is portable* but *the syntax is the bargain you strike with one specific interpreter*. Lesson 19 stays language-agnostic (what a programming language is, why two languages exist, what syntax even means). Lessons 20 and 21 introduce concrete syntax in both languages side by side: first output and variables (L20), then conditions (L21).

Programming is treated as the last layer; computational thinking remains the layer the course trains. AT3, released next week, will ask students to translate a piece of their own Week-6 pseudocode into a tiny program in the language they pick this week. Week 7 is the bridge.

### Week 7 theme statement

A programming language is a way to make instructions precise enough for a computer to follow without guessing. The thinking is what we have been doing all course; the language is just the syntax it gets written in. JavaScript and C# are two such languages — different surface, same underlying thinking. By the end of Week 7 a student can run a first command in **a language they chose** (either JavaScript in the browser console, or C# in an online .NET environment), declare a variable, do a simple comparison and write a first `if/else`. No IDE setup, no debugger, no testing framework.

### L19–L21 breakdown for Week 7

#### Lesson 19 — Why are programming languages needed? Syntax, commands, and the role of programming languages

- **Learning objectives** (Understanding-only at this stage):
  - (a) **Define** *programming language*, *syntax*, *command*, *interpreter* / *compiler* in own words (a one-sentence informal definition is enough; the *compiler/interpreter* distinction is named, not deeply explored).
  - (b) **Explain** why a programming language is needed when pseudocode is already precise — i.e. that a *real* computer cannot read English-language pseudocode.
  - (c) **Recognize** that the same algorithm can be written in different languages and still mean the same thing.
  - (d) **Name** two real-world programming languages (JavaScript, C#) and one place each is typically used (JS = the web browser; C# = .NET / desktop / games / Unity).
- **Language status:** **language-agnostic.** No working code is required of the student. Side-by-side examples may be *shown* on slides, but the lesson talks about syntax as a concept, not about JS- or C#-specific rules.
- **Key vocabulary preview:** programming language, syntax, command, interpreter (informal), compiler (informal), error message (preview), variable (preview).
- **Central message (one sentence):** Pseudocode is precise enough for a human to follow; a programming language is precise enough for a *literal* computer to follow.

#### Lesson 20 — First commands: output, values, variables, simple calculations (in JS and in C#)

- **Learning objectives** (Understanding + Applying):
  - (a) **Run** a first program that prints text to the console — `console.log("...")` in JavaScript, `Console.WriteLine("...")` in C#.
  - (b) **Declare** a variable and **assign** it a value — `let name = "..."` / `let age = 16` in JavaScript, `string name = "..."` / `int age = 16` in C# (we name the *type* in C# but do not labour over the type system).
  - (c) **Print** the value of a variable, including by concatenation (JS: `+` or template literals; C#: `+` or string interpolation `$"..."` — Rasmus picks **one** style per language and sticks to it).
  - (d) **Perform** a simple arithmetic calculation (e.g. years until adulthood, total price) and print the result.
  - (e) **Identify** that the *thinking* (sequence: read, compute, print) is the same in both languages.
- **Language status:** **dual-language.** Every concept presented twice, side by side.
- **Key vocabulary added:** console, output, variable, value, assignment, string, number/int, concatenation, template literal / string interpolation (informal).
- **Central message (one sentence):** A program is a sequence of literal commands — and "print a value to the console" is the simplest such command in either language.

#### Lesson 21 — Conditions in code: if, else, comparisons (in JS and in C#)

- **Learning objectives** (Understanding + Applying):
  - (a) **Write** a comparison expression (`age >= 18`, `password.length >= 8`) in both languages and recognise that the comparison operators are essentially identical in JS and C#.
  - (b) **Write** a first `if/else` block that prints one of two messages depending on a variable.
  - (c) **Map** a piece of Week-6 pseudocode (`IF age >= 18 THEN ... ELSE ...`) onto code in their chosen language.
  - (d) **Predict** the output of a small `if/else` program **before running it**, then run it and check (linking back to Week 6 dry-running).
- **Language status:** **dual-language.** Conditions presented in both languages with side-by-side snippets.
- **Key vocabulary added:** condition, comparison operator (`==`, `>=`, `<=`, `>`, `<`, `!=`), boolean (informal), block `{ ... }`, `if`, `else`.
- **Central message (one sentence):** `if/else` is the same decision you have been writing in pseudocode for two weeks — only the punctuation is different.

### Week 7 — must-do minimum vs. deepening

**Must-do minimum (every student must leave Week 7 able to):**
- Explain in plain English why a programming language is needed at all (not just pseudocode).
- Name JavaScript and C# as two real programming languages and one typical use of each.
- Open the **browser console** (JS path) **OR** an online C# environment such as .NET Fiddle, sharplab.io or a C#-enabled Replit (C# path) — student picks one.
- In their chosen language, run a program that:
  - prints a greeting,
  - declares a variable and prints its value,
  - uses an `if/else` to print one of two messages depending on the value of a variable.
- Save the code (paste into their week notes) — they will reuse it for AT3 next week.

**Deepening (optional, not required for AT3):**
- Do the **same** task in the *other* language (the one they did not pick) — feel the difference in syntax with the thinking already done.
- Translate one piece of their own Week-6 pseudocode into a tiny program in their chosen language (dry-runs to runtime — this is also the seed of AT3).
- Combine two comparisons with `&&` / `||` (named informally; deeper logic operators arrive in Week 5 already, so this is just the code form of what they know).
- Read a real error message: deliberately break the program (forget a semicolon in C#, forget a quote in JS) and write down what the interpreter / compiler said.

### Why dual-language?

Three reasons, in order of importance:

1. **Vocational realism.** First-year ICT students in Finland are split between web-leaning (JS/TS) and .NET-leaning (C#) paths in their second year. Anchoring computational thinking in *both* languages from the first contact frees Week 7 from prejudicing one path.
2. **The transferability message.** Showing the *same algorithm* in two languages is the strongest possible argument that *the thinking is the thing*, and the syntax is the bargain. A single-language Week 7 quietly suggests programming = JS (or = C#).
3. **AT3 fairness.** AT3 in Week 8 asks the student to translate their own pseudocode into a small program. The student should pick the language they prefer — not the one we taught them.

### Slides strategy (Sune's call)

`slides.md` is **one deck**. The deck mixes three slide types:

- **Agnostic slides** (for L19 and for cross-cutting summary slides in L20/L21) — no JS or C# specifics.
- **Side-by-side syntax slides** (the main format for L20 and L21) — one slide, two columns or two code blocks: JS on the left/top, C# on the right/bottom, with the **same thinking** labelled above them.
- **Single-language demo slides** (sparingly) — when one language needs a small mechanic shown (e.g. opening the browser console, opening .NET Fiddle). One such slide per language per such mechanic, clearly labelled.

Rasmus may add **at most two supplementary decks** (`slides-l<n>-<topic>.md`, 4–8 slides each) if a lecture segment genuinely needs deeper material. The two strong candidates are below in the briefing.

### How the three lessons fit together

L19 (concept of syntax, agnostic) → L20 (first concrete syntax, both languages, output + variables) → L21 (first concrete syntax for the most important control structure, both languages, `if/else`). L21 closes by mapping a Week-6 pseudocode snippet onto real code in both languages — this is the explicit hand-off to AT3 in Week 8.

---

## Rajaukset

**Out of scope for Week 7:**

- **No IDE setup.** No VS Code install, no Visual Studio install, no Node.js install, no .NET SDK install, no `dotnet new`. Execution targets are:
  - **JavaScript:** the browser DevTools console (Chrome, Firefox, Edge, Safari — any).
  - **C#:** an online C# environment — **.NET Fiddle** (default recommendation), **sharplab.io**, or a C#-enabled Replit. No account creation required for .NET Fiddle and sharplab.io.
- **No debugger.** No breakpoints, no step-through. "Print to the console and read the output" is the only debugging tool this week.
- **No testing frameworks.** No jest, mocha, vitest, pytest, xUnit, NUnit, MSTest. None mentioned anywhere in any file. Hard fail.
- **No types deep-dive in C#.** The word *type* is named (`int`, `string`) and used; the type system is not explained. We will not discuss `var` vs `int`, value vs reference types, nullable reference types, generics, or anything similar. C# is presented as "C# happens to want you to name the type — that's a small extra word, not a different way of thinking."
- **No semicolon-discipline drilling.** The semicolon difference between JS (optional in most cases, used by convention) and C# (mandatory) is *mentioned once* and not drilled.
- **No async, no classes, no methods (beyond `Console.WriteLine`), no LINQ, no DOM, no fetch, no Node modules, no NuGet packages.** Top-level code only.
- **No browser frameworks** (React, Vue, Svelte). JavaScript means the DevTools console.
- **No third-party C# tooling** beyond a hosted online sandbox.
- **No PDF, no PPTX rendering** in this pipeline run. Markdown release only.
- **No PowerPoint references** in any file. Rasmus writes `slides.md` (and optional `slides-l<n>-*.md`) only.
- **No Bloom levels above Applying.** No Analyzing, Evaluating or Creating in Week 7 objectives. AT3 (Creating-flavoured) lands next week.
- **No `(AI-resilient)` label** anywhere in learner-facing files. AI-resilience is a property Linnea audits; not a label students see.

**Pipeline scope this run:**

- Sune produces this Week 7 plan (you are reading it).
- Rasmus builds **only Week 7**, in the canonical week-XX structure but with the **dual-language task-file split** (`student-tasks-js.md` + `student-tasks-csharp.md` instead of a single `student-tasks.md`; an optional thin index `student-tasks.md` is allowed but not required).
- Linnea and Wilhelm audit Week 7 only.
- Alfred packages a Week 7 release in Markdown.

---

## Hyväksymiskriteerit

Wilhelm verifies the Week 7 package against the following concrete, checkable criteria.

### Structural — files and folders

1. **All canonical files present**, with exactly these filenames (case-sensitive, lowercase, kebab-case):
   - `student/week-07/overview.md`
   - `student/week-07/self-study.md`
   - `student/week-07/student-tasks-js.md`
   - `student/week-07/student-tasks-csharp.md`
   - `student/week-07/vocabulary.md`
   - `student/week-07/slides.md`
   - `teacher/week-07/teacher-materials.md`
   - `teacher/week-07/in-class-tasks.md`
2. **Optional eighth student file**: a thin `student/week-07/student-tasks.md` acting as an index pointing at the two language files. Allowed but not required. If present, it must be **≤200 words** and must not introduce any task numbering of its own.
3. **No `student-tasks.md` carrying task content.** All tasks live in the two language-specific files.
4. **No extra files beyond the canonical set plus at most two optional supplementary decks** named `slides-l<n>-<topic>.md` under `student/week-07/`. A `media/` subfolder is allowed only if a slide or self-study explicitly references a contained image.
5. **No `slides.pptx`, no `deck.md`, no `slides.key`, no Reveal.js HTML** anywhere. Hard fail if found.

### Volume (sanity-check brackets, not hard limits)

6. `overview.md`: **200–400 words**.
7. `self-study.md`: **2400–4000 words** total, covering all three lessons.
8. `student-tasks-js.md`: **600–1400 words** total. **1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING tasks.**
9. `student-tasks-csharp.md`: **600–1400 words** total. **1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING tasks.**
10. The two language task files have **the same number of MANDATORY tasks and the same number of DEEPENING tasks** as each other.
11. Optional `student-tasks.md`: **≤200 words** if present.
12. `vocabulary.md`: **10–18 terms.**
13. `slides.md`: **12–18 slides**, separated by `---` on their own line, each slide starting with an H1 (`#`) or H2 (`##`) title and containing minimal supporting content (3–5 short bullets or 1–2 short sentences). Code snippets on slides must be ≤6 lines and inside fenced code blocks.
14. `teacher-materials.md`: **2400–4200 words.** Contains **3 × 90-minute lesson plans** (L19, L20, L21), each with time slots summing to 90.
15. `in-class-tasks.md`: **400–1200 words.** Contains **≥1 MANDATORY teacher-led in-class exercise.**

### Required H2 sections per file

16. `overview.md` must contain (in this order):
    - `## Week 7 theme`
    - `## What you will be able to do by the end of the week`
    - `## Must-do minimum vs. deepening`
    - `## How the three lessons fit together`
    - `## Pick your language`
17. `self-study.md` must contain:
    - `# <Week title>` (Rasmus's invitation).
    - `## Introduction` — sets the week up, names the central question of the course again (verbatim once), and names the dual-language idea.
    - `## Lesson 19 — Why programming languages exist` *(language-agnostic; explicitly labelled so).*
    - `## Lesson 20 — First commands: output, values, variables` *(dual-language; side-by-side snippets in JS and C#).*
    - `## Lesson 21 — Conditions in code: if, else, comparisons` *(dual-language; side-by-side snippets in JS and C#).*
    - `## Picking your language for AT3` — short closing section that previews AT3 in Week 8 and explicitly tells the student the language they pick this week is the language they will use for AT3.
    - `## Summary and what comes next`.
    - **At least 4 `> **Pause for a moment:**` reflection prompts** across the three lesson sections (≥1 per lesson).
18. `student-tasks-js.md` must contain:
    - `## Overview of this week's JavaScript tasks`
    - 1–2 H2 task headers prefixed with `🟢 MANDATORY —` and 2–3 with `🟣 DEEPENING —`. Each MANDATORY task title is suffixed with `(JS)` so it is unambiguous when read in isolation.
    - A `### How to open the JavaScript console` block somewhere near the top (one tiny paragraph per common browser, or one universal recipe — Rasmus's call).
    - Each task ends with a `### Keep your notes` block that mentions **AT3 lands at the end of Week 8** and that the code from these tasks will be reused.
    - Every task that assumes a partner / follower / tester contains a `### If you are doing this alone` subsection with a concrete alternative (24h gap, video self, different browser, class chat).
19. `student-tasks-csharp.md` must contain the parallel structure to `student-tasks-js.md`:
    - `## Overview of this week's C# tasks`
    - 1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING H2 task headers. MANDATORY task titles suffixed with `(C#)`.
    - A `### How to open an online C# environment` block near the top (recommend .NET Fiddle by default; mention sharplab.io as an alternative; mention Replit as a third).
    - `### Keep your notes` blocks pointing at AT3.
    - `### If you are doing this alone` where a partner is assumed.
20. **Parallelism**: for each 🟢 MANDATORY task in `student-tasks-js.md` there is a corresponding 🟢 MANDATORY task in `student-tasks-csharp.md` teaching **the same concept**. Same for DEEPENING. The two task files form pairs.
21. `vocabulary.md` must contain a single H2 `## Week 7 vocabulary`, then each term as an H3 or as a bolded term in a definition list. At least **one term flagged as "looking ahead"** (e.g. *loop* or *error message* for Week 8). Definitions for `console`, `command`, `syntax`, `variable`, `condition`, `if/else`, `comparison operator`, `string`, `int / number`, and one each of `console.log` and `Console.WriteLine` are required.
22. `slides.md` must:
    - Start with a title slide.
    - Contain at least one slide that shows the central question of the course verbatim (revisited from Week 1).
    - Contain at least one **agnostic** slide for L19 ("programming languages exist because…").
    - Contain at least **three side-by-side JS/C# slides** across L20 and L21 combined, with both languages visible on the same slide.
    - Contain at least one slide showing **how to open the browser console** and at least one slide showing **how to open an online C# environment** (.NET Fiddle by default).
    - Use `---` on its own line between slides.
    - Have no embedded `.pptx` references and no speaker-note syntax that assumes a specific renderer.
23. `teacher-materials.md` must contain (in this order):
    - `## Week 7 learning objectives (mapped to Bloom)`
    - `## Common misconceptions for Week 7` — **at least 6 across the week** (≥2 per lesson), each with a `Correction:` line. At least two misconceptions must touch the **JS-vs-C# choice** (e.g. "C# is harder than JS", "JS isn't a real language because it runs in the browser").
    - `## Lesson 19 — 90-minute plan`, `## Lesson 20 — 90-minute plan`, `## Lesson 21 — 90-minute plan` — each with concrete time slots summing to 90, each allocating **30–50% to independent student work** (criterion #25), and each containing a `### Slide cues` subsection naming the slides to use in order during that lesson.
    - `## Facilitation tips` — short cross-cutting block. Must explicitly tell the teacher: "no IDE installation is required; .NET Fiddle / sharplab.io and the browser DevTools console are the only execution targets."
    - `## Answers to common student questions` — at least 5 across the week, including: *"Which language should I pick?"*, *"Is one language harder than the other?"*, *"Will the AT3 grade depend on my language?"*
    - `## Formative assessment tips`.
24. `in-class-tasks.md` must contain:
    - `## Overview`
    - At least 1 H2 task labelled **MANDATORY**, requiring teacher-led classroom interaction. The MANDATORY task must work for both JS and C# students in the same room (i.e. it must not assume the whole class picked one language).
    - Cross-reference back to `teacher-materials.md` so the teacher knows the slot.

### Pedagogical rules

25. **30–50% rule**: in `teacher-materials.md`, for each of the three 90-minute lesson plans, the time blocks visibly labelled as *independent student work* (not lecture, not pair, not group, not debrief) sum to **27–45 minutes** out of 90. Wilhelm checks arithmetically.
26. **Bloom cap**: Week 7 objectives use only Understanding and Applying verbs (*explain, recognise, name, define, run, declare, assign, print, write, predict, map*). **Forbidden verbs** in Week 7 objectives: *analyse, evaluate, design, create, build, debug, refactor, optimise*.
27. **Central question (course-level)**: *"How do I speak to a computer so that it understands what I want it to do?"* appears **verbatim** at least once in `self-study.md` (in the Introduction or Summary) and on at least one slide in `slides.md`.
28. **Language-agnostic L19**: in `self-study.md` and in `slides.md`, the Lesson-19 section / slides must not contain JS-specific or C#-specific working code. Naming the two languages is fine; saying "in JavaScript you would write `console.log(...)`" is fine *as a forward pointer*, but the L19 *exercises and explanations* must not depend on knowing JS or C# syntax. Wilhelm spot-checks.
29. **Dual-language equality** in L20 and L21: every concept introduced for one language is also shown for the other, in the same section, with comparable depth. Wilhelm spot-checks `self-study.md` Lesson-20 and Lesson-21 sections for this parallelism.
30. **No IDE setup mentioned anywhere.** No `node`, no `npm`, no `nvm`, no `dotnet`, no `dotnet new`, no `dotnet run`, no Visual Studio, no VS Code, no JetBrains Rider. Only "browser DevTools console" and "online C# environment (.NET Fiddle / sharplab.io / Replit)". Wilhelm greps.
31. **No testing frameworks** anywhere in any file (`jest`, `mocha`, `vitest`, `pytest`, `xunit`, `nunit`, `mstest`). Wilhelm greps.
32. **No `(AI-resilient)` label** appears in any learner-facing file. Wilhelm greps.
33. **"must-do minimum"** is the wording used in `overview.md` and in the two language task files (not "mandatory minimum"). Wilhelm greps.
34. **AT3 reference** in every task's `### Keep your notes` block in both `student-tasks-js.md` and `student-tasks-csharp.md` — explicitly naming AT3 (not AT1) since Week 7 is the bridge into AT3.
35. **Cross-file consistency**:
    - Task identifiers in `slides.md`'s "Tasks this week" slide list both language files clearly.
    - In-class activities referenced from `teacher-materials.md`'s lesson plans exist in `in-class-tasks.md`.
    - The vocabulary terms used in `self-study.md`, `slides.md` and the task files all appear in `vocabulary.md`.

### Tasks — AI resilience

36. At least **one MANDATORY task in each language file is AI-resilient by construction**, meaning it requires the student's own concrete context (their own name, their own age, their own chosen Week-6 pseudocode snippet, a screenshot of *their* console output, a sticker of their interpreter's exact error message) and produces an observable artefact a teacher can spot-check against an LLM transcript. The AI-resilience is a property; the `(AI-resilient)` label is forbidden in the file.
37. If a DEEPENING task uses an LLM as a sparring partner (e.g. "ask an LLM to translate your JS into C# and check it"), it must include a fenced code block with a sample prompt and an explicit instruction not to accept the LLM's output verbatim — the student must run the code themselves and report what actually happened.

### In-class tasks

38. `in-class-tasks.md` contains **≥1 MANDATORY teacher-led in-class exercise**. The default recommended activity is a **"console relay"** (see briefing below). It must work in a class where some students are on JS and some on C# simultaneously. It must be cross-referenced from `teacher-materials.md`.

### Language and polish

39. **English throughout.** No Finnish words in any of the 7+ files except clearly necessary proper nouns.
40. **Register**: `self-study.md`, the two task files, `overview.md`, `vocabulary.md`, `slides.md` at CEFR ~B1; `teacher-materials.md` and `in-class-tasks.md` at CEFR ~B2.
41. **Valid Markdown**: every fenced code block closes, every code fence uses an appropriate language tag (` ```javascript `, ` ```csharp `, ` ```text ` for output, ` ```pseudo ` for pseudocode echoes), every `---` separator in `slides.md` is alone on its own line.

---

## Briefing Rasmukselle

### Cross-cutting reminders (apply to all 7+ files)

- **Bring forward Week-6 pseudocode.** Lesson 21 is at its strongest when the `if/else` example is one the class has *already written in pseudocode*. Rasmus should pick a single running example (suggested: an age-limit check — "Are you old enough to attend?") and carry it from pseudocode → JS code → C# code across the week.
- **Side-by-side, not "JS first then C#".** When showing both languages, put them on the same slide, in the same section, in the same example. Do not teach JS for two weeks worth of slides and then bolt on C#. Side-by-side framing is the message.
- **No IDE.** Browser DevTools console for JS. .NET Fiddle (default), sharplab.io, or a C#-enabled Replit for C#. Say this once in `self-study.md` Introduction, once in `teacher-materials.md` Facilitation tips, and once at the top of each language task file. No `npm install`, no `dotnet new`.
- **Reference and respect Week 6.** Pseudocode and dry-running are *already a tool the class has*. Use them. The `### Predict before you run` step in L21 tasks is dry-running in code form.
- **"must-do minimum"**, not "mandatory minimum". Verbatim wording in `overview.md` and the task files.
- **No `(AI-resilient)` label.** Just build the tasks so an LLM transcript cannot replace the artefact.
- **No phrase "C# is harder than JS"** (or the reverse) anywhere. They are different surfaces over the same thinking.
- **No testing frameworks anywhere.**
- **No PowerPoint references.** Rasmus delivers `slides.md` (+ optional `slides-l<n>-*.md`).
- **Central course question** must appear verbatim at least once in `self-study.md` and at least once on a slide: *"How do I speak to a computer so that it understands what I want it to do?"*

---

### File 1 — `student/week-07/overview.md` (200–400 words)

**Required H2 structure (in order):**
1. `## Week 7 theme` — short paragraph: the central question revisited, the bridge into code, the dual-language framing.
2. `## What you will be able to do by the end of the week` — 5–7 plain-English "can do" statements (open the console, print a value, declare a variable, write a comparison, write an if/else).
3. `## Must-do minimum vs. deepening` — two-bullet-list contrast. Use the exact wording **"must-do minimum"**.
4. `## How the three lessons fit together` — short paragraph showing L19 (why a language) → L20 (output + variables in both) → L21 (if/else in both).
5. `## Pick your language` — 3–6 sentences telling the student: pick one for this week; you can swap at any point; AT3 next week will use the language you pick.

---

### File 2 — `student/week-07/self-study.md` (2400–4000 words)

**Required structure (in order):**

- `# <Week title>` — suggestion: *"From pseudocode to code — two languages, one way of thinking."*
- `## Introduction`
  - Open with a short scene: a student in Week 6 wrote a clear, dry-runned piece of pseudocode. A pseudocode reader (a friend, a teacher) can follow it. **A real computer cannot.** Why? Because the computer is a literal interpreter and English is not its language.
  - State the central course question verbatim once.
  - Name the week's plan: L19 = why; L20 = first commands; L21 = first decisions. Two languages, side by side.
  - One sentence about tooling: browser console for JavaScript, online environment (e.g. .NET Fiddle) for C#. **No installation needed.**
- `## Lesson 19 — Why programming languages exist` *(language-agnostic)*
  - `### From pseudocode to code` — the conceptual pivot. The thinking is already there; what's missing is a syntax the *computer* will accept.
  - `### What is syntax?` — definition + 2 everyday examples (English vs. Finnish word order; how a vending machine accepts only coins of the right shape) before 1 IT example.
  - `### Interpreter and compiler (one paragraph each, informal)` — informal definitions. Name JS as interpreted (browser) and C# as compiled (then run). Do not labour over JIT / bytecode.
  - `### Two languages, one way of thinking` — name JS and C#. One typical use of each (JS = web pages, browser; C# = .NET apps, games, Unity, tools). Show a **tiny** side-by-side teaser if it helps, but the actual coding starts in L20.
  - `### Why this matters for an IT professional` — short vocational paragraph (you will read more code than you write; you may switch languages multiple times in your career; the thinking is the portable skill).
  - 1 `> **Pause for a moment:**` reflection prompt.
- `## Lesson 20 — First commands: output, values, variables` *(dual-language; everything side by side)*
  - `### Output: speaking to the console` — show how to print a greeting. Two fenced code blocks, JS then C#, with the same text.
  - `### Variables: naming a value` — declare a `name` variable, declare an `age` variable, print both. Two code blocks per concept.
  - `### A first calculation` — compute years until adulthood (`18 - age`) and print the result. Two code blocks.
  - `### Reading the output` — the only debugging tool this week: read what the console says. If nothing appeared, the program did not reach the print.
  - `### The thinking is the same` — call out explicitly: the algorithm is identical (read a value, compute, print); the words and punctuation differ.
  - 1–2 `> **Pause for a moment:**` reflection prompts.
- `## Lesson 21 — Conditions in code: if, else, comparisons` *(dual-language; everything side by side)*
  - `### From pseudocode IF/ELSE to code if/else` — show one piece of pseudocode the class has seen in Week 6 (the age-limit example), then its JS form, then its C# form.
  - `### Comparison operators` — `==`, `!=`, `>=`, `<=`, `>`, `<`. Note they are essentially identical in JS and C#. (Note: JS also has `===`; mention it in one sentence, do not labour.)
  - `### Putting it together — the age-limit check` — a worked side-by-side example.
  - `### Predict before you run` — link explicitly to Week 6 dry-running. Predict the output; then run; then compare.
  - 1 `> **Pause for a moment:**` reflection prompt.
- `## Picking your language for AT3` — short closing section. Tell the student: AT3 lands next week, you will translate a piece of your Week-6 pseudocode into code, you pick the language. Either JS or C# is fine; the grade does not depend on the language.
- `## Summary and what comes next` — Week 8 preview: loops in code, AT3, reading real error messages, presentation of your AT3 program.

**Examples menu Rasmus should lean on:**
- Output: print a greeting; print your name; print "Hello, console".
- Variable: your name, your age, your favourite number.
- Calculation: years until 18; total price = unit price × quantity; password length.
- Condition: age ≥ 18 (the running example); password length ≥ 8; score ≥ pass mark.

---

### File 3 — `student/week-07/student-tasks-js.md` (600–1400 words)

**Required structure:**

- `## Overview of this week's JavaScript tasks`
  - 2–3 sentences naming the must-do minimum (🟢 MANDATORY) vs deepening (🟣 DEEPENING), with the **exact wording "must-do minimum"**.
  - 1 sentence: **AT3 at the end of Week 8 will reuse what you write here. Save your code.**
- `### How to open the JavaScript console` — short universal recipe (right-click → Inspect → Console tab; or `Ctrl+Shift+J` / `Cmd+Opt+J`). One short paragraph.
- Then the tasks.

**Five candidate tasks (Rasmus keeps 1–2 MANDATORY + 2–3 DEEPENING). Default ship: 1 MANDATORY + 3 DEEPENING.**

**Task JS-7.1 — 🟢 MANDATORY — "Your first console program (JS)"**
- Open the browser console. Run `console.log("Hello, <your name>")` with your real name. Screenshot or paste the output into your notes.
- Then: declare `let age = <your real age>;` and `console.log(age);`.
- Then: declare `let yearsToAdulthood = 18 - age;` and `console.log(yearsToAdulthood);`.
- Reflection (2–3 sentences): one thing that surprised you, one thing that worked exactly as you predicted.
- *AI-resilient by construction:* uses the student's real name, real age, real screenshot of their console.
- `### Keep your notes` references **AT3**.

**Task JS-7.2 — 🟢 MANDATORY (alternative to 7.1) — "Console relay: predict, then run (JS)"**
- 3 small JS snippets are provided. Predict the output of each *before* running. Then run them in the console. Compare your prediction with reality and write one sentence per snippet about any surprise.
- *AI-resilient by context:* the predictions in the student's own handwriting (notebook) are the artefact.
- Linnea: this task is also strong as the warm-up half of the in-class "console relay".

**Task JS-7.3 — 🟣 DEEPENING — "First if/else (JS)"**
- Write a 6-line JS program with a variable `age`, an `if (age >= 18) { ... } else { ... }`, and a print in each branch.
- Run it twice: once with `age = 17`, once with `age = 19`. Screenshot both outputs.
- `### If you are doing this alone`: this task has no partner step.

**Task JS-7.4 — 🟣 DEEPENING — "Translate your Week-6 pseudocode (JS)"**
- Pick one piece of your Week-6 pseudocode that has an IF/ELSE. Translate it into JavaScript. It does not have to be elegant; it has to run.
- Save the original pseudocode and the JS code side by side in your notes — **this is exactly the artefact AT3 will ask for.**

**Task JS-7.5 — 🟣 DEEPENING — "Break it on purpose (JS)"**
- Deliberately introduce one mistake at a time into your working program from JS-7.3 (forget a quote; forget a closing bracket; misspell `console.log`). For each, write down the **exact error message** the console prints.
- Reflection (2–3 sentences): which error message was clearest? Which was confusing?

---

### File 4 — `student/week-07/student-tasks-csharp.md` (600–1400 words)

**Parallel structure to File 3.** Tasks are concept-paired with the JS file.

- `## Overview of this week's C# tasks` — same shape as JS file. Same "must-do minimum" wording. Same AT3 reminder.
- `### How to open an online C# environment` — short paragraph: default recommendation is **.NET Fiddle** (`dotnetfiddle.net`, no account needed). Mention `sharplab.io` and a C#-enabled Replit as alternatives. One short paragraph each, or a single short paragraph for all three.

**Five candidate tasks. Default ship: 1 MANDATORY + 3 DEEPENING, paired with JS file.**

**Task CS-7.1 — 🟢 MANDATORY — "Your first console program (C#)"** *(pair of JS-7.1)*
- Open .NET Fiddle. Run `Console.WriteLine("Hello, <your name>")` with your real name. Screenshot the output.
- Then: declare `int age = <your real age>;` and `Console.WriteLine(age);`.
- Then: declare `int yearsToAdulthood = 18 - age;` and `Console.WriteLine(yearsToAdulthood);`.
- Reflection (2–3 sentences) — same prompt as JS-7.1.
- *AI-resilient by construction:* same logic as JS-7.1.

**Task CS-7.2 — 🟢 MANDATORY (alternative to 7.1) — "Console relay: predict, then run (C#)"** *(pair of JS-7.2)*
- 3 small C# snippets provided. Same predict-then-run protocol.

**Task CS-7.3 — 🟣 DEEPENING — "First if/else (C#)"** *(pair of JS-7.3)*
- Same structure, in C#. Note the curly braces are the same as JS; the difference the student will *feel* is the type annotation `int age = ...` and the mandatory semicolons.

**Task CS-7.4 — 🟣 DEEPENING — "Translate your Week-6 pseudocode (C#)"** *(pair of JS-7.4)*
- Same protocol as JS-7.4, in C#. Same AT3 hand-off note.

**Task CS-7.5 — 🟣 DEEPENING — "Break it on purpose (C#)"** *(pair of JS-7.5)*
- Deliberately break the program (forget a semicolon — this is a hard error in C# unlike in JS; misspell `Console.WriteLine`; mismatch a brace). Note the exact compiler error.

**Parallelism rule:** the MANDATORY task in CS-7.1 teaches the same three things as JS-7.1 (output, variable, calculation). The DEEPENING tasks pair 1-to-1.

---

### Optional File 4b — `student/week-07/student-tasks.md` (≤200 words, optional)

If Rasmus chooses to ship this, it is a thin index:

- 1 short paragraph: "This week tasks come in two flavours — pick your language."
- 2 bullet points linking to `student-tasks-js.md` and `student-tasks-csharp.md`.
- 1 sentence: "You can do the deepening tasks in the *other* language if you want to see the side-by-side directly."
- No task content, no numbering of its own.

Sune's default recommendation: **skip this file.** The two language files are clearly named and the overview points at both.

---

### File 5 — `student/week-07/vocabulary.md` (10–18 terms)

**Required terms** (Rasmus may add 1–4 of their own, but must not skip any required ones):

1. Programming language
2. Syntax
3. Command
4. Interpreter (informal)
5. Compiler (informal)
6. Console
7. Output
8. Variable
9. Value
10. Assignment
11. String
12. Int / number
13. Condition
14. If / else
15. Comparison operator
16. `console.log` *(JavaScript-specific entry)*
17. `Console.WriteLine` *(C#-specific entry)*
18. **Loop** — flagged as **"looking ahead — central topic of Week 8"**.

Optional additions: *boolean*, *block (curly braces)*, *semicolon*, *template literal / string interpolation*, *error message*.

Each definition is 1–3 sentences, plain English, with a short example where natural.

---

### File 6 — `student/week-07/slides.md` (~12–18 slides)

**Recommended slide outline (Rasmus may adjust order and titles within the spirit of the structure). Language tag per slide: AGN = agnostic, JS = JS-only, CS = C#-only, BOTH = side-by-side.**

1. `# Week 7 — From pseudocode to code` *(title slide)* — AGN.
2. `## The central question, one more time` — body: the central course question **verbatim** — AGN.
3. `## What this week trains` — 3 bullets for L19, L20, L21 — AGN.
4. `## Why a programming language?` — pseudocode is for humans; code is for the literal computer — AGN.
5. `## What is syntax?` — short definition + 1 everyday + 1 IT example — AGN.
6. `## Two languages we will meet` — JS (browser) and C# (.NET, Unity) — AGN.
7. `## Hello, console — side by side` — JS `console.log("Hello")` vs C# `Console.WriteLine("Hello");` — BOTH.
8. `## Opening the browser console` — quick how-to — JS.
9. `## Opening .NET Fiddle` — quick how-to — CS.
10. `## Variables — side by side` — `let age = 16;` vs `int age = 16;` — BOTH.
11. `## A first calculation — side by side` — years to adulthood — BOTH.
12. `## Predict before you run` — link back to Week 6 dry-running — AGN.
13. `## Comparison operators` — table of `==`, `!=`, `>=`, `<=`, `>`, `<`. Note "essentially identical in JS and C#" — BOTH.
14. `## First if/else — side by side` — age-limit check, both languages on the same slide — BOTH.
15. `## In-class: console relay` — 1-slide description of the in-class activity — AGN.
16. `## Tasks this week` — point at `student-tasks-js.md` and `student-tasks-csharp.md`; mention must-do minimum vs. deepening — AGN.
17. `## Picking your language for AT3` — preview AT3 in Week 8 — AGN.
18. `## Recap — central question` — verbatim again — AGN.

Aim 15–18 slides. **At least 3 BOTH slides required** (criterion #22). Use `---` on its own line between slides. Code on slides ≤6 lines per fenced block.

**Supplementary deck candidates (optional, ≤2 total, 4–8 slides each):**

- `slides-l20-walkthrough.md` — a step-by-step walkthrough of the "first program" demo, JS column and C# column, screenshot-by-screenshot. Strong candidate if the teacher wants a slide-by-slide demo for L20.
- `slides-l21-age-check.md` — the running age-limit example carried from pseudocode → JS → C#, one transformation per slide. Strong candidate.

Rasmus decides per his judgement.

---

### File 7 — `teacher/week-07/teacher-materials.md` (2400–4200 words)

**Required H2 sections (in order):**

1. `## Week 7 learning objectives (mapped to Bloom)` — restate the L19–L21 objectives, grouped by Bloom. Understanding + Applying only.
2. `## Common misconceptions for Week 7` — ≥6 across the week (≥2 per lesson). Suggested set:
   - **L19**: *"Pseudocode is enough — why do we need code?"* → Correction: pseudocode is for humans; the computer reads only what it can parse literally. // *"There is one 'correct' programming language."* → Correction: thousands of languages exist; JS and C# are two of many; the thinking transfers.
   - **L20**: *"C# is harder than JS"* (or the reverse) → Correction: the thinking is the same; the surface differs slightly. // *"`console.log` and `Console.WriteLine` do different things"* → Correction: they do the same thing — print to the console — with different syntax.
   - **L21**: *"`=` means 'is equal to'"* → Correction: `=` assigns, `==` compares (and JS also has `===`). // *"`if` without `else` is wrong"* → Correction: `else` is optional; `if` alone is valid.
3. `## Lesson 19 — 90-minute plan` — language-agnostic. Time slots summing to 90, with an independent block of 27–45 min. Suggested skeleton:
   - 0–10 min: warm-up — show one of last week's pseudocode pieces; ask the class "could a computer run this exactly as written?"
   - 10–30 min: instructor input — what is a programming language, what is syntax, why JS and C#.
   - 30–60 min: **INDEPENDENT WORK** (30 min) — students read the L19 section of `self-study.md` and write 4–6 sentences in their notes: *"Why does a programming language need to exist when pseudocode is already precise?"*
   - 60–80 min: pair activity — pairs share their answer; pairs find one place they disagree; whole-class debrief picks 2 disagreements.
   - 80–88 min: preview L20 — show one side-by-side JS/C# `Hello` slide.
   - 88–90 min: closing.
   - `### Slide cues`: slides 1–6 in order; show slide 7 only as a teaser.
4. `## Lesson 20 — 90-minute plan` — dual-language. Suggested:
   - 0–10 min: warm-up — open the browser console live; open .NET Fiddle live; print `"Hello, class"` in each, side by side.
   - 10–25 min: instructor input — variables, assignment, output. Teacher writes one example in JS, then the same example in C#, on the board or screen.
   - 25–55 min: **INDEPENDENT WORK** (30 min) — students complete the MANDATORY task in their chosen language (`JS-7.1` or `CS-7.1`).
   - 55–75 min: in-class teacher-led activity — **"Console relay"** (see `in-class-tasks.md`), language-mixed.
   - 75–85 min: whole-class debrief — collect one surprise per language; build a "we saw" board.
   - 85–90 min: closing + preview L21.
   - `### Slide cues`: slides 7–11 in order; slide 12 as transition into L21.
5. `## Lesson 21 — 90-minute plan` — dual-language. Suggested:
   - 0–10 min: warm-up — put the Week-6 age-limit pseudocode on the board; ask the class "what would this look like in code?"
   - 10–30 min: instructor input — comparison operators (board) and `if/else` block structure. Demo the age-limit example in both languages side by side.
   - 30–60 min: **INDEPENDENT WORK** (30 min) — students do the `if/else` deepening task in their chosen language (`JS-7.3` or `CS-7.3`).
   - 60–80 min: pair activity — pair JS-students with C#-students 1-to-1. Each pair compares their code line-by-line. Whole-class collects 2 differences.
   - 80–88 min: closing — explicit hand-off to AT3 in Week 8.
   - 88–90 min: housekeeping.
   - `### Slide cues`: slides 12–18 in order, including the "Picking your language for AT3" slide near the end.
6. `## Facilitation tips` — short cross-cutting block. Must contain: "**No IDE installation is required.** Students use the **browser DevTools console** for JavaScript and an **online C# environment** (.NET Fiddle, sharplab.io, or a C#-enabled Replit) for C#. Do not install Node.js, .NET SDK, Visual Studio or VS Code for this week." Plus 3–4 short tips on managing a language-mixed classroom (let students pick; don't push one language; pair JS+C# students for the L21 pair activity).
7. `## Answers to common student questions` — at least 5 across the week. Required questions:
   - *"Which language should I pick?"* — pick the one that looks less scary to you; you can swap any time.
   - *"Is one language harder than the other?"* — no; they are different surfaces.
   - *"Will my AT3 grade depend on my language?"* — no; the grade depends on the thinking.
   - *"Do I need to install anything?"* — no. Browser console for JS, .NET Fiddle for C#.
   - *"Can I use ChatGPT to write my code?"* — you can use it to check; you cannot submit AT3 code you do not understand line by line.
8. `## Formative assessment tips` — 3–5 quick checks. Suggested: exit ticket ("print one line of code, in either language, that prints your name"); pair report-back; one-minute paper; live show-of-screens.

Cross-reference `in-class-tasks.md` from the L20 plan (where the console relay sits).

---

### File 8 — `teacher/week-07/in-class-tasks.md` (400–1200 words)

**Required structure:**

- `## Overview` — 2–3 sentences naming the tasks and when in the week they fit. Note explicitly that activities are designed to work in a **language-mixed room** (some students on JS, some on C#).

**Two concrete activity ideas (default: both):**

**Activity A — MANDATORY — "Console relay"** *(whole-class + teacher-led, ~20 min, slotted in Lesson 20 between 55–75 min)*

- Teacher prepares **6 small snippets**: 3 in JavaScript, 3 in C#. Each is ≤4 lines. Examples:
  - JS: `let x = 5; let y = 3; console.log(x + y);`
  - JS: `let name = "Lyra"; console.log("Hello, " + name);`
  - JS: `let age = 17; if (age >= 18) console.log("adult"); else console.log("minor");`
  - C#: `int x = 5; int y = 3; Console.WriteLine(x + y);`
  - C#: `string name = "Lyra"; Console.WriteLine("Hello, " + name);`
  - C#: `int age = 17; if (age >= 18) Console.WriteLine("adult"); else Console.WriteLine("minor");`
- One snippet is shown at a time on the projector. **Before running**, each student writes down (on paper or in chat) what they think the console will print. **Then** the teacher runs it live. The class compares predictions with reality.
- Mix languages on purpose: even a student who picked JS sees C# snippets, and vice versa, side by side with the JS equivalent. The comparison is the lesson.
- 6 snippets × ~3 minutes = ~18 minutes. Fits the 55–75 min slot.
- **Why it requires the classroom:** the live predict-then-run rhythm with immediate peer comparison is the whole point. Cannot be done as homework.
- **Cross-reference:** `teacher-materials.md` Lesson-20 90-min plan, 55–75 min block.

**Activity B — OPTIONAL — "Translate-your-neighbour" (pair, ~20 min, slotted in Lesson 21 between 60–80 min)**

- Pair a JS-student with a C#-student.
- Each shows the other their `if/else` code from `JS-7.3` / `CS-7.3`.
- Each tries to **translate** the other's code into their own language — by hand, on paper, no LLM.
- Compare the result with the original. Discuss what stayed the same, what was different.
- Closing debrief: each pair contributes one observation to the board.

Cross-reference back to `teacher-materials.md` so the teacher knows the exact 90-min slot.

---

## Avoimet kysymykset

1. **Optional `student-tasks.md` index file.** This plan recommends **skipping it** — the two language-named task files are clear on their own. Wilhelm accepts either choice; if the file is present it must be ≤200 words and content-free. **Default assumption:** Rasmus does not ship `student-tasks.md`.
2. **Default selection of which MANDATORY task to ship in each language file.** Two candidates are offered (`X-7.1 "Your first console program"` vs `X-7.2 "Console relay predict-then-run"`). **Default assumption:** Rasmus ships **`X-7.1` as MANDATORY** (concrete artefact: screenshots of *their* console output with *their* name and *their* age — strongly AI-resilient) and keeps `X-7.2` as the in-class console-relay activity instead of as a take-home task.
3. **Number of MANDATORY tasks per language file.** The brief says 1–2. **Default assumption:** Rasmus ships **1** MANDATORY per language file plus **3** DEEPENING tasks. If the class is strong, the teacher can promote one DEEPENING to MANDATORY locally; this is not Rasmus's call.
4. **Supplementary decks.** Two strong candidates (`slides-l20-walkthrough.md` and `slides-l21-age-check.md`). **Default assumption:** Rasmus ships **one** of these — `slides-l21-age-check.md` (the carry-through from pseudocode to JS to C# is the highest-value supplementary lesson). The walkthrough deck is good to have but not necessary. Rasmus may decide otherwise.
5. **`===` in JavaScript.** Should we name strict equality or hide it for now? **Default assumption:** name it in **one sentence** in `self-study.md` Lesson-21 ("JS also has `===` for strict equality; both work for what we are doing here"); not on slides; not in tasks. Avoids tripping over loose equality next year while not labouring the type-coercion topic.
6. **C# string interpolation vs concatenation.** Two equally valid options (`"Hello, " + name` vs `$"Hello, {name}"`). **Default assumption:** Rasmus picks **concatenation with `+`** in both languages — the syntax overlap is the message. Mention `$"..."` once in vocabulary as a "looking ahead" optional term.
7. **Semicolons.** JS is lenient, C# is strict. **Default assumption:** Rasmus shows every JS example **with** a trailing semicolon for parallelism, mentions in one sentence that JS does not strictly need it, and moves on. Otherwise the side-by-side comparison gets a visual stutter for no learning gain.
8. **Slide count.** 12–18 by criterion. **Default assumption:** Rasmus targets **15–17 slides** in `slides.md`.
9. **Reflection-prompt count in `self-study.md`.** ≥4 across the three lessons (≥1 per lesson) required. **Default assumption:** Rasmus ships 5–6, with 2 in L20 (the densest lesson).
10. **MANDATORY label inline.** `in-class-tasks.md` uses **MANDATORY** as an inline tag in the H2. Wilhelm greps. **Default assumption:** consistent with Week 1.
11. **30–50% block contiguity.** Wilhelm accepts a single contiguous independent block per 90-min lesson or up to two blocks summing to 27–45 min. **Default assumption:** Rasmus ships **one contiguous block of 30 min** in each lesson — simplest, hardest to mis-audit.
12. **Whether L19 may *show* a side-by-side teaser snippet.** Criterion #28 says L19 must not depend on knowing JS or C# syntax. A teaser is allowed as a forward pointer. **Default assumption:** Rasmus includes **one** small teaser slide (slide 7 in the outline above) at the L19/L20 boundary — it is technically the first L20 slide, but functionally lives at the seam.
