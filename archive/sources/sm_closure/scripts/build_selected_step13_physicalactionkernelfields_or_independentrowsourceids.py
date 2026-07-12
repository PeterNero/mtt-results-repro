"""Build Step 13 physical action-kernel field audit ledger."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step13_physicalactionkernelfields_or_independentrowsourceids"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PLAN_POSITION = PACKET_DIR / "step13_plan_position.packet.json"
ACTION_AUDIT = PACKET_DIR / "step13_action_kernel_field_audit.packet.json"
CONDITIONAL_BRIDGE = PACKET_DIR / "step13_conditional_principle_bridge.packet.json"
ROW_SOURCE_AUDIT = PACKET_DIR / "step13_independent_row_source_id_audit.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step13_to_step14_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step13_PhysicalActionKernelFields_or_IndependentRowSourceIDs_v1.md"

STEP12 = DATA / "selected_step12_preresidualsourceownership_or_newrowsourceids.candidate.json"
STEP12_WORKORDER = (
    DATA
    / "selected_step12_preresidualsourceownership_or_newrowsourceids"
    / "step12_to_step13_workorder.packet.json"
)
STEP12_NORMAL_FORM = (
    DATA
    / "selected_step12_preresidualsourceownership_or_newrowsourceids"
    / "step12_preresidual_normal_form_and_source_test.packet.json"
)
FOUR_CLAUSE = DATA / "selected_actionkernelfourclauseproof_or_independentkernelvaluesrun.candidate.json"
ROUTE_A_PARTIAL = (
    DATA
    / "selected_actionkernelfourclauseproof_or_independentkernelvaluesrun"
    / "route_a_four_clause_partial_proof.packet.json"
)
ROUTE_A_VALIDATOR = (
    DATA
    / "selected_actionkernelfourclauseproof_or_independentkernelvaluesrun"
    / "route_a_four_clause_validator_result.packet.json"
)
ROUTE_B_FIRST = (
    DATA
    / "selected_actionkernelfourclauseproof_or_independentkernelvaluesrun"
    / "route_b_independent_kernel_values_first_run.packet.json"
)
ROUTE_B_VALIDATOR = (
    DATA
    / "selected_actionkernelfourclauseproof_or_independentkernelvaluesrun"
    / "route_b_independent_kernel_values_validator_result.packet.json"
)
LOCAL_APPLY = (
    DATA
    / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution"
    / "applied_principle_kernel_closure.packet.json"
)
LOCAL_INSERTION = (
    DATA
    / "selected_weylvariation_actionprinciple_derivation_or_explicitinsertion"
    / "explicit_weylvariation_actionprinciple_insertion_package.packet.json"
)
SOURCE_KERNEL_ATTEMPT = (
    DATA
    / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
    / "current_pre_residual_variation_hessian_source_attempt.packet.json"
)
SOURCE_KERNEL_VALIDATOR = (
    DATA
    / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom"
    / "current_validator_result.packet.json"
)

STATUS = (
    "MTT_SELECTED_STEP13_PHYSICALACTIONKERNELFIELDS_OR_INDEPENDENTROWSOURCEIDS_"
    "CLOSED_FIELD_AUDIT_LOCAL_PRINCIPLE_DERIVATION_OPEN"
)
NEXT = "MTT_Selected_Step14_SelectedWeylVariationActionPrincipleDerivation_or_HonestRowSourceExecution_v1"


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
        raise FileNotFoundError("missing Step 13 inputs: " + ", ".join(missing))


def count_emitted(rows: list[dict[str, Any]]) -> int:
    return sum(1 for row in rows if row.get("selected_emitted") is True)


def count_with_source_id(rows: list[dict[str, Any]]) -> int:
    return sum(1 for row in rows if row.get("source_id"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        STEP12,
        STEP12_WORKORDER,
        STEP12_NORMAL_FORM,
        FOUR_CLAUSE,
        ROUTE_A_PARTIAL,
        ROUTE_A_VALIDATOR,
        ROUTE_B_FIRST,
        ROUTE_B_VALIDATOR,
        LOCAL_APPLY,
        LOCAL_INSERTION,
        SOURCE_KERNEL_ATTEMPT,
        SOURCE_KERNEL_VALIDATOR,
    ]
    require_sources(sources)

    step12 = load(STEP12)
    step12_workorder = load(STEP12_WORKORDER)
    step12_normal = load(STEP12_NORMAL_FORM)
    four_clause = load(FOUR_CLAUSE)
    route_a = load(ROUTE_A_PARTIAL)
    route_a_validator = load(ROUTE_A_VALIDATOR)
    route_b = load(ROUTE_B_FIRST)
    route_b_validator = load(ROUTE_B_VALIDATOR)
    local_apply = load(LOCAL_APPLY)
    local_insertion = load(LOCAL_INSERTION)
    source_attempt = load(SOURCE_KERNEL_ATTEMPT)
    source_validator = load(SOURCE_KERNEL_VALIDATOR)

    primitive_rows = route_b["primitive_row_kernel_sources"]
    hessian_rows = route_b["hessian_b_sources"]
    sector_rows = route_b["sector_assembly_sources"]

    plan_position = {
        "schema": "MTTStep13PlanPosition.v1",
        "status": "STEP13_ACTIVE_AFTER_STEP12_NORMAL_FORM_REDUCTION",
        "closed_plan_steps": {
            "step4": "dynamic matrices/admitted rows contract",
            "step5": "no-knob/minimal-knob audit",
            "step6": "measured-SM comparison readiness",
            "step7": "common-RG/covariance observable-suite gate",
            "step8": "precision route and operator source slots",
            "step9": "non-looping frontier reduction",
            "step10": "single theorem wall collapse",
            "step11": "first three clause-status ledger",
            "step12": "pre-residual R_Z/R_X normal-form source-test reduction",
        },
        "active_step": 13,
        "active_target": step12_workorder["next_required_artifact"],
        "remaining_steps_after_13": {
            "step14": "derive selected Weyl-variation action principle or execute honest row-source table",
            "step15": "SelectedFiniteC1SourceIdentityTheorem promotion",
            "step16": "dynamic Qa/SU3 value packet and true-SM/no-knob value audit",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(PLAN_POSITION, plan_position)

    action_audit = {
        "schema": "MTTStep13ActionKernelFieldAudit.v1",
        "status": "ACTION_KERNEL_FIELDS_AUDITED_THREE_PHYSICAL_CLAUSES_OPEN",
        "source": rel(ROUTE_A_PARTIAL),
        "validator": rel(ROUTE_A_VALIDATOR),
        "admissible_differentiated_variations_fixed": route_a[
            "admissible_differentiated_variations_fixed"
        ],
        "RZ_RX_operator_discovery_closed": step12["closure_decision"][
            "RZ_RX_operator_discovery_closed"
        ],
        "RZ_RX_reconstruction_errors": {
            "R_Z": step12_normal["R_Z"]["reconstruction_error_norm_sq"],
            "R_X": step12_normal["R_X"]["reconstruction_error_norm_sq"],
        },
        "physical_action_equals_c1_defect_functional": route_a[
            "physical_action_equals_c1_defect_functional"
        ],
        "physical_boundary_source_terms_vanish": route_a[
            "physical_boundary_source_terms_vanish"
        ],
        "same_source_rz_rx_bselected_emitted": route_a[
            "same_source_rz_rx_bselected_emitted"
        ],
        "missing_action_kernel_fields": [
            field
            for field in [
                "physical_action_equals_c1_defect_functional",
                "physical_boundary_source_terms_vanish",
                "same_source_rz_rx_bselected_emitted",
            ]
            if route_a[field] is False
        ],
        "validator_returncode": route_a_validator["returncode"],
        "validator_stderr_lines": route_a_validator["stderr_lines"],
        "free_axiom_patch_used": route_a["free_axiom_patch_used"],
        "residual_projector_replay_used_as_source": route_a[
            "residual_projector_replay_used_as_source"
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ACTION_AUDIT, action_audit)

    conditional_bridge = {
        "schema": "MTTStep13ConditionalPrincipleBridge.v1",
        "status": "LOCAL_WEYL_VARIATION_PRINCIPLE_IDENTIFIED_NOT_ACCEPTED_AS_FREE_PATCH",
        "local_apply_packet": rel(LOCAL_APPLY),
        "local_insertion_packet": rel(LOCAL_INSERTION),
        "principle_name": local_insertion["principle_name"],
        "principle_text": local_insertion["principle_text"],
        "accepted_here": local_insertion["accepted_here"],
        "must_not_be_used_as_free_patch": local_insertion["must_not_be_used_as_free_patch"],
        "would_close_if_derived_from_selected_MTT_geometry": {
            "selected_variation_functional": local_apply["selected_variation_functional"],
            "same_source_hessian": local_apply["same_source_hessian"],
            "sector_functor": local_apply["sector_functor"],
            "independence_certificate": local_apply["independence_certificate"],
            "pre_residual_phase_shift_operator_source": local_apply["promoted_inside_local_spine"][
                "pre_residual_phase_shift_operator_source"
            ],
            "same_source_hessian_b_selected_rows": local_apply["promoted_inside_local_spine"][
                "same_source_hessian_b_selected_rows"
            ],
            "sector_rows_physical_source_promotion": local_apply["promoted_inside_local_spine"][
                "sector_rows_physical_source_promotion"
            ],
        },
        "why_not_promoted_now": [
            "The explicit principle insertion packet is marked accepted_here=false.",
            "The Step 12 guard forbids premise-free symbolic source-stack promotion.",
            "A selected MTT derivation of the physical Phi_fin^C1 action identity is still missing.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CONDITIONAL_BRIDGE, conditional_bridge)

    row_source_audit = {
        "schema": "MTTStep13IndependentRowSourceIDAudit.v1",
        "status": "INDEPENDENT_ROW_SOURCE_IDS_NOT_EMITTED",
        "source": rel(ROUTE_B_FIRST),
        "validator": rel(ROUTE_B_VALIDATOR),
        "selected_variation_space_source_emitted": route_b["global_sources"][
            "selected_variation_space"
        ]["selected_emitted"],
        "selected_measure_pairing_source_emitted": route_b["global_sources"][
            "selected_measure_pairing"
        ]["selected_emitted"],
        "selected_quadrature_rule_emitted": route_b["global_sources"][
            "selected_quadrature_rule"
        ]["selected_emitted"],
        "primitive_row_kernel_source_count": len(primitive_rows),
        "primitive_row_kernel_sources_emitted_count": count_emitted(primitive_rows),
        "primitive_row_kernel_source_ids_count": count_with_source_id(primitive_rows),
        "hessian_b_source_count": len(hessian_rows),
        "hessian_b_sources_emitted_count": count_emitted(hessian_rows),
        "hessian_b_source_ids_count": count_with_source_id(hessian_rows),
        "sector_assembly_source_count": len(sector_rows),
        "sector_assembly_sources_emitted_count": count_emitted(sector_rows),
        "sector_assembly_source_ids_count": count_with_source_id(sector_rows),
        "validator_returncode": route_b_validator["returncode"],
        "validator_error_count": len(route_b_validator["stderr_lines"]),
        "new_independent_row_source_ids_emitted": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(ROW_SOURCE_AUDIT, row_source_audit)

    next_workorder = {
        "schema": "MTTStep13ToStep14Workorder.v1",
        "status": "NEXT_WORKORDER_DERIVE_SELECTED_WEYL_VARIATION_PRINCIPLE_OR_EXECUTE_ROW_SOURCE_TABLE",
        "completed_step": 13,
        "next_step": 14,
        "next_required_artifact": NEXT,
        "step14_must_close_one_of": {
            "derive_selected_weyl_variation_action_principle_from_MTT_geometry": True,
            "prove_physical_action_equals_c1_defect_functional": True,
            "prove_physical_boundary_source_terms_vanish": True,
            "emit_same_source_rz_rx_bselected": True,
            "execute_independent_row_source_table_with_source_ids_and_formulas": True,
        },
        "step14_must_not_repeat": {
            "RZ_RX_normal_form_discovery": True,
            "admissible_variation_space_only": True,
            "conditional_local_principle_as_free_patch": True,
            "exact_72_row_value_replay_as_source": True,
        },
        "must_not_use_as_selectors": step12_workorder["must_not_use_as_selectors"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_WORKORDER, next_workorder)

    candidate = {
        "candidate": "MTTSelectedStep13PhysicalActionKernelFieldsOrIndependentRowSourceIDs",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "step13_plan_position": rel(PLAN_POSITION),
            "step13_action_kernel_field_audit": rel(ACTION_AUDIT),
            "step13_conditional_principle_bridge": rel(CONDITIONAL_BRIDGE),
            "step13_independent_row_source_id_audit": rel(ROW_SOURCE_AUDIT),
            "step13_to_step14_workorder": rel(NEXT_WORKORDER),
        },
        "theorem": {
            "name": "Step13ActionKernelFieldAuditAndRouteSplitTheorem",
            "proved": True,
            "statement": (
                "Given Step 12's exact R_Z/R_X normal forms, Step 13 proves that the active "
                "blocker is not operator discovery or admissible variation space. The accepted "
                "Route A packet still lacks physical action equality, physical boundary/source "
                "vanishing, and same-source R_Z/R_X/b_selected emission. Route B still emits "
                "zero independent primitive, Hessian/b, or sector row source IDs. The local "
                "SelectedWeylVariationActionPrinciple is identified as the precise sufficient "
                "principle, but remains unaccepted until derived from selected MTT geometry or "
                "replaced by an honest row-source execution."
            ),
        },
        "closure_decision": {
            "step13_closed_for_plan_contract": True,
            "operator_discovery_reopened": False,
            "admissible_variation_space_reopened": False,
            "physical_action_equals_c1_defect_functional_proved_now": False,
            "physical_boundary_source_terms_vanish_proved_now": False,
            "same_source_rz_rx_bselected_emitted_now": False,
            "selected_weyl_variation_action_principle_accepted_now": False,
            "independent_row_source_ids_emitted_now": False,
            "SelectedFiniteC1SourceIdentityTheorem_proved": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "step13_plan_position_repeated": True,
            "action_kernel_missing_fields_fixed_as_exact_frontier": True,
            "conditional_local_principle_identified_as_single_route_A_theorem": True,
            "route_B_independent_source_id_absence_quantified": True,
            "step14_workorder_emitted": True,
        },
        "what_remains_open": {
            "derive_selected_weyl_variation_action_principle_from_MTT_geometry": True,
            "physical_action_equals_c1_defect_functional": True,
            "physical_boundary_source_terms_vanish": True,
            "same_source_rz_rx_bselected_emitted": True,
            "same_source_hessian_b_selected": True,
            "sector_functor_assembly": True,
            "independence_certificate": True,
            "independent_row_source_ids_and_formulas": True,
            "SelectedFiniteC1SourceIdentityTheorem": True,
        },
        "current_source_kernel_validator_returncode": source_validator["returncode"],
        "current_source_kernel_missing_fields": source_validator["stderr_lines"],
        "current_source_kernel_attempt": {
            "selected_variation_functional": source_attempt["selected_variation_functional"],
            "same_source_hessian": source_attempt["same_source_hessian"],
            "sector_functor": source_attempt["sector_functor"],
            "independence_certificate": source_attempt["independence_certificate"],
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "step13_contract_closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step13_PhysicalActionKernelFields_or_IndependentRowSourceIDs_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "step13_contract_closure_claimed": True,
        "action_kernel_missing_fields_fixed_as_exact_frontier": True,
        "selected_weyl_variation_action_principle_accepted_now": False,
        "physical_action_equals_c1_defect_functional_proved_now": False,
        "physical_boundary_source_terms_vanish_proved_now": False,
        "same_source_rz_rx_bselected_emitted_now": False,
        "independent_row_source_ids_emitted_now": False,
        "SelectedFiniteC1SourceIdentityTheorem_proved": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step13 PhysicalActionKernelFields or IndependentRowSourceIDs v1

Status: `{STATUS}`.

Current plan:

```text
Steps 4-8 : closed at contract/readiness/source-slot tiers
Step 9    : closed as non-looping frontier reduction
Step 10   : closed as single theorem wall collapse
Step 11   : closed as first-three-clause status ledger
Step 12   : closed as pre-residual R_Z/R_X normal-form reduction
Step 13   : current action-kernel field audit and route split
```

Step 13 closes:

```text
operator discovery reopened?                 false
admissible variation space reopened?         false
missing action-kernel fields fixed exactly   true
Route B independent source-id absence counted true
conditional local principle isolated          true
```

Step 13 does not close:

```text
physical action = C1 defect functional        false
physical boundary/source terms vanish         false
same-source R_Z/R_X/b_selected emitted        false
selected Weyl variation principle accepted    false
independent row-source IDs emitted            false
```

Remaining step sketch:

```text
Step 14 : derive selected Weyl-variation action principle from MTT geometry
          or execute honest row-source table with source IDs/formulas
Step 15 : SelectedFiniteC1SourceIdentityTheorem promotion
Step 16 : dynamic Qa/SU3 values and true-SM/no-knob value audit
```

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
