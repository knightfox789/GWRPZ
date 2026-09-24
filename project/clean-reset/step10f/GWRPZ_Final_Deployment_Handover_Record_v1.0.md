# GWRPZ Final Deployment & Handover Record v1.0

**Project:** From Mapping to Decision  
**Step:** 10F — Handover / maintenance / update workflow  
**Status:** **COMPLETE — FINAL HANDOVER READY**  
**Live URL:** https://knightfox789.github.io/GWRPZ/

## 1. Final publication state

Step 10F does **not** alter the v1.0.4 reader-facing article content.

The final housekeeping deployment uses:

- publication commit: `f6a33e68dcfde8b2e11531d5279bc3ded85e9c2e`
- GitHub Pages run: `35978788805`
- Pages artifact ID: `10799650267`
- Pages artifact digest: `sha256:88a9df0fbebc5e1301de1964569d900f1c9c7ca8c01ade5c45ec45f476d7c8fb`
- production `index.html` Git blob: `08ddaeba57d304f8952cc831f4c2b241906446ce`
- production `index.html` SHA-256: `643f1e75d3de00d47b93cce4b9a28d7dc3f3361337ac6a49797a0e4a713ebee3`

The `index.html` hash is unchanged from v1.0.4, confirming that Step 10F housekeeping did not modify the live article itself.

## 2. Deployment-root cleanup

Before Step 10F, the Pages artifact still carried obsolete Phase-4 and prototype material, including:
- an old 58-record intervention export;
- village/vector exports;
- old rasters;
- Phase-4 config/smoke-test files;
- preview/prototype pages;
- unused assets.

These files were not required by the current article and increased the public/stale surface area.

They were removed from the current `docs/` deployment root.

## 3. Final deployed files

The verified GitHub Pages artifact now contains **6 files only**:

1. `.nojekyll`
2. `index.html`
3. `assets/v08-overlay.svg`
4. `social-preview.svg`
5. `robots.txt`
6. `sitemap.xml`

## 4. Handover documentation

Repository:
- `project/clean-reset/step10f/GWRPZ_Final_Handover_Index_v1.0.md`
- `project/clean-reset/step10f/GWRPZ_Maintenance_Update_Guide_v1.0.md`
- `project/clean-reset/step10f/GWRPZ_Public_Data_Regeneration_Guide_v1.0.md`

Library:
- `/GW Recharge/06_Web_Article/Clean_Reset_v1/handover/Step10F_v1.0/`

## 5. Release / rollback anchors

Preserved:
- `legacy-pre-clean-reset-2026-09-24`
- `release-v1.0.0`
- `release-v1.0.1`
- `release-v1.0.2`
- `release-v1.0.3`
- `release-v1.0.4`

Final Step 10F snapshot:
- `release-v1.0.5`

The GitHub connector does not expose tag creation, so release snapshot branches are the recorded release anchors. A formal Git tag may be added manually in GitHub if desired.

## 6. Final operational rule

**Website text/style change:** patch release.  
**Evidence/data change:** regenerate public-safe data and rerun QA.  
**Method/story change:** reopen the relevant clean-reset evidence/story stages.

## 7. Step 10F result

**PASS — handover, maintenance workflow, data-regeneration workflow, deployment cleanup and recovery references are complete.**