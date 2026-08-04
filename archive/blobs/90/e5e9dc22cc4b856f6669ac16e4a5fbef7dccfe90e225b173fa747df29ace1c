"""Audit HRG source-rule / QaSU3 retarded-matching frontier packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hrguniversalprimitivesourcerule_or_qasu3retardedmatchingmap"
BASE = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HRGUniversalPrimitiveSourceRule_or_QaSU3RetardedMatchingMap_v1.md"
BUILD = ROOT / "scripts" / f"build_{SLUG}.py"

NOVELTY = BASE / "frontier_novelty_scan.packet.json"
HRG_RULE = BASE / "hrg_universal_primitive_source_rule_attempt.packet.json"
QA_MATCHING = BASE / "qasu3_retarded_matching_map_attempt.packet.json"
B39_CHAIN = BASE / "b39_local_kernel_crossuse_bridge.packet.json"
B45_PORTFOLIO = BASE / "b45_portfolio_frontier_import.packet.json"
CUTSET = BASE / "next_cutset_after_hrg_source_rule_attempt.packet.json"

STATUS = (
    "MTT_SELECTED_HRGUNIVERSALPRIMITIVESOURCERULE_OR_QASU3RETARDEDMATCHINGMAP_"
    "B45_IMPORTED_ONE_PRIMITIVE_HANDOFF_HRG_NOT_PROMOTED"
)
NEXT = "MTT_Selected_B45PortfolioPrimitiveComparison_or_CONSTGR01SharedPrimitiveSourceTest_v1"
HRG = 391.39140285811936
SIN2 = 0.2315309482915084
LAMBDA_12 = 2.6179362173268497


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    cert = load(CERT)
    novelty = load(NOVELTY)
    hrg_rule = load(HRG_RULE)
    qa_matching = load(QA_MATCHING)
    b39_chain = load(B39_CHAIN)
    b45 = load(B45_PORTFOLIO)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(candidate["closure_claimed"] is True, "candidate closure")
    require(candidate["true_SM_equivalence_claimed"] is False, "true SM overclaim")
    require(candidate["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector")
    require(candidate["target_fitting_used"] is False, "target fitting")
    require(candidate["theorem"]["proved"] is True, "theorem proved")
    require(
        candidate["theorem"]["name"] == "HRGUniversalPrimitiveSourceRuleOrQaSU3RetardedMatchingMapTheorem",
        "theorem name",
    )

    decision = candidate["closure_decision"]
    for key in [
        "anti_loop_latest_frontier_scan_completed",
        "B39_not_latest_frontier",
        "B45_latest_adjacent_frontier_imported",
        "B45_weak_mixing_one_shared_primitive_tier",
        "B44_conditional_profile_replay_available",
        "B45_recommend_cross_constant_next",
        "next_nonlooping_target_identified",
    ]:
        require(decision[key] is True, f"decision true {key}")
    for key in [
        "B45_selected_numeric_primitive_value_available",
        "B45_physical_weak_angle_closed",
        "B45_strict_full_no_knob_closed",
        "HRG_numeric_source_rule_derived",
        "QaSU3_same_HRG_retarded_matching_map_accepted",
        "B45_same_HRG_crossuse_prediction_now",
        "UP_RET_OVERLAP_HRG_universal_admitted",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"decision false {key}")

    nums = candidate["key_numbers"]
    require(abs(nums["UP_RET_OVERLAP_HRG"] - HRG) < 1e-12, "HRG value")
    require(nums["QaSU3_chi_Qa"] == 1.0, "Qa chi")
    require(nums["B40_u_dyn"] == 1.0, "B40 u_dyn")
    require(abs(nums["B40_internal_lambda_12"] - LAMBDA_12) < 1e-12, "B40 lambda12")
    require(abs(nums["B44_conditional_minimal_threshold_sin2"] - SIN2) < 1e-15, "B44 sin2")
    require(nums["B45_current_shared_physical_primitives_needed_for_alpha_and_weak_mixing"] == 1, "B45 primitive count")
    require(nums["B45_selected_numeric_primitive_values_now"] == 0, "B45 selected primitive values")
    require(nums["HRG_source_rule_candidate_count"] == 5, "HRG lane count")
    require(nums["accepted_HRG_source_rule_count"] == 0, "accepted HRG rules")
    require(nums["tested_same_HRG_matching_map_count"] == 3, "matching map count")
    require(nums["accepted_same_HRG_matching_map_count"] == 0, "accepted matching maps")

    require(cert["status"] == STATUS, "cert status")
    require(cert["next_required_artifact"] == NEXT, "cert next")
    require(cert["anti_loop_latest_frontier_scan_completed"] is True, "cert anti-loop")
    require(cert["B39_not_latest_frontier"] is True, "cert B39 not latest")
    require(cert["B45_latest_adjacent_frontier_imported"] is True, "cert B45")
    require(cert["B45_weak_mixing_one_shared_primitive_tier"] is True, "cert one primitive")
    require(cert["B44_conditional_profile_replay_available"] is True, "cert replay")
    require(cert["B45_selected_numeric_primitive_value_available"] is False, "cert primitive value")
    require(cert["B45_physical_weak_angle_closed"] is False, "cert weak angle")
    require(cert["B45_strict_full_no_knob_closed"] is False, "cert no knob")
    require(cert["HRG_numeric_source_rule_derived"] is False, "cert HRG source")
    require(cert["QaSU3_same_HRG_retarded_matching_map_accepted"] is False, "cert matching")
    require(cert["accepted_HRG_source_rule_count"] == 0, "cert HRG accepted")
    require(cert["accepted_same_HRG_matching_map_count"] == 0, "cert matching accepted")
    require(cert["UP_RET_OVERLAP_HRG_universal_admitted"] is False, "cert universal")
    require(cert["true_SM_equivalence_claimed"] is False, "cert true SM")
    require(cert["full_no_knob_closure_claimed"] is False, "cert no knob claim")
    require(cert["observed_data_used_as_selector"] is False, "cert observed")
    require(cert["target_fitting_used"] is False, "cert fitting")

    require(novelty["status"] == "FRONTIER_NOVELTY_SCAN_B45_LATEST_IMPORTED_B39_NOT_LATEST", "novelty")
    require(novelty["closure_claimed"] is True, "novelty closure")
    require(novelty["observed_data_used_as_selector"] is False, "novelty observed")
    require(novelty["target_fitting_used"] is False, "novelty target")
    prior_statuses = [row["status"] for row in novelty["prior_hits_classified"]]
    require(any("B39" in status for status in prior_statuses), "B39 hit")
    require(any("B45" in status for status in prior_statuses), "B45 hit")
    for row in novelty["prior_hits_classified"]:
        require(row["already_closes_this_target"] is False, f"already closes {row['artifact']}")
    latest = novelty["latest_adjacent_frontier"]
    require("B45-UNIVERSAL-PRIMITIVE-PORTFOLIO-HANDOFF" in latest["active_label"], "latest B45 label")
    require(latest["weak_mixing_down_to_one_shared_primitive_tier"] is True, "latest one primitive")
    require(latest["conditional_profile_replay_available"] is True, "latest replay")
    require(latest["selected_numeric_primitive_values_now"] == 0, "latest primitive value")
    require(latest["recommend_cross_constant_next"] is True, "latest cross constant")
    require(latest["selected_next_constant"] == "CONST-GR-01 / ABSOLUTE-SCALE-GN", "latest next constant")
    require(latest["physical_weak_angle_closure"] is False, "latest physical")
    require(latest["strict_full_no_knob_closure"] is False, "latest no knob")
    for phrase in [
        "B39 is now a chain link",
        "B45 changes the problem",
        "one-primitive portfolio result",
    ]:
        require(any(phrase in item for item in novelty["why_not_loop"]), f"novelty phrase {phrase}")

    require(hrg_rule["status"] == "HRG_UNIVERSAL_PRIMITIVE_SOURCE_RULE_ATTEMPTED_ZERO_ACCEPTED_B45_SUPPORT_ONLY", "HRG status")
    require(hrg_rule["candidate_lane_count"] == 5, "HRG candidates")
    require(hrg_rule["accepted_source_rule_count"] == 0, "HRG accepted")
    require(hrg_rule["primitive"]["id"] == "UP-RET-OVERLAP.HRG", "primitive id")
    require(abs(hrg_rule["primitive"]["value"] - HRG) < 1e-12, "primitive value")
    require(hrg_rule["primitive"]["currently_empirical_H_calibration"] is True, "primitive empirical")
    lanes = {row["lane"]: row for row in hrg_rule["lanes"]}
    for lane in [
        "strict_HRG_determinant_index_RG_transport",
        "QaSU3_electroweak_matching_interface",
        "constants_B39_local_principle_source_kernel",
        "constants_B45_one_primitive_portfolio_handoff",
        "fit_once_HRG_as_universal_crossuse_parameter",
    ]:
        require(lane in lanes, f"missing lane {lane}")
        require(lanes[lane]["accepted_as_HRG_source_rule"] is False, f"accepted lane {lane}")
        require(lanes[lane]["source_selected"] is False, f"source lane {lane}")
    hrg_decision = hrg_rule["decision"]
    require(hrg_decision["HRG_remains_empirical_H_calibration"] is True, "HRG empirical")
    for key in [
        "HRG_numeric_source_rule_derived",
        "strict_R_H_RG_source_emitted",
        "B39_local_kernel_promotes_HRG",
        "B45_one_primitive_tier_promotes_HRG",
        "QaSU3_matching_promotes_HRG",
        "UP_RET_OVERLAP_HRG_universal_admitted",
    ]:
        require(hrg_decision[key] is False, f"HRG decision false {key}")

    require(qa_matching["status"] == "QASU3_RETARDED_MATCHING_MAP_ATTEMPTED_B45_IMPORTED_ZERO_SAME_HRG_MAPS", "Qa status")
    require(qa_matching["QaSU3_retarded_response_available"] is True, "Qa response")
    require(qa_matching["QaSU3_electroweak_interface_available"] is True, "Qa interface")
    require(qa_matching["B44_conditional_profile_available"] is True, "B44 available")
    require(qa_matching["B45_one_primitive_tier_available"] is True, "B45 available")
    require(qa_matching["tested_matching_map_count"] == 3, "Qa tested")
    require(qa_matching["accepted_same_HRG_matching_map_count"] == 0, "Qa accepted")
    qa_decision = qa_matching["decision"]
    require(qa_decision["B45_is_new_portfolio_support"] is True, "B45 support")
    for key in [
        "typed_same_HRG_QaSU3_electroweak_matching_map",
        "accepted_RO_nonHiggs_sector_map",
        "nonHiggs_prediction_emitted_without_retuning",
        "B44_conditional_profile_is_HRG_prediction_now",
        "B45_is_HRG_crossuse_prediction_now",
    ]:
        require(qa_decision[key] is False, f"Qa decision false {key}")
    for row in qa_matching["rows"]:
        require(row["accepted_as_same_HRG_matching_map"] is False, f"same HRG map {row['map']}")
        require(row["accepted_as_nonHiggs_prediction"] is False, f"prediction {row['map']}")

    require(b39_chain["status"] == "B39_IMPORTED_AS_CHAIN_LINK_SUPERSEDED_BY_B45", "B39 chain")
    require(b39_chain["decision"]["B39_is_latest_frontier"] is False, "B39 latest")
    require(b39_chain["decision"]["B39_remains_valid_support"] is True, "B39 support")
    require(b39_chain["decision"]["use_B45_as_latest_frontier"] is True, "B45 latest")
    require(b39_chain["decision"]["treat_B39_as_HRG_numeric_source"] is False, "B39 HRG")

    require(b45["status"] == "B45_PORTFOLIO_FRONTIER_IMPORTED_ONE_PRIMITIVE_TIER_HRG_NOT_PROMOTED", "B45 import")
    chain = b45["chain_support"]
    require(chain["B40_local_kernel_to_profile"]["u_dyn_source_derived"] is True, "B40 source")
    require(chain["B40_local_kernel_to_profile"]["u_dyn_value"] == 1.0, "B40 u")
    require(abs(chain["B40_local_kernel_to_profile"]["internal_lambda_12_value"] - LAMBDA_12) < 1e-12, "B40 lambda")
    require(chain["B41_physical_gate"]["one_universal_primitive_extension_ready"] is True, "B41 primitive ready")
    require(chain["B41_physical_gate"]["K_phys_or_f_ab_closed"] is False, "B41 K closed")
    require(chain["B42_one_primitive_bridge"]["contract_closed"] is True, "B42 contract")
    require(chain["B42_one_primitive_bridge"]["value_selected"] is False, "B42 value")
    require(chain["B44_conditional_profile"]["conditional_profile_execution_closed"] is True, "B44 profile")
    require(abs(chain["B44_conditional_profile"]["conditional_minimal_threshold_sin2"] - SIN2) < 1e-15, "B44 sin2")
    require(chain["B44_conditional_profile"]["assumption_lock"]["one_primitive_tier"]["value_selected"] is False, "B44 primitive value")
    require(chain["B45_portfolio"]["weak_mixing_down_to_one_shared_primitive_tier"] is True, "B45 one primitive")
    require(chain["B45_portfolio"]["recommend_cross_constant_next"] is True, "B45 cross")
    require(chain["B45_portfolio"]["selected_next_constant"] == "CONST-GR-01 / ABSOLUTE-SCALE-GN", "B45 next constant")
    require(chain["B45_portfolio"]["global_budget"]["selected_numeric_primitive_values_now"] == 0, "B45 numeric")
    require(chain["B45_portfolio"]["switch_decision"]["weak_mixing_physical_closure_claimed"] is False, "B45 closure")
    b45_decision = b45["decision"]
    for key in [
        "B45_latest_adjacent_frontier_imported",
        "weak_mixing_one_shared_primitive_tier_reached",
        "B44_conditional_profile_replay_available",
        "compare_HRG_to_E0L0_or_CONSTGR01_next",
    ]:
        require(b45_decision[key] is True, f"B45 decision true {key}")
    for key in [
        "selected_numeric_primitive_value_available",
        "B45_treat_as_physical_weak_angle_closure",
        "B45_treat_as_HRG_numeric_source",
    ]:
        require(b45_decision[key] is False, f"B45 decision false {key}")

    require(cutset["status"] == "NEXT_FRONTIER_B45_PORTFOLIO_PRIMITIVE_COMPARISON_OR_CONSTGR01_SHARED_SOURCE_TEST", "cutset status")
    require(cutset["next_required_artifact"] == NEXT, "cutset next")
    for phrase in [
        "anti-loop scan corrected latest constants frontier from B39 to B45",
        "B40-B45 weak-mixing chain imported as real one-primitive portfolio support",
        "B44 conditional profile replay classified as replay-only, not HRG prediction",
        "B45 one-shared-primitive tier classified as symbolic support with zero selected numeric primitive values",
    ]:
        require(phrase in cutset["closed_here"], f"closed missing {phrase}")
    for phrase in [
        "typed identity or separation theorem between E0/L0/modal-gap primitive and UP-RET-OVERLAP.HRG",
        "CONST-GR-01 shared primitive source test recommended by B45",
        "selected numeric primitive value for the B45 one-primitive tier",
        "universal admission of UP-RET-OVERLAP.HRG",
        "true SM/no-knob equivalence",
    ]:
        require(phrase in cutset["still_open"], f"open missing {phrase}")

    for phrase in [
        "B39 remains valid support, but it is not the latest frontier.",
        "current adjacent result",
        "Accepted HRG source rules: `0 / 5`.",
        "Accepted same-HRG Qa/SU3/electroweak/B45 matching maps: `0 / 3`.",
        "sin2_conditional = 0.2315309482915084",
        "selected_numeric_primitive_values_now = 0",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        "AUDIT_PASS: B45 is the latest adjacent weak-mixing frontier; "
        "HRG source rules remain 0/5 and same-HRG maps remain 0/3."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
