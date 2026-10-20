> **Fork note (2026-10-20):** The OpenRouter infographic generator was removed. Command blocks that called it were deleted. Build the figure with matplotlib, Mermaid, or Graphviz from verified data.

# Infographic Types Reference Guide

This reference provides extended templates, examples, and prompt patterns for each infographic type.
All example commands are illustrative and were not sent to paid generation APIs during review.
Numerical samples are layout inputs, not verified current facts: replace them with sourced
values, units, denominators, geography, and dates before producing a factual infographic.
For exact plots or maps, render with plotting/GIS tools and use the result as reference.

---

## 1. Statistical/Data-Driven Infographics

### Purpose
Present quantitative data, statistics, survey results, and numerical comparisons in an engaging visual format.

### Visual Elements
- **Bar charts**: Horizontal or vertical for comparisons
- **Pie/donut charts**: For proportions and percentages
- **Line charts**: For trends over time
- **Large number callouts**: Highlight key statistics
- **Icons**: Represent categories visually
- **Progress bars**: Show percentages or completion

### Layout Patterns
- **Single-stat hero**: One large number with supporting context
- **Multi-stat grid**: 3-6 statistics in a grid layout
- **Chart-centric**: Large visualization with supporting text
- **Comparison bars**: Side-by-side bar comparisons

### Prompt Templates

**Single Statistic Hero:**
```
Statistical infographic featuring one key statistic about [TOPIC]:
Main stat: [LARGE NUMBER] [UNIT/CONTEXT]
Supporting context: [2-3 sentences explaining the significance]
Large bold number in center, supporting text below,
relevant icon or illustration, [COLOR] accent color,
clean minimal design, white background.
```

**Multi-Statistic Grid:**
```
Statistical infographic presenting [TOPIC] data:
Stat 1: [NUMBER] [LABEL] (icon: [ICON])
Stat 2: [NUMBER] [LABEL] (icon: [ICON])
Stat 3: [NUMBER] [LABEL] (icon: [ICON])
Stat 4: [NUMBER] [LABEL] (icon: [ICON])
2x2 grid layout, large bold numbers, small icons above each,
[COLOR SCHEME], modern clean typography, white background.
```

**Chart-Focused:**
```
Statistical infographic with [CHART TYPE] showing [TOPIC]:
Data points: [VALUE 1], [VALUE 2], [VALUE 3], [VALUE 4]
Labels: [LABEL 1], [LABEL 2], [LABEL 3], [LABEL 4]
Large [bar/pie/donut] chart as main element,
title at top, legend below chart, [COLOR SCHEME],
data labels on chart, clean professional design.
```

### Example Prompts

**Synthetic Clinic Operations (layout example):**


**Business Metrics:**


---

## 2. Timeline Infographics

### Purpose
Display events, milestones, or developments in chronological order.

### Visual Elements
- **Timeline axis**: Horizontal or vertical line
- **Date markers**: Years, months, or specific dates
- **Event nodes**: Circles, icons, or images at each point
- **Description boxes**: Brief text for each event
- **Connecting elements**: Lines, arrows, or paths

### Layout Patterns
- **Horizontal timeline**: Left-to-right progression
- **Vertical timeline**: Top-to-bottom progression
- **Winding/snake timeline**: S-curve for many events
- **Circular timeline**: For cyclical or repeating events

### Prompt Templates

**Horizontal Timeline:**
```
Horizontal timeline infographic showing [TOPIC] from [START YEAR] to [END YEAR]:
[YEAR 1]: [EVENT 1] - [brief description]
[YEAR 2]: [EVENT 2] - [brief description]
[YEAR 3]: [EVENT 3] - [brief description]
[YEAR 4]: [EVENT 4] - [brief description]
Left-to-right timeline with circular nodes for each event,
connecting line between nodes, icons above each node,
[COLOR] gradient from past to present, date labels below,
clean modern design, white background.
```

**Vertical Timeline:**
```
Vertical timeline infographic showing [TOPIC]:
Top (earliest): [YEAR] - [EVENT]
Middle events: [YEAR] - [EVENT], [YEAR] - [EVENT]
Bottom (latest): [YEAR] - [EVENT]
Top-to-bottom flow, alternating left-right event boxes,
central vertical line connecting all events,
circular nodes with dates, [COLOR SCHEME],
professional clean design, white background.
```

**Project Milestone Timeline:**
```
Project timeline infographic for [PROJECT NAME]:
Phase 1: [DATES] - [MILESTONE] (status: complete)
Phase 2: [DATES] - [MILESTONE] (status: in progress)
Phase 3: [DATES] - [MILESTONE] (status: upcoming)
Phase 4: [DATES] - [MILESTONE] (status: planned)
Gantt-style horizontal bars, color-coded by status,
green for complete, yellow for in progress, gray for upcoming,
project name header, clean professional design.
```

### Example Prompts

**Technology Evolution:**


**Company History:**


---

## 3. Process/How-To Infographics

### Purpose
Explain step-by-step procedures, workflows, instructions, or methodologies.

### Visual Elements
- **Numbered steps**: Clear sequence indicators
- **Arrows/connectors**: Show flow and direction
- **Action icons**: Illustrate each step
- **Brief descriptions**: Concise action text
- **Start/end indicators**: Clear beginning and conclusion

### Layout Patterns
- **Vertical cascade**: Steps flow top-to-bottom
- **Horizontal flow**: Left-to-right progression
- **Circular process**: Steps form a cycle
- **Branching flow**: Decision points with alternatives

### Prompt Templates

**Linear Process:**
```
Process infographic: How to [ACCOMPLISH GOAL]
Step 1: [ACTION] - [brief explanation] (icon: [ICON])
Step 2: [ACTION] - [brief explanation] (icon: [ICON])
Step 3: [ACTION] - [brief explanation] (icon: [ICON])
Step 4: [ACTION] - [brief explanation] (icon: [ICON])
Step 5: [ACTION] - [brief explanation] (icon: [ICON])
Numbered circles connected by arrows, icons for each step,
[VERTICAL/HORIZONTAL] flow, [COLOR SCHEME],
clear step labels, clean instructional design, white background.
```

**Circular Process:**
```
Circular process infographic showing [CYCLE NAME]:
Step 1: [ACTION] leads to
Step 2: [ACTION] leads to
Step 3: [ACTION] leads to
Step 4: [ACTION] returns to Step 1
Circular arrangement with arrows forming a cycle,
icons at each point, step numbers, [COLOR SCHEME],
continuous flow design, white background.
```

**Decision Flowchart:**
```
Decision flowchart infographic for [SCENARIO]:
Start: [INITIAL QUESTION]
If Yes: [PATH A] → [OUTCOME A]
If No: [PATH B] → [OUTCOME B]
Diamond shapes for decisions, rectangles for actions,
arrows connecting all elements, [COLOR SCHEME],
clear yes/no labels, flowchart style, white background.
```

### Example Prompts

**Recipe Process:**


**Onboarding Workflow:**


---

## 4. Comparison Infographics

### Purpose
Compare two or more options, products, concepts, or choices side by side.

### Visual Elements
- **Split layout**: Clear division between options
- **Matching rows**: Same categories for fair comparison
- **Check/cross marks**: Quick visual indicators
- **Rating systems**: Stars, bars, or numbers
- **Headers**: Clear identification of each option

### Layout Patterns
- **Two-column split**: Left vs Right
- **Table format**: Rows and columns
- **Venn diagram**: Overlapping comparisons
- **Feature matrix**: Multi-option comparison grid

### Prompt Templates

**Two-Option Comparison:**
```
Comparison infographic: [OPTION A] vs [OPTION B]
Header: [OPTION A] on left | [OPTION B] on right
Row 1 - [CATEGORY 1]: [A VALUE] | [B VALUE]
Row 2 - [CATEGORY 2]: [A VALUE] | [B VALUE]
Row 3 - [CATEGORY 3]: [A VALUE] | [B VALUE]
Row 4 - [CATEGORY 4]: [A VALUE] | [B VALUE]
Row 5 - [CATEGORY 5]: [A VALUE] | [B VALUE]
Split layout with [COLOR A] for left, [COLOR B] for right,
icons for each option header, checkmarks for advantages,
clean symmetrical design, white background.
```

**Multi-Option Matrix:**
```
Comparison matrix infographic: [TOPIC]
Options: [OPTION 1], [OPTION 2], [OPTION 3]
Feature 1: [✓/✗ for each]
Feature 2: [✓/✗ for each]
Feature 3: [✓/✗ for each]
Feature 4: [✓/✗ for each]
Table layout with colored headers for each option,
checkmarks and X marks in cells, [COLOR SCHEME],
clean grid design, white background.
```

**Pros and Cons:**
```
Pros and Cons infographic for [TOPIC]:
Pros (left side, green):
- [PRO 1]
- [PRO 2]
- [PRO 3]
Cons (right side, red):
- [CON 1]
- [CON 2]
- [CON 3]
Split layout with green left side, red right side,
thumbs up icon for pros, thumbs down for cons,
balanced visual weight, white background.
```

### Example Prompts

**Software Comparison:**


**Study Design Comparison:**


---

## 5. List/Informational Infographics

### Purpose
Present tips, facts, key points, or information in an organized, scannable format.

### Visual Elements
- **Numbers or bullets**: Clear list indicators
- **Icons**: Visual representation of each point
- **Brief text**: Concise descriptions
- **Header**: Topic introduction
- **Consistent styling**: Uniform treatment of all items

### Layout Patterns
- **Vertical list**: Standard top-to-bottom
- **Two-column list**: For longer lists
- **Icon grid**: Icons with labels below
- **Cards**: Each point in a card/box

### Prompt Templates

**Numbered List:**
```
List infographic: [NUMBER] [TOPIC]
1. [POINT 1] - [brief explanation] (icon: [ICON])
2. [POINT 2] - [brief explanation] (icon: [ICON])
3. [POINT 3] - [brief explanation] (icon: [ICON])
4. [POINT 4] - [brief explanation] (icon: [ICON])
5. [POINT 5] - [brief explanation] (icon: [ICON])
Large numbers in circles, icons next to each point,
brief text descriptions, [COLOR SCHEME],
vertical layout with spacing, white background.
```

**Tips Format:**
```
Tips infographic: [NUMBER] Tips for [TOPIC]
Tip 1: [TIP] (lightbulb icon)
Tip 2: [TIP] (star icon)
Tip 3: [TIP] (checkmark icon)
Tip 4: [TIP] (target icon)
Tip 5: [TIP] (rocket icon)
Colorful tip boxes or cards, icons for each tip,
[COLOR SCHEME], engaging friendly design,
header at top, white background.
```

**Facts Format:**
```
Facts infographic: [NUMBER] Facts About [TOPIC]
Fact 1: [INTERESTING FACT]
Fact 2: [INTERESTING FACT]
Fact 3: [INTERESTING FACT]
Fact 4: [INTERESTING FACT]
Fact 5: [INTERESTING FACT]
Speech bubble or card style for each fact,
relevant icons, [COLOR SCHEME],
educational engaging design, white background.
```

### Example Prompts

**Productivity Tips:**


**Project Checklist:**


---

## 6. Geographic/Map-Based Infographics

### Purpose
Display location-based data, regional statistics, or geographic trends.

### Visual Elements
- **Map visualization**: World, country, or region
- **Color coding**: Data intensity by region
- **Data callouts**: Key statistics for regions
- **Legend**: Color scale explanation
- **Labels**: Region or country names

### Layout Patterns
- **Full map**: Map as primary element
- **Map with sidebar**: Data summary alongside
- **Regional focus**: Zoomed map section
- **Multi-map**: Several maps showing different data

### Prompt Templates

**World Map Data:**
```
Geographic infographic showing [TOPIC] globally:
Highest: [REGION/COUNTRY] - [VALUE]
Medium: [REGIONS] - [VALUE RANGE]
Lowest: [REGION/COUNTRY] - [VALUE]
World map with color-coded countries,
[DARK COLOR] for highest values, [LIGHT COLOR] for lowest,
legend showing color scale, key statistics callout,
clean cartographic design, light gray background.
```

**Country/Region Focus:**
```
Geographic infographic showing [TOPIC] in [COUNTRY/REGION]:
Region 1: [VALUE]
Region 2: [VALUE]
Region 3: [VALUE]
Map of [COUNTRY/REGION] with color-coded areas,
data labels for key regions, [COLOR] gradient,
legend with value scale, clean map design.
```

### Example Prompts

**Global Data:**


**US Regional:**


---

## 7. Hierarchical/Pyramid Infographics

### Purpose
Show levels of importance, organizational structures, or ranked information.

### Visual Elements
- **Pyramid shape**: Triangle with levels
- **Level labels**: Clear tier identification
- **Size progression**: Larger at base, smaller at top
- **Color progression**: Gradient or distinct colors per level
- **Icons**: Optional for each level

### Layout Patterns
- **Traditional pyramid**: Wide base, narrow top
- **Inverted pyramid**: Narrow base, wide top
- **Org chart**: Tree structure
- **Stacked blocks**: Square levels

### Prompt Templates

**Classic Pyramid:**
```
Hierarchical pyramid infographic: [TOPIC]
Top (Level 1 - most important/rare): [ITEM]
Level 2: [ITEM]
Level 3: [ITEM]
Level 4: [ITEM]
Base (Level 5 - foundation/most common): [ITEM]
Triangle pyramid with 5 horizontal sections,
[COLOR] gradient from [TOP COLOR] to [BASE COLOR],
labels on each tier, icons optional,
clean geometric design, white background.
```

**Organizational Hierarchy:**
```
Organizational chart infographic for [ORGANIZATION]:
Top: [CEO/LEADER]
Level 2: [VPs/DIRECTORS] (3-4 boxes)
Level 3: [MANAGERS] (6-8 boxes)
Level 4: [TEAM LEADS] (multiple boxes)
Tree structure flowing down, connecting lines between levels,
[COLOR SCHEME], professional corporate design,
role titles in boxes, white background.
```

### Example Prompts

**Project Hierarchy:**


**Energy Pyramid:**


---

## 8. Anatomical/Visual Metaphor Infographics

### Purpose
Explain complex systems using familiar visual metaphors (bodies, machines, trees, etc.).

### Visual Elements
- **Central metaphor image**: The main visual (body, tree, machine)
- **Labeled parts**: Components identified
- **Callout lines**: Connecting labels to parts
- **Descriptions**: Explanations for each part
- **Color coding**: Different parts in different colors

### Layout Patterns
- **Central image with callouts**: Labels pointing to parts
- **Exploded view**: Parts separated but arranged
- **Cross-section**: Inside view of metaphor
- **Before/after**: Metaphor in different states

### Prompt Templates

**Body Metaphor:**
```
Anatomical infographic using human body to explain [TOPIC]:
Brain represents [CONCEPT] - [explanation]
Heart represents [CONCEPT] - [explanation]
Hands represent [CONCEPT] - [explanation]
Feet represent [CONCEPT] - [explanation]
Human body silhouette with labeled callouts,
[COLOR SCHEME], clean medical illustration style,
connecting lines to descriptions, white background.
```

**Machine Metaphor:**
```
Anatomical infographic using machine/engine to explain [TOPIC]:
Fuel tank represents [CONCEPT]
Engine represents [CONCEPT]
Wheels represent [CONCEPT]
Steering represents [CONCEPT]
Machine illustration with labeled components,
callout lines and descriptions, [COLOR SCHEME],
technical illustration style, white background.
```

### Example Prompts

**Business as Body:**


**Computer as House:**


---

## 9. Resume/Professional Infographics

### Purpose
Present professional information, skills, experience, and achievements visually.

### Visual Elements
- **Photo/avatar section**: Personal branding
- **Skills visualization**: Bars, charts, ratings
- **Timeline**: Career progression
- **Contact icons**: Email, phone, social
- **Achievement badges**: Certifications, awards

### Layout Patterns
- **Single column**: Vertical flow
- **Two column**: Info left, skills right
- **Header focus**: Large header with photo
- **Modular**: Distinct sections/cards

### Prompt Templates

**Professional Resume:**
```
Resume infographic for [NAME], [PROFESSION]:
Photo area: Circular avatar placeholder
Skills: [SKILL 1] 90%, [SKILL 2] 85%, [SKILL 3] 75%
Experience: [YEAR-YEAR] [ROLE] at [COMPANY], [YEAR-YEAR] [ROLE] at [COMPANY]
Education: [DEGREE] from [INSTITUTION]
Contact: Email, LinkedIn, Portfolio icons
Professional photo area at top, horizontal skill bars,
timeline for experience, [COLOR SCHEME],
modern professional design, white background.
```

### Example Prompts

**Designer Resume:**


---

## 10. Social Media/Interactive Infographics

### Purpose
Create shareable, engaging content optimized for social media platforms.

### Visual Elements
- **Bold headlines**: Attention-grabbing text
- **Minimal text**: Quick to read
- **Vibrant colors**: Stand out in feeds
- **Central visual**: Eye-catching image or icon
- **Call to action**: Engagement prompt

### Layout Patterns
- **Square format**: Instagram, Facebook
- **Vertical format**: Pinterest, Stories
- **Carousel**: Multi-slide series
- **Quote card**: Impactful statement focus

### Illustrative Canvas Sizes (not API guarantees)

These are common layout examples, not a statement of current platform upload rules.
Check the destination platform before delivery; the script does not enforce pixel dimensions.
- **Instagram Square**: 1080x1080px
- **Instagram Portrait**: 1080x1350px
- **Twitter/X**: 1200x675px
- **LinkedIn**: 1200x627px
- **Pinterest**: 1000x1500px

### Prompt Templates

**Social Quote Card:**
```
Social media infographic: Inspirational quote
Quote: "[QUOTE TEXT]"
Attribution: - [AUTHOR]
Large quotation marks, centered quote text,
author name below, [COLOR SCHEME],
Instagram square format, bold typography,
solid gradient background.
```

**Quick Stats Social:**
```
Social media infographic: [TOPIC] in Numbers
Headline: [ATTENTION-GRABBING HEADLINE]
Stat 1: [BIG NUMBER] [CONTEXT]
Stat 2: [BIG NUMBER] [CONTEXT]
Call to action: [CTA]
Bold numbers, minimal text, [COLOR SCHEME],
vibrant engaging design, social media optimized,
Instagram square format.
```

### Example Prompts

**Inspirational Quote:**


**Engagement Stats:**


---

## Style Variations by Industry

### Corporate/Business Style
- Colors: Navy, gray, gold accents
- Typography: Clean sans-serif (Arial, Helvetica)
- Design: Minimal, professional, structured
- Elements: Charts, icons, clean lines

### Healthcare/Medical Style
- Colors: Blue, teal, green, white
- Typography: Clear, readable
- Design: Trust-inducing, clean, clinical
- Elements: Medical icons, anatomy, research imagery

### Technology/Data Style
- Colors: Dark backgrounds, neon accents, blue/purple
- Typography: Modern sans-serif, monospace for data
- Design: Futuristic, clean, dark mode friendly
- Elements: Circuit patterns, data visualizations, glows

### Education/Academic Style
- Colors: Neutral tones, soft blues, warm accents
- Typography: Readable, slightly traditional
- Design: Organized, clear hierarchy, accessible
- Elements: Books, lightbulbs, graduation icons

### Marketing/Creative Style
- Colors: Bold, vibrant, trendy combinations
- Typography: Mix of display and body fonts
- Design: Eye-catching, dynamic, playful
- Elements: Abstract shapes, gradients, illustrations

---

## Prompt Modifiers Reference

Add these modifiers to any prompt to adjust style:

### Design Style
- "clean minimal design"
- "modern professional design"
- "flat design with bold colors"
- "hand-drawn illustration style"
- "3D isometric style"
- "vintage retro style"
- "corporate business style"
- "playful friendly design"

### Color Instructions
- "[color] and [color] color scheme"
- "monochromatic [color] palette"
- "colorblind-safe palette"
- "warm/cool color tones"
- "high contrast design"
- "muted pastel colors"
- "bold vibrant colors"

### Layout Instructions
- "vertical layout"
- "horizontal layout"
- "centered composition"
- "asymmetrical balance"
- "grid-based layout"
- "flowing organic layout"

### Background Options
- "white background"
- "light gray background"
- "dark background"
- "gradient background from [color] to [color]"
- "subtle pattern background"
- "solid [color] background"

---

Use these templates and examples as starting points, then customize for your specific needs.
