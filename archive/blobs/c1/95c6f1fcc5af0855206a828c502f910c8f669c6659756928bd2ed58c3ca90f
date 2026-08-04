"""Audit the first selected HYM correction coefficient solve."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_nonlinear_hym_correction_coefficient_solve.candidate.json"
CERT = ROOT / "certificates" / "selected_nonlinear_hym_correction_coefficient_solve_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_Nonlinear_HYM_Correction_Coefficient_Solve_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_HYM_FIRST_TRACEFREE_CORRECTION_SOLVED_FULL_NONLINEAR_NEWTON_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim full closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    finite = data["finite_problem"]
    require(finite["mesh"] == 24, "unexpected mesh")
    require(abs(finite["mean_density"] - 1.0) < 1e-12, "unit density mean not one")
    require(finite["correction_interpretation"].startswith("S_1 = phi * T3"), "wrong correction direction")
    solution = data["solution_summary"]
    require(solution["first_tracefree_correction_closed"] is True, "first correction should close")
    require(solution["poisson_residual_l2"] < 1e-12, "Poisson residual too large")
    require(solution["phi_mean_abs"] < 1e-14, "phi not zero mean")
    require(len(solution["top_source_fourier_modes"]) == 12, "top modes not emitted")
    packet = data["coefficient_packet"]
    require(packet["selected_end0_direction"] == "T3", "wrong End0 direction")
    require(packet["continuous_parameters_added"] == 0, "must not add parameters")
    nonlinear = data["nonlinear_newton_status"]
    require(nonlinear["first_tracefree_poisson_step_solved"] is True, "Poisson step should solve")
    require(nonlinear["full_expS_nonlinear_iteration_run"] is False, "full nonlinear replay must remain open")
    require(nonlinear["newton_ready_for_operator_extraction"] is False, "operator extraction must remain blocked")
    require(cert["first_tracefree_correction_closed"] is True, "certificate should close first correction")
    require(cert["full_selected_A_HYM_coefficients_emitted"] is False, "certificate must not emit full HYM")
    require("not yet the full nonlinear HYM connection" in proof, "proof must state guardrail")

    print("PASS selected nonlinear HYM correction coefficient solve audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
