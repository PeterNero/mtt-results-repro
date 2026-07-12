"""Audit CONST-EW-02 B21 dynamic C1 / free-parameter bridge."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "const_ew_02_weak_mixing_b21_dynamic_c1_or_free_parameter_bridge"
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
    dynamic = load(BASE / "dynamic_c1_frontier_import.packet.json")
    params = load(BASE / "provisional_universal_parameter_bridge.packet.json")
    boundary = load(BASE / "weak_mixing_b21_boundary.packet.json")
    next_work = load(BASE / "next_labeled_workorder.packet.json")
    cert = load(CERT)

    for name, packet in [
        ("candidate", candidate),
        ("dynamic", dynamic),
        ("params", params),
        ("boundary", boundary),
        ("cert", cert),
    ]:
        require(packet["observed_data_used_as_selector"] is False, f"{name} used observed selector")
        require(packet["target_fitting_used"] is False, f"{name} used target fitting")
        require(packet["closure_claimed"] is False, f"{name} claimed closure")

    require(candidate["theorem"]["proved"] is True, "B21 theorem did not prove")
    require(candidate["conditional_dynamic_C1_exact"] is True, "conditional dynamic C1 not exact")
    require(candidate["dynamic_C1_selected_source_promoted"] is False, "selected dynamic C1 overpromoted")
    require(candidate["provisional_few_parameter_lane_available"] is True, "parameter lane missing")
    require(candidate["provisional_few_parameter_lane_not_no_knob"] is True, "parameter lane mislabeled")
    require(candidate["strict_xL_emitted_now"] is False, "xL overemitted")
    require(candidate["physical_weak_angle_closure"] is False, "weak angle overclosed")

    values = dynamic["conditional_values"]
    require(values["A_transpose_A"] == [[12, 0], [0, 12]], "A^T A mismatch")
    require(values["A_transpose_b"] == [12, 12], "A^T b mismatch")
    require(values["b_norm_square"] == 24, "b norm mismatch")
    require(values["condition_number"] == 1, "condition number mismatch")
    require(values["deltaTheta_conditional"] == [1, 1], "conditional deltaTheta mismatch")
    require(values["residual"] == 0, "conditional residual nonzero")

    require(dynamic["what_closes_conditionally"]["linear_algebra_obstruction_removed"] is True, "linear algebra obstruction not removed")
    require(dynamic["what_closes_conditionally"]["selected_source_promotion_gate_ready"] is True, "source promotion gate not ready")
    require(dynamic["not_promoted"]["dynamic_kernel_emitted"] is False, "dynamic kernel overemitted")
    require(dynamic["not_promoted"]["selected_C1_primitive_emitted"] is False, "primitive C1 overemitted")
    require(dynamic["not_promoted"]["selected_A_selected_claimed"] is False, "A_selected overclaimed")
    require(dynamic["not_promoted"]["selected_b_selected_claimed"] is False, "b_selected overclaimed")
    require(dynamic["not_promoted"]["selected_D_E_source_promotion"] is True, "D_E source not left open")
    require(dynamic["not_promoted"]["selected_dotD_source_verified"] is True, "dotD source not left open")

    require(params["credibility_policy"]["strict_no_knob_lane_remains_primary"] is True, "strict lane not primary")
    require(params["credibility_policy"]["few_parameter_lane_is_a_bridge_not_final"] is True, "parameter lane treated as final")
    require(params["credibility_policy"]["parameters_must_be_global_not_sector_tuned"] is True, "parameter lane allows sector tuning")
    require(params["credibility_policy"]["parameters_must_feed_multiple_constants_or_be_retired"] is True, "parameter lane lacks retirement rule")
    require([p["name"] for p in params["allowed_parameters"]] == ["u_dyn", "u_phys"], "wrong provisional parameter names")
    require("fitting observed alpha(0), alpha(M_Z), masses, CKM, or PMNS" in params["forbidden_uses"], "observed fitting not forbidden")
    require("claiming no-knob or physical weak-angle closure before source derivation" in params["forbidden_uses"], "no-knob overclaim not forbidden")

    require(boundary["closed_now"]["conditional_dynamic_C1_Gram_exact"] is True, "boundary dynamic Gram not closed")
    require(boundary["closed_now"]["provisional_few_parameter_lane_formalized"] is True, "boundary parameter lane not formalized")
    require(boundary["still_open"]["selected_same_source_dynamic_transfer_identity"] is True, "same-source dynamic identity not open")
    require(boundary["still_open"]["honest_Galerkin_C1_contractions"] is True, "honest Galerkin not open")
    require(boundary["still_open"]["selected_A_selected"] is True, "A_selected not open")
    require(boundary["still_open"]["selected_b_selected"] is True, "b_selected not open")
    require(boundary["still_open"]["strict_no_knob_closure"] is True, "strict no-knob not open")
    require(boundary["provisional_lane"]["not_no_knob"] is True, "boundary parameter lane mislabeled")
    require(boundary["provisional_lane"]["maximum_recommended_parameters_before_source_derivation"] == 2, "parameter cap changed")

    require(next_work["active_label"] == "CONST-EW-02 / WEAK-MIXING / B22-SOURCE-PROMOTION-OR-PARAMETERIZED-BRIDGE-REPLAY", "wrong B22 label")
    require("SAME-SOURCE-DYNAMIC-TRANSFER" in next_work["primary"]["label"], "primary B22 route wrong")
    require("PROVISIONAL-U-DYN-U-PHYS" in next_work["bridge"]["label"], "bridge B22 route wrong")

    require(cert["conditional_dynamic_C1_exact"] is True, "certificate conditional dynamic C1 missing")
    require(cert["dynamic_C1_selected_source_promoted"] is False, "certificate selected dynamic C1 overpromoted")
    require(cert["provisional_few_parameter_lane_not_no_knob"] is True, "certificate parameter lane mislabeled")

    print("CONST-EW-02 B21 dynamic C1 / free-parameter bridge audit: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
