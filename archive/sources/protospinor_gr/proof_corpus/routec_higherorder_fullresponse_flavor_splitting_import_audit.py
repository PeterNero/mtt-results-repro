from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "routec_higherorder_fullresponse_flavor_splitting_import_certificate.json"
STATUS = "ROUTEC_HIGHERORDER_FULLRESPONSE_FLAVOR_SPLITTING_IMPORTED_VALUES_OPEN"
NEXT_ARTIFACT = "MTT_Selected_RouteC_First_Selected_Correction_Matrix_Search_or_Galerkin_Run_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "flavor-splitting import theorem should be proved")
    require(all(cert["closed_now"].values()), "all closed-now checks should pass")
    require(all(cert["current_layer_checks"].values()), "all current-layer checks should pass")
    require(all(cert["criterion_checks"].values()), "all criterion checks should pass")
    require(all(cert["open_gate_checks"].values()), "all open-gate checks should pass")
    require(all(cert["still_open_checks"].values()), "all still-open checks should pass")
    require(cert["verdict"]["current_layer_no_go_proved"] is True, "current layer no-go should be proved")
    require(
        cert["verdict"]["higher_order_splitting_criterion_locked"] is True,
        "higher-order criterion should be locked",
    )
    require(
        cert["verdict"]["full_response_acceptance_tests_locked"] is True,
        "full-response tests should be locked",
    )
    require(cert["verdict"]["selected_correction_values_computed"] is False, "values must remain open")
    require(cert["verdict"]["physical_flavor_closure_claimed"] is False, "flavor closure must not be claimed")
    require(cert["verdict"]["observed_flavor_data_used"] is False, "observed flavor data must not be used")
    require(cert["verdict"]["next_required_artifact"] == NEXT_ARTIFACT, "wrong next artifact")

    path_a = packet["path_A_higher_order_criterion"]
    path_b = packet["path_B_full_response_criterion"]
    require("traceless" in path_a["mass_splitting_condition"], "mass criterion should use traceless part")
    require("commutator" in path_a["mixing_condition"], "mixing criterion should use commutator")
    require(all(path_b["required_outputs"].values()), "all full-response outputs should be required")
    require("No selected correction values are computed here" in note, "note must state values-open boundary")
    require("No observed masses" in note, "note must state target-fitting guardrail")

    print("AUDIT_PASS: higher-order/full-response flavor criteria imported; selected values remain open")


if __name__ == "__main__":
    main()
