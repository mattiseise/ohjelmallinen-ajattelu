# Week 1 — Teacher materials

This document covers all three lessons of Week 1 (L1, L2, L3) in one place. It is built around the same central question the students see: **"How do I speak to a computer so that it understands what I want it to do?"** Week 1 establishes the conceptual foundation for the whole 8-week course. No code, no flowcharts, no pseudocode is introduced this week; the three lessons sit together as a single arc — Lesson 1 names the problem (literal interpretation, ambiguity), Lesson 2 names the artefact that solves it (the algorithm), and Lesson 3 stress-tests the artefact by hunting and removing ambiguity.

Cross-references: the in-class activities used in Lesson 1 and Lesson 3 are described in detail in `in-class-tasks.md` in the same folder. Cross-references appear in the per-lesson plans below.

---

## Week 1 learning objectives (mapped to Bloom)

Week 1 stays inside **Remembering** and **Understanding**, with **light Applying** allowed in Lessons 2 and 3 (writing a short everyday algorithm; rewriting an imprecise instruction). The forbidden verbs for Week 1 objectives are *create, build, design, develop, evaluate, judge, analyze, decompose, abstract, debug*. These return in later weeks.

### Lesson 1 — Humans, computers, and interpreting instructions

- **Remembering:** the student can **define** computational thinking in their own words.
- **Understanding:** the student can **explain** that a computer follows instructions literally.
- **Understanding:** the student can **give** one everyday example and one IT example of "speaking to a computer".
- **Understanding:** the student can **recognize** that ambiguity is a property of the instruction, not of the computer.

### Lesson 2 — Algorithms in everyday life

- **Remembering:** the student can **define** *algorithm* in their own words.
- **Understanding:** the student can **identify** algorithms in everyday situations (recipe, route, morning routine).
- **Understanding:** the student can **describe** the four parts of an algorithm — goal, input, steps, output.
- **Understanding:** the student can **compare** two algorithms for the same goal at a surface level (which is shorter, which is easier to follow).
- **Light Applying:** the student can **write** a 5–10 step everyday algorithm in plain English.

### Lesson 3 — Precise and imprecise instructions

- **Understanding:** the student can **identify** ambiguous words in a short instruction.
- **Understanding:** the student can **explain** why testing reveals defects faster than re-reading.
- **Light Applying:** the student can **rewrite** an imprecise instruction so a literal follower can execute it.
- **Light Applying:** the student can **test** an instruction by acting as the "literal computer".

The course's higher Bloom levels — *Analyzing* (Week 4), *Creating* (final assessed task, Week 8) — are deliberately not in scope this week.

---

## Common misconceptions for Week 1

At least two misconceptions per lesson appear here. Pre-empt the first one on the list (*the computer is stupid*) at the very start of Lesson 1 — it is the most common and most damaging if left.

### Lesson 1 misconceptions

**Misconception:** "The computer is stupid."
**Correction:** The computer is **literal**, not stupid. A literal follower has no opinion about whether an instruction makes sense; it does exactly what the words allow. Insist on the word *literal* from minute one and gently correct *stupid/dumb* whenever it appears in student speech. The whole course rests on this reframing — students who keep "stupid" in their vocabulary will keep assuming the machine should have known what they meant.

**Misconception:** "Computational thinking is just programming."
**Correction:** Computational thinking is the **thinking behind** programming — taking a problem, naming what is fixed and what varies, and expressing the solution as clear steps. Programming is one place where computational thinking is used, not the only one. A recipe, a help-desk script and a fire-drill procedure are all forms of computational thinking. Programming arrives properly in Week 7.

### Lesson 2 misconceptions

**Misconception:** "Algorithms are only for computer scientists."
**Correction:** Every recipe is an algorithm. Every set of bus directions is an algorithm. Every morning routine is an algorithm. The word *algorithm* names something students already do — the lesson is giving them a name for the skill they already have, not teaching a brand-new skill.

**Misconception:** "An algorithm must be long to count."
**Correction:** Three clear steps can be a valid algorithm if they reach the goal without ambiguity. Length is not the criterion; **clarity and reaching the goal** are. Conversely, a 30-step instruction full of vague words is a poor algorithm.

### Lesson 3 misconceptions

**Misconception:** "Imprecise just means short."
**Correction:** A long instruction can still be imprecise. A short instruction can be perfectly precise. Imprecision is about **whether a literal follower has more than one defensible thing to do**, not about how many words there are.

**Misconception:** "If the instruction sounds right when I read it, it is right."
**Correction:** Reading your own instruction back to yourself rarely surfaces ambiguity, because you already know what you meant. **Only testing with a literal follower (a classmate, a sibling, or yourself reading it 24 hours later) reveals the gaps.** This is why Lesson 3's central activity is to act as the literal computer.

**Misconception (bonus, often appears in Lesson 1 or 3):** "If I add 'please' or 'kindly', the computer will be nicer."
**Correction:** A literal follower has no manners channel. *Please* and *kindly* are no more or less informative than the verbs around them; they neither add nor subtract literal meaning. This is also a useful moment to point out that human politeness conventions do not transfer to literal instruction-following.

---

## Lesson 1 — 90-minute plan

**Topic.** What does computational thinking mean? Humans, computers, and interpreting instructions.

**Central message for this lesson (one sentence).** A computer is a literal follower of instructions, so the quality of an instruction — not the cleverness of the machine — decides the outcome.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: 5-minute "Literal robot live" demo (one slip, e.g. *"Get me a chair"*), then introduce the central question on the board. | Teacher demo + whole-class |
| 0:10–0:25 | Instructor input: define computational thinking in own words first, then offer the short course-wide definition. Frame the four classic pillars by name (decomposition, pattern recognition, abstraction, algorithms) and tell students each gets its own future week. | Lecture |
| 0:25–0:55 | **Independent work** (30 min): each student drafts a 6–10 step instruction for a personal task they really do. **No follower yet** — this is the writing stage of Task 1.1. | Independent |
| 0:55–1:15 | Pair activity: students swap drafts and read each other's *literally*. The receiver underlines every step that is open to more than one interpretation. The writer watches and resists explaining. | Pair |
| 1:15–1:25 | Whole-class debrief: build an "Everyday vs. IT" board. Collect 3–4 everyday examples of literal misreading (sibling sandwich, ambiguous directions, autocorrect) and 3–4 IT examples (typo in a search query, file path with a missing slash). | Whole class |
| 1:25–1:30 | Closing reflection prompt on the board, plus a one-line preview of Lesson 2. | Whole class |

**Independent-work block: 30 minutes (33% of 90 minutes).** Meets the 30–50% rule.

**Cross-references.** The opening warm-up uses one slip from Activity A in `in-class-tasks.md`. The full Activity A is reserved for Lesson 3.

**What you say out loud at the warm-up.** "In a moment one of you is going to play a computer for five minutes. The computer does only what the words say — nothing more, nothing less. The audience's job is to spot the moment a word turns out to mean more than one thing." Run the demo. Resist the temptation to debrief at length; one sentence ("notice that the ambiguity was in the instruction, not the volunteer") is enough — the full debrief is in Lesson 3.

**Materials.** Board and marker; one ambiguous instruction on a slip of paper; a printed list of the four pillars by name (handout optional). No technology required for this lesson.

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** no slides. The literal-robot demo is live; a slide on screen would compete with it.
- **Lecture (0:10–0:25):** main deck slides **4 → 7**: *What is computational thinking?* · *A computer takes you literally* · *"Make a sandwich" — what could go wrong?* · *Ambiguity is in the instruction, not the computer*. Walk one slide per ~3–4 min. Pause on slide 7 long enough for the reframe to land.
- **Independent work (0:25–0:55):** no slides on screen. Students need quiet writing time and a clean board.
- **Pair activity (0:55–1:15):** leave slide **7** on screen as the silent reminder that ambiguity sits in the instruction, not in the follower.
- **Debrief (1:15–1:25):** slide **5** is useful if students struggle to generate everyday-vs-IT examples; otherwise build the two-column board fresh.
- **Closing (1:25–1:30):** no slides. End on the board.

The Week 1 main deck is enough for Lesson 1's lecture segment. No supplementary deck is required.

---

## Lesson 2 — 90-minute plan

**Topic.** Algorithms in everyday life: step-by-step instructions without code.

**Central message for this lesson (one sentence).** An algorithm is the everyday name for a clear sequence of literal steps, and writing one is a skill anyone can practice without code.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: ask the class to call out three algorithms from everyday life. Collect them on the board. Likely answers: a recipe, the bus route, brushing teeth. Resist correcting "wrong" answers; everything reasonable counts. | Whole-class |
| 0:10–0:25 | Instructor input: define *algorithm*, name the four parts — **goal, input, steps, output** — and walk one of the board's examples through the four parts live. | Lecture |
| 0:25–1:00 | **Independent work** (35 min): each student writes their own morning algorithm (or, if they prefer, another familiar everyday algorithm) in 7–12 numbered steps. They explicitly name goal, input, steps, output at the top of the page. | Independent |
| 1:00–1:20 | Pair activity: students swap algorithms. The reader **predicts the output** from the steps alone — without asking the writer. Then they compare prediction to intent and talk about which steps were specific enough to give the goal away. (This is Activity B from `in-class-tasks.md` in a shortened form; use the full version if time allows.) | Pair |
| 1:20–1:28 | Whole-class debrief: collect one finding from three pairs. What kind of step was specific enough to make the goal obvious? What kind of step was too vague to help? | Whole class |
| 1:28–1:30 | Two-sentence preview of Lesson 3. | Whole class |

**Independent-work block: 35 minutes (39% of 90 minutes).** Meets the 30–50% rule.

**Cross-references.** The 60–80 minute slot uses Activity B from `in-class-tasks.md` (Algorithm relay).

**What you say out loud at the lecture.** "An algorithm has four parts. The goal is what you want at the end. The input is what you must have before you can start. The steps are what you do, in order. The output is what you have when the steps are finished. If any of these is missing, the algorithm is incomplete." Then walk through one of the board's examples (e.g. making instant noodles): goal — a bowl of hot noodles; input — a kettle, water, a packet, a bowl, a fork; steps — listed; output — a bowl of hot noodles ready to eat. Avoid the temptation to add a fifth part (e.g. preconditions, postconditions). Four is enough for Week 1.

**Materials.** Board and marker. Paper and pens. No technology required.

**Slide cues — main deck `slides.md` + supplementary deck.**

- **Warm-up (0:00–0:10):** no slides. Collect everyday algorithms on the board, live.
- **Lecture (0:10–0:25):** main deck slides **8 → 10**: *Algorithm — a name for what you already do* · *Parts of an algorithm (goal · input · steps · output)* · *Two algorithms, one goal*. Walk slowly on slide 9 — the four parts need to stick.
  - **Supplementary deck available:** `slides-l2-algorithm-walkthrough.md` (6 short slides) takes the four parts and walks them through one concrete example (making instant noodles). **Run this immediately after slide 9 if your class needs the four parts shown on a real, complete example before they start writing their own.** Skip it if the live walk on the board is enough.
- **Independent work (0:25–1:00):** leave slide **9** on screen as the silent template (goal · input · steps · output). Otherwise no slides.
- **Pair activity (1:00–1:20):** no slides; pairs work on paper.
- **Debrief (1:20–1:28):** no slides. Stay on the board.
- **Closing (1:28–1:30):** no slides.

---

## Lesson 3 — 90-minute plan

**Topic.** Precise and imprecise instructions: testing and improving instructions.

**Central message for this lesson (one sentence).** Instructions are not finished when they sound right; they are finished when a literal follower can execute them without asking questions.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: two short ambiguous instructions on the board (e.g. *"Save the file in the usual place"* and *"Reply to him about it"*). Class names what is ambiguous and proposes a rewrite. Light pace. | Whole-class |
| 0:10–0:25 | Instructor input: define *precise* and *imprecise* in plain English. Walk through the four common ambiguity patterns — vague nouns ("the file"), deictic words ("here", "there", "him"), relative time ("later", "soon"), vague quantity ("a bit", "some"). One example per pattern. | Lecture |
| 0:25–0:55 | **Independent work** (30 min): each student takes their morning algorithm from Lesson 2 and rewrites it to remove ambiguity. They circle each word they changed and write a one-line reason next to it. | Independent |
| 0:55–1:20 | In-class teacher-led activity: **Activity A — "Literal robot live"** from `in-class-tasks.md`. Volunteer plays the literal computer for three prepared slips; class debriefs each one; rewrites go on the board; students each contribute one ambiguous sticky-note instruction for the closing minute. | Whole class |
| 1:20–1:28 | Whole-class debrief: which of the four ambiguity patterns showed up most during the live exercise? Briefly link back to the L1 idea that ambiguity is in the instruction, not the follower. | Whole class |
| 1:28–1:30 | Preview Week 2 — decomposition — in one line: *"Next week we deal with problems too big for a single algorithm."* | Whole class |

**Independent-work block: 30 minutes (33% of 90 minutes).** Meets the 30–50% rule.

**Cross-references.** The 55–80 minute slot is the full version of Activity A from `in-class-tasks.md`. Read that file before this lesson — it lists the exact slips of paper to prepare and the exact debrief moves.

**What you say out loud at the lecture.** "There are four kinds of words that almost always cause ambiguity. The first is a vague noun — 'the file', 'the button', 'the place'. Which file? The second is a word that points at something the reader cannot see — 'here', 'there', 'this one', 'him'. Pointing without a finger does not work in writing. The third is relative time — 'later', 'soon', 'after lunch'. Soon when? The fourth is vague quantity — 'a bit', 'some', 'enough'. These four are not the only sources of ambiguity, but they catch most of what you will see in practice." Write the four patterns on the board and keep them visible for the rest of the lesson.

**Materials.** Three prepared ambiguous-instruction slips for Activity A. Board and marker. Sticky notes (one pad per row). Paper and pens.

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** no slides; ambiguous instructions go on the board so the class can crowdsource the rewrites.
- **Lecture (0:10–0:25):** main deck slides **11 → 14**: *Precise vs. imprecise instructions* · *Hunting ambiguity — four patterns* · *Testing as a literal robot* · *Edge cases (gentle intro)*. Slide 12 carries the four patterns; copy them onto the board as well so they stay visible after you advance the deck.
- **Independent work (0:25–0:55):** leave slide **12** on screen as the on-screen reference while students hunt ambiguity in their own Lesson 2 algorithm.
- **In-class activity (0:55–1:20):** no slides. The literal-robot demo lives in the room, not on the wall.
- **Debrief (1:20–1:28):** no slides; talk through the four patterns against the live evidence on the board.
- **Closing (1:28–1:30):** slide **18** *(What comes next: Week 2 — decomposition)* as the one-line preview, then slide **19** *(Recap — the central question)* to send students out the door on the right line.

The Week 1 main deck is enough for Lesson 3's lecture segment. No supplementary deck is required.

---

## Facilitation tips

### Before any of the three classes

- **Test the central question on yourself first.** Read it aloud once, slowly. If you cannot say it from memory by the time you walk into class, students will not absorb it either. The verbatim form — *"How do I speak to a computer so that it understands what I want it to do?"* — appears on the slide deck twice; mirror that in your speech.
- **Pre-write the board layout.** For Lesson 1, sketch the "Everyday vs. IT" two-column grid in your notes. For Lesson 2, sketch the four parts of an algorithm. For Lesson 3, sketch the four ambiguity patterns. Drawing this on the board live is fine; thinking about it live is risky.
- **Read `in-class-tasks.md` end-to-end before Lesson 1.** Activity A appears twice during the week and needs slips of paper prepared. If you are co-teaching, hand off Activity A explicitly — it works better when one person owns it.

### During class

- **Lead with the everyday example. Always.** The brief is firm: the everyday example before the IT example. If a student offers an IT example first, accept it but pair it with an everyday one before moving on.
- **Insist on the word *literal*.** Every time a student says *the computer is stupid*, gently swap the word: "Literal — the computer is literal. Stupid is when you should have known better. The computer never had a chance to know." Two or three corrections in Lesson 1 are usually enough for the rest of the week.
- **Hold silence after handing the slip to the volunteer.** New teachers tend to narrate the volunteer's actions. Do not. The silence is the lesson.
- **Use the board for rewrites, not the slides.** Slides set up the question; rewrites must happen on the board so the class sees the live transition from ambiguous to precise.
- **Watch the clock for the 30–50% rule.** Independent work is the part teachers under-pressure cut first. Protect it. The schedules above leave 30–35 minutes per lesson; do not trim below 27.

---

## Answers to common student questions

- *"Is Google an algorithm?"* — Yes, Google search is implemented by algorithms (many of them, including modern machine-learning ones). For Week 1, the answer the student needs is: *yes, an algorithm in the everyday sense — a sequence of steps that takes an input (your query) and produces an output (a list of results)*. Deeper detail belongs in later weeks.
- *"Why doesn't autocorrect understand me?"* — Because autocorrect is also literal in its own way: it follows rules about which letter sequences look like which words, and it has no idea what you meant. Use this as a bridge to "ambiguity is in the instruction, not the computer".
- *"Is this on the assessed task?"* — Week 1 has no assessed task. AT1 lands at the end of Week 2. The notes students make this week are the raw material for AT1; that is the honest answer.
- *"Do I need a computer to do this homework?"* — No. Tasks 1.1 and 1.4 can be done with paper, a pen and a willing follower. Tasks 1.2 and 1.3 only need paper. The only "computer" Week 1 needs is the literal one inside the classroom.
- *"Can I use ChatGPT?"* — Yes, in the way Task 1.2 describes — as a sparring partner that pokes at your thinking. You may not paste its output and submit it. Task 1.1 in particular cannot be faked by an LLM, because it requires a real follower and an observable artefact.

---

## Formative assessment tips

Week 1 has **no summative assessment**. The role of formative checks is to make student understanding visible early, so misconceptions can be corrected before Week 2's decomposition layer is added on top. Use one or two of the following per lesson; do not try to use all of them.

### Per-lesson informal checks

- **Lesson 1 — exit ticket (3 min, end of class).** Each student writes one sentence answering: *"In your own words, what does it mean that a computer is literal?"* Collect the tickets, skim them on the way to Lesson 2, and start Lesson 2 by reading two anonymous strong answers aloud. Wrong answers are not corrected publicly; instead, the misconception list above tells you what to revisit in Lesson 2's warm-up.
- **Lesson 1 — board vote.** Show three statements: (a) *"The computer is stupid."* (b) *"The computer is literal."* (c) *"It depends."* Have each student raise a hand for one. The pattern of hands tells you whether the central reframing landed; a strong (a) or (c) vote means revisit before moving on.
- **Lesson 2 — pair report-back (2 min, after the pair activity).** Ask two pairs to name one part of their partner's algorithm that was clear and one that was vague. Listen for whether students are using the words *goal, input, steps, output* — that is the success signal.
- **Lesson 2 — one-minute paper.** End of class: *"Write down one algorithm you used today that you didn't think of as an algorithm before this lesson."* Read three at the start of Lesson 3 as a warm-up.
- **Lesson 3 — sticky-note collection.** Activity A already ends with sticky notes; keep them. The pattern of ambiguous instructions students write is itself an assessment of how well they recognise ambiguity in their own language.
- **Lesson 3 — exit ticket.** *"Name the ambiguity pattern you find easiest to spot, and the one you find hardest."* Use answers to choose Week 2's warm-up examples.

### What you are listening for across the week

The two phrases that mark genuine understanding by the end of Week 1 are:

- *"The instruction is ambiguous"* (rather than *the computer is wrong*).
- *"Let me test it with a literal follower"* (rather than *let me re-read it*).

If those two phrases appear in student speech by Lesson 3, Week 1 has done its job and Week 2 (decomposition) can build on it without remediation.
