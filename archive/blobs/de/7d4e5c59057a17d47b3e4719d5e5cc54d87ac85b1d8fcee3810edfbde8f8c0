"""Audit the minimal oriented Phi_fin leaf-fill / finite-quotient identity gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_minimal_leaf_fill_or_finitequotientidentity.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_minimal_leaf_fill_or_finitequotientidentity.candidate.json"
CONTRACT = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_minimal_finitequotientidentity_contract.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_minimal_leaf_fill_or_finitequotientidentity_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_MinimalSmoothEQa_LeafFill_or_FiniteQuotientIdentity_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_MINIMAL_LEAFFILL_FINITE_QUOTIENT_PRIMARY_SMOOTH_EQA_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_FiniteQuotientIdentity_SourceTheorem_or_SmoothEQaPayload_v1"


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
    contract = load(CONTRACT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    primary = data["route_ranking"]["primary"]
    secondary = data["route_ranking"]["secondary"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("finite route primary", decision["finite_quotient_identity_route_selected_primary"] is True and primary["rank"] == 1, primary)
    check("smooth route secondary", decision["smooth_EQa_route_retained_secondary"] is True and secondary["rank"] == 2, secondary)
    check("contract built", decision["minimal_contract_built"] is True and contract["schema"].endswith("v1"), contract["schema"])
    check("six finite leaves", decision["required_finite_identity_leaf_count"] == 6 and len(primary["missing_minimal_source_fields"]) == 6, primary)
    check("zero closed leaves", decision["closed_finite_identity_leaf_count"] == 0 and decision["closed_smooth_leaf_count"] == 0, decision)
    check("support imported", primary["available_support"]["oriented_table_dimension"] == 27 and primary["available_support"]["finite_internal_packet_selected"] is True, primary["available_support"])
    check("current source nogo", decision["current_source_nogo"] is True and decision["mathematical_impossibility_claimed"] is False, decision)
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records contract", str(CONTRACT.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin minimal leaf-fill / finite-quotient identity audit")


if __name__ == "__main__":
    main()
