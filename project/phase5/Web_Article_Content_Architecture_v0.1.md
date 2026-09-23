# Web Article Content Architecture

**Version:** v0.1  
**Date:** 23 September 2026  
**Project:** From Mapping to Decision — Interactive Groundwater Recharge Planning  
**Phase:** Phase 5 — Content architecture and UX prototype  
**Status:** DRAFT COMPLETE — Gate 5 pending user approval  
**Primary experience:** Guided Story + Explore Map  
**Evidence basis:** Spatial Evidence Register v0.1 and validated Phase 2/3 outputs

---

## 1. Editorial objective

The article should answer one practical question:

> **How can GIS help move groundwater-recharge planning from a broad potential map to a more defensible location-specific decision?**

The article is not a generic GIS tutorial and should not present GWRPZ as a final siting answer.

The reader should leave with four ideas:

1. recharge potential is shaped by several landscape controls;
2. a weighted GWRPZ map is a screening layer, not a final engineering decision;
3. hydrological position and structural context add useful siting evidence;
4. field and hydrogeological verification remain necessary before final intervention selection.

---

## 2. Primary audiences

### Primary
- watershed / groundwater practitioners;
- civil and soil-water conservation engineers;
- programme teams and implementing NGOs;
- district / block technical staff;
- donors and reviewers who need to understand the planning logic.

### Secondary
- students;
- researchers;
- hydrogeologists;
- GIS practitioners;
- interested public users.

The article should remain understandable without prior GIS software experience, while preserving enough technical depth for practitioners to inspect assumptions.

---

## 3. Experience architecture

### A. Guided Story

Purpose: explain the reasoning sequence.

Desktop:
- narrative column: ~38–42%;
- sticky map / evidence panel: ~58–62%;
- map remains visible while story steps change its state.

Mobile:
- map/evidence panel: sticky, ~42–48vh;
- narrative cards flow below;
- controls collapse into compact buttons / bottom sheets;
- no horizontal scrolling.

### B. Explore Map

Purpose: let a technically interested reader interrogate the validated layers after understanding the story.

Core capabilities:
- pan / zoom;
- layer toggles;
- raster opacity;
- structure filters;
- feature popups;
- village search / selection;
- legend update;
- reset-to-study-area;
- link back to relevant story section / methodology note.

---

## 4. Final Phase 5 narrative sequence

The original 17-part concept is consolidated into **13 story chapters plus Explore Map and technical appendices**. This reduces repetition while preserving the complete conceptual sequence.

### Chapter 1 — Hero: From Mapping to Decision

**Question:** What is this article about?

**Core message:** GIS can help screen where recharge may be more promising, but a map is only one step in a siting decision.

**Evidence / visual:** study-area extent, villages, final GWRPZ lightly visible.

**Map state:** `S01_CONTEXT`
- villages ON;
- final GWRPZ ON at low opacity;
- interventions OFF;
- drainage OFF;
- lineaments OFF.

**Primary text direction:**  
“Groundwater recharge planning starts with the landscape. GIS can help narrow the search, compare spatial evidence and ask better site questions. It does not replace field verification.”

---

### Chapter 2 — Why location matters

**Question:** Why can the same type of recharge structure behave differently in different places?

**Core message:** terrain, aquifer conditions, land cover, drainage and structural setting change from place to place.

**Map state:** `S02_VARIABILITY`
- villages ON;
- drainage ON;
- interventions ON;
- final GWRPZ OFF;
- lineaments optional faint.

**Decision implication:** start with spatial screening before choosing a structure type.

**Guardrail:** do not claim existing structures underperformed unless independent performance evidence is introduced.

---

### Chapter 3 — Read the landscape first

**Question:** How should a practitioner begin reading the area?

**Core message:** use ridge-to-valley context and drainage position to understand where runoff is generated, conveyed and accumulated.

**Map state:** `S03_LANDSCAPE`
- villages ON;
- drainage ON, stream-order styling active;
- final GWRPZ OFF;
- structures OFF by default.

**Interaction:** hover/tap drainage line to see stream order; legend explains nearest-network use later.

---

### Chapter 4 — Five controls of recharge potential

**Question:** What evidence is combined in the GWRPZ model?

This chapter is a five-step nested sequence rather than five separate article chapters.

#### 4A Aquifer — `S04_AQUIFER`
- aquifer score raster ON;
- aquifer polygons optional outline;
- other factors OFF;
- weight callout: **30%**.

#### 4B Slope — `S04_SLOPE`
- slope score raster ON;
- weight: **20%**;
- method note: `<3% → 3`, `3–8% → 2`, `>8% → 1`.

#### 4C Drainage density — `S04_DD`
- drainage-density score raster ON;
- drainage network faint;
- weight: **20%**.

#### 4D Lineament density — `S04_LD`
- lineament-density score raster ON;
- lineament vectors optional;
- weight: **15%**.

#### 4E LULC — `S04_LULC`
- LULC score raster or LULC classes ON;
- weight: **15%**;
- River Bed and Waterbodies remain separate.

**Narrative rule:** each factor gets what it represents, how it enters the model, why it matters to screening, and one short limitation. No factor is presented as sufficient on its own.

---

### Chapter 5 — Building the weighted GWRPZ score

**Question:** How are the five factors combined?

**Core equation:**

`Aquifer 30% + Slope 20% + Drainage Density 20% + Lineament Density 15% + LULC 15%`

**Map state:** `S05_WEIGHTED_MODEL`
- factor mini-selector visible;
- final GWRPZ OFF initially;
- weighted-overlay explanation diagram beside map.

**Technical note:** the reconstructed weighted score is reproducible over the five-input common domain. The historical full 1/2/3 class-break rule is not fully recoverable.

**Do not show:** the Phase 2D candidate threshold as the historical/original ArcGIS rule.

---

### Chapter 6 — Read GWRPZ as potential, not permission

**Question:** What do Low / Moderate / High classes actually mean?

**Core message:** they represent relative recharge potential in the supplied final raster, not guaranteed recharge or universal suitability.

**Map state:** `S06_GWRPZ`
- supplied final GWRPZ raster ON at 100%;
- village boundaries ON;
- structures OFF;
- legend: Low / Moderate / High.

**Technical note:** final article classing uses the supplied `GWRPZ_Class.tif`.

**Limitations drawer:** lower historical Class 1/2 break is unresolved from the reconstructed five-input domain.

---

### Chapter 7 — Potential is not the same as siting

**Question:** Why is a high-potential pixel not automatically the right site?

**Core message:** siting needs hydrological position, structural context, intervention purpose and field verification.

**Map state:** `S07_POTENTIAL_NOT_SITING`
- final GWRPZ ON;
- drainage ON;
- interventions ON;
- lineaments OFF initially.

**Visual device:** four-part decision stack:
1. recharge potential;
2. hydrological position;
3. structural / geological context;
4. field + engineering verification.

---

### Chapter 8 — Add hydrological position

**Question:** Where do existing structures sit relative to the drainage network?

**Evidence:**
- Order 1: **34** structures;
- Order 2: **12**;
- Order 3: **6**;
- Order 4: **6**;
- Orders 1–2 together: **46/58 (79.3%)**;
- nearest-stream distance: **1.3–986.2 m**, median **41.7 m**.

**Map state:** `S08_STREAM_ORDER`
- drainage ON with order styling;
- interventions ON;
- final GWRPZ ON at ~40–50% opacity.

**Interpretation:** existing structures are predominantly associated with lower-order drainage positions under the reproducible nearest-network rule.

**Mandatory limitation:** no intervention point literally intersects the supplied drainage lines; stream order is assigned from the nearest mapped drainage feature.

---

### Chapter 9 — Add structural context carefully

**Question:** What can the supplied lineament data tell us?

**Evidence:**
- direct point-lineament intersections: **0/58**;
- nearest mapped lineament distance: **27.4–5,177.5 m**;
- median distance: **1,209.5 m**.

**Map state:** `S09_LINEAMENT`
- lineaments ON;
- interventions ON;
- final GWRPZ low opacity;
- lineament-density layer available as compare toggle.

**Core message:** nearest-lineament distance is reproducible; a scientifically defensible “present/absent” proximity threshold is not documented.

**Retire:** “19/58 structures intersect lineaments.”

---

### Chapter 10 — Interrogate the 58 existing structures

**Question:** What does the validated intervention dataset show?

**Evidence:**
- **58 structures across 49 villages**;
- Moderate GWRPZ: **26 (44.8%)**;
- High GWRPZ: **32 (55.2%)**;
- Low GWRPZ: **0**.

**Map state:** `S10_STRUCTURES`
- interventions prominent;
- final GWRPZ ON;
- villages ON;
- drainage optional.

**Interaction:** click/tap structure popup with publication-safe attributes:
- structure ID;
- structure type;
- village / block;
- final GWRPZ class;
- nearest stream order;
- nearest stream distance;
- nearest lineament distance;
- Siting Alignment Spatial Setting.

**Do not expose as a primary field:** historical binary lineament flag.

---

### Chapter 11 — Spatial setting, not performance

**Question:** How can the combined GWRPZ + stream-order evidence be summarized without claiming effectiveness?

**Evidence:**
- Upper-catchment recharge setting: **46 (79.3%)**;
- Storage-oriented moderate-potential setting: **5 (8.6%)**;
- Higher-order high-potential setting — review: **7 (12.1%)**.

**Map state:** `S11_ALIGNMENT`
- structures colored by `Siting Alignment Spatial Setting`;
- final GWRPZ low opacity;
- drainage ON.

**Core message:** these categories describe spatial setting. They are not a performance score, success/failure rating or final engineering recommendation.

---

### Chapter 12 — From spatial evidence to a planning decision

**Question:** What should a practitioner do with the map?

**Planning sequence:**
1. identify candidate recharge-potential areas;
2. read ridge-to-valley and drainage position;
3. review mapped structural context;
4. match site context to intervention purpose;
5. visit and verify;
6. confirm engineering feasibility and local constraints;
7. decide / revise.

**Map state:** `S12_DECISION`
- final GWRPZ;
- drainage;
- lineaments;
- selected structure / candidate point;
- decision checklist beside map.

**Narrative emphasis:** the value of GIS is in narrowing and structuring the decision—not declaring a final site remotely.

---

### Chapter 13 — Field verification before final siting

**Question:** What cannot be settled from these GIS layers alone?

**Checklist themes:**
- local geology / weathering / fracture condition;
- actual drainage / runoff behavior;
- land ownership and access;
- structure-specific engineering feasibility;
- downstream / upstream implications;
- existing infrastructure;
- field-observed constraints;
- community and O&M considerations where relevant.

**Map state:** `S13_FIELD_VERIFY`
- map fades back;
- checklist becomes primary visual;
- selected location remains for context.

**Closing line direction:** “Use the map to ask better field questions.”

---

### Explore Map

Separate mode after the guided story.

**Default map state:** final GWRPZ + villages + structures.

**User controls:**
- GWRPZ;
- aquifer;
- slope score;
- drainage-density score;
- lineament-density score;
- LULC;
- drainage order;
- lineaments;
- villages;
- interventions;
- raster opacity;
- structure filters;
- reset extent.

Explore Map should never silently change the evidence definitions established in the story.

---

### Technical appendices

1. **Methodology**
2. **Data sources and lineage**
3. **Classification and weighting**
4. **Reconstruction / uncertainty notes**
5. **Structure QA**
6. **Replication considerations**
7. **Acknowledgements / disclaimer**

These should be accessible from the main story but should not interrupt the core narrative.

---

## 5. Evidence-to-section matrix

| Evidence | Story use | Headline? | Limitation required? |
|---|---|---:|---:|
| 58 structures / 49 villages | Ch. 10 | Yes | Yes — not district census |
| 26 Moderate / 32 High / 0 Low | Ch. 10 | Yes | Yes — potential, not effectiveness |
| 46/58 near Order 1–2 | Ch. 8 | Yes | Yes — nearest-network rule |
| nearest stream distance 1.3–986.2 m; median 41.7 m | Ch. 8 | Supporting | Yes |
| direct lineament intersections 0/58 | Ch. 9 | Yes | Explain supplied geometry |
| lineament distance 27.4–5177.5 m; median 1209.5 m | Ch. 9 | Supporting | Yes — no proximity threshold |
| 46 / 5 / 7 siting settings | Ch. 11 | Yes | Yes — not performance |
| Phase 2D 2/3 threshold candidate | Method appendix only | No | Strong |
| full historical class break unresolved | Ch. 6 + method appendix | Supporting | Yes |

---

## 6. Technical-detail placement

### In the main story
Keep only:
- decisions the reader needs to follow;
- key weights;
- key evidence counts;
- essential caveats that change interpretation.

### Inline “Method note” accordion
Use for:
- slope thresholds;
- DD / LD score thresholds;
- nearest-network rule;
- GWRPZ reference raster;
- lineament-distance method.

### “Evidence note” drawer
Use for:
- stored-vs-recalculated discrepancies;
- class-break reconstruction;
- coverage limitations;
- source lineage.

### Full Methodology appendix
Keep:
- CRS / grid;
- LULC geometry repair;
- common-grid reconstruction;
- Phase 2B scoring rules;
- weighted-overlay calculation;
- Phase 2D uncertainty;
- structure QA.

The main story should never require the reader to understand raster grid alignment before understanding the planning logic.

---

## 7. Writing rules for the article

Preferred:
- “associated with”;
- “located in”;
- “nearest mapped stream”;
- “nearest mapped lineament”;
- “consistent with”;
- “spatial setting”;
- “recharge potential”;
- “screening”;
- “decision support”.

Avoid unless independently supported:
- “proved”;
- “effective”;
- “successful”;
- “scientifically targeted”;
- “lineament intersection” for the historic 19/58 field;
- “performance category”;
- “optimal site”;
- “final suitability” from GWRPZ alone.

---

## 8. First evidence-led article outline

### Opening
Groundwater-recharge planning is not simply a question of where water can collect. The same intervention type can sit in very different aquifer, slope, land-use and drainage settings. GIS helps compare those conditions consistently across a landscape.

### Build the evidence
The Sabarkantha case combines five thematic factors: aquifer (30%), slope (20%), drainage density (20%), lineament density (15%) and LULC (15%). Each is scored on a 1–3 scale before weighted combination.

### Read the result correctly
The supplied final GWRPZ raster classifies relative recharge potential. It is a screening map, not a final siting map. The reconstructed weighted model supports the overall method, but the full historical Class 1/2/3 break rule could not be recovered exactly and should not be presented as an original ArcGIS setting.

### Add hydrological context
Among the 58 mapped structures, 46 (79.3%) are associated with Order 1–2 drainage under a nearest-network rule. That pattern is useful for describing hydrological position, but it does not by itself prove original programme intent or effectiveness.

### Add structural context
The supplied intervention points do not directly intersect the supplied lineament geometries. The reproducible relationship is therefore nearest-lineament distance, ranging from 27.4 m to 5,177.5 m, with a median of 1,209.5 m. No proximity threshold should be invented.

### Interrogate existing structures
Direct sampling of the final GWRPZ raster places 26 structures in Moderate and 32 in High potential cells. None of the 58 structures fall in Low cells. This describes mapped potential at structure locations—not measured recharge performance.

### Translate maps into decisions
Combining GWRPZ class and nearest stream order produces a conservative spatial-setting summary: 46 upper-catchment recharge settings, 5 storage-oriented moderate-potential settings and 7 higher-order high-potential settings requiring review. These categories organize spatial context; they do not rate performance.

### Close with field verification
The final decision still belongs in the field. GIS can narrow the search area, make assumptions explicit and structure technical discussion. Engineering feasibility, local geology, drainage behavior and site constraints still need direct verification.

---

## 9. Phase 5 content decision

This architecture is ready for UX prototyping.

**Gate 5 is not yet passed.**  
Gate 5 requires user approval of:
- the narrative sequence;
- the Guided Story / Explore Map split;
- the map-state logic;
- the interaction patterns in `Interaction_Specification_v0.1.md`.

Phase 6 full build must not begin until that approval.