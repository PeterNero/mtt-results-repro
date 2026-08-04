"""Audit Chern-Weil/D_E/determinant-torsion three-slot closing run."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_chernweilde_or_determinanttorsion_threeslotclosingrun"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RECON = PACKET_DIR / "same_source_chern_weil_row_reconciliation.packet.json"
SLOT_CLOSURE = PACKET_DIR / "same_source_chern_weil_row_slot_closure.packet.json"
FRONTIER = PACKET_DIR / "post_six_slot_true_equivalence_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ChernWeilDE_or_DeterminantTorsion_ThreeSlotClosingRun_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_CHERNWEILDE_OR_DETERMINANTTORSION_THREESLOTCLOSINGRUN_BUILT_CHERNWEIL_SLOT_CLOSED"
NEXT = "MTT_Selected_DETransition_or_DeterminantTorsion_TwoSlotClosingRun_v1"
SLOT = "same_source_Chern_Weil_row_derived"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    recon = load(RECON)
    slot = load(SLOT_CLOSURE)
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(recon["slot"] == SLOT, "reconciled slot mismatch")
    require(recon["slot_closes"] is True, "Chern-Weil row slot should close")
    for key, value in recon["proof_inputs"].items():
        require(value is True, f"Chern-Weil closure input false: {key}")
    scope = recon["scope"]
    for no_claim in [
        "transition rho_E/Cech-Dolbeault D_E data",
        "finite determinant/heat spectrum/torsion response",
        "pointwise finite curvature representative table",
        "full sector-ready Qa/SU3 dynamic operator packet",
        "full no-knob Standard Model data derivation",
    ]:
        require(no_claim in scope["does_not_close"], f"missing no-claim guard: {no_claim}")

    row = slot["same_source_chern_weil_row"]
    require(row["level"] == "same-source Chern/Bianchi cohomology row", "row level mismatch")
    require(row["branch"] == {"orientation": "F", "q": 79, "torsion_label_m": 1}, "branch mismatch")
    require(row["L_vector_abc"] == [1, -2, 0], "L vector mismatch")
    require(row["L_squared_vector_abc"] == [2, -4, 0], "L^2 vector mismatch")
    require(row["c1_V_alpha"] == [0, 0, 0], "c1 mismatch")
    require(row["c2_V_alpha"] == [4, 0, 0], "c2 mismatch")
    require(row["ch2_math"] == [-4, 0, 0], "ch2 mismatch")
    require("pointwise finite transition representative" in row["chern_weil_trace_normalization_note"], "row guard missing")

    require(slot["filled_slot"] == SLOT, "slot closure filled wrong slot")
    require(slot["closure_result"]["same_source_Chern_Weil_row_derived"] is True, "slot not closed")
    require(slot["closure_result"]["transition_rhoE_or_Cech_Dolbeault_DE_data_closed"] is False, "D_E overclosed")
    require(slot["closure_result"]["finite_determinant_heat_spectrum_or_torsion_response_closed"] is False, "torsion overclosed")
    require(slot["closure_result"]["actual_dynamic_QaSU3_operator_packet_closed"] is False, "dynamic packet overclosed")
    status = slot["slot_status_after_closure"]
    require(status["required_operator_slot_count"] == 8, "required slot count mismatch")
    require(status["filled_operator_slot_count"] == 6, "filled slot count should be 6")
    require(status["remaining_missing_slot_count"] == 2, "remaining slot count should be 2")
    require(SLOT in status["filled_slots"], "Chern-Weil slot not filled")
    require(SLOT not in status["missing_slots"], "Chern-Weil slot still missing")

    require(frontier["operator_source_slots_closed"] == 6, "frontier closed count mismatch")
    require(frontier["operator_source_slots_remaining"] == 2, "frontier remaining count mismatch")
    require(frontier["remaining_slots"] == [
        "finite_determinant_heat_spectrum_or_torsion_response",
        "transition_rhoE_or_Cech_Dolbeault_DE_data",
    ] or frontier["remaining_slots"] == [
        "transition_rhoE_or_Cech_Dolbeault_DE_data",
        "finite_determinant_heat_spectrum_or_torsion_response",
    ], "frontier remaining slots mismatch")
    require(frontier["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(frontier["no_knob_closed"] is False, "no-knob overclosed")

    closure = data["closure_decision"]
    require(closure["operator_source_slots_closed_total"] == 6, "candidate closed count mismatch")
    require(closure["operator_source_slots_remaining"] == 2, "candidate remaining count mismatch")
    require(closure["same_source_Chern_Weil_row_derived_slot_closed"] is True, "candidate slot closure missing")
    require(closure["transition_rhoE_or_Cech_Dolbeault_DE_data_closed"] is False, "candidate D_E overclosed")
    require(closure["finite_determinant_heat_spectrum_or_torsion_response_closed"] is False, "candidate torsion overclosed")
    require(closure["actual_dynamic_QaSU3_operator_packet_closed"] is False, "candidate dynamic overclosed")
    require(data["what_closes_now"]["Chern_Bianchi_row_level_only"] is True, "row-level guard missing")
    require(data["what_remains_open"]["transition_rhoE_or_Cech_Dolbeault_DE_data"] is True, "D_E should remain open")
    require(data["what_remains_open"]["finite_determinant_heat_spectrum_or_torsion_response"] is True, "torsion should remain open")
    require(data["closure_claimed"] is True, "candidate should claim Chern-Weil slot closure")

    require("cohomology/Chern-Bianchi row level" in note, "note row-level guard missing")
    require("does not emit transition `rho_E`/Cech-Dolbeault `D_E` tables" in note, "note D_E guard missing")
    require("Current count is now six closed operator-source slots and two open slots" in note, "note count missing")

    for packet in [data, recon, slot, frontier, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
