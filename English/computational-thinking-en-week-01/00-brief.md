# Brief — Computational Thinking course, Week 1 (English)

## Working title
Computational Thinking

## Purpose
Give beginning vocational IT students (~15 years old) a conceptual understanding of how programming works, before they learn an actual programming language in depth. Core question: *How do I speak to a computer so that it understands what I want it to do?*

## Target group
- First-year vocational ICT students, age ~15–17.
- No prior programming competence assumed; basic ICT skills only.
- May include students with support needs, low school motivation, or difficulty with abstract concepts.

## Output language
**English.** Börje (Finnish polishing) is skipped for this run.

## Course duration
8 weeks × 3 lessons × 90 min = 24 lessons.

## Test scope (this run)
- **Sune**: produce the Week 1 plan (covers L1–L3 as one weekly package) plus forward-looking stubs for weeks 2–8.
- **Rasmus**: build the **full Week 1 package** in the new canonical week-XX structure.
- **Linnea/Wilhelm**: audit Week 1.
- **Alfred**: package Week 1 release with slides.

## Canonical block structure per week (locked)
```
student/week-XX/
├── overview.md         # weekly theme + core minimum vs. deepening
├── self-study.md       # 3 lessons of theory in one document
├── student-tasks.md    # 1–2 🟢 RECOMMENDED + 2–3 🟣 DEEPENING tasks
├── vocabulary.md       # week's vocabulary
└── slides.md           # Markdown slide deck for the week (---)
teacher/week-XX/
├── teacher-materials.md  # 3 × 90 min facilitation
└── in-class-tasks.md     # ≥1 mandatory teacher-led in-class exercise
```

## Week 1 — Computational thinking (locked lesson topics)
- **L1**: What does computational thinking mean? Humans, computers, and interpreting instructions.
- **L2**: Algorithms in everyday life: step-by-step instructions without code.
- **L3**: Precise and imprecise instructions: testing and improving instructions.

## Week 1 specifics
- **Bloom cap**: Remembering + Understanding only. Applying may appear lightly in L2 (writing first algorithms in natural language) and L3 (testing and rewriting), but not as the dominant verb in objectives.
- **Central question** must appear verbatim somewhere in self-study.md and in the slide deck.
- **Concrete examples**: everyday before IT, always.
- **30–50% rule**: in teacher-materials.md, every 90-min lesson plan must allocate 30–50% to independent student work in class (not just lecture + group work).

## Tasks (this week)
- **RECOMMENDED (1–2)**: mandatory minimum, AI-resilient, each one anchored in the student's own context or producing observable artefacts.
- **DEEPENING (2–3)**: optional extension. May lean on LLM-as-sparring-partner with structured prompts, may dig into edge cases or vocational angles. Still AI-resilient.

## Slides
Produce `slides.md` with `---` as slide separators. Each slide: clear H1/H2 title plus minimal supporting content (3–5 short bullets or 1–2 short sentences). Aim ~10–20 slides for the whole week. Slides are for in-class use; they do not replace self-study.

## Out of scope
- No automatic testing/debugging frameworks (jest, mocha, vitest).
- No PowerPoint creation directly — Rasmus writes `slides.md` (Markdown); the orchestrator converts to PPTX.
- No IDE setup, no Node.js install.
- No platform-side independent exercises (those are produced by a different team).
- No deep CS theory.

## Language register
- Self-study + student-tasks: CEFR ~B1.
- Teacher-materials + in-class-tasks: CEFR ~B2.
- Slides: B1, very short sentences.

## Golden sample (for all gates — structure, depth, content volume)
`/Users/agent/ai-perusteet-md/` — Tekoälyn perusteet, Business College Helsinki, deployed to Netlify.
- The week-level volume is roughly **3×** a single golden-sample lesson (since one Week-1 self-study covers 3 lessons of content).
- Reference is for style/depth/volume only — do not copy content. Output language is English; reference is Finnish.

## Status of the earlier Lesson 1 test run
A prior pipeline run produced a per-lesson Lesson 1 output at:
`/Users/agent/material-pipeline/output/computational-thinking-en/release/`
This Week 1 run **replaces** that approach with the new weekly granularity. The earlier output is kept as historical record only and is not part of this release.
