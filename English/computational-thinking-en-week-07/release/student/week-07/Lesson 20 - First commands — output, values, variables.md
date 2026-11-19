# Lesson 20 — First commands: output, values, variables *(dual-language; everything side by side)*

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
