# Week 8 — Student tasks (JavaScript)

## Overview of the week's tasks

This week has **two 🟢 MANDATORY** and **three 🟣 DEEPENING** JavaScript tasks. The mandatory tasks are your **must-do minimum** — finish both to pass AT3. The deepening tasks are optional; pick one or two if you have time.

**AT3 is the central deliverable this week.** Task 8.1-JS *is* the AT3 brief. You submit source code, a screenshot, and a short reflection at the end of L23, and deliver a **2-minute** oral presentation in L24. Task 8.2-JS is a small loop warm-up before you translate your own pseudocode.

JS runs in your browser's DevTools console (`Cmd + Opt + J` on Mac, `Ctrl + Shift + J` on Win/Linux). "Testing" means running with two different values; "debugging" means reading a console error and changing one line.

---

## 🟢 MANDATORY — Task 8.1-JS — AT3 brief: translate your Week 6 pseudocode into JavaScript

**Goal.** Translate one piece of your own Week 6 pseudocode into a small, working JavaScript program (about 10–25 lines), run it in the browser console with two different starting values, find and fix one bug, and prepare a **2-minute** oral presentation. This is **AT3**.

**This is the must-do minimum for Week 8.** Without this task there is no AT3.

### Steps

1. **Pick one piece of your Week 6 pseudocode** (6–20 lines). If you cannot find one, use a fallback template and adapt the values: age-limit check; password-length check; points-to-feedback; simple counter (1 to 5); greeting by name three times.
2. **Translate it line by line into JavaScript**, using the translation table in `self-study.md`. Use hard-coded variable values at the top (no `prompt()` needed). Example:

   ```js
   let password = "hi";
   if (password.length >= 8) {
     console.log("strong enough");
   } else {
     console.log("too short");
   }
   ```

3. **Open the browser DevTools console**, paste the program, press Enter, read the output.
4. **Run it with two different starting values.** Change one variable at the top and run each version. Take a **screenshot** showing both outputs.
5. **Find and fix one bug.** If your program ran first try, **trigger** a bug on purpose: deliberately misspell one variable name, or remove one `;`. Run, read the error message, fix it back. Name the bug in plain English ("I had `passwrd` instead of `password`").
6. **Save the source** as `at3.js` (or paste as a fenced ```js block into your submission notes).
7. **Write a 3–5 sentence reflection** naming what the program does, the one bug you found, and the one fix you applied.
8. **Prepare your 2-minute oral presentation** for L24. Four beats, ~30 seconds each: **what** the program does → **how** it works (variables, `if/else`, loop?) → **what** went wrong → **how** you fixed it. Rehearse with a phone timer.

### If you are doing this alone

The L24 presentation assumes an audience. If you cannot present live — illness, hybrid attendance — record a **2-minute** video presenting to the camera, *or* post the program plus a 3-sentence summary in the class chat. The four beats are the same.

### Keep your notes

This **is** **AT3**. Bring four artefacts to L24: the source file (`at3.js`), the screenshot of two runs, the 3–5 sentence reflection naming the bug and the fix, and yourself ready to give the **2-minute** oral presentation.

AT3 is **submitted at the end of L23** and **presented in L24**. Pass / not-yet-pass on four checks: the program runs (or your failed attempt is documented), you can name what it does, one bug-and-fix pair is described, the **2-minute** presentation was delivered.

---

## 🟢 MANDATORY — Task 8.2-JS — Loop warm-up: count 1 to 5 in JavaScript

**Goal.** Write three short `for` loops in JavaScript — count up, count down, greet by name — so the loop pattern is in your fingers before AT3.

**This is part of the must-do minimum for Week 8.**

### Steps

1. **Open the browser console.** Paste and run:

   ```js
   for (let i = 1; i <= 5; i++) {
     console.log(i);
   }
   ```

   Expected output: 1, 2, 3, 4, 5, one per line.
2. **Modify it to print 5 down to 1.** Change `i = 1` to `i = 5`, `i <= 5` to `i >= 1`, `i++` to `i--`. Run.
3. **Modify it to print "Hello, NAME" three times.** Replace your name in the quotes:

   ```js
   for (let i = 0; i < 3; i++) {
     console.log("Hello, <your name>");
   }
   ```

4. **Save all three snippets in one file** (`loop-warmup.js`) with a one-line comment above each.

### Keep your notes

These three patterns are exactly the loop shapes you may need inside your **AT3** program. Keep `loop-warmup.js` in the same folder as your AT3 files.

---

## 🟣 DEEPENING — Task 8.3-JS — Combine loop + if/else in JavaScript

**Goal.** Write a small JS program that loops through a list of 5 passwords and prints "long enough" or "too short" for each.

### Steps

1. **In the browser console**, paste and run:

   ```js
   let passwords = ["hi", "correcthorse", "12345", "battery", "longpassword"];
   for (let i = 0; i < passwords.length; i++) {
     if (passwords[i].length >= 8) {
       console.log("long enough");
     } else {
       console.log("too short");
     }
   }
   ```

2. **Predict the output before pressing Enter.** Five lines, one per password.
3. **Compare prediction with reality.** If a line surprised you, find the password it came from and explain why.
4. **Write a 3-sentence reflection** on what the program does and one thing you would add next.

### Keep your notes

If your **AT3** program uses an `if/else` and you finish early, attach this snippet as a natural extension. Keep it in the AT3 folder.

---

## 🟣 DEEPENING — Task 8.4-JS — Read a real error message and fix it (JS)

**Goal.** Read three real JavaScript error messages and apply one small fix to each, so the first surprise error in AT3 does not stop you.

### Steps

1. **Paste each snippet below into the browser console, one at a time.** Each contains exactly one mistake.

   ```js
   // Snippet A
   let score = 75;
   if (scre >= 50) {
     console.log("you passed");
   }
   ```

   ```js
   // Snippet B
   let age = 17;
   if (age = 18) {
     console.log("adult");
   }
   ```

   ```js
   // Snippet C
   for (let i = 0; i < 3; i++) {
     console.log("Hello");
   
   ```

2. **For each snippet**, copy the exact error message (Snippet B prints unexpected output — a silent bug, not an error). Name the line and the fix in plain English. Apply the fix and re-run.
3. **Optional LLM sparring step.** Paste one error message plus the snippet into an LLM with this prompt:

   ```text
   Explain what this JavaScript error means without telling me how to fix it.
   I want to find the fix myself.
   <paste error message + snippet here>
   ```

   If the LLM gives the fix anyway, **reject** the answer and write the fix in your own words. Do not paste LLM output verbatim into your notes.

### Keep your notes

A small library of JS errors written down now will speed you through the L24 moment of **AT3** when you have to read a real error message and apply one small fix.

---

## 🟣 DEEPENING — Task 8.5-JS — Compare with a C# classmate

**Goal.** Read a classmate's C# program and write 3–5 sentences on the differences and one thing that is the same.

### Steps

1. **Find a classmate** who used C# for AT3. Show each other your programs.
2. **Read theirs line by line.** Identify the JS equivalent of each C# line.
3. **Write 3–5 sentences** on the differences (semicolons, `Console.WriteLine` vs `console.log`, `int` / `string` vs `let`, capital method names in C#) and **one thing that is the same** (the loop structure, the `if/else`, the goal).

### If you are doing this alone

If no C# classmate is available, read the C# version of one worked example in `self-study.md` (Programs A–E) and write the same 3–5 sentences comparing it with the JS version on the same page.

### Keep your notes

Attach the 3–5 sentences to your **AT3** folder. They are not part of the pass check, but they sharpen the L24 presentation: a student who can name one thing about the *other* language understands their own choice better.
