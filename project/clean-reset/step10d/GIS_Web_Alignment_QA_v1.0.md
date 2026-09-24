# GIS Web Alignment QA v1.0

**Result:** **PASS**

## Invariants
- interventions: 120
- unique sites: 109
- GWRPZ: 68 Moderate / 52 High / 0 Low
- multi-intervention sites: 10; records at those sites: 21; maximum at one site: 3
- litholog profiles: 19
- A–AA section points: 6
- groundwater site summaries: 109

All Step 9 public files carried into the release candidate match their authoritative byte counts and SHA-256 hashes.

The six GWRPZ/factor rasters retain the approved Step 9 three-class palette and metadata. All 120 intervention geometries fall within the final GWRPZ raster extent.

June 2024/2025/2026 groundwater rasters use one 660×904 grid, 30 m cell size and common six-class semantics.

Verified transitions:
- 2024→2025: 45 shallower / 61 same / 3 deeper
- 2025→2026: 14 / 81 / 14
- 2024→2026: 46 / 56 / 7

Litholog→site missing joins: 0. A–AA→litholog missing joins: 0.

Interpretation controls remain locked: GWRPZ decision support; lineaments context; Y as source flag; A–AA conceptual; groundwater as monitoring feedback.

**Decision:** PASS.
