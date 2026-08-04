"""Build candidate Chern/Bianchi packets for the Qa/SU3 source problem."""

from __future__ import annotations

import json
from math import pi
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\proof_corpus")
OBSIDIAN = Path(r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory")

SOURCE_SEARCH = CERTS / "selected_qa_su3_strominger_hym_source_packet_search_certificate.json"

SOURCES = {
    "heterotic_flux_selection": OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Modal_Triplet_Theory__MTT_as_a_Selection_Principle_for_Heterotic_Flux_Compactifications.md",
    "strominger_system": OBSIDIAN / "16 Strings, Flux, & M-Theory Encodings" / "Modal_Triplet_Theory__From_MTT_to_the_Strominger__Heterotic_Flux__System.md",
    "iwasawa_rhoE_validator": Q79 / "Iwasawa_RhoE_Validator_v1.md",
    "iwasawa_riesz_gap_validator": Q79 / "Iwasawa_Riesz_Gap_Validator_v1.md",
    "visible_chern_weil_gate": Q79 / "Visible_Chern_Weil_Quantization_Gate_v1.md",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def scan(path: Path, terms: list[str]) -> dict[str, Any]:
    if not path.exists():
        return {"path": str(path), "present": False, "terms_found": [], "missing_terms": terms}
    text = path.read_text(encoding="utf-8", errors="ignore")
    found = [term for term in terms if term.lower() in text.lower()]
    return {
        "path": str(path),
        "present": True,
        "terms_found": found,
        "missing_terms": [term for term in terms if term not in found],
    }


def main() -> None:
    source_search = load(SOURCE_SEARCH)

    u1_iwasawa = 8 * (2 * pi) ** 2
    candidate_packets = [
        {
            "id": "iwasawa_abelian_two_line_flux_row",
            "status": "CHERN_BIANCHI_ROW_SUPPORTED_NOT_QA_SU3_COLOR_SOURCE",
            "branch": "complex balanced Iwasawa invariant slice",
            "source_kind": "abelian line embedding in heterotic commutant",
            "source_selected_for_qa_su3_color_threshold": False,
            "data": {
                "flux_choice": "(1,2,0) plus (-1,-2,0)",
                "u": [u1_iwasawa, 0.0, 0.0],
                "dH": "w1=-4*r3^2, w2=w3=0",
                "gravitational_trace": "v1=8*r3^2/R^4, v2=v3=0 for r1=r2=R",
                "bianchi_equation": "8*(2*pi)^2 - 8*r3^2/R^4 = (16/alpha_prime)*r3^2",
            },
            "passes": {
                "invariant_componentwise_bianchi_shape": True,
                "integer_flux_row": True,
                "selected_su3_color_bundle": False,
                "selected_transition_rhoE": False,
                "endomorphism_E": False,
                "finite_part": False,
            },
            "meaning": (
                "This is the strongest current Chern/Bianchi row.  It may support "
                "a future nonabelian source packet, but by itself it is abelian "
                "commutant flux, not the selected Qa/SU3 color determinant."
            ),
        },
        {
            "id": "nonabelian_stable_su3_hym_bundle_template",
            "status": "TEMPLATE_ONLY_CANDIDATE_DATA_MISSING",
            "branch": "Strominger/HYM fixed topological sector",
            "source_kind": "stable SU3 bundle/sheaf expected by HYM correspondence",
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
                "selected_su3_color_bundle": False,
                "bianchi_packet": False,
                "selected_transition_rhoE": False,
                "endomorphism_E": False,
                "finite_part": False,
            },
            "meaning": "Most physically aligned route, but currently missing the actual candidate data.",
        },
        {
            "id": "iwasawa_rhoE_validator_route",
            "status": "VALIDATOR_AVAILABLE_CANDIDATE_UNSELECTED",
            "branch": "Iwasawa finite transition data route",
            "source_kind": "future transition matrices rho_E(g,z)",
            "source_selected_for_qa_su3_color_threshold": False,
            "data": {
                "validator": "constant generator matrices and Iwasawa group relations can be checked",
                "missing": [
                    "selected bundle E",
                    "Hermitian metric compatibility",
                    "sector projections",
                    "selected D_E action",
                ],
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
            "status": "REJECT_DIRECT_TRANSFER_TEMPLATE_ONLY",
            "branch": "q79 visible source branch",
            "source_kind": "visible Chern-Weil source-packet analogue",
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

    source_checks = {
        "heterotic_flux_selection": scan(
            SOURCES["heterotic_flux_selection"],
            ["Iwasawa", "u_1=8(2\\pi)^2", "Bianchi", "Hermitian Yang", "componentwise"],
        ),
        "strominger_system": scan(
            SOURCES["strominger_system"],
            ["fixed topological sector", "HYM", "Bianchi", "selection potential"],
        ),
        "iwasawa_rhoE_validator": scan(
            SOURCES["iwasawa_rhoE_validator"],
            ["rho_E", "Iwasawa group relations", "selected bundle E", "not selected data"],
        ),
        "iwasawa_riesz_gap_validator": scan(
            SOURCES["iwasawa_riesz_gap_validator"],
            ["Riesz", "selected D_E", "projector", "gap"],
        ),
        "visible_chern_weil_gate": scan(
            SOURCES["visible_chern_weil_gate"],
            ["Chern-Weil", "selected trace normalization", "not a selected visible bundle"],
        ),
    }

    output = {
        "certificate": "SelectedQaSU3ChernBianchiSourcePacketCandidates",
        "status": "QA_SU3_CHERN_BIANCHI_SOURCE_PACKET_CANDIDATES_BUILT_NO_SELECTED_SOURCE",
        "input_status": {
            "source_packet_search": source_search["status"],
        },
        "candidate_packets": candidate_packets,
        "source_checks": source_checks,
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
        "next_required_artifact": {
            "name": "Selected_Qa_SU3_Iwasawa_Abelian_Row_to_Nonabelian_Source_Gate_v1",
            "must_decide": [
                "whether the explicit abelian Iwasawa row can be embedded into a selected nonabelian SU3 source",
                "whether that source has transition data accepted by rho_E validators",
                "whether it yields endomorphism_E or finite determinant data",
            ],
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
