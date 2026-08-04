"""Audit smooth trace-lift or E_Qa finite-part gate for projective rho_E."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_smoothtracelift_or_eqafinitepart.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothtracelift_or_eqafinitepart.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_smoothtracelift_or_eqafinitepart_certificate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smooth_operator_source_packet_required.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_SmoothTraceLift_or_EQaFinitePartOperator_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SMOOTH_TRACE_LIFT_CURRENT_SOURCE_NOGO_EQA_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_SmoothOperator_SourcePacket_or_ComplementQuotientTheorem_v1"


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
    packet = load(PACKET)
    note = NOTE.read_text(encoding="utf-8")

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("finite result preserved", data["decision"]["finite_internal_result_preserved"] is True and data["finite_internal_result"]["value"] == "log(2008)", data["finite_internal_result"])
    check("nonidentifiability examples", len(data["smooth_nonidentifiability_witness"]["examples"]) == 3 and data["smooth_nonidentifiability_witness"]["examples"][0]["smooth_logdet"] == "log(2008) + log(2)", data["smooth_nonidentifiability_witness"])
    check("trace lift no-go", data["decision"]["current_source_no_go_for_trace_lift"] is True and data["lanes"]["trace_lift"]["status"] == "CURRENT_SOURCE_NO_GO", data["lanes"]["trace_lift"])
    check("E_Qa open", data["decision"]["E_Qa_computed"] is False and cert["E_Qa_computed"] is False and data["lanes"]["smooth_EQa_or_finitepart_operator"]["status"] == "OPEN_SOURCE_PACKET_REQUIRED", data["lanes"]["smooth_EQa_or_finitepart_operator"])
    check("complement quotient partial", data["lanes"]["complement_quotient"]["status"] == "PARTIAL_NOT_PROMOTED", data["lanes"]["complement_quotient"])
    check("required packet schema", packet["schema"] == "SelectedHeteroticProjectiveRhoESmoothOperatorSourcePacketRequired.v1" and packet["next_required_artifact"] == NEXT, packet)
    check("minimum payload explicit", set(packet["minimum_smooth_operator_payload"]) == {"smooth_projective_rhoE_transition_or_Deligne_Cech_representative", "selected_bundle_connection_A_or_equivalent_operator_source", "bundle_curvature_F_A", "representation_action_on_uE_one_forms", "kernel_and_quotient_policy", "E_Qa_matrix_or_equivalent_zero_order_block", "positive_spectrum_heat_zeta_or_torsion_finite_part", "trace_lift_or_complement_quotient_proof"}, packet["minimum_smooth_operator_payload"])
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and data["decision"]["smooth_finitepart_computed"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records Lambda obstruction", "logdet_smooth = log(2008) + log(Lambda)" in note and NEXT in note, NOTE)

    print("\nSelected heterotic projective rho_E smooth trace-lift/E_Qa finite-part audit")


if __name__ == "__main__":
    main()
