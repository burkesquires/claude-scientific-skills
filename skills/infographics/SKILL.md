---
name: infographics
description: Plans statistical, timeline, comparison, and process infographics from supplied data using local plotting tools. Use when a figure must present verified numbers or a process. This fork does not call OpenRouter.
compatibility: No network and no API key. Optional local tools are matplotlib, Mermaid, and Graphviz.
allowed-tools: Read Write Edit Bash
metadata:
  version: "1.10"
  last-reviewed: "2026-10-01"
  skill-author: K-Dense Inc.
---

# Infographics

## Overview

An infographic is a figure of information the reader can check. This fork removed the OpenRouter generator (`generate_infographic.py` and `generate_infographic_ai.py`). Those scripts walked parent directories for `.env` keys and sent the prompt to a paid image API, including an optional web-research pass.

Draw the figure locally:

- matplotlib or seaborn for charts of numbers you have in a table
- Mermaid or Graphviz for processes, timelines, and hierarchies
- the color and layout notes in the reference files below

Do not invent a percentage, map, or sample size to fill a layout. If a number is not in a source the user supplied or you retrieved and cited, leave it out and say so.

## Reference files

- `references/design_principles.md` — hierarchy, type, and layout
- `references/color_palettes.md` — accessible palette starting points
- `references/infographic_types.md` and `references/infographic_type_catalog.md` — what each layout is for

Worked prompts in those files that used to call the removed generator are not commands. Use them only as a description of the content, then plot it locally.
