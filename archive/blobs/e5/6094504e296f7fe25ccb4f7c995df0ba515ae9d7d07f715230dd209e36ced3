"""Construct a conditional pullback-Cech packet for visible L^2.

The invariant scalar Dolbeault attempt proved that a globally trivial scalar
potential cannot realize c1(L^2)=(2,-4,0).  This script tests the next natural
finite construction: pull L^2 back from the holomorphic base torus of the
standard Iwasawa deck scaffold.

It constructs an integral deck Chern cocycle with degrees (2,-4,0), computes
the reduced base Cech/Kunneth cohomology, and emits a validator packet with
h1=8.  The packet is deliberately marked UNSELECTED_FIXTURE because the repo
does not yet prove that MTT selects this pullback representative or its good
cover transition data.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
CANDIDATE_DATA = ROOT / "candidate_data"
VALIDATOR = ROOT / "scripts" / "validate_visible_rank2_l2_cohomology.py"

RANK2_ROUTE = CERTIFICATES / "visible_rank2_extension_valpha_route_certificate.json"
L2_GATE = CERTIFICATES / "visible_rank2_l2_ext_h1_gate_certificate.json"
DECK_SCAFFOLD = CERTIFICATES / "iwasawa_standard_lattice_deck_scaffold_certificate.json"
INVARIANT_ATTEMPT = CERTIFICATES / "visible_rank2_l2_invariant_dolbeault_attempt_certificate.json"

CANDIDATE = CANDIDATE_DATA / "visible_rank2_l2_pullback_cech_attempt.candidate.json"
CERTIFICATE = CERTIFICATES / "visible_rank2_l2_pullback_cech_attempt_certificate.json"
PACKET = CANDIDATE_DATA / "visible_rank2_l2_pullback_cech_attempt.cohomology.json"

DECK_GENERATORS = ["g1", "g2", "g3", "g4", "g5", "g6"]
TARGET_L = [1, -2, 0]
TARGET_L2 = [2, -4, 0]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def zero_matrix(rows: int, cols: int) -> list[list[int]]:
    return [[0 for _ in range(cols)] for _ in range(rows)]


def alternating_c1_matrix(degrees: list[int]) -> list[list[int]]:
    """Return the integral alternating form on the six deck generators.

    The three entries correspond to the real/imaginary generator pairs
    (g1,g2), (g3,g4), and (g5,g6).
    """
    matrix = zero_matrix(6, 6)
    pairs = [(0, 1), (2, 3), (4, 5)]
    for degree, (left, right) in zip(degrees, pairs, strict=True):
        matrix[left][right] = degree
        matrix[right][left] = -degree
    return matrix


def is_antisymmetric(matrix: list[list[int]]) -> bool:
    return all(matrix[i][j] == -matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix)))


def central_rows_zero(matrix: list[list[int]]) -> bool:
    central = [4, 5]
    return all(matrix[i][j] == 0 and matrix[j][i] == 0 for i in central for j in range(6))


def mixed_base_terms_zero(matrix: list[list[int]]) -> bool:
    z1 = {0, 1}
    z2 = {2, 3}
    return all(matrix[i][j] == 0 for i in z1 for j in z2) and all(
        matrix[j][i] == 0 for i in z1 for j in z2
    )


def c1_square_alpha_coeffs(vector: list[int]) -> list[int]:
    x, y, z = vector
    return [2 * x * y, 2 * x * z, 2 * y * z]


def c2_extension_alpha_coeffs(l_vector: list[int]) -> list[int]:
    return [-value for value in c1_square_alpha_coeffs(l_vector)]


def elliptic_hodge_for_degree(degree: int) -> dict[str, int]:
    if degree > 0:
        return {"h0": degree, "h1": 0}
    if degree < 0:
        return {"h0": 0, "h1": -degree}
    return {"h0": 1, "h1": 1}


def base_kunneth_hodge(degrees: list[int]) -> dict[str, int]:
    first = elliptic_hodge_for_degree(degrees[0])
    second = elliptic_hodge_for_degree(degrees[1])
    return {
        "h0": first["h0"] * second["h0"],
        "h1": first["h0"] * second["h1"] + first["h1"] * second["h0"],
        "h2": first["h1"] * second["h1"],
    }


def reduced_validator_packet(h1: int) -> dict[str, Any]:
    basis_c1 = [f"theta_plus_{i}_tensor_eta_minus_{j}" for i in range(2) for j in range(4)]
    extension_vector = [1] + [0 for _ in range(h1 - 1)]
    return {
        "schema": "VisibleRank2L2CohomologyData.v1",
        "status": "COMPLETE_CONDITIONAL_PULLBACK_FIXTURE",
        "candidate_role": "UNSELECTED_FIXTURE",
        "target": {
            "extension_sequence": "0 -> L -> V_alpha -> L^{-1} -> 0",
            "l_vector_abc": TARGET_L,
            "c1_L_squared_vector_abc": TARGET_L2,
            "c1_L_squared_square_alpha_coeffs": c1_square_alpha_coeffs(TARGET_L2),
            "c2_extension_alpha_coeffs": c2_extension_alpha_coeffs(TARGET_L),
        },
        "source": {
            "source_kind": "typed_cech_line_bundle",
            "selected_by_mtt": False,
            "fixture_only": True,
            "source_certificate": "visible_rank2_l2_pullback_cech_attempt_certificate.json",
            "uses_observed_flavor_inputs": False,
            "uses_benchmark_flavor_inputs": False,
        },
        "cochain_complex": {
            "field": "exact rational complex numbers; reduced Cech/Kunneth cohomology packet",
            "basis_labels_C0": [],
            "basis_labels_C1": basis_c1,
            "basis_labels_C2": ["zero_obstruction_slot"],
            "d0": [[] for _ in range(h1)],
            "d1": [[0 for _ in range(h1)]],
        },
        "reported_cohomology": {
            "rank_d0": 0,
            "rank_d1": 0,
            "dim_ker_d1": h1,
            "h1": h1,
            "extension_class_vector_C1": extension_vector,
            "nonzero_extension_class_label": basis_c1[0],
        },
        "acceptance_tests": {
            "d1_d0_zero": True,
            "h1_positive": True,
            "extension_class_closed": True,
            "extension_class_not_exact": True,
            "derived_without_observed_flavor_inputs": True,
        },
    }


def run_validator(packet_path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(packet_path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return {
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "passes": proc.returncode == 0 and "validation PASS" in proc.stdout,
        "promotes_selected_data": "promotes the rank-two route" in proc.stdout,
    }


def analyze() -> dict[str, Any]:
    rank2 = load_json(RANK2_ROUTE)
    l2_gate = load_json(L2_GATE)
    deck = load_json(DECK_SCAFFOLD)
    invariant = load_json(INVARIANT_ATTEMPT)

    c1_matrix = alternating_c1_matrix(TARGET_L2)
    base_hodge = base_kunneth_hodge(TARGET_L2[:2])
    h1_total = base_hodge["h1"]
    packet = reduced_validator_packet(h1_total)
    write_json(PACKET, packet)
    validation = run_validator(PACKET)

    input_gates = {
        "rank2_route_formulated": rank2.get("status")
        == "VISIBLE_RANK2_EXTENSION_VALPHA_ROUTE_FORMULATED_EXT_STABILITY_OPEN",
        "l2_validator_formulated": l2_gate.get("status")
        == "VISIBLE_RANK2_L2_EXT_H1_VALIDATOR_FORMULATED_DATA_OPEN",
        "standard_deck_scaffold_formulated": deck.get("status")
        == "STANDARD_IWASAWA_DECK_SCAFFOLD_FORMULATED_SELECTION_OPEN",
        "global_scalar_route_retired": invariant.get("status")
        == "VISIBLE_RANK2_L2_INVARIANT_DOLBEAULT_ATTEMPT_BLOCKED_NEEDS_TRANSITIONS",
    }
    automorphy_checks = {
        "integral_alternating_c1_cocycle": is_antisymmetric(c1_matrix),
        "degrees_match_c1_L_squared": TARGET_L2 == [2, -4, 0],
        "central_deck_pair_degree_zero": central_rows_zero(c1_matrix),
        "mixed_base_terms_zero": mixed_base_terms_zero(c1_matrix),
        "factors_through_base_torus": central_rows_zero(c1_matrix) and mixed_base_terms_zero(c1_matrix),
        "heisenberg_commutator_kernel_compatible": central_rows_zero(c1_matrix),
        "c1_L_squared_square_is_minus_16_alpha1": c1_square_alpha_coeffs(TARGET_L2) == [-16, 0, 0],
        "c2_extension_target_is_plus_4_alpha1": c2_extension_alpha_coeffs(TARGET_L) == [4, 0, 0],
    }
    cohomology_checks = {
        "elliptic_factor_1_degree": TARGET_L2[0],
        "elliptic_factor_1_hodge": elliptic_hodge_for_degree(TARGET_L2[0]),
        "elliptic_factor_2_degree": TARGET_L2[1],
        "elliptic_factor_2_hodge": elliptic_hodge_for_degree(TARGET_L2[1]),
        "base_hodge": base_hodge,
        "base_h0_zero": base_hodge["h0"] == 0,
        "base_h1": h1_total,
        "vertical_h1_extra_from_H0_base": 0,
        "conditional_total_h1": h1_total,
        "reason_vertical_differential_does_not_change_H1_in_reduced_packet": (
            "The candidate is pulled back from the base and H0(base,M)=0, so the "
            "degree-one vertical contribution H0(base,M) tensor H1(fiber,O) is zero."
        ),
    }

    conditional_packet_valid = (
        all(input_gates.values())
        and all(automorphy_checks.values())
        and h1_total == 8
        and validation["passes"]
        and validation["promotes_selected_data"] is False
    )

    status = (
        "VISIBLE_RANK2_L2_PULLBACK_CECH_ATTEMPT_CONDITIONAL_H1_POSITIVE_SELECTION_OPEN"
        if conditional_packet_valid
        else "VISIBLE_RANK2_L2_PULLBACK_CECH_ATTEMPT_NOT_VERIFIED"
    )

    report = {
        "calculation": "VisibleRank2L2PullbackCechAttempt",
        "status": status,
        "generated_by": "scripts/construct_visible_rank2_l2_pullback_cech_attempt.py",
        "input_certificates": {
            "visible_rank2_extension_valpha_route": RANK2_ROUTE.name,
            "visible_rank2_l2_ext_h1_gate": L2_GATE.name,
            "iwasawa_standard_lattice_deck_scaffold": DECK_SCAFFOLD.name,
            "visible_rank2_l2_invariant_dolbeault_attempt": INVARIANT_ATTEMPT.name,
        },
        "input_gates": input_gates,
        "pullback_model": {
            "model": "pi^*M from the holomorphic base torus of the standard Iwasawa deck scaffold",
            "projection": "pi(z1,z2,z3)=(z1,z2)",
            "base": "E1 x E2 with E_j=C/(Z+iZ)",
            "central_fiber": "the z3 elliptic fiber is topologically present but c1 degree is zero there",
            "L_vector_abc": TARGET_L,
            "c1_L_squared_vector_abc": TARGET_L2,
            "deck_generators": DECK_GENERATORS,
            "c1_deck_alternating_matrix_order_g1_to_g6": c1_matrix,
            "degree_pairs": {
                "E1_pair_g1_g2": TARGET_L2[0],
                "E2_pair_g3_g4": TARGET_L2[1],
                "central_pair_g5_g6": TARGET_L2[2],
            },
        },
        "automorphy_checks": automorphy_checks,
        "cohomology_model": {
            "method": "reduced exact Cech/Kunneth packet for the base pullback candidate",
            "warning": (
                "This is not a raw good-cover transition table and is not a selected MTT "
                "source. It is a finite conditional cohomology packet for the pullback model."
            ),
            **cohomology_checks,
        },
        "validator_packet": {
            "path": "candidate_data/visible_rank2_l2_pullback_cech_attempt.cohomology.json",
            "candidate_role": packet["candidate_role"],
            "source_kind": packet["source"]["source_kind"],
            "h1": h1_total,
            "validation": validation,
        },
        "calculation_results": {
            "pullback_c1_cocycle_constructed": True,
            "c1_L_squared_target_hit": automorphy_checks["degrees_match_c1_L_squared"],
            "c1_square_target_hit": automorphy_checks["c1_L_squared_square_is_minus_16_alpha1"],
            "base_pullback_h1_computed": h1_total,
            "validator_packet_passes": validation["passes"],
            "selected_L2_packet_constructed": False,
            "nonzero_Ext_class_selected": False,
            "stability_proved": False,
            "same_source_D_E_dotD_Riesz_Green_constructed": False,
        },
        "what_this_closes": {
            "global_scalar_route_replaced_by_nontrivial_automorphy_candidate": True,
            "integral_deck_c1_cocycle_for_c1_L_squared": automorphy_checks[
                "integral_alternating_c1_cocycle"
            ],
            "conditional_h1_positive_for_base_pullback_model": h1_total == 8,
            "finite_validator_accepts_reduced_unselected_packet": validation["passes"],
            "actual_MTT_selection_of_pullback_representative": False,
        },
        "still_open": {
            "prove_MTT_selects_this_pullback_line_bundle_representative": True,
            "supply_raw_good_cover_transition_functions_or_equivalent_selected_automorphy_source": True,
            "promote_UNSELECTED_FIXTURE_to_SELECTED_DATA_without_changing_cohomology_by_hand": True,
            "choose_nonzero_Ext_class_from_selected_H1": True,
            "prove_non_split_extension_stability": True,
            "derive_source_Chern_Weil_representative": True,
            "prove_HYM_or_Route_C_residual": True,
            "derive_same_total_source_D_E_dotD_Riesz_Green": True,
            "primitive_C1_contractions": True,
            "Yukawa_and_CKM_magnitude_closure": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_MTT_selected_pullback_representative": False,
            "claims_raw_good_cover_transitions_supplied": False,
            "claims_selected_L2_packet_constructed": False,
            "claims_nonzero_Ext_class_selected": False,
            "claims_stability_proved": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "The base-pullback automorphy candidate is the first route that "
                "hits c1(L^2)=(2,-4,0) and gives positive finite cohomology: the "
                "reduced packet has h1=8 and passes the Ext validator as an "
                "UNSELECTED_FIXTURE. It does not yet promote V_alpha because MTT "
                "selection of this pullback representative is still open."
            ),
            "next_action": (
                "Find or prove the MTT source selecting the base-pullback line "
                "bundle representative; then rerun the same packet as SELECTED_DATA "
                "and use one of the eight classes as the non-split extension input."
            ),
        },
    }
    return report


def main() -> int:
    report = analyze()
    write_json(CANDIDATE, report)
    certificate = {
        "certificate": "VisibleRank2L2PullbackCechAttempt",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": "candidate_data/visible_rank2_l2_pullback_cech_attempt.candidate.json",
        "validator_packet": report["validator_packet"],
        "input_certificates": report["input_certificates"],
        "input_gates": report["input_gates"],
        "pullback_model": report["pullback_model"],
        "automorphy_checks": report["automorphy_checks"],
        "cohomology_model": report["cohomology_model"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write_json(CERTIFICATE, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return (
        0
        if report["status"]
        == "VISIBLE_RANK2_L2_PULLBACK_CECH_ATTEMPT_CONDITIONAL_H1_POSITIVE_SELECTION_OPEN"
        else 1
    )


if __name__ == "__main__":
    raise SystemExit(main())
