"""Audit the U1/Y Route-C alpha1 tangent or retarded-overlap kernel gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_alpha1_tangent_or_retarded_overlap_kernel.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_alpha1_tangent_or_retarded_overlap_kernel.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_alpha1_tangent_or_retarded_overlap_kernel_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_Alpha1_Tangent_or_RetardedOverlap_Kernel_v1.md"

STATUS = "U1Y_ROUTEC_ALPHA1_TANGENT_KERNEL_REDUCED_MATTERSLOT_SOURCE_OPEN"
NEXT = "Selected_U1Y_RouteC_SameSource_MatterSlot_Overlap_OperatorPacket_or_SelectedResidual_v1"


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
    required = data["reduction"]["matter_slot_overlap_route"]["required_fields"]
    guardrails = data["guardrails"]
    audit_checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("support carried", decision["retarded_ckm_kernel_pattern_available"] is True and decision["source_level_weyl_carrier_available"] is True, decision),
        check("conditional A remains conditional", decision["conditional_weylpair_A_rank_solve_available"] is True and data["reduction"]["conditional_weylpair_A_route"]["is_A_selected"] is False, data["reduction"]["conditional_weylpair_A_route"]),
        check("matter packet is open", all(field["selected_emitted"] is False for field in required.values()), required),
        check("tangent not emitted", decision["selected_BN_tangent_or_retarded_kernel"] is False and decision["honest_dotD_replay_from_kernel"] is False, decision),
        check("normalization and sector open", decision["selected_sector_charge_or_chirality"] is False and decision["selected_transfer_normalization"] is False, decision),
        check("no closure overreach", data["closure_claimed"] is False and decision["lambda_12_computable"] is False and decision["A_selected_or_b_selected_emitted"] is False, decision),
        check("guardrails", guardrails["promotes_conditional_A_to_A_selected"] is False and guardrails["uses_observed_or_benchmark_inputs"] is False, guardrails),
        check("note records packet fields", "Required Packet Fields" in note and "Do not promote the conditional 72x2" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C alpha1 tangent/retarded-kernel audit")
    return 0 if all(audit_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
