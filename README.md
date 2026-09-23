# GWRPZ — From Mapping to Decision

Interactive groundwater recharge evidence story grounded in the Sabarkantha study and the professional work of Kaushal Gadariya, Soil and Water Conservation Engineer.

## Live technical testing

- GitHub Pages: https://knightfox789.github.io/GWRPZ/
- Phase 4 GIS smoke test: https://knightfox789.github.io/GWRPZ/config/phase4_smoke_test.html

## Phase 5 narrative reset

The earlier Phase 5 UX prototypes are retained as archived design experiments and are **not the controlling direction**.

Current controlling Phase 5 documents:

- `project/phase5-reset/Professional_Legacy_Story_Architecture_v1.0.md`
- `project/phase5-reset/Visual_Storyboard_Professional_Legacy_v1.0.md`
- `project/phase5-reset/Professional_Audience_Brand_Brief_v1.0.md`
- `project/phase5-reset/GWRPZ_Phase5_Narrative_Reset_QA_v1.0.md`

Current rule:

**Story first → visuals second → UX third.**

No replacement Phase 5 prototype should be built until the professional legacy story, visual storyboard and audience/brand brief are approved.

## Repository role

This repository is the testing and deployment target for the validated GWRPZ web article.

Current project state:
- Phase 2 GIS QA and methodology reconstruction: complete
- Phase 3 spatial evidence register: complete
- Phase 4 web-data package: deployed
- Gate 4: deployment and artifact integrity passed; visual desktop/mobile smoke confirmation remains pending
- Phase 5: narrative reset package complete; Gate 5 reopened pending story/visual/audience approval
- Phase 6: not started

## Deployment structure

- `docs/` — GitHub Pages deployment root
- `docs/vectors/` — browser-safe GeoJSON vectors
- `docs/structures/` — validated intervention GeoJSON
- `docs/rasters/` — categorical PNG overlays
- `docs/config/` — data metadata, QA and smoke-test harness
- `docs/styles/` — layer styling / legend configuration
- `project/phase5-reset/` — controlling narrative-reset documents

Scientific controls:
- supplied final `GWRPZ_Class.tif` remains the final-class reference;
- historical lineament binary flags are not treated as literal intersections;
- nearest-stream and nearest-lineament relationships retain their documented limitations;
- siting alignment is not presented as measured performance.
