# Web GIS Data Manifest

**Version:** v0.1  
**Date:** 22 September 2026  
**Project:** From Mapping to Decision — Interactive Groundwater Recharge Planning  
**Phase:** Phase 4 — Web data preparation  
**Status:** DATA PACKAGE COMPLETE; Gate 4 pending graphical browser smoke test  
**Persistent Library package:** `/GW Recharge/05_Web_Data/Phase4_Web_Data_Package_v0.1.zip`  
**Archive internal root:** `05_Web_Data/`

---

### Library persistence note

The complete web-data directory is preserved as one exact ZIP snapshot because direct per-file container-to-Library upload was unavailable in this session.

Inside the archive, the intended web structure is preserved exactly:

- `05_Web_Data/vectors/`
- `05_Web_Data/structures/`
- `05_Web_Data/rasters/`
- `05_Web_Data/config/`
- `05_Web_Data/styles/`
- `05_Web_Data/Web_GIS_Data_Manifest_v0.1.md`

References below to `/GW Recharge/05_Web_Data/...` describe the intended extracted/published paths. Until extraction into a build workspace, the authoritative persistent snapshot is the ZIP package above.


## 1. Purpose

This manifest records the browser-oriented GIS derivatives created from the validated Phase 2 and Phase 3 evidence base. It preserves lineage, conversion choices, styling conventions, payload size, and known limitations.

The original GIS sources remain unchanged.

Phase 4 does not alter the scientific evidence. It only prepares validated evidence for efficient browser use.

---

## 2. Format decision

### Vector layers

**Format:** GeoJSON, EPSG:4326.

Reason:
- current feature counts and geometry sizes are small;
- total vector payload is well below 1 MB;
- direct GeoJSON keeps the first web implementation simple and inspectable;
- PMTiles / vector tiling would add build and debugging complexity without a present performance need.

### Categorical raster layers

**Format:** transparent RGBA PNG + explicit corner coordinates in `config/raster_sources.json`.

Reason:
- the authoritative target grid is only 789 × 1066 cells for the principal reconstruction layers;
- category values are discrete 1/2/3;
- PNG compresses these categorical maps efficiently;
- MapLibre-compatible image-source metadata can be derived from the supplied raster bounds;
- no resampling occurs during PNG conversion.

**Important:** the PNGs are presentation derivatives. The TIFF sources / accepted analysis rasters remain authoritative.

---

## 3. Web vector derivatives

| Layer | Features | Simplification | Source vertices | Web vertices | Reduction | Area change | Length change | Bytes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| villages | 50 | 10 m | 7,681 | 6,649 | 13.436% | 0.00018% | — | 153,037 |
| aquifers | 9 | 10 m | 2,121 | 1,611 | 24.045% | -0.00085% | — | 37,522 |
| drainage_order | 796 | 5 m | 12,079 | 9,872 | 18.271% | — | -0.04674% | 307,292 |
| lineaments | 52 | 0 m | 131 | 131 | 0.000% | — | 0.00000% | 9,640 |
| lulc | 7 | 10 m | 19,014 | 14,307 | 24.755% | 0.01659% | — | 314,994 |
| interventions | 58 | 0 m | 58 | 58 | 0.000% | — | — | 26,747 |

### Vector lineage

#### `vectors/villages.geojson`
Source: Package A `Villages.shp`.  
Web attributes: village, block, gram panchayat, area.  
Simplification: 10 m coverage-aware simplification to retain shared village boundaries.

#### `vectors/aquifers.geojson`
Source: Package A `Aquifers.shp`.  
Web attributes: aquifer group/detail, aquifer system, hydraulic condition, recharge score.  
Simplification: 10 m topology-preserving simplification.

#### `vectors/drainage_order.geojson`
Source: Package A `Drainage_Order.shp`.  
Web attributes: source ID and stream order.  
Simplification: 5 m topology-preserving simplification.

#### `vectors/lineaments.geojson`
Source: Package A `Lineaments.shp`.  
No geometry simplification.  
The layer is for spatial context and nearest-distance interpretation. It must not be used to revive the historical 19/58 literal-intersection claim.

#### `vectors/lulc.geojson`
Source: accepted Phase 2A repaired `LULC3` derivative.  
Seven classes retained: Agriculture, Habitat, River Bed, Rocks, Shrubs, Trees, Waterbodies.  
Simplification: 10 m topology-preserving per-feature simplification.  
River Bed and Waterbodies remain separate.

#### `structures/interventions.geojson`
Source: accepted Phase 2E structure QA derivative.  
No point simplification.  
Exported fields use:
- sampled final GWRPZ class;
- nearest-stream order and distance;
- nearest-lineament distance;
- direct geometric intersection flag;
- Siting Alignment Spatial Setting.

The historical binary `Lineament_` attribute is deliberately excluded from the web derivative.

---

## 4. Web raster derivatives

The following categorical raster images are in `/GW Recharge/05_Web_Data/rasters/`:

- `gwrpz_class.png`
- `aquifer_score.png`
- `slope_score.png`
- `drainage_density_score.png`
- `lineament_density_score.png`
- `lulc_score.png`

### Authoritative lineage

- `gwrpz_class.png` ← supplied final `GWRPZ_Class.tif`
- five score PNGs ← accepted Phase 2B target-grid score rasters

### GWRPZ control

The supplied final `GWRPZ_Class.tif` remains the final-class reference.

The Phase 2D threshold candidate raster is **not** exported as a final GWRPZ layer.

### Georeferencing

`config/raster_sources.json` stores, for every image:
- source CRS;
- pixel dimensions;
- source NoData;
- class counts;
- transformed top-left, top-right, bottom-right and bottom-left WGS84 coordinates.

The PNG conversion preserves target-grid pixels exactly and does not perform raster resampling.

---

## 5. Styling / legend configuration

`styles/layer_styles.json` defines the initial, editable styling contract.

### GWRPZ / score palette

- Score / Class 1 — Low: `#BA493A`
- Score / Class 2 — Moderate: `#E2AA3E`
- Score / Class 3 — High: `#298079`

These are web presentation colors, not analytical values.

LULC, drainage, lineament, village and intervention styling is also recorded in the same file and can be refined during Phase 5 without changing data.

---

## 6. Payload and technical QA

**Core assets checked:** 15  
**HTTP static-server responses:** 15 / 15 returned HTTP 200  
**Core payload:** 1.077 MB  
**Estimated gzip transfer size:** 0.460 MB  

All GeoJSON files:
- parse as valid FeatureCollections;
- use EPSG:4326 coordinates;
- contain only selected publication-safe attributes;
- retain valid geometries after conversion.

All raster PNGs:
- decode successfully;
- are RGBA;
- retain transparent NoData;
- use the documented categorical palette.

Hashes are recorded in:

`config/web_payload_hashes.csv`

Detailed metrics are recorded in:

`config/Phase4_Web_Data_QA_Metrics_2026-09-22.json`

---

## 7. Responsive/browser smoke-test status

A zero-dependency smoke-test page exists at:

`config/phase4_smoke_test.html`

It:
- fetches the actual web GeoJSON and raster metadata;
- draws the final GWRPZ image and vector layers;
- reports feature counts and load/render timing;
- contains a viewport meta tag;
- switches to a one-column layout below 720 px;
- uses an SVG viewBox / preserved aspect ratio.

Static responsive-harness checks: PASS.

### Graphical browser limitation

The current execution environment's installed Chromium hangs even on `about:blank`, so a real graphical desktop/mobile browser screenshot could not be produced reliably.

This is an environment limitation, not a detected GIS-data failure.

**Gate decision:** Gate 4 remains OPEN pending one successful graphical browser smoke test at desktop and mobile viewport sizes.

No Phase 5 work should start until that check passes or an equivalent browser test is completed in a functioning runtime.

---

## 8. Publication and evidence safeguards carried into web data

1. GWRPZ is relative recharge potential, not guaranteed recharge.
2. Final GWRPZ class comes from the supplied final raster.
3. Historical final Class 1/2 break remains unresolved.
4. Stream order at structures is a nearest-network association with distance retained.
5. No structure point directly intersects supplied lineament geometry.
6. Nearest-lineament distance is the reproducible structural relationship.
7. Historical `Lineament_ = 1` must not be described as a literal intersection.
8. `Siting Alignment Spatial Setting` is not measured performance.
9. Field / hydrogeological verification remains necessary before siting decisions.

---

## 9. Phase 4 checkpoint

### Completed
- web-safe vector derivatives;
- web-safe categorical raster derivatives;
- metadata / source lineage;
- layer styles and legends;
- payload sizing;
- geometry and parsing QA;
- static HTTP asset loading;
- responsive smoke-test harness.

### Pending
- graphical browser smoke test at desktop and mobile viewport.

**Phase 4 status:** IN PROGRESS — data preparation complete; Gate 4 pending graphical browser smoke test.

**Exact next step:** run the existing `config/phase4_smoke_test.html` in a functioning browser at desktop and mobile viewport sizes. If all layers load and the responsive layout remains usable, record the result, pass Gate 4, update the Master Plan / Recovery Log, and only then start Phase 5.