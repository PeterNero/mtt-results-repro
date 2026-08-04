"""Attempt to prove Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_v1.

This script deliberately distinguishes a closed prefix from the full theorem.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CERTS = ROOT / "certificates"
SM = TEXPAPERS / "mtt-sm-parity-closure" / "certificates"

LOCAL_CW = CERTS / "selected_qa_su3_m1_cw_operator_source_attempt_certificate.json"
LOCAL_H1 = CERTS / "selected_qa_su3_m1_rank2_ext_h1_source_data_attempt_certificate.json"
LOCAL_ORBIT = CERTS / "q79_valpha_source_frontier_import_certificate.json"
SM_VISIBLE_CW = SM / "selected_visible_chern_weil_operator_source_certificate.json"
SM_SAME_SOURCE = SM / "selected_nonsplit_rank2_or_routec_same_source_packet_certificate.json"
SM_SOURCE_ALPHA1 = SM / "selected_source_origin_and_alpha1_driver_certificate.json"
SM_DE_BN = SM / "selected_routec_de_action_on_smooth_bn_certificate.json"
SM_DOTD_BN = SM / "selected_routec_sector_projectors_dotd_on_smooth_bn_certificate.json"
SM_C1_BN = SM / "selected_routec_c1_primitive_response_on_smooth_bn_certificate.json"
SM_SOURCE_BASIS = SM / "selected_routec_source_provenance_or_basis_certificate_certificate.json"

OUTPUT = CERTS / "selected_qa_su3_m1_cw_operator_source_proof_attempt_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    local_cw = load(LOCAL_CW)
    local_h1 = load(LOCAL_H1)
    local_orbit = load(LOCAL_ORBIT)
    sm_visible_cw = load(SM_VISIBLE_CW)
    sm_same_source = load(SM_SAME_SOURCE)
    sm_source_alpha1 = load(SM_SOURCE_ALPHA1)
    sm_de = load(SM_DE_BN)
    sm_dotd = load(SM_DOTD_BN)
    sm_c1 = load(SM_C1_BN)
    sm_source_basis = load(SM_SOURCE_BASIS)

    closed_prefix = {
        "formal_CW_row_and_integral_target_viable": local_cw["closed_now"][
            "formal_trace_free_CW_row_realizable"
        ]
        and local_cw["closed_now"]["rank2_extension_c2_arithmetic_viable"],
        "split_or_diagonal_HYM_shortcut_retired": sm_visible_cw["what_closes"][
            "split_line_hym_route_retired_as_final_source"
        ],
        "single_same_source_packet_contract_locked": sm_visible_cw["what_closes"][
            "single_same_source_packet_contract_locked"
        ],
        "rank2_or_routec_lanes_identified": sm_same_source["what_closes"][
            "two_live_same_source_lanes_identified"
        ],
        "h1_ext_fixture_exists_but_unselected": local_h1["imported_h1_packet"]["h1"] == 8
        and local_h1["imported_h1_packet"]["nonzero_ext_class"] is True
        and local_h1["imported_h1_packet"]["source_selected_by_mtt"] is False,
        "source_alpha1_reduced_to_payload": sm_source_alpha1["what_closes"][
            "source_and_alpha1_reduced_to_one_payload"
        ],
        "routec_DE_matrix_on_BN_emitted": sm_de["what_closes"][
            "D_E_matrix_on_27_mode_BN_emitted"
        ],
        "routec_sector_projectors_and_dotD_emitted": sm_dotd["what_closes"][
            "sector_projectors_on_27_mode_BN_emitted"
        ]
        and sm_dotd["what_closes"]["dotD_alpha1_matrix_in_same_basis_emitted"],
        "primitive_C1_engine_built": sm_c1["what_closes"][
            "primitive_C1_contraction_engine_built"
        ],
        "q79_valpha_frontier_agrees": local_orbit["closed_now"][
            "local_cross_repo_frontier_agrees"
        ],
    }

    theorem_blockers = {
        "selected_visible_source_certificate": sm_source_basis["what_remains_open"][
            "selected_source_flags_promoted"
        ],
        "quotient_valid_BN_basis_certificate": sm_source_basis["what_remains_open"][
            "quotient_valid_BN_basis_certificate"
        ],
        "honest_manifest_without_lifted_flags": sm_source_basis["what_remains_open"][
            "honest_manifest_without_lifted_flags"
        ],
        "selected_D_E_source_promotion": sm_de["what_remains_open"][
            "selected_D_E_source_promotion"
        ],
        "selected_dotD_source_verified": sm_dotd["what_remains_open"][
            "selected_dotD_source_verified"
        ],
        "alpha1_driver_verified": sm_dotd["what_remains_open"]["alpha1_driver_verified"],
        "selected_noninvariant_C1_primitive_or_vertex": sm_c1["what_remains_open"][
            "selected_noninvariant_C1_primitive_or_vertex"
        ],
        "nonzero_C1_response_matrices": sm_c1["what_remains_open"][
            "nonzero_C1_response_matrices"
        ],
    }

    theorem_proved = all(closed_prefix.values()) and not any(theorem_blockers.values())

    output = {
        "certificate": "SelectedQaSU3M1ChernWeilOperatorSourceProofAttempt",
        "status": "CW_OPERATOR_SOURCE_PREFIX_CLOSED_FULL_THEOREM_SOURCE_CERTIFICATE_OPEN",
        "inputs": {
            "local_cw_attempt": str(LOCAL_CW.relative_to(ROOT)),
            "local_h1_attempt": str(LOCAL_H1.relative_to(ROOT)),
            "q79_valpha_frontier": str(LOCAL_ORBIT.relative_to(ROOT)),
            "sm_visible_cw": str(SM_VISIBLE_CW),
            "sm_same_source": str(SM_SAME_SOURCE),
            "sm_source_alpha1": str(SM_SOURCE_ALPHA1),
            "sm_de_bn": str(SM_DE_BN),
            "sm_dotd_bn": str(SM_DOTD_BN),
            "sm_c1_bn": str(SM_C1_BN),
            "sm_source_or_basis": str(SM_SOURCE_BASIS),
        },
        "theorem_proved": theorem_proved,
        "closed_prefix": closed_prefix,
        "remaining_theorem_blockers": theorem_blockers,
        "maximal_current_theorem": {
            "name": "Selected_Qa_SU3_M1_Chern_Weil_Operator_Source_Prefix_Theorem_v1",
            "statement": (
                "The visible Chern-Weil/operator source target is reduced to a "
                "single same-source payload problem. The formal row, integral "
                "rank-two target, same-source contract, BN D_E matrix, same-basis "
                "dotD/projectors, and primitive C1 engine are available as a "
                "closed prefix, but the selected source certificate, BN basis "
                "certificate, honest replay, selected dotD flags, and nonzero "
                "selected C1 primitive remain open."
            ),
        },
        "next_closing_object": {
            "name": "Selected_Source_Provenance_or_BN_Basis_Certificate_then_C1_Primitive_v1",
            "must_prove": [
                "source provenance or quotient-valid BN basis certificate without lifted flags",
                "honest D_E and dotD validator replay on the same source",
                "alpha1 driver provenance in that same basis",
                "selected non-invariant C1 primitive or vertex with nonzero response matrices",
            ],
        },
        "guardrails": {
            "claims_full_CW_operator_source_theorem": theorem_proved,
            "claims_selected_source_promotion": False,
            "claims_selected_D_E_dotD": False,
            "claims_nonzero_C1_response": False,
            "claims_full_SM_closure": False,
            "uses_observed_cp_sign_or_masses": False,
            "uses_benchmark_flavor_entries": False,
        },
        "honest_answer": (
            "The full Selected_Qa_SU3_M1_Chern_Weil_Operator_Source theorem is "
            "not proved yet. The maximal current result is a closed prefix: "
            "the row and same-source operator scaffolding are reduced to a "
            "source/basis/C1 primitive certificate. The proof cannot be completed "
            "from current artifacts without promoting selected flags by hand."
        ),
    }

    if "--write-certificate" in __import__("sys").argv:
        OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
