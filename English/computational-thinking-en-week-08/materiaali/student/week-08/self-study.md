# Closing the loop — your first real program

## Introduction

You have arrived at the last week of the course. Eight weeks ago, the very first lesson posed one question, and you have been working towards answering it ever since:

> **How do I speak to a computer so that it understands what I want it to do?**

For seven weeks the answer came in pieces. In Week 1 a computer was a literal follower. In Week 2 you learned to break a task into smaller pieces. Weeks 3 and 4 named the building blocks: input, processing, output; sequence, alternative, repetition. Week 5 introduced precise conditions. Week 6 was pseudocode — the moment your instructions stopped being merely careful and started looking like real code. Week 7 finally crossed the bridge into JavaScript and C#: print, variables, `if/else`.

This week the answer becomes concrete. You write a small program in your chosen language — JavaScript or C# — and run it on a real machine. You pick what the program does from your own **Week 6 pseudocode**. You run it with two starting values. You break it (on purpose or by accident), read the error message, and fix one line. And on Lesson 24 you give a **2-minute** oral presentation: what it does, how, what went wrong, how you fixed it. That is **AT3**.

**Central message for this week:** *The course closes the loop: you take pseudocode you wrote yourself in Week 6, translate it into JavaScript or C#, run it, find one bug, fix it, and explain how it works. Programming has stopped being mysterious.*

Both languages are first-class this week, as in Week 7. Every example appears once in JavaScript and once in C#, side by side. Read your chosen language's column first, but glance at the other — the *shape* of the code is almost the same, and noticing that is half the point.

---

## Lesson 22 — Loops in code

### Why loops exist

In Week 5 you wrote your first *repeat-until* sentences (`REPEAT … UNTIL the password is long enough`), and in Week 6 you wrote pseudocode loops in similar shapes — `WHILE password is too short DO …`, `FOR each item in the list DO …`. They were already loops. The only thing missing was a computer that could read them.

A **loop** is the formal name for the *repeat-until* idea your pseudocode already used — only now the computer, not a human, is doing the repeating. The thinking is identical. What changes this week is the syntax: a small fixed shape JavaScript and C# both accept, with four named parts you can point at. The computer needs three things to loop: *Where do I start? When do I stop? What do I change between each repeat?* A loop is the place those three answers live in one tidy block.

> **Pause for a moment:** Find one Week 6 pseudocode page where you wrote `WHILE`, `REPEAT`, or `FOR each`. Read it. Write down, in your own words, what is repeating and what makes the repetition stop. Those two answers are exactly what a `for` or `while` loop will need.

### The shape of a `for` loop

The most useful loop for this week is the **`for` loop**. Use it when you know in advance how many times you want the body to run — for example, "print the numbers 1 to 5", or "say hello three times". Here is the same simple counter in both languages.

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

Both programs print:

```text
1
2
3
4
5
```

The two snippets are almost identical. Both use the keyword `for`, three small pieces in round brackets separated by semicolons, and a curly-brace body. The only surface differences are exactly the ones from Week 7: `let` vs `int`, and `console.log` vs `Console.WriteLine`.

### Counter, condition, body, update

Inside the brackets of a `for` loop, there are three small pieces. Add the curly-brace block after, and a `for` loop has four named parts:

- **Counter** — a small variable, usually called `i`, that keeps track of how far the loop has got. In the snippet above the counter starts at `1`.
- **Condition** — a yes/no test that runs *before* every repeat. While the condition is true, the loop runs the body once more. The condition above is `i <= 5` — "while the counter is still 5 or below, keep going".
- **Body** — the curly-brace block. Anything you write in here happens once per repeat. The body above is just `console.log(i);` (or `Console.WriteLine(i);`), so each repeat prints the current counter.
- **Update** — what changes between each repeat. Usually it adds one to the counter. The update above is `i++`, which is short for "increase `i` by one".

Read the loop out loud once: "**Counter** starts at 1. **Condition**: while the counter is 5 or below. **Body**: print the counter. **Update**: add one to the counter." Both languages let you read it in exactly that order.

If the counter never changes — if you forgot the `i++` — the condition stays true forever and the loop never stops. That is a bug called an **infinite loop**, and we will name it in a moment.

### The shape of a `while` loop

`for` is the loop you use when you know how many times. **`while`** is the loop you use when you know the *stopping condition* but not the exact number of repeats — "keep asking until the password is long enough", "keep going while there is still tea in the cup". The shape is even simpler than `for`: just a condition in brackets and a body in braces.

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

Both programs print:

```text
Hello
Hello
Hello
```

Read the while loop in plain English: "while `count` is less than 3, print `Hello`, then add one to `count`." Notice that the counter (`count`), the condition (`count < 3`), the body (`console.log("Hello")`) and the update (`count = count + 1`) are all still there — they are just spread out across the loop rather than packed into the brackets. A `while` loop is a `for` loop with the four parts moved around for legibility.

A small trade-off: `while` is more flexible, but you have to remember to update the counter yourself inside the body. A `for` loop puts the update in the brackets where it is hard to forget. Most of this week's programs are happier as `for` loops; reach for `while` only when "until" is more natural than "repeat N times".

### When a loop runs forever

An **infinite loop** is a loop whose condition never becomes false, so the body keeps running and the program never ends. It happens most often when you forget the update step.

```js
let count = 0;
while (count < 3) {
  console.log("Hello");
  // missing: count = count + 1;
}
```

```csharp
int count = 0;
while (count < 3) {
    Console.WriteLine("Hello");
    // missing: count = count + 1;
}
```

In the browser console you will see output stream by until the page hangs; in .NET Fiddle the run will time out after a few seconds with a message like *"The process was terminated"*. Neither is dangerous — close the tab if you need to — but the *fix* is the same in both languages: make sure something inside the body changes the value the condition is checking.

If your program seems to hang the first time you run it, the most likely cause is exactly this: a loop whose counter never updates.

> **Pause for a moment:** Look at the `for` loop above (counter from 1 to 5). What would happen if you changed `i++` to `i--`? Without running it, predict the output. Then mentally trace: does the condition `i <= 5` ever become false? If not, what kind of bug is that?

---

## Lesson 23 — From pseudocode to a small program

The build day. No new concept lands. You translate one piece of your own Week 6 pseudocode, line by line, into JavaScript or C#. The thinking has been done; the work is mostly substitution.

### Pick one piece of your Week 6 pseudocode

Open your Week 6 notes. Pick **one** snippet — age-limit check, password-length check, points-to-feedback, a counter, a greeting. The sweet spot is **6 to 20 lines**. If your favourite is bigger, pick *one part* of it that does one clear job from start to finish.

If you cannot find a piece of Week 6 pseudocode (or you lost the page), pick one of these fallback templates and adapt the values to your own context:

- **Age-limit check.** Set an age; if it is 18 or above print "allowed"; otherwise print "not allowed".
- **Password-length check.** Set a password; if it is 8 characters or more print "strong enough"; otherwise print "too short".
- **Points to feedback.** Set a score; if it is 80 or above print "great work"; if 50 or above print "you passed"; otherwise print "try again".
- **Simple counter.** Print the numbers 1 to 5 using a `for` loop.
- **Greeting by name.** Set a name; use a `for` loop to print "Hello, NAME" three times.

### The translation table

Most pseudocode lines have one clear shape in JavaScript and C#. Memorising this small table makes Lesson 23 almost mechanical.

| Pseudocode pattern              | JavaScript                                    | C#                                                |
|---------------------------------|-----------------------------------------------|---------------------------------------------------|
| `WRITE "Hello"`                 | `console.log("Hello");`                       | `Console.WriteLine("Hello");`                     |
| `SET x TO 5`                    | `let x = 5;`                                  | `int x = 5;`                                      |
| `SET name TO "Aino"`            | `let name = "Aino";`                          | `string name = "Aino";`                           |
| `IF x >= 18 THEN … ELSE …`      | `if (x >= 18) { … } else { … }`               | `if (x >= 18) { … } else { … }`                   |
| `REPEAT N TIMES`                | `for (let i = 0; i < N; i++) { … }`           | `for (int i = 0; i < N; i++) { … }`               |
| `WHILE x < 3 DO …`              | `while (x < 3) { … }`                         | `while (x < 3) { … }`                             |
| `INCREASE x BY 1`               | `x = x + 1;`  *(or `x++;`)*                   | `x = x + 1;`  *(or `x++;`)*                       |
| `IF x EQUALS 5 THEN …`          | `if (x === 5) { … }`  *(or `==`)*             | `if (x == 5) { … }`                               |

That is enough to translate everything you wrote in Week 6. The structure was already there; the table just gives you the right surface words for one specific language.

### Two worked examples — side by side

**Age-limit check.** *Week 6 pseudocode: set age to 17; if age is 18 or more, print "allowed", else print "not allowed".*

#### JavaScript

```js
let age = 17;
if (age >= 18) {
  console.log("allowed");
} else {
  console.log("not allowed");
}
```

#### C#

```csharp
int age = 17;
if (age >= 18) {
    Console.WriteLine("allowed");
} else {
    Console.WriteLine("not allowed");
}
```

Both print `not allowed`. Change `17` to `19` and both print `allowed`. The two snippets are line-for-line equivalent.

**Greeting by name (loop plus a variable).** *Week 6 pseudocode: repeat 3 times: print "Hello, name".*

#### C#

```csharp
string name = "Aino";
for (int i = 0; i < 3; i++) {
    Console.WriteLine("Hello, " + name);
}
```

#### JavaScript

```js
let name = "Aino";
for (let i = 0; i < 3; i++) {
  console.log("Hello, " + name);
}
```

Both print `Hello, Aino` three times. The `+` between text and a variable works the same in both languages — the word for what `+` is doing here is **concatenation**, gluing pieces together into one piece of text.

A common one-character trap to notice now (before Lesson 24's error reading): the **length** of a string is written `name.length` (small l) in JavaScript and `name.Length` (capital L) in C#. Mixing them up is the kind of typo that produces the error messages you will read tomorrow.

### Save, run, see output

**JavaScript — in the browser console:** open any web page; press `Cmd + Opt + J` (Mac) or `Ctrl + Shift + J` (Win/Linux); paste your code, press Enter, read the output. Save the same code as a plain text file with a `.js` extension — that is your **source code** for AT3.

**C# — in an online .NET runner:** open `dotnetfiddle.net`; choose **Console** at the top; paste your code into the `Main` method; press **Run**, read the output. Save the same code as a plain text file with a `.cs` extension — that is your source code for AT3.

Take a **screenshot** of the run with your output visible. That screenshot is one of the AT3 deliverables.

> **Pause for a moment:** Look at the program you just wrote (or are about to write). Read it once, line by line, *out loud*, in plain English. If you can say what each line does without looking at the table, you are ready to present it in 2 minutes on Lesson 24. If you stumble on a line, that is the line to read again before the presentation.

### When the screen is empty or silent

If you run your program and nothing happens, check the boring causes first:

- **Did you actually press Run / Enter?** Most common cause.
- **Did you paste only part of the program?** In .NET Fiddle especially, your code has to be inside the `Main` method.
- **Is there a typo in the print line?** `console.Log` (capital L) is a JavaScript error; in C#, `Console.Writeline` (small `l`) does not exist either — it must be `Console.WriteLine`.
- **Did the program stop earlier with an error?** Scroll up. A red message above the empty space *is* the problem — Lesson 24 teaches you to read these.

If none of those is the cause, add `console.log("got here");` (or `Console.WriteLine("got here");`) near the top. If "got here" prints, the program is running; the missing output is somewhere below.

> **Pause for a moment:** Compare your translated program with the original Week 6 pseudocode. Put them next to each other. Circle the parts of each line that are literally the same — variable names, numbers, keywords like `if`. The number of circles will surprise you. The remaining bits are syntax; the circles are the thinking the course has trained you to do since Week 1.

---

## Lesson 24 — Test, fix one bug, present

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
