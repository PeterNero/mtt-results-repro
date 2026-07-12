from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_primitive_source_selection_audit_import_certificate.json"
STATUS = "ROUTEC_PRIMITIVE_SOURCE_SELECTION_AUDIT_IMPORTED_ACTIVE_SHIFT_FORCED_FIBER_CLASS_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_FiberClass_Observable_Invariance_or_GaugeFix_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "source-selection import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["active_shift_checks"].values()), "all active-shift checks should pass")
    require(all(cert["fixed_fiber_checks"].values()), "all fixed-fiber checks should pass")
    require(all(cert["envelope_checks"].values()), "all envelope checks should pass")
    require(all(cert["open_gate_checks"].values()), "all open-gate checks should pass")
    require(all(cert["still_open_checks"].values()), "all still-open checks should pass")
    require(cert["verdict"]["active_shift_forced"] is True, "active shift should be forced")
    require(cert["verdict"]["forced_active_shift"] == [1, 1], "wrong forced active shift")
    require(cert["verdict"]["fixed_fiber_class_reduced"] is True, "fixed fiber class should reduce")
    require(cert["verdict"]["fixed_fiber_shifts"] == [0, 1, 2], "wrong fixed fiber shifts")
    require(cert["verdict"]["all_fiber_envelope_retired"] is True, "all-fiber envelope should be retired")
    require(cert["verdict"]["all_fiber_envelope_rank"] == 1, "all-fiber envelope should be rank one")
    require(cert["verdict"]["absolute_fiber_origin_selected"] is False, "absolute fiber origin must remain open")
    require(cert["verdict"]["observable_invariance_proved"] is False, "observable invariance must remain open")
    require(cert["verdict"]["selected_C1_source_closed"] is False, "selected C1 source must remain open")
    require(cert["verdict"]["observed_flavor_data_used"] is False, "observed flavor data must not be used")
    require(cert["verdict"]["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    fixed = packet["fiber_class_theorem"]["fixed_fiber_shifts"]
    require(
        all(all(rank == 3 for rank in ranks.values()) for ranks in fixed["ranks"].values()),
        "fixed fiber ranks should all be three",
    )
    require(
        packet["fiber_class_theorem"]["all_fiber_envelope"]["support_pattern_u"]
        == [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
        "all-fiber envelope should have all-ones support",
    )
    require("does not select an absolute fiber origin" in note, "note must state absolute-origin boundary")
    require("No observed Yukawa" in note, "note must state flavor-data guardrail")

    print("AUDIT_PASS: Route-C active shift forced; fixed fiber class reduced; C1 source remains open")


if __name__ == "__main__":
    main()
