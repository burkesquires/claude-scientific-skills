"""Offline API contract and local rendering regressions for the 2026 refresh."""
from pathlib import Path
import sys

import pytest

SKILL_ROOT = Path(__file__).resolve().parents[2] / "skills" / "scientific-slides"
sys.path.insert(0, str(SKILL_ROOT / "scripts"))
import pdf_to_images  # noqa: E402
import slides_to_pdf  # noqa: E402
import validate_presentation  # noqa: E402


def test_explicit_file_order_and_duplicate_identity_are_preserved(tmp_path):
    for name in ("title.png", "intro.png", "methods.png"):
        (tmp_path / name).touch()
    paths = [tmp_path / n for n in ("title.png", "intro.png", "methods.png")]
    assert slides_to_pdf.get_image_files([str(p) for p in paths] + [str(paths[0])]) == paths


@pytest.mark.parametrize("kwargs", [{"dpi": 0}, {"first_page": 0}, {"last_page": -1}, {"first_page": 3, "last_page": 2}])
def test_invalid_render_range_and_dpi_are_refused(kwargs):
    with pytest.raises(ValueError):
        pdf_to_images.PDFToImagesConverter("deck.pdf", "slide", **kwargs)


def test_range_beyond_pdf_is_refused_before_partial_render(tmp_path):
    import pymupdf
    source = tmp_path / "deck.pdf"
    with pymupdf.open() as doc:
        doc.new_page()
        doc.save(source)
    converter = pdf_to_images.PDFToImagesConverter(str(source), str(tmp_path / "slide"), last_page=2)
    with pytest.raises(ValueError, match="1-1"):
        converter.convert()
    assert not list(tmp_path.glob("slide*"))


def test_legacy_ppt_has_actionable_failure(tmp_path):
    source = tmp_path / "legacy.ppt"
    source.write_bytes(b"legacy")
    result = validate_presentation.PresentationValidator(str(source)).validate()
    assert not result["valid"]
    assert "convert" in result["issues"][0]
