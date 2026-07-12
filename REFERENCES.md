# References

Every external source used anywhere in this project is listed here, once.
Code comments (in `atr72_specs.py` and in notebooks) cite sources with a
short tag — e.g. `[ATR-FS]` — instead of repeating the full citation inline.
This file is where that tag resolves to a full reference: publisher/author,
title, URL, date accessed, and exactly which numbers it supports.

**Rule:** if a notebook or script introduces a new external number, it gets
a tag, and the tag gets an entry here in the same commit. Nothing gets
cited only in someone's head.

`[EST]`-tagged values in the code are *not* listed here — by definition
they are this project's own engineering estimates, not external sources.
The comment next to an `[EST]` value already says which phase is
responsible for replacing it with a sourced or derived number.

---

## Aircraft data — Phase 0.1 (`atr72_specs.py`)

| Tag | Source | Publisher / Author | URL | Accessed | Used for |
|---|---|---|---|---|---|
| `[ATR-FS]` | ATR 72-600 Factsheet | ATR (manufacturer) | <https://www.atr-aircraft.com/wp-content/uploads/2020/07/Factsheets_-_ATR_72-600.pdf> | 2026-07-12 | wingspan, wing area, overall length, height, propeller diameter & blade count, MTOW (basic/option), MLW, MZFW, OEW (tech spec & typical), max payload, max fuel, PW127M power ratings (takeoff/OEI/max continuous/climb/cruise), max cruise speed, optimum climb speed, rate of climb, time to climb, range, cruise fuel flow |
| `[REF]` | ATR72-600 Aircraft Data Sheet | Swift Jet Aviation | <https://swiftjetaviation.com/atr72-600/> | 2026-07-12 | cabin width (2.57 m) — used as the basis for the `[EST]` external fuselage diameter in `Geometry.fuselage_diameter_est` |

**Not yet used, but authoritative and worth pulling from directly in later
phases** (Weight & Balance in Phase 4, V-speeds and stability limits in
Phase 6/7 will likely need figures straight from the regulatory source
rather than a manufacturer factsheet):

| Tag | Source | Publisher | URL | Note |
|---|---|---|---|---|
| `[EASA-TCDS]` | Type Certificate Data Sheet No. EASA.A.084, ATR 42/72 | EASA | <https://www.easa.europa.eu/en/downloads/7358/en> | Located, not yet mined for specific values — do this before Phase 4/6/7 need CG limits, structural V-speeds, or certified weight variants. |

---

## Atmosphere & physical constants — Phase 0.2 (`phase0_isa_atmosphere.ipynb`)

| Tag | Source | Publisher / Author | URL | Accessed | Used for |
|---|---|---|---|---|---|
| `[ISA-STD]` | Manual of the ICAO Standard Atmosphere (Doc 7488), 3rd ed., 1993 | ICAO | <https://store.icao.int/en/manual-of-the-icao-standard-atmosphere-extended-to-80-kilometres-262500-feet-doc-7488> | 2026-07-12 | The official standard defining the ISA model: sea-level reference values, tropospheric lapse rate, layer boundaries. |
| `[ISA-DERIV]` | "The International Standard Atmosphere (ISA)" | Mustafa Cavcar, Anadolu University | <http://fisicaatmo.at.fcen.uba.ar/practicas/ISAweb.pdf> | 2026-07-12 | Worked derivation of the troposphere/stratosphere T(h) and p(h) equations; the published ISA table (0–12 km) used to validate `isa_temperature`/`isa_pressure`/`isa_density` against. |
| `[SUTH]` | "Sutherland's law" (citing Sutherland, W., 1893, *Phil. Mag.*, S.5, 36, pp.507–531) | CFD-Online Wiki | <https://www.cfd-online.com/Wiki/Sutherland's_law> | 2026-07-12 | Dynamic-viscosity formula and reference constants (μ₀ = 1.716×10⁻⁵ Pa·s, T_ref = 273.15 K, S = 110.4 K) used in `sutherland_viscosity()`. |

---

## How to extend this file (do this every phase)

1. New external number enters a notebook or `.py` file → give it a short
   tag in the code comment (`[XYZ]`), following the existing naming style.
2. Add one row to the relevant table above (create a new `## <Phase name>`
   section if it's a new phase) with: tag, source title, publisher/author,
   URL, date accessed, and a one-line note on exactly which value(s) it
   supports.
3. If a source is looked at but not yet mined for values (like
   `[EASA-TCDS]` above), still list it in a "not yet used" table so it
   isn't rediscovered from scratch next phase.
4. Commit this file together with the code change that used the source —
   same discipline as `atr72_specs.py` itself: one change, one place,
   one commit.
