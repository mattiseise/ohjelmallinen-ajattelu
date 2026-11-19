# Week 8 — Closing the loop

Computational Thinking

A first-year vocational ICT course

The last week. Loops, your first real program, and a 2-minute presentation.

---

## What lands this week

- Lesson 22 — **loops in code**: `for` and `while`, side by side in JavaScript and C#
- Lesson 23 — **build day**: translate your Week 6 pseudocode into a small running program
- Lesson 24 — **test, fix one bug, present**: AT3 is submitted and presented in class

> *The course closes the loop: you take pseudocode you wrote yourself in Week 6, translate it into JavaScript or C#, run it, find one bug, fix it, and explain how it works. Programming has stopped being mysterious.*

---

## Loops — the shape (JS and C# side by side)

#### JavaScript

```js
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
```

#### C#

```csharp
for (int i = 1; i <= 5; i++) {
    Console.WriteLine(i);
}
```

Both print 1, 2, 3, 4, 5. Same job — different surface words.

---

## Counter, condition, body, update

A `for` loop has four named parts:

- **Counter** — `i`, starts at 1
- **Condition** — `i <= 5`, checked before every repeat
- **Body** — the curly-brace block, runs once per repeat
- **Update** — `i++`, changes the counter between repeats

Read it aloud: *"Counter from 1, while 5 or below, print the counter, add one."*

---

## A `while` loop (JS and C# side by side)

#### JavaScript

```js
let count = 0;
while (count < 3) {
  console.log("Hello");
  count = count + 1;
}
```

#### C#

```csharp
int count = 0;
while (count < 3) {
    Console.WriteLine("Hello");
    count = count + 1;
}
```

Both print `Hello` three times. Use `while` when "until" is more natural than "repeat N times".

---

## When a loop runs forever

If the counter never changes, the condition never becomes false, and the body keeps running.

- Browser console — the page hangs; the browser warns the script is slow.
- .NET Fiddle — the run times out after a few seconds.

The **fix**: make sure something inside the body changes the value the condition tests.

---

## From your pseudocode to your program

Lesson 23 is the build day. Nothing new lands.

You pick one piece of your **Week 6 pseudocode** (6–20 lines). You translate it line by line using the table. You run it. You save the file.

The thinking was already done in Week 6. The work this week is mostly substitution.

---

## The translation table

| Pseudocode             | JavaScript                          | C#                                      |
|------------------------|-------------------------------------|-----------------------------------------|
| `WRITE "Hello"`        | `console.log("Hello");`             | `Console.WriteLine("Hello");`           |
| `SET x TO 5`           | `let x = 5;`                        | `int x = 5;`                            |
| `IF x >= 18 THEN …`    | `if (x >= 18) { … }`                | `if (x >= 18) { … }`                    |
| `REPEAT N TIMES`       | `for (let i = 0; i < N; i++) { … }` | `for (int i = 0; i < N; i++) { … }`     |
| `INCREASE x BY 1`      | `x = x + 1;`                        | `x = x + 1;`                            |

That is enough for everything you wrote in Week 6.

---

## Loop + if/else — password check (JS and C# side by side)

#### JavaScript

```js
let passwords = ["hi", "correcthorse", "12345678"];
for (let i = 0; i < 3; i++) {
  if (passwords[i].length >= 8) {
    console.log("long enough");
  } else {
    console.log("too short");
  }
}
```

#### C#

```csharp
string[] passwords = { "hi", "correcthorse", "12345678" };
for (int i = 0; i < 3; i++) {
    if (passwords[i].Length >= 8) {
        Console.WriteLine("long enough");
    } else {
        Console.WriteLine("too short");
    }
}
```

The structure (loop, condition, branch) is identical. Surface words differ.

---

## Save, run, see output

**JavaScript** — in the browser DevTools console:

- `Cmd + Opt + J` (Mac) or `Ctrl + Shift + J` (Win/Linux)
- Paste, press Enter, read the output
- Save the code as a `.js` file

**C#** — in an online .NET runner:

- Open `dotnetfiddle.net`, choose **Console**
- Paste into the `Main` method, press **Run**
- Save the code as a `.cs` file

Take a screenshot of the run.

---

## Reading a real error message (JavaScript)

```text
Uncaught ReferenceError: scre is not defined
    at <anonymous>:3:15
```

In plain English: *"I do not know what `scre` is."*

The cause: somewhere above, you declared `score`, then later wrote `scre` (missing the `o`).

The fix: find `scre`, type the missing `o`, re-run.

---

## Reading a real error message (C#)

```text
error CS0103: The name 'scre' does not exist in the current context
```

The same bug, the same fix. C# refuses to compile until you correct the spelling.

A second common C# error:

```text
error CS1002: ; expected
```

Missing semicolon. The message names the line. Add the `;`, re-run.

---

## One small fix, one re-run

That is what "debugging" means in this course.

- No debugger tool.
- No stop-the-program-line-by-line tool.
- No testing framework.

**Read the message → find the line → change one small thing → run again.**

You will do this at least once for AT3.

---

## Your 2-minute presentation

Four beats, roughly 30 seconds each:

1. **What** the program does (plain English).
2. **How** it does it (variables, `if/else`, loop).
3. **What went wrong** (the one bug, by name).
4. **How you fixed it** (the one line you changed).

Time it on a phone. Two minutes is short — aim for under, not over.

---

## Must-do minimum vs. deepening

**Must-do minimum** — every student leaves Week 8 with:

- A small program translated from their own Week 6 pseudocode
- Two runs, two outputs, one bug found and fixed
- A 2-minute oral presentation in class

**Deepening (optional):**

- Combine a loop with an `if/else`
- Compare your program with a classmate's other-language version
- Add input from `prompt()` or `Console.ReadLine()`

---

## Tasks this week (see your language's task file)

- **Task 8.1** *(MANDATORY)* — AT3 brief: translate your Week 6 pseudocode (in `student-tasks-js.md` or `student-tasks-csharp.md`)
- **Task 8.2** *(MANDATORY)* — Loop warm-up: count 1 to 5
- **Task 8.3** *(DEEPENING)* — Loop + if/else password check
- **Task 8.4** *(DEEPENING)* — Read a real error message and fix it
- **Task 8.5** *(DEEPENING)* — Compare with a classmate using the other language

---

## How AT3 is assessed

Pass / not-yet-pass on four checks:

- The program **runs** (or there is a documented attempt with the error recorded).
- You can **name** in plain English what the program does.
- One **bug-and-fix pair** is documented in your reflection.
- The **2-minute** presentation was delivered on Lesson 24.

No number grade. No rubric beyond this checklist.

---

## Closing the loop — Week 1, one more time

The course opened with one question:

> **How do I speak to a computer so that it understands what I want it to do?**

You have answered it. Not in theory — with a working program in your hand.

Programming has stopped being mysterious.

---

## Thank you, and what comes next

This was Computational Thinking — the foundation under the programming you will do for the rest of your studies.

Keep your AT3 source file. Read it again in six months. It will look small. That is the point — you wrote it.

Welcome to the other side of the central question.
