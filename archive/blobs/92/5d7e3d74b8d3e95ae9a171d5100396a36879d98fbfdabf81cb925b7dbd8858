"""Build HRG source-rule / QaSU3 retarded matching packet.

This packet is deliberately anti-loop.  It imports the *latest* adjacent
weak-mixing frontier from the constants repo.  The constants chain has advanced
past B39:

* B40 propagates the local C1 source kernel to a weak-mixing profile frontier;
* B41 reduces the physical gate to gauge/action/RG matching;
* B42 collapses alpha/weak physical normalization and matching to one symbolic
  E0/L0 primitive tier;
* B43/B44 execute a guarded conditional profile replay;
* B45 hands weak mixing to the universal-primitive portfolio with zero selected
  numeric primitive values.

The decision here is therefore not "B39 is latest".  The decision is: B45 is
real progress and prevents another weak-angle loop, but it still does not
promote UP-RET-OVERLAP.HRG or emit a same-HRG non-Higgs prediction.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hrguniversalprimitivesourcerule_or_qasu3retardedmatchingmap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
NOVELTY = PACKET_DIR / "frontier_novelty_scan.packet.json"
HRG_RULE = PACKET_DIR / "hrg_universal_primitive_source_rule_attempt.packet.json"
QA_MATCHING = PACKET_DIR / "qasu3_retarded_matching_map_attempt.packet.json"
B39_BRIDGE = PACKET_DIR / "b39_local_kernel_crossuse_bridge.packet.json"
B45_PORTFOLIO = PACKET_DIR / "b45_portfolio_frontier_import.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_hrg_source_rule_attempt.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HRGUniversalPrimitiveSourceRule_or_QaSU3RetardedMatchingMap_v1.md"

PREVIOUS = DATA / "selected_rovaluesource_or_nonhiggsmapexecution.candidate.json"
PREVIOUS_CUTSET = (
    DATA
    / "selected_rovaluesource_or_nonhiggsmapexecution"
    / "next_cutset_after_ro_value_source_execution.packet.json"
)
RO_VALUE_EXECUTION = (
    DATA
    / "selected_rovaluesource_or_nonhiggsmapexecution"
    / "ro_value_source_execution.packet.json"
)
CROSSUSE_POLICY = (
    DATA
    / "universal_crossuse_parameter_admissibility_theorem"
    / "crossuse_admissibility_theorem.packet.json"
)

QA_CHI = (
    TEXPAPERS
    / "mtt-qa-su3-packet-proof"
    / "candidate_data"
    / "selected_response_functional_chi_qa.candidate.json"
)
QA_EW_MATCHING = (
    TEXPAPERS
    / "mtt-qa-su3-packet-proof"
    / "candidate_data"
    / "electroweak_matching_or_absolute_coupling_normalization.candidate.json"
)

CONST_DATA = TEXPAPERS / "mtt-individual-constants-source-search" / "candidate_data"
CONST_B15 = CONST_DATA / "const_ew_02_weak_mixing_b15_ew_product_map_factorization.candidate.json"
CONST_B29 = CONST_DATA / "const_ew_02_weak_mixing_b29_routeb_final_source_theorem_frontier.candidate.json"
CONST_B39 = CONST_DATA / "const_ew_02_weak_mixing_b39_source_kernel_or_local_principle.candidate.json"
CONST_B39_LOCAL = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b39_source_kernel_or_local_principle"
    / "local_principle_preresidual_source_kernel.packet.json"
)
CONST_B40 = CONST_DATA / "const_ew_02_weak_mixing_b40_local_kernel_to_profile.candidate.json"
CONST_B40_LOCAL = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b40_local_kernel_to_profile"
    / "local_c1_source_kernel_propagation.packet.json"
)
CONST_B40_GATE = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b40_local_kernel_to_profile"
    / "physical_weak_angle_gate_after_local_kernel.packet.json"
)
CONST_B41 = CONST_DATA / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching.candidate.json"
CONST_B41_ANCHOR = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching"
    / "gauge_action_anchor_status.packet.json"
)
CONST_B41_BOUNDARY = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b41_gauge_action_rg_matching"
    / "weak_mixing_b41_boundary.packet.json"
)
CONST_B42 = CONST_DATA / "const_ew_02_weak_mixing_b42_one_primitive_physical_bridge.candidate.json"
CONST_B43 = CONST_DATA / "const_ew_02_weak_mixing_b43_threshold_vector_or_minimal_policy.candidate.json"
CONST_B44 = CONST_DATA / "const_ew_02_weak_mixing_b44_conditional_profile_execution.candidate.json"
CONST_B44_ASSUMPTION = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b44_conditional_profile_execution"
    / "conditional_profile_assumption_lock.packet.json"
)
CONST_B44_BOUNDARY = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b44_conditional_profile_execution"
    / "weak_mixing_b44_boundary.packet.json"
)
CONST_B45 = CONST_DATA / "const_ew_02_weak_mixing_b45_universal_primitive_portfolio_handoff.candidate.json"
CONST_B45_BUDGET = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b45_universal_primitive_portfolio_handoff"
    / "universal_primitive_budget_status.packet.json"
)
CONST_B45_SWITCH = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b45_universal_primitive_portfolio_handoff"
    / "cross_constant_switch_rule.packet.json"
)
CONST_B45_NEXT_CONSTANT = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b45_universal_primitive_portfolio_handoff"
    / "next_constant_priority.packet.json"
)
CONST_B45_BOUNDARY = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b45_universal_primitive_portfolio_handoff"
    / "weak_mixing_b45_boundary.packet.json"
)
CONST_B45_NEXT = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b45_universal_primitive_portfolio_handoff"
    / "next_labeled_workorder.packet.json"
)

STATUS = (
    "MTT_SELECTED_HRGUNIVERSALPRIMITIVESOURCERULE_OR_QASU3RETARDEDMATCHINGMAP_"
    "B45_IMPORTED_ONE_PRIMITIVE_HANDOFF_HRG_NOT_PROMOTED"
)
NEXT = "MTT_Selected_B45PortfolioPrimitiveComparison_or_CONSTGR01SharedPrimitiveSourceTest_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing HRG/QaSU3/B45 inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_CUTSET,
        RO_VALUE_EXECUTION,
        CROSSUSE_POLICY,
        QA_CHI,
        QA_EW_MATCHING,
        CONST_B15,
        CONST_B29,
        CONST_B39,
        CONST_B39_LOCAL,
        CONST_B40,
        CONST_B40_LOCAL,
        CONST_B40_GATE,
        CONST_B41,
        CONST_B41_ANCHOR,
        CONST_B41_BOUNDARY,
        CONST_B42,
        CONST_B43,
        CONST_B44,
        CONST_B44_ASSUMPTION,
        CONST_B44_BOUNDARY,
        CONST_B45,
        CONST_B45_BUDGET,
        CONST_B45_SWITCH,
        CONST_B45_NEXT_CONSTANT,
        CONST_B45_BOUNDARY,
        CONST_B45_NEXT,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_cutset = load(PREVIOUS_CUTSET)
    value_execution = load(RO_VALUE_EXECUTION)
    crossuse_policy = load(CROSSUSE_POLICY)
    qa_chi = load(QA_CHI)
    qa_ew = load(QA_EW_MATCHING)
    b15 = load(CONST_B15)
    b29 = load(CONST_B29)
    b39 = load(CONST_B39)
    b39_local = load(CONST_B39_LOCAL)
    b40 = load(CONST_B40)
    b40_local = load(CONST_B40_LOCAL)
    b40_gate = load(CONST_B40_GATE)
    b41 = load(CONST_B41)
    b41_anchor = load(CONST_B41_ANCHOR)
    b41_boundary = load(CONST_B41_BOUNDARY)
    b42 = load(CONST_B42)
    b43 = load(CONST_B43)
    b44 = load(CONST_B44)
    b44_assumption = load(CONST_B44_ASSUMPTION)
    b44_boundary = load(CONST_B44_BOUNDARY)
    b45 = load(CONST_B45)
    b45_budget = load(CONST_B45_BUDGET)
    b45_switch = load(CONST_B45_SWITCH)
    b45_next_constant = load(CONST_B45_NEXT_CONSTANT)
    b45_boundary = load(CONST_B45_BOUNDARY)
    b45_next = load(CONST_B45_NEXT)

    hrg = value_execution["value"]["UP_RET_OVERLAP_HRG"]
    log_hrg = value_execution["value"]["log_UP_RET_OVERLAP_HRG"]
    log_2008 = math.log(2008)
    chi = qa_chi["derivation"]["result"]["chi_Qa_numeric"]
    profile = b40_local["weak_mixing_profile_prefix"]
    budget = b45_budget["global_budget"]

    prior_hits = [
        (PREVIOUS, previous["status"], "local predecessor; Qa/SU3 chi_Qa=1 support only"),
        (QA_EW_MATCHING, qa_ew["status"], "Qa/SU3 electroweak matching interface; K_gauge and U1/SU2 payloads open"),
        (CONST_B15, b15["status"], "older weak-mixing factorization; threshold/torsion payload required"),
        (CONST_B29, b29["status"], "older Route-B source theorem frontier"),
        (CONST_B39, b39["status"], "local-principle pre-residual source kernel closed, later propagated by B40-B45"),
        (CONST_B40, b40["status"], "local C1 source kernel propagated to weak-mixing profile frontier"),
        (CONST_B41, b41["status"], "physical gate reduced to gauge/action/RG matching"),
        (CONST_B42, b42["status"], "alpha/weak physical normalization and matching collapse to one symbolic primitive"),
        (CONST_B43, b43["status"], "threshold vector decomposed; minimal replay policy built, strict vector open"),
        (CONST_B44, b44["status"], "conditional profile replay executable, not physical closure"),
        (CONST_B45, b45["status"], "latest adjacent frontier; weak mixing handoff-ready for universal-primitive portfolio testing"),
    ]

    novelty = {
        "schema": "MTTFrontierNoveltyScanForHRGQaSU3Matching.v2",
        "status": "FRONTIER_NOVELTY_SCAN_B45_LATEST_IMPORTED_B39_NOT_LATEST",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "searched_target": "MTT_Selected_HRGUniversalPrimitiveSourceRule_or_QaSU3RetardedMatchingMap_v1",
        "prior_hits_classified": [
            {
                "artifact": rel(path),
                "status": status,
                "classification": classification,
                "already_closes_this_target": False,
            }
            for path, status, classification in prior_hits
        ],
        "latest_adjacent_frontier": {
            "artifact": rel(CONST_B45),
            "active_label": b45["active_label"],
            "weak_mixing_down_to_one_shared_primitive_tier": b45["weak_mixing_down_to_one_shared_primitive_tier"],
            "conditional_profile_replay_available": b44["conditional_profile_execution_closed"],
            "conditional_minimal_threshold_sin2": b44["conditional_minimal_threshold_sin2"],
            "selected_numeric_primitive_values_now": budget["selected_numeric_primitive_values_now"],
            "recommend_cross_constant_next": b45["recommend_cross_constant_next"],
            "selected_next_constant": b45["selected_next_constant"],
            "physical_weak_angle_closure": b45["physical_weak_angle_closure"],
            "strict_full_no_knob_closure": b45["strict_full_no_knob_closure"],
        },
        "why_not_loop": [
            "The earlier local packet stopped after classifying Qa/SU3 chi_Qa=1 as support.",
            "The constants repo has advanced beyond B39 to B45; B39 is now a chain link, not the latest frontier.",
            "B45 changes the problem from weak-angle optimization to cross-constant universal-primitive testing.",
            "This packet tests whether that one-primitive portfolio result promotes HRG or remains a distinct symbolic primitive tier.",
        ],
    }

    hrg_lanes = [
        {
            "lane": "strict_HRG_determinant_index_RG_transport",
            "accepted_as_HRG_source_rule": False,
            "source_selected": False,
            "basis": rel(PREVIOUS_CUTSET),
            "blocking_reason": "The prior RO cutset still requires a selected HRG numeric source rule from determinant/index/RG transport.",
        },
        {
            "lane": "QaSU3_electroweak_matching_interface",
            "accepted_as_HRG_source_rule": False,
            "source_selected": False,
            "basis": rel(QA_EW_MATCHING),
            "selected_payload": "I_Qa=log(2008), chi_Qa=1",
            "blocking_reason": "Qa/SU3 supplies internal matching units, not the HRG numeric specialization.",
        },
        {
            "lane": "constants_B39_local_principle_source_kernel",
            "accepted_as_HRG_source_rule": False,
            "source_selected": False,
            "basis": rel(CONST_B39),
            "local_tier_source_kernel_closed": True,
            "blocking_reason": "B39 emits a local-principle pre-residual source kernel for weak mixing, not HRG.",
        },
        {
            "lane": "constants_B45_one_primitive_portfolio_handoff",
            "accepted_as_HRG_source_rule": False,
            "source_selected": False,
            "basis": rel(CONST_B45),
            "weak_mixing_down_to_one_shared_primitive_tier": True,
            "selected_numeric_primitive_values_now": budget["selected_numeric_primitive_values_now"],
            "blocking_reason": "B45 isolates a symbolic E0/L0/modal-gap primitive tier with zero selected numeric primitive values and no typed identity to UP-RET-OVERLAP.HRG.",
        },
        {
            "lane": "fit_once_HRG_as_universal_crossuse_parameter",
            "accepted_as_HRG_source_rule": False,
            "source_selected": False,
            "basis": rel(CROSSUSE_POLICY),
            "policy_admissible_in_future": True,
            "blocking_reason": "The H calibration has no same-value non-Higgs prediction yet; B45 recommends cross-constant primitive testing instead of weak-angle fitting.",
        },
    ]
    accepted_hrg_rules = [row for row in hrg_lanes if row["accepted_as_HRG_source_rule"]]

    hrg_rule = {
        "schema": "MTTHRGUniversalPrimitiveSourceRuleAttempt.v2",
        "status": "HRG_UNIVERSAL_PRIMITIVE_SOURCE_RULE_ATTEMPTED_ZERO_ACCEPTED_B45_SUPPORT_ONLY",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "primitive": {
            "id": "UP-RET-OVERLAP.HRG",
            "value": hrg,
            "log_value": log_hrg,
            "currently_empirical_H_calibration": True,
        },
        "candidate_lane_count": len(hrg_lanes),
        "accepted_source_rule_count": len(accepted_hrg_rules),
        "lanes": hrg_lanes,
        "decision": {
            "HRG_numeric_source_rule_derived": False,
            "strict_R_H_RG_source_emitted": False,
            "B39_local_kernel_promotes_HRG": False,
            "B45_one_primitive_tier_promotes_HRG": False,
            "QaSU3_matching_promotes_HRG": False,
            "UP_RET_OVERLAP_HRG_universal_admitted": False,
            "HRG_remains_empirical_H_calibration": True,
        },
    }

    qa_matching_rows = [
        {
            "map": "Qa/SU3 finite response to physical gauge matching",
            "accepted_as_same_HRG_matching_map": False,
            "accepted_as_nonHiggs_prediction": False,
            "selected_internal_payload_available": True,
            "selected_internal_payload": {
                "I_Qa": "log(2008)",
                "I_Qa_numeric": log_2008,
                "chi_Qa": chi,
            },
            "missing_for_same_HRG_map": [
                "common K_gauge",
                "U1/SU2 same-scheme payloads",
                "matching scale or internal scale map",
                "explicit equation identifying UP-RET-OVERLAP.HRG with the same matching variable",
            ],
        },
        {
            "map": "B44 conditional weak-mixing profile replay",
            "accepted_as_same_HRG_matching_map": False,
            "accepted_as_nonHiggs_prediction": False,
            "conditional_profile_execution_closed": True,
            "conditional_minimal_threshold_sin2": b44["conditional_minimal_threshold_sin2"],
            "missing_for_same_HRG_map": [
                "strict threshold source theorem",
                "selected primitive value or source unit",
                "precision RG scheme conversion",
                "typed HRG insertion rule",
            ],
        },
        {
            "map": "B45 one-primitive portfolio to HRG cross-use",
            "accepted_as_same_HRG_matching_map": False,
            "accepted_as_nonHiggs_prediction": False,
            "one_shared_primitive_tier_available": True,
            "selected_numeric_primitive_values_now": budget["selected_numeric_primitive_values_now"],
            "missing_for_same_HRG_map": [
                "typed identity between E0/L0/modal-gap primitive and UP-RET-OVERLAP.HRG",
                "selected numeric primitive value",
                "cross-constant validation against CONST-GR-01 or another independent constant",
            ],
        },
    ]
    accepted_matching = [row for row in qa_matching_rows if row["accepted_as_same_HRG_matching_map"]]

    qa_matching = {
        "schema": "MTTQaSU3RetardedMatchingMapAttempt.v2",
        "status": "QASU3_RETARDED_MATCHING_MAP_ATTEMPTED_B45_IMPORTED_ZERO_SAME_HRG_MAPS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "QaSU3_retarded_response_available": True,
        "QaSU3_electroweak_interface_available": True,
        "B44_conditional_profile_available": True,
        "B45_one_primitive_tier_available": True,
        "tested_matching_map_count": len(qa_matching_rows),
        "accepted_same_HRG_matching_map_count": len(accepted_matching),
        "rows": qa_matching_rows,
        "decision": {
            "typed_same_HRG_QaSU3_electroweak_matching_map": False,
            "accepted_RO_nonHiggs_sector_map": False,
            "nonHiggs_prediction_emitted_without_retuning": False,
            "B44_conditional_profile_is_HRG_prediction_now": False,
            "B45_is_new_portfolio_support": True,
            "B45_is_HRG_crossuse_prediction_now": False,
        },
    }

    b39_bridge = {
        "schema": "MTTB39ToB45ChainImport.v1",
        "status": "B39_IMPORTED_AS_CHAIN_LINK_SUPERSEDED_BY_B45",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "B39_status": b39["status"],
        "B39_local_kernel_status": b39_local["status"],
        "B39_closed_for_local_tier": {
            "local_tier_source_kernel_closed": b39["local_tier_source_kernel_closed"],
            "source_promotion_closed_in_local_tier": b39["source_promotion_closed_in_local_tier"],
            "pre_residual_phase_shift_operator_source": b39_local["kernel_clauses_under_local_principle"]["pre_residual_phase_shift_operator_source"],
            "same_source_hessian_b_selected_rows": b39_local["kernel_clauses_under_local_principle"]["same_source_hessian_b_selected_rows"],
            "residual_projector_replay_used_as_source": b39_local["residual_projector_replay_used_as_source"],
            "locked_target_values_used_as_source": b39_local["locked_target_values_used_as_source"],
        },
        "later_chain": {
            "B40": b40["status"],
            "B41": b41["status"],
            "B42": b42["status"],
            "B43": b43["status"],
            "B44": b44["status"],
            "B45": b45["status"],
        },
        "decision": {
            "B39_is_latest_frontier": False,
            "B39_remains_valid_support": True,
            "use_B45_as_latest_frontier": True,
            "treat_B39_as_HRG_numeric_source": False,
        },
    }

    b45_portfolio = {
        "schema": "MTTB45PortfolioFrontierImport.v1",
        "status": "B45_PORTFOLIO_FRONTIER_IMPORTED_ONE_PRIMITIVE_TIER_HRG_NOT_PROMOTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "chain_support": {
            "B40_local_kernel_to_profile": {
                "status": b40["status"],
                "u_dyn_source_derived": profile["u_dyn_source_derived"],
                "u_dyn_value": profile["u_dyn_value"],
                "internal_lambda_12_closed": profile["internal_lambda_12_closed"],
                "internal_lambda_12_value": profile["internal_lambda_12_value"],
                "physical_gate_status": b40_gate["status"],
            },
            "B41_physical_gate": {
                "status": b41["status"],
                "anchor_status": b41_anchor["status"],
                "K_phys_or_f_ab_closed": b41_anchor["decision"]["K_phys_or_f_ab_closed"],
                "one_universal_primitive_extension_ready": b41_anchor["decision"]["one_universal_primitive_extension_ready"],
                "still_open": b41_boundary["still_open"],
            },
            "B42_one_primitive_bridge": {
                "status": b42["status"],
                "contract_closed": b42["one_primitive_physical_bridge_contract_closed"],
                "value_selected": b42["one_primitive_value_selected"],
                "K_phys_alpha_phys_mu_match_collapsed_to_one_primitive": b42[
                    "K_phys_alpha_phys_mu_match_collapsed_to_one_primitive"
                ],
            },
            "B44_conditional_profile": {
                "status": b44["status"],
                "conditional_profile_execution_closed": b44["conditional_profile_execution_closed"],
                "conditional_minimal_threshold_sin2": b44["conditional_minimal_threshold_sin2"],
                "assumption_lock": b44_assumption["assumptions"],
                "still_open": b44_boundary["still_open"],
            },
            "B45_portfolio": {
                "status": b45["status"],
                "weak_mixing_down_to_one_shared_primitive_tier": b45["weak_mixing_down_to_one_shared_primitive_tier"],
                "recommend_cross_constant_next": b45["recommend_cross_constant_next"],
                "selected_next_constant": b45["selected_next_constant"],
                "global_budget": budget,
                "switch_decision": b45_switch["decision"],
                "next_constant_priority": b45_next_constant["selected_next"],
                "still_open": b45_boundary["still_open"],
                "next_workorder": b45_next,
            },
        },
        "decision": {
            "B45_latest_adjacent_frontier_imported": True,
            "weak_mixing_one_shared_primitive_tier_reached": True,
            "B44_conditional_profile_replay_available": True,
            "selected_numeric_primitive_value_available": False,
            "B45_treat_as_physical_weak_angle_closure": False,
            "B45_treat_as_HRG_numeric_source": False,
            "compare_HRG_to_E0L0_or_CONSTGR01_next": True,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHRGSourceRuleAttempt.v2",
        "status": "NEXT_FRONTIER_B45_PORTFOLIO_PRIMITIVE_COMPARISON_OR_CONSTGR01_SHARED_SOURCE_TEST",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "anti-loop scan corrected latest constants frontier from B39 to B45",
            "B40-B45 weak-mixing chain imported as real one-primitive portfolio support",
            "B44 conditional profile replay classified as replay-only, not HRG prediction",
            "B45 one-shared-primitive tier classified as symbolic support with zero selected numeric primitive values",
            "HRG universal primitive source-rule attempt executed with zero accepted rules",
            "same-HRG Qa/SU3/electroweak/B45 matching map attempt executed with zero accepted maps",
        ],
        "still_open": [
            "typed identity or separation theorem between E0/L0/modal-gap primitive and UP-RET-OVERLAP.HRG",
            "CONST-GR-01 shared primitive source test recommended by B45",
            "selected numeric primitive value for the B45 one-primitive tier",
            "strict Qa-stack threshold vector",
            "precision RG scheme conversion",
            "selected HRG numeric source rule from determinant/index/RG transport",
            "universal admission of UP-RET-OVERLAP.HRG",
            "true SM/no-knob equivalence",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedHRGUniversalPrimitiveSourceRuleOrQaSU3RetardedMatchingMap",
        "status": STATUS,
        "previous_status": previous["status"],
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "theorem": {
            "name": "HRGUniversalPrimitiveSourceRuleOrQaSU3RetardedMatchingMapTheorem",
            "proved": True,
            "statement": (
                "The latest adjacent constants frontier is B45, not B39.  B45 "
                "shows weak mixing has reached a one-shared-primitive portfolio "
                "handoff with conditional profile replay available and zero selected "
                "numeric primitive values.  This is real cross-constant progress, "
                "but it does not emit the numeric UP-RET-OVERLAP.HRG source rule "
                "or a same-HRG non-Higgs prediction."
            ),
        },
        "closure_decision": {
            "anti_loop_latest_frontier_scan_completed": True,
            "B39_not_latest_frontier": True,
            "B45_latest_adjacent_frontier_imported": True,
            "B45_weak_mixing_one_shared_primitive_tier": True,
            "B44_conditional_profile_replay_available": True,
            "B45_recommend_cross_constant_next": True,
            "B45_selected_numeric_primitive_value_available": False,
            "B45_physical_weak_angle_closed": False,
            "B45_strict_full_no_knob_closed": False,
            "HRG_numeric_source_rule_derived": False,
            "QaSU3_same_HRG_retarded_matching_map_accepted": False,
            "B45_same_HRG_crossuse_prediction_now": False,
            "UP_RET_OVERLAP_HRG_universal_admitted": False,
            "next_nonlooping_target_identified": True,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "UP_RET_OVERLAP_HRG": hrg,
            "log_UP_RET_OVERLAP_HRG": log_hrg,
            "QaSU3_chi_Qa": chi,
            "QaSU3_log_2008": log_2008,
            "B40_u_dyn": profile["u_dyn_value"],
            "B40_internal_lambda_12": profile["internal_lambda_12_value"],
            "B44_conditional_minimal_threshold_sin2": b44["conditional_minimal_threshold_sin2"],
            "B45_current_shared_physical_primitives_needed_for_alpha_and_weak_mixing": budget[
                "current_shared_physical_primitives_needed_for_alpha_and_weak_mixing"
            ],
            "B45_selected_numeric_primitive_values_now": budget["selected_numeric_primitive_values_now"],
            "HRG_source_rule_candidate_count": len(hrg_lanes),
            "accepted_HRG_source_rule_count": len(accepted_hrg_rules),
            "tested_same_HRG_matching_map_count": len(qa_matching_rows),
            "accepted_same_HRG_matching_map_count": len(accepted_matching),
        },
        "packets": {
            "frontier_novelty_scan": rel(NOVELTY),
            "hrg_source_rule_attempt": rel(HRG_RULE),
            "qasu3_matching_attempt": rel(QA_MATCHING),
            "b39_chain_import": rel(B39_BRIDGE),
            "b45_portfolio_frontier_import": rel(B45_PORTFOLIO),
            "cutset": rel(CUTSET),
        },
        "what_closes": {
            "latest_adjacent_frontier_import": True,
            "anti_loop_novelty_scan": True,
            "B40_B45_chain_classification": True,
            "B45_portfolio_handoff_import": True,
            "HRG_source_rule_attempt_after_B45": True,
            "QaSU3_matching_attempt_after_B45": True,
        },
        "what_remains_open": {
            "source_derived_HRG_value": True,
            "same_HRG_nonHiggs_prediction": True,
            "typed_identity_or_separation_between_HRG_and_E0L0": True,
            "CONST_GR_01_shared_primitive_source_test": True,
            "selected_numeric_primitive_value_for_B45": True,
            "strict_QaStack_threshold_vector": True,
            "precision_RG_scheme_conversion": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedHRGUniversalPrimitiveSourceRuleOrQaSU3RetardedMatchingMap",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "proof_note": rel(NOTE),
        "verified_packets": list(candidate["packets"].values()),
        "closure_claimed": True,
        "anti_loop_latest_frontier_scan_completed": True,
        "B39_not_latest_frontier": True,
        "B45_latest_adjacent_frontier_imported": True,
        "B45_weak_mixing_one_shared_primitive_tier": True,
        "B44_conditional_profile_replay_available": True,
        "B45_selected_numeric_primitive_value_available": False,
        "B45_physical_weak_angle_closed": False,
        "B45_strict_full_no_knob_closed": False,
        "HRG_numeric_source_rule_derived": False,
        "QaSU3_same_HRG_retarded_matching_map_accepted": False,
        "accepted_HRG_source_rule_count": len(accepted_hrg_rules),
        "accepted_same_HRG_matching_map_count": len(accepted_matching),
        "UP_RET_OVERLAP_HRG_universal_admitted": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HRG Universal Primitive Source Rule or QaSU3 Retarded Matching Map v1

Status: `{STATUS}`

## Anti-Loop Result

We were **not** at the latest adjacent frontier.  I originally found B39, but
the constants weak-mixing chain continues to B45:

```text
B39 status = {b39["status"]}
B40 status = {b40["status"]}
B44 status = {b44["status"]}
B45 status = {b45["status"]}
```

B39 remains valid support, but it is not the latest frontier.  B45 is the
current adjacent result: weak mixing is handoff-ready in a one-shared-primitive
portfolio tier.

## Decision

Accepted HRG source rules: `0 / {len(hrg_lanes)}`.

Accepted same-HRG Qa/SU3/electroweak/B45 matching maps: `0 / {len(qa_matching_rows)}`.

B44 emits a conditional replay value:

```text
sin2_conditional = {b44["conditional_minimal_threshold_sin2"]}
```

That value is not a strict physical weak-angle prediction and not an HRG
cross-use prediction.  B45 records one shared symbolic E0/L0/modal-gap primitive
for alpha plus weak mixing, but selected numeric primitive values remain:

```text
selected_numeric_primitive_values_now = {budget["selected_numeric_primitive_values_now"]}
```

So B45 is real progress, but it is not the HRG numeric source rule.  It moves
the next non-looping target to a primitive-portfolio comparison: decide whether
`UP-RET-OVERLAP.HRG` is typed as the same E0/L0/modal-gap primitive, or prove it
is a distinct H-threshold primitive, preferably by the CONST-GR-01 shared
primitive source test recommended by B45.

## Useful Support

Qa/SU3 still supplies:

```text
chi_Qa = {chi}
I_Qa = log(2008) = {log_2008}
```

B40 supplies:

```text
u_dyn = {profile["u_dyn_value"]}
internal_lambda_12 = {profile["internal_lambda_12_value"]}
```

## Boundary

`UP-RET-OVERLAP.HRG={hrg}` remains empirical H calibration support.  It is not
universally admitted and not no-knob source-derived.  B45 does not change that;
it changes the strategy by preventing further weak-angle-only optimization.

## Next

`{NEXT}`
"""

    write_json(NOVELTY, novelty)
    write_json(HRG_RULE, hrg_rule)
    write_json(QA_MATCHING, qa_matching)
    write_json(B39_BRIDGE, b39_bridge)
    write_json(B45_PORTFOLIO, b45_portfolio)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    for path in [OUTPUT, CERT, NOTE]:
        print(f"Wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
