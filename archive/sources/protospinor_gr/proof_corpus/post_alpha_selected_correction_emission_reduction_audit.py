from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_selected_correction_emission_reduction_certificate.json"
STATUS = "POST_ALPHA_SELECTED_CORRECTION_EMISSION_REDUCED_NONIDENTITY_RHOE_BN_OPEN"
NEXT = "Selected_U1Y_RouteC_NonIdentity_RhoE_and_QuotientValid_BN_Construction_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["diagnostic_splitter_candidate_count"] == 1170, "wrong diagnostic candidate count")
    require(cert["selected_correction_matrix_source_closed"] is False, "selected correction source must remain open")
    require(cert["reduced_to"] == NEXT, "wrong reduction target")
    require(all(cert["checks"].values()), "all certificate checks should pass")

    reduction = packet["reduction"]
    require(reduction["diagnostic_splitter_exists"] is True, "diagnostic splitter should exist")
    require(reduction["diagnostic_splitter_not_promoted"] is True, "diagnostic splitter must remain support")
    require(reduction["formal_lift_rejected_as_proof"] is True, "formal lift must be rejected")
    require(reduction["primitive_only_span_counterexample"] is True, "primitive-only counterexample missing")
    require(reduction["strict_primitive_search_found_no_legal_emission"] is True, "strict primitive no-emission missing")
    require(reduction["selected_correction_matrices_emitted"] is False, "selected correction matrices must remain open")
    require(reduction["selected_payload_values_emitted"] is False, "selected payload values must remain open")

    require(all(item["required"] is True for item in packet["required_payload"].values()), "all payload fields should be required")
    require(all(item["current_status"] == "open" for item in packet["required_payload"].values()), "payload fields should remain open")
    require(packet["acceptance_tests"]["mass_splitting"]["selected_status"] == "open", "mass splitting selected status should be open")
    require(packet["acceptance_tests"]["CKM_or_PMNS_commutator"]["selected_status"] == "open", "commutator selected status should be open")
    require(packet["acceptance_tests"]["CP_odd"]["selected_status"] == "open", "CP selected status should be open")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "diagnostic splitter candidates = 1170" in note, "note missing essentials")

    print("AUDIT_PASS: selected correction emission reduced to nonidentity rhoE and quotient-valid BN")


if __name__ == "__main__":
    main()
