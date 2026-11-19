# Worked example — making tea

A walk from English to pseudocode, end to end.

The same template Week 1 used for instant noodles, now in pseudocode.

---

## In English

You fill the kettle and switch it on. You wait until it clicks. You put a tea bag in your mug and pour the hot water. You leave the bag in for three minutes. If you take sugar, you add one spoon and stir.

Five sentences. Clear enough for a human friend. A computer would still trip on *"wait until it clicks"* (how long?) and *"if you take sugar"* (how does it know?).

---

## In pseudocode — the skeleton

```text
READ takesSugar
SET kettleOn TO YES
WHILE kettleHasNotClicked DO
  wait
ENDWHILE
SET bagInMug TO YES
WRITE "pour hot water"
WRITE "wait three minutes"
IF takesSugar = YES THEN
  WRITE "add one spoon of sugar"
  WRITE "stir"
ENDIF
WRITE "tea is ready"
```

Twelve lines. The `IF` and the `WHILE` from Week 5 are visible at a glance.

---

## Naming the parts

```text
READ takesSugar             <-- INPUT
SET kettleOn TO YES         <-- PROCESSING starts
WHILE kettleHasNotClicked DO
  wait
ENDWHILE
SET bagInMug TO YES
WRITE "pour hot water"      <-- OUTPUT
WRITE "wait three minutes"  <-- OUTPUT
IF takesSugar = YES THEN
  WRITE "add one spoon of sugar"  <-- OUTPUT
  WRITE "stir"                    <-- OUTPUT
ENDIF
WRITE "tea is ready"        <-- OUTPUT
```

One input. One processing block in the middle. Several outputs at the end. This is the L17 skeleton already.

---

## What got more precise

English left these vague — pseudocode pinned them down:

- *"the kettle"* → a named state `kettleHasNotClicked` we can actually check.
- *"if you take sugar"* → a named variable `takesSugar` with a clear `YES` / `NO` value.
- *"three minutes"* → an explicit `WRITE` line, not a side comment.

The pseudocode is longer than the English. That is the trade: more lines, less guessing.

---

## The template scales

The same shape works for very different tasks:

- **Help-desk ticket triage** — `READ ticketText`, `IF` it contains the word "password" THEN route to tier 1, `ELSE IF` "outage" THEN tier 2, `ELSE` tier 3.
- **Password-strength check** — `READ password`, count the length, `IF` length is at least 8 AND there is a digit THEN strong, `ELSE` weak.
- **Daily backup routine** — `FOR each folder IN backupList DO` copy it, `ENDFOR`. Output a list of what was copied.

Same skeleton: input on top, processing in the middle, output at the end.
