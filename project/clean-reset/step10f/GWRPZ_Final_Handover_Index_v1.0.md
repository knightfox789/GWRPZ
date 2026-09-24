# GWRPZ Final Handover Index v1.0

**Project:** From Mapping to Decision  
**Live site:** https://knightfox789.github.io/GWRPZ/  
**Repository:** `knightfox789/GWRPZ`  
**Step:** 10F  
**Status:** **COMPLETE — FINAL HANDOVER READY**

## 1. Final state

The clean-reset workflow is complete through Step 10F.

The public article remains the approved v1.0.4 reader-facing build. Step 10F performed handover and repository cleanup without changing the article content.

Final publication / housekeeping record:
- Pages publication commit: `f6a33e68dcfde8b2e11531d5279bc3ded85e9c2e`
- GitHub Pages run: `35978788805` — success
- deployed `index.html` SHA-256: `643f1e75d3de00d47b93cce4b9a28d7dc3f3361337ac6a49797a0e4a713ebee3`
- final release snapshot branch: `release-v1.0.5`

## 2. What is handed over

- published V01–V09 interactive article;
- controlling source/claim/story records;
- sanitized public-data package;
- Master Plan;
- Recovery Log;
- maintenance/update guide;
- public-data regeneration guide;
- final deployment/handover record;
- final release manifest;
- release/rollback branches.

## 3. Controlling Library records

### Evidence / story
- `/GW Recharge/08_Project_Admin/GWRPZ_Authoritative_Source_and_Decision_Register_v1.4.md`
- `/GW Recharge/08_Project_Admin/GWRPZ_Authoritative_Spatial_and_Professional_Evidence_Register_v1.1.md`
- `/GW Recharge/08_Project_Admin/GWRPZ_Web_Article_Story_Lock_v1.1.md`
- `/GW Recharge/08_Project_Admin/GWRPZ_Interactive_Web_Article_Clean_Reset_Master_Plan_v1.0.md`

### Recovery
- `/GW Recharge/09_Backup_Recovery/GWRPZ_Clean_Reset_Continuation_and_Recovery_Log_v1.0.md`
- `/GW Recharge/09_Backup_Recovery/GWRPZ_Clean_Reset_Restart_Prompt_v1.0.md`

### Public data
- `/GW Recharge/05_Web_Data/Clean_Reset_v1/`

### Final handover
- `/GW Recharge/06_Web_Article/Clean_Reset_v1/handover/Step10F_v1.0/`

## 4. Repository roles

`main`
: current production + project-documentation state.

`docs/`
: minimal GitHub Pages deployment root.

`project/clean-reset/step10f/`
: maintenance, regeneration and final handover records.

`release-v1.0.5`
: final Step 10F release snapshot.

`legacy-pre-clean-reset-2026-09-24`
: archive of the pre-clean-reset public site.

## 5. Final deployment-root contents

The verified Pages artifact contains only:
1. `.nojekyll`
2. `index.html`
3. `assets/v08-overlay.svg`
4. `social-preview.svg`
5. `robots.txt`
6. `sitemap.xml`

Obsolete Phase-4/prototype outputs, the old 58-record structure export, and old village/vector files were removed from the active deployment root. They remain recoverable through Git history and archive/release references.

## 6. Update decision tree

**Wording/layout only**  
→ patch branch → browser QA → PR → deploy → release snapshot.

**Evidence/data change**  
→ source register → claim register → regenerate public-safe data → privacy/GIS QA → rebuild affected visual(s) → integrated QA → release.

**Method/story change**  
→ reopen Story Lock and the relevant clean-reset phases.

## 7. Rollback anchors

- `legacy-pre-clean-reset-2026-09-24`
- `release-v1.0.0`
- `release-v1.0.1`
- `release-v1.0.2`
- `release-v1.0.3`
- `release-v1.0.4`
- `release-v1.0.5`

## 8. Git-tag note

The available GitHub connector does not expose Git-tag creation. Release snapshot branches are therefore the machine-created release anchors. A formal tag can be added manually in GitHub if required.

## 9. Restart rule

For any future continuation, start from:
1. this Final Handover Index;
2. the latest Recovery Log;
3. the Maintenance & Update Guide;
4. the Public-Data Regeneration Guide.

Do not restart from old Phase-4/Phase-5 prototype material.

**Handover result: PASS.**