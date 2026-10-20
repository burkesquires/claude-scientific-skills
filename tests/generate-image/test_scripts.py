"""The OpenRouter image client was removed from this fork."""

from __future__ import annotations

import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[2] / "skills" / "generate-image"


class RemovedGeneratorTests(unittest.TestCase):
    def test_the_openrouter_script_is_gone(self) -> None:
        self.assertFalse((SKILL_ROOT / "scripts" / "generate_image.py").exists())

    def test_the_skill_does_not_instruct_a_paid_image_call(self) -> None:
        text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertNotIn("OPENROUTER_API_KEY", text)
        self.assertNotIn("python scripts/generate_image.py", text)
        self.assertNotIn("## Citing Scientific Agent Skills", text)
