#!/usr/bin/env python3
"""Build a styled HTML + PDF from the 5 lesson files for the training team."""

import re
from pathlib import Path
import markdown
from weasyprint import HTML, CSS

BASE = Path("/sessions/awesome-stoic-allen/mnt/agent/material-pipeline/output/computational-thinking-en-week-01")
ROOT = BASE / "release"
OUT_HTML = BASE / "week-01-bundle.html"
OUT_PDF = BASE / "week-01-bundle.pdf"

SECTIONS = [
    ("readme",    "Course overview",        "README.md",                              ROOT / "README.md"),
    ("overview",  "Week 1 — orientation",   "student/week-01/overview.md",            ROOT / "student/week-01/overview.md"),
    ("self",      "Self-study material",    "student/week-01/self-study.md",          ROOT / "student/week-01/self-study.md"),
    ("tasks",     "Student tasks",          "student/week-01/student-tasks.md",       ROOT / "student/week-01/student-tasks.md"),
    ("vocab",     "Vocabulary",             "student/week-01/vocabulary.md",          ROOT / "student/week-01/vocabulary.md"),
    ("teacher",   "Teacher materials",      "teacher/week-01/teacher-materials.md",   ROOT / "teacher/week-01/teacher-materials.md"),
    ("inclass",   "In-class tasks",         "teacher/week-01/in-class-tasks.md",      ROOT / "teacher/week-01/in-class-tasks.md"),
]

MD = markdown.Markdown(extensions=["extra", "sane_lists", "tables", "toc"])


def md_to_html(text: str) -> str:
    """Render markdown to HTML, then post-process to tag special blockquotes."""
    html = MD.convert(text)
    MD.reset()

    # Tag "Pause for a moment" blockquotes
    html = re.sub(
        r'<blockquote>\s*<p>\s*<strong>Pause for a moment:?</strong>',
        '<blockquote class="pause"><p><strong>Pause for a moment:</strong>',
        html,
    )
    # Tag tip blockquotes
    html = re.sub(
        r'<blockquote>\s*<p>(?:💡\s*)?<strong>Tip:?</strong>',
        '<blockquote class="tip"><p><strong>Tip:</strong>',
        html,
    )
    # Tag "This is an optional deepening task" blockquote
    html = re.sub(
        r'<blockquote>\s*<p>\s*<strong>This is an optional deepening task\.</strong>',
        '<blockquote class="note"><p><strong>This is an optional deepening task.</strong>',
        html,
    )
    # Style MANDATORY / DEEPENING task labels as colored pills inside H2 headings
    html = re.sub(
        r'(<h2[^>]*>[^<]*?)\s*🟢\s*MANDATORY\s*(</h2>)',
        r'\1<span class="pill pill-mandatory">MANDATORY</span>\2',
        html,
    )
    html = re.sub(
        r'(<h2[^>]*>[^<]*?)\s*🟣\s*DEEPENING\s*(</h2>)',
        r'\1<span class="pill pill-deepening">DEEPENING</span>\2',
        html,
    )
    return html


def cover_block() -> str:
    return """
<section class="cover">
  <div class="cover-eyebrow">Pipeline release · Week 1</div>
  <h1 class="cover-title">Computational Thinking</h1>
  <p class="cover-subtitle">Speaking to a computer — what does it actually hear?</p>
  <div class="cover-question">
    <span class="cover-question-label">The course turns around one question</span>
    <p class="cover-question-text">How do I speak to a computer so that it understands what I want it to do?</p>
  </div>
  <dl class="cover-meta">
    <dt>Audience</dt><dd>First-year vocational ICT students, age ~15–17</dd>
    <dt>Course shape</dt><dd>8 weeks · 3 lessons / week · 90 min / lesson</dd>
    <dt>This bundle</dt><dd>Week 1 — lessons 1–3 in one weekly package</dd>
    <dt>Language</dt><dd>English (Finnish-language polishing skipped for this run)</dd>
  </dl>
  <div class="cover-footer">
    <span>Material Pipeline · Cowork edition</span>
    <span>Built for training-team review</span>
  </div>
</section>
"""


def toc_block() -> str:
    items = "\n".join(
        f'<li><span class="toc-num">{i+1:02}</span> <a href="#sec-{slug}">{title}</a>'
        f'<span class="toc-path">{path}</span></li>'
        for i, (slug, title, path, _) in enumerate(SECTIONS)
    )
    return f"""
<section class="toc">
  <h1>Contents</h1>
  <ol class="toc-list">
    {items}
  </ol>
</section>
"""


def section_block(slug: str, title: str, path: str, body_html: str, index: int) -> str:
    return f"""
<section class="lesson-section" id="sec-{slug}">
  <header class="section-header">
    <div class="section-eyebrow">Part {index:02} · {path}</div>
    <h1 class="section-title">{title}</h1>
  </header>
  <div class="section-body">
    {body_html}
  </div>
</section>
"""


CSS_TEXT = r"""
@page {
  size: A4;
  margin: 22mm 20mm 22mm 20mm;
  @bottom-left {
    content: "Computational Thinking · Week 1";
    font-family: 'Inter', 'Helvetica Neue', sans-serif;
    font-size: 8.5pt;
    color: #8a8470;
  }
  @bottom-right {
    content: counter(page) " / " counter(pages);
    font-family: 'Inter', 'Helvetica Neue', sans-serif;
    font-size: 8.5pt;
    color: #8a8470;
  }
}

/* No header/footer on cover */
@page :first {
  @bottom-left { content: ""; }
  @bottom-right { content: ""; }
  margin: 0;
}

/* TOC page also clean */
@page toc-page {
  @bottom-left { content: ""; }
  @bottom-right { content: ""; }
}
.toc { page: toc-page; }

html, body {
  margin: 0;
  padding: 0;
  font-family: 'Inter', 'Segoe UI', 'Helvetica Neue', sans-serif;
  font-size: 10.5pt;
  line-height: 1.55;
  color: #1f1d18;
  background: white;
}

/* === Cover === */
.cover {
  page: cover;
  page-break-after: always;
  height: 297mm;
  width: 210mm;
  box-sizing: border-box;
  padding: 32mm 28mm 28mm 28mm;
  background:
    radial-gradient(circle at 12% 8%, #fef0c8 0%, transparent 38%),
    radial-gradient(circle at 88% 95%, #cfe2ff 0%, transparent 38%),
    linear-gradient(180deg, #fbf8f1 0%, #f5efe1 100%);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.cover-eyebrow {
  font-size: 10pt;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #7a6d50;
  font-weight: 600;
}
.cover-title {
  font-family: 'Fraunces', 'Georgia', serif;
  font-size: 56pt;
  line-height: 1.02;
  margin: 8mm 0 4mm 0;
  font-weight: 600;
  letter-spacing: -0.02em;
  color: #20201c;
}
.cover-subtitle {
  font-family: 'Fraunces', 'Georgia', serif;
  font-style: italic;
  font-size: 19pt;
  line-height: 1.3;
  margin: 0 0 22mm 0;
  color: #4a4538;
  max-width: 130mm;
}
.cover-question {
  background: white;
  border: 1px solid #e6dbb8;
  border-left: 6px solid #c08b2c;
  padding: 9mm 11mm;
  margin: 0 0 12mm 0;
  box-shadow: 0 2px 0 rgba(0,0,0,0.03);
}
.cover-question-label {
  display: block;
  font-size: 8.5pt;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #9a8a5d;
  margin-bottom: 4mm;
  font-weight: 600;
}
.cover-question-text {
  font-family: 'Fraunces', 'Georgia', serif;
  font-size: 22pt;
  line-height: 1.25;
  margin: 0;
  color: #20201c;
  font-weight: 500;
}
.cover-meta {
  display: grid;
  grid-template-columns: 32mm 1fr;
  gap: 2.5mm 8mm;
  font-size: 10pt;
  margin: 0;
}
.cover-meta dt {
  color: #7a6d50;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  font-size: 8.5pt;
  font-weight: 600;
  padding-top: 0.4mm;
}
.cover-meta dd {
  margin: 0;
  color: #2c2a23;
}
.cover-footer {
  display: flex;
  justify-content: space-between;
  font-size: 8.5pt;
  color: #8a8470;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  border-top: 1px solid #d8c898;
  padding-top: 5mm;
  margin-top: 8mm;
}

/* === Table of contents === */
.toc {
  page-break-after: always;
  padding-top: 8mm;
}
.toc h1 {
  font-family: 'Fraunces', 'Georgia', serif;
  font-size: 28pt;
  margin: 0 0 12mm 0;
  font-weight: 600;
  letter-spacing: -0.01em;
  color: #20201c;
}
.toc-list {
  list-style: none;
  padding: 0;
  margin: 0;
  counter-reset: toc;
}
.toc-list li {
  display: grid;
  grid-template-columns: 14mm 1fr 1fr;
  align-items: baseline;
  padding: 5mm 0;
  border-top: 1px solid #ecdfb8;
  gap: 8mm;
  font-size: 11.5pt;
}
.toc-list li:last-child { border-bottom: 1px solid #ecdfb8; }
.toc-num {
  font-family: 'Fraunces', 'Georgia', serif;
  font-size: 14pt;
  color: #c08b2c;
  font-weight: 600;
}
.toc-list a {
  font-family: 'Fraunces', 'Georgia', serif;
  font-size: 14pt;
  color: #20201c;
  text-decoration: none;
  font-weight: 500;
}
.toc-path {
  font-family: 'JetBrains Mono', 'Menlo', monospace;
  font-size: 8.5pt;
  color: #8a8470;
  text-align: right;
}

/* === Section header === */
.lesson-section {
  page-break-before: always;
}
.section-header {
  border-bottom: 2px solid #c08b2c;
  padding-bottom: 6mm;
  margin-bottom: 8mm;
}
.section-eyebrow {
  font-size: 8.5pt;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #7a6d50;
  font-weight: 600;
  margin-bottom: 3mm;
  font-family: 'JetBrains Mono', 'Menlo', monospace;
}
.section-title {
  font-family: 'Fraunces', 'Georgia', serif;
  font-size: 32pt;
  line-height: 1.05;
  margin: 0;
  font-weight: 600;
  letter-spacing: -0.015em;
  color: #20201c;
}

/* === Body typography === */
.section-body h1, .section-body h2, .section-body h3, .section-body h4 {
  font-family: 'Fraunces', 'Georgia', serif;
  font-weight: 600;
  color: #20201c;
  letter-spacing: -0.005em;
  page-break-after: avoid;
}
.section-body h1 {
  font-size: 22pt;
  margin: 12mm 0 4mm 0;
  border-bottom: 1px solid #ecdfb8;
  padding-bottom: 2mm;
}
.section-body h2 {
  font-size: 17pt;
  margin: 9mm 0 3mm 0;
  color: #2c2a23;
}
.section-body h3 {
  font-size: 13pt;
  margin: 6mm 0 2mm 0;
  color: #3a3528;
}
.section-body h4 {
  font-size: 11pt;
  margin: 5mm 0 1.5mm 0;
  color: #5a533f;
  text-transform: none;
  letter-spacing: 0.01em;
}
.section-body p {
  margin: 0 0 3mm 0;
  text-align: justify;
  hyphens: auto;
  orphans: 3;
  widows: 3;
}
.section-body strong { color: #20201c; }
.section-body em { color: #4a4538; }

.section-body ul, .section-body ol {
  margin: 1.5mm 0 4mm 0;
  padding-left: 7mm;
}
.section-body li {
  margin: 0.8mm 0;
  page-break-inside: avoid;
}

.section-body a {
  color: #8a5a1a;
  text-decoration: none;
  border-bottom: 1px dotted #c08b2c;
}

/* === Tables === */
.section-body table {
  border-collapse: collapse;
  width: 100%;
  margin: 4mm 0 5mm 0;
  font-size: 9.5pt;
  page-break-inside: avoid;
}
.section-body th {
  background: #f5efe1;
  color: #2c2a23;
  text-align: left;
  padding: 2.5mm 3mm;
  border-bottom: 2px solid #c08b2c;
  font-weight: 600;
}
.section-body td {
  padding: 2.5mm 3mm;
  border-bottom: 1px solid #ecdfb8;
  vertical-align: top;
}
.section-body tr:nth-child(even) td { background: #faf6ec; }

/* === Code blocks === */
.section-body pre {
  background: #1f1d18;
  color: #f5efe1;
  font-family: 'JetBrains Mono', 'Menlo', monospace;
  font-size: 9pt;
  line-height: 1.45;
  padding: 4mm 5mm;
  border-radius: 1.5mm;
  overflow-x: auto;
  margin: 4mm 0;
  page-break-inside: avoid;
}
.section-body pre code { color: inherit; background: none; padding: 0; }
.section-body code {
  font-family: 'JetBrains Mono', 'Menlo', monospace;
  font-size: 9.5pt;
  background: #f5efe1;
  padding: 0.4mm 1.4mm;
  border-radius: 0.8mm;
  color: #5a3a0a;
}

/* === Blockquote variants === */
.section-body blockquote {
  margin: 4mm 0;
  padding: 4mm 6mm;
  border-left: 4px solid #c0c0b0;
  background: #fbf8f1;
  font-style: italic;
  color: #3a3528;
  page-break-inside: avoid;
}
.section-body blockquote p { margin: 0 0 2mm 0; }
.section-body blockquote p:last-child { margin: 0; }

.section-body blockquote.pause {
  border-left-color: #4080c0;
  background: #f0f5fc;
  font-style: normal;
  position: relative;
}
.section-body blockquote.pause::before {
  content: "Reflection";
  display: block;
  font-size: 7.5pt;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #4080c0;
  font-weight: 700;
  margin-bottom: 2mm;
  font-style: normal;
}

.section-body blockquote.tip {
  border-left-color: #c08b2c;
  background: #fdf5e0;
  font-style: normal;
}
.section-body blockquote.tip::before {
  content: "Tip";
  display: block;
  font-size: 7.5pt;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #8a5a1a;
  font-weight: 700;
  margin-bottom: 2mm;
}

.section-body blockquote.note {
  border-left-color: #8a5a9a;
  background: #f6f0fa;
  font-style: normal;
}

/* === Task label pills (RECOMMENDED / DEEPENING) === */
.section-body h2 .pill {
  display: inline-block;
  vertical-align: middle;
  font-family: 'Inter', 'Helvetica Neue', sans-serif;
  font-size: 9.5pt;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: white;
  padding: 1.2mm 3.5mm 0.8mm 3.5mm;
  border-radius: 100mm;
  margin-left: 3mm;
  position: relative;
  top: -1mm;
  text-transform: uppercase;
  line-height: 1;
}
.section-body h2 .pill-mandatory {
  background: #2ea15a;
}
.section-body h2 .pill-deepening {
  background: #8052c8;
}

/* === HR === */
.section-body hr {
  border: 0;
  border-top: 1px solid #ecdfb8;
  margin: 8mm 0;
}

/* Avoid orphaned headings near page breaks */
h1 + p, h2 + p, h3 + p, h4 + p { page-break-before: avoid; }
"""


def main():
    body_parts = [cover_block(), toc_block()]
    for i, (slug, title, path, src) in enumerate(SECTIONS):
        raw = src.read_text(encoding="utf-8")
        body_parts.append(section_block(slug, title, path, md_to_html(raw), i + 1))

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Computational Thinking — Lesson 1 bundle</title>
</head>
<body>
{''.join(body_parts)}
</body>
</html>"""

    OUT_HTML.write_text(html, encoding="utf-8")
    print(f"HTML: {OUT_HTML}")

    HTML(filename=str(OUT_HTML)).write_pdf(
        str(OUT_PDF),
        stylesheets=[CSS(string=CSS_TEXT)],
    )
    print(f"PDF:  {OUT_PDF}")


if __name__ == "__main__":
    main()
