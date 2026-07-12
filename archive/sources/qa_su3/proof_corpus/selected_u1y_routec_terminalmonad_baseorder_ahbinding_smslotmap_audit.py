"""Audit the U1/Y Route-C terminal-monad base-order/AH-binding/slot-map gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_terminalmonad_baseorder_ahbinding_smslotmap.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_terminalmonad_baseorder_ahbinding_smslotmap.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_terminalmonad_baseorder_ahbinding_smslotmap_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_TerminalMonad_BaseOrder_AHBinding_SMSlotMap_v1.md"

STATUS = "U1Y_ROUTEC_TERMINALMONAD_BASEORDER_AHBINDING_PROVED_SLOTMAP_SUPPORT_COMPLETE_BRANCHCOHERENCE_OPEN"
NEXT = "Selected_U1Y_RouteC_BranchCoherence_Selector_or_FiniteValidatorReplay_v1"


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
    base = data["baseorder_binding"]
    slot = data["slot_map"]
    decision = data["decision"]
    guardrails = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("same L3-K2 identity", base["same_L3_K2_identity"] is True and base["selected_L"] == [1, -2, 0] and base["selected_L2"] == [2, -4, 0], base),
        check("ordered source layer closes", cert["terminal_lane_selected_at_ordered_source_layer_under_explicit_principle"] is True and base["base_factor_order_selected_at_ordered_source_layer"] is True, base),
        check("AH binding closes at ordered layer", cert["AH_goodcover_binding_selected_at_ordered_source_layer"] is True and base["scope"] == "ordered Chern/H1/ordinary-curvature/stability layer only", base),
        check("principle dependency honest", base["principle_dependency"] is True and base["principle_unconditional_in_mtt_axioms"] is False, base),
        check("slot support complete", cert["slot_map_support_complete"] is True and slot["finite_structural_route"]["10_M_clock"] == "I_3" and slot["finite_structural_route"]["bar5_M_shift"] == "F", slot),
        check("slot not selected same branch", cert["slot_map_selected_same_branch"] is False and decision["selected_matter_slot_orientation_emitted"] is False, decision),
        check("operator closure still open", cert["operator_layer_Pic0_closed"] is False and cert["alpha1_driver_verified"] is False and cert["lambda_12_closed"] is False, cert),
        check("guardrails hold", guardrails["claims_selected_same_branch_slotmap"] is False and guardrails["uses_observed_data"] is False and guardrails["uses_locked_C1_columns"] is False, guardrails),
        check("note records boundary", "support-complete, not yet selected same-branch" in note and "operator-layer Pic0" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C terminal-monad base-order/AH-binding/slot-map audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
