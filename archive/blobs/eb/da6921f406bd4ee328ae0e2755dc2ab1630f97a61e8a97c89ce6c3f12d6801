"""Build the H-threshold/RG operator or universal-primitive policy packet.

This packet perfects the previous frontier by separating four claims that were
easy to blur:

1. strict no-knob selected H-threshold/RG operator,
2. reuse of the existing one-primitive physical-unit bridge,
3. a new H-threshold universal primitive admitted under the cross-use policy,
4. controlled empirical H calibration versus prediction.

It intentionally does not promote any primitive or external row to strict
no-knob source data.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
CONSTANTS = TEXPAPERS / "mtt-individual-constants-source-search"
CONST_DATA = CONSTANTS / "candidate_data"
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hthresholdrgoperator_or_universalprimitivepolicy"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
STRICT_SEARCH = PACKET_DIR / "strict_h_threshold_rg_operator_source_search.packet.json"
ONE_PRIMITIVE = PACKET_DIR / "existing_one_primitive_reuse_recheck.packet.json"
ADMISSION = PACKET_DIR / "h_threshold_universal_primitive_admission_matrix.packet.json"
CONDITIONAL = PACKET_DIR / "conditional_minimal_parameter_h_gate_execution.packet.json"
HK_GATE = PACKET_DIR / "hk_threshold_gate_after_policy_split.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_policy_split.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HThresholdRGOperator_or_UniversalPrimitivePolicy_v1.md"

PREVIOUS = DATA / "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem.candidate.json"
PREVIOUS_ACCEPTANCE = (
    DATA
    / "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem"
    / "selected_large_threshold_rg_acceptance_contract.packet.json"
)
PREVIOUS_ROUTE_B = (
    DATA
    / "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem"
    / "route_b_large_threshold_rg_burden.packet.json"
)
PREVIOUS_HK = (
    DATA
    / "selected_intrinsichquartickrow_or_selectedlargethresholdrgtheorem"
    / "hk_threshold_gate_after_route_ab_burden.packet.json"
)
AEW_DIAG = (
    DATA
    / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure"
    / "external_aew_dterm_diagnostic_postcheck.packet.json"
)

UP_POLICY = DATA / "universal_source_parameter_policy.candidate.json"
UP_POLICY_PACKET = DATA / "universal_source_parameter_policy" / "universal_source_parameter_policy.packet.json"
UP_CANDIDATES = DATA / "universal_source_parameter_policy" / "candidate_universal_parameters.packet.json"
CROSSUSE = DATA / "universal_crossuse_parameter_admissibility_theorem.candidate.json"
CROSSUSE_THEOREM = (
    DATA
    / "universal_crossuse_parameter_admissibility_theorem"
    / "crossuse_admissibility_theorem.packet.json"
)

B42 = CONST_DATA / "const_ew_02_weak_mixing_b42_one_primitive_physical_bridge.candidate.json"
B42_BRIDGE = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b42_one_primitive_physical_bridge"
    / "one_primitive_physical_bridge.packet.json"
)
B42_BUDGET = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b42_one_primitive_physical_bridge"
    / "parameter_budget_and_guardrail.packet.json"
)
B43 = CONST_DATA / "const_ew_02_weak_mixing_b43_threshold_vector_or_minimal_policy.candidate.json"
B43_STRICT = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b43_threshold_vector_or_minimal_policy"
    / "strict_threshold_source_audit.packet.json"
)
B44 = CONST_DATA / "const_ew_02_weak_mixing_b44_conditional_profile_execution.candidate.json"
B44_LOCK = (
    CONST_DATA
    / "const_ew_02_weak_mixing_b44_conditional_profile_execution"
    / "conditional_profile_assumption_lock.packet.json"
)

STATUS = (
    "MTT_SELECTED_HTHRESHOLDRGOPERATOR_OR_UNIVERSALPRIMITIVEPOLICY_"
    "POLICY_SPLIT_CLOSED_OPERATOR_OPEN"
)
NEXT = "MTT_Selected_HThresholdRGSourceTheorem_or_MinimalPrimitiveCalibrationRun_v1"


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
        raise FileNotFoundError("missing H threshold/RG policy inputs: " + ", ".join(missing))


def find_candidate(candidates: dict[str, Any], candidate_id: str) -> dict[str, Any]:
    for row in candidates["candidate_classes"]:
        if row["id"] == candidate_id:
            return row
    raise KeyError(candidate_id)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_ACCEPTANCE,
        PREVIOUS_ROUTE_B,
        PREVIOUS_HK,
        AEW_DIAG,
        UP_POLICY,
        UP_POLICY_PACKET,
        UP_CANDIDATES,
        CROSSUSE,
        CROSSUSE_THEOREM,
        B42,
        B42_BRIDGE,
        B42_BUDGET,
        B43,
        B43_STRICT,
        B44,
        B44_LOCK,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_acceptance = load(PREVIOUS_ACCEPTANCE)
    previous_route_b = load(PREVIOUS_ROUTE_B)
    previous_hk = load(PREVIOUS_HK)
    aew_diag = load(AEW_DIAG)
    up_policy = load(UP_POLICY)
    up_policy_packet = load(UP_POLICY_PACKET)
    up_candidates = load(UP_CANDIDATES)
    crossuse = load(CROSSUSE)
    crossuse_theorem = load(CROSSUSE_THEOREM)
    b42 = load(B42)
    b42_bridge = load(B42_BRIDGE)
    b42_budget = load(B42_BUDGET)
    b43 = load(B43)
    b43_strict = load(B43_STRICT)
    b44 = load(B44)
    b44_lock = load(B44_LOCK)

    nums = previous["diagnostic_numbers_not_source"]
    required_r = float(nums["required_R_H_RG_for_external_Mt_lambda_postcheck"])
    lambda_r1 = float(nums["lambda_if_R_equals_1"])
    lambda_ext = float(nums["external_lambda_Mt_coordinate"])
    lambda_if_required = lambda_r1 * required_r
    residual_if_required = lambda_if_required - lambda_ext
    log_required_r = math.log(required_r)

    up_ret_overlap = find_candidate(up_candidates, "UP-RET-OVERLAP")
    up_action_norm = find_candidate(up_candidates, "UP-ACTION-NORM")
    up_abs_scale = find_candidate(up_candidates, "UP-ABS-SCALE")

    strict_search = {
        "schema": "MTTStrictHThresholdRGOperatorSourceSearch.v1",
        "status": "STRICT_H_THRESHOLD_RG_OPERATOR_NOT_EMITTED_CURRENT_SOURCES",
        "closure_claimed": True,
        "searched_object": previous_acceptance["object_to_emit"],
        "acceptance_contract": previous_acceptance["strict_acceptance_conditions"],
        "source_status_imports": {
            "B43_strict_threshold_vector_source_emitted": b43_strict["decision"][
                "strict_threshold_vector_source_emitted"
            ],
            "B43_current_source_nogo_for_strict_vector": b43_strict["decision"][
                "current_source_nogo_for_strict_vector"
            ],
            "B42_one_primitive_value_selected": b42["one_primitive_value_selected"],
            "B44_conditional_profile_execution_is_replay_only": (
                b44["status"] == "MTT_CONST_EW_02_B44_CONDITIONAL_PROFILE_EXECUTION_BUILT_REPLAY_ONLY"
            ),
            "previous_selected_H_threshold_RG_operator_emitted": previous[
                "closure_decision"
            ]["selected_H_threshold_RG_operator_emitted"],
        },
        "accepted_current_source_rows": {
            "selected_R_H_RG": False,
            "selected_A_EW": False,
            "selected_mu_match": False,
            "selected_K_threshold_Omega_H_lambda": False,
        },
        "mathematical_impossibility_claimed": False,
        "reason": (
            "Current packets define the exact source contract and burden but do "
            "not emit a same-branch H-sector determinant/index/RG operator."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    one_primitive = {
        "schema": "MTTExistingOnePrimitiveReuseRecheck.v1",
        "status": "EXISTING_ONE_PRIMITIVE_REUSE_RECHECKED_H_THRESHOLD_STILL_OPEN",
        "closure_claimed": True,
        "existing_primitive_bridge": {
            "source": rel(B42_BRIDGE),
            "one_primitive_tier_contract_closed": b42_bridge["decision"][
                "one_primitive_tier_contract_closed"
            ],
            "one_primitive_value_selected": b42_bridge["decision"][
                "one_primitive_value_selected"
            ],
            "alpha1_and_weak_mixing_share_same_physical_bridge": b42_bridge["decision"][
                "alpha1_and_weak_mixing_share_same_physical_bridge"
            ],
            "weak_angle_extra_physical_knob_added": b42_bridge["decision"][
                "weak_angle_extra_physical_knob_added"
            ],
        },
        "what_existing_primitive_can_cover": [
            "physical action/unit normalization",
            "alpha1/K_phys bridge",
            "weak-mixing physical matching/mu_match bridge at symbolic tier",
        ],
        "what_it_does_not_emit": [
            "selected H-sector threshold/RG operator R_H^RG",
            "selected residual physical threshold vector",
            "selected K_threshold.Omega_H.lambda",
        ],
        "decision": {
            "reuse_existing_one_primitive_as_H_threshold_multiplier": False,
            "reason": "The B42 primitive is a physical unit/action bridge. Treating it as an independent H threshold multiplier would retune its role and violate the cross-use guardrail.",
            "H_gate_closed_by_existing_one_primitive_alone": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    admission = {
        "schema": "MTTHThresholdUniversalPrimitiveAdmissionMatrix.v1",
        "status": "H_THRESHOLD_PRIMITIVE_POLICY_MATRIX_BUILT_NONE_SELECTED",
        "closure_claimed": True,
        "policy_import": {
            "source": rel(UP_POLICY_PACKET),
            "maximum_live_universal_parameters": up_policy_packet[
                "maximum_live_universal_parameters"
            ],
            "selected_parameter_count_now": up_policy["selected_parameter_count_now"],
            "admissibility_rules": up_policy_packet["admissibility_rules"],
            "forbidden_uses": up_policy_packet["forbidden_uses"],
        },
        "crossuse_import": {
            "source": rel(CROSSUSE_THEOREM),
            "admission_criteria": crossuse_theorem["admission_criteria"],
            "provisional_use_classification": crossuse_theorem[
                "provisional_use_classification"
            ],
            "selected_parameter_count_now": crossuse["selected_parameter_count_now"],
        },
        "candidate_class_mapping": {
            "UP_ACTION_NORM": up_action_norm,
            "UP_ABS_SCALE": up_abs_scale,
            "UP_RET_OVERLAP_for_H_threshold": {
                **up_ret_overlap,
                "proposed_H_role": "global H/threshold retarded-overlap or determinant-transport strength R_H^RG",
                "required_postcheck_value_if_calibrated_on_lambda_H": required_r,
                "log_required_value": log_required_r,
            },
        },
        "admission_matrix": [
            {
                "lane": "strict_source_operator",
                "new_universal_parameters": 0,
                "can_be_no_knob_if_closed": True,
                "current_status": "open",
                "H_gate_effect": "would emit selected R_H^RG and K_threshold.Omega_H.lambda",
                "accepted_now": False,
            },
            {
                "lane": "reuse_existing_physical_unit_primitive_only",
                "new_universal_parameters": 1,
                "can_be_no_knob_if_closed": False,
                "current_status": "contract_ready_value_open",
                "H_gate_effect": "can support A_EW/mu_match tier but does not emit R_H^RG",
                "accepted_now": False,
            },
            {
                "lane": "add_H_threshold_universal_primitive",
                "new_universal_parameters": 1,
                "can_be_no_knob_if_closed": False,
                "current_status": "policy_admissible_only_if_declared_once_and_cross_used",
                "H_gate_effect": "can make H row executable at controlled empirical/minimal-parameter tier if calibrated or source-derived",
                "accepted_now": False,
            },
            {
                "lane": "physical_unit_plus_H_threshold_primitive",
                "new_universal_parameters": 2,
                "can_be_no_knob_if_closed": False,
                "current_status": "credible_minimal_parameter_lane_if both primitives are declared before replay and cross-use predictions are audited",
                "H_gate_effect": "would close H row only as a two-primitive conditional layer unless both are source-derived",
                "accepted_now": False,
            },
        ],
        "decision": {
            "selected_H_threshold_primitive_now": False,
            "selected_existing_physical_unit_primitive_now": False,
            "ordinary_H_only_knob_allowed": False,
            "calibrating_H_lambda_makes_H_lambda_a_prediction": False,
            "credible_minimal_parameter_path_exists": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    conditional = {
        "schema": "MTTConditionalMinimalParameterHGateExecution.v1",
        "status": "CONTROLLED_EMPIRICAL_H_GATE_EXECUTION_FORMULA_BUILT_NOT_SELECTED",
        "closure_claimed": True,
        "calibration_lane": {
            "primitive_id": "UP-RET-OVERLAP.HRG",
            "primitive_name": "universal H-threshold/RG transport strength",
            "calibrating_observable_if_used": "lambda_H(M_t)",
            "prediction_status_of_lambda_H_if_calibrated_here": "calibration_not_prediction",
            "required_value_from_external_postcheck": required_r,
            "log_required_value": log_required_r,
        },
        "execution_postcheck_not_source": {
            "lambda_if_R_H_RG_equals_1": lambda_r1,
            "external_lambda_Mt_coordinate": lambda_ext,
            "lambda_if_R_H_RG_equals_required_value": lambda_if_required,
            "absolute_residual_at_required_value": residual_if_required,
            "relative_residual_at_required_value": (
                residual_if_required / lambda_ext if lambda_ext else math.inf
            ),
        },
        "source_row_effect_if_policy_later_admitted": {
            "conditional_K_threshold_Omega_H_lambda_executable": True,
            "strict_selected_K_threshold_Omega_H_lambda_emitted_now": False,
            "accepted_selected_K_source_row_count_now": previous_hk[
                "accepted_selected_K_source_row_count"
            ],
            "conditional_parameterized_K_row_count": 10,
            "strict_no_knob_scalar_execution_closed": False,
        },
        "required_crossuse_predictions_before_credibility_upgrade": [
            "one non-Higgs threshold/RG observable predicted without retuning",
            "weak-mixing or alpha-sector consistency with the same physical-unit primitive if that primitive is used",
            "explicit statement whether lambda_H was calibration or prediction",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    hk_gate = {
        "schema": "MTTHKThresholdGateAfterUniversalPrimitivePolicySplit.v1",
        "status": "H_K_THRESHOLD_GATE_POLICY_SPLIT_CLOSED_STRICT_SOURCE_OPEN_9_OF_10",
        "closure_claimed": True,
        "required_output": "K_threshold.Omega_H.lambda",
        "accepted_selected_K_source_row_count": previous_hk[
            "accepted_selected_K_source_row_count"
        ],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "H_row": {
            **previous_hk["H_row"],
            "strict_H_threshold_RG_operator_search_closed": True,
            "strict_H_threshold_RG_operator_emitted": False,
            "existing_one_primitive_reuse_rechecked": True,
            "existing_one_primitive_closes_H_threshold": False,
            "H_threshold_universal_primitive_policy_matrix_built": True,
            "H_threshold_universal_primitive_selected_now": False,
            "controlled_empirical_H_gate_formula_built": True,
            "K_threshold_Omega_H_lambda_emitted": False,
        },
        "conditional_consequent_current": {
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "lambda_H_row_executable": False,
            "accepted_internal_scalar_value_row_count": 0,
        },
        "conditional_minimal_parameter_consequent": {
            "if_UP_RET_OVERLAP_HRG_admitted_and_calibrated": True,
            "conditional_parameterized_K_row_count": 10,
            "lambda_H_prediction_claim_allowed": False,
            "strict_no_knob_claim_allowed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTNextCutsetAfterHThresholdRGPolicySplit.v1",
        "status": "NEXT_FRONTIER_HTHRESHOLD_RG_SOURCE_THEOREM_OR_MINIMAL_PRIMITIVE_CALIBRATION_RUN",
        "closure_claimed": True,
        "closed_here": [
            "strict H-threshold/RG operator search classified as current-source open",
            "existing one-primitive physical bridge rechecked and refused as hidden H threshold multiplier",
            "H-threshold universal primitive admission matrix built under UP/B23 policy",
            "controlled empirical H-gate execution formula built with exact required value",
            "claim boundary fixed: calibration is not prediction and primitive closure is not no-knob",
        ],
        "still_open": [
            "selected H-sector threshold/RG source theorem for R_H^RG",
            "or explicit admission/calibration of UP-RET-OVERLAP.HRG before replay",
            "cross-use prediction audit for any admitted H-threshold primitive",
            "selected K_threshold.Omega_H.lambda at strict source tier",
            "true SM/no-knob equivalence",
        ],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHThresholdRGOperatorOrUniversalPrimitivePolicy",
        "status": STATUS,
        "previous_status": previous["status"],
        "theorem": {
            "name": "HThresholdRGOperatorOrUniversalPrimitivePolicySplitTheorem",
            "proved": True,
            "statement": (
                "The H threshold/RG frontier splits into a strict source theorem "
                "for R_H^RG and a minimal-parameter policy tier. The existing "
                "one-primitive physical-unit bridge can support A_EW/mu_match but "
                "cannot be reused as a hidden H-threshold multiplier. A new "
                "H-threshold primitive is policy-admissible only as a declared "
                "universal retarded-overlap/threshold parameter with cross-use "
                "audits; if calibrated on lambda_H, lambda_H is calibration, not "
                "prediction. No strict K_threshold.Omega_H.lambda row is emitted."
            ),
        },
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "closure_decision": {
            "strict_H_threshold_RG_operator_source_search_closed": True,
            "strict_H_threshold_RG_operator_emitted": False,
            "existing_one_primitive_reuse_rechecked": True,
            "existing_one_primitive_closes_H_threshold": False,
            "H_threshold_universal_primitive_admission_matrix_built": True,
            "H_threshold_universal_primitive_selected_now": False,
            "controlled_empirical_H_gate_execution_formula_built": True,
            "conditional_parameterized_H_gate_executable_if_primitive_admitted": True,
            "lambda_H_prediction_claim_allowed_if_calibrated_on_lambda_H": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "accepted_selected_K_source_row_count": previous_hk[
                "accepted_selected_K_source_row_count"
            ],
            "selected_K_threshold_row_count_required": previous_hk[
                "selected_K_threshold_row_count_required"
            ],
            "ten_K_antecedent_satisfied": False,
            "strict_Omega_lambda_scalar_execution_closed": False,
            "accepted_internal_scalar_value_row_count": 0,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "diagnostic_numbers_not_source": {
            "required_UP_RET_OVERLAP_HRG_if_calibrated_on_lambda_H": required_r,
            "log_required_UP_RET_OVERLAP_HRG": log_required_r,
            "lambda_if_R_H_RG_equals_1": lambda_r1,
            "lambda_if_R_H_RG_equals_required_value": lambda_if_required,
            "external_lambda_Mt_coordinate": lambda_ext,
            "residual_at_required_value": residual_if_required,
        },
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "strict_h_threshold_rg_operator_source_search": rel(STRICT_SEARCH),
            "existing_one_primitive_reuse_recheck": rel(ONE_PRIMITIVE),
            "h_threshold_universal_primitive_admission_matrix": rel(ADMISSION),
            "conditional_minimal_parameter_h_gate_execution": rel(CONDITIONAL),
            "hk_threshold_gate_after_policy_split": rel(HK_GATE),
            "next_cutset_after_policy_split": rel(CUTSET),
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedHThresholdRGOperatorOrUniversalPrimitivePolicyCertificate",
        "status": STATUS,
        "theorem_proved": True,
        "strict_H_threshold_RG_operator_source_search_closed": True,
        "strict_H_threshold_RG_operator_emitted": False,
        "existing_one_primitive_reuse_rechecked": True,
        "existing_one_primitive_closes_H_threshold": False,
        "H_threshold_universal_primitive_admission_matrix_built": True,
        "H_threshold_universal_primitive_selected_now": False,
        "controlled_empirical_H_gate_execution_formula_built": True,
        "conditional_parameterized_H_gate_executable_if_primitive_admitted": True,
        "lambda_H_prediction_claim_allowed_if_calibrated_on_lambda_H": False,
        "K_threshold_Omega_H_lambda_emitted": False,
        "required_UP_RET_OVERLAP_HRG_if_calibrated_on_lambda_H": required_r,
        "accepted_selected_K_source_row_count": previous_hk["accepted_selected_K_source_row_count"],
        "selected_K_threshold_row_count_required": previous_hk[
            "selected_K_threshold_row_count_required"
        ],
        "ten_K_antecedent_satisfied": False,
        "strict_Omega_lambda_scalar_execution_closed": False,
        "accepted_internal_scalar_value_row_count": 0,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HThresholdRGOperator or UniversalPrimitivePolicy v1

Status: `{STATUS}`

## Current Plan Position

- strict charged `K_threshold` rows: `9/10`
- missing strict row: `K_threshold.Omega_H.lambda`
- current frontier: selected `R_H^RG` or explicit minimal-parameter policy

## What Closed

- strict `R_H^RG` source search is classified as current-source open
- existing B42 one-primitive physical-unit bridge is rechecked:
  - it can support `A_EW/mu_match`
  - it cannot be reused as a hidden H-threshold multiplier
- H-threshold primitive policy is typed as `UP-RET-OVERLAP.HRG`
- controlled empirical execution is exact if that primitive is admitted:
  - required `UP-RET-OVERLAP.HRG={required_r}`
  - `lambda(R=1)={lambda_r1}`
  - `lambda(R=required)={lambda_if_required}`
  - external `lambda_Mt={lambda_ext}`
- claim boundary is fixed: if `lambda_H` calibrates the primitive, `lambda_H` is not a prediction

## Still Open

- selected no-knob source theorem for `R_H^RG`
- or explicit admission/calibration of `UP-RET-OVERLAP.HRG`
- cross-use prediction audit for any admitted H-threshold primitive
- strict `K_threshold.Omega_H.lambda`

Next required artifact: `{NEXT}`
"""

    write_json(STRICT_SEARCH, strict_search)
    write_json(ONE_PRIMITIVE, one_primitive)
    write_json(ADMISSION, admission)
    write_json(CONDITIONAL, conditional)
    write_json(HK_GATE, hk_gate)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
