# Week 5 — Teacher materials

This document covers all three lessons of Week 5 (L13, L14, L15) in one place. It is built around the same central message the students see: **"Almost any process can be described with three building blocks: sequence, condition, and repetition."** Week 5 names the three logic structures every described process is made of, and trains the student to recognise them in everyday speech *before* meeting them as code in Weeks 6–8. Week 5 is also the immediate foundation week for **AT2**, which lands at the end of Week 5 / during Week 6 and asks for a process description that explicitly uses all three structures. The three lessons sit together as a single arc — L13 names the *default* (sequence), L14 names *the test that splits the path* (condition), L15 names *the test that loops the path* (repetition with a stop).

No code is introduced this week. Pseudocode-like notation (`if … then … else …`, `for each …`, `repeat until …`) is allowed but treated as English shorthand, not as a formal language. Pseudocode proper arrives in Week 6.

Cross-references: the in-class activities used in L14 and L15 are described in `in-class-tasks.md` in the same folder.

---

## Week 5 learning objectives (mapped to Bloom)

Week 5 stays inside **Remembering** and **Understanding**, with **light Applying** allowed in all three lessons (express a condition in `if … then … else …` form; express a repetition with an explicit stop; draw a small decision tree; combine all three structures in one process description). The forbidden verbs for Week 5 objectives are *create, build, design, develop, evaluate, judge, debug, optimise, decompose*. *Analyze* may appear lightly in deepening tasks but not in the objectives. The course's higher Bloom levels return in later weeks.

### Lesson 13 — Sequence: a program proceeds step by step

- **Remembering:** the student can **define** *sequence* in their own words as "doing one step after another, in a fixed order".
- **Understanding:** the student can **identify** the sequence backbone in an everyday process (a recipe, a deployment checklist, a morning routine).
- **Understanding:** the student can **explain** why the order of steps usually matters, and give one example where swapping two steps breaks the process.
- **Light Applying:** the student can **write** a 6–10 step sequence for a familiar process, with the order made explicit by numbering.

### Lesson 14 — Conditions: if-then-else thinking and decision trees

- **Remembering:** the student can **define** *condition* in their own words as "a test that decides which step happens next".
- **Understanding:** the student can **recognise** `if … then … else …` shape in everyday rules (password rules, ticket-routing rules, *"if it rains, take the bus"*).
- **Understanding:** the student can **explain** the difference between `if … then …` (no alternative) and `if … then … else …` (an alternative).
- **Light Applying:** the student can **draw** a simple two- or three-branch decision tree for a familiar everyday rule.
- **Light Applying:** the student can **express** a real-life rule in natural-language `if … then … else …` form.

### Lesson 15 — Repetition: doing the same thing multiple times

- **Remembering:** the student can **define** *repetition* in their own words as "doing the same step or block of steps more than once, with a clear stop".
- **Understanding:** the student can **distinguish** *for each* (a known list), *repeat until* (a stopping condition), and *while* (a continuing condition) in everyday situations.
- **Understanding:** the student can **identify** repetition in familiar processes (an inbox sweep, marking attendance, charging a phone).
- **Light Applying:** the student can **express** a real-life repeated action in natural language with an explicit stopping or continuing condition.
- **Understanding:** the student can **spot** the difference between a one-off step and a repeated step in a process description.

---

## Common misconceptions for Week 5

At least two misconceptions per lesson appear here. Pre-empt them where they fit naturally — most surface on their own during the independent-work block or the classification game.

### Lesson 13 misconceptions

**Misconception:** "Sequence is too trivial to count as a building block."
**Correction:** Most real bugs come from a single swapped step. Sequence is the *default* — the absence of a written branch or loop — and the default is where breakdowns happen, because nobody thinks to test it. It is the foundation the other two structures sit on.

**Misconception:** "If I do not write a condition, the process has no decisions."
**Correction:** It means every step is unconditional — every step always happens, in the order written. Sequence is the *absence of branching*, not the absence of importance. A 6-step sequence with no conditions is still a complete process.

### Lesson 14 misconceptions

**Misconception:** "`if … then …` is the same as `if … then … else …`."
**Correction:** Without `else`, the follower does nothing extra otherwise. With `else`, the follower does something different on the false branch. *"If the milk smells off, throw it out"* and *"If the milk smells off, throw it out; otherwise pour it in your coffee"* are not the same instruction.

**Misconception:** "Compound conditions are advanced and I should avoid them."
**Correction:** Students already use AND and OR every day — *"if I have my card AND money on it, I can take the bus"*. Only the *symbols* are advanced; the *thinking* is not. Compound conditions stay in plain English in Week 5; symbolic logic does not appear at all.

### Lesson 15 misconceptions

**Misconception:** "A loop is just a sequence written down many times."
**Correction:** A loop is a single statement plus a stopping condition. If you write out *"check the next photo, check the next photo …"* 100 times, you have not understood repetition. `for each` and `repeat until` say *"the same thing, again, with a clear stop"* in one line.

**Misconception:** "`repeat until` always stops."
**Correction:** It stops if and only if the stopping condition can actually be observed and reached. *"Repeat until you understand"* is not a stop — a literal follower cannot check it. Honest repetitions need an observable stop, and many also need a *safety stop* (*"…or stop after 10 tries"*) to handle the runaway case.

**Bonus misconception:** "`for each` is a kind of sequence because it is just a list of steps."
**Correction:** `for each` is a repetition — the *same* step done once per item. The list is the stop: the follower stops when there are no more items. One statement, not many.

---

## Lesson 13 — 90-minute plan

**Topic.** Sequence: a program proceeds step by step.

**Central message for this lesson (one sentence).** Sequence is the default — when nothing else is said, *do A, then B, then C* is what a literal follower will do, so the order you write is the order you get.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: class names three everyday sequences out loud (likely answers: tea recipe, morning routine, route to school). Teacher writes them on the board, then **swaps two steps** in one of them (e.g. *"pour boiling water before putting the tea bag in"*) and asks the class what happens. | Whole-class |
| 0:10–0:25 | Instructor input: define *sequence*; walk one everyday sequence (tea or morning routine) and one IT sequence (a deployment checklist in plain English) side by side. Name *order* and *dependency* informally. | Lecture |
| 0:25–0:55 | **Independent work** (30 min): each student writes a 6–10 step sequence for a familiar process they really do, numbering every step. They explicitly name the **goal**, **input** and **output** at the top. This is the opening move on Task 5.1 — conditions and repetition are added in L14 and L15. | Independent |
| 0:55–1:15 | Pair activity: students swap sequences and try to **break** the partner's process by swapping any two steps the partner thinks might still work. The writer marks each swap as *"order matters"* or *"order doesn't"*. | Pair |
| 1:15–1:25 | Whole-class debrief: collect 2–3 cases where the order really mattered; build an "order matters / order doesn't" two-column board. Connect to the L13 central message. | Whole class |
| 1:25–1:30 | Closing: one-line preview of Lesson 14 — *"Next we name the moment a process splits in two."* | Whole class |

**Independent-work block: 30 minutes (33% of 90 minutes).** Meets the 30–50% rule.

**Cross-references.** L13 does not use any in-class activity from `in-class-tasks.md`. The pair activity is local to this lesson. Activity A (the classification game) starts in L14.

**What you say out loud.** *"A sequence is the easiest of the three building blocks — and the most underrated, because nobody notices it until it breaks. Watch what happens when I swap two steps."* Swap two steps in the tea recipe (pour water before tea bag). Pause. *"The follower did exactly what the new order said — and the tea is wrong. Sequence is the default; the default is where the bugs hide."*

**Materials.** Board and marker; paper and pens; no technology required.

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** no slides. The board carries the three sequences and the swapped version.
- **Lecture (0:10–0:25):** main deck slides **4 → 6**: *Sequence — the default move* · *When order matters* · *Sequence at work — deployment checklist*. Spend the most time on slide 5; the swap is where the lesson lands.
- **Independent work (0:25–0:55):** leave slide **4** on screen as the silent reminder of the goal–input–steps–output structure carried over from Week 1.
- **Pair activity (0:55–1:15):** no slides; the pairs work on paper.
- **Debrief (1:15–1:25):** no slides. Use the board for the "order matters / order doesn't" two-column collection.
- **Closing (1:25–1:30):** no slides.

---

## Lesson 14 — 90-minute plan

**Topic.** Conditions: if-then-else thinking and decision trees.

**Central message for this lesson (one sentence).** A condition is a test that splits the path of a process in two (or more), and naming the test in plain English is enough to make the split visible to a literal follower.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: teacher writes a verbal everyday rule on the board — *"If it rains, take the bus, else walk."* Class draws the tree on paper in 2 minutes. Teacher draws the canonical version on the board afterwards. | Whole-class |
| 0:10–0:30 | Instructor input: define *condition*; walk `if … then …`, `if … then … else …`, and `if … then … else if … then … else …`. Walk one decision tree end-to-end (the umbrella rule). **If the supplementary deck `slides-l14-decision-trees.md` is shipped, run it here in full.** | Lecture |
| 0:30–0:57 | **Independent work** (27 min): each student extends their L13 sequence by adding at least one condition with an `if … then … else …` test named in plain English. They also draw the condition as a small tree. | Independent |
| 0:57–1:20 | **MANDATORY teacher-led in-class activity** — *"Find the if"* (the first half of Activity A in `in-class-tasks.md`, ~23 min). Teacher reads short everyday/IT statements; class votes *condition / no condition* and names the test on each. Close calls get a rewrite on the board. | Whole class |
| 1:20–1:28 | Whole-class debrief: which statements were hardest to classify? Where was the test hidden behind everyday wording? | Whole class |
| 1:28–1:30 | Closing: one-line preview of Lesson 15 — *"Next we name the moment a step happens more than once."* | Whole class |

**Independent-work block: 27 minutes (30% of 90 minutes).** Meets the 30–50% rule at the lower bound. Protect this block — if the lecture runs long, trim the lecture, not the independent work.

**Cross-references.** The 57–80 minute slot is the first half of Activity A in `in-class-tasks.md` (*Find the if*). Stack 1 from that file must be prepared in advance. If you want to run Activity B (*Live decision tree on the board*) instead of part of the lecture, swap it into the 30–55 min slot and shorten the independent-work segment by 5 minutes to compensate (but **do not go below 27 minutes**).

**What you say out loud.** *"A condition is a test that splits the path. If the test is true, the follower goes one way; if not, the other — or, with no else, the follower just carries on. Three things make a good condition: an honest test the follower can actually check, a named action on the true branch, and a named action — or an explicit 'nothing extra' — on the false branch."* Walk the umbrella rule on the board: *"if it is raining now, take an umbrella; else if the forecast says rain, take an umbrella; else leave it home."* Draw the three-branch tree.

**Materials.** Board and marker; paper and pens; Stack 1 from `in-class-tasks.md` prepared as slips or on a printed list. If you ship `slides-l14-decision-trees.md`, have it ready on screen for the lecture segment.

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** slide **7** (*Condition — a test that splits the path*) on screen as the class draws the umbrella tree on paper.
- **Lecture (0:10–0:30):** main deck slides **7 → 10**: *Condition — a test that splits the path* · *`if … then … else …`* · *Decision tree — drawing the split* · *Condition at work — password validation*. **If the supplementary deck is shipped, run `slides-l14-decision-trees.md` end-to-end between main-deck slides 9 and 10** — it walks the umbrella tree slowly and mirrors it onto the IT login example.
- **Independent work (0:30–0:57):** leave slide **8** on screen as the silent reference for the `if … then … else …` shape.
- **In-class activity (0:57–1:20):** no slides. The classification game lives on the board.
- **Debrief (1:20–1:28):** no slides; talk through the close calls from the board rewrites.
- **Closing (1:28–1:30):** no slides.

If you do not ship the supplementary deck `slides-l14-decision-trees.md`, slide **9** of the main deck carries the decision-tree visual alone. Walk it slowly; the rest of the lecture leans on that one slide.

---

## Lesson 15 — 90-minute plan

**Topic.** Repetition: doing the same thing multiple times.

**Central message for this lesson (one sentence).** Repetition is how you say *"the same thing, again, with a clear stop"* — and naming the stop in plain English is what separates a useful repetition from a runaway one.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: class calls out three repetitions they have done so far today (likely: brushing teeth, walking past traffic lights, refreshing a chat for new messages). Teacher writes them on the board. | Whole-class |
| 0:10–0:28 | Instructor input: define *repetition*; show the three shapes (`for each` / `repeat until` / `while`) with one example per shape. Introduce *"the stopping condition is the safety belt"* and the runaway-repetition idea. | Lecture |
| 0:28–0:58 | **Independent work** (30 min): each student adds a repetition to their L13+L14 process and writes an explicit stopping condition. They also write one sentence describing what the runaway case would look like and how a safety stop would fix it. | Independent |
| 0:58–1:20 | **Recommended teacher-led in-class activity** — *"Find the loop"* (the second half of Activity A in `in-class-tasks.md`, ~22 min). Teacher reads short everyday/IT statements; class votes *repetition / no repetition* and names the stopping condition on each. | Whole class |
| 1:20–1:28 | Whole-class debrief: collect three runaway cases ("repeat until you understand", "while the page is still loading", "for each thing on the list"). Discuss what an honest stop would look like for each. | Whole class |
| 1:28–1:30 | Closing: preview Week 6 — *"Next week we tighten these natural-language descriptions into something a little closer to code, on paper. It is called pseudocode."* Mention that AT2 lands at the end of this week / during Week 6. | Whole class |

**Independent-work block: 30 minutes (33% of 90 minutes).** Meets the 30–50% rule.

**Cross-references.** The 58–80 minute slot is the second half of Activity A in `in-class-tasks.md` (*Find the loop*). Stack 2 from that file must be prepared in advance. Activity A is mandatory across the week — if you ran the L14 half, you should run the L15 half too, both for symmetry and because the *while* trick slip in Stack 2 is the diagnostic moment for the *one-off vs. repeated step* misconception.

**What you say out loud.** *"Repetition is the third building block and the most dangerous, because every repetition can run forever if its stop is dishonest. Three shapes: for-each, when you know the list; repeat-until, when the stop depends on something that happens; while, when the test is checked before each repeat. All three need a stop a literal follower can actually observe."* Then write *"repeat until you understand"* on the board: *"How would the follower know when to stop?"* The silence is the lesson. Pivot to *"…or stop after 10 attempts"* as the safety belt.

**Materials.** Board and marker; paper and pens; Stack 2 from `in-class-tasks.md` prepared as slips or on a printed list.

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** no slides. Collect repetitions on the board.
- **Lecture (0:10–0:28):** main deck slides **11 → 14**: *Repetition — doing it again, with a stop* · *Three shapes of repetition* · *Repetition at work — the inbox sweep* · *The stopping condition is the safety belt*. The inbox-sweep slide is the one to dwell on; flag explicitly that the inbox sweep uses all three building blocks at once.
- **Independent work (0:28–0:58):** leave slide **12** on screen as the silent reference for the three shapes (`for each` / `repeat until` / `while`).
- **In-class activity (0:58–1:20):** no slides. The classification game lives on the board.
- **Debrief (1:20–1:28):** no slides; use the board to write the three runaway cases the class collects.
- **Closing (1:28–1:30):** slide **18** (*What comes next: Week 6 — pseudocode*) for the one-line preview, then slide **19** (*Recap — the central message*) so students leave on the verbatim line.

---

## Facilitation tips

### Before any of the three classes

- **Test the central message on yourself first.** Read it aloud once, slowly: *"Almost any process can be described with three building blocks: sequence, condition, and repetition."* It appears verbatim on at least one slide and at least once in `self-study.md`. Mirror it in your own speech at least twice per lesson; it is the spine of the week.
- **Pre-write the board layout.** For L13, sketch the "order matters / order doesn't" two-column grid. For L14, sketch the umbrella decision tree and the password rule. For L15, sketch the inbox-sweep flow showing all three building blocks at once. Drawing this live is fine; thinking about it live is risky.
- **Read `in-class-tasks.md` end-to-end before Lesson 14.** Activity A appears in two halves — Stack 1 in L14, Stack 2 in L15 — and needs the slips (or a printed list) prepared in advance.

### During class

- **Insist on the canonical labels.** *Sequence, condition, repetition.* Synonyms (selection, branch, loop, iteration) are fine in passing, but always pair them with the canonical name the first time.
- **Lead with the everyday example. Always.** The password-validation rule, the inbox sweep and the deployment checklist arrive **after** a tea recipe, an *"if it rains, take the bus"*, and a *"mark each name in the register"*. If a student offers an IT example first, accept it but pair it with an everyday one before moving on.
- **Protect the independent-work block.** Week 5 builds the AT2-feeder artefact across three lessons. If a 90-minute plan slips, the cut comes from the debrief or the lecture, not from the independent-work block. Do not go below 27 minutes per lesson.
- **Don't slip into code.** When a student writes `if (x > 0) {` on their page, gently rewrite on the board as *"if x is greater than 0, then …"* in plain English. Code arrives in Week 7.
- **Name the test, not the answer.** When a student draws a decision tree with a vague branch like *"if it goes wrong"*, push: *"what specific test would a literal follower run to know it went wrong?"*
- **Honest stops.** When a student writes *"repeat until done"*, ask: *"how does the follower know it is done?"* If the answer is *"they just know"*, the stop is not honest yet.
- **Resist the *infinite loop* horror story.** *Runaway repetition* and *no honest stop* are the in-course phrases. *Infinite loop* arrives once code does.

---

## Answers to common student questions

- *"Is `if … then …` the same as `if … then … else …`?"* — No. Without `else`, the follower does nothing extra otherwise. With `else`, the follower does something different on the false branch. Both shapes are valid; they say different things.
- *"Can a condition have more than two branches?"* — Yes, with `else if`. Three or four branches are normal — *"if it rains, take the bus; else if you are late, run; else walk."* More than five usually means the rule is hiding a deeper structure.
- *"Is `for each` a loop or a sequence?"* — A loop. It does the same thing once for every item in a list, and the list is the stopping condition. One statement, not many.
- *"What if my `repeat until` could go on forever?"* — Add a safety stop: *"…or stop after 10 tries"*, *"…or stop after 30 minutes"*. Every honest repetition has at least one observable stop. The safety stop is part of the design, not an apology.
- *"Is this on AT2?"* — Yes. The artefact you build across L13, L14 and L15 is the AT2 artefact at a smaller scale. **AT2 lands at the end of Week 5 / during Week 6.** Keep your notes.
- *"Can I use code in AT2?"* — Not yet. AT2 is natural language with `if … then … else …` and `for each / repeat until / while` as loose, English-style notation. Pseudocode arrives next week. AT2 is graded on the *thinking*, not the syntax.
- *"What is the difference between *while* and *repeat until*?"* — `while X, keep doing …` checks the test **before** each repeat: if X is already false, the follower does the inner step zero times. `repeat … until X` runs the inner step **at least once**, then checks. Read your own loop aloud and ask: *"on the very first time through, does the follower do anything?"*

---

## Formative assessment tips

Week 5 has **no summative assessment** of its own — the summative artefact is AT2, due at the end of Week 5 / during Week 6. The role of formative checks is to make understanding visible early, so students still confusing the three building blocks can be helped before AT2 lands. Use one or two per lesson.

### Per-lesson informal checks

- **Lesson 13 — exit ticket (3 min, end of class).** Each student writes one sentence answering: *"Name the sequence backbone of one process you ran today."* Skim the tickets on the way to L14; if more than a few say *"I don't have one"*, revisit the L13 central message at the start of L14.
- **Lesson 14 — board vote.** Show three short rules on the board (e.g. *"if you have your bus card AND money on it, take the bus"*, *"if the milk smells off, throw it out"*, *"if it rains, take the bus, else walk"*) and ask the class which has the **most branches** in its decision tree. The pattern of hands tells you whether students can see structure under everyday phrasing.
- **Lesson 14 — sticky-note collection at the end of Activity A.** Each student writes one ambiguous condition they have heard or said this week. Read 3 at random; class proposes an honest test for each.
- **Lesson 15 — sticky-note collection.** Each student writes one *runaway repetition* they have heard or said this week ("repeat until you understand", "while the page is still loading"). Read 3 at random; class proposes a safety stop for each.
- **Lesson 15 — one-minute paper at end of week.** *"In one sentence, name the building block you find easiest to spot, and the one you find hardest."* The pattern across the class tells you what to revisit in Week 6's first 5 minutes.

### What you are listening for across the week

The three phrases that mark genuine understanding by the end of Week 5:

- *"Where is the test?"* (when reading a condition).
- *"What is the stop?"* (when reading a repetition).
- *"The sequence is the spine — the condition and the repetition hang off it."*

If those phrases appear in student speech by the end of L15, AT2 can land without remediation. If not, the most useful 5 minutes of Week 6 is a recap of the three building blocks before pseudocode arrives.

The classification game (Activity A in `in-class-tasks.md`) is the central diagnostic of the week. A class that votes confidently on the trick slips is a class ready for AT2.
