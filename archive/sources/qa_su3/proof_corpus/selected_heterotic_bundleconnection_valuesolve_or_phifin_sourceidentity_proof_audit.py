"""Audit bundle-connection value-solve or Phi_fin source-identity proof gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_bundleconnection_valuesolve_or_phifin_sourceidentity_proof.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_bundleconnection_valuesolve_or_phifin_sourceidentity_proof.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_bundleconnection_valuesolve_or_phifin_sourceidentity_proof_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_BundleConnection_ValueSolve_or_PhiFin_SourceIdentity_Proof_v1.md"

STATUS = "HETEROTIC_BUNDLECONNECTION_VALUESOLVE_OR_PHIFIN_SOURCEIDENTITY_PROOF_FINITE_INTERNAL_CLOSED_SMOOTH_SOURCE_OPEN"
NEXT = "Selected_Heterotic_FiniteInternalRhoE_to_PhiFin_or_SmoothBundleConnection_SourceLift_v1"


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
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("finite internal promoted", decision["finite_internal_projective_packet_promoted_for_internal_scope"] is True and data["value_packet_status"]["finite_internal_logdet_value"] == "log(2008)", data["value_packet_status"])
    check("PhiFin identity remains open", decision["same_source_PhiFin_identity_proved"] is False and data["lane_A_PhiFin_identity"]["closes_as_heterotic_PhiFin_identity"] is False, data["lane_A_PhiFin_identity"])
    check("EndE blockers retained", all(value is False for value in data["lane_A_PhiFin_identity"]["blocking_subclaims"].values()), data["lane_A_PhiFin_identity"]["blocking_subclaims"])
    check("bundle connection remains open", decision["explicit_bundle_connection_solved"] is False and data["lane_B_bundle_connection_value_solve"]["closes_now"] is False, data["lane_B_bundle_connection_value_solve"])
    check("smooth values absent", all(value is False for value in data["lane_B_bundle_connection_value_solve"]["smooth_bundle_connection_values"].values()), data["lane_B_bundle_connection_value_solve"]["smooth_bundle_connection_values"])
    check("no physical closure", decision["computed_physical_threshold_value"] is False and decision["E_Qa_computed"] is False and data["value_packet_status"]["physical_threshold_value_claimed"] is False, decision)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no closure overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False, cert)
    check("note records result", NEXT in note and "log(2008)" in note and "Theorem" in note, NOTE)

    print("\nSelected heterotic bundle-connection / PhiFin source-identity proof audit")


if __name__ == "__main__":
    main()
