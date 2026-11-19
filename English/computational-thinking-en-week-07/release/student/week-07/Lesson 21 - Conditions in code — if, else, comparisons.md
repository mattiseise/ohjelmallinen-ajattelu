# Lesson 21 — Conditions in code: if, else, comparisons *(dual-language; everything side by side)*

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
