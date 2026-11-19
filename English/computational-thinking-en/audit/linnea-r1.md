# Linnea — pedagoginen portti #3, kierros 1

Audit target: Lesson 1 of the Computational Thinking course (English).
Reference: Sune's plan `01-suunnitelma.md`; golden sample `ai-perusteet-md/.../lesson-01`.

## Päätös

hyväksytty

Approve with non-blocking notes. Every audited dimension passes the pedagogical floor. Wilhelm will see the notes below; none of them block the gate.

## Pedagogiset löydökset

1. **AI resilience — Task 1.1 (`student-tasks.md`, lines 5–33).** Pass. The task requires the student's own chosen everyday task, their own 6–10 step instruction, and a real human follower (or self-recorded video). The observation log (Step 3) demands the actual step number, exact ambiguous word, and what the follower did — concrete artefacts an LLM cannot fabricate convincingly. Step 4 (rewrite and re-test on the same follower) doubles the resilience: the student must re-run with the same person and report whether they still got stuck. Pasting this prompt into ChatGPT yields a generic story the teacher can spot in seconds.

2. **AI resilience — Task 1.2 (`student-tasks.md`, lines 37–84).** Pass. Step 2 (lines 56–58) explicitly requires the student to annotate on their own *before touching any AI tool*. Step 3 (lines 60–78) uses the LLM as a sparring partner with a well-formed prompt block (lines 64–76) that instructs the LLM *not* to give answers and to push back with questions. Final reflection asks "did the AI find anything you missed, or did you find things it missed?" — a question that only makes sense if the student did their own pass. Mirrors the golden sample's sparring-partner pattern correctly.

3. **Examples-first principle (`self-study.md`, lines 19–32).** Pass. The "A computer takes you literally" section opens with two everyday examples (sandwich, big tree directions, lines 21–23) before pivoting to two IT examples (`pyhton tutorial` search, missing file path, lines 27–29). Order is correct, examples are age-appropriate.

4. **Central question and conceptual pivot (`self-study.md`, lines 7, 33–41, 51).** Pass. The central question appears verbatim in the introduction (line 7) and is closed in the summary (line 51). The "Ambiguity lives in the instruction" section (lines 33–41) executes Sune's required reframe ("the computer is *literal*, not stupid") without using the forbidden phrase.

5. **Reflection prompts (`self-study.md`, lines 17, 31).** Pass. Two `> **Pause for a moment:**` block quotes, both substantive (one looks backward at today's instructions, one forces the literal-vs-broken reframe). Matches golden-sample pattern.

6. **Learning objectives ↔ self-study coverage (`teacher-materials.md` lines 7–11, `self-study.md`).** Pass. All five objectives are achievable from the self-study alone in a flipped-learning model: define CT (line 13), explain literal interpretation (lines 19–25), give everyday + IT example (lines 21–29), recognize ambiguity-in-instruction (lines 33–41), identify the four core terms (covered in both self-study and vocabulary).

7. **Bloom cap (`teacher-materials.md` lines 7–11).** Pass. All verbs are *define / explain / give / recognize / identify*. No "create / build / design / evaluate / apply / write a program" verbs. Lesson 1 stays in Remembering + Understanding as Sune required.

8. **Misconception coverage (`teacher-materials.md` lines 15–32).** Pass with a small bonus. Five misconceptions instead of the required four, each with a usable "Correction:" line. Misconception 5 ("Being precise just means being long-winded") is original to Rasmus and is a real classroom miss with this age group — good addition.

9. **Coherence — teacher block runs the student tasks (`teacher-materials.md` lines 70–77).** Pass. The 25–55 min pair-activity slot explicitly states "this is the start of Task 1.1". The 75–85 min vocabulary anchoring uses the four core terms that appear in `vocabulary.md`. The 90-minute slots sum to 90.

10. **Vocabulary ↔ self-study (`vocabulary.md`, `self-study.md`).** Pass. All seven required terms are present; *programmer* and *user* added as optional terms; *algorithm* explicitly flagged as "looking ahead — central topic of Lesson 2" (line 27). Every term in vocabulary appears in or is implied by the self-study text.

11. **Volume parity with golden sample.** Pass.
    - `self-study.md`: ~950 words, within the 800–1400 bracket; depth comparable to golden sample.
    - `student-tasks.md`: 5-step task + 4-step deepening task, full prompt block — clearly in the 400–900 bracket and matches golden depth.
    - `vocabulary.md`: 9 terms, each with 2–3 sentences — matches golden's range.
    - `teacher-materials.md`: 5 objectives + 5 misconceptions + facilitation guide + 90-min table + 3 assessment tips — matches or slightly exceeds golden depth.

12. **Support-student fit.** Pass with one note (non-blocking). Task 1.1 is excellent for low-motivation and abstract-struggling students: the artefact (sandwich, tea, hoodie) is concrete, the social setup (a partner) is built in, and reflection is bounded at 3–5 sentences. Note for Wilhelm: Task 1.1 Step 2 offers "record a short video of yourself" as a fallback, but does not mention writing the script as a fallback for students with severe social anxiety or who cannot record. Not a blocker — the teacher block compensates by running the activity in class.

13. **Non-blocking note: vocabulary section ordering.** `vocabulary.md` lists *Programmer* (line 21) and *User* (line 24) before the looking-ahead term *Algorithm* (line 27). Order is fine, but for consistency with the golden sample (which puts the preview term last and visually flagged), this is already correct. No action.

14. **Non-blocking note: Misconception 5 placement.** It is a strong addition but it is also more about *style* than about a misconception about the *computer*. Wilhelm may want to consider whether to keep five or trim to the canonical four. Not blocking.

15. **Non-blocking note: teacher block lacks an "if your school has a real example" prompt expansion.** Sune's brief suggested two-minute story about a real school IT setting. Rasmus mentions it briefly (`teacher-materials.md` lines 39–40) but does not give an example template. Wilhelm may upgrade this for richness; not required.

## Korjausvaatimukset Rasmukselle

None. Material passes the pedagogical gate.

## AI-resilienssin tila

- **Task 1.1 — RECOMMENDED — "The literal robot game": AI-RESILIENT.** Requires an actual human follower (or self-recorded video), the student's own original instructions, three concrete observation entries naming the step number and ambiguous word, and a re-test with the same follower. An LLM submission produces a fictional follower-experience the teacher can detect immediately. Satisfies Sune's criterion 12 via mechanisms (a) own context, (b) physical/observable evidence.

- **Task 1.2 — DEEPENING — "Spot the ambiguity": AI-RESILIENT via sparring-partner pattern.** Student must annotate the six instructions before opening any AI tool (explicit line 58). The provided LLM prompt (lines 64–76) is correctly constructed to forbid the LLM from giving answers and instructs it to push back with questions. Final reflection (lines 80–82) requires the student to compare their own findings against the AI's challenges — an answer that only exists if the student did their own pass. Satisfies criterion 12 via mechanism (c) critique an AI answer rather than produce one, and criterion 13 (sample prompt block + instruction not to accept verbatim).

Both tasks pass the Ehdoton kielto rule: a student who pastes either task verbatim into a language model and submits the output without doing the activity will produce something the teacher can recognise as fabricated, because both tasks demand artefacts (a real follower's behaviour, the student's own pre-AI annotation) that the LLM cannot supply.

## Seuraava

jatka Wilhelmille
