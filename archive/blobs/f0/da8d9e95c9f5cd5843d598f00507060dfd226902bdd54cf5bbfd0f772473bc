"""Audit the minimal emission subpacket plan for smooth rhoE payload closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_smoothoperatorpayload_minimalemissionsubpacket.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothoperatorpayload_minimalemissionsubpacket.candidate.json"
SUBPACKET = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothoperatorpayload_emission_order.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_smoothoperatorpayload_minimalemissionsubpacket_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_SmoothOperatorPayload_MinimalEmissionSubpacket_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SMOOTHOPERATORPAYLOAD_MINIMAL_EMISSION_SUBPACKET_BUILT_FIRST_LEAF_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothDomainCover_SourceLeaf_or_DirectComplementDomain_v1"


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
    subpacket = load(SUBPACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    decision = data["decision"]
    packets = subpacket["subpackets"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("emission order built", decision["minimal_emission_subpacket_built"] is True and subpacket["status"] == "EMISSION_ORDER_BUILT_VALUES_OPEN", subpacket["status"])
    check("four subpackets", decision["subpacket_count"] == 4 and len(packets) == 4, packets)
    check("first leaf exact", decision["first_leaf_identified"] == "S1_smooth_domain_cover_or_complement_domain" and subpacket["first_open_leaf"] == decision["first_leaf_identified"], decision)
    check("ordered priorities", [item["priority"] for item in packets] == [1, 2, 3, 4], packets)
    check("first leaf has source/domain obligations", "same-branch smooth heterotic Qa/SU3 source certificate" in packets[0]["must_emit"] and "selected good-cover incidence with nonempty overlaps, or selected smooth operator domain" in packets[0]["must_emit"], packets[0])
    check("dependencies enforced", packets[1]["depends_on"] == packets[0]["id"] and packets[2]["depends_on"] == packets[1]["id"] and packets[3]["depends_on"] == packets[2]["id"], packets)
    check("all values open", all(item["closed"] is False for item in packets) and decision["S1_closed"] is False and decision["S4_closed"] is False, decision)
    check("acceptance tests strict", subpacket["acceptance_tests"]["same_source_across_all_emitted_fields"] is True and subpacket["acceptance_tests"]["abstract_Z3_shadow_not_promoted_without_S1"] is True, subpacket["acceptance_tests"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records first leaf", NEXT in note and str(SUBPACKET.relative_to(ROOT)) in note and "first unavoidable leaf" in note, NOTE)

    print("\nSelected heterotic projective rho_E smooth operator payload minimal emission subpacket audit")


if __name__ == "__main__":
    main()
