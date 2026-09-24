# GWRPZ Interactive Web Article — Clean Reset Master Plan v1.0

**Project:** From Mapping to Decision  
**Date:** 23 September 2026  
**Clean-reset step:** Step 8 — End-to-end Master Plan  
**Status:** **APPROVED CONTROLLING MASTER PLAN — STEP 10E COMPLETE; PUBLICATION DEPLOYED; STEP 10F NEXT**  
**Primary owner:** Kaushal Gadariya — Soil and Water Conservation Engineer  
**Repository:** `knightfox789/GWRPZ`  
**Deployment target:** GitHub Pages  
**Library root:** `/GW Recharge/`  
**Narrative authority:** `GWRPZ_Web_Article_Story_Lock_v1.1.md` — approved 23 September 2026  
**Claim authority:** `GWRPZ_Authoritative_Spatial_and_Professional_Evidence_Register_v1.1.md`  
**Source / confidentiality authority:** `GWRPZ_Authoritative_Source_and_Decision_Register_v1.4.md`  
**Analytical baseline:** **120 defensible interventions / 109 unique exact-GPS sites**  
**Subsurface subset:** **19 implemented Recharge Borewell sites with primary lithologs**

---

# 1. Purpose

This document is the **new controlling end-to-end implementation plan** for the clean-reset GWRPZ web article.

It supersedes the earlier `GWRPZ_Interactive_Web_Article_Master_Plan_v0.28.md` for future production decisions. The v0.28 plan, Phase 4 deployment package and earlier Phase 5 prototypes remain valuable archive/reference material, but they no longer control the narrative, public-data schema, information architecture or production sequence.

The project is now governed by four layers:

1. **Source authority** — what the original data and documents are.
2. **Claim authority** — what may be said publicly.
3. **Story authority** — where and how approved evidence enters the article.
4. **Implementation authority** — this Master Plan: how the approved story becomes a tested, public web product.

The governing principle is:

> **Story is locked. Data are sanitised to serve the story. Visuals are built to answer the story’s analytical questions. Code implements those visuals. QA verifies the evidence, privacy and reader experience before release.**

---

# 2. Product definition

## 2.1 Final product

A static, interactive, mobile-responsive long-form web article:

# **From Mapping to Decision**

**Subtitle:**  
*How spatial evidence, field judgement, construction learning and groundwater monitoring shaped an applied recharge-planning approach.*

The product is an interactive technical evidence story grounded in Sabarkantha and in the author’s professional learning over time.

## 2.2 Final reader experience

The reader moves through:

**research question → spatial hypothesis → implemented evidence → site opportunity → intervention decision → subsurface evidence → hydrogeological interpretation → monitoring feedback → professional synthesis**

The article should feel closer to an interactive research atlas / evidence essay than a conventional project webpage.

## 2.3 Locked reader-facing section order

1. Hero — **From Mapping to Decision**
2. **Where the enquiry began**
3. **Reading the landscape as a spatial hypothesis**
4. **What the implemented sites taught us**
5. **Read the opportunity before choosing the intervention**
6. **When construction starts revealing the subsurface**
7. **Connecting the points below ground**
8. **Monitoring keeps the question open**
9. **What changed in the way recharge is planned**
10. Compact closing visual — **Map → Verify → Understand → Monitor**
11. **Acknowledgements**
12. **Note on this article**
13. **How the evidence was assembled**
14. **References and source notes**
15. **About the author**

This sequence may be refined only for layout or responsive behaviour. Reordering the analytical story requires a formal Story Lock revision.

---

# 3. Non-negotiable authorities

## 3.1 Story Lock

`/GW Recharge/08_Project_Admin/GWRPZ_Web_Article_Story_Lock_v1.1.md`

The Story Lock controls:
- article sequence;
- reader questions;
- PE claim families;
- visual role;
- Humanizer/Kaushal Voice;
- acknowledgement;
- article note;
- visual interaction grammar;
- public/private boundary;
- editorial exclusions.

## 3.2 Claim Register

`GWRPZ_Authoritative_Spatial_and_Professional_Evidence_Register_v1.1.md`

Every important public sentence, chart title, map annotation, tooltip and caption must trace to:
- an approved PE claim; or
- a Story Lock synthesis explicitly grounded in approved PE claims.

## 3.3 Source & Decision Register

`GWRPZ_Authoritative_Source_and_Decision_Register_v1.4.md`

Controls:
- source provenance;
- source hierarchy;
- methodology;
- confidentiality;
- original-vs-derived distinction;
- data governance;
- unresolved evidence.

## 3.4 Matrix Booklet

`/GW Recharge/07_Analysis/Clean_Reset_PreStep7_Matrices/GWRPZ_Pre_Step7_Matrix_Booklet_v1.0.md`

Controls the decision-oriented visual logic:
- hydrological function;
- surface opportunity;
- site-decision evidence role;
- surface GIS × subsurface evidence;
- research → practice learning.

---

# 4. Clean-reset step map

The clean-reset sequence remains:

| Step | Scope | Status |
|---|---|---|
| 1 | Freeze/archive old state | COMPLETE |
| 2 | Source & Decision Register | COMPLETE |
| 3 | Groundwater source recovery | COMPLETE |
| 4 | Full GIS analytical revisit | COMPLETE |
| 5 | Hydrogeology / monitoring / field evidence integration | COMPLETE |
| 6 | Authoritative Evidence Register | COMPLETE |
| 7 / 7A | Story Lock + Humanized / interactive visual refinement | **APPROVED** |
| 8 | Clean end-to-end Master Plan | **COMPLETE — APPROVED** |
| 9 | Sanitized public web data + data contracts | **COMPLETE — GATE P1 PASS** |
| 10A | Visual/data prototypes | **COMPLETE — GATE P2 PASS WITH PRODUCTION NOTES** |
| 10B | Editorial content package | **COMPLETE — GATE P3 PASS WITH NORMAL USER EDITORIAL REVIEW** |
| 10C | Front-end production build | **COMPLETE — GATE P4 PASS** |
| 10D | Integrated QA / browser / accessibility / performance | **NEXT STEP — NOT STARTED** |
| 10E | Release candidate + deployment | **COMPLETE — PUBLICATION DEPLOYED** |
| 10F | Handover / maintenance / update workflow | **NEXT STEP — NOT STARTED** |

No Step 9 production work begins until this Master Plan is approved.

---

# 5. Delivery phases and gates

The remaining work is organised into six implementation phases.

---

## Phase P1 — Public-data sanitisation and data contracts
**Maps to:** Step 9  
**Status:** **COMPLETE — GATE P1 PASS, 23 September 2026**

### Objective
Create the smallest public-safe analytical datasets required by the approved story.

### Tasks
- generate public intervention dataset from the 120-record defensible cohort;
- remove prohibited attributes before the data ever enter GitHub;
- retain geometry only where Story Lock permits;
- create stable public site/intervention identifiers that do not expose internal source IDs;
- generate aggregate summary JSON/CSV used by figures;
- create public litholog profiles from the 19 primary logs;
- generate browser-safe groundwater derivatives for 2024/2025/2026;
- create simplified web derivatives of required aquifer, drainage, LULC and GWRPZ layers;
- create cross-section-ready public data;
- document every public field;
- generate hashes and a manifest;
- run an automated privacy/forbidden-field audit.

### Required outputs
Library:
- `/GW Recharge/05_Web_Data/Clean_Reset_v1/Public_Data_Schema_v1.0.md`
- `/GW Recharge/05_Web_Data/Clean_Reset_v1/Public_Data_Manifest_v1.0.json`
- `/GW Recharge/05_Web_Data/Clean_Reset_v1/Public_Data_QA_v1.0.md`
- public-safe vector/raster/JSON derivatives

### Gate P1
Pass only when:
- 120 / 109 invariants reproduce correctly;
- excluded conflict records are absent;
- no prohibited fields appear;
- no raw lat/lon columns appear;
- geometry is explicitly approved;
- all public files have a source lineage;
- all public fields have a documented purpose.

---

## Phase P2 — Visual/data prototypes
**Maps to:** Step 10A  
**Status:** **COMPLETE — GATE P2 PASS WITH PRODUCTION NOTES**

### Objective
Prototype the nine locked analytical visuals using real sanitized data before writing the final page around them.

### Visuals
- V01 Question Evolution Spine
- V02 GWRPZ Layer Reveal
- V03 GWRPZ + Intervention Map
- V04 Surface Opportunity Selector
- V05 Decision Evidence Matrix
- V06 Litholog Explorer
- V07 Hydrogeological Cross-section
- V08 Groundwater 2024–2026
- V09 Learning Loop

### Prototype rule
Every visual must be tested first as an analytical communication object:

**Question → data → visual encoding → interaction → reader takeaway → limitation**

### Required outputs
- `Visual_Data_Contract_v1.0.md`
- `Visual_Prototype_Register_v1.0.md`
- one prototype specification per V01–V09
- approved representative screenshots / static fallbacks
- mobile fallback definitions

### Gate P2
Pass when every visual:
- answers a single Story Lock question;
- has a clear approved claim basis;
- uses public-safe data only;
- has a non-interactive fallback;
- has a mobile behaviour;
- has a concise source/method note.

---

## Phase P3 — Editorial content package
**Maps to:** Step 10B  
**Status:** **COMPLETE — GATE P3 PASS WITH NORMAL USER EDITORIAL REVIEW**

### Objective
Draft the complete article text around the approved visual sequence.

### Writing mode
**DSC Humanizer: Kaushal Voice + web-article, deep edit**

### Workflow
For each section:
1. identify reader question;
2. identify approved PE claims;
3. draft evidence-led prose;
4. link each key paragraph to its visual;
5. place limitation only where it materially changes interpretation;
6. run Humanizer pass;
7. run factual/claim audit.

### Required outputs
- `Article_Content_Draft_v0.1.md`
- `Article_Claim_Traceability_v1.0.csv`
- `Figure_Caption_Register_v1.0.csv`
- `Reference_Source_Note_Register_v1.0.md`

### Gate P3
Pass when:
- every substantive claim is traceable;
- no unsupported causal wording remains;
- repeated “not X / but Y” patterns have been removed from public prose;
- figures and body text use consistent numbers;
- acknowledgement and article note match the approved text;
- no institutional attribution exceeds approved scope.

---

## Phase P4 — Production front end
**Maps to:** Step 10C  
**Status:** **COMPLETE — GATE P4 PASS, 24 September 2026**

### Objective
Implement the approved story and visuals as a robust static web article.

### Recommended stack
- **Astro** for static generation and component structure;
- **MapLibre GL JS** for interactive mapping;
- browser-native `IntersectionObserver` for scroll states;
- SVG / CSS / lightweight JavaScript for explanatory diagrams;
- D3 only where a visual genuinely requires data-driven SVG logic;
- no runtime database;
- no user account;
- no proprietary GIS server;
- no external API required for the core article.

### Rationale
Astro gives:
- clean section/component architecture;
- static HTML output;
- strong SEO and metadata control;
- lazy loading;
- low JavaScript cost;
- easier responsive fallbacks;
- a maintainable path for future knowledge articles.

### Gate P4
Functional beta must:
- render all sections;
- load all public data;
- support all core interactions;
- retain readable fallback content without JavaScript;
- work on desktop and mobile;
- include methods/references/acknowledgement/footer.

---

## Phase P5 — Integrated QA and release candidate
**Maps to:** Step 10D  
**Status:** NOT STARTED

### Objective
Audit the complete product across evidence, privacy, GIS behaviour, editorial quality, browser rendering, accessibility and performance.

### Required outputs
- `GWRPZ_Web_Article_QA_Register_v1.0.md`
- `Claim_Audit_v1.0.csv`
- `Privacy_Sanitisation_Audit_v1.0.md`
- `GIS_Web_Alignment_QA_v1.0.md`
- `Accessibility_Performance_Audit_v1.0.md`
- release candidate package

### Gate P5
Release candidate approved only when all critical defects are closed.

---

## Phase P6 — Publication, handover and update workflow
**Maps to:** Step 10E–10F  
**Status:** **IN PROGRESS — STEP 10E COMPLETE; STEP 10F NEXT**

### Objective
Deploy a reproducible public release and preserve enough documentation to update it later.

### Required outputs
- live GitHub Pages URL;
- release tag;
- release manifest + hashes;
- final Master Plan status;
- final Recovery Log;
- maintenance/update guide;
- public-data regeneration guide.

### Gate P6
Release complete only after:
- production URL verified;
- desktop/mobile visual smoke test passed;
- deployed artifact hashes match approved release artifact;
- repository contains no confidential files;
- release tag and recovery checkpoint are recorded.

---

# 6. GitHub repository architecture

## 6.1 Existing repository state

The current repository already contains:
- `.github/workflows/pages.yml`
- `docs/` as the Pages deployment root
- earlier Phase 4 GIS data
- earlier `docs/prototype/`
- `project/` records

The earlier live material remains archive/reference until the clean-reset release is ready.

## 6.2 Branch strategy

Recommended:

- `main` — current deployable public state
- `clean-reset-v1` — active rebuild branch
- short feature branches only when a change is substantial enough to justify isolation

Do not replace the public root from early development commits.

### Preview strategy
At the first approved integrated prototype:
- publish under a temporary path such as `/preview-v1/`; or
- use a workflow artifact / branch preview if practical.

The current root remains intact until release-candidate approval.

## 6.3 Target source tree

```text
GWRPZ/
├── .github/
│   └── workflows/
│       ├── pages.yml
│       ├── qa.yml                 # lint/data/privacy/build checks
│       └── link-check.yml         # optional scheduled link check
│
├── src/
│   ├── components/
│   │   ├── article/
│   │   ├── maps/
│   │   ├── charts/
│   │   ├── litholog/
│   │   ├── cross-section/
│   │   └── ui/
│   ├── layouts/
│   ├── pages/
│   │   └── index.astro
│   ├── styles/
│   ├── scripts/
│   └── content/
│       ├── article/
│       ├── methods/
│       └── references/
│
├── public/
│   ├── data/
│   │   ├── interventions/
│   │   ├── gis/
│   │   ├── groundwater/
│   │   ├── litholog/
│   │   ├── cross-sections/
│   │   └── summaries/
│   ├── images/
│   │   ├── editorial/
│   │   └── brand/
│   ├── icons/
│   └── metadata/
│
├── scripts/
│   ├── validate-public-data.*
│   ├── audit-private-fields.*
│   ├── build-data-manifest.*
│   ├── verify-counts.*
│   └── release-hashes.*
│
├── tests/
│   ├── data/
│   ├── content/
│   ├── browser/
│   └── accessibility/
│
├── project/
│   ├── clean-reset/
│   │   ├── story-lock/
│   │   ├── data-contracts/
│   │   ├── visual-specs/
│   │   ├── qa/
│   │   └── releases/
│   └── archive/
│
├── astro.config.*
├── package.json
├── README.md
└── docs/                       # generated / deployed production output
```

## 6.4 Generated-vs-source rule

`src/`, `public/`, scripts and project specs are maintainable source.

`docs/` is generated deployment output.

The repository must never use `docs/` as the only copy of scientific/public data logic.

---

# 7. Public web-data architecture

## 7.1 Principle

Only data required for a locked visual or reader interaction enter the public repository.

The public dataset is **allowlist-based**, not “source dataset minus a few hidden fields”.

## 7.2 Proposed public files

Indicative package:

```text
public/data/
├── interventions/
│   ├── interventions_public.geojson
│   ├── intervention_sites_public.geojson
│   └── intervention_summary.json
├── gis/
│   ├── gwrpz_class_web.*
│   ├── aquifer_web.geojson
│   ├── drainage_web.geojson
│   ├── lulc_context_web.*
│   └── map_bounds.json
├── groundwater/
│   ├── june_2024_web.*
│   ├── june_2025_web.*
│   ├── june_2026_web.*
│   └── groundwater_site_summary.json
├── litholog/
│   ├── litholog_profiles_public.json
│   └── lithology_summary.json
├── cross-sections/
│   ├── section_manifest.json
│   └── section_*.json
└── summaries/
    ├── matrix_surface_opportunity.json
    ├── matrix_decision_evidence.json
    └── story_metrics.json
```

Exact formats are decided during Step 9 after measuring size and geometry complexity.

## 7.3 Public intervention fields — proposed allowlist

Possible:
- `public_intervention_id`
- `public_site_id`
- `intervention_type`
- `gwrpz_class`
- `financial_year`
- `new_renovation`
- selected public-safe spatial context required by Story Lock
- geometry

Not allowed:
- source row number;
- raw lat/lon attributes;
- confidential village/source reconciliation fields;
- costs;
- beneficiaries;
- storage;
- coverage;
- wells benefited;
- detailed fund source;
- SOP/internal project-management fields;
- private HUF/DSC-led flag;
- IDs of excluded conflict records.

The definitive allowlist is locked in `Public_Data_Schema_v1.0.md` during Step 9.

---

# 8. Visual architecture

The nine Story Lock visuals are production requirements.

| Visual | Primary implementation | Fallback |
|---|---|---|
| V01 Question Evolution Spine | scroll-linked sticky SVG/HTML | static vertical timeline |
| V02 GWRPZ Layer Reveal | MapLibre + story states | stacked/static layer explainer |
| V03 GWRPZ + Intervention Map | MapLibre + simple controls | annotated static map |
| V04 Surface Opportunity Selector | tabs + SVG/map excerpt | four-panel infographic |
| V05 Decision Evidence Matrix | accessible HTML/SVG heatmap | semantic table |
| V06 Litholog Explorer | map + SVG vertical profile | selected small multiples |
| V07 Hydrogeological Cross-section | responsive SVG + hover | labelled static section |
| V08 Groundwater 2024–26 | synchronized maps / year control | three static small multiples |
| V09 Learning Loop | SVG/CSS progressive reveal | static closing infographic |

## 8.1 Interaction restraint

Interaction is retained when it helps the reader compare, locate or reveal evidence.

Do not add interaction simply because a dataset supports filtering.

## 8.2 Mobile-first fallback

Every sticky or hover-based interaction requires:
- tap/keyboard equivalent;
- reduced-motion mode;
- readable linear mobile fallback;
- no critical evidence hidden behind hover.

---

# 9. Editorial production architecture

## 9.1 Content units

Each section should contain:
- reader question;
- 2–5 short narrative paragraphs;
- one primary visual;
- optional supporting visual;
- one insight line;
- a compact source/method note;
- natural transition.

## 9.2 Figure-title rule

Titles communicate the analytical finding.

Example pattern:
**Most implemented sites fall within 100 m of mapped drainage**

rather than:
**Drainage Distance Chart**

## 9.3 Claim traceability

Every public claim should be captured in a simple traceability register:

| content_id | section | draft sentence / figure claim | PE ID | status | source note | QA |
|---|---|---|---|---|---|---|

This register becomes the factual audit backbone.

---

# 10. Testing strategy

Testing runs throughout production, not only at the end.

## 10.1 Data invariants

Automated checks must verify at minimum:
- publication intervention count = 120;
- unique site count = 109;
- GWRPZ High = 52;
- GWRPZ Moderate = 68;
- GWRPZ Low = 0;
- litholog-linked implemented Recharge Borewell subset = 19;
- excluded conflict records = absent;
- multi-intervention sites are preserved;
- null/unmatched values remain null where required.

## 10.2 Privacy tests

Fail the build if public data contain forbidden field names or patterns such as:
- latitude / longitude attribute columns;
- cost;
- beneficiary;
- storage potential;
- wells benefited;
- fund source;
- SOP;
- internal row identifiers;
- private partner flags.

Also run a manual sample inspection of every public JSON/GeoJSON schema.

## 10.3 GIS tests

Verify:
- public features fall within expected study bounds;
- geometry count matches manifest;
- simplified geometry does not materially displace required spatial relationships;
- GWRPZ colours/classes match authoritative final classes;
- groundwater year rasters align visually and use identical class semantics;
- drainage and intervention overlays align;
- cross-section IDs map to the correct primary logs;
- no public map relies on the frozen old 58-record analysis.

## 10.4 Content tests

Verify:
- every numeric claim matches the traceability register;
- each sentence keeps its PE status/qualification;
- thesis results remain labelled as historical;
- lineament language remains structural/contextual;
- `Y` remains a source flag;
- monitoring remains feedback/context;
- no groundwater causal attribution is introduced;
- acknowledgement wording is preserved.

## 10.5 Interaction tests

For V01–V09:
- initial state correct;
- all controls reachable by keyboard;
- selected state announced appropriately;
- map controls work with mouse/touch;
- tabs do not reset unrelated scroll state unexpectedly;
- data fail states produce readable fallback text;
- Back/Forward navigation does not break page state where applicable.

## 10.6 Browser matrix

Minimum:
- Chrome / Chromium desktop;
- Edge desktop;
- Firefox desktop;
- Safari macOS if available;
- Chrome Android;
- Safari iOS if available.

Test widths:
- ~360 px;
- ~768 px;
- ~1280 px;
- ~1440+ px.

## 10.7 Accessibility

Target WCAG 2.2 AA principles where applicable:
- semantic headings;
- keyboard access;
- visible focus;
- sufficient contrast;
- alternative text;
- SVG title/description where meaningful;
- no critical hover-only content;
- reduced-motion support;
- labelled controls;
- meaningful tab order.

## 10.8 Performance

Performance principles:
- article text and hero load before heavy GIS;
- map libraries lazy-load near first map section;
- large data lazy-load by movement;
- raster derivatives are compressed appropriately;
- avoid shipping unused JavaScript;
- fonts should be system or web-safe unless a clear project need exists.

Indicative release targets:
- Lighthouse Accessibility ≥ 95 where environment permits;
- Lighthouse SEO ≥ 95;
- Lighthouse Best Practices ≥ 90;
- Lighthouse Performance target ≥ 85 on mobile simulation;
- CLS < 0.1 target;
- no single hidden GIS asset should block first content paint.

These are quality targets, not substitutes for human testing.

---

# 11. Audit framework

Eight audits are mandatory before release.

## Audit A — Source authority
Question: Is every derivative traceable to the correct authoritative source?

## Audit B — Claim authority
Question: Does every public claim preserve its PE status and qualification?

## Audit C — Public-data privacy
Question: Could a reader download anything that should remain internal?

## Audit D — GIS integrity
Question: Do web derivatives still represent the approved GIS evidence correctly?

## Audit E — Visual interpretation
Question: Could a visual imply a stronger causal or comparative claim than the data support?

## Audit F — Humanizer / editorial
Question: Does the writing sound like a practitioner, with evidence more visible than adjectives?

## Audit G — Accessibility / responsive
Question: Can the article be understood and operated across device, keyboard and reduced-motion contexts?

## Audit H — Release integrity
Question: Does the deployed artifact exactly match the approved release candidate?

Each audit receives:
- PASS;
- PASS WITH NOTE;
- FAIL / BLOCKER.

Release requires zero unresolved BLOCKER items.

---

# 12. GitHub CI / QA workflow

Recommended `qa.yml` on pull request / branch push:

1. install dependencies;
2. build Astro;
3. validate JSON / GeoJSON syntax;
4. run public-data schema tests;
5. run forbidden-field scan;
6. run invariant-count tests;
7. run link/reference validation;
8. run content lint for broken local paths;
9. run unit tests for transformation helpers;
10. optionally run Playwright smoke tests;
11. upload QA artifact.

`pages.yml` should deploy only from `main` after the release package is accepted.

---

# 13. SEO and metadata

The article should include:
- descriptive title;
- meta description;
- canonical URL;
- Open Graph title/description/image;
- article structured data where appropriate;
- author name and role;
- meaningful section anchors;
- social preview image;
- sitemap/robots compatibility through the wider portfolio if linked later.

SEO must not change claim wording or introduce unsupported keywords.

---

# 14. Brand and design system

## 14.1 Visual family
- deep navy;
- warm paper;
- water teal;
- aqua;
- earth ochre;
- slate.

## 14.2 Design principles
- restrained palette;
- large evidence visuals;
- minimal decorative cards;
- generous white space;
- clear typography;
- compact legends;
- message-led annotations;
- no traffic-light visual semantics unless scientifically required.

## 14.3 Photography
Maps, diagrams and analytical visuals dominate.

Field visuals are minimal:
- community consultation;
- recharge borewell / pond context;
- construction/drilling;
- groundwater monitoring.

Transformed/illustrated photographs must preserve the real documentary meaning of the source.

---

# 15. Repository migration and legacy handling

The current repository contains working Phase 4/5 material.

During clean-reset production:

1. preserve current state through Git history/tag before replacement;
2. develop on `clean-reset-v1`;
3. do not reuse old `docs/prototype/` as the production codebase;
4. reuse verified GIS assets only after the Step 9 privacy/data audit;
5. keep previous prototypes under repository history or archive records;
6. publish preview separately from the live root;
7. replace the live root only after Gate P5.

Recommended archival tag before replacement:
`legacy-pre-clean-reset-2026-09-23`

Recommended first clean-reset release tag:
`v1.0.0`

---

# 16. Library architecture for remaining work

Use the existing root; add only controlled clean-reset subfolders.

```text
/GW Recharge/
├── 03_GIS_Source/                  # preserved source authority
├── 04_GIS_QA/                      # source / spatial QA
├── 05_Web_Data/
│   └── Clean_Reset_v1/
│       ├── public/
│       ├── manifests/
│       └── qa/
├── 06_Web_Article/
│   └── Clean_Reset_v1/
│       ├── content/
│       ├── visual_specs/
│       ├── visual_assets/
│       ├── design/
│       ├── qa/
│       └── releases/
├── 07_Analysis/                    # accepted analytical evidence
├── 08_Project_Admin/               # registers, Story Lock, Master Plan
└── 09_Backup_Recovery/             # recovery log / restart controls
```

Raw authoritative GIS does not move into public-data folders.

---

# 17. Versioning

## Documents
- `v0.x` — active draft / review
- `v1.0` — approved controlling version
- `v1.1+` — controlled revision

## Public release
Use semantic release tags:
- `v1.0.0`
- `v1.0.1` content/bug correction
- `v1.1.0` new validated visual/data feature
- `v2.0.0` material narrative/data-model change

Avoid names such as `final`, `final-final` or `latest2`.

---

# 18. Change-control rules

Changes requiring a Story Lock revision:
- movement order;
- central interpretation;
- major new claim family;
- new causal assertion;
- new public acknowledgement/attribution;
- new visual that changes story meaning.

Changes that normally do not require Story Lock revision:
- copyediting;
- responsive layout;
- performance optimisation;
- accessible implementation;
- visual simplification preserving meaning;
- bug fixes;
- source-note formatting.

Changes requiring Source/Claim Register revision:
- newly recovered primary evidence;
- corrected intervention classification;
- new monitoring data;
- new verified hydrogeological measurement;
- change in confidentiality/attribution permission.

---

# 19. Risk register

| Risk | Current control |
|---|---|
| Old 58-record metrics accidentally reused | automated count tests + claim audit |
| Confidential attributes leak into GitHub | allowlist schema + forbidden-field build test |
| Raw coordinates exposed as attributes | schema rule + manual public-file inspection |
| GWRPZ reconstructed score mistaken for final map | authoritative raster rule |
| Lineament proximity overstated | PE-045 language + visual audit |
| 19 litholog subset over-generalised | method note + claim audit |
| `Y` interpreted as yield | locked caption language |
| Monitoring presented as intervention impact | causality audit |
| Existing old prototype drives layout | new source architecture + clean-reset branch |
| Too many controls create dashboard feel | interaction audit against Story Lock |
| Heavy GIS harms mobile experience | lazy loading + asset budget + mobile fallback |
| Humanizer removes technical nuance | fact/term preservation audit |
| Article becomes self-promotional | author-positioning lock + editorial audit |
| Acknowledgement implies co-authorship/endorsement | approved wording + article note |

---

# 20. Definition of done

The project is complete only when all of the following are true:

### Evidence
- every public claim is traceable;
- every figure has a source/method note;
- no causal overclaim is present.

### Data
- public package passes privacy audit;
- all key counts reproduce;
- all public files are manifested and hashed.

### Story
- Story Lock sequence is preserved;
- Humanizer/Kaushal Voice is applied;
- visuals carry the main analytical burden.

### UX
- V01–V09 work or have approved responsive fallbacks;
- desktop and mobile are readable;
- keyboard/reduced-motion experience is valid.

### Engineering
- clean build from repository succeeds;
- no critical console errors;
- deployment workflow succeeds;
- release artifact is reproducible.

### Governance
- Master Plan updated;
- Recovery Log updated;
- release tag created;
- maintenance guide saved.

---

# 21. Mandatory project-control routine