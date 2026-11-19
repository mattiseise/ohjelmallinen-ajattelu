# Week 8 — In-class tasks

## Overview

This file contains the **in-class, teacher-led** activities for Week 8. They run during class, not as homework. Both core activities work in a language-mixed room — some students on JavaScript, some on C# — at the same time.

- **Activity A — *Show-and-tell loops*** is **MANDATORY**. It belongs in the **55–75 min slot of Lesson 22**.
- **Activity B — *AT3 presentations*** is **MANDATORY**. It belongs in the **55–85 min slot of Lesson 24** and **is the AT3 oral component**.
- **Activity C — *Translation race*** is **OPTIONAL**, fits the 1:05–1:20 slot of Lesson 23 for classes that finish builds early.

Cross-referenced from `teacher-materials.md`.

---

## Activity A — *Show-and-tell loops* MANDATORY

**Goal.** Every pair (or solo student) walks the class through their loop snippets, and the room names the four parts (counter, condition, body, update) for one of them. Students see — not by being told — that the *shape* of a loop is the same in JavaScript and C#.

**Group size.** Whole class. Pairs take turns at the projector; the rest watches.

**Time required.** 20 min (Lesson 22, **55–75 min slot**). Do not borrow from the independent block before it.

**Teacher preparation.**

1. **Confirm every student has their three loop snippets** from Task 8.2 ready before the slot.
2. **Project the order.** Mix JS and C# in the order so the dual-language framing is unavoidable.
3. **Write the four parts on the board:** **Counter / Condition / Body / Update.**

**Step-by-step facilitation.**

1. **Set the rules (1 min).** *"Each pair shows one loop on the projector. Read it aloud, run it, read the output. Then someone else — not you — names one of the four parts and points at it. About 90 seconds per person."*
2. **Run the relay (~17 min).** For each student: 20s walk up, 20s read aloud, 10s run, 20s peer names a part, 20s next.
3. **Land the comparison (2 min).** Point at the board: *"You all wrote the same four parts. Some with `let` and `console.log`; others with `int` and `Console.WriteLine`. Same shape. That is the headline of Lesson 22."*

**Debrief questions** (use 1–2 in the 1:15–1:25 debrief).

- Whose count-down loop was the easiest to read aloud?
- Did anyone forget the update step? What happened?

**Why it requires the classroom.** The live run and the public naming of the four parts is the whole point. Cannot be done as homework.

**Cross-reference.** The **55–75 min slot of Lesson 22** in `teacher-materials.md`. The "we saw" pattern folds into the 1:15–1:25 debrief, where the infinite-loop hazard is surfaced once.

---

## Activity B — *AT3 presentations* MANDATORY

**Goal.** Every student delivers a **2-minute** oral presentation of their AT3 program, covering the four beats: what the program does, how it works, what went wrong, how it was fixed. This **is** the AT3 oral component.

**Group size.** Whole class. Each student presents in turn.

**Time required.** 30 min (Lesson 24, **55–85 min slot**). Two minutes per student plus ~30s transition fits ~12 students. Larger classes — see Facilitation tips in `teacher-materials.md`.

**Teacher preparation.**

1. **A visible phone timer**, projected on the wall.
2. **A pre-announced order** of presenters.
3. **The rubric deck `slides-l24-presentation-rubric.md`** projected between presentations. Not over a student presenting.
4. **A note sheet** with each student's name and four checkboxes (program runs / names what it does / one bug-and-fix described / 2-minute delivered). The pass-check record.

**Step-by-step facilitation.**

1. **Set the rules (2 min).** *"2 minutes each, four beats, 30s per beat. Soft chime at 2:00, hard cut at 2:30. After each presentation we ask the room one question: name one thing you noticed."*
2. **Run the presentations (~26 min).** Per student: 10s stand up, 2:00 present, 20s peer answer, 10s teacher ticks the boxes, next.
3. **Close the slot (2 min).** Thank every presenter. Course closure follows.

**Why it requires the classroom.** The live oral, the public timer, and the peer feedback only exist in the room.

**Cross-reference.** The **55–85 min slot of Lesson 24** in `teacher-materials.md`. The four-checkbox sheet is the AT3 pass / not-yet-pass record. Any missing check → not-yet-pass and a one-week re-submit window.

---

## Activity C — *Translation race* OPTIONAL

**Goal.** Two pairs translate the **same** Week 6 pseudocode — one pair into JS, one into C# — and compare line by line. For classes that finish L23 builds early.

**Group size.** Pairs of pairs (four students).

**Time required.** 15 min (Lesson 23, **1:05–1:20 slot**).

**Teacher preparation.** One piece of Week 6 pseudocode (the age-limit check is the safe default). Pair pairs across languages.

**Step-by-step facilitation.**

1. **Pose the pseudocode (1 min).** On the board.
2. **Race (10 min).** Each pair writes the pseudocode in their language, on paper. No laptops.
3. **Compare (3 min).** Pairs swap translations. Circle words that changed; underline words that did not.
4. **Close (1 min).** Ask one group: *"Which line did not change at all?"* Expected: the `if (...)` line.

**Why it requires the classroom.** Cross-language pairing only exists in the room.

**Cross-reference.** Optional **1:05–1:20 slot of Lesson 23** in `teacher-materials.md`.
