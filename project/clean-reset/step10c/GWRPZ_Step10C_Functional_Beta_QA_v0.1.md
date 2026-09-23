# GWRPZ Step 10C — Functional Beta QA v0.1

**Date:** 24 September 2026  
**Result:** **PASS — GATE P4 SATISFIED**

## Rendering and interaction smoke test

The functional beta was executed in headless Chromium by injecting the self-contained HTML into a browser page. Direct `file://` and localhost navigation are blocked by the current runtime administrator, so the test uses `page.set_content()` with the exact generated HTML bytes. Because the beta embeds its required data and raster images, this exercises the same CSS/JavaScript/DOM logic used by the delivered artifact.

### Desktop — 1440 × 1000
- visual modules: **9**
- article sections: **13**
- JavaScript initialized: **True**
- V03 Recharge Borewell filter result: **54**
- V06 selected profile smoke test: **L05 · 51.82 m drilled**
- V09 final-stage smoke test: **Monitor — What should the next decision investigate?**
- console/page errors: **0**
- horizontal overflow: **False**

### Mobile — 390 × 844
- visual modules: **9**
- article sections: **13**
- JavaScript initialized: **True**
- V03 Recharge Borewell filter result: **54**
- V06 selected profile smoke test: **L05 · 51.82 m drilled**
- V09 final-stage smoke test: **Monitor — What should the next decision investigate?**
- console/page errors: **0**
- horizontal overflow: **False**

## Gate P4 checklist

- all Story Lock article sections render — PASS
- V01–V09 implemented — PASS
- approved Step 9 public data embedded — PASS
- core interactions execute — PASS
- article remains readable without JavaScript — PASS
- responsive desktop/mobile rules — PASS
- reduced-motion CSS — PASS
- methods / references / acknowledgement / article note / author footer — PASS
- no external runtime API or database — PASS
- external script dependencies: **0**
- external stylesheet dependencies: **0**
- prohibited internal-field token scan: **None**

## Visual inspection

Representative V04 and V06 desktop/mobile screenshots were manually inspected after the automated run. Mobile navigation was changed from sticky to normal-flow so it does not obscure interactive controls. The desktop brand header was reduced to a single-line compact identity.

## Architecture note

The approved Master Plan recommended Astro and MapLibre. The Step 10C functional beta uses dependency-free HTML/CSS/browser-native JavaScript/SVG for the gated preview. This is an implementation adaptation, not a Story Lock or data-model change. Maintainable source inputs remain separate from generated `docs/` output in this package.

## Gate decision

**GATE P4: PASS.**

Exact next phase: **STEP 10D — Integrated QA and Release Candidate.**