"""Audit q79 same-source operator provenance or selected Route-C solve."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEP = ROOT / "scripts" / "analyze_q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual.py"
SCRIPT = ROOT / "scripts" / "analyze_q79_same_source_operator_provenance_or_selected_routec_solve.py"
CERT = ROOT / "certificates" / "q79_same_source_operator_provenance_or_selected_routec_solve_certificate.json"
CANDIDATE = ROOT / "candidate_data" / "q79_same_source_operator_provenance_or_selected_routec_solve.candidate.json"
TABLE = (
    ROOT
    / "candidate_data"
    / "q79_same_source_operator_provenance_or_selected_routec_solve"
    / "same_source_operator_frontier_summary.json"
)
PAPER = ROOT / "proof_corpus" / "Q79_SameSource_Operator_Provenance_or_Selected_RouteC_Solve_v1.md"

STATUS = "Q79_SAME_SOURCE_OPERATOR_PROVENANCE_ATTEMPT_PATCHWORK_NOGO_SELECTED_SOURCE_REQUIRED"
NEXT = "Q79_Selected_Visible_Bundle_Operator_Source_or_Primitive_C1_Contractions_v1"


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

    evidence = cert["source_evidence_status"]
    closes = cert["what_closes_now"]
    remaining = cert["what_remains_open"]
    reduction = cert["same_source_reduction"]
    validators = cert["validator_results"]

    require(evidence["selected_ordered_source_closed"] is True, "selected ordered source not closed", failures)
    require(evidence["selected_h1_ext_input_closed"] is True, "selected h1 Ext input not closed", failures)
    require(
        evidence["s3_freed_witten_and_projectors_closed"] is True,
        "S3 Freed-Witten/projector side condition not closed",
        failures,
    )
    require(
        evidence["same_source_visible_gs_row_from_valpha_to_DE_closed"] is False,
        "same-source GS row overclaimed",
        failures,
    )
    require(
        evidence["selected_operator_DE_Riesz_Green_dotD_closed"] is False,
        "selected operator response overclaimed",
        failures,
    )
    require(evidence["primitive_c1_contractions_closed"] is False, "primitive C1 overclaimed", failures)

    require(validators["honest_current_patchwork"]["exit_code"] == 2, "honest packet should be open", failures)
    require(
        validators["honest_current_patchwork"]["parsed_report"]["status"] == "OPEN",
        "honest packet parsed status should be OPEN",
        failures,
    )
    require(
        validators["honest_current_patchwork"]["parsed_report"]["subvalidators"]["ordered_source"]["exit_code"] == 0,
        "ordered subvalidator should pass inside honest packet",
        failures,
    )
    require(
        validators["honest_current_patchwork"]["parsed_report"]["subvalidators"]["selected_source_promotion"]["exit_code"] == 1,
        "original selected-source promotion should still fail",
        failures,
    )
    require(
        validators["hypothetical_same_source_operator_no_primitive_c1"]["exit_code"] == 2,
        "no-primitive diagnostic should stay open",
        failures,
    )
    require(
        reduction["no_primitive_open_items"] == ["primitive_C1_contractions must be true"],
        "no-primitive diagnostic should reduce to primitive C1 only",
        failures,
    )
    require(validators["hypothetical_full_plumbing"]["exit_code"] == 0, "full plumbing diagnostic should pass", failures)
    require(
        validators["hypothetical_full_plumbing"]["parsed_report"]["would_close_selected_monad_difference_source"] is True,
        "full plumbing diagnostic should close validator if supplied",
        failures,
    )

    for key in (
        "same_source_patchwork_nogo_for_current_artifacts",
        "selected_ordered_source_subvalidator_passes_in_honest_packet",
        "original_operator_promotion_still_rejected",
        "operator_provenance_plus_no_primitive_reduces_to_primitive_c1_only",
        "full_plumbing_validator_has_no_hidden_obstruction",
    ):
        require(closes[key] is True, f"close flag false: {key}", failures)

    for key in (
        "genuine_selected_visible_bundle_operator_source_certificate",
        "same_source_ChernWeil_GS_row_from_that_source",
        "operator_layer_Pic0_for_holonomy_sensitive_data",
        "selected_DE_rhoE_Riesz_Green_dotD_from_that_source",
        "primitive_C1_contractions",
        "honest_selected_RouteC_or_HYM_solve",
        "full_SM_or_no_knob_closure",
    ):
        require(remaining[key] is True, f"open flag false: {key}", failures)

    for key, value in cert["guardrails"].items():
        require(value is False, f"guardrail violated: {key}", failures)

    for name, path in cert["packet_paths"].items():
        packet = load(ROOT / path)
        shortcuts = packet["forbidden_shortcuts"]
        require(isinstance(shortcuts, dict), f"forbidden_shortcuts not object: {name}", failures)
        require(all(value is False for value in shortcuts.values()), f"shortcut flag true: {name}", failures)
        if name.startswith("hypothetical"):
            require(packet["diagnostic_not_proof"] is True, f"hypothetical not marked diagnostic: {name}", failures)
        else:
            require(packet["diagnostic_not_proof"] is False, "honest packet marked diagnostic", failures)

    for phrase in (
        "same-source operator theorem is **not** proved",
        "patchwork no-go theorem",
        "selected ordered monad source subvalidator now passes",
        "primitive_C1_contractions must be true",
        "not selected-source proofs",
        "Q79SameSourceOperatorProvenancePatchworkNoGoTheorem",
        "D_E/Riesz/Green/dotD",
        NEXT,
    ):
        require(phrase in paper, f"paper missing phrase: {phrase}", failures)

    if failures:
        print("Q79 same-source operator provenance audit FAILED")
        print("\n".join(f"- {failure}" for failure in failures))
        return 1

    print("Q79 same-source operator provenance audit PASS")
    print(f"status: {cert['status']}")
    print(f"next: {cert['next_required_artifact']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
