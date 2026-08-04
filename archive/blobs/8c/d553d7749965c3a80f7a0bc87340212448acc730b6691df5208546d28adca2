"""Audit CONST-EW-02 B20 matter-slot overlap static import."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b20_matterslot_overlap_static_import"
DATA = ROOT / "candidate_data"
BASE = DATA / SLUG
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(DATA / f"{SLUG}.candidate.json")
    imported = load(BASE / "smslot_static_matterslot_overlap_import.packet.json")
    boundary = load(BASE / "weak_mixing_b20_boundary.packet.json")
    next_work = load(BASE / "next_labeled_workorder.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("imported", imported),
        ("boundary", boundary),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed closure")

    require(candidate["theorem"]["proved"] is True, "B20 theorem did not prove")
    require(candidate["static_matterslot_overlap_blocker_retired"] is True, "static blocker not retired")
    require(candidate["dynamic_C1_promoted"] is False, "dynamic C1 overpromoted")
    require(candidate["strict_xL_emitted_now"] is False, "xL overemitted")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")
    require(cert["static_matterslot_overlap_blocker_retired"] is True, "certificate missing static blocker retirement")
    require(cert["dynamic_C1_promoted"] is False, "certificate dynamic C1 overpromoted")

    closes = imported["static_import_closes"]
    require(closes["selected_sector_route_Z_to_u_e_X_to_d_nuD"] is True, "static sector route not imported")
    require(closes["selected_1M_Dirac_neutrino_shift_rule"] is True, "1M Dirac rule not imported")
    require(closes["selected_overlap_transfer_normalization"] is True, "overlap normalization not imported")
    require(closes["selected_SMSlotFunctor_all_six_arrows"] is True, "all six arrows not imported")
    require(closes["static_readout_closed"] is True, "static readout not imported")
    require(closes["target_fitting_excluded"] is True, "target fitting not excluded")

    values = imported["static_values"]
    require(values["phase_route"] == ["u", "e"], "phase route wrong")
    require(values["shift_route"] == ["d", "nuD"], "shift route wrong")
    require(values["matter_triplet_rank"] == 3, "matter triplet rank wrong")
    require("rho_s(T_i)/sqrt(2)" in values["unit_trace_transfer"], "unit trace transfer missing")

    dynamic = imported["dynamic_tier_not_promoted"]
    require(dynamic["dynamic_visible_routec_operator_source_identity"] is True, "dynamic source identity not left open")
    require(dynamic["selected_D_E_Riesz_Green_dotD"] is True, "D_E/Riesz/Green/dotD not left open")
    require(dynamic["selected_dynamic_overlap_tensor_or_transfer_functor"] is True, "dynamic overlap not left open")
    require(dynamic["selected_primitive_C1_contractions"] is True, "primitive C1 not left open")
    require(dynamic["selected_b_selected_and_Hessian_normalization"] is True, "b/Hessian not left open")
    require(dynamic["promote_conditional_A_to_A_selected"] is True, "A_selected promotion not left open")

    require(boundary["closed_now"]["b19_matter_slot_overlap_static_blocker_retired"] is True, "boundary static blocker not retired")
    require(boundary["closed_now"]["selected_static_sector_route_Z_to_u_e_X_to_d_nuD"] is True, "boundary route not closed")
    require(boundary["closed_now"]["selected_static_1M_Dirac_neutrino_shift_rule"] is True, "boundary 1M not closed")
    require(boundary["closed_now"]["selected_static_trace_transfer_normalization"] is True, "boundary trace normalization not closed")
    require(boundary["still_open"]["selected_dynamic_overlap_tensor_or_transfer_functor"] is True, "boundary dynamic overlap not open")
    require(boundary["still_open"]["selected_primitive_C1_contractions"] is True, "boundary primitive C1 not open")
    require(boundary["still_open"]["actual_xL_source_emission"] is True, "boundary xL not open")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "boundary weak angle not open")

    require(next_work["active_label"] == "CONST-EW-02 / WEAK-MIXING / B21-DYNAMIC-C1-OR-ENDE-FINITE-RESPONSE", "wrong B21 label")
    require("DYNAMIC-OVERLAP" in next_work["primary"]["label"], "primary B21 route wrong")
    require("ENDE-RHOE-FINITE-RESPONSE" in next_work["fallback"]["label"], "fallback B21 route wrong")

    print("CONST-EW-02 B20 matter-slot overlap static import audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
