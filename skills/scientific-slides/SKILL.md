---
name: scientific-slides
description: Builds slide decks and presentations for research talks. Used for making PowerPoint slides, conference presentations, seminar talks, research presentations, thesis defense slides, or any scientific talk. Provides slide structure, design templates, timing guidance, and visual validation. Works with PowerPoint and LaTeX Beamer.
allowed-tools: Read Write Edit Bash
license: MIT license
compatibility: Python 3.12+; Pillow for image PDFs, PyMuPDF for rendering, pypdf and python-pptx for validation and template editing. Beamer needs TeX Live/MiKTeX; programmatic PPTX needs Node.js and PptxGenJS; rendering PPTX for review needs LibreOffice. No image-API key is used.
metadata:
  version: "1.12"
  last-reviewed: "2026-10-01"
  skill-author: K-Dense Inc.
---

# Scientific Slides

## Overview

Scientific presentations are a critical medium for communicating research, sharing findings, and engaging with academic and professional audiences. This skill provides comprehensive guidance for creating effective scientific presentations, from structure and content development to visual design and delivery preparation.

**Key Focus**: Oral presentations for conferences, seminars, defenses, and professional talks.

**CRITICAL DESIGN PHILOSOPHY**: Scientific presentations should be VISUALLY ENGAGING and RESEARCH-BACKED. Avoid dry, text-heavy slides at all costs. Great scientific presentations combine:
- **Compelling visuals**: High-quality figures, images, diagrams (not just bullet points)
- **Research context**: Proper citations from research-lookup establishing credibility
- **Minimal text**: Bullet points as prompts, YOU provide the explanation verbally
- **Professional design**: Modern color schemes, strong visual hierarchy, generous white space
- **Story-driven**: Clear narrative arc, not just data dumps

**Remember**: Boring presentations = forgotten science. Make your slides visually memorable while maintaining scientific rigor through proper citations.

## When to Use This Skill

This skill should be used when:
- Preparing conference presentations (5-20 minutes)
- Developing academic seminars (45-60 minutes)
- Creating thesis or dissertation defense presentations
- Designing grant pitch presentations
- Preparing journal club presentations
- Giving research talks at institutions or companies
- Teaching or tutorial presentations on scientific topics

## Building the deck

The OpenRouter image generators (`generate_slide_image.py`, `generate_schematic.py`, and their `_ai` helpers) were removed from this fork. They walked parent directories for `.env` keys and sent slide text to a paid third-party API.

Build the talk with local tools:

- LaTeX Beamer: `assets/beamer_template_conference.tex`, `assets/beamer_template_seminar.tex`, or `assets/beamer_template_defense.tex`. See `references/beamer_guide.md`.
- PowerPoint: `assets/powerpoint_design_guide.md`.
- Diagrams and plots: Mermaid, Graphviz, or matplotlib. Do not invent numerical results in a figure.
- Bundled checks that remain: `scripts/slides_to_pdf.py`, `scripts/pdf_to_images.py`, and `scripts/validate_presentation.py`.

Literature for the talk can come from the free paper-lookup and citation-management skills. research-lookup calls the paid Parallel API and is optional.

---

## Core Capabilities

Presentation structure and organization, slide design principles, data visualization for
slides, talk-specific guidance, implementation options (Beamer / PowerPoint / generated
PDF), visual review and iteration, timing and pacing, and validation are all documented
in [references/slide_capabilities.md](references/slide_capabilities.md).

The staged development process — planning, design and creation, content development,
visual validation, practice and refinement, and final preparation — is in
[references/presentation_workflow.md](references/presentation_workflow.md).

Prompt-writing guidance for both full-slide and visual-only generation is in
[references/prompt_writing.md](references/prompt_writing.md). Every bundled script's
arguments and options are in
[references/script_reference.md](references/script_reference.md). The mistakes that most
often sink a talk are catalogued in
[references/common_pitfalls.md](references/common_pitfalls.md).

## Integration with Other Skills

**Research Lookup** (Critical for Scientific Presentations):
- **Background development**: Search literature to build introduction context
- **Citation gathering**: Find key papers to cite in your talk
- **Gap identification**: Identify what's unknown to motivate research
- **Prior work comparison**: Find papers to compare your results against
- **Supporting evidence**: Locate literature supporting your interpretations
- **Question preparation**: Find papers that might inform Q&A responses
- Literature search is optional. Prefer the free paper-lookup and citation-management skills. research-lookup calls the paid Parallel API; use it only when the user asks for that service.

**Scientific Writing**:
- Convert paper content to presentation format
- Extract key findings and simplify
- Use same figures (but redesigned for slides)
- Maintain consistent terminology

**MarkItDown**:
- Extract the text of an existing template or prior deck before reusing it (`markitdown template.pptx`)

**Data Visualization**:
- Create presentation-appropriate figures
- Simplify complex visualizations
- Ensure readability from distance
- Use progressive disclosure

## Reference Files

Comprehensive guides for specific aspects:

- **`references/presentation_structure.md`**: Detailed structure for all talk types, timing allocation, opening/closing strategies, transition techniques
- **`references/slide_design_principles.md`**: Typography, color theory, layout, accessibility, visual hierarchy, design workflow
- **`references/data_visualization_slides.md`**: Simplifying figures, chart types, progressive disclosure, common mistakes, recreation workflow
- **`references/talk_types_guide.md`**: Specific guidance for conferences, seminars, defenses, grants, journal clubs, with examples
- **`references/beamer_guide.md`**: Complete LaTeX Beamer documentation, themes, customization, advanced features, compilation
- **`references/visual_review_workflow.md`**: PDF to images conversion, systematic inspection, issue documentation, iterative improvement

- **`references/slide_capabilities.md`**: presentation structure, design principles, data visualization, talk types, implementation options, visual review, timing, validation
- **`references/presentation_workflow.md`**: the six development stages from planning to final preparation
- **`references/prompt_writing.md`**: full-slide and visual-only prompt patterns
- **`references/script_reference.md`**: arguments and options for every bundled script
- **`references/common_pitfalls.md`**: content, design, and timing mistakes to avoid

## Assets

### Templates

- **`assets/beamer_template_conference.tex`**: 15-minute conference talk template
- **`assets/beamer_template_seminar.tex`**: 45-minute academic seminar template
- **`assets/beamer_template_defense.tex`**: Dissertation defense template

### Guides

- **`assets/powerpoint_design_guide.md`**: Complete PowerPoint design and implementation guide
- **`assets/timing_guidelines.md`**: Comprehensive timing, pacing, and practice strategies

## Quick Start Guide

### For a 15-Minute Conference Talk

1. **Research & Plan** (45 minutes):
   - **Use research-lookup** to find 8-12 relevant papers for citations
   - Build reference list (background, comparison studies)
   - Outline content (intro → methods → 2-3 key results → conclusion)
   - **Create detailed plan for each slide** (title, key points, visual elements)
   - Target 15-18 slides

2. **Build the slides locally**:
   - Start from a Beamer template in `assets/` or from `assets/powerpoint_design_guide.md`.
   - Draw diagrams with Mermaid, Graphviz, or matplotlib.
   - `scripts/slides_to_pdf.py` only assembles image files you already have. It does not generate them.

3. **Review** (30 minutes):
   - Open the PDF or the deck and read every slide.
   - `scripts/pdf_to_images.py` and `scripts/validate_presentation.py` check layout locally.

4. **Practice** (2-3 hours):
   - Practice 3-5 times with a timer.
   - Aim for 13-14 minutes (leave buffer).

5. **Finalize** (30 minutes):
   - Save the source and the PDF.
   - Test on the presentation computer.

## Summary: Key Principles

1. **Visual-First Design**: Every slide needs strong visual element (figure, image, diagram) - avoid text-only slides
2. **Research-Backed**: Use research-lookup to find 8-15 papers, cite 3-5 in intro, 3-5 in discussion
3. **Modern Aesthetics**: Choose contemporary color palette matching topic, not default themes
4. **Minimal Text**: 3-4 bullets, 4-6 words each (24-28pt font), let visuals tell story
5. **Structure**: Follow story arc, spend 40-50% on results
6. **High Contrast**: 7:1 preferred for professional appearance
7. **Varied Layouts**: Mix full-figure, two-column, visual overlays (not all bullets)
8. **Timing**: Practice 3-5 times, ~1 slide per minute, never skip conclusions
9. **Validation**: Visual review workflow to catch overflow and overlap
10. **White Space**: 40-50% of slide empty for visual breathing room

**Remember**: 
- **Boring = Forgotten**: Dry, text-heavy slides fail to communicate your science
- **Visual + Research = Impact**: Combine compelling visuals with research-backed context
- **You are the presentation, slides are visual support**: They should enhance, not replace your talk
