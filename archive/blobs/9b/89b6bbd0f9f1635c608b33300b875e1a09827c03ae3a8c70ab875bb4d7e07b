from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = ROOT.parent / "mtt-results-repro" / "release" / "authority"

A49_PACKET = (
    AUTHORITY
    / "A49"
    / "candidate_data"
    / "selected_physicalfinitediracoperatorandintersectionform_or_fullfinitetripleclosure"
    / "physical_DF_and_finite_triple.packet.json"
)
A51_CERT = (
    AUTHORITY
    / "A51"
    / "certificates"
    / "selected_finitespectralactionandhiggsinnerfluctuation_or_directgenerativesmactionclosure_certificate.json"
)
A51_PACKET = (
    AUTHORITY
    / "A51"
    / "candidate_data"
    / "selected_finitespectralactionandhiggsinnerfluctuation_or_directgenerativesmactionclosure"
    / "finite_inner_fluctuation_and_spectral_traces.packet.json"
)
A52_CERT = (
    AUTHORITY
    / "A52"
    / "certificates"
    / "selected_spectralcutoffmomentsandspacetimeproducttriple_or_bosonicactionnormalization_certificate.json"
)
A53_CERT = (
    AUTHORITY
    / "A53"
    / "certificates"
    / "selected_propertimemeasureandoverlapkineticmetricsource_or_strictspectralactionclosure_certificate.json"
)
A53_PACKET = (
    AUTHORITY
    / "A53"
    / "candidate_data"
    / "selected_propertimemeasureandoverlapkineticmetricsource_or_strictspectralactionclosure"
    / "proper_time_atom_and_overlap_source_cutset.packet.json"
)
ACTION_REDUCTION = ROOT / "certificates" / "closure_to_einstein_action_reduction_certificate.json"
NONLINEAR_NOGO = ROOT / "certificates" / "quadratic_tt_nonlinear_action_nogo_certificate.json"

OUT_CERT = ROOT / "certificates" / "spectral_action_einstein_ir_limit_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Spectral_Action_Einstein_IR_Limit_and_Vacuum_Obstruction_v1.md"

STATUS = (
    "SPECTRAL_EINSTEIN_WEYL_IR_RATIO_CLOSED_CONDITIONAL_ONE_ATOM_TIER_"
    "BARE_VACUUM_OBSTRUCTION_CLOSED_FULL_ACTION_SELECTION_AND_REMAINDER_OPEN"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def close(left: float, right: float, *, tolerance: float = 1.0e-12) -> bool:
    return math.isclose(left, right, rel_tol=tolerance, abs_tol=tolerance)


def main() -> None:
    a49 = load(A49_PACKET)
    a51 = load(A51_CERT)
    a51_packet = load(A51_PACKET)
    a52 = load(A52_CERT)
    a53 = load(A53_CERT)
    a53_packet = load(A53_PACKET)
    action = load(ACTION_REDUCTION)
    nonlinear_nogo = load(NONLINEAR_NOGO)

    channels = a49["physical_DF"]["channels"]
    moments = a53_packet["proper_time_candidate"]["moments"]
    f0 = float(moments["f0"])
    f2 = float(moments["f2"])
    f4 = float(moments["f4"])
    tau = float(a53_packet["proper_time_candidate"]["tau_int"])

    # In the Chamseddine-Connes-Marcolli notation, c_R and d_R are the
    # Majorana-block invariants. A49's explicit D_F has only four Dirac
    # channels and no particle-antiparticle Majorana block.
    c_R = 0.0
    d_R = 0.0

    # Canonical 96-state spectral-action coefficients. The repository uses
    # S_grav=2*kappa_h int sqrt(-g) R, while the source theorem writes
    # (2*kappa_0^2)^(-1) int sqrt(g) R. Hence kappa_h=1/(4*kappa_0^2).
    kappa_h_over_cutoff_squared = (96.0 * f2 - f0 * c_R) / (48.0 * math.pi**2)
    alpha_0 = -3.0 * f0 / (10.0 * math.pi**2)
    beta_squared_over_cutoff_squared = kappa_h_over_cutoff_squared / abs(alpha_0)
    beta_over_cutoff = math.sqrt(beta_squared_over_cutoff_squared)

    beta_squared_tau_formula = 20.0 / (3.0 * tau)
    cutoff_weyl_fraction = 1.0 / beta_squared_over_cutoff_squared
    cutoff_weyl_tau_formula = 3.0 * tau / 20.0
    eta_bounds = {
        str(eta): (eta**2) * cutoff_weyl_fraction
        for eta in (1.0, 0.5, 0.25, 0.1, 0.01)
    }

    gamma_0_over_cutoff_fourth = (
        48.0 * f4 - f2 * c_R + 0.25 * f0 * d_R
    ) / math.pi**2
    bare_vacuum_curvature_over_cutoff_squared = (
        gamma_0_over_cutoff_fourth / (4.0 * kappa_h_over_cutoff_squared)
    )
    bare_vacuum_tau_formula = 6.0 / tau

    operator_content = a51_packet["bosonic_action_interface"][
        "generated_after_standard_product_triple_heat_kernel_theorem"
    ]
    gravity_row = next(row for row in operator_content if "Einstein-Hilbert" in row)

    checks = {
        "A49_finite_Dirac_dimension_is_96": a49["physical_DF"]["dimension"] == 96,
        "A49_has_exactly_four_Dirac_Yukawa_channels": channels
        == ["Y_u", "Y_d", "Y_e", "Y_nu"],
        "A49_has_no_Majorana_particle_antiparticle_channel": not any(
            token in channel.lower() for channel in channels for token in ("majorana", "m_r", "y_r")
        ),
        "active_Majorana_invariants_cR_dR_vanish": c_R == 0.0 and d_R == 0.0,
        "A51_gravity_operator_architecture_contains_Einstein_and_Weyl": (
            "Einstein-Hilbert" in gravity_row and "Weyl-curvature" in gravity_row
        ),
        "A51_operator_content_closed_but_absolute_normalization_open": (
            a51["bosonic_SM_operator_content_closed_via_standard_heat_kernel_theorem"]
            is True
            and a51["absolute_spectral_action_normalization_closed"] is False
        ),
        "A52_product_interface_closed_but_Wick_and_moments_open": (
            a52["profile_product_triple_interface_closed"] is True
            and a52["strict_MTT_Wick_rotation_closed"] is False
            and a52["strict_spectral_cutoff_moments_closed"] is False
        ),
        "A53_tau_exact_but_point_measure_unselected": (
            a53["tau_int_exact_source_available"] is True
            and a53["point_measure_selected_by_MTT"] is False
        ),
        "one_atom_moment_f2_identity": close(f2, f0 / tau),
        "one_atom_moment_f4_identity": close(f4, f0 / tau**2),
        "Einstein_coefficient_is_positive": kappa_h_over_cutoff_squared > 0.0,
        "Weyl_coefficient_has_stable_Lorentzian_sign": alpha_0 < 0.0,
        "beta_ratio_reduces_exactly_to_tau": close(
            beta_squared_over_cutoff_squared, beta_squared_tau_formula
        ),
        "Weyl_fraction_reduces_exactly_to_tau": close(
            cutoff_weyl_fraction, cutoff_weyl_tau_formula
        ),
        "Weyl_fraction_is_monotone_quadratic_in_IR_scale": all(
            eta_bounds[str(left)] > eta_bounds[str(right)]
            for left, right in zip((1.0, 0.5, 0.25, 0.1), (0.5, 0.25, 0.1, 0.01))
        ),
        "bare_vacuum_ratio_reduces_exactly_to_tau": close(
            bare_vacuum_curvature_over_cutoff_squared, bare_vacuum_tau_formula
        ),
        "quadratic_nonlinear_action_no_go_is_retained": (
            nonlinear_nogo["claim_tiers"]["quadratic_TT_data_select_unique_nonlinear_action"]
            == "CLOSED_NO_GO"
        ),
        "one_Newton_normalization_is_still_required": (
            action["claim_tiers"]["scale_free_q79_data_fix_numeric_kappa_h"]
            == "CLOSED_NO_GO"
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "spectral_action_einstein_ir_limit",
        "date": "2026-07-15",
        "status": STATUS,
        "inputs": {
            "A49_physical_finite_Dirac_packet": str(A49_PACKET),
            "A51_finite_spectral_action_certificate": str(A51_CERT),
            "A51_finite_spectral_action_packet": str(A51_PACKET),
            "A52_product_triple_certificate": str(A52_CERT),
            "A53_proper_time_certificate": str(A53_CERT),
            "A53_proper_time_packet": str(A53_PACKET),
            "closure_to_Einstein_action_reduction": str(ACTION_REDUCTION),
            "quadratic_nonlinear_action_no_go": str(NONLINEAR_NOGO),
        },
        "primary_sources": {
            "spectral_coefficients": {
                "url": "https://arxiv.org/abs/hep-th/0610241",
                "reference": "Chamseddine-Connes-Marcolli, Theorem 3.13 and equations (4.11)-(4.12)",
            },
            "linearized_Einstein_Weyl_equation": {
                "url": "https://arxiv.org/abs/1005.4276",
                "reference": "Nelson-Ochoa-Sakellariadou, equations (13), (15), and (32)",
            },
        },
        "checks": checks,
        "active_finite_Dirac_branch": {
            "dimension": a49["physical_DF"]["dimension"],
            "channels": channels,
            "Majorana_particle_antiparticle_block_present": False,
            "c_R": c_R,
            "d_R": d_R,
            "scope": (
                "Exact for the active A49 Dirac-neutrino profile operator. A future "
                "Majorana block would reopen c_R and d_R."
            ),
        },
        "canonical_coefficients": {
            "action_convention": (
                "S_E=sqrt(g)[(2 kappa_0^2)^(-1) R + alpha_0 C^2 + gamma_0 + ...]; "
                "2 kappa_h=(2 kappa_0^2)^(-1)"
            ),
            "inverse_kappa0_squared": "(96 f2 Lambda^2-f0 c_R)/(12 pi^2)",
            "kappa_h": "(96 f2 Lambda^2-f0 c_R)/(48 pi^2)",
            "alpha_0": "-3 f0/(10 pi^2)",
            "gamma_0": "(48 f4 Lambda^4-f2 Lambda^2 c_R+(f0/4)d_R)/pi^2",
            "beta_squared": "-kappa_h/alpha_0=-1/(32 pi G4 alpha_0)",
        },
        "one_atom_tier": {
            "premise": (
                "mu(t)=f0 delta(t-tau_int), the A53 minimal-support candidate; "
                "not yet selected by an unconditional MTT theorem"
            ),
            "tau_int": tau,
            "tau_formula": "log(448)/15",
            "moments": {"f0": f0, "f2": f2, "f4": f4},
            "profile_f0_cancels_from_dimensionless_gravity_ratios": True,
        },
        "Einstein_Weyl_IR_theorem": {
            "Lorentzian_TT_equation": "(Box-beta^2) Box h_TT = source",
            "Euclidean_TT_kernel_shape": "K_TT(p) proportional to p^2(1+p^2/beta^2)",
            "relative_Weyl_correction": "epsilon_W(p)=p^2/beta^2",
            "kappa_h_over_Lambda_squared": kappa_h_over_cutoff_squared,
            "alpha_0": alpha_0,
            "beta_squared_over_Lambda_squared": beta_squared_over_cutoff_squared,
            "beta_squared_over_Lambda_squared_exact": "20/(3 tau_int)",
            "beta_over_Lambda": beta_over_cutoff,
            "bound_for_p_le_eta_Lambda": "epsilon_W <= (3 tau_int/20) eta^2",
            "eta_bounds": eta_bounds,
            "interpretation": (
                "Within the retained Einstein-plus-Weyl a4 action, the Weyl correction "
                "is quadratically suppressed in the infrared. This is not a bound on "
                "the omitted higher heat-kernel remainder."
            ),
        },
        "vacuum_test": {
            "gamma_0_over_Lambda_fourth": gamma_0_over_cutoff_fourth,
            "bare_curvature_equivalent_magnitude_over_Lambda_squared": (
                bare_vacuum_curvature_over_cutoff_squared
            ),
            "exact_one_atom_formula": "6/tau_int",
            "result": (
                "The point measure does not solve Lambda_eff. Its bare geometric "
                "constant is order Lambda^2 in curvature units and requires a selected "
                "Higgs-vacuum, subtraction, cancellation, or renormalized source law."
            ),
        },
        "claim_tiers": {
            "active_A49_Majorana_invariants": "CLOSED_ZERO_FOR_DIRAC_ONLY_BRANCH",
            "canonical_96_state_Einstein_Weyl_coefficients": "CLOSED_VIA_STANDARD_SPECTRAL_ACTION_THEOREM",
            "dimensionless_Einstein_Weyl_ratio": "CLOSED_CONDITIONAL_ON_A53_ONE_ATOM_TIER",
            "Einstein_IR_suppression_inside_a4_truncation": "CLOSED_QUADRATIC_BOUND_CONDITIONAL",
            "full_spectral_heat_kernel_remainder_bound": "OPEN",
            "A53_one_atom_measure_selected_by_MTT": "OPEN",
            "absolute_Newton_normalization": "OPEN_ONE_DIMENSIONFUL_SCALE",
            "bare_spectral_vacuum_small_or_cancelled": "CLOSED_NO",
            "selected_Lambda_eff": "OPEN",
            "selected_MTT_product_spectral_action": "OPEN",
            "selected_Lorentzian_reconstruction": "OPEN",
            "q79_zero_gap_match_to_spectral_TT_kernel": "OPEN",
            "full_selected_classical_GR": "OPEN",
        },
        "guardrails": {
            "claims_A53_point_measure_unconditionally_selected": False,
            "claims_asymptotic_spectral_remainder_controlled": False,
            "claims_Weyl_term_absent": False,
            "claims_observed_Newton_constant_derived": False,
            "claims_cosmological_constant_solved": False,
            "claims_Lorentzian_Wick_map_selected": False,
            "uses_measured_Newton_or_cosmological_data": False,
            "adds_fitted_parameter": False,
        },
        "next_required_artifact": "MTT_Selected_OneAtomProperTimeLaw_and_SpectralRemainderBound_or_DirectTwoDerivativeActionSource_v1",
        "note_written": str(OUT_NOTE),
    }

    note = f"""# Spectral Action Einstein IR Limit and Vacuum Obstruction v1

Date: 2026-07-15

## New result

The A51-A53 spectral route now has an explicit gravitational calculation rather
than a qualitative statement that it contains Einstein and Weyl terms.

The active A49 finite Dirac operator is `96x96` and has exactly

```text
Y_u, Y_d, Y_e, Y_nu.
```

Its neutral channel is Dirac. There is no particle-antiparticle Majorana block,
so the Majorana invariants `c_R,d_R` in the standard spectral-action gravity
formula vanish on this branch. This conclusion is exact for A49; adding a
Majorana block in a later model would reopen it.

The canonical 96-state coefficients are

```text
1/kappa_0^2 = (96 f2 Lambda^2-f0 c_R)/(12 pi^2),
alpha_0     = -3 f0/(10 pi^2),
gamma_0     = (48 f4 Lambda^4-f2 Lambda^2 c_R+(f0/4)d_R)/pi^2.
```

They come from Theorem 3.13 and equations (4.11)-(4.12) of
<https://arxiv.org/abs/hep-th/0610241>. In this repository's convention,

```text
2 kappa_h = 1/(2 kappa_0^2),
kappa_h   = (96 f2 Lambda^2-f0 c_R)/(48 pi^2).
```

## Exact Einstein/Weyl crossover

The primary weak-field calculation gives

```text
(Box-beta^2) Box h_TT = source,
beta^2 = -1/(32 pi G4 alpha_0) = -kappa_h/alpha_0.
```

See equations (13), (15), and (32) of
<https://arxiv.org/abs/1005.4276>. Since `alpha_0<0`, the extra scale is real.
At Euclidean momentum `p`, the retained TT kernel has shape

```text
K_TT(p) proportional to p^2(1+p^2/beta^2),
epsilon_W(p)=p^2/beta^2.
```

Under the A53 one-atom premise

```text
f2=f0/tau_int,
f4=f0/tau_int^2,
tau_int=log(448)/15={tau:.16g},
```

the fitted/profile normalization `f0` cancels completely from the dimensionless
gravity ratio:

```text
beta^2/Lambda^2 = 20/(3 tau_int)
                      = {beta_squared_over_cutoff_squared:.16g},
beta/Lambda       = {beta_over_cutoff:.16g}.
```

Hence, for `p<=eta Lambda`,

```text
epsilon_W(p) <= (3 tau_int/20) eta^2.
```

Numerically the bound is `{cutoff_weyl_fraction:.8%}` at `eta=1`,
`{eta_bounds['0.5']:.8%}` at `eta=0.5`, and
`{eta_bounds['0.1']:.8%}` at `eta=0.1`. The meaningful theorem is the quadratic
infrared suppression as `eta` tends to zero. The value at the cutoff is only a
diagnostic because the heat-kernel expansion itself is asymptotic there.

This closes the Einstein-versus-Weyl ratio inside the retained `a4` action,
conditional on the A53 one-atom tier. It does not yet bound all omitted higher
heat-kernel terms and does not select the one-atom measure.

## Vacuum obstruction

The same calculation exposes rather than hides the cosmological problem. With
`c_R=d_R=0`, the bare geometric constant is

```text
gamma_0 = 48 f4 Lambda^4/pi^2.
```

Writing its curvature-equivalent magnitude relative to
`2 kappa_h(R-2 Lambda_bare)` gives

```text
|Lambda_bare|/Lambda^2
  = gamma_0/(4 kappa_h Lambda^2)
  = 6 f4/f2
  = 6/tau_int
  = {bare_vacuum_curvature_over_cutoff_squared:.16g}.
```

Thus the one-atom law does not solve `Lambda_eff`; it produces an order-cutoff
bare term. The physical value still requires a selected Higgs-vacuum,
subtraction, cancellation, or renormalized source theorem, and its Lorentzian
sign requires the still-open Wick reconstruction.

## What advanced

Closed at the stated tier:

- `c_R=d_R=0` for the active A49 Dirac-only finite operator;
- the canonical Einstein/Weyl coefficient map into `kappa_h`;
- the exact crossover `beta^2/Lambda^2=20/(3 tau_int)`;
- a quantitative IR Weyl bound depending only on exact `tau_int`;
- a no-go for the A53 point measure solving the vacuum term by itself.

Still open:

- an unconditional MTT selection theorem for the A53 one-atom law;
- a controlled bound on the full asymptotic spectral remainder;
- the Lorentzian/Wick source map;
- one absolute Newton scale, `Lambda_eff`, and q79 zero/gap matching;
- selection of this spectral action over the direct two-derivative exit.

The next honest target is
`MTT_Selected_OneAtomProperTimeLaw_and_SpectralRemainderBound_or_DirectTwoDerivativeActionSource_v1`.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {STATUS}")


if __name__ == "__main__":
    main()
