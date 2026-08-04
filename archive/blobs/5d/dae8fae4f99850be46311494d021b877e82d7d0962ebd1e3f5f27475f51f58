"""Build Chern/Bianchi candidate source packets for Qa/SU3."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

SOURCE_SEARCH = DATA / "strominger_hym_source_packet_search.candidate.json"
OUTPUT_DATA = DATA / "chern_bianchi_source_packet_candidates.candidate.json"
OUTPUT_CERT = CERTS / "chern_bianchi_source_packet_candidates_certificate.json"


def main() -> None:
    search = json.loads(SOURCE_SEARCH.read_text(encoding="utf-8"))
    u1 = 8.0 * (2.0 * math.pi) ** 2
    candidate_packets = [
        {
            "id": "iwasawa_abelian_two_line_flux_row",
            "branch": "complex balanced Iwasawa invariant slice",
            "source_kind": "abelian line embedding in heterotic commutant",
            "status": "CHERN_BIANCHI_ROW_SUPPORTED_NOT_QA_SU3_COLOR_SOURCE",
            "source_selected_for_qa_su3_color_threshold": False,
            "data": {
                "flux_choice": "(1,2,0) plus (-1,-2,0)",
                "u": [u1, 0.0, 0.0],
                "dH": "w1=-4*r3^2, w2=w3=0",
                "gravitational_trace": "v1=8*r3^2/R^4, v2=v3=0 for r1=r2=R",
                "bianchi_equation": "8*(2*pi)^2 - 8*r3^2/R^4 = (16/alpha_prime)*r3^2",
            },
            "passes": {
                "integer_flux_row": True,
                "invariant_componentwise_bianchi_shape": True,
                "selected_su3_color_bundle": False,
                "selected_transition_rhoE": False,
                "endomorphism_E": False,
                "finite_part": False,
            },
            "meaning": "This is the strongest current Chern/Bianchi row. It may support a future nonabelian source packet, but by itself it is abelian commutant flux, not the selected Qa/SU3 color determinant.",
        },
        {
            "id": "nonabelian_stable_su3_hym_bundle_template",
            "branch": "Strominger/HYM fixed topological sector",
            "source_kind": "stable SU3 bundle/sheaf expected by HYM correspondence",
            "status": "TEMPLATE_ONLY_CANDIDATE_DATA_MISSING",
            "source_selected_for_qa_su3_color_threshold": False,
            "data": {
                "known": "Strominger/HYM framework and fixed-sector selection principles exist.",
                "missing": [
                    "explicit selected SU3 bundle/sheaf/twist on Qa branch",
                    "Chern/Mukai/gerbe vector",
                    "connection or transition data",
                    "endomorphism_E and finite determinant data",
                ],
            },
            "passes": {
                "framework_exists": True,
                "bianchi_packet": False,
                "selected_su3_color_bundle": False,
                "selected_transition_rhoE": False,
                "endomorphism_E": False,
                "finite_part": False,
            },
            "meaning": "Most physically aligned route, but currently missing the actual candidate data.",
        },
        {
            "id": "iwasawa_rhoE_validator_route",
            "branch": "Iwasawa finite transition data route",
            "source_kind": "future transition matrices rho_E(g,z)",
            "status": "VALIDATOR_AVAILABLE_CANDIDATE_UNSELECTED",
            "source_selected_for_qa_su3_color_threshold": False,
            "data": {
                "validator": "constant generator matrices and Iwasawa group relations can be checked",
                "missing": ["selected bundle E", "Hermitian metric compatibility", "sector projections", "selected D_E action"],
            },
            "passes": {
                "validator_exists": True,
                "candidate_transition_data": False,
                "selected_su3_color_bundle": False,
                "endomorphism_E": False,
                "finite_part": False,
            },
            "meaning": "Excellent downstream validator, not a source by itself.",
        },
        {
            "id": "visible_chern_weil_transfer",
            "branch": "q79 visible source branch",
            "source_kind": "visible Chern-Weil source-packet analogue",
            "status": "REJECT_DIRECT_TRANSFER_TEMPLATE_ONLY",
            "source_selected_for_qa_su3_color_threshold": False,
            "data": {
                "known": "visible branch has Chern-Weil quantization and operator-source gates",
                "missing": "same-branch Qa/SU3 compact Nil/Iwasawa color-source theorem",
            },
            "passes": {
                "template_exists": True,
                "same_branch_qa_su3": False,
                "selected_su3_color_bundle": False,
                "endomorphism_E": False,
                "finite_part": False,
            },
            "meaning": "Use as design pattern only.",
        },
    ]
    candidate = {
        "candidate": "SelectedQaSU3ChernBianchiSourcePacketCandidates",
        "status": "CHERN_BIANCHI_SOURCE_PACKET_CANDIDATES_BUILT_NO_SELECTED_SOURCE",
        "input_statuses": {"source_packet_search": search["status"]},
        "candidate_packets": candidate_packets,
        "best_current_candidate": {
            "id": "iwasawa_abelian_two_line_flux_row",
            "why_best": "It supplies an explicit invariant Chern/Bianchi row on Iwasawa.",
            "why_not_closure": "It is abelian commutant flux, not a selected SU3 color-threshold bundle/operator.",
        },
        "result": {
            "candidate_table_built": True,
            "chern_bianchi_row_found": True,
            "selected_qa_su3_source_found": False,
            "selected_endomorphism_E_found": False,
            "determinant_computable_now": False,
            "qa_su3_closed": False,
            "full_sm_closure_achieved": False,
            "target_fitting_used": False,
        },
        "do_not_use": [
            "Iwasawa abelian commutant flux row as selected SU3 color determinant",
            "rho_E validators as selected transition data",
            "visible Chern-Weil packet as Qa/SU3 source",
            "target residual to choose Chern/Bianchi candidate",
        ],
        "decision": {
            "result": "Chern/Bianchi candidate table built; explicit abelian Iwasawa row is best current support but not closure.",
            "why": "A Chern/Bianchi row is anomaly/topological support, while Qa/SU3 closure needs selected nonabelian transition/operator data.",
            "next_move": "Test whether the abelian Iwasawa row can be promoted into a selected nonabelian SU3 source packet.",
        },
        "next_required_artifact": "Selected_Qa_SU3_Iwasawa_Abelian_Row_to_Nonabelian_Source_Gate_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3ChernBianchiSourcePacketCandidates",
        "status": "QA_SU3_CHERN_BIANCHI_SOURCE_PACKET_CANDIDATES_BUILT_NO_SELECTED_SOURCE",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "candidate_table_built": True,
            "explicit_iwasawa_abelian_row_recorded": True,
            "nonabelian_su3_template_identified": True,
            "direct_visible_transfer_rejected": True,
        },
        "what_remains_open": {
            "selected_nonabelian_su3_source": True,
            "selected_transition_or_operator_data": True,
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
