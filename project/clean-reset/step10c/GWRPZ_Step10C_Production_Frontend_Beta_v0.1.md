# GWRPZ Step 10C — Production Front End Beta v0.1

**Date:** 24 September 2026  
**Status:** FUNCTIONAL BETA BUILT — Gate P4 browser checks pending/completed in companion QA

## Delivery

`docs/preview-v1/index.html` is a self-contained production beta of the approved long-form article. It embeds the sanitized Step 9 public data required for V01–V09 and does not require a runtime API, database, map server, third-party tiles, or external JavaScript library.

## Architecture choice

The Master Plan recommended Astro + MapLibre. For this gated preview, the implementation uses **dependency-free semantic HTML + CSS + browser-native JavaScript/SVG**. This keeps the preview reproducible in the current build environment, removes CDN/API dependencies, and makes the entire beta testable as one static artifact.

The interaction architecture still follows the approved design: scroll state, compact toggles, SVG maps/sections, linked profile selection, synchronized small multiples and progressive reveal. If a framework wrapper is desired later, this beta can be componentised without changing the Story Lock or public-data contracts.

## Implemented visuals

- V01 interactive question-evolution spine
- V02 six-state GWRPZ factor/final raster reveal
- V03 filtered intervention/GWRPZ map with type + compact FY/New-Renovation controls
- V04 four-family surface-opportunity selector
- V05 simplified decision-role matrix + expandable full matrix
- V06 anonymous 19-profile litholog explorer with lithology legend
- V07 six-log conceptual A–AA section
- V08 synchronized 2024/2025/2026 groundwater small multiples + transition selector
- V09 Map → Verify → Understand → Monitor learning loop

## Progressive enhancement

All narrative, methods, acknowledgement, note, references and author content remain readable without JavaScript. Interactive figures include plain-language headings/subtitles and `noscript` summaries.

## Public-data handling

The beta embeds only Step 9 sanitized public fields. Raw coordinates are never printed as properties or tooltip values; public geometry is used only to place anonymous points.

## Gate P4 criteria

- all article sections rendered;
- all nine visual modules implemented;
- data are embedded from Step 9 sanitized package;
- no external API / database required;
- desktop/mobile responsive rules included;
- reduced-motion rules included;
- methods, references, acknowledgement, note and author footer included.

## GitHub branch

The beta is staged on `knightfox789/GWRPZ` branch `clean-reset-v1` at `docs/preview-v1/index.html`. The Step 10C commits are isolated on this branch; the public root has not been replaced.


Draft review PR: `https://github.com/knightfox789/GWRPZ/pull/1`