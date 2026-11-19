# Computational Thinking — Week 5 Plan (Sune, Gate #1)

Course: Computational Thinking (English)
Target: First-year vocational ICT students, ~15–17, no prior programming
Duration: 8 weeks × 3 lessons/week × 90 min = 24 lessons
Week 5 scope: L13 (Sequence), L14 (Conditions), L15 (Repetition) — the three classic logic structures.
Pipeline scope this run: Sune produces this Week 5 plan; Rasmus builds the full Week 5 package in the canonical weekly structure; Linnea/Wilhelm audit Week 5; Alfred packages a Markdown-only Week 5 release (no PDF, no PPTX rendering this round).

Week 5 inherits the form of the Week 1 release at `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/release/` and the depth/volume of the golden sample at `/Users/agent/ai-perusteet-md/student/lesson-01/`. The H2 headings in *this plan file* remain in Finnish per the Sune template; **all 7 of Rasmus's Week 5 files must be fully English**.

---

## Suunnitelma

### Course position of Week 5

Weeks 1–4 built the conceptual chassis: a computer is a literal follower (W1), big problems are broken into smaller ones (W2), processes can be described and reused (W3), and "correct" is not unique (W4). **Week 5 names the three structural moves that every described process is made of** — sequence, condition, repetition — and trains the student to recognise them in everyday speech *before* meeting them as code in Weeks 6–8. Week 5 is also the **immediate foundation week for AT2**, which asks for a process description that explicitly uses all three structures and is submitted at the end of Week 5 / during Week 6. The plan therefore treats Week 5 as scaffolding for an artefact, not as a free-standing topic.

### Week 5 theme statement

Almost any process can be described with three building blocks: **sequence** (do A, then B, then C), **condition** (if X, do A; otherwise do B), and **repetition** (do A until/while/for-each). Once a student can name these three in everyday situations — a recipe, a password rule, an inbox sweep — they have the skeleton of every program. Week 5 stays at the *naming* and *expressing-in-natural-language* level. **No code, no testing frameworks, no formal flowchart syntax beyond what Week 3 already covered.** Loose, pseudocode-like notation is allowed (`if … then …`, `repeat until …`, `for each …`) but it is treated as English shorthand, not as a formal language with parser-level rules.

### L13–L15 breakdown for Week 5

#### Lesson 13 — Sequence: a program proceeds step by step

- **Learning objectives** (Remembering + Understanding, light Applying):
  - (a) **Define** *sequence* in own words as "doing one step after another, in a fixed order". *(Remembering)*
  - (b) **Identify** the sequence in an everyday process (a recipe, a deployment checklist, a morning routine). *(Understanding)*
  - (c) **Explain** why the order of steps usually matters and give one example where swapping two steps breaks the process. *(Understanding)*
  - (d) **Write** a 6–10 step sequence for a familiar process, with the order made explicit by numbering. *(light Applying)*
- **Key vocabulary preview:** sequence, step, order, dependency (preview term: *condition*).
- **Central message (one sentence):** Sequence is the default — when nothing else is said, "do A, then B, then C" is what a literal follower will do, so the order you write is the order you get.

#### Lesson 14 — Conditions: if-then-else thinking and decision trees

- **Learning objectives** (Remembering + Understanding, light Applying):
  - (a) **Define** *condition* in own words as "a test that decides which step happens next". *(Remembering)*
  - (b) **Recognise** if/then/else shape in everyday rules (password rules, ticket-routing rules, "if it rains, take the bus"). *(Understanding)*
  - (c) **Explain** the difference between *if … then …* (no alternative) and *if … then … else …* (an alternative). *(Understanding)*
  - (d) **Draw** a simple two- or three-branch decision tree for a familiar everyday rule. *(light Applying)*
  - (e) **Express** a real-life rule in natural-language `if … then … else …` form. *(light Applying)*
- **Key vocabulary preview:** condition, test, branch, decision tree, if-then, if-then-else, AND, OR (informal). Preview term: *repetition*.
- **Central message (one sentence):** A condition is a test that splits the path of a process in two (or more), and naming the test in plain English is enough to make the split visible to a literal follower.

#### Lesson 15 — Repetition: doing the same thing multiple times

- **Learning objectives** (Remembering + Understanding, light Applying):
  - (a) **Define** *repetition* in own words as "doing the same step or block of steps more than once". *(Remembering)*
  - (b) **Distinguish** *for each* (a known list), *repeat until* (a stopping condition), and *while* (a continuing condition) in everyday situations. *(Understanding)*
  - (c) **Identify** repetition in familiar processes (an inbox sweep, marking attendance, charging a phone). *(Understanding)*
  - (d) **Express** a real-life repeated action in natural language with an explicit stopping or continuing condition. *(light Applying)*
  - (e) **Spot** the difference between a one-off step and a repeated step in a process description. *(Understanding)*
- **Key vocabulary preview:** repetition, loop (informal), for-each, repeat-until, while, stopping condition, counter (light, informal). Preview term: *pseudocode* (Week 6).
- **Central message (one sentence):** Repetition is how you say "the same thing, again, with a clear stop" — and naming the stop in plain English is what separates a useful repetition from a runaway one.

### Week 5 — must-do minimum vs. deepening

**Must-do minimum (every student must leave Week 5 able to):**
- Name the three building blocks — sequence, condition, repetition — and recognise each one in a short everyday process.
- Express a single condition in natural-language `if … then … else …` form, anchored in a real-life rule.
- Express a single repetition in natural-language form with an explicit stop (`repeat until …`, `for each item in …`, `while … keep going`).
- Combine all three building blocks into one process description (3–6 sequence steps + at least one condition + at least one repetition) for a familiar task. This is the AT2-feeder artefact.

**Deepening (optional extension, not required for AT2 baseline):**
- Spot nested or compound conditions (`if A AND B` / `if A OR B`) in real rules they have seen.
- Notice and describe one edge case where a `repeat until` could loop forever, and add a safety stop in plain English.
- Apply the three building blocks to a vocational IT scene (a password-validation rule, an inbox sweep, a deployment checklist).
- Use an LLM as a sparring partner against their own decision tree, with a structured prompt and an explicit "do not accept the LLM's output verbatim" instruction.

### How Week 5 feeds AT2

AT2 (submitted end Week 5 / during Week 6) asks the student to describe a process they choose, in natural language, **with at least one sequence backbone, at least one condition, and at least one repetition**. The Week 5 must-do minimum is exactly that artefact at a smaller scale, so the AT2 submission is a controlled extension of the Week 5 mandatory task, not a leap. Every task's `### Keep your notes` block in `student-tasks.md` must remind the student that **the artefact they produce this week is the raw material for AT2** (not AT1, which has already been submitted by end of Week 2).

### How Week 5 hands off to Week 6

Week 6 (pseudocode and dry running) takes the natural-language sequence/condition/repetition descriptions from Week 5 and formalises them into pseudocode with variables and trace tables. The vocabulary preview at the end of Week 5 names **pseudocode** explicitly so students know what next week is for. Week 5 must not pre-empt Week 6 by introducing pseudocode syntax with strict rules; loose `if … then …` and `repeat until …` are fine, but formal indentation, variable assignment with `:=` or `=`, and trace tables stay in Week 6.

---

## Rajaukset

**Out of scope for Week 5:**
- **No code at all.** No JavaScript, no Python, no syntax-highlighted code fences for anything that looks like a programming language. The pseudocode-like notation that is allowed (`if … then …`, `repeat until …`, `for each …`) goes in *plain Markdown text or block quotes*, not in fenced code blocks tagged with a language. (Rasmus may use unlabelled fenced blocks for visual contrast on short examples.)
- **No formal pseudocode** with strict indentation, variable assignment, or operator semantics — that belongs in Week 6.
- **No testing frameworks** (jest, mocha, vitest, pytest, etc.) anywhere in any of the 7 files. This is a hard course-wide rule; Wilhelm greps.
- **No truth tables, no Boolean algebra notation** (`∧`, `∨`, `¬`). AND and OR appear only as plain English words in the deepening material.
- **No IDEs, no terminals, no install steps**, no developer tooling. Week 5 is paper-and-thinking.
- **No platform-side independent exercises** (those are produced by a different team).
- **No deep CS theory.** No automata, no halting problem (even informally — *runaway loop* is OK, *halting problem* is not), no Big-O.
- **No PDF, no PPTX rendering** in the pipeline this round. Alfred packages a Markdown-only Week 5 release.
- **No "(AI-resilient)" label** on tasks. The property is audited by Linnea; the label is internal and must not appear in any learner-facing file.

**Style guardrails:**
- **Everyday before IT, always.** The brief's named exemplars are mandatory: **password-validation rule (condition), inbox sweep (repetition), deployment checklist (sequence).** Each of these must appear at least once in `self-study.md` and be reused in `student-tasks.md` and `slides.md` so the everyday→IT pairing is visible across files.
- **"The computer is literal, not stupid."** Inherited from Week 1. The reframing is no longer the headline, but the phrasing "the computer is stupid" must not appear anywhere in Week 5 either.
- **No "computational thinking is just programming"** misconception; pre-empt as needed if the topic of conditions tempts a student to map them to `if` keywords. Week 5 still treats the three structures as *thinking moves first, syntax later*.

**Language:** English throughout. Börje (Finnish polishing) is skipped. The H2 headings in this plan file (`Suunnitelma`, `Rajaukset`, `Hyväksymiskriteerit`, `Briefing Rasmukselle`, `Avoimet kysymykset`) may stay in Finnish because they are part of the Sune template; **all 7 of Rasmus's Week 5 files must be fully English**, including their section headings.

**Pipeline scope this run:**
- Sune produces this Week 5 plan (you are reading it).
- Rasmus builds **only Week 5** in the canonical 7-file weekly structure (plus, at his discretion, one supplementary deck `slides-l14-decision-trees.md` if Lesson 14 needs deeper walkthrough scaffolding).
- Linnea and Wilhelm audit Week 5 only.
- Alfred packages a Markdown-only Week 5 release.

---

## Hyväksymiskriteerit

Wilhelm verifies the Week 5 package against the following concrete, checkable criteria.

### Structural — files and folders

1. **All 7 canonical files present**, with exactly these filenames (case-sensitive, lowercase, kebab-case):
   - `student/week-05/overview.md`
   - `student/week-05/self-study.md`
   - `student/week-05/student-tasks.md`
   - `student/week-05/vocabulary.md`
   - `student/week-05/slides.md`
   - `teacher/week-05/teacher-materials.md`
   - `teacher/week-05/in-class-tasks.md`
2. **At most one supplementary deck** under `student/week-05/`, named `slides-l14-decision-trees.md` (if Rasmus decides Lesson 14 needs it — see #16). No other extra files. No `.pptx`, no other slide formats. A `media/` subfolder allowed only if a slide explicitly references a contained image (not expected for Week 5).
3. **No `slides.pptx`, no `deck.md`, no Reveal.js HTML, no PDF** anywhere. Hard fail if found.

### Volume (sanity-check brackets, not hard limits)

4. `overview.md`: **200–400 words**.
5. `self-study.md`: **2400–4000 words** (covers L13, L14, L15 in one document, mirroring Week 1's structure).
6. `student-tasks.md`: **1000–2200 words**. **1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING** tasks (see #18).
7. `vocabulary.md`: **10–18 terms**, each with a 1–3 sentence English definition.
8. `slides.md`: **10–20 slides**, separated by `---` on their own line, each slide starting with an H1 (`#`) or H2 (`##`) title with 3–5 short bullets or 1–2 short sentences.
9. `teacher-materials.md`: **2800–4500 words**. Contains **3 × 90-minute lesson plans** (one per lesson), each with time slots summing to 90.
10. `in-class-tasks.md`: **500–1400 words**. Contains **at least 1 MANDATORY teacher-led in-class exercise**.
11. (Optional) `slides-l14-decision-trees.md`: **4–8 slides**, only if Rasmus ships it.

### Required H2 sections per file

12. `overview.md` must contain (in this order):
    - `## Week 5 theme`
    - `## What you will be able to do by the end of the week`
    - `## Must-do minimum vs. deepening` (using the exact phrasing **must-do minimum**, not "core minimum" and not "mandatory minimum")
    - `## How the three lessons fit together`
    - `## How this week feeds AT2`
13. `self-study.md` must contain:
    - `# <Week title>` (inviting H1, suggestion: *"Three moves: sequence, condition, repetition"* — Rasmus may improve).
    - `## Introduction` — names the central message of the week (verbatim form below).
    - `## Lesson 13 — Sequence: a program proceeds step by step` (or close variant).
    - `## Lesson 14 — Conditions: if-then-else thinking and decision trees`.
    - `## Lesson 15 — Repetition: doing the same thing multiple times`.
    - `## Summary and what comes next` — previews Week 6 (pseudocode + dry-running).
    - **At least 5 `> **Pause for a moment:**` reflection prompts** across the three lessons (≥1 per lesson, with at least 2 in the lesson Rasmus judges longest).
14. `student-tasks.md` must contain:
    - `## Overview of the week's tasks` — names the must-do minimum and reminds the student that **AT2 lands at end of Week 5 / during Week 6**, fed by this week's mandatory task.
    - One H2 per task, prefixed with `🟢 MANDATORY —` or `🟣 DEEPENING —`. **The phrase "must-do minimum" must appear in the Overview** (not "mandatory minimum"). **The label "(AI-resilient)" must not appear** anywhere.
    - Each task that assumes a partner / follower / tester has a `### If you are doing this alone` subsection with a concrete alternative (24h gap, video self, different device, class chat).
    - Each task ends with a `### Keep your notes` block referencing **AT2** explicitly (not AT1).
15. `vocabulary.md` must contain a single H2 `## Week 5 vocabulary`, then each term as an H3 or bolded definition list. **At least one term flagged as "looking ahead"** (suggested: *pseudocode* for Week 6).
16. `slides.md` must:
    - Start with a title slide.
    - Contain at least one slide whose body shows the **central message verbatim** (see #21).
    - Use `---` on its own line between slides.
    - Have no `.pptx` references and no speaker-note syntax that assumes a specific renderer.
    - **Supplementary deck `slides-l14-decision-trees.md`** is optional; if shipped, it must be 4–8 slides walking ONE everyday-then-IT decision tree (suggested pair: "should I take an umbrella?" → "should this login attempt be blocked?"). If Rasmus does not ship it, no penalty — the main deck must cover decision trees on at least one slide regardless.
17. `teacher-materials.md` must contain, with **exactly these H2 headings** (Wilhelm greps):
    - `## Week 5 learning objectives (mapped to Bloom)`
    - `## Common misconceptions for Week 5`
    - `## Lesson 13 — 90-minute plan`
    - `## Lesson 14 — 90-minute plan`
    - `## Lesson 15 — 90-minute plan`
    - `## Facilitation tips`
    - `## Answers to common student questions`
    - `## Formative assessment tips`
    - Each 90-min plan must include a **Slide cues** subsection (referencing the main deck and, if applicable, the supplementary deck).
    - **Common misconceptions for Week 5**: at least 6 across the week (≥2 per lesson), each with a `Correction:` line.
    - **Answers to common student questions**: at least 5 across the week.
17b. `in-class-tasks.md` must contain:
    - `## Overview`
    - At least 1 H2 task labelled **MANDATORY**, requiring teacher-led classroom interaction, cross-referenced from `teacher-materials.md`.

### Pedagogical rules

18. **30–50% rule**: in `teacher-materials.md`, each 90-minute plan has independent-student-work blocks summing to **27–45 minutes**. Wilhelm checks arithmetically.
19. **Bloom cap**: Week 5 objectives stay in Remembering + Understanding with **light Applying** allowed (express conditions and loops in natural language; draw a simple decision tree; combine the three structures in one process description). **Forbidden verbs** in Week 5 objectives: *create, build, design, develop, evaluate, judge, debug, optimise, decompose* (decompose belongs to Week 2; abstraction-heavy verbs belong to Week 3). *Analyze* may appear lightly only in the deepening tasks, not in objectives.
20. **The three building blocks must be named the same way everywhere**: *sequence*, *condition*, *repetition*. Synonyms (selection, iteration, loop, branch) may appear in passing but the three nouns above are the canonical labels used in every file. Wilhelm greps for `sequence`, `condition`, `repetition` in `overview.md`, `self-study.md`, `slides.md` and `teacher-materials.md`.
21. **Central message verbatim** — *"Almost any process can be described with three building blocks: sequence, condition, and repetition."* — appears verbatim **on at least one slide** in `slides.md` and **at least once** in `self-study.md` (Introduction or Summary). Rasmus may extend the sentence with the brief's "Once you can name them in everyday tasks, you have the skeleton of every program." continuation.
22. **Everyday-before-IT principle**: in `self-study.md`, every section that uses both kinds of examples places the everyday example first. The brief's three exemplars must be honoured: **deployment checklist (sequence), password-validation rule (condition), inbox sweep (repetition)** — each one used at least once across the week, and each one paired with an everyday counterpart that comes first (e.g. recipe → deployment checklist; "if it rains, take the bus" → password-validation rule; emptying a dishwasher → inbox sweep).
23. **No code anywhere** in any of the 7 files. Pseudocode-like notation in natural-language fragments is fine; fenced code blocks with a language tag are not. Wilhelm greps for ` ```js`, ` ```javascript`, ` ```python`, ` ```ts`, etc.
24. **No testing frameworks** mentioned anywhere.
25. **"The computer is literal, not stupid."** The phrase "the computer is stupid" / "the computer is dumb" must not appear.
26. **AT2, not AT1.** Every `### Keep your notes` block in `student-tasks.md` references **AT2 (end of Week 5 / during Week 6)**, not AT1.

### Tasks (selection rules)

27. `student-tasks.md` contains **1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING** tasks. At least **one MANDATORY task** is the AT2 feeder — it asks the student to produce a process description combining sequence + condition + repetition.
28. Each task that assumes a partner / follower / tester has an `### If you are doing this alone` subsection. Wilhelm greps for the exact heading.
29. If a DEEPENING task uses an LLM as a sparring partner, it must include a fenced code block with a sample prompt and an explicit "do not accept the LLM's output verbatim" instruction.

### In-class tasks

30. `in-class-tasks.md` contains **at least 1 MANDATORY teacher-led in-class exercise** that genuinely requires classroom interaction. Default mandatory: the "find the loop / find the if" classification game on real-life examples (see Briefing Rasmukselle below). Default optional: a live decision-tree exercise on a chosen everyday rule. Both must be cross-referenced from the relevant 90-min plan in `teacher-materials.md`.

### Language and polish

31. **English throughout**, all 7 files (and the optional supplementary deck if shipped).
32. **Register**: `self-study.md`, `student-tasks.md`, `overview.md`, `vocabulary.md` and `slides.md` at CEFR ~B1; `teacher-materials.md` and `in-class-tasks.md` at CEFR ~B2.
33. **Valid Markdown**: every code fence closes, every table renders, no broken internal links, `---` separators in `slides.md` alone on their own line.

---

## Briefing Rasmukselle

### Cross-cutting reminders (apply to all 7 files)

- **Everyday before IT, always.** The brief locks the three exemplars: **deployment checklist (sequence), password-validation rule (condition), inbox sweep (repetition).** Each must appear, and each must be preceded by an everyday counterpart on first introduction. Suggested everyday pairings: a tea recipe / a morning routine → deployment checklist; "if it rains, take the bus" / "if the milk smells off, throw it out" → password-validation rule; emptying a dishwasher / marking attendance → inbox sweep.
- **Three building blocks, three names.** Use *sequence*, *condition*, *repetition* as the canonical labels in every file. Synonyms (selection, branch, loop, iteration) may appear once in self-study with the canonical name in parentheses, but do not switch labels mid-document.
- **No code, no testing frameworks, no formal pseudocode.** Natural-language pseudocode-like fragments (`if it rains, then take the bus, else walk`, `for each message in the inbox, …`, `repeat until the inbox is empty`) are fine — they go in plain Markdown text or in `>` block quotes, not in fenced code blocks tagged with a programming language. Short unlabelled fenced blocks for visual contrast are acceptable.
- **"The computer is literal, not stupid."** Inherited from Week 1. Do not write "the computer is stupid/dumb" anywhere.
- **AT2, not AT1.** Every `### Keep your notes` references AT2.
- **No "(AI-resilient)" label.** Linnea audits the property, not the label.
- **Central message verbatim** must appear on a slide AND in `self-study.md`: *"Almost any process can be described with three building blocks: sequence, condition, and repetition."*
- **Bloom cap.** Light Applying only. The student *expresses* a condition and a loop in natural language; they do not *implement*, *debug* or *optimise* anything.
- **Reuse the Week 1 release form.** Mirror the file shapes at `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/release/`. Same headings, same depth, same "Pause for a moment" prompt convention.

---

### File 1 — `student/week-05/overview.md` (200–400 words)

**Required H2 structure (in order):**
1. `## Week 5 theme` — one short paragraph naming the three building blocks and the central message. State the central message *verbatim* (Rasmus's choice whether to bold or italicise — it must be there word for word).
2. `## What you will be able to do by the end of the week` — bullet list of 5–7 plain-English "can do" statements, mapped to the L13–L15 objectives but stated in student-facing language. Suggested set:
   - Name and recognise sequence, condition and repetition in an everyday process.
   - Write a 6–10 step sequence with the order made explicit by numbering.
   - Express an everyday rule as `if … then … else …` in plain English.
   - Draw a small decision tree (two or three branches) for a familiar rule.
   - Express a repeated action in plain English with an explicit stop (`repeat until …`, `for each item in …`).
   - Combine all three structures into one short process description for a familiar task.
3. `## Must-do minimum vs. deepening` — two-column or two-bullet contrast. The mandatory column must include the AT2 feeder task. The deepening column must include the AND/OR compound condition idea, the runaway-loop edge case, the vocational angle, and the LLM-sparring option.
4. `## How the three lessons fit together` — one short paragraph showing the L13 → L14 → L15 arc (the *default*, then *the test that splits it*, then *the test that loops it*).
5. `## How this week feeds AT2` — two to three sentences. Name AT2 explicitly. Say that the mandatory task this week *is the AT2 artefact at a smaller scale*, and that keeping notes is non-negotiable.

**Examples to lean on:** a tea recipe and a deployment checklist (sequence); "if it rains, take the bus" and a password-validation rule (condition); marking attendance and an inbox sweep (repetition).

**Length target:** ~300 words.

---

### File 2 — `student/week-05/self-study.md` (2400–4000 words)

**Required structure (in order):**

- `# <Week title>` — suggestion: *"Three moves: sequence, condition, repetition"*. Rasmus may improve.
- `## Introduction` (~250–400 words)
  - Open with a familiar 15-year-old scene that mixes all three moves without naming them — e.g. *"You wake up. You check your phone. If it is past 7:30, you skip breakfast; otherwise you eat. Then you walk to school. On the way you check every traffic light: if it is red, you stop; if it is green, you keep going. You repeat this for every crossing until you are at the gate."*
  - Then surface the names: **that scene has all three building blocks at work.**
  - State the central message **verbatim**: *"Almost any process can be described with three building blocks: sequence, condition, and repetition."* Continue with the brief's: *"Once you can name them in everyday tasks, you have the skeleton of every program."*
  - Name AT2 (end of Week 5 / during Week 6) and say the week is a feeder.

- `## Lesson 13 — Sequence: a program proceeds step by step` (~600–900 words)
  - `### What sequence means` — short definition: "doing one step after another, in a fixed order, unless the instruction tells you otherwise." Note: sequence is the **default** — when no condition or repetition is written, a literal follower walks the steps top-to-bottom.
  - `### Sequence in everyday processes` — **everyday first.** Walk one familiar process step-by-step (suggested: making tea or a morning routine), numbering each step. Then **swap two steps** (e.g. "pour boiling water" before "put the tea bag in the mug") and ask the reader what happens. The point: order matters because steps **depend** on earlier steps.
  - `### Sequence in an IT context` — the brief's exemplar: a **deployment checklist** in plain English (e.g. *"merge the branch → run the build → run the smoke tests → deploy to staging → notify the team → wait for sign-off → deploy to production"*). Note that several of these steps cannot be reordered without breaking the process.
  - `### Independence vs. dependency` — gentle introduction: some steps can be reordered (e.g. brushing teeth before or after dressing); some cannot (e.g. boil the water before pouring it). Do not formalise dependency graphs — this is Week 3 territory revisited. Keep it intuitive.
  - **≥1 `> **Pause for a moment:**` prompt.** Suggested: *"Write down a 3-step everyday process where the order can be swapped, and another 3-step process where it cannot. What word would you use to describe the difference?"*

- `## Lesson 14 — Conditions: if-then-else thinking and decision trees` (~700–1000 words)
  - `### What a condition is` — short definition: "a test that decides which step happens next." A condition is the moment in a process where the path splits.
  - `### Everyday conditions you already use` — **everyday first.** Three short examples:
    - *"If it rains, take the bus; otherwise walk."* — `if … then … else …`.
    - *"If you finish your homework before dinner, you can play games."* — `if … then …` (no else).
    - *"If the milk smells off, throw it out."* — `if … then …` (one-branch).
  - `### Writing a condition in natural language` — introduce the casual notation `if … then …` / `if … then … else …` (not fenced as code; in plain text). Show two or three rules expressed both as a natural sentence and as the casual shape. **No code blocks tagged with a language.**
  - `### Decision trees — drawing the split` — explain a decision tree as a picture of the condition. Show a 2-branch tree for "if it rains, bus; else walk" and a 3-branch tree for "if it rains, bus; else if you are late, run; else walk." Keep diagrams ASCII or Mermaid-free; describe how to draw it on paper.
  - `### Conditions in an IT context — password validation` — the brief's exemplar. Walk a real-feel password rule in natural language: *"If the password is shorter than 8 characters, reject it. If it has no number, reject it. If it has no capital letter, reject it. Otherwise accept it."* Show the same as a small decision tree.
  - `### Compound conditions — AND, OR (informal, optional reading)` — short paragraph. Use plain English words *and* and *or*. **No Boolean symbols.** Example: *"If you have your bus card AND there is money on it, take the bus."* Mark this subsection as *deepening reading* if the reader is comfortable.
  - **≥2 `> **Pause for a moment:**` prompts.** Suggested: (i) *"Write down a rule someone in your family uses with you that has the shape if … then … else … . What is the test?"* (ii) *"Look at a website's sign-up form. Can you name three different conditions the form is checking before it lets you submit?"*

- `## Lesson 15 — Repetition: doing the same thing multiple times` (~700–1000 words)
  - `### What repetition means` — short definition: "doing the same step or block of steps more than once, with a stopping condition that tells the follower when to stop."
  - `### Everyday repetitions you already use` — **everyday first.** Three short examples:
    - *"Mark each name in the register present or absent."* (`for each name in the register, …`).
    - *"Keep adding sugar and stirring until it tastes right."* (`repeat until …`).
    - *"While the kettle is still hot, you don't need to boil it again."* (`while …`).
  - `### Three shapes of repetition` — give the three casual shapes side by side:
    - **For each** — "for each item in a list, do …". Use when the list is known in advance.
    - **Repeat until** — "do … until a stopping condition is true". Use when the stop depends on what happens.
    - **While** — "while a condition is true, keep doing …". Use when the test is checked before each repeat.
    - Keep this informal; do not draw a flowchart for each.
  - `### Repetition in an IT context — the inbox sweep` — the brief's exemplar. Walk the natural-language process: *"For each unread message in the inbox, decide: if it is from a person, mark it for reply; if it is a newsletter, archive it; if it is spam, delete it. Repeat until the inbox is empty."* Point out: this is one process that uses **all three building blocks** — a sequence per message, a condition per decision, a repetition over the inbox.
  - `### The stopping condition is the safety belt` — gentle warning about runaway repetitions. Use the homework example: *"Keep working on it until you understand"* — what if you never understand? Show that *every* repetition needs an honest, observable stop. **Do not use the word "infinite loop"** as a horror term; use "runaway repetition" or "no honest stop" in plain English.
  - `### Counters (light, informal)` — *if needed*, one short paragraph: sometimes the stop is a count ("do this five times"). Treat the count as a kind of `for each` over the numbers 1 to 5. No variable syntax. This subsection may be skipped if it crowds the lesson.
  - **≥2 `> **Pause for a moment:**` prompts.** Suggested: (i) *"Name one thing you did today that was a repetition. What was the stopping condition?"* (ii) *"Imagine a 'repeat until …' with no stop you can actually observe. What goes wrong?"*

- `## Summary and what comes next` (~200–350 words)
  - Close the loop: re-state the central message verbatim if it was not in the Introduction.
  - Make the AT2 connection explicit: the artefact you produce in this week's mandatory task is the same shape as AT2, just smaller.
  - Preview Week 6 (pseudocode + dry-running). Say: *"Next week we tighten these natural-language descriptions into something a little closer to code — but still on paper. It is called pseudocode."*

**Examples menu Rasmus should pick from (everyday first, IT second):**
- Sequence (everyday): tea recipe, morning routine, sandwich, route to school, getting ready for bed.
- Sequence (IT): deployment checklist; first-line help-desk ticket triage; "what to do when the printer doesn't work" runbook.
- Condition (everyday): "if it rains, take the bus", "if the milk smells off, throw it out", "if you finish homework before dinner, you can play games", "if you have your bus card AND there is money on it, …".
- Condition (IT): password validation, login attempt (lock account after 3 failed tries), spam filter rule, ticket routing rule ("if from a teacher, priority 1; else priority 3").
- Repetition (everyday): marking attendance, doing reps in a gym set, peeling a bag of potatoes, brushing each tooth.
- Repetition (IT): inbox sweep, processing each row of a spreadsheet by hand, checking each item in a delivery against a packing list.

**Length target:** ~3000 words.

---

### File 3 — `student/week-05/student-tasks.md` (1000–2200 words)

**Required structure:**

- `## Overview of the week's tasks` — 3–4 sentences. State that the 🟢 MANDATORY task is the **must-do minimum** and the 🟣 DEEPENING tasks are optional extensions. Remind that **AT2 lands at the end of Week 5 / during Week 6** and that the mandatory task this week is the AT2 artefact at a smaller scale.

**Five candidate task ideas (Rasmus keeps 1–2 MANDATORY + 2–3 DEEPENING). Default selection at the bottom.**

**Task 5.1 — 🟢 MANDATORY — "Three moves in one process"** *(AT2 feeder)*
- Student picks a familiar process they really do (laundry; making breakfast; checking the family chat; closing all browser tabs at end of school day; on phone, going through every photo from the weekend and choosing which to keep).
- They describe the process in plain English with **all three building blocks**:
  - A sequence of 3–6 steps as the backbone.
  - At least one `if … then … else …` condition with a test named in plain English.
  - At least one repetition with an explicit stop (`for each …`, `repeat until …`, or `while …`).
- They draw the condition as a small decision tree on paper or in a notes app (rough sketch is fine).
- They write a 3–5 sentence reflection: *which building block was hardest to name? where did the boundary between sequence and repetition blur?*
- **Why MANDATORY:** this is the AT2 artefact in miniature. Linnea audits whether the task is AI-resilient by construction (it is — anchored in the student's own process, requires an observable artefact with a hand-drawn tree, and demands a reflection on a real decision the student made).
- **`### If you are doing this alone`** — not strictly needed here (no partner assumed). Rasmus may omit, OR include a 1-sentence "you can pick a process you do entirely alone, like brushing your teeth or charging your phone overnight — no follower needed."

**Task 5.2 — 🟢 MANDATORY (alternative to 5.1) — "Find the three in someone else's process"**
- Student finds a real process description in the wild — a recipe from a parent, a school protocol PDF, a how-to from a YouTube video transcript, a help-desk reply they have received.
- They annotate the document by underlining (or copying out) every sequence backbone, circling every condition, and boxing every repetition. They write a short sentence next to each marking explaining the shape.
- They then **rewrite one paragraph** of the process in cleaner natural-language `if … then … else …` and `for each / repeat until` form, keeping the meaning identical.
- **Why MANDATORY-candidate:** AT2-aligned but the artefact is annotation + rewrite rather than original writing. Rasmus picks 5.1 *or* 5.2 as the mandatory backbone (default: 5.1). The other can be shipped as a 🟣 DEEPENING.

**Task 5.3 — 🟣 DEEPENING — "Decision tree for a real rule"**
- Student picks a real rule from their own life that has at least two branches (the school's lateness policy; the family rule about screens after dinner; a website's account-recovery flow; a job application's eligibility checklist).
- They draw a decision tree with 2–4 branches, name the test on each branch in plain English, and write 3–5 sentences about which branch is hardest to test honestly.
- Optional: they spot **one compound condition** (AND or OR) in the rule and rewrite it as two simpler tests.
- **`### If you are doing this alone`** — not strictly needed (no partner assumed). Rasmus may include the 24-hour gap as a self-check ("come back tomorrow and re-draw the tree from memory; did you remember every branch?").

**Task 5.4 — 🟣 DEEPENING — "The stopping condition is the safety belt"** *(edge-case work)*
- Student writes three short repetitions in plain English (e.g. *"Keep refreshing the page until the seat is available"* / *"For each photo, decide if it should be deleted"* / *"While the train hasn't arrived, keep checking the platform sign"*).
- For each, they ask: **what if the stop never happens?** They describe the runaway case in one sentence and add a safety stop in plain English (e.g. *"…or stop after 10 tries"*, *"…or after 30 minutes"*).
- **Why deepening:** edge-case thinking; harder than expressing a single loop.
- No partner needed; no `### If you are doing this alone` block required.

**Task 5.5 — 🟣 DEEPENING — "Vocational angle: password rule, ticket routing, or inbox sweep"** *(LLM sparring optional)*
- Student picks **one** of the three classic vocational scenes:
  - A password-validation rule (express the conditions in `if … then … else …` form).
  - A help-desk ticket routing rule (express as a small decision tree).
  - An inbox sweep (express as a `for each … if … then … else …` repetition with conditions inside it).
- They write the rule in plain English and draw the decision tree if relevant.
- **Optional LLM sparring step** — only here in Week 5. Provide the structured prompt below in a **fenced code block** and instruct: *"do not accept the LLM's output verbatim — for every suggestion, decide whether to keep, modify or reject it, and write one sentence next to each saying why."*

  Sample prompt to include verbatim:
  ```
  You are my sparring partner, not my teacher. I am a vocational ICT
  student practising sequence, condition and repetition in plain English.

  Below is my description of a [password rule / ticket routing rule /
  inbox sweep] using "if … then … else …" and "for each …" / "repeat
  until …" in natural language:

  [paste your description here]

  Please challenge me:
  - Is any condition I wrote ambiguous? Name the ambiguous word.
  - Is any repetition missing an honest stopping condition?
  - Did I confuse a one-off step (sequence) with a repeated step?
  Do not give me the "right" answer outright. Ask me a question that
  helps me see the gap myself.
  ```
- **`### If you are doing this alone`** — not strictly needed (no human partner assumed in the LLM variant). If Rasmus offers a "test it with a classmate who plays the validator" variant, that variant must carry the heading.

**Default selection Rasmus should ship:**
- 🟢 MANDATORY: **Task 5.1** (*Three moves in one process* — the AT2 feeder).
- 🟣 DEEPENING: **Task 5.3** (*Decision tree for a real rule*), **Task 5.4** (*The stopping condition is the safety belt*), **Task 5.5** (*Vocational angle*).
- Task 5.2 is held in reserve: Rasmus may swap it in as a second MANDATORY or as a fourth DEEPENING if Linnea/Wilhelm request more annotation practice.

Each task ends with a `### Keep your notes` block referencing **AT2 (end of Week 5 / during Week 6)** — not AT1. Suggested phrasing: *"Keep your process description, your decision tree, and your reflection in the same notebook. AT2 lands at the end of this week / during Week 6 and will ask you to scale exactly this artefact up."*

**Length target:** ~1500 words.

---

### File 4 — `student/week-05/vocabulary.md` (10–18 terms)

**Required terms** (Rasmus may add 1–4 of their own, but must not skip any required ones):
1. Sequence
2. Step (revisited from Week 1; refresh the definition)
3. Order
4. Dependency *(light — "step B needs the result of step A")*
5. Condition
6. Test (revisited from Week 1; new meaning: "the question a condition asks")
7. Branch
8. Decision tree
9. If-then
10. If-then-else
11. Repetition
12. For-each
13. Repeat-until
14. While
15. Stopping condition
16. **Pseudocode** — flagged as **"looking ahead — central topic of Week 6"**.

Optional additions Rasmus may include if useful: *counter* (light, informal), *runaway repetition*, *AND / OR (informal compound condition)*, *loop* (synonym for repetition, flag it as such).

Each definition is 1–3 sentences, plain English, with a short everyday example where natural.

**Length target:** ~14 terms.

---

### File 5 — `student/week-05/slides.md` (10–20 slides; target 14–17)

**Recommended slide outline (Rasmus may adjust order and titles within the spirit of the structure):**

1. `# Week 5 — Three moves: sequence, condition, repetition` *(title slide)*
2. `## The central message` — body: the central message **verbatim**. *"Almost any process can be described with three building blocks: sequence, condition, and repetition."*
3. `## What this week trains` — 3-bullet preview of L13 (sequence), L14 (conditions), L15 (repetition).
4. `## Sequence — the default move` — short definition + 2-line example (a tea recipe in 4 numbered steps).
5. `## When order matters` — side-by-side: two orderings of the same recipe, one works, one doesn't.
6. `## Sequence at work — deployment checklist` — short list (merge → build → smoke test → deploy to staging → sign-off → deploy to production).
7. `## Condition — a test that splits the path` — short definition + the `if it rains, take the bus, else walk` example.
8. `## if … then … else …` — the casual notation on one slide, with one everyday and one IT example side by side. **Not fenced as code.**
9. `## Decision tree — drawing the split` — a small two-branch tree shown in ASCII or as a description of the branches.
10. `## Condition at work — password validation` — the password rule in natural language; 3–5 short bullets.
11. `## Repetition — doing it again, with a stop` — short definition + the everyday example "mark each name in the register".
12. `## Three shapes of repetition` — for each / repeat until / while, one line each.
13. `## Repetition at work — the inbox sweep` — the inbox sweep in natural language; flag that it uses all three building blocks.
14. `## The stopping condition is the safety belt` — short slide on runaway repetitions and honest stops.
15. `## Three moves in one process` — visual of one short process with sequence-backbone, one condition, one repetition labelled.
16. `## Must-do minimum vs. deepening` — two-column contrast.
17. `## Tasks this week` — 1 line per task (5.1 mandatory; 5.3, 5.4, 5.5 deepening).
18. `## What comes next: Week 6 — pseudocode` — preview.
19. `## Recap — the central message, one more time` — central message **verbatim** again (satisfies the verbatim requirement explicitly alongside slide #2).

Aim ~15–17 slides. Use `---` on its own line between every slide. Body content: 3–5 short bullets or 1–2 short sentences. No `.pptx` references.

---

### Supplementary deck — `student/week-05/slides-l14-decision-trees.md` (4–8 slides; OPTIONAL)

**Need assessment.** Lesson 14 (conditions + decision trees) is the densest 90-min slot of the week: students meet *condition*, *if-then-else*, *decision tree*, and (optionally) *AND / OR compound conditions* all in one lesson. Rasmus should ship a supplementary deck **if** the main deck's slides 7–10 feel cramped or if he wants to give the teacher a "walk one decision tree slowly, end to end" option for Lesson 14's lecture segment.

**If shipped, 4–8 slide sketch:**

1. `# Decision trees — one tree end to end` *(title slide)*
2. `## The everyday rule` — *"Should I take an umbrella today?"* — show the verbal rule: *"If it is raining now, yes. If it is not raining but the forecast says rain, yes. Otherwise no."*
3. `## Draw the tree — branches and tests` — render the three-branch tree in ASCII or in described form: root question, "raining now?", then "forecast says rain?", three leaves.
4. `## Express the rule in natural-language if … then …` — write the same rule as casual notation on one slide. **Not fenced as code.**
5. `## The IT mirror — should this login attempt be blocked?` — *"If the password is wrong AND it is the 4th try in 5 minutes, block. If the password is wrong but fewer than 4 tries, retry. If the password is right, log in."* Show the tree.
6. `## Same shape, different scene` — side-by-side: the umbrella tree and the login tree. Identical shape, different tests.
7. `## Naming the test honestly` — closing slide: the quality of a decision tree is the quality of the tests on its branches. *"Is it raining now?"* is honest. *"Will it rain at some point?"* is not.

**If Rasmus does not ship the supplementary deck**, the main deck must still cover decision trees on at least one slide (slide #9 in the outline above). No penalty for skipping; default assumption is **YES — ship it**, because Lesson 14 is the densest.

---

### File 6 — `teacher/week-05/teacher-materials.md` (2800–4500 words)

**Required H2 sections (in this exact wording — Wilhelm greps):**

1. `## Week 5 learning objectives (mapped to Bloom)` — restate L13–L15 objectives from this plan, grouped by Bloom stage. Remembering + Understanding dominant; light Applying acceptable.

2. `## Common misconceptions for Week 5` — at least 6 across the week (≥2 per lesson). Suggested set:
   - **L13:** *"Sequence is too trivial to count as a building block."* → Correction: most real bugs come from a single swapped step. Sequence is the default and the default is where breakdowns happen. // *"If I don't write a condition, the process has no decisions."* → Correction: it just means every step is unconditional — sequence is the *absence of branching*, not the absence of importance.
   - **L14:** *"`if … then …` is the same as `if … then … else …`."* → Correction: `if … then …` with no else means "do nothing extra otherwise"; `else` says what to do instead. The follower behaves differently. // *"Compound conditions are advanced and I should avoid them."* → Correction: you already use AND and OR every day ("if I have my card AND money on it"). Naming them is fine. Only the symbols are advanced; the thinking is not.
   - **L15:** *"A loop is just a sequence written down many times."* → Correction: a loop is a single statement plus a stopping condition. If you have to write it out 100 times, you have not understood repetition. // *"`repeat until` always stops."* → Correction: it stops if and only if the stopping condition can actually be observed and reached. *"Repeat until you understand"* is not a stop.

3. `## Lesson 13 — 90-minute plan` — concrete time slots summing to 90, with an independent-student-work block of **27–45 min**. Suggested skeleton:
   - 0–10 min: warm-up — class names three everyday sequences on the board; teacher swaps two steps in one and asks what happens.
   - 10–25 min: instructor input — define sequence; show one everyday sequence and one IT sequence (deployment checklist) side by side.
   - 25–55 min: **INDEPENDENT WORK** (30 min) — students write a 6–10 step sequence for a process they really do, numbering every step, with explicit input and output (this kicks off the AT2-feeder task; conditions and repetition will be added in L14/L15).
   - 55–75 min: pair activity — students swap sequences, swap any two steps the partner thinks might still work, hand it back; the writer tries to break it.
   - 75–85 min: whole-class debrief — collect 2–3 cases where the order really mattered; build an "order matters / order doesn't" two-column board.
   - 85–90 min: preview of Lesson 14 (conditions).
   - **Slide cues** subsection: warm-up no slides; lecture slides 4 → 6 (Sequence + When order matters + Deployment checklist); independent work no slides (or leave slide 5 up as silent reminder); pair activity no slides; debrief no slides (use the board); closing no slides.

4. `## Lesson 14 — 90-minute plan` — same arithmetic constraint. Suggested:
   - 0–10 min: warm-up — teacher writes a verbal everyday rule on the board (*"if it rains, take the bus, else walk"*) and asks the class to draw the tree on paper in 2 minutes.
   - 10–30 min: instructor input — define condition; walk through `if … then …`, `if … then … else …`, and `if … then … else if … then … else …`. Walk one decision tree end-to-end (umbrella rule). **This is the segment where the supplementary deck — if shipped — gets used in full.**
   - 30–55 min: **INDEPENDENT WORK** (25 min) — students extend their L13 sequence by adding at least one condition with an `if … then … else …` test named in plain English. They also draw the condition as a small tree.
   - 55–80 min: **MANDATORY teacher-led in-class activity** — *"Find the if"* classification game (see `in-class-tasks.md`). Teacher reads short everyday/IT statements; class classifies each as containing a condition (and what test) or not.
   - 80–88 min: whole-class debrief — which statements were hardest to classify? where was the test hidden?
   - 88–90 min: preview of Lesson 15 (repetition).
   - **Slide cues** subsection: warm-up uses slide 7 (Condition — a test that splits the path); lecture slides 7 → 10 (Condition + if/then/else + Decision tree + Password validation); **if supplementary deck shipped**, run it between slides 9 and 10 of the main deck; independent work leave slide 8 up; in-class activity no slides; debrief no slides; closing no slides.

5. `## Lesson 15 — 90-minute plan` — same arithmetic constraint. Suggested:
   - 0–10 min: warm-up — class calls out three repetitions they have done so far today (brushing teeth, walking past 10 traffic lights, refreshing a chat for new messages); collect on the board.
   - 10–28 min: instructor input — define repetition; show the three shapes (for each / repeat until / while) with one example per shape; introduce "the stopping condition is the safety belt".
   - 28–58 min: **INDEPENDENT WORK** (30 min) — students add a repetition to their L13+L14 process and write an explicit stopping condition. They also write one sentence describing what the runaway case would look like.
   - 58–80 min: **OPTIONAL but recommended teacher-led activity** — *"Find the loop"* classification game (companion to L14's "Find the if"). Teacher reads short everyday/IT statements; class classifies each as containing a repetition (and what stop) or not. This is the second half of the classification game in `in-class-tasks.md`; teachers may run only "Find the if" in L14 and only "Find the loop" in L15, or run a combined version across both.
   - 80–88 min: whole-class debrief — collect three runaway cases ("repeat until you understand", "while the page is still loading", "for each thing on the list"); discuss what an honest stop would look like.
   - 88–90 min: preview Week 6 (pseudocode + dry-running). Mention that AT2 is due end of this week / during Week 6.
   - **Slide cues** subsection: warm-up no slides; lecture slides 11 → 14 (Repetition + Three shapes + Inbox sweep + Stopping condition); independent work leave slide 12 up; in-class activity no slides; debrief no slides; closing slide 18 (What comes next: Week 6) then slide 19 (Recap — central message verbatim).

6. `## Facilitation tips` — at least 5 short tips. Suggested:
   - **Insist on the canonical labels.** *Sequence, condition, repetition.* Synonyms (selection, branch, loop, iteration) are fine, but always pair them with the canonical name the first time.
   - **Lead with the everyday example. Always.** Same rule as Week 1. The password-validation rule, the inbox sweep and the deployment checklist arrive *after* a tea recipe, an "if it rains, take the bus", and a "mark each name in the register".
   - **Protect the independent-work block.** Week 5 builds the AT2 artefact across three lessons. If a 90-min plan slips, the cut comes from the whole-class debrief, not from the independent-work block.
   - **Don't slip into code.** When a student naturally writes `if (x > 0) {` or similar, gently rewrite on the board as `if x is greater than 0, then …` in plain English. Code arrives in Week 7, not Week 5.
   - **Name the test, not the answer.** When a student draws a decision tree with a vague branch like *"if it goes wrong"*, push: *"what specific test would a literal follower do to know it went wrong?"*
   - **Honest stops.** When a student writes *"repeat until done"*, ask: *"how does the follower know it is done? What would they look at?"* If the answer is *"they just know"*, the stop is not honest yet.

7. `## Answers to common student questions` — at least 5 across the week. Suggested:
   - *"Is `if … then …` the same as `if … then … else …`?"* — No. Without `else`, the follower does nothing extra otherwise. With `else`, the follower does something different.
   - *"Can a condition have more than two branches?"* — Yes, with `else if`. Three or four branches are normal; more than five usually means the rule is hiding a deeper structure.
   - *"Is `for each` a loop or a sequence?"* — A loop (repetition). It does the same thing once for every item, and the list of items is the stopping condition.
   - *"What if my `repeat until` could go on forever?"* — Add a safety stop: `or stop after N tries`, `or stop after 30 minutes`. Every honest repetition has at least one observable stop.
   - *"Is this on AT2?"* — Yes. The artefact you build across L13, L14 and L15 is the AT2 artefact at a smaller scale. Keep your notes.
   - *"Can I use code in AT2?"* — Not yet. AT2 is natural language with `if … then … else …` and `for each / repeat until / while` as loose, English-style notation. Pseudocode (slightly more formal) is introduced next week, in Week 6.

8. `## Formative assessment tips` — 3–5 quick checks. Suggested:
   - **Exit ticket after L13:** *"Name the sequence backbone of a process you ran today."* One sentence per student.
   - **Board vote after L14:** show three short rules and ask the class which has the most branches in its decision tree.
   - **Sticky-note collection after L15:** each student writes one "runaway repetition they have heard or said" on a sticky note. Read 3 at random; class proposes a safety stop for each.
   - **One-minute paper at end of week:** *"In one sentence, name the building block you find easiest to spot, and the one you find hardest."*

Cross-reference `in-class-tasks.md` from L14 and L15. The classification game is the mandatory anchor for the week.

**Length target:** ~3500 words.

---

### File 7 — `teacher/week-05/in-class-tasks.md` (500–1400 words)

**Required structure:**
- `## Overview` — 2–3 sentences naming the tasks and when in the week they fit.
- At least 1 H2 task labelled **MANDATORY**.

**Two concrete activity ideas Rasmus should ship (default: both):**

**Activity A — MANDATORY — "Find the if / Find the loop" (classification game)** *(whole-class + teacher-led, 25 min per half, slotted in L14 and L15)*
- Teacher prepares **two stacks of slips** (or a slide list):
  - Stack 1 — **Conditions:** ~10 short statements, some containing a condition and some not. Mix everyday and IT. Suggested seeds: *"If the password is shorter than 8 characters, reject it."* / *"Boil the water."* / *"If it rains, take the bus, else walk."* / *"Pour 30 ml of milk into the mug."* / *"If the user has not logged in for 90 days, deactivate the account."* / *"Add a teaspoon of sugar."* / *"If you finish your homework before dinner, you can play games."* / *"Switch the kettle on."*
  - Stack 2 — **Repetitions:** ~10 short statements. Suggested seeds: *"For each name in the register, mark present or absent."* / *"Make a cup of tea."* / *"While the kettle is still hot, do not boil it again."* / *"Repeat until the inbox is empty."* / *"Press the button once."* / *"For each photo on the phone, decide if it should be deleted."* / *"Keep refreshing the page until the seat is available."* / *"Open the front door."*
- Run order:
  1. **In Lesson 14 (60–80 min slot, 25 min):** teacher reads stack 1 one slip at a time. Class votes: *condition* or *no condition*. If condition, class names the test. Teacher writes the result on the board with the canonical `if … then … else …` shape if relevant.
  2. **In Lesson 15 (58–80 min slot, ~22 min):** teacher reads stack 2 one slip at a time. Class votes: *repetition* or *no repetition*. If repetition, class names the **stopping condition**. Teacher writes the result on the board with the canonical `for each / repeat until / while` shape.
- **Closing for each half:** one short whole-class question — *"Which slip was hardest to classify, and why?"*
- **Why MANDATORY.** This activity is the calibration moment of the week. Students cannot complete the AT2-feeder task confidently unless they can recognise the three building blocks in language they did not write themselves. The classroom version is faster and more diagnostic than asking each student to do it alone in their notebook.

**Activity B — OPTIONAL but recommended — "Live decision tree on the board"** *(whole-class + teacher-led, 20 min, slotted in L14, 30–55 min slot or as an alternative to part of the lecture)*
- Teacher picks one everyday rule the class will all know (suggested: the school's lateness policy; or the family rule about screens before bed; or "should I take an umbrella?"). Writes the rule in one sentence on the board.
- Step 1: **Identify the root question.** Class proposes a one-sentence test. Teacher writes it at the top of the tree.
- Step 2: **Branch.** Class proposes the two or three branches (yes / no, or three buckets). Teacher draws the lines.
- Step 3: **Test at each branch.** For each branch, class proposes what happens at the leaf — and whether there is *another* test waiting there.
- Step 4: **Spot the bad test.** Teacher invites the class to name *one* branch where the test is not honest — *"will I be late?"* is not honest until it becomes *"is it later than 8:15?"*. Rewrite the test on the board.
- Step 5: **Connect to AT2.** Teacher reminds: *"In your own AT2 artefact, every condition will have a tree like this hiding behind it. The honesty of the test matters more than the shape of the tree."*
- **Why OPTIONAL.** It overlaps with Activity A's classification game. If a teacher has time only for one, run Activity A — the classification game is more diagnostic and covers both conditions and repetitions. Activity B is the deeper option for classes that already feel confident.

Cross-reference both activities back to `teacher-materials.md` so the teacher knows the exact 90-min slot for each.

**Length target:** ~900 words.

---

## Avoimet kysymykset

1. **Supplementary deck — ship or hold?** This plan recommends shipping `slides-l14-decision-trees.md` (4–8 slides) because L14 is the densest lesson. **Default assumption:** Rasmus ships it. If he holds, the main deck must still cover decision trees on at least one slide.
2. **MANDATORY task choice — 5.1 or 5.2?** The brief allows 1–2 mandatory tasks. The AT2 alignment is cleaner with 5.1 (*Three moves in one process*) than with 5.2 (*Find the three in someone else's process*) because AT2 expects original writing. **Default assumption:** Rasmus ships 5.1 as the single MANDATORY task; 5.2 is held in reserve.
3. **AND / OR — keep in the everyday block or push to deepening?** Compound conditions are useful but risk crowding L14. **Default assumption:** keep the AND / OR subsection in `self-study.md` Lesson 14 marked as *deepening reading* (3–6 sentences max), and DO NOT include compound conditions in the must-do minimum.
4. **Counters in repetition — include or skip?** Counters are tempting because *"do this 5 times"* is intuitive, but introducing them flirts with variable assignment and is closer to Week 6. **Default assumption:** Rasmus may include one short paragraph in `self-study.md` Lesson 15 framed as *"sometimes the stop is a count — this is a kind of for-each over the numbers 1 to N"*. No variable syntax.
5. **`### If you are doing this alone` — required on Task 5.1?** Task 5.1 does not assume a partner. The brief says the heading is required *where a partner is assumed*. **Default assumption:** Rasmus may omit `### If you are doing this alone` from Task 5.1, OR include a 1-sentence "you can pick a process you do entirely alone" note. Tasks 5.2, 5.3, 5.5 likewise do not require it; Task 5.4 likewise. If Rasmus ships a partner-based variant of any task, the heading becomes mandatory there.
6. **Mermaid vs. ASCII for decision trees in slides.** Slides should render in plain Markdown. **Default assumption:** Rasmus uses **ASCII trees** or **described branches** (text only), not Mermaid syntax. Hand-drawn trees stay in the student's notebook, not in slides.
7. **Reflection-prompt count in `self-study.md`.** This plan requires ≥5 across the three lessons (≥1 per lesson). **Default assumption:** Rasmus ships 5–6 prompts, with at least 2 in L14 (the densest lesson).
8. **Word "loop".** *Loop* is a useful shorthand for *repetition* but the brief locks *repetition* as the canonical noun. **Default assumption:** Rasmus uses *repetition* as the primary label and may use *loop* once in `vocabulary.md` flagged as a synonym, plus inline in `self-study.md` Lesson 15 the first time as *"repetition (also called a loop in everyday tech speak)"*. After that, *repetition* throughout.
9. **Central-message length.** The brief's full central message is two sentences (*"Almost any process can be described with three building blocks: sequence, condition, and repetition. Once you can name them in everyday tasks, you have the skeleton of every program."*). **Default assumption:** the first sentence is the *verbatim* slide/self-study requirement; the second sentence is recommended but not mandatory.
10. **AT2 framing in `### Keep your notes`.** Some Week 1 release tasks reference AT1 with the phrase *"end of Week 2"*. For Week 5, the parallel is *"end of Week 5 / during Week 6"*. **Default assumption:** Rasmus uses the exact phrase *"AT2 lands at the end of Week 5 / during Week 6"* in every `### Keep your notes` block.
11. **Stack contents for the classification game.** This plan offers seed statements for both stacks in `in-class-tasks.md`. **Default assumption:** Rasmus ships exactly the seed lists in Activity A, or extends them by 2–4 each but does not shorten below 10 per stack.
12. **30–50% rule per lesson.** This plan budgets 30 / 25 / 30 minutes of independent work in L13, L14, L15 respectively (33% / 28% / 33% of 90 min). L14 sits at the lower bound because the in-class classification game eats 25 minutes; Wilhelm accepts 25 min as inside the 27–45 min range *only if* the independent-work block is genuinely independent. **Default assumption:** Rasmus tightens L14's independent-work block to **27–30 min** to stay safely inside the rule, trimming the lecture or the debrief if needed.
