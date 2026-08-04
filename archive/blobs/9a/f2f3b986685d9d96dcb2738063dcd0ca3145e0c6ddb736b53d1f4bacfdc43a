"""Audit q79 selected trace equality / HYM Newton replay theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP = ROOT / "scripts" / "execute_q79_selected_finite_connection_solve.py"
SCRIPT = (
    ROOT
    / "scripts"
    / "prove_q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay.py"
)
CERT = (
    ROOT
    / "certificates"
    / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay_certificate.json"
)
CANDIDATE = (
    ROOT
    / "candidate_data"
    / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay.candidate.json"
)
OUT_DIR = (
    ROOT / "candidate_data" / "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay"
)
TRACE_PROOF = OUT_DIR / "selected_trace_equality_gap_layer_proof.json"
HYM_ROUTE = OUT_DIR / "full_hym_newton_route_status.json"
BOUNDARY = OUT_DIR / "dotd_c1_response_boundary.open.json"
PAPER = (
    ROOT
    / "proof_corpus"
    / "Q79_Selected_Trace_Equals_Emitted_27Mode_Operator_or_Full_HYM_Newton_Replay_v1.md"
)

STATUS = "Q79_SELECTED_TRACE_EQUALS_EMITTED_27MODE_DE_GAP_LAYER_PROVED_DOTD_C1_OPEN"
NEXT = "Q79_Selected_dotD_Alpha1_C1_Response_Emission_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def run(script: Path, failures: list[str]) -> None:
    proc = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    require(proc.returncode == 0, f"{script.name} failed:\n{proc.stdout}", failures)


def main() -> int:
    failures: list[str] = []
    run(DEP, failures)
    run(SCRIPT, failures)
    for path in (CERT, CANDIDATE, TRACE_PROOF, HYM_ROUTE, BOUNDARY, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    trace = load(TRACE_PROOF)
    hym = load(HYM_ROUTE)
    boundary = load(BOUNDARY)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate differ", failures)
    require(cert["status"] == STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "full closure must stay false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)

    require(
        cert["input_statuses"]["selected_canonical_trace_formula_source_lemma"]["status"]
        == "SELECTED_CANONICAL_TRACE_FORMULA_SOURCE_LEMMA_PROVED_GAP_LAYER_CLOSES",
        "canonical trace lemma not imported",
        failures,
    )
    require(
        cert["input_statuses"]["selected_phifin_s2_gap_layer_honest_replay_lock"]["status"]
        == "SELECTED_PHIFIN_S2_D_E_GAP_LAYER_LOCKED",
        "gap-layer lock not imported",
        failures,
    )

    require(trace["schema"] == "Q79SelectedTraceEqualsEmitted27ModeDEGapLayerProof.v1", "trace schema wrong", failures)
    require(trace["status"] == "SELECTED_TRACE_EQUALITY_AND_DE_GAP_LAYER_PROVED", "trace status wrong", failures)
    for key, step in trace["proof_steps"].items():
        require(step["proved"] is True, f"trace proof step not proved: {key}", failures)
    equality = trace["selected_trace_equality"]
    gap = trace["gap_layer"]
    require(equality["proved"] is True, "selected trace equality not proved", failures)
    require("canonical F3xF3 Fourier Laplacian" in equality["family_sectors"], "family formula wrong", failures)
    require("rank-two projector" in equality["H_sector"], "H sector formula wrong", failures)
    require(equality["zero_cluster_indices"] == [12, 13, 14], "zero cluster indices wrong", failures)
    require(gap["D_E_source_flags_are_theorem_derived"] is True, "D_E flags not theorem-derived", failures)
    require(gap["D_E_honest_replay_passes_after_theorem_derived_source_flags"] is True, "D_E replay lock missing", failures)
    require(gap["Riesz_Green_layer_closes"] is True, "Riesz/Green not closed", failures)
    require(gap["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3", "basis id wrong", failures)
    require(gap["basis_dimension"] == 27, "basis dimension wrong", failures)
    require(gap["selected_eta_N"] == 1.0, "selected eta changed", failures)
    require(gap["selected_eta_N"] < gap["eta_threshold"], "eta threshold not satisfied", failures)
    require(gap["selected_gap_lower_bound"] > 0, "selected gap lower bound not positive", failures)
    require(gap["selected_green_norm_bound"] > 0, "Green norm bound not positive", failures)

    require(hym["schema"] == "Q79FullHYMNewtonReplayRouteStatus.v1", "HYM route schema wrong", failures)
    require(
        hym["status"] == "SCALAR_AND_DIAGONAL_EXPS_SOLVED_FULL_OPERATOR_PAYLOAD_OPEN",
        "HYM route status wrong",
        failures,
    )
    require(hym["scalar_expS"]["selected_scalar_exps_equation_solved"] is True, "scalar expS not solved", failures)
    require(hym["scalar_expS"]["quadratic_exp_density_terms_included"] is True, "scalar quadratic terms missing", failures)
    require(hym["scalar_expS"]["residual_l2"] < 1e-11, "scalar residual too large", failures)
    require(hym["scalar_expS"]["full_connection_lift_open"] is True, "full connection lift should be open", failures)
    require(hym["diagonal_expS"]["diagonal_expS_solution_closed"] is True, "diagonal expS not solved", failures)
    require(hym["diagonal_expS"]["final_residual_l2"] < 1e-11, "diagonal residual too large", failures)
    require(hym["diagonal_expS"]["operator_extraction_ready"] is False, "operator extraction overclaimed", failures)

    require(boundary["schema"] == "Q79SelectedDotDAlpha1C1ResponseBoundary.v1", "boundary schema wrong", failures)
    require(boundary["status"] == "OPEN_DOTD_ALPHA1_C1_RESPONSE_REQUIRED", "boundary status wrong", failures)
    require(
        boundary["carried_forward_from_gap_lock"]["D_E_gap_Riesz_Green_layer_locked"] is True,
        "boundary did not carry D_E lock",
        failures,
    )
    for required in (
        "selected dotD_alpha1 source on the same B_N basis",
        "selected alpha1 driver from the same q79/F,m=1 source",
        "selected primitive or non-invariant C1 tensor",
    ):
        require(required in boundary["required_next_payload"], f"boundary missing requirement: {required}", failures)

    for key in (
        "selected_trace_equality_for_emitted_27mode_DE",
        "D_E_source_flags_theorem_derived",
        "D_E_honest_replay_contract_locked",
        "selected_Riesz_Green_gap_layer_closed",
        "selected_eta_N_below_threshold",
        "positive_selected_gap_lower_bound",
        "scalar_expS_HYM_replay_imported_as_support",
        "diagonal_expS_HYM_replay_imported_as_support",
    ):
        require(cert["what_closes_now"][key] is True, f"close flag false: {key}", failures)

    for key in (
        "dotD_alpha1_source",
        "alpha1_driver",
        "primitive_C1_response",
        "full_S2_value_emission",
        "full_HYM_connection_lift",
        "validator_ready_full_HYM_operator_payload",
        "A_selected",
        "b_selected",
        "Yukawa_or_full_SM_closure",
    ):
        require(cert["what_remains_open"][key] is True, f"remaining flag false: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail violated: {key}", failures)

    theorem = cert["theorem"]
    require(theorem["proved"] is True, "theorem not proved", failures)
    require(theorem["closure_claimed"] is False, "theorem closure overclaimed", failures)
    for phrase in (
        "selected trace equality route is now proved",
        "D_E` gap/Riesz/Green",
        "SelectedCanonicalTraceFormulaSourceLemma",
        "projective-flat connection",
        "H-sector rank-two zero-cluster",
        "selected eta_N",
        "operator extraction ready",
        "dotD_alpha1",
        "Q79SelectedTraceEqualsEmitted27ModeDEGapLayerTheorem",
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 selected trace equality / HYM Newton replay audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 selected trace equality / HYM Newton replay audit PASS")
    print(f"status: {cert['status']}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
