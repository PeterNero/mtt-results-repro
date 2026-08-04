from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_noninvariant_c1_fiberclass_certificate.json"
STATUS = "POST_ALPHA_NONINVARIANT_C1_FIBERCLASS_SPECTRAL_QUOTIENT_CLOSED_FULL_RESPONSE_OPEN"
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
    require(cert["active_shift_selected"] is True, "active shift should close")
    require(cert["fiberclass_spectral_quotient_closed"] is True, "spectral quotient should close")
    require(cert["full_matrix_representative_selected"] is False, "full representative should remain open")
    require(cert["current_layer_flavor_splitting_possible"] is False, "current layer should be degenerate")
    require(all(cert["checks"].values()), "all checks should pass")
    require(packet["theorem"]["proved"] is True, "theorem should be proved")
    require(packet["status"] == STATUS, "packet status mismatch")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(packet["quotient_theorem"]["selected_active_shift"] == [1, 1], "wrong active shift")
    require(packet["quotient_theorem"]["fixed_fiber_class"] == [0, 1, 2], "wrong fiber class")
    require(packet["quotient_theorem"]["absolute_fiber_shift_selected"] is False, "absolute fiber origin overclaimed")
    require(packet["spectral_observable_summary"]["YYstar_scalar_identity_invariant"] is True, "spectral invariant missing")
    require(packet["spectral_observable_summary"]["current_layer_flavor_splitting_possible"] is False, "flavor split overclaimed")
    require(packet["downstream_boundary"]["can_compute_yukawa_hierarchy"] is False, "yukawa hierarchy overclaimed")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "scalar-permutation degenerate" in note, "note missing essentials")
    print("AUDIT_PASS: noninvariant C1 fiberclass spectral quotient closed; full response remains open")


if __name__ == "__main__":
    main()
