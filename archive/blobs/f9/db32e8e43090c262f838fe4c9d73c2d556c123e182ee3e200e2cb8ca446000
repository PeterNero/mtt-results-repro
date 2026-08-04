"""Audit the heterotic End(E)->B_N functor / rho_E transition value-packet interface."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_ende_to_bn_functor_or_rhoe_transition_valuepacket.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_ende_to_bn_functor_or_rhoe_transition_valuepacket.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_ende_to_bn_functor_or_rhoe_transition_valuepacket_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_EndE_to_BN_Functor_or_RhoETransitionData_ValuePacket_v1.md"

STATUS = "HETEROTIC_ENDE_TO_BN_FUNCTOR_OR_RHOE_TRANSITION_VALUEPACKET_INTERFACE_BUILT_VALUES_OPEN"


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

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("interface built open", data["decision"]["valuepacket_interface_built"] is True and data["decision"]["values_filled"] is False, data["decision"])
    check("support allowed but not promoted", data["imported_support_allowed"]["u1y_27mode_gap_layer_closed"] is True and data["imported_support_allowed"]["promotion_allowed_without_this_packet"] is False, data["imported_support_allowed"])

    template = data["packet_template"]
    expected_groups = {"source_certificate", "EndE_domain", "EndE_to_BN_functor", "rhoE_transition_data", "operator_payload"}
    check("required groups", set(template) == expected_groups, template.keys())
    check("required field count", data["field_counts"]["required"] == cert["required_fields"] == 14, data["field_counts"])
    check("no values filled", data["field_counts"]["filled_values"] == 0 and data["field_counts"]["source_emitted"] == 0 and data["field_counts"]["same_branch_selected"] == 0, data["field_counts"])
    check("functor fields present", {"basis_map_matrix", "commuting_projection_certificate", "gap_transfer_certificate"} <= set(template["EndE_to_BN_functor"]), template["EndE_to_BN_functor"])
    check("rhoE fields present", {"nonidentity_rho_E", "curvature_or_cocycle", "shared_line_compatibility"} <= set(template["rhoE_transition_data"]), template["rhoE_transition_data"])
    check("operator fields present", {"D_E_or_E_Qa_matrix", "positive_spectrum_or_gap", "finite_part_regularization"} <= set(template["operator_payload"]), template["operator_payload"])
    check("acceptance fails now", data["acceptance"]["passes_now"] is False and data["decision"]["same_source_identity_proved"] is False, data["acceptance"])
    check("guardrails", not any(data["guardrails"].values()), data["guardrails"])
    check("note records template", "Packet Template" in NOTE.read_text(encoding="utf-8") and cert["next_required_artifact"] in NOTE.read_text(encoding="utf-8"), NOTE)

    print("\nSelected heterotic End(E)->B_N functor / rho_E transition value-packet audit")


if __name__ == "__main__":
    main()
