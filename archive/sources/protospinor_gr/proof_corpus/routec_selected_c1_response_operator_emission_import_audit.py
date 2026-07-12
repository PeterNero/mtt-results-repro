from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_selected_c1_response_operator_emission_import_certificate.json"
STATUS = "ROUTEC_SELECTED_C1_RESPONSE_OPERATOR_EMISSION_IMPORTED_A_SELECTED_NOT_EMITTED"
NEXT_ARTIFACT = "MTT_Selected_RouteC_Selected_C1_Operator_Source_or_Galerkin_Rebuild_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "selected C1 response-operator import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["emission_checks"].values()), "all emission checks should pass")
    require(all(cert["schema_checks"].values()), "all schema checks should pass")
    require(all(cert["lane_checks"].values()), "all lane checks should pass")
    require(all(cert["contract_checks"].values()), "all contract checks should pass")
    require(all(cert["open_gate_checks"].values()), "all open-gate checks should pass")
    require(all(cert["still_open_checks"].values()), "all still-open checks should pass")
    require(cert["verdict"]["A_selected_emitted"] is False, "A_selected must not be emitted")
    require(cert["verdict"]["b_selected_emitted"] is False, "b_selected must not be emitted")
    require(cert["verdict"]["selected_operator_schema_audited"] is True, "schema should be audited")
    require(cert["verdict"]["canonical_response_zero"] is True, "canonical response should be zero")
    require(cert["verdict"]["nonzero_unselected_candidates_exist"] is True, "unselected candidates should exist")
    require(cert["verdict"]["rank_test_computable"] is False, "rank test must remain unavailable")
    require(cert["verdict"]["least_squares_computable"] is False, "least squares must remain unavailable")
    require(cert["verdict"]["observed_flavor_data_used"] is False, "observed flavor data must not be used")
    require(cert["verdict"]["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    contract = packet["operator_emission_contract"]
    require(contract["codomain_real_dimension"] == 72, "contract codomain should be 72")
    require("A_selected" in contract["operator_equation"], "contract should name A_selected")
    require("selected C1 response operator is not emitted yet" in note, "note must state non-emission")
    require("canonical smooth B_N C1 response: computed zero" in note, "note must separate lanes")

    print("AUDIT_PASS: selected C1 response operator emission imported; A_selected remains open")


if __name__ == "__main__":
    main()
