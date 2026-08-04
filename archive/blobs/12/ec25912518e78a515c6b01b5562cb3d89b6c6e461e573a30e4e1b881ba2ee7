"""Audit the first-leaf smooth domain/cover or direct complement-domain attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_smoothdomaincover_sourceleaf_or_directcomplementdomain.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothdomaincover_sourceleaf_or_directcomplementdomain.candidate.json"
REQUEST = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothdomaincover_minimal_source_request.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_smoothdomaincover_sourceleaf_or_directcomplementdomain_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_SmoothDomainCover_SourceLeaf_or_DirectComplementDomain_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SMOOTHDOMAINCOVER_FIRSTLEAF_CURRENT_SOURCE_NOGO_REQUEST_BUILT"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothDomainCover_SourceAmendment_or_ExternalConstruction_v1"


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
    request = load(REQUEST)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    decision = data["decision"]
    domain = data["domain_cover_attempt"]
    complement = data["direct_complement_attempt"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("first leaf exact", data["first_leaf"]["id"] == "S1_smooth_domain_cover_or_complement_domain", data["first_leaf"])
    check("domain support not emitted", all(item["selected_emitted"] is False for item in domain.values()) and domain["same_branch_smooth_heterotic_QaSU3_source_certificate"]["support_present"] is True, domain)
    check("complement support not emitted", all(item["selected_emitted"] is False for item in complement.values()) and complement["projection_P11"]["support_present"] is True, complement)
    check("current source nogo", decision["current_source_nogo_for_S1"] is True and cert["current_source_nogo_for_S1"] is True, decision)
    check("minimal request built", decision["minimal_source_request_built"] is True and request["status"] == "SOURCE_VALUES_REQUIRED", request["status"])
    check("request has both lanes", set(request) >= {"lane_A_required_first_leaf", "lane_B_required_first_leaf", "acceptable_external_construction_templates"}, request.keys())
    check("request forbids shortcuts", "finite eleven-label quotient alone" in request["must_not_use"] and "abstract Z3 shadow alone" in request["must_not_use"], request["must_not_use"])
    check("external templates useful", len(request["acceptable_external_construction_templates"]) == 4, request["acceptable_external_construction_templates"])
    check("no closure", decision["domain_cover_leaf_closed"] is False and decision["direct_complement_domain_closed"] is False and data["closure_claimed"] is False, decision)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records request", NEXT in note and str(REQUEST.relative_to(ROOT)) in note and "first smooth payload leaf is not present" in note, NOTE)

    print("\nSelected heterotic projective rho_E smooth domain/cover source leaf audit")


if __name__ == "__main__":
    main()
