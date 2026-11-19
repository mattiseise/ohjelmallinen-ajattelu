# Computational Thinking — Week 2 Plan (Sune, Gate #1)

Course: Computational Thinking (English)
Target: First-year vocational ICT students, ~15–17, no prior programming
Duration: 8 weeks x 3 lessons/week x 90 min = 24 lessons
Pipeline scope this run: Sune produces this Week 2 plan; Rasmus builds the full Week 2 package in the canonical weekly structure; Linnea/Wilhelm audit Week 2; Alfred packages a Week 2 release in Markdown only (no PDF/PPTX rendering this round).

The 24-lesson topic table and 8-week roadmap are inherited verbatim from Week 1's plan (`/Users/agent/material-pipeline/output/computational-thinking-en-week-01/01-suunnitelma.md`). This file is the **per-week** plan for Week 2 only.

---

## Suunnitelma

### Course overview (brief reuse)

The course answers one central question: **"How do I speak to a computer so that it understands what I want it to do?"** Week 1 trained students to see that a computer is a literal follower and that an algorithm is the everyday name for a clear sequence of literal steps. Week 2 builds the next core skill on top of that foundation: when a task is too big for a single algorithm, you **decompose** it — name the main task, name the subtasks that have to happen, and put them in the order they actually depend on. AT1 is submitted at the end of Lesson 6 (start of L7) and asks students to decompose an everyday or IT-related task into steps.

### Week 2 theme statement + connection to Week 1

Week 2 introduces **decomposition** — the first of the four classic pillars of computational thinking that the course works through in depth. In Week 1 every instruction students wrote was small enough to fit in one flat list of steps (make tea, walk to school, send a message). Week 2 changes the scale: the tasks are now too big to keep as one flat list. The student's new move is to look at a problem, find the **main task** and its **goal**, split it into **subtasks** that each have their own small algorithm, and then think carefully about the **order** of those subtasks and which ones depend on which. The literal-follower mindset from Week 1 is still in force — every subtask, on its own, must be writeable as a clear sequence of literal steps a literal follower could carry out. Week 2 does not retire that mindset; it stacks decomposition on top of it.

The arc across L4–L6: **L4** names the move and the vocabulary (main task, subtasks, goal). **L5** sharpens the move by introducing order and dependency. **L6** stress-tests the move on a real IT-related task and ends with AT1.

### L4 / L5 / L6 breakdown

#### Lesson 4 — Decomposing a problem: main task, subtasks, and goal

- **Topic (verbatim from brief):** *Decomposing a problem: main task, subtasks, and goal.*
- **Learning objectives** (Remembering + Understanding dominant, light Applying allowed; Applying is acceptable here because the brief explicitly says "students decompose real tasks"):
  - (a) **Define** *decomposition*, *main task*, *subtask*, *goal* in own words. *(Remembering)*
  - (b) **Explain** why a big task is easier to write up as several small algorithms than as one long one. *(Understanding)*
  - (c) **Recognize** subtasks inside a familiar everyday task (e.g. "make breakfast" decomposes into "decide what to eat", "prepare it", "eat it", "clean up"). *(Understanding)*
  - (d) **Identify** the goal of a main task and the goal of each of its subtasks. *(Understanding)*
  - (e) **Decompose** one everyday task into a main task + 3–6 subtasks. *(Applying — first time the verb appears in the course)*
- **Key vocabulary preview (3–6 terms):** decomposition, main task, subtask, sub-goal (or "goal of a subtask"), parent task; preview term *dependency* (formalised in L5).
- **Central message (one sentence):** A task is easier to think about, easier to write down, and easier to hand to a literal follower once you split it into a main task with a clear goal and a handful of subtasks that each have their own clear goal.
- **Vocational examples to lean on (from brief):** creating a user account (main task; subtasks: collect details, choose username, set password, send confirmation); onboarding a new colleague (subtasks: paperwork, accounts, hardware, intro to team).

#### Lesson 5 — Order of steps and dependencies

- **Topic (verbatim from brief):** *Order of steps and dependencies.*
- **Learning objectives** (Remembering + Understanding dominant, light Applying allowed):
  - (a) **Define** *dependency*, *order*, *parallel* (informally; we do not introduce concurrency, just "could happen at the same time"). *(Remembering)*
  - (b) **Explain** that a subtask can depend on another subtask because its input is the previous subtask's output. *(Understanding)*
  - (c) **Identify** dependencies between subtasks in a familiar decomposition. *(Understanding)*
  - (d) **Reorder** an out-of-order list of subtasks into a valid order. *(light Applying)*
  - (e) **Recognize** when two subtasks have no dependency on each other and could happen in either order (or "at the same time" in the everyday sense). *(Understanding)*
- **Key vocabulary preview (3–6 terms):** dependency, order, sequence, parallel (everyday sense), prerequisite; revisit *subtask* and *sub-goal* from L4.
- **Central message (one sentence):** Subtasks have an order because some subtasks need the output of another subtask before they can start; when there is no such dependency, the order is free.
- **Vocational examples to lean on:** sharing a file (you cannot send the link before you have set the sharing permissions; but you can write the email body in parallel); troubleshooting a startup problem (check power → check cable → check OS boot; some checks must happen in order, some are independent).

#### Lesson 6 — Decomposing an IT-related task (AT1)

- **Topic (verbatim from brief):** *Decomposing an IT-related task (AT1 submitted at end of L6 / start of L7).*
- **Learning objectives** (Remembering + Understanding dominant, light-to-moderate Applying allowed because the lesson culminates in AT1):
  - (a) **Identify** the main task and its goal in a realistic IT-related scenario (e.g. *"set up a new colleague's email account on their laptop"*). *(Understanding)*
  - (b) **Decompose** the IT-related main task into 4–8 subtasks. *(Applying)*
  - (c) **Order** those subtasks and mark at least one dependency. *(Applying)*
  - (d) **Explain** the decomposition to a partner (or to themselves in writing) in one short paragraph. *(Understanding)*
  - (e) **Submit AT1**: a short artefact that names the main task, its goal, 4–8 subtasks with sub-goals, and the order with at least one dependency called out.
- **Key vocabulary preview (3–6 terms):** revisit all Week 2 terms in an IT context; preview term *abstraction* (Week 3).
- **Central message (one sentence):** A real IT task is rarely small — the move that lets a beginner take it on at all is to decompose it into subtasks with named goals and a defensible order.
- **Vocational examples to lean on:** filling in a support ticket (decompose into: collect facts, reproduce, classify, write up, assign); onboarding a new colleague's email; resetting a forgotten password from the help-desk side.

### Week 2 — core minimum vs. deepening

**Core minimum — every student must leave Week 2 able to:**
- Define *decomposition*, *main task*, *subtask*, *sub-goal*, *dependency* in plain English.
- Take one everyday task and one IT-related task and decompose each into a main task + 4–6 subtasks with named sub-goals.
- Put the subtasks in a defensible order and identify at least one dependency.
- Submit AT1: a short artefact that does the above for one IT-related task.

**Deepening (optional extension):**
- Identify a subtask that is itself big enough to be decomposed further (a hint at recursion-free hierarchical decomposition — without using the word "recursion").
- Spot subtasks with no dependency on each other and describe in plain English where the order is free.
- Use an LLM as a sparring partner against the student's own decomposition (with a structured prompt that asks the LLM to challenge, not to answer).
- Compare two valid decompositions of the same IT task and explain which one is easier for a literal follower to act on.

### Forward-looking stubs for Weeks 3–8

**Week 3 — Describing a process and abstraction (Lessons 7–9).** Students learn to draw simple flowcharts (start/end + arrows), discover *abstraction* as "hide detail, keep what matters", and informally name reusable blocks of instructions ("functions without code"). Bloom focus: Understanding + Applying.

**Week 4 — Alternative solutions and evaluation (Lessons 10–12).** "Correct" is not unique. Students produce multiple valid solutions to the same problem, apply criteria (correctness, simplicity, readability, speed) to compare them, and practice peer feedback. Bloom focus: Applying + Analyzing + light Evaluating.

**Week 5 — Logic structures (Lessons 13–15).** Sequence, conditions (if-then-else, AND/OR informally) and repetition (repeat-until, for-each) are formalised. Bloom focus: Understanding + Applying. Foundation for AT2.

**Week 6 — Pseudocode and dry running (Lessons 16–18).** Synthesis of Weeks 1–5 into pseudocode. Variables and input/processing/output appear. Students dry-run pseudocode with a trace table and fix bugs. **AT2** is submitted. Bloom focus: Applying + Analyzing.

**Week 7 — First JavaScript (Lessons 19–21).** The bridge into code. Browser console only. `console.log`, `let`, `if/else`, comparison operators. Lesson 1's central question is revisited: a formal language exists precisely *because* computers cannot disambiguate. Bloom focus: Understanding + Applying.

**Week 8 — Loops, AT3, debugging, presentation (Lessons 22–24).** Loops in JavaScript, translation of a piece of own pseudocode into JavaScript (**AT3**), reading a real error message, and a 2-minute oral presentation of the AT3 program. The course closes where Lesson 1 started — speaking to a computer so it understands. Bloom focus: Applying + Analyzing + Creating (AT3).

---

## Rajaukset

**Out of scope for Week 2:**
- **No code, no JavaScript, no pseudocode, no flowcharts.** Decomposition is described in plain English, with bullet lists or shallow indentation only. Flowcharts arrive in Week 3.
- **No conditions, no loops.** Students notice that some subtasks "happen in some cases and not others," but `if/else` and `for/while` are not introduced. Week 5 handles those.
- **No recursion.** Hierarchical decomposition (a subtask that is itself a small main task) is allowed informally as a deepening idea, but the word *recursion* must not appear.
- **No automatic testing or debugging frameworks** (jest, mocha, vitest, pytest, etc.). Stated as a course-level rule.
- **No IDEs, no Node.js, no npm.** No tooling required.
- **No slide deck files beyond `slides.md`** plus, *only if a lecture segment genuinely needs more material than the main deck provides*, one or two `slides-l<n>-<topic>.md` supplementary decks (4–8 slides each). No `.pptx`, no `.key`, no Reveal.js, no Google Slides. Alfred packages a Markdown-only release this round; no PPTX rendering downstream this run.
- **No `media/` images required.** Rasmus may include 0–2 simple Markdown diagrams (e.g. a tree sketch for decomposition) under `student/week-02/media/` only if a slide or self-study explicitly references them.
- **No platform-side independent exercises** (different team).
- **No graded essays, no long written reports.** AT1 is an artefact + short reflection, not an essay.
- **No external accounts** that require email signup.
- **No phrase "computational thinking is just programming"** (carried over from Week 1).
- **No phrase "the computer is stupid/dumb"** (carried over from Week 1; the framing remains *literal*).
- **No `"AI-resilient"` label** anywhere in the 7 learner-facing files. Linnea audits the AI-resilience property, not the label.

**Language:** English throughout. The H2 headings in *this plan file* may remain in Finnish (`Suunnitelma`, `Rajaukset`, `Hyväksymiskriteerit`, `Briefing Rasmukselle`, `Avoimet kysymykset`) because they are part of the Sune template; **all 7 of Rasmus's Week 2 files must be fully English**, including their section headings. Börje (Finnish polishing) is skipped this run.

**Pipeline scope this run:**
- Sune produces this Week 2 plan (you are reading it).
- Rasmus builds **only Week 2** in the canonical 7-file weekly structure (plus an optional supplementary slides deck for L5 only if needed; see briefing). Weeks 3–8 are stubbed only.
- Linnea and Wilhelm audit Week 2 only.
- Alfred packages a Week 2 release in **Markdown only**. No PPTX conversion this round.

---

## Hyväksymiskriteerit

Wilhelm verifies the Week 2 package against the following concrete, checkable criteria.

### Structural — files and folders

1. **All 7 canonical files present**, with exactly these filenames (case-sensitive, lowercase, kebab-case):
   - `student/week-02/overview.md`
   - `student/week-02/self-study.md`
   - `student/week-02/student-tasks.md`
   - `student/week-02/vocabulary.md`
   - `student/week-02/slides.md`
   - `teacher/week-02/teacher-materials.md`
   - `teacher/week-02/in-class-tasks.md`
2. **No extra files** in `student/week-02/` or `teacher/week-02/` except possibly: (a) a `media/` subfolder under `student/week-02/` *only if* a slide or self-study reference contains it, and (b) **at most one** supplementary slides deck named `student/week-02/slides-l<n>-<topic>.md` (4–8 slides), *only if* a lecture segment in the 90-min plan in `teacher-materials.md` genuinely needs more material than `slides.md` provides.
3. **No `slides.pptx`, no `deck.md`, no `slides.key`, no Reveal.js HTML, no `.pdf`** anywhere. Hard fail if found.

### Volume (sanity-check brackets)

4. `overview.md`: **200–400 words**.
5. `self-study.md`: **2400–4000 words** (covers L4, L5, L6).
6. `student-tasks.md`: **800–1800 words** total.
7. `vocabulary.md`: **10–18 terms**, each with a 1–3 sentence English definition.
8. `slides.md`: **~10–20 slides**, separated by `---` on their own line, each slide starting with an H1 (`#`) or H2 (`##`) title and containing minimal supporting content (3–5 short bullets or 1–2 short sentences).
9. `teacher-materials.md`: **2400–4200 words**. Contains **3 × 90-minute lesson plans** (one per lesson L4/L5/L6), each with time slots summing to 90.
10. `in-class-tasks.md`: **400–1200 words**. Contains **at least 1 MANDATORY teacher-led in-class exercise**.
11. If a supplementary deck is shipped: **4–8 slides**, `---` separators, named `slides-l<n>-<topic>.md` (kebab-case topic), referenced by name from the relevant Slide cues subsection in `teacher-materials.md`.

### Required H2 sections — `teacher-materials.md` (EXACT WORDING — Wilhelm rejects variants)

12. `teacher-materials.md` must contain these H2 sections, in this order, with **exactly this wording**:
    - `## Week 2 learning objectives (mapped to Bloom)`
    - `## Common misconceptions for Week 2`
    - `## Lesson 4 — 90-minute plan`
    - `## Lesson 5 — 90-minute plan`
    - `## Lesson 6 — 90-minute plan`
    - `## Facilitation tips`
    - `## Answers to common student questions`
    - `## Formative assessment tips`
13. Each of `## Lesson 4 — 90-minute plan`, `## Lesson 5 — 90-minute plan`, `## Lesson 6 — 90-minute plan` must end with a subsection whose exact heading is `**Slide cues — main deck \`slides.md\`.**` (formatted bold, with the backtick-wrapped filename). If a supplementary deck is used, the same Slide cues subsection names it inline (e.g. `**Slide cues — main deck \`slides.md\` + supplementary deck \`slides-l5-dependencies.md\`.**`).
14. `## Common misconceptions for Week 2` contains **at least 6 misconceptions across the week (≥2 per lesson)**, each with a `Correction:` line.
15. `## Answers to common student questions` contains **at least 5 questions across the week**, with answers.
16. `## Formative assessment tips` contains 3–5 quick checks (exit ticket, board vote, pair report-back, one-minute paper, etc.).

### Required H2 sections — other files

17. `overview.md` must contain (in this order):
    - `## Week 2 theme`
    - `## What you will be able to do by the end of the week`
    - `## Core minimum vs. deepening` (with a clear two-bullet-list contrast; the **must-do minimum** wording appears here, not "mandatory minimum")
    - `## How the three lessons fit together`
18. `self-study.md` must contain:
    - `# <Week title>` (an inviting H1 title)
    - `## Introduction` — recalls Week 1's central question and names the Week 2 central message verbatim somewhere in the file.
    - `## Lesson 4 — Decomposing a problem (main task, subtasks, and goal)` (or close variant)
    - `## Lesson 5 — Order of steps and dependencies` (or close variant)
    - `## Lesson 6 — Decomposing an IT-related task` (or close variant)
    - `## Summary and what comes next` — closes the loop, previews Week 3 (abstraction + flowcharts).
    - **At least 4 `> **Pause for a moment:**` reflection prompts** across the three lessons (≥1 per lesson).
19. `student-tasks.md` must contain:
    - `## Overview of the week's tasks` — uses the wording **"must-do minimum"** for the MANDATORY tasks (not "mandatory minimum").
    - One H2 per task, prefixed with `🟢 MANDATORY —` or `🟣 DEEPENING —`.
    - Each task ends with a `### Keep your notes` block (or equivalent named block) that **explicitly mentions AT1** and reminds the student that AT1 is submitted at the end of Lesson 6.
20. `vocabulary.md` must contain a single H2 `## Week 2 vocabulary`, then each term as an H3 (or as a bolded term in a definition list). **At least one term is flagged as a "looking ahead" preview** (e.g. *abstraction* for Week 3). The Week 1 term *decomposition* must reappear here with a richer Week-2 definition (it was previewed in Week 1; Week 2 owns it).
21. `slides.md` must:
    - Start with a title slide.
    - Contain at least one slide whose body shows the Week 2 central message verbatim (see below).
    - Use `---` on its own line between slides.
    - Have **no embedded `.pptx` references** and no speaker-note syntax that assumes a specific renderer.
22. `in-class-tasks.md` must contain:
    - `## Overview`
    - At least 1 H2 task labelled **MANDATORY**, requiring teacher-led classroom interaction (pair work, role play, whole-class debrief, board sort, sticky-note sort).

### Pedagogical rules

23. **30–50% rule**: in `teacher-materials.md`, for each of the three 90-minute lesson plans, the time blocks visibly labelled as *independent student work* (not lecture, not group/pair activity, not debrief) sum to **27–45 minutes** out of 90. Wilhelm checks the time slots arithmetically.
24. **Bloom cap (Week 2)**: Remembering + Understanding **dominant**, **Applying allowed** (students decompose real tasks). Higher Bloom levels — *Analyzing, Evaluating, Creating* — are **out of scope** for Week 2 objectives. **Forbidden verbs** in Week 2 objectives: *evaluate, judge, critique, design (a system), build, develop, debug, abstract* (note: *abstract* is reserved for Week 3). *Analyze* is also out of scope as a primary verb (a stronger version arrives in Week 4).
25. **Central message of Week 2** appears **verbatim** on at least one slide in `slides.md` and at least once in `self-study.md`. The canonical wording is the brief's:
    > *"A big problem becomes a manageable problem once you name the main task, its subtasks, and the order in which they have to happen."*
26. **Continuity with Week 1**: at least one explicit reference to Week 1's central question (*"How do I speak to a computer so that it understands what I want it to do?"*) appears in `self-study.md` (typically in the Introduction or in L4). The literal-follower framing from Week 1 is mentioned at least once in `self-study.md` and at least once in `teacher-materials.md` (in either the misconceptions section or facilitation tips).
27. **Examples-first principle**: in `self-study.md`, every conceptual section that uses both kinds of examples places the **everyday example before the IT example**. Wilhelm spot-checks the three lesson sections.
28. **No automatic testing frameworks** mentioned anywhere in any of the 7 files. No `.pptx`, `.key`, Reveal.js, or PDF references.
29. **Literal interpretation framing**: the phrase "the computer is stupid / dumb" must not appear; "the computer is literal" framing must hold, even in Week 2's lighter mentions of it.
30. **No `"AI-resilient"` label** appears in any of the 7 learner-facing files (overview, self-study, student-tasks, vocabulary, slides, teacher-materials, in-class-tasks). Linnea audits the *property* of AI-resilience; the *label* must not leak into student- or teacher-facing files.

### Tasks (volume, balance, AI-resilience, alone-mode)

31. `student-tasks.md` contains **1–2 🟢 MANDATORY tasks + 2–3 🟣 DEEPENING tasks** (3–5 tasks total).
32. The MANDATORY task(s) use the **"must-do minimum"** wording in their introductory framing and in `overview.md`. The word "mandatory" is allowed in the H2 label `🟢 MANDATORY —`, but the *describing* phrase used in `overview.md` and the Overview section of `student-tasks.md` must be **"must-do minimum"**, not "mandatory minimum".
33. **AI-resilience property (Linnea verifies)**: at least one MANDATORY task is AI-resilient by construction, meaning it requires the student's own concrete context, an observable artefact (a real decomposition tied to a specific named task in the student's life or school, a recording, a screenshot, a real follower's reaction), or a critique-the-LLM mechanism. Linnea audits this; **the label "(AI-resilient)" must not appear** in the file.
34. **"If you are doing this alone" subsection** (`### If you are doing this alone`) is required in **every task that assumes a partner, follower, tester, or live reaction**. The subsection must propose a concrete alternative (24h gap, video self, different device, class chat). Specifically:
    - Task 2.1 (default MANDATORY — *Decompose your own everyday task*): **not required** (no partner needed), but Rasmus may include one with a 24h-gap alternative if useful.
    - Task 2.2 (default MANDATORY — *Decompose with a partner, then re-test*): **required**, with a 24h-gap + class-chat alternative.
    - Task 2.3 (default DEEPENING — *Order and dependencies*): not strictly required; include only if Rasmus designs it to need a partner.
    - Task 2.4 (default DEEPENING — *Vocational angle: decompose an IT task at your school*): **required**, with a class-chat + different-device alternative.
    - Task 2.5 (default DEEPENING — *LLM-as-sparring-partner against your own decomposition*): not required (no human partner needed); the sparring-partner step uses an LLM prompt in a fenced code block and **must not accept the LLM output verbatim**.
35. If a DEEPENING task uses an LLM as a sparring partner, it must include a fenced code block with a sample prompt and an explicit instruction not to accept the LLM's output verbatim.
36. **AT1 reminder in every task's `### Keep your notes` block**: every task explicitly names AT1, says it is submitted at the end of Lesson 6, and tells the student which artefact from this task they should keep for AT1.

### In-class tasks

37. `in-class-tasks.md` contains **at least 1 MANDATORY teacher-led in-class exercise** that genuinely requires classroom interaction. It must be cross-referenced from `teacher-materials.md` (one of the 90-minute plans names it in the relevant time slot).

### Cross-file consistency

38. **Task numbering in `slides.md` matches `student-tasks.md`.** If `slides.md` mentions "Task 2.1 / 2.2 / 2.3 / 2.4 / 2.5", the same identifiers must appear in `student-tasks.md`.
39. **In-class activities referenced in `teacher-materials.md` exist in `in-class-tasks.md`** (and vice versa: every activity in `in-class-tasks.md` is slotted into a 90-min plan in `teacher-materials.md`).
40. **Vocabulary terms used in `self-study.md`, `student-tasks.md` and `slides.md`** all appear (and are defined) in `vocabulary.md`. Wilhelm spot-checks 5 terms.

### Language and polish

41. **English throughout.** No Finnish words in any of the 7 files except clearly necessary proper nouns.
42. **Register:** `self-study.md`, `student-tasks.md`, `overview.md`, `vocabulary.md` and `slides.md` at CEFR ~B1 (short sentences, common vocabulary); `teacher-materials.md` and `in-class-tasks.md` at CEFR ~B2.
43. **Valid Markdown:** every code fence closes, every table renders, no broken internal links, `---` separators in `slides.md` are alone on their own line.
44. **No `jest`, `mocha`, `vitest`, `pytest`** anywhere. No `.pptx`. No `.key`. No `Reveal.js`. No `.pdf`. Wilhelm greps.

---

## Briefing Rasmukselle

### Cross-cutting reminders (apply to all 7 files)

- **Everyday before IT, always.** Week 2 has a strong vocational lean (the brief explicitly names "creating a user account, sharing a file, onboarding a new colleague, troubleshooting a startup problem, filling in a support ticket"), but every new idea is still introduced with a familiar 15-year-old scene first (making breakfast, organising a birthday party, packing a school bag for a sports day) and only then pivots to the IT example.
- **The computer is literal, not stupid.** Carried over from Week 1. If the framing slips, Linnea will flag it.
- **No code, no flowcharts, no pseudocode, no variables, no loops, no if/else.** Decomposition is described in plain English with bullets and shallow indentation only.
- **No `"AI-resilient"` label** in any learner-facing file. Linnea audits the property, not the label.
- **"Must-do minimum"** is the wording for MANDATORY in `overview.md` and in the Overview section of `student-tasks.md`. Do NOT write "mandatory minimum" anywhere.
- **AT1 reminder** in every task's `### Keep your notes` block. AT1 is submitted at the end of Lesson 6.
- **Central message of Week 2 must appear verbatim** in `self-study.md` and on at least one slide in `slides.md`:
  > *"A big problem becomes a manageable problem once you name the main task, its subtasks, and the order in which they have to happen."*
- **Continuity reminder.** Week 2 builds on Week 1. Mention the literal-follower lens at least once in `self-study.md` and reference the Week 1 central question once (typically in the Introduction).
- **Bloom cap.** Remembering + Understanding dominant. Applying allowed because students *decompose* real tasks — *decompose* is the new verb that arrives this week. Do **not** use *evaluate*, *design (a system)*, *build*, *develop*, *debug*, *abstract*, or *analyze* in Week 2 objectives.
- **No `.pptx`** references. Rasmus delivers `slides.md` (and optionally one supplementary deck for L5). Alfred packages Markdown only this round.

---

### File 1 — `student/week-02/overview.md` (200–400 words)

**Required H2 structure (in order):**
1. `## Week 2 theme` — one short paragraph naming the new move (decomposition: main task + subtasks + order) and the three lesson topics (L4, L5, L6). Mention AT1 at the end of L6 in one sentence.
2. `## What you will be able to do by the end of the week` — bullet list of 5–7 plain-English "can do" statements derived from the L4–L6 objectives.
3. `## Core minimum vs. deepening` — clear two-bullet-list contrast. Use the wording **"must-do minimum"** for the MANDATORY side. Mirror the "Core minimum vs. deepening" section above.
4. `## How the three lessons fit together` — one short paragraph showing the L4 → L5 → L6 arc (name the move → sharpen with dependencies → real IT task + AT1).

**Examples to lean on:** "making breakfast" decomposed (everyday); "creating a user account" decomposed (IT, light preview only — full version in L6).

---

### File 2 — `student/week-02/self-study.md` (2400–4000 words)

**Required structure (in order):**
- `# <Week title>` — suggestion: *"From one list of steps to a tree of small tasks — decomposing problems"* or similar. Rasmus may improve.
- `## Introduction` — opens with a familiar scene (planning a birthday party; packing for a school sports day; making a full breakfast for the family on a Sunday). Recalls Week 1's central question (*verbatim* once) and names the new Week 2 move. States the **Week 2 central message verbatim** somewhere here or in the Summary. Tells the student what the week will train.
- `## Lesson 4 — Decomposing a problem (main task, subtasks, and goal)`
  - `### What is decomposition?` — short, quotable definition. Place it next to the Week 1 hook: "Last week your instructions were small enough to be one flat list. This week they get too big for that."
  - `### Main task, subtasks, and the goal` — define the three terms. Use one everyday example (e.g. *making breakfast for four people*) walked through in detail: main task ("make breakfast for four people"), goal ("everyone is eating breakfast within 30 minutes"), subtasks ("decide menu", "check what's in the fridge", "prepare hot food", "prepare cold food", "set the table", "call everyone to the table").
  - `### Why decompose at all?` — three reasons in plain English: (1) you can write each subtask as a clean small algorithm; (2) you can give different subtasks to different people; (3) you can check your work subtask by subtask, instead of all at once.
  - `### A first IT example` — *creating a user account* lightly: main task, goal, 4–5 subtasks. Keep it shallow — depth lives in L6.
  - 1 `> **Pause for a moment:**` reflection prompt.
- `## Lesson 5 — Order of steps and dependencies`
  - `### Some subtasks depend on others` — define *dependency* with a tiny everyday example: you can't eat the toast before you've toasted it. The toast subtask **depends on** the "put bread in toaster" subtask because its input is the previous subtask's output.
  - `### Some subtasks are independent` — informal *parallel*. The "set the table" subtask doesn't depend on "make the tea": they could happen in either order, or "at the same time" if two people are doing it. **Do not introduce concurrency formally.**
  - `### Putting subtasks in a defensible order` — one worked example (everyday): organising a birthday party. List 6–8 out-of-order subtasks; show how dependencies pin some into a fixed order and leave others free.
  - `### The IT mirror` — sharing a file with a colleague: pick the recipient → set sharing permissions → copy the link → write the email body → send. Note which steps are dependent and which are free.
  - 1–2 `> **Pause for a moment:**` reflection prompts.
- `## Lesson 6 — Decomposing an IT-related task`
  - `### Stepping up to a realistic IT task` — describe the scenario: *"set up a new colleague's email account on their new laptop on their first day"*. Walk through main task + goal first.
  - `### From scenario to subtasks` — show 5–7 subtasks with sub-goals.
  - `### Order and dependencies in the real task` — pick out 2–3 dependencies.
  - `### Two valid decompositions of the same task` — a gentle nod to Week 4: more than one decomposition can be valid.
  - `### Preparing for AT1` — short paragraph explicitly naming AT1: at the end of this lesson, the student submits a decomposition of an everyday or IT-related task. The notes the student has been keeping all week become the raw material. Re-state the central message of the week here verbatim if it has not appeared yet.
  - 1 `> **Pause for a moment:**` reflection prompt.
- `## Summary and what comes next` — closes the loop on the week's central message (verbatim). Previews Week 3 (abstraction and flowcharts) in one short paragraph.

**Examples menu Rasmus should pick from (everyday first, IT after):**
- Everyday: making breakfast for four people; organising a birthday party; packing for a school sports day; planning a movie night with friends; doing the weekly grocery shop; tidying a shared room.
- IT (from brief): **creating a user account; sharing a file; onboarding a new colleague; troubleshooting a startup problem; filling in a support ticket.** Use creating a user account in L4 (light), sharing a file in L5, onboarding/email setup in L6.

**Length target:** ~3000 words. Lesson 4 ~1100, Lesson 5 ~900, Lesson 6 ~900, plus intro and summary.

---

### File 3 — `student/week-02/student-tasks.md` (800–1800 words)

**Required structure:**
- `## Overview of the week's tasks` — 2–4 sentences. State that 🟢 MANDATORY tasks are the **must-do minimum** and 🟣 DEEPENING are optional extension. **AT1 lands at the end of Lesson 6**, so notes from these tasks become AT1 raw material. (Do NOT write "AI-resilient" anywhere.)

**Five candidate task ideas Rasmus should ship (default: keep 2 MANDATORY + 3 DEEPENING):**

**Task 2.1 — 🟢 MANDATORY — "Decompose one task from your own week"**
- **AI-resilience property (do NOT label):** anchored in the student's own concrete week — an event they actually have to do this week (a project deadline, a sports practice they organise, a trip home for the weekend). The artefact is their own decomposition tied to their own calendar.
- Student picks **one real task they actually have this week** (not a hypothetical one).
- Writes: main task name; goal in one sentence; 4–6 subtasks with a sub-goal each; one short paragraph (3–5 sentences) of reflection on what was surprising about the decomposition.
- **"If you are doing this alone" subsection:** NOT REQUIRED (no partner needed). Rasmus may optionally include a 24h-gap variant ("come back the next day and read your own decomposition fresh; cross out any subtask that feels unclear").
- **Keep your notes** block: this is the raw material for AT1 if the student chooses an IT task in Task 2.4; otherwise it warms them up for AT1.

**Task 2.2 — 🟢 MANDATORY — "Decompose with a partner, then re-test"**
- **AI-resilience property (do NOT label):** requires a real partner's literal interpretation of the student's decomposition; an LLM cannot fake the partner's questions.
- Student picks a small everyday task (making a sandwich for someone else's specific dietary needs; organising a small surprise; planning a 2-day camping trip). Decomposes it into 4–6 subtasks with sub-goals.
- Hands the decomposition to a partner. Partner reads it once and asks at least 3 clarifying questions ("what does subtask 3 actually mean?", "is subtask 5 supposed to happen before or after subtask 4?", "where does the output of subtask 2 go?").
- Student rewrites the decomposition with the questions answered.
- 3–5 sentence reflection: which subtask was the most ambiguous, and why?
- **"If you are doing this alone" subsection: REQUIRED.** Alternative: **24h-gap technique** (write the decomposition today, come back tomorrow with no notes, and read it as if a colleague handed it to you; write down the 3 questions you ask yourself). Or: **class chat** — post the decomposition with one line "Trying this for a class task — would anyone read it and tell me which subtask they got stuck on?"
- **Keep your notes** block: AT1 reminder.

**Task 2.3 — 🟣 DEEPENING — "Order and dependencies on a familiar task"**
- Student picks one of their own decompositions (from Task 2.1 or 2.2), or writes a new one for a familiar task.
- Identifies for each subtask: (a) which other subtask(s) it **depends on** (its input is their output), (b) which subtasks it does **not** depend on (could happen in any order).
- Re-draws the decomposition as a numbered ordered list with dependency notes ("subtask 4 depends on subtask 2").
- 3–5 sentence reflection: which subtasks were "free" in the order, and why does that matter?
- **"If you are doing this alone" subsection:** NOT REQUIRED (no partner needed).
- **Keep your notes** block: AT1 reminder.

**Task 2.4 — 🟣 DEEPENING — "Vocational angle: decompose an IT task at your school"**
- **AI-resilience property (do NOT label):** the school's specific UI, naming conventions, and a real classmate-as-tester are all things an LLM cannot fake without giving itself away.
- Student picks one concrete IT task that actually exists in their school (set up a new student's school email on a school laptop; reset a forgotten password from the help-desk side; share a folder with a class group; install one specific piece of school-licensed software).
- Decomposes it into 5–8 subtasks with sub-goals, names dependencies, and writes a one-paragraph explanation aimed at a first-line help-desk colleague.
- Optional: shows the decomposition to a classmate who has never done that task and asks them to predict what subtask 3 would actually look like. Note whether their prediction matched.
- **"If you are doing this alone" subsection: REQUIRED.** Alternatives: **class chat** ("Trying this for a class task — would anyone read it and tell me which subtask they don't understand?"); **different device** (walk through the decomposition on a different device — phone vs. classroom PC vs. home laptop — the change in context will surface assumptions); **24h-gap technique** as a last resort.
- **Keep your notes** block: this is the strongest candidate for AT1. The AT1 reminder here should be unusually direct: *"If you ship a clean version of this task, you have most of AT1 already."*

**Task 2.5 — 🟣 DEEPENING — "Sparring partner: challenge your own decomposition"**
- Student takes one of their own decompositions (Task 2.1, 2.2 or 2.4) and pastes it into an LLM with the **sample prompt below** (in a fenced code block). The LLM is asked to challenge, not to answer.
- After the LLM responds, the student decides for each challenge whether to accept, modify or reject it, and writes one short sentence next to each decision.
- **Sample prompt (Rasmus provides in fenced code block):**
  ```
  You are my sparring partner, not my teacher. I am a vocational ICT
  student practising decomposition: I have broken a task into a main
  task, subtasks with sub-goals, and an order with dependencies.

  Below is my decomposition.

  [paste your decomposition here]

  Please challenge me. For each subtask:
  - Could it be split further? If so, into what?
  - Is the sub-goal really specific to that subtask, or is it the
    main task's goal in disguise?
  - Is there a dependency I missed?
  Do not give me the "right" answer. Ask me a question that helps
  me see the gap myself.
  ```
- **Explicit instruction not to accept the LLM's output verbatim.**
- **"If you are doing this alone" subsection:** NOT REQUIRED (the LLM is the sparring partner; no human needed).
- **Keep your notes** block: AT1 reminder.

**Default selection Rasmus should ship:**
- 🟢 MANDATORY: Task 2.1 (*Decompose one task from your own week*) **and** Task 2.2 (*Decompose with a partner, then re-test*). 2.2 carries the AI-resilience property strongly.
- 🟣 DEEPENING: Task 2.3 (*Order and dependencies*), Task 2.4 (*Vocational IT decomposition*), Task 2.5 (*LLM sparring partner*). Task 2.4 also carries the AI-resilience property.

Each task ends with `### Keep your notes` containing an explicit AT1 reminder.

---

### File 4 — `student/week-02/vocabulary.md` (10–18 terms)

**Required terms** (Rasmus may add 1–4 of their own, but must not skip any required ones):
1. **Decomposition** — full Week 2 definition (it was previewed in Week 1; now it owns this week).
2. **Main task**
3. **Subtask**
4. **Sub-goal** (the goal of a subtask, as distinct from the goal of the main task)
5. **Goal** (revisit from Week 1, now in the context of a main task)
6. **Dependency**
7. **Order** (in the sense of *order of subtasks*)
8. **Sequence** (revisit from Week 1; now in the context of subtasks)
9. **Prerequisite** (a near-synonym of dependency; explain the difference if used — a prerequisite is a condition that must be true before you start; a dependency is a connection between two subtasks)
10. **Parallel** (informal, everyday sense only — "could happen at the same time" — explicitly say concurrency is not introduced)
11. **Parent task** (synonym for main task, when discussing hierarchy)
12. **Hierarchy** (informal sense — a main task at the top, subtasks underneath)
13. **AT1** — define as "the first assessed task, submitted at the end of Lesson 6"
14. **Abstraction** — flagged as **"looking ahead — central topic of Week 3"**.

Optional additions Rasmus may include if useful: *artefact* (revisit), *literal follower* (revisit from Week 1), *checklist* (as a flat decomposition without dependencies), *workflow* (informal sense), *handover* (vocational).

Each definition is 1–3 sentences, plain English, with a short everyday example where natural.

**Target:** ~14 terms.

---

### File 5 — `student/week-02/slides.md` (~10–20 slides)

**Recommended slide outline (Rasmus may adjust order and titles within the spirit of the structure):**

1. `# Week 2 — Decomposing problems` *(title slide)*
2. `## What we covered in Week 1` — 3 short bullets recalling literal follower + algorithm + ambiguity.
3. `## This week's central message` — body shows the **Week 2 central message verbatim**.
4. `## What is decomposition?` — short quotable definition.
5. `## Main task, subtasks, goal` — visual: a main task with 4 subtasks beneath it (Markdown indentation is fine; no images needed).
6. `## Everyday example — making breakfast for four` — 3–5 bullets showing the decomposition.
7. `## IT example — creating a user account` — 3–5 bullets, light depth.
8. `## Why decompose at all?` — 3 reasons.
9. `## Some subtasks depend on others` — define dependency in 1 sentence + a tiny example.
10. `## Some subtasks are independent` — define informally + a tiny example.
11. `## Putting subtasks in order` — show an out-of-order list and a corrected order side by side.
12. `## IT example — sharing a file` — 4–5 subtasks with one dependency flagged.
13. `## Decomposing a real IT task` — preview L6 scenario (set up a new colleague's email).
14. `## Two valid decompositions of one task` — gentle nod to Week 4 (no formal evaluation).
15. `## Week 2 vocabulary at a glance` — 6–8 key terms in one slide.
16. `## Tasks this week` — 1 line per task (Task 2.1 through 2.5 by ID, matching `student-tasks.md`).
17. `## AT1 — the first assessed task` — what AT1 is, when it is submitted (end of Lesson 6), what artefact to bring.
18. `## What comes next: Week 3 — abstraction and flowcharts` — one-line preview.
19. `## Recap — the central message, one more time` — repeat the Week 2 central message verbatim (this guarantees the verbatim requirement holds even if slide 3 changes).

**Aim ~15–18 slides.** Use `---` on its own line between every slide. Body content: 3–5 short bullets or 1–2 short sentences. No speaker-note syntax. Task IDs in slide 16 must match `student-tasks.md` exactly.

---

### File 6 — `teacher/week-02/teacher-materials.md` (2400–4200 words)

**Required H2 sections (EXACT wording — Wilhelm will reject variants):**

1. `## Week 2 learning objectives (mapped to Bloom)` — restate the L4–L6 objectives from this plan, grouped by Bloom stage. Remembering + Understanding dominant; Applying allowed where students decompose real tasks. Forbidden verbs: *evaluate, judge, critique, design (a system), build, develop, debug, abstract, analyze*.

2. `## Common misconceptions for Week 2` — **at least 6 across the week (≥2 per lesson)**, each with a `Correction:` line. Suggested set:
   - **L4**: "Decomposition is just making a long list." → Correction: a decomposition has a main task and named subtasks with sub-goals, not just a flat sequence of steps. // "There's one right decomposition." → Correction: more than one decomposition can be valid; in Week 4 we'll learn to compare them.
   - **L5**: "Every step has to come right after the previous step." → Correction: dependencies pin some steps into a fixed order; others are free. // "If two subtasks can be done in any order, the order doesn't matter at all." → Correction: it matters less, but a sensible default order still helps the literal follower.
   - **L6**: "Decomposing an IT task is just listing the buttons to click." → Correction: it names the main task, the goal, and the subtasks that have their own sub-goals; the buttons are inside subtasks, not the decomposition itself. // "AT1 wants a perfect decomposition." → Correction: AT1 wants a defensible decomposition with a stated goal, named subtasks, and at least one dependency called out.
   - Bonus (good to include): "If I decompose hard enough, I won't have to write any actual steps." → Correction: decomposition is a planning move; the steps still have to exist underneath, just at a manageable size.

3. `## Lesson 4 — 90-minute plan` — concrete time slots summing to 90, with an independent-student-work block of **27–45 min**. Suggested skeleton:
   - 0–10 min: warm-up — collect 3 everyday tasks from students that "feel too big for one list of steps".
   - 10–25 min: instructor input — define decomposition, main task, subtask, sub-goal; walk one everyday example live.
   - 25–55 min: **INDEPENDENT WORK** (30 min) — students decompose their own everyday task (start of Task 2.1).
   - 55–75 min: pair activity — students swap decompositions; the partner asks 3 clarifying questions.
   - 75–85 min: whole-class debrief.
   - 85–90 min: closing reflection + preview of Lesson 5.
   - End with: `**Slide cues — main deck \`slides.md\`.**` subsection mapping main-deck slide numbers (4 → 8) to time slots.

4. `## Lesson 5 — 90-minute plan` — same arithmetic constraint. Suggested:
   - 0–10 min: warm-up — quick "what depends on what" board game (the teacher writes 6–8 out-of-order subtasks on the board for one familiar task; the class reorders them).
   - 10–25 min: instructor input — define dependency, order, informal parallel; one everyday example walked through.
   - 25–60 min: **INDEPENDENT WORK** (35 min) — students take their own decomposition from L4 and add dependencies + order.
   - 60–80 min: in-class teacher-led activity — **MANDATORY "Dependency sort"** from `in-class-tasks.md`.
   - 80–88 min: whole-class debrief.
   - 88–90 min: preview of Lesson 6.
   - End with: `**Slide cues — main deck \`slides.md\`.**` subsection. **This is the lesson where a supplementary deck may be useful** — see "Supplementary deck" note below.

5. `## Lesson 6 — 90-minute plan` — same arithmetic constraint. Suggested:
   - 0–10 min: warm-up — recap the Week 2 central message verbatim; one short example of an IT task that is "too big for one flat list".
   - 10–25 min: instructor input — walk through the IT scenario (set up a new colleague's email account on their new laptop); identify main task, goal, 5–7 subtasks, 2–3 dependencies.
   - 25–55 min: **INDEPENDENT WORK** (30 min) — students draft their AT1 artefact (pick a real IT task; decompose it; name dependencies).
   - 55–75 min: pair review — partner reads AT1 draft, asks 3 clarifying questions, student notes one thing to fix before submission.
   - 75–85 min: AT1 submission moment + whole-class debrief on the most common subtle errors (subtasks too vague, sub-goals duplicate the main goal, no dependency at all).
   - 85–90 min: preview Week 3 (abstraction and flowcharts).
   - End with: `**Slide cues — main deck \`slides.md\`.**` subsection.

6. `## Facilitation tips` — 4–6 tips. Suggested: *Insist on a named sub-goal for every subtask; resist solving for the student; protect the 30–50% rule; use the board for live re-orderings; bridge back to Week 1's "literal follower" every time a subtask comes out vague; reframe "stupid computer" if it slips.*

7. `## Answers to common student questions` — at least 5. Suggested: *How many subtasks is the "right" number? / What's the difference between a subtask and a step? / Is AT1 graded? / Can I use ChatGPT for AT1? / What if my partner asks more than 3 clarifying questions? / Can I pick a school-IT task I have never actually done?*

8. `## Formative assessment tips` — 3–5 quick checks. Suggested: *Exit ticket "name one subtask in your decomposition whose sub-goal you struggled to write"; board vote on three out-of-order subtask lists; pair report-back on dependencies; one-minute paper "what surprised you about decomposing your own task?"; sticky-note collection during the dependency sort.*

**Cross-reference `in-class-tasks.md` from the L5 plan** (Dependency sort is mandatory and lives in L5's 60–80 min slot). Optionally also from L4 (a short pair activity may use a variant).

**Supplementary deck — recommended for L5 only (Rasmus's call).** If the lecture segment on dependencies (L5, 0:10–0:25) needs more material than the main deck slides 9–11 provide (because dependencies are the conceptually hardest move of Week 2), Rasmus may ship one supplementary deck named:
- `student/week-02/slides-l5-dependencies.md` (5–7 slides). Outline:
  1. `## Dependency in one picture` — two subtasks, an arrow between them.
  2. `## When the input of subtask B is the output of subtask A` — short example.
  3. `## Free order — when there is no dependency` — short example.
  4. `## "Parallel" in the everyday sense` — two people, two subtasks.
  5. `## Out of order vs. wrong order` — two side-by-side decompositions, one valid, one broken.
  6. `## Spotting dependencies in a real task` — sharing a file with a colleague.
  7. `## When you cannot tell — ask the literal follower` — bridge back to Week 1.
- If shipped, L5's Slide cues subsection must name it: `**Slide cues — main deck \`slides.md\` + supplementary deck \`slides-l5-dependencies.md\`.**`
- Rasmus's call: ship if the main deck doesn't carry the dependency idea by itself; skip if it does.

**L4 and L6 should NOT need a supplementary deck.** The main deck carries them.

---

### File 7 — `teacher/week-02/in-class-tasks.md` (400–1200 words)

**Required structure:**
- `## Overview` — 2–3 sentences naming the tasks and when in the week they fit.
- At least 1 H2 task labelled **MANDATORY** that genuinely requires teacher-led classroom interaction.

**Two concrete activity ideas Rasmus should ship (default: both):**

**Activity A — MANDATORY — "Dependency sort" (whole-class + teacher-led, ~20 min, slotted in Lesson 5 between 60–80 min)**
- Teacher prepares one familiar everyday task (e.g. *organising a class trip*) and writes 8 of its subtasks on 8 large cards, one subtask per card. Subtasks include some hard dependencies (e.g. "collect parental consent forms" → "book the bus") and some free-order ones (e.g. "make a packing list" can be done any time).
- The class sorts the cards into a valid order on the board, with the teacher drawing arrows between cards that have a dependency.
- After one round, the teacher hands a fresh stack of 8 cards (different scenario — e.g. *sharing a file with the whole class*) to two student volunteers who lead a second round in front of the class.
- Closing: each student sketches the dependency arrows for their own L4 decomposition on the back of their paper. The teacher walks around and checks.
- **Why it requires the classroom:** the embodied act of physically sorting cards (or sticky notes) makes dependencies visible in a way reading a list does not. It cannot be done as homework with the same impact.

**Activity B — OPTIONAL — "Two decompositions, one task" (pair, ~25 min, can be slotted in Lesson 4 between 55–75 min or Lesson 6 between 55–75 min)**
- Pair A and Pair B independently decompose the **same** task (e.g. *make breakfast for four people* — given by the teacher) into 4–6 subtasks each.
- They swap and look for differences: same number of subtasks? Same boundaries between subtasks? Different sub-goals?
- Whole-class brief debrief: *"more than one valid decomposition can exist"* (preview of Week 4).

Cross-reference back to `teacher-materials.md` so the teacher knows the exact 90-min slot for each.

---

## Avoimet kysymykset

1. **Slide count.** The brief says "~10–20 slides for the whole week" with optional supplementary 4–8 slide decks. This plan recommends ~15–19 main-deck slides plus an optional 5–7 slide supplementary deck for L5. **Default assumption:** Rasmus targets 15–19 slides for the main deck and ships the L5 supplementary deck only if the dependency idea doesn't fit naturally into the main deck.

2. **Where exactly AT1 lives in L6's 90-min plan.** The brief says "AT1 submitted at the end of L6 / start of L7" — leaving ambiguity. **Default assumption:** AT1 is *drafted* during L6's independent-work block (0:25–0:55) and *submitted* at the 75-min mark of L6. If the teacher prefers to extend submission to "before the start of L7", that is acceptable — Wilhelm accepts either reading.

3. **AT1 artefact format.** The brief says AT1 is "decompose an everyday or IT-related task into steps". **Default assumption:** AT1 is a single-page artefact containing: (1) main task name and goal, (2) 4–8 subtasks with named sub-goals, (3) the order with at least one dependency called out, (4) a 3–5 sentence reflection. Format: Markdown or paper, student's choice. Length: ~250–500 words.

4. **MANDATORY task count.** Brief says "1–2 🟢 MANDATORY". This plan defaults to **2 MANDATORY** (2.1 + 2.2) because Week 2 is heavier than Week 1 (decomposition is new and AT1 lands at the end). Rasmus may drop to 1 MANDATORY (Task 2.2 only) if the workload feels too heavy — **but Task 2.2 must remain MANDATORY** because it carries the AI-resilience property.

5. **"Parallel" vs. concurrency.** This plan uses *parallel* informally only ("could happen at the same time") and explicitly bans concurrency. **Default assumption:** Rasmus uses *parallel* exactly once in the vocabulary, marks it informal, and avoids the word in `student-tasks.md` and `slides.md` to prevent confusion.

6. **Whether to ship the L5 supplementary deck.** This is Rasmus's call. **Default assumption:** ship it if the main deck cannot fit the dependency idea cleanly in slides 9–11; skip it otherwise. Either choice is acceptable to Wilhelm — but if shipped, the Slide cues subsection in `teacher-materials.md` for L5 must name it.

7. **AI-resilience labelling.** The brief is firm: do NOT label any task as "(AI-resilient)" in the learner-facing files. Linnea audits the property internally. **Default assumption:** Rasmus does not use the label anywhere; he writes tasks that are AI-resilient by construction (real partners, real artefacts, real school context).

8. **"Must-do minimum" wording placement.** The brief says this wording appears in `overview.md` and `student-tasks.md`. **Default assumption:** Rasmus uses "must-do minimum" verbatim in `overview.md` (in the Core minimum vs. deepening section) and in `student-tasks.md` (in the Overview section). The H2 label `🟢 MANDATORY —` itself stays as MANDATORY.

9. **Reflection-prompt count.** This plan requires "≥4 across the three lessons (≥1 per lesson)" in `self-study.md`. **Default assumption:** Rasmus aims for 4–5 prompts to give Wilhelm slack.

10. **Whether `overview.md` should preview Week 3.** **Default assumption:** `overview.md` does *not* preview Week 3 (it is a within-week document); only `self-study.md` and `slides.md` preview Week 3.

11. **30–50% rule — single contiguous block?** **Default assumption:** the plan uses a single contiguous 30–35 min block per 90-min lesson. Wilhelm accepts either a single block or up to two clearly-labelled "INDEPENDENT WORK" blocks summing to 27–45 min.

12. **`media/` subfolder.** No images are strictly required. **Default assumption:** Rasmus may include 0–2 simple Markdown diagrams (e.g. a tree sketch for decomposition) under `student/week-02/media/`, but is not required to. If no images, no `media/` folder.
