"""Audit the smooth source-certificate or complement-operator payload gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_smoothsourcecertificate_or_complementoperatorpayload.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothsourcecertificate_or_complementoperatorpayload.candidate.json"
PAYLOAD = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smooth_operator_payload_minimal_contract.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_smoothsourcecertificate_or_complementoperatorpayload_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_SmoothSourceCertificate_or_ComplementOperatorPayload_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SMOOTHSOURCECERTIFICATE_SUPPORT_PREFILTER_CLOSED_OPERATOR_PAYLOAD_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothOperatorPayload_MinimalEmissionSubpacket_v1"


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
    payload = load(PAYLOAD)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    decision = data["decision"]
    support = data["support_prefilter"]
    retired = data["retired_blockers"]
    cutset = data["remaining_operator_cutset"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("support prefilter closed", decision["support_prefilter_closed"] is True and cert["support_prefilter_closed"] is True and all(support.values()), support)
    check("retired blockers", decision["retired_blockers_count"] == 8 and all(retired.values()), retired)
    check("payload contract built", decision["operator_payload_contract_built"] is True and payload["status"] == "VALUES_REQUIRED", payload["status"])
    check("contract has two lanes", set(payload) >= {"lane_A_good_cover_operator_payload", "lane_B_complement_operator_payload", "source_certificate"}, payload.keys())
    check("lane A values open", all(value is None for value in payload["lane_A_good_cover_operator_payload"].values()), payload["lane_A_good_cover_operator_payload"])
    check("lane B values open", all(value is None for value in payload["lane_B_complement_operator_payload"].values()), payload["lane_B_complement_operator_payload"])
    check("remaining cutset strict", len(cutset) == 9 and all(cutset.values()) and "operator_action_D_E_or_E_Qa" in cutset, cutset)
    check("no payload closure", decision["lane_A_operator_payload_closed"] is False and decision["lane_B_complement_payload_closed"] is False and decision["smooth_finitepart_computed"] is False, decision)
    check("forbidden shortcuts", "promote abstract Z3 shadow to smooth transition tables" in payload["forbidden_shortcuts"] and "compute E_Qa or physical thresholds before one payload lane emits values" in payload["forbidden_shortcuts"], payload["forbidden_shortcuts"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records payload", NEXT in note and str(PAYLOAD.relative_to(ROOT)) in note and "support-level blockers are now retired" in note, NOTE)

    print("\nSelected heterotic projective rho_E smooth source certificate / complement operator payload audit")


if __name__ == "__main__":
    main()
