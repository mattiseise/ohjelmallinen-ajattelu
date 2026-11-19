#!/usr/bin/env python3
"""Convert slides.md (Markdown with --- separators) into a styled PPTX deck."""

import re
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

BASE = Path("/sessions/awesome-stoic-allen/mnt/agent/material-pipeline/output/computational-thinking-en-week-01")

# Decks to render. Each entry: (input_md, output_pptx, eyebrow_label).
DECKS = [
    (BASE / "release/student/week-01/slides.md",
     BASE / "week-01-slides.pptx",
     "WEEK 1 · PIPELINE RELEASE"),
    (BASE / "release/student/week-01/slides-l2-algorithm-walkthrough.md",
     BASE / "week-01-slides-l2-algorithm-walkthrough.pptx",
     "WEEK 1 · LESSON 2 · SUPPLEMENT"),
]

# 16:9 widescreen, 13.333 x 7.5 inches
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

# Palette
COLOR_BG_CREAM = RGBColor(0xFB, 0xF8, 0xF1)
COLOR_BG_DEEP = RGBColor(0x20, 0x20, 0x1C)
COLOR_TEXT = RGBColor(0x20, 0x20, 0x1C)
COLOR_TEXT_LIGHT = RGBColor(0xF5, 0xEF, 0xE1)
COLOR_ACCENT = RGBColor(0xC0, 0x8B, 0x2C)
COLOR_MUTED = RGBColor(0x7A, 0x6D, 0x50)
COLOR_BLUE = RGBColor(0x40, 0x80, 0xC0)


def parse_slides(text: str):
    """Split slide markdown by --- separators. Returns list of (title, body_lines)."""
    raw_slides = re.split(r'(?m)^---\s*$', text)
    slides = []
    for raw in raw_slides:
        raw = raw.strip()
        if not raw:
            continue
        lines = raw.split("\n")
        title = ""
        body = []
        for ln in lines:
            ln = ln.rstrip()
            if not title and ln.startswith("# "):
                title = ln[2:].strip()
            elif not title and ln.startswith("## "):
                title = ln[3:].strip()
            elif ln.strip():
                body.append(ln)
        slides.append((title, body))
    return slides


def add_bg(slide, color):
    """Fill slide background with a solid colour rectangle (PPTX has no first-class slide BG color via py-pptx easily; rectangle hack)."""
    rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H)
    rect.fill.solid()
    rect.fill.fore_color.rgb = color
    rect.line.fill.background()  # no border
    # send to back is non-trivial; py-pptx adds new shapes on top by default, so add bg FIRST.
    return rect


def _runs_from_markdown(line: str):
    """Yield (text, bold, italic) tuples from inline-markdown text."""
    # Tokenize **bold** and *italic* (italic must not greedy across boundaries)
    pattern = re.compile(r'(\*\*[^*]+\*\*|\*[^*]+\*)')
    pos = 0
    for m in pattern.finditer(line):
        if m.start() > pos:
            yield (line[pos:m.start()], False, False)
        token = m.group(0)
        if token.startswith("**") and token.endswith("**"):
            yield (token[2:-2], True, False)
        else:
            yield (token[1:-1], False, True)
        pos = m.end()
    if pos < len(line):
        yield (line[pos:], False, False)


def add_text(slide, x, y, w, h, text, *, font="Calibri", size=18, bold=False, italic=False,
             color=COLOR_TEXT, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Pt(0)
    tf.margin_right = Pt(0)
    tf.margin_top = Pt(0)
    tf.margin_bottom = Pt(0)
    tf.vertical_anchor = anchor
    paras = text.split("\n")
    for i, line in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        for chunk_text, chunk_bold, chunk_italic in _runs_from_markdown(line):
            if not chunk_text:
                continue
            run = p.add_run()
            run.text = chunk_text
            run.font.name = font
            run.font.size = Pt(size)
            run.font.bold = bold or chunk_bold
            run.font.italic = italic or chunk_italic
            run.font.color.rgb = color
    return tb


def add_bullets(slide, x, y, w, h, lines, *, font="Calibri", size=18, color=COLOR_TEXT):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Pt(0); tf.margin_right = Pt(0); tf.margin_top = Pt(0); tf.margin_bottom = Pt(0)
    for i, raw in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(8)
        # Strip leading bullet marker if any
        text = re.sub(r'^\s*[-*]\s+', '', raw).strip()
        chunks = re.split(r'(\*\*[^*]+\*\*)', text)
        # bullet glyph
        bullet_run = p.add_run()
        bullet_run.text = "•  "
        bullet_run.font.name = font
        bullet_run.font.size = Pt(size)
        bullet_run.font.color.rgb = COLOR_ACCENT
        bullet_run.font.bold = True
        for c in chunks:
            if not c:
                continue
            run = p.add_run()
            if c.startswith("**") and c.endswith("**"):
                run.text = c[2:-2]
                run.font.bold = True
            else:
                run.text = c
            run.font.name = font
            run.font.size = Pt(size)
            run.font.color.rgb = color
    return tb


def add_accent_bar(slide, x, y, w, h, color=COLOR_ACCENT):
    rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    rect.fill.solid()
    rect.fill.fore_color.rgb = color
    rect.line.fill.background()
    return rect


def is_bullet_block(body):
    """Body is bullets if a majority of non-empty lines begin with '-' or '*'."""
    nonempty = [ln for ln in body if ln.strip()]
    if not nonempty:
        return False
    bullets = sum(1 for ln in nonempty if re.match(r'^\s*[-*]\s+', ln))
    return bullets >= max(2, len(nonempty) // 2)


def emit_cover(slide, eyebrow, title, subtitle, footer):
    add_bg(slide, COLOR_BG_CREAM)
    # gold left bar
    add_accent_bar(slide, Inches(0), Inches(0), Inches(0.4), SLIDE_H, COLOR_ACCENT)
    add_text(slide, Inches(1.0), Inches(0.9), Inches(11), Inches(0.5),
             eyebrow.upper(),
             font="Calibri", size=14, bold=True, color=COLOR_MUTED)
    add_text(slide, Inches(1.0), Inches(1.6), Inches(11), Inches(3.0),
             title,
             font="Cambria", size=72, bold=True, color=COLOR_TEXT, anchor=MSO_ANCHOR.TOP)
    add_text(slide, Inches(1.0), Inches(4.3), Inches(11), Inches(1.2),
             subtitle,
             font="Cambria", size=28, italic=True, color=RGBColor(0x4A, 0x45, 0x38))
    add_text(slide, Inches(1.0), Inches(6.7), Inches(11), Inches(0.5),
             footer,
             font="Calibri", size=12, color=COLOR_MUTED)


def emit_question(slide, title, body):
    """Featured large-quote slide for the central question."""
    add_bg(slide, COLOR_BG_DEEP)
    add_text(slide, Inches(1.0), Inches(0.9), Inches(11), Inches(0.5),
             "THE CENTRAL QUESTION",
             font="Calibri", size=14, bold=True, color=COLOR_ACCENT)
    quote = " ".join(b for b in body if b.strip())
    add_text(slide, Inches(1.0), Inches(2.0), Inches(11), Inches(4.5),
             quote,
             font="Cambria", size=46, italic=True, bold=False, color=COLOR_TEXT_LIGHT,
             anchor=MSO_ANCHOR.MIDDLE)
    add_text(slide, Inches(1.0), Inches(6.7), Inches(11), Inches(0.5),
             "Computational Thinking · Week 1",
             font="Calibri", size=12, color=RGBColor(0x9A, 0x8A, 0x5D))


def emit_content(slide, title, body, slide_index, total):
    add_bg(slide, COLOR_BG_CREAM)
    add_accent_bar(slide, Inches(0.8), Inches(0.9), Inches(0.18), Inches(0.9), COLOR_ACCENT)
    add_text(slide, Inches(1.2), Inches(0.85), Inches(11), Inches(1.0),
             title,
             font="Cambria", size=36, bold=True, color=COLOR_TEXT, anchor=MSO_ANCHOR.MIDDLE)
    # Detect dense bodies (many items / numbered lists) and use smaller font.
    nonempty = [b for b in body if b.strip()]
    numbered = sum(1 for ln in nonempty if re.match(r'^\s*\d+\.\s+', ln))
    is_numbered_list = numbered >= max(2, len(nonempty) // 2)

    if is_bullet_block(body):
        size = 19 if len(nonempty) > 5 else 22
        add_bullets(slide, Inches(1.2), Inches(2.4), Inches(11), Inches(4.4),
                    nonempty, font="Calibri", size=size, color=COLOR_TEXT)
    elif is_numbered_list:
        text = "\n".join(nonempty)
        add_text(slide, Inches(1.2), Inches(2.4), Inches(11), Inches(4.4),
                 text, font="Calibri", size=20, color=COLOR_TEXT, anchor=MSO_ANCHOR.TOP)
    else:
        text = "\n\n".join(nonempty)
        add_text(slide, Inches(1.2), Inches(2.4), Inches(11), Inches(4.4),
                 text, font="Cambria", size=24, color=COLOR_TEXT, anchor=MSO_ANCHOR.TOP)
    add_text(slide, Inches(11.8), Inches(6.85), Inches(1.2), Inches(0.4),
             f"{slide_index:02} / {total:02}",
             font="Calibri", size=10, color=COLOR_MUTED, align=PP_ALIGN.RIGHT)
    add_text(slide, Inches(0.8), Inches(6.85), Inches(8), Inches(0.4),
             "Computational Thinking · Week 1",
             font="Calibri", size=10, color=COLOR_MUTED)


def render_deck(in_md: Path, out_pptx: Path, eyebrow: str):
    md = in_md.read_text(encoding="utf-8")
    parsed = parse_slides(md)
    print(f"Parsed {len(parsed)} slides from {in_md.name}")

    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    blank = prs.slide_layouts[6]
    total = len(parsed)

    for idx, (title, body) in enumerate(parsed, 1):
        slide = prs.slides.add_slide(blank)
        if idx == 1:
            subtitle = body[0] if body else ""
            footer = body[1] if len(body) > 1 else "Computational Thinking"
            emit_cover(slide, eyebrow, title, subtitle, footer)
        elif "central question" in title.lower():
            emit_question(slide, title, body)
        elif "recap" in title.lower() and "central question" in " ".join(body).lower():
            emit_question(slide, title, body)
        else:
            emit_content(slide, title, body, idx, total)

    prs.save(str(out_pptx))
    print(f"Saved: {out_pptx}")


def main():
    for in_md, out_pptx, eyebrow in DECKS:
        render_deck(in_md, out_pptx, eyebrow)


if __name__ == "__main__":
    main()
