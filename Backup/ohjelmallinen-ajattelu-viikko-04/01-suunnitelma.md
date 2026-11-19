# Computational Thinking — Week 4 Plan (Sune, Gate #1)

Course: Computational Thinking (English)
Target: First-year vocational ICT students, ~15–17, no prior programming
Duration: 8 weeks x 3 lessons/week x 90 min = 24 lessons
Pipeline scope this run: Sune produces this Week 4 plan; Rasmus builds the Week 4 package in the canonical weekly structure; Linnea/Wilhelm audit Week 4; Alfred packages the Week 4 release in Markdown only (no PDF, no PPTX).

This file uses the same shape as Week 1's `01-suunnitelma.md` and inherits all course-level invariants — central question, 24-lesson topic table, Bloom mapping, AT placement, vocational angle — verbatim from the course plan at `/Users/agent/material-pipeline/output/computational-thinking-en-week-01/01-suunnitelma.md`. The slice handed to Rasmus below is **Week 4 only**.

---

## Suunnitelma

### Where Week 4 sits in the course arc

Week 4 is the **mid-course reflection week**. Weeks 1–3 built three artefacts the students can now hold in their hands: a clear everyday algorithm in plain English (Week 1), a decomposed problem with a main task, subtasks and dependencies (Week 2), and a simple flowchart with at least one named, reusable block ("function without code") plus an early sense of abstraction (Week 3). Week 4 stops adding new computational-thinking primitives and instead **turns a critical eye on the artefacts the students already produced** — particularly the Week 3 algorithms/flowcharts and the Week 2 decompositions. Students learn that more than one valid solution can solve the same problem, and that picking between them is **not a matter of taste — it is a matter of stated criteria**. The week ends by training the peer-feedback-and-revision habit that students will lean on heavily in **AT2** (Week 5/6 process description) and **AT3** (Week 8 program).

### Week 4 theme statement

The central message for the week is, verbatim:

> **More than one valid solution can solve the same problem. Picking between them is not a matter of taste — it is a matter of stated criteria.**

The three lessons sit together as one arc — **L10** demonstrates that "correct" is not unique (the same problem, solved two different ways, both valid); **L11** names the four criteria that turn taste into reasoning (clarity, efficiency, repeatability, error-proneness); **L12** puts the criteria to work in a structured peer-review protocol on a real artefact a student made in Week 2 or Week 3, followed by a revision. No new artefact type is introduced this week. No code, no testing frameworks, no PowerPoint. The cognitive level is **Understanding + light Analyzing** (compare two solutions against named criteria), and the verbs *evaluate*, *judge*, *grade*, *score*, *create* are explicitly out of scope.

### L10–L12 breakdown for Week 4

#### Lesson 10 — Same problem, multiple solutions

- **Learning objectives** (Understanding, with one light Analyzing in (d)):
  - (a) **Recognize** that the same problem can have more than one correct solution. *(Understanding)*
  - (b) **Describe** in plain English how two valid solutions to the same problem can differ in their steps, in their order, or in what they leave to the user. *(Understanding)*
  - (c) **Give** one everyday example and one IT example of two valid solutions to the same problem. *(Understanding)*
  - (d) **Identify** at least two ways in which two given solutions differ from each other. *(light Analyzing)*
- **Key vocabulary preview:** solution, valid solution, alternative, trade-off (preview only), variation; preview term *criterion*.
- **Central message (one sentence):** A problem is not the same as its solution; one problem can be solved many ways, and noticing that is the start of choosing well.

#### Lesson 11 — Criteria for evaluating solutions

- **Learning objectives** (Understanding + light Analyzing):
  - (a) **Define** the four working criteria in own words: **clarity**, **efficiency**, **repeatability**, **error-proneness**. *(Understanding)*
  - (b) **Explain** that a criterion turns "I like this one better" into "this one is better at X". *(Understanding)*
  - (c) **Apply** the four criteria to a small worked example (two short algorithms or two short decompositions for the same goal). *(Understanding)*
  - (d) **Compare** two solutions criterion-by-criterion and **identify** which solution is stronger on which criterion. *(light Analyzing)*
  - (e) **Recognize** that a single solution does not have to win on every criterion — different criteria can pull in different directions. *(Understanding)*
- **Key vocabulary preview:** criterion / criteria, clarity, efficiency, repeatability, error-proneness, trade-off; preview term *iteration* (Week 5/6 link).
- **Central message (one sentence):** A criterion is a stated yardstick — name it, and "better" stops being a feeling and starts being a comparison.

#### Lesson 12 — Improving one's own solution and using peer feedback

- **Learning objectives** (Understanding + light Analyzing):
  - (a) **Apply** the four-criteria rubric in a structured peer-review protocol on a partner's existing artefact (a Week 2 decomposition or a Week 3 algorithm/flowchart). *(Understanding)*
  - (b) **Identify** at least two concrete weaknesses in a partner's solution, named by criterion. *(light Analyzing)*
  - (c) **Rewrite** one of their own existing Week 2 or Week 3 solutions to address two specific pieces of peer feedback. *(Understanding — revision, not new creation)*
  - (d) **Describe** in 3–5 sentences what changed and why, citing the criterion that drove each change. *(Understanding)*
- **Key vocabulary preview:** peer review, feedback, revision, rubric, criterion (revisited).
- **Central message (one sentence):** Feedback that names a criterion is feedback you can act on; feedback that doesn't is taste in disguise.

### Week 4 — must-do minimum vs. deepening

**Must-do minimum (every student must leave Week 4 able to):**
- State the central message of the week in their own words.
- Name and define the four working criteria — **clarity, efficiency, repeatability, error-proneness** — in plain English.
- Recognize that one problem can have more than one valid solution, and give one everyday example and one IT example.
- Compare two short, given solutions criterion-by-criterion using the four criteria, in writing.
- Apply the structured peer-review protocol to a partner's Week 2 or Week 3 artefact and produce two concrete, criterion-named pieces of feedback.
- Revise one of their own existing Week 2 or Week 3 solutions in response to peer feedback, and write 3–5 sentences naming what changed and which criterion drove the change.

**Deepening (optional extension, not required for AT1; feeds AT2 strongly):**
- Apply the four criteria to a vocational IT scenario of their choice (e.g. two ways to back up a project folder; two ways to onboard a new user; two ways to write a help-desk macro).
- Notice and describe a **criterion trade-off** in their own words — one solution wins on clarity, the other on efficiency, and the "best" choice depends on context.
- Use an LLM as a sparring partner to critique their own criterion analysis (with a structured prompt provided).
- Run a second revision pass on the same artefact after a 24-hour gap, comparing the two revisions and naming what the second pass caught that the first did not.

### Forward-looking note (Weeks 5–8 unchanged)

Week 4 does not change the course's forward roadmap. Weeks 5–8 remain as committed in the course plan: logic structures (W5), pseudocode and dry running with **AT2 submission** (W6), first JavaScript (W7), loops, **AT3**, debugging and presentation (W8). The peer-review-and-revision habit trained in Week 4 is reused in AT2 (process description requires a self-revision step) and in AT3 (a partner reviews a JavaScript program against criteria before the oral presentation).

---

## Rajaukset

**Out of scope for Week 4 (in addition to all course-level exclusions inherited from Week 1's plan):**

- **No new computational-thinking primitive** is introduced. Week 4 reuses Week 1's algorithms, Week 2's decompositions and Week 3's flowcharts/abstraction as its raw material. If a student doesn't yet have a Week 2 or Week 3 artefact (absence, low completion), Rasmus must provide a **standby artefact pair** in `student-tasks.md` so the peer-review protocol still works.
- **No formal Evaluating-level Bloom verb** in any objective. The cap is *Understanding + light Analyzing* — the brief is explicit. Forbidden verbs in Week 4 objectives: *evaluate, judge, grade, score, rank, rate, decide which is best, create, build, design, develop, debug*. The verb *compare* is allowed (light Analyzing); *identify* is allowed; *describe* is allowed.
- **No numeric scoring, no points, no rubric grades.** The four criteria are used **descriptively** ("solution A is clearer in step 3 because…"), never **quantitatively** ("solution A scores 4/5 on clarity"). The week is about *reasoning*, not *measurement*.
- **No code, no flowcharts beyond the level introduced in Week 3, no pseudocode, no variables, no loops, no JavaScript.** Those land in Weeks 5–8.
- **No "(AI-resilient)" label** in any learner-facing file. Linnea audits the property, not the label. (This is the explicit hard-rule update for Week 4.)
- **No automatic testing or debugging frameworks** (jest, mocha, vitest, pytest, etc.). No IDEs, no Node.js, no npm.
- **No slide deck files beyond `slides.md`** — plus, only if a lecture segment truly needs it, **one** optional `slides-l<n>-<topic>.md` of 4–8 slides (see §"Supplementary deck" in the Briefing below). No `.pptx`, no `.key`, no Reveal.js, no Google Slides.
- **No PDF, no PPTX rendering** anywhere in this run's pipeline. Markdown release only. Rasmus never references `.pptx`.
- **No `media/` subfolder** unless a slide explicitly needs a diagram. Week 4 does not strictly require one; the worked-example side-by-side can be expressed in plain Markdown tables.
- **No platform-side independent exercises** (a different team handles those).

**Language:** English throughout. Börje (Finnish polishing) is skipped for this run. The H2 headings of *this plan file* may remain in Finnish (`Suunnitelma`, `Rajaukset`, `Hyväksymiskriteerit`, `Briefing Rasmukselle`, `Avoimet kysymykset`) because they are part of the Sune template; **all 7 of Rasmus's Week 4 files must be fully English**, including their section headings.

**Pipeline scope this run:**
- Sune produces this Week 4 plan (you are reading it).
- Rasmus builds **only Week 4** in the canonical 7-file weekly structure, plus optionally one supplementary deck. Weeks 1–3 are already released; Weeks 5–8 are not in scope this run.
- Linnea and Wilhelm audit Week 4 only.
- Alfred packages a Week 4 release in **Markdown only**; no PPTX, no PDF.

---

## Hyväksymiskriteerit

Wilhelm verifies the Week 4 package against the following concrete, checkable criteria. These mirror Week 1's structure with Week-4-specific updates (must-do minimum wording, no "(AI-resilient)" label, "If you are doing this alone" subsection, Bloom cap, AT2 link).

### Structural — files and folders

1. **All 7 canonical files present**, with exactly these filenames (case-sensitive, lowercase, kebab-case):
   - `student/week-04/overview.md`
   - `student/week-04/self-study.md`
   - `student/week-04/student-tasks.md`
   - `student/week-04/vocabulary.md`
   - `student/week-04/slides.md`
   - `teacher/week-04/teacher-materials.md`
   - `teacher/week-04/in-class-tasks.md`
2. **Optional supplementary deck.** At most one extra file of the form `student/week-04/slides-l<n>-<topic>.md` (4–8 slides). Rasmus's default for Week 4: **ship one such deck for L11**, named `slides-l11-criteria-walkthrough.md` (see §"Supplementary deck" in the Briefing). If Rasmus chooses not to ship it, the main deck must cover the L11 worked example in at least 3 dedicated slides.
3. **No other extra files** in `student/week-04/` or `teacher/week-04/`. No `.pptx`, no other slide formats, no orphan `media/` directory unless a slide actually references an image. Hard fail on `slides.pptx`, `deck.md`, `slides.key`, Reveal.js HTML.

### Volume (sanity-check brackets, not hard limits)

4. `overview.md`: **200–400 words**.
5. `self-study.md`: **2400–4000 words** (covers L10, L11 and L12).
6. `student-tasks.md`: **800–1800 words** total. **1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING** tasks.
7. `vocabulary.md`: **10–18 terms**, each with a 1–3 sentence English definition.
8. `slides.md`: **~12–18 slides** (acceptance range 10–20), separated by `---` on their own line, each slide starting with an H1 (`#`) or H2 (`##`) title and containing minimal supporting content (3–5 short bullets or 1–2 short sentences).
9. `teacher-materials.md`: **2400–4200 words**. Contains **3 × 90-minute lesson plans**, each with time slots summing to 90.
10. `in-class-tasks.md`: **400–1200 words**. Contains **at least 1 MANDATORY teacher-led in-class exercise**; for Week 4, that mandatory exercise must be a **peer-review protocol** (criteria → feedback → revision).
11. Optional `slides-l11-criteria-walkthrough.md`: **4–8 slides**, same `---` separator convention, no `.pptx` references.

### Required H2 sections per file

12. `overview.md` must contain (in this order):
    - `## Week 4 theme`
    - `## What you will be able to do by the end of the week`
    - `## Must-do minimum vs. deepening` (with a clear two-bullet-list contrast; use the wording **must-do minimum**, not "core minimum" and not "mandatory minimum")
    - `## How the three lessons fit together`
13. `self-study.md` must contain:
    - `# <Week title>` (an inviting H1 title)
    - `## Introduction` — names the central message of the week **verbatim** at least once.
    - `## Lesson 10 — Same problem, multiple solutions` (or close variant)
    - `## Lesson 11 — Criteria for evaluating solutions`
    - `## Lesson 12 — Improving one's own solution and using peer feedback`
    - `## Summary and what comes next`
    - **At least 4 `> **Pause for a moment:**` reflection prompts** across the three lessons (at least 1 per lesson).
    - At least one explicit forward link to **AT2 (Week 5/6 process description)** in the L12 section or the Summary, stating that Week 4's peer-review-and-revision habit is reused in AT2.
14. `student-tasks.md` must contain:
    - `## Overview of the week's tasks` — uses the wording **must-do minimum** for MANDATORY tasks.
    - One H2 per task, prefixed with `🟢 MANDATORY —` or `🟣 DEEPENING —`. **No "(AI-resilient)" label** anywhere in the task titles or bodies.
    - Every task whose flow assumes a partner / follower / reviewer contains a subsection `### If you are doing this alone` with a concrete alternative (24h gap, video self, different device, class chat, async partner).
    - Each task ends with a `### Keep your notes` block stating that Week 4 work feeds **AT2** (the Week 5/6 process description) — not AT1 (already submitted at end of Week 2).
15. `vocabulary.md` must contain a single H2 `## Week 4 vocabulary`, then each term as an H3 or as a bolded term in a definition list. **At least one term flagged as a "looking ahead" preview** (suggested: *iteration*, linking to Weeks 5/6).
16. `slides.md` must:
    - Start with a title slide.
    - Contain at least one slide whose body shows the **central message of the week verbatim**.
    - Use `---` on its own line between slides.
    - Have no embedded `.pptx` references and no speaker-note syntax that assumes a specific renderer.
17. `teacher-materials.md` must contain — using **exactly these required H2 headings, verbatim**:
    - `## Week 4 learning objectives (mapped to Bloom)`
    - `## Common misconceptions for Week 4`
    - `## Lesson 10 — 90-minute plan`
    - `## Lesson 11 — 90-minute plan`
    - `## Lesson 12 — 90-minute plan`
    - `## Facilitation tips`
    - `## Answers to common student questions`
    - `## Formative assessment tips`
    Each 90-minute plan must contain a **`Slide cues`** subsection that names the slide numbers from `slides.md` (and from any supplementary deck) used in each time block. At least **6 common misconceptions** across the week (≥2 per lesson), each with a "Correction:" line. At least **5 student questions** across the week, with answers.
18. `in-class-tasks.md` must contain:
    - `## Overview`
    - At least 1 H2 task labelled **MANDATORY**, which is the **peer-review protocol** (criteria → feedback → revision) used inside L12. Optional further tasks may be labelled OPTIONAL.

### Pedagogical rules

19. **30–50% independent-work rule**: in `teacher-materials.md`, for each of the three 90-minute lesson plans, the time blocks visibly labelled **INDEPENDENT WORK** (not lecture, not pair, not group, not whole-class debrief) sum to **27–45 minutes** out of 90. Wilhelm checks arithmetically.
20. **Bloom cap**: Week 4 learning objectives use only **Understanding** verbs and **light Analyzing** verbs. Allowed verbs: *recognize, describe, define, explain, identify, give an example of, list, apply (the four criteria), compare (criterion-by-criterion), rewrite (a revision, not a creation)*. **Forbidden verbs** in Week 4 objectives: *evaluate, judge, grade, score, rank, rate, decide which is best, create, build, design, develop, debug, decompose (new), abstract (new)*.
21. **Central message verbatim**: the sentence *"More than one valid solution can solve the same problem. Picking between them is not a matter of taste — it is a matter of stated criteria."* appears verbatim **at least once in `self-study.md`** and **on at least one slide in `slides.md`**.
22. **The four criteria are stated and used.** All of `self-study.md`, `slides.md` and `teacher-materials.md` use the same four criterion names — **clarity, efficiency, repeatability, error-proneness** — in that order on first mention. No synonyms ("readability" for "clarity", "robustness" for "error-proneness") in primary definitions; synonyms may appear once as a sidebar gloss.
23. **No "(AI-resilient)" label** anywhere in learner-facing files. Linnea separately audits AI-resilience as a property; Wilhelm greps for the literal substring `AI-resilient` and `(AI-resilient)` and **hard fails** if it appears in any of the 7 files.
24. **"Must-do minimum"** is the exact wording for MANDATORY tasks in `overview.md` and `student-tasks.md`. Wilhelm greps for the substring `core minimum` (must not appear) and `mandatory minimum` (must not appear); only **must-do minimum** is acceptable.
25. **"If you are doing this alone"** subsection is required in every task whose flow assumes a partner / follower / reviewer, with a concrete alternative.
26. **AT2 link**: each task's `### Keep your notes` block names AT2 explicitly (the Week 5/6 process description), not AT1.
27. **Examples-first principle**: in `self-study.md`, every conceptual section that uses both kinds of examples places the **everyday example before the IT example**.
28. **Vocational angle present**: at least one of the three IT examples chosen for `self-study.md` and at least one DEEPENING task draws on the brief's vocational menu — **two ways to back up a project folder; two ways to onboard a new user; two ways to write a help-desk macro**.
29. **Taste vs. criterion framing**: the framing must be *taste* → *criterion*, not *opinion* → *fact*. The phrases "the better one", "the right answer", "the best solution" without a named criterion next to them must be flagged by Wilhelm as drift.
30. **No numeric scoring**: Wilhelm greps for `/5`, `/10`, `out of` (in scoring contexts), `points`, `score:`. These must not appear in criterion contexts. (`step 1 out of 5` and similar non-scoring uses are fine.)

### Tasks (AI resilience as property, not label)

31. `student-tasks.md` contains **1–2 🟢 MANDATORY + 2–3 🟣 DEEPENING** tasks. At least **one MANDATORY task is AI-resilient by construction** — requires the student's own concrete artefact from Week 2 or Week 3, a real partner's observable feedback, or a critique-the-LLM mechanism. The property is audited; the label is not used.
32. If a DEEPENING task uses an LLM as a sparring partner, it must include a fenced code block with a sample prompt and explicit instruction not to accept the LLM's output verbatim.
33. At least one MANDATORY task is an **in-class activity** (cross-referenced from `teacher-materials.md` and resolved in `in-class-tasks.md`). Week 4 requirement: this MANDATORY in-class activity is the **peer-review protocol** in L12.

### In-class tasks

34. `in-class-tasks.md` contains at least 1 MANDATORY teacher-led in-class exercise. For Week 4 it must be the **peer-review protocol** (criteria → feedback → revision). It is cross-referenced from `teacher-materials.md` (the L12 plan).

### Language and polish

35. **English throughout**. No Finnish words in any of the 7 files except clearly necessary proper nouns.
36. **Register**: `self-study.md`, `student-tasks.md`, `overview.md`, `vocabulary.md` and `slides.md` at CEFR ~B1; `teacher-materials.md` and `in-class-tasks.md` at CEFR ~B2.
37. **Valid Markdown**: every code fence closes, every table renders, no broken internal links, `---` separators in `slides.md` are alone on their own line.

---

## Briefing Rasmukselle

### Cross-cutting reminders (apply to all 7 files)

- **Continuity, not novelty.** Week 4 reuses the artefacts students made in Week 2 (decompositions) and Week 3 (algorithms / flowcharts / named blocks). Do not introduce a new artefact type. The L12 peer review **must** operate on something the student already has from W2/W3. Provide a standby artefact pair for students who don't have their own.
- **Everyday before IT, always.** When introducing any new idea (e.g. "two valid solutions"), lead with a familiar 15-year-old scene (two ways to make tea; two routes home; two ways to split a pizza bill) and only then pivot to an IT example (two ways to back up a project folder; two ways to onboard a new user; two ways to write a help-desk macro).
- **Taste → criterion.** The whole week is the move from "I like this one better" to "this one is better at clarity". Police the framing in `self-study.md` and `slides.md`. Phrases like "the right way" or "the best solution" without a criterion next to them are drift.
- **Four criteria, in this fixed order on first mention:** **clarity, efficiency, repeatability, error-proneness**. Use the same four names throughout. Glosses are fine; synonyms in primary definitions are not.
- **Bloom cap: Understanding + light Analyzing.** Allowed verbs: *recognize, describe, define, explain, identify, give an example of, list, apply (the four criteria), compare (criterion-by-criterion), rewrite*. Forbidden: *evaluate, judge, grade, score, rank, rate, decide which is best, create, build, design, develop, debug*.
- **No numeric scoring.** Criteria are descriptive lenses, not measurements. Never assign 4/5 or 3 points or a rubric grade.
- **No "(AI-resilient)" label** anywhere in any of the 7 files. Linnea audits the property separately.
- **"Must-do minimum"** is the wording for MANDATORY in `overview.md` and `student-tasks.md`. Do not write "core minimum" or "mandatory minimum".
- **"If you are doing this alone"** subsection is mandatory in every task that assumes a partner / follower / reviewer.
- **AT2, not AT1.** Every `### Keep your notes` block names **AT2 (the Week 5/6 process description)**. AT1 was already submitted at the end of Week 2.
- **No code, no pseudocode, no variables, no loops, no JavaScript, no testing frameworks, no `.pptx` references.**
- **Central message verbatim** in `self-study.md` and on a slide: *"More than one valid solution can solve the same problem. Picking between them is not a matter of taste — it is a matter of stated criteria."*

---

### File 1 — `student/week-04/overview.md` (200–400 words)

**Required H2 structure (in order):**

1. `## Week 4 theme` — one short paragraph naming the central message and the three lesson topics (L10 same problem, multiple solutions; L11 criteria; L12 improving via peer feedback). Includes the central message **verbatim**.
2. `## What you will be able to do by the end of the week` — bullet list of 5–7 plain-English "can do" statements, mapped to the L10–L12 objectives, stated in student-facing language. Examples:
   - "Recognize that one problem can have more than one correct solution."
   - "Name and define the four criteria — clarity, efficiency, repeatability, error-proneness — in your own words."
   - "Compare two short solutions criterion-by-criterion and say which is stronger on which criterion."
   - "Give a partner two pieces of feedback that each name a criterion."
   - "Revise one of your own Week 2 or Week 3 solutions in response to feedback, and explain what changed and why."
3. `## Must-do minimum vs. deepening` — two-bullet-list contrast. Mirror the §"must-do minimum vs. deepening" section of this plan. Use the wording **must-do minimum**, not "core minimum".
4. `## How the three lessons fit together` — one short paragraph showing the L10 → L11 → L12 arc (notice variety → name the criteria → use the criteria in a peer-review-and-revision cycle).

**Vocabulary to use:** valid solution, criterion (singular)/criteria (plural), clarity, efficiency, repeatability, error-proneness, peer review, revision.

**Length target:** ~300 words.

---

### File 2 — `student/week-04/self-study.md` (2400–4000 words)

**Required structure (in order):**

- `# <Week title>` — suggestion: *"More than one right answer — comparing solutions"*. Rasmus may improve.
- `## Introduction` — opens with a familiar scene (two friends both make tea, but in different orders; two routes home, both arrive). States the central message **verbatim** at least once. Tells the student that Week 4 is the *mid-course reflection* — no new artefact type — and that we will reuse Week 2 and Week 3 work.
- `## Lesson 10 — Same problem, multiple solutions`
  - `### A problem is not the same as its solution` — short conceptual paragraph.
  - `### Two valid solutions, side by side (everyday)` — pick **two ways to make a cup of tea** as the worked example, and lay them out as two short numbered algorithms side by side in a Markdown table. Both reach the goal; they differ in step order and in what they leave to the user.
  - `### Two valid solutions, side by side (IT)` — pick **two ways to back up a project folder** as the IT mirror (e.g. copy-paste the folder to a USB drive vs. zip the folder and email it to yourself). Same side-by-side treatment. **Vocational angle, from brief.**
  - `### What is the same, what is different?` — a short list naming concrete differences (number of steps, order, where the user has to choose, what gets left implicit).
  - 1 `> **Pause for a moment:**` reflection prompt — ask the student to think of two ways they personally do one familiar task and write both down.
- `## Lesson 11 — Criteria for evaluating solutions`
  - `### From taste to criterion` — short conceptual paragraph. Use the exact framing *taste → criterion*. Quote the central message **verbatim** here if not already done in the Introduction.
  - `### The four criteria for this course`
    - `**Clarity:**` A literal follower can read it once and know what to do, with no question that needs asking.
    - `**Efficiency:**` It reaches the goal without wasted steps or wasted time.
    - `**Repeatability:**` It produces the same result the second, third and tenth time, with the same input.
    - `**Error-proneness:**` It is hard to do the wrong thing while following it (fewer easy mistakes, fewer foot-guns).
    Each criterion gets a 2–4 sentence definition followed by a one-line everyday example and a one-line IT example.
  - `### Applying the four criteria to the two tea recipes` — walk through the L10 tea example again, but now look at each recipe with each of the four criteria in turn. Use a small Markdown comparison table (criterion column; "Recipe A" column; "Recipe B" column). Each cell is one short sentence.
  - `### Applying the four criteria to the two backup methods` — same treatment for the IT example. **Vocational angle.**
  - `### Trade-offs — when criteria pull in different directions` — short paragraph. One solution may be clearer; the other may be more efficient; the "best" choice depends on context. Resist ranking; describe the trade-off.
  - 1–2 `> **Pause for a moment:**` reflection prompts.
- `## Lesson 12 — Improving one's own solution and using peer feedback`
  - `### Why your own solution is the hardest to see clearly` — short paragraph. Echoes the Lesson 3 (Week 1) point about reading your own instruction back: the four criteria are a way to read it *with someone else's eyes*.
  - `### The peer-review protocol (criteria → feedback → revision)` — describe the three-step protocol students will use in class:
    1. The reviewer reads the partner's artefact silently. Once per criterion (in the fixed order), the reviewer writes one sentence: either "Strong on X because…" or "Could be improved on X because…". The reviewer must mention the criterion by name.
    2. The reviewer hands back **two pieces of feedback total** (not four; pick the two most useful), each tied to a criterion.
    3. The author then **revises the artefact** to act on at least one of the two pieces of feedback, and writes 3–5 sentences naming what changed and which criterion drove the change.
  - `### Giving feedback that someone can actually use` — short list:
    - Always name the criterion. ("This is unclear" → "This is unclear at step 3 because the word *file* doesn't say which file.")
    - One concrete spot, not a general impression. ("The whole thing is too long" → "Steps 4 and 5 repeat step 2.")
    - A suggestion is optional but welcome. ("Maybe combine steps 4 and 5 with the rest.")
    - Critique the artefact, not the person.
  - `### Receiving feedback you don't agree with` — short paragraph. You are not obliged to act on every piece of feedback. You **are** obliged to consider it, and to be able to say which criterion it speaks to.
  - `### Looking ahead to AT2` — one short paragraph. AT2 lands at the end of **Week 5/6** as a process description. AT2 requires you to **revise your own work after feedback** — exactly the habit Week 4 trains. Keep your peer's feedback notes and your revision notes from this week; you will reuse them.
  - 1 `> **Pause for a moment:**` reflection prompt.
- `## Summary and what comes next` — closes the loop on the central message (state it verbatim again if not in the Introduction). Previews Week 5 (logic structures: sequence, conditions, repetition) as the next computational-thinking primitive, and reminds the student that AT2 is built from Week 5/6 work plus the Week 4 revision habit.

**Examples menu Rasmus should pick from (everyday before IT):**

- *Everyday:* two ways to make tea/instant noodles; two routes from school to home; two ways to organise a pile of laundry; two ways to split a pizza bill; two ways to pack a school bag.
- *IT (must include vocational angle):* two ways to back up a project folder; two ways to onboard a new user (account-first vs. tour-first); two ways to write a help-desk macro (single long macro vs. several short macros).

**Reflection-prompt count target:** 5–6 prompts across the file (~2 in L11 as the longest section).

**Length target:** ~3000 words.

---

### File 3 — `student/week-04/student-tasks.md` (800–1800 words)

**Required structure:**

- `## Overview of the week's tasks` — 2–4 sentences. State that 🟢 MANDATORY tasks are the **must-do minimum** and 🟣 DEEPENING are optional extension. Remind that **AT2 lands at the end of Week 5/6**, so peer-feedback notes and revision notes from these tasks should be kept.

**Five candidate tasks for Rasmus to pick from (he ships 1–2 MANDATORY + 2–3 DEEPENING; default selection at the end of this section):**

**Task 4.1 — 🟢 MANDATORY — "Peer review with the four criteria"** *(AI-resilient by construction — must-do minimum)*
- Each student brings **one of their own Week 2 decompositions or Week 3 algorithms/flowcharts** to class. (If they don't have one, Rasmus provides a **standby artefact pair** at the end of the file — two short pre-written examples, one decomposition and one algorithm, that any student can use.)
- Pair up. Each student silently reads the partner's artefact and produces **two pieces of feedback**, each naming a specific criterion (clarity / efficiency / repeatability / error-proneness) and pointing to a specific step or block.
- Pairs exchange feedback in writing first, then a 5-minute spoken Q&A per pair.
- Each student then **revises their own artefact** to act on at least one piece of feedback, and writes a 3–5 sentence change note that names the criterion driving the change.
- ### If you are doing this alone — *concrete alternative required:* the student writes a peer-review pass on their **24-hour-old self**: leave the artefact for at least 24 hours, then read it as if a colleague handed it to you and write two criterion-named pieces of feedback. (Optionally: post the artefact in the class chat and ask any classmate or the teacher for one criterion-named comment by end of day.)
- **Why AI-resilient (audited as property, not labelled):** the artefact is the student's own from a previous week, the partner's feedback is a real classmate's, and the revision narrative is tied to specific lines of the student's own work. An LLM could simulate feedback but not the back-and-forth with a real partner over a real artefact.

**Task 4.2 — 🟢 MANDATORY candidate (alternative to 4.1, if pair-work is hard to organise) — "Two tea recipes, four criteria"** *(must-do minimum, AI-resilient by construction)*
- Rasmus supplies two short, deliberately different tea recipes (or two short backup procedures) in the task. The student fills in a 4-row comparison table (one row per criterion) with one sentence per cell for each recipe, then writes 3–5 sentences naming which solution is stronger on which criterion and where the trade-offs sit. **No "best" verdict required.**
- ### If you are doing this alone — already a solo task; if it is run in class as the must-do minimum, the alone-version is identical.
- **Why AI-resilient:** the artefact under review is supplied, but the criterion-by-criterion analysis must reference specific steps, and the trade-off paragraph must be argued in the student's own voice — graders can spot generic LLM output trivially.
- **Sune default:** ship Task 4.1 as the must-do minimum; offer 4.2 as a backup that the teacher can swap in if pair-work is impossible that day. **In practice Rasmus ships 4.1 only as MANDATORY**, unless he has reason to suspect pair-work will fail this cohort.

**Task 4.3 — 🟣 DEEPENING — "Backup methods, criterion by criterion"** *(vocational, from brief)*
- The student picks two ways they could back up a real project folder of their own (USB copy vs. zipped email; OneDrive sync vs. weekly manual copy; etc.). They write each as a 5–8 step algorithm, then fill in a 4-criterion comparison table.
- 3–5 sentence trade-off paragraph: in **which situation** would they pick A, in which would they pick B?
- ### If you are doing this alone — already a solo task by design.
- **Vocational angle satisfied (from brief).**

**Task 4.4 — 🟣 DEEPENING — "Help-desk macro: long vs. short"** *(vocational, from brief)*
- The student writes two help-desk responses to the same realistic ticket (e.g. "I can't log in to the school portal on my new phone"): one as a single long step-by-step reply; one as a short reply plus a checklist of "if it's still not working, try X / Y / Z".
- Compare with the four criteria in a table; write a 3–5 sentence reflection on which form they would use as a real first-line agent and which criterion drove the choice.
- ### If you are doing this alone — already solo. Optional sparring-partner step: paste both versions into an LLM with the supplied prompt below and ask it to criticise the criterion analysis. Reject / keep / revise.
- **Sample prompt provided in a fenced code block.** The prompt explicitly instructs the LLM to challenge the criterion analysis, not to rewrite the response.

**Task 4.5 — 🟣 DEEPENING — "Onboarding a new user: account-first vs. tour-first"** *(vocational, from brief)*
- The student writes two short onboarding flows for the same new user (e.g. a new student joining the school portal): one that creates the account first, then offers a tour; one that gives the tour first, then creates the account.
- Compare with the four criteria in a table. Add an explicit *trade-off* note: which criterion is the deciding one and **why does it depend on the situation**?
- ### If you are doing this alone — already solo.

**Default selection Rasmus should ship:**
- 🟢 MANDATORY: **Task 4.1** (*Peer review with the four criteria*). [AI-resilient by construction]
- 🟣 DEEPENING: **Task 4.3** (backup), **Task 4.4** (help-desk macro), **Task 4.5** (onboarding).
- Standby artefact pair for Task 4.1 (for students without a Week 2/3 artefact): a 4-step decomposition example and a 6-step algorithm example, both pre-written by Rasmus, both deliberately containing 2–3 weaknesses across the four criteria for a peer reviewer to find. **Place these in an appendix at the end of `student-tasks.md`, clearly labelled "Standby artefacts (use only if you do not have your own Week 2 or Week 3 work)".**

**Each task ends with `### Keep your notes`** — names **AT2** (the Week 5/6 process description) explicitly: "Keep your peer-feedback notes, the revision, and the change note. AT2 at the end of Week 5/6 will ask you to describe a process and to revise it after feedback — exactly the habit you trained this week."

**Length target:** ~1300 words.

---

### File 4 — `student/week-04/vocabulary.md` (10–18 terms)

**Required terms** (Rasmus may add 1–3 more if useful, but must not skip any required ones):

1. Valid solution
2. Alternative (solution)
3. Criterion (singular)
4. Criteria (plural)
5. Clarity (as a criterion)
6. Efficiency (as a criterion)
7. Repeatability (as a criterion)
8. Error-proneness (as a criterion)
9. Trade-off
10. Peer review
11. Feedback (criterion-named)
12. Revision
13. Rubric (informal)
14. **Iteration** — flagged as **"looking ahead — central in Week 5 and reused in AT2/AT3"**.

Optional additions Rasmus may include: *artefact* (revisited from W1), *protocol*, *reviewer*, *author*.

Each definition is 1–3 sentences, plain English, with a short everyday example where natural.

**Target:** ~14 terms.

---

### File 5 — `student/week-04/slides.md` (~12–18 slides, acceptance 10–20)

**Recommended slide outline (Rasmus may adjust order and titles within the spirit of the structure). The numbering below is the one teacher-materials.md will cite in its "Slide cues" subsections — keep it stable.**

1. `# Week 4 — Comparing solutions` *(title slide)*
2. `## The central message` — body: the central message **verbatim**.
3. `## Where Week 4 sits` — one-line recap of Weeks 1–3, one-line preview of Weeks 5–8.
4. `## A problem is not the same as its solution` — short framing slide.
5. `## Two ways to make tea` — side-by-side recipe (use a Markdown table; or pair of short numbered lists).
6. `## Two ways to back up a project folder` — IT mirror, side-by-side.
7. `## What is the same, what is different?` — 3–4 bullets.
8. `## From taste to criterion` — the conceptual pivot.
9. `## The four criteria` — one-line definitions, in fixed order: **clarity · efficiency · repeatability · error-proneness**.
10. `## Clarity in two tea recipes` — worked example.
11. `## Efficiency in two backup methods` — worked example.
12. `## Repeatability and error-proneness — quick examples` — combined slide.
13. `## Trade-offs — when criteria pull in different directions` — short slide.
14. `## The peer-review protocol` — three bullets: criteria → feedback → revision.
15. `## Feedback that someone can use` — 3 short rules (name the criterion; one concrete spot; critique the artefact, not the person).
16. `## Tasks this week` — must-do minimum vs. deepening, 1 line per task.
17. `## What comes next: Week 5 — logic structures` — preview, plus AT2 reminder.
18. `## Recap — the central message, one more time` — the central message **verbatim** (satisfies the verbatim-on-slide requirement alongside slide #2).

**Target:** ~16 slides. Use `---` on its own line between every slide. Body content: 3–5 short bullets or 1–2 short sentences. No speaker-note syntax that assumes a specific renderer.

---

### Supplementary deck — `student/week-04/slides-l11-criteria-walkthrough.md` (4–8 slides, OPTIONAL but recommended)

**Recommendation: ship it.** The four-criteria walkthrough on the two tea recipes (slide 10) plus the two backup methods (slide 11) is the densest lecture segment of the week. A short supplementary deck lets the teacher project the side-by-side comparison without the main deck losing its rhythm. If Rasmus chooses **not** to ship this deck, slides 10–12 of the main deck must each have at least 3 bullets and the L11 plan in `teacher-materials.md` must include an alternative paper-handout fallback.

**Suggested 6-slide outline for `slides-l11-criteria-walkthrough.md`:**

1. `# Worked example — two tea recipes` — title slide.
2. `## Recipe A (boil-first)` — the 5-step recipe.
3. `## Recipe B (steep-first)` — the 5-step recipe.
4. `## Both reach the goal — but the steps differ` — short list of the concrete differences.
5. `## The four criteria, side by side` — a 4-row table (criterion · Recipe A · Recipe B), one short sentence per cell.
6. `## The trade-off in plain English` — 1–2 sentences: A wins on clarity, B wins on efficiency, the right choice depends on whether the follower has done this before.

Optional 7th and 8th slides if Rasmus also wants to walk the backup-methods example in the supplementary deck — recommended only if it doesn't pad the main deck.

---

### File 6 — `teacher/week-04/teacher-materials.md` (2400–4200 words)

**Required H2 sections (in this order, with these exact headings — verbatim per acceptance criterion #17):**

1. `## Week 4 learning objectives (mapped to Bloom)` — restate the L10–L12 objectives from this plan, grouped by Bloom stage. Understanding dominant; light Analyzing acceptable in L10(d), L11(d) and L12(b). Forbidden verbs list spelled out.

2. `## Common misconceptions for Week 4` — at least 6 across the week (2 per lesson). Suggested set:
   - **L10**: "If there is more than one valid solution, then it doesn't matter which I pick." → Correction: it matters once you have a stated criterion. Without one, "doesn't matter" is honest; with one, you can defend a choice. // "If my solution is different from the teacher's, mine must be wrong." → Correction: as long as the solution reaches the goal and is clearly written, it is valid. The teacher's is one option among several.
   - **L11**: "Efficient = fast." → Correction: efficient in this course means *no wasted steps*. A fast but error-prone solution can still be inefficient overall because of the rework. // "A good solution wins on every criterion." → Correction: real solutions trade off — the four criteria can pull in different directions, and naming the trade-off is the analysis.
   - **L12**: "Feedback is criticism." → Correction: feedback that names a criterion is information; without a criterion it is taste. The protocol forces the criterion. // "I have to act on every piece of feedback." → Correction: you have to *consider* it and be able to say which criterion it speaks to. You may reasonably reject feedback if the criterion doesn't apply here.
   - Bonus (often appears in L11): "These four are the only criteria that exist." → Correction: many criteria exist in the wider world (cost, accessibility, security). For this course we work with four because they are enough to train the habit; later weeks and later courses add more.

3. `## Lesson 10 — 90-minute plan` — concrete time slots summing to 90, with an independent-work block of **27–45 min**. Suggested skeleton (must contain a `Slide cues` subsection):
   - 0–10 min: warm-up — pair "two ways to make tea" on the board (collect 2–3 student variations).
   - 10–25 min: instructor input — central message; "a problem is not the same as its solution"; the two tea recipes side by side.
   - 25–55 min: **INDEPENDENT WORK** (30 min) — each student picks one familiar everyday task they personally do and writes **two valid alternative algorithms** for it (5–8 steps each). No criteria yet; just notice variety.
   - 55–75 min: pair activity — students swap and identify, in writing, two concrete ways the partner's two solutions differ from each other.
   - 75–88 min: whole-class debrief — collect on the board 4–5 places where students found differences (step order, what's left implicit, where the user has to choose).
   - 88–90 min: preview of Lesson 11.
   - **`Slide cues` subsection.** main deck slides used: title (slide 1), central message (2), where Week 4 sits (3), problem vs. solution (4), two tea recipes (5), two backups (6 — optional in L10, can defer to L11), what is same/different (7). No supplementary deck in L10.

4. `## Lesson 11 — 90-minute plan` — same arithmetic constraint. Suggested:
   - 0–10 min: warm-up — recap "two valid solutions" with one student-supplied pair from L10.
   - 10–35 min: instructor input — *taste → criterion*, the four criteria with definitions, the worked example on the tea recipes (project the **supplementary deck** here). Roughly 25 min of lecture — the densest input block of the week.
   - 35–65 min: **INDEPENDENT WORK** (30 min) — each student takes their own two L10 alternative algorithms and applies all four criteria, criterion by criterion, in a 4-row table. They are explicitly *not* asked to pick a winner.
   - 65–82 min: pair activity — students swap criterion tables and check: did the partner mention the criterion by name in every row? Did they cite a specific step?
   - 82–88 min: whole-class debrief — collect 3–4 places where criteria pulled in different directions (trade-offs).
   - 88–90 min: preview of Lesson 12 (peer review).
   - **`Slide cues` subsection.** main deck slides 8 → 13 (from taste to criterion through trade-offs). **Supplementary deck `slides-l11-criteria-walkthrough.md` slides 1 → 6 used during the 10–35 min lecture block, between main-deck slide 9 and main-deck slide 13.**

5. `## Lesson 12 — 90-minute plan` — same arithmetic constraint. The MANDATORY in-class activity (peer-review protocol) **lives in this lesson**. Suggested:
   - 0–10 min: warm-up — restate the peer-review protocol in three bullets on the board; remind students to bring their own Week 2 or Week 3 artefact (have standby artefacts ready).
   - 10–22 min: instructor input — "Giving feedback someone can use" and "Receiving feedback you don't agree with" walkthroughs. Brief.
   - 22–52 min: in-class activity — **MANDATORY peer-review protocol** (see `in-class-tasks.md`), pairs, 30 min. Criteria → feedback → exchange.
   - 52–82 min: **INDEPENDENT WORK** (30 min) — each student revises their own Week 2/Week 3 artefact in response to one piece of partner feedback, and writes the 3–5 sentence change note.
   - 82–88 min: whole-class debrief — 3 volunteers share what changed and which criterion drove it.
   - 88–90 min: preview of Week 5 (logic structures) and the AT2 link.
   - **`Slide cues` subsection.** main deck slides 14 → 18 (peer-review protocol, feedback rules, tasks this week, what comes next, recap). No supplementary deck in L12.

6. `## Facilitation tips` — 6–10 short tips. Suggestions:
   - Police the *taste → criterion* framing. Every "I just like this one" gets gently bounced back to "which criterion?"
   - Resist the urge to crown a winner in the L10/L11 worked examples. Both tea recipes work. The point is *how they differ*, not which is best.
   - In L11, the lecture block is unusually long (25 min). Break it with one student-voiced example halfway through.
   - In L12, pairs that get stuck on "I have no feedback" should be prompted with the criterion list: "go through clarity, efficiency, repeatability, error-proneness in order, one at a time".
   - Have the standby artefact pair printed and on the teacher's desk before L12; some students will forget theirs.
   - Mid-course pulse-check: this is a natural moment to ask the class "what from Weeks 1–3 still feels shaky?". Note it for revision in later weeks; do not derail Week 4.

7. `## Answers to common student questions` — at least 5 across the week. Suggested:
   - *"What if my two solutions are basically the same?"* — Then they are not really two solutions. Push for differences in step order, in what is left implicit, or in who has to choose.
   - *"Which criterion is the most important?"* — None of them in the abstract. The most important criterion depends on the situation. Naming the trade-off is the answer.
   - *"Is there a right answer to the comparison?"* — There is a right answer **once you name a criterion**. Without a criterion, "right" is taste.
   - *"What if my partner's feedback is wrong?"* — Say which criterion it speaks to, and say why you don't think it applies here. That is the answer.
   - *"Do I need a computer for any of this?"* — No. Week 4 is all paper, board and conversation.
   - *"Can I use ChatGPT for the comparison?"* — Only as a sparring partner in the DEEPENING tasks, with the supplied prompt. The MANDATORY work is your own artefact and a real partner's feedback.

8. `## Formative assessment tips` — 3–5 quick checks (exit ticket on "name the four criteria"; one-minute paper on "describe one trade-off from today's lesson"; pair report-back; board vote on which criterion was hardest to apply). No summative assessment in Week 4. Mid-course pulse check is a soft formative tool here.

**Cross-references.** `in-class-tasks.md` is cross-referenced from the L12 plan (the MANDATORY peer-review protocol).

**Length target:** ~3300 words.

---

### File 7 — `teacher/week-04/in-class-tasks.md` (400–1200 words)

**Required structure:**

- `## Overview` — 2–3 sentences. The week's mandatory in-class exercise is the **peer-review protocol**; an optional pair activity exists for L10. Both fit inside their respective 90-min plans.

**Two activity ideas Rasmus should ship (default: both):**

**Activity A — MANDATORY — "Peer review with the four criteria"** *(pair, teacher-led, ~30 min, slotted in Lesson 12 between 22–52 min)*
- Pre-class: students are told in L11 to bring **one of their own Week 2 decompositions or Week 3 algorithms/flowcharts**. Teacher has the standby artefact pair printed for students who forget.
- Pairing: simple seat-neighbour pairs; teacher pre-pairs students with very different artefacts when possible.
- Protocol, on the board:
  1. **Silent read** (4 min). The reviewer reads the partner's artefact without speaking.
  2. **Criterion pass** (10 min). The reviewer writes one sentence per criterion (4 sentences total) in the fixed order — clarity, efficiency, repeatability, error-proneness — each sentence either "Strong on X because…" or "Could be improved on X because…", each naming a specific step or block.
  3. **Pick two** (3 min). The reviewer picks the **two most useful** of the four sentences. Those are the feedback the partner will receive.
  4. **Exchange + 5-min Q&A per pair** (~10 min total for both directions). The reviewer hands over the two pieces of feedback. The author may ask one clarifying question per piece. **No defending — only clarifying.**
  5. **Hand back** to the author; the revision step lives in the 52–82 min INDEPENDENT WORK block, not in this activity.
- Teacher's job during the activity: rotate, listen for "I just like this one" or "this is wrong" without a criterion, and gently bounce the comment back to a criterion. Police taste → criterion in real time.
- **Why it requires the classroom:** the live exchange, the silent read, the no-defending Q&A, and the on-the-spot bouncing of taste-comments back to criteria all depend on the room. The protocol cannot be done asynchronously without losing its training effect.
- **Cross-referenced from `teacher-materials.md`** in the L12 plan.

**Activity B — OPTIONAL — "Variation hunt" (pair, ~20 min, can be slotted in Lesson 10 between 55–75 min)**
- Students pair up. Each student brings their two valid alternative algorithms from the L10 INDEPENDENT WORK block.
- Pair A reads Pair B's two algorithms aloud and identifies **at least two ways they differ from each other**, naming the differences in plain English (step order; implicit choice points; granularity).
- Roles swap.
- Whole-class harvest: 4–5 differences go on the board. This becomes the lead-in to L11's criterion lecture.

**Cross-reference back to `teacher-materials.md` so the teacher knows the exact 90-min slot for each.**

**Length target:** ~700 words.

---

## Avoimet kysymykset

1. **Standby artefact pair.** Some students will not have a Week 2 or Week 3 artefact to bring to L12 (absence, low completion, transferred in). **Default assumption:** Rasmus ships a short standby pair (one 4-step decomposition + one 6-step algorithm, both with 2–3 deliberate weaknesses) in an appendix of `student-tasks.md`, clearly labelled as a fallback. Wilhelm spot-checks that it exists.

2. **Supplementary deck for L11.** This plan recommends shipping `slides-l11-criteria-walkthrough.md` (6 slides). **Default assumption:** Rasmus ships it. If he doesn't, slides 10–12 of the main deck must each carry the walkthrough load with ≥3 bullets, and `teacher-materials.md` L11 plan must include a paper-handout fallback for the worked example.

3. **Bloom cap interpretation of "compare".** The brief caps Bloom at *Understanding + light Analyzing*. *Compare criterion-by-criterion* sits at the boundary. **Default assumption:** the verb *compare* is used as light Analyzing only when it is criterion-named (e.g. "compare A and B on clarity"). Bare *compare* without a criterion stays in Understanding. Wilhelm uses the criterion-named test.

4. **"Best solution" wording.** The plan forbids "the right answer / the best solution" without a criterion next to them. **Default assumption:** Rasmus may use "the better one on clarity" or "the better one in this situation" freely; bare "the best one" gets flagged. Wilhelm uses substring grep + context check.

5. **Numeric scoring temptation.** Students will reach for "I'd give recipe A a 4/5 on clarity". **Default assumption:** Rasmus pre-empts this explicitly in `self-study.md` (one sentence: "We do not assign numeric scores. The four criteria are lenses to describe with, not a rubric to grade with.") and in `teacher-materials.md` (one bullet in facilitation tips).

6. **AT2 link wording.** Every `### Keep your notes` block should reference AT2. The exact phrasing matters because Wilhelm greps. **Default assumption:** Rasmus uses the wording "AT2 at the end of Week 5/6" or "the AT2 process description in Week 5/6". AT1 is not mentioned in any Keep-your-notes block in Week 4.

7. **"If you are doing this alone" — which tasks need it?** Plan requires it on every task whose flow assumes a partner / follower / reviewer. **Default assumption:** Task 4.1 (MANDATORY) needs it (concrete alternative: 24-hour-gap self-review, optionally class-chat post). Tasks 4.3, 4.4, 4.5 are inherently solo and don't need the subsection — but Task 4.4's optional sparring step uses an LLM, which is solo too. Wilhelm checks task-by-task.

8. **Verbatim central message — punctuation and dashes.** The central message contains an em-dash. **Default assumption:** Rasmus uses the em-dash form (`—`, not `--` and not a hyphen) consistently. Wilhelm greps with the literal em-dash form first; if zero hits, also greps with `--` as a hint and reports drift.

9. **Pair-work failure mode.** If a cohort cannot reliably pair up (odd numbers, absences, an isolated student), the L12 plan needs a fallback. **Default assumption:** the teacher pairs the isolated student with the teacher themselves for the protocol, or runs Task 4.2 (the supplied tea-recipe comparison) as the must-do-minimum substitute that one day. Rasmus mentions this fallback explicitly in `teacher-materials.md` §Facilitation tips.

10. **Mid-course pulse check vs. forward motion.** L12 is a natural moment to surface Week-1–3 gaps. **Default assumption:** Rasmus mentions the pulse check in `teacher-materials.md` §Facilitation tips and §Formative assessment tips, but **does not** add a dedicated whole-class debrief slot to the L12 plan — Week 4 must end on the peer-review-and-revision habit, not on a Week 1–3 review.
