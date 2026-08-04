from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_noninvariant_c1_primitive_search_import_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == "ROUTEC_NONINVARIANT_C1_PRIMITIVE_SEARCH_IMPORTED_UNSELECTED_CANDIDATES_OPEN", "unexpected status")
    require(cert["theorem"]["proved"] is True, "non-invariant C1 search import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["candidate_checks"].values()), "all candidate checks should pass")
    require(all(cert["still_open_checks"].values()), "all still-open checks should pass")
    require(cert["verdict"]["nonzero_C1_candidates_found"] is True, "nonzero candidates should be found")
    require(cert["verdict"]["selected_C1_closed"] is False, "selected C1 must not close")
    require(cert["verdict"]["minimal_active_shift"] == [1, 1], "wrong active shift")
    require(set(map(str, cert["verdict"]["fiber_shifts_tested"])) == {"0", "1", "2", "all"}, "wrong fiber shifts")
    require(cert["verdict"]["fiber_rule_selected"] is False, "fiber rule must remain open")
    require(cert["verdict"]["observed_flavor_data_used"] is False, "must not use observed flavor data")
    require(
        cert["verdict"]["next_required_artifact"] == "MTT_Selected_RouteC_Primitive_Source_Selection_Theorem_or_FiberRule_Audit_v1",
        "wrong next artifact",
    )
    require(packet["calculation_results"]["nonzero_unselected_candidates_found"] == 4, "wrong candidate count")
    require("Selected C1 closure is still false" in note and "No observed Yukawa" in note, "note must state guardrail")

    print("AUDIT_PASS: non-invariant C1 candidates imported; fiber/source selection remains open")


if __name__ == "__main__":
    main()
