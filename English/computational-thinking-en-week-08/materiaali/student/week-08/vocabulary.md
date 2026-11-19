# Vocabulary

## Week 8 vocabulary

The terms below cover Lessons 22, 23 and 24. Definitions are short on purpose — read the self-study for examples in context. Where a term has a different surface in JavaScript and C#, both forms are shown side by side. Several terms at the end are flagged as **course wrap-up — revisited from earlier weeks**; for those, the entry highlights what is new this week.

### Loop

A control structure that runs a block of code several times in a row, with a stopping condition. You met the idea in Week 5 (`REPEAT … UNTIL`) and wrote it in Week 6 pseudocode as `WHILE` and `FOR each`. This week the same idea arrives in real code as `for` and `while` in both JavaScript and C#. A loop is the formal name for the *repeat-until* idea your pseudocode already used.

### `for` *(loop keyword in both JavaScript and C#)*

The loop keyword you use when you know in advance how many times you want the body to run. Both languages write it the same way: `for (start; condition; update) { … body … }`. Example, side by side:

```js
for (let i = 1; i <= 5; i++) { console.log(i); }
```

```csharp
for (int i = 1; i <= 5; i++) { Console.WriteLine(i); }
```

The only difference is `let` in JS versus `int` in C#, and the print command.

### `while` *(loop keyword in both JavaScript and C#)*

The loop keyword you use when you know the *stopping condition* but not the exact number of repeats. Shape: `while (condition) { … body … }`. The condition is checked **before** every repeat; while it is true, the body runs once more. You are responsible for changing something inside the body so the condition eventually becomes false — otherwise the loop runs forever.

### Counter

A small variable, usually called `i` (sometimes `count`), that keeps track of how far a loop has got. The counter starts at some value, the condition tests it, the update changes it. In `for (let i = 1; i <= 5; i++)` the counter is `i`, starting at `1`.

### Condition *(revisited from Week 5; reused in Week 8 inside loops)*

A small expression that is either true or false. You met conditions in Week 5 inside `IF/ELSE`, and you wrote them in code last week with comparison operators (`==`, `>=`, `<`). This week the same conditions also live inside `for` and `while` loops — the loop runs the body **while** the condition is true.

### Body *(of a loop)*

The block of code that runs once per repeat — the part between the curly braces `{ … }` after the loop header. Anything you put in the body happens every time around. The body can contain print commands, assignments, and even an `if/else`.

### Iteration

One run of a loop's body. A `for (let i = 1; i <= 5; i++) { … }` loop has five iterations, because the body runs five times. The word *iteration* is just the formal name for "one repeat".

### Infinite loop

A loop whose condition never becomes false, so the body keeps running forever. The most common cause is forgetting the update step (the counter never changes). In the browser console you will see output stream by until the page hangs; in `dotnetfiddle.net` the run will time out after a few seconds. The fix is to make sure something inside the body changes the value the condition is testing.

### Source code

The text of the program you wrote, before it is run — the contents of a `.js` file (for JavaScript) or a `.cs` file (for C#). Source code is what you submit for AT3. It is human-readable. The interpreter or compiler reads it and either runs it or prints an error.

### Run *(a program)*

To make the computer execute the source code you wrote. In JavaScript you run code by pasting it into the browser's DevTools console and pressing Enter; in C# you press the **Run** button in .NET Fiddle. After you run a program, you read its **output** (or its **error message**).

### Error message

The text the computer prints when it cannot make sense of your code. The message names what went wrong (often a missing word, a misspelled name, a missing semicolon) and points at the line that caused it. Example: `ReferenceError: scre is not defined` (JS) or `CS0103: The name 'scre' does not exist in the current context` (C#). Error messages are not failures; they are the computer telling you where to look.

### Bug

A line in your source code that makes the program either crash with an error message or print the wrong output. Bugs at this course's level are almost always small — a typo, a missing semicolon, a `=` where a `==` belongs. A bug is **in your code**, not in the computer.

### Fix

The one small change you make to the source code to make a bug go away. A fix is typically one character (add an `o` to `scre`), one symbol (change `=` to `==`), or one keystroke (add a missing `;`). After applying the fix you re-run the program and check the new output.

### Test *(revisited from Week 1; reused in Week 8 on a real program)*

Running a program by hand with at least two different starting values and checking that the output makes sense each time. In Week 1 you "tested" an instruction by handing it to a literal follower; this week you test a program by changing one number or string at the top and pressing Run. No automatic testing tool is used.

### Presentation

A short, spoken explanation of your program — what it does, how it does it, what went wrong, how you fixed it. For AT3 the presentation is **2 minutes** long and is delivered in class on Lesson 24. The presentation is the **oral component** of AT3.

### Concatenation

The action of joining two pieces of text (or text and a number) into one piece of text with `+`. `"Hello, " + name` produces `"Hello, Aino"` if `name` is `"Aino"`. Both JavaScript and C# use `+` for this, the same way.

### Algorithm *(course wrap-up — revisited from Week 1)*

A clear sequence of literal steps that gets you from a known input to a known output. You met the word in Week 1 as the everyday name for clear instructions, you wrote algorithms in pseudocode in Week 6, and this week you finally hand one to a real computer in the form of JavaScript or C# source code. The thinking has not changed since Week 1; what changes is who follows the algorithm — first a person, then pseudocode on paper, now a real machine.

### Pseudocode *(course wrap-up — revisited from Week 6)*

The bridge language you wrote in Week 6: more precise than English, less strict than real code. This week pseudocode is the **starting point** for AT3 — you pick one piece of your own Week 6 pseudocode and translate it line by line into JavaScript or C#, using the translation table in the self-study.
