# Interaction Specification

**Version:** v0.3  
**Date:** 23 September 2026  
**Project:** From Mapping to Decision  
**Positioning:** Practitioner-focused interactive evidence story / guide  
**Status:** REFINED DRAFT COMPLETE — Gate 5 pending user approval

---

## 1. Core interaction principle

### Guided Evidence Story
**Explain how a practitioner thinks.**

### Explore the Evidence
**Let the reader interrogate what was shown.**

### Research & Method
**Let a technical reader examine the intellectual and methodological basis.**

### Collaborate
**Provide a restrained route for technical / research enquiries.**

---

## 2. UX objective by audience

### Practitioner / NGO / CSR professional
Needs:
- decision logic;
- field implications;
- understandable evidence;
- limitations;
- transferability.

### Hydrogeologist / technical specialist
Needs:
- methods;
- source lineage;
- structural / hydrological caveats;
- uncertainty;
- reproducibility.

### Academic / student
Needs:
- conceptual model;
- research references;
- methodology notes;
- terminology;
- further reading.

### Donor / CSR decision-maker
Needs:
- why the method improves planning quality;
- what evidence exists;
- what remains uncertain;
- how community / field processes connect to technical planning.

---

## 3. Story interaction rhythm

Every chapter follows a four-beat pattern:

1. **Field question**
2. **Map / evidence**
3. **Practitioner interpretation**
4. **What we still need to verify**

This is the visible implementation of Kaushal Voice in the UX.

---

## 4. Map states

| State | Story question | Main visual |
|---|---|---|
| P01 | Why is a map not yet a decision? | villages + faint GWRPZ + drainage |
| P02 | What is the Sabarkantha case? | structures + villages |
| P03 | How does a practitioner read the landscape? | drainage order + context |
| P04A | What does aquifer evidence add? | aquifer |
| P04B | What does slope add? | slope score |
| P04C | What does drainage density add? | drainage-density score |
| P04D | What does lineament density add? | lineament-density score |
| P04E | What does land use add? | LULC |
| P05 | How does MCDA structure judgement? | factor-weight composer |
| P06 | What can GWRPZ say? | final GWRPZ |
| P07 | What changes when hydrological position is added? | GWRPZ + drainage + structures |
| P08 | What changes when structural context is added? | structures + lineaments |
| P09 | What do the 58 structures reveal? | structure evidence + filters |
| P10 | How does a candidate become a field decision? | decision pathway |
| P11 | What evidence exists after construction? | outcome evidence cards when available |

---

## 5. New story components

### Field Question card
At the start of each chapter:
> “What would I want to know before recommending a structure here?”

### Practitioner Note
Short, visually distinct observation:
> “A high-potential pixel narrows the search. It does not tell us whether the intended structure is constructible or hydrogeologically appropriate.”

### Evidence Note
Shows:
- source;
- method;
- evidence class;
- limitation.

### Research Link
“Related research” opens 1–3 relevant papers for the current concept.

### Field Reality strip
Used selectively:
**Map → Site visit → Community discussion → Engineering check → Construction → Observation**

---

## 6. Main navigation

Desktop:
- Story
- Explore Evidence
- Research & Method
- About
- Collaborate

Mobile:
- Story / Explore
- compact menu for Research / About / Collaborate

Avoid a consultancy-style primary button in the hero.

Collaboration CTA appears only after the reader has seen substantive evidence.

---

## 7. Explore the Evidence mode

### Layers
Potential:
- Final GWRPZ
- Aquifer score
- Slope score
- Drainage-density score
- Lineament-density score
- LULC

Context:
- Villages
- Drainage order
- Lineaments

Implementation:
- Structures

### Filters
- Structure Type
- Village
- Block
- Final GWRPZ Class
- Nearest Stream Order
- Siting Alignment Spatial Setting

Do not expose:
- historical lineament yes/no as a primary filter;
- performance / success;
- invented proximity threshold.

---

## 8. Structure detail panel

### Identity
- Structure ID
- Structure Type
- Village
- Block

### Spatial context
- Final GWRPZ Class
- Nearest mapped Stream Order
- Nearest mapped Stream Distance
- Nearest mapped Lineament Distance
- Siting Alignment Spatial Setting

### Implementation context
Add only where reliable source data become available:
- community consultation / approval status;
- construction status;
- verified field observation;
- monitoring record.

### Evidence footer
> “Spatial setting describes planning context; it is not a performance rating.”

---

## 9. MCDA explainer interaction

Do not build a full “calculator” in the story.

Instead:
- five factors shown as weighted cards;
- user may highlight one factor at a time;
- final composition shown visually;
- “Open technical method” reveals the selected score / threshold table.

This maintains transparency without turning the article into an operational software tutorial.

---

## 10. Research-reference interaction

References must remain **secondary to the evidence story**.

### Story-level behavior
Use at most a small `Research` or `Further reading` marker where a concept needs external support. It should not open a large panel unless the reader chooses to go deeper.

### Main public references control
Use one collapsed disclosure:

`References & further reading  +`

Default state: **closed**.

On click/tap:
- expand the selected references directly below;
- keep the list compact;
- show citation + one-line relevance;
- optionally link to DOI / publisher page.

On second click/tap:
- collapse the list again.

### Full research register
The deeper `Research_Reference_Register` remains available separately for technical readers and does not occupy permanent space in the main story.

---

## 10A. Practitioner quote anchor

Use the following quote once prominently and optionally repeat it near the closing decision section:

> **“GIS helps validate the evidence. The decision still has to be made in the field, with the community.”**

Purpose:
- captures the GIS + field + community philosophy in one line;
- reinforces that GIS supports validation and decision-making rather than replacing field and community processes;
- acts as a memorable bridge between the technical and community dimensions.

Do not over-repeat it. One hero/transition use plus one closing echo is sufficient.

## 11. Outcome evidence interaction

If positive results are included, every result card carries an evidence tag:

- **Measured**
- **Monitored**
- **Field-observed**
- **Community-reported**

This prevents a testimonial or observation from visually looking equivalent to a measured result.

---

## 12. Community / implementation interaction

Use a decision-pathway diagram, not a generic “participation” paragraph.

Clickable steps:
1. technical screening;
2. field reconnaissance;
3. local / community consultation;
4. site / land / access confirmation;
5. technical design;
6. approval;
7. construction;
8. observation / O&M / monitoring.

Only describe steps as universal if the project record supports them.

---

## 13. Author-positioning interaction

### About card
Keep biography concise.

### “Why this work”
One short timeline:
- postgraduate research on groundwater recharge site identification using MCDA + RS + GIS;
- applied professional work on the subject since 2019;
- continuing focus on connecting GIS evidence with field decisions.

### CTA
After the references / closing:
- Discuss a technical collaboration
- Explore an applied research question
- Connect on groundwater / GIS / NRM work

No pop-ups.
No aggressive lead form.
No hero-level self-promotion.

---

## 14. Desktop wireframe

```text
┌────────────────────────────────────────────────────────────────┐
│ From Mapping to Decision   Story | Explore | Research | About │
├────────────────────────────────────────────────────────────────┤
│ STORY 40%                    EVIDENCE / MAP 60%                 │
│                                                                │
│ Field question               interactive map                   │
│ short narrative              evidence figure                  │
│ practitioner note            layer transition                 │
│ key evidence                 compact legend                    │
│ limitation                   [research] [method]               │
│                                                                │
│ community / field strip where relevant                        │
├────────────────────────────────────────────────────────────────┤
│ Case learning → Research & Method → Author / Collaborate       │
└────────────────────────────────────────────────────────────────┘
```

---

## 15. Mobile wireframe

```text
┌──────────────────────────────┐
│ Title      Story | Explore   │
├──────────────────────────────┤
│ map / evidence ~44vh         │
├──────────────────────────────┤
│ FIELD QUESTION               │
│ narrative                    │
│ key evidence                 │
│ practitioner note            │
│ limitation                   │
│ [Research] [Method]          │
├──────────────────────────────┤
│ next chapter                 │
└──────────────────────────────┘
```

Reference and methodology panels become bottom sheets.

---

## 16. Curiosity / depth pattern

Use **progressive disclosure**:

### Level 1
Plain-language story.

### Level 2
Evidence / method note.

### Level 3
Research reference / technical detail.

### Level 4
Professional collaboration for new-geography application, deeper analysis or research.

This is more credible than artificially hiding basic methodology.

---

## 17. Gate 5

This v0.3 supersedes `Interaction_Specification_v0.2.md`.

**Gate 5 remains pending user approval.**