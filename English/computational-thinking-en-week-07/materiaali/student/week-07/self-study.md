# From pseudocode to code — two languages, one way of thinking

## Introduction

Picture last week. You wrote pseudocode for some small task — a tea recipe, an age-limit check, a password-length test. Ten or fifteen lines on paper with `SET`, `IF`, `WHILE`. You drew a trace table and dry-ran it for one normal and one awkward input. By Lesson 18 it did what you expected. A friend could read it. A teacher could mark it. AT2 took it.

Now hand the same piece of paper to a computer.

It would do nothing.

A computer cannot read English-keyword pseudocode any more than it can read your grocery list. It is a literal interpreter of a *specific* set of words, and pseudocode is not in that set. This is the gap Week 7 closes. The course's central question is the same one you have been answering since Week 1:

> **How do I speak to a computer so that it understands what I want it to do?**

The answer this week is **a programming language**. A programming language is a tighter version of the pseudocode you already wrote — tight enough that a real computer can run it without guessing. The *thinking* you have built over six weeks is already there. The *language* is just the syntax it gets written in.

One more move this week: we introduce **two** languages, not one — JavaScript and C# — side by side. Lesson 19 talks about programming languages and syntax in plain English, with no working code. Lessons 20 and 21 show concrete syntax in both languages at the same time. JavaScript runs in your browser's DevTools console. C# runs in **.NET Fiddle**. **No installation is needed for either.** No IDE, no Node.js, no .NET SDK, no debugger, no testing framework.

By the end of the week you will pick one of the two languages, run a first program, declare a variable, and write a first `if/else`. The picking matters: AT3 lands next week, and it will ask you to translate a piece of your own Week-6 pseudocode into a small program in the language you pick this week.

---

## Lesson 19 — Why programming languages exist *(language-agnostic — no working code in this lesson)*

### From pseudocode to code

Last week's pseudocode was already careful. You used a small keyword set, indented blocks, closed every `IF` with an `ENDIF`. Why is that not enough?

It is not enough because *who* pseudocode is for and *who* code is for are different. Pseudocode is for **a human follower** who reads English. Even at its strictest, pseudocode still relies on the reader being a person — a person who knows what "wait" means and what counts as "a number". A computer does not bring any of that. It knows the words it has been built to know, and nothing else. If the words on the page are not in its small list, it stops.

The move from pseudocode to code is not a giant intellectual leap. It is a tightening. We swap your English keywords for the exact words *one specific computer system* will recognise. The thinking — sequence, condition, repetition, variables, input, processing, output — does not change at all.

> **Pause for a moment:** Take one piece of Week-6 pseudocode you wrote. Read it aloud. Notice which lines a stranger could follow only because they are a person — for example, `wait`, `the user enters their age`, `display a friendly message`. Those are exactly the lines that will need a precise, computer-accepted word in real code.

### What is syntax?

**Syntax** is the rule for *how words have to be arranged* so the reader can parse them. Every language has syntax, not just programming languages.

**Example — English vs. Finnish word order.** In English you say "the red car." In Finnish you say "punainen auto." The syntax — the order of adjective and noun — is just a different bargain. If you write "car red" in English, a reader can still guess what you meant, because humans are generous. A computer is not.

**Example — a vending machine.** A vending machine accepts coins of certain shapes and refuses others. If you push a button before inserting a coin, nothing happens. The machine's *syntax* is "coin first, then button". Try it in the other order and you do not get a drink; you get the coin back.

**Example — a file path.** `Users/maria/documents/report.txt` is a valid path. `Users/maria/documents report.txt` (with a space and no slash) is not — and the computer will not say "I think you meant the file in documents." It will say "no such file." The slash is part of the syntax.

A programming language's syntax is exactly this kind of rule, just more of it: which words exist, in what order they may appear, what punctuation has to surround them, what counts as the end of a statement. If your code follows the rules, the computer can run it. If a single comma or quote is in the wrong place, the computer stops and prints an **error message** showing where it got stuck.

This is not a trap. It is the deal. Fix the one place the error message points at, and it will run.

### Interpreter and compiler — one paragraph each, informal

You will meet two words this week for "the thing that reads the code and makes it run": *interpreter* and *compiler*. The difference is not important right now; the names are.

An **interpreter** reads your code one line at a time and runs each line as it goes. JavaScript in the browser is interpreted this way: the browser reads your `console.log("Hello")`, runs it, sees the next line, runs that. There is no separate "make the program first, then run it" step. You write a line, you press Enter, you see the result.

A **compiler** reads your whole program at once, translates it into a lower-level form the computer can run faster, and then runs that translated version. C# works this way: the online environment (or a real .NET tool) compiles your C# code into something else first, and then runs it. From your point of view as a student this week, the difference is mostly invisible — you press the Run button and a moment later you see the output. The main place you will *notice* the difference is in the error messages: a C# error often points at "this won't compile" before it even tries to run, while a JS error often shows up while the code is running.

You do not have to memorise this distinction. Just know the two words; you will see both.

### Two languages, one way of thinking

This course meets two real programming languages, side by side, starting this week.

**JavaScript** (often shortened to **JS**) is the language of the web browser. Every browser you have ever used — Chrome, Firefox, Edge, Safari — has a JavaScript interpreter built in. That interpreter is sitting one keyboard shortcut away from you right now, in the **DevTools console**. JavaScript is used to make web pages interactive (the buttons, the menus, the live updates), and also runs on servers (through a tool called Node.js, which we will not use this week).

**C#** (pronounced "C sharp") is one of the main languages of the **.NET** platform built by Microsoft. C# is used to build desktop applications, web servers, mobile apps and — through a tool called **Unity** — a very large share of the world's video games. You do not need to install .NET this week; the online environment **.NET Fiddle** (at `dotnetfiddle.net`) runs C# code in your browser with no account.

Two languages, two homes, one way of thinking. The thinking — *sequence, condition, repetition, variables, input, processing, output* — is the thing that travels. The syntax is what each language decided to do at the surface.

### Why this matters for an IT professional

You will read more code than you write. Over your career you will probably touch three, four, five different programming languages — because the job changes, the team changes, the project changes. The IT people who get stuck think of themselves as "a JavaScript person" or "a C# person." The IT people who do well treat every new language as a new surface over a familiar floor.

Anchoring your first programming experience in **two** languages on purpose makes that transfer obvious from day one. When you see `console.log("Hello")` next to `Console.WriteLine("Hello")`, two things become unavoidable: yes, the words differ; no, the work the computer is doing is not different. That insight is the most valuable thing Week 7 gives you.

> **Pause for a moment:** Without writing any code yet, write one sentence in your notes that finishes this thought: *"A programming language is needed, not just pseudocode, because…"* — answer in your own words. Then read the answer back. If it mentions the word *computer* somewhere, you have probably got it.

---

## Lesson 20 — First commands: output, values, variables *(dual-language; everything side by side)*

This is the lesson where you write your first real code. Everything below appears twice — once in JavaScript, once in C#. Pick one language to actually run, but read both — the side-by-side is the lesson.

### Output: speaking to the console

The smallest possible program is one that prints text. In pseudocode last week you wrote `WRITE "Hello"`. Here is the same line in each language.

#### JavaScript

```javascript
console.log("Hello, console");
```

#### C#

```csharp
Console.WriteLine("Hello, console");
```

Read the two lines next to each other. In JavaScript the printing function is called `console.log`. In C# it is called `Console.WriteLine`. Both take one piece of text in quotes and print it to the console. Both end with a semicolon `;`. (JavaScript does not strictly *require* the semicolon — it is lenient — but we keep it in every example for parallelism with C#. C# does require it; forgetting one is a compile error.)

To run the JavaScript version: open your browser, press `Cmd+Opt+J` on a Mac or `Ctrl+Shift+J` on Windows / Linux (or right-click anywhere on the page, choose **Inspect**, then click the **Console** tab). Paste the line in, press Enter, read the output.

To run the C# version: open `dotnetfiddle.net` in your browser. Choose "Console" at the top. Paste the line into the editor inside the `Main` method (the template gives you one). Press the Run button. The output appears in the lower box.

Two different environments, two slightly different words, the same one job: print one line.

### Variables: naming a value

Last week you wrote `SET passwordLength TO 7`. In a real language, the equivalent is **declaring a variable** and **assigning** it a value.

#### JavaScript

```javascript
let name = "Lyra";
let age = 16;
console.log(name);
console.log(age);
```

#### C#

```csharp
string name = "Lyra";
int age = 16;
Console.WriteLine(name);
Console.WriteLine(age);
```

Same idea on both sides: make a labelled container, put a value in it, then print the value. The differences are at the surface.

In JavaScript you write `let` in front of every new variable. You do **not** tell JavaScript what kind of value goes in — JavaScript figures that out from the value itself (`"Lyra"` is text, `16` is a number).

In C# you write the **type** of the value first: `string` for text, `int` for a whole number. C# wants you to commit upfront to what kind of thing the variable will hold. This is not a different way of thinking — it is one extra word. The word *type* will become important later in your studies; for this week, just write `string` when the value is text and `int` when it is a whole number, and that is enough.

Both languages use `=` for assignment — the same symbol pseudocode used in `SET x TO 7` (just written differently). And both languages let you print a variable by passing its name to the print function — no quotes around the variable name, because you are asking for the value *inside* the box, not for the word "name".

> **Pause for a moment:** Look at the two snippets above. Which line shapes do you find easier to read at first glance — JavaScript's `let name = "Lyra";` or C#'s `string name = "Lyra";`? There is no right answer; pay attention to your honest reaction, because it is a hint at which language to pick for this week's tasks.

### A first calculation

Last week's pseudocode used assignments like `SET total TO unitPrice * quantity`. Real languages do the same; the arithmetic operators (`+`, `-`, `*`, `/`) are the same on both sides.

The running example for the rest of the week is: **how many years until you turn 18?** Given an age, compute `18 - age` and print the result.

#### JavaScript

```javascript
let age = 16;
let yearsToAdulthood = 18 - age;
console.log("Years until you turn 18:");
console.log(yearsToAdulthood);
```

#### C#

```csharp
int age = 16;
int yearsToAdulthood = 18 - age;
Console.WriteLine("Years until you turn 18:");
Console.WriteLine(yearsToAdulthood);
```

Read these together. The algorithm is identical: *make age, compute the difference, print a label, print the result.* The words are different — `let` vs `int`, `console.log` vs `Console.WriteLine` — but the steps line up one-for-one. Change `age = 16` to your real age, run it, and the program tells you how many years until you turn 18.

You can also combine the label and the number into a single line, by joining text and numbers with `+`. Both languages let you do this:

#### JavaScript

```javascript
let age = 16;
console.log("You have " + (18 - age) + " years to go.");
```

#### C#

```csharp
int age = 16;
Console.WriteLine("You have " + (18 - age) + " years to go.");
```

Notice that the `+` between text and a number is the *same operator symbol* in both languages — what it does is glue the pieces together into one piece of text. The word for this is **concatenation**. C# also has a tidier form called **string interpolation** (`$"You have {18 - age} years to go."`) and JavaScript has a similar form called a **template literal**; both are optional this week and are listed in the vocabulary as "looking ahead."

### Reading the output

This week the only debugging tool you have is *reading the output*. There is no breakpoint, no step-through debugger, no test framework. If the program prints what you expected, it worked. If it prints something else, the difference between expected and actual is the bug — and it is a bug *in your code*, exactly the way Week 6 trained you to look.

If nothing appears at all, the program did not reach the print line. Maybe it stopped earlier with an error message; maybe you ran the wrong file; maybe you forgot to press Run. Read the error message if there is one — the interpreter or compiler usually points right at the problem.

### The thinking is the same

Here is the side-by-side summary. Both programs do this:

1. Make a variable called `age` and put a number in it.
2. Make a variable called `yearsToAdulthood` and put `18 - age` in it.
3. Print a label.
4. Print the value.

That is the algorithm. It is identical in JavaScript and identical in C#. The differences (`let` vs `int`, `console.log` vs `Console.WriteLine`, semicolons mandatory vs by-convention) are the **syntax**. The syntax is the deal you strike with one specific computer. The thinking is the thing.

> **Pause for a moment:** If you swapped the two snippets — wrote the JavaScript code into .NET Fiddle, or the C# code into the browser console — what do you think would happen? Try it. The error you get is the language telling you "this is not my syntax." Read what it says.

---

## Lesson 21 — Conditions in code: if, else, comparisons *(dual-language; everything side by side)*

### From pseudocode IF/ELSE to code if/else

Bring forward a piece of pseudocode you have seen many times now — the age-limit check:

```text
READ age
IF age >= 18 THEN
  WRITE "You may enter."
ELSE
  WRITE "Sorry, you are not old enough."
ENDIF
```

That is the pseudocode shape. Each language writes it slightly differently, but the structure — *test, then-block, else-block* — is exactly the same.

#### JavaScript

```javascript
let age = 16;
if (age >= 18) {
  console.log("You may enter.");
} else {
  console.log("Sorry, you are not old enough.");
}
```

#### C#

```csharp
int age = 16;
if (age >= 18)
{
    Console.WriteLine("You may enter.");
}
else
{
    Console.WriteLine("Sorry, you are not old enough.");
}
```

The two snippets are almost identical. Both use the keyword `if`, both put the test in round brackets `( ... )`, both wrap each branch in curly braces `{ ... }`, both use the keyword `else`. The only surface differences are the print function and the type word `int`. The curly-brace formatting in C# is conventionally on a new line; in JS it is conventionally on the same line as `if`. This is style, not rules.

### Comparison operators

Inside the brackets after `if`, you write a **comparison**. A comparison is a small expression that is either *true* or *false* — the same yes/no test you wrote in Week 5 and Week 6, just in symbols. The good news: the operators are essentially the same in JavaScript and C#.

| Operator | Meaning                      | Example (JS or C#)   |
|----------|------------------------------|----------------------|
| `==`     | equal to                     | `age == 18`          |
| `!=`     | not equal to                 | `age != 18`          |
| `>`      | greater than                 | `age > 18`           |
| `>=`     | greater than or equal to     | `age >= 18`          |
| `<`      | less than                    | `age < 18`           |
| `<=`     | less than or equal to        | `age <= 18`          |

One small extra note about JavaScript: it also has `===` (three equals signs) which is called **strict equality**. For everything we do this week, either `==` or `===` works the same way; both are fine. Use whichever feels natural and keep going. (You will meet the subtlety later in your studies; it does not change anything this week.)

A comparison on its own can also be put into a variable. The value of a comparison is **boolean** — either `true` or `false`. Both languages use the words `true` and `false` (lowercase) for this.

#### JavaScript

```javascript
let age = 16;
let isAdult = age >= 18;
console.log(isAdult);
```

#### C#

```csharp
int age = 16;
bool isAdult = age >= 18;
Console.WriteLine(isAdult);
```

C# names the type (`bool`); JavaScript figures it out from the value. Same idea, one extra word in C#.

### Putting it together — the age-limit check

Now combine everything from Lessons 20 and 21 in one small program. We declare an age, compute a comparison, branch on it, and print one of two messages. This is the program you will save in your notes — AT3 will reuse it.

#### JavaScript

```javascript
let age = 16;
if (age >= 18) {
  console.log("You may enter.");
  console.log("Welcome!");
} else {
  let yearsToGo = 18 - age;
  console.log("Sorry, you are not old enough.");
  console.log("Come back in " + yearsToGo + " years.");
}
```

#### C#

```csharp
int age = 16;
if (age >= 18)
{
    Console.WriteLine("You may enter.");
    Console.WriteLine("Welcome!");
}
else
{
    int yearsToGo = 18 - age;
    Console.WriteLine("Sorry, you are not old enough.");
    Console.WriteLine("Come back in " + yearsToGo + " years.");
}
```

Line by line, the two programs match. The differences are exactly the differences you already named: `let` vs `int`, `console.log` vs `Console.WriteLine`, brace placement. Everything else — the `if`, the `>=`, the `else`, the curly braces, the assignment — is the same.

### Predict before you run

This is the same move you trained in Week 6. **Before** you click Run, read each line, predict the output, write the prediction down. Then run, and compare prediction with reality.

For the program above, with `age = 16`, the prediction is:

```text
Sorry, you are not old enough.
Come back in 2 years.
```

Run the program. Did you get exactly that? If yes, your dry-run habit from Week 6 is now your dry-run habit in code, and that is the most valuable transfer of the week. If no, the line where prediction and reality first diverged is the line to look at.

Then change `age = 16` to `age = 19`, predict again, and run again. The output should change to the *other* branch. If both runs match your predictions, the program is doing what you wrote.

> **Pause for a moment:** Look at the `if/else` block above and at the pseudocode at the top of this lesson. Take a pen and circle, on paper, the parts that *literally are the same words* in pseudocode and in your chosen real language. The number of circles will surprise you. The remaining bits are the syntax; the circles are the thinking.

---

## Picking your language for AT3

AT3 lands at the **end of Week 8**. It will ask you to take one piece of your own Week-6 pseudocode that contains an `IF/ELSE` and turn it into a small program that actually runs — in the language of your choice. You will hand in the original pseudocode, the program, a sentence about which Week-6 piece you picked and why, and a screenshot of the output for two inputs (one normal, one awkward).

**Pick your language this week.** The recommendation is: pick the one that looks less scary when you read this self-study. If `console.log("...")` looks more readable to you, pick JavaScript. If `Console.WriteLine("...")` and the named types `string` / `int` feel more like the careful pseudocode you got used to in Week 6, pick C#. You can swap any time before AT3 is due, but it is much easier to swap early than late.

**The grade does not depend on which language you pick.** It depends on the thinking — on whether your program does the same job as your pseudocode, and on whether you can talk about it line by line.

A short reminder, in case you forget: **no installation is needed for either language**. JavaScript runs in your browser's DevTools console (`Ctrl+Shift+J` / `Cmd+Opt+J`). C# runs in **.NET Fiddle** at `dotnetfiddle.net`, with no account.

---

## Summary and what comes next

**Central message for this week:** *A programming language is a way to make instructions precise enough for a computer to follow without guessing. The thinking is what we have been doing all course; the language is just the syntax it gets written in.*

This week you crossed the bridge. You met two real programming languages — JavaScript and C# — and you saw them next to each other on every concept: output, variables, calculation, comparison, `if/else`. You wrote a first program in your chosen language. You ran it, predicted before you ran it, and read the output the way Week 6 trained you to read a trace table.

**Week 8** finishes the course. It brings in **loops** in code — the `WHILE` and `FOR` you already know from Week-6 pseudocode, now in JavaScript and C#. It introduces real **error messages** as a learning tool (you broke the program; what did the computer say?). And it lands **AT3** — your translation of one Week-6 pseudocode snippet into a small running program. Everything you wrote this week is the foundation; keep your code saved.

The central question one more time — and read it aloud, because in Week 8 you finally get to answer it with a program that does exactly what you said:

> *How do I speak to a computer so that it understands what I want it to do?*
