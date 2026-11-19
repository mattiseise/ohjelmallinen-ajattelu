# Lesson 16 — Pseudocode: from natural language to a more precise format

### From English to pseudocode

Here is a familiar process in English. You are making a mug of tea, and you may or may not take sugar today.

> You fill the kettle and switch it on. You wait until it clicks. You put a tea bag in your mug and pour the hot water. You leave the bag in for three minutes. If you take sugar, you add one spoon and stir. Then the tea is ready.

Read it once aloud. A human friend understands it. A computer does not — *"wait until it clicks"* (how long? how does the computer notice the click?) and *"if you take sugar"* (how does it know?) are both polite gaps that depend on the reader being a person.

Now the same process in pseudocode:

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

Side by side: what is different? The English is shorter and friendlier. The pseudocode is longer, but every line is one thing the follower must do, and every gap the English left polite (the click, the sugar) is now a named question (`kettleHasNotClicked`, `takesSugar`) with a clear answer. The pseudocode also separates *what we ask the user* (the `READ`) from *what we tell the user* (the `WRITE`s) — the English squashed those together. Notice that the `IF` and `WHILE` you met in Week 5 in plain English are still there: they have just been given a uniform shape and a closing word (`ENDIF`, `ENDWHILE`) so a reader can see where each block starts and stops at a glance.

Pseudocode is not a new language to memorise. It is the things you already write in Week 5, with a few shared words and a fixed shape so a stranger can read it the same way you do.

### The small set of keywords

This course uses a small fixed set of pseudocode keywords. All of them appeared, in plain English form, in Week 5. The keywords are always written in UPPERCASE so the eye finds them quickly. Everything else (variable names, values, messages) is your own English.

```text
SET passwordLength TO 7
```
*Assignment.* Put the value `7` into the named container `passwordLength`. After this line, `passwordLength` is `7`.

```text
READ password
```
*Input.* Take whatever the user types and put it into the named container `password`.

```text
WRITE "your password is strong"
```
*Output.* Show this message to the user.

```text
IF length >= 8 THEN
  WRITE "long enough"
ELSE
  WRITE "too short"
ENDIF
```
*Condition.* If the test is true, do the first block; otherwise do the second block. The `ENDIF` says where the condition stops.

```text
WHILE inboxIsNotEmpty DO
  WRITE "process one message"
ENDWHILE
```
*Repetition with the test before each repeat.* As soon as the test stops being true, the loop stops.

```text
FOR each folder IN backupList DO
  WRITE "back up the folder"
ENDFOR
```
*Repetition over a list known in advance.* The follower does the inside once for every item in the list.

Six shapes. Treat this section as a reference card — you will come back to it through L17 and L18.

### Sequence, condition, repetition — meet again

Look back at the tea pseudocode. The lines that just run top to bottom (`SET kettleOn TO YES`, then `SET bagInMug TO YES`, then the `WRITE`s) are *sequence*. The block opening with `IF takesSugar = YES THEN` is *condition*. The block opening with `WHILE kettleHasNotClicked DO` is *repetition*. Sequence, condition, repetition — exactly the three building blocks from Week 5. Pseudocode does not add a fourth move; it only gives each of the three moves a shared shape on paper.

### Why pseudocode is more reliable to share than English prose

If you and a classmate both wrote the tea process in English, two friendly readers could read the two versions and come away with subtly different ideas of what happens in the sugar step. The pseudocode version closes those gaps. *"If you take sugar"* becomes *"is the value of `takesSugar` equal to `YES` right now?"* There is one and only one way to read that. The point of pseudocode is not that it is easier to write — it is usually harder to write than English. The point is that it is harder to *misread*. When you hand it to a stranger, the stranger gets the same process you meant.

> **Pause for a moment:** Pick one short process you do every morning (charging your phone, brushing your teeth, checking your bus app). Where in that process would your English be polite — where would it leave a gap a literal follower would trip on? Name one specific gap, in writing, before moving on.

> **Pause for a moment:** The tea pseudocode above is 12 lines. If you removed the `ENDIF` and `ENDWHILE`, would the meaning still be clear? Why do you think the course uses them anyway?

---
