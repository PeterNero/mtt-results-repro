"""Audit the selected U1/Y matter-slot charge/overlap theorem gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_selected_matter_slot_charge_and_overlap_normalization_theorem.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_selected_matter_slot_charge_and_overlap_normalization_theorem_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_Selected_MatterSlot_Charge_and_Overlap_Normalization_Theorem_v1.md"

STATUS = "U1Y_ROUTEC_SELECTED_MATTERSLOT_CHARGE_OVERLAP_THEOREM_REDUCED_SAMESOURCE_OPERATOR_PACKET_OPEN"
NEXT = "Selected_U1Y_RouteC_SameSource_OperatorPacket_Fill_or_NoGo_v1"


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
    counts = data["same_source_operator_packet_summary"]["field_counts"]
    guards = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("theorem reduction proved", data["theorem"]["proved"] is True and decision["theorem_reduction_proved"] is True, data["theorem"]),
        check("finite algebra not blocker", decision["finite_algebra_is_not_blocker"] is True and decision["conditional_routing_and_normalization_exact"] is True, decision),
        check("field counts", counts["required"] == 7 and counts["support_present"] == 6 and counts["selected_emitted"] == 0, counts),
        check("N alpha support carried", cert["candidate_value_N_alpha1_h_ext"] == 1.0 and decision["selected_value_N_alpha1_h_ext_promoted"] is False, cert),
        check("driver not promoted", decision["alpha1_driver_verified_now"] is False and decision["honest_dotD_validator_closed_now"] is False, decision),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("guardrails", guards["claims_selected_matter_slot_charge"] is False and guards["claims_selected_N_alpha1_value"] is False and guards["uses_observed_or_benchmark_inputs"] is False, guards),
        check("note documents promotion boundary", "promotes `N_alpha1(h_ext)=1`" in note and "zero fields are selected-emitted" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C matter-slot charge/overlap theorem audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
