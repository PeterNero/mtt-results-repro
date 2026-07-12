"""Audit CONST-EW-02 B24 u_dyn source derivation import."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b24_udyn_source_derivation_import"
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
    imported = load(BASE / "qa_su3_alpha1_driver_import.packet.json")
    udyn = load(BASE / "udyn_source_derivation_decision.packet.json")
    cross_use = load(BASE / "cross_use_prediction_update.packet.json")
    boundary = load(BASE / "weak_mixing_b24_boundary.packet.json")
    next_work = load(BASE / "next_labeled_workorder.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("imported", imported),
        ("udyn", udyn),
        ("cross_use", cross_use),
        ("boundary", boundary),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed closure")

    require(candidate["theorem"]["proved"] is True, "B24 theorem did not prove")
    require(candidate["u_dyn_source_derived"] is True, "u_dyn not source-derived")
    require(candidate["u_dyn_value"] == 1.0, "u_dyn value not 1")
    require(candidate["source_strength_prefix_closed"] is True, "source-strength prefix not closed")
    require(candidate["physical_weak_angle_closure"] is False, "physical weak angle overclosed")
    require(candidate["strict_full_no_knob_closure"] is False, "strict full no-knob overclosed")

    require(imported["imported_closure"]["selected_N_alpha1_h_ext_value"] is True, "N_alpha1(h_ext) not selected")
    require(imported["imported_closure"]["du_dalpha1_equals_h_ext"] is True, "du/dalpha1 not emitted")
    require(imported["imported_closure"]["alpha1_driver_verified"] is True, "alpha1 driver not verified")
    require(imported["imported_closure"]["honest_dotD_validator_closed"] is True, "honest dotD not closed")
    require(imported["imported_closure"]["observed_data_used"] is False, "QA import used observed data")
    require(imported["guardrails_imported"]["uses_diagnostic_lift_as_proof"] is False, "diagnostic lift used")
    require(imported["guardrails_imported"]["claims_A_selected"] is False, "QA import claims A_selected")
    require(imported["guardrails_imported"]["claims_b_selected"] is False, "QA import claims b_selected")
    require(imported["residual_open_imported"]["primitive_C1_contractions"] is True, "primitive C1 not left open")
    require(imported["residual_open_imported"]["lambda_12"] is True, "lambda12 not left open")

    require(udyn["decision"]["u_dyn_source_derived"] is True, "u_dyn decision not source-derived")
    require(udyn["decision"]["u_dyn_value"] == 1.0, "u_dyn decision value wrong")
    require(udyn["decision"]["not_a_physical_weak_angle_closure"] is True, "u_dyn decision overcloses physical weak angle")
    require(udyn["bridge_replay_update"]["matches_B22_u_dyn_1"] is True, "B22 replay mismatch")
    require(abs(udyn["bridge_replay_update"]["sin2_no_threshold_source_bridge"] - 0.2315309482915084) < 1e-15, "source sin2 bridge drifted")
    require("selected lambda_12 local determinant/spectral table" in udyn["still_not_closed"], "lambda12 missing from open list")
    require("alpha_phys/u_phys physical unit anchor" in udyn["still_not_closed"], "u_phys missing from open list")

    require(cross_use["calibration_mode"] == "source_derived", "cross-use calibration mode wrong")
    require(cross_use["single_value"] == 1.0, "cross-use single value wrong")
    require(cross_use["cross_uses"]["alpha1_source_strength"]["source_derived"] is True, "alpha1 source not derived")
    require(cross_use["cross_uses"]["weak_mixing_no_threshold_bridge"]["physical_closure"] is False, "weak bridge overclosed")
    require(cross_use["cross_uses"]["dynamic_C1_dotD_prefix"]["primitive_C1_atoms_closed"] is False, "primitive atoms overclosed")

    require(boundary["closed_now"]["u_dyn_source_derived_for_source_strength_lane"] is True, "boundary u_dyn not closed")
    require(boundary["closed_now"]["u_dyn_value_locked_to_1"] is True, "boundary u_dyn value not locked")
    require(boundary["closed_now"]["alpha1_driver_verified_imported"] is True, "boundary alpha1 driver not imported")
    require(boundary["closed_now"]["B22_no_threshold_bridge_replayed_with_source_udyn"] is True, "boundary B22 replay not closed")
    require(boundary["still_open"]["physical_weak_angle_closure"] is True, "boundary physical weak angle not open")
    require(boundary["still_open"]["selected_threshold_or_no_threshold_physical_policy"] is True, "threshold policy not open")
    require(boundary["still_open"]["selected_lambda12_spectral_table"] is True, "lambda12 not open")
    require(boundary["still_open"]["all_24_primitive_C1_atoms"] is True, "primitive atoms not open")
    require(boundary["still_open"]["u_phys_source_derivation_or_single_calibration"] is True, "u_phys not open")

    require(next_work["active_label"] == "CONST-EW-02 / WEAK-MIXING / B25-PHYSICAL-EW-GATES-OR-U-PHYS", "wrong B25 label")
    require("LAMBDA12-SPECTRAL-TABLE" in next_work["primary"]["label"], "primary B25 route wrong")
    require("U-PHYS-SOURCE-DERIVATION" in next_work["parallel"]["label"], "parallel B25 route wrong")
    require("PRIMITIVE-C1-ATOM-TABLE" in next_work["c1"]["label"], "C1 B25 route wrong")

    require(cert["u_dyn_source_derived"] is True, "certificate u_dyn not source-derived")
    require(cert["u_dyn_value"] == 1.0, "certificate u_dyn value wrong")
    require(cert["alpha1_driver_verified_imported"] is True, "certificate alpha1 missing")
    require(cert["selected_dotD_source_verified_imported"] is True, "certificate dotD missing")
    require(cert["physical_weak_angle_closure"] is False, "certificate weak angle overclosed")
    require(cert["strict_full_no_knob_closure"] is False, "certificate strict closure overclosed")

    print("CONST-EW-02 B24 u_dyn source derivation import audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
