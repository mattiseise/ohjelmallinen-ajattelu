# Week 7 — In-class tasks

## Overview

This file contains the **in-class, teacher-led** activities for Week 7. They run during class, not as homework, and cannot be replaced by an LLM or a worksheet. Both activities are designed to work in a **language-mixed room** — some students on JavaScript, some on C#, at the same time. That is the point, not a problem.

- **Activity A — *Console relay*** is **MANDATORY**. It belongs in the **55–75 min slot of Lesson 20**. Every student in the room — JS and C# alike — sees and predicts both languages' snippets, and the comparison is the lesson.
- **Activity B — *Translate-your-neighbour*** is **OPTIONAL**. It fits the **60–80 min pair-activity slot of Lesson 21**.

---

## Activity A — *Console relay* MANDATORY

**Goal.** The class predicts the output of six small snippets — three JavaScript, three C# — before the teacher runs each one live. Students see — not by being told — that the *thinking* is the same in both languages and the syntax is the only thing that changes. The Week-7 antidote to the "C# is harder than JS" misconception.

**Group size.** Whole class. Every student writes their own prediction; the teacher runs each snippet on the projector.

**Time required.** 20 min (Lesson 20, **55–75 min slot**). Do not borrow from the 30-min independent block before it.

**Teacher preparation.**

1. **Open both environments side by side** on the projector before class: browser DevTools console (any browser) on one half, `dotnetfiddle.net` on the other. Have the C# `Main` skeleton already visible in Fiddle.
2. **Prepare the six snippets** in advance — either copied into a notes file, or on numbered cards. Recommended default set (three JS, three C#, in this order):

   ```javascript
   // Snippet 1 (JS)
   let x = 5;
   let y = 3;
   console.log(x + y);
   ```

   ```javascript
   // Snippet 2 (JS)
   let name = "Lyra";
   console.log("Hello, " + name);
   ```

   ```javascript
   // Snippet 3 (JS)
   let age = 17;
   if (age >= 18) console.log("adult");
   else console.log("minor");
   ```

   ```csharp
   // Snippet 4 (C#)
   int x = 5;
   int y = 3;
   Console.WriteLine(x + y);
   ```

   ```csharp
   // Snippet 5 (C#)
   string name = "Lyra";
   Console.WriteLine("Hello, " + name);
   ```

   ```csharp
   // Snippet 6 (C#)
   int age = 17;
   if (age >= 18) Console.WriteLine("adult");
   else Console.WriteLine("minor");
   ```

   The pairing is on purpose: snippet 1 ↔ 4, 2 ↔ 5, 3 ↔ 6. Same job, different surface.
3. **Decide your snippet order.** Alternate (1, 4, 2, 5, 3, 6) for the strongest side-by-side feel, or block (1, 2, 3, then 4, 5, 6) if your class needs the JS-only / C#-only frame first. Alternating is the default recommendation.
4. **Have the board ready** with a two-column tally: **Predicted correctly | Surprised by output**. Tick marks during the relay tell you in real time whether the class is reading code or guessing.

**Step-by-step facilitation.**

1. **Set the rules (2 min).** *"I will show six small snippets, one at a time. Three are JavaScript, three are C#. For each snippet, you write — on paper or in your chat — exactly what you think the console will print, **before** I press Run. Then I run it. Then we look at the difference, if any. The point is not to be right; the point is to read code line by line."*
2. **Show snippet 1 on screen (2 min).** Read it aloud once. Give students 30 seconds. Run it. Read the output aloud. Ask one student: *"What did you predict?"* Tick the right column on the board.
3. **Repeat for snippets 2–6 (~15 min total)**, alternating between JS and C# (1, 4, 2, 5, 3, 6 is the default order). For each snippet:
   - 20 seconds to predict in silence,
   - run live,
   - read the output aloud,
   - one student volunteers what they wrote, the room compares, tick the board.
4. **Land the comparison at the end (1 min).** Point at the board. *"The thinking was identical for snippets 1 and 4. For 2 and 5. For 3 and 6. The thing that changed each time was only the words. That is what 'syntax is the deal, thinking is the thing' means."*

**Debrief questions** (use 1–2 of these in the L20 1:15–1:25 debrief, not inside the relay itself).

- Which pair (1↔4, 2↔5, or 3↔6) felt the most "obviously the same"?
- Did anyone predict a snippet correctly in *the other* language?
- Which one C# word did you have to look up? Which one JS word?

**Why it requires the classroom.** The live predict-then-run rhythm and the immediate peer comparison are the whole point. Cannot be done as homework.

**Cross-reference.** This is the **55–75 min slot of the Lesson 20 plan** in `teacher-materials.md`. The "we saw" board built in this slot is then folded back into the 1:15–1:25 debrief.

---

## Activity B — *Translate-your-neighbour* OPTIONAL

**Goal.** A JS-student and a C#-student translate each other's `if/else` code into their own language, by hand, no LLM. Students discover that the translation is mostly word-for-word and the residual differences are small.

**Group size.** Pairs — **one JS-student with one C#-student**. (Odd numbers: one group of three with two of one language.)

**Time required.** 20 min (Lesson 21, **60–80 min pair-activity slot**).

**Teacher preparation.**

1. **A board prompt** with the rules of the translation.
2. **Paper and a pen per student.** No laptops during the translation itself.
3. **A fallback `if/else` snippet** in case a student does not have their own task code yet (any age-limit `if/else` from the self-study works).

**Step-by-step facilitation.**

1. **Pair across languages (2 min).** Each pair has one JS-student and one C#-student.
2. **Swap `if/else` code (1 min).** Each student gives the other their working code from the *First if/else* task. No verbal hints.
3. **Translate by hand (8 min).** Each student writes — on paper, no laptop — the *other* student's code in their **own** language. Where word-for-word fails, circle the line.
4. **Run the translations (5 min).** Now allow laptops. Each student paste-tests their translation in their own environment.
5. **Reveal and discuss (2 min).** Pairs compare what each circled. Which lines translated cleanly?
6. **Whole-class debrief (2 min).** Ask two pairs: *"Which one word changed the most? Which one did not change at all?"* Expected pattern: `let` ↔ `int`/`string`, `console.log` ↔ `Console.WriteLine`. `if`, `else`, `>=`, `{`, `}` did not change.

**Debrief questions.**

- Which lines did you translate without hesitating?
- Which lines made you stop and think?

**Why it requires the classroom.** The cross-language pairing only exists in the room. The live translation by hand is what an LLM cannot replace.

**Cross-reference.** This is the **60–80 min slot of the Lesson 21 plan** in `teacher-materials.md`. If a teacher must drop one activity this week, drop Activity B — **Activity A carries the central message of Week 7** and is the diagnostic of AT3 readiness.
