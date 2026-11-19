# Wilhelm — auditor (Cowork-portti #4), kierros 1

Audit target: Lesson 1 of the Computational Thinking course (English).
Reference: Sune's plan `01-suunnitelma.md` (17 criteria in `## Hyväksymiskriteerit`); Linnea passed the pedagogical gate.

## Päätös

approved

## Blocking-löydökset

None. All 17 acceptance criteria pass.

### Walk-through of all 17 criteria

1. **Four canonical files, exact filenames.** Pass. `ls` of `student/lesson-01/` returns exactly `self-study.md`, `student-tasks.md`, `vocabulary.md`; `teacher/lesson-01/` returns exactly `teacher-materials.md`. All lowercase, kebab-case, no typos.
2. **No extra files.** Pass. Directory listing shows only the three student files and one teacher file. No `slides.md`, no images directory, no stray drafts.
3. **`teacher-led-tasks.md` correctly absent.** Pass. Not required for Lesson 1, not present.
4. **`self-study.md` 800–1400 words, intro + 3–5 body H2 + summary, ≥2 reflection prompts.** Pass. `wc -w` reports 1307 words (within bracket). H2 headings: `Introduction`, `What is computational thinking?`, `A computer takes you literally`, `Ambiguity lives in the instruction, not in the computer`, `Why this matters for an IT professional`, `Summary` — i.e. intro + 4 body + summary. Two `> **Pause for a moment:**` block quotes at lines 17 and 31.
5. **`student-tasks.md` 400–900 words, 1–2 tasks, recommended/deepening split.** Pass. `wc -w` reports 900 words (top of bracket but inside). Two tasks: `Task 1.1 — The literal robot game 🟢 RECOMMENDED` (line 5) and `Task 1.2 — Spot the ambiguity 🟣 DEEPENING` (line 37). Labels translated to English as plan permitted.
6. **`vocabulary.md` 6–10 terms, ≥1 looking-ahead preview.** Pass. 9 H2 terms; `Algorithm — *looking ahead, central topic of Lesson 2*` flagged at line 27. Each term has a 1–3 sentence definition (verified by inspection).
7. **`teacher-materials.md` 800–1400 words, all required H2 sections.** Pass. `wc -w` reports 1397 words (top end, inside bracket). Required H2 sections all present: `Learning objectives for this lesson` (line 3), `Common misconceptions` (line 15), `Teacher facilitation guide` (line 34) with H3 `Before class`/`During class`/`Answers to common student questions` (lines 36, 43, 52), `A realistic 90-minute lesson structure` (line 66), `Assessment tips` (line 81).
8. **≥2 everyday examples and ≥2 IT examples in `self-study.md`, everyday first.** Pass. Everyday examples: charger on the kitchen table (line 5), sandwich-with-cheese-outside (line 21), "turn left at the big tree" (line 23). IT examples: `pyhton tutorial` search typo (line 27), missing file path `report-final.docx` (line 29). Everyday block (lines 21–25) precedes IT block (lines 27–29).
9. **Central question verbatim in intro and/or summary.** Pass. Appears verbatim in the introduction at line 7 (bolded) and the summary at line 51 (italicised).
10. **Establishes "computer is literal, ambiguity is in the instruction".** Pass. Section `Ambiguity lives in the instruction, not in the computer` (lines 33–41) explicitly states "The computer is not dumb. The computer is *literal*" (line 37) and "Ambiguity is a property of what you wrote" (line 39).
11. **Bloom cap: Remembering + Understanding only.** Pass. `teacher-materials.md` lines 7–11 use only `define`, `explain`, `give`, `recognize`, `identify`. Bloom tags in parentheses are only "Remembering" or "Understanding". No `create`, `build`, `design`, `apply`, `evaluate`, `analyze`.
12. **1–2 tasks, ≥1 AI-resilient.** Pass. Task 1.1 requires the student's own 6–10 step instruction plus a real human follower or self-recorded video (lines 13, 15–19), step-by-step observation notes citing step number and exact ambiguous word (line 23), and a re-test with the same follower (line 27) — satisfies mechanisms (a) own context and (b) physical/observable evidence. Task 1.2 also resilient via sparring-partner pattern (Linnea's audit confirms).
13. **Sparring-partner task includes fenced sample prompt + instruction not to accept output verbatim.** Pass. `student-tasks.md` lines 64–76 contain a fenced code block with a properly scoped sparring-partner prompt. Line 78: "Do not accept whatever the AI says — it is wrong often enough to keep you on your toes." Line 58 forbids touching AI before own pass.
14. **Teacher block: Bloom-mapped objectives, ≥4 misconceptions with corrections, 90-minute slots summing to 90.** Pass. Objectives Bloom-tagged (lines 7–11). Five misconceptions, each with "**Correction:**" line (lines 19, 22, 25, 28, 31). Slot sum: 0–10 + 10–25 + 25–55 + 55–75 + 75–85 + 85–90 = 10 + 15 + 30 + 20 + 10 + 5 = **90 min** (verified arithmetically; teacher file confirms "Total: 90 minutes." at line 79).
15. **English throughout in Rasmus's output.** Pass. All four lesson files reviewed end-to-end. Section headings, body prose, table headers, and reflection prompts are English. No Finnish words present (grepped `ja|tai|että|Pysähdy|Johdanto|hetkeksi` against the materials dir — only false positives matching the English word "on" and similar). The plan file's Finnish section labels (`Suunnitelma`, `Rajaukset`) are out of scope for this criterion.
16. **No slide deck references anywhere.** Pass. Recursive case-insensitive grep for `slide|powerpoint|keynote|reveal|pptx|slides\.md` across `materiaali/` returned zero matches.
17. **Markdown validity: code fences close, tables render, no broken links.** Pass. Code-fence count is even in every file (self-study 0, student-tasks 2, vocabulary 0, teacher-materials 0). The single markdown table in `teacher-materials.md` (lines 70–77) has well-formed header + separator + 6 data rows of 3 columns each. No external links to break.

## Non-blocking-parannukset

1. **(Linnea, carried forward) Task 1.1 Step 2 fallback for severe social anxiety.** A "write the script and read it to yourself out loud" option is missing alongside the existing "record a video" fallback. Teacher block covers it in-class, but the student-facing text should name the third path. Alfred/Börje can patch in one line.
2. **(Linnea, carried forward) Misconception 5 ("Being precise just means being long-winded") is stylistic rather than about the *computer*.** It is a good addition, but a future pass might either trim back to four canonical computer-misconceptions or relabel it as a "writing pitfall". Not blocking.
3. **(Linnea, carried forward) `Before class` two-minute story prompt is mentioned but not given a template.** `teacher-materials.md` lines 38–39 nudges the teacher to bring a real IT-incident story, but no skeleton or example is provided. Adding two sentences of scaffolding would help less experienced teachers.
4. **(Wilhelm) Word-count headroom is thin on `student-tasks.md` (900 / 900) and `teacher-materials.md` (1397 / 1400).** Both are inside Sune's bracket but at the ceiling. Any future expansion (e.g. the social-anxiety fallback above) risks pushing them over. Worth tracking — not a finding.
5. **(Wilhelm) Linnea's word-count estimate for `self-study.md` was "~950 words"; actual is 1307.** Both numbers sit inside the 800–1400 bracket, so no criterion violation. Flag only because it suggests Linnea's spot-check used a different counter; orchestrator may want to standardise word-count tooling for future rounds.
6. **(Wilhelm) Vocabulary preview marker is in the H2 itself.** `## Algorithm — *looking ahead, central topic of Lesson 2*` works, but a golden-sample-style block quote ("> Preview term — see Lesson 2") under a clean `## Algorithm` heading would be more parser-friendly for downstream tooling (e.g. an auto-generated glossary). Cosmetic.
7. **(Wilhelm) Missing criterion in Sune's spec — no explicit rule on emoji usage.** Rasmus uses 🟢, 🟣, 📌, 💡. Golden sample uses similar markers, and the plan implicitly permits them (criterion 5 says "Rasmus may translate the labels"). Surface to orchestrator for the next pipeline run if emoji policy should be made explicit. Not blocking.

## Tarkistettu evidenssi

**Files read in full:**
- `/Users/agent/material-pipeline/output/computational-thinking-en/01-suunnitelma.md` (Sune's plan, all 17 criteria in `## Hyväksymiskriteerit`)
- `/Users/agent/material-pipeline/output/computational-thinking-en/audit/linnea-r1.md` (Linnea's audit, all pedagogical findings + non-blocking notes)
- `/Users/agent/material-pipeline/output/computational-thinking-en/materiaali/student/lesson-01/self-study.md`
- `/Users/agent/material-pipeline/output/computational-thinking-en/materiaali/student/lesson-01/student-tasks.md`
- `/Users/agent/material-pipeline/output/computational-thinking-en/materiaali/student/lesson-01/vocabulary.md`
- `/Users/agent/material-pipeline/output/computational-thinking-en/materiaali/teacher/lesson-01/teacher-materials.md`

**Spot-checks executed:**
- `ls` of both `student/lesson-01/` and `teacher/lesson-01/` to confirm exactly 4 files and no extras (criteria 1, 2, 3).
- `wc -w` on every Rasmus file (criteria 4, 5, 6 implicit, 7). Counts: 1307 / 900 / 329 / 1397.
- `grep -n "^## "` on `self-study.md`, `vocabulary.md`, and `teacher-materials.md` to confirm required section headings (criteria 4, 7, 14).
- `grep -c "Pause for a moment"` on `self-study.md` → 2 (criterion 4).
- Verbatim search for the central question in `self-study.md` (criterion 9): hits at lines 7 and 51.
- Time-slot arithmetic on the 90-minute table (criterion 14): 10 + 15 + 30 + 20 + 10 + 5 = 90.
- Recursive case-insensitive grep `(slide|powerpoint|keynote|reveal|pptx|slides\.md)` across `materiaali/` (criterion 16): zero matches.
- Finnish-word grep across the four output files (criterion 15): zero true positives.
- Code-fence balance check on all four files (criterion 17): all even.
- Manual inspection of the markdown table in `teacher-materials.md` (criterion 17): well-formed.

**Criteria verified individually:** 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17. None skipped.

## Seuraava

jatka Alfredille
