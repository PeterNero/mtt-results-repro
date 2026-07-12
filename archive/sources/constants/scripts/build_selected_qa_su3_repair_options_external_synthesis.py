"""Synthesize the Qa/SU3 source-augmentation repair options.

This imports only audited local artifacts plus bibliographic external anchors.
It does not claim that external papers select MTT data; they only justify which
mathematical container is appropriate for each route.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
OUTPUT_CERT = CERTS / "selected_qa_su3_repair_options_external_synthesis_certificate.json"

QA_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof")
Q79_REPO = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")


INPUT_CERTS = {
    "current_fill_attempt": CERTS / "selected_qa_su3_source_augmentation_packet_fill_attempt_certificate.json",
    "current_source_interface": CERTS / "selected_qa_su3_source_augmentation_iwasawa_monad_maps_interface_certificate.json",
    "qa_phiq_obstruction": QA_REPO / "certificates" / "phiq_ansatz_solver_or_gerbe_obstruction_certificate.json",
    "qa_gerbe_twist_cancellation": QA_REPO / "certificates" / "gerbe_twist_cancellation_packet_certificate.json",
    "q79_iwasawa_discrete_gerbe": Q79_REPO / "certificates" / "iwasawa_discrete_gerbe_holonomy_candidate_certificate.json",
    "q79_selected_gerbe_fourier": Q79_REPO / "certificates" / "selected_gerbe_fourier_type_theorem_certificate.json",
}

EXTERNAL_ANCHORS = [
    {
        "id": "iwasawa_complex_geometry",
        "url": "https://arxiv.org/abs/1710.02180",
        "role": "Confirms the Iwasawa manifold is a compact quotient of the complex Heisenberg/unipotent group by a lattice; supports the need for nilmanifold, not purely torus, data.",
    },
    {
        "id": "appell_humbert_torus_line_bundles",
        "url": "https://en.wikipedia.org/wiki/Appell%E2%80%93Humbert_theorem",
        "role": "Explains why torus pullback factors can model ordinary closed ab directions, but not the full nonabelian/c-axis Iwasawa problem.",
    },
    {
        "id": "nil_theta_functions",
        "url": "https://www.ams.org/tran/2010-362-02/S0002-9947-09-04852-1/",
        "role": "Supports nil-theta/Heisenberg harmonic analysis as the right type of ordinary-section machinery if a closed full nil representative is supplied.",
    },
    {
        "id": "kapustin_b_field_twisted_bundles",
        "url": "https://arxiv.org/abs/hep-th/9909089",
        "role": "Supports the physical legitimacy of twisted Chan-Paton/projective bundles in a topologically nontrivial B-field.",
    },
    {
        "id": "holonomy_on_dbranes",
        "url": "https://arxiv.org/abs/hep-th/0204199",
        "role": "Supports Deligne cohomology and bundle-gerbe descriptions of D-brane/Chan-Paton holonomy.",
    },
    {
        "id": "bundle_gerbe_modules",
        "url": "https://ncatlab.org/nlab/show/bundle+gerbe+module",
        "role": "Supports the interpretation of a gerbe module as the geometric presentation of a twisted bundle.",
    },
]


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    inputs = {name: load(path) for name, path in INPUT_CERTS.items()}
    fill = inputs["current_fill_attempt"]["fill_result"]
    obstruction = inputs["qa_phiq_obstruction"]
    gerbe_twist = inputs["qa_gerbe_twist_cancellation"]
    discrete_gerbe = inputs["q79_iwasawa_discrete_gerbe"]
    selected_gerbe = inputs["q79_selected_gerbe_fourier"]

    routes = [
        {
            "id": "ordinary_line_bundle_full_nil_theta",
            "status": "CONDITIONALLY_RETIRED_UNLESS_C_SOURCE_AMENDED",
            "evidence": [
                "Current fill attempt leaves automorphy, section ring, f/g, and operator exit open.",
                "Phi_q obstruction certificate reports eight c-axis obstructed spaces out of eleven.",
                "External Appell-Humbert style torus factors support only ordinary closed torus directions without extra nil data.",
            ],
            "can_close_now": False,
            "revival_condition": "source-amended closed c representative plus full nil-theta section bases and products",
        },
        {
            "id": "source_certified_direct_operator_exit",
            "status": "LIVE_BUT_NO_CURRENT_SOURCE_EXIT",
            "evidence": [
                "It would bypass individual section factors if a selected D_E/rho_E packet were printed or derived.",
                "Current fill attempt and transfer gates report no D_E, rho_E, Cech, or Dolbeault finite operator exit.",
            ],
            "can_close_now": False,
            "revival_condition": "source-certified corrected A01/D_E or rho_E packet with finite determinant/torsion response",
        },
        {
            "id": "projective_gerbe_twisted_module",
            "status": "PRIMARY_SOLUTION_CANDIDATE_SOURCE_SELECTION_OPEN",
            "evidence": [
                "Gerbe twist cancellation packet closes all Fi/Gi c-twist cancellation products to untwisted P.",
                "q79 repo supplies a closed finite Z3 discrete-gerbe holonomy candidate, but selection and smooth/source promotion remain open.",
                "Selected gerbe Fourier type is proved up to orientation/ordered packet, but selected D_E/dotD remains open.",
                "External B-field/Chan-Paton and bundle-gerbe references support this as the correct mathematical container.",
            ],
            "can_close_now": False,
            "what_it_solves_now": [
                "literal nonclosed c obstruction at the monad product-typing level",
                "ordinary c-axis line-bundle requirement is replaced by opposite twists on F_i and G_i",
                "P sector remains untwisted because c(F_i)+c(G_i)=0 for every product",
            ],
            "remaining_gate": "selected Deligne/Cech or B-field representative, twisted section ring, Freed-Witten/Bianchi check, projector retention, and D_E/rho_E finite part",
        },
    ]

    recommendation = {
        "primary_next_route": "projective_gerbe_twisted_module",
        "why": (
            "It is the only route that solves the c-axis obstruction without asking the "
            "source to reinterpret a nonclosed literal c form as an ordinary first Chern class."
        ),
        "next_required_artifact": "Selected_Qa_SU3_Twisted_Section_Ring_and_Gerbe_Source_Gate_v1",
        "first_packet_to_build": {
            "selected_twist": "Z3/finite-Heisenberg gerbe representative or source-selected smooth lift",
            "ordinary_ab_part": "Appell-Humbert style closed a,b line-bundle factors",
            "twisted_spaces": "F_i and G_i as ordinary_ab factors tensored by c twist +/-1 or 0",
            "multiplication": "twisted product constants with c twist cancellation into P",
            "checks": [
                "Deligne/Cech cocycle or B-field period table",
                "Freed-Witten and Green-Schwarz/Bianchi admissibility",
                "twisted section basis dimensions and product constants",
                "operator retention and D_E/rho_E finite response",
            ],
        },
    }

    output = {
        "certificate": "SelectedQaSU3RepairOptionsExternalSynthesis",
        "status": "QA_SU3_REPAIR_OPTIONS_SYNTHESIZED_GERBE_ROUTE_PRIMARY_VALUES_OPEN",
        "input_status": {name: cert.get("status", "UNKNOWN") for name, cert in inputs.items()},
        "external_anchors": EXTERNAL_ANCHORS,
        "local_evidence_summary": {
            "current_fill_no_closure": fill["qa_su3_closed"] is False and fill["target_fitting_used"] is False,
            "ordinary_c_axis_obstruction": obstruction["what_closes"]["literal_c_nonclosed_check"],
            "c_axis_obstructed_spaces": obstruction["counts"]["c_axis_obstructed_spaces"],
            "gerbe_twist_products_close": gerbe_twist["what_closes"]["all_Fi_Gi_c_twists_cancel_to_P"],
            "finite_z3_gerbe_candidate_closed": discrete_gerbe["what_this_closes"]["candidate_zeta3_holonomy_map"],
            "selected_gerbe_fourier_type_closed": selected_gerbe["calculation_results"]["selected_gerbe_fourier_type_closed"],
            "selected_operator_still_open": selected_gerbe["still_open"]["selected_D_E_dotD_or_monad_source_for_matter_slots"],
        },
        "routes": routes,
        "recommendation": recommendation,
        "verdict": {
            "solution_found_at_typing_level": True,
            "full_packet_closed": False,
            "best_solution_candidate": "ordinary_ab_line_bundles_plus_c_gerbe_twist_cancellation",
            "ordinary_line_bundle_route_should_not_be_used_as_proof_source_now": True,
            "direct_operator_exit_available_now": False,
            "target_fitting_used": False,
        },
    }
    text = json.dumps(output, indent=2, sort_keys=True)
    if "--write-certificate" in __import__("sys").argv:
        OUTPUT_CERT.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
