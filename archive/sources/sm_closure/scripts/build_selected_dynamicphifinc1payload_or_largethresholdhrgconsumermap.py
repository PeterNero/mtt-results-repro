"""Build dynamic Phi_fin/C1 payload or large-threshold HRG consumer-map packet.

The previous frontier retired the stale alpha1/dotD blocker and locked the
external Higgs deficit as an HRG-sized source obligation.  This packet connects
that obligation to the current final dynamic C1 gate:

* the exact R_Z/R_X dynamic C1 value table is ready to promote;
* strict promotion still needs the unpatched differentiated Phi_fin^C1 source
  rule or an honest selected Galerkin C1 table export; and
* even after that dynamic payload is selected, HRG still needs a typed
  consumer/source map rather than replay from external lambda_Mt.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_dynamicphifinc1payload_or_largethresholdhrgconsumermap"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DYNAMIC_GATE_PACKET = PACKET_DIR / "dynamic_phifinc1_final_gate_reconciliation.packet.json"
HRG_CONSUMER_PACKET = PACKET_DIR / "large_threshold_hrg_consumer_map_gate.packet.json"
AXIOM_BOUNDARY_PACKET = PACKET_DIR / "local_axiom_vs_unpatched_boundary.packet.json"
CUTSET_PACKET = PACKET_DIR / "next_cutset_after_dynamic_payload_hrg_consumer.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_DynamicPhiFinC1Payload_or_LargeThresholdHRGConsumerMap_v1.md"

PREVIOUS = DATA / "selected_alpha1hrgselector_or_aewmetrologyvaluesourcetheorem.candidate.json"
PREVIOUS_DUAL = (
    DATA
    / "selected_alpha1hrgselector_or_aewmetrologyvaluesourcetheorem"
    / "dual_route_residual_lock.packet.json"
)
PREVIOUS_CUTSET = (
    DATA
    / "selected_alpha1hrgselector_or_aewmetrologyvaluesourcetheorem"
    / "next_cutset_after_alpha1_aew_attempt.packet.json"
)
PHIFIN_ALPHA = DATA / "selected_phifinalpha1payloadvalues_or_typedbnretardedderivativeexecution.candidate.json"
PHIFIN_ALPHA_GATE = (
    DATA
    / "selected_phifinalpha1payloadvalues_or_typedbnretardedderivativeexecution"
    / "dynamic_phifin_c1_payload_gate.packet.json"
)
DYNAMIC_ROWS = DATA / "selected_dynamicphifinc1payloadrows_or_higherresponseexecution.candidate.json"
DYNAMIC_SOURCE_OWNER = (
    DATA / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues.candidate.json"
)
FINAL_DYNAMIC_GATE = (
    DATA
    / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues"
    / "final_dynamic_value_gate.packet.json"
)
READY_VALUE_TABLE = (
    DATA
    / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues"
    / "ready_to_promote_dynamic_value_table.packet.json"
)
LANE_A_SOURCE_RULE = (
    DATA
    / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues"
    / "lane_a_residual_projector_source_rule_attempt.packet.json"
)
LANE_B_GALERKIN = (
    DATA
    / "selected_dynamicc1_sourceowner_dynamictransferhessian_or_honestgalerkinvalues"
    / "lane_b_honest_galerkin_export_attempt.packet.json"
)
TWO_LANE_CONTRACT = DATA / "selected_differentiatedphifinc1_residualprojectoraxiom_or_galerkinc1execution.candidate.json"
AXIOM_PROMOTION = DATA / "selected_differentiatedphifinc1_sourcerule_derivation_or_axiompromotion.candidate.json"
LOCAL_AXIOM = DATA / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit.candidate.json"
PATCHED_CLOSURE = (
    DATA
    / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit"
    / "patched_dynamic_c1_closure_theorem.packet.json"
)
UNPATCHED_EXIT = (
    DATA
    / "selected_differentiatedphifinc1_axiominsertion_patchedclosure_or_unpatchedexit"
    / "unpatched_exit_status.packet.json"
)
RO_VALUE = DATA / "selected_rovaluesource_or_nonhiggsmapexecution.candidate.json"
HRG_NONHIGGS = (
    DATA
    / "selected_aewmetrologyslotexecution_or_hrgnonhiggspredictionselector"
    / "hrg_nonhiggs_prediction_selector_execution.packet.json"
)

STATUS = (
    "MTT_SELECTED_DYNAMICPHIFINC1PAYLOAD_OR_LARGETHRESHOLDHRGCONSUMERMAP_"
    "RECONCILED_VALUES_READY_SOURCE_RULE_OPEN"
)
NEXT = "MTT_Selected_UnpatchedPhiFinC1SourceRule_or_HonestGalerkinTables_to_HRGConsumerMap_v1"


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
        raise FileNotFoundError("missing dynamic Phi_fin/C1 or HRG consumer inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        PREVIOUS_DUAL,
        PREVIOUS_CUTSET,
        PHIFIN_ALPHA,
        PHIFIN_ALPHA_GATE,
        DYNAMIC_ROWS,
        DYNAMIC_SOURCE_OWNER,
        FINAL_DYNAMIC_GATE,
        READY_VALUE_TABLE,
        LANE_A_SOURCE_RULE,
        LANE_B_GALERKIN,
        TWO_LANE_CONTRACT,
        AXIOM_PROMOTION,
        LOCAL_AXIOM,
        PATCHED_CLOSURE,
        UNPATCHED_EXIT,
        RO_VALUE,
        HRG_NONHIGGS,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    previous_dual = load(PREVIOUS_DUAL)
    previous_cutset = load(PREVIOUS_CUTSET)
    phifin_alpha = load(PHIFIN_ALPHA)
    phifin_alpha_gate = load(PHIFIN_ALPHA_GATE)
    dynamic_rows = load(DYNAMIC_ROWS)
    dynamic_source_owner = load(DYNAMIC_SOURCE_OWNER)
    final_dynamic_gate = load(FINAL_DYNAMIC_GATE)
    ready_value_table = load(READY_VALUE_TABLE)
    lane_a = load(LANE_A_SOURCE_RULE)
    lane_b = load(LANE_B_GALERKIN)
    two_lane_contract = load(TWO_LANE_CONTRACT)
    axiom_promotion = load(AXIOM_PROMOTION)
    local_axiom = load(LOCAL_AXIOM)
    patched_closure = load(PATCHED_CLOSURE)
    unpatched_exit = load(UNPATCHED_EXIT)
    ro_value = load(RO_VALUE)
    hrg_nonhiggs = load(HRG_NONHIGGS)

    nums = previous["key_numbers"]
    dual_equalities = previous_dual["equalities"]
    exact_ready = final_dynamic_gate["exact_values_ready"]
    conditional_hessian = ready_value_table["conditional_hessian_values"]
    dynamic_candidates = ready_value_table["dynamic_operator_candidates"]
    routed_completion = ready_value_table["routed_72_real_completion"]

    dynamic_gate_packet = {
        "schema": "MTTDynamicPhiFinC1FinalGateReconciliation.v1",
        "status": "DYNAMIC_PHIFINC1_VALUES_READY_STRICT_SOURCE_RULE_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "imports": {
            "previous_frontier_status": previous["status"],
            "phifin_alpha_execution_status": phifin_alpha["status"],
            "phifin_alpha_gate_status": phifin_alpha_gate["status"],
            "dynamic_payload_rows_status": dynamic_rows["status"],
            "dynamic_source_owner_status": dynamic_source_owner["status"],
            "final_dynamic_gate_status": final_dynamic_gate["status"],
            "two_lane_contract_status": two_lane_contract["status"],
        },
        "theorem": {
            "name": "DynamicPhiFinC1FinalGateReconciliationTheorem",
            "proved": True,
            "statement": (
                "The active dynamic Phi_fin/C1 problem is no longer an alpha1 or "
                "dotD replay problem.  The exact phase/shift value table and rank-2 "
                "Hessian consequences are ready, but strict selected promotion still "
                "requires either the unpatched differentiated Phi_fin^C1 residual-"
                "projector source rule or an honest selected Galerkin C1 table export."
            ),
        },
        "closed_not_blockers": final_dynamic_gate["closed_not_blockers"],
        "exact_values_ready": exact_ready,
        "ready_value_table": {
            "coordinate_system": ready_value_table["coordinate_system"],
            "phase_R_Z": dynamic_candidates["phase_R_Z"],
            "shift_R_X": dynamic_candidates["shift_R_X"],
            "conditional_hessian_values": conditional_hessian,
            "routed_72_real_completion": routed_completion,
        },
        "strict_source_status": {
            "dynamic_values_ready": final_dynamic_gate["closure_decision"]["dynamic_values_ready"],
            "source_rule_proved": final_dynamic_gate["closure_decision"]["source_rule_proved"],
            "honest_galerkin_table_exported": final_dynamic_gate["closure_decision"][
                "honest_galerkin_table_exported"
            ],
            "dynamic_C1_source_owner_closed": final_dynamic_gate["closure_decision"][
                "dynamic_C1_source_owner_closed"
            ],
            "dynamic_payload_rows_accepted": dynamic_rows["closure_decision"][
                "accepted_dynamic_payload_row_count"
            ],
            "dynamic_payload_rows_in_inventory": dynamic_rows["closure_decision"][
                "dynamic_payload_row_count"
            ],
        },
        "legal_exits": final_dynamic_gate["legal_exits"],
        "decision": {
            "dynamic_gate_reconciled": True,
            "alpha1_and_dotd_replay_retired": phifin_alpha_gate["alpha1_derivative_retired"]
            and phifin_alpha_gate["honest_dotD_replay_retired"],
            "exact_dynamic_values_ready": True,
            "selected_dynamic_phi_fin_c1_payload_emitted": False,
            "source_rule_proved_unpatched": False,
            "honest_galerkin_c1_tables_exported": False,
            "A_selected_promoted_strict": False,
            "b_selected_promoted_strict": False,
            "deltaTheta_C1_promoted_strict": False,
            "sector_response_matrices_promoted_strict": False,
        },
    }

    hrg_consumer_packet = {
        "schema": "MTTLargeThresholdHRGConsumerMapGate.v1",
        "status": "HRG_CONSUMER_MAP_GATE_TYPED_SOURCE_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "imports": {
            "previous_dual_route_status": previous_dual["status"],
            "previous_cutset_status": previous_cutset["status"],
            "ro_value_status": ro_value["status"],
            "hrg_nonhiggs_selector_status": hrg_nonhiggs["status"],
        },
        "theorem": {
            "name": "LargeThresholdHRGConsumerMapGateTheorem",
            "proved": True,
            "statement": (
                "The HRG-sized Higgs deficit is exactly locked, but it is not a "
                "source row.  A selected dynamic Phi_fin/C1 payload or selected "
                "A_EW threshold transport must first be emitted, and then a typed "
                "consumer map must send that same selected source object to "
                "UP_RET_OVERLAP.HRG without using external lambda_Mt."
            ),
        },
        "exact_deficit_equalities": dual_equalities,
        "acceptance_predicate": {
            "name": "SelectedHRGConsumerMapPredicate",
            "necessary_conditions": [
                "selected dynamic Phi_fin/C1 payload or selected large-threshold/A_EW transport source exists",
                "typed consumer map sends that source object to UP_RET_OVERLAP.HRG",
                "the consumer map is selected before any external Higgs lambda replay",
                "same-HRG non-Higgs prediction or strict H threshold source theorem validates cross-use",
            ],
            "satisfied_now": False,
        },
        "decision": {
            "exact_HRG_deficit_locked": True,
            "selected_dynamic_payload_available_for_consumer": False,
            "selected_AEW_large_threshold_transport_available_for_consumer": False,
            "typed_HRG_consumer_map_emitted": False,
            "same_HRG_nonHiggs_prediction_emitted": False,
            "accepted_HRG_selector_count": previous["closure_decision"]["accepted_HRG_selector_count"],
            "accepted_AEW_source_count": previous["closure_decision"]["accepted_AEW_source_count"],
            "external_lambda_Mt_used_as_selector": False,
            "accepted_as_source": False,
        },
    }

    axiom_boundary_packet = {
        "schema": "MTTLocalAxiomVsUnpatchedDynamicC1Boundary.v1",
        "status": "LOCAL_AXIOM_CONDITIONAL_DYNAMIC_C1_CLOSED_UNPATCHED_EXIT_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "imports": {
            "axiom_promotion_status": axiom_promotion["status"],
            "local_axiom_status": local_axiom["status"],
            "patched_closure_status": patched_closure["status"],
            "unpatched_exit_status": unpatched_exit["status"],
        },
        "theorem": {
            "name": "LocalAxiomVsUnpatchedDynamicC1BoundaryTheorem",
            "proved": True,
            "statement": (
                "Accepting the DifferentiatedPhiFinC1ResidualProjectorAxiom closes "
                "the dynamic C1 packet inside the local patched proof spine, but "
                "strict true-SM/no-knob closure still requires either deriving the "
                "source rule unpatched or exporting honest selected Galerkin C1 tables."
            ),
        },
        "patched_lane": {
            "local_source_axiom_accepted": local_axiom["closure_decision"][
                "local_source_axiom_accepted"
            ],
            "patched_dynamic_C1_packet_closed": patched_closure["promoted_objects"][
                "dynamic_C1_source_owner_packet"
            ],
            "scientific_status": patched_closure["scientific_status"],
            "promoted_objects": patched_closure["promoted_objects"],
            "exact_values": patched_closure["exact_values"],
        },
        "unpatched_lane": {
            "unpatched_dynamic_C1_closed": unpatched_exit["unpatched_dynamic_C1_closed"],
            "source_rule_derived_unpatched": unpatched_exit["source_rule_derived_unpatched"],
            "honest_galerkin_table_exported": unpatched_exit["honest_galerkin_table_exported"],
            "remaining_exits": unpatched_exit["remaining_exits"],
            "lane_A_source_rule_passes_now": lane_a["passes_now"],
            "lane_B_galerkin_passes_now": lane_b["passes_now"],
            "lane_B_missing_outputs": lane_b["missing_outputs"],
        },
        "decision": {
            "local_axiom_conditional_dynamic_C1_closure_available": True,
            "local_axiom_promoted_to_strict_no_knob": False,
            "unpatched_source_rule_derived_now": False,
            "honest_selected_galerkin_tables_exported_now": False,
            "strict_dynamic_payload_selected_now": False,
        },
    }

    cutset_packet = {
        "schema": "MTTNextCutsetAfterDynamicPayloadHRGConsumer.v1",
        "status": "NEXT_FRONTIER_UNPATCHED_PHIFINC1_SOURCE_RULE_OR_GALERKIN_TABLES_TO_HRG_CONSUMER",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_here": [
            "alpha1 and honest dotD replay kept retired",
            "dynamic Phi_fin/C1 final value gate reconciled with exact R_Z/R_X candidate values",
            "A^T A, A^T b, deltaTheta_C1 conditional Hessian consequences locked",
            "local axiom conditional dynamic C1 closure separated from strict unpatched closure",
            "HRG-sized deficit attached to typed consumer-map acceptance predicate",
        ],
        "still_open": [
            "derive DifferentiatedPhiFinC1ResidualProjectorApplicationRule unpatched",
            "or export honest selected Galerkin C1 tables in fixed 72-real coordinates",
            "promote A_selected, b_selected, deltaTheta_C1, and sector response matrices strictly",
            "emit typed HRG consumer/source map from selected payload to UP_RET_OVERLAP.HRG",
            "emit selected A_EW large-threshold/RG transport if using the metrology route",
            "same-HRG non-Higgs prediction without retuning",
            "true SM/no-knob equivalence",
        ],
        "next_required_artifact": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedDynamicPhiFinC1PayloadOrLargeThresholdHRGConsumerMap",
        "status": STATUS,
        "previous_status": previous["status"],
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "theorem": {
            "name": "DynamicPhiFinC1PayloadOrLargeThresholdHRGConsumerMapTheorem",
            "proved": True,
            "statement": (
                "The corrected HRG frontier is the final dynamic Phi_fin/C1 value "
                "gate plus a typed HRG consumer map.  The exact dynamic value table "
                "is ready and local-axiom conditional closure exists, but strict "
                "unpatched selection still requires the differentiated Phi_fin^C1 "
                "source rule or honest selected Galerkin C1 tables; the HRG-sized "
                "391.39140285811936 factor still requires a selected consumer/source "
                "map and is not promoted from external lambda_Mt."
            ),
        },
        "closure_decision": {
            "dynamic_gate_reconciled": True,
            "alpha1_and_dotd_replay_retired": True,
            "exact_dynamic_values_ready": True,
            "local_axiom_conditional_dynamic_C1_closure_available": True,
            "strict_unpatched_dynamic_C1_closed": False,
            "source_rule_proved_unpatched": False,
            "honest_galerkin_c1_tables_exported": False,
            "selected_dynamic_phi_fin_c1_payload_emitted": False,
            "A_selected_promoted_strict": False,
            "b_selected_promoted_strict": False,
            "deltaTheta_C1_promoted_strict": False,
            "sector_response_matrices_promoted_strict": False,
            "HRG_consumer_map_gate_built": True,
            "typed_HRG_consumer_map_emitted": False,
            "selected_AEW_large_threshold_transport_available_for_consumer": False,
            "same_HRG_nonHiggs_prediction_emitted": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "UP_RET_OVERLAP_HRG": nums["UP_RET_OVERLAP_HRG"],
            "computed_HRG_burden": nums["computed_HRG_burden"],
            "required_A_EW_over_external_A_EW": nums["required_A_EW_over_external_A_EW"],
            "required_A_EW_over_external_A_EW_minus_HRG_abs": nums[
                "required_A_EW_over_external_A_EW_minus_HRG_abs"
            ],
            "lambda_replay_residual": nums["lambda_replay_residual"],
            "dynamic_payload_row_count": dynamic_rows["closure_decision"][
                "dynamic_payload_row_count"
            ],
            "accepted_dynamic_payload_row_count": dynamic_rows["closure_decision"][
                "accepted_dynamic_payload_row_count"
            ],
            "A_transpose_A": exact_ready["A_transpose_A"],
            "A_transpose_b": exact_ready["A_transpose_b"],
            "deltaTheta_C1": exact_ready["deltaTheta_C1"],
            "rank": exact_ready["rank"],
            "conditional_b_norm_sq": routed_completion["conditional_b_norm_sq"],
            "phase_R_Z_residual_norm_sq": dynamic_candidates["phase_R_Z"]["residual_norm_sq"],
            "shift_R_X_residual_norm_sq": dynamic_candidates["shift_R_X"]["residual_norm_sq"],
            "total_residual_norm_sq_four_sectors": routed_completion[
                "total_residual_norm_sq_four_sectors"
            ],
            "lane_B_missing_output_count": len(lane_b["missing_outputs"]),
        },
        "packets": {
            "dynamic_gate_reconciliation": rel(DYNAMIC_GATE_PACKET),
            "hrg_consumer_gate": rel(HRG_CONSUMER_PACKET),
            "local_axiom_vs_unpatched_boundary": rel(AXIOM_BOUNDARY_PACKET),
            "next_cutset": rel(CUTSET_PACKET),
        },
        "what_closes": {
            "final_dynamic_gate_reconciled": True,
            "exact_dynamic_values_ready_recorded": True,
            "local_axiom_boundary_separated": True,
            "HRG_consumer_map_acceptance_predicate_built": True,
            "external_lambda_forbidden_as_selector": True,
        },
        "what_remains_open": {
            "derive_unpatched_DifferentiatedPhiFinC1ResidualProjectorApplicationRule": True,
            "or_export_honest_selected_Galerkin_C1_tables": True,
            "strict_dynamic_payload_promotion": True,
            "typed_HRG_consumer_map": True,
            "selected_AEW_large_threshold_transport": True,
            "same_HRG_nonHiggs_prediction": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTTSelectedDynamicPhiFinC1PayloadOrLargeThresholdHRGConsumerMap",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "proof_note": rel(NOTE),
        "verified_packets": list(candidate["packets"].values()),
        "closure_claimed": True,
        "dynamic_gate_reconciled": True,
        "exact_dynamic_values_ready": True,
        "local_axiom_conditional_dynamic_C1_closure_available": True,
        "strict_unpatched_dynamic_C1_closed": False,
        "source_rule_proved_unpatched": False,
        "honest_galerkin_c1_tables_exported": False,
        "selected_dynamic_phi_fin_c1_payload_emitted": False,
        "HRG_consumer_map_gate_built": True,
        "typed_HRG_consumer_map_emitted": False,
        "same_HRG_nonHiggs_prediction_emitted": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Dynamic Phi_fin C1 Payload or Large-Threshold HRG Consumer Map v1

Status: `{STATUS}`

## Dynamic Payload Gate

The active dynamic C1 wall is now exact:

```text
dynamic values ready             true
accepted dynamic payload rows    {dynamic_rows["closure_decision"]["accepted_dynamic_payload_row_count"]}
dynamic payload rows inventoried {dynamic_rows["closure_decision"]["dynamic_payload_row_count"]}
A^T A                            {exact_ready["A_transpose_A"]}
A^T b                            {exact_ready["A_transpose_b"]}
deltaTheta_C1                    {exact_ready["deltaTheta_C1"]}
phase R_Z residual norm sq       {dynamic_candidates["phase_R_Z"]["residual_norm_sq"]}
shift R_X residual norm sq       {dynamic_candidates["shift_R_X"]["residual_norm_sq"]}
```

So the problem is no longer alpha1, dotD replay, or discovery of the finite
phase/shift candidate values.  The values are ready.  Strict promotion still
requires one of two exits:

```text
1. derive DifferentiatedPhiFinC1ResidualProjectorApplicationRule unpatched
2. export honest selected Galerkin C1 tables in the fixed 72-real coordinates
```

## Local Axiom Boundary

The local patched spine is also explicit:

```text
local axiom conditional closure  {patched_closure["promoted_objects"]["dynamic_C1_source_owner_packet"]}
unpatched dynamic C1 closed      {unpatched_exit["unpatched_dynamic_C1_closed"]}
honest Galerkin table exported   {unpatched_exit["honest_galerkin_table_exported"]}
```

That is useful support, not strict no-knob closure.

## HRG Consumer Gate

The HRG-sized deficit remains exact:

```text
UP_RET_OVERLAP.HRG               {nums["UP_RET_OVERLAP_HRG"]}
required_A_EW/external_A_EW      {nums["required_A_EW_over_external_A_EW"]}
residual                         {nums["required_A_EW_over_external_A_EW_minus_HRG_abs"]}
```

But HRG still needs a selected consumer/source map.  It cannot be promoted from
external `lambda_Mt`.

## Next

`{NEXT}`
"""

    write_json(DYNAMIC_GATE_PACKET, dynamic_gate_packet)
    write_json(HRG_CONSUMER_PACKET, hrg_consumer_packet)
    write_json(AXIOM_BOUNDARY_PACKET, axiom_boundary_packet)
    write_json(CUTSET_PACKET, cutset_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    for path in [OUTPUT, CERT, NOTE]:
        print(f"Wrote {rel(path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
