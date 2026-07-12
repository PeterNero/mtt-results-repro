from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_deltatheta_c1_solve_gate_import_certificate.json"
STATUS = "ROUTEC_DELTATHETA_C1_SOLVE_GATE_IMPORTED_SELECTED_RESPONSE_OPERATOR_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_Selected_C1_Response_Operator_Emission_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "DeltaTheta solve gate import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["target_checks"].values()), "all target checks should pass")
    require(all(cert["selected_operator_checks"].values()), "all selected-operator checks should pass")
    require(all(cert["diagnostic_checks"].values()), "all diagnostic checks should pass")
    require(all(cert["open_gate_checks"].values()), "all open-gate checks should pass")
    require(all(cert["still_open_checks"].values()), "all still-open checks should pass")
    require(cert["verdict"]["splitter_target_vector_built"] is True, "target vector should be built")
    require(cert["verdict"]["target_real_dimension"] == 72, "target dimension should be 72")
    require(cert["verdict"]["target_vector_norm_sq"] == 24.0, "target norm should be 24")
    require(cert["verdict"]["selected_operator_available"] is False, "selected operator must remain open")
    require(cert["verdict"]["rank_test_computable"] is False, "rank test must not be computable")
    require(cert["verdict"]["least_squares_solution_computable"] is False, "least-squares must not be computable")
    require(cert["verdict"]["diagnostic_identity_lift_promotable"] is False, "identity lift must not promote")
    require(cert["verdict"]["observed_flavor_data_used"] is False, "observed flavor data must not be used")
    require(cert["verdict"]["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    gate = packet["selected_deltatheta_c1_solve_gate"]
    require("A_selected" in gate["equation"] and "b_splitter" in gate["equation"], "equation should be locked")
    require("A_selected * deltaTheta_C1 = b_splitter" in note, "note must state selected equation")
    require("identity lift is diagnostic only" in note, "note must reject identity lift")

    print("AUDIT_PASS: DeltaTheta C1 solve gate imported; selected response operator remains open")


if __name__ == "__main__":
    main()
