"""Decide whether the explicit Iwasawa SU3 monad fills the Qa/SU3 operator packet."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
NONSM_CERTS = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob\certificates")

INPUTS = {
    "operator_packet_interface": CERTS / "color_bundle_operator_packet_interface_certificate.json",
    "operator_packet_fill_attempt": CERTS / "color_bundle_operator_packet_fill_attempt_certificate.json",
    "a01_de_operator_exit_gate": CERTS / "a01_de_operator_exit_gate_certificate.json",
    "ext_stability_source_search": CERTS / "ext_stability_source_search_certificate.json",
}
OPTIONAL_EXTERNAL = {
    "hym_connection_matrix": NONSM_CERTS / "selected_qa_su3_hym_color_connection_spectrum_or_torsion_certificate.json",
    "full_curvature_attempt": NONSM_CERTS / "selected_qa_su3_full_left_invariant_curvature_matrix_attempt_certificate.json",
    "erratum_resolution": NONSM_CERTS / "selected_qa_su3_hym_connection_erratum_or_convention_resolution_certificate.json",
    "mu_operator_domain": NONSM_CERTS / "selected_qa_su3_hym_mu_and_operator_domain_selection_certificate.json",
}
SOURCE_DATA = DATA / "ext_stability_source_search.candidate.json"
OUTPUT_DATA = DATA / "monad_to_operator_packet_transfer_gate.candidate.json"
OUTPUT_CERT = CERTS / "monad_to_operator_packet_transfer_gate_certificate.json"


def load(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def optional_status(path: Path) -> dict[str, object]:
    if not path.exists():
        return {"path": str(path), "present": False, "status": "MISSING"}
    data = load(path)
    return {"path": str(path), "present": True, "status": data.get("status", "UNKNOWN")}


def main() -> None:
    inputs = {name: load(path) for name, path in INPUTS.items()}
    external = {name: optional_status(path) for name, path in OPTIONAL_EXTERNAL.items()}
    source = load(SOURCE_DATA)
    monad = source["monad_computation"]
    packet_transfer = {
        "selected_branch_and_source_certificate": {
            "status": "PARTIAL_PASS",
            "value": "explicit Iwasawa indecomposable rank-three SU3 monad found in strings/flux corpus",
            "evidence": inputs["ext_stability_source_search"]["status"],
            "limitation": "source is not yet identified as the Qa/SU3 threshold determinant source",
        },
        "selected_color_bundle_sheaf_or_twist": {
            "status": "CANDIDATE_PASS_NOT_SELECTED_FOR_THRESHOLD",
            "value": "monad E with c1=0, c2=0, integral c3=6",
            "evidence": monad,
            "limitation": "requires theorem selecting E, End(E), adjoint, or an associated local system as the Qa/SU3 threshold block",
        },
        "operator_domain_after_quotient_rules": {
            "status": "PASS_IMPORTED",
            "value": "p0 and p!=0 quotient constraints imported from packet interface",
            "limitation": "domain constraints do not select representation trace or determinant value",
        },
        "connection_curvature_hym_data": {
            "status": "PARTIAL_EXTERNAL_CONTEXT_ONLY",
            "value": "corpus claims Li-Yau/HYM existence; older repo records A01/erratum gates",
            "evidence": external,
            "limitation": "current repo has no source-certified A01 repair, selected mu, or monad-derived curvature operator",
        },
        "laplace_type_principal_symbol": {
            "status": "OPEN",
            "value": None,
            "limitation": "no selected threshold Laplace-type operator on E, End(E), adjoint, or local-system representation",
        },
        "endomorphism_E_or_heat_zero_order_block": {
            "status": "OPEN",
            "value": None,
            "limitation": "Chern classes, HYM existence, and source context do not compute the Weitzenbock zero-order block",
        },
        "spectrum_heat_torsion_finite_part": {
            "status": "OPEN",
            "value": None,
            "limitation": "no heat table, spectrum, zeta derivative, Ray-Singer torsion, or finite determinant",
        },
        "trace_normalization_and_gauge_quotient": {
            "status": "OPEN",
            "value": None,
            "limitation": "trace must be selected from source data rather than chosen as fundamental, End(E), adjoint, or local-system trace by hand",
        },
    }
    route_decision = [
        {
            "id": "visible_E8_to_E6_benchmark_route",
            "status": "SUPPORTED_AS_SOURCE_CONTEXT_NOT_QA_SU3_CLOSURE",
            "reason": "The monad is framed in the corpus as a heterotic visible-sector construction, not yet as the Qa/SU3 threshold determinant.",
            "can_fill_operator_packet_now": False,
        },
        {
            "id": "direct_Qa_SU3_threshold_source_route",
            "status": "OPEN_REQUIRES_REPRESENTATION_MAP",
            "reason": "No current certificate maps E, End(E), adjoint, or a local-system carrier into the Qa/SU3 determinant trace.",
            "can_fill_operator_packet_now": False,
        },
        {
            "id": "monad_DE_route",
            "status": "OPEN_REQUIRES_TYPED_MAPS_OR_TRANSITIONS",
            "reason": "The monad line classes are known, but selected f,g sections, patching maps, rho_E, and a derived D_E are not supplied.",
            "can_fill_operator_packet_now": False,
        },
        {
            "id": "A01_left_invariant_operator_route",
            "status": "OPEN_REQUIRES_SOURCE_CERTIFIED_ERRATUM_AND_MU",
            "reason": "Older artifacts identify an A01/erratum/mu gate, but this repo cannot accept it as determinant source without source certification.",
            "can_fill_operator_packet_now": False,
        },
        {
            "id": "rhoE_transition_packet_route",
            "status": "OPEN_NO_TRANSITION_PACKET",
            "reason": "A future transition packet could be checked, but the monad has not supplied finite transition matrices.",
            "can_fill_operator_packet_now": False,
        },
    ]
    candidate = {
        "candidate": "SelectedQaSU3MonadToOperatorPacketTransferGate",
        "status": "MONAD_TO_OPERATOR_PACKET_TRANSFER_PARTIAL_SOURCE_FOUND_OPERATOR_OPEN",
        "input_statuses": {name: data.get("status", "UNKNOWN") for name, data in inputs.items()},
        "optional_external_statuses": external,
        "packet_transfer": packet_transfer,
        "route_decision": route_decision,
        "result": {
            "monad_updates_operator_packet": True,
            "selected_source_slot_partially_filled": True,
            "selected_threshold_representation_found": False,
            "rhoE_packet_found": False,
            "D_E_operator_found": False,
            "endomorphism_E_computed": False,
            "determinant_computable_now": False,
            "qa_su3_closed": False,
            "full_sm_closure_achieved": False,
            "target_fitting_used": False,
        },
        "do_not_use": [
            "visible E8-to-E6 monad as Qa/SU3 threshold determinant without representation map",
            "printed A01 matrix as source-certified integrable operator before erratum/mu resolution",
            "mu chosen from Qa/SU3 residual",
            "Chern classes as substitute for endomorphism_E or determinant finite part",
            "hidden abelian Bianchi row as nonabelian determinant",
        ],
        "next_required_artifact": "Selected_Qa_SU3_Source_Certified_A01_Erratum_or_Monad_DE_Operator_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3MonadToOperatorPacketTransferGate",
        "status": "QA_SU3_MONAD_TO_OPERATOR_PACKET_TRANSFER_PARTIAL_SOURCE_FOUND_OPERATOR_OPEN",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "source_slot_partially_filled": True,
            "monad_chern_data_imported": True,
            "operator_transfer_gap_identified": True,
            "forbidden_shortcuts_guarded": True,
        },
        "what_remains_open": {
            "selected_threshold_representation": True,
            "same_source_rhoE_or_DE": True,
            "source_certified_A01_or_monad_DE": True,
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
