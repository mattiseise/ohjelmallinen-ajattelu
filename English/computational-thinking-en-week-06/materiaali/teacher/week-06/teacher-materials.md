# Week 6 — Teacher materials

This document covers all three lessons of Week 6 (L16, L17, L18) in one place. It is built around the same central message the students see: **"Pseudocode is the bridge between everyday English and real code: precise enough for a computer to follow if it had to, readable enough to share with a non-programmer."** Week 6 is the synthesis week of the computational-thinking half of the course. Everything from Weeks 1–5 — clear sequence, abstraction, conditions and repetition — is folded into a single more precise notation, and the under-practised skill of reading code on paper is trained for the first time.

**AT2 is submitted around Lesson 18 of this week.** It asks for a short piece of pseudocode for a small process, a trace table for one normal and one awkward input, and a short reflection in plain English. The L16–L18 arc is the AT2 raw-material factory: L16 produces the pseudocode, L17 sharpens the variables and input/processing/output skeleton, L18 produces the trace and surfaces any bugs.

No real programming language appears anywhere this week. Pseudocode keywords are UPPERCASE shared course conventions, not a language a computer can run. Testing means dry-running on paper with a trace table, full stop. Real code arrives in Week 7.

Cross-references: the supplementary deck `slides-l16-pseudocode-walkthrough.md` is used during L16's lecture segment. The mandatory in-class activity *Dry-run as a class* is described in `in-class-tasks.md` and belongs in the 55–80 min slot of L18.

---

## Week 6 learning objectives (mapped to Bloom)

Week 6 stays inside **Understanding** and **Applying**. Forbidden verbs for Week 6 objectives: *evaluate, judge, design, create, build, develop, abstract, decompose* — those belong to Weeks 4 and 8. Light Analysing (naming the type of bug) appears in deepening tasks only, never as a primary objective.

### Lesson 16 — Pseudocode: from natural language to a more precise format

- **Understanding:** the student can **define** *pseudocode* in their own words, and **contrast** it with everyday English and with a real programming language.
- **Understanding:** the student can **identify** the three building blocks already met in Week 5 — sequence, condition, repetition — inside a short piece of pseudocode.
- **Applying:** the student can **write** a 10–20 line piece of pseudocode for a familiar process, using the small fixed keyword set (`SET`, `READ`, `WRITE`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`).
- **Understanding:** the student can **explain** why pseudocode is more reliable to share than English prose for an instruction a computer will eventually execute.

### Lesson 17 — Input, processing, output, and the idea of a variable

- **Understanding:** the student can **describe** the input → processing → output skeleton of a piece of pseudocode.
- **Understanding:** the student can **define** *variable* in their own words: a named container for one value that can change while the pseudocode runs.
- **Applying:** the student can **use** `SET variableName TO value`, `READ variableName` and `WRITE variableName` correctly in pseudocode.
- **Understanding:** the student can **recognise** that the *name* of a variable should describe what it holds.

### Lesson 18 — Testing pseudocode: dry running and finding errors

- **Understanding:** the student can **explain** what a trace table is and why dry-running on paper finds bugs that re-reading does not.
- **Applying:** the student can **dry-run** a short piece of pseudocode line by line using a trace table, updating each variable at each step.
- **Applying:** the student can **find** at least one bug in deliberately broken pseudocode by dry-running it.
- **Applying:** the student can **fix** the bug and dry-run the corrected pseudocode to confirm the expected output.

---

## Common misconceptions for Week 6

At least two misconceptions per lesson. Pre-empt them where they fit naturally — most surface on their own during the independent-work block or the in-class dry-run.

### Lesson 16 misconceptions

**Misconception:** *"Pseudocode is a programming language."*
**Correction:** Pseudocode is a shared writing convention, not a language a computer can run. No interpreter exists for `SET counter TO 5`. A human reader (or a translator) is always in the loop. The point of the shared keywords is so that every reader in the room interprets the same shape the same way.

**Misconception:** *"There is one correct pseudocode."*
**Correction:** Different teachers and textbooks use different keyword sets. Some prefer lowercase `if`, some prefer `:=` for assignment. This course uses one fixed set so the room reads each other's pseudocode the same way. In a real workplace, every team picks one set and sticks to it.

### Lesson 17 misconceptions

**Misconception:** *"A variable is the same as a number."*
**Correction:** A variable is a named container. Today it holds a number; tomorrow the same variable might hold a different number, a yes/no, or a short string. The container is the variable; the value inside it is a separate thing. Connect to the labelled-box metaphor every time.

**Misconception:** *"The name of a variable does not matter."*
**Correction:** `x` and `passwordLength` do the exact same thing for an imaginary computer, but very different things for the next person reading the pseudocode (which, often, is tomorrow-you). The whole point of pseudocode is that a stranger can read it. A bad name throws that away.

### Lesson 18 misconceptions

**Misconception:** *"If the pseudocode reads correctly, it is correct."*
**Correction:** Reading does not catch off-by-ones, wrong comparisons, or missing initialisations. The eye glides over them. Only a trace table forces every line to declare what every variable equals after it has run. That is the whole point.

**Misconception:** *"A trace table is busywork — I can dry-run it in my head."*
**Correction:** Head-tracing is exactly where bugs survive. The table forces each step onto paper, and the act of writing the new value of a variable is where the brain catches what the eye missed. Students who skip the table are the students who submit AT2 with an undiscovered off-by-one.

**Bonus misconception:** *"Pseudocode is the same as code, so I might as well write real code."*
**Correction:** Not yet. Pseudocode strips away syntax noise so the structure is visible. The same student who writes real code next week with confidence is the student who built the pseudocode habit this week. Skipping the pseudocode step is skipping the thinking step.

---

## Lesson 16 — 90-minute plan

**Topic.** Pseudocode: from natural language to a more precise format.

**Central message for this lesson (one sentence).** Pseudocode is not a new language to memorise — it is the things you already write, with a few shared words and a fixed shape so a stranger can read it the same way you do.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: teacher reads one short English instruction aloud (suggested: a tea recipe, four sentences). Class compresses it on the board into pseudocode-like form, line by line, using only words they have already heard in earlier weeks. | Whole-class |
| 0:10–0:30 | Instructor input: define *pseudocode*; introduce the small keyword set (`SET`, `READ`, `WRITE`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`). **Run the supplementary deck `slides-l16-pseudocode-walkthrough.md` here in full** — it walks the tea recipe from English to a finished annotated piece of pseudocode. | Lecture |
| 0:30–1:00 | **Independent work** (30 min): each student begins Task 6.1 — writing pseudocode for a familiar process they personally do. Just the writing this lesson; the dry-run waits for L18. | Independent |
| 1:00–1:20 | Pair activity: students swap drafts and read each other's pseudocode silently, underlining one line that is unclear and circling one variable name that does not describe what it holds. | Pair |
| 1:20–1:28 | Whole-class debrief: collect three example lines from the swap; rewrite together on the board. Connect to the L16 central message. | Whole class |
| 1:28–1:30 | Closing: one-line preview of Lesson 17 — *"Next we name the place pseudocode keeps the things it needs to remember while it runs."* | Whole class |

**Independent-work block: 30 minutes (33% of 90 minutes).** Meets the 30–50% rule.

**Cross-references.** L16 does not use any activity from `in-class-tasks.md`. The mandatory in-class activity belongs in L18.

**What you say out loud.** *"You have been writing this kind of thing since Week 1. Pseudocode is the same thinking with a few shared words on top. A `SET` is just *the bag now contains*. An `IF` is just *the test that splits the path*. A `WHILE` is just *keep doing this until the stop happens*. The point of the shared words is that every reader in this room interprets the same line the same way."*

**Materials.** Board and marker; paper and pens; the supplementary deck `slides-l16-pseudocode-walkthrough.md` on screen during the lecture segment. No technology required for students.

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** slide **4** (*What is pseudocode?*) on screen as the board carries the live English → pseudocode compression.
- **Lecture (0:10–0:30):** main deck slides **4 → 7**: *What is pseudocode?* · *The small set of keywords* · *English vs. pseudocode — making tea* · *Sequence · condition · repetition*. **Between slides 5 and 6, switch to the supplementary deck `slides-l16-pseudocode-walkthrough.md` and run it end-to-end** (6 short slides, ~10 min) — it walks the tea example all the way through. Return to main deck slide 6 for the side-by-side close.
- **Independent work (0:30–1:00):** leave main deck slide **5** (*The small set of keywords*) on screen as the silent reference card.
- **Pair activity (1:00–1:20):** no slides; work on paper.
- **Debrief (1:20–1:28):** no slides. Use the board for the three rewrites.
- **Closing (1:28–1:30):** no slides.

---

## Lesson 17 — 90-minute plan

**Topic.** Input, processing, output, and the idea of a variable.

**Central message for this lesson (one sentence).** A pseudocode program is almost always a small machine that takes input, does something with it, and produces output — and a variable is the place where it keeps the things it needs to remember while it runs.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: name three real-world "variables" in the room (the date on the board, the current speaker, the lunch menu). Set up the labelled-box metaphor before the keyword arrives. | Whole-class |
| 0:10–0:30 | Instructor input: define *variable*; walk the input → processing → output skeleton; write the password-strength example on the board, line by line, using `SET`, `READ`, `IF/ELSE/ENDIF` and `WRITE`. Pause to name each line as input, processing or output. | Lecture |
| 0:30–1:00 | **Independent work** (30 min): each student takes their L16 pseudocode and (a) labels the input, processing and output sections; (b) replaces any unnamed values with named variables; (c) underlines any variable name that does not describe what it holds. | Independent |
| 1:00–1:20 | Pair activity: pairs trace each other's input/processing/output skeleton on paper — can you spot where the processing happens? Where the input ends? Mark on the partner's pseudocode. | Pair |
| 1:20–1:28 | Whole-class debrief: one example on the board. Where did the processing block start and end? Which variable name had to be rewritten? | Whole class |
| 1:28–1:30 | Closing: preview L18 and AT2. *"Next lesson we test the pseudocode. AT2 is submitted around the end of next lesson."* | Whole class |

**Independent-work block: 30 minutes (33% of 90 minutes).** Meets the 30–50% rule.

**Cross-references.** L17 does not use any activity from `in-class-tasks.md`. No supplementary deck is shipped for L17; the password-strength example is short enough to walk live on the board, and main-deck slide 11 carries it for review.

**What you say out loud.** *"Look at any pseudocode you wrote last lesson. There is a part where it asks for something from the outside — that is the input. There is a part where it decides or counts or compares — that is the processing. There is a part where it tells the outside something back — that is the output. Most useful pseudocode has all three. The middle bit is where the variables earn their pay."* Walk the password-strength example: read a password, count its length, set `isStrong` to YES if length is at least 8 and it contains a digit, otherwise NO; write the result.

**Materials.** Board and marker; paper and pens; main deck on screen.

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** slide **8** (*Input → processing → output*) on screen as the class names variables in the room.
- **Lecture (0:10–0:30):** main deck slides **8 → 11**: *Input → processing → output* · *What is a variable?* · *A good variable name* · *A vocational example — password strength*. Dwell on slide 11; walk every line of the password example on the board next to it.
- **Independent work (0:30–1:00):** leave slide **9** (*What is a variable?*) on screen as the silent reference.
- **Pair activity (1:00–1:20):** no slides; pairs work on paper.
- **Debrief (1:20–1:28):** no slides; use the board.
- **Closing (1:28–1:30):** slide **15** (*AT2 — submitted around Lesson 18*) for the calm preview.

---

## Lesson 18 — 90-minute plan

**Topic.** Testing pseudocode: dry running and finding errors. **AT2 is submitted around this lesson.**

**Central message for this lesson (one sentence).** Pseudocode is not finished when it looks right; it is finished when a trace table proves it produces the expected output, including on at least one awkward input.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: board demo of a trace table for a 4-line pseudocode snippet (suggested: swap two values using a temporary variable). The teacher writes; the class calls out each new value. | Whole-class |
| 0:10–0:25 | Instructor input: define *dry run*; show how to draw a trace table (columns = line, each variable, output); name what counts as a bug (actual output differs from expected output). Link back to Week 1's "literal robot" — the student playing literal robot on their own pseudocode, on paper. | Lecture |
| 0:25–0:55 | **Independent work** (30 min): each student dry-runs their own Task 6.1 pseudocode for one normal input and one awkward input, drawing the trace table by hand. | Independent |
| 0:55–1:20 | **MANDATORY teacher-led in-class activity — *Dry-run as a class*** (Activity A in `in-class-tasks.md`, ~25 min). Teacher writes a deliberately broken short pseudocode on the board; the class becomes the trace table, one student per variable, calling out updates line by line. The bug emerges. The class fixes it on the board. | Whole class |
| 1:20–1:28 | AT2 handover: 5 minutes on what AT2 expects (pseudocode for a small process, trace table for one normal and one awkward input, short reflection), 3 minutes for clarifying questions. Calm pace. | Whole class |
| 1:28–1:30 | Closing: one-line preview of Week 7 — *"Next week the same pseudocode shape becomes a tiny program in a real language you run in a browser."* | Whole class |

**Independent-work block: 30 minutes (33% of 90 minutes).** Meets the 30–50% rule.

**Cross-references.** The 55–80 min slot is **Activity A — *Dry-run as a class*** from `in-class-tasks.md`. Prepare the broken pseudocode on a slip or in your notes before class. Activity B (*Pseudocode swap and trace*) from the same file is optional and fits L16's 1:00–1:20 slot if the lecture runs short.

**What you say out loud.** *"You read your own pseudocode last lesson and it looked fine. Today we test it. The trace table is the test. You write down what every variable equals after every line. When you do this honestly, two things happen: first, the pseudocode that looked fine sometimes turns out to be wrong, and second, the pseudocode that you suspected might be wrong turns out to be fine. Either way you learn something the eye could not."* For the AT2 handover: *"AT2 is one piece of pseudocode for a small process, a trace table for one normal and one awkward input, and a five-sentence reflection. The work you have done in Tasks 6.1 and 6.2 is the work AT2 asks for. Nothing new."*

**Materials.** Board and marker; paper and pens; the broken pseudocode from `in-class-tasks.md` Activity A ready to write on the board at 0:55.

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** slide **12** (*What is a dry run?*) on screen as the board carries the live swap-values trace.
- **Lecture (0:10–0:25):** main deck slides **12 → 14**: *What is a dry run?* · *The trace table* · *Finding a bug — actual vs. expected output*. Dwell on slide 13; the trace table on screen and the live demo on the board reinforce each other.
- **Independent work (0:25–0:55):** leave slide **13** (*The trace table*) on screen as the silent reference for the table format.
- **In-class activity (0:55–1:20):** no slides. The dry-run lives on the board — that is the lesson.
- **AT2 handover (1:20–1:28):** slide **15** (*AT2 — submitted around Lesson 18*).
- **Closing (1:28–1:30):** slide **19** (*What comes next — Week 7: first real code*) for the one-line preview, then slide **20** (*Recap — the central question, one more time*) so students leave on the verbatim central question.

---

## Facilitation tips

### Before any of the three classes

- **Test the central message on yourself.** Read it aloud slowly: *"Pseudocode is the bridge between everyday English and real code: precise enough for a computer to follow if it had to, readable enough to share with a non-programmer."* It appears verbatim on at least one slide. Mirror it in your own speech at least twice per lesson; it is the spine of the week.
- **Pre-write the board layout.** For L16, sketch the English → pseudocode side-by-side for tea. For L17, sketch the password-strength example with input/processing/output boxes. For L18, sketch a blank trace table with three named columns (line, variable, output). Drawing this live is fine; thinking about it live is risky.
- **Read `in-class-tasks.md` end-to-end before Lesson 18.** Activity A — *Dry-run as a class* — needs the broken pseudocode prepared in advance. Decide which bug type you will use (off-by-one in a `WHILE` condition is the recommended default — easy to introduce, easy to fix, hard to spot by reading alone).

### During class

- **Insist on UPPERCASE keywords.** `SET`, `IF`, `WHILE` in capitals; everything else in lowercase. The visual contrast is the half of the readability that is free. Students who write `set` and `if` lose that.
- **Insist that students read pseudocode out loud during the dry run.** The voice catches what the eye misses. *"WHILE counter is greater than one, do…"* — heard aloud, the off-by-one becomes audible.
- **Do not let students re-write pseudocode while they trace it.** Trace first on one page; fix on a separate page. Mixing the two is how bugs hide.
- **Protect the 30-minute independent block.** It is the part teachers under pressure cut first, and it is where AT2 readiness is built. If the lecture runs long, trim the lecture, not the independent work.
- **Use the board for trace tables, not slides.** Slides set up the question; the trace must happen live. The embodied trace in L18 is the lesson — a slide cannot do what a moving marker on a board does.
- **Connect every new term back to Weeks 1 and 5.** Week 6 is synthesis. *Variable* is a labelled box (Week 1's clear naming). *Trace table* is the literal robot reading line by line (Week 1). *Sequence, condition, repetition* are Week 5's three structures. Nothing new appeared without precedent.
- **When students argue with the trace table, ask three questions in order:** *"What did line 4 say? Read it aloud. Now what does the variable equal after line 4?"* The argument always loses.

---

## Answers to common student questions

- *"Is pseudocode a real language?"* — No. It is a shared writing convention. Different teachers use different keyword sets. We use one fixed set in this course so every reader in the room interprets the same line the same way.
- *"Can a computer run pseudocode?"* — Not directly. A human, or a translator, has to turn it into a real language first. Week 7 is where that translation starts.
- *"Do I have to use these exact keywords?"* — In this course, yes — so we can read each other's pseudocode the same way. In a real workplace, every team picks one set and sticks to it.
- *"What does AT2 actually want from me?"* — Short pseudocode (10–20 lines) for a small process you choose, a trace table for one normal and one awkward input, and a five-sentence reflection on what your trace found. Nothing new beyond Tasks 6.1 and 6.2.
- *"What if my trace table disagrees with my pseudocode?"* — Trust the trace over your head. Then either your pseudocode has a bug, or your trace has one. Re-do the trace on a fresh page; whichever one budges is the one that was wrong.
- *"Is `WRITE` the same as `PRINT`?"* — In this course, yes. We use `WRITE` consistently; some textbooks use `PRINT`. Pick one and stay with it.
- *"What if my variable is a yes/no?"* — Then it is still a variable. `SET isStrong TO YES` is exactly the same kind of `SET` as `SET counter TO 0`. The variable does not care what is inside it; the reader does.

---

## Formative assessment tips

Week 6 leads directly to AT2, so the role of formative checks is to make understanding visible *before* the AT2 deadline. Use one or two per lesson.

### Per-lesson informal checks

- **Lesson 16 — exit ticket (3 min, end of class).** Each student writes one sentence: *"Name one keyword from the L16 set and one line you used it on."* Skim on the way to L17. If more than a few students cannot name a keyword in their own pseudocode, revisit the keyword card at the start of L17.
- **Lesson 17 — sticky-note collection.** Each student writes one variable from their pseudocode and one value it could hold. Read three at random; the class spots the one bad name. Pattern across the class tells you whether name-honesty has landed.
- **Lesson 17 — board vote.** Show three short snippets on the board and ask which has the clearest input/processing/output skeleton. The pattern of hands shows you whether the three-part shape is visible to students yet.
- **Lesson 18 — pair report-back at end of independent work.** Each pair reports one thing the trace caught that the reading missed. If most pairs say *"nothing"*, the traces were probably not honest — push back gently and re-seed with the swap-values demo.
- **Lesson 18 — one-minute paper at end of week.** *"In one sentence, what does a trace table do that re-reading does not?"* The answers tell you, before AT2 lands, who has internalised the L18 central message and who still believes head-tracing is enough.

### What you are listening for across the week

The three phrases that mark genuine understanding by the end of Week 6:

- *"What does the variable equal after this line?"* (when reading pseudocode aloud).
- *"Let me trace it on paper."* (when an output looks suspicious).
- *"Actual differs from expected at line 4."* (when reporting a bug — line number, not vibe).

If those phrases appear in student speech by the end of L18, AT2 lands without remediation. If not, the most useful 5 minutes of L18's AT2 handover is a recap of the trace-table format. The *Dry-run as a class* activity in `in-class-tasks.md` is the central diagnostic of the week — a class that catches the bug confidently is a class ready for AT2.
