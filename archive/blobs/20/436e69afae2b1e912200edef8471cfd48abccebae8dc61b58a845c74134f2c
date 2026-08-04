from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_hym_correction_and_gauge_projector_value_table_certificate.json"
STATUS = "SELECTED_HYM_FIRST_TRACEFREE_CORRECTION_IMPORTED_FULL_GAUGE_PROJECTOR_OPEN"
NEXT = "MTT_Selected_Full_ExpS_HYM_Newton_Replay_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim full closure")
    require(all(cert["checks"].values()), "all checks should pass")
    require(all(cert["what_closes_now"].values()), "all closure flags should be true")
    require(all(cert["what_remains_open"].values()), "all blockers should remain open")
    require(cert["next_required_artifact"] == NEXT, "wrong next artifact")

    row = packet["row_level_value_table"]
    require(row["row_projector_name"] == "P_eta_00", "wrong row projector")
    require(row["matrix_on_eta00_plus_complement"] == [[1.0, 0.0], [0.0, 0.0]], "projector matrix wrong")
    require(row["full_connection_gauge_projector"] is False, "must not claim full projector")

    correction = packet["first_tracefree_hym_correction"]
    require(correction["first_tracefree_correction_closed"] is True, "first correction should close")
    require(correction["selected_End0_direction"] == "T3", "wrong End0 correction direction")
    require(abs(correction["mean_density"] - 1.0) < 1e-12, "mean density should be one")
    require(correction["poisson_residual_l2"] < 1e-12, "Poisson residual too large")
    require(correction["phi_mean_abs"] < 1e-14, "phi should be zero mean")
    require(correction["full_selected_A_HYM_coefficients_emitted"] is False, "must not emit full HYM")

    gate = packet["full_connection_projector_gate"]
    require(gate["row_projector_values_emitted"] is True, "row projector should be emitted")
    require(gate["full_connection_projector_values_emitted"] is False, "full projector must remain open")
    require("exp(S)" in gate["requires"][0], "must require nonlinear replay")

    guards = packet["guardrails"]
    require(guards["does_not_promote_row_projector_to_full_connection_projector"], "missing row/full guardrail")
    require(guards["does_not_promote_first_poisson_step_to_full_HYM_connection"], "missing HYM guardrail")
    require(guards["keeps_shared_circle_degree_zero_spectator"], "shared circle guardrail missing")
    require(STATUS in note and NEXT in note and "S_1 = phi * T3" in note, "note missing essentials")

    print("AUDIT_PASS: first HYM correction and eta_00 row projector imported; full nonlinear projector remains open")


if __name__ == "__main__":
    main()
