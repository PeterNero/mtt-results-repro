"""Audit the smooth projective rho_E operator source packet fill attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build_selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_fillattempt.py"
DATA = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_fillattempt.candidate.json"
CERT = ROOT / "certificates" / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_fillattempt_certificate.json"
PACKET = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket.fill_attempt.json"
MISSING = ROOT / "candidate_data" / "selected_heterotic_projectiverhoe_smoothoperator_sourcepacket_missing_leaves.json"
NOTE = ROOT / "proof_corpus" / "Selected_Heterotic_ProjectiveRhoE_SmoothOperator_SourcePacket_FillAttempt_v1.md"

STATUS = "HETEROTIC_PROJECTIVERHOE_SMOOTHOPERATOR_SOURCEPACKET_FILL_ATTEMPT_SUPPORT_FILLED_VALUES_OPEN"
NEXT = "Selected_Heterotic_ProjectiveRhoE_RepresentativeToCocycleMap_or_SmoothFinitePart_SourceAmendment_v1"


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
    missing = load(MISSING)
    note = NOTE.read_text(encoding="utf-8")

    check("status", data["status"] == STATUS and cert["status"] == STATUS, (data["status"], cert["status"]))
    check("next artifact", data["decision"]["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, data["decision"])
    check("support filled", data["decision"]["support_context_filled"] is True and cert["support_context_filled"] is True, data["fill_result"])
    check("source support fields true", data["fill_result"]["same_branch_strominger_iwasawa_context"] is True and data["fill_result"]["fixed_differential_class_context"] is True and data["fill_result"]["primitive_central_support"] is True, data["fill_result"])
    check("selected source values absent", data["fill_result"]["selected_representative_filled"] is False and data["fill_result"]["representative_to_central_cocycle_map_filled"] is False and data["fill_result"]["projective_rhoE_transition_tables_filled"] is False, data["fill_result"])
    check("operator values absent", data["decision"]["bundle_operator_values_filled"] is False and data["decision"]["E_Qa_computed"] is False and packet["bundle_operator"]["E_Qa_matrix_or_zero_order_block"] is None, packet["bundle_operator"])
    check("finite part absent", data["decision"]["finite_part_values_filled"] is False and packet["finite_part"]["finite_part_value"] is None, packet["finite_part"])
    check("admissibility absent", data["decision"]["admissibility_values_filled"] is False and packet["admissibility"]["Freed_Witten_or_twisted_admissibility"] is None and packet["admissibility"]["projector_retention"] is None, packet["admissibility"])
    check("missing leaves", missing["status"] == "VALUES_OPEN" and len(missing["hard_missing"]) >= 16 and len(missing["legal_repairs"]) == 5, missing)
    check("cross checks retain blockers", data["cross_checks"]["central_search_map_verified"] is False and data["cross_checks"]["typed_projective_tables_emitted"] is False and data["cross_checks"]["trace_lift_no_go_retained"] is True, data["cross_checks"])
    check("no closure", data["closure_claimed"] is False and cert["closure_claimed"] is False and cert["smooth_operator_source_packet_filled"] is False, cert)
    check("guardrails", all(v is True for k, v in data["guardrails"].items() if k != "target_fitting_used") and data["guardrails"]["target_fitting_used"] is False, data["guardrails"])
    check("note records missing", NEXT in note and "Still Missing" in note and str(MISSING.relative_to(ROOT)) in note, NOTE)

    print("\nSelected heterotic projective rho_E smooth-operator source-packet fill audit")


if __name__ == "__main__":
    main()
