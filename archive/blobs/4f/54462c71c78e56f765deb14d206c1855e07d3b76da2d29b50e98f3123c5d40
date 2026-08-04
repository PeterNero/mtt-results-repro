"""Build Step 11 selected finite-C1 source identity clause proof ledger."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step11_selectedfinitec1sourceidentity_clauseproof"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PLAN_POSITION = PACKET_DIR / "step11_plan_position.packet.json"
FIRST_THREE = PACKET_DIR / "step11_first_three_clause_attack.packet.json"
FULL_CLAUSE_MAP = PACKET_DIR / "step11_full_clause_status_map.packet.json"
OVERCLAIM_RECONCILIATION = PACKET_DIR / "step11_historical_overclaim_reconciliation.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step11_to_step12_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step11_SelectedFiniteC1SourceIdentityTheorem_ClauseProof_v1.md"

STEP10 = DATA / "selected_step10_finitec1sourceidentity_singlewall_or_newrows.candidate.json"
STEP10_WORKORDER = (
    DATA
    / "selected_step10_finitec1sourceidentity_singlewall_or_newrows"
    / "step10_to_step11_workorder.packet.json"
)
CLAUSE_PROOF = DATA / "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission.candidate.json"
UPDATED_GATE = (
    DATA
    / "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission"
    / "updated_source_identity_clause_gate.packet.json"
)
TRACE_ASSEMBLY = (
    DATA
    / "selected_finitec1sourceidentityclauseproof_or_independentrowdataemission"
    / "finite_weyl_trace_assembly_clause_proof.packet.json"
)
VARIATION = DATA / "selected_variationoperatorshapecompatibility_or_hessiansourcegap.candidate.json"
VARIATION_COMPAT = (
    DATA
    / "selected_variationoperatorshapecompatibility_or_hessiansourcegap"
    / "variation_operator_shape_compatibility.packet.json"
)
VARIATION_ROUTING = (
    DATA
    / "selected_variationoperatorshapecompatibility_or_hessiansourcegap"
    / "variation_operator_72_slot_routing.packet.json"
)
ALL_72 = (
    DATA
    / "selected_firstrowprovenancepromotion_or_allrowsweylexecution"
    / "all_72_exact_weyl_row_execution.packet.json"
)
BASIS_FILL = (
    DATA
    / "selected_routeb_selectedbasisindependencefill_or_rowsourcegap"
    / "route_b_selected_basis_independence_fill.packet.json"
)
SOURCE_REPLAY = DATA / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate.candidate.json"
SOURCE_REPLAY_SUMMARY = (
    DATA
    / "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate"
    / "unpatched_source_promotion_replay_summary.packet.json"
)
VSD01 = DATA / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource.candidate.json"
VSD01_BACKIMPORT = (
    DATA
    / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
    / "premise_free_physical_source_backimport.packet.json"
)
VSD01_ASSEMBLY = (
    DATA
    / "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource"
    / "all_primitive_rows_assembly_map.packet.json"
)

STATUS = (
    "MTT_SELECTED_STEP11_SELECTEDFINITEC1SOURCEIDENTITY_CLAUSEPROOF_"
    "CLOSED_STATUS_LEDGER_SOURCEOWNERSHIP_OPEN"
)
NEXT = "MTT_Selected_Step12_PreResidualSourceOwnershipClauseProof_or_NewRowSourceEmission_v1"


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
        raise FileNotFoundError("missing Step 11 inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        STEP10,
        STEP10_WORKORDER,
        CLAUSE_PROOF,
        UPDATED_GATE,
        TRACE_ASSEMBLY,
        VARIATION,
        VARIATION_COMPAT,
        VARIATION_ROUTING,
        ALL_72,
        BASIS_FILL,
        SOURCE_REPLAY,
        SOURCE_REPLAY_SUMMARY,
        VSD01,
        VSD01_BACKIMPORT,
        VSD01_ASSEMBLY,
    ]
    require_sources(sources)

    step10 = load(STEP10)
    step10_workorder = load(STEP10_WORKORDER)
    clause_proof = load(CLAUSE_PROOF)
    updated_gate = load(UPDATED_GATE)
    trace_assembly = load(TRACE_ASSEMBLY)
    variation = load(VARIATION)
    compat = load(VARIATION_COMPAT)
    routing = load(VARIATION_ROUTING)
    all_72 = load(ALL_72)
    basis = load(BASIS_FILL)
    source_replay = load(SOURCE_REPLAY)
    source_replay_summary = load(SOURCE_REPLAY_SUMMARY)
    vsd01 = load(VSD01)
    vsd01_backimport = load(VSD01_BACKIMPORT)
    vsd01_assembly = load(VSD01_ASSEMBLY)

    rows = routing["rows"]
    row_count = len(rows)
    all_shapes_attached = all(row["operator_shape_attached"] for row in rows)
    all_slots_typed = all(row["slot_typed_by_selected_basis"] for row in rows)
    no_row_uses_residual_projector_as_shape_source = all(
        row["residual_projector_used_as_source"] is False for row in rows
    )
    no_operator_selected_as_source = all(row["operator_selected_as_source_now"] is False for row in rows)
    no_hessian_counterterm_sourced = all(row["hessian_counterterm_sourced"] is False for row in rows)

    selected_basis_certificate = basis["route_B_independent_execution"][
        "selected_basis_independence_certificate"
    ]
    source_replay_depends_on_symbolic_certificate = (
        vsd01_backimport["premise_free_route_A_certificate_valid"] is True
        and vsd01_backimport["raw_27mode_guardrail"]["raw_27mode_finite_replay_closed"] is False
        and vsd01_backimport["symbolic_transport_closed_quotient"]["symbolic_transport_envelope"] is True
    )

    plan_position = {
        "schema": "MTTStep11PlanPosition.v1",
        "status": "STEP11_ACTIVE_AFTER_STEP10_SINGLE_WALL_COLLAPSE",
        "closed_plan_steps": {
            "step4_dynamic_physical_matrices_and_admitted_rows": "closed_contract_tier",
            "step5_no_knob_minimal_knob_audit": "closed_audit_tier_zero_internal_rows",
            "step6_measured_sm_comparison_readiness": "closed_readiness_tier",
            "step7_common_rg_covariance_observable_suite": "closed_gate_contract_tier",
            "step8_precision_route_and_operator_source_slots": "closed_source_slot_tier",
            "step9_dynamic_qasu3_c1_frontier_reduction": "closed_frontier_reduction_tier",
            "step10_route_duplication_collapse": "closed_single_wall_tier",
        },
        "active_step": 11,
        "active_object": "SelectedFiniteC1SourceIdentityTheorem",
        "step11_role": "clause proof/status ledger, not route restatement",
        "step10_next_workorder": rel(STEP10_WORKORDER),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(PLAN_POSITION, plan_position)

    first_three = {
        "schema": "MTTStep11FirstThreeClauseAttack.v1",
        "status": "FIRST_THREE_CLAUSES_REDUCED_TO_SOURCEOWNERSHIP",
        "clauses": {
            "selected_phase_shift_variation_operators_before_residual_projection": {
                "shape_and_72_slot_routing_closed": (
                    compat["all_routed_operator_shapes_attached"] is True
                    and compat["compatible_with_72_slot_table"] is True
                    and routing["phase_R_Z_rows"] == 36
                    and routing["shift_R_X_rows"] == 36
                    and row_count == 72
                    and all_shapes_attached
                    and no_row_uses_residual_projector_as_shape_source
                ),
                "operator_shapes_selected_as_physical_source": compat[
                    "operator_shapes_selected_as_source_now"
                ],
                "source_map_selected_by_MTT_now": compat["source_map_selected_by_MTT_now"],
                "full_clause_proved": False,
                "reason_open": (
                    "R_Z/R_X shapes and routing are closed before residual projection, "
                    "but the operators are not selected as physical source data."
                ),
            },
            "selected_basis_feeds_72_row_functions": {
                "slot_typing_closed_for_all_72_rows": all_slots_typed,
                "selected_basis_independent_of_residual_projector": basis["route_B_independent_execution"][
                    "selected_basis_independent_of_residual_projector"
                ],
                "all_sector_sources_verified_by_transport_conjugation": selected_basis_certificate[
                    "all_sector_sources_verified_by_transport_conjugation"
                ],
                "source_independent_of_residual_projector_replay": basis["route_B_independent_execution"][
                    "source_independent_of_residual_projector_replay"
                ],
                "full_clause_proved": False,
                "reason_open": (
                    "The selected transported basis types the 72 slots and is independent of "
                    "the residual projector, but the row source still inherits residual-lineage provenance."
                ),
            },
            "row_formula_source_theorem_derived": {
                "all_72_row_values_exact": all_72["exactness_clause_closed_for_all_rows"],
                "all_72_row_count": all_72["row_count"],
                "provenance_independent_of_residual_projector_replay_for_all_rows": all_72[
                    "provenance_independent_of_residual_projector_replay_for_all_rows"
                ],
                "new_independent_row_packet_emitted": False,
                "full_clause_proved": False,
                "reason_open": (
                    "Exact finite Weyl row formulas exist, but their accepted provenance is "
                    "postcheck/replay lineage rather than a selected source theorem."
                ),
            },
        },
        "first_three_clause_attack_completed": True,
        "first_three_all_values_or_routing_closed": True,
        "first_three_source_ownership_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(FIRST_THREE, first_three)

    full_clause_map = {
        "schema": "MTTStep11FullClauseStatusMap.v1",
        "status": "CLAUSE_STATUS_REFINED_SOURCEOWNERSHIP_OPEN",
        "theorem_name": "SelectedFiniteC1SourceIdentityTheorem",
        "clause_status": {
            "selected_phase_shift_variation_operators_before_residual_projection": "PARTIAL_ROUTING_CLOSED_SOURCE_SELECTION_OPEN",
            "selected_basis_feeds_72_row_functions": "PARTIAL_SLOT_TYPING_AND_BASIS_INDEPENDENCE_CLOSED_ROW_SOURCE_OPEN",
            "row_formula_source_theorem_derived": "PARTIAL_72_EXACT_VALUES_CLOSED_SOURCE_THEOREM_OPEN",
            "residual_projector_replay_not_used_as_source": "OPEN_FOR_ROW_PROVENANCE",
            "selected_hessian_counterterm_and_b_source": "OPEN_QUARANTINED_OLD_PREMISE_FREE_SUPPORT",
            "zero_extra_boundary_or_source_terms": "OPEN_QUARANTINED_OLD_PREMISE_FREE_SUPPORT",
            "C1_action_restricts_to_finite_trace_measure": "PARTIAL_TRACE_ASSEMBLY_CLOSED_PHYSICAL_ACTION_RESTRICTION_OPEN",
        },
        "imported_prior_clause_gate": rel(UPDATED_GATE),
        "trace_assembly_subclause_closed": trace_assembly["proved_subclaim"]["trace_assembly_closed"],
        "source_identity_theorem_proved_now": False,
        "new_independent_110_row_source_export_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(FULL_CLAUSE_MAP, full_clause_map)

    overclaim_reconciliation = {
        "schema": "MTTStep11HistoricalOverclaimReconciliation.v1",
        "status": "HISTORICAL_SOURCE_STACK_REPLAY_RETAINED_AS_SUPPORT_NOT_STEP11_PROOF",
        "historical_sources": {
            "selected_unpatchedsourcepromotionreplay_or_fullsmclosuregate": rel(SOURCE_REPLAY),
            "selected_vsd01_allprimitiverowsassemblymap_or_physicalphifinc1actionsource": rel(VSD01),
        },
        "historical_claims": {
            "source_replay_SelectedFiniteC1SourceIdentityTheorem_promoted": source_replay[
                "promotion_decision"
            ]["SelectedFiniteC1SourceIdentityTheorem_promoted"],
            "source_replay_A_b_delta_promoted": (
                source_replay["promotion_decision"]["unpatched_A_selected_promoted"]
                and source_replay["promotion_decision"]["unpatched_b_selected_promoted"]
                and source_replay["promotion_decision"]["unpatched_deltaTheta_C1_promoted"]
            ),
            "vsd01_physical_PhiFinC1_action_source": vsd01["what_closes_now"][
                "physical_PhiFinC1_action_source"
            ],
            "vsd01_source_owner_verified": vsd01["what_closes_now"]["source_owner_verified"],
        },
        "reason_not_imported_as_step11_theorem": {
            "depends_on_premise_free_symbolic_transport_certificate": source_replay_depends_on_symbolic_certificate,
            "raw_27mode_finite_replay_closed": vsd01_backimport["raw_27mode_guardrail"][
                "raw_27mode_finite_replay_closed"
            ],
            "step10_forbids_route_restatement_without_new_clause_status": step10_workorder[
                "forbidden_next_moves"
            ]["restate_route_A_or_route_B_without_new_clause_status"],
            "step10_requires_clause_proof_or_new_row_source_ids": True,
        },
        "accepted_use_in_step11": "support/postcheck only",
        "source_identity_theorem_proved_by_historical_claims_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(OVERCLAIM_RECONCILIATION, overclaim_reconciliation)

    next_workorder = {
        "schema": "MTTStep11ToStep12Workorder.v1",
        "status": "NEXT_WORKORDER_PRE_RESIDUAL_SOURCE_OWNERSHIP_OR_NEW_ROW_SOURCE_EMISSION",
        "completed_step": 11,
        "next_step": 12,
        "next_required_artifact": NEXT,
        "step12_target": {
            "primary": "prove source ownership of pre-residual R_Z/R_X variation operators",
            "secondary": "derive row formula source theorem from that owner",
            "fallback": "emit genuinely new independent 110-row source packet with row-level source ids",
        },
        "forbidden_next_moves": {
            "repeat_exact_72_values_without_new_source_owner": True,
            "import_premise_free_symbolic_source_stack_as_final_theorem": True,
            "promote_shape_routing_as_source_selection": True,
            "use_observed_SM_values_as_selectors": True,
        },
        "must_not_use_as_selectors": step10_workorder["must_not_use_as_selectors"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_WORKORDER, next_workorder)

    candidate = {
        "candidate": "MTTSelectedStep11SelectedFiniteC1SourceIdentityClauseProof",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "step11_plan_position": rel(PLAN_POSITION),
            "step11_first_three_clause_attack": rel(FIRST_THREE),
            "step11_full_clause_status_map": rel(FULL_CLAUSE_MAP),
            "step11_historical_overclaim_reconciliation": rel(OVERCLAIM_RECONCILIATION),
            "step11_to_step12_workorder": rel(NEXT_WORKORDER),
        },
        "theorem": {
            "name": "Step11FiniteC1SourceIdentityClauseStatusTheorem",
            "proved": True,
            "statement": (
                "Step 11 proves a clause-status theorem for SelectedFiniteC1SourceIdentityTheorem. "
                "The first three attack clauses are reduced to a single source-ownership gap: "
                "phase/shift shapes route to all 72 slots before residual projection, selected bases "
                "type those slots, and exact 72 finite-Weyl row values exist, but none of these by "
                "itself selects the physical pre-residual R_Z/R_X source or row-formula source theorem. "
                "Historical source-stack closures are retained as support only because they depend on "
                "premise-free symbolic transport certificates under the stricter Step 10 gate."
            ),
        },
        "closure_decision": {
            "step11_closed_for_plan_contract": True,
            "first_three_clause_attack_completed": True,
            "phase_shift_72_slot_routing_closed": True,
            "selected_basis_slot_typing_closed": True,
            "all_72_exact_values_closed": True,
            "finite_trace_assembly_subclause_closed": True,
            "pre_residual_RZ_RX_source_ownership_closed": False,
            "row_formula_source_theorem_derived": False,
            "SelectedFiniteC1SourceIdentityTheorem_proved": False,
            "new_independent_110_row_source_export_emitted": False,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "step11_plan_position_repeated": True,
            "first_three_clause_status_refined": True,
            "historical_source_stack_overclaim_quarantined": True,
            "source_ownership_gap_minimized": True,
            "step12_workorder_emitted": True,
        },
        "what_remains_open": {
            "pre_residual_RZ_RX_source_ownership": True,
            "row_formula_source_theorem": True,
            "selected_hessian_counterterm_and_b_source": True,
            "physical_action_restriction_without_premise_free_shortcut": True,
            "new_independent_110_row_source_export": True,
            "SelectedFiniteC1SourceIdentityTheorem": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "step11_contract_closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step11_SelectedFiniteC1SourceIdentityTheorem_ClauseProof_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "step11_contract_closure_claimed": True,
        "first_three_clause_attack_completed": True,
        "phase_shift_72_slot_routing_closed": True,
        "selected_basis_slot_typing_closed": True,
        "all_72_exact_values_closed": True,
        "pre_residual_RZ_RX_source_ownership_closed": False,
        "SelectedFiniteC1SourceIdentityTheorem_proved": False,
        "new_independent_110_row_source_export_emitted": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step11 SelectedFiniteC1SourceIdentityTheorem ClauseProof v1

Status: `{STATUS}`.

Plan position:

```text
Steps 4-8 : closed at their contract/readiness/source-slot tiers
Step 9    : closed as non-looping frontier reduction
Step 10   : closed as route-duplication collapse to one theorem wall
Step 11   : current clause-proof/status ledger
```

Step 11 attacks the first three clauses of `SelectedFiniteC1SourceIdentityTheorem`.

```text
phase/shift shapes routed to 72 slots       : true
selected basis types all 72 slots           : true
all 72 finite-Weyl row values exact         : true
finite trace assembly subclause closed      : true
pre-residual R_Z/R_X source ownership       : false
row-formula source theorem                  : false
SelectedFiniteC1SourceIdentityTheorem proved: false
```

The old source-stack/VSD-01 promotion claims are retained only as support under
the stricter Step 10 gate, because they depend on premise-free symbolic
transport certificates rather than a new clause proof or new independent row
source ids.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
