# GWRPZ — From Mapping to Decision

Interactive groundwater recharge planning web article for the Sabarkantha case study.

## Live testing

- GitHub Pages: https://knightfox789.github.io/GWRPZ/
- Phase 4 GIS smoke test: https://knightfox789.github.io/GWRPZ/config/phase4_smoke_test.html

## Repository role

This repository is the testing and deployment target for the validated GWRPZ web article.

Current project state:
- Phase 2 GIS QA and methodology reconstruction: complete
- Phase 3 spatial evidence register: complete
- Phase 4 web-data package: deployed
- Gate 4: deployment and artifact integrity passed; visual desktop/mobile smoke confirmation remains pending

## Deployment structure

- `docs/` — GitHub Pages deployment root
- `docs/vectors/` — browser-safe GeoJSON vectors
- `docs/structures/` — validated intervention GeoJSON
- `docs/rasters/` — categorical PNG overlays
- `docs/config/` — data metadata, QA and smoke-test harness
- `docs/styles/` — layer styling / legend configuration

Scientific controls:
- supplied final `GWRPZ_Class.tif` remains the final-class reference;
- historical lineament binary flags are not treated as literal intersections;
- nearest-stream and nearest-lineament relationships retain their documented limitations;
- siting alignment is not presented as measured performance.
