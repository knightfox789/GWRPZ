# Web Article Content Architecture

**Version:** v0.2  
**Date:** 23 September 2026  
**Project:** From Mapping to Decision — Interactive Groundwater Recharge Planning  
**Phase:** Phase 5 — Content architecture and UX prototype revision  
**Positioning:** Practitioner-focused interactive evidence story / guide, grounded in the Sabarkantha case  
**Status:** REVISED DRAFT COMPLETE — Gate 5 pending user approval  
**Writing mode:** Kaushal Voice — technical + research-quality + data-storytelling

---

## 1. Revised product positioning

This article is neither a conventional institutional case study nor a step-by-step GIS manual.

It should read as:

> **A practitioner-focused interactive evidence story and decision guide on how GIS, hydrogeological reasoning, field knowledge, engineering judgement and community-informed planning can work together for groundwater recharge — grounded in the Sabarkantha experience.**

The article should be useful to:
- groundwater / watershed practitioners;
- hydrogeologists;
- soil and water conservation engineers;
- academicians and researchers;
- students;
- CSR professionals and CSR donors;
- NGOs and implementation agencies;
- government / technical teams.

A secondary professional objective is to demonstrate applied expertise through the quality of the reasoning, evidence and field interpretation. The article should create confidence and curiosity without using promotional language or publishing every operational detail of the applied workflow.

### Professional-authority principle

**Demonstrate expertise; do not announce expertise.**

The reader should infer that the author understands:
- RS–GIS and spatial modelling;
- MCDA / weighted-overlay reasoning;
- hydrogeological context;
- ridge-to-valley and drainage interpretation;
- structure siting;
- field verification;
- engineering feasibility;
- community consultation and approval;
- implementation realities;
- monitoring, uncertainty and evidence quality.

---

## 2. The central intellectual message

The article must reject the simplistic equation:

> **GIS map = final recharge site**

Instead, the story should build toward:

> **Remote sensing & GIS + MCDA + hydrogeological reasoning + field observation + hydrological position + engineering judgement + community consultation = better-informed recharge planning**

Even this is a decision-support pathway, not a guarantee of recharge performance.

The short memorable line for the article is:

> **A map can narrow the search. The field completes the decision.**

---

## 3. What we reveal — and what we deliberately do not over-publish

The article must remain scientifically transparent enough for a reader to understand and critically assess the approach.

### Reveal in the main article
- the planning question;
- the five principal thematic factors;
- scoring direction;
- model weights;
- why each factor matters;
- the concept of weighted GIS-MCDA;
- final GWRPZ interpretation;
- hydrological position;
- lineament / structural context;
- validated structure evidence;
- the role of field verification;
- the role of community consultation and approval;
- major methodological limitations.

### Reveal in methodology / evidence notes
- key thresholds;
- source lineage;
- important QA decisions;
- reconstructed-vs-original distinction;
- nearest-network rules;
- validation caveats;
- selected reproducibility notes.

### Retain as deeper professional working methodology
Unless needed for scientific interpretation, the article does not need to publish:
- every GIS processing step;
- complete scripts;
- all QA diagnostics;
- full internal decision matrices;
- detailed field-survey forms;
- every troubleshooting rule;
- all structure-level engineering checks;
- reusable client-ready templates;
- full analytical workflow automation.

**Boundary:** professional-method protection must never be used to hide a limitation that materially changes interpretation.

---

## 4. Story voice

Use the `dsc-humanizer` / **Kaushal Voice** discipline:

**Context → Field question → Spatial evidence → Interpretation → Limitation → Decision implication → Next field question**

The article should sound like a practitioner who has used maps in the field, not like:
- a marketing page;
- a textbook;
- an academic paper copied into a website;
- a software tutorial.

Prefer:
- evidence before adjectives;
- short field-oriented questions;
- practical decision implications;
- restrained claims;
- clear acknowledgement of uncertainty.

---

## 5. Revised experience architecture

### A. Guided Evidence Story

Purpose:
- build curiosity;
- explain the reasoning;
- show Sabarkantha evidence progressively;
- connect map evidence to field and implementation choices.

Desktop:
- narrative/evidence rail: ~40%;
- sticky interactive spatial panel: ~60%.

Mobile:
- sticky / anchored map: ~42–46vh;
- concise narrative cards below;
- deeper evidence in drawers / bottom sheets.

### B. Explore the Evidence

Not just “Explore Map”.

Purpose:
- let technically interested readers interrogate the validated evidence after they understand the story.

Includes:
- layer controls;
- structure filters;
- feature popups;
- evidence notes;
- data lineage;
- “Why this matters in the field” prompts.

### C. Research & Method

A dedicated layer for academics, students and technical reviewers.

Purpose:
- show intellectual lineage;
- explain the MCDA / GIS logic;
- disclose important methodological choices and uncertainties;
- provide selected research references.

### D. Work / Collaborate

A restrained closing section.

Purpose:
- make it possible for readers to approach the author for:
  - applied GIS studies;
  - groundwater recharge planning;
  - RS/GIS–MCDA analysis;
  - field-linked hydrogeological / NRM studies;
  - research collaboration;
  - decision-support tools / analytical work.

This should be professional, not promotional.

---

# 6. Revised story sequence

The narrative is reduced to **10 core chapters**, followed by **Explore the Evidence**, **Research & Method**, and **Author / Collaboration**.

---

## Chapter 1 — A recharge map is not yet a recharge decision

### Story purpose
Open with the practical tension, not the methodology.

### Opening idea
Two locations can appear close on a map and still differ in aquifer conditions, slope, runoff behaviour, land cover, structural controls and constructability.

### Main message
GIS can help narrow the search and make spatial evidence explicit. It cannot replace field judgement.

### Sabarkantha role
Introduce the case geography visually.

### Map state
- villages;
- drainage;
- final GWRPZ at low opacity;
- structures not yet dominant.

### Suggested headline
**A recharge map is not yet a recharge decision**

### Suggested standfirst
*The real question is not only where recharge potential appears high. It is whether the landscape, drainage, subsurface conditions, structure purpose and field reality support the same decision.*

---

## Chapter 2 — The Sabarkantha field question

### Story purpose
Make Sabarkantha the main evidence spine early.

### Show
- landscape / village context;
- mapped interventions;
- **58 validated structures across 49 villages**;
- structures were implemented on the ground through project processes that included community consultation and approval.

### Narrative direction
The case is not presented as “GIS selected 58 sites and therefore succeeded”.

Instead:

> Existing structures provide a real set of locations against which the spatial planning logic can be interrogated.

### Community / implementation lens
Show that technical siting is embedded in:
- field reconnaissance;
- community priorities / local knowledge;
- consultation;
- approval;
- land / access considerations;
- engineering feasibility;
- construction.

### Outcome language
Positive field results/outcomes can be included later only according to evidence class:
- measured;
- monitored;
- field-observed;
- community-reported.

Do not convert reported/observed outcomes into quantified impact without supporting records.

---

## Chapter 3 — Reading the landscape before choosing the structure

### Story purpose
Bring field knowledge before MCDA.

### Central idea
A practitioner first reads the landscape:
- ridge to valley;
- runoff pathways;
- drainage hierarchy;
- slope;
- exposed geology / weathering clues;
- land use;
- existing water bodies / structures;
- local observations.

### Map
Drainage order + villages + selected landscape context.

### Practitioner insight
**The map becomes more useful when the field questions are already good.**

This chapter is an important professional-authority signal.

---

## Chapter 4 — Turning field questions into spatial evidence

### Story purpose
Introduce the five thematic controls as evidence layers rather than software layers.

### Five evidence lenses
1. **Aquifer — 30%**
2. **Slope — 20%**
3. **Drainage Density — 20%**
4. **Lineament Density — 15%**
5. **LULC — 15%**

### Story device
Each layer answers a practical field question:

**Aquifer**  
*What kind of subsurface storage / transmission setting are we dealing with?*

**Slope**  
*Will water tend to slow and infiltrate, or move rapidly downslope?*

**Drainage density**  
*How dissected is the surface drainage system, and what does that imply for runoff / infiltration?*

**Lineament density**  
*Where does mapped structural complexity suggest possible fracture influence?*

**LULC**  
*How does the surface condition affect runoff, infiltration and practical intervention context?*

### Interaction
Progressive factor switching with one short “field meaning” card per factor.

---

## Chapter 5 — MCDA helps structure judgement; it does not remove judgement

### Story purpose
Explain the model in an intellectually credible but non-tutorial manner.

### Show
Weighted model:

`0.30 Aquifer + 0.20 Slope + 0.20 Drainage Density + 0.15 Lineament Density + 0.15 LULC`

### Main message
GIS-MCDA makes assumptions visible:
- which factors matter;
- how they are scored;
- how much weight they receive;
- how they combine spatially.

It does not make the assumptions universally correct.

### Research bridge
Link to:
- GIS-MCDA literature;
- MAR suitability-mapping reviews;
- India / South Asia recharge-potential studies.

### Curiosity strategy
Main article stops at the decision logic.

“See Method & Research” opens:
- scoring table;
- selected thresholds;
- evidence / QA notes;
- related papers.

Do not publish every internal processing / QA step in the main narrative.

---

## Chapter 6 — What the GWRPZ map can—and cannot—say

### Show
Supplied final GWRPZ raster.

### Explain
Low / Moderate / High = **relative recharge potential**, not:
- guaranteed recharge;
- performance;
- structure recommendation;
- construction approval.

### Key methodological honesty
The supplied final raster remains the class reference.

The full historical final 1/2/3 class-break rule could not be uniquely reconstructed from the preserved five-input workflow.

### Professional signal
A technically credible article is willing to say what is not recoverable.

---

## Chapter 7 — The interesting part begins after the potential map

This is the key narrative pivot.

### Central question
**Where do the structures actually sit in relation to hydrology and structural context?**

### Hydrological evidence
- Order 1: 34
- Order 2: 12
- Order 3: 6
- Order 4: 6
- Order 1–2: **46/58 (79.3%)**
- nearest mapped stream distance:
  - min **1.3 m**
  - median **41.7 m**
  - max **986.2 m**

### Interpretation
The observed structure set is predominantly associated with lower-order drainage under the reproducible nearest-network rule.

### Limitation
No structure point literally intersects the supplied drainage lines.

Use:
**“nearest mapped stream order”**

Not:
**“the structure lies on Order X stream”**

---

## Chapter 8 — Structural context needs more caution than a yes/no lineament flag

### Evidence
- direct point-lineament intersections: **0/58**
- nearest lineament:
  - min **27.4 m**
  - median **1,209.5 m**
  - max **5,177.5 m**

### Main message
Mapped lineaments can be useful structural evidence, but distance alone does not prove:
- active fracture connectivity;
- transmissivity;
- recharge pathway;
- structure performance.

### Retired claim
Do not use:
“19/58 structures intersect lineaments”.

### Strong professional signal
Show why a hydrogeological interpretation needs more than a GIS overlay.

---

## Chapter 9 — What the 58 structures reveal

### GWRPZ at structure points
- Moderate: **26 (44.8%)**
- High: **32 (55.2%)**
- Low: **0**

### Combined spatial setting
- Upper-catchment recharge setting: **46 (79.3%)**
- Storage-oriented moderate-potential setting: **5 (8.6%)**
- Higher-order high-potential setting — review: **7 (12.1%)**

### Main message
The categories describe **spatial context**, not measured performance.

### Ground implementation thread
Add a short field strip:
**Map → site discussion → community consultation / approval → engineering check → construction → observation / monitoring**

This is where available field photographs and verified implementation records can add significant credibility.

---

## Chapter 10 — From mapped evidence to a field decision

### The decision pathway

**1. Screen**
Identify candidate recharge-potential areas.

**2. Read**
Understand ridge-to-valley context and drainage position.

**3. Interpret**
Review hydrogeological / structural evidence.

**4. Match**
Relate site conditions to the intended recharge / storage function and structure type.

**5. Consult**
Bring in local knowledge, community priorities, access and approval.

**6. Verify**
Visit the site; check geology, runoff behaviour, existing structures, land and constructability.

**7. Engineer**
Confirm dimensions, safety, feasibility and downstream/upstream implications.

**8. Decide**
Select, revise or reject the candidate.

### Closing line
> **Use GIS to make the field visit smarter—not to eliminate the field visit.**

---
# 7. Outcomes / field evidence section

Add only when evidence is assembled.

Possible title:

## What happened after construction?

Evidence hierarchy:

### Level A — Measured
Examples:
- groundwater-level changes;
- storage / recharge estimation;
- command / irrigation effects;
- monitored structure performance.

### Level B — Systematically observed
Examples:
- water retention duration;
- visible recharge / availability changes;
- repeated site observations.

### Level C — Community-reported
Examples:
- farmer / village reports;
- local experience;
- user observations.

Label the evidence class explicitly.

Do not use “impact” unless the measurement and attribution justify it.

---

# 8. Research & Method section

This section should make the article academically useful without turning the story into a paper.

Subsections:
1. Why GIS-MCDA is used for spatial suitability questions
2. Selection of criteria
3. Scoring and weighting
4. Weighted overlay
5. GWRPZ interpretation
6. Hydrological-position method
7. Lineament / structural-context method
8. Field verification
9. Community / implementation pathway
10. Uncertainty and reproducibility
11. Related research

### Research-reading pattern

For each key paper show:
- citation;
- geography / context;
- method;
- why it is relevant to this article;
- what should *not* be directly transferred to Sabarkantha.

---

# 9. Selected research references for the first release

### GIS-MCDA foundations

**Malczewski, J. (2006).**  
*GIS-based multicriteria decision analysis: a survey of the literature.*  
International Journal of Geographical Information Science, 20(7), 703–726.  
DOI: `10.1080/13658810600661508`

**Use here:** conceptual foundation for GIS-MCDA as spatial decision support.

---

### MAR suitability mapping — methodology review

**Sallwey, J., Bonilla Valverde, J. P., Vásquez López, F., Junghanns, R., & Stefan, C. (2019).**  
*Suitability maps for managed aquifer recharge: a review of multi-criteria decision analysis studies.*  
Environmental Reviews, 27(2), 138–150.  
DOI: `10.1139/er-2018-0069`

**Use here:** supports the point that MAR suitability studies vary in criteria and weighting and should be applied with context and expertise.

---

### Suitability map + further hydrogeological modelling

**Rahman, M. A., Rusteberg, B., Gogu, R. C., Ferreira, J. P. L., & Sauter, M. (2013).**  
*An integrated study of spatial multicriteria analysis and mathematical modelling for managed aquifer recharge site suitability mapping and site ranking at Northern Gaza coastal aquifer.*  
Journal of Environmental Management, 124, 25–39.  
DOI: `10.1016/j.jenvman.2013.03.023`

**Use here:** strongly supports the article’s argument that suitability mapping can be a first-stage decision tool and that deeper hydrogeological analysis can be needed.

---

### South India — recharge structures

**Aju, C. D., Achu, A. L., Raicy, M. C., & Reghunath, R. (2021).**  
*Identification of suitable sites and structures for artificial groundwater recharge for sustainable water resources management in Vamanapuram River Basin, South India.*  
HydroResearch, 4, 24–37.  
DOI: `10.1016/j.hydres.2021.04.001`

**Use here:** direct Indian example linking recharge-potential assessment with possible recharge-structure selection.

---

### Western India — recharge potential + MCDA

**Kadam, A. K., Umrikar, B. N., & Sankhua, R. N. (2020).**  
*Assessment of recharge potential zones for groundwater development and management using geospatial and MCDA technologies in semiarid region of Western India.*  
SN Applied Sciences, 2, 312.  
DOI: `10.1007/s42452-020-2079-7`

**Use here:** regionally relevant evidence for geospatial / MCDA recharge-potential assessment in semiarid Western India.

---

### India — GIS + AHP groundwater-potential mapping

**Arulbalaji, P., Padmalal, D., & Sreelash, K. (2019).**  
*GIS and AHP techniques based delineation of groundwater potential zones: a case study from Southern Western Ghats, India.*  
Scientific Reports, 9, 2082.  
DOI: `10.1038/s41598-019-38567-x`

**Use here:** illustrates integration of multiple thematic layers and validation against groundwater information.

---

### Global MAR context

**Dillon, P., Stuyfzand, P., Grischek, T., et al. (2019).**  
*Sixty years of global progress in managed aquifer recharge.*  
Hydrogeology Journal, 27, 1–30.  
DOI: `10.1007/s10040-018-1841-z`

**Use here:** global managed-aquifer-recharge context, and the wider role of design, operation, governance and hydrogeology.

---

### Recent GIS-MCDA recharge siting

**Talozi, S. A., Alharahsheh, T. A., & Hamdan, I. A. (2023).**  
*Selecting suitable sites for groundwater recharge in Jordan using the spreading techniques via the integration of multi-criteria decision analysis and geographic information system tools.*  
Groundwater for Sustainable Development, 22, 100948.  
DOI: `10.1016/j.gsd.2023.100948`

**Use here:** demonstrates that MAR siting criteria can include technical, environmental and economic considerations and are context-specific.

---

# 10. Author / practitioner lens

The author section should establish provenance without becoming a résumé.

Suggested structure:

## About the practitioner behind the work

> Kaushal Gadariya is a Soil and Water Conservation Engineer working across groundwater, watershed and natural-resource management. His postgraduate research in Soil and Water Conservation Engineering examined the identification of potential sites for groundwater recharge structures using MCDA, remote sensing and GIS. He has continued applying and refining this field–GIS decision approach in professional work since 2019.

Then:

### Areas of applied work
- groundwater recharge planning;
- GIS / RS–MCDA;
- watershed and NRM planning;
- field-linked spatial analysis;
- water-security diagnostics;
- technical decision-support tools;
- applied research.

Avoid:
- “leading expert”;
- “renowned”;
- “best”;
- unsupported professional superlatives.

---

# 11. Collaboration / contact CTA

Use one restrained CTA near the end:

## Working on a similar groundwater or NRM question?

> The framework shown here is intentionally presented as a decision approach rather than a universal recipe. Applying it to a new geography requires local data, hydrogeological interpretation, field verification and context-specific judgement.

**CTA options:**
- **Discuss a technical collaboration**
- **Explore an applied research question**
- **Connect on GIS / groundwater recharge planning**

Possible supporting line:

*For applied GIS studies, groundwater-recharge planning, field-linked MCDA, analytical tools, research collaboration or NRM decision-support assignments.*

The CTA should link to the author’s existing professional profile/contact route.

---

# 12. Professional curiosity without artificial secrecy

Curiosity should come from:
- good questions;
- selected deeper evidence notes;
- “what the map cannot tell us” moments;
- field decision examples;
- model limitations;
- structure-level interrogation;
- references to further analysis that a real assignment would require.

Do not use:
- “secret method”;
- “proprietary formula” unless legally true;
- artificial withholding of basic scientific information;
- unexplained black-box scoring.

---

# 13. Revised evidence-story flow

**Field problem**  
→ **Sabarkantha case**  
→ **Read the landscape**  
→ **Convert field questions into spatial evidence**  
→ **Structure the evidence with GIS-MCDA**  
→ **Interpret GWRPZ cautiously**  
→ **Add hydrological position**  
→ **Add structural context**  
→ **Test against 58 constructed structures**  
→ **Bring community + engineering + field verification back into the decision**  
→ **Show outcomes only at the evidence level available**  
→ **Extract transferable learning**  
→ **Invite exploration / research / collaboration**

---

# 14. Gate 5 decision

This revision supersedes `Web_Article_Content_Architecture_v0.1.md`.

**Gate 5 remains PENDING USER APPROVAL.**

Approval should focus on:
- whether this evidence-story positioning feels right;
- whether the balance between useful disclosure and deeper professional methodology is appropriate;
- whether the author / collaboration sections are restrained enough;
- whether the research layer is sufficiently academic without making the story heavy;
- whether community consultation / approval and field implementation are represented accurately.

Phase 6 should use this v0.2 architecture after approval.