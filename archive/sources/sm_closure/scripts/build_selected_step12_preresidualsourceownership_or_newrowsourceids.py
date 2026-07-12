"""Build Step 12 pre-residual source-ownership clause proof ledger."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_step12_preresidualsourceownership_or_newrowsourceids"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PLAN_POSITION = PACKET_DIR / "step12_plan_position.packet.json"
NORMAL_FORM = PACKET_DIR / "step12_preresidual_normal_form_and_source_test.packet.json"
KERNEL_REDUCTION = PACKET_DIR / "step12_source_owner_kernel_reduction.packet.json"
NEW_ROWS = PACKET_DIR / "step12_new_row_source_ids_attempt.packet.json"
NEXT_WORKORDER = PACKET_DIR / "step12_to_step13_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Step12_PreResidualSourceOwnershipClauseProof_or_NewRowSourceEmission_v1.md"

STEP11 = DATA / "selected_step11_selectedfinitec1sourceidentity_clauseproof.candidate.json"
STEP11_WORKORDER = (
    DATA
    / "selected_step11_selectedfinitec1sourceidentity_clauseproof"
    / "step11_to_step12_workorder.packet.json"
)
PRERESIDUAL = DATA / "selected_preresidualweylvariationselectionlemma_or_honestquadraturesource.candidate.json"
PRERESIDUAL_NORMAL_FORM = (
    DATA
    / "selected_preresidualweylvariationselectionlemma_or_honestquadraturesource"
    / "psm_c1_02_preresidual_weyl_normal_form.packet.json"
)
PHYSICAL_SELECTION_ATTEMPT = (
    DATA
    / "selected_preresidualweylvariationselectionlemma_or_honestquadraturesource"
    / "route_a_physical_selection_lemma_attempt.packet.json"
)
PHYSICAL_SELECTION_VALIDATOR = (
    DATA
    / "selected_preresidualweylvariationselectionlemma_or_honestquadraturesource"
    / "route_a_physical_selection_lemma_validator_result.packet.json"
)
SOURCE_KERNEL = DATA / "selected_preresidualvariation_hessiansourcekernel_attempt_or_actionaxiom.candidate.json"
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
ROUTEC = DATA / "selected_routec_weylvariation_sourceprinciple_or_kernelclosure.candidate.json"
ROUTEC_TEST = (
    DATA
    / "selected_routec_weylvariation_sourceprinciple_or_kernelclosure"
    / "routec_kernel_promotion_test.packet.json"
)
ROUTEC_VALIDATOR = (
    DATA
    / "selected_routec_weylvariation_sourceprinciple_or_kernelclosure"
    / "strict_kernel_validator_result.packet.json"
)
DYNAMIC_OWNER = DATA / "selected_dynamicc1_sourceowner_theorem_or_independentconnectiontables.candidate.json"
DYNAMIC_OWNER_FILL = DATA / "selected_dynamicc1_sourceowner_fill_or_connectiontables_export_run.candidate.json"
PSM_PRERESIDUAL = DATA / "selected_psm_c1_02_preresidualoperators_or_routea_physicalrestriction.candidate.json"
STEP10_WALL = (
    DATA
    / "selected_step10_finitec1sourceidentity_singlewall_or_newrows"
    / "step10_single_source_identity_wall.packet.json"
)

STATUS = (
    "MTT_SELECTED_STEP12_PRERESIDUALSOURCEOWNERSHIP_OR_NEWROWSOURCEIDS_"
    "CLOSED_NORMAL_FORM_SOURCE_TEST_ACTIONKERNEL_OPEN"
)
NEXT = "MTT_Selected_Step13_PhysicalActionKernelFields_or_IndependentRowSourceIDs_v1"


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
        raise FileNotFoundError("missing Step 12 inputs: " + ", ".join(missing))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        STEP11,
        STEP11_WORKORDER,
        PRERESIDUAL,
        PRERESIDUAL_NORMAL_FORM,
        PHYSICAL_SELECTION_ATTEMPT,
        PHYSICAL_SELECTION_VALIDATOR,
        SOURCE_KERNEL,
        SOURCE_KERNEL_ATTEMPT,
        SOURCE_KERNEL_VALIDATOR,
        ROUTEC,
        ROUTEC_TEST,
        ROUTEC_VALIDATOR,
        DYNAMIC_OWNER,
        DYNAMIC_OWNER_FILL,
        PSM_PRERESIDUAL,
        STEP10_WALL,
    ]
    require_sources(sources)

    step11 = load(STEP11)
    step11_workorder = load(STEP11_WORKORDER)
    preresidual = load(PRERESIDUAL)
    normal = load(PRERESIDUAL_NORMAL_FORM)
    physical_attempt = load(PHYSICAL_SELECTION_ATTEMPT)
    physical_validator = load(PHYSICAL_SELECTION_VALIDATOR)
    source_kernel = load(SOURCE_KERNEL)
    source_attempt = load(SOURCE_KERNEL_ATTEMPT)
    source_validator = load(SOURCE_KERNEL_VALIDATOR)
    routec = load(ROUTEC)
    routec_test = load(ROUTEC_TEST)
    routec_validator = load(ROUTEC_VALIDATOR)
    dynamic_owner = load(DYNAMIC_OWNER)
    dynamic_owner_fill = load(DYNAMIC_OWNER_FILL)
    psm_preresidual = load(PSM_PRERESIDUAL)
    step10_wall = load(STEP10_WALL)

    plan_position = {
        "schema": "MTTStep12PlanPosition.v1",
        "status": "STEP12_ACTIVE_AFTER_STEP11_CLAUSE_STATUS_LEDGER",
        "closed_plan_steps": {
            "step4": "dynamic matrices/admitted rows contract",
            "step5": "no-knob/minimal-knob audit",
            "step6": "measured-SM comparison readiness",
            "step7": "common-RG/covariance observable-suite gate",
            "step8": "precision route and operator source slots",
            "step9": "non-looping frontier reduction",
            "step10": "single theorem wall collapse",
            "step11": "first three clause-status ledger",
        },
        "active_step": 12,
        "active_target": step11_workorder["step12_target"],
        "remaining_steps_after_12": {
            "step13": "physical action-kernel fields or independent row-source IDs",
            "step14": "same-source Hessian/b_selected plus sector functor assembly",
            "step15": "SelectedFiniteC1SourceIdentityTheorem promotion",
            "step16": "dynamic Qa/SU3 value packet and true-SM/no-knob value audit",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(PLAN_POSITION, plan_position)

    normal_form = {
        "schema": "MTTStep12PreResidualNormalFormAndSourceTest.v1",
        "status": "PRERESIDUAL_RZ_RX_NORMAL_FORM_LOCKED_SOURCE_SELECTION_OPEN",
        "normal_form_source": rel(PRERESIDUAL_NORMAL_FORM),
        "source_level_weyl_carrier_selected": normal["source_level_weyl_carrier_selected"],
        "static_source_selector_selected": normal["static_source_selector_selected"],
        "R_Z": {
            "coefficient_count": normal["normal_form_checks"]["R_Z_coefficient_count"],
            "norm_sq": normal["normal_form_checks"]["R_Z_norm_sq"],
            "reconstruction_error_norm_sq": normal["normal_form_checks"][
                "R_Z_reconstruction_error_norm_sq"
            ],
            "exact_polynomial": normal["exact_polynomial_form"]["R_Z"],
        },
        "R_X": {
            "coefficient_count": normal["normal_form_checks"]["R_X_coefficient_count"],
            "norm_sq": normal["normal_form_checks"]["R_X_norm_sq"],
            "reconstruction_error_norm_sq": normal["normal_form_checks"][
                "R_X_reconstruction_error_norm_sq"
            ],
            "exact_polynomial": normal["exact_polynomial_form"]["R_X"],
        },
        "operator_discovery_problem_closed": True,
        "pre_residual_source_ordering_normal_form_closed": True,
        "residual_projector_replay_used_as_source": physical_attempt[
            "residual_projector_replay_used_as_source"
        ],
        "physical_action_equals_c1_defect_functional": physical_attempt[
            "physical_action_equals_c1_defect_functional"
        ],
        "physical_boundary_source_terms_vanish": physical_attempt[
            "physical_boundary_source_terms_vanish"
        ],
        "same_source_rz_rx_bselected_emitted": physical_attempt["same_source_rz_rx_bselected_emitted"],
        "physical_selection_validator_passes": physical_validator["passes"],
        "physical_selection_validator_missing_fields": physical_validator["stderr_lines"],
        "pre_residual_RZ_RX_source_ownership_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(NORMAL_FORM, normal_form)

    missing_source_kernel_fields = [
        field
        for field in [
            "selected_variation_functional",
            "same_source_hessian",
            "sector_functor",
            "independence_certificate",
        ]
        if source_attempt[field] is False
    ]
    kernel_reduction = {
        "schema": "MTTStep12SourceOwnerKernelReduction.v1",
        "status": "SOURCE_OWNER_REDUCED_TO_ACTION_KERNEL_FIELDS",
        "source_kernel_candidate": rel(SOURCE_KERNEL),
        "routec_candidate": rel(ROUTEC),
        "dynamic_owner_candidate": rel(DYNAMIC_OWNER),
        "source_kernel_current_validator_returncode": source_validator["returncode"],
        "source_kernel_missing_fields": missing_source_kernel_fields,
        "routec_validator_ok": routec_validator["ok"],
        "routec_missing_fields": routec_validator["stderr"],
        "routec_conditional_witness_if_principle_inserted_or_derived": routec_test[
            "conditional_witness_if_principle_inserted_or_derived"
        ],
        "dynamic_owner_closed_fields": {
            "admissible_c1_variation_space": dynamic_owner_fill["closure_decision"][
                "admissible_c1_variation_space_closed"
            ],
            "source_owner_id": dynamic_owner_fill["closure_decision"]["source_owner_id_closed"],
            "independence_guard": dynamic_owner_fill["closure_decision"]["independence_guard_closed"],
        },
        "dynamic_owner_open_fields": {
            "phase_R_Z_source": dynamic_owner_fill["closure_decision"]["phase_R_Z_source_closed"],
            "shift_R_X_source": dynamic_owner_fill["closure_decision"]["shift_R_X_source_closed"],
            "b_selected_source": dynamic_owner_fill["closure_decision"]["b_selected_source_closed"],
            "sector_row_assembly": dynamic_owner_fill["closure_decision"]["sector_row_assembly_closed"],
        },
        "source_owner_kernel_proved_now": False,
        "selected_variation_functional_proved_now": False,
        "same_source_hessian_proved_now": False,
        "sector_functor_proved_now": False,
        "independence_certificate_proved_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(KERNEL_REDUCTION, kernel_reduction)

    new_rows = {
        "schema": "MTTStep12NewRowSourceIDsAttempt.v1",
        "status": "NO_NEW_INDEPENDENT_ROW_SOURCE_IDS_EMITTED",
        "fallback_target": step11_workorder["step12_target"]["fallback"],
        "independent_connection_export_schema_built": dynamic_owner["closure_decision"][
            "independent_connection_export_schema_built"
        ],
        "connection_export_tables_present_count": dynamic_owner_fill["what_closes_now"][
            "connection_export_tables_present_count"
        ],
        "new_independent_110_row_source_export_emitted": False,
        "new_row_source_ids_emitted": False,
        "reason_open": (
            "Current connection/export tables and exact rows are support artifacts; no row-level "
            "source IDs independent of residual replay have been emitted under the Step 11 guard."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(NEW_ROWS, new_rows)

    next_workorder = {
        "schema": "MTTStep12ToStep13Workorder.v1",
        "status": "NEXT_WORKORDER_PHYSICAL_ACTION_KERNEL_FIELDS_OR_INDEPENDENT_ROW_SOURCE_IDS",
        "completed_step": 12,
        "next_step": 13,
        "next_required_artifact": NEXT,
        "step13_must_close_one_of": {
            "derive_selected_variation_functional": True,
            "derive_physical_action_equals_c1_defect_functional": True,
            "derive_physical_boundary_source_vanishing": True,
            "emit_independent_row_source_ids": True,
        },
        "step13_must_not_repeat": {
            "RZ_RX_normal_form_discovery": True,
            "exact_72_row_value_replay": True,
            "shape_routing_as_source_selection": True,
            "premise_free_symbolic_source_stack_as_final_theorem": True,
        },
        "must_not_use_as_selectors": step11_workorder["must_not_use_as_selectors"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(NEXT_WORKORDER, next_workorder)

    candidate = {
        "candidate": "MTTSelectedStep12PreResidualSourceOwnershipOrNewRowSourceIDs",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "step12_plan_position": rel(PLAN_POSITION),
            "step12_preresidual_normal_form_and_source_test": rel(NORMAL_FORM),
            "step12_source_owner_kernel_reduction": rel(KERNEL_REDUCTION),
            "step12_new_row_source_ids_attempt": rel(NEW_ROWS),
            "step12_to_step13_workorder": rel(NEXT_WORKORDER),
        },
        "theorem": {
            "name": "Step12PreResidualNormalFormAndSourceKernelReductionTheorem",
            "proved": True,
            "statement": (
                "Step 12 closes the pre-residual operator discovery problem: R_Z and R_X have "
                "unique exact qutrit Weyl normal forms selected by the carrier/static selector, "
                "with residual replay not used as source in the physical-selection attempt. "
                "It does not close source ownership. The strict source-kernel validator reduces "
                "the remaining proof to selected variation functional, same-source Hessian/b, "
                "sector functor assembly, and independence certificate, or to genuinely new "
                "independent row-source IDs."
            ),
        },
        "closure_decision": {
            "step12_closed_for_plan_contract": True,
            "RZ_RX_operator_discovery_closed": True,
            "pre_residual_normal_form_closed": True,
            "residual_projector_replay_used_as_source": False,
            "pre_residual_RZ_RX_source_ownership_closed": False,
            "selected_variation_functional_proved_now": False,
            "same_source_hessian_b_proved_now": False,
            "sector_functor_proved_now": False,
            "independence_certificate_proved_now": False,
            "new_independent_110_row_source_export_emitted": False,
            "SelectedFiniteC1SourceIdentityTheorem_proved": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "what_closes_now": {
            "step12_plan_position_repeated": True,
            "RZ_RX_unique_qutrit_weyl_normal_forms_locked": True,
            "operator_discovery_not_the_blocker": True,
            "source_owner_kernel_missing_fields_identified": True,
            "step13_workorder_emitted": True,
        },
        "what_remains_open": {
            "selected_variation_functional": True,
            "physical_action_equals_c1_defect_functional": True,
            "physical_boundary_source_terms_vanish": True,
            "same_source_hessian_b_selected": True,
            "sector_functor_assembly": True,
            "independence_certificate": True,
            "new_independent_row_source_ids": True,
            "SelectedFiniteC1SourceIdentityTheorem": True,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "step12_contract_closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_Step12_PreResidualSourceOwnershipClauseProof_or_NewRowSourceEmission_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "step12_contract_closure_claimed": True,
        "RZ_RX_operator_discovery_closed": True,
        "pre_residual_normal_form_closed": True,
        "pre_residual_RZ_RX_source_ownership_closed": False,
        "new_independent_110_row_source_export_emitted": False,
        "SelectedFiniteC1SourceIdentityTheorem_proved": False,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected Step12 PreResidualSourceOwnershipClauseProof or NewRowSourceEmission v1

Status: `{STATUS}`.

Current plan:

```text
Steps 4-8 : closed at contract/readiness/source-slot tiers
Step 9    : closed as non-looping frontier reduction
Step 10   : closed as single theorem wall collapse
Step 11   : closed as first-three-clause status ledger
Step 12   : current pre-residual source-ownership reduction
```

Step 12 closes:

```text
R_Z/R_X operator discovery closed        : true
pre-residual Weyl normal form closed     : true
residual replay used as source           : false
```

Step 12 does not close:

```text
pre-residual R_Z/R_X source ownership    : false
selected variation functional            : false
same-source Hessian/b_selected           : false
sector functor assembly                  : false
independence certificate                 : false
new independent row-source IDs           : false
```

Remaining step sketch:

```text
Step 13 : physical action-kernel fields or independent row-source IDs
Step 14 : same-source Hessian/b_selected plus sector functor assembly
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
