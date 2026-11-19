# Vocabulary

## Week 6 vocabulary

The terms below cover Lessons 16, 17 and 18. Definitions are short on purpose — read the self-study for examples in context. One term at the end (*console*) is a preview of Week 7, flagged as such.

### Pseudocode

A tighter, more rule-bound way of writing process descriptions on paper. It uses a small set of shared keywords (`SET`, `IF`, `WHILE`, and so on), but is still meant to be read by people, not run by a computer. Pseudocode is the bridge between everyday English and real code: precise enough for a computer to follow if it had to, readable enough to share with a non-programmer.

### Keyword

One of the small fixed words pseudocode uses to mark structure: `SET`, `READ`, `WRITE`, `IF`, `ELSE`, `ENDIF`, `WHILE`, `ENDWHILE`, `FOR`, `ENDFOR`. Keywords always look the same (UPPERCASE in this course) so the eye can find them quickly. Everything that is not a keyword is your own English: a variable name, a value, a message.

### Variable

A named container for one value that can change while the pseudocode runs. *"Make a sticky note on a jar that says `passwordLength`; the number on the note can change, but the note stays."* Today the variable might hold a number, tomorrow a yes/no, tomorrow a short string.

### Value

The actual content stored in a variable at a given moment — a number (`7`), a yes/no (`YES`), or a short piece of text (`"hunter2"`). The variable is the labelled box; the value is what is inside the box right now.

### Assignment

The action of putting a value into a variable. In this course it is always written `SET variableName TO value`, for example `SET passwordLength TO 7`. After an assignment, the variable holds the new value and forgets the old one.

### Input

What the pseudocode receives from outside — usually a number, a string, or a yes/no the user types in. In pseudocode it shows up as `READ variableName`. Until the input arrives, the variable has no useful value yet.

### Processing

What the pseudocode does in the middle, between reading the input and writing the output. Processing is where the rules live: a condition that decides which branch to take, a repetition that does something for every item, an assignment that combines values.

### Output

What the pseudocode sends back to the outside world — usually a short message, a number, or a yes/no. In pseudocode it shows up as `WRITE expression`. Output is what the user actually sees.

### Condition

A test that decides which branch the pseudocode takes next. *(Revisited from Week 5.)* In pseudocode it is written as `IF test THEN … ELSE … ENDIF`. The `IF` and `ENDIF` mark where the test starts and stops, so a reader can see the branches at a glance.

### Repetition

Doing the same block of pseudocode more than once, with a stopping condition. *(Revisited from Week 5.)* In pseudocode it is written as `WHILE test DO … ENDWHILE` or `FOR each item IN list DO … ENDFOR`. As in Week 5, every repetition needs an honest stop.

### Block

The body of an `IF`, `WHILE` or `FOR` — everything between the opening keyword and its matching `ENDIF`, `ENDWHILE` or `ENDFOR`. The block is indented by two spaces in this course so the eye can see where the inside of a structure starts and stops.

### Dry run

Walking through a piece of pseudocode by hand, line by line, on paper, pretending to be the computer. The dry run is you playing literal robot on your own pseudocode (the same literal-robot idea from Week 1, applied to your own text). Dry-running on paper finds bugs that re-reading does not.

### Trace table

The small table you draw next to your pseudocode while you dry-run it. It usually has one column per variable, plus a column for output. Each row of the table is one line of pseudocode executed. The trace table is what forces you to write each step down, instead of pretending to keep it all in your head.

### Bug

A place in your pseudocode where the actual output does not match the expected output. A bug is a small, specific defect — one wrong line, one wrong test, one missing assignment — not a vague "it does not work". Naming the bug is the first half of fixing it.

### Expected output

What you, the author, wanted the pseudocode to write for a given input. Before you dry-run, you write the expected output down at the side of the page. *Before* — not after; otherwise it stops being a check.

### Actual output

What the dry run actually produced for the same input, line by line. When *actual output* matches *expected output* on both a normal input and an awkward one, you can call the pseudocode finished. When they disagree, you have a bug to find.

### Edge case

*(Revisited from Week 1.)* An input that sits at the boundary of what the pseudocode expects: an empty string, the number zero, a negative number, a list with no items, a password that is exactly 8 characters long when the rule says "at least 8". Edge cases are where most bugs hide; the trace table is what catches them.

### Console *(looking ahead — Week 7, where pseudocode meets a real language)*

In Week 7 the words `READ` and `WRITE` from your pseudocode start landing in a real place on the screen called the *console*: a small text area where a program asks for input and prints its output. You do not need to know how to use a console yet — this term is here so the word is not new next week.
