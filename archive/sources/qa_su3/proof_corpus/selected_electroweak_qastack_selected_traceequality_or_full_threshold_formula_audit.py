"""Audit the electroweak Qa-stack selected trace-equality/full-formula gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"
SCRIPT = ROOT / "scripts" / "build_selected_electroweak_qastack_selected_traceequality_or_full_threshold_formula.py"
OUTPUT_DATA = DATA / "selected_electroweak_qastack_selected_traceequality_or_full_threshold_formula.candidate.json"
OUTPUT_CERT = CERTS / "selected_electroweak_qastack_selected_traceequality_or_full_threshold_formula_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_Electroweak_QaStack_SelectedTraceEquality_or_FullThresholdOperatorFormula_v1.md"

EXPECTED_STATUS = "ELECTROWEAK_QASTACK_TRACEEQUALITY_IMPORTED_QUOTIENT_FUNCTOR_AND_ABASE_IDENTITY_OPEN"
EXPECTED_NEXT = "Selected_Electroweak_QaStack_QuotientFunctor_and_AbaseIdentity_Theorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object = "") -> None:
    if not condition:
        print(f"FAIL: {name} -- {detail}")
        raise SystemExit(1)
    print(f"PASS: {name} -- {detail}")


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    check("script reruns", proc.returncode == 0, proc.stdout)

    candidate = load(OUTPUT_DATA)
    cert = load(OUTPUT_CERT)
    note = OUTPUT_NOTE.read_text(encoding="utf-8")

    check("status", candidate["status"] == EXPECTED_STATUS, candidate["status"])
    check("cert status", cert["status"] == EXPECTED_STATUS, cert["status"])
    check("next", candidate["decision"]["next_required_artifact"] == EXPECTED_NEXT, candidate["decision"])

    trace = candidate["imported_trace_layer"]
    tests = candidate["threshold_formula_tests"]
    decision = candidate["decision"]
    guards = candidate["guardrails"]
    frontier = candidate["frontier_reclassification"]

    check("DE trace equality closed", trace["selected_trace_equality_for_27mode_DE"] is True, trace)
    check("DE gap layer closed", trace["DE_gap_Riesz_Green_layer_closed"] is True, trace)
    check("finite HYM gap promoted", trace["finite_HYM_DE_gap_layer_promoted"] is True, trace)
    check("full finite HYM still open", trace["finite_HYM_full_connection_solve_closed"] is False, trace)
    check("dotD source still open", trace["finite_HYM_dotD_alpha1_source_closed"] is False, trace)

    check("DE layer test passes", tests["selected_trace_equality_for_DE_gap_layer"]["passed"] is True, tests)
    check("full formula open", tests["full_selected_threshold_operator_formula"]["passed"] is False, tests)
    check("quotient functor open", tests["quotient_functor_BN_to_Pperp_shared_line"]["passed"] is False, tests)
    check("A_base identity open", tests["exact_A_base_tensor_I3_identity"]["passed"] is False, tests)
    check("weights open", tests["Qa_stack_weights_and_scale_policy"]["passed"] is False, tests)

    check("decision does not overpromote", decision["selected_DE_gap_trace_equality_closed"] is True and decision["full_threshold_operator_formula_closed"] is False, decision)
    check("p_a/lambda remain open", decision["selected_p_a_promoted"] is False and decision["lambda_12_closed"] is False, decision)
    check("frontier sharpened", frontier["resolved_part"].startswith("selected trace equality") and "quotient" in " ".join(frontier["true_frontier"]), frontier)
    check("guardrails false", all(value is False for value in guards.values()), guards)
    check("note scope", "gap/Riesz/Green layer" in note and "does not identify the electroweak Qa-stack" in note, OUTPUT_NOTE)

    print("\nSelected electroweak Qa-stack trace-equality/full-formula audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
