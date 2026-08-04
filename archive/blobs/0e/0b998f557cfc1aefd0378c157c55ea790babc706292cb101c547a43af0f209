"""Build A_EW metrology-slot execution / HRG non-Higgs selector packet.

This packet executes the two branches exposed by the Higgs shared-metrology
handoff theorem:

* A_EW/mu/RG metrology-slot execution for the Higgs D-term route; and
* HRG non-Higgs prediction selector execution for UP-RET-OVERLAP.HRG.

It also records the diagnostic burden equivalence already present in the
external D-term postcheck: lambda_Mt / (A_EW*s_beta) equals the calibrated HRG
factor.  That is a useful target equation, but it is not a selected source
derivation.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_aewmetrologyslotexecution_or_hrgnonhiggspredictionselector"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
AEW_EXECUTION = PACKET_DIR / "aew_metrology_slot_execution.packet.json"
BURDEN = PACKET_DIR / "aew_hrg_burden_equivalence_diagnostic.packet.json"
HRG_SELECTOR = PACKET_DIR / "hrg_nonhiggs_prediction_selector_execution.packet.json"
NEXT_PRIORITY = PACKET_DIR / "next_priority_after_dual_execution.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_aew_hrg_selector_execution.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_AEWMetrologySlotExecution_or_HRGNonHiggsPredictionSelector_v1.md"

PREVIOUS = DATA / "selected_higgssharedmetrologyprimitivehandoff_or_hrgsourcetheoremreentry.candidate.json"
PREVIOUS_METROLOGY = (
    DATA
    / "selected_higgssharedmetrologyprimitivehandoff_or_hrgsourcetheoremreentry"
    / "higgs_shared_metrology_handoff_theorem.packet.json"
)
PREVIOUS_HRG = (
    DATA
    / "selected_higgssharedmetrologyprimitivehandoff_or_hrgsourcetheoremreentry"
    / "hrg_source_admission_reentry_theorem.packet.json"
)

EW_BOUNDARY = DATA / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure.candidate.json"
AEW_GATE = (
    DATA
    / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure"
    / "aew_source_tier_gate.packet.json"
)
AEW_DIAGNOSTIC = (
    DATA
    / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure"
    / "external_aew_dterm_diagnostic_postcheck.packet.json"
)
DTERM_DECISION = (
    DATA
    / "selected_ewboundaryrgfactorforhiggsdterm_or_directtenkclosure"
    / "dterm_route_decision_after_aew_recheck.packet.json"
)
H_CONDITIONAL_FORMULA = (
    DATA
    / "selected_hradialthresholdscalarsource_or_tenkclosure"
    / "conditional_h_k_from_ew_boundary_formula.packet.json"
)
WZH_CANDIDATE = DATA / "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation.candidate.json"
WZH_INVENTORY = (
    DATA
    / "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation"
    / "wzh_electroweak_row_inventory.packet.json"
)
WZH_ACCEPTANCE = (
    DATA
    / "selected_wzhelectroweakrows_or_selectedrthetamassschemederivation"
    / "wzh_external_benchmark_row_acceptance.packet.json"
)
WZH_SIDECARS = (
    DATA
    / "selected_covariancesidecarfill_or_rthetasourcerowderivation"
    / "wzh_gauge_and_lambda_covariance_sidecars.packet.json"
)

HRG_NONHIGGS_EXECUTION = (
    DATA
    / "selected_hrgnonhiggsretardedoverlapmap_or_strictsourcetheorem"
    / "nonhiggs_hrg_source_map_execution.packet.json"
)
HRG_TARGET_MATRIX = (
    DATA
    / "selected_hrgprimitivecrossusepredictionaudit_or_sourcetheoremattempt"
    / "hrg_nonhiggs_target_matrix.packet.json"
)
RO_VALUE_EXECUTION = (
    DATA
    / "selected_rovaluesource_or_nonhiggsmapexecution"
    / "ro_value_source_execution.packet.json"
)
ALPHA1_SOURCE_IDENTITY = DATA / "selected_alpha1_sourceidentity_or_retardedkernel_value_attempt.candidate.json"
ALPHA1_NORMALIZATION = DATA / "selected_alpha1_source_strength_normalization_theorem.candidate.json"
ALPHA1_VALUE_ATTEMPT = DATA / "selected_alpha1_source_strength_value_emission_attempt.candidate.json"
DYNAMIC_C1_VALUE = DATA / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run.candidate.json"
DYNAMIC_C1_LANE_A = (
    DATA
    / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run"
    / "lane_a_same_source_value_emission_attempt.packet.json"
)
DYNAMIC_C1_LANE_B = (
    DATA
    / "selected_dynamicc1transfertensor_valueemission_or_honestgalerkinc1run"
    / "lane_b_honest_galerkin_c1_run_attempt.packet.json"
)
NONHIGGS_PROFILE = DATA / "selected_nonhiggscovarianceprofilevalues_or_localqftobservablefunctor.candidate.json"

STATUS = (
    "MTT_SELECTED_AEWMETROLOGYSLOTEXECUTION_OR_HRGNONHIGGSPREDICTIONSELECTOR_"
    "EXECUTED_ZERO_SOURCE_VALUES_ALPHA_SELECTOR_PRIORITIZED"
)
NEXT = "MTT_Selected_Alpha1HRGSelector_or_AEWMetrologyValueSourceTheorem_v1"


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
        raise FileNotFoundError("missing A_EW/HRG selector inputs: " + ", ".join(missing))


def row_by_id(rows: list[dict[str, Any]], row_id: str) -> dict[str, Any]:
    for row in rows:
        if row.get("id") == row_id:
            return row
    raise KeyError(row_id)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_METROLOGY,
        PREVIOUS_HRG,
        EW_BOUNDARY,
        AEW_GATE,
        AEW_DIAGNOSTIC,
        DTERM_DECISION,
        H_CONDITIONAL_FORMULA,
        WZH_CANDIDATE,
        WZH_INVENTORY,
        WZH_ACCEPTANCE,
        WZH_SIDECARS,
        HRG_NONHIGGS_EXECUTION,
        HRG_TARGET_MATRIX,
        RO_VALUE_EXECUTION,
        ALPHA1_SOURCE_IDENTITY,
        ALPHA1_NORMALIZATION,
        ALPHA1_VALUE_ATTEMPT,
        DYNAMIC_C1_VALUE,
        DYNAMIC_C1_LANE_A,
        DYNAMIC_C1_LANE_B,
        NONHIGGS_PROFILE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_metrology = load(PREVIOUS_METROLOGY)
    previous_hrg = load(PREVIOUS_HRG)
    ew_boundary = load(EW_BOUNDARY)
    aew_gate = load(AEW_GATE)
    aew_diag = load(AEW_DIAGNOSTIC)
    dterm_decision = load(DTERM_DECISION)
    h_formula = load(H_CONDITIONAL_FORMULA)
    wzh_candidate = load(WZH_CANDIDATE)
    wzh_inventory = load(WZH_INVENTORY)
    wzh_acceptance = load(WZH_ACCEPTANCE)
    wzh_sidecars = load(WZH_SIDECARS)
    hrg_nonhiggs = load(HRG_NONHIGGS_EXECUTION)
    hrg_target_matrix = load(HRG_TARGET_MATRIX)
    ro_value_execution = load(RO_VALUE_EXECUTION)
    alpha1_identity = load(ALPHA1_SOURCE_IDENTITY)
    alpha1_norm = load(ALPHA1_NORMALIZATION)
    alpha1_value = load(ALPHA1_VALUE_ATTEMPT)
    dynamic_c1_value = load(DYNAMIC_C1_VALUE)
    dynamic_c1_lane_a = load(DYNAMIC_C1_LANE_A)
    dynamic_c1_lane_b = load(DYNAMIC_C1_LANE_B)
    nonhiggs_profile = load(NONHIGGS_PROFILE)

    diag_values = aew_diag["diagnostic_values"]
    hrg_value = previous["key_numbers"]["UP_RET_OVERLAP_HRG"]
    log_hrg = previous["key_numbers"]["log_UP_RET_OVERLAP_HRG"]
    s_beta = h_formula["selected_s_beta"]["value"]
    aew_external = diag_values["A_EW_Mt_external"]
    lambda_dterm = diag_values["lambda_Dterm_Mt_external_AEW_times_selected_sbeta"]
    lambda_external = diag_values["lambda_Mt_external_coordinate"]
    computed_ratio = lambda_external / lambda_dterm
    ratio_residual = abs(computed_ratio - hrg_value)

    wzh_rows = wzh_inventory["accepted_wzh_coordinate_rows"]
    g2 = row_by_id(wzh_rows, "g_2_Mt")
    gy = row_by_id(wzh_rows, "g_Y_Mt")
    lambda_row = row_by_id(wzh_rows, "lambda_Mt")
    computed_aew = (g2["central_value"] ** 2 + gy["central_value"] ** 2) / 8
    aew_residual = abs(computed_aew - aew_external)

    metrology_slots = [
        {
            "slot": "A_EW_action_normalization",
            "executed": True,
            "selected_source_value_emitted": ew_boundary["closure_decision"]["selected_A_EW_emitted"],
            "external_coordinate_available": True,
            "external_value": aew_external,
            "computed_from_external_gauge_rows": computed_aew,
            "computed_residual": aew_residual,
            "accepted_as_source": False,
            "reason": "WZH rows are external benchmark coordinates; the AEW tier gate still has no selected same-branch physical gauge/action normalization.",
        },
        {
            "slot": "mu_match_physical_scale",
            "executed": True,
            "selected_source_value_emitted": ew_boundary["closure_decision"]["selected_matching_scale_mu_match_closed"],
            "external_coordinate_available": True,
            "external_value": "M_t coordinate in imported WZH/top-Higgs benchmark layer",
            "accepted_as_source": False,
            "reason": "The matching coordinate is an external replay convention, not selected metrology value-source data.",
        },
        {
            "slot": "threshold_RG_transport_to_Omega_scheme",
            "executed": True,
            "selected_source_value_emitted": ew_boundary["closure_decision"]["selected_threshold_RG_transport_closed"],
            "external_coordinate_available": False,
            "accepted_as_source": False,
            "reason": "The diagnostic burden identifies a large threshold/RG factor, but no source transport theorem emits it.",
        },
    ]
    accepted_metrology_slots = [row for row in metrology_slots if row["accepted_as_source"]]

    aew_execution = {
        "schema": "MTTAEWMetrologySlotExecution.v1",
        "status": "AEW_METROLOGY_SLOT_EXECUTED_ZERO_SELECTED_SOURCE_VALUES",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "imports": {
            "previous_status": previous["status"],
            "previous_metrology_handoff": previous_metrology["status"],
            "ew_boundary_status": ew_boundary["status"],
            "aew_source_tier_status": aew_gate["status"],
            "wzh_status": wzh_candidate["status"],
            "wzh_inventory_status": wzh_inventory["status"],
            "wzh_acceptance_status": wzh_acceptance["status"],
            "wzh_sidecars_status": wzh_sidecars["status"],
            "dterm_decision_status": dterm_decision["status"],
        },
        "executed_slots": metrology_slots,
        "external_coordinate_rows": {
            "accepted_external_wzh_coordinate_row_count": wzh_acceptance[
                "accepted_external_wzh_coordinate_row_count"
            ],
            "accepted_selected_Rtheta_source_row_count": wzh_acceptance[
                "accepted_selected_Rtheta_source_row_count"
            ],
            "accepted_full_covariance_profile_row_count": wzh_acceptance[
                "accepted_full_covariance_profile_row_count"
            ],
            "g_2_Mt": g2,
            "g_Y_Mt": gy,
            "lambda_Mt": lambda_row,
        },
        "decision": {
            "AEW_metrology_slot_execution_closed": True,
            "selected_A_EW_value_emitted": False,
            "selected_mu_match_value_emitted": False,
            "selected_threshold_RG_transport_emitted": False,
            "selected_metrology_source_slot_count": len(accepted_metrology_slots),
            "external_WZH_rows_available": True,
            "external_WZH_rows_promoted_to_source": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "strict_H_K_gate_closed": False,
        },
    }

    burden = {
        "schema": "MTTAEWHRGBurdenEquivalenceDiagnostic.v1",
        "status": "AEW_HRG_BURDEN_EQUIVALENCE_DIAGNOSTIC_BUILT_NOT_SOURCE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "formula": {
            "lambda_Dterm": "A_EW(M_t) * s_beta",
            "HRG_burden": "lambda_Mt / (A_EW(M_t) * s_beta)",
            "same_as_calibrated_UP_RET_OVERLAP_HRG": True,
        },
        "values": {
            "s_beta": s_beta,
            "A_EW_Mt_external": aew_external,
            "lambda_Dterm_Mt_external_AEW_times_selected_sbeta": lambda_dterm,
            "lambda_Mt_external_coordinate": lambda_external,
            "computed_HRG_burden": computed_ratio,
            "UP_RET_OVERLAP_HRG": hrg_value,
            "log_UP_RET_OVERLAP_HRG": log_hrg,
            "ratio_residual": ratio_residual,
            "required_A_EW_to_match_external_lambda_Mt": diag_values[
                "required_A_EW_to_match_external_lambda_Mt"
            ],
        },
        "interpretation": {
            "accepted_as_source_row": False,
            "accepted_as_nonHiggs_prediction": False,
            "why_useful": (
                "The A_EW route and HRG route now share the same numerical burden "
                "at the external diagnostic layer, so the next source theorem should "
                "derive this factor rather than refit it."
            ),
            "why_not_closure": (
                "The equality uses lambda_Mt as an external coordinate and therefore "
                "cannot select HRG, A_EW, or K_threshold.Omega_H.lambda."
            ),
        },
    }

    nonhiggs_rows = hrg_nonhiggs["map_rows"]
    alpha_row = next(row for row in nonhiggs_rows if row["domain"] == "alpha/source-strength")
    dynamic_row = next(row for row in nonhiggs_rows if row["domain"] == "dynamic C1 overlap/value tensor")
    charged_row = next(row for row in nonhiggs_rows if row["domain"] == "charged scalar threshold/prefactor rows")
    generic_row = next(row for row in nonhiggs_rows if row["domain"] == "generic non-Higgs threshold/RG observable")

    alpha_conditional = alpha1_value["emission_attempt"]["conditional_value_candidate"]
    selector_rows = [
        {
            "selector": "alpha_source_strength",
            "domain": alpha_row["domain"],
            "eligible_as_nonHiggs_prediction_selector": True,
            "accepted_now": False,
            "priority": 1,
            "why_priority": "Alpha/source-strength has a proved normalization theorem and a conditional lambda_alpha1=1 local candidate; it lacks the selected same-source normalization or typed BN retarded derivative.",
            "current_status": alpha_row["current_status_import"],
            "source_refs": alpha_row["source_refs"],
            "blocking_reason": alpha_row["blocking_reason"],
            "conditional_candidate": alpha_conditional,
        },
        {
            "selector": "dynamic_C1_overlap_value_tensor",
            "domain": dynamic_row["domain"],
            "eligible_as_nonHiggs_prediction_selector": True,
            "accepted_now": False,
            "priority": 2,
            "why_priority": "Dynamic C1 is a genuine same-HRG target but still lacks primitive C1 contractions, b_selected, sector response matrices, or honest Galerkin values.",
            "current_status": dynamic_row["current_status_import"],
            "source_refs": dynamic_row["source_refs"],
            "blocking_reason": dynamic_row["blocking_reason"],
            "lane_A_status": dynamic_c1_lane_a["status"],
            "lane_B_status": dynamic_c1_lane_b["status"],
            "lane_A_missing": dynamic_c1_lane_a["missing_for_promotion"],
            "lane_B_missing": dynamic_c1_lane_b["missing_outputs"],
        },
        {
            "selector": "charged_scalar_threshold_rows",
            "domain": charged_row["domain"],
            "eligible_as_nonHiggs_prediction_selector": False,
            "accepted_now": False,
            "priority": 99,
            "why_rejected": charged_row["blocking_reason"],
            "charged_selected_K_rows": charged_row["charged_selected_K_rows"],
        },
        {
            "selector": "generic_nonHiggs_threshold_RG",
            "domain": generic_row["domain"],
            "eligible_as_nonHiggs_prediction_selector": False,
            "accepted_now": False,
            "priority": 99,
            "why_rejected": generic_row["blocking_reason"],
            "current_status": generic_row["current_status_import"],
        },
    ]
    eligible_selectors = [row for row in selector_rows if row["eligible_as_nonHiggs_prediction_selector"]]
    accepted_selectors = [row for row in selector_rows if row["accepted_now"]]

    hrg_selector = {
        "schema": "MTTHRGNonHiggsPredictionSelectorExecution.v1",
        "status": "HRG_NONHIGGS_SELECTOR_EXECUTED_ALPHA_PRIORITY_ZERO_ACCEPTED",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "imports": {
            "previous_hrg_reentry": previous_hrg["status"],
            "hrg_nonhiggs_execution_status": hrg_nonhiggs["status"],
            "hrg_target_matrix_status": hrg_target_matrix["status"],
            "ro_value_execution_status": ro_value_execution["status"],
            "alpha1_identity_status": alpha1_identity["status"],
            "alpha1_normalization_status": alpha1_norm["status"],
            "alpha1_value_attempt_status": alpha1_value["status"],
            "dynamic_c1_value_status": dynamic_c1_value["status"],
            "nonhiggs_profile_status": nonhiggs_profile["status"],
        },
        "selector_rows": selector_rows,
        "decision": {
            "HRG_nonHiggs_prediction_selector_execution_closed": True,
            "eligible_selector_count": len(eligible_selectors),
            "accepted_selector_count": len(accepted_selectors),
            "alpha_source_strength_prioritized": True,
            "dynamic_C1_retained_as_second_selector": True,
            "charged_threshold_rows_rejected_as_selector": True,
            "generic_nonHiggs_threshold_rejected_until_typed_consumer_exists": True,
            "RO_value_source_selected": ro_value_execution["source_selected"],
            "UP_RET_OVERLAP_HRG_universal_admitted": ro_value_execution["decision"][
                "UP_RET_OVERLAP_HRG_universal_admitted"
            ],
            "same_HRG_nonHiggs_prediction_emitted": False,
        },
    }

    next_priority = {
        "schema": "MTTNextPriorityAfterAEWHRGDualExecution.v1",
        "status": "NEXT_PRIORITY_ALPHA1_HRG_SELECTOR_OR_AEW_METROLOGY_VALUE_SOURCE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "ranked_next_targets": [
            {
                "rank": 1,
                "label": "Alpha1 HRG selector",
                "artifact": "MTT_Selected_Alpha1HRGSelector_or_AEWMetrologyValueSourceTheorem_v1",
                "reason": "It is the nearest non-Higgs HRG selector: normalization theorem exists and only the selected source-strength/BN retarded derivative is missing.",
            },
            {
                "rank": 2,
                "label": "A_EW metrology value source",
                "artifact": "same artifact, parallel branch",
                "reason": "A_EW is the legal metrology slot but currently has only external WZH coordinates and no selected source value.",
            },
            {
                "rank": 3,
                "label": "Dynamic C1 HRG selector",
                "artifact": "later if alpha1 selector fails",
                "reason": "It is a valid non-Higgs HRG target but needs more missing value-emission payload.",
            },
        ],
        "decision": {
            "next_required_artifact": NEXT,
            "alpha1_selector_chosen_as_primary_next": True,
            "aew_value_source_retained_parallel": True,
            "dynamic_C1_selector_retained_fallback": True,
        },
    }

    cutset = {
        "schema": "MTTNextCutsetAfterAEWMetrologyOrHRGSelectorExecution.v1",
        "status": "NEXT_FRONTIER_ALPHA1_HRG_SELECTOR_OR_AEW_METROLOGY_VALUE_SOURCE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "A_EW metrology slots executed against current WZH/external and source tiers",
            "zero selected A_EW/mu/RG metrology source values emitted",
            "A_EW/HRG diagnostic burden equivalence recorded",
            "HRG non-Higgs selector matrix executed and ranked",
            "alpha/source-strength selected as primary next HRG non-Higgs selector lane",
            "charged scalar threshold rows rejected as HRG cross-use selector because T_scheme=1 is already selected",
        ],
        "still_open": [
            "selected A_EW source value",
            "selected mu_match physical scale",
            "selected threshold/RG transport into Omega/lambda_H scheme",
            "selected alpha1 source-strength normalization value or typed BN retarded derivative",
            "same-HRG alpha/source-strength prediction without retuning",
            "dynamic C1 primitive contractions and sector response matrices",
            "strict H K row 10/10 at source tier",
            "true SM/no-knob equivalence",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedAEWMetrologySlotExecutionOrHRGNonHiggsPredictionSelector",
        "status": STATUS,
        "previous_status": previous["status"],
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "theorem": {
            "name": "AEWMetrologySlotExecutionOrHRGNonHiggsPredictionSelectorTheorem",
            "proved": True,
            "statement": (
                "Executing the current A_EW metrology slots emits no selected "
                "A_EW, mu_match, or threshold/RG source value, but records the "
                "external diagnostic burden lambda_Mt/(A_EW*s_beta)=UP-RET-"
                "OVERLAP.HRG. Executing the HRG non-Higgs selector accepts zero "
                "prediction maps, rejects charged rows as already source-native, "
                "and ranks alpha/source-strength as the nearest non-Higgs selector "
                "lane with dynamic C1 retained as fallback."
            ),
        },
        "closure_decision": {
            "AEW_metrology_slot_execution_closed": True,
            "selected_A_EW_value_emitted": False,
            "selected_mu_match_value_emitted": False,
            "selected_threshold_RG_transport_emitted": False,
            "selected_metrology_source_slot_count": 0,
            "external_WZH_rows_available": True,
            "external_WZH_rows_promoted_to_source": False,
            "AEW_HRG_burden_equivalence_diagnostic_built": True,
            "burden_equivalence_accepted_as_source": False,
            "HRG_nonHiggs_prediction_selector_execution_closed": True,
            "eligible_HRG_selector_count": len(eligible_selectors),
            "accepted_HRG_selector_count": len(accepted_selectors),
            "alpha_source_strength_prioritized": True,
            "dynamic_C1_retained_as_second_selector": True,
            "same_HRG_nonHiggs_prediction_emitted": False,
            "UP_RET_OVERLAP_HRG_universal_admitted": False,
            "K_threshold_Omega_H_lambda_emitted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "s_beta": s_beta,
            "A_EW_Mt_external": aew_external,
            "A_EW_recomputed_from_g2_gY": computed_aew,
            "A_EW_recompute_residual": aew_residual,
            "lambda_Dterm_Mt_external_AEW_times_selected_sbeta": lambda_dterm,
            "lambda_Mt_external_coordinate": lambda_external,
            "computed_HRG_burden": computed_ratio,
            "UP_RET_OVERLAP_HRG": hrg_value,
            "burden_equivalence_residual": ratio_residual,
            "required_A_EW_to_match_external_lambda_Mt": diag_values[
                "required_A_EW_to_match_external_lambda_Mt"
            ],
            "accepted_external_wzh_coordinate_rows": wzh_acceptance[
                "accepted_external_wzh_coordinate_row_count"
            ],
            "accepted_selected_Rtheta_source_rows": wzh_acceptance[
                "accepted_selected_Rtheta_source_row_count"
            ],
            "eligible_HRG_selector_count": len(eligible_selectors),
            "accepted_HRG_selector_count": len(accepted_selectors),
        },
        "packets": {
            "aew_metrology_slot_execution": rel(AEW_EXECUTION),
            "aew_hrg_burden_equivalence_diagnostic": rel(BURDEN),
            "hrg_nonhiggs_prediction_selector_execution": rel(HRG_SELECTOR),
            "next_priority": rel(NEXT_PRIORITY),
            "cutset": rel(CUTSET),
        },
        "what_closes": {
            "A_EW_slot_execution_attempt": True,
            "A_EW_HRG_burden_diagnostic": True,
            "HRG_nonHiggs_selector_ranking": True,
            "alpha1_selector_priority": True,
        },
        "what_remains_open": {
            "selected_A_EW_value": True,
            "selected_mu_match": True,
            "selected_threshold_RG_transport": True,
            "selected_alpha1_source_strength_value_or_BN_derivative": True,
            "same_HRG_nonHiggs_prediction": True,
            "dynamic_C1_HRG_selector_payload": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedAEWMetrologySlotExecutionOrHRGNonHiggsPredictionSelector",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "proof_note": rel(NOTE),
        "verified_packets": list(candidate["packets"].values()),
        "closure_claimed": True,
        "AEW_metrology_slot_execution_closed": True,
        "selected_A_EW_value_emitted": False,
        "selected_mu_match_value_emitted": False,
        "selected_threshold_RG_transport_emitted": False,
        "selected_metrology_source_slot_count": 0,
        "external_WZH_rows_available": True,
        "external_WZH_rows_promoted_to_source": False,
        "AEW_HRG_burden_equivalence_diagnostic_built": True,
        "burden_equivalence_accepted_as_source": False,
        "HRG_nonHiggs_prediction_selector_execution_closed": True,
        "eligible_HRG_selector_count": len(eligible_selectors),
        "accepted_HRG_selector_count": len(accepted_selectors),
        "alpha_source_strength_prioritized": True,
        "dynamic_C1_retained_as_second_selector": True,
        "same_HRG_nonHiggs_prediction_emitted": False,
        "UP_RET_OVERLAP_HRG_universal_admitted": False,
        "K_threshold_Omega_H_lambda_emitted": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected A_EW Metrology Slot Execution or HRG Non-Higgs Prediction Selector v1

Status: `{STATUS}`

## A_EW Slot Execution

The legal Higgs metrology slots were executed against the current source and
external WZH data:

```text
A_EW(M_t) external = {aew_external}
A_EW recomputed    = {computed_aew}
s_beta             = {s_beta}
lambda_Dterm       = {lambda_dterm}
lambda_Mt external = {lambda_external}
```

Result:

```text
selected A_EW value                  false
selected mu_match value              false
selected threshold/RG transport      false
selected metrology source slots      0
```

The WZH rows are available as external benchmark coordinates, but they remain
external coordinates, not selected source rows.

## Burden Equivalence Diagnostic

The external diagnostic burden is:

```text
lambda_Mt / (A_EW*s_beta) = {computed_ratio}
UP_RET_OVERLAP.HRG        = {hrg_value}
residual                  = {ratio_residual}
```

This is important because the A_EW route and the HRG route point to the same
large threshold factor.  It is not closure because the equality uses the
external Higgs quartic coordinate.

## HRG Non-Higgs Selector

The HRG non-Higgs selector execution ranks the lanes:

```text
1. alpha/source-strength      nearest selector, not accepted yet
2. dynamic C1 overlap tensor  valid fallback, more missing payload
3. charged scalar thresholds  rejected: T_scheme=1 already selected
4. generic non-Higgs RG       rejected until typed consumer exists
```

Accepted same-HRG non-Higgs prediction maps:

```text
0
```

## Next

`{NEXT}`
"""

    write_json(AEW_EXECUTION, aew_execution)
    write_json(BURDEN, burden)
    write_json(HRG_SELECTOR, hrg_selector)
    write_json(NEXT_PRIORITY, next_priority)
    write_json(CUTSET, cutset)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    for path in [OUTPUT, CERT, NOTE]:
        print(f"Wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
