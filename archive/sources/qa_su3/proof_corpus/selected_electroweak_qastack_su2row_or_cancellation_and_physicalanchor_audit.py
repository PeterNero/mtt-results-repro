"""Audit the Qa-stack SU2 row / cancellation and physical-anchor gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_electroweak_qastack_su2row_or_cancellation_and_physicalanchor.py"
DATA = ROOT / "candidate_data" / "selected_electroweak_qastack_su2row_or_cancellation_and_physicalanchor.candidate.json"
CERT = ROOT / "certificates" / "selected_electroweak_qastack_su2row_or_cancellation_and_physicalanchor_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Electroweak_QaStack_SU2Row_or_Cancellation_and_PhysicalAnchor_v1.md"

STATUS = "ELECTROWEAK_QASTACK_INTERNAL_LAMBDA12_CLOSED_PHYSICAL_ANCHOR_OPEN"
NEXT = "Selected_Electroweak_PhysicalAnchor_RG_and_MatchingScale_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return proc.returncode

    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    vec = data["selected_internal_threshold_vector"]
    same = data["same_scheme_argument"]
    guards = data["guardrails"]

    expected_p_y = 29.201650332199108 / 36.0 + 2.442340583291322 / 4.0
    expected_lambda = expected_p_y - (-1.1961941178318218)
    expected_delta = 0.405623467693425 * expected_lambda / (4.0 * 3.141592653589793)

    checks = [
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"])),
        check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, cert),
        check("same scheme closed", decision["same_scheme_SU2_row_or_cancellation_closed"] is True and same["selected"] is True, same),
        check("Qa p_a source closed", decision["Qa_stack_p_a_source_closed"] is True and abs(vec["p_a_internal"] - 29.201650332199108) < 1e-12, vec),
        check("Qc and SU2 imported", decision["Qc_row_closed_for_weaksplit"] is True and decision["SU2_row_closed_for_weaksplit"] is True, decision),
        check("typed map closed", decision["typed_hypercharge_map_closed"] is True and same["typed_hypercharge_map"]["weights"]["Qa_stack_weight_in_pY"] == "1/36", same["typed_hypercharge_map"]),
        check("p_Y value", abs(vec["p_Y_internal"] - expected_p_y) < 1e-12, vec),
        check("lambda value", decision["lambda_12_internal_closed"] is True and abs(vec["lambda_12_internal"] - expected_lambda) < 1e-12, vec),
        check("Delta value", abs(vec["Delta_G12_internal"] - expected_delta) < 1e-12, vec),
        check("physical still open", decision["physical_K_gauge_anchor_closed"] is False and decision["measured_electroweak_closure"] is False, decision),
        check("guardrails", all(value is False for value in guards.values()), guards),
        check("note boundary", "dimensionless internal weak-split threshold" in note and "not compare to measured electroweak data" in note, NOTE),
    ]
    print("\nSelected electroweak Qa-stack SU2 row / physical-anchor audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
