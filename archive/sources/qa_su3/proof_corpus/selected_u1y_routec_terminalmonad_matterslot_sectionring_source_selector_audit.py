"""Audit the U1/Y Route-C terminal-monad matter-slot section-ring selector gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "build_selected_u1y_routec_terminalmonad_matterslot_sectionring_source_selector.py"
DATA = REPO / "candidate_data" / "selected_u1y_routec_terminalmonad_matterslot_sectionring_source_selector.candidate.json"
CERT = REPO / "certificates" / "selected_u1y_routec_terminalmonad_matterslot_sectionring_source_selector_certificate.json"
NOTE = REPO / "proof_corpus" / "Selected_U1Y_RouteC_TerminalMonad_MatterSlot_SectionRing_SourceSelector_v1.md"

STATUS = "U1Y_ROUTEC_TERMINALMONAD_MATTERSLOT_SELECTOR_REDUCED_BASEORDER_AHBINDING_SLOTMAP_OPEN"
NEXT = "Selected_U1Y_RouteC_TerminalMonad_BaseOrder_AHBinding_SMSlotMap_v1"


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
    terminal = data["imported_terminal_candidate"]
    pic0 = data["ordered_layer_pic0_result"]
    obligations = data["source_selector_obligations"]
    slot = data["slot_map_contract"]
    decision = data["decision"]
    guardrails = data["guardrails"]
    checks = [
        check("status", data["status"] == STATUS and cert["status"] == STATUS, cert["status"]),
        check("script reruns", len([line for line in proc.stdout.splitlines() if line.startswith("wrote ")]) == 3, proc.stdout),
        check("next artifact", data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT and NEXT in note, cert["next_required_artifact"]),
        check("L3-K2 candidate imported", terminal["forced_label"] == "L3-K2" and terminal["forced_value"] == [1, -2, 0] and terminal["forced_double"] == [2, -4, 0] and terminal["closed_as_unique_candidate"] is True, terminal),
        check("not selected yet", terminal["selected_by_mtt"] is False and decision["terminal_monad_lane_selected_by_MTT"] is False, terminal),
        check("ordered Pic0 only", pic0["ordered_layer_pic0_removed_as_blocker"] is True and pic0["operator_layer_pic0_closed"] is False, pic0),
        check("obligations all open", cert["closed_obligations"] == 0 and cert["required_obligations"] == len(obligations) and all(row["closed"] is False for row in obligations.values()), obligations),
        check("AH support but not selected", obligations["AH_or_Cech_transition_binding_selected"]["support_closed"] is True and obligations["AH_or_Cech_transition_binding_selected"]["closed"] is False, obligations["AH_or_Cech_transition_binding_selected"]),
        check("slot map exact and open", slot["closed"] is False and slot["must_map_without_locked_C1_columns"]["10_M_clock"] == ["u", "e"] and slot["must_map_without_locked_C1_columns"]["1_M_Dirac_shift"] == ["nuD"] and slot["must_preserve_q79_polarization"]["U_bar5"] == "F", slot),
        check("no orientation promotion", decision["selected_matter_slot_orientation_emitted"] is False and decision["selected_U10_Ubar5_polarization_emitted"] is False and decision["alpha1_driver_verified"] is False, decision),
        check("guardrails hold", guardrails["claims_selected_matter_slot_orientation"] is False and guardrails["uses_locked_C1_columns"] is False and data["target_fitting_used"] is False, guardrails),
        check("note records boundaries", "Do not treat the unique `L3-K2` candidate" in note and "Do not inherit ordered-layer Pic0" in note, NOTE),
    ]
    print("\nSelected U1/Y Route-C terminal-monad matter-slot section-ring selector audit")
    return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
