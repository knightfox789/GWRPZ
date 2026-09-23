# Phase 5 — Humanization, Lineament Logic & Layout QA

**Version:** v0.5  
**Date:** 23 September 2026  
**Status:** REFINEMENT COMPLETE — Gate 5 pending user approval

## 1. Revision trigger

User review of the live Phase 5 v0.4 prototype identified the following issues:

- replace the temporary `KG` header mark with the approved Water Security Intelligence logo;
- change the hero label from `Practitioner evidence story` to an evidence-based decision-guide framing;
- remove the `What this is / What this is not` contrast block;
- align the four summary cards and chapter evidence cards properly;
- remove repetitive warning-box text shown in the reviewed screenshots;
- rewrite the lineament section around hydrogeological planning logic rather than exact line intersection;
- remove the `Explore applied work` CTA button;
- apply the DSC Humanizer / Kaushal Voice more strictly because parts of the article still sounded AI-written.

## 2. Water Security Intelligence branding

Approved logo source:

`knightfox789/dsc-humanizer/skills/water-security-intelligence/assets/water-security-intelligence-logo.png`

Git blob:

`c9ad90f1ebf743fa8a649dcfd4807b48095bfdb1`

The asset is to be preserved unchanged.

Header pattern:

`[Water Security Intelligence logo] From Mapping to Decision`

The article title remains the primary text identity.

## 3. Hero copy

Changed:

`Practitioner evidence story · Sabarkantha, Gujarat`

to:

`Evidence-based decision guide · Sabarkantha, Gujarat`

Removed:
- `What this is`
- `What this is not`

Replaced with one affirmative description of the guide.

## 4. Summary-card alignment

The four top cards now use an equal-width grid with centred vertical alignment:

- 58 structures analysed;
- 49 villages represented;
- 5 spatial evidence layers;
- Field + community + engineering.

Chapter metric cards use a common minimum height so numeric values and labels align consistently.

## 5. Humanization rule

The main story no longer repeatedly follows the pattern:

`finding → not X → warning`

Instead it states:
- what the evidence means;
- how it is used;
- what the next field / technical check is.

Material caveats are retained in collapsed `Method note` disclosures.

This follows the `dsc-humanizer` / Kaushal Voice rules:
- evidence before adjectives;
- practical field reasoning;
- technically precise but readable language;
- uncertainty preserved;
- avoid repetitive contrast constructions;
- avoid generic AI-style framing.

## 6. Removed prominent warning-card copy

The following items no longer appear as yellow warning boxes in the main story:

- structure dataset is not a district census;
- spatial alignment is not proof of performance;
- historical final class-break caveat;
- literal stream-line intersection caveat;
- spatial setting is not a performance score.

Where material, the method / interpretation issue remains available in ordinary prose or a collapsed Method note.

## 7. Lineament logic — revised

The main section now uses:

**Use lineaments to guide where to investigate**

Displayed evidence:
- closest mapped lineament: 27.4 m;
- median nearest-lineament distance: 1,209.5 m;
- farthest distance: 5,177.5 m.

Interpretation:

Mapped lineaments can indicate structural discontinuities such as fractures or fault zones. When open and hydraulically connected, such features can act as preferential pathways for groundwater movement and recharge. The planning value of the lineament layer is therefore to identify structural zones that deserve closer field investigation around a candidate site.

A structure does not need to sit exactly on a mapped lineament for the lineament to be hydrogeologically relevant.

Technical diagnostic moved to the collapsed Method note:
- none of the 58 intervention point geometries coincides exactly with a supplied lineament polyline;
- nearest-lineament distance is retained as the reproducible spatial relationship;
- no undocumented proximity threshold is imposed.

## 8. Author / CTA

The author section now uses:
- `Author`;
- `Kaushal Gadariya`;
- `Soil and Water Conservation Engineer`;
- direct provenance paragraph;
- LinkedIn;
- Portfolio.

Removed:
- `Research-grounded. Field-linked. Decision-oriented.`
- `Explore applied work` CTA button.

Only one primary CTA remains:

`Discuss a technical collaboration`

## 9. Critical outputs

- `/GW Recharge/06_Web_Article/content/Web_Article_Content_Architecture_v0.5.md`
- `/GW Recharge/06_Web_Article/components/Interaction_Specification_v0.5.md`
- `/GW Recharge/06_Web_Article/releases/Phase5_UX_Prototype_v0.5.html`
- `/GW Recharge/06_Web_Article/releases/GWRPZ_Phase5_Humanization_QA_v0.5.md`

## 10. Gate

**Gate 5 remains PENDING USER APPROVAL.**

The next review should focus on:
1. whether the writing now sounds like an experienced practitioner rather than AI-generated copy;
2. whether the lineament explanation reflects the intended hydrogeological logic;
3. whether the header/logo and author section feel appropriate;
4. whether summary/evidence cards are visually aligned;
5. whether Method notes now hold the right amount of technical caveat without interrupting the story.