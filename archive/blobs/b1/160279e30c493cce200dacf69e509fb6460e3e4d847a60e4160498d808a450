"""Audit the selected diagonal exp(S) HYM replay."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "candidate_data" / "selected_full_exps_hym_newton_replay.candidate.json"
CERT = ROOT / "certificates" / "selected_full_exps_hym_newton_replay_certificate.json"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_Full_ExpS_HYM_Newton_Replay_v1.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    proof = PROOF.read_text(encoding="utf-8")

    require(
        data["status"] == "MTT_SELECTED_DIAGONAL_EXPS_HYM_REPLAY_SOLVED_OFFDIAGONAL_OPERATOR_PAYLOAD_OPEN",
        "unexpected status",
    )
    require(data["closure_claimed"] is False, "must not claim full closure")
    require(data["target_fitting_used"] is False, "must not use target fitting")
    eq = data["nonlinear_equation"]
    require("exp(-2u)" in eq["equation"], "nonlinear exp factor missing")
    require("mean(u)=0" in eq["unknown"], "zero-mean unknown missing")
    solver = data["solver"]
    require(solver["mesh"] == 24, "unexpected mesh")
    require(solver["converged"] is True, "solver should converge")
    require(solver["iterations_run"] < 60, "too many iterations")
    summary = data["solution_summary"]
    require(summary["final_residual_l2"] < 1e-12, "final residual too large")
    require(summary["u_mean_abs"] < 1e-14, "u mean not zero")
    require(summary["u_min"] < 0 < summary["u_max"], "nontrivial correction expected")
    require(max(summary["tail_contraction_ratios"]) < 0.6, "tail contraction weak")
    packet = data["coefficient_packet"]
    require(packet["selected_end0_direction"] == "T3", "wrong End0 direction")
    require(packet["diagonal_expS_solution_closed"] is True, "diagonal replay should close")
    require(packet["operator_extraction_ready"] is False, "operator extraction must remain open")
    require(data["what_closes_now"]["diagonal_expS_nonlinear_replay"] is True, "diagonal closure flag missing")
    require(data["what_remains_open"]["validator_ready_rhoE_DE_Riesz_Green_dotD_payload"] is True, "payload must remain open")
    require(cert["diagonal_expS_solution_closed"] is True, "certificate should close diagonal replay")
    require(cert["operator_extraction_ready"] is False, "certificate must keep extraction open")
    require("not the full validator-ready operator" in proof, "proof must state guardrail")

    print("PASS selected diagonal exp(S) HYM Newton replay audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
