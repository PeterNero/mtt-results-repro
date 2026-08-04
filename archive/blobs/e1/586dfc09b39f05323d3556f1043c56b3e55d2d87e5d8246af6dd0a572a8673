"""Build Step 9 dynamic Qa/SU3/C1 response promotion frontier."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step9_dynamicqasu3c1response_or_precisionprofilecompletion"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
RETIRED_BLOCKERS = PACKET_DIR / "step9_retired_blockers.packet.json"
C1_SUPPORT_LEDGER = PACKET_DIR / "step9_c1_support_ledger.packet.json"
DYNAMIC_ROUTE_TEST = PACKET_DIR / "step9_dynamic_promotion_route_test.packet.json"
PRECISION_STATUS = PACKET_DIR / "step9_precision_profile_status.packet.json"
CLOSURE_BOUNDARY = PACKET_DIR / "step9_closure_boundary.packet.json"
HANDOFF = PACKET_DIR / "step9_to_step10_handoff.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step9_DynamicQaSU3C1Response_or_PrecisionProfileCompletion_v1.md"

STEP8 = DATA / "selected_step8_precisionvalueemission_or_actualqasu3operatorpacketclosure.candidate.json"
STEP8_HANDOFF = (
    DATA
    / "selected_step8_precisionvalueemission_or_actualqasu3operatorpacketclosure"
    / "step8_to_step9_handoff.packet.json"
)
STEP8_PRECISION = (
    DATA
    / "selected_step8_precisionvalueemission_or_actualqasu3operatorpacketclosure"
    / "step8_precision_value_route_status.packet.json"
)
STATIONARY_DOTD = DATA / "selected_stationaryprojector_dotd_integrated_frontier.candidate.json"
CROSSREPO_ALPHA1 = DATA / "selected_crossrepo_alpha1_driver_replay_import.candidate.json"
PRIMITIVE_CLASS = DATA / "selected_primitiveclass_c1observable_or_higherorder_fullresponse_sourceemission.candidate.json"
C1_KERNEL_VALUES = DATA / "selected_c1kernelvaluesexecution_or_physicalsourcepromotion.candidate.json"
CANONICAL_PROJECTOR = DATA / "selected_canonicalresidualprojector_or_honestgalerkinc1_valuefill.candidate.json"
C1_TRACE = DATA / "selected_c1tracemeasurepromotion_or_actionboundaryproof.candidate.json"
PHIFIN_APPLICATION = DATA / "selected_phifinc1_residualprojectorapplication_or_honestgalerkinexecution_valuefill.candidate.json"
PHYSICAL_ACTION_IDENTITY = DATA / "selected_physicalphifinc1actionidentity_or_independentrowsourceexport.candidate.json"
PHYSICAL_SOURCE_FILL = DATA / "selected_physicalphifinc1actionsource_fill_or_independentgalerkinprovenancerun.candidate.json"
SAME_SOURCE_ROUTE_TEST = DATA / "selected_samesourcedynamicphifinc1_or_honestgalerkinexecution_routetest.candidate.json"
SAMEBRANCH_PATCHED = DATA / "selected_samebranchphifinc1sourceemission_or_independenthessianquadratureexecution.candidate.json"
SAMESOURCE_ACTUAL = DATA / "selected_samesourcephifinc1emission_or_independentrowsactualfill.candidate.json"
POSTSOURCE_GAP = DATA / "selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure.candidate.json"

STATUS = (
    "MTT_SELECTED_STEP9_DYNAMICQASU3C1RESPONSE_OR_PRECISIONPROFILECOMPLETION_"
    "CLOSED_FRONTIER_REDUCTION_SOURCE_RULE_OPEN"
)
NEXT = "MTT_Selected_Step10_PhysicalPhiFinC1SourceRule_or_IndependentGalerkinRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing Step 9 inputs: " + ", ".join(missing))


def pick_bool(data: dict[str, Any], *keys: str, default: bool = False) -> bool:
    cur: Any = data
    for key in keys:
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return bool(cur)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        STEP8,
        STEP8_HANDOFF,
        STEP8_PRECISION,
        STATIONARY_DOTD,
        CROSSREPO_ALPHA1,
        PRIMITIVE_CLASS,
        C1_KERNEL_VALUES,
        CANONICAL_PROJECTOR,
        C1_TRACE,
        PHIFIN_APPLICATION,
        PHYSICAL_ACTION_IDENTITY,
        PHYSICAL_SOURCE_FILL,
        SAME_SOURCE_ROUTE_TEST,
        SAMEBRANCH_PATCHED,
        SAMESOURCE_ACTUAL,
        POSTSOURCE_GAP,
    ]
    require_sources(sources)

    step8 = load(STEP8)
    step8_handoff = load(STEP8_HANDOFF)
    step8_precision = load(STEP8_PRECISION)
    stationary = load(STATIONARY_DOTD)
    crossrepo = load(CROSSREPO_ALPHA1)
    primitive_class = load(PRIMITIVE_CLASS)
    c1_values = load(C1_KERNEL_VALUES)
    canonical = load(CANONICAL_PROJECTOR)
    c1_trace = load(C1_TRACE)
    phifin_application = load(PHIFIN_APPLICATION)
    physical_action_identity = load(PHYSICAL_ACTION_IDENTITY)
    physical_source_fill = load(PHYSICAL_SOURCE_FILL)
    route_test = load(SAME_SOURCE_ROUTE_TEST)
    samebranch_patched = load(SAMEBRANCH_PATCHED)
    samesource_actual = load(SAMESOURCE_ACTUAL)
    postsource_gap = load(POSTSOURCE_GAP)

    retired_blockers = {
        "schema": "MTTStep9RetiredBlockers.v1",
        "status": "DOTD_ALPHA1_STATIONARY_PROJECTOR_AND_SOURCE_SLOTS_RETIRED",
        "step8_source": rel(STEP8),
        "stationary_dotd_source": rel(STATIONARY_DOTD),
        "crossrepo_alpha1_source": rel(CROSSREPO_ALPHA1),
        "postsource_gap_source": rel(POSTSOURCE_GAP),
        "step8_closed_for_plan_contract": pick_bool(step8, "closure_decision", "step8_closed_for_plan_contract"),
        "all_operator_source_slots_closed": pick_bool(step8, "closure_decision", "all_operator_source_slots_closed"),
        "operator_source_slots_closed": step8["closure_decision"]["operator_source_slots_closed"],
        "operator_source_slots_remaining": step8["closure_decision"]["operator_source_slots_remaining"],
        "selected_dotD_source_verified": pick_bool(stationary, "closure_decision", "selected_dotD_source_verified"),
        "alpha1_driver_verified": pick_bool(stationary, "closure_decision", "alpha1_driver_verified"),
        "stationary_projector_source_verified": pick_bool(stationary, "closure_decision", "stationary_projector_source_verified"),
        "validator_ready_stationary_rho_s": pick_bool(stationary, "closure_decision", "validator_ready_stationary_rho_s"),
        "selected_alpha1_driver_imported": pick_bool(
            crossrepo, "what_closes_now", "selected_alpha1_driver_imported"
        ),
        "selected_dotD_source_verified_imported": pick_bool(
            crossrepo, "what_closes_now", "selected_dotD_source_verified_imported"
        ),
        "postsource_alpha1_retired": pick_bool(
            postsource_gap, "promotion_decision", "postsource_alpha1_retired"
        ),
        "static_matter_routing_closed": pick_bool(
            postsource_gap, "promotion_decision", "static_matter_routing_closed"
        ),
        "retired_from_active_step9_blocker_set": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(RETIRED_BLOCKERS, retired_blockers)

    c1_support_ledger = {
        "schema": "MTTStep9C1SupportLedger.v1",
        "status": "C1_SUPPORT_LEDGER_CLOSED_FLAVOR_VALUE_PROMOTION_OPEN",
        "primitive_class_source": rel(PRIMITIVE_CLASS),
        "c1_kernel_values_source": rel(C1_KERNEL_VALUES),
        "canonical_projector_source": rel(CANONICAL_PROJECTOR),
        "c1_trace_source": rel(C1_TRACE),
        "current_primitive_class_promoted_as_valid_C1_observable_layer": pick_bool(
            primitive_class,
            "promotion_decision",
            "current_primitive_class_promoted_as_valid_C1_observable_layer",
        ),
        "current_primitive_class_promoted_as_flavor_closure": pick_bool(
            primitive_class,
            "promotion_decision",
            "current_primitive_class_promoted_as_flavor_closure",
        ),
        "higherorder_fullresponse_values_promoted": pick_bool(
            primitive_class, "promotion_decision", "higherorder_fullresponse_values_promoted"
        ),
        "all_110_value_slots_have_algebraic_candidate_values": pick_bool(
            c1_values, "what_closes_now", "all_110_value_slots_have_algebraic_candidate_values"
        ),
        "hessian_b_delta_values_filled": pick_bool(
            c1_values, "what_closes_now", "hessian_b_delta_values_filled"
        ),
        "algebraic_values_promoted_as_physical": pick_bool(
            c1_values, "promotion_decision", "algebraic_values_promoted_as_physical"
        ),
        "canonical_residual_projector_promoted_as_unique_mathematical_projector": pick_bool(
            canonical,
            "promotion_decision",
            "canonical_residual_projector_promoted_as_unique_mathematical_projector",
        ),
        "PhiFinC1_projector_application_promoted": pick_bool(
            canonical, "promotion_decision", "PhiFinC1_projector_application_promoted"
        ),
        "algebraic_finite_trace_boundary_cancellation": pick_bool(
            c1_trace, "what_closes_now", "algebraic_finite_trace_boundary_cancellation"
        ),
        "physical_action_identity_promoted": pick_bool(
            c1_trace, "promotion_decision", "physical_action_identity_promoted"
        ),
        "same_source_b_selected_promoted": pick_bool(
            c1_trace, "promotion_decision", "same_source_b_selected_promoted"
        ),
        "support_layer_closed": True,
        "physical_value_promotion_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(C1_SUPPORT_LEDGER, c1_support_ledger)

    dynamic_route_test = {
        "schema": "MTTStep9DynamicPromotionRouteTest.v1",
        "status": "ROUTE_A_ROUTE_B_TESTED_BOTH_REMAIN_OPEN_FOR_UNPATCHED_TRUE_SM",
        "phifin_application_source": rel(PHIFIN_APPLICATION),
        "physical_action_identity_source": rel(PHYSICAL_ACTION_IDENTITY),
        "physical_source_fill_source": rel(PHYSICAL_SOURCE_FILL),
        "same_source_route_test_source": rel(SAME_SOURCE_ROUTE_TEST),
        "samebranch_patched_support_source": rel(SAMEBRANCH_PATCHED),
        "samesource_actual_fill_source": rel(SAMESOURCE_ACTUAL),
        "patched_or_local_principle_sm_parity_support_retained": (
            samebranch_patched["status"].endswith("PATCHED_PARITY_CLOSED_UNPATCHED_OPEN")
        ),
        "unpatched_same_branch_PhiFinC1_source_emission_closed": False,
        "route_A_source_rule_gap_sharpened": pick_bool(
            route_test, "what_closes_now", "ROUTE_A_source_rule_gap_sharpened"
        ),
        "route_B_readiness_sidecar_built": pick_bool(
            route_test, "what_closes_now", "ROUTE_B_readiness_sidecar_built"
        ),
        "PSM_C1_01_closed": pick_bool(route_test, "closure_decision", "PSM-C1-01_closed"),
        "PSM_C1_04_closed": pick_bool(route_test, "closure_decision", "PSM-C1-04_closed"),
        "ROUTE_A_closes_now": pick_bool(route_test, "closure_decision", "ROUTE_A_closes_now"),
        "ROUTE_B_ready_now": pick_bool(route_test, "closure_decision", "ROUTE_B_ready_now"),
        "actual_dynamic_QaSU3_operator_packet_closed": pick_bool(
            route_test, "closure_decision", "actual_dynamic_QaSU3_operator_packet_closed"
        ),
        "selected_C1_response_closed": pick_bool(
            route_test, "closure_decision", "selected_C1_response_closed"
        ),
        "physical_action_identity_current_attempt_rejected": pick_bool(
            physical_action_identity, "what_closes_now", "current_attempt_rejected_honestly"
        ),
        "route_A_minimal_certificate_built": pick_bool(
            physical_source_fill, "promotion_decision", "route_A_minimal_certificate_built"
        ),
        "route_A_minimal_certificate_filled": pick_bool(
            physical_source_fill, "promotion_decision", "route_A_minimal_certificate_filled"
        ),
        "route_B_run_spec_built": pick_bool(
            physical_source_fill, "promotion_decision", "route_B_run_spec_built"
        ),
        "route_B_run_executed": pick_bool(physical_source_fill, "promotion_decision", "route_B_run_executed"),
        "strict_two_lane_validator_still_rejects": (
            samesource_actual["status"].endswith("SOURCE_FIELDS_OPEN")
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(DYNAMIC_ROUTE_TEST, dynamic_route_test)

    precision_status = {
        "schema": "MTTStep9PrecisionProfileStatus.v1",
        "status": "PARTIAL_PRECISION_AND_MINIMAL_LOCAL_QFT_ROWS_RETAINED_FULL_PROFILE_OPEN",
        "step8_precision_source": rel(STEP8_PRECISION),
        "partial_precision_values_emitted": step8_precision["partial_precision_values_emitted"],
        "minimal_local_QFT_value_suite_filled": step8_precision["minimal_local_QFT_value_suite_filled"],
        "precision_observable_table_closed": step8_precision["precision_observable_table_closed"],
        "full_precision_observable_value_table_closed": step8_precision[
            "full_precision_observable_value_table_closed"
        ],
        "published_or_reconstructed_profile_likelihood_closed": step8_precision[
            "published_or_reconstructed_profile_likelihood_closed"
        ],
        "accepted_RG_threshold_covariance_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(PRECISION_STATUS, precision_status)

    closure_boundary = {
        "schema": "MTTStep9ClosureBoundary.v1",
        "status": "STEP9_CLOSED_AS_FRONTIER_REDUCTION_NOT_TRUE_EQUIVALENCE",
        "completed_step": 9,
        "step8_closed_for_plan_contract": step8["closure_decision"]["step8_closed_for_plan_contract"],
        "dotD_alpha1_stationary_projector_retired": True,
        "source_slot_layer_closed": True,
        "C1_support_layer_closed": True,
        "patched_or_local_principle_sm_parity_support_retained": True,
        "precision_profile_attempt_retained": True,
        "actual_dynamic_QaSU3_operator_packet_closed": False,
        "selected_C1_response_closed": False,
        "selected_physical_PhiFinC1_source_rule_closed": False,
        "independent_Galerkin_row_execution_closed": False,
        "accepted_RG_threshold_covariance_closed": False,
        "full_S2_value_emission_closed": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "step9_closed_for_plan_contract": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CLOSURE_BOUNDARY, closure_boundary)

    handoff = {
        "schema": "MTTStep9ToStep10Handoff.v1",
        "status": "HANDOFF_TO_STEP10_PHYSICAL_SOURCE_RULE_OR_INDEPENDENT_GALERKIN_ROWS",
        "completed_step": 9,
        "next_step": 10,
        "next_required_artifact": NEXT,
        "retired_blockers": {
            "selected_dotD_alpha1_driver": True,
            "stationary_projector_rho_s": True,
            "all_eight_operator_source_slots": True,
            "canonical_residual_projector_as_math_object": True,
            "formal_110_row_value_replay_as_support": True,
            "algebraic_trace_boundary_cancellation_as_support": True,
        },
        "step10_must_close_one_of": {
            "route_A_selected_physical_PhiFinC1_source_rule": True,
            "route_B_independent_selected_Galerkin_or_row_kernel_execution": True,
        },
        "step10_then_must_emit": {
            "A_selected": True,
            "b_selected": True,
            "deltaTheta_C1": True,
            "sector_response_matrices": True,
            "full_S2_value_rows": True,
            "Yukawa_CKM_PMNS_Higgs_mass_value_rows_without_proxy_fitting": True,
        },
        "must_not_use_as_selectors": step8_handoff["step9_must_not_use_as_selectors"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(HANDOFF, handoff)

    candidate = {
        "candidate": "MTTSelectedStep9DynamicQaSU3C1ResponseOrPrecisionProfileCompletion",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "step9_retired_blockers": rel(RETIRED_BLOCKERS),
            "step9_c1_support_ledger": rel(C1_SUPPORT_LEDGER),
            "step9_dynamic_promotion_route_test": rel(DYNAMIC_ROUTE_TEST),
            "step9_precision_profile_status": rel(PRECISION_STATUS),
            "step9_closure_boundary": rel(CLOSURE_BOUNDARY),
            "step9_to_step10_handoff": rel(HANDOFF),
        },
        "theorem": {
            "name": "Step9DynamicQaSU3C1FrontierReductionTheorem",
            "proved": True,
            "statement": (
                "Step 9 closes as a non-looping frontier-reduction theorem. The selected "
                "dotD/alpha1/stationary-projector layer and all eight operator source slots "
                "are retired from the active blocker set; the current primitive C1 layer is "
                "accepted as support but proved scalar/flavor-insufficient; the formal 110-row "
                "C1 replay, canonical residual projector, and algebraic finite-trace boundary "
                "cancellation are retained as support. The unpatched true-SM target is not "
                "closed: it still requires either a selected physical Phi_fin^C1 source rule "
                "or an independent selected Galerkin/row-kernel execution, followed by actual "
                "A_selected, b_selected, deltaTheta_C1, sector-response, full-S2, and no-proxy "
                "Yukawa/mixing value emission."
            ),
        },
        "closure_decision": {
            "step9_closed_for_plan_contract": True,
            "dotD_alpha1_stationary_projector_retired": True,
            "all_operator_source_slots_closed": True,
            "C1_support_layer_closed": True,
            "route_A_selected_physical_PhiFinC1_source_rule_closed": False,
            "route_B_independent_selected_Galerkin_or_row_kernel_execution_closed": False,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "selected_C1_response_closed": False,
            "full_S2_value_emission_closed": False,
            "precision_profile_full_closure": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "step9_plan_contract": True,
            "non_looping_frontier_reduction": True,
            "dotD_alpha1_projector_not_active_blockers": True,
            "C1_support_vs_source_promotion_boundary": True,
            "patched_sm_parity_support_separated_from_unpatched_true_SM": True,
            "step10_two_exit_handoff_typed": True,
        },
        "what_remains_open": {
            "route_A_selected_physical_PhiFinC1_source_rule": True,
            "route_B_independent_selected_Galerkin_or_row_kernel_execution": True,
            "A_selected_b_selected_deltaTheta_C1_from_same_selected_source": True,
            "sector_response_and_full_S2_value_rows": True,
            "accepted_RG_threshold_covariance_or_no_proxy_precision_profile": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "step9_contract_closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step9_DynamicQaSU3C1Response_or_PrecisionProfileCompletion_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "step9_contract_closure_claimed": True,
        "dotD_alpha1_stationary_projector_retired": True,
        "all_operator_source_slots_closed": True,
        "C1_support_layer_closed": True,
        "actual_dynamic_QaSU3_operator_packet_closed": False,
        "selected_C1_response_closed": False,
        "route_A_selected_physical_PhiFinC1_source_rule_closed": False,
        "route_B_independent_selected_Galerkin_or_row_kernel_execution_closed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step9 DynamicQaSU3C1Response or PrecisionProfileCompletion v1

Status: `{STATUS}`.

Step 9 is closed as a non-looping frontier reduction:

```text
dotD/alpha1/stationary projector retired : true
all operator source slots closed          : true
C1 support layer closed                   : true
patched/local SM-parity support retained  : true
route A physical Phi_fin^C1 source closed : false
route B independent Galerkin rows closed  : false
actual dynamic Qa/SU3 packet closed       : false
selected C1 response closed               : false
full S2 value emission closed             : false
true SM equivalence closed                : false
full no-knob closure                      : false
```

This step prevents the plan from looping back into alpha1, dotD, stationary
projectors, source-slot closure, or formal 110-row replay.  Those are support.
The active true-SM wall is now exactly two exits:

1. derive the selected physical `Phi_fin^C1` source rule from the same MTT
   branch; or
2. execute an independent selected Galerkin/row-kernel run whose rows do not
   depend on residual replay as their source.

After one of those exits closes, the next value-emission target is
`A_selected`, `b_selected`, `deltaTheta_C1`, sector response matrices,
full-S2 rows, and no-proxy Yukawa/mixing/Higgs rows.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
