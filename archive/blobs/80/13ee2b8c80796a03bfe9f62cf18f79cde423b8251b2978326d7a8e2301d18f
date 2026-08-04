"""Audit selected projective rho_E E_Qa/threshold finite-part theorem."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_eqa_or_thresholdfinitepart.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_eqa_or_thresholdfinitepart.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_eqa_or_thresholdfinitepart_certificate.json"
VALUE = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_internal_threshold_finitepart.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_EQa_or_ThresholdFinitePart_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_INTERNAL_THRESHOLD_FINITEPART_CLOSED_EQA_SMOOTH_PHYSICAL_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_PhysicalThresholdNormalization_or_SmoothOperatorIdentity_v1"


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
    cert = load(CERT)
    value = load(VALUE)
    note = NOTE.read_text(encoding="utf-8")

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("finitepart checks true", all(data["finitepart_checks"].values()), data["finitepart_checks"])
    check("internal finitepart closed", data["decision"]["selected_internal_threshold_finitepart_closed"] is True and cert["selected_internal_threshold_finitepart_closed"] is True, data["decision"])
    check("value selected", value["selected"] is True and value["scope"] == "selected_internal_finite_Qa_SU3_projective_threshold_units", value)
    check("determinant exact", value["determinant"] == 2008 and value["logdet_exact"] == "log(2008)", value)
    check("numeric logdet", abs(value["logdet_numeric"] - math.log(2008)) < 1e-12 and abs(value["Delta_selected_internal_numeric"] - math.log(2008)) < 1e-12, value)
    check("chi and zero policy", value["chi_Qa"] == "1" and "smooth/GR complement" in value["zero_mode_policy"], value)
    check("E_Qa still open", data["decision"]["E_Qa_computed"] is False and cert["E_Qa_computed"] is False, cert)
    check("physical normalization still open", data["decision"]["physical_threshold_normalization_closed"] is False and cert["physical_threshold_normalization_closed"] is False, cert)
    check("no measured match", data["decision"]["measured_coupling_match_claimed"] is False and cert["measured_coupling_match_claimed"] is False, cert)
    check("no closure overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False, cert)
    check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False and value["target_fitting_used"] is False, cert)
    check("guardrails true", all(data["guardrails"].values()), data["guardrails"])
    check("note records finite part", "Delta_selected_internal = chi_Qa * logdet(H_sel)" in note and NEXT in note, NOTE)

    print("\nSelected heterotic projective rho_E E_Qa/threshold finite-part audit")


if __name__ == "__main__":
    main()
