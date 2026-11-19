## Slide 1 — Lesson 21 — The age-limit check, three times

Frame this supplement. Lesson 21 introduces if/else in code. This deck walks one tiny algorithm — an age-limit check — three times: first in pseudocode, then in JavaScript, then in C#. Tell the class: "Same algorithm, three skins. Watch the thinking stay still." This is the exact shape AT3 will use. ~1 min.

## Slide 2 — The Week-6 pseudocode we already know

Read the six-line block. READ age. IF age >= 18 THEN write enter-message; ELSE write reject-message; ENDIF. Tell the class: "A friend can follow this. A computer cannot — the words 'READ' and 'WRITE' and 'ENDIF' are not in its dictionary." This sets up the need for a real language. Ask the class: "Which line is the input? Which is the test?" Quick answers. ~3 min.

## Slide 3 — Step 1 — JavaScript, line by line

Walk the JavaScript translation. `let age = 16;` hard-codes the input — we are not asking the user yet. `if (age >= 18) {` is the IF. `console.log("You may enter.");` is the WRITE for the true branch. `} else {` is the ELSE. The closing `}` is the ENDIF. Note the keyword maps under the block. Ask the class: "Why hard-code age instead of asking?" Steer to: keeps the focus on the if/else; we will add input later. ~3 min.

## Slide 4 — Step 2 — C#, line by line

Now the same algorithm in C#. `int age = 16;` — almost identical, but with the type word. `if (age >= 18) {` — identical syntax to JS. `Console.WriteLine("You may enter.");` — capital C, capital W, parentheses, semicolon. Else and closing brace match. Stress: the only differences are `int` vs `let` and `Console.WriteLine` vs `console.log`. Ask the class: "Which two lines are the only real differences from the JS version?" ~3 min.

## Slide 5 — What is the same in all three?

The thinking. Read the four bullets. Test, then-block, else-block — same structure. The `>=` comparison — same operator. The two messages — same words. The top-to-bottom order — same flow. Tell the class: "Once you spot the shape, all three look like cousins, not strangers." Ask the class: "Which would you bet is the easiest of the three to read for a non-programmer?" Pseudocode usually wins. ~3 min.

## Slide 6 — What is different?

Read the four bullets. A real value instead of READ. The print function name. The C# type word. Curly braces replacing THEN/ELSE/ENDIF. Stress: these are *surface* differences — the syntax. The thinking does not change. Tell the class: "When a syntax error pops up, ask which bullet on this slide you got wrong." Ask the class: "Which difference do you think trips students up most?" Often: forgetting the semicolon or the closing brace. ~3 min.

## Slide 7 — Predict — then run

Live demo or write on the board. Set age to 16. Predict the output. Then run. Output: "Sorry, you are not old enough." Now change age to 19. Predict. Run. Output switches to "You may enter." Tell the class: "If both predictions matched, you just dry-ran code. Same skill as Week 6." Ask the class: "Predict the output for age = 18." Answer: "You may enter." — because `>=`, not `>`. ~3 min.

## Slide 8 — Hand-off to AT3

End by pointing forward. AT3 in Week 8 will ask them to take one piece of their own Week 6 pseudocode that has an IF/ELSE and turn it into a running program. The walkthrough they just saw *is* the shape AT3 expects. Tell the class: "Save the code you wrote today. It is the seed of next week's submission." Ask the class: "Which Week 6 pseudocode of yours has an IF/ELSE you could translate?" ~3 min.
