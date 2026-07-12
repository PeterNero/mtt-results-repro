"""Audit final gate for oriented Phi_fin branch identity or smooth E_Qa quotient."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_orientedphifin_branchidentity_sourcecertificate_or_smootheqa_finalgate.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_branchidentity_sourcecertificate_or_smootheqa_finalgate.candidate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_orientedphifin_branchidentity_minimal_source_certificate_packet.json"
CERT = ROOT / "certificates" / "selected_heterotic_orientedphifin_branchidentity_sourcecertificate_or_smootheqa_finalgate_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_OrientedPhiFin_BranchIdentity_SourceCertificate_or_SmoothEQa_FinalGate_v1.md"

STATUS = "HETEROTIC_ORIENTEDPHIFIN_BRANCH_IDENTITY_FINAL_GATE_OPEN_MINIMAL_SOURCE_PACKET_BUILT"
NEXT = "Selected_Heterotic_OrientedPhiFin_BranchIdentity_MinimalSourceCertificate_Fill_v1"


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
    direct = data["routes"]["direct_same_source_branch_identity"]
    smooth = data["routes"]["smooth_E_Qa_quotient_theorem"]

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", decision["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, decision)
    check("final gate executed", decision["branch_identity_final_gate_executed"] is True and cert["branch_identity_final_gate_executed"] is True, cert)
    check("direct route strongest but open", decision["strongest_route"] == "direct_same_source_branch_identity" and direct["closed"] is False, direct)
    check("direct support present", all(value is True for value in direct["support"].values()), direct["support"])
    check("direct missing exact", set(direct["missing"]) == {"selected_heterotic_QaSU3_source_certificate_names_both_branches", "source_emits_oriented_BN_carrier_as_threshold_domain", "source_emits_positive_PhiFin_DE_magnitude_with_Ctau_orientation", "source_owns_finitepart_trace_identity_for_oriented_nonzero_sector"}, direct["missing"])
    check("smooth fallback open", smooth["closed"] is False and decision["smooth_EQa_quotient_closed"] is False, smooth)
    check("smooth missing exact", set(smooth["missing"]) == {"selected_A_or_F_A", "representation_action_and_trace", "Weitzenbock_or_endomorphism_EQa_identity", "quotient_projection_to_oriented_BN_packet", "finite_spectral_functor_to_log92160000"}, smooth["missing"])
    check("minimal packet built", decision["minimal_source_certificate_packet_built"] is True and cert["minimal_source_certificate_packet_built"] is True, cert)
    check("packet acceptance rule", packet["acceptance_rule"]["observed_data_allowed"] is False and packet["acceptance_rule"]["promote_log92160000_only_if_packet_filled"] is True, packet["acceptance_rule"])
    check("packet must emit seven fields", set(packet["must_emit"]) == {"source_certificate", "branch_identity", "carrier_domain", "operator_identity", "commutation_in_source_algebra", "finitepart_trace_identity", "audit_replay"}, packet["must_emit"])
    check("coemission still open", decision["orientation_magnitude_coemission_closed"] is False and cert["orientation_magnitude_coemission_closed"] is False, cert)
    check("no logdet promotion", decision["oriented_logdet_promoted"] is False and cert["oriented_logdet_promoted"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records packet", str(PACKET.relative_to(ROOT)) in note and NEXT in note and "minimal_source_certificate_packet_built = true" in note, NOTE)

    print("\nSelected heterotic oriented Phi_fin branch-identity final gate audit passed")


if __name__ == "__main__":
    main()
