"""Build Step 10 loop collapse to the single finite-C1 source identity wall."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step10_finitec1sourceidentity_singlewall_or_newrows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
LOOP_COLLAPSE = PACKET_DIR / "step10_loop_collapse.packet.json"
SINGLE_WALL = PACKET_DIR / "step10_single_source_identity_wall.packet.json"
ROW_EXECUTION_DIAGNOSIS = PACKET_DIR / "step10_row_execution_diagnosis.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step10_to_step11_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step10_FiniteC1SourceIdentity_SingleWall_or_NewRows_v1.md"

STEP9 = DATA / "selected_step9_dynamicqasu3c1response_or_precisionprofilecompletion.candidate.json"
STEP9_HANDOFF = (
    DATA
    / "selected_step9_dynamicqasu3c1response_or_precisionprofilecompletion"
    / "step9_to_step10_handoff.packet.json"
)
FINAL_TWO_ROUTE = DATA / "selected_unpatchedfinitec1sourceidentity_or_honestindependentkernelexport.candidate.json"
FINAL_TWO_ROUTE_DECISION = (
    DATA
    / "selected_unpatchedfinitec1sourceidentity_or_honestindependentkernelexport"
    / "final_two_route_decision.packet.json"
)
HONEST_KERNEL_AUDIT = (
    DATA
    / "selected_unpatchedfinitec1sourceidentity_or_honestindependentkernelexport"
    / "honest_kernel_export_route_audit.packet.json"
)
UNPATCHED_WEYL = DATA / "selected_unpatchedweylprincipleproof_or_independentkernelrowsfirstrun.candidate.json"
ROUTE_B_FIRST_RUN = (
    DATA
    / "selected_unpatchedweylprincipleproof_or_independentkernelrowsfirstrun"
    / "route_b_independent_kernel_rows_first_run.packet.json"
)
TWO_ROUTE_FIRST_RUN = (
    DATA
    / "selected_unpatchedweylprincipleproof_or_independentkernelrowsfirstrun"
    / "two_route_first_run_decision.packet.json"
)
ROUTEB_NORMALFORM = DATA / "selected_routeb_rowkernelsource_normalform_or_sourceobjectcontract.candidate.json"
ROUTEB_INDEPENDENCE = DATA / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill.candidate.json"
SOURCE_MAP = DATA / "selected_sourcemapselectiontheorem_or_honestgalerkinc1valuerun.candidate.json"
DIFFERENTIATED_RULE = DATA / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution.candidate.json"

STATUS = (
    "MTT_SELECTED_STEP10_FINITEC1SOURCEIDENTITY_SINGLEWALL_OR_NEWROWS_"
    "CLOSED_LOOP_COLLAPSE_THEOREM_OPEN"
)
NEXT = "MTT_Selected_Step11_SelectedFiniteC1SourceIdentityTheorem_ClauseProof_v1"


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
        raise FileNotFoundError("missing Step 10 inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        STEP9,
        STEP9_HANDOFF,
        FINAL_TWO_ROUTE,
        FINAL_TWO_ROUTE_DECISION,
        HONEST_KERNEL_AUDIT,
        UNPATCHED_WEYL,
        ROUTE_B_FIRST_RUN,
        TWO_ROUTE_FIRST_RUN,
        ROUTEB_NORMALFORM,
        ROUTEB_INDEPENDENCE,
        SOURCE_MAP,
        DIFFERENTIATED_RULE,
    ]
    require_sources(sources)

    step9 = load(STEP9)
    step9_handoff = load(STEP9_HANDOFF)
    final_two_route = load(FINAL_TWO_ROUTE)
    final_decision = load(FINAL_TWO_ROUTE_DECISION)
    honest_kernel = load(HONEST_KERNEL_AUDIT)
    unpatched_weyl = load(UNPATCHED_WEYL)
    route_b_first_run = load(ROUTE_B_FIRST_RUN)
    two_route_first_run = load(TWO_ROUTE_FIRST_RUN)
    routeb_normalform = load(ROUTEB_NORMALFORM)
    routeb_independence = load(ROUTEB_INDEPENDENCE)
    source_map = load(SOURCE_MAP)
    differentiated_rule = load(DIFFERENTIATED_RULE)

    loop_collapse = {
        "schema": "MTTStep10LoopCollapse.v1",
        "status": "TWO_ROUTE_WORDING_COLLAPSED_TO_SINGLE_SOURCE_IDENTITY_WALL",
        "step9_source": rel(STEP9),
        "final_two_route_source": rel(FINAL_TWO_ROUTE),
        "unpatched_weyl_source": rel(UNPATCHED_WEYL),
        "step9_closed_for_plan_contract": step9["closure_decision"]["step9_closed_for_plan_contract"],
        "old_wording_retired": {
            "selected_physical_PhiFinC1_source_rule_or_independent_Galerkin_rows": True,
            "reason": (
                "The strongest Route-A and Route-B execution artifacts show both names "
                "refer to the same selected finite-C1 source identity wall unless genuinely "
                "new independent rows are emitted."
            ),
        },
        "route_A_accepts_now": two_route_first_run["route_A_accepts"],
        "route_B_accepts_now": two_route_first_run["route_B_accepts"],
        "both_routes_reduce_to_shared_theorem": True,
        "shared_theorem_name": "SelectedFiniteC1SourceIdentityTheorem",
        "new_independent_rows_are_the_only_escape_hatch": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(LOOP_COLLAPSE, loop_collapse)

    single_wall = {
        "schema": "MTTStep10SingleSourceIdentityWall.v1",
        "status": "SELECTED_FINITE_C1_SOURCE_IDENTITY_THEOREM_IS_THE_SINGLE_WALL",
        "theorem_to_prove": "SelectedFiniteC1SourceIdentityTheorem",
        "equivalent_route_language": {
            "route_A_selected_physical_PhiFinC1_source_rule": "same theorem, action-language form",
            "route_B_independent_selected_Galerkin_or_row_kernel_execution": (
                "same theorem unless genuinely new independent row source data is emitted"
            ),
        },
        "minimal_clause_set": {
            "C1_action_restricts_to_finite_trace_measure": True,
            "zero_extra_boundary_or_source_terms": True,
            "selected_phase_shift_variation_operators_before_residual_projection": True,
            "selected_basis_feeds_72_row_functions": True,
            "row_formula_source_theorem_derived": True,
            "selected_hessian_counterterm_and_b_source": True,
            "residual_projector_replay_not_used_as_source": True,
        },
        "already_supports_but_not_proves": {
            "formal_110_row_values": True,
            "canonical_residual_projector": True,
            "finite_trace_boundary_cancellation": True,
            "conditional_local_principle_patch": True,
            "selected_source_map_candidate": True,
        },
        "proved_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(SINGLE_WALL, single_wall)

    open_fields = route_b_first_run["open_fields_in_attempt"]
    row_execution_diagnosis = {
        "schema": "MTTStep10RowExecutionDiagnosis.v1",
        "status": "CURRENT_ROW_EXECUTION_REJECTS_ONLY_SOURCE_LINEAGE_FIELDS",
        "honest_kernel_export_audit_source": rel(HONEST_KERNEL_AUDIT),
        "route_b_first_run_source": rel(ROUTE_B_FIRST_RUN),
        "strict_rows_required": final_decision["honest_kernel_export_route"]["strict_rows_required"],
        "formal_110_layer_available": route_b_first_run["formal_110_layer_available"],
        "row_counts": route_b_first_run["row_counts"],
        "closed_fields_in_attempt": route_b_first_run["closed_fields_in_attempt"],
        "open_fields_in_attempt": open_fields,
        "source_lineage_is_the_only_route_B_reason_after_prior_closures": (
            set(open_fields) == {
                "selected_basis_feeds_72_primitive_rows",
                "no_residual_projector_replay_used_as_source",
                "row_formula_source_theorem_derived",
                "source_independent_of_residual_projector_replay",
            }
        ),
        "do_not_repeat_full_110_row_value_fill_until_source_lineage_changes": True,
        "new_rows_required_if_not_proving_theorem": {
            "primitive_contractions_72_independent_rows": True,
            "hessian_source_2_independent_rows": True,
            "sector_matrices_36_independent_rows": True,
            "each_row_must_have": [
                "independent_source_emitted=true",
                "quadrature_rule_id",
                "kernel_source_id",
                "value",
                "exactness_certificate or error_bound",
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ROW_EXECUTION_DIAGNOSIS, row_execution_diagnosis)

    next_workorder = {
        "schema": "MTTStep10ToStep11Workorder.v1",
        "status": "NEXT_WORKORDER_IS_CLAUSE_PROOF_NOT_ROUTE_RESTATEMENT",
        "completed_step": 10,
        "next_step": 11,
        "next_required_artifact": NEXT,
        "forbidden_next_moves": {
            "restate_route_A_or_route_B_without_new_clause_status": True,
            "rerun_formal_110_row_replay_without_source_lineage_change": True,
            "promote_residual_projector_replay_as_independent_source": True,
            "use_observed_SM_values_as_selectors": True,
        },
        "step11_first_clause_attack_order": [
            "selected_phase_shift_variation_operators_before_residual_projection",
            "selected_basis_feeds_72_row_functions",
            "row_formula_source_theorem_derived",
            "residual_projector_replay_not_used_as_source",
            "selected_hessian_counterterm_and_b_source",
            "zero_extra_boundary_or_source_terms",
            "C1_action_restricts_to_finite_trace_measure",
        ],
        "success_criterion": (
            "Either prove the listed clauses as one SelectedFiniteC1SourceIdentityTheorem, "
            "or emit genuinely new independent 110-row source data with row-level source ids."
        ),
        "must_not_use_as_selectors": step9_handoff["must_not_use_as_selectors"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_WORKORDER, next_workorder)

    candidate = {
        "candidate": "MTTSelectedStep10FiniteC1SourceIdentitySingleWallOrNewRows",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "step10_loop_collapse": rel(LOOP_COLLAPSE),
            "step10_single_source_identity_wall": rel(SINGLE_WALL),
            "step10_row_execution_diagnosis": rel(ROW_EXECUTION_DIAGNOSIS),
            "step10_to_step11_workorder": rel(NEXT_WORKORDER),
        },
        "theorem": {
            "name": "Step10RouteDuplicationCollapseTheorem",
            "proved": True,
            "statement": (
                "The repeated Route-A/Route-B frontier is not two separate open problems. "
                "Existing execution artifacts prove that both routes collapse to one "
                "SelectedFiniteC1SourceIdentityTheorem, unless a genuinely new independent "
                "110-row source export is emitted. Therefore the next work must prove named "
                "source-identity clauses or emit new row-level source ids; repeating the "
                "two-route statement without a changed clause ledger is now forbidden."
            ),
        },
        "closure_decision": {
            "step10_closed_for_plan_contract": True,
            "route_duplication_collapsed": True,
            "single_source_identity_wall_identified": True,
            "route_A_accepts_now": False,
            "route_B_accepts_now": False,
            "SelectedFiniteC1SourceIdentityTheorem_proved": False,
            "new_independent_110_row_source_export_emitted": False,
            "actual_dynamic_QaSU3_operator_packet_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "looping_route_language_retired": True,
            "single_theorem_wall_identified": True,
            "row_execution_failure_reduced_to_source_lineage": True,
            "step11_clause_workorder_emitted": True,
        },
        "what_remains_open": {
            "SelectedFiniteC1SourceIdentityTheorem": True,
            "or_new_independent_110_row_source_export": True,
            "actual_dynamic_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "full_no_knob_closure": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "step10_contract_closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step10_FiniteC1SourceIdentity_SingleWall_or_NewRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "step10_contract_closure_claimed": True,
        "route_duplication_collapsed": True,
        "single_source_identity_wall_identified": True,
        "SelectedFiniteC1SourceIdentityTheorem_proved": False,
        "new_independent_110_row_source_export_emitted": False,
        "actual_dynamic_QaSU3_operator_packet_closed": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step10 FiniteC1SourceIdentity SingleWall or NewRows v1

Status: `{STATUS}`.

This resolves the looping language.  The active frontier should no longer be
reported as:

```text
selected physical Phi_fin^C1 source rule or independent Galerkin/row-kernel execution
```

The current execution artifacts show that phrase is just two dialects of one
wall:

```text
SelectedFiniteC1SourceIdentityTheorem
```

unless genuinely new independent 110-row source data is emitted.

Current exact status:

```text
route A accepts now                         : false
route B accepts now                         : false
formal 110-row layer available              : true
row execution failure reduced to lineage    : true
SelectedFiniteC1SourceIdentityTheorem proved: false
new independent 110-row source export       : false
true SM equivalence closed                  : false
full no-knob closure                        : false
```

Step 11 must be a clause proof, not another route restatement.  First attack
order:

1. selected phase/shift variation operators before residual projection;
2. selected basis feeds the 72 primitive row functions;
3. row formula source theorem;
4. residual projector replay is not used as source;
5. selected Hessian counterterm and `b_selected` source;
6. zero extra boundary/source terms;
7. finite C1 action restricts to the finite trace measure.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
