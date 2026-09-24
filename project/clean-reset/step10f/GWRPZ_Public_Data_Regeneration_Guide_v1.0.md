# GWRPZ Public-Data Regeneration Guide v1.0

**Purpose:** Safely rebuild browser/public data when the evidence changes.

## 1. Do not start from the website

The website is an output.  
Start from the authoritative source/evidence records and the clean-reset Step 9 data contracts.

Controlling records:
- `GWRPZ_Authoritative_Source_and_Decision_Register_v1.4.md`
- `GWRPZ_Authoritative_Spatial_and_Professional_Evidence_Register_v1.1.md`
- `GWRPZ_Web_Article_Story_Lock_v1.1.md`
- `/GW Recharge/05_Web_Data/Clean_Reset_v1/`

## 2. Current analytical baseline

The clean-reset publication baseline is:
- **120 interventions**
- **109 unique sites**
- **52 High / 68 Moderate GWRPZ**
- **19 primary litholog profiles**
- **6 reconciled A–AA logs**
- groundwater class rasters for **June 2024 / June 2025 / June 2026**

Do not silently change these values.  
If a corrected source changes them, update the source register and claim register first.

## 3. Intervention regeneration

Source workflow:
1. recover the source intervention inventory;
2. apply the approved conflict/exclusion decisions;
3. preserve legitimate same-location multi-intervention records;
4. recompute the 120-intervention / 109-site invariants;
5. attach only approved analytical attributes;
6. remove all private fields before any GitHub/public export.

Required checks:
- expected intervention count;
- expected unique-site count;
- GWRPZ class total;
- intervention-type total;
- multi-intervention-site logic;
- geometry validity;
- point/raster alignment.

## 4. GIS regeneration

### Final GWRPZ
The supplied final GWRPZ class raster remains authoritative unless a formally approved new model replaces it.

### Aquifer / slope / LULC
Retain the actual mapped classes/ranges used in the publication.

### Drainage / lineament
Retain the accepted reconstructed class logic and source linework.  
Density surfaces and line overlays should remain distinguishable.

### Browser cartography
- use a common spatial extent;
- preserve aspect ratio/georeferencing;
- never position points by visual/manual offsets;
- after conversion, sample the class at known intervention positions as a QA check.

## 5. Groundwater monitoring regeneration

For a future monitoring year:
1. obtain the authoritative groundwater-depth class raster;
2. confirm the class semantics match the publication;
3. confirm CRS/grid/extent/cell size;
4. sample at the same 109 public monitoring/intervention locations where valid;
5. calculate class movement against the prior reference year;
6. report counts as class movement, not exact-metre movement;
7. update V08 and the article text together.

If grid/classes differ, stop and reconcile before comparison.

## 6. Litholog regeneration

For new primary logs:
1. validate the original interval table;
2. create a public litholog ID;
3. retain depth intervals and lithology names;
4. remove village/shaft/source identity;
5. link to an approved public site;
6. update the litholog explorer;
7. update any conceptual section only after explicit section reconciliation.

## 7. Public field policy

Public fields should be necessary for a reader-facing question.

Allowed examples:
- public anonymous ID;
- intervention type;
- GWRPZ class;
- approved FY / New-Renovation fields where intentionally used;
- approved analytical distance/class summaries;
- approved geometry.

Do not export:
- village/block/district/source identity;
- internal IDs;
- raw latitude/longitude columns;
- finance;
- beneficiaries;
- storage/coverage/wells-benefited;
- fund/SOP/private partner fields;
- internal QA flags that do not serve the reader.

## 8. Manifest and QA

Every regenerated public-data package should include:
- schema/data dictionary;
- source lineage;
- counts/invariants;
- privacy audit;
- file byte size;
- SHA-256 hash;
- generation date/version.

Minimum acceptance:
- no prohibited fields;
- no private identifiers;
- all expected joins resolve;
- current analytical totals reproduce;
- browser assets load;
- desktop/mobile visual smoke test passes.

## 9. Versioning

- copy/style only: patch release `v1.0.x`
- refreshed public data with same method/story: minor release `v1.x.0`
- changed method/story/evidence architecture: major release `v2.0.0`

## 10. Storage

Persistent evidence/data:
`/GW Recharge/`

Public-data package:
`/GW Recharge/05_Web_Data/Clean_Reset_v1/`

Release/handover packages:
`/GW Recharge/06_Web_Article/Clean_Reset_v1/releases/`

GitHub contains deployable/public material and project documentation; the Library remains the long-term evidence/recovery store.