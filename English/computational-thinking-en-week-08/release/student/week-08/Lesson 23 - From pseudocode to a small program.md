# Lesson 23 — From pseudocode to a small program

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
