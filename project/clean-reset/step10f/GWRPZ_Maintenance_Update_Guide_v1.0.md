# GWRPZ Maintenance & Update Guide v1.0

**Project:** From Mapping to Decision  
**Live site:** https://knightfox789.github.io/GWRPZ/  
**Repository:** `knightfox789/GWRPZ`  
**Current public article baseline:** v1.0.4 before Step 10F housekeeping  
**Primary owner:** Kaushal Gadariya — Soil and Water Conservation Engineer

## 1. Purpose

This guide is the operating manual for maintaining the published groundwater-recharge article after the clean-reset build.

The key rule is:

> **Do not patch scientific numbers or GIS results directly in the published HTML when the underlying evidence changes. Regenerate the public-safe evidence first, then rebuild the article.**

Small editorial and styling corrections can be made as patch releases, but analytical changes must move through the evidence and public-data controls.

## 2. Current production model

The public site is a static GitHub Pages article.

- deployment root: `docs/`
- production article: `docs/index.html`
- V02 maps: embedded inside `index.html` to avoid missing-asset failures
- V03 intervention points: plotted against the same final GWRPZ georeferencing used by the map
- V08 overlay: `docs/assets/v08-overlay.svg`
- social metadata: `docs/social-preview.svg`
- search support: `docs/robots.txt` and `docs/sitemap.xml`
- deployment workflow: `.github/workflows/pages.yml`
- runtime API/database: none

The page is intentionally dependency-light. The scientific/public evidence authority remains in the project Library and clean-reset records, not only in `docs/`.

## 3. Authority order

When sources disagree, use this order:

1. authoritative source/decision register;
2. authoritative claim/evidence register;
3. approved Story Lock;
4. sanitized public-data package;
5. editorial/content package;
6. production HTML.

Never treat an older web file as stronger evidence than the source and claim registers.

## 4. Change classes

### A. Editorial patch
Examples:
- wording;
- headings;
- author bio;
- link correction;
- spacing;
- colour tuning that does not change analytical meaning.

Workflow:
1. branch from `main`;
2. edit;
3. desktop/mobile smoke test;
4. PR;
5. merge;
6. confirm Pages deployment;
7. create a release snapshot branch.

Recommended version bump: `v1.0.x`.

### B. Visual/cartographic patch
Examples:
- palette;
- legend layout;
- overlays;
- label placement.

Additional checks:
- map class meaning unchanged;
- point/raster alignment verified;
- no layer is visually implying unsupported causality;
- all external assets are actually deployed, or embed them in the HTML.

### C. Data refresh
Examples:
- corrected intervention record;
- new monitoring year;
- new litholog;
- updated GIS source.

Required workflow:
1. update the authoritative source register;
2. update/reconfirm the claim register;
3. regenerate sanitized public data;
4. rerun privacy and invariant tests;
5. rebuild affected visual(s);
6. rerun factual/GIS/browser QA;
7. publish as a new minor release.

Recommended version bump: `v1.1.0`, `v1.2.0`, etc.

### D. Methodology/story change
Examples:
- new GWRPZ factor;
- changed weighting;
- revised intervention-selection logic;
- major new evidence chain;
- new geography.

Required:
- reopen Story Lock;
- rebuild the relevant public-data contracts and visual sequence;
- full integrated QA.

Recommended version bump: `v2.0.0`.

## 5. Release workflow

Use this sequence for every release:

1. create a short-lived branch from `main`;
2. make the smallest necessary change;
3. run evidence/privacy/GIS/browser checks appropriate to the change class;
4. open PR into `main`;
5. merge only after checks pass;
6. verify GitHub Pages workflow success;
7. verify the deployed `index.html` hash/blob against `main`;
8. create a `release-vX.Y.Z` snapshot branch;
9. update the recovery log;
10. save the release package/manifest in `/GW Recharge/06_Web_Article/Clean_Reset_v1/releases/`.

## 6. Rollback

Two stable recovery references are maintained:

- `legacy-pre-clean-reset-2026-09-24` — public state before the clean-reset replacement;
- release snapshot branches — one per published clean-reset version.

To roll back:
1. identify the desired release snapshot;
2. restore `docs/` from that snapshot on a recovery branch;
3. PR to `main`;
4. verify Pages deployment;
5. record the rollback in the recovery log.

Do not force-move `main` unless there is an emergency and the repository history is understood.

## 7. GIS-specific maintenance rules

### V02
- preserve real aquifer, slope and LULC class labels;
- preserve drainage/lineament context;
- if using external SVG/image files, confirm they exist under `docs/`;
- embedding maps in `index.html` is the current stable approach.

### V03
- do not manually nudge intervention points;
- use the authoritative raster georeferencing/transform;
- after any GIS refresh, verify all intervention points against their stored GWRPZ class at the plotted pixel/location.

### V06/V07
- preserve primary litholog order/depth;
- do not reintroduce source identities;
- keep the section conceptual unless stronger hydrogeological evidence is added.

### V08
- use a single class definition across years;
- preserve a common map extent for comparison;
- drainage and lineament remain context layers;
- implemented structures remain context;
- describe positive class movement only as observed monitoring change unless causal evidence is added.

## 8. Privacy rules

Never publish:
- internal row/source IDs;
- source shaft identities;
- village/block/district attributes when restricted by the controlling source register;
- cost, storage, beneficiary, coverage or wells-benefited fields;
- internal fund/SOP/management fields;
- unresolved conflict-record identities;
- raw latitude/longitude columns.

Geometry should only be carried through approved public geometry objects required by the visual.

## 9. Browser/release checks

Minimum checks after each patch:
- desktop layout;
- mobile layout;
- V02 map loading;
- V03 background + point alignment;
- V08 overlay loading;
- no horizontal overflow;
- no console/page errors;
- keyboard navigation for interactive controls;
- source and author links;
- Pages workflow success.

## 10. Current reference hashes before Step 10F housekeeping

- public commit: `1149e009eb7abd03d7ce5fed39594510fa6d0072`
- `docs/index.html` Git blob: `08ddaeba57d304f8952cc831f4c2b241906446ce`
- `docs/index.html` SHA-256: `643f1e75d3de00d47b93cce4b9a28d7dc3f3361337ac6a49797a0e4a713ebee3`
- `docs/assets/v08-overlay.svg` SHA-256: `2824531847bb4a72dbb0cefc05e25bfad694e3358d45e44aaa83e675cd03778f`

These references identify the v1.0.4 publication state before the final Step 10F deployment-root cleanup.