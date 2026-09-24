# GWRPZ — From Mapping to Decision

Interactive groundwater-recharge evidence article by **Kaushal Gadariya, Soil and Water Conservation Engineer**.

## Live article

https://knightfox789.github.io/GWRPZ/

## Current production state

- clean-reset article: **published**
- public article baseline: **120 interventions / 109 unique sites**
- GWRPZ implementation split: **68 Moderate / 52 High**
- primary litholog profiles: **19**
- representative A–AA section logs: **6**
- groundwater monitoring: **June 2024 / June 2025 / June 2026**
- public frontend: static HTML/CSS/JavaScript/SVG
- GitHub Pages deployment root: `docs/`

## Repository roles

- `main` — deployable production state
- `docs/` — current public GitHub Pages output
- `project/clean-reset/` — clean-reset project, QA and handover records
- `release-v1.0.x` — published release snapshot branches
- `legacy-pre-clean-reset-2026-09-24` — pre-clean-reset public archive

## Maintenance

Start with:

- `project/clean-reset/step10f/GWRPZ_Final_Handover_Index_v1.0.md`
- `project/clean-reset/step10f/GWRPZ_Maintenance_Update_Guide_v1.0.md`
- `project/clean-reset/step10f/GWRPZ_Public_Data_Regeneration_Guide_v1.0.md`

Scientific/source authority remains in the project Library and the authoritative clean-reset registers. The published website is an output, not the source of truth.

## Deployment

`.github/workflows/pages.yml` deploys `docs/` on pushes to `main` that modify `docs/**` or the Pages workflow.

## Update rule

**Editorial change → patch release.**  
**Data change → regenerate public-safe data and rerun QA.**  
**Method/story change → reopen the relevant clean-reset evidence/story phases.**
