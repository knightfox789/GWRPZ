# GWRPZ Step 10E — Publication & Deployment Verification v1.0

**Project:** From Mapping to Decision  
**Date:** 24 September 2026  
**Status:** **STEP 10E COMPLETE — PUBLICATION DEPLOYMENT VERIFIED**  
**Live URL:** https://knightfox789.github.io/GWRPZ/  
**Repository:** `knightfox789/GWRPZ`

## Publication actions completed

1. Preserved the pre-replacement `main` state on:
   `legacy-pre-clean-reset-2026-09-24`.

2. Promoted the approved Step 10D release candidate to:
   `docs/index.html`.

3. Added production metadata/support files:
   - `docs/social-preview.svg`
   - `docs/robots.txt`
   - `docs/sitemap.xml`

4. Marked PR #1 ready and merged it into `main`.

5. Merge commit:
   `07b261b271806da9a1bb8c8558938c8de2d49732`

6. Created a release snapshot branch:
   `release-v1.0.0`

## GitHub Pages deployment

GitHub Actions workflow:
- workflow: **Deploy GitHub Pages**
- run ID: **35957623561**
- conclusion: **success**
- deployed commit: `07b261b271806da9a1bb8c8558938c8de2d49732`

The `actions/deploy-pages` step reported:

- Pages deployment status: **success**
- evaluated environment URL:
  **https://knightfox789.github.io/GWRPZ/**

## Deployment artifact verification

GitHub Pages artifact:
- artifact ID: **10791595106**
- artifact digest: `sha256:1be44bc4ab0f06f3f706e8470b2b434d839896aad4d0b3ada397b6cb5c93d88a`
- deployed files: **29**

Deployed `index.html`:
- bytes: **613,004**
- SHA-256: `fda70f14e4b0dae5d213b0fb22f3b6c35caf29b3e0766a92c7c30142d6ff4464`
- Git blob SHA-1: `749165c396b09cd5cf82881f0cec77b22005254b`

GitHub `main/docs/index.html` blob SHA:
- `749165c396b09cd5cf82881f0cec77b22005254b`

**Integrity result: PASS.**  
The GitHub Pages deployment artifact contains the exact `index.html` blob committed at the production root on `main`.

## Production support files verified in deployment artifact

- `social-preview.svg` — present
- `robots.txt` — present
- `sitemap.xml` — present
- `.nojekyll` — preserved
- complete production `index.html` — present

## Evidence and privacy state

The publication inherits the Step 10D Gate P5 approvals:
- 120 interventions / 109 unique sites;
- 52 High / 68 Moderate / 0 Low;
- 19 litholog profiles;
- six A–AA logs;
- 29/29 substantive claims traceable;
- no private project-management fields in the public payload;
- groundwater remains monitoring feedback rather than a causal-impact claim;
- `Y` remains a source flag;
- A–AA remains conceptual.

## Deployed-URL verification note

The available web-reading service in this environment does not fetch `github.io` pages directly.  
Accordingly, Step 10E verifies publication through three independent GitHub-side checks:

1. successful `Deploy GitHub Pages` workflow;
2. the deployment step explicitly reporting the production environment URL;
3. exact blob-level match between `main/docs/index.html` and the downloaded GitHub Pages deployment artifact.

This is sufficient to confirm that the approved production artifact was the artifact GitHub Pages deployed. A normal browser open of the live URL remains a useful human-facing smoke check.

## Step 10E decision

**STEP 10E: PASS — PUBLICATION DEPLOYED.**

The public root has been replaced by the clean-reset article, and the prior public state remains recoverable on the archival branch.

## Next project step

**STEP 10F — Handover / maintenance / update workflow**

Step 10F should finalize:
- maintenance and regeneration guide;
- final recovery checkpoint;
- final release manifest/hashes;
- update workflow for future data/article revisions;
- repository housekeeping.

The current GitHub connector does not expose a tag-creation action. A release snapshot branch (`release-v1.0.0`) therefore pins the publication commit for now; creation of an actual Git tag, if desired, must be done through a GitHub interface that exposes tag creation.