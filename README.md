# ATR-72-600 — From Physics to Final Render

*Every shape justified by a number. Every number explained by physics.*

A full engineering and visualization project: every dimension in the final
3D render of an ATR-72-600 traces back to a real calculation — the lift
equation, the stability margin, the center-of-mass balance — rather than
to an artist's guess. The project runs from ISA atmosphere modeling and
airfoil aerodynamics through wing theory, propulsion, weight & balance,
landing gear kinematics, stability & control, flight performance, CAD, and
finally a physically-based Blender render.

## Status

| Phase | Topic | Status |
|---|---|---|
| 0 | Specifications & ISA atmosphere model | done |
| 1 | Airfoil aerodynamics (Xfoil / XFLR5) | next |
| 2 | Full wing aerodynamics (LLT / VLM / OpenVSP) | — |
| 3 | Propulsion (Brayton cycle, propeller) | — |
| 4 | Fuselage geometry, weight & balance | — |
| 5 | Landing gear loads & kinematics | — |
| 6 | Stability & control | — |
| 7 | Flight performance & V-n diagram | — |
| 8 | CAD in Fusion 360 | — |
| 9 | Rendering & animation in Blender | — |

## Repository structure

```
atr72-engineering-project/
├── README.md
├── REFERENCES.md          # master bibliography — see below
├── atr72_specs.py          # single source of truth for every aircraft number
├── phase0/
│   └── phase0_isa_atmosphere.ipynb
├── phase1/                 # created when Phase 1 starts
├── ...
```

`atr72_specs.py` lives at the repo root because every phase imports from
it — geometry, weights, performance, and engine data are defined exactly
once and never re-typed in a notebook.

## Data provenance

Every constant in `atr72_specs.py` and every external fact used in a
notebook is source-tagged (`[ATR-FS]`, `[EASA-TCDS]`, `[ISA-STD]`, ...) and
resolved in full in **[`REFERENCES.md`](./REFERENCES.md)**. Values that
aren't sourced from an external reference are explicitly flagged `[EST]`
in-line, with a note on which phase is responsible for refining them.

## Environment

- Python 3.11, conda environment `atr72`
- Core libraries: NumPy, SciPy, Pandas, Matplotlib, Plotly
- Aerodynamics: Xfoil / PyXFOIL, XFLR5, OpenVSP
- GNU Octave / MATLAB for dynamic simulation (Phases 3, 6)
- Fusion 360 (Phase 8), Blender / Cycles (Phase 9)

```bash
conda env create -f environment.yml   # once environment.yml exists
conda activate atr72
```

## Phase 0 summary

- `atr72_specs.py`: centralized `Geometry`, `Weights`, `Performance`, and
  `Engine` classes, every value source-tagged.
- `phase0/phase0_isa_atmosphere.ipynb`: ICAO Standard Atmosphere
  implementation (troposphere + lower stratosphere), validated against the
  published ISA table (T error 0.000 K, p/ρ error < 0.01%). Computes
  cruise Mach ≈ 0.457 and Reynolds number ≈ 1.14×10⁷, feeding directly
  into the Phase 1 Xfoil setup.

*This README is a living document — updated at the end of every phase
with a short summary and, where useful, a sample plot.*
