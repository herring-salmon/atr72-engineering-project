# ATR-72-600 — From Physics to Final Render

> Every shape justified by a number. Every number explained by physics.

A full engineering and visualization project built around the ATR-72-600 regional turboprop aircraft. The goal is simple but ambitious: every dimension in the final 3D model must trace back to a real calculation. The wing chord comes from a lift equation. The stabilizer area comes from a stability margin requirement. The engine position comes from a center-of-mass balance.

This is what separates engineering visualization from pretty-but-wrong 3D art.

---

## Project Structure

| Phase | Folder | Description |
|-------|--------|-------------|
| 0 | `00_specs/` | Aircraft specifications & ISA atmosphere model |
| 1 | `01_aerodynamics/` | Airfoil analysis, polar curves, Xfoil |
| 2 | `02_propulsion/` | Brayton cycle, propeller thrust, engine model |
| 3 | `03_fuselage/` | Fuselage geometry, interior layout, weight & balance |
| 4 | `04_landing_gear/` | Gear loads, retraction kinematics |
| 5 | `05_stability/` | Static & dynamic stability, control surfaces |
| 6 | `06_performance/` | Takeoff, climb, cruise range, V-n diagram |
| 7 | `07_cad/` | Fusion 360 model driven by Python exports |
| 8 | `08_render/` | Blender Cycles rendering & animation |

---

## Tool Stack

- **Calculations:** Python 3.11, Jupyter Notebooks
- **Numerics:** NumPy, SciPy
- **Data:** Pandas
- **Plots:** Matplotlib, Plotly
- **Aerodynamics:** Xfoil + PyXFOIL, XFLR5, OpenVSP (NASA)
- **Simulation:** GNU Octave / MATLAB
- **CAD:** Fusion 360
- **Rendering:** Blender (Cycles)
- **Version control:** Git + GitHub

---

## Current Status

🔧 **Phase 0 in progress** — collecting ATR-72-600 specifications and implementing the ISA atmosphere model.

| Phase | Status |
|-------|--------|
| 0 — Specs & Atmosphere | 🔧 In progress |
| 1 — Airfoil Aerodynamics | ⏳ Pending |
| 2 — Propulsion | ⏳ Pending |
| 3 — Fuselage & Balance | ⏳ Pending |
| 4 — Landing Gear | ⏳ Pending |
| 5 — Stability & Control | ⏳ Pending |
| 6 — Flight Performance | ⏳ Pending |
| 7 — CAD in Fusion 360 | ⏳ Pending |
| 8 — Render in Blender | ⏳ Pending |

---

## Philosophy

Most 3D aircraft animations online share the same flaw: they look impressive at first glance but fall apart under scrutiny. Wrong proportions, engines in the wrong place, wings too thick or too swept. Art projects pretending to be engineering.

This project is different. When someone asks *"why does the wing look like that?"* — there will be a Jupyter notebook with the answer.

---

*Project by herring-salmon — data engineer learning aerospace, one calculation at a time.*