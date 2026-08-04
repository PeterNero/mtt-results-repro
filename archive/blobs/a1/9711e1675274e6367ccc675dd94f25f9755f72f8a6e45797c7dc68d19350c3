"""Audit oriented Phi_fin branch-identity minimal source-certificate fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_branchidentity_minimalsourcecertificate_fill.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_branchidentity_minimalsourcecertificate_fill.candidate.json"
REPORT = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_branchidentity_fill_attempt_report.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_branchidentity_minimalsourcecertificate_fill_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BranchIdentity_MinimalSourceCertificate_Fill_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BRANCH_IDENTITY_FILL_ATTEMPT_DOMAIN_BRIDGE_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceDomainBridge_or_SmoothEQa_Quotient_v1"


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
    report = load(REPORT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    fill = report["fill_status"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("fill attempted", decision["minimal_source_certificate_fill_attempted"] is True and cert["minimal_source_certificate_fill_attempted"] is True, cert)
    check("only audit replay filled", report["filled_count"] == 1 and report["required_count"] == 7 and fill["audit_replay"]["filled"] is True, report)
    check("source certificate open", fill["source_certificate"]["filled"] is False and decision["source_certificate_closed"] is False, fill["source_certificate"])
    check("domain bridge named", decision["minimal_new_leaf"] == "selected_BN27_source_domain_bridge" and report["minimal_new_leaf"]["name"] == decision["minimal_new_leaf"], report["minimal_new_leaf"])
    check("domain mismatch recorded", fill["carrier_domain"]["support"]["finite_11_label_domain_closed"] is True and fill["carrier_domain"]["support"]["routec_BN_domain_dimension"] == 27 and fill["carrier_domain"]["filled"] is False, fill["carrier_domain"])
    check("operator identity open", fill["operator_identity"]["filled"] is False and fill["operator_identity"]["support"]["product_support_ready"] is True, fill["operator_identity"])
    check("source algebra commutation open", fill["commutation_in_source_algebra"]["filled"] is False and fill["commutation_in_source_algebra"]["support"]["support_commutation_closed"] is True, fill["commutation_in_source_algebra"])
    check("finitepart support only", fill["finitepart_trace_identity"]["filled"] is False and fill["finitepart_trace_identity"]["support"]["oriented_abs_sector_product"] == 92160000, fill["finitepart_trace_identity"])
    check("bridge remains open", decision["selected_BN27_source_domain_bridge_closed"] is False and cert["selected_BN27_source_domain_bridge_closed"] is False, cert)
    check("branch remains open", decision["branch_identity_closed"] is False and cert["branch_identity_closed"] is False, cert)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records report", str(REPORT.relative_to(ROOT)) in note and NEXT in note and "selected_BN27_source_domain_bridge_closed = false" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin branch-identity minimal source-certificate fill audit passed")


if __name__ == "__main__":
    main()
