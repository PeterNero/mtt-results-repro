"""Audit the U1/Y Route-C same-source matter-slot packet or residual gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_samesource_matter_slot_overlap_operatorpacket_or_selected_residual.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_samesource_matter_slot_overlap_operatorpacket_or_selected_residual.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_samesource_matter_slot_overlap_operatorpacket_or_selected_residual_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_SameSource_MatterSlot_Overlap_OperatorPacket_or_SelectedResidual_v1.md"

STATUS = "U1Y_ROUTEC_SAMESOURCE_PACKET_REDUCED_VISIBLE_OPERATOR_OR_PRIMITIVE_C1_OPEN"
NEXT = "Selected_U1Y_RouteC_SelectedVisibleOperatorSource_or_PrimitiveC1Contractions_v1"


def check(name: str, ok: bool, detail: object) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}: {name} -- {detail}")
    return ok


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    data = json.loads(DATA.read_text(encoding="utf-8"))
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = NOTE.read_text(encoding="utf-8")
    decision = data["decision"]
    reduction = data["reduction"]
    guardrails = data["guardrails"]
    rows = reduction["same_source_packet_fill"]["rows"]
    audit_checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("seven-field no-go", decision["seven_field_packet_validator_nogo"] is True and len(rows) == 7, rows.keys()),
        check("support not selection", decision["support_fields_present"] == 6 and decision["selected_fields_emitted"] == 0 and decision["same_source_emitted"] == 0, decision),
        check("reduced AH stability carried", decision["reduced_AH_global_stability_proved"] is True and reduction["selected_residual_or_stability_lane"]["finite_without_cutoff"] is True, reduction["selected_residual_or_stability_lane"]),
        check("subvalidators pass only", decision["selected_ordered_source_subvalidator_passes"] is True and decision["selected_s3_class_subvalidator_passes"] is True and decision["visible_operator_source_validator_passes"] is False, decision),
        check("primitive C1 open", reduction["visible_operator_or_primitive_c1_lane"]["primitive_missing_atom_count"] == 24 and decision["primitive_C1_contractions_emitted"] is False, reduction["visible_operator_or_primitive_c1_lane"]),
        check("no downstream closure", data["closure_claimed"] is False and decision["A_selected_or_b_selected_emitted"] is False and decision["lambda_12_computable"] is False, decision),
        check("guardrails", guardrails["promotes_hypothetical_full_plumbing"] is False and guardrails["uses_observed_or_benchmark_inputs"] is False, guardrails),
        check("note documents seven fields", "Seven Required Fields" in note and "Primitive C1 Contract" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C same-source packet/residual audit")
    return 0 if all(audit_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
