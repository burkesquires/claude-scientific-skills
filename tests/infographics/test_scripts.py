"""The OpenRouter infographic generator was removed from this fork."""

from __future__ import annotations

import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parents[2] / "skills" / "infographics"


class RemovedGeneratorTests(unittest.TestCase):
    def test_the_openrouter_scripts_are_gone(self) -> None:
        scripts = SKILL_ROOT / "scripts"
        self.assertFalse((scripts / "generate_infographic.py").exists())
        self.assertFalse((scripts / "generate_infographic_ai.py").exists())

    def test_the_skill_does_not_instruct_a_paid_image_call(self) -> None:
        text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertNotIn("OPENROUTER_API_KEY", text)
        self.assertNotIn("python skills/infographics/scripts/generate_infographic.py", text)
        self.assertNotIn("## Citing Scientific Agent Skills", text)
