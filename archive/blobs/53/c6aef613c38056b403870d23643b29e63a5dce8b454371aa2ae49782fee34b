from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_dotd_alpha1_c1_response_certificate.json"
STATUS = "POST_ALPHA_DOTD_ALPHA1_C1_RESPONSE_ALPHA_REPLAY_CLOSED_PRIMITIVE_C1_OPEN"
NEXT = "Selected_U1Y_RouteC_Primitive_C1_Contractions_or_Lambda12_Gate_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim full closure")
    require(cert["alpha1_driver_verified_locally"] is True, "local alpha1 closure should carry forward")
    require(cert["selected_dotD_source_verified_locally"] is True, "local dotD source closure should carry forward")
    require(cert["C1_response_operator_emitted"] is False, "C1 response operator must remain open")
    require(cert["reduced_to"] == NEXT, "wrong reduction target")
    require(all(cert["checks"].values()), "all certificate checks should pass")

    require(packet["theorem"]["proved"] is True, "theorem should be proved")
    require(packet["alpha_reconciliation"]["sibling_packet_alpha_flags_stale_locally"] is True, "stale alpha flags not recorded")
    require(packet["alpha_reconciliation"]["local_alpha1_driver_verified"] is True, "alpha driver not reconciled")
    require(packet["alpha_reconciliation"]["local_selected_dotD_source_verified"] is True, "dotD source not reconciled")
    require(packet["alpha_reconciliation"]["local_honest_dotD_replay_without_lifted_flags"] is True, "honest replay not reconciled")
    require(packet["decision"]["same_branch_alpha1_driver_proved"] is True, "reconciled alpha decision not true")
    require(packet["decision"]["selected_dotD_source_theorem_proved"] is True, "reconciled dotD decision not true")
    require(packet["decision"]["C1_response_operator_emitted"] is False, "C1 should not be emitted")
    require(packet["decision"]["A_selected_emitted"] is False, "A_selected should not be emitted")
    require(packet["decision"]["b_selected_emitted"] is False, "b_selected should not be emitted")
    require(packet["decision"]["sector_response_matrices_emitted"] is False, "sector response matrices should not be emitted")
    require(packet["decision"]["lambda_12_computable"] is False, "lambda12 should not be computable")

    require(packet["carried_forward"]["same_basis_nonzero_dotD_value_packet"]["status"] == "VALUE_PACKET_AVAILABLE_NOT_SOURCE_THEOREM", "wrong dotD value packet status")
    require(packet["carried_forward"]["canonical_smooth_bn_response"]["status"] == "COMPUTED_ZERO_RESPONSE", "canonical response status changed")
    require(packet["carried_forward"]["noninvariant_candidate_response"]["usable_as_proof"] is False, "noninvariant candidates must not be proof")

    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "alpha1_driver_verified = true" in note, "note missing essentials")

    print("AUDIT_PASS: post-alpha dotD/C1 frontier reconciled; primitive C1 payload remains open")


if __name__ == "__main__":
    main()
