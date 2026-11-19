## Slide 1 — Week 6 — From thinking to code

Open with the arc. Weeks 1-5 trained the eyes: literal robots, three building blocks, decision trees. This week the hand joins in. They start writing things down in a shape that is one step from code. Tell the class: "By Friday you will be writing pseudocode. By next Friday you will be reading real code. Same thinking, tighter shape." Ask the class: "Show of hands — who has ever written code before?" Note the room, no judgment. ~2 min.

## Slide 2 — The central question

Read the question aloud. This is the question the whole course exists to answer. Tell the class: "Every week has been a partial answer. This week we get explicit." Pseudocode is the bridge word. Ask the class: "Has anyone heard the word *pseudocode* before? Guess what it means." Steer toward: "fake-code" or "almost-code." ~1 min.

## Slide 3 — This week — pseudocode, variables, dry run

Walk through the three lessons. Pseudocode (the shape), variables (the containers), dry run (the test). Be explicit about the assessment: AT2 lands around Lesson 18. Everything they write this week is its raw material. Ask the class: "Which lesson sounds most useful at work?" Steer to dry running — debugging a thought before the code is written saves hours. ~2 min.

## Slide 4 — What is pseudocode?

Read the bold sentence twice. Pseudocode is a bridge: precise enough for a machine to follow, readable enough for a human to share. Stress: still on paper, still in English, just with a small set of shared words. This matters because students often think there is a giant leap from English to code; pseudocode shows the leap is small. Ask the class: "Could you read pseudocode to your grandparent?" Answer: yes, mostly. ~2 min.

## Slide 5 — The small set of keywords

This is the keyword toolbox for the whole week. Six words. Read them slowly. SET writes a value into a container; READ takes input; WRITE prints output; IF is a condition; WHILE and FOR are repetitions. Tell the class: these six words are the entire vocabulary of pseudocode for AT2. Ask the class: "Which three keywords map to Week 5's three moves?" Answer: sequence is implicit, IF is condition, WHILE/FOR are repetition. ~3 min.

## Slide 6 — English vs. pseudocode — making tea

Read the English paragraph, then walk through the pseudocode line by line. Point at SET, WHILE, IF — the keywords from the previous slide. Tell the class: this is the same tea recipe from Week 5, just tightened. Note `kettleHasNotClicked` — a named state we can check. Ask the class: "Which line is the condition? Which is the loop?" Have a student point. ~3 min.

## Slide 7 — Sequence, condition, repetition — meet again

Tie it back. Pseudocode is just Week 5's three building blocks wearing keyword clothes. Sequence is lines top to bottom. Condition is IF/ELSE/ENDIF. Repetition is WHILE or FOR. Tell the class: "Nothing new in the thinking. Only the shape tightens." Ask the class: "Why does the shape need to tighten?" Steer to: because the computer will not guess what we mean. ~2 min.

## Slide 8 — Input → processing → output

This is the universal skeleton. Most pseudocode, and most real code, follows it. Read the three parts. Use the doubling example: READ a number, double it, WRITE the result. Three lines, three sections. Tell the class: "When you sit down to write pseudocode and you do not know where to start — start with these three labels." Ask the class: "An ATM: name the input, the processing, the output." ~2 min.

## Slide 9 — What is a variable?

Read the definition. The sticky-note-on-a-jar image is the one to keep. The label is the name; the number is the value. The two lines on the slide show the value changing while the name stays the same. Tell the class: a variable is a memory drawer with a label. Ask the class: "Where in real life do you have a labelled container whose contents change?" Examples: a fridge shelf, a Spotify playlist, a chat thread. ~3 min.

## Slide 10 — A good variable name

Read both lines. They do the same thing for the computer. They do very different things for the next reader. Stress: code is read more often than written. A good name is a gift to your future self. Tell the class: "When you read your own code in a week, you will not remember what `x` was." Ask the class: "Rename `SET t TO 30` for a kitchen timer." Possible: `cookingMinutes`, `restTimer`. ~2 min.

## Slide 11 — A vocational example — password strength

Walk down the lines. READ password (input). SET length and SET hasDigit (processing — pulling two facts out of the password). IF length and hasDigit (condition). WRITE isStrong (output). Tell the class: this is the password rule from Week 5, now pinned down in pseudocode. Ask the class: "What input would make this say NO?" A short password without a digit. ~3 min.

## Slide 12 — What is a dry run?

Read the definition. A dry run is being the computer, on paper, with your own pseudocode. The Week 1 literal-robot is back — but now the robot is the student, reading their own text. Tell the class: this is how you debug a thought before it becomes code. Ask the class: "Why do this on paper instead of just running it?" Steer to: because there is no code yet, and the bug might be in the thinking. ~2 min.

## Slide 13 — The trace table

Read the table column by column. One column per variable, plus output. One row per executed line. The table forces honesty — you cannot skip a step. Tell the class: "The trace table is the safety net. If you skipped a step in your head, the table catches it." Ask the class: "What is `total` after line 4?" Answer: 3. Have a student narrate one row. ~3 min.

## Slide 14 — Finding a bug — actual vs. expected output

This is the debugging move in its purest form. Predict. Run. Compare. Find the first line where prediction and reality diverge. The bug lives there. Tell the class: "You will use this exact move for the rest of your career." Ask the class: "If expected is 15 and actual is 10 for input 5, what kind of arithmetic mistake might cause that?" Steer to a doubling instead of tripling. ~3 min.

## Slide 15 — AT2 — submitted around Lesson 18

Make AT2 concrete. The deliverable: a short piece of pseudocode plus a trace table. Normal input plus one awkward input. A short reflection. What NOT to submit: any real programming language. Pseudocode only — AT2 is about thinking, not about syntax. Ask the class: "Which 'awkward input' would you try on the password example?" Answer: empty string, one character, very long string. ~3 min.

## Slide 16 — Week 6 vocabulary at a glance

Read the list. These words appear in AT2 and in the rest of the course. Trace table, dry run, expected vs. actual — these are debugging words they will use forever. The console is the bridge to Week 7. Ask the class: "Which of these words is brand new this week?" Likely: trace table, dry run, pseudocode itself. ~1 min.

## Slide 17 — Must-do minimum vs. deepening

Set the bar. The minimum: 10–20 lines of pseudocode with one condition and one repetition, plus a dry run on two inputs. Deepening: bug-hunting, peer tracing, LLM sparring. Tell the class: "Aim for the minimum first. Then deepen." Ask the class: "Why do we want one *awkward* input in the dry run?" Steer to: real users will give weird input. ~2 min.

## Slide 18 — Tasks this week

Walk through the four tasks. Task 6.1 is the spine of AT2. The deepening tasks add depth and the higher grade. Stress: AT2 is submitted *this week*, around Lesson 18. Keep the pseudocode and the trace table. Ask the class: "Pick one mandatory and one deepening — which two?" Write the pair in your notebook. ~2 min.

## Slide 19 — What comes next — Week 7: first real code

Preview Week 7. The pseudocode shape becomes JavaScript or C#. The six keywords get partners in real languages — SET becomes `let` or `int`, IF stays IF, WRITE becomes `console.log` or `Console.WriteLine`. The thinking does not change. Ask the class: "Which language sounds less scary on the title — JavaScript or C#?" ~1 min.

## Slide 20 — Recap — the central question, one more time

Close where you opened. The central question is the same one from Week 1. Pseudocode is the bridge. This week they built it. Next week they walk across it. Ask the class: "How do you speak to a computer so that it understands what you want it to do?" Wait for someone to say "pseudocode." ~1 min.
