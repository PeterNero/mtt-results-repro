"""Audit Phi_fin payload/global-destabilizer closing run with slot reconciliation."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phifinpayload_or_globaldestabilizerenumeration_closingrun"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
RECONCILIATION = PACKET_DIR / "stationary_phifin_slot_reconciliation.packet.json"
SLOT_CLOSURE = PACKET_DIR / "riesz_green_dotd_projector_slot_closure.packet.json"
FRONTIER = PACKET_DIR / "post_four_slot_true_equivalence_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFinPayload_or_GlobalDestabilizerEnumeration_ClosingRun_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PHIFINPAYLOAD_OR_GLOBALDESTABILIZERENUMERATION_CLOSINGRUN_BUILT_RIESZ_DOTD_SLOT_CLOSED"
NEXT = "MTT_Selected_ChernWeilHYMDE_or_DeterminantTorsion_FourSlotClosingRun_v1"
SLOT = "Riesz_Green_dotD_projector_retention"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    reconciliation = load(RECONCILIATION)
    slot = load(SLOT_CLOSURE)
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(reconciliation["slot"] == SLOT, "reconciled slot mismatch")
    require(reconciliation["slot_closes"] is True, "slot should close")
    inputs = reconciliation["closure_inputs"]
    for key, value in inputs.items():
        require(value is True, f"closure input not true: {key}")
    superset = reconciliation["superset_explanation"]
    require(superset["using_one_straight_way"] is False, "superset mode not recorded")
    for excluded in [
        "same-source Chern-Weil row",
        "selected HYM/Strominger or Route-C residual",
        "transition rho_E/Cech-Dolbeault D_E payload",
        "dynamic Phi_fin^C1 or primitive C1 response",
    ]:
        require(excluded in superset["not_claimed"], f"missing no-claim guard: {excluded}")

    require(slot["filled_slot"] == SLOT, "slot closure filled wrong slot")
    require(slot["closure_result"]["selected_source_value_emitted"] is True, "selected source value not emitted")
    require(slot["closure_result"]["riesz_green_dotd_projector_slot_closed"] is True, "slot not closed")
    require(slot["closure_result"]["actual_dynamic_QaSU3_operator_packet_closed"] is False, "dynamic packet overclosed")
    source = slot["selected_source_value"]
    require(source["source_selected_by_mtt"] is True, "source not selected")
    require(source["stationary_rho_s_promoted"] is True, "rho_s not promoted")
    require(source["dynamic_C1_scope_excluded"] is True, "dynamic C1 exclusion missing")
    status = slot["slot_status_after_closure"]
    require(status["required_operator_slot_count"] == 8, "required count mismatch")
    require(status["filled_operator_slot_count"] == 4, "filled count should be 4")
    require(status["remaining_missing_slot_count"] == 4, "remaining count should be 4")
    require(SLOT in status["filled_slots"], "slot not in filled slots")
    require(SLOT not in status["missing_slots"], "slot still missing")

    require(frontier["operator_source_slots_closed"] == 4, "frontier closed count mismatch")
    require(frontier["operator_source_slots_remaining"] == 4, "frontier remaining count mismatch")
    for remaining in [
        "same_source_Chern_Weil_row_derived",
        "selected_HYM_or_RouteC_residual",
        "transition_rhoE_or_Cech_Dolbeault_DE_data",
        "finite_determinant_heat_spectrum_or_torsion_response",
    ]:
        require(remaining in frontier["remaining_slots"], f"remaining slot absent: {remaining}")
    require(frontier["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(frontier["no_knob_closed"] is False, "no-knob overclosed")

    closure = data["closure_decision"]
    require(closure["operator_source_slots_closed_total"] == 4, "candidate closed count mismatch")
    require(closure["operator_source_slots_remaining"] == 4, "candidate remaining count mismatch")
    require(closure["Riesz_Green_dotD_projector_retention_slot_closed"] is True, "candidate slot closure missing")
    require(closure["actual_dynamic_QaSU3_operator_packet_closed"] is False, "candidate dynamic overclosed")
    require(data["what_closes_now"]["Riesz_Green_dotD_projector_retention_slot"] is True, "what-closes flag missing")
    require(data["what_remains_open"]["same_source_Chern_Weil_row"] is True, "Chern-Weil should remain open")
    require(data["what_remains_open"]["transition_rhoE_or_Cech_Dolbeault_DE_data"] is True, "D_E should remain open")
    require(data["closure_claimed"] is True, "candidate should claim this slot closure")

    require("Current count is now four closed operator-source slots and four open slots" in note, "note count missing")
    require("It does not close the same-source Chern-Weil row" in note, "note no-claim missing")

    for packet in [data, reconciliation, slot, frontier, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
