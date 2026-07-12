"""Audit physical-boundary or smooth-identity gate after direct payload closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_directoperatorpayload_physicalboundary_or_smoothidentity.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_directoperatorpayload_physicalboundary_or_smoothidentity.candidate.json"
CONTRACT = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_physicalboundary_or_smoothidentity_contract.json"
DECISION = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_next_bridge_decision_after_direct_payload.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_directoperatorpayload_physicalboundary_or_smoothidentity_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_DirectOperatorPayload_PhysicalBoundary_or_SmoothIdentity_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_DIRECT_PAYLOAD_BOUNDARY_LOCKED_NEXT_SMOOTH_IDENTITY_CONTRACT_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothIdentity_TraceLift_or_ComplementQuotient_FillAttempt_v1"


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
    decision_packet = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS and contract["status"] == "TWO_EXTENSION_CONTRACT_OPEN", (data["status"], cert["status"], contract["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and decision_packet["next_required_artifact"] == NEXT, decision)
    check("boundary locked", decision["direct_payload_boundary_locked"] is True and cert["direct_payload_boundary_locked"] is True, decision)
    check("finite complete", decision["finite_internal_payload_complete"] is True and contract["finite_internal_payload_locked"]["selected_internal_logdet"] == "log(2008)", contract["finite_internal_payload_locked"])
    check("physical lane open", decision["physical_lane_closed"] is False and decision["physical_lane_blocked_by_anchor_and_rg"] is True and decision_packet["physical_lane"]["can_close_now"] is False, decision_packet["physical_lane"])
    check("smooth lane selected", decision["smooth_identity_lane_closed"] is False and decision["smooth_identity_lane_selected_next"] is True and decision_packet["selected_next_lane"] == "S_smooth_identity_or_complement_quotient", decision_packet)
    check("contract has both lanes", len(contract["physical_lane_required"]) == 5 and len(contract["smooth_identity_lane_required"]) >= 7, contract)
    check("forbidden promotions", "set K_phys=1 from internal action units" in contract["forbidden_shortcuts"] and "compare log(2008) directly to observed inverse couplings" in contract["forbidden_shortcuts"], contract["forbidden_shortcuts"])
    check("open fields retained", all(data["still_open"].values()), data["still_open"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and contract["closure_claimed"] is False, cert)
    check("note records outputs", str(CONTRACT.relative_to(ROOT)) in note and str(DECISION.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic projective rho_E direct payload boundary / smooth identity audit")


if __name__ == "__main__":
    main()
