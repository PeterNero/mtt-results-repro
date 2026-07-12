"""Audit Chern-Weil/HYM/D_E/determinant-torsion closing run."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_chernweilhymde_or_determinanttorsion_fourslotclosingrun"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
HYM_RECON = PACKET_DIR / "selected_hym_residual_slot_reconciliation.packet.json"
SLOT_CLOSURE = PACKET_DIR / "selected_hym_or_routec_residual_slot_closure.packet.json"
FRONTIER = PACKET_DIR / "post_five_slot_true_equivalence_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ChernWeilHYMDE_or_DeterminantTorsion_FourSlotClosingRun_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_CHERNWEILHYMDE_OR_DETERMINANTTORSION_FOURSLOTCLOSINGRUN_BUILT_HYM_SLOT_CLOSED"
NEXT = "MTT_Selected_ChernWeilDE_or_DeterminantTorsion_ThreeSlotClosingRun_v1"
SLOT = "selected_HYM_or_RouteC_residual"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    recon = load(HYM_RECON)
    slot = load(SLOT_CLOSURE)
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(recon["slot"] == SLOT, "reconciled slot mismatch")
    require(recon["slot_closes"] is True, "HYM slot should close")
    for key, value in recon["closure_inputs"].items():
        require(value is True, f"HYM closure input false: {key}")
    scope = recon["scope"]
    for no_claim in [
        "same-source Chern-Weil row",
        "full transition rho_E/Cech-Dolbeault D_E sector payload",
        "finite determinant/heat/torsion response",
        "dynamic Phi_fin^C1/primitive response",
    ]:
        require(no_claim in scope["does_not_close"], f"missing no-claim guard: {no_claim}")

    require(slot["filled_slot"] == SLOT, "slot closure filled wrong slot")
    require(slot["closure_result"]["selected_source_value_emitted"] is True, "selected source not emitted")
    require(slot["closure_result"]["selected_HYM_or_RouteC_residual_slot_closed"] is True, "slot not closed")
    require(slot["closure_result"]["actual_dynamic_QaSU3_operator_packet_closed"] is False, "dynamic packet overclosed")
    value = slot["selected_source_value"]
    require(value["source_selected_by_mtt"] is True, "source not selected")
    require(value["determinant_one"] is True, "determinant-one flag missing")
    require(value["final_residual_l2"] < value["tolerance"], "HYM residual not below tolerance")
    status = slot["slot_status_after_closure"]
    require(status["required_operator_slot_count"] == 8, "required slot count mismatch")
    require(status["filled_operator_slot_count"] == 5, "filled slot count should be 5")
    require(status["remaining_missing_slot_count"] == 3, "remaining slot count should be 3")
    require(SLOT in status["filled_slots"], "HYM slot not filled")
    require(SLOT not in status["missing_slots"], "HYM slot still missing")

    require(frontier["operator_source_slots_closed"] == 5, "frontier closed count mismatch")
    require(frontier["operator_source_slots_remaining"] == 3, "frontier remaining count mismatch")
    for remaining in [
        "same_source_Chern_Weil_row_derived",
        "transition_rhoE_or_Cech_Dolbeault_DE_data",
        "finite_determinant_heat_spectrum_or_torsion_response",
    ]:
        require(remaining in frontier["remaining_slots"], f"remaining slot absent: {remaining}")
    require(frontier["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(frontier["no_knob_closed"] is False, "no-knob overclosed")

    closure = data["closure_decision"]
    require(closure["operator_source_slots_closed_total"] == 5, "candidate closed count mismatch")
    require(closure["operator_source_slots_remaining"] == 3, "candidate remaining count mismatch")
    require(closure["selected_HYM_or_RouteC_residual_slot_closed"] is True, "candidate HYM slot closure missing")
    require(closure["actual_dynamic_QaSU3_operator_packet_closed"] is False, "candidate dynamic overclosed")
    require(data["what_closes_now"]["selected_HYM_or_RouteC_residual_slot"] is True, "what-closes flag missing")
    require(data["what_remains_open"]["same_source_Chern_Weil_row"] is True, "Chern-Weil should remain open")
    require(data["what_remains_open"]["transition_rhoE_or_Cech_Dolbeault_DE_data"] is True, "D_E should remain open")
    require(data["closure_claimed"] is True, "candidate should claim HYM slot closure")

    require("Current count is now five closed operator-source slots and three open slots" in note, "note count missing")
    require("This is not a full sector-ready Qa/SU3 operator packet" in note, "note guard missing")

    for packet in [data, recon, slot, frontier, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
