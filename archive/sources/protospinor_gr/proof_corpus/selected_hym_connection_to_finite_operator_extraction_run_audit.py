from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_hym_connection_to_finite_operator_extraction_run_certificate.json"
STATUS = "SELECTED_HYM_CONNECTION_TO_FINITE_OPERATOR_EXTRACTION_RUN_CURRENT_INPUTS_FAIL_SOURCE_FLAGS"
NEXT = "MTT_Selected_HYM_SelectedConnection_or_RouteC_SelectedResidual_ValueSolve_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["theorem"]["proved"] is True, "run no-go theorem should be proved")
    require(all(cert["checks"].values()), "all run checks should pass")
    verdict = cert["verdict"]
    require(verdict["selected_values_emitted"] is False, "selected values must not emit")
    require(verdict["all_validators_pass_honestly"] is False, "all honest validators must not pass yet")
    require({"rhoE_mesh", "rhoE_metric", "sector_maps"}.issubset(set(verdict["pass_set"])), "support passes missing")
    require(
        {"route_c_residuals", "de_action", "riesz_gap", "reduced_green", "dotd_response"}.issubset(
            set(verdict["fail_set"])
        ),
        "expected source/operator failures missing",
    )
    require(verdict["can_emit_A_selected"] is False, "A_selected must remain open")
    require(verdict["can_emit_b_selected"] is False, "b_selected must remain open")
    require(verdict["observed_flavor_data_used"] is False, "observed data must not be used")
    require(verdict["next_required_artifact"] == NEXT, "wrong next artifact")
    require(len(packet["source_flag_failures"]) >= 5, "source/provenance failures should be recorded")
    require("does not emit selected finite operator values" in note and NEXT in note, "note must state boundary")

    print("AUDIT_PASS: extraction run executed; current inputs fail selected-source operator gates")


if __name__ == "__main__":
    main()
