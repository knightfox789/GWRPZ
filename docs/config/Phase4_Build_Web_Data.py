# Phase 4 web-data build
# Reproduces the accepted format choices recorded in Web_GIS_Data_Manifest_v0.1.md.
# Source data must be the preserved Package A archive plus accepted Phase 2A/2B/2E derivatives.
#
# Conversion contract:
# - vectors -> EPSG:4326 GeoJSON with publication-safe attributes
# - villages -> 10 m coverage-aware simplification
# - aquifers -> 10 m topology-preserving simplification
# - drainage -> 5 m topology-preserving simplification
# - lineaments -> unsimplified
# - LULC -> 10 m topology-preserving simplification from repaired Phase 2A derivative
# - interventions -> accepted Phase 2E point derivative; no historical Lineament_ field
# - categorical rasters -> RGBA PNG preserving target-grid pixels; NoData transparent
# - raster corner coordinates -> EPSG:4326, written to raster_sources.json
#
# See Phase4_Web_Data_QA_Metrics_2026-09-22.json and vector_conversion_qa.csv
# for reproducibility checks and accepted geometry changes.