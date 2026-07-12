"""Audit the U1/Y Route-C terminal-orientation branch-coherence bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_terminal_orientation_branchcoherence_bridge.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_terminal_orientation_branchcoherence_bridge.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_terminal_orientation_branchcoherence_bridge_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_Terminal_Orientation_BranchCoherence_Bridge_v1.md"

STATUS = "U1Y_ROUTEC_TERMINAL_ORIENTATION_BRIDGE_ORDERED_SELECTOR_CLOSED_OPERATOR_EMISSION_OPEN"
NEXT = "Selected_U1Y_RouteC_OperatorEmission_and_OverlapNormalization_from_TerminalSlotMap_v1"


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
    ordered = data["ordered_orientation"]
    bridge = data["replay_bridge"]
    gap = data["emission_gap"]
    guardrails = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("ordered orientation closes", ordered["closed"] is True and cert["ordered_matter_slot_orientation_selector_closed"] is True, ordered),
        check("phase shift exact", ordered["phase_sectors"] == ["u", "e"] and ordered["shift_sectors"] == ["d", "nuD"], ordered),
        check("1M shift exact", ordered["shift_packet"]["one_M_Dirac_shift"]["1_M"] == "N^c" and cert["selected_1M_Dirac_shift_at_ordered_layer"] is True, ordered["shift_packet"]),
        check("HYM no-go retained", bridge["hym_replay_orientation_nogo_retained"] is True and guardrails["claims_hym_replay_selects_orientation"] is False, bridge),
        check("operator emission open", gap["same_branch_selected_operator_emission"] is False and cert["same_branch_selected_operator_emission"] is False, gap),
        check("normalization and alpha open", cert["selected_overlap_normalization_emitted"] is False and cert["alpha1_driver_verified"] is False and cert["lambda_12_closed"] is False, cert),
        check("no target fitting", guardrails["uses_observed_data"] is False and guardrails["uses_locked_C1_columns"] is False and data["target_fitting_used"] is False, guardrails),
        check("note records boundary", "without contradicting the HYM replay no-go" in note and "same-branch operator emission" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C terminal-orientation branch-coherence bridge audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
