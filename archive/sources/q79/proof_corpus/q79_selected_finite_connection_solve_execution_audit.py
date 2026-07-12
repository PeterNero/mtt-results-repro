"""Audit q79 selected finite connection solve execution."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP = ROOT / "scripts" / "analyze_q79_typed_monad_cech_or_hym_connection_witness.py"
SCRIPT = ROOT / "scripts" / "execute_q79_selected_finite_connection_solve.py"
CERT = ROOT / "certificates" / "q79_selected_finite_connection_solve_execution_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_selected_finite_connection_solve_execution.candidate.json"
OUT_DIR = ROOT / "candidate_data" / "q79_selected_finite_connection_solve_execution"
IMPORT_SUMMARY = OUT_DIR / "finite_connection_execution_import_summary.json"
ATTEMPT = OUT_DIR / "selected_finite_connection_execution_attempt.open.json"
CUTSET = OUT_DIR / "honest_replay_cutset.json"
CONTRACT = OUT_DIR / "selected_trace_or_full_hym_source_contract.open.json"
PAPER = ROOT / "proof_corpus" / "Q79_Selected_Finite_Connection_Solve_Execution_v1.md"

STATUS = "Q79_SELECTED_FINITE_CONNECTION_SOLVE_EXECUTED_PREFIX_VALUES_SOURCE_TRACE_OPEN"
NEXT = "Q79_Selected_Trace_Equals_Emitted_27Mode_Operator_or_Full_HYM_Newton_Replay_v1"


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
    for path in (CERT, CANDIDATE, IMPORT_SUMMARY, ATTEMPT, CUTSET, CONTRACT, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    summary = load(IMPORT_SUMMARY)
    attempt = load(ATTEMPT)
    cutset = load(CUTSET)
    contract = load(CONTRACT)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate differ", failures)
    require(cert["status"] == STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must stay false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)
    require(
        cert["prior_witness_status"] == "Q79_TYPED_MONAD_CECH_OR_HYM_CONNECTION_WITNESS_ATTEMPT_OPEN_VALUES_ABSENT",
        "prior witness status not imported",
        failures,
    )

    require(summary["status"] == "FINITE_PREFIX_VALUES_IMPORTED_SOURCE_PROMOTION_OPEN", "summary status wrong", failures)
    rhoe = summary["nonidentity_rhoE"]
    bn = summary["smooth_BN"]
    de = summary["DE"]
    dotd = summary["dotD"]
    c1 = summary["C1"]
    hym = summary["first_HYM_correction"]

    require(rhoe["nonidentity_projective_rhoE_candidate_built"] is True, "nonidentity rhoE missing", failures)
    require(rhoe["identity_smoke_replaced"] is True, "identity smoke not replaced in imported prefix", failures)
    require(rhoe["rank"] == 3, "rhoE rank wrong", failures)
    require(rhoe["nonidentity_norm"] and rhoe["nonidentity_norm"] > 1.0, "rhoE nonidentity norm too small", failures)
    require(rhoe["projective_commutator_residual"] < 1e-12, "projective commutator residual too large", failures)
    require(rhoe["selected_by_mtt"] is False, "rhoE should not be selected yet", failures)

    require(bn["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3", "basis id wrong", failures)
    require(bn["dimension"] == 27, "BN dimension wrong", failures)
    require(bn["zero_cluster_dimension"] == 3, "zero cluster dimension wrong", failures)
    require(bn["complement_gap"] > 0, "complement gap not positive", failures)
    require(bn["smooth_scalar_basis_functions_phi_m_emitted"] is True, "smooth basis not emitted", failures)
    require(bn["gram_stiffness_emitted"] is True, "Gram/stiffness not emitted", failures)

    require(de["D_E_matrix_on_27_mode_BN_emitted"] is True, "D_E matrix not emitted", failures)
    require(de["family_kernel_dimension"] == 3, "family kernel dimension wrong", failures)
    require(de["higgs_kernel_dimension"] == 1, "Higgs kernel dimension wrong", failures)
    require(
        de["honest_validator_fails_only_by_selected_source_flags"] is True,
        "D_E honest failure should be source flags",
        failures,
    )

    require(dotd["sector_projectors_on_27_mode_BN_emitted"] is True, "sector projectors missing", failures)
    require(dotd["dotD_alpha1_matrix_in_same_basis_emitted"] is True, "dotD alpha1 missing", failures)
    require(dotd["diagnostic_lift_validator_passes"] is True, "dotD diagnostic should pass", failures)
    require(
        dotd["honest_validator_fails_only_by_source_driver_flags"] is True,
        "dotD honest failure should be source/driver flags",
        failures,
    )
    require(dotd["projector_ranks"]["H"] == 1.0, "H projector rank wrong", failures)
    for sector in ("Q", "u", "d", "L", "e", "N"):
        require(dotd["projector_ranks"][sector] == 3.0, f"{sector} projector rank wrong", failures)

    require(c1["primitive_C1_contraction_engine_built"] is True, "C1 engine missing", failures)
    require(c1["canonical_tensor_zero_response_result_proved_finitely"] is True, "C1 zero no-go missing", failures)
    require(c1["all_c1_matrices_zero_for_canonical_tensor"] is True, "canonical C1 should be zero", failures)

    require(hym["first_tracefree_hym_density_source_computed"] is True, "first HYM correction missing", failures)
    require(hym["selected_End0_direction"] == "T3", "selected End0 direction changed", failures)
    require(hym["poisson_residual_l2"] < 1e-12, "HYM Poisson residual too large", failures)
    require(hym["full_selected_A_HYM_coefficients_open"] is True, "full HYM coefficients should be open", failures)

    require(attempt["schema"] == "Q79SelectedFiniteConnectionSolveExecutionAttempt.v1", "attempt schema wrong", failures)
    require(attempt["status"] == "FINITE_VALUES_EXECUTED_SELECTED_SOURCE_TRACE_OPEN", "attempt status wrong", failures)
    require(all(attempt["finite_values_present"].values()), "not all finite values marked present", failures)
    require(attempt["selected_promotion"]["rhoE_selected_by_mtt"] is False, "rhoE promotion overclaimed", failures)
    require(attempt["selected_promotion"]["selected_trace_equality"] is False, "trace equality overclaimed", failures)
    require(
        attempt["selected_promotion"]["selected_finite_connection_solve_closed"] is False,
        "selected finite solve overclosed",
        failures,
    )
    require(attempt["closure_claimed"] is False, "attempt closure must stay false", failures)

    require(cutset["schema"] == "Q79SelectedFiniteConnectionHonestReplayCutset.v1", "cutset schema wrong", failures)
    require(
        cutset["status"] == "HONEST_REPLAY_BLOCKED_BY_SOURCE_TRACE_AND_FULL_OPERATOR_PROVENANCE",
        "cutset status wrong",
        failures,
    )
    for key, value in cutset["open_items"].items():
        require(value is True, f"cutset open item not true: {key}", failures)

    require(contract["schema"] == "Q79SelectedTraceOrFullHYMSourceContract.v1", "contract schema wrong", failures)
    require(contract["status"] == "OPEN", "contract status wrong", failures)
    require(
        set(contract["accepted_closing_routes"])
        == {"finite_trace_identification", "full_HYM_Newton_replay", "typed_monad_Cech_payload"},
        "contract route set wrong",
        failures,
    )
    for forbidden in (
        "selected flags added by diagnostic lift",
        "observed masses, CKM magnitudes, or benchmark Yukawa entries",
        "identity rho_E smoke",
    ):
        require(forbidden in contract["must_not_use"], f"forbidden input missing: {forbidden}", failures)

    for key in (
        "identity_rhoE_smoke_replaced_by_nonidentity_projective_candidate",
        "smooth_27_mode_BN_imported",
        "model_active_DE_Riesz_Green_values_imported",
        "sector_projectors_and_dotD_imported",
        "canonical_C1_zero_response_no_go_imported",
        "first_tracefree_HYM_correction_imported",
        "honest_replay_cutset_identified",
        "selected_trace_or_full_hym_contract_created",
        "all_finite_value_shapes_present",
    ):
        require(cert["what_closes_now"][key] is True, f"close flag false: {key}", failures)
    for key in (
        "selected_finite_connection_solve_closed",
        "selected_trace_equality",
        "canonical_metric_connection_source",
        "H_sector_shift_source",
        "theorem_derived_selected_source_flags",
        "full_selected_iwasawa_strominger_operator_formula",
        "selected_gap_error_certificate",
        "honest_replay_without_lifted_flags",
        "selected_noninvariant_C1_primitive_or_basis_transport",
        "primitive_C1_nonzero_values",
        "A_selected_b_selected_full_SM_closure",
    ):
        require(cert["what_remains_open"][key] is True, f"remaining flag false: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail violated: {key}", failures)

    for phrase in (
        "identity-rho smoke is no longer the strongest finite object",
        "nonidentity projective `rho_E`",
        "smooth 27-mode `B_N`",
        "source trace equality",
        "full selected operator provenance",
        "canonical C1 zero response",
        "first tracefree HYM direction",
        "selected source replay has not been theorem-derived",
        "full nonlinear HYM/Strominger Newton replay",
        "Q79SelectedFiniteConnectionSolveExecutionCutsetTheorem",
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 selected finite connection solve execution audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 selected finite connection solve execution audit PASS")
    print(f"status: {cert['status']}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
