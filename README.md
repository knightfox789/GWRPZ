# GWRPZ — From Mapping to Decision

Interactive groundwater recharge planning web article for the Sabarkantha case study.

## Repository role

This repository is the testing and deployment target for the validated GWRPZ web article.

Current project state:
- Phase 2 GIS QA and methodology reconstruction: complete
- Phase 3 spatial evidence register: complete
- Phase 4 web-data preparation: in progress
- Gate 4: pending deployed desktop/mobile browser smoke test

## Deployment structure

- `docs/` — GitHub Pages / browser testing site
- `docs/data/` — browser-safe GIS derivatives
- `docs/config/` — data metadata and layer configuration
- `docs/styles/` — layer styling / legend configuration
- `project/` — project manifests, QA notes and recovery documentation

Scientific controls:
- supplied final `GWRPZ_Class.tif` remains the final-class reference;
- historical lineament binary flags are not treated as literal intersections;
- nearest-stream and nearest-lineament relationships retain their documented limitations;
- siting alignment is not presented as measured performance.
