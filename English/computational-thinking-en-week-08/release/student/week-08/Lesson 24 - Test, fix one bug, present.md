# Lesson 24 — Test, fix one bug, present

Three things land here, and they all depend on a program that runs. **Test** with two starting values. **Read** one real error message and **fix** one line. **Present** the whole story in 2 minutes.

### Testing by hand

"Testing" this week means one specific thing: **run the program with at least two different starting values, and check that the output makes sense each time.** No automatic testing tool, no test framework, no special vocabulary. Just changing one number or one string at the top and pressing Run.

For the age-limit program above, the two values might be `age = 17` and `age = 19`. The first should print `not allowed`; the second `allowed`. If both runs match what you predicted, the program passes your by-hand test. If one prints the wrong message, you have just found a bug.

#### JavaScript — change one line between runs

```js
let age = 17;   // run once with 17, then change to 19 and run again
```

#### C# — change one line between runs

```csharp
int age = 17;   // run once with 17, then change to 19 and run again
```

For AT3 you will run your own program with two different values and capture both outputs (one screenshot with both runs visible is fine; two screenshots also fine).

### Reading a real error message

When the computer is unhappy it prints an **error message**. It looks scary the first time — long, technical — but for the simple bugs this week the message almost always points right at the line that needs changing.

A common JavaScript error:

```text
Uncaught ReferenceError: scre is not defined
    at <anonymous>:3:15
```

And its C# cousin:

```text
error CS0103: The name 'scre' does not exist in the current context
```

Both messages say the same thing: *I do not know what `scre` is.* The cause is almost always a typo — somewhere up in your program you declared `score`, and somewhere later you wrote `scre` (missing the `o`). The fix: find `scre`, type the missing `o`, run again.

This is **debugging at this course's level**: read what the computer told you, find the line it was talking about, change one small thing, run again.

Two more shapes of error you may meet. **JavaScript** with `=` instead of `===` usually shows no error message but a silent wrong answer — you catch it by *testing with two values* and noticing the second is wrong. **C#** with a missing semicolon prints `error CS1002: ; expected` and tells you the line number. Add the `;` at the end of that line, save, run again.

> **Pause for a moment:** Pick one program you wrote in Lesson 23. Without changing the logic, deliberately misspell a variable name somewhere in the middle of the program. Run it. Read the error message. Predict, before you fix it, exactly which word in your program the message is pointing at. Then fix it and re-run. The first time you do this, the mystery of error messages disappears.

### One small fix, one re-run

"Debugging" in this course is **reading a console error message and applying one small fix**. It is not a debugger tool and not a stop-the-program-line-by-line tool. There is no special software to install. There is no testing framework to learn. The whole loop is:

1. Run the program.
2. See an error message *or* an unexpected output.
3. Read the message (or compare expected and actual output line by line).
4. Find the line responsible.
5. Change one small thing.
6. Run the program again.

For AT3 you have to do this at least once. The bug can be a typo, a missing semicolon (C#), `=` instead of `==`, a missing `}` — any counts. If your program ran first try, **trigger** a bug on purpose: break one thing, read the message, fix it back.

### Your 2-minute presentation

On Lesson 24 you will give a **2-minute** oral presentation of your program to the room. Two minutes is short — about 200 spoken words. The presentation has **four beats**, roughly 30 seconds each:

1. **What the program does.** One or two sentences in plain English. *"My program takes a password and prints either 'strong enough' or 'too short' depending on its length."*
2. **How it does it.** Walk through the structure. *"At the top I set a variable called `password`. Then there is an `if/else`: if the length of the password is 8 or more, it prints 'strong enough', otherwise 'too short'."* If your program has a loop, name the four parts (counter, condition, body, update).
3. **What went wrong.** Name the one bug you found. *"The first time I ran it, I had written `password.length` with a small l, but my code was C# where it has to be capital L, so I got a CS0103 error."*
4. **How you fixed it.** One sentence. *"I changed the small l to a capital L on that one line and re-ran the program."*

That is your 2 minutes. No slides, no script read word-for-word, no need for elegant code. You **stand by your own program** and explain it in your own words.

Practical tip: rehearse once at home with a phone timer. If you finish in 45 seconds, you are skipping a beat. If you go past 2 minutes, you are probably reading the code line by line — cut that and talk about what the program *does* instead.

> **Pause for a moment:** Open your program on screen now. Try the four beats out loud, with a timer if you have one. The first run will probably either be too short or too long. The second run is almost always closer. The presentation is not a test of memorisation — it is a test of whether you can stand by your own work.

### Comparing with a classmate

If you have time on L24 (after the presentations), find a classmate who used the **other** language. Read each other's program. Write 3–5 sentences in plain English on the differences — semicolons everywhere in C# vs. optional in JS, `Console.WriteLine` vs. `console.log`, `int` / `string` vs. `let`, capital first letters in C# method names — and one thing that is the same: the loop and the `if/else` look almost identical on both sides. That last observation is the whole point of having seen both.

---

## How AT3 is assessed

AT3 is **pass / not-yet-pass**. No number grade, no rubric beyond a short checklist.

**You submit:**

- The **source code** (a `.js` or `.cs` file, or a clearly fenced snippet with the right language tag).
- A **screenshot** of the program running with at least one expected output.
- A **3–5 sentence written reflection** naming the one bug you found and the one fix you applied.
- A **2-minute oral presentation** in class on Lesson 24 covering the four beats above.

**The teacher checks four things:**

- The program runs (or your failed attempt is documented with the error message).
- You can name in plain English what the program does.
- One bug-and-fix pair is documented.
- The 2-minute presentation was delivered.

If any of the four is missing, the work is **not yet pass** and the teacher tells you which one to fix. There is no shame in not-yet-pass; it just means there is one more small thing to do.

---

## Summary — closing the loop on the central question

Eight weeks ago this course opened with one question. You have answered it, in pieces, every week since. Now you can answer it whole, in your own words, with a working program in your hand. Here it is one more time — the same wording it has had since Week 1:

> **How do I speak to a computer so that it understands what I want it to do?**

You answer it this week by doing it. You take pseudocode you wrote yourself in Week 6 and translate it into JavaScript or C#. You declare a variable. You write an `if/else`. You write a `for` loop. You press Run. If the computer is unhappy, it prints an error message that points at the one line you got wrong, and you fix that one line. Then you stand up in front of the room and say, in 2 minutes, what your program does and how you fixed the thing that went wrong.

That is programming, at this level. Not magic. Not mystery. A small, careful file of instructions that does exactly what you said. Everything the rest of your education adds — more languages, bigger projects, libraries, frameworks, teamwork — sits on top of this same one thing: a literal computer following instructions you wrote, telling you in plain text when something does not parse.

Programming has stopped being mysterious. Keep your AT3 source file. Open it again in six months. It will look small. That is the point — you wrote it.

Welcome to the other side of the central question.
