"""Audit q79 selected monad L2 source and operator/Route-C frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP = ROOT / "scripts" / "analyze_q79_ah_source_selection_or_routec_residual_reduction.py"
SCRIPT = ROOT / "scripts" / "analyze_q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual.py"
CERT = ROOT / "certificates" / "q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual.candidate.json"
TABLE = (
    ROOT
    / "candidate_data"
    / "q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual"
    / "selected_monad_operator_frontier_summary.json"
)
PAPER = (
    ROOT
    / "proof_corpus"
    / "Q79_Selected_Monad_Difference_L2_Source_and_OperatorPic0_or_RouteC_Residual_v1.md"
)

STATUS = "Q79_SELECTED_MONAD_L2_SOURCE_CLOSED_UNDER_SECTION_PRINCIPLE_OPERATOR_PROVENANCE_OPEN"
NEXT = "Q79_SameSource_Operator_Provenance_or_Selected_RouteC_Solve_v1"


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
    require(table["status"] == cert["status"], "summary table status mismatch", failures)
    require(cert["status"] == STATUS, f"unexpected status: {cert['status']}", failures)
    require(cert["next_required_artifact"] == NEXT, "unexpected next artifact", failures)
    require(cert["closure_claimed"] is False, "closure must stay false", failures)
    require(cert["target_fitting_used"] is False, "target fitting must stay false", failures)

    source = cert["selected_monad_difference_L2_source_theorem"]
    ext = cert["selected_non_split_ext_input_theorem"]
    frontier = cert["operator_pic0_and_routec_residual_frontier"]
    hyp = frontier["hypothetical_flags_only_test"]
    validators = cert["validator_results"]
    closes = cert["what_closes_now"]
    remaining = cert["what_remains_open"]

    require(
        source["proved_under_explicit_terminal_admissible_section_principle"] is True,
        "selected monad source not closed under principle",
        failures,
    )
    require(source["unconditional_in_current_corpus_without_named_principle"] is False, "unconditional overclaimed", failures)
    require(source["selected_source_label"] == "g3 / L3-K2", "wrong selected source label", failures)
    require(source["selected_L"] == [1, -2, 0], "wrong selected L", failures)
    require(source["selected_L2"] == [2, -4, 0], "wrong selected L2", failures)
    require(source["ordered_source_validator_pass"] is True, "ordered-source validator did not pass", failures)

    require(
        ext["proved_under_explicit_terminal_admissible_section_principle"] is True,
        "selected Ext input not closed under principle",
        failures,
    )
    require(ext["h1"] == 8, "h1 changed", failures)
    require(ext["nonzero_extension_class_label"] == "theta_plus_0_tensor_eta_minus_0", "Ext label changed", failures)
    require(ext["cohomology_validator_pass"] is True, "cohomology validator did not pass", failures)

    require(frontier["operator_layer_pic0_recheck_required"] is True, "operator Pic0 recheck missing", failures)
    require(frontier["source_certified_target_wall_present"] is False, "Gauduchon wall overclaimed", failures)
    require(
        frontier["original_routec_and_promotion_fail_because_selected_flags_absent"] is True,
        "original Route-C failure classification wrong",
        failures,
    )
    require(hyp["routec_residual_passes"] is True, "hypothetical Route-C residual should pass", failures)
    require(hyp["selected_source_promotion_passes"] is True, "hypothetical selected-source promotion should pass", failures)
    require(
        all(info.get("all_changes_are_source_or_status_flags", True) for key, info in hyp["diffs"].items() if key != "selected_source_promotion"),
        "operator packet hypothetical changed non-flag fields",
        failures,
    )
    require(
        hyp["diffs"]["selected_source_promotion"]["all_changes_are_source_or_status_flags_or_paths"] is True,
        "promotion hypothetical changed non-flag/non-path fields",
        failures,
    )

    require(validators["selected_ordered_source"]["pass"] is True, "ordered validator result false", failures)
    require(validators["selected_h1_ext_cohomology"]["pass"] is True, "cohomology validator result false", failures)
    require(validators["routec_residual_original"]["pass"] is False, "original routec should fail", failures)
    require(validators["selected_source_promotion_original"]["pass"] is False, "original promotion should fail", failures)
    require(validators["routec_residual_hypothetical_flags_only"]["pass"] is True, "hyp routec should pass", failures)
    require(
        validators["selected_source_promotion_hypothetical_flags_only"]["pass"] is True,
        "hyp promotion should pass",
        failures,
    )

    for key in (
        "selected_monad_difference_L2_source_under_explicit_terminal_section_principle",
        "strict_ordered_source_validator_passes_for_selected_packet",
        "selected_h1_8_nonzero_Ext_input",
        "ordered_Chern_H1_curvature_layer_Pic0_quotient",
        "routec_operator_arithmetic_reduced_to_selected_source_provenance_flags",
    ):
        require(closes[key] is True, f"close flag false: {key}", failures)

    for key in (
        "promote_terminal_admissible_section_principle_to_main_MTT_spine_or_derivation",
        "operator_layer_Pic0_selection_or_quotient_for_holonomy_sensitive_data",
        "same_source_operator_provenance_for_routec_residual_DE_Riesz_Green_dotD",
        "selected_Gauduchon_chamber_or_selected_RouteC_residual_source",
        "full_SM_or_no_knob_closure",
    ):
        require(remaining[key] is True, f"open flag false: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail violated: {key}", failures)

    for phrase in (
        "TerminalAdmissibleSectionSourcePrinciple.v1",
        "not closed",
        "hypothetical selected-flags-only diagnostic",
        "not a selected-source proof",
        "operator provenance",
        "Q79SelectedMonadL2SourceAndOperatorProvenanceFrontierTheorem",
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 selected monad/operator frontier audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 selected monad/operator frontier audit PASS")
    print(f"status: {cert['status']}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
