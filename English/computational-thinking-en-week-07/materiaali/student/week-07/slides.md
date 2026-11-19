# Week 7 — From pseudocode to code

Computational Thinking

A first-year vocational ICT course

Two languages, one way of thinking — JavaScript and C# side by side.

---

## The central question, one more time

How do I speak to a computer so that it understands what I want it to do?

This week we finally answer it — in code.

---

## What this week trains

- Lesson 19 — **why** a programming language exists, and what *syntax* means (no working code yet)
- Lesson 20 — first commands in **JavaScript and C#** side by side: output, values, variables
- Lesson 21 — first decisions in **JavaScript and C#** side by side: `if`, `else`, comparisons

---

## Why a programming language?

Pseudocode is for a **human follower** who reads English.

Real code is for a **computer**: a literal interpreter of a fixed word list.

The thinking is the same. The words tighten.

---

## What is syntax?

The rule for *how words have to be arranged* so the reader can parse them.

- Everyday: in English we say "the red car"; in Finnish "punainen auto" — different word order.
- IT: `Users/maria/documents/report.txt` is a valid path; the same with a space and no slash is not.

A computer is not generous. If the syntax is broken it stops and says where.

---

## Two languages we will meet

- **JavaScript** — runs in every browser (Chrome, Firefox, Edge, Safari). Web pages, Node.js servers.
- **C#** — runs on .NET. Desktop apps, web servers, games (Unity).

You will see both, every concept, side by side.

> *A programming language is a way to make instructions precise enough for a computer to follow without guessing. The thinking is what we have been doing all course; the language is just the syntax it gets written in.*

---

## Hello, console — side by side

#### JavaScript

```javascript
console.log("Hello, console");
```

#### C#

```csharp
Console.WriteLine("Hello, console");
```

Same job — print one line. Different words, same idea.

---

## Opening the browser console (JavaScript)

- Mac: `Cmd + Opt + J`
- Windows / Linux: `Ctrl + Shift + J`
- Or: right-click → **Inspect** → **Console** tab

Paste a line of JavaScript, press Enter, read the output.

---

## Opening an online C# environment

- Go to **`dotnetfiddle.net`** in any browser.
- Choose **Console** at the top.
- Paste C# code inside the `Main` method, press **Run**.

No account, no install. `sharplab.io` and Replit also work.

---

## Variables — side by side

#### JavaScript

```javascript
let name = "Lyra";
let age = 16;
console.log(age);
```

#### C#

```csharp
string name = "Lyra";
int age = 16;
Console.WriteLine(age);
```

C# names the type (`string`, `int`); JavaScript figures it out. One extra word, same thinking.

---

## A first calculation — side by side

#### JavaScript

```javascript
let age = 16;
let years = 18 - age;
console.log(years);
```

#### C#

```csharp
int age = 16;
int years = 18 - age;
Console.WriteLine(years);
```

The algorithm is identical: *make age, compute the difference, print the result.*

---

## Predict before you run

Look at each line. **Before** clicking Run, write what you expect.

Then run it. Compare prediction with reality.

If they disagree, the line where they first differ is your bug.

This is Week 6's dry-running, now on code.

---

## Comparison operators

| Operator | Meaning              |
|----------|----------------------|
| `==`     | equal to             |
| `!=`     | not equal to         |
| `>`      | greater than         |
| `>=`     | greater than or equal |
| `<`      | less than            |
| `<=`     | less than or equal   |

Essentially identical in JavaScript and C#.

---

## First if/else — side by side (age-limit check)

#### JavaScript

```javascript
let age = 16;
if (age >= 18) {
  console.log("You may enter.");
} else {
  console.log("Sorry, not yet.");
}
```

#### C#

```csharp
int age = 16;
if (age >= 18) {
    Console.WriteLine("You may enter.");
} else {
    Console.WriteLine("Sorry, not yet.");
}
```

Same `if`, same `>=`, same `else`, same curly braces. The thinking is what carries.

---

## Tasks this week

- **One** must-do minimum task in your chosen language — print, declare, calculate, `if/else`.
- 2–3 deepening tasks: do it in the other language; translate Week-6 pseudocode; break it on purpose.
- See `student-tasks-js.md` and `student-tasks-csharp.md`.

Save your code — **AT3 lands at the end of Week 8** and will reuse it.

---

## Picking your language for AT3

- Pick the one that looks less scary on the side-by-side slides.
- You can swap any time.
- AT3 grade does not depend on which language you pick.
- No installation needed: browser console (JS) or .NET Fiddle (C#).

---

## What comes next — Week 8

- **Loops** in code — Week-6 `WHILE` / `FOR` arrive as `while` / `for`, side by side.
- **Real error messages** as a learning tool.
- **AT3** — translate one piece of your own Week-6 pseudocode into a small running program.

---

## Recap — the central question, one more time

How do I speak to a computer so that it understands what I want it to do?

This week: **with a programming language** — JavaScript or C#, side by side, with no installation.

The thinking is the thing. The syntax is the deal.
