# Week 8 — Teacher materials

This document covers L22, L23 and L24. Central message for the week: **"The course closes the loop: you take pseudocode you wrote yourself in Week 6, translate it into JavaScript or C#, run it, find one bug, fix it, and explain how it works. Programming has stopped being mysterious."** Nothing genuinely new lands conceptually — only the loop in code — but everything since Week 1 finally meets in one small file each student can defend out loud.

**AT3 is submitted and presented this week.** L23 is the build day: each student translates one piece of their own Week 6 pseudocode into JavaScript or C#, runs it, screenshots the output, writes a 3–5 sentence reflection. Submission at the end of L23. L24 is the test-and-present day: every student delivers a **2-minute** oral presentation, covering what the program does, how it works, the one bug, and the fix. The 2-minute slot in L24 is the AT3 oral component; pass / not-yet-pass check is described in `self-study.md` and in the AT3-brief task in both student-tasks files.

Tooling. JavaScript runs in the browser DevTools console; C# in **.NET Fiddle** (`dotnetfiddle.net`). No installs. No automatic testing tools. "Testing" means running by hand with two different starting values. "Debugging" means reading an error message and applying one small fix.

Cross-references. The supplementary deck `slides-l24-presentation-rubric.md` is used in L24 between presentations as a reminder of the 2-minute structure. The mandatory in-class activity **Show-and-tell loops** belongs in the 55–75 min slot of L22; **AT3 presentations** is the 55–85 min slot of L24. Both are described in `in-class-tasks.md`.

---

## Week 8 learning objectives (mapped to Bloom)

Week 8 stays inside **Applying** with one segment of **light Evaluating** in L24 (the student explains their own choice and compares their solution to a peer's). Forbidden verbs for Week 8 objectives: *design, develop, build, create (as a Bloom verb), analyse, architect, optimize, refactor, judge, critique*. "Create a file" in the everyday sense is fine — it is the Bloom-level *Creating* that is out of scope. Week 8 is consolidation.

### Lesson 22 — Loops in code

- **Understanding:** the student can **recognise** a `for` or `while` loop in code and **name** the four parts: counter, condition, body, update.
- **Understanding:** the student can **read** a 3–6 line loop and **predict** what it prints, in either language.
- **Applying:** the student can **write** a short `for` loop that runs a known number of times (count 1 to 5, greet by name three times) in their chosen language.
- **Applying:** the student can **map** a `REPEAT N TIMES` or `WHILE` line from their Week 6 pseudocode onto a working `for` or `while` loop in code.

### Lesson 23 — From pseudocode to a small program

- **Applying:** the student can **select** one piece of their own Week 6 pseudocode that is the right size to translate (6–20 lines).
- **Applying:** the student can **translate** that pseudocode into a working JavaScript or C# program of about 10–25 lines, using the translation table from `self-study.md`.
- **Applying:** the student can **run** the program in the browser console (JS) or `dotnetfiddle.net` (C#) and **confirm** at least one expected output.
- **Applying:** the student can **save** the source as a `.js` or `.cs` file (or a clearly labelled snippet pasted into the AT3 submission).

### Lesson 24 — Test, fix one bug, present

- **Applying:** the student can **test** the program by running it with at least **two** different starting values and checking the output against a prediction.
- **Applying:** the student can **read** a real console or compiler error message and **locate** the line it points at.
- **Applying:** the student can **apply** one small fix and re-run.
- **Light Evaluating:** the student can **explain** the program to the class in **2 minutes**, covering what it does, how it works, what went wrong, and how it was fixed.
- **Light Evaluating:** the student can **compare** their own solution with a peer's (optionally in the other language) in plain English — different choices, same goal.

---

## Common misconceptions for Week 8

At least two misconceptions per lesson, each with a *Correction:* line. These are the ones that come up most often in the closing week; address them before the misconception becomes a barrier to AT3.

### Lesson 22 misconceptions

**Misconception:** *"A loop is a complicated thing only programmers understand."*
**Correction:** A loop is the formal name for the "repeat 3 times" pattern the class has been writing in pseudocode since Week 5. The thinking has not changed; the syntax is the only new thing. Show one Week 6 `REPEAT` line and its `for`-loop translation side by side — usually enough.

**Misconception:** *"You need `while`; `for` is more advanced."*
**Correction:** For beginners the opposite is true. A `for` loop packs all four parts into one tidy header where it is hard to forget the update. A `while` loop depends on remembering to update the counter inside the body — the classic infinite-loop trap. Recommend `for` for AT3 unless the student genuinely has an "until" pattern.

### Lesson 23 misconceptions

**Misconception:** *"Pseudocode and code are completely different."*
**Correction:** Most of the work is replacing English words with the language's syntax — the structure is already there. The translation table in `self-study.md` covers eight common patterns and is enough for everything Week 6 produced. If a student claims their pseudocode is "too different to translate", sit with them and circle the parts of each line that are literally the same: variable names, numbers, `if`, `else`.

**Misconception:** *"If my program does not print anything, something is broken."*
**Correction:** More often the student did not press Run, or pasted only part of the program (.NET Fiddle needs code inside `Main`), or there is a typo in the print line (`console.Log` with capital L, `Console.Writeline` with small l). The `## When the screen is empty or silent` section of `self-study.md` lists the boring causes in order.

### Lesson 24 misconceptions

**Misconception:** *"Debugging needs a special tool."*
**Correction:** At this level, debugging is reading the message and changing one line. No special software, no automated testing tool. Say this out loud in L24: *"Debugging is reading and fixing, not tooling."* More advanced tools exist in later courses; the L24 exercise is reading text and changing one character.

**Misconception:** *"If the program runs, it is correct."*
**Correction:** Running and being correct are not the same. A JS program with `=` instead of `==` will often run silently and print the wrong answer. That is why AT3 requires **two** starting values: the second run catches the silent bug. Show `if (age = 18)` in the L24 warm-up — it runs, it prints "adult" for any age.

**Misconception:** *"The 2-minute presentation has to be a memorised script."*
**Correction:** It does not. The four beats (what / how / what went wrong / how I fixed it) are a structure, not a script. A student standing next to their open program and talking in their own words is exactly the target. The rubric deck lists what is **not** required: perfect code, fancy slides, memorised words.

---

## Lesson 22 — 90-minute plan

**Topic.** Loops in code: `for` and `while` in JavaScript and C# side by side, the four parts, the infinite-loop trap, the Week 6 pseudocode bridge.

**Central message for this lesson (one sentence).** A loop is the formal name for the *repeat-until* idea your pseudocode already used — only now the computer, not a human, is doing the repeating.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: put two Week 6 pseudocode "repeat" lines on the board (`REPEAT 5 TIMES: print N` and `WHILE password is too short DO ASK AGAIN`). Ask the class: *"What do you think these look like in real code?"* Collect three guesses; do not correct yet. | Whole class |
| 0:10–0:25 | Instructor input: walk Program D (counter from 1 to 5) in JS and C# side by side on the projector. Run each. Name the four parts (counter, condition, body, update) by pointing at them. Then show the `while` shape briefly with the count = 0 / count < 3 example. | Lecture |
| 0:25–0:55 | **INDEPENDENT WORK (30 min):** every student completes Task 8.2 in their chosen language (count 1 to 5; reverse to 5 down to 1; greet by name three times). Three snippets in one file. Teacher circulates. | Independent |
| 0:55–1:15 | **MANDATORY in-class activity — *Show-and-tell loops*** (Activity A in `in-class-tasks.md`, ~20 min). Each pair (or solo student) runs their loop live in front of the class, reads the output aloud, and the room names the four parts for one of the loops shown. Mixed JS and C# on purpose. | Whole class |
| 1:15–1:25 | Whole-class debrief: collect one "easy" and one "weird" moment per language onto the board. Surface the infinite-loop hazard once — show what forgetting `i++` does on screen. | Whole class |
| 1:25–1:30 | Closing + preview L23: *"Tomorrow is the build day. Pick which Week 6 pseudocode you will translate — bring it on paper."* | Whole class |

**Independent-work block: 30 minutes (33% of 90 minutes).** Meets the 30–50% rule.

**Cross-references.** The 55–75 min slot is **Activity A — *Show-and-tell loops*** from `in-class-tasks.md`. Have Task 8.2 ready on the projector as a fallback if a student arrives without their three snippets.

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** slide **1** (title) on screen while the board carries the live Week 6 pseudocode discussion.
- **Lecture (0:10–0:25):** slides **2** (*What lands this week*), **3** (*Loops — the shape (JS and C# side by side)*), **4** (*Counter, condition, body, update*), **5** (*A `while` loop (JS and C# side by side)*). Dwell on slide 4; the four-parts naming is the L22 fulcrum.
- **Independent work (0:25–0:55):** leave slide **3** on screen as the silent reference for the counter loop.
- **In-class activity (0:55–1:15):** no slide; the live loops in the room are the slide.
- **Debrief (1:15–1:25):** slide **6** (*When a loop runs forever*) to land the infinite-loop hazard.
- **Closing (1:25–1:30):** no slides.

---

## Lesson 23 — 90-minute plan

**Topic.** Build day for AT3. Every student translates one piece of their own Week 6 pseudocode into a working JavaScript or C# program and submits the source plus a screenshot at the end of the lesson.

**Central message for this lesson (one sentence).** Translating pseudocode into a programming language is mostly a matter of replacing English words with the language's syntax — the structure was already there.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: round the room, each student names — in one sentence — the Week 6 pseudocode they are going to translate today. Teacher notes anyone who has not picked one yet and steers them to the fallback templates in Task 8.1. | Whole class |
| 0:10–0:25 | Instructor input: the translation table on the projector. Walk Program A (age-limit check) end to end, pseudocode → JS → C#, with both languages side by side. Then walk one loop variant (Program E, greeting by name three times). | Lecture |
| 0:25–1:05 | **INDEPENDENT WORK (40 min):** every student translates their chosen Week 6 pseudocode into their chosen language, runs it, runs it again with a second starting value, takes the screenshot. Teacher circulates and answers individual questions. | Independent |
| 1:05–1:20 | Pair check: each student shows their partner the program and the output. Partner asks two questions: *"What does this line do?"* and *"What did you change between the two runs?"* No fixes yet — that is L24. | Pair |
| 1:20–1:28 | Whole-class debrief: collect typical pain points (semicolons in C#, capital L vs small l for `.Length` / `.length`, missing closing braces). Confirm everyone has saved the source file and the screenshot. | Whole class |
| 1:28–1:30 | Preview L24: *"Tomorrow you test, fix one bug, and present. Bring your source file and your screenshot — they are AT3."* | Whole class |

**Independent-work block: 40 minutes (44% of 90 minutes).** Meets the 30–50% rule.

**Cross-references.** No mandatory in-class activity from `in-class-tasks.md` is slotted into L23. Optional Activity C (*Translation race*) from `in-class-tasks.md` may be used in the 1:05–1:20 pair-check slot for classes that finish early.

**Slide cues — main deck `slides.md`.**

- **Warm-up (0:00–0:10):** slide **7** (*From your pseudocode to your program*) on screen as students name their pseudocode pieces aloud.
- **Lecture (0:10–0:25):** slide **8** (*The translation table*) for the table walk-through, then briefly back to slide **3** (*Loops — the shape*) when the loop variant comes up, and slide **9** (*Loop + if/else — password check*) if a student's pseudocode combines them.
- **Independent work (0:25–1:05):** leave slide **8** (*The translation table*) on screen as the silent reference. Slide **10** (*Save, run, see output*) in the last five minutes of the independent block reminds students how to capture the screenshot.
- **Pair check (1:05–1:20):** no slides; the partners look at each other's programs.
- **Debrief (1:20–1:28):** no slides; use the board for the pain-points list.
- **Preview L24 (1:28–1:30):** no slides.

---

## Lesson 24 — 90-minute plan

**Topic.** Test the AT3 program with two starting values, read one real error message and apply one small fix, deliver the **2-minute** oral presentation in class. Course closure.

**Central message for this lesson (one sentence).** Debugging at this level means reading what the computer told you, finding the one line it was talking about, and making one small change — no special tools needed.

| Time | Activity | Format |
|---|---|---|
| 0:00–0:10 | Warm-up: put one JavaScript error (`Uncaught ReferenceError: scre is not defined`) and one C# error (`error CS0103: The name 'scre' does not exist in the current context`) on the board, side by side. Ask the class: *"What is each one telling you?"* Land on *"both say 'I do not know what `scre` is' — you have a typo where you meant `score`."* | Whole class |
| 0:10–0:25 | Instructor input: reading an error message (one JS, one C#, both walked on screen). The one-small-fix-one-re-run loop named explicitly. Then walk the **2-minute presentation outline**: four beats, ~30 seconds each — what / how / what went wrong / how I fixed it. Use the rubric deck `slides-l24-presentation-rubric.md` here, in full. | Lecture |
| 0:25–0:55 | **INDEPENDENT WORK (30 min):** every student tests their program with two different starting values, deliberately or accidentally triggers one error, reads the message, applies one small fix, finalises the 3–5 sentence reflection, and rehearses the 2-minute presentation once with a phone timer. Teacher circulates and signs off readiness for each student. | Independent |
| 0:55–1:25 | **MANDATORY in-class activity — *AT3 presentations*** (Activity B in `in-class-tasks.md`, ~30 min). Each student gives a **2-minute** presentation of their program, in the order the teacher calls. Use a visible phone timer projected on the wall. After each presentation, the room answers one peer feedback prompt: *"Name one thing you noticed."* | Whole class |
| 1:25–1:30 | Course closure: re-read the central question of the course aloud from slide 18 — *"How do I speak to a computer so that it understands what I want it to do?"* Thank the class. Remind students to keep their AT3 source file; open it again in six months. | Whole class |

**Independent-work block: 30 minutes (33% of 90 minutes).** Meets the 30–50% rule.

**Class-size note.** The 30-minute presentation slot fits a class of ~12 at 2 minutes each plus 30 seconds of transition. For a larger class, see *Facilitation tips* below for the two adaptations (split into two simultaneous groups with a co-teacher, or rotate over two L24-style sessions). The submitted source plus screenshot already cover the written component for absentees; the oral component is the one that needs the live slot.

**Cross-references.** The 55–85 min slot is **Activity B — *AT3 presentations*** from `in-class-tasks.md`. This **is** the AT3 oral component. The supplementary deck `slides-l24-presentation-rubric.md` is projected between presentations as a reminder of the 4-beat / 2-minute structure.

**Slide cues — main deck `slides.md` and supplementary `slides-l24-presentation-rubric.md`.**

- **Warm-up (0:00–0:10):** slides **11** (*Reading a real error message (JavaScript)*) and **12** (*Reading a real error message (C#)*) side by side on the projector while the board carries the live "what is it telling you?" discussion.
- **Lecture (0:10–0:25):** slide **13** (*One small fix, one re-run*) to land the debugging-is-reading-not-tooling frame, then slide **14** (*Your 2-minute presentation*) for the four-beat outline. Then switch to the supplementary deck `slides-l24-presentation-rubric.md` and walk all 4–6 slides end-to-end so students see the rubric once before they rehearse.
- **Independent work (0:25–0:55):** leave slide **14** on screen as the silent reference for the four beats during rehearsal.
- **AT3 presentations (0:55–1:25):** project the supplementary deck `slides-l24-presentation-rubric.md` between presentations as a calm reminder; do **not** project slides over a student presenting. The pass-criteria slide of `slides-l24-presentation-rubric.md` is the most useful one to leave up.
- **Course closure (1:25–1:30):** slide **18** (*Closing the loop — Week 1, one more time*) so the class leaves on the verbatim central question, then slide **19** (*Thank you, and what comes next*).

---

## Facilitation tips

### Running the 2-minute presentations on time

- **Use a visible phone timer**, projected on the wall or held by a student timer-keeper. The visible timer self-edits the room.
- **Set a hard cap at 2:30** with a soft chime at 2:00. A student who keeps going past 2:30 is gently cut off — next presenter steps up.
- **Order the room before the slot starts.** A pre-announced order keeps transitions to 20–30 seconds.
- **The peer feedback question — *"Name one thing you noticed"* — is asked once per presentation**, of the whole room. One short answer; not a discussion.

### Handling a student whose program never ran

- **Focus the presentation on the bug they could not fix and what they tried.** The pass criterion accepts a documented failed attempt — the student names the error message and the fix they attempted. That counts.
- **Keep the same 4-beat structure** but the last beats become "what went wrong / what I tried."
- **Mark not-yet-pass when there is no documented attempt at all.** Offer a one-week re-submit window.

### Managing the dual-language room

- **Group JS and C# students at adjacent tables** for L23's pair-check slot.
- **Project both languages side by side on every code slide.** The visual parallelism does half the work.
- **When .NET Fiddle is slow** (shared school Wi-Fi), allow submission from home — the screenshot plus source covers it; the 2-minute presentation can be given without a live demo.

### Helping the shy presenter

- **The 2-minute presentation is the AT3 oral component**, non-negotiable. But form is flexible: a severely uncomfortable student may present in a small group of three (teacher plus two peers). Four beats are the same; the audience is smaller.
- **The recorded-video alternative** in Task 8.1's "If you are doing this alone" is for absentees, not in-class avoidance.

---

## Answers to common student questions

- *"Can I use `console.log` inside my C# program by mistake?"* — No; the compiler will reject it with `error CS0103: The name 'console' does not exist in the current context`. C# uses `Console.WriteLine` (capital C, capital W, capital L). If you see CS0103 with the word `console` in lowercase, this is what happened. Add the capital C.
- *"Why does my C# program say `CS0103`?"* — The compiler does not know one of the names you used. It is almost always a typo: `scre` instead of `score`, `console` instead of `Console`, `Writeline` (small l) instead of `WriteLine`. Find the line the message names; the wrong word is on it.
- *"What if my Week 6 pseudocode is too big?"* — Pick one part of it that does one clear job from start to finish (6–20 lines is the sweet spot). The whole program does not have to be there. If your Week 6 pseudocode is missing or lost, pick one of the five fallback templates in Task 8.1 (age, password, score, counter, greeting) and adapt the values to your own context. That counts as AT3.
- *"Do I have to do the presentation if I am shy?"* — Yes; the 2-minute oral is the AT3 oral component and there is no way to pass AT3 without it. But the audience can be small (the teacher plus two peers in a corner of the room) and the form is conversational — the four beats are a structure, not a memorised script. Talk to the teacher in L23 if presenting to the whole room is a barrier.
- *"Can I use ChatGPT to write the program?"* — You can use an LLM as a sparring partner — for example to explain an error message — but the program you submit must be one you can read line by line and walk the room through in 2 minutes. A student who pastes LLM output without understanding it will be caught at the presentation; the four beats require the student to name what each line does. Task 8.4 has an explicit LLM sparring step with a prompt that does *not* ask for the fix; that is the intended use.
- *"What counts as 'one bug'?"* — A typo (misspelled variable name), a missing semicolon (C#), a missing closing brace, a `=` where `==` was meant, a capitalisation mismatch (`length` vs `Length`). Any one of these is fine. The bug must be one you can name in plain English; "my program just did not work" is not enough.
- *"Do I need to install anything?"* — No. JavaScript runs in the browser DevTools console (`Cmd + Opt + J` / `Ctrl + Shift + J`). C# runs in `dotnetfiddle.net` with no account. Both are the same tools you used in Week 7.

---

## Formative assessment tips

Week 8 is the last week. Formative checks here are not preparing for a future assessment; they are confirming that AT3 is on track and that the central question of the course has actually been answered for each student. Three quick checks across the week, plus one closure check at the end of L24.

### Per-lesson informal checks

- **Lesson 22 — exit ticket (3 min, end of class).** Each student writes, on one line, the four parts of a `for` loop. Counter, condition, body, update. Read four at random aloud. A class that names all four correctly is ready for L23's build day.
- **Lesson 23 — sign-off circulation.** During the 40-minute independent block, the teacher visits every student at least once. Sign off two things: (a) the program ran with one starting value, (b) the screenshot exists. A student who is stuck after 20 minutes of independent work is the one who needs intervention, not the one who is still typing.
- **Lesson 23 — pair-report-back.** At the end of the 1:05–1:20 pair-check slot, each pair gives one observation in one sentence: *"One thing my partner's program does well; one thing I would change in mine after seeing theirs."* The pattern across the room tells you whether students can read code that is not their own — a key Week 8 transfer.
- **Lesson 24 — readiness check at 0:55.** Just before the presentations start, ask the room: *"By show of hands, how many of you have a program that runs, a screenshot, and a 3-sentence reflection ready?"* Hands that do not go up are the students you visit first during the 30-minute independent block. No-one presents without those three artefacts in hand.
- **Lesson 24 — one-minute paper at the end.** *"In one sentence: did the course answer its central question for you?"* (*"How do I speak to a computer so that it understands what I want it to do?"*) This is the closure check. A class where most students answer "yes, and here is the program in my hand" has met the course's goal.

### What you are listening for across the week

By the end of L24, three phrases mark genuine course-level understanding:

- *"My program does X and here is why each line is there"* — said without hesitation, by a student presenting their own program.
- *"The error message said scre — that is the line where I had `scre` instead of `score` — I added the `o` and it worked"* — the bug-and-fix narrative, with no mystery.
- *"It is the same shape in C# as in JavaScript — I just used `int` instead of `let` and `Console.WriteLine` instead of `console.log`"* — the dual-language transfer landed.

If those three phrases appear in student speech in L24, the course has done its job. The 2-minute presentation slot is the diagnostic and the celebration at the same time.
