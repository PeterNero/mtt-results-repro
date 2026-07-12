"""Audit the heterotic End(E)->B_N / rho_E value-packet fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_ende_to_bn_functor_or_rhoe_transition_valuepacket_fill.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_ende_to_bn_functor_or_rhoe_transition_valuepacket_fill.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_ende_to_bn_functor_or_rhoe_transition_valuepacket_fill_certificate.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_EndE_to_BN_Functor_or_RhoETransitionData_ValuePacket_Fill_v1.md"

STATUS = "HETEROTIC_ENDE_TO_BN_FUNCTOR_OR_RHOE_TRANSITION_VALUEPACKET_FILL_PARTIAL_SOURCECERT_VALUES_OPEN"


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
    check("fill executed", data["decision"]["fill_attempt_executed"] is True and cert["fill_attempt_executed"] is True, data["decision"])
    check("source certificate closed only", data["decision"]["source_certificate_leaves_closed"] is True and data["field_counts"]["source_emitted"] == 2 and data["field_counts"]["same_branch_selected"] == 2, data["field_counts"])
    check("field count exact", data["field_counts"]["required"] == 14 and data["field_counts"]["filled_values"] == 2, data["field_counts"])
    check("support count broad but not closure", data["field_counts"]["support_present"] >= 10 and data["closure_claimed"] is False, data["field_counts"])

    packet = data["filled_packet"]
    check("EndE basis not filled", packet["EndE_domain"]["finite_EndE_basis"]["source_emitted"] is False and packet["EndE_domain"]["finite_EndE_basis"]["value"] is None, packet["EndE_domain"]["finite_EndE_basis"])
    check("functor not filled", packet["EndE_to_BN_functor"]["basis_map_matrix"]["source_emitted"] is False and packet["EndE_to_BN_functor"]["basis_map_matrix"]["value"] is None, packet["EndE_to_BN_functor"])
    check("rhoE not filled", packet["rhoE_transition_data"]["nonidentity_rho_E"]["source_emitted"] is False and packet["rhoE_transition_data"]["nonidentity_rho_E"]["value"] is None, packet["rhoE_transition_data"]["nonidentity_rho_E"])
    check("operator not filled", packet["operator_payload"]["D_E_or_E_Qa_matrix"]["source_emitted"] is False and packet["operator_payload"]["finite_part_regularization"]["source_emitted"] is False, packet["operator_payload"])

    blockers = data["blockers"]
    check("next blocker named", blockers["first_true_value_blocker"] == "selected finite End(E) domain basis or nonidentity rho_E transition packet", blockers)
    check("no closure", data["decision"]["same_source_identity_proved"] is False and data["decision"]["E_Qa_computed"] is False and data["decision"]["computed_threshold_value"] is False, data["decision"])
    check("guardrails", not any(data["guardrails"].values()), data["guardrails"])
    check("note records next", cert["next_required_artifact"] in NOTE.read_text(encoding="utf-8"), NOTE)

    print("\nSelected heterotic End(E)->B_N / rho_E value-packet fill audit")


if __name__ == "__main__":
    main()
