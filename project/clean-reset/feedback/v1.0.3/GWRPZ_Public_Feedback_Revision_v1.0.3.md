# GWRPZ Public Feedback Revision v1.0.3

**Date:** 24 September 2026  
**Status:** READY FOR PUBLICATION

## V08 groundwater-monitoring revision

### Cartography
- Reworked the groundwater-depth palette into a clearer six-class hydro-monitoring sequence from light mint/aqua to deep navy.
- Added drainage overlay to all three June maps.
- Added lineament overlay to all three June maps.
- Added implemented-site overlay using the 109 unique intervention locations.
- All overlays use the same groundwater-raster georeferencing and are shown consistently across 2024, 2025 and 2026.

### Comparison emphasis
- The default comparison now opens on **2024→2026** to show the full monitoring period first.
- The full-period comparison shows:
  - **46** locations moving to a shallower groundwater-depth class;
  - **56** remaining in the same class;
  - **7** moving to a deeper class.

### Positive publication narrative
A compact three-point interpretation is added immediately after V08:

1. From June 2024 to June 2026, **46 of 109 monitored locations moved to a shallower groundwater-depth class**, while 7 moved to a deeper class and 56 remained in the same class.
2. The **10–20 m bgl class is the most common in 2025 and 2026**, covering 81 and 89 monitored locations respectively.
3. Drainage, lineament and implemented-site overlays place these changes in their landscape context and help show where continued monitoring can focus.

The text describes the positive monitoring shift directly without attributing the change to any single intervention.

## Browser QA

### Desktop 1440×1000
- console/page errors: **0**
- horizontal overflow: **False**
- 3 groundwater maps rendered
- drainage / lineament / implemented-site overlay legend present
- 2024→2026 comparison opens by default

### Mobile 390×844
- console/page errors: **0**
- horizontal overflow: **False**
- V08 stacks correctly
- interpretation box remains readable

## Evidence integrity

No groundwater class values, site counts, intervention locations or monitoring transitions were changed.

The revision changes:
- V08 visual styling;
- map context overlays;
- ordering of the comparison control;
- publication-language interpretation after V08.