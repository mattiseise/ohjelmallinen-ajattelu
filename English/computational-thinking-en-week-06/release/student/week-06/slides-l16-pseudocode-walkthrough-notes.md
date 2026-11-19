## Slide 1 — Worked example — making tea

Frame the supplement. Lesson 16 introduced pseudocode in the abstract; this short deck walks one example end to end, from English paragraph to clean pseudocode. The tea recipe is the spine — same one we used in Week 1 with instant noodles and again on the main deck. Tell the class: "By the end of these six slides you will have a template you can copy for AT2." ~1 min.

## Slide 2 — In English

Read the paragraph as you would tell a friend over coffee. Five sentences, all clear to a human. Then point at the two trip-wires: "wait until it clicks" — how long? "if you take sugar" — how does the computer know? Tell the class: a human friend fills in those gaps from context; a computer cannot. Ask the class: "Where else in the paragraph would a computer get stuck?" Examples: "the bag," "the water." ~3 min.

## Slide 3 — In pseudocode — the skeleton

Walk the twelve lines slowly. READ takesSugar is the input. SET kettleOn is processing. WHILE… ENDWHILE is the wait loop with an observable test. SET bagInMug stays processing. WRITE lines are output. IF takesSugar… ENDIF is the condition. Stress: the IF and the WHILE from Week 5 are visible at a glance. Ask the class: "Which line was the trip-wire 'until it clicks' from the English?" Answer: the WHILE block. ~3 min.

## Slide 4 — Naming the parts

Now we put labels on the regions. One INPUT line at the top. PROCESSING in the middle. OUTPUT lines at the end. This is the L17 skeleton showing up early — input, processing, output. Tell the class: this three-band shape is the structure of most pseudocode and most real code. Ask the class: "Why is there only one READ but several WRITEs?" Steer to: we ask once, then we narrate the steps. ~3 min.

## Slide 5 — What got more precise

Three concrete tightenings. "The kettle" became a named state we can check. "If you take sugar" became a YES/NO variable. "Three minutes" became its own WRITE line instead of a side comment. Stress the trade-off: pseudocode is longer than English, but less guessing. Ask the class: "Is longer-but-clearer always better? When is shorter better?" Steer to: a poster needs shorter; a recipe a stranger follows needs longer. ~3 min.

## Slide 6 — The template scales

Show that the skeleton is universal. Help-desk triage, password check, daily backup — all three reuse the same input/processing/output shape with different keywords inside. Tell the class: "If you can pseudocode making tea, you can pseudocode triaging a ticket. The shape is the shape." Ask the class: "Pick one of the three vocational examples — which input does it READ?" ~3 min.
