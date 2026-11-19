## Slide 1 — Week 8 — Closing the loop

The last week. Open with weight: every step since Week 1 was preparing for this — a small real program, a single bug found and fixed, a short presentation to the room. Tell the class: "Programming stops being mysterious by Friday. You will hold a working program in your hand." Ask the class: "Which Week 6 pseudocode of yours are you thinking of translating?" Let two or three answer. ~2 min.

## Slide 2 — What lands this week

Walk through the three lessons. L22 — loops in code, side by side. L23 — build day, no new material, just translate your pseudocode and run it. L24 — test, fix one bug, present. Read the italic block aloud. Tell the class: "The loop in the title is the course itself — you opened with a question, this week you answer it." Ask the class: "What is your honest worry about AT3?" Listen, no fixing yet. ~3 min.

## Slide 3 — Loops — the shape (JS and C# side by side)

Walk both blocks. `for (let i = 1; i <= 5; i++)` in JS, `for (int i = 1; i <= 5; i++)` in C#. Both print 1, 2, 3, 4, 5. Difference: the type word. Everything else is identical. Tell the class: "This is the WHILE/FOR from Week 6 wearing real-language clothes." Ask the class: "What is the output if we change `i <= 5` to `i < 5`?" Answer: 1, 2, 3, 4. ~3 min.

## Slide 4 — Counter, condition, body, update

Read the four named parts. Counter — i, starts at 1. Condition — i <= 5, checked before every repeat. Body — what runs each time. Update — i++, the +1 between repeats. Read the sentence at the bottom aloud: "Counter from 1, while 5 or below, print the counter, add one." Tell the class: "If you can name the four parts, you can write any for loop." Ask the class: "Where is the update in our slide?" Answer: i++. ~3 min.

## Slide 5 — A `while` loop (JS and C# side by side)

Walk both blocks. `let count = 0;` then `while (count < 3) { console.log("Hello"); count = count + 1; }`. Same in C# with `int`. Both print Hello three times. Stress: use while when "until" is more natural than "repeat N times." Ask the class: "What happens if I delete the `count = count + 1;` line?" Steer to: infinite loop — exactly the next slide. ~3 min.

## Slide 6 — When a loop runs forever

This is the most common loop bug. If the counter never changes, the condition stays true, the body runs forever. In the browser the page hangs and the browser may pop a warning. In dotnetfiddle the run times out after a few seconds. The fix is always: change something in the body that the condition tests. Tell the class: "Every infinite loop is a forgotten update line." Ask the class: "What is the safety belt here?" Steer to: a real update line. ~3 min.

## Slide 7 — From your pseudocode to your program

Lesson 23 is the build day. Nothing new lands. The work is mostly substitution: take 6 to 20 lines of your own Week 6 pseudocode and translate them. Tell the class: "The hard work was done in Week 6. This week is mostly typing carefully." Ask the class: "Which of your Week 6 pseudocodes is between 6 and 20 lines and has an IF or a loop?" That is the one you translate. ~3 min.

## Slide 8 — The translation table

Walk the table row by row. WRITE becomes console.log or Console.WriteLine. SET becomes `let` or `int`. IF becomes `if` with braces. REPEAT N TIMES becomes a for loop. INCREASE x BY 1 becomes `x = x + 1` in both. Tell the class: "This table is enough for everything you wrote in Week 6. Print it, tape it on your laptop." Ask the class: "Which row will you use first in your AT3 translation?" ~3 min.

## Slide 9 — Loop + if/else — password check (JS and C# side by side)

Walk both blocks. A list of three passwords. A for loop running three times. Inside, an if/else testing length >= 8. Tell the class: "Loop, condition, branch — all three Week 5 moves, finally in real code." Note `passwords[i].length` in JS vs `passwords[i].Length` in C# — capital L. Ask the class: "Which of the three passwords prints 'long enough'?" Answer: correcthorse and 12345678. ~3 min.

## Slide 10 — Save, run, see output

Practical demo time. JavaScript: open the browser DevTools console with Cmd+Opt+J or Ctrl+Shift+J, paste, press Enter, save as a .js file. C#: open dotnetfiddle.net, choose Console, paste inside Main, press Run, save as a .cs file. Tell the class: "Take a screenshot of the run. AT3 wants evidence." Ask the class: "Where will you save your AT3 file so you can find it during the presentation?" ~3 min.

## Slide 11 — Reading a real error message (JavaScript)

Read the error aloud as the computer talking: "I do not know what `scre` is." The cause is a typo — `score` declared, then `scre` used. The fix: find `scre`, type the missing `o`, re-run. Tell the class: "The error message is the computer pointing at the bug. Read it like a friend's text." Ask the class: "What does `at <anonymous>:3:15` mean?" Steer to: line 3, column 15 — the location. ~3 min.

## Slide 12 — Reading a real error message (C#)

Same bug in C#: `error CS0103: The name 'scre' does not exist in the current context`. Same fix — correct the spelling. The second example, `error CS1002: ; expected`, is even simpler — add a semicolon at the line the message names. Tell the class: "Every C# error has a code. Search the code and you find a Microsoft page explaining it." Ask the class: "Which is more common in your typing — typos or missing semicolons?" ~3 min.

## Slide 13 — One small fix, one re-run

This is what debugging means in this course. No fancy debugger. No stop-the-program tool. No testing framework. Just: read the message, find the line, change one small thing, run again. Tell the class: "You will do this at least once for AT3. The cycle is the deliverable as much as the fix." Ask the class: "Why is 'change one small thing' important?" Steer to: changing many things at once hides which change actually fixed it. ~3 min.

## Slide 14 — Your 2-minute presentation

Walk the four beats. 30 seconds each. What the program does (plain English). How it does it (variables, if/else, loop). What went wrong (the bug, by name). How you fixed it (the line). Tell the class: "Time it on your phone. Under is fine. Over is not." Ask the class: "Which beat will be hardest for you?" Often the 'how it does it' beat — that is the technical one. ~3 min.

## Slide 15 — Must-do minimum vs. deepening

Set the bar. The minimum: a small program from your own Week 6 pseudocode, two runs, one bug found and fixed, 2-minute presentation. That is enough to pass AT3. Deepening: loop + if/else combo, comparing with a classmate's other-language version, adding input from prompt() or Console.ReadLine(). Ask the class: "What is your minimum plan and what deepening would feel reachable?" ~2 min.

## Slide 16 — Tasks this week (see your language's task file)

Walk the five tasks. Task 8.1 is the AT3 brief — translate your Week 6 pseudocode. Task 8.2 is the loop warm-up: count 1 to 5. The deepening tasks: combine loop and if/else, read a real error message, compare with a classmate. Tell the class: "Open the task file that matches your language." Ask the class: "JS or C# — which file are you opening tonight?" ~2 min.

## Slide 17 — How AT3 is assessed

Read the four checks. The program runs (or there is a documented failed attempt with the error). You can name what it does in plain English. One bug-and-fix pair is documented in your reflection. The 2-minute presentation was delivered on Lesson 24. Pass / not-yet-pass — no number grade. Tell the class: "Honest failure documented well still passes. Hidden failure does not." Ask the class: "Which check feels easiest? Hardest?" ~3 min.

## Slide 18 — Closing the loop — Week 1, one more time

Quote the Week 1 question on the slide. Wait a beat. Tell the class: "You have answered it. Not in theory — with a working program in your hand." Programming has stopped being mysterious. Read the line aloud. Ask the class: "What is the one thing about programming that is less scary now than it was in Week 1?" Let several students answer. ~3 min.

## Slide 19 — Thank you, and what comes next

Close the course. This was the foundation under the programming they will do for the rest of their studies. Keep the AT3 source file. Read it again in six months — it will look small. That is the point. Tell the class: "Welcome to the other side of the central question." Thank them by name if you can. End on time. ~2 min.
