"""Build CONST-EW-02 B38 actual proof/fill attempt."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SM = ROOT.parent / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_ew_02_weak_mixing_b38_actual_proof_fill_attempt"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = BASE / "route_a_physical_action_identity_actual_attempt.packet.json"
ROUTE_B = BASE / "route_b_independent_payload_actual_fill_attempt.packet.json"
LOCAL = BASE / "local_principle_conditional_closure_boundary.packet.json"
NOGO = BASE / "unpatched_current_material_no_go.packet.json"
BOUNDARY = BASE / "weak_mixing_b38_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B38_ActualProofFillAttempt_v1.md"

STATUS = "MTT_CONST_EW_02_B38_ACTUAL_PROOF_FILL_ATTEMPT_BUILT_DECISIVE_NOGO"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b37_path = DATA / "const_ew_02_weak_mixing_b37_ra2_boundary_or_rb4_independent_source.candidate.json"
    b37_boundary_path = DATA / "const_ew_02_weak_mixing_b37_ra2_boundary_or_rb4_independent_source" / "weak_mixing_b37_boundary.packet.json"

    source_push_path = SM / "candidate_data" / "selected_sourcetheorem_push_attempt_or_minimalnewlemma.candidate.json"
    current_validator_path = SM / "candidate_data" / "selected_sourcetheorem_push_attempt_or_minimalnewlemma" / "current_validator_result.packet.json"
    minimal_lemma_path = SM / "candidate_data" / "selected_sourcetheorem_push_attempt_or_minimalnewlemma" / "minimal_selected_finitec1_source_promotion_lemma.packet.json"
    proof_counter_path = SM / "candidate_data" / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel.candidate.json"
    countermodel_path = SM / "candidate_data" / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel" / "closed_support_not_enough_countermodel.packet.json"
    obligation_path = SM / "candidate_data" / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel" / "minimal_lemma_obligation_status.packet.json"
    typed_functor_path = SM / "candidate_data" / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel" / "typed_row_functor_sublemma.packet.json"
    next_kernel_path = SM / "candidate_data" / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel" / "next_source_promotion_kernel.packet.json"
    local_apply_path = SM / "candidate_data" / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution.candidate.json"
    local_closure_path = SM / "candidate_data" / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "applied_principle_kernel_closure.packet.json"
    local_exit_path = SM / "candidate_data" / "selected_weylvariation_actionprinciple_apply_or_independentkernelexecution" / "unpatched_or_independent_kernel_execution_exit.packet.json"

    b37 = load(b37_path)
    b37_boundary = load(b37_boundary_path)
    source_push = load(source_push_path)
    current_validator = load(current_validator_path)
    minimal_lemma = load(minimal_lemma_path)
    proof_counter = load(proof_counter_path)
    countermodel = load(countermodel_path)
    obligation = load(obligation_path)
    typed_functor = load(typed_functor_path)
    next_kernel = load(next_kernel_path)
    local_apply = load(local_apply_path)
    local_closure = load(local_closure_path)
    local_exit = load(local_exit_path)

    route_a_missing = [
        "physical_action_restricts_to_finite_weyl_quotient",
        "zero_extra_boundary_or_source_term",
        "phase_R_Z_source_selection",
        "shift_R_X_source_selection",
        "same_source_b_selected_emission",
    ]
    route_b_missing = [
        "selected_basis_feeds_all_72_row_functionals",
        "pre_residual_phase_shift_variation_operators",
        "independent_hessian_counterterm_source_rows",
        "sector_rows_assembled_from_source_rows",
        "no_residual_projector_replay_or_locked_target_as_source",
    ]

    route_a = {
        "schema": "MTTConstEW02B38RouteAPhysicalActionIdentityActualAttempt.v1",
        "status": "ROUTE_A_ACTUAL_UNPATCHED_PROOF_REJECTED_LOCAL_PREMISE_AVAILABLE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B38-ROUTEA-PHYSICAL-PHIFINC1-ACTION-IDENTITY",
        "inputs": {
            "current_two_exit_validator_result": rel(current_validator_path),
            "local_principle_apply_candidate": rel(local_apply_path),
            "local_principle_kernel_closure": rel(local_closure_path),
            "unpatched_exit_packet": rel(local_exit_path),
        },
        "actual_unpatched_route_A_accepts": local_exit["route_A_accepts_without_local_principle"],
        "missing_unpatched_fields": route_a_missing,
        "local_principle_closes_kernel_conditionally": local_closure["promoted_inside_local_spine"],
        "local_principle_accepted": local_apply["closure_decision"]["local_principle_accepted"],
        "unpatched_principle_derived_now": local_apply["closure_decision"]["unpatched_principle_derived_now"],
        "why_not_actual_unpatched_proof": (
            "The only passing action-identity lane assumes SelectedWeylVariationActionPrinciple as an explicit local premise. "
            "The same artifacts explicitly report that the principle is not derived unpatched and that Route A does not accept without the premise."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    route_b = {
        "schema": "MTTConstEW02B38RouteBIndependentPayloadActualFillAttempt.v1",
        "status": "ROUTE_B_ACTUAL_INDEPENDENT_FILL_REJECTED_COUNTERMODEL_CERTIFIED",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B38-ROUTEB-FILLED-INDEPENDENT-QUADRATURE-PAYLOAD",
        "inputs": {
            "source_push_candidate": rel(source_push_path),
            "current_validator_result": rel(current_validator_path),
            "minimal_lemma": rel(minimal_lemma_path),
            "proof_or_countermodel": rel(proof_counter_path),
            "closed_support_countermodel": rel(countermodel_path),
            "obligation_status": rel(obligation_path),
            "typed_row_functor_sublemma": rel(typed_functor_path),
        },
        "actual_current_validator_returncode": current_validator["returncode"],
        "actual_current_validator_stderr_lines": current_validator["stderr_lines"],
        "actual_route_B_accepts_now": False,
        "full_minimal_lemma_proved": proof_counter["full_minimal_lemma_proved"],
        "typed_row_functor_sublemma_proved": typed_functor["proved"],
        "typed_row_counts": typed_functor["row_counts"],
        "countermodel_to_support_only": countermodel,
        "obligation_status": obligation["obligations"],
        "missing_actual_independent_fields": route_b_missing,
        "why_not_actual_fill": (
            "The current material fills row shapes and algebraic values, but the countermodel proves these support facts do not force source-promotion. "
            "The strict validator still rejects because the values are not emitted by independent selected source ids before residual replay."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    local = {
        "schema": "MTTConstEW02B38LocalPrincipleConditionalClosureBoundary.v1",
        "status": "LOCAL_PREMISE_CONDITIONAL_CLOSURE_SEPARATED_FROM_UNPATCHED_PROOF",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B38-LOCAL-PREMISE-BOUNDARY",
        "hypothesis": local_closure["hypothesis"],
        "conditional_kernel_closed": local_apply["closure_decision"]["local_pre_residual_kernel_closed"],
        "strict_pre_residual_kernel_closed_under_local_principle": local_apply["what_closes_now"][
            "strict_pre_residual_kernel_closed_under_local_principle"
        ],
        "does_not_close": local_closure["does_not_close"],
        "remaining_unpatched_exits": local_exit["remaining_unpatched_exits"],
        "allowed_use": "May be recorded as a local-premise/paper-axiom route or one-universal-principle tier, not as strict unpatched no-knob derivation.",
        "forbidden_use": "May not be cited as actual unpatched B38 proof/fill.",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    nogo = {
        "schema": "MTTConstEW02B38UnpatchedCurrentMaterialNoGo.v1",
        "status": "DECISIVE_CURRENT_MATERIAL_NOGO_FOR_ACTUAL_UNPATCHED_PROOF_OR_FILL",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B38-NO-GO-CURRENT-MATERIAL",
        "proof_basis": {
            "strict_validator_rejects_current_two_exit_packet": current_validator["returncode"] != 0,
            "closed_support_not_enough_countermodel": proof_counter["what_closes_now"]["closed_support_not_enough_countermodel"],
            "full_minimal_source_promotion_lemma_proved": proof_counter["full_minimal_lemma_proved"],
            "local_principle_is_not_unpatched": local_apply["closure_decision"]["unpatched_principle_derived_now"] is False,
        },
        "conclusion": (
            "From the current corpus/repo material alone, B38 cannot be honestly closed as an actual unpatched proof or actual independent fill. "
            "A new source kernel must be emitted, or the local Weyl-variation principle must be explicitly accepted as an added premise/tier."
        ),
        "next_kernel_required": next_kernel,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B38Boundary.v1",
        "status": "B38_BOTH_ROUTES_ATTEMPTED_DECISIVE_CURRENT_MATERIAL_NOGO",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B38-BOUNDARY",
        "previous_B37": {
            "candidate": b37["candidate"],
            "status": b37["status"],
            "still_open": b37_boundary["still_open"],
        },
        "closed_or_decided_now": {
            "Route_A_actual_unpatched_proof_attempted": True,
            "Route_A_actual_unpatched_proof_closed": False,
            "Route_A_local_principle_conditional_kernel_closed": True,
            "Route_B_actual_independent_payload_fill_attempted": True,
            "Route_B_actual_independent_payload_fill_closed": False,
            "typed_row_functor_sublemma_proved": True,
            "closed_support_not_enough_countermodel_imported": True,
            "current_material_no_go_for_unpatched_B38": True,
        },
        "still_open": {
            "derive_SelectedWeylVariationActionPrinciple_unpatched": True,
            "emit_PreResidualVariationAndHessianSourceKernel": True,
            "same_source_b_selected_emission_unpatched": True,
            "actual_independent_110_row_source_values": True,
            "selected_source_promotion": True,
            "physical_weak_angle_closure": True,
            "strict_full_no_knob_closure": True,
        },
        "superset_strategy": {
            "straight_way_or_combined": "both superset paths were tested against the same strict B38 validator boundary",
            "route_A": "passes only under explicit local Weyl-variation principle, not unpatched",
            "route_B": "proves typed row functor but fails actual independent source-value promotion",
            "locked_target": "same 110-row finite C1 source packet and weak-mixing dynamic C1 bridge",
            "credibility_guardrail": "conditional/local-premise closure is separated from strict no-knob closure",
        },
        "anti_cycle_delta_from_B37": {
            "B37": "formal RA2 support and RB4 schema imported",
            "B38": "actual proof/fill attempted and rejected by validator/countermodel under current unpatched material",
            "not_repeated": [
                "not another schema import",
                "not another algebraic 110-row replay",
                "not treating local principle as unpatched proof",
            ],
        },
        "allowed_claim": "B38 proves a decisive current-material no-go for actual unpatched proof/fill and preserves a conditional local-premise closure lane.",
        "forbidden_claim": "actual unpatched physical action identity, filled independent payload, physical weak-angle closure, or strict no-knob closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B38NextWork.v1",
        "status": "NEXT_WORKORDER_NEW_SOURCE_KERNEL_OR_EXPLICIT_LOCAL_PREMISE_TIER",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B39-SOURCE-KERNEL-OR-LOCAL-PREMISE-DECISION",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B39-PRERESIDUAL-VARIATION-HESSIAN-SOURCE-KERNEL",
            "task": "Construct a new source-owned kernel emitting the selected variation functional, same-source Hessian/b_selected, sector functor, and independence certificate before residual replay.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B39-LOCAL-WEYLVARIATION-PRINCIPLE-TIER",
            "task": "If acceptable, formalize SelectedWeylVariationActionPrinciple as an explicit local/universal principle tier and keep it separate from strict unpatched no-knob closure.",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB38ActualProofFillAttempt",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B38-ACTION-IDENTITY-OR-RB4-PAYLOAD-FILL",
        "output_packets": {
            "route_a_physical_action_identity_actual_attempt": rel(ROUTE_A),
            "route_b_independent_payload_actual_fill_attempt": rel(ROUTE_B),
            "local_principle_conditional_closure_boundary": rel(LOCAL),
            "unpatched_current_material_no_go": rel(NOGO),
            "weak_mixing_b38_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B38ActualProofFillAttemptAndCurrentMaterialNoGoTheorem",
            "proved": True,
            "statement": (
                "Both B38 exits were tested against the current corpus/repo material. Route A closes only under an explicit local SelectedWeylVariationActionPrinciple premise and is not unpatched. Route B proves the typed 110-row functor shape but the existing strict validator rejects actual source promotion, and the closed-support countermodel proves that algebraic values plus support facts do not imply independent selected source emission. Therefore current material cannot honestly close B38 without a new pre-residual variation/Hessian source kernel or explicit acceptance of the local principle tier."
            ),
        },
        "Route_A_actual_unpatched_proof_closed": False,
        "Route_A_local_principle_conditional_kernel_closed": True,
        "Route_B_actual_independent_payload_fill_closed": False,
        "typed_row_functor_sublemma_proved": True,
        "closed_support_not_enough_countermodel": True,
        "current_material_no_go_for_unpatched_B38": True,
        "source_promotion_closed_now": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B38_ActualProofFillAttempt_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "Route_A_actual_unpatched_proof_closed": False,
        "Route_A_local_principle_conditional_kernel_closed": True,
        "Route_B_actual_independent_payload_fill_closed": False,
        "typed_row_functor_sublemma_proved": True,
        "closed_support_not_enough_countermodel": True,
        "current_material_no_go_for_unpatched_B38": True,
        "source_promotion_closed_now": False,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B38 Actual Proof Fill Attempt v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B38-ACTION-IDENTITY-OR-RB4-PAYLOAD-FILL`

## Result

```text
Route A actual unpatched proof closed          False
Route A local-principle conditional close      True
Route B actual independent payload fill closed False
typed 110-row functor sublemma proved          True
closed-support countermodel imported           True
current-material unpatched B38 no-go           True
```

This is not a cycle. It is a stop sign for the current assumptions: the support
facts and algebraic row values are insufficient to promote source ownership.

## Next

`CONST-EW-02 / WEAK-MIXING / B39-SOURCE-KERNEL-OR-LOCAL-PREMISE-DECISION`
"""

    for path, payload in [
        (ROUTE_A, route_a),
        (ROUTE_B, route_b),
        (LOCAL, local),
        (NOGO, nogo),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
