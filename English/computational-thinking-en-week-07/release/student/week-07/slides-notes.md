## Slide 1 — Week 7 — From pseudocode to code

This is the week the training wheels come off. Tell the class: "Today, for the first time, you write something a computer actually runs." JavaScript and C# arrive side by side — not to pick a winner, but to show the thinking is bigger than any one language. Ask the class: "Have you used a browser console before? Anyone touched Visual Studio?" Get a quick read of the room. ~2 min.

## Slide 2 — The central question, one more time

The course's opening question is on the slide again. This week is the answer. Tell the class: "We have been circling this question since Week 1. This week we land on the runway." Ask the class: "What was your best answer to this question after Week 1? After Week 6?" Compare. The Week 7 answer adds: with a real language, in a real browser. ~2 min.

## Slide 3 — What this week trains

Walk through the three lessons. L19 is the *why* — no working code yet, just the idea of a language and its syntax. L20 is the first commands: print, variables, calculations. L21 is decisions: if, else, comparisons. Stress: everything is side-by-side in both languages. Ask the class: "Which lesson sounds most useful for the work you want to do?" ~2 min.

## Slide 4 — Why a programming language?

Read the three lines. Pseudocode was for a human. Real code is for a computer — a literal interpreter of a fixed word list. The thinking stays. The words tighten. Tell the class: "When you were eight, the literal robot in Week 1 needed exact words. The computer is the same robot, only stricter." Ask the class: "What happens when you misspell a function name?" Steer to: the computer stops. ~2 min.

## Slide 5 — What is syntax?

Syntax is *how* the words have to be arranged. English vs. Finnish — different word order, same meaning. A valid file path vs. a path with a space — same characters, different rules. Stress: a computer is not generous; broken syntax produces an exact error message. Tell the class: "Treat errors as the computer pointing at the line. Read it." Ask the class: "What is the syntax of a URL?" Steer to: scheme, slashes, domain, path. ~3 min.

## Slide 6 — Two languages we will meet

JavaScript runs everywhere there is a browser — every laptop and phone in the room can run it without installation. C# runs on .NET — desktop apps, web servers, Unity games. Tell the class: "Pick the one that looks friendlier on the slides. AT3 grade does not care which you pick." Read the italicized definition aloud. Ask the class: "Anyone here played a Unity game?" Often a few hands. ~3 min.

## Slide 7 — Hello, console — side by side

The classic first line. JavaScript: `console.log("Hello, console");` writes one line to the browser console. C#: `Console.WriteLine("Hello, console");` writes one line to the run window. Same job: print one line. Different words: `console.log` vs. `Console.WriteLine`. Stress: capital C, capital W in C#. Punctuation matters. Ask the class: "Which one looks more like English to you?" No wrong answer. ~3 min.

## Slide 8 — Opening the browser console (JavaScript)

Live demo time. Open Chrome or Firefox on the projector. Press the shortcut — Cmd+Opt+J on Mac, Ctrl+Shift+J on Windows. The console opens. Paste `console.log("Hello, console");` and press Enter. The text appears. Tell the class: "That is your JavaScript runtime. It is built into every browser you own." Ask the class: "Which browser are you going to try this in tonight?" ~3 min.

## Slide 9 — Opening an online C# environment

For C#, the path is the web. Open dotnetfiddle.net. Choose Console at the top. The template appears. Paste the code inside `Main`, click Run, see the output at the bottom. No account, no install. Mention sharplab.io and Replit as alternatives. Tell the class: "You do not need Visual Studio for this course." Ask the class: "What if dotnetfiddle is blocked at home?" Have a backup like sharplab. ~3 min.

## Slide 10 — Variables — side by side

Read the JS block: `let name = "Lyra";` puts the text "Lyra" into a container called name. `let age = 16;` puts the number 16 into age. `console.log(age);` prints 16. C# does the same with type words: `string name`, `int age`. Tell the class: C# names the type explicitly; JavaScript figures it out. One extra word, same thinking. Ask the class: "What is a `string`? What is an `int`?" Steer to: text and whole number. ~3 min.

## Slide 11 — A first calculation — side by side

Walk both blocks. Make a variable age = 16. Make a new variable years = 18 - age. Print years. The output is 2. Tell the class: "The arithmetic is identical. The only difference is the word that introduces the variable — `let` vs. `int`." Ask the class: "What is the output if age = 22?" Wait for someone to say -4. Then discuss whether that makes sense for the problem. ~3 min.

## Slide 12 — Predict before you run

This is the debugging discipline. Before clicking Run, write what you expect. Then run. Compare. The line where prediction and reality first diverge is the bug. Tell the class: "This is Week 6's dry run, now on code that actually runs." Ask the class: "Why is it better to predict first instead of just running and reading?" Steer to: running first hides which line is wrong. ~3 min.

## Slide 13 — Comparison operators

Read the table. `==` equal. `!=` not equal. `>`, `>=`, `<`, `<=`. Same in JavaScript and C#. Tell the class: "Pay attention — `=` is assignment, `==` is comparison. One equals sign puts a value in; two equals signs ask a question." This is the most common beginner mistake. Ask the class: "What does `age = 18` do? What does `age == 18` do?" One sets, one tests. ~3 min.

## Slide 14 — First if/else — side by side (age-limit check)

Walk both blocks. `let age = 16;`, `if (age >= 18) { console.log("You may enter."); } else { console.log("Sorry, not yet."); }`. C# is nearly identical — same `if`, same `>=`, same `else`, same braces. Tell the class: "Once you see the shape, both languages disappear into the same thinking." Ask the class: "What is the output? What if we change age to 21?" ~3 min.

## Slide 15 — Tasks this week

Walk the structure. One must-do task in your chosen language — print, declare, calculate, if/else. Then two or three deepening tasks: do the same in the other language, translate Week 6 pseudocode, break it on purpose. Stress: AT3 lands at the end of Week 8 and will reuse this code. Save everything. Ask the class: "Which language are you trying first?" ~2 min.

## Slide 16 — Picking your language for AT3

Be reassuring. Pick the one that looks less scary on the side-by-side slides. You can swap any time before AT3. Grade does not depend on choice. No installation needed — browser console for JS, .NET Fiddle for C#. Tell the class: "There is no wrong answer. Both languages are real and used at real jobs." Ask the class: "What might tip you toward C# instead of JS?" Steer to: Unity games, .NET shops, type clarity. ~2 min.

## Slide 17 — What comes next — Week 8

Preview the finale. Loops in code — Week 6's WHILE and FOR get real `while` and `for`. Real error messages as a learning tool. AT3 — translate one of your own Week 6 pseudocode pieces into a running program. Tell the class: "Week 8 is the closing of the loop. Programming stops being mysterious by Friday." Ask the class: "Which Week 6 pseudocode of yours do you already want to translate?" ~2 min.

## Slide 18 — Recap — the central question, one more time

End where the course began. "How do I speak to a computer?" Answer: with a programming language — JavaScript or C#, side by side, with no installation. Tell the class: "The thinking is the thing. The syntax is the deal." Ask the class one final time: "What did you write today that a computer actually ran?" Someone will mention console.log or WriteLine. End on time. ~1 min.
