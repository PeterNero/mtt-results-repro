"""Audit the U1/SU2 normalization-index run."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
CERT = REPO / "certificates" / "u1_su2_source_response_or_normalization_index_run_certificate.json"
DATA = REPO / "candidate_data" / "u1_su2_source_response_or_normalization_index_run.candidate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1_SU2_Source_Response_or_Normalization_Index_Run_v1.md"
SCRIPT = REPO / "scripts" / "build_u1_su2_source_response_or_normalization_index_run.py"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def source_row(data: dict[str, object], name: str) -> dict[str, object]:
    return next(row for row in data["closure_attempt"]["source_prior_candidates"] if row["name"] == name)


def imported_row(data: dict[str, object], name: str) -> dict[str, object]:
    return next(row for row in data["closure_attempt"]["diagnostic_imported_hits"] if row["name"] == name)


def main() -> int:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    data = json.loads(DATA.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    computed = json.loads(proc.stdout)
    attempt = data["closure_attempt"]
    decision = data["decision"]
    best_scan = attempt["bounded_rational_scan_top_hits"][0]
    checks = [
        check("status", cert["status"] == "U1_SU2_NORMALIZATION_INDEX_ITERATED_NO_PROMOTABLE_SOURCE_INDEX", cert["status"]),
        check("script agreement", computed["what_closes"] == cert["what_closes"], computed["what_closes"]),
        check("old pieces imported", abs(attempt["input_scalar_proxy_pieces"]["scalar_unit_lambda_12"] - 3.040437642207233) < 1e-12, attempt["input_scalar_proxy_pieces"]),
        check("GUT 3/5 tested", source_row(data, "GUT_hypercharge_3_5")["weights"]["U1"] == "3/5", source_row(data, "GUT_hypercharge_3_5")),
        check("2/3 tested and near", source_row(data, "complex_nesting_or_shared_circle_2_3")["weights"]["U1"] == "2/3" and source_row(data, "complex_nesting_or_shared_circle_2_3")["absolute_residual_lambda_12"] < 0.04, source_row(data, "complex_nesting_or_shared_circle_2_3")),
        check("best source motivated is not target-discovered", decision["best_source_motivated_index"] == "complex_nesting_or_shared_circle_2_3", decision),
        check("old 5/9 7/5 is diagnostic only", imported_row(data, "best_small_rational_old_scan_5_9_7_5")["source_prior"] == "TARGET_DISCOVERED_ONLY", imported_row(data, "best_small_rational_old_scan_5_9_7_5")),
        check("bounded scan found very near hit", best_scan["absolute_residual_lambda_12"] < 1e-4, best_scan),
        check("near hit not promotable", best_scan["promotable"] is False and best_scan["status"] == "TARGET_NEAR_HIT_REJECTED_UNLESS_SOURCE_SELECTED", best_scan),
        check("no promotable rows", attempt["promotable_rows"] == [] and decision["promotable_index_found"] is False, attempt["promotable_rows"]),
        check("source obstructions still open", attempt["source_obstructions"]["selected_operator_values_closed"] is False and attempt["source_obstructions"]["selected_spectra_closed"] is False, attempt["source_obstructions"]),
        check("no payload closure", decision["I_1_filled"] is False and decision["I_2_filled"] is False and decision["K_gauge_filled"] is False, decision),
        check("cannot close now", decision["can_close_now"] is False and decision["measured_electroweak_closure"] is False, decision),
        check("guardrails block 2/3 and 3/5 overpromotion", any("2/3" in item for item in data["guardrails"]) and any("3/5" in item for item in data["guardrails"]), data["guardrails"]),
        check("note records next object", "Selected_U1_SU2_Threshold_Index_Source_Selector_or_Operator_Spectrum_v1" in note, NOTE),
    ]
    print("\nSelected U1/SU2 source response or normalization-index run audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
