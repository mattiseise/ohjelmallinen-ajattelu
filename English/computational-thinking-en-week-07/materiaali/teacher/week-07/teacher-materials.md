# Week 7 — Teacher materials

This document covers all three lessons of Week 7 (L19, L20, L21) in one place. It is built around the same central message the students see: **"A programming language is a way to make instructions precise enough for a computer to follow without guessing. The thinking is what we have been doing all course; the language is just the syntax it gets written in."** Week 7 is the bridge into code. Six weeks of pseudocode, sequence-condition-repetition, decomposition and dry-running meet real syntax for the first time — and in two languages, JavaScript and C#, side by side, not one after the other.

**AT3 is released at the end of Week 8**, not this week. Week 7's job is to make AT3 boring to start: a student who has typed three working lines in their chosen language this week opens the AT3 brief next week and recognises the shape immediately. Every task in `student-tasks-js.md` and `student-tasks-csharp.md` carries an AT3 reminder for this reason.

No real IDE is used. No `node`, no `npm`, no `dotnet new`, no Visual Studio, no VS Code, no JetBrains Rider. JavaScript runs in the browser's DevTools console. C# runs in **.NET Fiddle** (`dotnetfiddle.net`) — sharplab.io and a C#-enabled Replit are acceptable alternatives. No automatic testing or debugging frameworks are used anywhere. The level is *try it, run it, see what happens, read the output*.

Cross-references: the supplementary deck `slides-l21-age-check.md` is used during L21's lecture segment. The mandatory in-class activity *Console relay* is described in `in-class-tasks.md` and belongs in the 55–75 min slot of L20.

---

## Week 7 learning objectives (mapped to Bloom)

Week 7 stays inside **Understanding** and **Applying**. Forbidden verbs for Week 7 objectives: *analyse, evaluate, design, create, build, debug, refactor, optimise*. AT3 in Week 8 is where the Creating-flavoured work lands.

### Lesson 19 — Why programming languages are needed (language-agnostic)

- **Understanding:** the student can **define** *programming language*, *syntax*, *command*, *interpreter* and *compiler* informally in their own words.
- **Understanding:** the student can **explain** why a programming language is needed when pseudocode is already precise — i.e. that a real computer cannot read English-keyword pseudocode.
- **Understanding:** the student can **recognise** that the same algorithm can be written in different languages and still mean the same thing.
- **Understanding:** the student can **name** two real-world programming languages (JavaScript, C#) and one place each is typically used (JS = the browser; C# = .NET, Unity).

### Lesson 20 — First commands: output, values, variables (dual-language)

- **Applying:** the student can **run** a first program that prints text to the console — `console.log("…")` in JavaScript or `Console.WriteLine("…")` in C#.
- **Applying:** the student can **declare** a variable and **assign** it a value — `let` in JS, typed declarations (`int`, `string`) in C#.
- **Applying:** the student can **print** the value of a variable, including by concatenation with `+`.
- **Applying:** the student can **perform** a simple arithmetic calculation (years to adulthood, total price) and print the result.
- **Understanding:** the student can **identify** that the *thinking* — read a value, compute, print — is the same in both languages.

### Lesson 21 — Conditions in code: if, else, comparisons (dual-language)

- **Applying:** the student can **write** a comparison expression (`age >= 18`) in both languages and **recognise** that the comparison operators are essentially identical.
- **Applying:** the student can **write** a first `if/else` block that prints one of two messages depending on a variable.
- **Applying:** the student can **map** a piece of Week-6 pseudocode (`IF age >= 18 THEN … ELSE …`) onto code in their chosen language.
- **Applying:** the student can **predict** the output of a small `if/else` program before running it, then run and check — Week-6 dry-running, now in code.

---

## Common misconceptions for Week 7

At least two misconceptions per lesson. Two touch the JS-vs-C# choice directly, as Week 7 students are deciding which language to take into AT3 and several rumours circulate.

### Lesson 19 misconceptions

**Misconception:** *"Pseudocode is already enough — why do we need code?"*
**Correction:** Pseudocode is for a human follower who reads English. A computer reads only the small word list it was built to know, and pseudocode is not in that list. Code is not "more thinking than pseudocode"; it is the same thinking written in a word list a computer actually accepts.

**Misconception:** *"There is one 'correct' or 'real' programming language and the others are toys."*
**Correction:** Thousands of programming languages exist. JavaScript and C# are two of many. The thinking — sequence, condition, repetition, variables, input, processing, output — transfers across all of them. The language is the surface; the thinking is the floor.

### Lesson 20 misconceptions

**Misconception:** *"C# is harder than JavaScript"* (or the reverse — *"JavaScript isn't a real language because it runs in the browser"*).
**Correction:** Neither statement is true. C# asks you to name the type (`int`, `string`) where JavaScript figures it out from the value; that is one extra word per declaration, not a different way of thinking. JavaScript runs the same kinds of decisions C# does — it just happens to run them in a browser. The thinking transfers in both directions.

**Misconception:** *"`console.log` and `Console.WriteLine` do different things."*
**Correction:** They do the same thing — print one line to the console. The words differ. The job is identical. Showing them side by side on every L20 slide is the antidote.

### Lesson 21 misconceptions

**Misconception:** *"`=` means 'is equal to'."*
**Correction:** `=` is the **assignment** operator — it puts a value into a variable. The **comparison** operator is `==` (and in JavaScript also `===`). This trips students who have only ever seen `=` in maths class. Read `let age = 16;` aloud as *"age takes the value 16"*, not *"age equals 16"*.

**Misconception:** *"`if` is wrong without an `else`."*
**Correction:** `else` is optional. `if (condition) { … }` on its own is valid in both languages. Many real programs use lonely `if`s where there is nothing to do in the "else" case.

---

## Lesson 19 — 90-minute plan

**Topic.** Why programming languages exist. Syntax, commands, interpreters and compilers. Language-agnostic — no working code from students this lesson.

**Central message for this lesson (one sentence).** Pseudocode is precise enough for a human to follow; a programming language is precise enough for a literal computer to follow — same thinking, tighter words.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: put one piece of last week's pseudocode on the board (the age-limit check is ideal). Ask the class: *"Could a computer run this exactly as written?"* Collect three answers. Land on "no, because the words are not in any computer's word list." | Whole class |
| 0:10–0:30 | Instructor input: define *programming language*, *syntax*, *command*, *interpreter*, *compiler* informally. Name JS and C#, name one typical use of each. Show one side-by-side `Hello` teaser slide only — no live coding from the class yet. | Lecture |
| 0:30–1:00 | **Independent work** (30 min): students read the L19 section of `self-study.md` and write 4–6 sentences in their notes answering: *"Why does a programming language need to exist when pseudocode is already precise?"* | Independent |
| 1:00–1:20 | Pair activity: pairs swap answers, find one place they disagree, mark it. Whole-class debrief picks two disagreements off the board. | Pair |
| 1:20–1:28 | Preview L20: show the side-by-side `Hello` slide one more time and tell the class *"next lesson you type these lines yourselves."* Two-minute show-of-hands: who thinks they will pick JS, who thinks C#, who has no idea yet. All answers are fine. | Whole class |
| 1:28–1:30 | Closing. | Whole class |

**Independent-work block: 30 minutes (33% of 90 minutes).** Meets the 30–50% rule.

**Cross-references.** L19 does not use any activity from `in-class-tasks.md` — the mandatory *Console relay* belongs in L20.

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** slide **2** (*The central question, one more time*) on screen as the board carries the live "could the computer run this?" discussion.
- **Lecture (0:10–0:30):** main deck slides **3 → 6**: *What this week trains* · *Why a programming language?* · *What is syntax?* · *Two languages we will meet*. Dwell on slide 5; the syntax definition is the L19 fulcrum.
- **Independent work (0:30–1:00):** leave slide **4** (*Why a programming language?*) on screen as the silent prompt for the writing.
- **Pair activity (1:00–1:20):** no slides; work on paper.
- **Preview L20 (1:20–1:28):** slide **7** (*Hello, console — side by side*) shown briefly as a teaser only.

---

## Lesson 20 — 90-minute plan

**Topic.** First commands in both languages, side by side: output, values, variables, a first calculation. **Dual-language** — both languages run in the room at once.

**Central message for this lesson (one sentence).** A program is a sequence of literal commands; "print a value to the console" is the simplest such command in either language.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: live demo. Open the browser console on one half of the screen and `dotnetfiddle.net` on the other. Print `"Hello, class"` in each. Two lines, two homes, one job. | Whole class |
| 0:10–0:25 | Instructor input: variables, assignment, output. Teacher writes one example in JS, then the same example in C#, on the board next to the screens. Make the parallelism unavoidable. | Lecture |
| 0:25–0:55 | **Independent work** (30 min): every student completes the MANDATORY task in their chosen language (`Your first console program (JS)` or `Your first console program (C#)`). Screenshots in the notes file at the end. | Independent |
| 0:55–1:15 | **MANDATORY teacher-led activity — *Console relay*** (Activity A in `in-class-tasks.md`, ~20 min). Six small snippets (3 JS, 3 C#), shown one at a time on the projector. Each student writes a prediction; the teacher runs the snippet live; the class compares. Language-mixed by design — even a JS-student sees the C# snippets, and vice versa. | Whole class |
| 1:15–1:25 | Whole-class debrief: collect one surprise per language onto a "we saw" board. Connect explicitly to L19's "thinking is portable, syntax is the deal." | Whole class |
| 1:25–1:30 | Closing + preview L21: *"Next lesson, the same side-by-side trick for the `if/else` you have been writing in pseudocode for two weeks."* | Whole class |

**Independent-work block: 30 minutes (33% of 90 minutes).** Meets the 30–50% rule.

**Cross-references.** The 55–75 min slot is **Activity A — *Console relay*** from `in-class-tasks.md`. Prepare the six snippets in advance (the file gives a default set). Activity B from `in-class-tasks.md` is optional and belongs in L21.

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** slides **7** (*Hello, console — side by side*), **8** (*Opening the browser console*) and **9** (*Opening an online C# environment*) in order while the live demo runs on the screens.
- **Lecture (0:10–0:25):** main deck slides **10** (*Variables — side by side*) and **11** (*A first calculation — side by side*). Walk every line on the board next to the slide.
- **Independent work (0:25–0:55):** leave slide **11** on screen as the silent reference for the years-to-adulthood example.
- **In-class activity (0:55–1:15):** slide **12** (*Predict before you run*) on screen during the relay. The snippets themselves live in the live editor, not on a slide.
- **Debrief (1:15–1:25):** no slides; use the "we saw" board.
- **Closing (1:25–1:30):** no slides.

---

## Lesson 21 — 90-minute plan

**Topic.** Conditions in code: `if`, `else`, comparisons, in both languages side by side. The hand-off to AT3.

**Central message for this lesson (one sentence).** `if/else` is the same decision you have been writing in pseudocode for two weeks — only the punctuation is different.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: put the Week-6 age-limit pseudocode on the board. Ask: *"What would this look like in code?"* Take three guesses; do not correct yet. | Whole class |
| 0:10–0:30 | Instructor input: comparison operators on the board (`==`, `!=`, `>=`, `<=`, `>`, `<`); `if/else` block structure. Run the supplementary deck `slides-l21-age-check.md` in full — six short slides walking the age-limit example from pseudocode → JS → C#. | Lecture |
| 0:30–1:00 | **Independent work** (30 min): each student does the *First if/else* deepening task in their chosen language (`First if/else (JS)` or `First if/else (C#)`). Predict, run, screenshot both runs. | Independent |
| 1:00–1:20 | Pair activity — *Translate-your-neighbour* (Activity B in `in-class-tasks.md`, ~20 min). Pair a JS-student with a C#-student. Each translates the other's `if/else` into their own language by hand, no LLM. Compare with the original. | Pair |
| 1:20–1:28 | Hand-off to AT3: *"AT3 is released at the end of Week 8. It asks you to take one piece of your own Week-6 pseudocode and turn it into a running program in the language you picked this week. The task you just did is the dress rehearsal."* | Whole class |
| 1:28–1:30 | Closing: housekeeping; remind students to save everything. | Whole class |

**Independent-work block: 30 minutes (33% of 90 minutes).** Meets the 30–50% rule.

**Cross-references.** The 60–80 min slot is **Activity B — *Translate-your-neighbour*** from `in-class-tasks.md`. The supplementary deck `slides-l21-age-check.md` is used during the lecture segment.

**Slide cues — main deck `slides.md` (and supplementary `slides-l21-age-check.md`).**

- **Warm-up (0:00–0:10):** slide **12** (*Predict before you run*) on screen as the board carries the Week-6 pseudocode.
- **Lecture (0:10–0:30):** main deck slide **13** (*Comparison operators*) for the operator table, then **switch to the supplementary deck `slides-l21-age-check.md` and run it end-to-end** (6 short slides). Return to main deck slide **14** (*First if/else — side by side*) for the close.
- **Independent work (0:30–1:00):** leave main deck slide **14** on screen as the silent reference.
- **Pair activity (1:00–1:20):** no slides; pairs work on paper and screens.
- **AT3 hand-off (1:20–1:28):** main deck slide **17** (*Picking your language for AT3*) for the calm preview.
- **Closing (1:28–1:30):** slide **18** (*Recap — the central question, one more time*) so the class leaves on the verbatim central question.

---

## Facilitation tips

### Tooling — say it out loud once per lesson

**No IDE installation is required.** Students use the **browser DevTools console** for JavaScript and an **online C# environment** (.NET Fiddle by default; sharplab.io or a C#-enabled Replit are acceptable alternatives) for C#. Do not install Node.js, the .NET SDK, Visual Studio or VS Code for this week. If a student turns up with a local install already, that is fine — but the class runs on browsers, and demos should use browsers so every student can follow.

### Managing a language-mixed classroom

- **Let students pick.** Do not push one language. The exit show-of-hands in L19 is a survey, not a sorting hat. Students may swap up to and during L21.
- **Pair JS-students with C#-students** for the L21 pair activity (*Translate-your-neighbour*). The translation is the whole point; same-language pairs miss the lesson.
- **Project the side-by-side slides for every concept.** Never project a single-language slide for a concept that has a side-by-side equivalent. The visual parallelism does half the work.
- **When a student says "C# is harder" (or "JS isn't real"),** redirect with one sentence: *"They are different surfaces over the same thinking — show me where you actually got stuck."* The misconception almost always hides a concrete confusion (a missing semicolon, a missing closing quote) that is one fix away.

### Reading error messages out loud

When the *Console relay* produces an unexpected output or error, **read the error message aloud word for word** before saying anything else. Modelling this in front of the class is the single best Week-7 habit transfer: students who watch a teacher read an error message aloud learn that the message is not random noise; it is the language pointing at the line.

---

## Answers to common student questions

- *"Which language should I pick?"* — Pick the one that looks less scary when you read the side-by-side slides. There is no wrong choice. You can swap any time before AT3 is due, but it is easier to swap earlier than later.
- *"Is one language harder than the other?"* — No. They are different surfaces. C# asks for one extra word (the type, e.g. `int`) at every declaration. JavaScript figures the type out from the value. Neither is harder; they are different.
- *"Will my AT3 grade depend on which language I pick?"* — No. AT3 marks the thinking — whether your program does the job your pseudocode described, and whether you can talk about it line by line. The language is your choice and does not change the marking.
- *"Do I need to install anything?"* — No. JavaScript runs in your browser's DevTools console (`Ctrl+Shift+J` / `Cmd+Opt+J`). C# runs in **.NET Fiddle** at `dotnetfiddle.net`, with no account needed.
- *"Can I use ChatGPT (or another LLM) to write my code?"* — You can use an LLM to **check** code you wrote — to compare your answer with another answer. You cannot submit AT3 code you do not understand line by line; AT3 includes a short walk-through of your own program, and a student who cannot read their own code aloud has not done the task.
- *"What if the error message is in English I do not understand?"* — Read the line number first, look at that line, and ignore the rest of the message until you have read your own code. Half of all error messages point straight at a missing quote or semicolon visible by eye on the line they name.
- *"Is pseudocode dead now that we have real code?"* — No. Pseudocode is still the first draft. Real code is the final draft for a computer. AT3 asks for both: the pseudocode you wrote in Week 6, then the code you build from it this week.

---

## Formative assessment tips

Week 7 ends one week before AT3 lands. The role of formative checks is to make confidence visible *before* AT3 starts.

### Per-lesson informal checks

- **Lesson 19 — exit ticket (3 min, end of class).** Each student writes one sentence: *"A programming language is needed, not just pseudocode, because…"* Skim on the way to L20. If many sentences do not mention the word *computer*, revisit the "literal interpreter" framing at the start of L20.
- **Lesson 20 — live show-of-screens.** At the end of independent work, ask students to lift their laptops so the room can see each console / .NET Fiddle. A glance tells you which students have run something and which have not. Do not move on until every screen has output on it.
- **Lesson 20 — one-line exit ticket.** *"Type one line of code, in either language, that prints your name."* Read four at random aloud. The mix of `console.log` and `Console.WriteLine` in the room is healthy and shows the dual-language frame has landed.
- **Lesson 21 — pair report-back.** At the end of the pair activity, each pair gives one observation: *"What was the same in both languages? What was different?"* The pattern across the room tells you whether the "thinking is portable, syntax is the deal" message has been internalised.
- **Lesson 21 — AT3 readiness one-minute paper.** *"In one sentence, which Week-6 pseudocode piece will you turn into code for AT3?"* The answer tells you, a week before AT3 lands, who has already picked their material and who needs a nudge.

### What you are listening for across the week

By the end of L21, three phrases mark genuine understanding:

- *"`console.log` and `Console.WriteLine` do the same thing"* — said without prompting, by a student explaining their own code.
- *"I predicted `X`, the console said `Y`, so the bug is on line `N`"* — Week 6 dry-running, now applied to code.
- *"I'll do AT3 in `<language>` because…"* — and the *because* refers to readability, not to a rumour about difficulty.

If those phrases appear in student speech by the end of L21, AT3 lands without remediation next week. The *Console relay* in L20 is the central diagnostic — a class that predicts most of the six snippets correctly is a class ready for AT3.
