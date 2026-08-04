"""Gate the Iwasawa abelian Chern/Bianchi row against nonabelian SU3 closure."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

INPUT = DATA / "chern_bianchi_source_packet_candidates.candidate.json"
OUTPUT_DATA = DATA / "iwasawa_abelian_row_to_nonabelian_source_gate.candidate.json"
OUTPUT_CERT = CERTS / "iwasawa_abelian_row_to_nonabelian_source_gate_certificate.json"


def main() -> None:
    source = json.loads(INPUT.read_text(encoding="utf-8"))
    abelian = next(row for row in source["candidate_packets"] if row["id"] == "iwasawa_abelian_two_line_flux_row")
    promotion_tests = [
        {
            "id": "diagonal_det_one_embedding",
            "ansatz": "E_split = L_(1,2,0) + L_(-1,-2,0) + O",
            "what_it_preserves": ["c1(E)=0", "abelian Chern/Bianchi row", "same Iwasawa branch"],
            "passes": {
                "same_branch": True,
                "determinant_one_topology": True,
                "chern_bianchi_support": True,
                "nonabelian_su3_structure_group": False,
                "irreducible_or_stable_hym_source": False,
                "selected_transition_matrices": False,
                "endomorphism_E": False,
                "finite_part": False,
            },
            "decision": "REJECT_AS_CLOSURE_SUPPORT_ONLY",
            "reason": "The split diagonal embedding is reducible abelian data inside SU3 topology, not a selected nonabelian color-threshold operator packet.",
        },
        {
            "id": "non_split_extension_promotion",
            "ansatz": "0 -> L_(1,2,0) -> E -> L_(-1,-2,0) + O -> 0",
            "what_it_would_preserve": ["c1(E)=0", "same Chern/Bianchi class as the abelian row"],
            "required_new_data": [
                "selected nonzero extension class eta in Ext^1(L_(-1,-2,0)+O, L_(1,2,0))",
                "same-branch stability or HYM certificate",
                "explicit transition matrices with det=1",
                "Chern connection/curvature or rho_E response",
                "zero-order Weitzenbock block endomorphism_E",
                "finite heat/spectrum/torsion determinant part",
            ],
            "passes": {
                "same_branch_possible": True,
                "topological_promotion_possible": True,
                "selected_extension_class_present": False,
                "stability_or_hym_certificate_present": False,
                "selected_transition_matrices": False,
                "endomorphism_E": False,
                "finite_part": False,
            },
            "decision": "BEST_LIVE_PROMOTION_ROUTE_VALUES_OPEN",
            "reason": "A non-split extension could turn the abelian topological row into a genuine SU3 bundle, but the current corpus does not select the extension class or operator.",
        },
        {
            "id": "monad_section_ring_promotion",
            "ansatz": "Use the 11-space monad/section-ring packet to build E from selected f,g with g*f=0.",
            "what_it_would_preserve": ["existing symbolic charge closure", "same c/gerbe typing constraints"],
            "required_new_data": [
                "finite Cech/Dolbeault cochain bases",
                "selected multiplication constants mu_i",
                "selected f,g matrices",
                "proof that the resulting E has the abelian row as Chern/Bianchi shadow",
            ],
            "passes": {
                "symbolic_charge_products": True,
                "selected_f_g_present": False,
                "chern_bianchi_match_proved": False,
                "endomorphism_E": False,
                "finite_part": False,
            },
            "decision": "LIVE_PARALLEL_ROUTE_BLOCKED_BY_SAME_FINITE_SOURCE_GAP",
            "reason": "This remains principled, but it depends on the finite cochain source solve that was already audited as open.",
        },
        {
            "id": "direct_invariant_su3_instanton_promotion",
            "ansatz": "Choose invariant su(3)-valued connection one-forms on the Iwasawa frame and solve HYM/Bianchi.",
            "what_it_would_preserve": ["same branch", "direct operator construction"],
            "required_new_data": [
                "source rule selecting the su(3) matrices",
                "HYM equations solved without target residual",
                "Bianchi row matched to the explicit abelian row or independent selected class",
            ],
            "passes": {
                "equation_template_exists": True,
                "selected_matrix_rule_present": False,
                "hym_solution_present": False,
                "endomorphism_E": False,
                "finite_part": False,
            },
            "decision": "LIVE_BUT_RISKY_WITHOUT_SELECTOR",
            "reason": "Useful for computation, but arbitrary su(3) matrix choices would reintroduce knobs unless selected by the same MTT branch.",
        },
    ]
    candidate = {
        "candidate": "SelectedQaSU3IwasawaAbelianRowToNonabelianSourceGate",
        "status": "IWASAWA_ABELIAN_ROW_TO_NONABELIAN_SOURCE_GATE_BUILT_PROMOTION_OPEN",
        "input_statuses": {"chern_bianchi_candidates": source["status"]},
        "abelian_row": abelian,
        "promotion_tests": promotion_tests,
        "best_live_route": {
            "id": "non_split_extension_promotion",
            "why": "It preserves the explicit Chern/Bianchi row while giving the only current path from reducible abelian support to a genuine SU3 source.",
            "minimal_next_computation": "Compute or certify the selected Ext^1 class and stability/HYM condition for the same Iwasawa branch.",
        },
        "result": {
            "abelian_row_embeds_det_one_topology": True,
            "abelian_row_is_selected_nonabelian_source": False,
            "promotion_route_identified": True,
            "selected_extension_or_transition_data_found": False,
            "selected_endomorphism_E_found": False,
            "determinant_computable_now": False,
            "qa_su3_closed": False,
            "full_sm_closure_achieved": False,
            "target_fitting_used": False,
        },
        "do_not_use": [
            "split diagonal SU3 topology as nonabelian SU3 source",
            "arbitrary extension class eta",
            "arbitrary invariant su(3) connection matrices",
            "Qa residual or observed constants to choose the extension",
        ],
        "decision": {
            "result": "Promotion is plausible but not closed.",
            "why": "The abelian row supplies real same-branch topological support; the missing selected object is the non-split/stable SU3 transition or operator packet.",
            "next_move": "Build an Ext/stability source search and, if possible, a finite transition-matrix validator for the non-split extension.",
        },
        "next_required_artifact": "Selected_Qa_SU3_Ext_Stability_Source_Search_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3IwasawaAbelianRowToNonabelianSourceGate",
        "status": "QA_SU3_IWASAWA_ABELIAN_ROW_TO_NONABELIAN_SOURCE_GATE_BUILT_PROMOTION_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "det_one_split_embedding_tested": True,
            "split_embedding_rejected_as_closure": True,
            "non_split_extension_route_identified": True,
            "arbitrary_su3_matrix_route_guarded": True,
        },
        "what_remains_open": {
            "selected_extension_class": True,
            "stability_or_hym_certificate": True,
            "selected_transition_matrices": True,
            "endomorphism_E": True,
            "finite_part_data": True,
            "qa_su3_packet_closed": False,
        },
        "next_required_artifact": candidate["next_required_artifact"],
        "closure_claimed": False,
        "target_fitting_used": False,
    }
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
