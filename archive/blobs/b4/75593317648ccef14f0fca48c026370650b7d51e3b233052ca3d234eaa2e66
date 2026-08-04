from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_physical_dotd_alpha1_sourcevalues_certificate.json"
STATUS = "PHYSICAL_DOTD_ALPHA1_SOURCE_VALUES_REDUCED_TO_SELECTED_PHIFIN_ALPHA1_PAYLOAD_VALUES_OPEN"
NEXT = "MTT_Selected_PhiFin_Alpha1_Payload_Value_Emission_From_Selected_HYM_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(all(cert["checks"].values()), "all checks should pass")
    require(all(cert["what_closes_now"].values()), "all closure flags should be true")
    require(all(cert["what_remains_open"].values()), "all blockers should remain open")
    require(cert["next_required_artifact"] == NEXT, "wrong next artifact")

    route = packet["direct_alpha1_route"]
    require(route["attempted"] is True, "route should be attempted")
    require(route["closed"] is False, "values must remain open")
    require(route["values_emitted"] is False, "values must not be emitted")
    require(route["reduced_to"] == "SelectedPhiFinAlpha1Payload", "wrong reduction object")
    require(route["source_reduction_closed"] is True, "source reduction should close")
    require(route["direct_values_absent"] is True, "direct absence should be proved")

    status = packet["current_value_status"]
    require(status["evaluated_grad_V_C1_alpha1_source_vector"] is None, "alpha1 source vector must be null")
    require(status["A_selected_emitted"] is False, "A_selected must not be emitted")
    require(status["b_selected_emitted"] is False, "b_selected must not be emitted")
    require(status["selected_operator_available"] is False, "selected operator must be unavailable")
    require(all(value is False for value in status["selected_payload_flags"].values()), "selected payload flags must remain false")
    require(all(value is False for value in status["alpha1_selected_values"].values()), "alpha1 selected values must remain false")

    support = packet["diagnostic_support"]
    require(support["dotD_alpha1_shapes_27x27"] is True, "diagnostic shapes should be retained")
    require(support["alpha1_driver_row_computed"] is True, "alpha1 driver row should be present")
    require(support["single_driver_not_algebraically_fatal"] is True, "rank-lift support missing")

    require(packet["guardrails"]["does_not_promote_diagnostic_dotD_alpha1_shapes"], "diagnostic guardrail missing")
    require(packet["guardrails"]["does_not_emit_A_selected_or_b_selected"], "emission guardrail missing")
    require(STATUS in note and NEXT in note and "SelectedPhiFinAlpha1Payload" in note, "note missing essentials")

    print("AUDIT_PASS: direct physical dotD_alpha1 values reduce to SelectedPhiFinAlpha1Payload; values remain open")


if __name__ == "__main__":
    main()
