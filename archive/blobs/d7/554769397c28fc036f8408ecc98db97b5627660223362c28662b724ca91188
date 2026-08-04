"""Audit q79 selected alpha1 tangent / retarded-kernel analytic theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP = ROOT / "scripts" / "prove_q79_selected_dotd_alpha1_c1_response_emission.py"
SCRIPT = ROOT / "scripts" / "prove_q79_selected_alpha1_tangent_or_retarded_overlap_kernel.py"
CERT = ROOT / "certificates" / "q79_selected_alpha1_tangent_or_retarded_overlap_kernel_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_selected_alpha1_tangent_or_retarded_overlap_kernel.candidate.json"
OUT_DIR = ROOT / "candidate_data" / "q79_selected_alpha1_tangent_or_retarded_overlap_kernel"
FORMULA = OUT_DIR / "analytic_variational_kernel_formula.json"
TRIAGE = OUT_DIR / "cross_repo_external_source_triage.json"
CONTRACT = OUT_DIR / "selected_tangent_value_fill_contract.open.json"
PAPER = ROOT / "proof_corpus" / "Q79_Selected_Alpha1_Tangent_or_Retarded_Overlap_Kernel_v1.md"

STATUS = "Q79_SELECTED_ALPHA1_TANGENT_KERNEL_ANALYTIC_FORMULA_PROVED_SOURCE_VALUES_OPEN"
NEXT = "Q79_Selected_Physical_Alpha1_SourceNormalization_or_End0SectorRouting_Value_Fill_v1"


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
    for path in (CERT, CANDIDATE, FORMULA, TRIAGE, CONTRACT, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    formula = load(FORMULA)
    triage = load(TRIAGE)
    contract = load(CONTRACT)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate differ", failures)
    require(cert["status"] == STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must remain false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)

    require(
        cert["input_statuses"]["q79_dotd_alpha1_c1_response_reduction"]["status"]
        == "Q79_SELECTED_DOTD_ALPHA1_C1_RESPONSE_REDUCED_TANGENT_OPEN",
        "previous q79 dotD/C1 reduction not imported",
        failures,
    )
    require(
        cert["input_statuses"]["sm_physical_dotd_or_end0_sector_routing"]["status"]
        == "MTT_SELECTED_EXT_SCALE_DOTD_TANGENT_CLOSED_PHYSICAL_ALPHA1_ROUTING_OPEN",
        "SM physical dotD/End0 routing status not imported",
        failures,
    )

    require(
        formula["schema"] == "Q79AnalyticRetardedRieszKernelFormula.v1",
        "formula schema wrong",
        failures,
    )
    require(
        formula["status"] == "ANALYTIC_FORMULA_PROVED_SELECTED_TANGENT_VALUES_OPEN",
        "formula status wrong",
        failures,
    )
    require(formula["selected_gap_layer"]["basis_dimension"] == 27, "basis dimension wrong", failures)
    require(
        formula["selected_gap_layer"]["D_E_gap_Riesz_Green_layer_locked"] is True,
        "gap layer not locked",
        failures,
    )
    require(
        formula["assumptions"]["isolated_family_cluster"] is True,
        "isolated cluster assumption should be verified by gap",
        failures,
    )
    for key in (
        "riesz_projection",
        "riesz_projection_derivative",
        "duhamel_retarded_semigroup_derivative",
        "reduced_green_limit",
        "horizontal_zero_mode_response",
    ):
        require(key in formula["formulae"], f"missing formula: {key}", failures)

    scalar = formula["exact_scalar_check"]
    require(scalar["all_three_formulas_agree"] is True, "scalar sign check failed", failures)
    require(scalar["expected_exact_fraction"] == "-2/5", "scalar fraction wrong", failures)
    require(abs(scalar["horizontal_response_minus_G_source"] + 0.4) < 1e-12, "response value wrong", failures)

    for key in (
        "analytic_riesz_projection_derivative_formula",
        "duhamel_retarded_kernel_derivative_formula",
        "reduced_green_horizontal_response_identity",
        "conditional_projector_retention_given_selected_tangent",
    ):
        require(
            formula["what_the_formula_closes"][key] is True,
            f"formula close flag false: {key}",
            failures,
        )
    for key in (
        "selected_alpha1_tangent_parameter",
        "selected_retarded_overlap_values",
        "sector_equality_to_existing_dotD_matrices",
        "honest_dotD_replay_without_lifted_flags",
    ):
        require(
            formula["what_the_formula_does_not_close"][key] is True,
            f"formula overclosed: {key}",
            failures,
        )

    require(
        triage["status"] == "FORMULA_SUPPORTED_SOURCE_NORMALIZATION_OPEN",
        "triage status wrong",
        failures,
    )
    require(len(triage["external_references"]) >= 4, "external references missing", failures)
    urls = {ref["url"] for ref in triage["external_references"]}
    for expected in (
        "https://link.springer.com/book/10.1007/978-3-662-12678-3",
        "https://arxiv.org/abs/1402.1532",
        "https://arxiv.org/abs/2409.16524",
    ):
        require(expected in urls, f"missing external URL: {expected}", failures)
    require(
        "no longer the blocker" in triage["triage_conclusion"],
        "triage conclusion should identify new blocker",
        failures,
    )

    require(
        contract["status"] == "OPEN_SOURCE_NORMALIZATION_OR_ROUTING_VALUES_REQUIRED",
        "contract status wrong",
        failures,
    )
    require(len(contract["must_emit_before_selected_dotD_replay"]) == 6, "contract must emit count wrong", failures)
    require(contract["next_required_artifact"] == NEXT, "contract next wrong", failures)

    for key in (
        "analytic_riesz_projection_derivative_formula",
        "duhamel_retarded_kernel_derivative_formula",
        "reduced_green_horizontal_response_identity",
        "conditional_projector_retention_given_selected_tangent",
        "external_research_and_cross_repo_triage_completed",
        "selected_tangent_acceptance_contract_written",
        "target_fitting_excluded",
    ):
        require(cert["what_closes_now"][key] is True, f"close flag false: {key}", failures)

    for key in (
        "selected_alpha1_source_normalization",
        "selected_End0_to_sector_routing_values",
        "selected_alpha1_tangent_parameter_or_kernel_values",
        "sector_equality_from_selected_derivative_to_dotD_matrices",
        "honest_dotD_replay_without_lifted_flags",
        "selected_dotD_source_theorem",
        "same_branch_alpha1_driver_theorem",
        "selected_Hess_Xi_finite_blocks",
        "selected_primitive_C1_contractions",
        "A_selected",
        "b_selected",
        "Yukawa_or_full_SM_closure",
    ):
        require(cert["what_remains_open"][key] is True, f"remaining flag false: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail violated: {key}", failures)

    theorem = cert["theorem"]
    require(theorem["proved"] is True, "analytic theorem not proved", failures)
    require(theorem["closure_claimed"] is False, "theorem overclaims closure", failures)
    for phrase in (
        "analytic retarded/Riesz kernel formula is proved",
        "selected physical source values are still open",
        "dotPsi_i = - G Q dotD_alpha1 Psi_i",
        "Riesz/Duhamel machinery",
        "first-order deformations live in operator/cohomology data",
        "same-branch selected alpha1 source-normalization",
        "End0-to-sector routing",
        "Q79AnalyticRetardedRieszKernelFormulaTheorem",
        "does not emit the selected alpha1 tangent",
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 selected alpha1 tangent / retarded kernel audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 selected alpha1 tangent / retarded kernel audit PASS")
    print(f"status: {cert['status']}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
