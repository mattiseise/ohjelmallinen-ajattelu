# Computational Thinking — Week 1 Plan (Sune, Gate #1)

Course: Computational Thinking (English)
Target: First-year vocational ICT students, ~15–17, no prior programming
Duration: 8 weeks x 3 lessons/week x 90 min = 24 lessons
Pipeline scope this run: Sune produces this Week 1 plan; Rasmus builds the full Week 1 package in the canonical weekly structure; Linnea/Wilhelm audit Week 1; Alfred packages a Week 1 release with `slides.md` converted to PPTX downstream.

The 24-lesson topic table, Bloom mapping, AT placement and vocabulary previews are inherited verbatim from the earlier course plan at `/Users/agent/material-pipeline/output/computational-thinking-en/01-suunnitelma.md`. This file replaces the per-lesson granularity with **per-week** granularity, starting from Week 1.

---

## Suunnitelma

### Course overview

The course answers one central question: **"How do I speak to a computer so that it understands what I want it to do?"** Students start from familiar everyday situations (instructions for a younger sibling, a recipe, getting to school) and gradually move toward a formal, step-by-step way of expressing instructions. By the end of week 6 students can write pseudocode that includes sequence, condition, and repetition. In weeks 7–8 the same pseudocode pattern is translated into a tiny, browser-based JavaScript program. Programming is treated as the *last* layer; computational thinking is the layer the course actually trains. Three assessed tasks (AT1, AT2, AT3) are spaced so each rests on competencies the preceding weeks actually built. All three are AI-resilient by construction.

### Week 1 theme statement

Week 1 establishes the **conceptual foundation of the entire course**: a computer follows instructions literally, ambiguity lives in the instruction (not in the machine), and the everyday skill of telling someone how to do something is already a form of computational thinking. The three lessons sit together as a single arc — Lesson 1 names the problem (literal interpretation, ambiguity), Lesson 2 names the artefact that solves it (the algorithm), and Lesson 3 stress-tests the artefact by hunting and removing ambiguity. By the end of the week the student can write a clear, step-by-step everyday instruction in plain English, hand it to a literal follower, and improve it based on what breaks. No code, no flowcharts, no pseudocode — those arrive in weeks 3–6.

### L1–L3 breakdown for Week 1

#### Lesson 1 — What does computational thinking mean? Humans, computers, and interpreting instructions

- **Learning objectives** (Remembering + Understanding only):
  - (a) **Define** computational thinking in own words. *(Remembering)*
  - (b) **Explain** that a computer follows instructions literally. *(Understanding)*
  - (c) **Give** one everyday and one IT example of "speaking to a computer". *(Understanding)*
  - (d) **Recognize** that ambiguity is a property of the *instruction*, not of the computer. *(Understanding)*
- **Key vocabulary preview:** computational thinking, instruction, literal interpretation, ambiguity, computer (as instruction-follower); preview term *algorithm*.
- **Central message (one sentence):** A computer is a literal follower of instructions, so the quality of an instruction — not the cleverness of the machine — decides the outcome.

#### Lesson 2 — Algorithms in everyday life: step-by-step instructions without code

- **Learning objectives** (Remembering + Understanding, light Applying):
  - (a) **Define** algorithm in own words. *(Remembering)*
  - (b) **Identify** algorithms in everyday situations (recipe, route, morning routine). *(Understanding)*
  - (c) **Describe** the parts of an algorithm: goal, steps, input, output. *(Understanding)*
  - (d) **Write** a 5–10 step everyday algorithm in plain language. *(light Applying)*
  - (e) **Compare** two algorithms for the same goal at a surface level. *(Understanding)*
- **Key vocabulary preview:** algorithm, step, input, output, goal; preview term *precision*.
- **Central message (one sentence):** An algorithm is the everyday name for a clear sequence of literal steps, and writing one is a skill anyone can practice without code.

#### Lesson 3 — Precise and imprecise instructions: testing and improving instructions

- **Learning objectives** (Remembering + Understanding, light Applying):
  - (a) **Identify** ambiguous words in an instruction. *(Understanding)*
  - (b) **Explain** why testing reveals defects faster than re-reading. *(Understanding)*
  - (c) **Rewrite** an imprecise instruction to be unambiguous. *(light Applying)*
  - (d) **Test** instructions by acting as the "literal computer". *(light Applying)*
- **Key vocabulary preview:** precise, imprecise, ambiguity (revisited), test, edge case; preview term *decomposition*.
- **Central message (one sentence):** Instructions are not finished when they sound right; they are finished when a literal follower can execute them without asking questions.

### Week 1 — core minimum vs. deepening

**Core minimum (every student must leave Week 1 able to):**
- State the central question of the course in their own words.
- Explain that a computer follows instructions literally and that ambiguity is in the instruction.
- Define *computational thinking*, *instruction*, *algorithm*, *ambiguity*, *precision* in plain English.
- Write a short (5–10 step) everyday algorithm in plain English.
- Find at least one ambiguous word in a given instruction and rewrite the instruction more precisely.

**Deepening (optional extension, not required for AT1):**
- Test their own instruction with a real follower and iterate on it (literal-robot game in full).
- Use an LLM as a sparring partner to challenge their own ambiguity analysis (with a structured prompt).
- Apply the literal-follower lens to a vocational IT scenario of their choice (a help-desk ticket, a README, a chat-bot instruction).
- Notice edge cases — instructions that work for the common case but break for an unusual one — and describe them in plain English.

### Forward-looking stubs for Weeks 2–8

**Week 2 — Decomposition (Lessons 4–6).** Students learn to break a problem too big for a single algorithm into a main task, subtasks and a goal. Order and dependencies (Lesson 5) are introduced. Week 2 ends with a decomposed IT-related task that becomes **AT1**. Bloom focus: Understanding + Applying.

**Week 3 — Describing a process and abstraction (Lessons 7–9).** Students learn to draw simple flowcharts (start/end + arrows), discover *abstraction* as "hide detail, keep what matters", and informally name reusable blocks of instructions ("functions without code"). Bloom focus: Understanding + Applying.

**Week 4 — Alternative solutions and evaluation (Lessons 10–12).** "Correct" is not unique. Students produce multiple valid solutions to the same problem, apply criteria (correctness, simplicity, readability, speed) to compare them, and practice peer feedback. Bloom focus: Applying + Analyzing + light Evaluating.

**Week 5 — Logic structures (Lessons 13–15).** Sequence, conditions (if-then-else, AND/OR informally) and repetition (repeat-until, for-each) are formalised. Bloom focus: Understanding + Applying. Foundation for AT2.

**Week 6 — Pseudocode and dry running (Lessons 16–18).** Synthesis of Weeks 1–5 into pseudocode. Variables and input/processing/output appear. Students dry-run pseudocode with a trace table and fix bugs. **AT2** is submitted. Bloom focus: Applying + Analyzing.

**Week 7 — First JavaScript (Lessons 19–21).** The bridge into code. Browser console only. `console.log`, `let`, `if/else`, comparison operators. Lesson 1's central question is revisited: a formal language exists precisely *because* computers cannot disambiguate. Bloom focus: Understanding + Applying.

**Week 8 — Loops, AT3, debugging, presentation (Lessons 22–24).** Loops in JavaScript, translation of a piece of own pseudocode into JavaScript (**AT3**), reading a real error message, and a 2-minute oral presentation of the AT3 program. The course closes where Lesson 1 started — speaking to a computer so it understands. Bloom focus: Applying + Analyzing + Creating (AT3).

---

## Rajaukset

**Out of scope for Week 1 (and the course at large):**
- **No automatic testing or debugging frameworks** (jest, mocha, vitest, pytest, etc.). Stated explicitly here as a course-level rule even though Week 1 has no code anyway.
- **No IDEs, no Node.js, no npm**: the course uses a browser console only (and that only from Week 7). Week 1 needs no tooling at all.
- **No slide deck files beyond `slides.md`**: Rasmus produces a single Markdown deck per week. No `.pptx`, no `.key`, no Reveal.js, no Google Slides. The orchestrator handles PPTX conversion downstream from `slides.md`.
- **No images directory** unless a slide explicitly references an image, in which case Rasmus may add a `media/` subfolder under `student/week-01/`. None should be required for Week 1.
- **No platform-side independent exercises** (those are produced by a different team).
- **No deep CS theory**: no Big-O, no Turing machines, no formal grammars, no recursion as a topic.
- **No coverage of programming languages other than JavaScript** in the course; in Week 1 no programming language is named at all.
- **No graded essays, no long written reports**: assessed tasks are artefact + short reflection. Week 1 has no assessed task.
- **No external accounts** that require email signup.

**Language:** English throughout. **Börje (Finnish polishing) is skipped** for this run. The H2 headings in *this plan file* may remain in Finnish (`Suunnitelma`, `Rajaukset`, `Hyväksymiskriteerit`, `Briefing Rasmukselle`, `Avoimet kysymykset`) because they are part of the Sune template; **all 7 of Rasmus's Week 1 files must be fully English**, including their section headings.

**Pipeline scope this run:**
- Sune produces this Week 1 plan (you are reading it).
- Rasmus builds **only Week 1** in the canonical 7-file weekly structure. Weeks 2–8 are planned (see stubs above), not built.
- Linnea and Wilhelm audit Week 1 only.
- Alfred packages a Week 1 release; the orchestrator converts `slides.md` to PPTX outside Rasmus's scope.

---

## Hyväksymiskriteerit

Wilhelm verifies the Week 1 package against the following concrete, checkable criteria.

### Structural — files and folders

1. **All 7 canonical files present**, with exactly these filenames (case-sensitive, lowercase, kebab-case):
   - `student/week-01/overview.md`
   - `student/week-01/self-study.md`
   - `student/week-01/student-tasks.md`
   - `student/week-01/vocabulary.md`
   - `student/week-01/slides.md`
   - `teacher/week-01/teacher-materials.md`
   - `teacher/week-01/in-class-tasks.md`
2. **No extra files** in `student/week-01/` or `teacher/week-01/` (no `.pptx`, no other slide formats, no orphan images directory). A `media/` subfolder is allowed only if a slide or self-study explicitly references a contained image.
3. **No `slides.pptx`, no `deck.md`, no `slides.key`, no Reveal.js HTML** anywhere. Hard fail if found.

### Volume (sanity-check brackets, not hard limits)

4. `overview.md`: **200–400 words**. Short. One section per area below.
5. `self-study.md`: **2400–4000 words** (roughly 3× a golden-sample single lesson, since this covers L1, L2 and L3).
6. `student-tasks.md`: **800–1800 words** total. **1–2 RECOMMENDED + 2–3 DEEPENING** tasks (see #14).
7. `vocabulary.md`: **10–18 terms**, each with a 1–3 sentence English definition.
8. `slides.md`: **~10–20 slides**, separated by `---` on their own line, each slide starting with an H1 (`#`) or H2 (`##`) title and containing minimal supporting content (3–5 short bullets or 1–2 short sentences).
9. `teacher-materials.md`: **2400–4200 words**. Contains **3 × 90-minute lesson plans** (one per lesson), each with time slots summing to 90.
10. `in-class-tasks.md`: **400–1200 words**. Contains **at least 1 mandatory teacher-led in-class exercise** (pair/group/whole class) that genuinely requires classroom interaction.

### Required H2 sections per file

11. `overview.md` must contain (in this order):
    - `## Week 1 theme`
    - `## What you will be able to do by the end of the week`
    - `## Core minimum vs. deepening` (with a clear two-column or two-bullet contrast)
    - `## How the three lessons fit together`
12. `self-study.md` must contain:
    - `# <Week title>` (an inviting H1 title)
    - `## Introduction` — names the central question verbatim.
    - `## Lesson 1 — Speaking to a computer (literal interpretation and ambiguity)` (or close variant)
    - `## Lesson 2 — Algorithms in everyday life`
    - `## Lesson 3 — Precise and imprecise instructions`
    - `## Summary and what comes next`
    - **At least 4 `> **Pause for a moment:**` reflection prompts** across the three lessons (at least 1 per lesson).
13. `student-tasks.md` must contain:
    - `## Overview of the week's tasks`
    - One H2 per task, prefixed with `🟢 RECOMMENDED —` or `🟣 DEEPENING —`.
    - Each task ends with a `### Tip` or `### Keep your notes` block reminding the student that AT1 lands at end of Week 2.
14. `vocabulary.md` must contain a single H2 `## Week 1 vocabulary`, then each term as an H3 or as a bolded term in a definition list. **At least one term flagged as a "looking ahead" preview** (e.g. *decomposition* for Week 2).
15. `slides.md` must:
    - Start with a title slide.
    - Contain at least one slide whose body shows the central question verbatim.
    - Use `---` on its own line between slides.
    - Have **no embedded `.pptx` references** and no speaker-note syntax that assumes a specific renderer.
16. `teacher-materials.md` must contain:
    - `## Week 1 learning objectives (mapped to Bloom)`
    - `## Common misconceptions` — **at least 6 across the week** (≥2 per lesson), each with a "Correction:" line.
    - `## Lesson 1 — 90-minute plan`, `## Lesson 2 — 90-minute plan`, `## Lesson 3 — 90-minute plan` — each with concrete time slots summing to 90, each allocating **30–50% to independent student work** (criterion #18).
    - `## Answers to common student questions` — at least 5 across the week.
    - `## Formative assessment tips`.
17. `in-class-tasks.md` must contain:
    - `## Overview`
    - At least 1 H2 task labelled **MANDATORY**, requiring teacher-led classroom interaction (pair work, role play, whole-class debrief, or board game). Optional further tasks may be labelled OPTIONAL.

### Pedagogical rules

18. **30–50% rule**: in `teacher-materials.md`, for each of the three 90-minute lesson plans, the time blocks visibly labelled as *independent student work* (not lecture, not group/pair activity, not debrief) sum to **27–45 minutes** out of 90. Wilhelm checks the time slots arithmetically.
19. **Bloom cap**: Week 1 learning objectives use only Remembering and Understanding verbs (*define, describe, explain, identify, recognize, give an example of, list, restate, summarize*) with light Applying allowed in L2 (*write a short algorithm in plain English*) and L3 (*rewrite an instruction*, *test an instruction*). **Forbidden verbs** in Week 1 objectives: *create, build, design, develop, evaluate, judge, analyze, decompose, abstract, debug*.
20. **Central question** — *How do I speak to a computer so that it understands what I want it to do?* — appears **verbatim** in `self-study.md` (at least once in the Introduction or Summary) **and** on at least one slide in `slides.md`.
21. **Examples-first principle**: in `self-study.md`, every conceptual section that uses both kinds of examples must place the **everyday example before the IT example**. Wilhelm spot-checks the three lesson sections.
22. **No automatic testing frameworks** mentioned anywhere in any of the 7 files.
23. **Literal interpretation framing**: the phrase "the computer is stupid / dumb" must not appear; the framing must be "the computer is literal". Wilhelm greps.

### Tasks (AI resilience)

24. `student-tasks.md` contains **1–2 🟢 RECOMMENDED + 2–3 🟣 DEEPENING** tasks. At least **one RECOMMENDED task is AI-resilient by construction**, meaning it requires the student's own concrete context, an observable artefact (a real instruction written by the student, a recording, a screenshot, a real follower's reaction), or a critique-the-LLM mechanism.
25. If a DEEPENING task uses an LLM as a sparring partner, it must include a fenced code block with a sample prompt and explicit instruction not to accept the LLM's output verbatim.

### In-class tasks

26. `in-class-tasks.md` contains **at least 1 MANDATORY teacher-led in-class exercise** that genuinely requires classroom interaction (pair work, role play, whole-class debrief, board game). It must be cross-referenced from `teacher-materials.md` (the teacher should know when to run it in the 90-minute plan).

### Language and polish

27. **English throughout**. No Finnish words in any of the 7 files except clearly necessary proper nouns.
28. **Register**: `self-study.md`, `student-tasks.md`, `overview.md`, `vocabulary.md` and `slides.md` at CEFR ~B1 (short sentences, common vocabulary); `teacher-materials.md` and `in-class-tasks.md` at CEFR ~B2.
29. **Valid Markdown**: every code fence closes, every table renders, no broken internal links, `---` separators in `slides.md` are alone on their own line.

---

## Briefing Rasmukselle

### Cross-cutting reminders (apply to all 7 files)

- **Everyday before IT, always.** When introducing any new idea, lead with a familiar 15-year-old scene (a sandwich, a TikTok dance, directions to a friend's house, a recipe) and only then pivot to an IT example (search query typo, file path, autocorrect, chat-bot instruction).
- **The computer is literal, not stupid.** Reframe any "the computer is dumb" intuition.
- **No code, no flowcharts, no pseudocode, no variables, no loops** in Week 1. All of those have their own weeks.
- **No phrase "computational thinking is just programming".** Pre-empt this misconception in self-study and teacher-materials.
- **No `.pptx` references.** Rasmus delivers `slides.md`; the orchestrator handles PPTX conversion.
- **No automatic testing frameworks anywhere.**
- **Central question must appear verbatim** in `self-study.md` and on a slide in `slides.md`: *How do I speak to a computer so that it understands what I want it to do?*

---

### File 1 — `student/week-01/overview.md` (200–400 words)

**Required H2 structure (in order):**
1. `## Week 1 theme` — one short paragraph naming the central question and the three lesson topics.
2. `## What you will be able to do by the end of the week` — bullet list of 5–7 plain-English "can do" statements, mapped to the L1–L3 objectives above but stated in student-facing language.
3. `## Core minimum vs. deepening` — a clear two-column contrast or two-bullet-list contrast (mandatory vs. optional). Mirror the "Core minimum vs. deepening" section of this plan.
4. `## How the three lessons fit together` — one short paragraph showing the L1 → L2 → L3 arc (problem → artefact → stress-test).

**Examples to lean on:** the recipe example (mandatory: write any 5-step recipe; deepening: rewrite it for a literal robot), the directions-to-school example.

---

### File 2 — `student/week-01/self-study.md` (2400–4000 words)

**Required structure (in order):**
- `# <Week title>` — suggestion: *"Speaking to a computer — what does it actually hear?"* Rasmus may improve.
- `## Introduction` — opens with a familiar scene (sibling, sandwich, dance). States the central question **verbatim**. Tells the student what the week will train.
- `## Lesson 1 — Speaking to a computer (literal interpretation and ambiguity)`
  - `### What is computational thinking?` — short, quotable definition. Name the four classic pillars (decomposition, pattern recognition, abstraction, algorithms) once, then say each gets its own future lesson.
  - `### A computer takes you literally` — **2 everyday examples first** (sibling + sandwich, ambiguous directions to "the big tree"), then **2 IT examples** (`pyhton tutorial` typo search; file path with a missing slash).
  - `### Ambiguity is in the instruction, not the computer` — the conceptual pivot.
  - `### Why this matters for an IT professional` — short vocational paragraph (you write instructions for machines, colleagues, end users).
  - 1 `> **Pause for a moment:**` reflection prompt.
- `## Lesson 2 — Algorithms in everyday life`
  - `### What is an algorithm?` — short definition: a clear sequence of literal steps that solves a problem or completes a task.
  - `### Algorithms you already use` — 3 everyday algorithms (a recipe; the route from home to school; a morning routine). For each, identify *goal*, *input*, *steps*, *output* in plain English.
  - `### Two algorithms for the same goal` — show two valid recipes for the same dish, or two routes to the same place. Note they are both correct.
  - `### Writing your first algorithm in plain English` — the student is invited to write one (no submission yet; this becomes Task 1.1).
  - 1–2 `> **Pause for a moment:**` reflection prompts.
- `## Lesson 3 — Precise and imprecise instructions`
  - `### What does "imprecise" mean here?` — define imprecise/ambiguous instruction; show one short ambiguous instruction and ask the reader what it could mean.
  - `### Hunting ambiguity` — a list of common ambiguity patterns in everyday English (vague nouns like "the file", deictic words like "here/there", relative time like "later", vague quantities like "some"). Then the IT mirror: vague paths, vague filenames, vague timing in cron-like contexts (kept casual — no cron).
  - `### Testing instructions by acting as the literal computer` — describe the "literal-robot" technique. Reference Task 1.1 / 1.3 of `student-tasks.md`.
  - `### Edge cases` — gentle introduction: the instruction works for the common case but not for an unusual one (e.g. "open the fridge and take out milk" — what if there is no milk?).
  - 1 `> **Pause for a moment:**` reflection prompt.
- `## Summary and what comes next` — closes the loop on the central question (state it verbatim again here if not in the Introduction). Previews Week 2 (decomposition).

**Examples menu Rasmus should pick from (use the everyday ones first):**
- Everyday: making a sandwich; making tea/coffee; brushing teeth; tying shoelaces; logging into a school portal; sending a Discord/WhatsApp message; following a TikTok dance; giving directions to a friend's house; recipe for a familiar dish.
- IT: a search query with a typo; a file path missing a slash; autocorrect that "corrects" the wrong word; a chat-bot that misreads "next Friday"; an email filter that flags the wrong message.

---

### File 3 — `student/week-01/student-tasks.md` (800–1800 words)

**Required structure:**
- `## Overview of the week's tasks` — 2–4 sentences. State that 🟢 RECOMMENDED tasks are the mandatory minimum and 🟣 DEEPENING are optional extension. Remind that **AT1 lands at the end of Week 2**, so notes from these tasks should be kept.

**Five candidate tasks for Rasmus to pick from (he keeps 1–2 RECOMMENDED + 2–3 DEEPENING):**

**Task 1.1 — 🟢 RECOMMENDED — "The literal robot game"** *(AI-resilient by construction)*
- Student writes a 6–10 step instruction in plain English for a familiar task they personally do (make tea, log in to the school portal, send a message on Discord). The instruction must be their own, written from scratch.
- Student gives the instructions to a real follower (classmate / family member / themselves on video) who follows them **literally**.
- Student observes at least 3 places the follower got stuck, notes which word or step was ambiguous, rewrites, and re-tests with the same follower.
- 3–5 sentence reflection.
- **Why AI-resilient:** requires a real follower or a self-recording plus an original instruction tied to the student's life. An LLM cannot fake the follower's confusion in a way the teacher can't spot.

**Task 1.2 — 🟢 RECOMMENDED candidate (alternative to 1.1) — "Write your morning algorithm"** *(AI-resilient by context anchor)*
- Student writes their own morning routine as a 7–12 step algorithm in plain English, naming *goal*, *input*, *steps*, *output* explicitly.
- Student then circles 3 words or steps that a literal follower could misread, and writes a more precise version next to each.
- **Why AI-resilient:** anchored in the student's own real morning routine.

**Task 1.3 — 🟣 DEEPENING — "Spot the ambiguity"**
- Student is given 5–6 short ambiguous instructions (Rasmus writes these — e.g. *"Save the file in the usual place"*, *"Run the script after lunch"*, *"Make the button bigger"*, *"Reply to him about it"*). Student annotates each: what is ambiguous and how would they fix it.
- Optional sparring-partner step: paste annotations into an LLM with the supplied prompt, ask the LLM to challenge the analysis, then reject/keep/revise. **Sample prompt provided in a fenced code block.**

**Task 1.4 — 🟣 DEEPENING — "Two algorithms, one goal"**
- Student writes **two different valid algorithms** for the same goal (e.g. two routes from home to school, two ways to make tea). For each, list goal/input/steps/output.
- Reflection (3–5 sentences): which is "better" and by what informal criterion? (This is a gentle precursor to Week 4 — Rasmus does not introduce the word *criterion* formally here.)

**Task 1.5 — 🟣 DEEPENING — "Vocational angle: write a help-desk instruction"** *(AI-resilient)*
- Student writes a short, precise instruction a first-line help-desk agent could follow to walk an end user through one specific task (e.g. "change your school password", "connect to the Wi-Fi", "find your timetable"). The student must include the task they picked from their own school context.
- Student gives the instruction to a classmate who has *not* done this task before, observes where the literal interpretation breaks, and revises.
- **Why AI-resilient:** the school context, the specific UI, and the real classmate-as-tester are all things an LLM cannot fake without giving itself away.

**Default selection Rasmus should ship:**
- 🟢 RECOMMENDED: Task 1.1 (*The literal robot game*). [AI-resilient]
- 🟣 DEEPENING: Task 1.3 (*Spot the ambiguity*), Task 1.4 (*Two algorithms, one goal*), Task 1.5 (*Vocational help-desk instruction*).

Each task ends with a `### Tip` block: "Keep your notes — you'll reuse them in AT1 at the end of Week 2."

---

### File 4 — `student/week-01/vocabulary.md` (10–18 terms)

**Required terms** (Rasmus may add 1–4 of their own, but must not skip any required ones):
1. Computational thinking
2. Instruction
3. Algorithm
4. Step
5. Goal
6. Input
7. Output
8. Literal interpretation
9. Ambiguity
10. Precision
11. Imprecise (instruction)
12. Edge case
13. Computer (as instruction-follower)
14. Test (an instruction)
15. **Decomposition** — flagged as **"looking ahead — central topic of Week 2"**.

Optional additions Rasmus may include if useful: *programmer*, *user*, *artefact*, *literal-robot game*.

Each definition is 1–3 sentences, plain English, with a short everyday example where natural.

---

### File 5 — `student/week-01/slides.md` (~10–20 slides)

**Recommended slide outline (Rasmus may adjust order and titles within the spirit of the structure):**

1. `# Week 1 — Speaking to a computer` *(title slide; instructor name optional)*
2. `## The central question` — body: the question **verbatim**.
3. `## What this week trains` — 3-bullet preview of L1, L2, L3.
4. `## What is computational thinking?` — short quotable definition.
5. `## A computer takes you literally` — 1 everyday example as a 2-line scene.
6. `## "Make a sandwich" — what could go wrong?` — visual prompt for the literal-robot demo.
7. `## Ambiguity is in the instruction, not the computer` — the conceptual pivot.
8. `## Algorithm — a name for what you already do` — short definition.
9. `## Parts of an algorithm` — goal / input / steps / output, 1 line each.
10. `## Two algorithms, one goal` — visual contrast (e.g. two routes to school).
11. `## Precise vs. imprecise instructions` — short side-by-side.
12. `## Hunting ambiguity` — the 4 common patterns (vague noun, deictic, relative time, vague quantity).
13. `## Testing as a literal robot` — describe the in-class exercise in one slide.
14. `## Edge cases (gentle intro)` — one short example.
15. `## Week 1 vocabulary at a glance` — 8–10 key terms in a single slide.
16. `## Core minimum vs. deepening` — two-column contrast.
17. `## Tasks this week` — 1 line per task.
18. `## What comes next: Week 2 — decomposition` — preview.
19. `## Recap — the central question, one more time` — the question **verbatim** (this satisfies the slide-deck verbatim requirement explicitly, alongside slide #2).

Aim ~15–18 slides. Use `---` on its own line between every slide. Body content: 3–5 short bullets or 1–2 short sentences. No speaker-note syntax that assumes a specific renderer.

---

### File 6 — `teacher/week-01/teacher-materials.md` (2400–4200 words)

**Required H2 sections (in order):**

1. `## Week 1 learning objectives (mapped to Bloom)` — restate the L1–L3 objectives from this plan, grouped by Bloom stage. Remembering + Understanding dominant; light Applying acceptable in L2 and L3.
2. `## Common misconceptions` — at least 6 across the week (2 per lesson). Suggested set:
   - **L1**: "The computer is stupid." → Correction: literal, not stupid. // "Computational thinking = programming." → Correction: it's the thinking *behind* programming.
   - **L2**: "Algorithms are only for computer scientists." → Correction: every recipe is an algorithm. // "An algorithm must be long to count." → Correction: 3 steps can be an algorithm if they are clear and produce the goal.
   - **L3**: "Imprecise just means short." → Correction: a long instruction can still be imprecise. // "If the instruction sounds right, it is right." → Correction: only testing with a literal follower shows that.
3. `## Lesson 1 — 90-minute plan` — concrete time slots summing to 90, with an independent-student-work block of **27–45 min** (30–50% rule). Suggested skeleton:
   - 0–10 min: warm-up — teacher demo of a literal-robot moment.
   - 10–25 min: instructor input — central question + definition of computational thinking.
   - 25–55 min: **INDEPENDENT WORK** (30 min) — students draft their own ambiguous instruction (start of Task 1.1, no follower yet).
   - 55–75 min: pair activity — students swap instructions and read each other's literally.
   - 75–85 min: whole-class debrief — build the "everyday vs. IT" board.
   - 85–90 min: closing reflection + preview of Lesson 2.
4. `## Lesson 2 — 90-minute plan` — same arithmetic constraint. Suggested:
   - 0–10 min: warm-up — collect 3 student-named algorithms from everyday life.
   - 10–25 min: instructor input — definition of *algorithm*, goal/input/steps/output.
   - 25–60 min: **INDEPENDENT WORK** (35 min) — each student writes their own morning algorithm (or alternative everyday algorithm).
   - 60–80 min: pair activity — read each other's algorithm and predict the output.
   - 80–88 min: whole-class debrief — what was easy, what was hard.
   - 88–90 min: preview of Lesson 3.
5. `## Lesson 3 — 90-minute plan` — same arithmetic constraint. Suggested:
   - 0–10 min: warm-up — quick "spot the ambiguity" in 2 instructions on the board.
   - 10–25 min: instructor input — precise vs. imprecise, the 4 ambiguity patterns.
   - 25–55 min: **INDEPENDENT WORK** (30 min) — each student rewrites their morning algorithm (from L2) with ambiguity removed.
   - 55–80 min: in-class teacher-led "literal robot" exercise (see `in-class-tasks.md`).
   - 80–88 min: whole-class debrief.
   - 88–90 min: preview of Week 2.
6. `## Answers to common student questions` — at least 5 across the week. Suggested: *Is Google an algorithm? / Why doesn't autocorrect understand me? / Is this on the assessed task? / Do I need a computer to do this homework? / Can I use ChatGPT?*
7. `## Formative assessment tips` — 3–5 quick checks (exit ticket, board vote, pair report-back, one-minute paper). No summative assessment in Week 1.

Cross-reference `in-class-tasks.md` from the L1 and L3 plans (the literal-robot exercise belongs in L1 as a teacher demo and L3 as a full student exercise).

---

### File 7 — `teacher/week-01/in-class-tasks.md` (400–1200 words)

**Required structure:**
- `## Overview` — 2–3 sentences naming the tasks and when in the week they fit.
- At least 1 H2 task labelled **MANDATORY** that genuinely requires teacher-led classroom interaction.

**Two concrete activity ideas Rasmus should ship (default: both):**

**Activity A — MANDATORY — "Literal robot live"** *(whole-class + teacher-led, ~25 min, slotted in Lesson 3 between 55–80 min)*
- Teacher prepares 3 ambiguous instructions on slips of paper (e.g. *"Get me a chair"*, *"Open the window a bit"*, *"Write your name on the board"*).
- One volunteer student plays "the computer" and must follow each instruction **literally**, taking nothing for granted.
- After each demo, the whole class names the ambiguity and proposes a more precise instruction. The teacher rewrites it live on the board.
- Closing: each student writes one short ambiguous instruction from their own life on a sticky note; the teacher reads 3 aloud and the class disambiguates collectively.
- **Why it requires the classroom:** the live, embodied literal interpretation is the whole point. It cannot be done as homework.

**Activity B — OPTIONAL — "Algorithm relay (pair work)"** *(pair, ~20 min, can be slotted in Lesson 2 between 60–80 min)*
- Pair A writes a 6-step everyday algorithm without naming the goal.
- Pair B reads the algorithm and tries to **guess the goal** based only on the steps.
- Pair A then reveals the intended goal. Discuss: which steps gave it away? Which steps were too vague?
- Roles swap.

Cross-reference back to `teacher-materials.md` so the teacher knows the exact 90-min slot for each.

---

## Avoimet kysymykset

1. **Slide count.** The brief says "aim ~10–20 slides for the whole week". This plan recommends ~15–18. **Default assumption:** Rasmus targets 15–18 slides; Wilhelm accepts anywhere in 10–20.
2. **PPTX conversion responsibility.** The brief says the orchestrator converts `slides.md` to PPTX; Alfred packages the release. **Default assumption:** Rasmus writes `slides.md` only and never mentions `.pptx`. Orchestrator confirm.
3. **`media/` subfolder.** No images are strictly required for Week 1, but a teacher may want a simple diagram on the "Parts of an algorithm" slide. **Default assumption:** Rasmus may include 0–2 simple inline diagrams as Markdown image references under `student/week-01/media/`, but is not required to. If no images, no `media/` folder.
4. **Language register inside `slides.md`.** Slides should be short (B1). **Default assumption:** B1, 3–5 short bullets per slide.
5. **In-class task labelling in `in-class-tasks.md`.** This plan suggests **MANDATORY** and **OPTIONAL** as inline tags. **Default assumption:** Rasmus uses exactly those labels in the H2 of each task; Wilhelm greps for "MANDATORY".
6. **Reflection-prompt count.** This plan requires "≥4 across the three lessons (≥1 per lesson)" in `self-study.md`. **Default assumption:** Rasmus aims for 5–6 (around 2 in the longest lesson section) to give Wilhelm slack.
7. **Vocabulary count.** This plan says 10–18 terms (≥10 required, 1 preview term mandatory). The brief said 10–18 explicitly. **Default assumption:** Rasmus ships ~14 terms.
8. **AI-resilience labelling in `student-tasks.md`.** Rasmus must mark the AI-resilient RECOMMENDED task explicitly with an inline tag like *(AI-resilient)*. **Default assumption:** the tag appears in the task's H2 title.
9. **Whether `overview.md` should preview Week 2.** This plan says "preview Week 2 (decomposition)" in `self-study.md`'s summary section. **Default assumption:** `overview.md` does *not* preview Week 2 (it is a within-week document); only `self-study.md` previews Week 2.
10. **Whether 30–50% independent work needs to be a single contiguous block.** This plan suggests one contiguous 30–35 min block per 90-min lesson. **Default assumption:** Wilhelm accepts either a single block or up to two blocks that together sum to 27–45 min, as long as each block is clearly labelled "INDEPENDENT WORK" and is genuinely independent (not pair, not group, not lecture).
