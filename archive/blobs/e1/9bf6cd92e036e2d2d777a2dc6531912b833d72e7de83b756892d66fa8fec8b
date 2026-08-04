"""Build the neutral physical-unit / nil-anchor invariant obstruction."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralphysicalunitornilanchorprojector"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "neutral_scale_invariant_obstruction_and_spectral_repair.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralPhysicalUnitOrNilAnchorProjector_v1.md"
STATUS = "MTT_SELECTED_NEUTRAL_COMMON_SCALE_ROUTE_REJECTED_SPECTRAL_ACTION_OR_SEESAW_REQUIRED"
NEXT = "MTT_Selected_NeutralSpectralActionSlopeOrSeesawSource_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    internal = load(
        ROOT / "candidate_data" / "selected_neutralabsoluteamplitudenilanchorordiracmajoranacompletion"
        / "neutral_internal_dimensionless_response.packet.json"
    )
    relative = load(
        ROOT / "candidate_data" / "selected_neutralactioncostprefactorordiracmajoranacompletion"
        / "neutral_second_order_relative_amplitude_orbit.packet.json"
    )
    nil_packet = load(
        ROOT / "candidate_data" / "selected_neutralnilboundarymassfunctional"
        / "neutral_nil_boundary_mass_functional.packet.json"
    )

    spectrum = relative["orbit_invariants"]["hermitian_spectrum"]
    shifted = [value - min(spectrum) for value in spectrum]
    direct_ratio = shifted[1] / shifted[2]
    no_masses = nil_packet["ordering_candidates_postcheck_only"]["normal_ordering"]["masses_eV"]
    postcheck_ratio = no_masses[1] ** 2 / no_masses[2] ** 2
    beta = math.log(1.0 / postcheck_ratio - 1.0) / 3.0
    c_eV2 = no_masses[2] ** 2 / (math.exp(6.0 * beta) - 1.0)
    reconstructed_ratio = (math.exp(3.0 * beta) - 1.0) / (math.exp(6.0 * beta) - 1.0)

    gate = all(
        [
            internal["theorem"]["proved"],
            relative["theorem"]["proved"],
            nil_packet["minimal_trace_mass_functional"]["mathematical_theorem_proved"],
            spectrum == [1.0, 4.0, 7.0],
            shifted == [0.0, 3.0, 6.0],
            abs(direct_ratio - 0.5) < 1e-15,
            abs(postcheck_ratio - direct_ratio) > 0.4,
            abs(reconstructed_ratio - postcheck_ratio) < 1e-15,
        ]
    )

    packet = {
        "schema": "MTTSelectedNeutralPhysicalUnitOrNilAnchorProjector.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralAbsoluteAmplitudeNilAnchorOrDiracMajoranaCompletion_v1",
        "theorem": {
            "name": "NeutralCommonScaleAndNilShiftNoGoTheorem",
            "proved": gate,
            "statement": "For the selected second-order neutral orbit with Hermitian spectrum {1,4,7}, any common physical-unit or prefactor multiplication preserves all eigenvalue ratios. Nil-boundary subtraction of the minimum gives {0,3,6} and therefore the scale-invariant splitting ratio 1/2. The repository's normal-ordering oscillation postcheck ratio is about 0.029805, so neither a physical unit nor nil anchoring alone can turn the selected internal operator into the physical neutrino mass spectrum. A non-affine selected spectral action/channel weight or a selected Majorana/seesaw block is necessary.",
        },
        "scale_invariant_obstruction": {
            "selected_internal_hermitian_spectrum": spectrum,
            "nil_shifted_spectrum": shifted,
            "direct_nil_shift_ratio": direct_ratio,
            "normal_ordering_postcheck_ratio": postcheck_ratio,
            "ratio_mismatch": abs(direct_ratio - postcheck_ratio),
            "common_rescaling_changes_ratio": False,
            "nil_shift_alone_matches_postcheck": False,
            "simple_M_D_equals_common_scale_times_selected_orbit_rejected": gate,
            "postcheck_values_used_as_selector": False,
        },
        "minimal_nonlinear_repair_contract": {
            "family": "m_k^2 = C * (exp(beta*(lambda_k-lambda_min)) - 1)",
            "selected_internal_lambda": spectrum,
            "nil_anchor_automatic": True,
            "free_dimensionless_shape_parameters": 1,
            "free_dimensionful_scale_parameters": 1,
            "ratio_formula": "r=1/(exp(3*beta)+1)",
            "beta_diagnostic_from_postcheck_not_selected": beta,
            "C_eV2_diagnostic_from_postcheck_not_selected": c_eV2,
            "reconstructed_ratio_diagnostic": reconstructed_ratio,
            "exact_source_beta_emitted": False,
            "physical_scale_C_emitted": False,
            "accepted_as_prediction": False,
            "purpose": "prove that one selected action slope plus one universal scale is algebraically sufficient; the diagnostic values are not source inputs",
        },
        "route_reduction": {
            "retired": [
                "identify the A29/A30 internal operator directly with Y_nu and attach only v_u or one common physical unit",
                "apply only the nil-boundary offset to the selected {1,4,7} spectrum",
            ],
            "surviving": [
                "derive a non-affine neutral spectral/action functional from selected S_gamma/A_gamma rows",
                "emit a selected Majorana/seesaw M_R or M_L block that changes the light spectrum",
                "derive a different same-source neutral reconstruction operator before physical-unit attachment",
            ],
        },
        "what_closes_here": {
            "common_scale_invariance_theorem": gate,
            "nil_shifted_selected_orbit_ratio": gate,
            "simple_scale_only_physical_route_rejected": gate,
            "minimal_two_parameter_spectral_repair_contract": gate,
            "selected_spectral_action_slope_beta": False,
            "selected_physical_scale_C": False,
            "nil_boundary_source_promotion": False,
            "Dirac_only_action_completeness": False,
            "selected_Majorana_seesaw_blocks": False,
        },
        "neutral_overlap_OK_gate_acceptance": internal["neutral_overlap_OK_gate_acceptance"],
        "neutral_overlap_OK_gates_closed": internal["neutral_overlap_OK_gates_closed"],
        "neutral_overlap_OK_gates_total": internal["neutral_overlap_OK_gates_total"],
        "readiness_subfields_closed": internal["readiness_subfields_closed"],
        "readiness_subfields_total": internal["readiness_subfields_total"],
        "new_physical_value_fields_closed_here": 0,
        "accepted_route_exit_count": 0,
        "route_exit_count": 3,
        "dimensionful_M_D_3x3_closed": False,
        "dimensionful_M_L_3x3_closed": False,
        "dimensionful_M_R_3x3_closed": False,
        "absolute_normalization_and_scheme_closed": False,
        "selected_neutral_operator_accepted": False,
        "U5_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralPhysicalUnitOrNilAnchorProjector_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": gate,
        "simple_common_scale_route_rejected": gate,
        "selected_orbit_spectrum": spectrum,
        "nil_shifted_spectrum": shifted,
        "direct_nil_shift_ratio": direct_ratio,
        "normal_ordering_postcheck_ratio": postcheck_ratio,
        "minimal_spectral_shape_parameter_count": 1,
        "minimal_physical_scale_parameter_count": 1,
        "beta_diagnostic_not_selected": beta,
        "selected_beta_closed": False,
        "physical_scale_C_closed": False,
        "physical_unit_selected": False,
        "nil_anchor_projector_closed": False,
        "Dirac_only_action_completeness_closed": False,
        "neutral_overlap_OK_gates_closed": packet["neutral_overlap_OK_gates_closed"],
        "neutral_overlap_OK_gates_total": packet["neutral_overlap_OK_gates_total"],
        "readiness_subfields_closed": packet["readiness_subfields_closed"],
        "readiness_subfields_total": packet["readiness_subfields_total"],
        "new_physical_value_fields_closed_here": 0,
        "accepted_route_exit_count": 0,
        "route_exit_count": 3,
        "dimensionful_M_D_3x3_closed": False,
        "dimensionful_M_L_3x3_closed": False,
        "dimensionful_M_R_3x3_closed": False,
        "absolute_normalization_and_scheme_closed": False,
        "selected_neutral_operator_accepted": False,
        "U5_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Neutral Physical Unit or Nil Anchor Projector v1

## Result

The selected A29 orbit has Hermitian spectrum `[1,4,7]`. A common physical
unit or prefactor cannot change eigenvalue ratios. Nil subtraction gives
`[0,3,6]`, hence

```text
r_direct = 3/6 = {direct_ratio}.
```

The normal-ordering oscillation postcheck already stored in the neutral packet
gives `r_post = {postcheck_ratio}`. It is used only as a downstream falsification
check. Therefore attaching `v_u`, `Omega0`, or any other common scale, even
together with nil subtraction, cannot make the selected internal orbit the
physical neutrino mass spectrum.

## Minimal surviving repair

One economical non-affine family is

```text
m_k^2 = C * (exp(beta*(lambda_k-lambda_min)) - 1),
r = 1/(exp(3 beta)+1).
```

For orientation only, replaying the postcheck gives `beta={beta}` and
`C={c_eV2} eV^2`. These are diagnostic values, not selected source rows. The
important theorem is the parameter count: one dimensionless action slope and
one universal physical scale are algebraically sufficient, whereas one common
scale alone is impossible.

Next artifact: `{NEXT}`.
"""

    dump(PACKET, packet)
    dump(CANDIDATE, packet)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
