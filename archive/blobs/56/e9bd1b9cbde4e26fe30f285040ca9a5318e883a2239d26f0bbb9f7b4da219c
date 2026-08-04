"""Audit scoped trace-equality refinement for BN27 source identity."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_bn27_selectedtraceequality_fulloperatorformula_or_sourceflagtheorem.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_selectedtraceequality_fulloperatorformula_or_sourceflagtheorem.candidate.json"
REFINED = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_sourceidentity_refined_root_cutset.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_bn27_selectedtraceequality_fulloperatorformula_or_sourceflagtheorem_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BN27_SelectedTraceEquality_FullOperatorFormula_or_SourceFlagTheorem_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BN27_TRACE_EQUALITY_SCOPED_CLOSED_FULL_SOURCE_FLAGS_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_FullOperatorFormula_SourceFlags_or_QuotientFunctor_ValueConstruction_v1"


def check(label: str, condition: bool, detail: object) -> None:
    if not condition:
        print(f"FAIL: {label} -- {detail}")
        sys.exit(1)
    print(f"PASS: {label} -- {detail}")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True, capture_output=True)
    check("script reruns", proc.returncode == 0, proc.stdout + proc.stderr)

    data = load(DATA)
    refined = load(REFINED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    scoped = refined["scoped_root_refinement"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("gap trace closes", decision["selected_trace_equality_for_27mode_DE_gap_layer_closed"] is True and scoped["selected_trace_equality_for_27mode_DE_gap_layer"]["closed"] is True, scoped["selected_trace_equality_for_27mode_DE_gap_layer"])
    check("scope is narrow", "full selected threshold operator formula" in scoped["selected_trace_equality_for_27mode_DE_gap_layer"]["does_not_close"], scoped["selected_trace_equality_for_27mode_DE_gap_layer"])
    check("full formula open", decision["full_selected_operator_formula_closed"] is False and scoped["full_selected_iwasawa_strominger_operator_formula"]["closed"] is False, scoped["full_selected_iwasawa_strominger_operator_formula"])
    check("quotient/source functor open", decision["quotient_or_source_identity_functor_closed"] is False and scoped["quotient_or_source_identity_functor"]["closed"] is False, scoped["quotient_or_source_identity_functor"])
    check("source flags open", decision["theorem_derived_selected_source_flags_for_full_BN27"] is False and scoped["theorem_derived_selected_source_flags_for_full_BN27"]["closed"] is False, scoped["theorem_derived_selected_source_flags_for_full_BN27"])
    check("S source open", decision["source_object_named_S_QaSU3_BN27"] is False and scoped["source_object_named_S_QaSU3_BN27"]["closed"] is False, scoped["source_object_named_S_QaSU3_BN27"])
    check("no identity closure", decision["BN27_source_identity_closed"] is False and data["closure_claimed"] is False, decision)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records refined cutset", NEXT in note and str(REFINED.relative_to(ROOT)) in note and "selected_trace_equality_for_27mode_DE_gap_layer_closed = true" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin BN27 scoped trace-equality refinement audit passed")


if __name__ == "__main__":
    main()
