# GWRPZ Public Feedback Revision v1.0.2

**Date:** 24 September 2026  
**Status:** BROWSER QA PASS — READY FOR DEPLOYMENT

## Additional user corrections applied

### Implemented-sites section
- Removed the reader-facing explanation about 122 source records and the two excluded conflicts.
- Replaced research/QA wording such as **cohort**, **defensible cohort**, and **publication cohort** with direct practitioner wording.
- Opening now states simply: **120 interventions at 109 locations**.

### V03
- Replaced the internal/design subtitle with a direct map instruction.
- `Filtered cohort` → `Interventions shown`.
- Removed the note about anonymous public IDs and hidden coordinate values.
- Removed the EPSG:32643 / pixel-reproduction georeferencing note from the reader-facing visual.
- The corrected raster/point alignment from v1.0.1 is retained unchanged.

### Litholog / V06
- Removed the reader-facing paragraph explaining source flag `Y`.
- Removed `Y` from litholog layer labels, outlines and context statistics.
- Retained the underlying source field internally; it is no longer part of the reader-facing article.
- Removed `anonymous public` terminology from the V06 introduction.

### V07
- Removed the sentence about not inferring measured groundwater-flow direction.
- Replaced it with a short practitioner description of how the six borehole logs are arranged.
- Removed reader-facing `Y` outlines from the section.

### Wider language pass
The public article was checked for internal production / research-QA language. The following were removed or simplified where they appeared in reader-facing text:
- cohort / publication cohort
- defensible
- public IDs / anonymous IDs
- publication reference / publication layer
- internal source/package wording
- defensive technical caveats that belong in QA rather than the narrative
- `Reader takeaway:` labels
- developer-facing no-JavaScript message

The analytical numbers and evidence interpretation remain unchanged.

## Browser QA

### Desktop 1440×1000
- console/page errors: **0**
- horizontal overflow: **False**
- V03 points rendered: **120**
- Chapters drawer opens: **True**

### Mobile 390×844
- console/page errors: **0**
- horizontal overflow: **False**
- V03 points rendered: **120**

### Reader-facing language scan
All targeted phrases are absent from the rendered article:
- `122 records`
- `cohort` / `publication cohort`
- `defensible`
- `general-purpose dashboard`
- `anonymous public` / public-ID note
- EPSG:32643 reader-facing georeferencing note
- source flag `Y` explanation
- measured groundwater-flow-direction disclaimer
- `Reader takeaway:` labels

## Evidence integrity

The v1.0.2 revision changes reader-facing language and removes internal QA/development wording. It does **not** change:
- 120-intervention / 109-location analysis;
- GWRPZ classification;
- intervention coordinates or the corrected V03 georeferencing;
- litholog depths or layer sequences;
- groundwater monitoring values;
- acknowledgement or author links.