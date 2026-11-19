# Week 2 — Teacher materials

This document covers Lessons 4, 5 and 6 — the **decomposition** week. The three lessons sit together as one arc: Lesson 4 names the move and the vocabulary (main task, subtask, sub-goal); Lesson 5 sharpens the move with order and dependencies; Lesson 6 stress-tests the move on a realistic IT task and ends with **AT1**, the first assessed task of the course.

The literal-follower mindset from Week 1 is still in force, every single subtask. Decomposition does not retire it; it stacks on top. Bridging back to Week 1 whenever a subtask comes out vague ("could a literal follower carry that out?") is one of this week's most useful facilitation moves.

Cross-references: the in-class activities used in Lesson 5 (and optionally L4 and L6) are described in detail in `in-class-tasks.md` in the same folder.

---

## Week 2 learning objectives (mapped to Bloom)

Week 2 stays inside **Remembering** and **Understanding**, with **Applying** allowed where students decompose real tasks (the verb *decompose* is the new applying verb that arrives this week). The forbidden verbs for Week 2 objectives are *evaluate, judge, critique, design (a system), build, develop, debug, abstract, analyze*. These return in later weeks (*abstract* is reserved for Week 3; *evaluate/analyze* arrive in Week 4).

### Lesson 4 — Decomposing a problem (main task, subtasks, goal)

- **Remembering:** the student can **define** *decomposition*, *main task*, *subtask*, *sub-goal* in their own words.
- **Understanding:** the student can **explain** why a big task is easier to write up as several small algorithms than as one long one.
- **Understanding:** the student can **recognize** subtasks inside a familiar everyday task.
- **Understanding:** the student can **identify** the goal of a main task and the goal of each of its subtasks.
- **Applying:** the student can **decompose** one everyday task into a main task plus 3–6 subtasks with sub-goals.

### Lesson 5 — Order of steps and dependencies

- **Remembering:** the student can **define** *dependency*, *order*, *parallel* (informally).
- **Understanding:** the student can **explain** that a subtask depends on another because its input is the other subtask's output.
- **Understanding:** the student can **identify** dependencies inside a familiar decomposition.
- **Understanding:** the student can **recognize** when two subtasks have no dependency on each other.
- **Applying:** the student can **reorder** an out-of-order list of subtasks into a valid order.

### Lesson 6 — Decomposing an IT-related task (AT1)

- **Understanding:** the student can **identify** the main task and its goal in a realistic IT-related scenario.
- **Applying:** the student can **decompose** the IT-related main task into 4–8 subtasks with sub-goals.
- **Applying:** the student can **order** those subtasks and mark at least one dependency.
- **Understanding:** the student can **explain** the decomposition in one short paragraph.
- **Applying:** the student **submits AT1** — a short artefact with main task, goal, 4–8 subtasks with sub-goals, an order, and at least one dependency called out.

---

## Common misconceptions for Week 2

At least two misconceptions per lesson appear here, each with a `Correction:` line. Pre-empt the L4 one (*"decomposition is just making a long list"*) in the first ten minutes of Lesson 4 — it is the most common and the most damaging if left.

### Lesson 4 misconceptions

**Misconception:** "Decomposition is just making a long list."
**Correction:** A decomposition has a **shape**, not just a length. One main task at the top, a handful of subtasks underneath, each with its own sub-goal. A flat list of 30 steps is not a decomposition; it is a long instruction. The shape is what makes the subtasks small enough to write a clean algorithm for one at a time.

**Misconception:** "There is one right decomposition for any task."
**Correction:** More than one valid decomposition can exist for the same task. The right decomposition depends on the shape of the work in front of you — which tools, which colleagues, which constraints. Week 4 returns to "how to compare two valid solutions". For Week 2 the message is gentler: name *a* defensible decomposition, not *the* decomposition.

### Lesson 5 misconceptions

**Misconception:** "Every subtask has to come right after the previous subtask."
**Correction:** Dependencies pin some subtasks into a fixed order; others are free. If the second subtask does not need the output of the first, the order between them is free. A linear list with no free pairs is usually a flat checklist in disguise.

**Misconception:** "If two subtasks can be done in any order, the order doesn't matter at all."
**Correction:** It matters less, but a sensible default order still helps the literal follower. *"Pick either"* is not a useful instruction; *"either of these can be done first; here is the order we will use today"* is.

### Lesson 6 misconceptions

**Misconception:** "Decomposing an IT task is just listing the buttons to click."
**Correction:** The decomposition names the main task, the goal, and subtasks with their own sub-goals. The buttons live *inside* the subtasks (a subtask is then a clean little algorithm of the Week 1 kind), not in the decomposition itself. If your decomposition is a list of clicks, you have stopped at the wrong layer.

**Misconception:** "AT1 wants a perfect decomposition."
**Correction:** AT1 wants a **defensible** decomposition — a stated goal, named subtasks with sub-goals, an order, and at least one dependency called out. There is no single perfect answer to find.

### Bonus misconception (often appears in L4 or L6)

**Misconception:** "If I decompose hard enough, I won't have to write any actual steps."
**Correction:** Decomposition is a planning move. The steps still have to exist underneath each subtask, just at a manageable size. A literal follower will eventually need them.

---

## Lesson 4 — 90-minute plan

**Topic.** Decomposing a problem: main task, subtasks, and goal.

**Central message for this lesson (one sentence).** A task is easier to think about, write down, and hand to a literal follower once you split it into a main task with a clear goal and a handful of subtasks that each have their own clear goal.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: ask students to call out three of their own everyday tasks that "feel too big for one list of steps". Collect on the board. Likely answers: organising a class trip, moving flat, planning a long weekend. | Whole-class |
| 0:10–0:25 | Instructor input: define *decomposition*, *main task*, *subtask*, *sub-goal*. Walk one of the board's examples through main task + goal + 4–6 subtasks with sub-goals, live. | Lecture |
| 0:25–0:55 | **Independent work** (30 min): each student decomposes their own everyday task into a main task, a goal, and 4–6 subtasks with sub-goals. This is the writing stage of Task 2.1. | Independent |
| 0:55–1:15 | Pair activity: students swap decompositions and the partner asks **at least three clarifying questions**. The writer stays quiet. (This is the partner stage of Task 2.2, on an everyday task.) Optional variant: Activity B ("Two decompositions, one task") from `in-class-tasks.md`. | Pair |
| 1:15–1:25 | Whole-class debrief: collect one finding from three pairs. What kind of sub-goal was easy to write? What kind of sub-goal turned out to be the main task's goal in disguise? | Whole class |
| 1:25–1:30 | Closing reflection prompt on the board: *"Which of your subtasks is itself big enough to need its own decomposition?"* One-line preview of Lesson 5. | Whole class |

**Independent-work block: 30 minutes (33% of 90).** Meets the 30–50% rule.

**Cross-references.** The 55–75 min pair slot can use Activity B from `in-class-tasks.md` (everyday-task version).

**What you say out loud at the lecture.** "A decomposition has a main task, written in one sentence, and a goal, written in one sentence — the goal says when you are done. Under the main task you write subtasks. Each subtask has its own sub-goal — one sentence that says what is true once that subtask is done. The most common mistake is to skip the sub-goal. A subtask without a sub-goal is just a heading; a subtask with a sub-goal is a thing you can check off." Walk one board example through main task → goal → 4–6 subtasks with sub-goals. Resist adding a third concept (dependencies) — that arrives in Lesson 5.

**Materials.** Board and marker; the everyday-tasks list (collected live in the warm-up). No technology required.

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** no slides. Collect everyday tasks on the board.
- **Lecture (0:10–0:25):** main deck slides **4 → 7**: *What is decomposition?* · *Main task, subtasks, goal* · *Everyday example — making breakfast for four* · *IT example — creating a user account*. Walk slowly on slide 5 — the four words need to stick.
- **Independent work (0:25–0:55):** leave slide **5** on screen as the silent template (main task · goal · subtask · sub-goal). No other slides.
- **Pair activity (0:55–1:15):** no slides; the conversation happens between students.
- **Debrief (1:15–1:25):** slide **8** *(Why decompose at all?)* if useful as a closing prompt; otherwise stay on the board.
- **Closing (1:25–1:30):** no slides.

---

## Lesson 5 — 90-minute plan

**Topic.** Order of steps and dependencies.

**Central message for this lesson (one sentence).** Subtasks have an order because some subtasks need the output of another subtask before they can start; where there is no such dependency, the order is free.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: write 6–8 out-of-order subtasks for one familiar everyday task on the board (e.g. *organising a class trip*). Ask the class to call out *"X depends on Y because …"* sentences. Draw arrows live. | Whole-class |
| 0:10–0:25 | Instructor input: define *dependency*, *order*, *parallel* (informal). One everyday example walked through with arrows. Then a brief IT mirror — *sharing a file with a colleague*. Always everyday first, IT second. | Lecture |
| 0:25–1:00 | **Independent work** (35 min): each student takes their own L4 decomposition and adds dependencies and a defensible order. They mark at least one dependency and at least one free pair. (This is Task 2.3.) | Independent |
| 1:00–1:20 | In-class teacher-led activity: **MANDATORY Activity A — "Dependency sort"** from `in-class-tasks.md`. Whole-class card sort on the board, then a volunteer-led second round on a different scenario. | Whole class |
| 1:20–1:28 | Whole-class debrief: which subtask had the most dependencies pointing at it? Did any "obvious" dependency turn out to be free? Briefly link back to Week 1: bridge to the literal follower ("if you cannot tell whether two subtasks depend on each other, write the sub-goals out and ask whether one sub-goal's output is the other sub-goal's input"). | Whole class |
| 1:28–1:30 | One-line preview of Lesson 6. | Whole class |

**Independent-work block: 35 minutes (39% of 90).** Meets the 30–50% rule.

**Cross-references.** The 60–80 min slot is the full version of Activity A from `in-class-tasks.md` (Dependency sort). Read that file before this lesson — it lists the exact card stacks to prepare.

**What you say out loud at the lecture.** "A dependency is a connection between two subtasks where one needs the output of another before it can start. Notice the word *output*. A dependency is not 'feels like it should come first' — it is a precise fact: the second subtask cannot start until the first has produced something. When the second subtask does not need the first one's output, the two are free — they can swap, or run at the same time if there are two pairs of hands. In this course we say *parallel* for that, in the everyday sense only. We are not introducing concurrency this week."

**Materials.** Two stacks of 8 cards (for Activity A); magnets or blu-tack; board and marker.

The Week 2 main deck (slides 9–11) carries the dependency idea well enough that no supplementary deck is needed for L5.

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** no slides; arrows live on the board.
- **Lecture (0:10–0:25):** main deck slides **9 → 12**: *Some subtasks depend on others* · *Some subtasks are independent* · *Putting subtasks in order — birthday party* · *IT example — sharing a file*. Walk slowly on slide 9 — the *output*-as-input definition is the heart of the move.
- **Independent work (0:25–1:00):** leave slide **9** on screen as the silent reminder of the dependency definition. Otherwise no slides.
- **Activity A (1:00–1:20):** no slides. Cards on the board are the lesson.
- **Debrief (1:20–1:28):** no slides; stay on the board with the arrows visible.
- **Closing (1:28–1:30):** no slides.

---

## Lesson 6 — 90-minute plan

**Topic.** Decomposing an IT-related task. AT1 is drafted in the independent block and submitted at the 75-min mark.

**Central message for this lesson (one sentence).** A real IT task is rarely small — the move that lets a beginner take it on at all is to decompose it into subtasks with named goals and a defensible order.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: recap the **Week 2 central message verbatim** ("*A big problem becomes a manageable problem once you name the main task, its subtasks, and the order in which they have to happen*"). Then read one short IT scenario aloud and ask the class for one main task + goal + first two subtasks. | Whole-class |
| 0:10–0:25 | Instructor input: walk through the L6 scenario *"set up a new colleague's email account on their new laptop in time for their 10:00 start"*. Name main task, goal, 5–7 subtasks, 2–3 dependencies, and at least one free pair (preparing the laptop runs in parallel with creating the account). | Lecture |
| 0:25–0:55 | **Independent work** (30 min): students draft their AT1 artefact. They pick one real IT task — ideally the one from Task 2.4 — and write main task, goal, 4–8 subtasks with sub-goals, an order with at least one named dependency, and a 3–5 sentence reflection. | Independent |
| 0:55–1:15 | Pair review: partner reads the AT1 draft and asks three clarifying questions. The writer notes one thing to fix before submission. Optional variant: Activity B ("Two decompositions, one task") from `in-class-tasks.md` on the IT scenario. | Pair |
| 1:15–1:25 | **AT1 submission moment.** Students hand in their AT1 artefact at the 75-min mark. Whole-class debrief on the three most common subtle errors — subtasks too vague, sub-goals that duplicate the main task's goal, decompositions with no dependency at all. | Whole class |
| 1:25–1:30 | Preview Week 3 — abstraction and flowcharts — in one line. *"Next week we add a way to hide detail you don't need, and draw a first picture of a process."* | Whole class |

**Independent-work block: 30 minutes (33% of 90).** Meets the 30–50% rule.

**Cross-references.** The 55–75 min pair-review slot can use Activity B from `in-class-tasks.md` (IT-task version) as the structured variant of the partner read-through.

**What you say out loud at the lecture.** "This scenario looks small until you start writing the subtasks. There is no one button to press. Several systems are involved — the laptop, the mail server, the staff directory — and several pieces of information have to be gathered before anything else can happen. Watch where the dependencies sit, and watch where one branch can run in parallel with another. That is the move." Walk the scenario through main task → goal → 6 subtasks → 4 dependencies → one free branch (preparing the laptop). Avoid the temptation to write the per-subtask click-by-click steps — that is Week 1's job, not Week 2's.

**Materials.** Board and marker; paper or laptops for AT1 drafting; collection method for AT1 submissions (paper into a tray, or a shared folder).

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** slide **3** *(This week's central message)* on screen for the verbatim recap, then back to the board for the one-IT-scenario opener.
- **Lecture (0:10–0:25):** main deck slides **13 → 14**: *Decomposing a real IT task — Lesson 6 preview* · *Two valid decompositions of one task*. Walk slowly on slide 13.
- **Independent work (0:25–0:55):** leave slide **17** *(AT1 — the first assessed task)* on screen as the silent reference. Otherwise no slides.
- **Pair review (0:55–1:15):** no slides.
- **Submission + debrief (1:15–1:25):** no slides; the conversation is on the board with the common-error patterns named live.
- **Closing (1:25–1:30):** slide **18** *(What comes next: Week 3)* as the one-line preview, then slide **19** *(Recap — the central message)* to close.

---

## Facilitation tips

### Before any of the three classes

- **Read `in-class-tasks.md` end-to-end before Lesson 4.** Activity A (Dependency sort) needs two card stacks of 8 cards each. Activity B (Two decompositions, one task) needs a single named task or scenario. Both take 5–10 minutes of preparation that is easy to forget.
- **Pre-write the board layout.** For Lesson 4, sketch the four words (*main task · goal · subtask · sub-goal*) in your notes. For Lesson 5, sketch the dependency arrow notation (`X ← Y`). For Lesson 6, write the central message verbatim at the top of your notes — you read it aloud in the warm-up.
- **Decide your AT1 submission channel before Lesson 6.** Paper into a tray, a shared folder, or a single message in the course chat. Tell students the channel in Lesson 5's closing minute so they are not improvising on the day.

### During class

- **Lead with the everyday example. Always.** Lesson 4 lectures the everyday example *before* the IT example. Lesson 5 lectures the everyday example *before* the IT example. Lesson 6 starts with the central message and one IT scenario; the everyday examples are already on the board from earlier in the week.
- **Insist on the word *literal*.** Carried over from Week 1. If a student says *"the computer is dumb / stupid"*, gently swap: *"Literal. The computer is literal. It does what the subtask says — no more, no less."* The framing has to hold for the literal follower lens to do its work inside a subtask.
- **Insist on a named sub-goal for every subtask.** This is the most common Week 2 omission. The fastest fix in class: ask the student to say the sub-goal aloud. If they cannot say it in one sentence, the subtask is too big.
- **Resist solving for the student during independent work.** Walk past, ask one question (*"what's the sub-goal of subtask 3?"*), keep walking. The discomfort of writing the sub-goal themselves is where the learning lives.
- **Protect the 30–50% rule.** Independent work is the part teachers under pressure cut first. The schedules above leave 30–35 minutes; do not trim below 27. The L6 independent block also doubles as AT1 drafting time — cutting it cuts AT1.
- **Use the board for live re-orderings.** Slides set up the question; arrows happen on the board so students see the transition from out-of-order to ordered live.

---

## Answers to common student questions

- *"How many subtasks is the 'right' number?"* — For Week 2, 4–6 subtasks for an everyday task and 5–8 for an IT task is a good range. Fewer than 3 means the task was small enough to be one algorithm in the first place; more than 10 means at least one subtask is itself big enough to be its own decomposition. AT1's bracket is 4–8.
- *"What's the difference between a subtask and a step?"* — A subtask has its own **sub-goal** and is small enough to be written as a clean little algorithm of literal steps. A step is one line inside that algorithm. In Week 2 we stop at the subtask layer; the step layer is the Week 1 job, inside each subtask.
- *"Is AT1 graded?"* — Yes — AT1 is the first assessed task of the course. It is short (about a single page, ~250–500 words), submitted at the end of Lesson 6, and assessed on whether the main task, goal, 4–8 named subtasks with sub-goals, an order, and at least one dependency are present and defensible. There is no single "right" decomposition the assessor is looking for.
- *"Can I use ChatGPT for AT1?"* — Yes, as Task 2.5 describes — as a sparring partner that challenges your decomposition, not as a writer. You may not paste an LLM's text into AT1 and submit it. The AT1 candidate the LLM has helped you challenge is exactly the kind of artefact we want; the LLM's text by itself is not.
- *"What if my partner asks more than 3 clarifying questions?"* — Good. Write them all down. The point of the three-question minimum is to force at least three; more questions mean more usefully exposed ambiguity.
- *"Can I pick a school-IT task I have never actually done?"* — Yes, but you must be able to walk over to a computer and verify the button names. A decomposition with invented menu paths fails the literal-follower test, because no real follower could carry it out. If you have not done it, find someone who has and check.

---

## Formative assessment tips

Week 2 has its first **summative** moment (AT1 at the end of Lesson 6), but the per-lesson checks below are formative — they make student understanding visible early so misconceptions can be corrected before AT1 lands. Use one or two per lesson; do not try to use all of them.

### Per-lesson informal checks

- **Lesson 4 — exit ticket (3 min, end of class).** Each student writes one sentence: *"In your own words, what is the difference between a main task's goal and a subtask's sub-goal?"* Skim on the way to Lesson 5; read two strong answers at the start of L5.
- **Lesson 4 — pair report-back (2 min, after the pair activity).** Ask two pairs to name one sub-goal that turned out to duplicate the main task's goal. Listen for whether students are using the word *sub-goal* spontaneously.
- **Lesson 5 — board vote.** Three statements: (a) *"Two subtasks always depend on each other."* (b) *"Subtasks are independent when neither one's output is the other's input."* (c) *"Order doesn't matter once you have the subtasks."* Vote by hands. A strong (a) or (c) vote means the dependency definition has not landed; revisit before Activity A.
- **Lesson 5 — sticky-note collection (during Activity A).** Each student writes one dependency from their own L4 decomposition on a sticky note in the form *"X ← Y, because …"*. The pattern of complete vs. incomplete sentences is itself an assessment of how well they have grasped the *output* part of the definition.
- **Lesson 6 — one-minute paper (just before AT1 submission).** *"Write one sentence on what surprised you about decomposing your IT task."* Collect with the AT1 artefacts; the surprises tell you where the conceptual gaps still are going into Week 3.
- **Lesson 6 — exit ticket (after submission).** *"Which one of this week's tasks (2.1, 2.2, 2.3, 2.4, 2.5) was the most useful for AT1?"* Use the answers to tune Week 3's warm-up.

### What you are listening for across the week

The two phrases that mark genuine understanding by the end of Week 2 are:

- *"The sub-goal of that subtask is …"* (rather than *"the goal is to do this thing"*).
- *"X depends on Y because the input is the output"* (rather than *"X comes after Y"*).

If those two phrases appear in student speech by Lesson 6, Week 2 has done its job and Week 3 (abstraction and flowcharts) can build on it without remediation.
