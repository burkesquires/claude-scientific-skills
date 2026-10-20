---
name: generate-image
description: Points image and illustration requests at local tools. Use when a task asks for a generated picture, icon, or composite. This fork does not call OpenRouter or any other paid image API.
license: MIT
compatibility: No network and no API key. Use local drawing tools or a figure the user already supplied.
allowed-tools: Read Write Edit Bash
metadata:
  version: "3.3"
  skill-author: K-Dense Inc.
  last-reviewed: "2026-09-30"
---

# Generate Image

This fork removed the OpenRouter image script. The upstream script walked parent directories for an API key in .env files and posted the prompt, and any reference image, to that service.

Do not send unpublished figures, patient images, or other sensitive pixels to a third-party image API unless the user explicitly asks for that service and supplies a key for that call.

For diagrams, plots, and schematics, use Mermaid, Graphviz, or matplotlib, or the scientific-schematics skill. For a picture the user already has, edit the file they provided.
