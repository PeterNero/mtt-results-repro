"""Audit q79 selected dotD/alpha1/C1 response emission reduction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP = (
    ROOT
    / "scripts"
    / "prove_q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay.py"
)
SCRIPT = ROOT / "scripts" / "prove_q79_selected_dotd_alpha1_c1_response_emission.py"
CERT = ROOT / "certificates" / "q79_selected_dotd_alpha1_c1_response_emission_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_selected_dotd_alpha1_c1_response_emission.candidate.json"
OUT_DIR = ROOT / "candidate_data" / "q79_selected_dotd_alpha1_c1_response_emission"
FRONTIER = OUT_DIR / "dotd_alpha1_frontier.json"
OBSTRUCTION = OUT_DIR / "selected_tangent_or_retarded_kernel_obstruction.json"
C1_CONTRACT = OUT_DIR / "c1_response_emission_contract.open.json"
PAPER = ROOT / "proof_corpus" / "Q79_Selected_dotD_Alpha1_C1_Response_Emission_v1.md"

STATUS = "Q79_SELECTED_DOTD_ALPHA1_C1_RESPONSE_REDUCED_TANGENT_OPEN"
NEXT = "Q79_Selected_Alpha1_Tangent_or_Retarded_Overlap_Kernel_v1"


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
    for path in (CERT, CANDIDATE, FRONTIER, OBSTRUCTION, C1_CONTRACT, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    frontier = load(FRONTIER)
    obstruction = load(OBSTRUCTION)
    c1_contract = load(C1_CONTRACT)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate differ", failures)
    require(cert["status"] == STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must remain false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)

    require(
        cert["input_statuses"][
            "q79_selected_trace_equals_emitted_27mode_operator_or_full_hym_newton_replay"
        ]["status"]
        == "Q79_SELECTED_TRACE_EQUALS_EMITTED_27MODE_DE_GAP_LAYER_PROVED_DOTD_C1_OPEN",
        "q79 trace/gap certificate not imported",
        failures,
    )
    require(
        cert["input_statuses"]["selected_phifin_dotd_alpha1_c1_response_emission_attempt"][
            "status"
        ]
        == "SELECTED_PHIFIN_DOTD_ALPHA1_C1_RESPONSE_FRONTIER_SHARPENED",
        "PhiFin dotD/C1 frontier not imported",
        failures,
    )
    require(
        cert["input_statuses"]["selected_dotd_alpha1_source_and_driver_theorem_attempt"][
            "status"
        ]
        == "SELECTED_DOTD_ALPHA1_SOURCE_AND_DRIVER_THEOREM_NOT_PROVED_CRITERION_SHARPENED",
        "source/driver criterion not imported",
        failures,
    )
    require(
        cert["input_statuses"]["selected_dotd_alpha1_source_derivative_payload_attempt"][
            "status"
        ]
        == "SELECTED_DOTD_ALPHA1_SOURCE_DERIVATIVE_PAYLOAD_ATTEMPT_BUILT_SOURCE_TANGENT_OPEN",
        "derivative payload attempt not imported",
        failures,
    )

    require(frontier["schema"] == "Q79SelectedDotDAlpha1Frontier.v1", "frontier schema wrong", failures)
    require(
        frontier["status"] == "DOTD_VALUES_AVAILABLE_SOURCE_DRIVER_OPEN",
        "frontier status wrong",
        failures,
    )
    require(
        frontier["selected_DE_gap_layer"]["D_E_gap_Riesz_Green_layer_locked"] is True,
        "D_E layer not carried",
        failures,
    )
    require(frontier["selected_DE_gap_layer"]["basis_dimension"] == 27, "basis dimension wrong", failures)
    require(
        frontier["closed_finite_prefix"]["dotD_alpha1_value_matrices_emitted"] is True,
        "dotD matrices not emitted",
        failures,
    )
    require(
        frontier["closed_finite_prefix"]["dotD_alpha1_has_nonzero_entries"] is True,
        "dotD nonzero flag missing",
        failures,
    )
    require(
        frontier["c1_response_emission"]["can_emit_c1_response_now"] is False,
        "C1 response overclaimed",
        failures,
    )
    require(
        frontier["c1_response_emission"]["A_selected_emitted"] is False,
        "A_selected overclaimed",
        failures,
    )

    require(
        obstruction["schema"] == "Q79SelectedDotDAlpha1SourceObstruction.v1",
        "obstruction schema wrong",
        failures,
    )
    require(
        obstruction["status"] == "SELECTED_TANGENT_OR_RETARDED_KERNEL_REQUIRED",
        "obstruction status wrong",
        failures,
    )
    require(
        obstruction["source_driver_obstruction"]["not_a_gap_problem"] is True,
        "obstruction should not be a gap issue",
        failures,
    )
    checks = obstruction["derivative_payload_checks"]
    for key in ("D0_locked_basis_and_D_E_gap_available", "D1_same_basis_dotD_values_available"):
        require(checks[key] is True, f"required closed derivative prefix false: {key}", failures)
    for key in (
        "D4_operator_level_selected_projector_retention_for_dotD",
        "D5_selected_alpha1_tangent_parameter",
        "D6_retarded_overlap_derivative_formula",
        "D7_sector_equality_from_selected_derivative_to_dotD_matrices",
        "D8_honest_dotD_replay_without_lifted_flags",
    ):
        require(checks[key] is False, f"open derivative check unexpectedly true: {key}", failures)

    require(
        c1_contract["schema"] == "Q79SelectedC1ResponseEmissionContract.v1",
        "C1 contract schema wrong",
        failures,
    )
    require(
        c1_contract["status"] == "OPEN_C1_RESPONSE_EMISSION_REQUIRES_SELECTED_OPERATOR_BLOCKS",
        "C1 contract status wrong",
        failures,
    )
    for key in (
        "emit_selected_A_selected",
        "emit_selected_b_selected",
        "selected_Hess_Xi_finite_blocks",
        "selected_dotD_Q_u_d_L_e_N_H",
        "selected_primitive_C1_contractions",
        "selected_sector_response_matrices",
        "full_SM_closure",
    ):
        require(c1_contract["not_closed"][key] is True, f"C1 not-closed flag false: {key}", failures)

    for key in (
        "selected_D_E_gap_Riesz_Green_layer_carried",
        "same_basis_dotD_value_matrices_available",
        "dotD_alpha1_has_nonzero_entries",
        "finite_horizontal_response_diagnostic_passes",
        "projectors_clean",
        "dotD_C1_frontier_sharpened",
        "exact_missing_tangent_identified",
        "D_E_lock_not_sufficient_for_dotD",
        "target_fitting_excluded",
    ):
        require(cert["what_closes_now"][key] is True, f"close flag false: {key}", failures)

    for key in (
        "operator_level_projector_retention_for_dotD",
        "selected_alpha1_tangent_parameter",
        "retarded_overlap_derivative_formula",
        "sector_equality_from_selected_derivative_to_dotD_matrices",
        "honest_dotD_replay_without_lifted_flags",
        "selected_dotD_source_theorem",
        "same_branch_alpha1_driver_theorem",
        "selected_Hess_Xi_finite_blocks",
        "selected_zero_mode_bases_and_Gram_Schmidt",
        "selected_primitive_C1_contractions",
        "selected_sector_response_matrices",
        "A_selected",
        "b_selected",
        "Yukawa_or_full_SM_closure",
    ):
        require(cert["what_remains_open"][key] is True, f"remaining flag false: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail violated: {key}", failures)

    theorem = cert["theorem"]
    require(theorem["proved"] is True, "reduction theorem not proved", failures)
    require(theorem["closure_claimed"] is False, "theorem overclaims closure", failures)
    for phrase in (
        "not closed, but its obstruction",
        "is now exact",
        "Same-basis nonzero `dotD_alpha1` value matrices",
        "first variation along an `alpha1` deformation",
        "not another `D_E` gap theorem",
        "Selected_alpha1_Tangent_or_Retarded_Overlap_Kernel_v1",
        "honestly without",
        "selected C1 response equation is structurally specified but not computable",
        "Q79SelectedDotDAlpha1C1ResponseReductionTheorem",
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 selected dotD alpha1 C1 response emission audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 selected dotD alpha1 C1 response emission audit PASS")
    print(f"status: {cert['status']}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
