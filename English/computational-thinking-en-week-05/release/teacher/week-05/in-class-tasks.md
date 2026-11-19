# Week 5 — In-class tasks

## Overview

This file contains the **in-class, teacher-led** activities for Week 5. They run during class, not as homework. The week's job is to make the three building blocks — *sequence, condition, repetition* — easy to spot in real language, so students can produce the AT2-feeder artefact.

- **Activity A — "Find the if / Find the loop"** is **MANDATORY**. Two halves: *Find the if* in Lesson 14 (60–80 min slot, ~23 min); *Find the loop* in Lesson 15 (58–80 min slot, ~22 min).
- **Activity B — "Live decision tree on the board"** is **OPTIONAL** but recommended for Lesson 14.

Both require live classroom interaction — voting, writing on the board, rewrites happening in front of everyone. They cannot be replaced by homework or by an LLM.

---

## Activity A — "Find the if / Find the loop" 🟢 MANDATORY

**Goal.** Students cannot complete the AT2-feeder task confidently unless they can recognise the three building blocks in language they did not write themselves. This game makes that recognition fast, public and diagnostic.

**Group size.** Whole class. **Time required.** Two halves of 22–23 min: *Find the if* in L14, *Find the loop* in L15. Either half can run alone; the *Find the if* half is the more diagnostic one for AT2.

**Teacher preparation.** Prepare the two stacks below (paper slips or a printed list). Two columns of board space — one for canonical `if … then … else …` rewrites, one for `for each / repeat until / while` rewrites.

### Stack 1 — Conditions (read in Lesson 14)

Read each slip out loud. Class votes: *condition* or *no condition*. If condition, class names the test.

1. *"If the password is shorter than 8 characters, reject it."* — **condition** (test: *length < 8*).
2. *"Boil the water."* — **no condition**.
3. *"If it rains, take the bus; otherwise walk."* — **condition** (test: *raining now?*).
4. *"Pour 30 ml of milk into the mug."* — **no condition**.
5. *"If the user has not logged in for 90 days, deactivate the account."* — **condition** (test: *last login > 90 days?*).
6. *"Add a teaspoon of sugar."* — **no condition**.
7. *"If you finish your homework before dinner, you can play games."* — **condition**.
8. *"Switch the kettle on."* — **no condition**.
9. *"If the ticket mentions a printer, send it to Hardware; otherwise send it to General Support."* — **condition** (default branch).
10. *"If the milk smells off, throw it out."* — **condition** (one-branch, no else).

### Stack 2 — Repetitions (read in Lesson 15)

Read each slip out loud. Class votes: *repetition* or *no repetition*. If repetition, class names the **stopping condition**.

1. *"For each name in the register, mark present or absent."* — **repetition** (stop: end of the register).
2. *"Make a cup of tea."* — **no repetition** (a sequence).
3. *"While the kettle is still hot, do not boil it again."* — **the deliberate trick**: a *while* in English does not always mean a loop. Debrief on the board.
4. *"Repeat until the inbox is empty."* — **repetition** (stop: *inbox empty*).
5. *"Press the button once."* — **no repetition**.
6. *"For each photo on the phone, decide if it should be deleted."* — **repetition**.
7. *"Keep refreshing the page until the seat is available."* — **repetition** (watch the runaway case).
8. *"Open the front door."* — **no repetition**.
9. *"While the train has not arrived, keep checking the platform sign."* — **repetition** (flag the runaway case).
10. *"For each row of the spreadsheet, check that the date column is not empty."* — **repetition**.

### Step-by-step facilitation

1. **Set the rules (2 min).** *"I read a short statement. You vote: condition / no condition (L14) or repetition / no repetition (L15). If it is a condition, name the **test**. If it is a repetition, name the **stopping condition**."*
2. **Read each slip, take the vote, name the test or stop, write the canonical shape on the board.** ~90 seconds per slip.
3. **Debrief the close calls (1–2 min each).** Disagreement is the lesson.
4. **Close (2 min).** *"Which slip was hardest to classify, and why?"* Connect to AT2: *"In your AT2 process description, every condition and repetition must be visible enough that a stranger could vote on it like we just did."*

### Debrief questions

- Was there a slip where the **test was hidden** in everyday phrasing?
- Was there a repetition whose **stop was unobservable**?
- Did any *while* statement turn out **not** to be a real loop?

**Why it requires the classroom.** The public vote and the live rewrite teach a skill a worksheet cannot. Students learn to see structure in language they did not write themselves — exactly what AT2 asks.

**Cross-reference.** Named in `## Lesson 14 — 90-minute plan` (60–80 min) and `## Lesson 15 — 90-minute plan` (58–80 min) in `teacher-materials.md`.

---

## Activity B — "Live decision tree on the board" 🟣 OPTIONAL

**Goal.** Walk one decision tree slowly, end-to-end, in front of the class — students see *honest tests* and *named branches* before they draw their own.

**Time required.** 20 min. Fits the 30–55 min slot of L14 as an alternative to part of the lecture.

**Teacher preparation.** Pick one rule the class will all know (school lateness policy; *"should I take an umbrella today?"*). Have an IT mirror in your back pocket (e.g. *"should this login attempt be blocked?"*). If you ship `slides-l14-decision-trees.md`, this activity is its companion.

### Step-by-step facilitation

1. **Write the rule on the board (2 min).** Read it aloud.
2. **Identify the root question (3 min).** *"What is the first test the follower runs?"* Write it at the top.
3. **Branch (3 min).** *"What are the possible answers?"* Draw the lines.
4. **Test at each branch (5 min).** *"What happens at the leaf, or is there another test waiting?"*
5. **Spot the bad test (4 min).** *"Could a literal follower actually check this test?"* Push on vague branches — *"will I be late?"* is not honest until it becomes *"is it later than 8:15?"*. **Rewrite on the board.**
6. **Connect to AT2 (2 min).** *"Every condition in your AT2 artefact has a tree like this hiding behind it."*
7. **Optional — IT mirror (1 min).** If the supplementary deck is on screen, point to the login-block example: *"Same shape, different scene."*

### Debrief questions

- Did the class agree on the root question?
- Was there a branch where the test was vague? How did the rewrite change the meaning?

**Why OPTIONAL.** Overlaps with Activity A. If you have time for only one, run Activity A — it covers both conditions and repetitions and is more diagnostic.

**Cross-reference.** Named in `## Lesson 14 — 90-minute plan` (30–55 min slot) in `teacher-materials.md`.

---

## How these activities connect to `teacher-materials.md`

- **Activity A (MANDATORY)** — L14 plan, 60–80 min (*Find the if*); L15 plan, 58–80 min (*Find the loop*).
- **Activity B (OPTIONAL)** — L14 plan, 30–55 min.

If a teacher must drop one, drop Activity B. Activity A is the calibration moment of the week.
