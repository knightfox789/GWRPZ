# GWRPZ Web Article — Clean Reset Continuation & Recovery Log v1.0

**Date:** 23 September 2026  
**Status:** CLEAN RESET — STEPS 1–5 COMPLETE; CHECKPOINT BEFORE STEP 6

## Controlling instruction

`/GW Recharge/09_Backup_Recovery/GWRPZ_Clean_Reset_Restart_Prompt_v1.0.md`

## Locked sequence

1. Freeze/archive old state. **COMPLETE**
2. Build authoritative Source & Decision Register. **COMPLETE**
3. Recover original groundwater-level source data; digitize image only as fallback. **COMPLETE**
4. Full GIS revisit using 122 interventions. **COMPLETE**
5. Integrate legacy / monitoring evidence. **NEXT**
6. Create authoritative Spatial & Professional Evidence Register.
7. Lock story.
8. Draft new end-to-end master plan.
9. Build sanitized public web data.
10. Design/build/test/deploy.

## Checkpoint A — Step 1 Freeze / Archive

**Completed:** 23 September 2026

Created:
`/GW Recharge/09_Backup_Recovery/GWRPZ_Clean_Reset_Freeze_Archive_Register_v1.0.md`

Frozen as preserved but non-controlling:
- Phase 5 UX prototypes and interaction specifications;
- Phase 5 content/narrative/storyboard branches;
- old Phase 5 QA branches;
- pre-reset Master Plans v0.1–v0.28;
- old 58-intervention publication evidence and old Spatial Evidence Register;
- old 58-intervention web-ready data package.

No files were deleted.

## Checkpoint B — Step 2 Authoritative Source & Decision Register

**Completed:** 23 September 2026

Created:
`/GW Recharge/08_Project_Admin/GWRPZ_Authoritative_Source_and_Decision_Register_v1.0.md`

Key authority decisions:
- the updated source table contains **122 intervention rows** and is the new intervention baseline;
- 122 is intervention count, not yet unique site count;
- repeated GPS may represent legitimate multi-intervention sites;
- GPS geometry is authoritative for spatial analysis;
- final supplied `GWRPZ_Class.tif` remains the final class reference;
- `LULC3_Multiclass_2026-09-21` remains authoritative LULC;
- reconstructed weighted score remains diagnostic only;
- exact historical final GWRPZ class-break rule remains unresolved and must never be invented;
- field-confirmed MARP / intervention-type logic is retained;
- old 58-derived counts/statistics remain frozen;
- groundwater temporal image is source-only pending recovery of underlying monitoring/GIS data;
- existing-structure diagnosis remains approach context only; source dataset still needs recovery/registration;
- hydrogeological cross-section work is retained as professional-context source evidence;
- Water Security Intelligence / Kaushal Voice / minimal-image direction is retained;
- Mr. Samarpan Hanspara acknowledgement scope is locked;
- public/private data rules are locked.

## Open gaps at this checkpoint

1. Original June 2024/2025/2026 groundwater well/GIS data not yet recovered.
2. Authoritative existing-structure diagnosis dataset not yet registered.
3. Unique site count for 122 interventions not yet derived.
4. All 122 GIS relationships not yet rerun.
5. Public stakeholder-category mapping not yet formalised.
6. Private `HUF_DSC_led` field not yet constructed/verified.
7. Historical final GWRPZ class-break rule remains unresolved.
8. Historical ArcGIS snap/processing environment remains undocumented.
9. Historical binary lineament rule remains unrecovered.
10. Primary litholog / recharge-shaft spreadsheet should be recovered if available for claim-level hydrogeology verification.
11. Rainfall + monitoring consistency + intervention timing must be integrated before groundwater-change interpretation.
12. Defunct Recharge Tubewell role remains open if present in the new source.
13. Public terminology normalization must preserve source traceability.

## Checkpoint C — Step 3 Groundwater-Level Source Recovery

**Completed:** 23 September 2026

User-supplied source package:
`GWL.zip`

Recovered source raster packages:
- `Reclass_June24_SK.tif`
- `Reclass_June25_SK.tif`
- `Reclass_June26_SK.tif`

QA result:
- all three rasters are EPSG:32643;
- all three are 660 × 904 cells;
- all three use an identical 30 m grid and identical extent;
- all three include raster attribute tables defining the groundwater classes;
- class mapping is 0–2, 2–5, 5–10, 10–20, 20–40, >40 m bgl;
- VAT pixel counts match independently recalculated raster counts exactly;
- no screenshot georeferencing/digitisation is required.

Created:
`/GW Recharge/04_GIS_QA/GWRPZ_Groundwater_Level_Source_Recovery_QA_v1.0.md`

Updated authority register:
`/GW Recharge/08_Project_Admin/GWRPZ_Authoritative_Source_and_Decision_Register_v1.1.md`

Source package archived under:
`/GW Recharge/03_GIS_Source/00_Source_Archive/GWL_June_2024_2026_Recovery_2026-09-23/`

### Step 3 residual gaps

Not yet recovered:
- primary monitoring-well point dataset / well IDs;
- measured well-level June values;
- continuous interpolation surfaces / contours;
- interpolation method / parameters;
- source GIS project.

These do not block use of the recovered class rasters for descriptive spatial analysis, but they remain required if the article later makes stronger method or causal claims.

Causal discipline remains locked:
groundwater temporal change must not be attributed to interventions until rainfall, monitoring consistency, intervention timing and hydrogeological context are integrated.

## Previous next step — now completed

**STEP 4 — full GIS analytical revisit on the 122-intervention inventory. — COMPLETE**

Required Step 4 analysis:
- intervention count vs unique site count;
- multi-intervention sites;
- structure type;
- financial year;
- New/Renovation;
- GWRPZ;
- aquifer;
- slope;
- drainage density;
- lineament density;
- LULC;
- nearest drainage order / distance;
- nearest lineament distance;
- structure-type-specific patterns;
- temporal patterns;
- selected site examples;
- groundwater class context where analytically appropriate.

Do not reuse old 58-intervention statistics.

Do not interpret groundwater change causally yet.

Do not start frontend work, Story Lock or the new Master Plan before the analytical revisit and later evidence-integration gates.


## Checkpoint D — Step 4 Full 122-Intervention GIS Analytical Revisit

**Completed:** 23 September 2026

Created QA:
`/GW Recharge/04_GIS_QA/GWRPZ_Clean_Reset_Step4_122_Intervention_GIS_Analytical_Revisit_QA_v1.0.md`

Created internal analytical package:
`/GW Recharge/07_Analysis/Clean_Reset_Step4_122/`

Key fresh results:
- 122 interventions = **111 unique exact GPS sites**;
- **10** exact-GPS sites contain multiple intervention records;
- final GWRPZ: **53 High / 69 Moderate / 0 Low** interventions;
- aquifer context: **97 Alluvium / 24 Limestone / 1 Sandstone**;
- slope: **88 <3% / 32 at 3–8% / 2 >8%**;
- nearest drainage order 1–2: **82 / 122**;
- nearest drainage order 1–3: **97 / 122**;
- median nearest drainage distance: **33.6 m**;
- median nearest lineament distance: **855.3 m**;
- LULC point setting: **35 Waterbodies / 29 Agriculture / 24 River Bed / 24 Shrubs / 8 Habitat / 2 unmatched**;
- groundwater class rasters were sampled at unique-site grain for descriptive temporal context only.

Intervention-type logic supported by fresh GIS:
- Recharge Borewell shows strong lower-order drainage tendency and partial mapped-waterbody correspondence;
- Pond Deepening/Widening shows strong mapped-waterbody correspondence;
- RRWHS strongly corresponds to Habitat context;
- Checkdam/Nala Deepening-Widening shows strong mapped-drainage proximity;
- New Checkdam shows strong mapped-drainage proximity.

Critical interpretation retained:
- GWRPZ is a decision-support layer, not a Class-3-only site-selection rule;
- lineament proximity is structural context, not hydraulic proof;
- groundwater class shifts are descriptive and cannot yet be attributed to interventions.

Updated authority register:
`/GW Recharge/08_Project_Admin/GWRPZ_Authoritative_Source_and_Decision_Register_v1.2.md`

### Step 4 residual gaps moving to Step 5

1. rainfall context for June 2024 / 2025 / 2026;
2. monitoring-well lineage, well-level values and monitoring consistency;
3. intervention construction/completion timing;
4. primary litholog/recharge-shaft data and hydrogeological reconciliation;
5. authoritative existing-structure functionality assessment;
6. field verification for LULC/context mismatches;
7. defunctional recharge-borewell role;
8. explanation of financial-year portfolio shift;
9. public stakeholder mapping for ambiguous source partners;
10. final evidence-backed site examples.

## Exact next step

**STEP 5 ONLY — integrate legacy / hydrogeology / monitoring / field evidence.**

Do not start the Spatial & Professional Evidence Register, Story Lock, new Master Plan, sanitized web data or frontend work until Step 5 has been completed and checkpointed.

## Checkpoint E — Step 5 Hydrogeology / Monitoring / Evidence Integration

**Completed:** 23 September 2026

User-supplied source package:
`litholog.zip`

Archived primary hydrogeology source:
`/GW Recharge/03_GIS_Source/00_Source_Archive/Litholog_Cross_Sections_2026-09-23/`

Created QA:
`/GW Recharge/04_GIS_QA/GWRPZ_Clean_Reset_Step5_Hydrogeology_Monitoring_Evidence_Integration_QA_v1.0.md`

Created internal analytical package:
`/GW Recharge/07_Analysis/Clean_Reset_Step5_Evidence_Integration/`

Updated authority register:
`/GW Recharge/08_Project_Admin/GWRPZ_Authoritative_Source_and_Decision_Register_v1.3.md`

Key Step 5 results:
- primary litholog GIS contains **19 recharge-shaft logs**, codes 101–119, from 19 villages;
- drilling dates represented: **6–17 June 2025**;
- drill depth range: **30.00–51.90 m**, mean **43.69 m**;
- all **19/19 litholog coordinates** exactly link to Step 4 intervention sites;
- all linked sites contain a Recharge Borewell intervention; Bolundra is a valid co-located Pond Deepening/Widening + Recharge Borewell site;
- uploaded cross-section layer contains **6 conceptual traces A–F**;
- legacy A–AA profile is retained as a professional/method source but discrepancies are explicitly registered;
- long-term average annual rainfall **~855 mm/year** is accepted as climate context only;
- a June 2026 MPR provides secondary Sabarkantha rainfall context (0 mm June 2026 vs 163 mm June 2025), but no raw rainfall series is recovered;
- groundwater monitoring sources remain programme-level supporting evidence, not site-level impact evidence.

Evidence ceiling now locked:
- no rainfall-normalized groundwater impact analysis;
- no intervention-attributed metre rise/fall;
- no unverified pumping/yield claims;
- no quantified existing-structure functionality claim;
- no silent reconciliation of legacy-guide discrepancies.

## Exact next step

**STEP 6 ONLY — create the authoritative Spatial & Professional Evidence Register.**

Step 6 must convert Steps 2–5 into a claim-level publication register identifying:
- publishable facts;
- publishable analytical interpretations;
- practitioner-confirmed field logic;
- claims requiring attribution/qualification;
- private/confidential fields;
- claims that must be omitted for insufficient evidence.

Do not start Story Lock, a new Master Plan, sanitized web data or frontend work until Step 6 is completed and checkpointed.


## Checkpoint F — Step 6 Authoritative Spatial & Professional Evidence Register

**Completed:** 23 September 2026

Created:
`/GW Recharge/08_Project_Admin/GWRPZ_Authoritative_Spatial_and_Professional_Evidence_Register_v1.0.md`

Purpose:
- converts Steps 2–5 into a **claim-level publication authority**;
- every future article claim must trace to a `PE-###` entry;
- distinguishes publishable fact, publishable interpretation, practitioner-confirmed logic, qualified/attributed claim, private/internal-only content, and omit/not-supported content.

Key Step 6 decisions:
- the 122-intervention / 111-site evidence is now the only current intervention publication baseline;
- GWRPZ is publishable as decision-support evidence, not as a Class-3-only siting rule;
- intervention-type field logic and the fresh GIS spatial support are separated so GIS is not made to prove field facts it cannot prove;
- groundwater temporal evidence is publishable only as class-band / programme-monitoring context, not intervention impact;
- ~855 mm/year rainfall is long-term climatic context only;
- primary 19-litholog source and its exact linkage to intervention sites are publishable facts;
- legacy hydrogeological discrepancies are retained as QA and primary source values take precedence;
- exact historical GWRPZ class-break rule remains unresolved;
- raw GPS, partner attribution, `HUF_DSC_led`, costs, storage, beneficiaries, coverage, wells benefited, detailed fund, SOP and internal management attributes remain private;
- old 58-intervention findings, old groundwater screenshot, old existing-structures map showcase and causal groundwater-impact claims remain prohibited.

The register also defines evidence families recommended for Story Lock without yet deciding final narrative sequence.

## Exact next step

**STEP 7 ONLY — LOCK THE STORY.**

Create:
`/GW Recharge/08_Project_Admin/GWRPZ_Web_Article_Story_Lock_v1.0.md`

The Story Lock must specify:
- final narrative sequence;
- section purpose;
- approved `PE-###` claim IDs per section;
- required map / analytical visual / photograph;
- public/private boundary;
- acknowledgement placement;
- author / professional-legacy positioning;
- reference / methods placement;
- intentional omissions.

Do not draft the clean end-to-end Master Plan until the Story Lock is explicitly approved.
Do not start sanitized public web data, frontend design or another prototype yet.

---

## Checkpoint G2 — Step 6 Re-run: thesis evidence + defensible publication cohort

**Completed:** 23 September 2026

Reason for re-run:
- user supplied the 2021 M.Tech thesis for professional-learning review;
- user authorized exclusion of unresolved conflicted intervention records from the publication analysis.

### Thesis evidence integrated

The thesis is now treated as authoritative **historical/professional-development evidence** for:
- 2021 research origin in groundwater-recharge site identification;
- RS + GIS + MCDA/AHP basin-scale screening;
- six thesis thematic inputs: lineament density, stream density, runoff, slope, LULC and soil;
- structure-specific suitability rules;
- physical ground truthing as validation;
- explicit thesis distinction between broad spatial screening and subsequent detailed hydro-meteorological, hydrological and hydrogeological investigation.

The thesis is **not** used to:
- supply current Sabarkantha statistics;
- replace the current GWRPZ model;
- impose thesis weights/rules on the current project;
- restore universal lineament-intersection logic;
- claim universal transferability independent of context.

### Conflict exclusion and revised publication baseline

The original **122-record source inventory remains preserved unchanged**.

Two unresolved cross-field label conflicts are excluded from publication analytics:
- internal SR 174 — Check Dam Repairing group vs `Deepning of Pond`;
- internal SR 175 — Roof Water Harvesting group vs `Recharge Borewell`.

These two records remain internal QA records and may be restored only if original field/project evidence resolves their type.

**New controlling publication-analysis cohort:**
- **120 interventions**
- **109 unique exact-GPS sites**
- 10 legitimate multi-intervention sites containing 21 records

Revised headline spatial counts:
- GWRPZ = **52 High / 68 Moderate / 0 Low**
- nearest Order 1–2 drainage = **81/120 (67.5%)**
- nearest Order 1–3 drainage = **96/120 (80.0%)**
- median nearest drainage distance = **33.6 m**
- within 100 m mapped drainage = **90/120**
- median nearest lineament distance = **855.3 m**
- within 250 m mapped lineament = **24/120**

Revised intervention types:
- Recharge Borewell 54
- Checkdam/Nala Deepening-Widening 41
- Pond Deepening/Widening 13
- RRWHS 5
- New Checkdam 5
- Checkdam Repair/Renovation 1
- Defunctional Recharge Borewell 1

Revised groundwater temporal grain:
- **109 unique defensible sites**
- 2024→2025 class transitions = 45 shallower / 61 same / 3 deeper
- 2025→2026 = 14 shallower / 81 same / 14 deeper
- 2024→2026 = 46 shallower / 56 same / 7 deeper

### New controlling files

Claim register:
`/GW Recharge/08_Project_Admin/GWRPZ_Authoritative_Spatial_and_Professional_Evidence_Register_v1.1.md`

Source & Decision Register:
`/GW Recharge/08_Project_Admin/GWRPZ_Authoritative_Source_and_Decision_Register_v1.4.md`

QA:
`/GW Recharge/04_GIS_QA/GWRPZ_Clean_Reset_Step6_Rerun_Thesis_and_Publication_Cohort_QA_v1.0.md`

Internal filtered analytical package:
`/GW Recharge/07_Analysis/Clean_Reset_Step6_Revised/`

### Approved professional-learning synthesis for Story Lock

**Spatial hypothesis → field-tested decision support → direct subsurface evidence → monitoring feedback.**

The thesis establishes where the systematic spatial enquiry began.  
The GWRPZ guide shows the shift from map output to location-specific decision support.  
Construction/lithologs add direct subsurface evidence.  
Cross-sections develop hydrogeological understanding.  
Monitoring turns planning into an iterative learning process.

## Exact next step

**STEP 7 ONLY — LOCK THE STORY.**

Use the revised Step 6 v1.1 evidence register and the **120-intervention / 109-site** defensible publication cohort.

Do not draft the new Master Plan, sanitized public web data, frontend design or a prototype before Story Lock is explicitly approved.

---

## Checkpoint G3 — Pre-Step-7 decision-matrix exploration

**Completed:** 23 September 2026

Before Story Lock, three decision-oriented matrices were created from the accepted Step 4/Step 6 spatial evidence and Step 5 primary litholog evidence:

1. **Hydrological Function × Intervention Type**
2. **Surface GIS × Subsurface Litholog Evidence — 19 Recharge Borewell sites**
3. **Site-Decision Evidence Role × Intervention Type**

Controlling analytical cohort remains:
- **120 interventions**
- **109 unique exact-GPS sites**
- original 122-record source preserved unchanged.

Important matrix conclusions:
- intervention types represent different hydrological functions and should not be forced into one siting rule;
- Recharge Borewell and Pond Deepening show strong pond/waterbody-related evidence;
- Checkdam/Nala and New Checkdam show strong drainage-corridor evidence;
- RRWHS is primarily a settlement/roof/dry-well decision rather than a drainage-proximity decision;
- the 19 litholog-linked Recharge Borewell sites demonstrate that surface GIS classes do not directly determine site-specific subsurface conditions;
- both High and Moderate GWRPZ sites contain primary litholog intervals flagged `Y`;
- proximity to mapped lineaments is not a sufficient direct proxy for the litholog evidence;
- primary `Y` flags are retained as source observations and are not converted into quantified aquifer yield.

New supplement:
`/GW Recharge/07_Analysis/Clean_Reset_PreStep7_Matrices/GWRPZ_Pre_Step7_Decision_Matrices_v1.0.md`

Supporting matrix CSVs are stored in the same folder.

No Step 7 Story Lock, Master Plan, sanitized public data or frontend work has been started.

## Exact next step

**STEP 7 ONLY — LOCK THE STORY**, using the Step 6 v1.1 evidence register, the 120/109 cohort and this matrix supplement.

---

## Checkpoint G4 — Pre-Step-7 Five-Matrix Booklet

**Completed:** 23 September 2026

User selected **Option B**: consolidate all five priority matrices into one compact Matrix Booklet before Story Lock.

Created:
`/GW Recharge/07_Analysis/Clean_Reset_PreStep7_Matrices/GWRPZ_Pre_Step7_Matrix_Booklet_v1.0.md`

The booklet now covers:

1. **Hydrological Function × Intervention Type**
2. **Surface GIS × Subsurface Litholog Evidence**
3. **Site-Decision Evidence Role × Intervention Type**
4. **Surface Opportunity × Intervention Type**
5. **Research → Practice Learning**

New supporting files:
- `Matrix_E_Surface_Opportunity_by_Intervention_Type_v1.0.csv`
- `Matrix_F_Research_to_Practice_Learning_v1.0.csv`
- `Matrix_Booklet_Publication_Priority_v1.0.csv`

Booklet decisions:
- Matrix 5 (Research → Practice Learning), Matrix 4 (Surface Opportunity × Intervention Type), and Matrix 2 (Surface GIS × Litholog) are recommended as **Tier 1 main-story visuals**.
- Matrix 1 (Hydrological Function × Intervention Type) and Matrix 3 (Site-Decision Evidence Role × Intervention Type) are recommended as **Tier 2 explanatory/supporting visuals**.
- The detailed Step 4 structure-variable matrix remains an internal analytical/fact-checking source rather than a public full-table exhibit.
- Story Lock should evaluate a sequence of: research origin → GWRPZ → site opportunity → hydrological function → decision evidence → litholog/subsurface → monitoring feedback.

Controlling evidence baseline remains:
- **120 interventions / 109 unique exact-GPS sites**
- original 122-record source preserved unchanged
- 19 implemented Recharge Borewell sites with primary lithologs
- Step 6 Evidence Register v1.1 remains claim authority.

No Story Lock, Master Plan, sanitized public data, frontend design or prototype has been started.

## Exact next step

**STEP 7 ONLY — LOCK THE STORY**, using:
- Step 6 Evidence Register v1.1;
- 120/109 defensible publication cohort;
- Pre-Step-7 Matrix Booklet v1.0.

---

## Checkpoint H — Step 7 Story Lock draft

**Completed:** 23 September 2026  
**Status:** **AWAITING EXPLICIT USER APPROVAL**

Step 7 Story Lock created:
`/GW Recharge/08_Project_Admin/GWRPZ_Web_Article_Story_Lock_v1.0.md`

### Locked narrative proposition

The article is a technical professional-learning story, not a GIS tutorial, dashboard, donor report or intervention catalogue.

Core progression:

**Spatial hypothesis → field-tested decision support → direct subsurface evidence → monitoring feedback.**

### Proposed locked article order

1. Hero — From Mapping to Decision
2. Thesis/research origin
3. GWRPZ — build the spatial hypothesis
4. 120-intervention / 109-site implementation reality check
5. Surface opportunity + hydrological function + site-decision evidence
6. Construction as investigation — 19 lithologs
7. Hydrogeological cross-section / surface-to-subsurface interpretation
8. Monitoring as feedback, not causal verdict
9. Closing synthesis
10. Acknowledgements
11. Note on this article
12. Methods & Evidence
13. References / Source Notes
14. Author footer

### Acknowledgement / note lock

Acknowledgement section explicitly recognizes:
- Hindustan Unilever Foundation (HUF) for supporting the broader water-security programme and enabling evidence-based recharge practice;
- Samarpan Hanspara, Civil Engineer, Development Support Centre (DSC), for field implementation, construction, site-level engineering and coordination support;
- Development Support Centre (DSC) for the professional platform and field exposure.

Institution naming is permitted in the acknowledgement only; this does not unlock row-level partner attribution or public donor/partner data fields.

The article note is locked as:

“This article is shared as a knowledge and learning resource, drawing on professional experience, field observations and technical analysis. The views and interpretations presented are the author’s own and are intended to support learning, reflection and professional discussion rather than represent an official institutional position.”

### Visual hierarchy

Maps and analytical evidence dominate. Tier 1 visuals:
- research→practice evolution spine;
- final GWRPZ + 120 interventions;
- surface-opportunity typology;
- surface GIS × litholog evidence;
- hydrogeological cross-section;
- 2024/2025/2026 groundwater-class sequence.

Photos remain minimal and transformed/illustrative where useful.

### Evidence limits retained

- 120 / 109 remains the publication baseline; 122 source records preserved internally;
- two unresolved conflict records remain excluded;
- no GWRPZ pass/fail rule;
- no mandatory lineament-intersection claim;
- litholog `Y` remains a source flag, not yield;
- no intervention→groundwater causality claim;
- no confidential row-level project metrics;
- thesis Panam results remain historical evidence only.

### Gate

Do **not** proceed to Step 8 until the user explicitly approves the Story Lock.

Exact next action after approval:
**STEP 8 — Draft the clean end-to-end Master Plan.**

---

## Checkpoint H1 — Step 7A Humanized Story Lock v1.1

**Completed:** 23 September 2026  
**Status:** **AWAITING EXPLICIT USER APPROVAL**

Story Lock v1.0 was revised after reviewing the connected GitHub style references:
- `knightfox789/dsc-humanizer` (`SKILL.md`, Kaushal Voice and AI-pattern controls);
- `knightfox789/DSC_article01`;
- `knightfox789/GIS-Recharge-Web-Article-V2`;
- `knightfox789/weir-web-article`;
- the user’s portfolio Knowledge Hub conventions.

McKinsey’s 2024 “Year in Charts” was used only as a reference for visual-information discipline: one clear analytical message per figure, message-led titles, direct annotations, source visibility and restrained visual hierarchy.

New controlling file:
`/GW Recharge/08_Project_Admin/GWRPZ_Web_Article_Story_Lock_v1.1.md`

### Main changes

1. **DSC Humanizer / Kaushal Voice applied**
   - evidence-first;
   - field-grounded;
   - natural sentence rhythm;
   - technical terms and qualifiers preserved;
   - limitations written once where material;
   - first person allowed sparingly for professional learning only.

2. **Reader-facing “not this / not that” pattern removed**
   - negative guardrails moved to an internal evidence-control appendix;
   - public story now states what the evidence shows, what it means and what question follows.

3. **Humanized section titles**
   - Where the enquiry began
   - Reading the landscape as a spatial hypothesis
   - What the implemented sites taught us
   - Read the opportunity before choosing the intervention
   - When construction starts revealing the subsurface
   - Connecting the points below ground
   - Monitoring keeps the question open
   - What changed in the way recharge is planned

4. **Interactive visual system locked**
   - Question Evolution Spine
   - Progressive GWRPZ Layer Reveal
   - GWRPZ + Intervention Map
   - Surface Opportunity Selector
   - Decision Evidence Matrix
   - Linked Map + Litholog Explorer
   - Interactive Hydrogeological Cross-section
   - 2024/2025/2026 groundwater small multiples
   - closing Learning Loop.

5. **Acknowledgement and article note retained**
   - HUF;
   - Mr. Samarpan Hanspara, Civil Engineer, DSC;
   - DSC;
   - soft knowledge-and-learning note without organisation names.

6. **Visual direction**
   - long-form editorial, not dashboard;
   - maps/sections/infographics dominate;
   - existing GitHub scrollytelling/toggle/tab patterns carried forward selectively;
   - McKinsey-style information discipline used as a reference without copying visual identity.

### Gate

Do **not** proceed to Step 8 until v1.1 is explicitly approved.

Exact next action after approval:
**STEP 8 — Draft the clean end-to-end Master Plan.**

---

## Checkpoint I — Step 8 Clean Reset Master Plan v1.0

**Completed:** 23 September 2026  
**Status:** **STEP 8 DRAFT COMPLETE — AWAITING USER APPROVAL BEFORE STEP 9**

User explicitly approved Story Lock v1.1 and authorised Step 8.

Story Lock v1.1 status was updated to:
**APPROVED — NARRATIVE AND VISUAL-STORYTELLING AUTHORITY FOR STEP 8+**

New controlling implementation-plan draft:
`/GW Recharge/08_Project_Admin/GWRPZ_Interactive_Web_Article_Clean_Reset_Master_Plan_v1.0.md`

### Master Plan controls

The clean-reset implementation sequence is now:

- Phase P1 / Step 9 — public-data sanitisation and data contracts
- Phase P2 / Step 10A — real-data visual prototypes
- Phase P3 / Step 10B — editorial content package
- Phase P4 / Step 10C — production front end
- Phase P5 / Step 10D — integrated QA and release candidate
- Phase P6 / Step 10E–10F — publication, handover and maintenance

### GitHub architecture

Target repo remains:
`knightfox789/GWRPZ`

Recommended:
- `main` remains current deployable state;
- new `clean-reset-v1` development branch;
- Astro static source under `src/`;
- browser-safe public derivatives under `public/data/`;
- generated production output under `docs/`;
- MapLibre for maps;
- SVG/CSS/browser-native JS for most explanatory visuals;
- GitHub Actions for data/privacy/build QA and Pages deployment.

### Mandatory audits before release

1. Source authority
2. Claim authority
3. Public-data privacy
4. GIS integrity
5. Visual interpretation
6. Humanizer/editorial
7. Accessibility/responsive
8. Release integrity

### Data controls

Step 9 will be allowlist-based. Confidential project data must never be copied into the public repository and then hidden in the UI.

Public data must pass:
- 120 intervention / 109 site invariants;
- excluded-record check;
- forbidden-field scan;
- raw lat/lon attribute exclusion;
- source lineage / manifest / hash checks.

### Exact next step

Do not begin Step 9 until the user approves the Master Plan.

After approval:
**STEP 9 — Build the sanitized public web-data package and data contracts.**

---

## Checkpoint J — Step 9 Sanitized Public Web Data

**Completed:** 23 September 2026  
**Status:** **STEP 9 COMPLETE — GATE P1 PASS**

The user approved the Clean Reset Master Plan v1.0 and authorised Step 9.

Step 9 generated a new allowlist-based public-data package from the controlling 120-intervention / 109-site publication cohort.

### Key outputs

Library target:
`/GW Recharge/05_Web_Data/Clean_Reset_v1/`

Core governance:
- `Public_Data_Schema_v1.0.md`
- `Public_Data_Contracts_v1.0.md`
- `Public_Data_Field_Allowlist_Denylist_v1.0.md`
- `Public_Data_Manifest_v1.0.json`
- `Public_Data_QA_v1.0.md`
- `public_payload_hashes_v1.0.csv`

Public data:
- 120 intervention GeoJSON with anonymous public IDs;
- 109 unique-site GeoJSON;
- re-sanitised aquifer, drainage, lineament and LULC browser layers;
- GWRPZ + five factor score PNGs with revised non-traffic-light presentation palette;
- recovered June 2024 / 2025 / 2026 groundwater class PNGs;
- groundwater site summary joined only by public site ID;
- 19 public litholog profiles with source shaft/village identities removed;
- public A–AA conceptual cross-section data;
- story metrics, intervention-type summary, surface-opportunity summary and decision-evidence matrix.

### QA passed

- 120 / 109 invariant;
- 52 High / 68 Moderate / 0 Low;
- 10 multi-intervention sites / 21 records;
- 19 litholog-linked Recharge Borewell sites;
- 2024→2025 = 45 shallower / 61 same / 3 deeper;
- 2025→2026 = 14 / 81 / 14;
- 2024→2026 = 46 / 56 / 7;
- no prohibited public fields;
- no numeric lat/lon public properties;
- old 58-intervention web points excluded;
- source `Y` retained as a flag only;
- monitoring kept descriptive rather than causal.

### Project control

Story Lock v1.1 remains the narrative authority.
Master Plan v1.0 is now approved and updated through Step 9 completion.

### Exact next step

**STEP 10A — build V01–V09 real-data visual prototypes from the sanitized Step 9 package.**

Do not start production frontend implementation before the visual/data prototype gate is reviewed.

---

## Checkpoint K — Step 10A V01–V03 Prototype Set

**Completed:** 23 September 2026  
**Status:** **STEP 10A IN PROGRESS — V01–V03 COMPLETE; GATE P2 OPEN**

Built the first real-data prototype tranche from the Step 9 sanitized public package.

### Completed visuals

1. **V01 Question Evolution Spine**
   - six-stage technical learning sequence;
   - click + scroll-linked active question;
   - static fallback prepared.

2. **V02 Progressive GWRPZ Layer Reveal**
   - Aquifer 30%, Slope 20%, Drainage Density 20%, Lineament Density 15%, LULC 15% and supplied final GWRPZ;
   - real Step 9 categorical rasters;
   - compact factor switching;
   - static six-panel fallback.

3. **V03 GWRPZ + Implemented Interventions**
   - supplied final GWRPZ background;
   - all 120 sanitized interventions;
   - intervention type / FY / New-Renovation filters;
   - 68 Moderate / 52 High annotation;
   - static fallback prepared.

### Package

Target Library folder:
`/GW Recharge/06_Web_Article/Clean_Reset_v1/visual_specs/V01_V03_v0.1/`

### QA

- real sanitized Step 9 data used;
- V03 payload count = 120;
- 68 Moderate / 52 High / 0 Low confirmed;
- no reader-facing coordinates;
- JavaScript syntax check passed;
- reduced-motion and mobile stacking rules included;
- current runtime blocks graphical `file://` browser navigation, so static fallbacks are used for immediate visual review.

### Exact next step

Continue Step 10A with:
**V04 Surface Opportunity Selector + V05 Decision Evidence Matrix + V06 Litholog Explorer.**

Do not start production frontend work while Gate P2 remains open.

---

## Checkpoint L — Step 10A V04–V06 Prototype Set

**Completed:** 23 September 2026  
**Status:** **STEP 10A IN PROGRESS — V01–V06 COMPLETE; GATE P2 OPEN**

Second real-data visual tranche completed from the Step 9 sanitized public package.

### V04 — Surface Opportunity Selector
- four opportunity families:
  - Pond-linked direct recharge
  - Existing-storage enhancement
  - Drainage-corridor intervention
  - Roof-to-well recharge
- five intervention selections;
- mapped spatial signature + hydrological function + required field evidence shown together.

### V05 — Decision Evidence Matrix
- 12 evidence types;
- 5 principal intervention types;
- Core / Supporting / Context / Feedback / Not controlling;
- role categories explicitly remain non-numeric decision classifications.

### V06 — Litholog Explorer
- 19 anonymous public litholog profiles;
- site-location selector;
- vertical interval rendering;
- selected mapped surface context;
- source `Y` intervals retained only as source flags;
- no source shaft or village identities in the public prototype.

### QA
- V04 controlling counts reproduced;
- V05 dimensions = 12 × 5;
- V06 = 19 profiles;
- 16/19 profiles contain at least one source `Y` interval;
- JavaScript syntax: PASS;
- mobile/reduced-motion behaviour included;
- static fallbacks manually inspected and layout overlaps corrected.

### Library target
`/GW Recharge/06_Web_Article/Clean_Reset_v1/visual_specs/V04_V06_v0.1/`

### Exact next step
Continue Step 10A with:
**V07 Hydrogeological Cross-section + V08 Groundwater 2024–2026 + V09 Learning Loop.**

Do not start the production frontend while Gate P2 remains open.

---

## Checkpoint M — Step 10A Complete / Gate P2 Pass

**Completed:** 24 September 2026  
**Status:** **V01–V09 COMPLETE — GATE P2 PASS WITH PRODUCTION NOTES**

### Final tranche
V07 Hydrogeological Cross-section, V08 Groundwater 2024–2026 and V09 Learning Loop were completed from the Step 9 sanitized package and approved Story Lock synthesis.

### Full visual-system review
The nine visual prototypes were reviewed together using their static fallbacks and prototype specifications.

Overall sequence:
**question → spatial hypothesis → implemented reality → site opportunity → decision evidence → litholog → conceptual section → monitoring feedback → learning loop**

### Gate P2
**PASS WITH PRODUCTION NOTES**

No evidence/privacy blocker remains at prototype level.

Important production notes:
- V04 is the signature bridge from map to field decision.
- V05 should open in simplified single-intervention mode.
- V03 must retain compact controls.
- V06 should add a compact lithology legend / small-multiple teaser.
- V07 stays conceptual; do not draw continuous units or groundwater-flow direction without additional evidence.
- V08 remains class-based monitoring feedback.
- V09 remains synthesis only.

### New review artifacts
- full V01–V09 contact sheet;
- full visual-system review;
- final Visual Prototype Register v1.0.

### Exact next step
**STEP 10B — Editorial Content Package**

Required Step 10B outputs:
- complete article draft;
- claim traceability register;
- figure-caption register;
- reference/source-note register;
- Humanizer pass;
- factual/claim audit.

Frontend production remains Step 10C.

---

## Checkpoint N — Step 10B Editorial Content Package

**Completed:** 24 September 2026  
**Status:** **STEP 10B COMPLETE — GATE P3 PASS WITH NORMAL USER EDITORIAL REVIEW**

### Completed outputs
- complete reader-facing article draft;
- 29-row claim traceability register;
- V01–V09 figure-caption register;
- reference/source-note register;
- Humanizer pass;
- factual/claim audit.

### Editorial character
- DSC Humanizer / Kaushal Voice;
- evidence-first and field-grounded;
- professional-learning first person used sparingly;
- article prose avoids repeated “not this / but that” framing;
- technical limitations stated once where they alter interpretation.

### Evidence controls
- 120 interventions / 109 sites;
- 52 High / 68 Moderate;
- intervention-specific spatial evidence preserved;
- 19 lithologs;
- A–AA six-log reconciliation;
- groundwater transitions remain class-based feedback;
- no causal attribution;
- private row-level project attributes remain excluded.

### Exact next step
After user review/approval:
**STEP 10C — Production Front End**

Use the Step 10B article/content registers and the Step 10A approved visual system as production authorities.

---

## Checkpoint O — Step 10C Production Front End / Gate P4 Pass

**Completed:** 24 September 2026  
**Status:** **STEP 10C COMPLETE — GATE P4 PASS**

### Production beta
A self-contained static web article was generated from the approved Step 10B content and Step 9 sanitized data.

The beta implements V01–V09, complete article sections, methods, references, acknowledgement, article note and author footer.

### Architecture
For the gated beta, dependency-free HTML/CSS/browser-native JavaScript/SVG is used instead of the recommended Astro/MapLibre stack. The change improves reproducibility in the current build environment and does not change Story Lock, data contracts or public evidence.

Maintainable inputs remain separate from generated output:
- `src/content/article/`
- `public/data/`
- `scripts/build_frontend.py`
- `docs/preview-v1/index.html`

### Browser checks
Desktop 1440×1000 and mobile 390×844 smoke tests passed with:
- 9 visual modules;
- no console/page errors;
- no horizontal overflow;
- representative interactions passing;
- responsive and reduced-motion rules active.

### GitHub staging
- repository: `knightfox789/GWRPZ`
- branch: `clean-reset-v1`
- preview: `docs/preview-v1/index.html`
- Step 10C commits remain isolated from `main`
- `main` remains unchanged
- draft PR: `https://github.com/knightfox789/GWRPZ/pull/1`

### Library target
`/GW Recharge/06_Web_Article/Clean_Reset_v1/production/Step10C_v0.1/`