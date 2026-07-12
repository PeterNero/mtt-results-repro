"""Audit refined source-owned BN27 certificate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_sourceowned_bn27_certificate_or_bundleA_selector.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_sourceowned_bn27_certificate_or_bundleA_selector.candidate.json"
REFINED = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_bn27_source_owned_certificate.refined.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_sourceowned_bn27_certificate_or_bundleA_selector_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_SourceOwned_BN27_Certificate_or_BundleA_Selector_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_SOURCEOWNED_BN27_CERTIFICATE_REFINED_BRANCH_CERT_CLOSED_BN27_OWNERSHIP_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BN27_SourceOwnership_Transport_or_ConnectionWitness_Values_v1"


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
    refined = load(REFINED)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    fields = refined["BN27_source_ownership_fields"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("branch certificate closed", decision["heterotic_branch_certificate_closed"] is True and refined["source_certificate"]["heterotic_QaSU3_branch_certificate_closed"] is True, refined["source_certificate"])
    check("BN27 source not declared", decision["S_QaSU3_BN27_declared_as_selected_source"] is False and refined["source_certificate"]["S_QaSU3_BN27_declared_as_selected_source"] is False, refined["source_certificate"])
    check("support retained", refined["support_owned_or_replayed"]["C_tau_orientation_bound_to_same_threshold_complex"] is True and refined["support_owned_or_replayed"]["audit_replay_export_filled"] is True and refined["support_owned_or_replayed"]["exact_finitepart_ready"] is True, refined["support_owned_or_replayed"])
    check("BN27 ownership fields open", all(value is False for value in fields.values()), fields)
    check("support values retained", refined["support_values"]["basis_dimension"] == 27 and refined["support_values"]["oriented_abs_sector_product"] == 92160000, refined["support_values"])
    check("no closure", decision["BN27_source_ownership_closed"] is False and decision["direct_BN27_source_declaration_closed"] is False and data["closure_claimed"] is False, decision)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records refinement", NEXT in note and str(REFINED.relative_to(ROOT)) in note and "heterotic_branch_certificate_closed = true" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin source-owned BN27 certificate audit passed")


if __name__ == "__main__":
    main()
