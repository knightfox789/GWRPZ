# Interaction Specification

**Version:** v0.1  
**Date:** 23 September 2026  
**Project:** From Mapping to Decision — Interactive Groundwater Recharge Planning  
**Phase:** Phase 5 — UX prototype  
**Status:** DRAFT COMPLETE — Gate 5 pending user approval

---

## 1. Interaction principles

1. **Story mode explains; Explore mode interrogates.**
2. The map changes only when the narrative reason is clear.
3. No interaction may imply evidence that does not exist.
4. Every technical control needs a plain-language label.
5. Mobile must preserve the same evidence and decisions, even if the interaction is simpler.
6. Accessibility and reduced-motion behavior are part of the design, not a late addition.

---

## 2. Global navigation

### Desktop
Sticky top navigation:
- **Story**
- **Explore Map**
- **Method**
- **Data & limitations**
- optional progress indicator.

### Mobile
Compact top bar:
- title / home;
- Story / Explore switch;
- “More” menu for Method + Data.

The user should never lose a direct route back to the Guided Story.

---

## 3. Guided Story interaction model

### Desktop pattern
- left story rail: 38–42%;
- right sticky map: 58–62%;
- one story step becomes active when ~45–55% of its card crosses the viewport focus line;
- active step triggers one named map state;
- state transitions use 200–350 ms opacity changes;
- avoid repeated dramatic fly-to animations.

### Mobile pattern
- sticky map: 42–48vh;
- story cards below;
- active state changes when card enters the middle of the remaining reading viewport;
- controls are compact;
- detailed legends open in a bottom sheet;
- map is not allowed to create horizontal page overflow.

### Reduced motion
If `prefers-reduced-motion: reduce`:
- disable fly-to / animated zoom;
- use immediate layer visibility changes;
- preserve active-step highlighting.

---

## 4. Map-state contract

Each story state is declarative.

Required state properties:
- `id`;
- `title`;
- visible layers;
- raster opacity;
- vector emphasis;
- legend mode;
- selected feature / filter if any;
- camera extent;
- interaction lock state;
- evidence-note ID.

### State list

| State | Primary layer | Supporting layers | Story purpose |
|---|---|---|---|
| S01_CONTEXT | final GWRPZ faint | villages | locate study area |
| S02_VARIABILITY | interventions | villages, drainage | show spatial variability |
| S03_LANDSCAPE | drainage order | villages | ridge-to-valley reading |
| S04_AQUIFER | aquifer score | aquifer outline | factor 1 |
| S04_SLOPE | slope score | villages faint | factor 2 |
| S04_DD | drainage-density score | drainage faint | factor 3 |
| S04_LD | lineament-density score | lineaments faint | factor 4 |
| S04_LULC | LULC | villages | factor 5 |
| S05_WEIGHTED_MODEL | factor selector | weight diagram | combine evidence |
| S06_GWRPZ | final GWRPZ | villages | interpret potential |
| S07_POTENTIAL_NOT_SITING | final GWRPZ | drainage, structures | add decision context |
| S08_STREAM_ORDER | drainage order | GWRPZ 45%, structures | hydrological position |
| S09_LINEAMENT | lineaments | structures, GWRPZ 35% | structural context |
| S10_STRUCTURES | structures | GWRPZ, villages | inspect intervention sample |
| S11_ALIGNMENT | structures by siting setting | drainage, GWRPZ 30% | spatial-setting summary |
| S12_DECISION | final GWRPZ | drainage, lineaments, selected point | planning sequence |
| S13_FIELD_VERIFY | selected point | faint context | handoff to field |

---

## 5. Story-map controls

### Allowed in Guided Story
- zoom in / zoom out;
- reset view;
- legend expand/collapse;
- “Open in Explore Map”;
- factor tabs during Chapter 4;
- opacity comparison during Chapters 5–6;
- tap/click structures during Chapters 10–11.

### Restricted in Guided Story
Do not expose all layer toggles at once. Too much map freedom during explanation makes the narrative hard to follow.

If the user pans far from the story area, show a small “Return to story view” action.

---

## 6. Explore Map controls

### Layer panel
Groups:

**Potential**
- Final GWRPZ;
- Aquifer score;
- Slope score;
- Drainage-density score;
- Lineament-density score;
- LULC.

**Context**
- Villages;
- Drainage order;
- Lineaments.

**Structures**
- Interventions.

Only one thematic raster should be fully opaque by default. Other raster layers can be toggled but should not all stack at 100%.

### Opacity
- one 0–100% slider for the active thematic raster;
- default 75–85% depending on layer;
- vector context remains visible.

### Reset
One action restores:
- study-area extent;
- final GWRPZ;
- villages;
- structures;
- default opacity;
- no filters.

---

## 7. Structure filters

Available:
- Structure Type;
- Village;
- Block;
- Final GWRPZ Class: Moderate / High;
- Nearest Stream Order: 1–4;
- Siting Alignment Spatial Setting.

Not available:
- historical `Lineament_` yes/no;
- invented “near lineament” band;
- performance / success filter.

Filter counts update live.

Mobile filters open as a bottom sheet with **Apply** and **Clear** actions.

---

## 8. Structure popup

Popup / details panel fields:

**Identity**
- Structure ID
- Structure Type
- Village
- Block

**Spatial evidence**
- Final GWRPZ Class
- Nearest Stream Order
- Nearest Stream Distance (m)
- Nearest Lineament Distance (m)
- Siting Alignment Spatial Setting

**Interpretation note**
“Spatial setting is decision-support evidence, not measured structure performance.”

Optional link:
- “How these fields were calculated”

Do not show the historical binary lineament field as a primary attribute.

---

## 9. Legends

Legend updates by state.

### GWRPZ
- Low — Class 1
- Moderate — Class 2
- High — Class 3

### Factor scores
Use:
- Score 1 — lower contribution to recharge potential;
- Score 2 — moderate;
- Score 3 — higher contribution.

Avoid using “bad / good” labels.

### Drainage
Display stream orders with line thickness.

### Siting setting
Use full category names, not “Optimal / Moderate / Poor”.

---

## 10. “Why is this location classified this way?”

Phase 5 specification only; implementation belongs to Phase 6.

For a selected location:
- show final GWRPZ class;
- show factor scores where available;
- show factor weights;
- show nearest stream order / distance;
- show nearest lineament distance;
- show explicit message:  
  “The final historical class break is not fully reconstructable from the preserved source workflow. The supplied final GWRPZ raster remains the class reference.”

This explainer must not fabricate an exact historical final threshold.

---

## 11. Compare interactions

### Recommended
- factor tabs;
- opacity slider;
- optional split / swipe only for:
  - factor vs final GWRPZ;
  - GWRPZ vs structure context.

### Defer from first build if unstable
- multi-raster swipe with several simultaneous layers;
- complex synchronized mini-maps.

The first release should prioritize interpretability over novelty.

---

## 12. Technical-detail interaction

### Method note
Inline accordion linked to the current story section.

### Evidence note
A small “Evidence & limitation” link opens a side drawer (desktop) / bottom sheet (mobile).

### Full methodology
Dedicated appendix route/section with:
- inputs;
- scoring;
- weights;
- grid / resampling;
- reconstruction;
- limitations;
- source lineage.

The article should never hide a limitation that materially changes interpretation behind an optional interaction only. Essential caveats remain visible in the main copy.

---

## 13. Desktop wireframe

```text
┌──────────────────────────────────────────────────────────────┐
│ Logo/Title        Story   Explore Map   Method   Data        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  STORY RAIL (40%)          STICKY MAP / EVIDENCE (60%)       │
│                                                              │
│  [chapter title]           ┌───────────────────────────────┐  │
│  short narrative           │ dynamic map state             │  │
│  evidence callout          │ legend                        │  │
│  limitation                │ optional structure popup      │  │
│                            └───────────────────────────────┘  │
│  [next story card]                                           │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│  Explore Map CTA / Methodology / replication / footer        │
└──────────────────────────────────────────────────────────────┘
```

---

## 14. Mobile wireframe

```text
┌────────────────────────────┐
│ Title      Story | Explore │
├────────────────────────────┤
│ Sticky map / evidence      │
│ ~44vh                      │
│ [legend] [open explore]    │
├────────────────────────────┤
│ Chapter title              │
│ short narrative            │
│ key evidence               │
│ limitation                 │
│ [method note]              │
├────────────────────────────┤
│ Next chapter               │
│ ...                        │
└────────────────────────────┘
```

Controls open as bottom sheets instead of permanent sidebars.

---

## 15. Accessibility

Required for Phase 6:
- keyboard-focusable controls;
- visible focus styles;
- no information encoded by color alone;
- map legend labels in text;
- sufficient contrast;
- responsive text;
- `aria-live` only where state updates need announcement;
- reduced-motion support;
- structure popup accessible without hover;
- story remains understandable if map fails to load.

---

## 16. Failure / fallback behavior

If GIS assets fail:
- story text and evidence numbers still render;
- map panel shows a plain fallback message;
- methodology and data links remain usable.

If a raster fails:
- vector context remains;
- legend indicates unavailable layer.

If mobile performance is weak:
- defer nonessential lineaments / complex vector layers until requested.

---

## 17. Phase 5 prototype acceptance checks

Prototype should demonstrate:
- story rail + sticky map relationship;
- named map states;
- factor switching;
- key evidence callouts;
- Explore Map handoff;
- responsive desktop/mobile layout;
- technical-note pattern;
- explicit evidence caveats.

Prototype is a UX validation artifact, not the Phase 6 production build.

---

## 18. Gate 5

**Gate 5 status: PENDING USER APPROVAL.**

Approval should cover:
1. 13-chapter narrative sequence;
2. Guided Story + Explore Map split;
3. map-state sequence;
4. structure popup fields;
5. filters;
6. technical-detail placement;
7. mobile interaction pattern.

After approval, Phase 6 can establish the production codebase and implement the agreed interactions.