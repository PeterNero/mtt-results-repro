"""Audit CONST-EW-02 B23 cross-use universal parameter admissibility."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b23_cross_use_universal_parameter_admissibility"
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
    theorem = load(BASE / "cross_use_admissibility_theorem.packet.json")
    protocol = load(BASE / "fit_once_predict_elsewhere_protocol.packet.json")
    ledger = load(BASE / "u_dyn_u_phys_cross_use_ledger.packet.json")
    boundary = load(BASE / "weak_mixing_b23_boundary.packet.json")
    next_work = load(BASE / "next_labeled_workorder.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("theorem", theorem),
        ("protocol", protocol),
        ("ledger", ledger),
        ("boundary", boundary),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed closure")

    require(candidate["theorem"]["proved"] is True, "B23 theorem did not prove")
    require(candidate["cross_use_tier_formalized"] is True, "cross-use tier not formalized")
    require(candidate["fit_once_predict_elsewhere_protocol_built"] is True, "protocol not built")
    require(candidate["strict_no_knob_closed"] is False, "strict no-knob overclosed")
    require(candidate["universal_parameter_closure_claimed"] is False, "universal closure overclaimed")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")

    tiers = theorem["tier_definitions"]
    require(tiers["strict_no_knob"]["may_use_observed_constant_to_set_parameter"] is False, "strict tier allows observed calibration")
    require(tiers["cross_use_universal_parameter"]["may_use_one_independent_measurement_to_set_parameter"] is True, "cross-use tier too strict")
    require(tiers["cross_use_universal_parameter"]["minimum_independent_uses"] == 2, "minimum cross-use count wrong")
    require(tiers["bad_fitting"]["allowed"] is False, "bad fitting allowed")
    require("at most one independent empirical calibration per parameter" in theorem["admissibility_conditions"], "single calibration condition missing")
    require("all other sectors receive the identical value unchanged" in theorem["admissibility_conditions"], "unchanged reuse condition missing")
    require("drop failed cross-use sectors after seeing results" in theorem["forbidden_shortcuts"], "cherry-pick failure shortcut not forbidden")

    modes = protocol["calibration_modes"]
    require(modes["source_derived"]["strict_no_knob_possible"] is True, "source-derived tier cannot no-knob")
    require(modes["single_empirical_calibration"]["strict_no_knob_possible"] is False, "single calibration mislabeled no-knob")
    require(modes["multi_target_fit"]["claim_allowed"] == "diagnostic only; not closure", "multi-target fit overallowed")
    require(modes["per_observable_retune"]["allowed"] is False, "per-observable retune allowed")
    require("single_value_hash_or_exact_expression" in protocol["audit_fields_required_for_each_parameter"], "single value audit field missing")

    require(ledger["global_policy"]["maximum_live_universal_parameters"] == 3, "global max parameter policy changed")
    require(ledger["global_policy"]["selected_parameter_count_now"] == 0, "global selected count changed")
    require(ledger["global_policy"]["current_B23_live_provisional_parameters"] == 2, "B23 provisional count wrong")
    require(ledger["global_policy"]["strict_no_knob_selected_parameter_count"] == 0, "strict selected count wrong")
    require(set(ledger["parameters"].keys()) == {"u_dyn", "u_phys"}, "wrong ledger parameters")
    require(ledger["parameters"]["u_dyn"]["may_be_calibrated_once"] is True, "u_dyn cannot calibrate once")
    require(ledger["parameters"]["u_dyn"]["cannot_claim_no_knob"] is True, "u_dyn no-knob allowed")
    require("weak mixing no-threshold profile y" in ledger["parameters"]["u_dyn"]["candidate_cross_uses"], "u_dyn weak use missing")
    require("alpha_phys physical normalization" in ledger["parameters"]["u_phys"]["candidate_cross_uses"], "u_phys alpha use missing")
    require(ledger["parameters"]["u_phys"]["cannot_claim_no_knob"] is True, "u_phys no-knob allowed")

    require(boundary["closed_now"]["cross_use_universal_parameter_tier_formalized"] is True, "boundary cross-use not closed")
    require(boundary["closed_now"]["superset_strategy_allows_shared_parameter_cross_use"] is True, "superset cross-use not allowed")
    require(boundary["closed_now"]["bad_per_observable_retuning_forbidden"] is True, "retuning not forbidden")
    require(boundary["still_open"]["u_dyn_source_derivation_or_single_calibration"] is True, "u_dyn not left open")
    require(boundary["still_open"]["u_phys_source_derivation_or_single_calibration"] is True, "u_phys not left open")
    require(boundary["still_open"]["strict_no_knob_closure"] is True, "strict no-knob not left open")
    require(boundary["allowed_next_claim_if_calibrated_once"] == "universal-parameter conditional prediction tier", "wrong calibrated claim")
    require(boundary["forbidden_next_claim_if_calibrated_once"] == "strict no-knob closure", "wrong forbidden claim")

    require(next_work["active_label"] == "CONST-EW-02 / WEAK-MIXING / B24-CROSS-USE-TEST-OR-SOURCE-DERIVATION", "wrong B24 label")
    require("U-DYN-SOURCE-DERIVATION" in next_work["primary"]["label"], "primary B24 route wrong")
    require("FIT-ONCE-PREDICT-ELSEWHERE" in next_work["bridge"]["label"], "bridge B24 route wrong")

    require(cert["cross_use_tier_formalized"] is True, "certificate cross-use missing")
    require(cert["single_empirical_calibration_allowed"] is True, "certificate calibration too strict")
    require(cert["per_observable_retuning_allowed"] is False, "certificate retuning allowed")
    require(cert["minimum_independent_uses"] == 2, "certificate minimum uses wrong")
    require(cert["strict_no_knob_closed"] is False, "certificate strict no-knob overclosed")
    require(cert["universal_parameter_closure_claimed"] is False, "certificate universal closure overclaimed")

    print("CONST-EW-02 B23 cross-use universal parameter admissibility audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
