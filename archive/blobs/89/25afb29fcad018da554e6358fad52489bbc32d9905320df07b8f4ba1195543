"""Bridge the qutrit orientation fork to selected D_E/dotD data.

The four-route torsion-label selector reduces the flat gerbe label to the
nontrivial conjugate pair m in {1,2}.  This script checks whether the current
proof package already contains the orientation-carrying selected operator data
needed to choose between those two labels.

It does not promote an orientation convention.  It records the precise contract
that a selected D_E/dotD package must satisfy to select m=1 versus m=2.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"


def load_json(name: str) -> dict[str, Any]:
    return json.loads((CERTIFICATES / name).read_text(encoding="utf-8"))


def all_false(values: dict[str, Any], keys: list[str]) -> bool:
    return all(values.get(key) is False for key in keys)


def build_branch_packets() -> list[dict[str, Any]]:
    return [
        {
            "branch": "current_q79_orientation",
            "torsion_label_m": 1,
            "global_cp_label": 79,
            "inverse_cp_label": 369,
            "sector_orientations": {
                "Q": 1,
                "L": 1,
                "u": 2,
                "d": 2,
                "e": 2,
                "N": 2,
                "H": 0,
            },
            "allowed_pairings": {
                "u": "Q1+u2",
                "d": "Q1+d2",
                "e": "L1+e2",
                "nuD": "L1+N2",
            },
            "c6_left_representative_labels": {
                "u:C6": 79,
                "d:C6": 79,
                "e:C6": 79,
                "nuD:C6": 79,
            },
            "conditional_su5_transport_orientation": "F",
            "role": "conditional current orientation; not yet selected by D_E/dotD",
        },
        {
            "branch": "conjugate_q369_orientation",
            "torsion_label_m": 2,
            "global_cp_label": 369,
            "inverse_cp_label": 79,
            "sector_orientations": {
                "Q": 2,
                "L": 2,
                "u": 1,
                "d": 1,
                "e": 1,
                "N": 1,
                "H": 0,
            },
            "allowed_pairings": {
                "u": "Q2+u1",
                "d": "Q2+d1",
                "e": "L2+e1",
                "nuD": "L2+N1",
            },
            "c6_left_representative_labels": {
                "u:C6": 369,
                "d:C6": 369,
                "e:C6": 369,
                "nuD:C6": 369,
            },
            "conditional_su5_transport_orientation": "F*",
            "role": "global complex-conjugate orientation; not independently selected",
        },
    ]


def analyze() -> dict[str, Any]:
    torsion = load_json("iwasawa_torsion_label_four_route_selector_certificate.json")
    common_c6 = load_json("iwasawa_c6_common_holonomy_branch_pair_certificate.json")
    global_c6 = load_json("iwasawa_c6_global_phase_block_certificate.json")
    coupling = load_json("iwasawa_block_coupling_invariant_selection_rule_certificate.json")
    selected_de = load_json("iwasawa_selected_de_construction_attempt_certificate.json")
    de_hunt = load_json("selected_de_source_hunt_certificate.json")
    zero_dotd = load_json("selected_zero_mode_basis_dotd_interface_certificate.json")
    route_c = load_json("iwasawa_route_c_finite_solve_scaffold_certificate.json")
    su5 = load_json("selected_su5_qutrit_polarization_packet_fill_attempt_certificate.json")

    torsion_calc = torsion.get("calculation_results", {})
    c6_calc = common_c6.get("calculation_results", {})
    global_c6_calc = global_c6.get("calculation_results", {})
    coupling_calc = coupling.get("calculation_results", {})
    zero_gates = zero_dotd.get("completion_gates", {})
    selected_de_constructed = (
        selected_de.get("verdict", {}).get("selected_D_E_constructed") is True
    )
    selected_de_source_found = (
        de_hunt.get("hunt_result", {}).get("selected_D_E_source_found") is True
    )
    dotd_values_closed = (
        zero_dotd.get("verdict", {}).get("closes_dotD_operator_values") is True
    )
    route_c_ready = route_c.get("verdict", {}).get("route_c_scaffold_constructed") is True

    branch_packets = build_branch_packets()
    branch_labels = [packet["torsion_label_m"] for packet in branch_packets]
    cp_labels = [packet["global_cp_label"] for packet in branch_packets]

    existing_orientation_sources_cohere = (
        torsion_calc.get("common_candidate_labels") == branch_labels
        and torsion_calc.get("selected_torsion_label") is None
        and c6_calc.get("global_conjugate_label_patterns")
        == [[79, 79, 79, 79], [369, 369, 369, 369]]
        and global_c6_calc.get("global_pair_are_complex_conjugates") is True
        and coupling_calc.get("allowed_nontrivial_pair_orientations") == ["1+2", "2+1"]
        and coupling_calc.get("conjugate_matter_pair_with_trivial_Higgs_allowed") is True
    )

    selected_operator_data_absent = (
        not selected_de_constructed
        and not selected_de_source_found
        and not dotd_values_closed
        and all_false(
            zero_gates,
            [
                "all_D_operators_supplied",
                "all_dotD_alpha1_operators_supplied",
                "primitive_contractions_filled",
                "response_matrices_computed",
                "rank_and_ckm_tests_evaluated",
            ],
        )
    )

    su5_is_only_conditional_fixture = (
        su5.get("calculation_results", {}).get("validator_orientation") == "F"
        and su5.get("calculation_results", {}).get("selected_source_available") is False
        and su5.get("calculation_results", {}).get("promotes_to_selected_heavy_link_input")
        is False
    )

    unique_branch_selected_now = (
        existing_orientation_sources_cohere
        and not selected_operator_data_absent
        and selected_de_constructed
        and dotd_values_closed
    )

    return {
        "calculation": "IwasawaOrientationDEDotDBridge",
        "status": "REDUCED_TO_GLOBAL_CONJUGATE_PAIR_SELECTED_OPERATOR_OPEN",
        "branch_packets": branch_packets,
        "calculation_results": {
            "existing_orientation_sources_cohere": existing_orientation_sources_cohere,
            "torsion_candidate_labels": torsion_calc.get("common_candidate_labels"),
            "global_cp_label_pair": cp_labels,
            "c6_label_patterns": c6_calc.get("global_conjugate_label_patterns"),
            "conjugate_pair_only": True,
            "selected_D_E_constructed": selected_de_constructed,
            "selected_D_E_source_found": selected_de_source_found,
            "selected_dotD_values_closed": dotd_values_closed,
            "selected_operator_data_absent": selected_operator_data_absent,
            "route_c_scaffold_ready": route_c_ready,
            "su5_orientation_is_conditional_fixture": su5_is_only_conditional_fixture,
            "unique_branch_selected_now": unique_branch_selected_now,
        },
        "selection_contract": {
            "must_select_exactly_one_torsion_label_m": [1, 2],
            "must_bind_m_to_global_cp_label": {
                "m=1": 79,
                "m=2": 369,
            },
            "must_bind_sector_orientations_to_D_E_domains": [
                "Q,L carry the selected left family orientation",
                "u,d,e,N carry the conjugate right family orientation",
                "H remains the trivial Higgs line",
            ],
            "must_verify_same_branch_for_dotD": (
                "dotD_alpha1 must be the derivative of the same selected "
                "D_E branch, not an independently chosen sign or phase"
            ),
            "must_feed_existing_validators": [
                "validate_iwasawa_de_action.py",
                "validate_iwasawa_riesz_gap.py",
                "validate_iwasawa_reduced_green.py",
                "validate_iwasawa_dotd_response.py",
            ],
            "allowed_outcomes_after_selected_operator": [
                "retarded/selected operator fixes m=1 and q=79",
                "retarded/selected operator fixes m=2 and q=369",
                "operator package proves the two are antiunitarily equivalent, so only CP-odd signs differ",
            ],
        },
        "dependent_quantities": {
            "orientation_sensitive": [
                "C6 holonomy phase sign",
                "q79 versus q369 CP character convention",
                "SU(5) qutrit transport F versus F*",
                "complex signs of selected C1/C6 interference blocks",
                "CP-odd observables such as Jarlskog sign",
            ],
            "orientation_insensitive_until_selected_operator_breaks_conjugation": [
                "three-family rank count",
                "finite invariant-pairing support",
                "pure flat torsion zero-action statement",
                "Yukawa singular values under exact antiunitary conjugation",
                "CKM angle magnitudes under exact antiunitary conjugation",
            ],
        },
        "guardrails": {
            "claims_unique_m_label_now": False,
            "claims_two_unrelated_physical_universes": False,
            "uses_observed_cp_sign_to_select_branch": False,
            "uses_benchmark_flavor_entries": False,
            "claims_selected_D_E_or_dotD_constructed": False,
            "claims_full_sm_closure": False,
        },
        "verdict": {
            "orientation_dependency_sharpened": True,
            "current_status": "one nontrivial structure up to global conjugation",
            "unique_orientation_selected_now": unique_branch_selected_now,
            "not_two_independent_solutions": True,
            "first_missing_data": "selected orientation-carrying D_E/dotD operator package",
            "next_step": (
                "extend Route C so its residual certificate carries one branch "
                "packet, then run both conjugate packets through the D_E/dotD "
                "validators or prove antiunitary equivalence."
            ),
        },
    }


def main() -> int:
    print(json.dumps(analyze(), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
