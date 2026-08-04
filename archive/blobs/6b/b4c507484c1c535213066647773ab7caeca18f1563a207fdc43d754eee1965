"""Audit selected finite packet emission for heterotic projective rho_E."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_selectedpacketemission_or_operatoridentity.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_selectedpacketemission_or_operatoridentity.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_selectedpacketemission_or_operatoridentity_certificate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_finite_internal_operator_packet.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_SelectedPacketEmission_or_OperatorIdentity_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SELECTED_FINITE_PACKET_EMITTED_SMOOTH_OPERATOR_IDENTITY_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_EQa_or_ThresholdFinitePart_v1"


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
    check("emission checks all true", all(data["emission_checks"].values()), data["emission_checks"])
    check("selected finite emission closed", data["decision"]["selected_finite_internal_packet_emitted"] is True and cert["selected_finite_internal_packet_emitted"] is True, data["decision"])
    check("validator-only blocker closed", data["decision"]["finite_rhoE_packet_selected_not_validator_only"] is True and cert["finite_rhoE_packet_selected_not_validator_only"] is True, data["decision"])
    check("packet selected scope", packet["selected"] is True and packet["scope"] == "selected_finite_internal_Qa_SU3_projective_response_only", packet)
    check("packet labels and tau", packet["labels"][-1] == "P" and packet["tau_values"]["F1"] == 1 and packet["tau_values"]["P"] == 0, packet["tau_values"])
    check("packet matrices", packet["D_E_diagonal_matrix_on_labels"][0][0] == 1 and packet["D_E_diagonal_matrix_on_labels"][1][1] == -1 and packet["Riesz_projector"][2][2] == 1, packet)
    check("green and chi", packet["Green_operator"][2][2] == "1/8" and packet["chi_Qa"] == "1", packet)
    check("smooth still open", data["decision"]["smooth_rhoE_transition_tables_emitted"] is False and data["decision"]["same_source_smooth_operator_identity_proved"] is False, data["decision"])
    check("E and threshold still open", data["decision"]["E_Qa_computed"] is False and data["decision"]["threshold_value_computed"] is False, data["decision"])
    check("no full closure", data["closure_claimed"] is False and cert["closure_claimed"] is False, cert)
    check("no target fitting", data["target_fitting_used"] is False and cert["target_fitting_used"] is False and packet["target_fitting_used"] is False, cert)
    check("guardrails true", all(data["guardrails"].values()), data["guardrails"])
    check("note records packet and frontier", "finite `rho_E/D_E` packet is now selected" in note and NEXT in note, NOTE)

    print("\nSelected heterotic projective rho_E packet-emission audit")


if __name__ == "__main__":
    main()
