from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_selected_c1_operator_source_rebuild_import_certificate.json"
STATUS = "ROUTEC_SELECTED_C1_OPERATOR_SOURCE_REBUILD_IMPORTED_BASISTRANSPORT_NEXT"
NEXT_ARTIFACT = "MTT_Selected_RouteC_BasisTransport_Primitive_Source_Theorem_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "operator-source rebuild import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["ranking_checks"].values()), "all ranking checks should pass")
    require(all(cert["selected_lane_checks"].values()), "all selected-lane checks should pass")
    require(all(cert["support_checks"].values()), "all support checks should pass")
    require(all(cert["open_gate_checks"].values()), "all open-gate checks should pass")
    require(all(cert["still_open_checks"].values()), "all still-open checks should pass")
    require(
        cert["verdict"]["best_next_lane"] == "L3_noninvariant_basis_transport_or_vertex_source",
        "basis-transport lane should be selected",
    )
    require(cert["verdict"]["forced_active_shift"] == [1, 1], "active shift should be 1,1")
    require(cert["verdict"]["fixed_fiber_class_available"] is True, "fiber class should be available")
    require(cert["verdict"]["canonical_zero_lane_retired_for_flavor"] is True, "zero lane should retire")
    require(cert["verdict"]["full_rebuild_fallback_kept"] is True, "full rebuild fallback should remain")
    require(cert["verdict"]["A_selected_emitted"] is False, "A_selected must remain open")
    require(cert["verdict"]["selected_source_theorem_proved"] is False, "source theorem must remain open")
    require(cert["verdict"]["observed_flavor_data_used"] is False, "observed flavor data must not be used")
    require(cert["verdict"]["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    ranked = packet["solution_space_iteration"]["ranked_lanes"]
    require(ranked[0]["score"] > ranked[1]["score"], "top lane should outrank second lane")
    require("L3_noninvariant_basis_transport_or_vertex_source" in note, "note must name selected lane")
    require("no observed targets or lifted flags" in note, "note must state guardrail")

    print("AUDIT_PASS: selected C1 rebuild space imported; basis-transport theorem is next")


if __name__ == "__main__":
    main()
