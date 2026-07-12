"""Evaluate whether the Iwasawa abelian Chern/Bianchi row promotes to SU3."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"

INPUTS = {
    "chern_bianchi_candidates": CERTS / "selected_qa_su3_chern_bianchi_source_packet_candidates_certificate.json",
    "repair_a_b_test": CERTS / "selected_qa_su3_repair_a_quotient_or_b_torsion_source_test_certificate.json",
    "repair_retirement": CERTS / "selected_qa_su3_repair_retirement_stress_test_certificate.json",
    "repair_b_no_go": CERTS / "selected_qa_su3_repair_b_primitive_correction_no_go_certificate.json",
    "projective_decision": CERTS / "selected_qa_su3_projective_clock_shift_or_endomorphism_route_decision_certificate.json",
    "operator_packet_interface": CERTS / "selected_qa_su3_color_bundle_operator_packet_interface_certificate.json",
    "operator_packet_fill": CERTS / "selected_qa_su3_color_bundle_operator_packet_fill_attempt_certificate.json",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    inputs = {name: load(path) for name, path in INPUTS.items()}
    candidates = inputs["chern_bianchi_candidates"]

    promotion_tests = [
        {
            "id": "direct_sum_line_bundle_promotion",
            "claim": "Promote the two-line abelian row to a direct-sum SU3 source.",
            "status": "REJECT_AS_SELECTED_QA_SU3_SOURCE",
            "positive_data": [
                "explicit invariant Iwasawa Chern/Bianchi row exists",
                "integer two-line flux row has determinant-one Cartan flavor",
            ],
            "blocking_tests": {
                "nonabelian_color_source": False,
                "indecomposable_rank3_branch": False,
                "extra_stabilizer_absent": False,
                "selected_transition_rhoE": False,
                "endomorphism_E": False,
                "finite_determinant": False,
            },
            "reason": (
                "A direct sum of line data preserves abelian reducibility.  It can "
                "support anomaly bookkeeping, but it is not the currently selected "
                "indecomposable rank-3 Qa/SU3 color-threshold source."
            ),
        },
        {
            "id": "stable_su3_bundle_same_chern_row",
            "claim": "Use the abelian row as Chern-Weil target for a stable SU3 bundle.",
            "status": "LIVE_BUT_UNCONSTRUCTED",
            "positive_data": [
                "Strominger/HYM framework favors stable or indecomposable SU3 data",
                "the abelian row supplies a concrete Chern/Bianchi numerical target",
            ],
            "blocking_tests": {
                "nonabelian_color_source": "OPEN",
                "indecomposable_rank3_branch": "OPEN",
                "explicit_transition_functions": False,
                "selected_transition_rhoE": False,
                "endomorphism_E": False,
                "finite_determinant": False,
            },
            "reason": (
                "This is the best forward route: construct a stable rank-3 SU3 "
                "bundle or sheaf whose selected Chern-Weil row matches the Iwasawa "
                "Bianchi support row.  No such source packet is present yet."
            ),
        },
        {
            "id": "indecomposable_extension_promotion",
            "claim": "Realize the row through a non-split rank-3 extension.",
            "status": "BEST_CURRENT_RESEARCH_ROUTE",
            "positive_data": [
                "prior repair gates prefer the indecomposable rank-3 HYM branch",
                "Repair A is retired exactly because it splits",
                "Repair B remains algebraically compatible with no extra unitary centralizer",
            ],
            "blocking_tests": {
                "extension_class_selected": False,
                "hym_connection_source_certified": False,
                "primitive_correction_source_certified": False,
                "selected_transition_rhoE": False,
                "endomorphism_E": False,
                "finite_determinant": False,
            },
            "reason": (
                "This route keeps the abelian row as topological support while "
                "requiring the actual color operator to come from a non-split "
                "SU3 extension.  It is compatible with the guardrails and is the "
                "next constructive target."
            ),
        },
        {
            "id": "projective_clock_shift_carrier_promotion",
            "claim": "Use the projective order-64 clock-shift carrier as the source.",
            "status": "AUXILIARY_ONLY_NOT_SELECTED_SOURCE",
            "positive_data": [
                "projective nonabelian finite carrier is mathematically real",
                "it may constrain future endomorphism or sector data",
            ],
            "blocking_tests": {
                "same_branch_chern_bianchi_packet": False,
                "selected_su3_bundle": False,
                "endomorphism_E": False,
                "finite_determinant": False,
            },
            "reason": (
                "The projective carrier is not a selected Qa/SU3 Chern/Bianchi "
                "source packet.  It can remain a validator or auxiliary finite "
                "carrier, not the determinant proof source."
            ),
        },
    ]

    best_route = "indecomposable_extension_promotion"
    output = {
        "certificate": "SelectedQaSU3IwasawaAbelianRowToNonabelianSourceGate",
        "status": "QA_SU3_IWASAWA_ABELIAN_ROW_PROMOTION_GATE_BUILT_EXTENSION_ROUTE_PRIMARY",
        "input_status": {
            name: data.get("status", "UNKNOWN") for name, data in inputs.items()
        },
        "starting_point": {
            "best_chern_bianchi_candidate": candidates["best_current_candidate"]["id"],
            "best_candidate_not_closure": candidates["best_current_candidate"]["why_not_closure"],
        },
        "promotion_tests": promotion_tests,
        "decision": {
            "abelian_row_promoted_to_selected_su3_source_now": False,
            "abelian_row_remains_valid_support_data": True,
            "direct_sum_route_selected": False,
            "stable_bundle_route_live": True,
            "indecomposable_extension_route_primary": True,
            "projective_clock_shift_route_source": False,
            "determinant_computable_now": False,
            "qa_su3_closed": False,
            "target_fitting_used": False,
        },
        "primary_route": {
            "id": best_route,
            "constructive_requirement": [
                "produce a non-split rank-3 SU3 bundle or sheaf on the selected Iwasawa/Strominger branch",
                "prove its Chern-Weil/Bianchi row equals or legally refines the abelian support row",
                "supply selected transition matrices accepted by the rho_E validator",
                "compute the Laplace-type endomorphism_E or determinant finite part from that source",
            ],
        },
        "guardrails": [
            "Do not treat abelian Cartan flux as the nonabelian color determinant.",
            "Do not revive the split Repair A branch without changing the selected branch.",
            "Do not use the projective clock-shift carrier as a source packet.",
            "Do not choose the extension class by matching the target residual.",
        ],
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_NonSplit_Extension_Source_Construction_v1",
            "must_supply": [
                "extension class or transition cocycle",
                "SU3 determinant/tracelessness check",
                "Chern/Bianchi row check",
                "rho_E validator input",
                "operator packet fields through endomorphism_E or finite determinant",
            ],
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
