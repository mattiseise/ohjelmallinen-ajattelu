# Week 6 — Student tasks

## Overview of the week's tasks

This week has **four tasks**. The green-dot task (🟢 MANDATORY) is the **must-do minimum** — finish it to keep up with the class and to be ready for **AT2, which is submitted around Lesson 18 of this week**. The purple-dot tasks (🟣 DEEPENING) are optional extensions that all sharpen the same skills AT2 will check.

Every task feeds AT2 directly. AT2 asks you to write a short piece of pseudocode for a small process, dry-run it on paper with a trace table, and explain in plain English what each part does. Tasks 6.1, 6.2 and 6.3 build exactly those three pieces: your pseudocode, your trace, and your explanation. **Throw nothing away** — keep your sheets in one folder until L18.

A reminder before you start: this week is the synthesis week. Pseudocode is not a new language to memorise; it is the sequence-condition-repetition thinking from Week 5 written in a fixed shape, with a small set of keywords (`SET`, `READ`, `WRITE`, `IF/ELSE/ENDIF`, `WHILE/ENDWHILE`, `FOR/ENDFOR`). No real code anywhere. Paper and pen are enough.

---

## Task 6.1 — Pseudocode a familiar process 🟢 MANDATORY

**Goal:** Write a short piece of pseudocode for a process you really do, then dry-run it on paper with a trace table. This is the spine of the week and the direct feeder for AT2.

This is the most important task of Week 6. Tasks 6.2, 6.3 and 6.4 deepen the same skills, but this one *is* the AT2 rehearsal.

### Steps

1. **Pick a process you personally do almost every day.** Making tea, checking notifications, packing your bag, charging your phone overnight, sending a routine Discord message. It must be a process your hands already know — not a textbook example.
2. **Write the process in pseudocode (10–20 lines).** Use the keyword set from class: `SET … TO …`, `READ`, `WRITE`, `IF … THEN … ELSE … ENDIF`, and `WHILE … DO … ENDWHILE` or `FOR each … IN … DO … ENDFOR`. **At least one condition and at least one repetition are required.** Indent every block body by two spaces.
3. **Name your variables honestly.** `SET cupsOfTea TO 1` tells the next reader what the line is for; `SET x TO 1` does not.
4. **Dry-run your pseudocode for one *normal* input.** Draw a trace table: one column per variable, one for any output, one row per executed line. Walk down line by line.
5. **Dry-run it again for one *awkward* input** — something missing, something extra: the kettle is empty, the tea jar is out, your phone is at 1%. Fresh table.
6. **Compare the two traces.** If the awkward case did not behave the way you wanted, that is a bug — circle the line where the trace and your expectation first disagree.
7. **Write a 3–5 sentence reflection.** What was harder to express in pseudocode than in plain English? What was easier? Did the awkward-input trace surface anything English prose hid?

### If you are doing this alone

This task does not assume a partner — your two traces are the test. To get a second pair of eyes without a classmate, use the **24-hour gap**: write the pseudocode today, dry-run it tomorrow without re-reading your reflection. A day-old you is a surprisingly literal follower. You can also trace it once on your phone and once on paper the next day — the change of medium catches things the eye glided over the first time.

> Tip: resist the urge to write real-looking code. UPPERCASE keywords and plain-English values is exactly what the course wants. Real code arrives next week, and pseudocode keywords map onto it cleanly.

### Keep your notes

Keep your pseudocode, both trace tables and your reflection in one folder. **AT2 is submitted around Lesson 18 of this week**, and it asks for exactly this artefact — a short piece of pseudocode for a small process, a trace table for one normal and one awkward input, and a short reflection. Task 6.1 is the AT2 rehearsal at full scale.

---

## Task 6.2 — Find the bug 🟣 DEEPENING

**Goal:** Take a deliberately broken piece of pseudocode, dry-run it, identify the bug, fix it, and re-trace. AT2's reflection asks you to name what went wrong — this task is the rehearsal.

### The broken pseudocode

This is supposed to count down from 5 to 1 and then write `LIFT OFF`. **Exactly one line is wrong.**

```text
SET counter TO 5
WHILE counter > 1 DO
  WRITE counter
  SET counter TO counter - 1
ENDWHILE
WRITE "LIFT OFF"
```

The **expected output** is:

```text
5
4
3
2
1
LIFT OFF
```

### Steps

1. **Predict the output by reading.** Before you trace, write down what you think it prints. Keep this prediction.
2. **Dry-run it on paper.** Columns: line number, `counter`, output. Walk every line. Do not skip the `WHILE` re-check at the bottom of the loop.
3. **Compare actual output (from your trace) with expected.** Where do they first differ?
4. **Name the bug in plain English.** Pick from: *off-by-one*, *wrong comparison*, *missing initialisation*, *wrong branch*. One sentence on why.
5. **Fix the pseudocode** (often a single character) and write the corrected version next to the broken one.
6. **Re-trace the fix on a fresh table.** Confirm actual output now matches expected.
7. **Write 3–5 sentences** on what the trace caught that your initial reading missed.

### If you are doing this alone

This task does not assume a partner — the trace table is the partner. If you want a sanity check, post your trace (not the bug name) in the class chat: *"Does my actual output match yours?"*

> Tip: when actual and expected disagree, do not start by editing the pseudocode. Start by re-tracing on a *fresh* page. Half the time the bug is in your trace.

### Keep your notes

Keep your prediction, both trace tables, the named bug type and your fixed pseudocode. **AT2 is submitted around Lesson 18 of this week**, and AT2 asks you to comment on at least one bug you caught by dry-running.

---

## Task 6.3 — Trace a classmate's pseudocode 🟣 DEEPENING

**Goal:** Practise reading pseudocode you did not write. The skill tells you whether your own pseudocode is *readable* — and readability is exactly what AT2 checks.

### Steps

1. **Swap Task 6.1 pseudocode with a classmate.** Do not tell each other what the process is.
2. **Read silently. Before tracing, write a one-sentence guess** at what process it describes.
3. **Dry-run it on a trace table** for one input the writer suggests and one awkward input you invent.
4. **Compare with the writer.** Did your output match? Was the goal guessable from the steps, or did you have to ask? Which line did you re-read the most?
5. **Swap roles.** They trace yours; you compare. Each of you keeps both traces.
6. **Write 3–5 sentences** on which keyword (`IF`, `WHILE`, `FOR`) made the goal most guessable in your classmate's pseudocode, and which variable name carried the most meaning.

### If you are doing this alone

If you have no classmate to swap with, run the task against your **past self**. Use a 24-hour gap: trace pseudocode you wrote earlier (Task 6.1, or a re-encoded Week 5 exercise) the next day, without re-reading your reflection. Alternatives that also work: post your pseudocode in the class chat and ask anyone to trace it; trace once on your phone and once on paper a day later. Any swap of person, day or device counts.

> Tip: if you re-read any one line more than twice during a trace, mark it — that line is a candidate for a rewrite.

### Keep your notes

Keep your guess sentence, both trace tables, and your comparison. **AT2 is submitted around Lesson 18 of this week**, and AT2's reflection rewards students who can say which parts of their pseudocode were easy and which were hard for an outside reader to follow. Task 6.3 gives you a real outside reader.

---

## Task 6.4 — LLM as sparring partner against your own trace 🟣 DEEPENING

**Goal:** Use an LLM to challenge your own dry-run. Practise treating the LLM as a sparring partner, not a teacher.

### Steps

1. **Start from your Task 6.1 work** — your pseudocode and your hand trace for the awkward input.
2. **Paste only your pseudocode** (not your trace) into an LLM with the prompt below.
3. **Compare the LLM's predicted trace with yours, line by line.**
4. **Where you disagree, re-trace by hand a third time.** Decide who is right and write one sentence saying why.
5. **Write 4–6 sentences** on where you and the LLM disagreed, who was right after the re-trace, and what that tells you about your pseudocode or the LLM's reading.

### Sample prompt

```text
You are my sparring partner, not my teacher. I am a vocational ICT
student practising how to dry-run pseudocode with a trace table.

Below is my pseudocode. The keywords SET, READ, WRITE, IF, ELSE,
ENDIF, WHILE, ENDWHILE, FOR, ENDFOR are shared course conventions,
not a real programming language.

[paste your pseudocode here]

Predict the trace for this input: [paste your awkward input here]

Show your trace as a table: one row per executed line, one column
per variable, plus a column for output. No prose explanations.

Do not assume your trace is correct. I will compare it to my own
hand trace and decide. If a line looks ambiguous, name the line
number — but do not rewrite my pseudocode for me.
```

**Do not accept the LLM's trace as the truth.** Treat every disagreement as a question.

### If you are doing this alone

This task does not assume a human partner — the LLM stands in for one. If you would also like a human reader, post your pseudocode (not your trace) in the class chat: *"Would anyone hand-trace this?"* Three traces — yours, the LLM's, a classmate's — and any two-way disagreement is the most interesting line in your pseudocode.

> Tip: LLMs are often off by one iteration inside a `WHILE`. If you differ by exactly one row, check the stopping condition first.

### Keep your notes

Keep your pseudocode, your hand trace, the LLM's trace and your decide-who-was-right paragraph. **AT2 is submitted around Lesson 18 of this week**, and a student who can point at a moment they out-traced an LLM has a strong paragraph for the AT2 reflection.
