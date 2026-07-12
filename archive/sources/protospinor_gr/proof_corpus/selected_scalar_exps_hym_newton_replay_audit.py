from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_scalar_exps_hym_newton_replay_certificate.json"
STATUS = "SELECTED_SCALAR_EXPS_HYM_REPLAY_CLOSED_FULL_CONNECTION_LIFT_OPEN"
NEXT = "MTT_Selected_ScalarExpS_to_Full_HYM_Operator_Lift_v1"


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

    problem = packet["finite_scalar_exps_problem"]
    require(problem["ansatz"] == "S=s*T3", "wrong ansatz")
    require(problem["mesh"] == 24, "wrong mesh")
    require("rho*exp(-2s)" in problem["equation"], "nonlinear exponential term missing")
    require(problem["coercive_zero_mean_jacobian_lower_bound"] > 39.0, "coercive bound too small")

    solution = packet["solution_summary"]
    require(solution["closed_on_finite_grid"] is True, "scalar replay should close")
    require(solution["residual_l2"] < 1e-12, "residual too large")
    require(solution["s_mean_abs"] < 1e-14, "solution must be zero mean")
    require(solution["s_max"] - solution["s_min"] > 0.1, "solution should be nonconstant")
    require(len(solution["top_nonlinear_source_fourier_modes"]) == 12, "top modes missing")

    guards = packet["guardrails"]
    require(guards["does_not_promote_scalar_diagonal_replay_to_full_HYM_connection"], "missing scalar/full guardrail")
    require(guards["does_not_promote_finite_grid_residual_to_continuum_error_bound"], "missing truncation guardrail")
    require(guards["does_not_use_observed_or_benchmark_data"], "must not use observed data")
    require(STATUS in note and NEXT in note and "rho*exp(-2s)" in note, "note missing essentials")

    print("AUDIT_PASS: selected scalar exp(S) HYM replay closed; full connection lift remains open")


if __name__ == "__main__":
    main()
