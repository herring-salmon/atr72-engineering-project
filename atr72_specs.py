"""
atr72_specs.py
==============
Centralized specification file for the ATR-72-600 engineering project (Phase 0.1).

RULE OF THIS FILE: every notebook in every later phase imports its aircraft
numbers from HERE. Nothing gets hard-coded a second time anywhere else. If a
number is refined later, it changes in exactly one place and every downstream
calculation updates automatically.

Every constant below carries a source tag in its inline comment:

    [ATR-FS]  ATR 72-600 Factsheet (manufacturer), atr-aircraft.com,
              https://www.atr-aircraft.com/wp-content/uploads/2020/07/Factsheets_-_ATR_72-600.pdf
    [REF]     A well-established third-party technical reference, cited by name.
    [EST]     An ENGINEERING ESTIMATE made by this project because the true
              value is not publicly published (ATR does not release detailed
              wing planform or airfoil data). Each [EST] comment says which
              later phase is responsible for refining or replacing it.

Units: SI throughout (m, kg, s, Pa, K, W). Where the source published a
different unit (ft, lb, kt, SHP...), that original figure is kept in the
comment so the conversion can always be checked by hand.
"""

# ---------------------------------------------------------------------------
# GEOMETRY
# ---------------------------------------------------------------------------

class Geometry:
    """External airframe geometry, all lengths in meters, areas in m^2."""

    # --- Wing ---
    wingspan = 27.05            # m   [ATR-FS: 27.050 m / 88 ft 9 in]
    wing_area = 61.0            # m^2 [ATR-FS: 61 m^2 / 657 sq ft]
    aspect_ratio = wingspan ** 2 / wing_area   # derived, dimensionless (~12)

    # Detailed wing planform (taper, sweep, twist) is NOT published by ATR —
    # the project plan itself notes the airfoil is proprietary and the exact
    # planform must be reconstructed. The two figures below are placeholders,
    # NOT to be trusted for load calculations until Phase 2.1 replaces them
    # with a planform reverse-engineered from three-view drawings/photos.
    taper_ratio_est = 0.55              # [EST] refine in Phase 2.1
    quarter_chord_sweep_deg_est = 0.0   # [EST] ATR-72 wing is essentially unswept

    # First-pass mean aerodynamic chord, rectangular-wing approximation
    # (valid only as a placeholder for Phase 0 Reynolds number estimate).
    # Phase 2.1 replaces this with the proper tapered-wing MAC formula.
    mean_aerodynamic_chord_est = wing_area / wingspan   # [EST] m, ~2.26 m

    # --- Fuselage ---
    fuselage_length = 27.166    # m   [ATR-FS: 27.166 m / 89 ft 1.5 in] (overall aircraft length)
    cabin_width = 2.57          # m   [REF: Swift Jet Aviation ATR72-600 spec sheet]
    fuselage_diameter_est = 2.87  # m [EST: external diameter, consistent with the
                                   #    2.57 m cabin width plus typical skin/frame
                                   #    allowance; refine in Phase 4.1]

    # --- Overall ---
    height = 7.65                # m [ATR-FS: 7.65 m / 25 ft 1 in]

    # --- Propeller ---
    propeller_diameter = 3.93    # m [ATR-FS: Ø 3.93 m / 12.9 ft, Hamilton Standard 568F]
    propeller_blades = 6         # [ATR-FS]


# ---------------------------------------------------------------------------
# WEIGHTS
# ---------------------------------------------------------------------------

class Weights:
    """Mass properties, all in kilograms."""

    mtow_basic = 22800.0     # kg [ATR-FS] max take-off weight, basic
    mtow_option = 23000.0    # kg [ATR-FS] max take-off weight, option 1
    mlw = 22350.0            # kg [ATR-FS] max landing weight, basic
    mzfw = 20800.0           # kg [ATR-FS] max zero fuel weight, basic

    oew_tech_spec = 13010.0  # kg [ATR-FS] operational empty weight (technical spec)
    oew_typical = 13450.0    # kg [ATR-FS] operational empty weight (typical in-service)

    max_payload = 7550.0     # kg [ATR-FS] at typical in-service OEW
    max_fuel = 5000.0        # kg [ATR-FS] max fuel load

    n_pax_standard = 72      # [ATR-FS] standard configuration, 29" pitch


# ---------------------------------------------------------------------------
# PERFORMANCE
# ---------------------------------------------------------------------------

class Performance:
    """Reference flight performance figures, SI units."""

    # The project plan describes cruise altitude as "roughly 7.5 km".
    # 7620 m = 25,000 ft is the published service ceiling and sits inside
    # that stated range, so it is used as the representative cruise altitude
    # for Phase 0/1 Reynolds-number and Mach-number work.
    cruise_altitude = 7620.0        # m (25,000 ft) [ATR-FS: service-related figure]

    max_cruise_speed_TAS = 141.4    # m/s [ATR-FS: 275 KTAS = 509.4 km/h, 95% MTOW, optimum FL]
    max_cruise_mach_est = 0.45      # [EST/REF] consistent with project plan's stated cruise regime

    optimum_climb_speed_CAS = 87.5  # m/s [ATR-FS: 170 KCAS]
    rate_of_climb_SL_MTOW = 6.88    # m/s [ATR-FS: 1355 ft/min]
    time_to_climb_FL170_s = 1050.0  # s  [ATR-FS: 17.5 min to FL170]

    range_max_pax_m = 1403896.0     # m  [ATR-FS: 758 NM]
    fuel_flow_cruise = 0.2117       # kg/s [ATR-FS: 762 kg/hr]


# ---------------------------------------------------------------------------
# ENGINE — Pratt & Whitney Canada PW127M (figures are PER ENGINE; aircraft has 2)
# ---------------------------------------------------------------------------

class Engine:
    """Turboprop shaft-power ratings, per engine."""

    n_engines = 2

    takeoff_power_SHP = 2475.0          # [ATR-FS]
    takeoff_power_W = 1845737.0         # 2475 SHP x 745.7 W/SHP
    one_engine_inop_power_SHP = 2750.0  # [ATR-FS] automatic power reserve (APR) rating
    max_continuous_SHP = 2500.0         # [ATR-FS]
    max_climb_SHP = 2192.0              # [ATR-FS]
    max_cruise_SHP = 2132.0             # [ATR-FS]
    max_cruise_W = max_cruise_SHP * 745.7


# ---------------------------------------------------------------------------
# Sanity-check printout when this file is run directly
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("ATR-72-600 — Phase 0 specification summary")
    print("=" * 60)
    print(f"Wingspan             : {Geometry.wingspan:.2f} m")
    print(f"Wing area             : {Geometry.wing_area:.1f} m^2")
    print(f"Aspect ratio          : {Geometry.aspect_ratio:.2f}")
    print(f"MAC (rectangular est.): {Geometry.mean_aerodynamic_chord_est:.3f} m")
    print(f"MTOW (basic)          : {Weights.mtow_basic:.0f} kg")
    print(f"OEW (typical)         : {Weights.oew_typical:.0f} kg")
    print(f"Cruise altitude       : {Performance.cruise_altitude:.0f} m")
    print(f"Max cruise TAS        : {Performance.max_cruise_speed_TAS:.1f} m/s")
    print(f"Engine takeoff power  : {Engine.takeoff_power_SHP:.0f} SHP x {Engine.n_engines}")
    print("=" * 60)
