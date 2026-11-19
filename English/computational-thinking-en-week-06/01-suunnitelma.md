# Computational Thinking — Week 6 Plan (Sune, Gate #1)

Course: Computational Thinking (English)
Target: First-year vocational ICT students, ~15–17, no prior programming language
Duration: 8 weeks x 3 lessons/week x 90 min = 24 lessons
Pipeline scope this run: Sune produces this Week 6 plan; Rasmus builds the full Week 6 package in the canonical weekly structure; Linnea/Wilhelm audit Week 6; Alfred packages a Markdown-only Week 6 release (no PDF, no PPTX rendering this round).

The 24-lesson topic table, Bloom mapping and AT placement are inherited verbatim from the locked course plan at `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/01-suunnitelma.md`. This file specifies Week 6 only.

---

## Suunnitelma

### Week 6 theme statement

Week 6 is the **synthesis week of the computational-thinking half of the course**. Everything the student has practised in plain English — clear sequence (Weeks 1–2), abstraction and process description (Weeks 3–4), conditions and repetition (Week 5) — is folded into a single more precise notation: **pseudocode**. The week's central message is that pseudocode is the bridge between everyday English and real code: precise enough for a computer to follow if it had to, readable enough to share with a non-programmer. No real programming language appears this week. Week 6 closes by training the most under-practised skill of beginning programmers: **reading code on paper and predicting what it will do**, line by line, with a trace table. **AT2 is submitted around Lesson 18**, drawing directly on the pseudocode and dry-run work of L16–L18. Real code (JavaScript) arrives in Week 7.

### Week 6 central message (one sentence)

Pseudocode is the bridge between everyday English and real code: precise enough for a computer to follow if it had to, readable enough to share with a non-programmer.

### L16–L18 breakdown for Week 6

#### Lesson 16 — Pseudocode: from natural language to a more precise format

- **Learning objectives** (Understanding + Applying):
  - (a) **Define** pseudocode in own words, and contrast it with everyday English and with a real programming language. *(Understanding)*
  - (b) **Identify** the three building blocks already met in earlier weeks — sequence, condition, repetition — inside a short piece of pseudocode. *(Understanding)*
  - (c) **Write** a short piece of pseudocode (10–20 lines) for a familiar process, using a small fixed set of keywords (`SET`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`, `READ`, `WRITE`). *(Applying)*
  - (d) **Explain** why pseudocode is more reliable to share than English prose for an instruction a computer will eventually execute. *(Understanding)*
- **Key vocabulary preview:** pseudocode, keyword, indentation (informal), block, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`; preview term *variable*.
- **Central message:** Pseudocode is not a new language to memorise — it is the things you already write, with a few shared words and a fixed shape so a stranger can read it the same way you do.

#### Lesson 17 — Input, processing, output, and the idea of a variable

- **Learning objectives** (Understanding + Applying):
  - (a) **Describe** the input → processing → output pattern of a piece of pseudocode. *(Understanding)*
  - (b) **Define** *variable* in own words: a named container for one value that can change while the pseudocode runs. *(Understanding)*
  - (c) **Use** `SET variableName TO value`, `READ variableName`, and `WRITE variableName` correctly in pseudocode. *(Applying)*
  - (d) **Recognise** that the *name* of a variable should describe what it holds, and that bad names make pseudocode hard to read. *(Understanding)*
- **Key vocabulary preview:** variable, value, name (of a variable), assignment, input, processing, output; revisit *sequence*, *condition*, *repetition* from Week 5.
- **Central message:** A pseudocode program is almost always a small machine that takes input, does something with it, and produces output — and a variable is the place where it keeps the things it needs to remember while it runs.

#### Lesson 18 — Testing pseudocode: dry running and finding errors (AT2 submitted around this lesson)

- **Learning objectives** (Understanding + Applying):
  - (a) **Explain** what a trace table is and why dry-running on paper finds bugs that re-reading does not. *(Understanding)*
  - (b) **Dry-run** a short piece of pseudocode line by line using a trace table, updating the value of each variable at each step. *(Applying)*
  - (c) **Find** at least one bug in a deliberately broken piece of pseudocode by dry-running it. *(Applying)*
  - (d) **Fix** the bug and dry-run the corrected pseudocode to confirm the expected output. *(Applying)*
- **Key vocabulary preview:** dry run, trace table, bug, off-by-one (informal), expected output, actual output; preview term *console* for Week 7.
- **Central message:** Pseudocode is not finished when it looks right; it is finished when a trace table proves it produces the expected output, including on at least one awkward input.

### Week 6 — must-do minimum vs. deepening

**Must-do minimum (every student must leave Week 6 able to):**
- Define pseudocode, variable, dry run, trace table, bug in plain English.
- Read a short pseudocode snippet (about 10–15 lines, with at least one condition and one repetition) and say what it does.
- Write a piece of pseudocode (10–20 lines) for a familiar process, using `SET`, `IF/ELSE/ENDIF` and either `WHILE/ENDWHILE` or `FOR/ENDFOR` at least once each.
- Dry-run a piece of pseudocode with a trace table, updating each variable line by line.
- Find a bug in given pseudocode by dry-running it, and fix the bug.

**Deepening (optional extension, but recommended because AT2 lands this week):**
- Take a piece of pseudocode written by a classmate (or your past self) and trace it without first asking what it does, then compare.
- Write pseudocode for a small vocational scenario: a help-desk reply triage, a password-strength check, a daily backup routine. Trace it on one normal input and one awkward input.
- Identify the **type** of bug you found by dry-running — off-by-one, wrong comparison, missing initialisation, wrong branch — in plain English.
- Add one *edge case* to a given pseudocode (empty input, negative number, zero) and trace what happens.

### How L16, L17 and L18 fit together

The three lessons are deliberately ordered as a single arc. L16 introduces pseudocode as a notation that bundles together everything Weeks 1–5 already practised. L17 narrows the lens onto the most useful new idea inside that notation — the variable, and the input/processing/output skeleton most pseudocode follows. L18 zooms out again and trains the skill that makes pseudocode actually useful: dry-running it on paper to find and fix bugs. **AT2 is submitted around L18**, asking the student to write a short piece of pseudocode for a small vocational task, dry-run it, and explain in plain English what each part does and where any bugs were caught.

### Forward-looking note for Week 7

Week 7 is the first week with real code. The L16 keywords (`SET`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`, `READ`, `WRITE`) map cleanly onto JavaScript primitives (`let x = ...`, `if/else`, `while`, `for`, prompt/console.log) in Week 7. Rasmus should choose pseudocode keywords that *make this jump easy* without ever naming JavaScript in Week 6.

---

## Rajaukset

**Out of scope for Week 6:**
- **Absolutely no JavaScript, no Python, no C#, no Java, no real programming language anywhere.** Pseudocode only. This is the hardest hard rule of the week. Wilhelm greps for `console.log`, `let `, `function `, `def `, `var `, `print(`, `js`, `javascript` and fails the audit on a hit.
- **No automatic testing or debugging frameworks** (jest, mocha, vitest, pytest, etc.). "Testing" in Week 6 means **dry-running on paper with a trace table**, full stop.
- **No flowcharts as a new topic.** Flowcharts were Week 3. They may appear as a one-line reference back to Week 3 if Rasmus wants, but no new flowchart notation is taught this week.
- **No object-oriented thinking, no functions-with-parameters as a formal topic, no data structures beyond a single variable holding a number, a string, or a yes/no.** Lists/arrays may appear at most once, casually, in a `FOR each x in list` example — but they are not a learning objective.
- **No big-O, no Turing machines, no compiler/interpreter theory.**
- **No IDE setup, no Node.js install, no browser console.** Week 6 needs paper and pen.
- **No graded essays.** AT2 is artefact + short reflection; the artefact is pseudocode plus a trace table.
- **No PowerPoint creation directly.** Rasmus writes `slides.md` (Markdown only). No PDF, no PPTX in this round — Alfred packages Markdown only.
- **No slide deck files beyond `slides.md` and at most one optional `slides-l<n>-*.md` per lesson** where genuinely needed. Default expectation for Week 6: **one optional supplementary deck for L16** (a worked pseudocode walkthrough) is strongly recommended; L17 and L18 do not need supplementary decks.
- **No `media/` folder** unless a slide explicitly references an image. Week 6 should not need any images; ASCII or Markdown tables are enough for trace tables.
- **No use of the internal label "AI-resilient"** in any of the seven learner-facing files. Rasmus designs tasks to be AI-resilient by construction; Linnea audits the property, not the label.

**Language and pipeline:**
- English throughout. Börje (Finnish polishing) is skipped for this run.
- The H2 headings in *this plan file* may remain in Finnish (`Suunnitelma`, `Rajaukset`, `Hyväksymiskriteerit`, `Briefing Rasmukselle`, `Avoimet kysymykset`) because they are part of the Sune template; **all seven of Rasmus's Week 6 files must be fully English**, including their section headings.

---

## Hyväksymiskriteerit

Wilhelm verifies the Week 6 package against the following concrete, checkable criteria.

### Structural — files and folders

1. **All 7 canonical files present**, with exactly these filenames (case-sensitive, lowercase, kebab-case):
   - `student/week-06/overview.md`
   - `student/week-06/self-study.md`
   - `student/week-06/student-tasks.md`
   - `student/week-06/vocabulary.md`
   - `student/week-06/slides.md`
   - `teacher/week-06/teacher-materials.md`
   - `teacher/week-06/in-class-tasks.md`
2. **Supplementary deck allowed:** one optional `student/week-06/slides-l16-pseudocode-walkthrough.md` (4–8 slides). No other supplementary decks expected. If Rasmus ships an L17 or L18 supplementary deck, Wilhelm accepts it as long as it is 4–8 short slides and is referenced from `teacher-materials.md`.
3. **No extra files** in `student/week-06/` or `teacher/week-06/`. No `.pptx`, no `.key`, no Reveal.js HTML, no PDF. Hard fail if found. A `media/` subfolder is allowed only if a slide or self-study explicitly references a contained image.

### Volume (sanity-check brackets, not hard limits)

4. `overview.md`: **200–400 words**. One section per area in #11 below.
5. `self-study.md`: **2400–4000 words** (≈3× a golden-sample single lesson; this file covers L16, L17, L18).
6. `student-tasks.md`: **900–2000 words** total. **1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING** tasks (see #14, #24).
7. `vocabulary.md`: **10–18 terms**, each with a 1–3 sentence English definition. At least one term flagged as "looking ahead" to Week 7 (suggested: *console*).
8. `slides.md` (main deck): **~12–20 slides**, separated by `---` on their own line, each slide starting with H1 (`#`) or H2 (`##`) and containing minimal supporting content (3–5 short bullets or 1–2 short sentences). Aim ~15–18.
9. `slides-l16-pseudocode-walkthrough.md` (supplementary deck, if shipped): **4–8 slides** walking one concrete pseudocode example end-to-end.
10. `teacher-materials.md`: **2600–4400 words**. Contains **3 × 90-minute lesson plans** (one per lesson), each with time slots summing to 90. Plus required H2s in #16.
11. `in-class-tasks.md`: **500–1400 words**. Contains **at least 1 MANDATORY teacher-led in-class exercise** that genuinely requires classroom interaction.

### Required H2 sections per file

12. `overview.md` must contain (in this order):
    - `## Week 6 theme`
    - `## What you will be able to do by the end of the week`
    - `## Must-do minimum vs. deepening` (the words **must-do minimum** are required; "mandatory minimum" is wrong)
    - `## How the three lessons fit together`
13. `self-study.md` must contain:
    - `# <Week title>` (suggestion: *"From thinking to code — meet pseudocode"*; Rasmus may improve).
    - `## Introduction` — re-states the course's central question and names this week's central message verbatim.
    - `## Lesson 16 — Pseudocode: from natural language to a more precise format` (or close variant).
    - `## Lesson 17 — Input, processing, output, and the idea of a variable`
    - `## Lesson 18 — Testing pseudocode: dry running and finding errors`
    - `## Summary and what comes next` (previews Week 7 — first JavaScript — without naming JavaScript syntax in detail).
    - **At least 4 `> **Pause for a moment:**` reflection prompts** across the three lessons (≥1 per lesson; aim 5–6).
14. `student-tasks.md` must contain:
    - `## Overview of the week's tasks` — names that **AT2 is submitted around L18** and that this week's tasks feed directly into AT2.
    - One H2 per task, prefixed with `🟢 MANDATORY —` or `🟣 DEEPENING —`. Wording **must use "must-do minimum"**, not "mandatory minimum".
    - Each task ends with a `### Keep your notes` block reminding the student that **AT2 lands around L18 of this week** (not AT1).
    - For any task that assumes a partner / follower / tester / classmate, a **`### If you are doing this alone`** subsection with a concrete alternative (24-hour gap, video self, different device, class chat).
15. `vocabulary.md` must contain a single H2 `## Week 6 vocabulary`, then each term as an H3 or as a bolded term in a definition list. At least one term flagged as a **"looking ahead"** preview (suggested: *console*, *expression*, or *return value* — anything used in Week 7).
16. `slides.md` must:
    - Start with a title slide.
    - Contain at least one slide whose body shows **the course's central question verbatim**: *How do I speak to a computer so that it understands what I want it to do?*
    - Use `---` on its own line between slides.
    - Have **no embedded `.pptx` references** and no speaker-note syntax that assumes a specific renderer.
    - Reference Week 6's central message ("Pseudocode is the bridge between everyday English and real code…") on at least one slide.
17. `teacher-materials.md` must contain (verbatim H2 wording):
    - `## Week 6 learning objectives (mapped to Bloom)`
    - `## Common misconceptions for Week 6` — **at least 6 across the week** (≥2 per lesson), each with a "**Correction:**" line.
    - `## Lesson 16 — 90-minute plan`
    - `## Lesson 17 — 90-minute plan`
    - `## Lesson 18 — 90-minute plan`
    - `## Facilitation tips`
    - `## Answers to common student questions` — at least 5 across the week.
    - `## Formative assessment tips`
    - Each 90-min plan has **concrete time slots summing to 90**, allocates **30–50% to independent student work** (see #19), and includes a **Slide cues** block referencing slide numbers in `slides.md` (and the supplementary deck if Rasmus ships one).
18. `in-class-tasks.md` must contain:
    - `## Overview`
    - At least 1 H2 task labelled **MANDATORY**, requiring teacher-led classroom interaction.
    - The MANDATORY activity must be cross-referenced from `teacher-materials.md` so the teacher knows the exact 90-min slot.

### Pedagogical rules

19. **30–50% rule**: in `teacher-materials.md`, for each of the three 90-minute lesson plans, the time blocks visibly labelled as *independent student work* sum to **27–45 minutes** out of 90. Wilhelm checks the time slots arithmetically.
20. **Bloom cap**: Week 6 learning objectives use only **Understanding + Applying** verbs (define, describe, explain, identify, recognise, use, write, dry-run, find, fix). **Forbidden verbs** in Week 6 objectives: *evaluate, judge, design, create, build, develop, abstract, decompose* (those belong to Weeks 4 and 8). Light Analysing may appear in DEEPENING tasks only (identify the type of bug), never as a primary objective.
21. **Central question** of the course — *How do I speak to a computer so that it understands what I want it to do?* — appears verbatim on **at least one slide** in `slides.md`. (Self-study mentions it but does not need to be verbatim a second time; the verbatim slide is the audit anchor.)
22. **Week 6 central message** — *"Pseudocode is the bridge between everyday English and real code: precise enough for a computer to follow if it had to, readable enough to share with a non-programmer."* — appears verbatim or near-verbatim in `self-study.md`'s introduction and on at least one slide.
23. **Examples-first principle**: in `self-study.md`, every conceptual section that uses both kinds of examples places the **everyday example before the IT example**. Wilhelm spot-checks the three lesson sections. (Vocational angle examples — help-desk triage, password check, backup routine — count as IT.)
24. **No real programming language anywhere.** Wilhelm greps for `console.log`, `let `, `var `, `const `, `function `, `def `, `print(`, `system.out`, `int main`, `<script`, `.js`, `JavaScript`, `Python`, `Java`, `C#`. **Hard fail on any hit** in any of the seven Week 6 files (and the supplementary deck if shipped). Pseudocode keywords (`SET`, `IF`, `ELSE`, `ENDIF`, `WHILE`, `ENDWHILE`, `FOR`, `ENDFOR`, `READ`, `WRITE`) are obviously allowed.
25. **No automatic testing frameworks mentioned anywhere** (jest, mocha, vitest, pytest, junit).
26. **"Must-do minimum" wording**: the phrase **must-do minimum** is used (not "mandatory minimum", not "core minimum") in `overview.md` and `student-tasks.md`. Wilhelm greps.
27. **"AI-resilient" label** must not appear in any of the seven learner-facing files. The property is enforced; the internal label is not exposed.
28. **AT framing in tasks**: every task's `### Keep your notes` block names **AT2 around L18 of this week** (not AT1, not AT3). Wilhelm greps.

### Tasks (AI resilience by construction)

29. `student-tasks.md` contains **1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING** tasks. **At least one MANDATORY task is AI-resilient by construction** — i.e. it requires the student's own concrete context (a real familiar process they personally do), an observable artefact (their own pseudocode on paper, their own trace table, their own list of bugs found), or a critique-the-LLM mechanism.
30. **One MANDATORY task must be:** "Write pseudocode for a familiar process you personally do, with at least one condition and one repetition, then dry-run it on paper with a trace table." This is the spine of AT2 readiness. Rasmus picks the exact wording.
31. If a DEEPENING task uses an LLM as a sparring partner, it must include a fenced code block with a sample prompt and explicit instruction not to accept the LLM's output verbatim. (Same rule as Week 1.)
32. Any task assuming a partner / follower / tester contains a **`### If you are doing this alone`** subsection.

### In-class tasks

33. `in-class-tasks.md` contains **at least 1 MANDATORY teacher-led in-class exercise** that genuinely requires classroom interaction. Strong default: a **"dry-run as a class"** exercise where the teacher writes a short piece of pseudocode on the board and the class collectively acts as the trace table (one student per variable, calling out updates line by line).
34. The MANDATORY activity is cross-referenced from `teacher-materials.md` with a specific time slot.

### Language and polish

35. **English throughout**. No Finnish words in any of the 7 (or 8 with supplementary deck) files except clearly necessary proper nouns.
36. **Register**: `self-study.md`, `student-tasks.md`, `overview.md`, `vocabulary.md`, `slides.md` and any supplementary deck at CEFR ~B1; `teacher-materials.md` and `in-class-tasks.md` at CEFR ~B2.
37. **Valid Markdown**: every code fence closes, every table renders, no broken internal links, `---` separators in slide files are alone on their own line.

---

## Briefing Rasmukselle

### Cross-cutting reminders (apply to all 7 files)

- **Everyday before IT, always.** When introducing any new idea, lead with a familiar 15-year-old scene (laundry, charging a phone, making tea, checking the bus app, sending a Discord reply) and only then pivot to a vocational IT example (help-desk reply triage, password-strength check, daily backup routine).
- **No real programming language anywhere.** Pseudocode only. No `console.log`, no `let`, no `function`, no `var`, no Python, no JavaScript by name. Even the phrase "this is just like JavaScript" is forbidden — Week 7 is one week away and earns the comparison itself.
- **No testing frameworks.** "Testing" = dry-running on paper with a trace table.
- **Use one consistent pseudocode dialect across all seven files.** Recommended fixed keyword set: `SET name TO value` · `READ name` · `WRITE expression` · `IF condition THEN … ELSE … ENDIF` · `WHILE condition DO … ENDWHILE` · `FOR each x IN list DO … ENDFOR` (lists optional). Indent block bodies by 2 spaces inside fenced code blocks marked ` ```text `. Do **not** use ` ```js ` or any language tag that suggests a real language.
- **AT framing.** Every `### Keep your notes` block names **AT2 around L18 of this week**. Not AT1, not AT3.
- **"Must-do minimum"** (not "mandatory minimum", not "core minimum"). Use exactly this phrase in `overview.md` and `student-tasks.md`.
- **"AI-resilient" label** does not appear in learner-facing files; Linnea audits the property.
- **Central question** of the course appears verbatim on at least one slide.
- **Week 6 central message** appears verbatim or near-verbatim in `self-study.md`'s Introduction and on at least one slide: *"Pseudocode is the bridge between everyday English and real code: precise enough for a computer to follow if it had to, readable enough to share with a non-programmer."*

---

### File 1 — `student/week-06/overview.md` (200–400 words)

**Required H2 structure (in order):**
1. `## Week 6 theme` — one short paragraph naming the week's central message and the three lesson topics (L16 pseudocode, L17 variable + input/processing/output, L18 dry-run + trace table). Also names that **AT2 is submitted around L18**.
2. `## What you will be able to do by the end of the week` — bullet list of 6–8 plain-English "can do" statements mapped to L16–L18 objectives.
3. `## Must-do minimum vs. deepening` — two-bullet-list contrast. The phrase **must-do minimum** is required.
4. `## How the three lessons fit together` — one short paragraph showing the arc L16 (notation) → L17 (variables + I/P/O skeleton) → L18 (dry-run + bug fix) → AT2.

**Examples to lean on:** making tea with `IF` (sugar or not) and `WHILE` (until the kettle clicks); a password-strength check; a help-desk triage that branches on the type of ticket. Everyday first.

**Length target:** 250–320 words is the sweet spot.

---

### File 2 — `student/week-06/self-study.md` (2400–4000 words)

**Required structure (in order):**

- `# <Week title>` — suggestion: *"From thinking to code — meet pseudocode"*. Rasmus may improve.
- `## Introduction` — opens with a familiar scene (laundry: *"if the basket has darks, do a darks load; otherwise check whites"*). Re-states the course's central question. States the **Week 6 central message verbatim**. Tells the student that AT2 lands this week (around L18).
- `## Lesson 16 — Pseudocode: from natural language to a more precise format`
  - `### From English to pseudocode` — show one everyday process in English (4–5 sentences). Then the same process in pseudocode (10–14 lines). Side-by-side commentary: what got more precise, what got shorter, what stayed the same.
  - `### The small set of keywords` — introduce `SET`, `READ`, `WRITE`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`. One short pseudocode snippet per keyword, with one line of English next to it. Keep this section visually clean — students should be able to use it as a reference card.
  - `### Sequence, condition, repetition — meet again` — one short paragraph reminding the student that Week 5's sequence/condition/repetition are exactly the three things pseudocode encodes.
  - `### Why pseudocode is more reliable to share than English prose` — the conceptual pivot. Brief.
  - 1–2 `> **Pause for a moment:**` reflection prompts.
- `## Lesson 17 — Input, processing, output, and the idea of a variable`
  - `### Input → processing → output` — name the three-part skeleton. Show one short pseudocode example (e.g. ask for a number, compute its double, write the result).
  - `### What is a variable?` — short definition: a named container for one value that can change while the pseudocode runs. Everyday metaphor first (a labelled box on a shelf, a sticky note on a jar), then pseudocode example with `SET`.
  - `### A variable name should describe what it holds` — contrast `SET x TO 7` with `SET passwordLength TO 7`. Why the second is easier to read.
  - `### A vocational example` — a password-strength check in pseudocode (read a password, count its length, set `isStrong` to YES if length ≥ 8 AND it contains a digit, otherwise NO; write the result). Use this same example again in `slides.md`.
  - 1–2 `> **Pause for a moment:**` reflection prompts.
- `## Lesson 18 — Testing pseudocode: dry running and finding errors`
  - `### What is a dry run?` — short definition. Compare to Week 1's "literal robot": the dry-run is the student playing literal robot on their own pseudocode, on paper.
  - `### The trace table` — show a worked example. Use Markdown table syntax: columns = line number, each variable, output. Walk a 6–8-line pseudocode snippet through 5–7 rows. Highlight the moment a variable changes.
  - `### Finding a bug` — give a deliberately broken short pseudocode (suggested: an off-by-one in a `WHILE` condition, or a `<` that should be `<=`). Trace it; the trace shows the actual output differs from the expected output; identify the line and fix it.
  - `### Edge cases on paper` — one paragraph: empty input, zero, a negative number. The trace catches what the eye misses.
  - `### About AT2` — short, calm paragraph: AT2 is submitted around this lesson; it asks the student to write a short piece of pseudocode for a small vocational task and dry-run it with a trace table. The work of L16–L18 IS the AT2 raw material. No new tools, no new notation.
  - 1 `> **Pause for a moment:**` reflection prompt.
- `## Summary and what comes next` — closes the loop: pseudocode is the bridge to real code, which arrives in Week 7. Preview Week 7 in one sentence ("Next week the same pseudocode shape becomes a tiny program in a real language you run in a browser"), without naming JavaScript syntax in detail.

**Examples menu Rasmus should pick from (everyday first, then vocational):**

- Everyday: making tea (`IF` sugar, `WHILE` kettle not clicked), brushing teeth as a `FOR each tooth-region`, the morning alarm-snooze loop, checking a chat for unread messages.
- Vocational: help-desk ticket triage (`IF` ticket has the word "password" THEN route to support tier 1, ELSE IF it has "outage" THEN tier 2, ELSE tier 3); password-strength check; daily backup routine (`FOR each folder in backupList`); duplicate-file detector (`FOR each file`, count by name).

**Length target:** 2800–3400 words.

---

### File 3 — `student/week-06/student-tasks.md` (900–2000 words)

**Required structure:**
- `## Overview of the week's tasks` — 3–5 sentences. State that 🟢 MANDATORY tasks are the **must-do minimum** and 🟣 DEEPENING are optional extensions. **Name that AT2 is submitted around L18 of this week** and that the tasks below feed directly into AT2.

**Five candidate tasks for Rasmus to pick from (Rasmus keeps 1–2 MANDATORY + 2–3 DEEPENING). Default selection at the end.**

**Task 6.1 — 🟢 MANDATORY — "Pseudocode a familiar process"** *(AI-resilient by construction)*
- Student picks one process they personally do almost every day (making tea, checking their morning notifications, packing a bag for school, charging a phone overnight, sending a routine Discord message). It must be a process the student really does — not a textbook example.
- Student writes the process in **pseudocode** (10–20 lines) using `SET`, `IF/ELSE/ENDIF`, and at least one of `WHILE/ENDWHILE` or `FOR/ENDFOR`. **At least one condition AND at least one repetition are required.**
- Student dry-runs the pseudocode on paper with a trace table for **one normal input** (a typical day) and **one awkward input** (something missing, something extra).
- Reflection (3–5 sentences): what was harder to express in pseudocode than in English? What was easier?
- **Why AI-resilient:** anchored in the student's own real routine. An LLM cannot fake the awkward-input case for *your* morning without exposing itself. The trace table is also an observable artefact a teacher can compare to the pseudocode.
- **No `### If you are doing this alone` section needed** — this task does not assume a partner.

**Task 6.2 — 🟢 MANDATORY (alternative candidate to 6.1) — "Vocational pseudocode + dry run"** *(AI-resilient by vocational anchor)*
- Student picks one small vocational scenario from a fixed list: **help-desk ticket triage**, **password-strength check**, or **daily backup routine**. They write 12–20 lines of pseudocode and dry-run it on a trace table for two inputs.
- Suggested default: keep **Task 6.1** as the MANDATORY task (everyday anchor is more accessible for L16/L17) and use 6.2 as a DEEPENING.

**Task 6.3 — 🟣 DEEPENING — "Find the bug"** *(AI-resilient; observable artefact)*
- Rasmus writes a short broken pseudocode snippet (8–14 lines) with exactly one bug. Suggested bug: a `WHILE counter < 5` when it should be `<= 5`, or a wrong-branch `IF` (an `ELSE` block reachable when it shouldn't be), or a missing `SET total TO 0` before a loop.
- Student dry-runs it with a trace table, identifies the bug, fixes it, and re-traces the fixed version.
- Student writes one short paragraph in plain English: what type of bug it was (off-by-one, wrong comparison, missing initialisation, wrong branch). This is the only place "type of bug" naming is required in the week.

**Task 6.4 — 🟣 DEEPENING — "Trace a classmate's pseudocode"** *(partner-assumed → needs `### If you are doing this alone`)*
- Student swaps pseudocode with a classmate (a snippet of 10–15 lines, ideally from Task 6.1). **Without first asking what it does**, they dry-run it on a trace table and write a one-sentence guess at the goal.
- They then compare with the writer: did the trace produce the expected output? Was the goal guessable from the steps?
- `### If you are doing this alone` — the alternative is: trace your **own** pseudocode from a previous week (Week 5 has logic-structure exercises that can be re-encoded) with a 24-hour gap, OR exchange via the class chat, OR trace a piece you wrote on your phone and traced on paper a day later.

**Task 6.5 — 🟣 DEEPENING — "LLM as sparring partner against your own dry run"** *(critique-the-LLM mechanism)*
- Student has dry-run their own pseudocode from Task 6.1. They now paste the pseudocode (not the trace) into an LLM with the supplied prompt and ask the LLM to predict the trace for the same awkward input.
- Student compares the LLM's predicted trace with their own. They write a short paragraph: where the LLM disagreed, who was right (justified by re-tracing), and what the disagreement reveals about either their pseudocode or the LLM's reading.
- Fenced sample prompt provided, with explicit "do not accept the LLM's trace as the truth" line.

**Default selection Rasmus should ship:**
- 🟢 MANDATORY: **Task 6.1** (*Pseudocode a familiar process*). The "write pseudocode for a familiar process with a condition and a repetition, then dry-run on paper" task is the locked spine of the week.
- 🟣 DEEPENING: **Task 6.3** (*Find the bug*), **Task 6.4** (*Trace a classmate's pseudocode*), **Task 6.5** (*LLM sparring*).

Each task ends with a `### Keep your notes` block: "Keep your pseudocode and trace table — **AT2 is submitted around Lesson 18 of this week** and these are exactly the raw material AT2 will ask for."

**Vocabulary to make sure each task uses in plain English:** pseudocode, variable, trace table, dry run, bug, expected output, actual output.

---

### File 4 — `student/week-06/vocabulary.md` (10–18 terms)

**Required terms (Rasmus may add 1–4 of their own, but must not skip any required ones):**

1. **Pseudocode**
2. **Keyword** (in the pseudocode sense — `SET`, `IF`, `WHILE` etc.)
3. **Variable**
4. **Value**
5. **Assignment** (the `SET … TO …` action)
6. **Input**
7. **Processing**
8. **Output**
9. **Condition** (revisit from Week 5)
10. **Repetition** (revisit from Week 5)
11. **Block** (the body of an `IF`, `WHILE` or `FOR`)
12. **Dry run**
13. **Trace table**
14. **Bug**
15. **Expected output**
16. **Actual output**
17. **Edge case** (revisit from Week 1)
18. **Console** — flagged as **"looking ahead — Week 7, where pseudocode meets a real language"**. (If Rasmus prefers, *expression* or *return value* can replace this as the looking-ahead term, but exactly one looking-ahead term is required.)

Each definition is 1–3 sentences, plain English, with a short everyday example where natural. Aim ~14–16 terms total.

---

### File 5 — `student/week-06/slides.md` (~12–20 slides; target 15–18)

**Recommended slide outline (Rasmus may adjust order and titles within the spirit of the structure):**

1. `# Week 6 — From thinking to code` *(title slide)*
2. `## The central question` — body: the course's central question **verbatim**.
3. `## This week — pseudocode, variables, dry run` — 3-bullet preview of L16, L17, L18. Mention AT2 lands this week.
4. `## What is pseudocode?` — short quotable definition. Include the **Week 6 central message** verbatim or near-verbatim: *"Pseudocode is the bridge between everyday English and real code."*
5. `## The small set of keywords` — `SET`, `READ`, `WRITE`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`. One column.
6. `## English vs. pseudocode — making tea` — side-by-side, 4 lines each.
7. `## Sequence · condition · repetition` — one-line reminder that pseudocode encodes the three building blocks from Week 5.
8. `## Input → processing → output` — three boxes, one example sentence each.
9. `## What is a variable?` — definition + the labelled-box everyday metaphor.
10. `## A good variable name` — `SET x TO 7` vs. `SET passwordLength TO 7`. Two lines.
11. `## A vocational example — password strength` — 8–10 lines of pseudocode on one slide. (This slide ties to the L17 self-study example.)
12. `## What is a dry run?` — definition + link back to Week 1's "literal robot".
13. `## The trace table` — small worked example: 4 rows, 3 columns (line, variable, output).
14. `## Finding a bug — actual vs. expected output` — short before/after.
15. `## AT2 — submitted around Lesson 18` — 3 bullets: what AT2 asks for, what to bring, what NOT to bring.
16. `## Week 6 vocabulary at a glance` — 8–10 key terms.
17. `## Must-do minimum vs. deepening` — two-bullet contrast.
18. `## Tasks this week` — 1 line per task.
19. `## What comes next — Week 7: first real code` — preview, no syntax detail.
20. `## Recap — the central question, one more time` — the central question **verbatim again** as the closing slide.

Use `---` on its own line between every slide. Body content: 3–5 short bullets or 1–2 short sentences. No speaker-note syntax that assumes a specific renderer. **No `.pptx` references.**

---

### File 6 — `teacher/week-06/teacher-materials.md` (2600–4400 words)

**Required H2 sections (in order, with the verbatim wording listed in the brief):**

1. `## Week 6 learning objectives (mapped to Bloom)` — restate L16–L18 objectives from this plan, grouped by Bloom stage. Understanding + Applying only.
2. `## Common misconceptions for Week 6` — at least 6 across the week (≥2 per lesson). Suggested set:
   - **L16:** *"Pseudocode is a programming language."* → Correction: pseudocode is a shared convention, not a language a computer can run. // *"There is one correct pseudocode."* → Correction: different teachers use different keyword sets; this course uses one fixed set so everyone reads pseudocode the same way.
   - **L17:** *"A variable is the same as a number."* → Correction: a variable is a named container; today it holds a number, tomorrow it can hold a different one (or a yes/no, or a short string). // *"The name of a variable does not matter."* → Correction: `x` and `passwordLength` do the same thing for the computer, but very different things for the next person reading the pseudocode.
   - **L18:** *"If the pseudocode reads correctly, it is correct."* → Correction: reading does not catch off-by-ones, wrong comparisons, or missing initialisations. Only a trace table does. // *"A trace table is busywork — I can dry-run it in my head."* → Correction: head-tracing is exactly where bugs survive. The point of the table is that it forces you to write each step down.
3. `## Lesson 16 — 90-minute plan` — concrete time slots summing to 90. Suggested skeleton (mirrors the Week 1 release style):
   - 0–10 min: warm-up — read one short English instruction aloud, then ask the class to compress it into pseudocode-like form on the board.
   - 10–30 min: instructor input — definition of pseudocode + the small keyword set. Use supplementary deck `slides-l16-pseudocode-walkthrough.md` here (4–8 slides) to walk one familiar example through end-to-end.
   - 30–60 min: **INDEPENDENT WORK** (30 min) — each student begins Task 6.1 (write pseudocode for a familiar process). Just the writing; the dry-run waits for L18.
   - 60–80 min: pair activity — students swap drafts and read each other's pseudocode silently, underlining one line that is unclear.
   - 80–88 min: whole-class debrief — collect 3 example lines from the swap, rewrite together on the board.
   - 88–90 min: preview L17.
   - **Slide cues — main deck `slides.md` + supplementary deck `slides-l16-pseudocode-walkthrough.md`.** Map slide numbers to time slots explicitly.
4. `## Lesson 17 — 90-minute plan` — concrete time slots summing to 90. Suggested:
   - 0–10 min: warm-up — name three real-world "variables" in the room (the date on the board, the current speaker, the lunch menu). Set up the metaphor.
   - 10–30 min: instructor input — input/processing/output skeleton + the variable. Walk the password-strength example live on the board.
   - 30–60 min: **INDEPENDENT WORK** (30 min) — each student takes their L16 pseudocode and (a) labels the input, processing, and output sections; (b) replaces any unnamed values with named variables.
   - 60–80 min: pair activity — pairs trace each other's input/processing/output skeleton: can you spot where the processing happens?
   - 80–88 min: whole-class debrief — one example on the board.
   - 88–90 min: preview L18 and AT2.
   - **Slide cues — main deck `slides.md`.** (No supplementary deck recommended for L17.)
5. `## Lesson 18 — 90-minute plan` — concrete time slots summing to 90. AT2 is submitted around this lesson. Suggested:
   - 0–10 min: warm-up — board demo of a trace table for a 4-line pseudocode (e.g. swap two values).
   - 10–25 min: instructor input — what a dry run is, how to draw a trace table, what counts as "a bug".
   - 25–55 min: **INDEPENDENT WORK** (30 min) — students dry-run their own Task 6.1 pseudocode for **one normal and one awkward input**, drawing the trace table by hand.
   - 55–80 min: in-class teacher-led MANDATORY activity — **"Dry-run as a class"** (see `in-class-tasks.md`). The teacher writes a deliberately-broken short pseudocode on the board; students are the trace table.
   - 80–88 min: AT2 handover — 5 minutes on what AT2 expects, 3 minutes for clarifying questions. Calm pace.
   - 88–90 min: preview Week 7.
   - **Slide cues — main deck `slides.md`.** (No supplementary deck recommended for L18.)
6. `## Facilitation tips` — 4–8 short tips. Suggested:
   - Insist that students read pseudocode out loud during the dry run. The voice catches what the eye misses.
   - Do not let students re-write pseudocode while they trace it. Trace first, then fix on a separate page.
   - Protect the 30-min independent block; it is the part teachers under-pressure cut first.
   - Use the board for trace tables, not slides. Slides set up the question; the trace must happen live.
   - Connect every new term back to Week 5 (sequence, condition, repetition) and Week 1 (literal interpretation, ambiguity). Week 6 is synthesis, not a fresh start.
   - When students argue with the trace table, ask: *"What did line 4 say? Read it aloud. Now what does the variable equal after line 4?"*
7. `## Answers to common student questions` — at least 5. Suggested:
   - *"Is pseudocode a real language?"* — No. It is a shared convention. Different teachers use different keyword sets.
   - *"Can a computer run pseudocode?"* — Not directly. A human (or a translator) has to turn it into a real language first. Week 7 is where that translation starts.
   - *"Do I have to use these exact keywords?"* — Yes, in this course, so we can read each other's pseudocode the same way. In real workplaces, every team picks one set and sticks to it.
   - *"What does AT2 actually want from me?"* — A short piece of pseudocode for a small vocational task (or a familiar process), a trace table for one normal and one awkward input, and a 5-sentence reflection on what your trace found.
   - *"What if my trace table disagrees with my pseudocode?"* — Trust the trace table over your head. Then either your pseudocode has a bug, or your trace has one; do the trace a second time on a fresh page and see which one budges.
8. `## Formative assessment tips` — 3–5 quick checks. Exit ticket ("name one variable from your L16 pseudocode and one value it could hold"), board vote ("does this 5-line snippet write the right output?"), pair report-back, one-minute paper.

Cross-reference `in-class-tasks.md` from the L18 plan (the "Dry-run as a class" exercise belongs in the 55–80 min slot of L18). Cross-reference `slides-l16-pseudocode-walkthrough.md` from the L16 plan.

---

### File 7 — `teacher/week-06/in-class-tasks.md` (500–1400 words)

**Required structure:**
- `## Overview` — 2–3 sentences naming the tasks and when in the week they fit.
- At least 1 H2 task labelled **MANDATORY** that genuinely requires teacher-led classroom interaction.

**Two concrete activity ideas Rasmus should ship (default: both):**

**Activity A — MANDATORY — "Dry-run as a class"** *(whole-class + teacher-led, ~25 min, slotted in L18 between 55–80 min)*
- Teacher prepares a **short, deliberately broken pseudocode snippet on the board** (8–14 lines, exactly one bug). Suggested bug type: off-by-one in a `WHILE` condition (e.g. `WHILE counter < 5` should be `WHILE counter <= 5`).
- The class becomes the trace table. The teacher assigns one student per variable (or one per "column"). The teacher reads the pseudocode line by line, slowly. After each line, every "variable student" calls out the current value of their variable, and one "output student" calls out anything written to output.
- The whole-class trace runs to completion. The expected output is announced *only after* the trace finishes. The actual output differs (because of the bug). The class diagnoses which line caused the divergence.
- The teacher fixes the bug on the board (with student input on which line and what change). The class re-runs the trace from the line above the fix. Expected output now matches.
- **Closing (3 min):** the teacher names the type of bug in plain English ("this was an off-by-one"). The class adds the bug type to a running list of "bugs we have found by dry-running" — keep this list across L18 and into Week 7.
- **Why it requires the classroom:** every student gets a job (their variable). The embodied trace makes "the trace table catches what the eye misses" physically visible. It cannot be done as homework.

**Activity B — OPTIONAL — "Pseudocode swap and trace"** *(pair work, ~20 min, fits L16 60–80 min slot or as a L17 warm-up)*
- Pair A writes a short piece of pseudocode (6–10 lines, with one `IF` and one `WHILE` or `FOR`) for any familiar process. They do **not** name the goal.
- Pair B reads it and traces it on paper for one input the writer chooses. They write a one-sentence guess at what the pseudocode does.
- Reveal. Discuss: did the trace produce the expected output? Could the goal be inferred from the trace?
- Roles swap. Closing discussion: which keyword (`IF`, `WHILE`, `FOR`) made the goal most guessable?

Cross-reference back to `teacher-materials.md` so the teacher knows the exact 90-min slot for each.

---

### Supplementary deck — `student/week-06/slides-l16-pseudocode-walkthrough.md` (RECOMMENDED, 4–8 slides)

L16 is the lecture-heaviest segment of the week — students meet a new notation, a small keyword set, and the I/P/O skeleton in 20 minutes. The main deck has one summary slide per concept, which is fine for review but thin for first contact. **Rasmus should ship a supplementary deck for L16 that walks one concrete pseudocode example from English to a finished, traced piece**, so the teacher can run it slide by slide during the L16 lecture segment without losing the room.

**Suggested 6-slide outline for `slides-l16-pseudocode-walkthrough.md`:**

1. `# Worked example — making tea` *(title slide; brief intro: same template Week 1 used for instant noodles)*
2. `## In English` — 4–5 short English sentences describing how the student makes tea.
3. `## In pseudocode — the skeleton` — the same process in pseudocode (10–14 lines), with the `IF` (sugar yes/no) and the `WHILE` (until the kettle clicks) visible.
4. `## Naming the parts` — annotate which lines are input, which are processing, which are output. (Bridges to L17.)
5. `## What got more precise` — one short slide naming 3 things pseudocode pinned down that English left vague (which kettle, how full, how long).
6. `## The template scales` — one short slide naming three other places this skeleton works: a help-desk reply triage, a password-strength check, a daily backup routine.

**Why a supplementary deck for L17 is NOT recommended:** the L17 password-strength example is already short enough to walk live on the board, and the main deck slide 11 carries it.

**Why a supplementary deck for L18 is NOT recommended:** the L18 trace table is best done live on the board (the embodied trace is the lesson). A slide would compete with the board.

If Rasmus disagrees about L17 or L18, he may ship a supplementary deck for either; Wilhelm accepts any 4–8-slide supplementary deck cross-referenced from `teacher-materials.md`.

---

## Avoimet kysymykset

1. **Pseudocode dialect.** This plan recommends a fixed keyword set (`SET`, `READ`, `WRITE`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`). Some teachers prefer lowercase (`if`, `while`) or `:=` for assignment. **Default assumption:** Rasmus uses UPPERCASE keywords + `SET … TO …` for assignment, applied consistently across all 7 (or 8) files. Wilhelm checks consistency, not the specific choice.
2. **Code-fence language tag.** Pseudocode goes in fenced blocks. **Default assumption:** Rasmus uses ` ```text ` (or no language tag) — **never** ` ```js `, ` ```python ` or any other real-language tag. Wilhelm greps the language tags.
3. **Lists/arrays.** The brief allows a `FOR each x IN list` example. **Default assumption:** Rasmus uses lists at most once across the week, casually, never as a learning objective.
4. **AT2 detailed brief.** AT2 is "submitted around L18" — the actual AT2 brief lives outside Week 6 (Week 5 plan ends Bloom-applying foundation; AT2 brief is a separate document). **Default assumption:** Rasmus does not write AT2's brief; he names AT2 in the way the Week 6 files require (the `### Keep your notes` blocks, the L18 plan handover, the slide on AT2) and assumes the AT2 brief is delivered by the orchestrator.
5. **Looking-ahead term in vocabulary.** This plan suggests *console* as the Week-7 preview term. **Default assumption:** Rasmus uses *console*; if he prefers *expression* or *return value*, that is also acceptable as long as exactly one looking-ahead term is flagged.
6. **Reflection-prompt count.** Required: ≥4 across the three lessons in self-study (≥1 per lesson). **Default assumption:** Rasmus aims for 5–6 to give Wilhelm slack.
7. **30–50% rule — single block or split.** As in Week 1, Wilhelm accepts either one contiguous independent-work block or up to two clearly labelled "INDEPENDENT WORK" blocks per lesson summing to 27–45 min. **Default assumption:** one contiguous 30-min block per lesson (matches the suggested skeletons above).
8. **In-class activity scope.** "Dry-run as a class" is the strong default MANDATORY exercise for Week 6. **Default assumption:** Rasmus ships it as Activity A in L18, plus Activity B (pseudocode swap-and-trace) as OPTIONAL in L16/L17.
9. **No-real-language grep list.** This plan lists `console.log`, `let `, `var `, `const `, `function `, `def `, `print(`, `system.out`, `int main`, `<script`, `.js`, `JavaScript`, `Python`, `Java`, `C#` as the audit grep set. **Default assumption:** Wilhelm uses this exact list; any other obvious real-language token Rasmus accidentally writes will also fail.
10. **AT2 wording in `### Keep your notes`.** This plan requires the phrase "AT2 lands around L18 of this week" (or close variant). **Default assumption:** Rasmus uses *"AT2 is submitted around Lesson 18 of this week"* consistently across all tasks.
