"""Audit physical normalization or smooth-operator identity gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_physicalthresholdnormalization_or_smoothoperatoridentity.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_physicalthresholdnormalization_or_smoothoperatoridentity.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_physicalthresholdnormalization_or_smoothoperatoridentity_certificate.json"
CONTRACT = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_physicalnormalization_or_smoothidentity_contract.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_PhysicalThresholdNormalization_or_SmoothOperatorIdentity_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_PHYSICAL_NORMALIZATION_REDUCED_KPHYS_OR_SMOOTH_IDENTITY_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_KPhysAnchor_or_SmoothOperatorIdentity_Fill_v1"


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
    contract = load(CONTRACT)
    note = NOTE.read_text(encoding="utf-8")

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("internal checks closed", all(data["internal_checks"].values()) and data["decision"]["internal_interface_closed"] is True, data["internal_checks"])
    check("physical checks remain open", not any(data["physical_checks"].values()), data["physical_checks"])
    check("contract has two bridges", set(contract["must_prove_one_of"]) == {"physical_normalization_bridge", "smooth_operator_identity_bridge"}, contract)
    check("forbidden shortcuts exact", "set K_phys=1 from internal action units" in contract["forbidden_shortcuts"] and "compare log(2008) directly to observed inverse couplings" in contract["forbidden_shortcuts"], contract["forbidden_shortcuts"])
    check("no physical closure", data["decision"]["physical_threshold_normalization_closed"] is False and cert["physical_threshold_normalization_closed"] is False, cert)
    check("no smooth closure", data["decision"]["smooth_operator_identity_proved"] is False and cert["smooth_operator_identity_proved"] is False and cert["E_Qa_computed"] is False, cert)
    check("no measured match", data["decision"]["measured_coupling_match_claimed"] is False and cert["measured_coupling_match_claimed"] is False, cert)
    check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False, cert)
    check("guardrails true", all(data["guardrails"].values()), data["guardrails"])
    check("note records contract", "K_gauge,int = 1" in note and NEXT in note, NOTE)

    print("\nSelected heterotic projective rho_E physical-normalization/smooth-identity audit")


if __name__ == "__main__":
    main()
