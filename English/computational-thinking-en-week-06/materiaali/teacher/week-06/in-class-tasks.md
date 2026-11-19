# Week 6 — In-class tasks

## Overview

This file contains the **in-class, teacher-led** activities for Week 6. They run during class, not as homework, and cannot be replaced by an LLM or a worksheet.

- **Activity A — "Dry-run as a class"** is **MANDATORY**. It belongs in the **55–80 min slot of Lesson 18** and is the embodied diagnostic for AT2 readiness. The whole class becomes the trace table, one student per variable, and the bug surfaces in front of everyone.
- **Activity B — "Pseudocode swap and trace"** is **OPTIONAL**. It fits the **60–80 min pair-activity slot of Lesson 16**.

---

## Activity A — "Dry-run as a class" MANDATORY

**Goal.** The class collectively performs a dry run, embodying the trace table. Students see — not by being told — that reading pseudocode does not catch what a written trace catches. Makes the Lesson 18 central message physically visible just before AT2 handover.

**Group size.** Whole class. One student per variable, one as "output recorder", the rest as observers who shout when an update is missed.

**Time required.** 25 min (Lesson 18, **55–80 min slot**). Do not borrow from the 30-min independent block before it.

**Teacher preparation.**

1. **Choose your bug.** Recommended default: an **off-by-one** in a `WHILE` condition. Alternatives: wrong comparison, missing initialisation, wrong-branch `IF`.
2. **Pre-write the broken pseudocode** on a slip — do not improvise live. Recommended snippet:

   ```text
   SET counter TO 5
   WHILE counter > 1 DO
     WRITE counter
     SET counter TO counter - 1
   ENDWHILE
   WRITE "LIFT OFF"
   ```

   **Expected output (announce only after the trace finishes):** `5`, `4`, `3`, `2`, `1`, `LIFT OFF`. **Actual output from a faithful trace:** `5`, `4`, `3`, `2`, `LIFT OFF` — the `1` is missing because `counter > 1` stops one step early. Bug name: **off-by-one**.
3. **Decide your roster.** For the countdown snippet: one variable student for `counter`, one output recorder.
4. **Have the board ready** with column headings **Line · counter · Output**. The empty trace table is the stage.

**Step-by-step facilitation.**

1. **Set the rules (2 min).** *"One of you is the variable `counter`. After every line I read, you say out loud what `counter` equals now. One of you is the output recorder. The rest watch and shout if a variable student misses an update. We follow the pseudocode literally."*
2. **Assign the roles (1 min).** Confirm both speakers have a clear voice and view of the board.
3. **Read the pseudocode aloud, line by line, slowly (10 min).** After each line: the variable student calls out the new value; the output recorder writes anything `WRITE`-d to the output column; you fill in the Line column. **At the bottom of each loop, re-check the `WHILE` condition aloud as a class.** *"Counter is 1. Is 1 greater than 1? No. Loop ends."* The bug surfaces here.
4. **Announce the expected output (1 min).** *Only after the trace has completed.* Write expected next to actual on the board. The class sees the gap.
5. **Diagnose (4 min).** Ask: *"At which line did the actual output first stop matching the expected output? What does that line say?"* Read it aloud. Invite a student to propose the fix (`>` becomes `>=`, or `> 1` becomes `> 0`).
6. **Apply the fix and re-trace from the loop's last iteration (4 min).** Start from the line above the fix. The output now ends with `1`, then `LIFT OFF`.
7. **Name the bug type (2 min).** Write **"off-by-one"** on the board. *"This is the most common bug in the world. The trace table is what finds it."*
8. **Add to the running bug list (1 min).** Keep a list across L18 and into Week 7 titled *"Bugs we have found by dry-running"*. Add this one.

**Debrief questions.**

- At which line did the actual output first diverge from the expected output? How did you know?
- Could you have spotted this bug by re-reading the pseudocode without the trace?
- Why is *off-by-one* a more useful name than *"the loop was wrong"*?
- If your own Task 6.1 pseudocode has a `WHILE` or `FOR`, where could an off-by-one hide there?

**Why it requires the classroom.** Every student has a job. The variable student *says* the new value aloud — the voice catches what the eye misses. The shared board and the live divergence between expected and actual output are the whole point.

**Cross-reference.** This is the **55–80 min slot of the Lesson 18 plan** in `teacher-materials.md`. The bug name (*off-by-one*) feeds straight into the AT2 reflection vocabulary at 80–88 min.

---

## Activity B — "Pseudocode swap and trace" OPTIONAL

**Goal.** Students discover whether their own pseudocode is *readable* by an outside human. Reading pseudocode you did not write is the skill AT2 checks indirectly when it asks for plain-English explanations.

**Group size.** Pairs. (Odd numbers: one group of three.)

**Time required.** 20 min (Lesson 16, **60–80 min pair-activity slot**).

**Teacher preparation.**

1. A board prompt with the rules of the swap.
2. 3–4 fallback processes for students whose draft is too short — making tea, charging a phone overnight, sending a routine Discord message.
3. Paper and a pen per student. No technology.

**Step-by-step facilitation.**

1. **Explain the swap (2 min).** *"You exchange the pseudocode you wrote earlier. You do not name the process. Your partner reads it silently, writes a one-sentence guess at the goal, then traces it for one input you choose."*
2. **Hand over papers (1 min).** No verbal hints.
3. **Silent guess sentence (3 min).** Each reader writes *"I think this pseudocode is about ___."* at the bottom of the page **before** any trace begins.
4. **Trace for one input the writer picks (5 min).** On a separate sheet, draw a small trace table. Follow the pseudocode literally. No questions during the trace.
5. **Reveal and discuss (2 min).** Writer names the goal. Together answer: *"Did the trace produce the expected output? Was the goal guessable from the steps alone?"* Mark the **one line the reader re-read the most** — that is the rewrite candidate.
6. **Swap roles (5 min).** Same loop.
7. **Whole-class debrief (2 min).** Ask two pairs: *"Which keyword made the goal most guessable — `IF`, `WHILE`, or `FOR`?"* Usually `IF` carries the goal. Connect: **honest variable names + a visible `IF` are the readability levers**.

**Debrief questions.**

- Did your partner's trace produce the output you expected? If not, was the gap in their trace or in your pseudocode?
- Which one line did your partner re-read the most? What change would make that line read cleanly on first pass?
- Was the goal guessable from the steps alone, or only after the reveal?

**Why it requires the classroom.** The silent guess sentence forces the reader to commit before they can ask for help. The shared paper and live reveal are what an LLM cannot replace.

**Cross-reference.** This is the **60–80 min slot of the Lesson 16 plan** in `teacher-materials.md`. If a teacher must drop one activity this week, drop Activity B — **Activity A carries the central message of Week 6** and is the diagnostic of AT2 readiness.
