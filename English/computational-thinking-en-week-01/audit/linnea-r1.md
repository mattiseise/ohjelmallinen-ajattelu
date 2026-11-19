# Linnea — Pedagogical audit (R1) — Week 1, Computational Thinking (EN)

Auditor: Linnea (gate #3, pedagogical gate)
Run: R1
Date: 2026-05-20
Scope: Week 1 package (7 files) against Sune's locked plan `01-suunnitelma.md`.

---

## Päätös

**korjattava**

The package is pedagogically strong, structurally complete, and 9 of 10 audit
dimensions pass cleanly. One blocking issue: **Task 1.2 ("Spot the ambiguity")
fails the AI-resilience rule** — it is solvable by pasting the five generic
instructions verbatim into an LLM and submitting the output. Under the absolute
rule set for this gate, that alone forces a return to Rasmus, even though the
fix is small (≈5 minutes of editing). Everything else is approved.

---

## Pedagogiset löydökset

### 1. AI resilience — Task 1.1 is exemplary (PASS)
`student-tasks.md:13–41`. Task 1.1 ("The literal robot game", RECOMMENDED, AI-resilient)
requires (a) a personal real-life task the student already does daily, (b) a real
follower (classmate, sibling, parent, or self on video), (c) observable artefacts —
exact word-level notes of where the follower got stuck, including step number,
the ambiguous phrase, and what the follower did. An LLM cannot fabricate the
follower's hesitation in a way the teacher cannot detect, because the artefact
chain (instruction → follower's literal misread → student's word-level note)
encodes real-world friction. This is the highest possible AI-resilience grade
and matches the plan's design (`01-suunnitelma.md:263–268, 289`).

### 2. AI resilience — Task 1.2 FAILS the absolute rule (FAIL — blocker)
`student-tasks.md:45–89`. Task 1.2 ("Spot the ambiguity", DEEPENING) presents
five generic ambiguous instructions verbatim in the file (lines 57–61):

```
1. "Save the file in the usual place."
2. "Reply to him about it before the weekend."
3. "Make the button a bit bigger."
4. "Send the homework when you're done."
5. "Open the window a little."
```

The required deliverable (`student-tasks.md:51–55`) is for each instruction:
(a) which word is ambiguous, (b) two literal interpretations, (c) a rewrite.

**This is pasteable verbatim into ChatGPT/Claude and the output is submission-ready.**
There is no student-specific anchor (no own context, no real follower, no
observable artefact, no critique-the-LLM mechanism required as the *primary*
artefact). The LLM-sparring block (`student-tasks.md:63–83`) is explicitly
optional and acts as a *second pass*, not as the work itself. The audit rule
("no task may be solvable by pasting verbatim into an LLM and submitting the
output") allows no exception for deepening tasks.

The fix is small (see Korjausvaatimukset below). The task is otherwise
pedagogically valuable and should be kept after the fix.

### 3. AI resilience — Task 1.3 is borderline but acceptable (PASS, marginal)
`student-tasks.md:93–115`. Task 1.3 ("Two algorithms, one goal") is anchored
by the student picking a goal "you have at least two real ways of reaching"
(line 99) and writing about their *own* routes/processes. An LLM could
produce two plausible algorithms for any common goal, but the comparison
question — "Which one would you give to someone who has never done this task
before, and why?" (line 106) — cuts against pure paste-and-submit because it
requires a real-world judgement tied to the student's choice. Not the strongest
AI-resilience, but acceptable for a DEEPENING task. **No action required.**

### 4. AI resilience — Task 1.4 is strong (PASS)
`student-tasks.md:118–141`. Task 1.4 ("Vocational angle: help-desk instruction",
DEEPENING, AI-resilient) requires the exact UI of the student's own school
(line 124: "the exact name of buttons, menu items and pages as they appear in
your school's software") and a real classmate as tester (line 126). An LLM
cannot know the school's actual portal screen or fabricate the tester's
real-time confusion. Properly AI-resilient.

### 5. MANDATORY in-class task genuinely requires the classroom (PASS)
`in-class-tasks.md:14–46`. Activity A ("Literal robot live") is whole-class,
teacher-led, with an embodied volunteer following ambiguous instructions
literally in front of the class. The "Why it requires the classroom" rationale
(line 45) is correct: the embodied public moment of literal interpretation is
the pedagogical engine. It cannot be replaced by homework or by an LLM. Properly
cross-referenced from `teacher-materials.md:89` (L1 warm-up) and
`teacher-materials.md:133, 139` (L3 full version).

### 6. 30–50% independent-work rule — all three plans pass arithmetically (PASS)
- L1: `teacher-materials.md:82` — Independent work 0:25–0:55 = **30 min (33%)**. In range.
- L2: `teacher-materials.md:107` — Independent work 0:25–1:00 = **35 min (39%)**. In range.
- L3: `teacher-materials.md:132` — Independent work 0:25–0:55 = **30 min (33%)**. In range.

All three blocks are explicitly labelled `**Independent work**` in the schedule
table and are genuinely independent (writing alone, not pair/group/lecture).
Time slots sum to 90 in each lesson. Rule met.

### 7. Pedagogical coherence across the 7 files (PASS)
Vocabulary terms in `vocabulary.md` (computational thinking, instruction, computer
as instruction-follower, literal interpretation, ambiguity, algorithm, goal, input,
step, output, precision, imprecise instruction, test, edge case, literal-robot game,
decomposition — 16 terms) all appear in context in `self-study.md` and in tasks.
Slides (`slides.md:9–11, 174–176`) state the central question verbatim twice as
required. The self-study story (sandwich → big tree → typo search → missing slash)
is mirrored by slides 5–7 (`slides.md:31–60`). `teacher-materials.md` runs the
exact activities described in `student-tasks.md` (Task 1.1 drafted in L1 independent
work, line 82; in-class Activity A in L3, line 133). `overview.md` core-minimum
section (`overview.md:18–22`) matches `self-study.md` summary (`self-study.md:163–169`)
and `student-tasks.md` framing (`student-tasks.md:5–7`). Cross-file pedagogical
threads hold.

### 8. Examples-first principle (PASS)
`self-study.md:29–41` opens Lesson 1's examples block with two everyday examples
(sandwich line 31, big tree line 33), *then* the IT examples (typo search line 37,
missing slash line 39). Order is correct.
`self-study.md:69–85` Lesson 2 leads with everyday (tea recipe line 73, route line
77, morning routine line 79) before the IT mirror (help-desk script line 83).
`self-study.md:121–135` Lesson 3 lists the four ambiguity patterns with everyday
examples *first* (line 125 vague nouns, 127 deictic, 129 relative time, 131 vague
quantity), then the IT mirror in a single paragraph at line 133. Three for three.
Slides mirror the same order (`slides.md:31–38, 41–50` everyday before IT).

### 9. Bloom cap (PASS)
`teacher-materials.md:9–35`. All L1 verbs are Remembering/Understanding (define,
explain, give, recognize). L2 adds light Applying (write) for the algorithm-writing
objective only — explicitly permitted by the plan. L3 adds light Applying (rewrite,
test). No forbidden verbs (create, build, design, develop, evaluate, judge, analyze,
decompose, abstract, debug) appear in any objective. Confirmed at line 35: "higher
Bloom levels — *Analyzing* (Week 4), *Creating* (final assessed task, Week 8) —
are deliberately not in scope this week."

### 10. Misconception coverage (PASS)
`teacher-materials.md:39–69`. **Seven** misconceptions across the week:
- L1: "computer is stupid" (line 45) + "CT = programming" (line 48). [2]
- L2: "algorithms only for computer scientists" (line 53) + "must be long" (line 56). [2]
- L3: "imprecise means short" (line 61) + "sounds right = is right" (line 64). [2]
- Bonus: "adding 'please' helps" (line 67). [1]

Each has an explicit "Correction:" line. Plan requires ≥6 across the week with
≥2 per lesson — met with one to spare. Quality of corrections is high (the
"please/kindly" misconception in particular is a useful unprompted addition).

### 11. Core minimum vs. deepening clearly separated (PASS)
`overview.md:18–28` uses two clearly labelled bullet lists. `student-tasks.md:5–7`
marks 🟢 RECOMMENDED as mandatory minimum and 🟣 DEEPENING as optional.
`slides.md:142–151` has a dedicated "Core minimum vs. deepening" slide. The
separation is visible at every level a student encounters the material.

### 12. Support-student fit (PASS)
The core-minimum tasks (Task 1.1 only — Task 1.2 is DEEPENING in the shipped
selection) anchor in a task the student already does daily (`student-tasks.md:21`:
"making a cup of tea or coffee, logging in to the school portal on your phone,
sending a message on Discord or WhatsApp"). Self-study leads with the sandwich
scene (`self-study.md:5`) which is concretely accessible at CEFR B1. The
"if you truly cannot find anyone, record yourself on video" fallback
(`student-tasks.md:23`) is a thoughtful low-friction option for students with
low social capital or anxiety. Sentence length and vocabulary in
`overview.md`, `self-study.md`, `vocabulary.md`, `student-tasks.md`,
`slides.md` read at ~B1 throughout.

### 13. Volume / depth vs golden sample (PASS)
- Golden sample (1 lesson): self-study 877 words, vocabulary 260, student-tasks 820,
  teacher-materials 624. Total ~2581 words.
- Week 1 (3 lessons): self-study 3692, vocabulary 813, student-tasks 1643,
  teacher-materials 3248, overview 398, slides 772, in-class-tasks 1177.
- Self-study ratio: 3692 / 877 ≈ **4.2×** golden (target: ~3×; week has more
  conceptual ground to cover, ratio is justified).
- Teacher-materials ratio: 3248 / 624 ≈ **5.2×** golden (target: ~3×; week
  includes three 90-min plans instead of one, ratio is justified).
- All seven files within the volume brackets set by `01-suunnitelma.md:128–137`.

### 14. Slide structure (PASS)
`slides.md` — counting `---` separators: **18 separators → 19 slides** (within
10–20). Title slide present (lines 1–7). Central question verbatim on slide 2
(line 11) and recap slide (line 176). All slides separated by `---` on their
own line. No `.pptx` references, no Reveal.js syntax, no embedded speaker-note
syntax. Body content stays at 3–5 short bullets or 1–2 short sentences as
required.

### 15. "Stupid/dumb" framing rule — nuanced (PASS, with note)
Plan rule (`01-suunnitelma.md:180`): "the phrase 'the computer is stupid / dumb'
must not appear; the framing must be 'the computer is literal'".

The word "stupid" appears 5 times in `teacher-materials.md` (lines 41, 45, 46,
158, 180) and once in `student-tasks.md` (line 9). **In every occurrence it is
either inside quotation marks as a misconception being explicitly named and
refuted, or it is the contrast pole in "literal, not stupid".** This is the
intended pedagogical move — name the bad framing in order to displace it. The
plan's misconception list itself (`01-suunnitelma.md:355` "L1: 'The computer
is stupid.' → Correction: literal, not stupid.") explicitly requires this
treatment in `teacher-materials.md`. Reading Rasmus's text in good faith, the
rule is honoured: the *framing* of the course is literal-not-stupid. **No
correction required.** A Wilhelm grep will flag the word; Wilhelm should accept
the explicit-correction context.

### 16. Forbidden topics — confirmed absent (PASS)
No mentions of jest/mocha/vitest/pytest/automatic testing frameworks anywhere
in the 7 files. No Big-O, Turing machines, formal grammars. No flowcharts, no
pseudocode, no variables, no loops, no programming-language names in Week 1.
No `.pptx`, `.key`, `deck.md`, Reveal.js HTML, or media directory references.
The phrase "computational thinking is just programming" is pre-empted in
`self-study.md:25` and `teacher-materials.md:48`. Clean.

### 17. Required H2 section structures — spot-checked (PASS)
- `overview.md`: Week 1 theme (line 3) / What you will be able to do (line 7) /
  Core minimum vs. deepening (line 16) / How the three lessons fit together
  (line 29). Order correct.
- `self-study.md`: Introduction (line 3) / Lesson 1 (line 17) / Lesson 2 (line 61) /
  Lesson 3 (line 109) / Summary (line 161). Order correct. Four `Pause for a
  moment` prompts at lines 57, 85, 105, 157 (≥1 per lesson, total ≥4). Met.
- `student-tasks.md`: Overview (line 3) / 4 task H2s (lines 13, 45, 93, 118).
  Each task ends with `### Keep your notes` block referencing AT1 at end of
  Week 2 (lines 39, 87, 112, 138). Met.
- `vocabulary.md`: Single H2 `## Week 1 vocabulary` (line 3), 16 terms as H3.
  Decomposition flagged "*(looking ahead — central topic of Week 2)*" (line 52). Met.
- `teacher-materials.md`: Bloom-mapped objectives (line 9) / Common misconceptions
  (line 39) / three 90-min plans (lines 72, 97, 122) / Facilitation tips (line 147)
  / Formative assessment (line 173). Substantively matches required sections;
  "Common student questions" content lives inside Facilitation tips (line 163)
  rather than under its own H2. **Minor structural deviation, not blocking.**
- `in-class-tasks.md`: Overview (line 3), Activity A MANDATORY (line 14),
  Activity B OPTIONAL (line 49). Met.

### 18. Central question verbatim (PASS)
Required form: *"How do I speak to a computer so that it understands what I want
it to do?"*
- `self-study.md:11` — verbatim in Introduction.
- `self-study.md:163` — verbatim in Summary ("You started this week with a
  question:").
- `slides.md:11` — verbatim on central-question slide.
- `slides.md:176` — verbatim on recap slide.
Met four times. Plan only required twice.

---

## Korjausvaatimukset Rasmukselle

**Single required change.** Rewrite Task 1.2 so it cannot be solved by pasting
the five instructions into an LLM and submitting the output. Two acceptable
fixes (pick one):

### Fix option A — anchor the five instructions in the student's own context (preferred)

Replace `student-tasks.md:51–61` so that the student must **collect** five real
ambiguous instructions from their own life this week, instead of being handed
generic ones. Suggested wording:

> Over the next two to three days, **collect five ambiguous instructions you
> have actually received or given this week** — in a chat, an email, a
> classroom announcement, a help-desk reply, a sticky note on the fridge, a
> WhatsApp from a parent. Copy each one into your notes **with one sentence of
> context** (who said it to whom and in what situation). For each:
> (a) which word or phrase is ambiguous, (b) at least two different things a
> literal follower might do, (c) a rewritten version that removes the ambiguity.

This adds an unfakeable real-world artefact (the instruction *plus its
context*) and makes the task at least as AI-resilient as Task 1.1. Keep the
optional LLM-sparring block; it now operates on student-supplied raw material,
which is what the plan envisaged.

### Fix option B — make the critique-the-LLM step mandatory and the primary artefact

Restructure Task 1.2 so the *primary* deliverable is the **student's written
disagreement** with the LLM, not the analysis itself. The student first asks
the LLM to do its own analysis of the five instructions, then writes — for at
least three of the LLM's annotations — a sentence explaining what the LLM
missed, over-claimed, or got wrong, with evidence (a literal-follower
counterexample, an edge case the LLM ignored). The artefact is the *critique
record*, not the annotations. Keep the sample prompt.

This satisfies the rule because pasting the original task into an LLM produces
something the *follow-on rubric* explicitly demands be argued against, which
the LLM cannot do on behalf of the student without leaving fingerprints.

### Smaller follow-on (nice to fix while editing)

`teacher-materials.md` does not have a dedicated `## Answers to common student
questions` H2 — the content exists inline at line 163 under "Common student
questions during class" within "Facilitation tips". Plan
`01-suunnitelma.md:167–168` listed it as its own H2. This is not pedagogically
material but Wilhelm may flag the H2 structure deviation. Suggest promoting it
to its own `## Answers to common student questions` H2.

---

## AI-resilienssin tila

Per-task verdict:

| Task | Tier | Verdict | Evidence |
|---|---|---|---|
| 1.1 — The literal robot game (RECOMMENDED) | 🟢 PASS — exemplary | Real follower or self-video required; observable word-level artefact of where follower got literally misled; student's own daily routine as topic; rewrite + re-test loop. | `student-tasks.md:21–27` |
| 1.2 — Spot the ambiguity (DEEPENING) | 🔴 FAIL — blocker | Five generic instructions printed verbatim in the file; deliverable is annotation; no real-world anchor; LLM sparring is optional second pass. Solvable by paste-and-submit. | `student-tasks.md:51–61` |
| 1.3 — Two algorithms, one goal (DEEPENING) | 🟡 PASS — marginal | Student picks own real-life goal with two ways of reaching it; comparison includes "who would you give it to and why" which resists pure LLM output. Could be tightened but acceptable for DEEPENING. | `student-tasks.md:99–106` |
| 1.4 — Help-desk instruction (DEEPENING) | 🟢 PASS — strong | Real school portal/UI required by name; real classmate as tester; observable break-points; rewrite + re-test loop. | `student-tasks.md:124–128` |

**Overall:** 3 of 4 tasks pass; 1 of 4 fails the absolute paste-and-submit rule.
Under the gate's rule ("Reject any task that fails this") the package must be
returned to Rasmus.

---

## Seuraava

**palauta Rasmukselle korjattavaksi**

Send the package back to Rasmus with the single required fix to Task 1.2 (pick
option A or B above; A is preferred). The fix is small — Rasmus can turn this
around quickly. Once Task 1.2 is anchored in real student context or made
critique-primary, the package is approved for Wilhelm.

The optional H2 promotion of "Answers to common student questions" in
`teacher-materials.md` is a courtesy fix Rasmus may bundle with the Task 1.2
edit but it is not gate-blocking from the pedagogical side; Wilhelm decides
whether to insist.

All other pedagogical dimensions are clean. Do not re-litigate them on the
return pass.
