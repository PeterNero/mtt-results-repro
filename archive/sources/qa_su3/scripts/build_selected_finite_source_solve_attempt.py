"""Build the selected finite source solve attempt for Qa/SU3."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
NONSM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")

FINITE_GATE = DATA / "finite_cochain_packet_or_de_response_gate.candidate.json"
OUTPUT_DATA = DATA / "selected_finite_source_solve_attempt.candidate.json"
OUTPUT_CERT = CERTS / "selected_finite_source_solve_attempt_certificate.json"

EXTERNAL_CERTS = {
    "repair_b_no_go": NONSM / "certificates" / "selected_qa_su3_repair_b_primitive_correction_no_go_certificate.json",
    "explicit_hym_retirement": NONSM / "certificates" / "selected_qa_su3_explicit_hym_route_retirement_certificate.json",
    "projective_or_endomorphism": NONSM
    / "certificates"
    / "selected_qa_su3_projective_clock_shift_or_endomorphism_route_decision_certificate.json",
    "endomorphism_source_hunt": NONSM
    / "certificates"
    / "selected_qa_su3_endomorphism_source_hunt_after_torsion_no_go_certificate.json",
}


def load_cert(path: Path) -> dict[str, object]:
    if not path.exists():
        return {"present": False, "path": str(path)}
    data = json.loads(path.read_text(encoding="utf-8"))
    data["present"] = True
    data["path"] = str(path)
    return data


def route_result(route_id: str, verdict: str, evidence: list[str], blocks: list[str], next_step: str) -> dict[str, object]:
    return {
        "route_id": route_id,
        "verdict": verdict,
        "evidence": evidence,
        "blocks_closure_now": blocks,
        "next_step": next_step,
    }


def main() -> None:
    finite_gate = json.loads(FINITE_GATE.read_text(encoding="utf-8"))
    external = {name: load_cert(path) for name, path in EXTERNAL_CERTS.items()}
    repair_b = external["repair_b_no_go"]
    hym_retirement = external["explicit_hym_retirement"]
    route_decision = external["projective_or_endomorphism"]
    endomorphism_hunt = external["endomorphism_source_hunt"]
    route_tests = [
        route_result(
            "finite_cochain_product_lane",
            "NOT_FILLED_SELECTED_BASES_AND_PRODUCT_TABLES_MISSING",
            [
                "The current repo carries 11 spaces and five typed products.",
                "No selected finite basis, differential complex, or product table is supplied.",
            ],
            [
                "selected bases absent",
                "selected mu_i absent",
                "selected f,g entries absent",
            ],
            "Construct actual Cech/Dolbeault product tables or derive them from a selected operator packet.",
        ),
        route_result(
            "explicit_hym_matrix_lane",
            "RETIRED_FOR_CURRENT_SOURCE_RECORD",
            [
                hym_retirement.get("status", "missing"),
                "Printed HYM matrix fails integrability; Repair A splits; Repair B needs an unsourced primitive correction.",
            ],
            [
                "printed HYM matrix not a proof source",
                "A/B repairs not source-certified",
            ],
            "Do not use the printed matrix or A/B repairs unless a source-certified erratum reopens them.",
        ),
        route_result(
            "repair_b_primitive_correction_lane",
            "CURRENT_CORPUS_NO_GO",
            [
                repair_b.get("status", "missing"),
                "Required correction has shape -(w1*mu+w3*mu^2) diag(1,-1,0).",
            ],
            [
                "current corpus has endomorphism_E = null",
                "R_+ and abelian flux are not SU3 color Cartan endomorphisms",
                "mu-independent torsion or scalar OU weights cannot supply the required term",
            ],
            "Reopen only with selected Strominger/Dirac/Weitzenbock endomorphism_E or source-certified Repair B curvature.",
        ),
        route_result(
            "projective_clock_shift_lane",
            "AUXILIARY_NOT_SELECTED_THRESHOLD_OPERATOR",
            [
                route_decision.get("status", "missing"),
                "The order-64 projective carrier exists but is not tied to the Qa/SU3 determinant complex.",
            ],
            [
                "projective carrier existence is not torsion/determinant finite part",
                "visible qutrit projective sources do not legally transfer to q64 Qa/SU3",
            ],
            "Promote only with a selected q64 twisted-bundle source acting on the Qa/SU3 operator domain.",
        ),
        route_result(
            "endomorphism_or_threshold_operator_lane",
            "PRIMARY_REMAINING_ROUTE_SOURCE_MISSING",
            [
                endomorphism_hunt.get("status", "missing"),
                "Visible Fu-Yau/Strominger material gives the right template but not selected Qa/SU3 operator data.",
            ],
            [
                "selected endomorphism_E not found",
                "selected Qa/SU3 operator source not found",
                "heat/spectrum/torsion finite part not computed",
            ],
            "Build the selected Qa/SU3 color-bundle/operator packet directly.",
        ),
    ]
    current_sources_close = False
    primary_remaining = "source_certified_endomorphism_E_full_operator"
    candidate = {
        "candidate": "SelectedQaSU3SelectedFiniteSourceSolveAttempt",
        "status": "SELECTED_FINITE_SOURCE_SOLVE_ATTEMPT_CURRENT_CORPUS_NO_GO_OPERATOR_SOURCE_MISSING",
        "input_statuses": {
            "finite_cochain_or_DE_response_gate": finite_gate["status"],
            "repair_b_no_go": repair_b.get("status", "MISSING"),
            "explicit_hym_retirement": hym_retirement.get("status", "MISSING"),
            "projective_or_endomorphism_decision": route_decision.get("status", "MISSING"),
            "endomorphism_source_hunt": endomorphism_hunt.get("status", "MISSING"),
        },
        "external_certificates": {
            name: {"present": cert.get("present", False), "path": cert.get("path"), "status": cert.get("status")}
            for name, cert in external.items()
        },
        "route_tests": route_tests,
        "finite_solve_results": {
            "selected_finite_cochain_packet_supplied": False,
            "selected_DE_dotD_response_supplied": False,
            "explicit_HYM_matrix_route_retired_current_record": hym_retirement.get("verdict", {}).get("explicit_hym_matrix_route_currently_retired") is True,
            "repair_B_current_source_no_go": repair_b.get("verdict", {}).get("repair_B_current_source_no_go") is True,
            "projective_clock_shift_selected_as_proof_source": False,
            "selected_endomorphism_E_found": endomorphism_hunt.get("source_hunt_result", {}).get("selected_endomorphism_E_found") is True,
            "selected_Qa_SU3_operator_source_found": endomorphism_hunt.get("source_hunt_result", {}).get("selected_qa_su3_operator_source_found") is True,
            "current_sources_close_last_part": current_sources_close,
            "qa_su3_packet_closed": False,
            "closure_claimed": False,
        },
        "last_part_resolution": {
            "result": "The selected finite source solve cannot be completed from the current corpus/repo data without adding a new selected operator source.",
            "proved_negative_scope": "current source record only",
            "not_proved": [
                "No theorem says Qa/SU3 closure is mathematically impossible.",
                "A future source-certified erratum, endomorphism_E, or threshold operator can reopen the route.",
            ],
            "primary_remaining_object": primary_remaining,
            "required_packet": [
                "selected Qa/SU3 operator domain after p0 and p!=0 quotient",
                "selected color bundle/sheaf or twisted module",
                "connection/curvature/HYM or Strominger residual data",
                "endomorphism_E or equivalent zero-order Weitzenbock block",
                "spectrum, heat coefficient, analytic torsion, or finite determinant part",
                "same-source bridge to the monad/Cech packet if the cochain lane is used",
            ],
        },
        "decision": {
            "result": "Last part attempted and blocked by an explicit current-source no-go.",
            "why": "Every available route either lacks selected cochain products, is retired as an HYM proof source, is auxiliary only, or lacks selected endomorphism/operator data.",
            "next_move": "Construct Selected_Qa_SU3_Color_Bundle_Operator_Packet_Interface_v1 and fill it with a real selected threshold operator.",
        },
        "next_required_artifact": "Selected_Qa_SU3_Color_Bundle_Operator_Packet_Interface_v1",
        "target_fitting_used": False,
    }
    certificate = {
        "certificate": "SelectedQaSU3SelectedFiniteSourceSolveAttempt",
        "status": "QA_SU3_SELECTED_FINITE_SOURCE_SOLVE_ATTEMPT_CURRENT_CORPUS_NO_GO_OPERATOR_SOURCE_MISSING",
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "selected_finite_source_solve_attempted": True,
            "finite_cochain_lane_not_filled": True,
            "explicit_HYM_matrix_route_retired_current_record": candidate["finite_solve_results"]["explicit_HYM_matrix_route_retired_current_record"],
            "repair_B_current_source_no_go_imported": candidate["finite_solve_results"]["repair_B_current_source_no_go"],
            "projective_clock_shift_auxiliary_only": True,
            "primary_remaining_route_identified": primary_remaining,
        },
        "what_remains_open": {
            "selected_Qa_SU3_operator_source": True,
            "selected_endomorphism_E_or_equivalent_threshold_operator": True,
            "heat_spectrum_torsion_or_determinant_finite_part": True,
            "same_source_bridge_to_monad_or_cochain_packet": True,
            "qa_su3_packet_closed": False,
        },
        "negative_scope": candidate["last_part_resolution"]["proved_negative_scope"],
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
