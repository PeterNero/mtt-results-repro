"""Audit oriented Phi_fin threshold-identity source fill / smooth E_Qa construction attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_thresholdidentity_sourcefill_or_smootheqa_construction.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_thresholdidentity_sourcefill_or_smootheqa_construction.candidate.json"
FILL = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_thresholdidentity_sourcefill_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_thresholdidentity_sourcefill_or_smootheqa_construction_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_ThresholdIdentity_SourceFill_or_SmoothEQa_Construction_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_THRESHOLDIDENTITY_SOURCEFILL_PARTIAL_FINITE_SELECTED_SMOOTH_EQA_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_MinimalSmoothEQa_LeafFill_or_FiniteQuotientIdentity_v1"


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
    fill = load(FILL)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    leaves = data["required_leaves"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("attempt executed", decision["fill_attempt_executed"] is True and decision["selected_finite_internal_packet_reused"] is True and decision["oriented_table_reused"] is True, decision)
    check("required leaves all open", decision["closed_required_leaf_count"] == 0 and all(value is False for value in leaves.values()), leaves)
    check("source certificate partial only", fill["source_certificate"]["finite_internal_projective_packet_selected"] is True and fill["source_certificate"]["closes_threshold_source_certificate"] is False, fill["source_certificate"])
    check("operator identity open", fill["operator_identity"]["oriented_table_available"] is True and fill["operator_identity"]["closes_operator_identity"] is False, fill["operator_identity"])
    check("smooth E_Qa open", fill["smooth_payload_if_used"]["E_Qa_matrix_filled"] is False and decision["smooth_EQa_constructed"] is False, fill["smooth_payload_if_used"])
    check("finitepart leaf open", fill["finitepart_payload"]["finitepart_trace_identity_for_oriented_table"] is False and decision["heterotic_threshold_magnitude_promoted"] is False, fill["finitepart_payload"])
    check("current source nogo", decision["current_source_nogo"] is True and decision["mathematical_impossibility_claimed"] is False, decision)
    check("guardrails", all(value is True for key, value in data["guardrails"].items() if key != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("no overclaim", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["target_fitting_used"] is False, cert)
    check("note records fill packet", str(FILL.relative_to(ROOT)) in note and NEXT in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin threshold-identity source-fill / smooth E_Qa construction audit")


if __name__ == "__main__":
    main()
