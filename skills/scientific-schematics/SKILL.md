---
name: scientific-schematics
description: Plans scientific diagrams with local, deterministic tools (Mermaid, Graphviz, matplotlib). Use for flowcharts, pathways, architectures, and CONSORT or PRISMA counts when every label must be traceable. Does not call a paid image API.
allowed-tools: Read Write Edit Bash
license: MIT license
compatibility: No network and no API key. Optional local tools are Mermaid, Graphviz, and matplotlib.
metadata:
  version: "1.10"
  last-reviewed: "2026-09-30"
  skill-author: K-Dense Inc.
---

# Scientific Schematics and Diagrams

## Overview

Build diagrams locally so every label, count, and arrow is something you can check. This fork does not ship the upstream OpenRouter image generator. That helper walked parent directories for `.env` API keys and sent the prompt, and then the image, to a paid third-party API.

## How to draw

- **Flowcharts and pathways:** Mermaid in Markdown, or Graphviz (`dot`).
- **Quantitative charts:** matplotlib (or the seaborn / scientific-visualization skills). Do not draw a bar, error bar, or count that is not in a table you can point to.
- **Publication layout:** edit the vector or the plotting script. A raster from an image model is not a substitute for a figure a journal can regenerate.

Save figures under a project `figures/` directory, not inside this skill.

## Counts in trial and review diagrams

For trial flows, use the [CONSORT 2025 template and item 22a](https://www.consort-spirit.org/item-22a-randomized), reconcile enrollment, allocation, follow-up, and analysis counts, and report the specified primary outcome. For reviews, choose the appropriate [PRISMA 2020 template](https://www.prisma-statement.org/prisma-2020-flow-diagram). Records, reports, and studies are distinct units. Do not invent a count to make a diagram balance.
