"""Audit the q79 Weyl-pair conditional A-assembly certificate."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP_SCRIPT = ROOT / "scripts" / "analyze_q79_routec_basis_transport_primitive_source_theorem.py"
SCRIPT = ROOT / "scripts" / "analyze_q79_routec_weylpair_aselected_assembly_or_source_proof.py"
CERT = ROOT / "certificates" / "q79_routec_weylpair_aselected_assembly_or_source_proof_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_routec_weylpair_aselected_assembly_or_source_proof.candidate.json"
TABLE = (
    ROOT
    / "candidate_data"
    / "q79_routec_weylpair_aselected_assembly_or_source_proof"
    / "conditional_weylpair_solve_table.json"
)
PAPER = ROOT / "proof_corpus" / "Q79_RouteC_WeylPair_Aselected_Assembly_or_Source_Proof_v1.md"

EXPECTED_STATUS = "Q79_ROUTEC_WEYLPAIR_CONDITIONAL_A_SOLVE_BUILT_SOURCE_PROVENANCE_OPEN"
EXPECTED_NEXT = "Q79_Selected_RouteC_WeylPair_Source_Provenance_Lemma_v1"


EXPECTED_STATUSES = {
    "q79:primitive_counterexample_and_weyl_gate": (
        "Q79_ROUTEC_BASISTRANSPORT_PRIMITIVE_COUNTEREXAMPLE_CLOSED_WEYLPAIR_GATE_BUILT_SOURCE_PROOF_OPEN"
    ),
    "adjacent:gr_weylpair_source_gate_import": (
        "ROUTEC_WEYLPAIR_SOURCE_GATE_IMPORTED_ASELECTED_SOURCE_OPEN"
    ),
    "adjacent:gr_weylpair_aselected_assembly_import": (
        "ROUTEC_WEYLPAIR_CONDITIONAL_A_SOLVE_BUILT_SOURCE_PROVENANCE_OPEN"
    ),
    "adjacent:sm_weylpair_source_gate": (
        "MTT_SELECTED_ROUTEC_WEYLPAIR_BASISTRANSPORT_OR_VERTEX_SOURCE_GATE_BUILT_ALGEBRAICALLY_SUFFICIENT_SOURCE_PROOF_OPEN"
    ),
    "adjacent:sm_weylpair_aselected_assembly": (
        "MTT_SELECTED_ROUTEC_WEYLPAIR_ASELECTED_ASSEMBLY_BUILT_CONDITIONAL_SOLVE_EXACT_SOURCE_PROOF_OPEN"
    ),
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def close_to(value: float, expected: float, tol: float = 1.0e-12) -> bool:
    return math.isclose(float(value), expected, rel_tol=tol, abs_tol=tol)


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
    run(DEP_SCRIPT, failures)
    run(SCRIPT, failures)

    for path in (CERT, CANDIDATE, TABLE, PAPER):
        require(path.exists(), f"missing artifact: {path}", failures)
    if failures:
        print("\n".join(failures))
        return 1

    cert = load(CERT)
    candidate = load(CANDIDATE)
    table = load(TABLE)
    paper = PAPER.read_text(encoding="utf-8")

    require(cert == candidate, "certificate and candidate JSON differ", failures)
    require(table == cert["conditional_solve"], "conditional solve table mismatch", failures)
    require(cert["status"] == EXPECTED_STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == EXPECTED_NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must stay false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)

    q79_statuses = cert["q79_input_statuses"]
    adjacent_statuses = cert["adjacent_input_statuses"]
    for key, expected in EXPECTED_STATUSES.items():
        group, name = key.split(":", 1)
        actual = q79_statuses[name]["status"] if group == "q79" else adjacent_statuses[name]["status"]
        require(actual == expected, f"unexpected status for {key}: {actual}", failures)

    require(all(cert["support_reductions"].values()), "support reductions must all pass", failures)

    solve = cert["conditional_solve"]
    operator = solve["conditional_operator"]
    locked = solve["locked_solve"]
    verdict = solve["verdict"]
    require(operator["name"] == "A_weylpair_conditional", "wrong conditional operator name", failures)
    require(operator["columns"] == ["phase_packet", "shift_packet"], "wrong columns", failures)
    require(operator["shape"] == [72, 2], "wrong conditional operator shape", failures)
    require(operator["is_A_selected"] is False, "conditional operator must not be A_selected", failures)
    require(locked["rank"] == 2, "locked solve rank must be 2", failures)
    require(locked["consistent"] is True, "locked solve must be consistent", failures)
    require(close_to(locked["deltaTheta_conditional"][0], 1.0), "first deltaTheta entry wrong", failures)
    require(close_to(locked["deltaTheta_conditional"][1], 1.0), "second deltaTheta entry wrong", failures)
    require(float(locked["residual_norm"]) < 1.0e-12, "residual too large", failures)
    require(float(locked["relative_residual"]) < 1.0e-12, "relative residual too large", failures)
    require(solve["exact_to_tolerance"] is True, "exact-to-tolerance false", failures)

    require(verdict["conditional_A_weylpair_built"] is True, "conditional A not built", failures)
    require(
        verdict["conditional_deltaTheta_solution_found"] is True,
        "conditional DeltaTheta solution not found",
        failures,
    )
    require(verdict["A_selected_emitted"] is False, "A_selected overclaimed", failures)
    require(verdict["b_selected_emitted"] is False, "b_selected overclaimed", failures)
    require(
        verdict["honest_selected_deltaTheta_C1_solve_run"] is False,
        "honest selected solve overclaimed",
        failures,
    )
    require(
        verdict["selected_source_provenance_proved"] is False,
        "source provenance overclaimed",
        failures,
    )

    decision = cert["decision"]
    for key in (
        "conditional_A_weylpair_assembled",
        "conditional_deltaTheta_solve_exact",
        "algebraic_rank_obstruction_absent_for_weylpair_packet",
    ):
        require(decision[key] is True, f"decision flag false: {key}", failures)
    for key in (
        "conditional_A_promoted_to_A_selected",
        "selected_source_provenance_proved",
        "A_selected_emitted",
        "b_selected_emitted",
        "honest_selected_deltaTheta_C1_solve_run",
        "full_SM_or_no_knob_closure",
        "target_fitting_used",
    ):
        require(decision[key] is False, f"decision overclaim: {key}", failures)

    closed = cert["closed_by_this_attempt"]
    for key in (
        "conditional_A_weylpair_assembled",
        "conditional_deltaTheta_solve_exact",
        "algebraic_rank_obstruction_absent_for_weylpair_packet",
        "remaining_gap_reduced_to_source_provenance",
        "next_target_advanced_to_source_provenance_lemma",
        "target_fitting_excluded",
    ):
        require(closed[key] is True, f"closed flag false: {key}", failures)

    still_open = cert["still_open"]
    for key in (
        "prove_selected_weylpair_source_provenance",
        "promote_conditional_A_to_A_selected",
        "emit_theorem_derived_b_selected",
        "run_honest_selected_deltaTheta_C1_solve",
        "selected_PhiFin_alpha1_payload_values",
        "full_SM_or_no_knob_closure",
    ):
        require(still_open[key] is True, f"open flag missing: {key}", failures)

    require(all(value is False for value in cert["guardrails"].values()), "guardrail false-map violated", failures)
    require(cert["theorem"]["proved"] is True, "theorem must be proved", failures)
    require(cert["theorem"]["closure_claimed"] is False, "theorem closure must stay false", failures)

    for phrase in (
        "closed conditionally",
        "This is not yet `A_selected`",
        "same-branch source",
        "Q79ConditionalWeylPairDeltaThetaSolveTheorem",
        EXPECTED_NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 Weyl-pair A assembly audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 Weyl-pair A assembly audit PASS")
    print(f"status: {cert['status']}")
    print(
        "conditional solve: "
        f"shape={operator['shape']}, rank={locked['rank']}, residual={locked['residual_norm']}"
    )
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
