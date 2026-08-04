"""Build the neutral radial second-variation and VEV-coordinate theorem."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralradialsecondvariationandvevcoordinatetheorem"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "neutral_radial_second_variation_and_vev_coordinate.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralRadialSecondVariationAndVEVCoordinateTheorem_v1.md"
STATUS = "MTT_SELECTED_NEUTRAL_RADIAL_SECOND_VARIATION_CLOSED_HIGGS_INSERTION_NORMALIZATION_OPEN"
NEXT = "MTT_Selected_NeutralHiggsInsertionFunctorAndRadialCoordinateNormalization_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def clean(values: np.ndarray, tol: float = 1e-13) -> list[float]:
    return [0.0 if abs(float(value)) < tol else float(value) for value in values]


def splitting_ratio(y0: np.ndarray, dy: np.ndarray, h: float) -> tuple[list[float], float]:
    gram = (y0 + h * dy) @ (y0 + h * dy).T
    eigenvalues = np.linalg.eigvalsh(gram)
    gaps = np.diff(eigenvalues)
    ratio = float(min(gaps) / (eigenvalues[-1] - eigenvalues[0]))
    return clean(eigenvalues), ratio


def main() -> int:
    prior = load(
        ROOT / "candidate_data" / "selected_protospinoralignmenttodiracmassreadout"
        / "protospinor_finite_dirac_and_alignment_readout.packet.json"
    )
    h_source = load(
        ROOT / "candidate_data" / "selected_hscalarfunctionalonfiniteprojectedhymalgebra_or_halfdensitysourcerule"
        / "tauh_rh_source_value_execution.packet.json"
    )
    h_transport = load(
        ROOT / "candidate_data" / "selected_hlambdathresholdpayload_from_finitehscalarsource_or_fullsmclosureaudit.candidate.json"
    )
    profile = load(
        ROOT / "candidate_data" / "selected_commonscaleyukawahiggstransport_or_finalreplayaudit"
        / "yukawa_higgs_common_scale_transport_kernel.packet.json"
    )

    response = load(
        ROOT / "candidate_data" / "selected_neutralabsoluteamplitudenilanchorordiracmajoranacompletion"
        / "neutral_internal_dimensionless_response.packet.json"
    )["neutral_internal_response"]
    a = float(response["a_internal"])
    y0 = np.asarray(response["baseline_Y0"], dtype=float)
    dy = np.asarray(response["correction_dY"], dtype=float)
    h2_coefficient = dy @ dy.T
    gram_second_variation = 2.0 * h2_coefficient
    h2_eigenvalues = clean(np.linalg.eigvalsh(h2_coefficient))
    second_variation_eigenvalues = clean(np.linalg.eigvalsh(gram_second_variation))
    tau_h = float(h_source["source_values"]["tau_H_A_N"])
    r_h = float(h_source["source_values"]["r_H_A_N"])
    v_profile = float(profile["native_values_to_transport"]["higgs_tree"]["v_GeV"])
    postcheck = float(prior["coefficient_matched_alignment_trial"]["postcheck_ratio"])

    coordinates = {
        "a_internal_coefficient_match": a,
        "tau_H_direct": tau_h,
        "r_H_direct": r_h,
        "sqrt_r_H": math.sqrt(r_h),
        "tau_H_squared": tau_h**2,
        "tau_H_squared_minus_two_a": tau_h**2 - 2.0 * a,
    }
    trials = {}
    for name, coordinate in coordinates.items():
        spectrum, ratio = splitting_ratio(y0, dy, coordinate)
        trials[name] = {
            "coordinate": coordinate,
            "Gram_eigenvalues": spectrum,
            "splitting_ratio": ratio,
            "absolute_postcheck_residual": abs(ratio - postcheck),
            "selected_as_neutral_radial_coordinate": False,
            "accepted_as_prediction": False,
        }
    closest_name = min(trials, key=lambda key: trials[key]["absolute_postcheck_residual"])

    checks = {
        "finite_Dirac_predecessor_closed": prior["theorem"]["proved"],
        "H_scalar_source_row_selected": h_source["accepted_H_scalar_source_rows"] == 1,
        "strict_tau_H_promoted": h_source["strict_tau_H_promoted"],
        "strict_r_H_promoted": h_source["strict_r_H_promoted"],
        "H_radial_transport_selected": h_transport["closure_decision"]["selected_H_radial_source_row_emitted"],
        "Gram_second_variation_positive_semidefinite": min(second_variation_eigenvalues) >= 0.0,
        "Gram_second_variation_rank_three": int(np.linalg.matrix_rank(gram_second_variation)) == 3,
        "direct_tau_H_identity_insertion_rejected": trials["tau_H_direct"]["absolute_postcheck_residual"] > 0.05,
        "direct_r_H_identity_insertion_rejected": trials["r_H_direct"]["absolute_postcheck_residual"] > 0.02,
        "no_tested_coordinate_exact": all(row["absolute_postcheck_residual"] > 1e-6 for row in trials.values()),
    }
    checks = {key: bool(value) for key, value in checks.items()}
    theorem_proved = all(checks.values())

    packet = {
        "schema": "MTTSelectedNeutralRadialSecondVariationAndVEVCoordinateTheorem.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_ProtoSpinorAlignmentToDiracMassReadout_v1",
        "theorem": {
            "name": "NeutralRadialSecondVariationTypingAndVEVCoordinateNoShortcutTheorem",
            "proved": theorem_proved,
            "statement": "For the selected formal Gram family G(h)=(Y0+h dY)(Y0+h dY)^dagger, the exact second variation is G''(h)=2 dY dY^dagger with positive spectrum {2,2,8}. The H sector independently emits selected tau_H and r_H radial source values, and the profile-standard electroweak VEV is a shared baseline rather than a neutrino-specific parameter. However, no current theorem types dY as the derivative with respect to that H radial coordinate, and direct identity substitutions of tau_H or r_H fail the downstream hierarchy postcheck. Therefore the positive second variation is closed algebraically, while the H-to-neutral insertion functor and radial-coordinate normalization remain open.",
        },
        "source_checks": checks,
        "radial_second_variation": {
            "formal_Gram_family": "G(h)=(Y0+h*dY)(Y0+h*dY)^dagger",
            "quadratic_coefficient_H2": h2_coefficient.tolist(),
            "H2_eigenvalues": h2_eigenvalues,
            "second_variation_formula": "d^2G/dh^2=2*dY*dY^dagger",
            "second_variation_matrix": gram_second_variation.tolist(),
            "second_variation_eigenvalues": second_variation_eigenvalues,
            "positive_semidefinite": True,
            "positive_definite": min(second_variation_eigenvalues) > 0.0,
            "rank": int(np.linalg.matrix_rank(gram_second_variation)),
            "exact_algebraic_second_variation_closed": theorem_proved,
            "typed_as_physical_neutral_mass_Hessian": False,
            "reason_not_physical_yet": "dY is selected as a neutral shift/C1 response direction, but no source theorem identifies it with differentiation by the selected H radial coordinate",
        },
        "selected_H_sector_radial_source": {
            "tau_H_A_N": tau_h,
            "r_H_A_N": r_h,
            "strict_tau_H_promoted": h_source["strict_tau_H_promoted"],
            "strict_r_H_promoted": h_source["strict_r_H_promoted"],
            "selected_H_radial_source_row_emitted": h_transport["closure_decision"]["selected_H_radial_source_row_emitted"],
            "H_to_neutral_insertion_map_emitted": False,
            "identity_insertion_tau_H_accepted": False,
            "identity_insertion_r_H_accepted": False,
        },
        "coordinate_trials": {
            "postcheck_role": "downstream falsification only; not a selector",
            "postcheck_ratio": postcheck,
            "trials": trials,
            "closest_tested_candidate": closest_name,
            "closest_tested_residual": trials[closest_name]["absolute_postcheck_residual"],
            "any_exact_selected_coordinate": False,
            "target_inverted_coordinate_not_computed_or_promoted": True,
        },
        "VEV_policy": {
            "profile_standard_v_GeV": v_profile,
            "profile_source": "v from measured G_F in frozen SM-equivalence reference/profile data",
            "role": "shared electroweak alignment baseline used after dimensionless Y_nu is selected",
            "counts_as_neutrino_specific_parameter": False,
            "allowed_at_adopted_one_shared_physical_primitive_profile_standard": True,
            "selected_by_strict_no_knob_MTT_source": False,
            "can_select_neutral_shape_or_hierarchy": False,
            "mass_formula_after_shape_selection": "M_D=v_profile*Y_nu/sqrt(2) under the declared SM convention",
        },
        "missing_Higgs_insertion_functor": {
            "domain": "selected finite H scalar/radial source on A_N",
            "codomain": "neutral mixed L x N^c Yukawa response",
            "required_map": "iota_Hnu: h_H -> h_nu with d/dh_H Y_nu = (dh_nu/dh_H)*dY",
            "required_normalization": "source-selected dh_nu/dh_H and alignment point h_H=v_align",
            "required_checks": [
                "same selected H_u carrier and source branch",
                "gauge-flat lens quotient invariance",
                "circle/lens/nil compatibility",
                "positive anchored Hessian after insertion",
                "no neutrino measurements used to select the map",
            ],
            "emitted": False,
        },
        "what_closes_here": {
            "exact_positive_Gram_second_variation": theorem_proved,
            "selected_H_radial_source_inventory": theorem_proved,
            "direct_H_radial_identity_insertion_no_go": theorem_proved,
            "VEV_as_shared_profile_baseline_policy": theorem_proved,
            "selected_H_to_neutral_insertion_functor": False,
            "selected_radial_coordinate_normalization": False,
            "physical_neutral_mass_Hessian": False,
            "dimensionless_Y_nu_physical_readout": False,
            "dimensionful_M_D": False,
        },
        "neutral_overlap_OK_gates_closed": prior["neutral_overlap_OK_gates_closed"],
        "neutral_overlap_OK_gates_total": prior["neutral_overlap_OK_gates_total"],
        "readiness_subfields_closed": prior["readiness_subfields_closed"],
        "readiness_subfields_total": prior["readiness_subfields_total"],
        "new_physical_value_fields_closed_here": 0,
        "selected_neutral_operator_accepted": False,
        "U5_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralRadialSecondVariationAndVEVCoordinateTheorem_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "second_variation_eigenvalues": second_variation_eigenvalues,
        "positive_second_variation_closed": theorem_proved,
        "typed_as_physical_neutral_mass_Hessian": False,
        "selected_tau_H": tau_h,
        "selected_r_H": r_h,
        "direct_H_radial_identity_insertion_rejected": theorem_proved,
        "closest_tested_coordinate": closest_name,
        "closest_tested_residual": trials[closest_name]["absolute_postcheck_residual"],
        "profile_v_GeV": v_profile,
        "VEV_counts_as_neutrino_specific_parameter": False,
        "strict_no_knob_VEV_source_closed": False,
        "selected_H_to_neutral_insertion_functor_closed": False,
        "dimensionful_M_D_closed": False,
        "new_physical_value_fields_closed_here": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Neutral Radial Second Variation and VEV Coordinate Theorem v1

## Positive second variation

For the selected formal neutral Gram family

```text
G(h)=(Y0+h*dY)(Y0+h*dY)^dagger,
G''(h)=2*dY*dY^dagger,
```

the exact second-variation spectrum is `{second_variation_eigenvalues}`. It is
positive definite. This closes the algebraic second variation, but not its
identification as the physical neutral mass Hessian: `dY` is a selected neutral
shift/C1 direction, not yet a theorem-derived derivative with respect to the H
radial coordinate.

## H radial source and VEV

The finite H scalar source independently emits
`tau_H={tau_h}` and `r_H={r_h}`. Directly substituting either as the neutral
coordinate fails the hierarchy postcheck. The tested source-motivated
coordinates are recorded in the packet; none is promoted by residual fitting.

At the adopted profile standard, `v={v_profile} GeV` is the shared electroweak
alignment baseline obtained from the frozen `G_F` reference. It is not a new
neutrino-specific parameter and cannot select the neutral hierarchy. Strict
no-knob derivation of the physical VEV remains a stronger program.

## Exact frontier

The remaining object is the typed insertion

```text
iota_Hnu: h_H -> h_nu,
dY_nu/dh_H = (dh_nu/dh_H)*dY,
```

including its source-selected normalization and alignment point. Next artifact:
`{NEXT}`.
"""

    dump(PACKET, packet)
    dump(CANDIDATE, packet)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
