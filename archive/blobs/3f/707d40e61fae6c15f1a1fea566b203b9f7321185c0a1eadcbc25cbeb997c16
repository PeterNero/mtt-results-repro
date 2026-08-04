from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_fiberclass_c1_observable_quotient_certificate.json"
STATUS = "POST_ALPHA_FIBERCLASS_C1_OBSERVABLE_QUOTIENT_CLOSED_FULL_RESPONSE_OPEN"
NEXT = "Selected_U1Y_RouteC_PrimitiveClass_C1Observable_or_HigherOrderFullResponse_SourceEmission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim full closure")
    require(cert["quotient_closed_for_current_spectral_observables"] is True, "quotient should close")
    require(cert["full_C1_matrix_representative_selected"] is False, "full representative must remain open")
    require(cert["reduced_to"] == NEXT, "wrong reduction target")
    require(all(cert["checks"].values()), "all certificate checks should pass")

    quotient = packet["quotient_theorem"]
    require(quotient["active_shift_selected"] is True, "active shift should be selected")
    require(quotient["selected_active_shift"] == [1, 1], "wrong selected active shift")
    require(quotient["fiber_class_quotient_selected"] is True, "fiber quotient should be selected")
    require(quotient["fixed_fiber_class"] == [0, 1, 2], "wrong fixed fiber class")
    require(quotient["computation_representative"] == "fiber_shift_0", "wrong computation representative")
    require(quotient["absolute_fiber_shift_selected"] is False, "absolute fiber shift must remain unselected")
    require(quotient["absolute_fiber_origin_not_hidden_knob"] is True, "hidden knob guard missing")

    spectral = packet["spectral_observable_summary"]
    require(spectral["rank_invariant"] is True, "rank should be invariant")
    require(spectral["YYstar_scalar_identity_invariant"] is True, "YYstar scalar should be invariant")
    require(spectral["current_layer_flavor_splitting_possible"] is False, "current layer should not split flavor")

    boundary = packet["downstream_boundary"]
    require(boundary["can_promote_fixed_fiber_representative_for_current_spectral_observables"] is True, "spectral representative should be usable")
    require(boundary["can_promote_fixed_fiber_representative_for_full_C1_matrix_operator"] is False, "full matrix representative must remain open")
    require(boundary["can_compute_yukawa_hierarchy"] is False, "Yukawa hierarchy should remain open")
    require(boundary["can_compute_CKM_PMNS_CP"] is False, "mixing/CP should remain open")

    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "computation representative = fiber_shift_0" in note, "note missing essentials")

    print("AUDIT_PASS: fiber-class C1 spectral quotient closed; full response remains open")


if __name__ == "__main__":
    main()
