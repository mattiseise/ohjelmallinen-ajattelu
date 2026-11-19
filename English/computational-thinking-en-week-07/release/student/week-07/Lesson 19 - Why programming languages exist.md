# Lesson 19 — Why programming languages exist *(language-agnostic — no working code in this lesson)*

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
