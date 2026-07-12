"""Audit oriented Phi_fin orientation/magnitude co-emission reduction theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_orientation_magnitude_coemission_theorem.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_orientation_magnitude_coemission_theorem.candidate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_orientation_magnitude_coemission_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_orientation_magnitude_coemission_theorem_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_OrientationMagnitude_CoEmission_Theorem_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_ORIENTATION_MAGNITUDE_COEMISSION_REDUCED_TO_BRANCH_IDENTITY_OPEN"
NEXT = "Selected_Heterotic_OrientedPhiFin_BranchIdentity_SourceCertificate_or_SmoothEQa_FinalGate_v1"


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
    packet = load(PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    support = data["support_reduction"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("all support closed", all(value is True for value in support.values()), support)
    check("support count exact", decision["closed_support_count"] == 10 and decision["support_required_count"] == 10, decision)
    check("packet support count exact", packet["closed_support_count"] == 10 and packet["support_required_count"] == 10, packet)
    check("five fields reduced", decision["five_field_coemission_request_reduced_to_single_leaf"] is True and packet["five_field_coemission_request_reduced"] is True, packet)
    check("original five fields retained", set(packet["original_remaining_required_fields"]) == {"same_source_identity_between_routec_gap_layer_and_heterotic_oriented_phifin", "C_tau_orientation_emitted_on_full_27mode_BN_domain", "proof_C_tau_commutes_with_selected_routec_DE_as_source_operator", "oriented_positive_sector_policy_selected_before_finitepart", "finitepart_trace_identity_inherits_source_ownership"}, packet["original_remaining_required_fields"])
    check("single branch leaf open", packet["reduced_single_leaf"]["same_source_orientation_magnitude_branch_identity"]["closed"] is False, packet["reduced_single_leaf"])
    check("coemission remains open", decision["orientation_magnitude_coemission_closed"] is False and cert["orientation_magnitude_coemission_closed"] is False, cert)
    check("full threshold remains open", decision["full_oriented_phi_fin_threshold_closed"] is False, decision)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("trace values support only", data["trace_values_support_only"]["oriented_abs_sector_product"] == 92160000 and data["trace_values_support_only"]["finitepart_expression"] == "log(92160000)", data["trace_values_support_only"])
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records frontier", str(PACKET.relative_to(ROOT)) in note and NEXT in note and "same_source_orientation_magnitude_branch_identity_closed = false" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin orientation/magnitude co-emission audit passed")


if __name__ == "__main__":
    main()
