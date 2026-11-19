# Week 6 — From thinking to code

Computational Thinking

A first-year vocational ICT course

---

## The central question

How do I speak to a computer so that it understands what I want it to do?

This week we answer it with one new word: **pseudocode**.

---

## This week — pseudocode, variables, dry run

- Lesson 16 — **pseudocode**: a tighter way to write what you already write.
- Lesson 17 — **variables** and the input → processing → output skeleton.
- Lesson 18 — **dry running** on paper with a trace table.

**AT2 is submitted around Lesson 18.** The work below is its raw material.

---

## What is pseudocode?

**Pseudocode is the bridge between everyday English and real code: precise enough for a computer to follow if it had to, readable enough to share with a non-programmer.**

Still on paper. Still in English. Just with a few shared words and a fixed shape.

---

## The small set of keywords

- `SET name TO value` — assignment
- `READ name` — input
- `WRITE expression` — output
- `IF test THEN … ELSE … ENDIF` — a condition
- `WHILE test DO … ENDWHILE` — a repetition with the test first
- `FOR each item IN list DO … ENDFOR` — a repetition over a known list

These are all the keywords you need this week.

---

## English vs. pseudocode — making tea

**English:** Fill the kettle. Switch it on. Wait until it clicks. Put the bag in the mug. Pour the water. If you take sugar, add one spoon.

**Pseudocode:**

```text
SET kettleOn TO YES
WHILE kettleHasNotClicked DO
  wait
ENDWHILE
SET bagInMug TO YES
WRITE "pour water"
IF takesSugar THEN
  WRITE "add one spoon"
ENDIF
```

---

## Sequence, condition, repetition — meet again

Pseudocode is just Week 5's three building blocks with shared words:

- *sequence* — lines top to bottom.
- *condition* — `IF … THEN … ELSE … ENDIF`.
- *repetition* — `WHILE … ENDWHILE` or `FOR … ENDFOR`.

The thinking is the same. The shape just tightens.

---

## Input → processing → output

Most pseudocode follows the same skeleton:

- **Input** — `READ` something from outside.
- **Processing** — decide, calculate, repeat.
- **Output** — `WRITE` the answer back.

Example: ask for a number, double it, write the result.

---

## What is a variable?

A **variable** is a named container for one value that can change while the pseudocode runs.

Picture a sticky note on a jar. The label stays the same. The number on the note can change.

```text
SET passwordLength TO 7
SET passwordLength TO 8
```

Now the jar holds 8.

---

## A good variable name

Bad: `SET x TO 7`

Good: `SET passwordLength TO 7`

Both do the same thing for the computer. The second tells the next reader (or future you) what the 7 means.

---

## A vocational example — password strength

```text
READ password
SET length TO numberOfCharactersIn(password)
SET hasDigit TO doesPasswordContainADigit(password)
IF length >= 8 AND hasDigit = YES THEN
  SET isStrong TO YES
ELSE
  SET isStrong TO NO
ENDIF
WRITE isStrong
```

Input → processing → output. One variable per idea.

---

## What is a dry run?

A **dry run** is walking through your pseudocode by hand, line by line, pretending to be the computer.

It is Week 1's "literal robot" — but now the robot is you, on paper, reading your own text.

---

## The trace table

A small table next to your pseudocode. One column per variable, plus an output column. One row per line you execute.

| Line | counter | total | Output |
|------|---------|-------|--------|
| 1    | 1       | 0     |        |
| 2    | 1       | 1     |        |
| 3    | 2       | 1     |        |
| 4    | 2       | 3     |        |
| 5    | 3       | 3     | 3      |

The table is what forces you to write each step down.

---

## Finding a bug — actual vs. expected output

Expected output for input `5`: write `15`.

Trace says actual output is `10`.

Look at the line where the values diverge. The bug lives there.

Fix that one line. Re-trace. Expected and actual now match.

---

## AT2 — submitted around Lesson 18

- **What it asks:** a short piece of pseudocode for a small task you choose, plus a trace table.
- **What to bring:** the pseudocode, the trace table (normal input + one awkward input), a 5-sentence reflection.
- **What NOT to bring:** any real programming language. Pseudocode only.

---

## Week 6 vocabulary at a glance

- pseudocode, keyword, variable, value, assignment
- input, processing, output
- condition, repetition, block
- dry run, trace table, bug, expected output, actual output

Looking ahead: *console* (Week 7).

---

## Must-do minimum vs. deepening

**Must-do minimum**

- Write 10–20 lines of pseudocode for a familiar process, with one condition and one repetition.
- Dry-run it on a trace table for one normal and one awkward input.

**Deepening**

- Find and name the type of bug in a broken snippet.
- Trace a classmate's pseudocode and compare.
- Use an LLM as a sparring partner against your own trace.

---

## Tasks this week

- Task 6.1 — Pseudocode a familiar process (MANDATORY, AT2 spine)
- Task 6.3 — Find the bug (DEEPENING)
- Task 6.4 — Trace a classmate's pseudocode (DEEPENING)
- Task 6.5 — LLM sparring against your dry run (DEEPENING)

Keep your pseudocode and trace table — **AT2 is submitted around Lesson 18 of this week.**

---

## What comes next — Week 7: first real code

Next week the same pseudocode shape becomes a tiny program in a real language you run in a browser.

The keywords you learned this week have direct partners there. The thinking does not change.

---

## Recap — the central question, one more time

How do I speak to a computer so that it understands what I want it to do?

**Pseudocode is the bridge between everyday English and real code.** This week you built the bridge. Next week you walk across it.
