# Computational Thinking — Week 3 Plan (Sune, Gate #1)

Course: Computational Thinking (English)
Target: First-year vocational ICT students, ~15–17, no prior programming
Duration: 8 weeks x 3 lessons/week x 90 min = 24 lessons
Pipeline scope this run: Sune produces this Week 3 plan; Rasmus builds **only Week 3** in the canonical 7-file weekly structure; Linnea/Wilhelm audit Week 3; Alfred packages a Markdown-only Week 3 release (no PDF, no PPTX rendering this round).

The 24-lesson topic table, Bloom mapping, AT placement and vocabulary previews are inherited from the locked course plan at `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/01-suunnitelma.md`. This file replaces the per-lesson granularity with **per-week** granularity for Week 3. Where this plan and the Week 1 plan disagree, the Week 3 **brief** wins.

---

## Suunnitelma

### Course overview (short, reused)

The course answers one central question: **"How do I speak to a computer so that it understands what I want it to do?"** Students start from familiar everyday situations and gradually move toward a formal, step-by-step way of expressing instructions. By the end of Week 6 students can write pseudocode that includes sequence, condition, and repetition; in Weeks 7–8 the same pattern is translated into a tiny browser-based JavaScript program. Programming is the *last* layer; computational thinking is what the course actually trains. Three assessed tasks (AT1, AT2, AT3) are spaced so each rests on competencies the preceding weeks actually built; all three are AI-resilient by construction.

### Week 3 theme and connection to Week 2

Week 3 theme is **"Describing a process"**. Week 2 ended with **decomposition**: the student can take a problem too big for a single algorithm and break it into a main task, subtasks and a goal (this was the foundation for **AT1**, submitted at the start of Week 3). Week 3 continues by asking *how do I write down a process so someone else can run it?* It introduces three closely linked ideas:

1. A **process** has a shape that a list does not — it has a beginning, an end, and (sometimes) decision points. The simple flowchart is the first visual artefact in the course (L7).
2. To draw a flowchart that fits on a page, you must **abstract** — keep what matters at the level you are describing, hide everything below it (L8). Abstraction is kept concrete: a bus stop is not a "transport node"; a username is not "a user identifier"; abstraction means *choosing what to leave out for this audience*.
3. When the same chunk of process keeps appearing, give it a name and reuse it — this is the **informal idea of a function**, without code (L9). "Log a user in" is a function; "register a new device" is a function. Both are reused everywhere.

The central message for the week is the one in the brief, kept verbatim where it appears in materials: **"Once you can decompose a problem, the next skill is to *describe* the process so someone else can run it — and to decide which details matter and which can be safely hidden."**

Week 3 carries Bloom dominant verbs **Remembering + Understanding**, with light **Applying** acceptable in all three lessons (students draw a small flowchart, name what is hidden in a given abstraction, and box a reused chunk of process and give it a name). No Analyzing, Evaluating, Creating in Week 3 objectives. No code, no pseudocode, no variables, no loops, no testing frameworks.

Week 3 produces **no AT submission**, but every task's `### Keep your notes` block reminds the student that **AT2 (process description) is submitted at the end of Week 5 / during Week 6**. The vocabulary built this week (flowchart, decision, abstraction, level of detail, reusable block / function-without-code) is exactly the vocabulary AT2 will ask the student to use.

### L7 breakdown — Describing a process: list, step-by-step structure, and simple flowchart

**Topic (verbatim from the brief):** *Describing a process: list, step-by-step structure, and simple flowchart.*

**Learning objectives** (Remembering + Understanding, light Applying):
- (a) **Recognise** when a process is more than a flat list — i.e. when it has decision points or branches. *(Understanding)*
- (b) **Name** the four basic flowchart shapes used in this course: start/end (oval), step (rectangle), decision (diamond), arrow (flow). *(Remembering)*
- (c) **Read** a small flowchart and **describe in plain English** what it does and where it ends. *(Understanding)*
- (d) **Draw** a small flowchart (≤8 shapes) for a familiar everyday process with at least one decision point. *(light Applying)*
- (e) **Explain** why a flowchart is easier than a list when a process has branches. *(Understanding)*

**Key vocabulary preview:** process, flowchart, step (rectangle), decision (diamond), start/end (oval), arrow / flow, branch, Yes/No path. Preview term: *abstraction* for L8.

**Central message for L7 (one sentence):** A flowchart is the shape a process takes on paper when a flat list of steps stops being enough — and the moment you draw one, you have to decide *which* steps deserve their own box.

**Vocational examples to lean on:** help-desk triage flow ("can the user log in? → if yes, do X; if no, do Y"), a file-naming check ("does the file name match the convention? → if yes, save; if no, rename"), an "is the device on the school network?" check before installing software.

### L8 breakdown — Abstraction

**Topic (verbatim from the brief):** *Abstraction.*

**Learning objectives** (Remembering + Understanding, light Applying):
- (a) **Define** abstraction in plain English: hide the detail that does not matter at this level of description. *(Remembering)*
- (b) **Identify** what has been hidden in a given everyday abstraction (a bus stop, a username, a "send" button). *(Understanding)*
- (c) **Explain** that the right level of detail depends on **who is reading the process and what they will do with it**. *(Understanding)*
- (d) **Choose** a single level of detail for a small flowchart and **rewrite** one step at a lower level of detail if asked. *(light Applying)*
- (e) **Recognise** the difference between *hiding* a detail and *forgetting* it. *(Understanding)*

**Key vocabulary preview:** abstraction, level of detail, hidden detail, audience (of a description), "what does the box mean?". Preview term: *function* (the L9 informal sense).

**Central message for L8 (one sentence):** Abstraction is not philosophy; it is choosing what to leave out so the description fits the audience — a bus stop is enough for a passenger, a GPS coordinate is enough for a bus dispatcher, neither is right for the other.

**Vocational examples to lean on:** the school portal's "Log in" button (abstracts away the OAuth dance, the password store, the cookie); a help-desk ticket title ("printer broken") that abstracts away which printer and what "broken" means until the agent opens the ticket; a file-naming convention (`2026-05-20_invoice-001.pdf`) that abstracts the *purpose* of the file into its name.

Hard rule from the brief: **Keep abstraction concrete.** Use a bus stop, a username, a "Save" button, a help-desk ticket title. Do not let the lecture drift into "abstraction is a way of thinking about everything"; that is a philosophy lecture, not Week 3.

### L9 breakdown — Reusable instructions and the idea of a function without code

**Topic (verbatim from the brief):** *Reusable instructions and the idea of a function without code.*

**Learning objectives** (Remembering + Understanding, light Applying):
- (a) **Recognise** that the same small chunk of process can appear inside many larger processes. *(Understanding)*
- (b) **Name** a reused chunk with a short verb-phrase ("log the user in", "rename the file", "back up the device"). *(light Applying)*
- (c) **Explain** in plain English what *function* means in this Week 3 informal sense: a named, reusable, well-described chunk of process. *(Understanding)*
- (d) **Spot** a reused chunk in two example processes and **draw it as a single box** instead of repeating the steps. *(light Applying)*
- (e) **Describe** the trade-off in one sentence: a named reused block hides detail (abstraction!) but makes the larger process readable. *(Understanding)*

**Key vocabulary preview:** reusable block, named block, function (informal — *"a named chunk of process you can use more than once"*), input to a function (informal), output of a function (informal), "what does this function do?". Preview term: *condition* / *if-then-else* for Week 5.

**Central message for L9 (one sentence):** When the same chunk of process keeps reappearing, give it a name; "register a new device" is one named block you can drop into a dozen larger processes without rewriting the steps.

**Vocational examples to lean on:** a "register a new device" procedure used for every new laptop, projector, conference-room display; a "reset a password" mini-procedure used in dozens of help-desk tickets; a "format a USB stick the school way" mini-procedure used by every new IT trainee.

**Important boundary:** L9 introduces the *idea* of a function, in English prose and as a named box in a flowchart. **No code, no parentheses, no `function name() { ... }` syntax, no return values, no parameters as named slots.** All of that is Weeks 5–7. In Week 3 the function is a labelled box with a verb-phrase inside and a short English description below.

### Core minimum vs. deepening (must-do minimum)

**Must-do minimum (every student must leave Week 3 able to):**
- State the central message of the week in their own words.
- Read a small flowchart (≤8 shapes) and describe in plain English what it does.
- Draw a small flowchart for a familiar everyday process with at least one decision point.
- Define *flowchart*, *decision*, *abstraction*, *level of detail*, *reusable block / function (Week 3 sense)* in plain English.
- Identify, in a given everyday abstraction (e.g. a "Login" button), at least two details that have been hidden.
- Spot one reused chunk of process in two example flowcharts and propose a short name for it.

**Deepening (optional extension, not required for AT2):**
- Draw a flowchart with two decision points (nested branching) for a vocational scenario.
- Take one of their own flowcharts and **rewrite a single step at a lower level of detail** — opening up one box into 2–4 sub-boxes — and explain in one sentence which audience the new version is for.
- Identify three reusable blocks across two or more example processes (or across the student's own previous AT1 decomposition) and name each.
- Use an LLM as a sparring partner to challenge their abstraction choices, with a structured prompt and an explicit reject/keep/revise step.

### Forward-looking stubs for Weeks 4–8

**Week 4 — Alternative solutions and evaluation (Lessons 10–12).** "Correct" is not unique. Students produce multiple valid solutions to the same problem, apply criteria (correctness, simplicity, readability, speed) to compare them, and practise peer feedback. Bloom focus: Applying + Analyzing + light Evaluating. Week 4 picks up Week 3's flowchart skill to compare two flowcharts for the same goal.

**Week 5 — Logic structures (Lessons 13–15).** Sequence, conditions (if-then-else, AND/OR informally) and repetition (repeat-until, for-each) are formalised. The Week 3 *decision diamond* is renamed *condition* and gets formal language. Bloom focus: Understanding + Applying. Foundation for AT2.

**Week 6 — Pseudocode and dry running (Lessons 16–18).** Synthesis of Weeks 1–5 into pseudocode. Variables and input/processing/output appear. Students dry-run pseudocode with a trace table and fix bugs. **AT2** is submitted (process description — Week 3 vocabulary is exactly the vocabulary AT2 reuses). Bloom focus: Applying + Analyzing.

**Week 7 — First JavaScript (Lessons 19–21).** The bridge into code. Browser console only. `console.log`, `let`, `if/else`, comparison operators. Lesson 1's central question is revisited: a formal language exists precisely *because* computers cannot disambiguate. The Week 3 informal "function" becomes a real JS function shape. Bloom focus: Understanding + Applying.

**Week 8 — Loops, AT3, debugging, presentation (Lessons 22–24).** Loops in JavaScript, translation of a piece of own pseudocode into JavaScript (**AT3**), reading a real error message, and a 2-minute oral presentation of the AT3 program. The course closes where Lesson 1 started — speaking to a computer so it understands. Bloom focus: Applying + Analyzing + Creating (AT3).

---

## Rajaukset

**Out of scope for Week 3 (some items repeated from the course-level scope for clarity):**

- **No code, no pseudocode, no JavaScript, no variables, no loops** in Week 3. Pseudocode is Week 6. JavaScript is Week 7+.
- **No formal `function() { ... }` syntax** in any Week 3 file. The L9 "function" is a verb-phrase in a flowchart box, plus a short English description of what it does. No parentheses around a name.
- **No formal conditions or logic operators** (if-then-else, AND/OR). The L7 decision diamond carries a plain-English question and two outgoing arrows labelled Yes/No (or equivalent). The formal language belongs to Week 5.
- **No automatic testing or debugging frameworks** (jest, mocha, vitest, pytest, etc.). Stated explicitly even though Week 3 has no code anyway. Hard fail if any appear.
- **No IDEs, no Node.js, no npm.**
- **No slide deck files beyond `slides.md`**, plus the optional `slides-l<n>-<topic>.md` supplement(s) when a lecture segment genuinely needs more material. No `.pptx`, no `.key`, no Reveal.js, no Google Slides. Alfred handles release packaging in Markdown only this round; PPTX rendering is not in scope this run.
- **No images required.** A `media/` subfolder is allowed only if a slide or self-study explicitly references a contained image (a hand-drawn flowchart screenshot is the most likely candidate; pure ASCII / Mermaid-style inline diagrams in fenced code blocks are preferred and require no `media/` folder).
- **No platform-side independent exercises.**
- **No deep CS theory.** No Big-O, no formal grammars, no recursion, no graph theory. The flowchart is a teaching device, not a graph in the CS-theoretic sense.
- **No "abstraction is everything" philosophy lecture.** Abstraction stays concrete: a bus stop, a username, a Login button, a file-naming convention.
- **No external accounts requiring email signup.**
- **No graded essays in Week 3.** Week 3 has no AT submission.

**Language:** English throughout, in all 7 (or 7 + optional supplementary deck) files. The H2 headings in *this plan file* may remain in Finnish (`Suunnitelma`, `Rajaukset`, `Hyväksymiskriteerit`, `Briefing Rasmukselle`, `Avoimet kysymykset`) because they are part of the Sune template; **all of Rasmus's Week 3 files must be fully English**, including their section headings. Börje (Finnish polishing) is skipped for this run.

**Pipeline scope this run:**
- Sune produces this Week 3 plan (you are reading it).
- Rasmus builds **only Week 3** in the canonical weekly structure (5 student files + 2 teacher files, plus 0–2 optional supplementary deck files).
- Linnea and Wilhelm audit Week 3 only.
- Alfred packages a **Markdown-only** Week 3 release this round. No PDF, no PPTX.

---

## Hyväksymiskriteerit

Wilhelm verifies the Week 3 package against the following concrete, checkable criteria.

### Structural — files and folders

1. **All 7 canonical files present**, with exactly these filenames (case-sensitive, lowercase, kebab-case):
   - `student/week-03/overview.md`
   - `student/week-03/self-study.md`
   - `student/week-03/student-tasks.md`
   - `student/week-03/vocabulary.md`
   - `student/week-03/slides.md`
   - `teacher/week-03/teacher-materials.md`
   - `teacher/week-03/in-class-tasks.md`
2. **Optional supplementary slide deck(s)** may exist as `student/week-03/slides-l<n>-<topic>.md` (4–8 slides, same `---` separator rule). Wilhelm accepts 0, 1, or 2 such files. Any other slide file in either folder is a hard fail.
3. **No extra files** in `student/week-03/` or `teacher/week-03/`. A `media/` subfolder is allowed only if a slide or `self-study.md` explicitly references a contained image.
4. **No `slides.pptx`, no `deck.md`, no `slides.key`, no Reveal.js HTML, no `.pdf`** anywhere in the Week 3 folders. Hard fail if found.

### Volume (sanity-check brackets, not hard limits)

5. `overview.md`: **200–400 words**.
6. `self-study.md`: **2400–4000 words** (roughly 3× a golden-sample single lesson, since this covers L7, L8 and L9).
7. `student-tasks.md`: **800–1800 words** total. **1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING** tasks (see #18).
8. `vocabulary.md`: **10–18 terms**, each with a 1–3 sentence English definition.
9. `slides.md`: **~10–20 slides**, separated by `---` on its own line. Each slide starts with `#` or `##` and carries minimal supporting content (3–5 short bullets or 1–2 short sentences).
10. `teacher-materials.md`: **2400–4200 words**. Contains **3 × 90-minute lesson plans** (L7, L8, L9), each with time slots summing to 90.
11. `in-class-tasks.md`: **400–1200 words**. Contains **at least 1 MANDATORY teacher-led in-class exercise** (pair/group/whole class) that genuinely requires classroom interaction.

### Required H2 sections per file

12. `overview.md` must contain (in this order):
    - `## Week 3 theme`
    - `## What you will be able to do by the end of the week`
    - `## Must-do minimum vs. deepening` (with a clear two-column or two-bullet contrast; the words **"must-do minimum"** appear in this section — *not* "core minimum", *not* "mandatory minimum")
    - `## How the three lessons fit together`
13. `self-study.md` must contain:
    - `# <Week title>` — inviting H1.
    - `## Introduction` — names the connection to Week 2 (decomposition → AT1) and states the Week 3 central message in plain English at least once.
    - `## Lesson 7 — Describing a process and the simple flowchart` (or close variant)
    - `## Lesson 8 — Abstraction`
    - `## Lesson 9 — Reusable instructions: the idea of a function without code`
    - `## Summary and what comes next` — closes the loop on the central message and previews Week 4.
    - **At least 4 `> **Pause for a moment:**` reflection prompts** across the three lessons (at least 1 per lesson).
14. `student-tasks.md` must contain:
    - `## Overview of the week's tasks` — names the must-do minimum vs. deepening contrast and reminds the student that **AT2 (process description) lands end of Week 5 / during Week 6**.
    - One H2 per task, with **🟢 MANDATORY —** or **🟣 DEEPENING —** in the H2 title (the green/purple dot plus the word in caps).
    - Each task ends with a `### Keep your notes` block that **references AT2 by name** (e.g. *"AT2 — process description — is submitted at the end of Week 5 / during Week 6, and the flowchart vocabulary you build here is exactly what AT2 expects."*). **No mention of AT1**; AT1 was submitted at the start of Week 3.
15. `vocabulary.md` must contain a single H2 `## Week 3 vocabulary`. Each term as an H3 (or as a bolded term in a definition list). **At least one term flagged as a "looking ahead" preview** (e.g. *condition* for Week 5, or *parameter* for Week 6 — Rasmus picks one).
16. `slides.md` must:
    - Start with a title slide.
    - Contain **at least one slide whose body shows the Week 3 central message verbatim** (from the brief: *"Once you can decompose a problem, the next skill is to describe the process so someone else can run it — and to decide which details matter and which can be safely hidden."*).
    - Use `---` on its own line between slides.
    - Have no embedded `.pptx` references and no speaker-note syntax that assumes a specific renderer.
17. `teacher-materials.md` must contain (Wilhelm checks the exact H2 wording — case-sensitive on the keywords, hyphen tolerated either way around "90-minute"):
    - `## Week 3 learning objectives (mapped to Bloom)`
    - `## Common misconceptions for Week 3`
    - `## Lesson 7 — 90-minute plan`
    - `## Lesson 8 — 90-minute plan`
    - `## Lesson 9 — 90-minute plan`
    - `## Facilitation tips`
    - `## Answers to common student questions`
    - `## Formative assessment tips`
    - Each 90-min plan ends with a **Slide cues** subsection (`### Slide cues — main deck \`slides.md\`` or `### Slide cues — main deck \`slides.md\` + supplementary deck` when a supplementary deck exists for that lesson).

### Pedagogical rules

18. `student-tasks.md` contains **1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING** tasks. The MANDATORY task(s) use the wording **"must-do minimum"** (in the overview at the top of the file, or in the task body, or both). The phrase **"mandatory minimum" must not appear**; **"AI-resilient" must not appear in any learner-facing file** (it is an internal property Linnea audits, not a label that ships).
19. **"If you are doing this alone" subsection.** Every task that assumes a partner / follower / tester contains an `### If you are doing this alone` H3 subsection with a **concrete alternative** (24-hour gap, recording yourself on video, executing the process on a different device, posting the process in the class chat or course platform). Wilhelm greps the exact phrase *"If you are doing this alone"*.
20. **30–50% rule.** In `teacher-materials.md`, for each of the three 90-minute lesson plans, the time blocks visibly labelled **independent student work** (not lecture, not pair, not group, not debrief, not in-class teacher-led activity) sum to **27–45 minutes** out of 90. Wilhelm checks arithmetically. A single contiguous block or up to two blocks both clearly labelled INDEPENDENT WORK are acceptable.
21. **Bloom cap (Week 3).** Learning objectives use only Remembering and Understanding verbs (*define, describe, explain, identify, recognise, give an example of, list, name, restate, summarise, read*) with light Applying allowed in all three lessons (*draw a small flowchart, rewrite one step at a lower level of detail, name a reused block, draw a reused chunk as one box*). **Forbidden verbs** in Week 3 objectives: *create, build, design, develop, evaluate, judge, analyze, decompose (no — that was Week 2), debug, optimise, refactor*.
22. **Central message verbatim**, as in the brief, appears on at least one slide in `slides.md` and at least once in `self-study.md` (introduction or summary).
23. **Examples-first principle.** In `self-study.md`, every conceptual section that uses both kinds of examples places the **everyday example before the IT example**. Wilhelm spot-checks each of the three lesson sections.
24. **Concrete abstraction.** In `self-study.md`'s L8 section and in `slides.md`'s abstraction slides, the abstraction examples must be concrete (a bus stop, a username, a "Login" button, a help-desk ticket title, a file-naming convention). Wilhelm spot-checks: if any sentence drifts to *"abstraction is a fundamental mode of human cognition"* or similar philosophy, hard fail.
25. **"The computer is literal" framing preserved.** The phrase "the computer is stupid / dumb" must not appear; the literal framing inherited from Week 1 must hold throughout Week 3 materials. Wilhelm greps.
26. **No automatic testing frameworks** mentioned anywhere in any of the Week 3 files.
27. **No code, no pseudocode, no `function() { ... }` syntax** anywhere in Week 3 files. Wilhelm greps for parentheses immediately after a verb-phrase and for the words `console.log`, `let `, `if (`, `function `.
28. **Slide cues exist for every 90-min plan** (criterion #17 already; restated as a pedagogical-rule cross-check). Each Slide cues subsection names which main-deck slides are on screen during which activity, and explicitly states "no slides" during independent work or board work.

### Cross-file consistency

29. **Task numbering matches across files.** Tasks in `student-tasks.md` are numbered `3.1`, `3.2`, `3.3`, … (Week 3 prefix). Any reference to a task in `slides.md`, `teacher-materials.md`, or `in-class-tasks.md` uses the same numbering.
30. **In-class activities referenced in `teacher-materials.md` exist in `in-class-tasks.md`** by the same name. Wilhelm cross-checks.
31. **English throughout.** No Finnish words in any of the Week 3 files except clearly necessary proper nouns.

### Tasks (AI-resilience without the label)

32. At least one 🟢 MANDATORY task is **AI-resilient by construction** — requires the student's own concrete context (a specific everyday or vocational process from their own life or school), an observable artefact (a hand-drawn flowchart with a date and the student's initials, a photo of a board, a real follower's reaction), or a critique-the-LLM mechanism. The word *AI-resilient* does **not** appear in the file.
33. If a 🟣 DEEPENING task uses an LLM as a sparring partner, it must include a fenced code block with a sample prompt and an explicit instruction not to accept the LLM's output verbatim — followed by a written accept / modify / reject step.

### In-class tasks

34. `in-class-tasks.md` contains **at least 1 MANDATORY teacher-led in-class exercise** that genuinely requires classroom interaction (pair work, role play, whole-class debrief, board game, whiteboard flowchart relay). The MANDATORY tag appears in the H2 of that task. It is cross-referenced from `teacher-materials.md` with the exact 90-min slot in which it runs.

### Language and polish

35. **Register**: `self-study.md`, `student-tasks.md`, `overview.md`, `vocabulary.md` and `slides.md` at CEFR ~B1 (short sentences, common vocabulary); `teacher-materials.md` and `in-class-tasks.md` at CEFR ~B2.
36. **Valid Markdown**: every code fence closes, every table renders, no broken internal links, `---` separators in any slide deck are alone on their own line.

---

## Briefing Rasmukselle

### Cross-cutting reminders (apply to all Week 3 files)

- **Everyday before IT, always.** When introducing flowcharts, abstraction or reusable blocks, lead with a familiar 15-year-old scene (the route from home to school, the morning routine, the "should I bring an umbrella?" decision, the "Save" button) and only then pivot to an IT example (a help-desk triage, a file-naming check, a "register a new device" mini-procedure, a Login button).
- **The computer is literal, not stupid.** Keep the Week 1 framing alive.
- **No code, no pseudocode, no JavaScript, no variables, no loops, no `function name() { ... }`** in Week 3. The L9 function is a verb-phrase in a box and a short English description below. That is all.
- **No "AI-resilient" label in learner-facing files.** The property holds (Linnea audits it); the word does not ship.
- **MANDATORY tasks use the wording "must-do minimum"** in `overview.md` and `student-tasks.md`. Not "mandatory minimum", not "core minimum".
- **Every task that assumes a partner / follower / tester needs an `### If you are doing this alone` subsection** with a concrete alternative (24-hour gap, recording yourself on video, walking through it on a different device, posting in the class chat).
- **Every task's `### Keep your notes` block references AT2** (process description, end of Week 5 / during Week 6) — *not* AT1 (already submitted), *not* AT3 (Week 8, too far ahead).
- **Flowcharts in Markdown.** Prefer inline ASCII / Mermaid-style fenced code blocks for flowcharts in `self-study.md` and `slides.md`. Example pattern (Rasmus, feel free to refine the layout — what matters is the four shapes are visible):

  ```
  ( Start )
     |
     v
  [ Check if file name follows convention ]
     |
     v
  < Does it match? >
   /         \
  Yes         No
   |           |
   v           v
  [ Save it ] [ Rename it first ]
   |           |
   v           v
   ...        ...
  ```

  If Rasmus prefers Mermaid syntax in a fenced ` ```mermaid ... ``` ` block, that is also fine; Alfred renders Markdown only this round, so the Mermaid source ships as text and renders in viewers that support it. If neither is comfortable, a labelled list (e.g. *"Step 1 (rectangle) — Check the file name; Step 2 (diamond) — Does it match the convention? Yes → Step 3a; No → Step 3b"*) is also acceptable.
- **Central message verbatim.** *"Once you can decompose a problem, the next skill is to describe the process so someone else can run it — and to decide which details matter and which can be safely hidden."* Place this on at least one slide and in `self-study.md` (Introduction or Summary).

---

### File 1 — `student/week-03/overview.md` (200–400 words)

**Structure (in order):**
1. `## Week 3 theme` — one short paragraph naming the connection to Week 2 (you just finished AT1 by decomposing a problem; Week 3 asks how to *describe* the resulting process so someone else can run it) and the three lesson topics.
2. `## What you will be able to do by the end of the week` — bullet list of 5–7 plain-English "can do" statements, mapped to the L7–L9 objectives but in student-facing language ("draw a small flowchart with one decision point", "name what's hidden inside a 'Login' button", "spot a reused chunk and give it a name").
3. `## Must-do minimum vs. deepening` — clear two-column or two-bullet contrast. The words *must-do minimum* appear here.
4. `## How the three lessons fit together` — short paragraph showing the L7 → L8 → L9 arc (shape of a process → choose level of detail → name reusable chunks).

**Suggested examples to lean on:** route from home to school as a flowchart with one "is the tram running?" decision; the "Save" button as an abstraction; "register a new device" as a reusable block.

**Length target:** ~280 words.

---

### File 2 — `student/week-03/self-study.md` (2400–4000 words)

**Structure (in order):**

- `# <Week title>` — suggestion: *"Drawing the process — flowcharts, abstraction, and reusable blocks."* Rasmus may improve.
- `## Introduction` — opens with the Week 2 handoff: *you just finished AT1 by decomposing a problem; you have a list of subtasks; now what?* Then states the Week 3 central message **verbatim** at least once. Tells the student what the week will train.
- `## Lesson 7 — Describing a process and the simple flowchart`
  - `### When a list is not enough` — short scene (the morning routine works as a list; but as soon as "did I sleep through my alarm?" enters the picture, the list breaks). Pivot: a flowchart is what a list becomes when a process has branches.
  - `### The four shapes` — start/end (oval), step (rectangle), decision (diamond), arrow (flow). One sentence per shape; one tiny example flowchart drawn inline.
  - `### Reading a flowchart` — show a 6-shape flowchart for an everyday scene (e.g. "Should I bring an umbrella?"). Walk through the paths in plain English.
  - `### Drawing your first flowchart` — instructions for the student to draw a small flowchart for their own everyday process; references Task 3.1.
  - `### IT examples` — a help-desk triage flow ("can the user log in? Yes → close ticket; No → ask for screenshot"), a file-naming convention check.
  - 1–2 `> **Pause for a moment:**` reflection prompts.
- `## Lesson 8 — Abstraction`
  - `### What "abstraction" means here` — plain English definition: *hiding the detail that does not matter at the level you are describing*. Concrete first example: a bus stop. (A passenger sees "Park Street bus stop"; the bus dispatcher sees GPS coordinates and a schedule; the bus engineer sees an electrical junction box. Same physical thing, three abstractions.)
  - `### A "Login" button is an abstraction` — what is hidden? The password store, the cookie, the OAuth dance. The button works because the abstraction is right *for the user*. Concrete IT example.
  - `### Level of detail follows the audience` — emphasise: *who is reading this process?* A flowchart for a new help-desk hire needs different boxes than a flowchart for a senior IT admin.
  - `### Hiding vs. forgetting` — the conceptual pivot of the lesson. Hiding a detail means you know it is there and you have a place to find it; forgetting means it is gone. Brief everyday example.
  - 1–2 `> **Pause for a moment:**` reflection prompts.
- `## Lesson 9 — Reusable instructions: the idea of a function without code`
  - `### When the same chunk keeps reappearing` — show two example processes side by side (e.g. "first day at school" and "first day at a summer job") that both contain *"log in to the school portal"*. The same chunk, twice.
  - `### Give the chunk a name` — *"log the user in"*, *"rename the file"*, *"back up the device"*. A verb-phrase that says *what it does*, not *how it does it* (that is abstraction again).
  - `### What a "function" means in this week's sense` — define informally: *a named, reusable chunk of process, described in plain English, with a clear input and a clear output*. Show the same flowchart with the chunk drawn as one box.
  - `### Vocational example` — "register a new device" as one named block in a flowchart. Show the same flowchart without the named block (a tangle of 12 boxes) and with the named block (1 box, with a small note saying *"see the named-block description"*).
  - `### The trade-off in one sentence` — a named block hides detail (so readers at this level don't drown) but you must know where to look when you need the detail. Bridge: in Week 7 these named blocks become real JavaScript functions.
  - 1 `> **Pause for a moment:**` reflection prompt.
- `## Summary and what comes next` — closes the loop on the central message (state it verbatim again here if not in the Introduction). Previews Week 4 (alternative solutions and evaluation — *"more than one valid flowchart for the same process; how do you decide?"*).

**Examples menu Rasmus should pick from (use the everyday ones first):**
- Everyday: morning routine; "should I bring an umbrella?"; route from home to school; "should I wear the jacket or the hoodie?"; the bus-stop abstraction; making instant noodles (from Week 1) re-rendered as a flowchart.
- IT: help-desk triage flow (can the user log in?); file-naming convention check; "is the device on the school network?" before installing software; the "Login" button; the "register a new device" reusable block; the "reset a password" reusable block.

**Length target:** ~3200 words.

---

### File 3 — `student/week-03/student-tasks.md` (800–1800 words)

**Structure:**
- `## Overview of the week's tasks` — 3–5 sentences. State that 🟢 MANDATORY task(s) are the **must-do minimum** and 🟣 DEEPENING are optional extension. Remind that **AT2 — process description — is submitted at the end of Week 5 / during Week 6**, and that this week's notes (flowcharts, named reusable blocks, abstraction choices) are exactly what AT2 will reuse. **No mention of AT1** (already submitted).

**Five candidate task ideas for Rasmus (he ships 1–2 MANDATORY + 2–3 DEEPENING):**

**Task 3.1 — 🟢 MANDATORY — "Draw your first flowchart"** *(AI-resilient by construction — internal property, do not label)*
- The student picks one familiar everyday process they personally do that contains **at least one decision point** (e.g. "should I bring an umbrella today?", "should I take the bus or walk?", "which charger fits this device?", "should I save this file with the date in the name?").
- They draw a flowchart with **the four shapes** (start/end oval, step rectangle, decision diamond, arrow). Maximum 8 shapes. The flowchart is hand-drawn on paper (preferred) or on a tablet, and the student writes their **initials and the date** somewhere on the page.
- They take a photo of the drawing, paste it (or describe it in text if their notes are text-only) into their week notebook.
- In 3–5 sentences they answer: *what does the decision diamond ask? What two paths come out of it? What is the "end" state on each path?*
- **Why this is AI-resilient (internal note, do not write in the file):** the artefact is a dated, initialed hand-drawing of a process from the student's own life. An LLM cannot fake the drawing without the teacher being able to spot it.
- **No partner needed**, so **no "If you are doing this alone" subsection** required for this task.

**Task 3.2 — 🟢 MANDATORY candidate (alternative to 3.1) — "Read someone else's flowchart"**
- Rasmus provides 2 small flowcharts (one everyday — e.g. "should I bring an umbrella?", one vocational — e.g. help-desk triage). The student describes in plain English **what each flowchart does, what the decision point asks, and where each path ends**. Then they identify **one step in each flowchart that could be broken into smaller steps** (foreshadowing L8 / abstraction).
- *(Sune's recommendation: ship 3.1 as the MANDATORY and keep 3.2 as a DEEPENING — Task 3.1 produces a stronger artefact for AT2 prep. If Rasmus disagrees, ship 3.2 as MANDATORY and 3.1 as deepening; either single-MANDATORY choice satisfies the brief.)*

**Task 3.3 — 🟣 DEEPENING — "What's hidden inside the Login button?"**
- The student picks one button or menu item in software they actually use (the school portal's "Login", Discord's "Send", Spotify's "Play", their phone's "Take photo"). They list at least **5 things that are hidden inside that button** — what happens when you press it that you cannot see.
- Then they list **at least 2 things that are NOT hidden** (i.e. that the button still requires you to do or know — e.g. "you must already have a password").
- Reflection (3–5 sentences): *who is the audience of this abstraction — who decided what to hide and why?*
- **No partner needed.**

**Task 3.4 — 🟣 DEEPENING — "Spot the reused chunk"** *(pair task — needs an "If you are doing this alone" subsection)*
- Rasmus provides 2 vocational flowcharts that share at least one reusable chunk (e.g. both contain "log the user in" or both contain "verify the device is on the school network"). The student finds the shared chunk and **proposes a short verb-phrase name for it**.
- The student then takes one of their **own flowcharts from Task 3.1 or 3.2**, finds a chunk that might be reused in a *different* familiar process they do, and **draws that chunk as a single named box** in a redraw of the flowchart.
- **Pair step:** show the redraw to a classmate. Ask them what they think the named box does, without showing them the original details. If their answer matches the original, the name is good; if not, the name needs work.
- **`### If you are doing this alone`** — the student leaves the redraw for 24 hours and comes back with fresh eyes; or shows it in the class chat / course platform; or shows it to a family member who has never seen the original flowchart. The point is to test whether the verb-phrase carries the meaning on its own.

**Task 3.5 — 🟣 DEEPENING — "Rewrite a step at a lower level of detail"** *(may include LLM sparring-partner step)*
- The student picks one step from their Task 3.1 flowchart (e.g. *"Check the weather forecast"*) and rewrites it as a **mini-flowchart of 3–5 sub-steps** (e.g. *open the weather app → look at today's forecast → is rain probability > 50%? → yes → bring umbrella; no → don't bring umbrella*). They state in one sentence **which audience the lower-level version is for** (a younger sibling? a brand-new help-desk agent? a colleague at the same level?).
- **Optional sparring-partner step:** paste the two versions (the high-level step and the lower-level expansion) into an LLM with the supplied prompt and ask the LLM to challenge whether the lower-level version still describes the same thing. **Accept / modify / reject** each LLM suggestion in writing. Do not paste the LLM's answer back into the artefact. (Sample prompt in a fenced code block.)
- **No human partner needed** for this task — the LLM step is optional and is not a partner-substitute.

**Default selection Rasmus should ship:**
- 🟢 MANDATORY: **Task 3.1** (*Draw your first flowchart*) — strongest artefact for AT2 prep.
- 🟣 DEEPENING: **Task 3.3** (*What's hidden inside the Login button?*), **Task 3.4** (*Spot the reused chunk*), **Task 3.5** (*Rewrite a step at a lower level of detail*).
- Task 3.2 (*Read someone else's flowchart*) folds into the L7 in-class warm-up rather than shipping as its own task; Rasmus may include it as a fifth task only if he keeps the file under 1800 words.

**"If you are doing this alone" subsections required:** Task 3.4 (pair step). Task 3.1, 3.3, 3.5 do not assume a partner and do not need the subsection. Task 3.2, if shipped, does not assume a partner.

**Each task ends with `### Keep your notes`** referencing AT2 by name (process description, end of Week 5 / during Week 6).

**Length target:** ~1300 words.

---

### File 4 — `student/week-03/vocabulary.md` (10–18 terms)

**Required terms** (Rasmus may add 1–4 of their own, but must not skip any required ones):
1. Process
2. Flowchart
3. Start / end (oval)
4. Step (rectangle)
5. Decision (diamond)
6. Arrow / flow
7. Branch
8. Yes/No path (or "decision outcome")
9. Abstraction
10. Level of detail
11. Hidden detail
12. Audience (of a description)
13. Reusable block
14. Named block / function (Week 3 informal sense — explicitly flagged as "not a code function yet; a named chunk of process")
15. **Condition** — flagged as **"looking ahead — central topic of Week 5"** (alternatively: *parameter* flagged as Week 6 — Rasmus picks one).

Each definition is 1–3 sentences in plain English, with a short everyday or IT example where natural. Rasmus may add: *trade-off (in abstraction)*, *input to a function (informal)*, *output of a function (informal)*.

**Length target:** ~14 terms, ~700–900 words total.

---

### File 5 — `student/week-03/slides.md` (~12–18 slides)

**Recommended slide outline (~15 slides; Rasmus may adjust):**

1. `# Week 3 — Drawing the process` *(title slide)*
2. `## Where Week 2 left off` — one-bullet recap: you can decompose a problem into smaller subtasks; AT1 done.
3. `## The Week 3 central message` — body: the central message **verbatim**.
4. `## What this week trains` — 3-bullet preview of L7, L8, L9.
5. `## When a list is not enough` — show a list, then the same content with a branch; visual prompt.
6. `## The four shapes` — oval (start/end), rectangle (step), diamond (decision), arrow (flow). One small example flowchart on this slide or the next.
7. `## A flowchart for "should I bring an umbrella?"` — 6-shape example, inline.
8. `## Abstraction — hide the detail that does not matter` — short quotable definition.
9. `## A bus stop is an abstraction` — three audiences (passenger, dispatcher, engineer).
10. `## The "Login" button is an abstraction` — list 3–4 things hidden inside it.
11. `## Level of detail follows the audience` — short side-by-side: a help-desk new hire vs. a senior IT admin reading the same process.
12. `## Reusable instructions — give the chunk a name` — show two processes that both contain "log the user in"; draw the second one with the named box.
13. `## A function (Week 3 sense)` — a named, reusable chunk of process — described in plain English — with a clear input and a clear output. *Not code yet.*
14. `## Vocational example — "register a new device"` — one named block reused across a dozen processes.
15. `## Week 3 vocabulary at a glance` — 8–10 key terms in a single slide.
16. `## Must-do minimum vs. deepening` — two-column contrast.
17. `## Tasks this week` — 1 line per task, by number (3.1, 3.3, 3.4, 3.5).
18. `## What comes next: Week 4 — alternative solutions and evaluation` — preview.
19. `## Recap — the central message, one more time` — central message **verbatim** again (this satisfies criterion #22 even if slide 3 is skipped).

Aim ~15–18 slides. `---` on its own line between every slide. Body content: 3–5 short bullets or 1–2 short sentences.

---

### File 6 — `teacher/week-03/teacher-materials.md` (2400–4200 words)

**Required H2 sections (in order — Wilhelm checks the exact wording on these six headings):**

1. `## Week 3 learning objectives (mapped to Bloom)` — restate L7–L9 objectives from this plan, grouped by Bloom stage. Remembering + Understanding dominant; light Applying acceptable in all three lessons (draw a small flowchart; rewrite one step at a lower level of detail; name a reused chunk; draw a reused chunk as one box).
2. `## Common misconceptions for Week 3` — at least 6 across the week (2 per lesson). Suggested set:
   - **L7**: "A flowchart is just a list with boxes drawn around it." → Correction: a flowchart has *branches*; a list does not. The decision diamond is what a list cannot show. // "Flowcharts need special software." → Correction: paper, a pen and the four shapes are enough; the school's whiteboard works fine. (No drawing-tool homework will ever be set in this course.)
   - **L8**: "Abstraction means making it vague." → Correction: abstraction means **choosing what to leave out for this audience**; it is the opposite of vague — every box you do draw is precise *at that level of detail*. // "If I hide a detail, I have lost it." → Correction: hiding ≠ forgetting; you still know where to find it (the named block has its own description below). The detail is filed, not deleted.
   - **L9**: "A function in this week's sense is a piece of code." → Correction: in Week 3 a function is a named, reusable chunk of process — described in **plain English** — with a clear input and a clear output. Code arrives in Week 7. // "If I name a chunk, I have hidden everything important." → Correction: a good name carries the meaning ("log the user in" tells the reader exactly what to expect); a bad name hides too much ("do the thing" tells the reader nothing).
3. `## Lesson 7 — 90-minute plan` — table of time slots summing to 90, with an INDEPENDENT WORK block of **27–45 min** (30–50% rule). Suggested skeleton:
   - 0–10 min: warm-up — show a list that breaks (e.g. morning routine including "if alarm did not go off"); class points out where the list fails. Introduce the central message on the board.
   - 10–25 min: instructor input — the four shapes; read one prepared flowchart together ("should I bring an umbrella?"). Walk one path, then the other.
   - 25–55 min: **INDEPENDENT WORK** (30 min) — each student drafts their own first flowchart (start of Task 3.1) on paper, with at least one decision point. Hands and pens, no devices.
   - 55–75 min: pair activity — students swap flowcharts and **read each other's literally**. The receiver describes in one sentence what they think the flowchart does, without asking the writer. Writer notes the gap.
   - 75–85 min: whole-class debrief — collect 3–4 flowcharts on the document camera; class names which decision diamond was clearest.
   - 85–90 min: preview L8 — one sentence: *"Tomorrow we decide which boxes deserve to be drawn and which ones can be hidden."*
   - **Slide cues subsection** at the end (Rasmus drafts it; see slide map at top of this brief).
4. `## Lesson 8 — 90-minute plan` — same arithmetic constraint. Suggested:
   - 0–10 min: warm-up — three pictures on screen: a bus stop sign, a "Login" button, a file-naming convention (`2026-05-20_invoice-001.pdf`). Class names one thing hidden behind each.
   - 10–25 min: instructor input — define abstraction in plain English; the bus stop example with three audiences; *level of detail follows the audience*; the "hiding vs. forgetting" pivot.
   - 25–60 min: **INDEPENDENT WORK** (35 min) — each student takes a flowchart from L7 (their own or one Rasmus provides) and **rewrites one step at a lower level of detail** (i.e. opens one box into 2–4 sub-boxes). They write one sentence at the bottom: *"this lower-level version is for [audience]."*
   - 60–80 min: pair activity — *Activity B — Audience swap* from `in-class-tasks.md` (see below).
   - 80–88 min: whole-class debrief — which audiences came up most? Which lower-level versions felt right? Which felt over-engineered?
   - 88–90 min: preview L9.
   - **Slide cues subsection.**
5. `## Lesson 9 — 90-minute plan` — same arithmetic constraint. Suggested:
   - 0–10 min: warm-up — show two processes side by side that both contain *"log the user in"*. Class spots the shared chunk.
   - 10–25 min: instructor input — give the chunk a name; what a "function" means in this Week 3 informal sense; show "register a new device" as one named block reused in three different vocational flowcharts.
   - 25–55 min: **INDEPENDENT WORK** (30 min) — each student finds a reused chunk across their own Week 3 flowcharts (or, if they only have one, across their Week 2 AT1 decomposition) and **draws it as a single named box in a redrawn flowchart**.
   - 55–80 min: **MANDATORY teacher-led in-class activity** — *Activity A — Whiteboard flowchart relay* from `in-class-tasks.md` (see below).
   - 80–88 min: whole-class debrief — which verb-phrases worked? Which were too vague? Which were too specific?
   - 88–90 min: preview Week 4 in one line: *"Next week — when more than one flowchart reaches the same goal, how do you decide which is better?"*
   - **Slide cues subsection.**
6. `## Facilitation tips` — 4–6 bullets. Suggested: lead with the everyday example before the IT one; insist on the word *literal* (Week 1 framing); keep abstraction concrete (a bus stop, a Login button) and reject philosophy drift; protect independent work time against the temptation to lecture longer on flowchart shapes; use the board for redraws, not slides; if a student says "let me write code" remind them gently that code arrives in Week 7.
7. `## Answers to common student questions` — at least 5. Suggested: *"Do I need an app to draw flowcharts?" / "Is a 'function' here the same as in JavaScript?" / "Why are we hiding details — won't I need them later?" / "What if my flowchart has no decision points?" / "Can I draw a flowchart for my AT2?" / "Can I use ChatGPT to draw a flowchart?"*
8. `## Formative assessment tips` — 4–6 quick checks. Suggested: L7 exit ticket — *"name the four flowchart shapes and what each one means"*; L8 board vote — *"is 'open the fridge' an abstraction?"*; L9 sticky-note collection — each student writes one named block they spotted, posts it on the board. No summative assessment in Week 3.

**Cross-reference `in-class-tasks.md` from the L8 and L9 plans.** The activities below must be named identically in both files.

**Supplementary deck decision (per L7, L8, L9):**

- **L7 — `slides-l7-flowchart-walkthrough.md` recommended.** Lesson 7 introduces *four new shapes* and asks students to read a flowchart for the first time. The main deck carries the four-shapes overview and one inline example; a 5-slide supplementary deck can walk one fully-worked everyday flowchart (the "should I bring an umbrella?" example) shape by shape, with one shape revealed per slide. Suggested 5-slide sketch:
  - Slide 1: the starting oval, alone on the page, labelled *"Start."*
  - Slide 2: add the first rectangle, labelled *"Check the weather forecast."*
  - Slide 3: add the decision diamond, labelled *"Is rain probability > 50%?"* with two outgoing arrows labelled *Yes / No*.
  - Slide 4: add the two rectangles at the ends of the Yes/No arrows: *"Bring umbrella"* / *"Don't bring umbrella"*.
  - Slide 5: add the closing oval, labelled *"Leave the house."* Show the complete 6-shape flowchart.
  - Optional slide 6: re-render the same flowchart with a help-desk triage example overlaid, to make the vocational parallel concrete.
  - **Run this supplementary deck only if the class needs the shape-by-shape build; skip it if the live whiteboard build at 10–25 min lands well.**
- **L8 — no supplementary deck recommended.** The main deck's bus-stop and Login-button slides plus a live board sketch of "hiding vs. forgetting" are enough. If Rasmus *strongly* wants one, a 4-slide *"three audiences for a bus stop"* deck is acceptable; Sune's default is no.
- **L9 — no supplementary deck recommended.** The main deck slides 12–14 plus a live board demo of "register a new device" as one named block is enough.

**Length target:** ~3400 words.

---

### File 7 — `teacher/week-03/in-class-tasks.md` (400–1200 words)

**Structure:**
- `## Overview` — 2–3 sentences naming the activities and the 90-min slots they fit (L8 60–80 min for Activity B; L9 55–80 min for Activity A).
- At least 1 H2 task labelled **MANDATORY**.

**Two concrete activity ideas (Rasmus should ship both; the MANDATORY tag goes on Activity A):**

**Activity A — MANDATORY — "Whiteboard flowchart relay"** *(whole-class + teacher-led, ~25 min, slotted in L9 between 55–80 min)*
- Teacher prepares one vocational process on a board: *"A new student arrives — set them up with a school laptop."* The high-level flowchart is sketched with 8–10 boxes, several of which are mini-procedures that recur in other contexts (*"register the device on the school network"*, *"log the user in"*, *"install the standard software set"*).
- The class takes turns at the board: each volunteer identifies one chunk that could be a named, reusable block, **proposes a verb-phrase name**, and the teacher redraws that chunk as a single box on the right-hand side of the board.
- After 3–4 named blocks are drawn, the class compares the original 8–10 box flowchart with the new 4–5 box flowchart. Debrief: *what did we gain? what did we lose? where do the named blocks' details now live?*
- Closing: each student writes one verb-phrase on a sticky note — a named block from their own life (everyday or vocational). Teacher reads 3 aloud and asks the class whether the name carries the meaning.
- **Why it requires the classroom:** the relay-at-the-board format, the live redraw, and the collective name-checking are the whole point. It cannot be done as homework.

**Activity B — OPTIONAL — "Audience swap (pair work)"** *(pair, ~20 min, slotted in L8 between 60–80 min)*
- Pair A and Pair B each receive the same one-step flowchart box: *"Check the file naming convention."* Pair A is told their audience is *"a brand-new IT trainee on day one"*. Pair B is told their audience is *"a senior IT admin who already knows the convention by heart"*.
- Each pair rewrites the single box as a mini-flowchart for their audience: Pair A's version will likely have 4–6 sub-steps; Pair B's may have 0–2 (or *"already done"* as the only sub-step).
- Pairs swap and read each other's mini-flowcharts. Debrief in pairs: *was the right level of detail chosen for each audience?*
- This activity makes the L8 abstraction lecture physical without requiring a teacher-led whole-class moment.

Cross-reference back to `teacher-materials.md` so the teacher knows the exact 90-min slot for each. Activity A is referenced from the L9 plan; Activity B is referenced from the L8 plan.

**Length target:** ~700–900 words.

---

## Avoimet kysymykset

1. **Number of MANDATORY tasks.** The brief says 1–2 MANDATORY. **Default assumption:** Rasmus ships **one** MANDATORY task (Task 3.1 — *Draw your first flowchart*), plus three DEEPENING tasks. Two MANDATORY tasks are also acceptable if Rasmus prefers (e.g. add 3.2 as MANDATORY); Wilhelm accepts either 1 or 2.
2. **Flowchart encoding in Markdown.** ASCII art vs. Mermaid vs. labelled lists. Alfred renders Markdown only this run; no PPTX. **Default assumption:** Rasmus uses ASCII art inside fenced code blocks for all flowcharts in `self-study.md` and `slides.md`, because it renders identically in every viewer. Mermaid blocks are acceptable as an addition (their source is human-readable even un-rendered), but ASCII is the primary encoding.
3. **Supplementary deck for L7.** Sune recommends `slides-l7-flowchart-walkthrough.md` (5 slides). **Default assumption:** Rasmus ships it. If Rasmus decides the main deck's slides 5–7 already carry the shape-by-shape build, he may skip; Wilhelm accepts 0–2 supplementary decks.
4. **`media/` subfolder.** Hand-drawn flowchart photos for Task 3.1 are student artefacts, not Rasmus's job. **Default assumption:** no `media/` folder in the Rasmus output; if a slide needs an image, Rasmus may add one PNG and reference it from one slide, but is not required to.
5. **Preview term in `vocabulary.md`.** Two reasonable candidates: *condition* (Week 5) or *parameter* (Week 6). **Default assumption:** Rasmus picks *condition* (it is the natural Week 5 follow-on from the L7 decision diamond) and flags it explicitly as *"looking ahead — central topic of Week 5"*.
6. **AT2 wording in `### Keep your notes` blocks.** The course plan has AT2 at end of Week 5 / during Week 6. **Default assumption:** Rasmus writes *"AT2 — process description — is submitted at the end of Week 5 / during Week 6, and the flowchart vocabulary you build here is exactly what AT2 expects."* Verbatim or near-verbatim across the four tasks.
7. **Whether 30–50% independent work needs to be one contiguous block.** Same answer as Week 1. **Default assumption:** Wilhelm accepts either a single block or up to two blocks both labelled INDEPENDENT WORK that together sum to 27–45 min.
8. **In-class Activity A length.** 25 min slotted; the slot in L9 is 55–80 (25 min). **Default assumption:** if Rasmus's draft of Activity A runs longer, he tightens the closing sticky-note step; if shorter, he expands the *"compare original vs. redrawn flowchart"* debrief. The 55–80 min window is the constraint.
9. **Bloom verbs for L9's "draw a reused chunk as one box".** This is light Applying. **Default assumption:** Wilhelm accepts *draw*, *redraw*, *box*, *name* as light-Applying verbs in Week 3, in line with the brief's *"students draw simple flowcharts and identify reusable blocks"*. *Refactor* / *abstract* (as a verb) / *decompose* are forbidden in Week 3 objectives (decompose was Week 2; the others are too high on Bloom).
10. **Whether `overview.md` should preview Week 4.** Following Week 1's pattern. **Default assumption:** `overview.md` does *not* preview Week 4 (it is a within-week document); only `self-study.md` previews Week 4.
