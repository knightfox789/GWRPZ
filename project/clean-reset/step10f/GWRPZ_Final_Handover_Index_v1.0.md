# GWRPZ Final Handover Index v1.0

**Project:** From Mapping to Decision  
**Live site:** https://knightfox789.github.io/GWRPZ/  
**Repository:** `knightfox789/GWRPZ`  
**Handover stage:** Step 10F

## 1. What is being handed over

A published, static, mobile-responsive groundwater-recharge evidence article with:
- V01–V09 interactive evidence visuals;
- sanitized public data embedded or referenced by the page;
- GitHub Pages deployment workflow;
- evidence/claim/source registers;
- Story Lock;
- Master Plan;
- Recovery Log;
- maintenance/update guide;
- public-data regeneration guide;
- release manifests and hashes.

## 2. Current controlling Library records

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

### Releases / revisions
- `/GW Recharge/06_Web_Article/Clean_Reset_v1/releases/`
- `/GW Recharge/06_Web_Article/Clean_Reset_v1/revisions/`

## 3. Repository roles

`main`
: deployable production state.

`release-v1.0.x`
: immutable-by-convention snapshot branches for published patch versions.

`legacy-pre-clean-reset-2026-09-24`
: archive of the public site before the clean-reset replacement.

`.github/workflows/pages.yml`
: GitHub Pages deployment workflow.

`docs/`
: deployed public root.

`project/clean-reset/`
: project documentation / handover records.

## 4. Final production-root policy

After Step 10F housekeeping, `docs/` should contain only files required by the live article.

Legacy Phase-4 smoke-test files, old 58-record intervention output, old village/vector exports and obsolete prototypes should remain recoverable in Git history/legacy branches, but should not continue to ship in the current GitHub Pages artifact.

## 5. Update decision tree

**Only wording/layout changed?**  
→ patch branch → browser QA → PR → release snapshot.

**Numbers/data changed?**  
→ source register → claim register → regenerate public data → privacy/GIS QA → rebuild affected visuals → integrated QA → release.

**Method/story changed?**  
→ reopen Story Lock and relevant clean-reset phases.

## 6. Rollback anchors

- pre-clean-reset archive: `legacy-pre-clean-reset-2026-09-24`
- each published clean-reset state: `release-v1.0.x`

## 7. Known connector limitation

The available GitHub connector does not expose Git-tag creation. Release snapshot branches are therefore used as the machine-created release anchors in this workflow. If a formal Git tag is required, create it in GitHub manually at the final release commit.

## 8. Handover acceptance

Step 10F is complete when:
- stale deployment-root artifacts are removed;
- current live article remains unchanged in meaning/content;
- latest Pages deployment succeeds;
- deployed files/hashes are recorded;
- maintenance guide is saved;
- regeneration guide is saved;
- Master Plan and Recovery Log are finalized;
- final release snapshot branch is created.