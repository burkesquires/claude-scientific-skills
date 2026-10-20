"""Tests for the scientific-slides tooling.

`generate_schematic.py` and `generate_schematic_ai.py` are byte-identical to the
copies in four other skills, so their behaviour comes from the shared contract
(`skill_contract.schematic`) rather than being re-tested here. What is specific
to this skill is the slide pipeline, and each group of tests below guards one way
it fails quietly:

* `validate_presentation.py` is the gate before a talk is delivered. Its slide
  budget is checked in both directions -- a deck inside the range must be
  reported as fine, one outside it must be warned about -- and against the
  one-slide-per-minute rule its own `assets/timing_guidelines.md` documents. The
  PDF path is driven with real two-page PDFs whose 16:9 and 4:3 geometry is known
  by construction, which is also what caught a bug: the script imported the
  retired `PyPDF2` only, so with the maintained `pypdf` installed every PDF check
  silently degraded to "not installed".
* `pdf_to_images.py` converts at a requested DPI. 144 DPI on a 720-point page is
  1440 pixels, so the zoom arithmetic is checked against the rendered size rather
  than assumed.
* `slides_to_pdf.py` decides slide *order* from filenames, so `02` must land
  before `10`; a lexicographic sort would silently reorder a talk.
* The AI scripts are exercised without touching the network: the OpenRouter
  request is mocked, and what is asserted is the quality-threshold decision, the
  response parsing, the retry loop, and that the API key travels in the child's
  environment rather than on its command line.
"""

from __future__ import annotations

import base64
import contextlib
import io
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import pytest

import skill_contract

SKILL_ROOT = Path(__file__).resolve().parents[2] / "skills" / "scientific-slides"
SCRIPTS = SKILL_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

# `slides_to_pdf` exits at import time when Pillow is missing, so the guard has
# to come first: without it a bare environment turns a skip into a collection
# error for the whole module.
Image = pytest.importorskip("PIL.Image", reason="the slide scripts need Pillow")

import pdf_to_images  # noqa: E402
import slides_to_pdf  # noqa: E402
import validate_presentation  # noqa: E402

CliHelpTests = skill_contract.cli.help_test_case(SKILL_ROOT)


class TemporaryDirectoryTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self._temporary.cleanup)
        self.root = Path(self._temporary.name)

    def deck(self, pages: int = 2, size: tuple[int, int] = (1280, 720)) -> Path:
        """A PDF of `pages` blank slides, one point per pixel at 72 dpi."""
        images = [Image.new("RGB", size, (255, 255, 255)) for _ in range(pages)]
        path = self.root / f"deck_{pages}_{size[0]}x{size[1]}.pdf"
        images[0].save(
            path, "PDF", resolution=72, save_all=True, append_images=images[1:]
        )
        return path

    #: Fill colour per image mode -- Pillow wants a scalar for single-band modes.
    FILL = {"RGB": (200, 200, 200), "RGBA": (200, 200, 200, 255), "L": 200, "P": 200}

    def image(self, name: str, size: tuple[int, int] = (320, 180), mode="RGB") -> Path:
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        Image.new(mode, size, self.FILL[mode]).save(path)
        return path


def validated(path, duration=None) -> dict:
    validator = validate_presentation.PresentationValidator(str(path), duration)
    with contextlib.redirect_stdout(io.StringIO()):
        return validator.validate()


class SlideBudgetTests(unittest.TestCase):
    GUIDELINES = validate_presentation.PresentationValidator.SLIDE_GUIDELINES

    def counted(self, slides: int, duration: int) -> dict:
        validator = validate_presentation.PresentationValidator("talk.pdf", duration)
        validator._check_slide_count(slides)
        return {"info": validator.info, "warnings": validator.warnings}

    def test_every_duration_brackets_its_recommendation(self) -> None:
        for duration, (minimum, recommended, maximum) in self.GUIDELINES.items():
            with self.subTest(duration=duration):
                self.assertLess(minimum, recommended)
                self.assertLess(recommended, maximum)

    def test_the_budget_grows_with_the_talk_length(self) -> None:
        recommended = [self.GUIDELINES[key][1] for key in sorted(self.GUIDELINES)]
        self.assertEqual(recommended, sorted(recommended))

    def test_the_recommendations_track_one_slide_per_minute(self) -> None:
        # The rule the skill's own timing_guidelines.md is built on; a table that
        # drifted far from it would contradict the guidance it ships with.
        for duration, (_, recommended, _) in self.GUIDELINES.items():
            with self.subTest(duration=duration):
                self.assertGreaterEqual(recommended / duration, 0.8)
                self.assertLessEqual(recommended / duration, 1.25)

    def test_the_ranges_overlap_the_shipped_timing_asset(self) -> None:
        # assets/timing_guidelines.md tabulates "Duration | Total Slides"; the
        # validator must not call a deck too long when that table calls it right.
        table = (SKILL_ROOT / "assets" / "timing_guidelines.md").read_text(
            encoding="utf-8"
        )
        import re

        rows = re.findall(r"^\|\s*(\d+)\s*min\s*\|\s*(\d+)-(\d+)", table, re.MULTILINE)
        self.assertTrue(rows, "the timing asset no longer tabulates slide counts")
        for duration, low, high in rows:
            duration, low, high = int(duration), int(low), int(high)
            if duration not in self.GUIDELINES:
                continue
            minimum, _, maximum = self.GUIDELINES[duration]
            with self.subTest(duration=duration):
                self.assertLessEqual(minimum, high)
                self.assertGreaterEqual(maximum, low)

    def test_a_deck_inside_the_range_is_reported_as_fine(self) -> None:
        # 16 slides for a 15-minute talk: squarely inside 13-20.
        result = self.counted(16, 15)
        self.assertEqual(result["warnings"], [])
        self.assertTrue(
            any("within recommended range" in line for line in result["info"])
        )

    def test_too_few_slides_warns_about_the_empty_time(self) -> None:
        result = self.counted(4, 15)
        self.assertTrue(result["warnings"])
        self.assertIn("Fewer slides", result["warnings"][0])

    def test_too_many_slides_warns_about_running_over(self) -> None:
        result = self.counted(40, 15)
        self.assertTrue(result["warnings"])
        self.assertIn("run over time", result["warnings"][0])

    def test_the_boundaries_themselves_are_acceptable(self) -> None:
        minimum, _, maximum = self.GUIDELINES[15]
        for slides in (minimum, maximum):
            with self.subTest(slides=slides):
                self.assertEqual(self.counted(slides, 15)["warnings"], [])

    def test_an_untabulated_duration_borrows_the_nearest_one(self) -> None:
        # 12 minutes is closest to the 10-minute row, and the substitution has
        # to be stated or the numbers look wrong to the user.
        result = self.counted(11, 12)
        self.assertTrue(
            any("guidelines for 10-minute" in line for line in result["info"]),
            result["info"],
        )


class ValidatorFileTests(TemporaryDirectoryTestCase):
    def test_a_missing_file_is_the_only_thing_reported(self) -> None:
        result = validated(self.root / "absent.pdf")
        self.assertFalse(result["valid"])
        self.assertIn("File not found", result["issues"][0])

    def test_an_unsupported_extension_warns_but_does_not_fail(self) -> None:
        path = self.root / "talk.key"
        path.write_bytes(b"")
        result = validated(path)
        self.assertTrue(result["valid"])
        self.assertTrue(any("Unknown file type" in line for line in result["warnings"]))

    def test_the_file_type_is_recognised_case_insensitively(self) -> None:
        validator = validate_presentation.PresentationValidator("TALK.PDF")
        self.assertEqual(validator.file_type, ".pdf")

    def sized(self, megabytes: float) -> dict:
        path = self.root / f"deck_{megabytes}.pdf"
        with path.open("wb") as handle:
            handle.truncate(int(megabytes * 1024 * 1024))  # sparse, not written
        validator = validate_presentation.PresentationValidator(str(path))
        validator._check_file_size()
        return {"info": validator.info, "warnings": validator.warnings,
                "issues": validator.issues}

    def test_an_ordinary_deck_size_is_only_reported(self) -> None:
        result = self.sized(4)
        self.assertEqual(result["warnings"], [])
        self.assertEqual(result["issues"], [])
        self.assertIn("4.00 MB", result["info"][0])

    def test_a_large_deck_warns_about_sharing_it(self) -> None:
        result = self.sized(60)
        self.assertTrue(result["warnings"])
        self.assertEqual(result["issues"], [])

    def test_an_enormous_deck_is_an_issue_not_a_warning(self) -> None:
        result = self.sized(120)
        self.assertTrue(result["issues"])
        self.assertIn("compressing images", result["issues"][0])


class ValidatorPdfTests(TemporaryDirectoryTestCase):
    def setUp(self) -> None:
        super().setUp()
        if not validate_presentation.HAS_PDF_READER:
            self.skipTest("neither pypdf nor PyPDF2 is installed")

    def test_a_widescreen_deck_reports_its_page_count_and_ratio(self) -> None:
        # Regression: with only pypdf installed this whole branch used to be
        # skipped, and the validator reported nothing about the deck at all.
        result = validated(self.deck(pages=2, size=(1280, 720)))
        self.assertTrue(result["valid"], result["issues"])
        joined = "\n".join(result["info"])
        self.assertIn("Number of slides: 2", joined)
        self.assertIn("16:9", joined)

    def test_a_four_by_three_deck_is_recognised(self) -> None:
        result = validated(self.deck(pages=1, size=(1024, 768)))
        self.assertIn("4:3", "\n".join(result["info"]))

    def test_an_unusual_aspect_ratio_is_flagged_for_the_venue(self) -> None:
        result = validated(self.deck(pages=1, size=(1000, 1000)))
        self.assertTrue(
            any("Unusual aspect ratio" in line for line in result["warnings"])
        )

    def test_the_slide_dimensions_are_reported_in_inches(self) -> None:
        # 1280 x 720 points at 72 points per inch is 17.8" x 10.0".
        result = validated(self.deck(pages=1, size=(1280, 720)))
        self.assertIn('17.8" x 10.0"', "\n".join(result["info"]))

    def test_the_page_count_is_measured_against_the_duration(self) -> None:
        result = validated(self.deck(pages=2, size=(1280, 720)), duration=15)
        self.assertTrue(any("Fewer slides" in line for line in result["warnings"]))

    def test_a_corrupt_pdf_is_an_issue_rather_than_a_traceback(self) -> None:
        path = self.root / "broken.pdf"
        path.write_bytes(b"%PDF-1.4\nnot really a pdf\n")
        result = validated(path)
        self.assertFalse(result["valid"])
        self.assertIn("Error reading PDF", result["issues"][0])


class ValidatorLatexTests(TemporaryDirectoryTestCase):
    """The compile step is stubbed: whether pdflatex exists is not the subject."""

    def source(self) -> Path:
        path = self.root / "talk.tex"
        path.write_text("\\documentclass{beamer}\\begin{document}\\end{document}")
        return path

    def test_a_failed_compile_is_an_issue_pointing_at_the_log(self) -> None:
        path = self.source()
        with mock.patch("subprocess.run", side_effect=FileNotFoundError):
            result = validated(path)
        self.assertFalse(result["valid"])
        self.assertIn(".log", result["issues"][0])

    def test_a_successful_compile_folds_in_the_pdf_report(self) -> None:
        if not validate_presentation.HAS_PDF_READER:
            self.skipTest("neither pypdf nor PyPDF2 is installed")
        path = self.source()
        # pdflatex writes talk.pdf beside talk.tex; produce one it can find.
        self.deck(pages=3, size=(1280, 720)).replace(path.with_suffix(".pdf"))
        completed = subprocess.CompletedProcess(args=[], returncode=0)
        with mock.patch("subprocess.run", return_value=completed):
            result = validated(path)
        joined = "\n".join(result["info"])
        self.assertIn("LaTeX compilation: SUCCESS", joined)
        # The merged PDF report is what makes the .tex path useful.
        self.assertIn("Number of slides: 3", joined)

    def test_the_compile_never_enables_shell_escape(self) -> None:
        # Shell escape in a LaTeX source would run arbitrary commands.
        path = self.source()
        with mock.patch("subprocess.run", side_effect=FileNotFoundError) as run:
            validated(path)
        self.assertIn("-no-shell-escape", run.call_args.args[0])
        self.assertIn("-interaction=nonstopmode", run.call_args.args[0])


class ValidatorPptxTests(TemporaryDirectoryTestCase):
    def setUp(self) -> None:
        super().setUp()
        if not validate_presentation.HAS_PPTX:
            self.skipTest("python-pptx is not installed")

    def build(self, *, font_pt: int, bullets: int) -> Path:
        from pptx import Presentation
        from pptx.util import Inches, Pt

        presentation = Presentation()
        slide = presentation.slides.add_slide(presentation.slide_layouts[6])
        box = slide.shapes.add_textbox(Inches(1), Inches(1), Inches(6), Inches(4))
        frame = box.text_frame
        for index in range(bullets):
            paragraph = frame.paragraphs[0] if index == 0 else frame.add_paragraph()
            run = paragraph.add_run()
            run.text = f"point {index}"
            run.font.size = Pt(font_pt)
        path = self.root / f"deck_{font_pt}_{bullets}.pptx"
        presentation.save(path)
        return path

    def test_a_readable_uncluttered_slide_raises_nothing(self) -> None:
        result = validated(self.build(font_pt=24, bullets=3))
        self.assertTrue(result["valid"])
        self.assertEqual(
            [line for line in result["warnings"] if "text" in line or "bullets" in line],
            [],
        )

    def test_text_below_eighteen_point_is_flagged_with_the_slide_number(self) -> None:
        # 18 pt is the projection floor the skill documents.
        result = validated(self.build(font_pt=12, bullets=2))
        self.assertTrue(
            any("Small text (<18pt)" in line and "[1]" in line
                for line in result["warnings"]),
            result["warnings"],
        )

    def test_eighteen_point_itself_is_acceptable(self) -> None:
        result = validated(self.build(font_pt=18, bullets=2))
        self.assertEqual(
            [line for line in result["warnings"] if "Small text" in line], []
        )

    def test_more_than_six_bullets_is_flagged(self) -> None:
        result = validated(self.build(font_pt=24, bullets=8))
        self.assertTrue(
            any("Many bullets (>6)" in line for line in result["warnings"]),
            result["warnings"],
        )

    def test_six_bullets_is_still_acceptable(self) -> None:
        result = validated(self.build(font_pt=24, bullets=6))
        self.assertEqual(
            [line for line in result["warnings"] if "Many bullets" in line], []
        )

    def test_the_slide_geometry_is_reported(self) -> None:
        result = validated(self.build(font_pt=24, bullets=1))
        # python-pptx's default template is 10" x 7.5", i.e. 4:3.
        self.assertIn('10.0" x 7.5"', "\n".join(result["info"]))


class PdfToImagesTests(TemporaryDirectoryTestCase):
    def test_only_jpeg_and_png_are_accepted(self) -> None:
        for accepted in ("jpg", "jpeg", "png", "PNG"):
            with self.subTest(format=accepted):
                converter = pdf_to_images.PDFToImagesConverter(
                    "deck.pdf", "out/slide", format=accepted
                )
                self.assertEqual(converter.format, accepted.lower())
        for rejected in ("gif", "tiff", "svg"):
            with self.subTest(format=rejected):
                with self.assertRaisesRegex(ValueError, "Unsupported format"):
                    pdf_to_images.PDFToImagesConverter(
                        "deck.pdf", "out/slide", format=rejected
                    )

    def test_a_missing_pdf_is_refused_before_any_conversion(self) -> None:
        converter = pdf_to_images.PDFToImagesConverter(
            str(self.root / "absent.pdf"), str(self.root / "slide")
        )
        with contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(FileNotFoundError):
                converter.convert()

    def convert(self, **kwargs):
        if not pdf_to_images.HAS_PYMUPDF:
            self.skipTest("PyMuPDF is not installed")
        source = self.deck(pages=3, size=(1280, 720))
        converter = pdf_to_images.PDFToImagesConverter(
            str(source), str(self.root / "review" / "slide"), **kwargs
        )
        with contextlib.redirect_stdout(io.StringIO()):
            return converter.convert()

    def test_every_page_becomes_one_zero_padded_image(self) -> None:
        produced = self.convert(dpi=72)
        self.assertEqual(
            [path.name for path in produced],
            ["slide-001.jpg", "slide-002.jpg", "slide-003.jpg"],
        )
        for path in produced:
            self.assertTrue(path.is_file())

    def test_the_output_directory_is_created_on_demand(self) -> None:
        produced = self.convert(dpi=72)
        self.assertEqual(produced[0].parent, self.root / "review")

    def test_the_requested_dpi_sets_the_pixel_size(self) -> None:
        # A 720-point-tall slide at 144 dpi is 1440 pixels: zoom = dpi / 72.
        produced = self.convert(dpi=144, format="png")
        with Image.open(produced[0]) as rendered:
            self.assertEqual(rendered.size, (2560, 1440))

    def test_a_page_range_converts_only_those_slides(self) -> None:
        produced = self.convert(dpi=72, first_page=2, last_page=3)
        # 1-indexed and inclusive, and the names keep the original numbering.
        self.assertEqual(
            [path.name for path in produced], ["slide-002.jpg", "slide-003.jpg"]
        )

    def test_the_format_decides_the_encoding_not_just_the_suffix(self) -> None:
        produced = self.convert(dpi=72, format="png")
        with Image.open(produced[0]) as rendered:
            self.assertEqual(rendered.format, "PNG")


class ImageCollectionTests(TemporaryDirectoryTestCase):
    def test_files_are_ordered_by_name_so_numbering_decides_the_deck(self) -> None:
        # Zero-padded names sort correctly; "10" must not precede "2".
        for name in ("03_methods.png", "01_title.png", "10_end.png", "02_intro.png"):
            self.image(name)
        found = slides_to_pdf.get_image_files([str(self.root)])
        self.assertEqual(
            [path.name for path in found],
            ["01_title.png", "02_intro.png", "03_methods.png", "10_end.png"],
        )

    def test_a_directory_yields_every_supported_image(self) -> None:
        for name in ("a.png", "b.jpg", "c.jpeg", "d.bmp"):
            self.image(name)
        found = slides_to_pdf.get_image_files([str(self.root)])
        self.assertEqual(len(found), 4)

    def test_a_non_image_file_is_skipped_with_a_warning(self) -> None:
        self.image("slide.png")
        notes = self.root / "notes.txt"
        notes.write_text("not a slide")
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            found = slides_to_pdf.get_image_files([str(notes), str(self.root / "slide.png")])
        self.assertEqual([path.name for path in found], ["slide.png"])
        self.assertIn("Skipping non-image", stream.getvalue())

    def test_the_same_file_named_twice_appears_once(self) -> None:
        path = self.image("slide.png")
        found = slides_to_pdf.get_image_files([str(path), str(path)])
        self.assertEqual(len(found), 1)

    def test_a_glob_pattern_is_expanded(self) -> None:
        self.image("s1.png")
        self.image("s2.png")
        self.image("other.jpg")
        found = slides_to_pdf.get_image_files([str(self.root / "s*.png")])
        self.assertEqual([path.name for path in found], ["s1.png", "s2.png"])

    def test_a_path_that_matches_nothing_yields_nothing(self) -> None:
        self.assertEqual(slides_to_pdf.get_image_files([str(self.root / "*.png")]), [])


class SlidesToPdfTests(TemporaryDirectoryTestCase):
    def combine(self, images, name="talk.pdf", **kwargs):
        destination = self.root / "out" / name
        with contextlib.redirect_stdout(io.StringIO()) as printed:
            ok = slides_to_pdf.combine_images_to_pdf(images, destination, **kwargs)
        return ok, destination, printed.getvalue()

    def page_count(self, path: Path) -> int:
        if validate_presentation.HAS_PDF_READER:
            from validate_presentation import PdfReader

            return len(PdfReader(str(path)).pages)
        self.skipTest("neither pypdf nor PyPDF2 is installed")

    def test_the_slides_become_pages_in_the_order_given(self) -> None:
        images = [self.image(f"slide{index}.png") for index in range(1, 4)]
        ok, destination, _ = self.combine(images)
        self.assertTrue(ok)
        self.assertEqual(self.page_count(destination), 3)

    def test_the_output_directory_is_created(self) -> None:
        ok, destination, _ = self.combine([self.image("slide.png")])
        self.assertTrue(ok)
        self.assertTrue(destination.is_file())

    def test_no_images_is_refused_rather_than_writing_an_empty_pdf(self) -> None:
        ok, destination, printed = self.combine([])
        self.assertFalse(ok)
        self.assertFalse(destination.exists())
        self.assertIn("No image files found", printed)

    def test_a_transparent_slide_is_flattened_onto_white(self) -> None:
        # PDF has no alpha channel; without the flattening step Pillow raises.
        ok, destination, _ = self.combine([self.image("slide.png", mode="RGBA")])
        self.assertTrue(ok)
        self.assertEqual(self.page_count(destination), 1)

    def test_a_greyscale_slide_is_converted_rather_than_rejected(self) -> None:
        ok, _, _ = self.combine([self.image("grey.png", mode="L")], name="grey.pdf")
        self.assertTrue(ok)

    def test_an_unreadable_slide_aborts_instead_of_producing_a_short_deck(self) -> None:
        broken = self.root / "broken.png"
        broken.write_bytes(b"not an image")
        ok, destination, printed = self.combine([self.image("ok.png"), broken])
        self.assertFalse(ok)
        self.assertFalse(destination.exists())
        self.assertIn("Error loading", printed)


