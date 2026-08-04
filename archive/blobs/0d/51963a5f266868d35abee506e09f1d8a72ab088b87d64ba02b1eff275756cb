from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_fiberclass_source_target_certificate.json"
STATUS = "POST_ALPHA_FIBERCLASS_SOURCE_TARGET_REDUCED_BASISTRANSPORT_PROOF_OPEN"
NEXT = "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Proof_or_Counterexample_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")
    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(all(cert["checks"].values()), "all certificate checks should pass")
    require(packet["active_shift_result"]["nonzero_active_shifts"] == [[1, 1]], "active shift should be unique")
    require(packet["fiber_class_result"]["fixed_fiber_shifts"] == [0, 1, 2], "fixed shifts should be 0,1,2")
    require(packet["fiber_class_result"]["all_fiber_envelope_retired"] is True, "all-fiber envelope should be retired")
    require(packet["current_layer_observable_invariance"]["proved"] is True, "current-layer invariance should be proved")
    require(packet["selected_next_lane"]["lane"] == "L3_noninvariant_basis_transport_or_vertex_source", "wrong next lane")
    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(STATUS in note and NEXT in note and "shift 0 = computation gauge only" in note, "note missing essentials")
    print("AUDIT_PASS: post-alpha fiber-class source target reduced without flavor overclaim")


if __name__ == "__main__":
    main()
