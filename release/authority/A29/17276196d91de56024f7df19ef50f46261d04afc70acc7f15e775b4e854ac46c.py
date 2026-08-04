"""Build the neutral relative-amplitude orbit successor after finite channels."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralactioncostprefactorordiracmajoranacompletion"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "neutral_second_order_relative_amplitude_orbit.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralActionCostPrefactorOrDiracMajoranaCompletion_v1.md"
STATUS = "MTT_SELECTED_NEUTRAL_RELATIVE_AMPLITUDE_ORBIT_CLOSED_ABSOLUTE_ACTION_SCALE_OPEN"
NEXT = "MTT_Selected_NeutralAbsoluteAmplitudeNilAnchorOrDiracMajoranaCompletion_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    predecessor = load(
        ROOT / "candidate_data" / "selected_neutralfinitegammarowsoractioncostsource"
        / "neutral_finite_gamma_channel_rows.packet.json"
    )
    orbit = load(
        ROOT / "candidate_data" / "selected_lambdaorbitsecondordermatrixpacket_or_rthetascalarexecution"
        / "lambda_orbit_second_order_matrix_packet.packet.json"
    )
    orbit_cert = load(ROOT / "certificates" / "selected_lambdaorbitsecondordermatrixpacket_or_rthetascalarexecution_certificate.json")

    expected_shift = {
        "1+omega": [1.5, math.sqrt(3.0) / 2.0],
        "1+omega2": [1.5, -math.sqrt(3.0) / 2.0],
    }
    branches = []
    for source in orbit["matrix_branches"]:
        label = source["lambda_static"]
        coefficient = expected_shift[label]
        matrix = source["d_nuD_matrix"]
        expected = [
            [1.0, coefficient, 0.0],
            [0.0, 1.0, coefficient],
            [coefficient, 0.0, 1.0],
        ]
        branches.append(
            {
                "branch_id": source["branch_id"],
                "lambda_static": label,
                "Gamma_nu_relative_formula": source["d_nuD_matrix_formula"],
                "Gamma_nu_relative_matrix": matrix,
                "exact_matrix_match": matrix == expected,
                "diagonal_coefficient": 1.0,
                "cyclic_shift_coefficient_exact": "3/2+i*sqrt(3)/2" if coefficient[1] > 0 else "3/2-i*sqrt(3)/2",
                "cyclic_shift_coefficient_numeric": coefficient,
                "cyclic_shift_magnitude_exact": "sqrt(3)",
                "cyclic_shift_phase": "+pi/6" if coefficient[1] > 0 else "-pi/6",
                "hermitian_spectrum": source["hermitian_spectrum_each_sector"],
                "selected_as_orbit_representative": True,
                "selected_as_unique_representative": False,
            }
        )

    source_gate = all(
        [
            predecessor["what_closes_here"]["finite_Gamma_nu_ij_channel_sets"],
            orbit["orbit_matrix_packet_selected"],
            orbit["closure_claimed"],
            orbit_cert["selected_second_order_orbit_matrix_packet_closed"],
            orbit_cert["theorem_proved"],
            len(branches) == 2,
            all(row["exact_matrix_match"] for row in branches),
            {row["lambda_static"] for row in branches} == {"1+omega", "1+omega2"},
        ]
    )

    packet = {
        "schema": "MTTSelectedNeutralActionCostPrefactorOrDiracMajoranaCompletion.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralFiniteGammaRowsOrActionCostSource_v1",
        "theorem": {
            "name": "SelectedNeutralSecondOrderRelativeAmplitudeOrbitTheorem",
            "proved": source_gate,
            "statement": "The selected lambda orbit and second-order Weyl packet restrict the dimensionless neutral Dirac response to two conjugate representatives. In either representative the diagonal coefficient is 1 and each active cyclic-shift coefficient is 3/2 plus or minus i sqrt(3)/2, with magnitude sqrt(3), phase plus or minus pi/6, and Hermitian spectrum {1,4,7}. The orbit is selected without observed flavor data; no individual representative or absolute physical scale is selected.",
        },
        "selected_relative_amplitude_orbit": branches,
        "orbit_representative_count": len(branches),
        "relative_value_rows_per_representative": 9,
        "relative_value_rows_closed": 18 if source_gate else 0,
        "orbit_invariants": {
            "diagonal_coefficient": 1.0,
            "active_shift_magnitude_exact": "sqrt(3)",
            "active_shift_phase_orbit": ["+pi/6", "-pi/6"],
            "hermitian_spectrum": [1.0, 4.0, 7.0],
            "first_response_twofold_family_degeneracy_removed": True,
            "conjugate_orbit_coexists_at_current_invariant_layer": True,
        },
        "what_closes_here": {
            "selected_second_order_neutral_relative_amplitude_orbit": source_gate,
            "nine_relative_coefficients_per_orbit_representative": source_gate,
            "relative_magnitude_and_phase_orbit": source_gate,
            "individual_orbit_representative": False,
            "neutral_action_cost_rows_S_gamma": False,
            "absolute_prefactors_A_gamma": False,
            "unique_retarded_sign_row": False,
            "Dirac_only_action_completeness": False,
            "physical_Gamma_nu_amplitudes": False,
        },
        "neutral_overlap_OK_gate_acceptance": predecessor["neutral_overlap_OK_gate_acceptance"],
        "neutral_overlap_OK_gates_closed": predecessor["neutral_overlap_OK_gates_closed"],
        "neutral_overlap_OK_gates_total": predecessor["neutral_overlap_OK_gates_total"],
        "readiness_subfields": predecessor["readiness_subfields"],
        "readiness_subfields_closed": predecessor["readiness_subfields_closed"],
        "readiness_subfields_total": predecessor["readiness_subfields_total"],
        "new_relative_dimensionless_value_rows_closed_here": 18,
        "new_absolute_value_fields_closed_here": 0,
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
        "remaining_value_blockers": [
            "source-selected absolute action weight/prefactor and same-scheme physical unit",
            "theorem selecting one conjugate representative or proving both are physically equivalent/coexisting",
            "Dirac-only action completeness or selected Majorana M_L/M_R rows",
            "nil-anchor/coherence projector and RG/threshold transport for absolute neutrino observables",
        ],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralActionCostPrefactorOrDiracMajoranaCompletion_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": source_gate,
        "selected_second_order_neutral_relative_amplitude_orbit_closed": source_gate,
        "orbit_representative_count": 2,
        "relative_value_rows_closed": packet["relative_value_rows_closed"],
        "diagonal_coefficient": 1.0,
        "active_shift_magnitude_exact": "sqrt(3)",
        "active_shift_phase_orbit": ["+pi/6", "-pi/6"],
        "individual_orbit_representative_selected": False,
        "neutral_action_cost_rows_S_gamma_closed": False,
        "absolute_prefactors_A_gamma_closed": False,
        "unique_retarded_sign_row_closed": False,
        "Dirac_only_action_completeness_closed": False,
        "neutral_overlap_OK_gates_closed": packet["neutral_overlap_OK_gates_closed"],
        "neutral_overlap_OK_gates_total": packet["neutral_overlap_OK_gates_total"],
        "readiness_subfields_closed": packet["readiness_subfields_closed"],
        "readiness_subfields_total": packet["readiness_subfields_total"],
        "new_absolute_value_fields_closed_here": 0,
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

    note = f"""# MTT Selected Neutral Action Cost, Prefactor, or Dirac-Majorana Completion v1

## Result

The selected second-order lambda-orbit packet supplies exact relative neutral
Dirac coefficients beyond the A28 channel multiplicities. The two selected
conjugate representatives are

```text
Gamma_nu^rel(+) = I3 + (3/2 + i sqrt(3)/2) X3,
Gamma_nu^rel(-) = I3 + (3/2 - i sqrt(3)/2) X3.
```

Thus every diagonal coefficient is `1`; every active cyclic-shift coefficient
has magnitude `sqrt(3)` and phase `+pi/6` or `-pi/6`. Each representative has
Hermitian spectrum `[1,4,7]`. The two representatives form the already selected
conjugate orbit and coexist at the current invariant layer. No observed
neutrino or flavor datum selects either branch.

## Boundary

This closes relative dimensionless values, not `OK6`. The source-selected
absolute action weight/prefactor, physical unit, and a theorem selecting one
conjugate representative (or proving physical equivalence/coexistence) remain
open. Dirac-only completeness and Majorana `M_L/M_R` rows also remain open.
Neutral gates therefore remain `{packet['neutral_overlap_OK_gates_closed']}/{packet['neutral_overlap_OK_gates_total']}`
and readiness remains `{packet['readiness_subfields_closed']}/{packet['readiness_subfields_total']}`.

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
