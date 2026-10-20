# Bundled Script Reference

Arguments and options for `slides_to_pdf.py`, `validate_presentation.py`, and `pdf_to_images.py`. The OpenRouter slide-image scripts were removed.

The OpenRouter slide and schematic generators were removed from this fork. Build decks with the Beamer templates in `assets/` or with PowerPoint. The scripts below check and assemble local files.

### slides_to_pdf.py

Combine multiple slide images into a single PDF.

```bash
# Combine PNG files
python scripts/slides_to_pdf.py slides/*.png -o presentation.pdf

# Combine specific files in order
python scripts/slides_to_pdf.py title.png intro.png methods.png -o talk.pdf

# From directory (sorted by filename)
python scripts/slides_to_pdf.py slides/ -o presentation.pdf
```

**Options:**
- `-o, --output`: Output PDF path (required)
- `--dpi`: PDF resolution (default: 150)
- `-v, --verbose`: Verbose output

**Ordering:** Explicit file arguments retain their given order. Each directory/glob expands in filename order; duplicates are removed at their first occurrence.

**Tip:** Name slides with numbers for correct ordering: `01_title.png`, `02_intro.png`, etc.

---

## Tools and Scripts

**slides_to_pdf.py** - Combine slide images into PDF:
```bash
# From glob pattern
python scripts/slides_to_pdf.py slides/*.png -o presentation.pdf

# From directory (sorted by filename)
python scripts/slides_to_pdf.py slides/ -o presentation.pdf

# Options:
# -o, --output    Output PDF path (required)
# --dpi N         PDF resolution (default: 150)
# -v, --verbose   Verbose output
```

### Validation Scripts

**validate_presentation.py**:
```bash
python scripts/validate_presentation.py presentation.pdf --duration 15

# Checks:
# - Slide count vs. recommended range
# - File size warnings
# - Slide dimensions
# - Font sizes (PowerPoint)
# - Compilation (Beamer)
```

**pdf_to_images.py**:
```bash
python scripts/pdf_to_images.py presentation.pdf output/slide --dpi 150

# Converts PDF to images for visual inspection
# Supports: JPG, PNG
# Adjustable DPI
# Page range selection
```

### Validation limits and external PowerPoint tools

`validate_presentation.py` supports PDF, PPTX and TEX. Convert legacy PPT to PPTX/PDF
first. It counts PDF pages (including Beamer overlays/appendices), not conceptual frames;
its timing guidance is only a rehearsal aid. Font checks inspect explicit text-run sizes,
not inherited theme sizes, tables, groups, reading order or text overflow. TEX validation
runs one `pdflatex -no-shell-escape` pass; resolve citations and navigation with `latexmk`
or the full bibliography build before delivery.

`pdf_to_images.py` uses the current `pymupdf` import and `get_pixmap(dpi=...)`;
`--first`/`--last` are inclusive and 1-based. Invalid ranges and nonpositive DPI fail.
`slides_to_pdf.py` uses Pillow's `save_all`/`append_images`; DPI controls page dimensions,
not new image detail. All input slides should share an aspect ratio and pixel size.

To review a PPTX deck, export it to PDF in PowerPoint or LibreOffice
(`soffice --headless --convert-to pdf deck.pptx`) and use the bundled PDF renderer.

Sources: [PyMuPDF rendering](https://pymupdf.readthedocs.io/en/latest/recipes-images.html),
[Pillow PDF](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#pdf),
[python-pptx presentations](https://python-pptx.readthedocs.io/en/latest/user/presentations.html),
[pypdf reader](https://pypdf.readthedocs.io/en/latest/modules/PdfReader.html).

### External Tools

**Recommended**:
- PDF viewer: For reviewing presentations
- Color contrast checker: WebAIM Contrast Checker
- Color blindness simulator: Coblis
- Timer app: For practice sessions
- Screen recorder: For self-review
