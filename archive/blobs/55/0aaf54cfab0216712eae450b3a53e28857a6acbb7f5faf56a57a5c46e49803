"""Audit the physical gauge-anchor and electroweak threshold-vector gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_physical_gauge_anchor_and_electroweak_threshold_vector.py"
DATA = REPO / "candidate_data" / "selected_physical_gauge_anchor_and_electroweak_threshold_vector.candidate.json"
CERT = REPO / "certificates" / "selected_physical_gauge_anchor_and_electroweak_threshold_vector_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_Physical_Gauge_Anchor_and_Electroweak_Threshold_Vector_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(name: str, condition: bool, detail: object) -> None:
    if condition:
        print(f"PASS: {name} -- {detail}")
        return
    print(f"FAIL: {name} -- {detail}")
    raise SystemExit(1)


def main() -> int:
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(proc.stdout)
    check("builder exits cleanly", proc.returncode == 0, proc.returncode)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    theorem = data["theorem"]
    decision = data["decision"]
    checks = data["source_checks"]

    check("status reduced open", data["status"] == "PHYSICAL_EW_MATCHING_REDUCED_TO_OMEGA0_AND_LOCAL_DETERMINANT_OPEN", data["status"])
    check("physical closure refused", decision["physical_electroweak_matching_closed"] is False and decision["target_fitting_used"] is False, decision)
    check("internal inputs carried", theorem["selected_internal_inputs"] == {"I_U1": "2/3", "I_SU2": "1", "I_Qa_or_SU3": "log(2008)", "K_gauge_int": "1"}, theorem["selected_internal_inputs"])
    check("tree diagnostic is 9/19 only", theorem["zero_threshold_diagnostic"]["gut_normalized_sin2_tree"] == "9/19" and theorem["zero_threshold_diagnostic"]["status"] == "DIAGNOSTIC_ONLY_NOT_PHYSICAL_PREDICTION", theorem["zero_threshold_diagnostic"])
    check("threshold gate open with lambda12", theorem["threshold_vector_gate"]["status"] == "OPEN" and "lambda_12" in theorem["threshold_vector_gate"]["weak_split_minimal_scalar"], theorem["threshold_vector_gate"])
    check("target witness forbidden", theorem["threshold_vector_gate"]["target_witness_status"] == "FORBIDDEN_AS_PROOF_INPUT", theorem["threshold_vector_gate"])
    check("physical anchor open", theorem["physical_anchor_gate"]["status"] == "OPEN" and "Omega_0" in theorem["physical_anchor_gate"]["required_source"], theorem["physical_anchor_gate"])
    check("convention gate open", theorem["convention_reconciliation_gate"]["status"] == "OPEN" and "hypercharge" in theorem["convention_reconciliation_gate"]["issue"], theorem["convention_reconciliation_gate"])
    check("all source checks pass", all(checks.values()), checks)
    check("certificate agrees", cert["open"]["physical_anchor_K_phys_or_Omega0"] is True and cert["closed"]["zero_threshold_tree_diagnostic"] == "9/19", cert)
    check("note has guardrail", "not a physical weak-angle prediction" in note and "target_fitting_used = false" in note, NOTE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
