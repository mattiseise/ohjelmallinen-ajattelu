# Week 4 — Teacher materials

This document covers Lessons 10, 11 and 12 — the **comparing solutions** week. L10 demonstrates that one problem can be solved more than one valid way. L11 names the four working criteria: **clarity · efficiency · repeatability · error-proneness**. L12 puts them to work in a structured peer-review-and-revision protocol on artefacts students made in Weeks 2 and 3.

The literal-follower mindset from Week 1, the decomposition vocabulary from Week 2 and the flowchart vocabulary from Week 3 are still in force. Week 4 introduces **no new computational-thinking primitive**. Its raw material is artefacts students already have. If a student arrives without one, use the standby artefact pair printed in `student-tasks.md`.

Week 4 produces **no AT submission**. Every task this week feeds **AT2 — process description**, submitted at the end of Week 5 / during Week 6. AT2 explicitly asks for a self-revision step after feedback. That habit is exactly what L12 trains. The peer-review-and-revision loop is also reused in AT3 (Week 8).

Cross-references: the in-class activities used in Lessons 10 and 12 are described in `in-class-tasks.md`. **Activity A — Peer review with the four criteria** (mandatory) sits in the 22–52 min slot of Lesson 12; **Activity B — Variation hunt** (optional) sits in the 55–75 min slot of Lesson 10.

---

## Week 4 learning objectives (mapped to Bloom)

Week 4 stays inside **Understanding**, with **light Analyzing** in three specific places — L10(d), L11(d) and L12(b) — where students *compare two solutions criterion-by-criterion* or *identify weaknesses by criterion*. Forbidden verbs in Week 4 objectives: *evaluate, judge, grade, score, rank, rate, decide which is best, create, build, design, develop, debug*. The verb *compare* is light Analyzing only when criterion-named.

### Lesson 10 — Same problem, multiple solutions

- **Understanding:** the student can **recognize** that the same problem can have more than one correct solution.
- **Understanding:** the student can **describe** in plain English how two valid solutions can differ in their steps, in their order, or in what they leave to the user.
- **Understanding:** the student can **give** one everyday example and one IT example of two valid solutions.
- **Light Analyzing:** the student can **identify** at least two ways in which two given solutions differ from each other.

### Lesson 11 — Criteria for evaluating solutions

- **Understanding:** the student can **define** the four working criteria in their own words: clarity, efficiency, repeatability, error-proneness.
- **Understanding:** the student can **explain** that a criterion turns *"I like this one better"* into *"this one is better at X"*.
- **Understanding:** the student can **apply** the four criteria to a small worked example.
- **Light Analyzing:** the student can **compare** two solutions criterion-by-criterion and **identify** which is stronger on which criterion.
- **Understanding:** the student can **recognize** that a single solution does not have to win on every criterion — criteria can pull in different directions.

### Lesson 12 — Improving one's own solution and using peer feedback

- **Understanding:** the student can **apply** the four-criteria rubric in a structured peer-review protocol on a partner's existing artefact.
- **Light Analyzing:** the student can **identify** at least two concrete weaknesses in a partner's solution, named by criterion.
- **Understanding:** the student can **rewrite** one of their own existing Week 2 or Week 3 solutions to address two specific pieces of peer feedback. (Revision, not new creation.)
- **Understanding:** the student can **describe** in 3–5 sentences what changed and why, citing the criterion that drove each change.

---

## Common misconceptions for Week 4

At least two per lesson, each with a `Correction:` line. The L11 one (*efficient = fast*) and the L12 one (*feedback is criticism*) are the most common; pre-empt both in the first ten minutes of their lessons.

### Lesson 10 misconceptions

**Misconception:** *"If there is more than one valid solution, then it doesn't matter which I pick."*
**Correction:** It matters once you have a stated criterion. Without one, *"doesn't matter"* is honest. With one — say, *clarity for a first-time follower* — you can defend the choice. This week is exactly the move from *no criterion → criterion*.

**Misconception:** *"If my solution is different from the teacher's, mine must be wrong."*
**Correction:** As long as the solution reaches the goal and is clearly written, it is **valid**. The teacher's solution is one option among several. Collect 2–3 student variations of *"make a cup of tea"* on the board in the L10 warm-up to show this.

### Lesson 11 misconceptions

**Misconception:** *"Efficient = fast."*
**Correction:** In this course, *efficient* means **no wasted steps**. A fast but error-prone solution can still be inefficient overall, because the rework eats the time the speed saved. The everyday picture is *"the long way round is sometimes faster because you don't have to redo it"*.

**Misconception:** *"A good solution wins on every criterion."*
**Correction:** Real solutions **trade off**. The four criteria can pull in different directions. *"Recipe A wins on clarity, Recipe B may win on efficiency, the right choice depends on the follower"* is a complete L11 answer.

**Bonus misconception (often appears late in L11):** *"These four are the only criteria that exist."*
**Correction:** Many criteria exist in the wider world — cost, accessibility, security. For this course we work with four because they are enough to train the habit.

### Lesson 12 misconceptions

**Misconception:** *"Feedback is criticism."*
**Correction:** Feedback that **names a criterion** is information; without a criterion it is taste. The protocol forces the criterion. *"I just didn't like step 3"* is not feedback; *"step 3 is unclear because the word **file** does not say which file"* is.

**Misconception:** *"I have to act on every piece of feedback."*
**Correction:** You have to **consider** every piece and be able to say **which criterion it speaks to**. You may reasonably reject feedback if the criterion does not apply here — that is itself a criterion-named answer.

---

## Lesson 10 — 90-minute plan

**Topic.** Same problem, multiple solutions.

**Central message for this lesson.** A problem is not the same as its solution; one problem can be solved many ways, and noticing that is the start of choosing well.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: write *"make a cup of tea"* on the board. Collect 2–3 student variations. Underline what is the same and what is different. Read the Week 4 central message aloud and write it at the top of the board. | Whole-class |
| 0:10–0:25 | Instructor input: state the central message; draw *problem vs. solution* in two columns; present Recipe A and Recipe B side by side; present the two backup methods as the IT mirror. Everyday before IT. | Lecture |
| 0:25–0:55 | **INDEPENDENT WORK (30 min):** each student picks one familiar everyday task and writes **two valid alternative algorithms** for it (5–8 steps each). No criteria yet — just notice the variety. Hands and pens, no devices. | Independent |
| 0:55–1:15 | In-class pair activity: **Activity B — "Variation hunt"** from `in-class-tasks.md`. Pairs swap two-algorithm pairs and identify **at least two ways** the partner's two solutions differ. Roles swap. | Pair |
| 1:15–1:28 | Whole-class debrief: collect 4–5 *kinds of difference* on the board (step order; what is left implicit; where the user has to choose; how the solution handles things going wrong). This is the **seed of the L11 criteria**. Do **not** name them yet. | Whole class |
| 1:28–1:30 | One-line preview of Lesson 11: *"Tomorrow we give those differences names."* | Whole class |

**Independent-work block: 30 minutes (33% of 90).** Meets the 30–50% rule.

**What you say out loud at the lecture.** "Same goal — a drinkable cup of tea — two recipes, both work. They differ in **order** (boil first vs. bag first) and in what is **left to the user** (count three minutes vs. judge the colour). Neither is wrong. One problem can have many valid solutions. **Validity** in this course means: reaches the goal, can be carried out by a literal follower. Nothing about *better*. *Better* is next lesson's word."

**Materials.** Board and marker; the two tea recipes and the two backup methods written or projected before class; paper for the independent block. No supplementary deck used in L10.

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** slide **1** *(title)* on screen as students arrive; switch to slide **2** *(The central message)* for the verbatim opener. Then board for the tea-recipe variations.
- **Lecture (0:10–0:25):** slides **3 → 6**: *Where Week 4 sits · A problem is not the same as its solution · Two ways to make tea · Two ways to back up a project folder*. Linger on slide 4 — the L10 hinge.
- **Independent work (0:25–0:55):** leave slide **4** on screen as the silent framing reminder.
- **Activity B — Variation hunt (0:55–1:15):** no slides; the conversation happens between pairs.
- **Debrief (1:15–1:28):** slide **7** *(What is the same, what is different?)* as the collection template; write the class's *kinds of difference* on the board next to it.
- **Closing (1:28–1:30):** no slides; one spoken line previewing L11.

---

## Lesson 11 — 90-minute plan

**Topic.** Criteria for evaluating solutions — clarity, efficiency, repeatability, error-proneness.

**Central message for this lesson.** A criterion is a stated yardstick — name it, and *better* stops being a feeling and starts being a comparison.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: recap *two valid solutions* with one student-supplied pair from L10. Ask: *"What was the most useful kind of difference we found yesterday?"* Collect one answer on the board. | Whole-class |
| 0:10–0:35 | Instructor input — the longest lecture block of the week. State the *taste → criterion* move. Introduce the four criteria in fixed order with a 2–4 sentence definition each and a one-line everyday + one-line IT example. Project the **supplementary deck `slides-l11-criteria-walkthrough.md`** for the worked example on the two tea recipes. Return to the main deck for the backup-methods example. Break the 25-minute block with one student-voiced example halfway through. | Lecture |
| 0:35–1:05 | **INDEPENDENT WORK (30 min):** each student takes their own two L10 alternative algorithms and applies all four criteria in a 4-row table. **Not asked to pick a winner.** One short sentence per cell. Hands and pens. | Independent |
| 1:05–1:22 | Pair activity: students swap criterion tables and check — *Did the partner name the criterion in every row? Did they cite a specific step?* Each pair writes back one or two improvement suggestions. | Pair |
| 1:22–1:28 | Whole-class debrief: collect 3–4 places where criteria **pulled in different directions** (trade-offs). Write each as *"Solution X wins on clarity; solution Y wins on efficiency."* Resist crowning a winner. | Whole class |
| 1:28–1:30 | One-line preview of Lesson 12: *"Tomorrow we use these four criteria on each other's real artefacts from Weeks 2 and 3."* | Whole class |

**Independent-work block: 30 minutes (33% of 90).** Meets the 30–50% rule.

**What you say out loud at the lecture.** "Yesterday we found differences. Today we give them names. **Four** names — clarity, efficiency, repeatability, error-proneness — in that order. **Clarity:** a literal follower can read it once and know what to do. **Efficiency:** the goal is reached without wasted steps. *Efficient is not the same as fast — a fast but error-prone solution wastes more time on rework than it saved.* **Repeatability:** same input, same result, every time. *'A bit of water'* breaks repeatability. **Error-proneness:** it is hard to do the wrong thing while following it." Then walk Recipe A vs. Recipe B with each criterion in turn. End with the trade-off sentence: *"Recipe A wins on clarity, Recipe B may win on efficiency — the right choice depends on whether the follower has done this before."*

**Materials.** Board and marker; the two tea recipes and the two backup methods from L10 still visible; paper and ruler for the criterion tables. The supplementary deck `slides-l11-criteria-walkthrough.md` is projected for the worked example.

**Slide cues — main deck `slides.md` + supplementary deck `slides-l11-criteria-walkthrough.md`.**

- **Warm-up (0:00–0:10):** main deck slide **7** *(What is the same, what is different?)* as the L10 carry-over. Then board for the student-supplied example.
- **Lecture (0:10–0:35):** main deck slides **8 → 9** *(From taste to criterion · The four criteria)* for the opening framing. From slide 9 forward, switch to **the supplementary deck `slides-l11-criteria-walkthrough.md` (slides 1 → 6)** for the worked example on Recipe A vs. Recipe B. Then back to main deck slides **10 → 12** *(Clarity in two tea recipes · Efficiency in two backup methods · Repeatability and error-proneness)* for the IT mirror. Finish on main deck slide **13** *(Trade-offs)*.
- **Independent work (0:35–1:05):** leave main deck slide **9** *(The four criteria)* on screen as the silent reminder of the four names and the fixed order.
- **Pair activity (1:05–1:22):** no slides; conversations on the criterion tables.
- **Debrief (1:22–1:28):** slide **13** *(Trade-offs)* as the collection template; trade-off sentences go on the board.
- **Closing (1:28–1:30):** no slides; one spoken line previewing L12.

---

## Lesson 12 — 90-minute plan

**Topic.** Improving one's own solution using peer feedback. The mandatory in-class activity (the peer-review protocol) lives in this lesson.

**Central message for this lesson.** Feedback that names a criterion is feedback you can act on; feedback that does not is taste in disguise.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: write the three-step protocol on the board in big letters — **criteria → feedback → revision**. Remind students to take out their Week 2 decomposition or Week 3 flowchart. For students who forgot, hand out the standby artefact pair from `student-tasks.md`. | Whole-class |
| 0:10–0:22 | Instructor input: brief walkthroughs of *Giving feedback someone can actually use* (name the criterion; one concrete spot; critique the artefact, not the person) and *Receiving feedback you do not agree with* (consider every piece; you may reject one if the criterion does not apply). Twelve minutes. Resist longer. | Lecture |
| 0:22–0:52 | In-class teacher-led activity: **MANDATORY Activity A — "Peer review with the four criteria"** from `in-class-tasks.md`. Silent read → criterion pass → pick two → exchange with no-defending Q&A. The teacher rotates and polices *taste → criterion* in real time. Isolated students pair with the teacher. | Pair |
| 0:52–1:22 | **INDEPENDENT WORK (30 min):** each student revises their own Week 2 / Week 3 artefact in response to **one** of the two pieces of partner feedback, and writes the 3–5 sentence change note. A five-word change can be exactly the point. Hands and pens. | Independent |
| 1:22–1:28 | Whole-class debrief: three volunteers share what changed and which criterion drove it. Listen for the criterion name — *"clarity at step 3"*, *"error-proneness on the diamond"*. Bridge to AT2. | Whole class |
| 1:28–1:30 | One-line preview of Week 5 (*if / then / else*) and the AT2 reminder: *"AT2 lands at the end of Week 5 / during Week 6, and it asks for exactly this loop on your own work."* | Whole class |

**Independent-work block: 30 minutes (33% of 90).** Meets the 30–50% rule.

**What you say out loud at the lecture.** "Your own work is the hardest to read clearly — you remember what you **meant**, so you cannot see what you **wrote**. The four criteria are a way to read it **with someone else's eyes**. Today the eyes are real: your partner's. Three steps. Read silently first — no narrating. Write one sentence per criterion in the fixed order. Pick the two most useful. Hand them over. **Clarifying questions only, no defending.** Then you have something to act on. You will revise one thing — not everything — and write three to five sentences naming what changed and why. *Why* names a criterion. That is the loop AT2 will ask you to run on your own work in two weeks' time."

**Materials.** Board and marker; the three-step protocol pre-written on the board before students arrive; **standby artefact pair printed and on the teacher's desk** (at least 4 copies); paper for the criterion sentences and the change note. No supplementary deck used in L12.

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** slide **14** *(The peer-review protocol)* as the silent reminder; the board carries the in-room version in big letters.
- **Lecture (0:10–0:22):** slide **15** *(Feedback someone can use)* for the three rules; stay on slide 15 throughout the twelve minutes.
- **Activity A — Peer review with the four criteria (0:22–0:52):** leave slide **14** on screen as the silent protocol reminder. No other slides — the pair conversation is the lesson.
- **Independent work (0:52–1:22):** leave slide **14** on as background; the board carries the in-room reminder.
- **Debrief (1:22–1:28):** slide **16** *(Tasks this week)* as the framing — volunteers' change notes show the must-do-minimum task in flight.
- **Closing (1:28–1:30):** slide **17** *(What comes next: Week 5)* for the one-line preview and the AT2 reminder, then close on slide **18** *(Recap — the central message)*.

---

## Facilitation tips

- **Police the *taste → criterion* move.** Every *"I just like this one"* gets gently bounced back to *"which criterion?"*. Every *"the right answer is…"* gets *"…on which criterion?"*. The single most important facilitation move of the week.
- **Resist crowning a winner.** Both tea recipes work. Both backup methods work. The point is *how they differ*. If a student insists *"but A is just better"*, ask *"better on which criterion, and for which follower?"*.
- **No numeric scoring. Ever.** *"4/5 on clarity"* is not allowed. *"Clearer at step 5"* is. The criteria are **descriptive lenses**, not a rubric to grade with. If students reach for numbers, swap to words.
- **In L11, the lecture block is unusually long (25 min).** Break it with one student-voiced example halfway through — ask a student to read their L10 *two valid solutions* and walk the class through how *clarity* applies to step 3 of each.
- **In L12, pairs stuck on *"I have no feedback"* should be prompted with the criterion list.** *"Go through clarity, efficiency, repeatability, error-proneness in order. One sentence per criterion."*
- **Pair-work failure mode.** Pair an isolated student with **the teacher**, not with another isolated student. If pair-work is fundamentally impossible that day, swap in Task 4.2 from the plan (*"Two tea recipes, four criteria"*) as the must-do-minimum substitute.
- **Standby artefact pair on the desk before L12.** At least 4 copies. Hand one to any student empty-handed at 0:00–0:10, not at 0:22.
- **Mid-course pulse check — surface but do not derail.** L12 is a natural moment for *"what from Weeks 1–3 still feels shaky?"*. Note it on a sticky note; **do not** open it up in L12. Week 4 must end on the peer-review-and-revision habit, not on a Week 1–3 review.

---

## Answers to common student questions

- *"What if my two solutions are basically the same?"* — Then they are not really two solutions. Push for differences in step order, in what is left implicit, or in who has to choose. The two need to differ in **something a literal follower would notice**.

- *"Which criterion is the most important?"* — None in the abstract. The most important criterion depends on the **situation**. For a brand-new IT trainee, clarity is usually deciding. For a help-desk macro firing a thousand times a day, efficiency may be. **Naming the trade-off is the answer**, not picking a champion.

- *"Is there a right answer to the comparison?"* — There is a right answer **once you name a criterion**. *"Which is clearer at step 3?"* has a right answer. *"Which is the better recipe?"* without a criterion does not — it is taste.

- *"What if my partner's feedback is wrong?"* — Say which criterion it speaks to, and say **why you don't think it applies here**. That is the answer. *"Acting on every piece of feedback"* is not the goal; *"considering every piece and naming the criterion you weighed it against"* is.

- *"Do I need a computer for any of this?"* — No. Week 4 is paper, board and conversation. The artefacts you bring are the ones you drew in Weeks 2 and 3. Devices are not needed.

- *"Can I use ChatGPT for the comparison?"* — Only as a sparring partner in the DEEPENING tasks. The MANDATORY work is **your own artefact** and **a real partner's feedback**. An LLM cannot run the back-and-forth with a real partner.

- *"What if I missed Week 2 or Week 3?"* — Use the standby artefact pair at the end of `student-tasks.md`. Pick one; tell your partner you are using a standby. The standbys are deliberately rough — a reviewer can find criterion-named weaknesses in under five minutes.

---

## Formative assessment tips

Week 4 has **no summative moment**. The checks below are formative — they make understanding visible so misconceptions can be corrected before AT2 starts in Week 5. Use one or two per lesson; do not use all.

### Per-lesson informal checks

- **L10 exit ticket (2 min).** *"Two valid solutions to the same problem can differ in [X] and [Y]."* If more than a third write only *"order"*, recap *"what is left to the user"* and *"how it handles things going wrong"* at the start of L11.
- **L10/L11 board vote.** Three statements: (a) *"If two solutions reach the goal, only one is right."* (b) *"If two solutions reach the goal, both are valid."* (c) *"The shorter one is better."* A strong (a) or (c) vote means the validity-vs-criterion move has not landed.
- **L11 name-the-four (2 min).** Each student writes the four criterion names from memory, in order. If more than a third miss one (usually error-proneness or repeatability), recap at the start of L12 — same fixed order.
- **L11 one-minute paper.** *"Describe one trade-off you found today."* Listen for the criterion names in their writing.
- **L12 pair report-back.** Two pairs report one piece of feedback they gave. Listen for the criterion name and the specific step. If the criterion is missing, ask *"on which criterion?"* in front of the class — model the move out loud.
- **L12 exit ticket.** *"Which criterion drove your revision today, and what did you change?"* Vague answers (*"I made it clearer"*) flag the same gap as a missed *clarity at step X*.

### Mid-course pulse-check (optional, fits L12 closing only if time allows)

Sticky-note collection at the very end of L12. Each student writes one of *"One thing from Weeks 1–3 that still feels shaky"* or *"One thing I now feel solid on"*. Read three of each aloud. Note shaky ones for Week 5/6 revision — **do not** open them up in L12.

### What you are listening for across the week

Three phrases that mark genuine understanding by the end of Week 4:

- *"Both solutions reach the goal — they differ in …"* (rather than *"this one is right"*).
- *"Solution A wins on clarity; solution B wins on efficiency — it depends on the follower."* (rather than *"A is better"*).
- *"I changed step 3 because of clarity — my partner pointed out that …"* (rather than *"I made it better"*).

If those three phrases appear in student speech by the end of Lesson 12, Week 4 has done its job and Week 5 can build on a class that knows how to read its own work and revise it.
