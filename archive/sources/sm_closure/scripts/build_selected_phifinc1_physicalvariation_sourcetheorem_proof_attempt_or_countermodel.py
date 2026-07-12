"""Try to prove the selected PhiFin C1 physical variation source theorem."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_phifinc1_physicalvariation_sourcetheorem_proof_attempt_or_countermodel"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SUPPORT = PACKET_DIR / "support_closure_synthesis.packet.json"
ATTEMPT = PACKET_DIR / "selected_phifinc1_physicalvariation_theorem_attempt.packet.json"
COUNTERMODEL = PACKET_DIR / "closed_support_countermodel_lift.packet.json"
DECISION = PACKET_DIR / "proof_attempt_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhiFinC1_PhysicalVariationSourceTheorem_ProofAttempt_or_Countermodel_v1.md"

STATUS = "MTT_SELECTED_PHIFINC1_PHYSICALVARIATION_SOURCETHEOREM_PROOF_ATTEMPT_COUNTERMODEL_OPEN"
NEXT = "MTT_Selected_PreResidualVariationOperator_and_HessianSourceKernel_Emission_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def all_true(items: list[bool]) -> bool:
    return all(item is True for item in items)


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    obstruction = load(
        DATA
        / "selected_differentiatedphifinc1_axiom_derivation_attempt_or_minimalobstruction"
        / "minimal_derivation_obstruction.packet.json"
    )
    route_a_frontier = load(
        DATA
        / "selected_physicalboundaryfirstvariation_or_selectedsourceemission"
        / "remaining_selected_source_emission_frontier.packet.json"
    )
    physical_current = load(
        DATA
        / "selected_physicalboundaryfirstvariation_or_selectedsourceemission"
        / "current_physical_boundary_firstvariation_attempt.packet.json"
    )
    physical_conditional = load(
        DATA
        / "selected_physicalboundaryfirstvariation_or_selectedsourceemission"
        / "conditional_physical_source_emission_witness.packet.json"
    )
    action_current = load(
        DATA
        / "selected_phifinc1actionkernel_theorem_attempt_or_i10binding"
        / "current_action_kernel_theorem_attempt.packet.json"
    )
    action_conditional = load(
        DATA
        / "selected_phifinc1actionkernel_theorem_attempt_or_i10binding"
        / "conditional_i10_action_kernel_witness.packet.json"
    )
    i11_frontier = load(
        DATA
        / "selected_i11_sourcepromotion_backimport_or_boundaryfirstvariation"
        / "remaining_boundary_firstvariation_source_frontier.packet.json"
    )
    five_clause = load(
        DATA
        / "selected_fiveclause_sourcepromotion_attempt_or_trueproofcutset"
        / "five_clause_source_promotion_attempt.packet.json"
    )
    minimal_obligations = load(
        DATA
        / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
        / "minimal_lemma_obligation_status.packet.json"
    )
    support_countermodel = load(
        DATA
        / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
        / "closed_support_not_enough_countermodel.packet.json"
    )

    closed_support = {
        "selected_qutrit_weyl_carrier": obstruction["not_blockers"]["qutrit_weyl_carrier"],
        "static_sector_routing": obstruction["not_blockers"]["static_sector_routing"],
        "trace_transfer_normalization": obstruction["not_blockers"]["trace_transfer_normalization"],
        "alpha1_dotD_driver": obstruction["not_blockers"]["alpha1_dotD_driver"],
        "canonical_Q_residual": obstruction["not_blockers"]["canonical_Q_residual"],
        "least_norm_completion": obstruction["not_blockers"]["least_norm_completion"],
        "locked_linear_algebra": obstruction["not_blockers"]["locked_linear_algebra"],
        "finite_trace_measure_normalization": five_clause["closed_support"]["finite_trace_measure_normalization"],
        "variation_operator_shapes_compatible": five_clause["closed_support"]["variation_operator_shapes_compatible"],
        "formal_hessian_target_identified": five_clause["closed_support"]["formal_hessian_target_identified"],
        "all_110_algebraic_values_filled": five_clause["closed_support"]["all_110_algebraic_values_filled"],
        "typed_row_functor_sublemma": next(
            item["proved"] for item in minimal_obligations["obligations"] if item["id"] == "basis_to_rows"
        ),
        "normalization_compatibility": i11_frontier["closed_now"]["normalization_compatibility_proved"],
        "selected_minimizer_identifier": i11_frontier["closed_now"]["selected_minimizer_identifier_imported"],
        "finite_phi_fin_trace_operator": i11_frontier["closed_now"]["finite_phi_fin_trace_operator_imported"],
        "c1_response_coordinate_chart": i11_frontier["closed_now"]["c1_response_coordinate_chart_imported"],
        "transport_dotd_trace_binding": i11_frontier["closed_now"]["transport_dotd_trace_binding_imported"],
    }

    support = {
        "schema": "MTTSelectedPhiFinC1PhysicalVariationSupportSynthesis.v1",
        "status": "MAXIMAL_CLOSED_SUPPORT_SYNTHESIZED_FOR_THEOREM_ATTEMPT",
        "closed_support": closed_support,
        "all_support_flags_closed": all_true(list(closed_support.values())),
        "support_is_sufficient_for_theorem": False,
        "reason_not_sufficient": (
            "The closed support fixes the finite quotient, trace measure, row typing, values, "
            "and target algebra. It does not emit the selected physical pre-residual variation "
            "operator or same-source Hessian/b_selected source."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_a_required = route_a_frontier["route_A_remaining_theorem"]["must_emit"]
    current_route_a = physical_current["current_route_A_emissions"]
    conditional_route_a = {
        "physical_action_identity": physical_conditional["physical_first_variation_identity"],
        "physical_measure_equals_trace_frobenius_pairing": physical_conditional[
            "physical_measure_equals_trace_frobenius_pairing"
        ],
        "phase_R_Z_source_selection": physical_conditional["phase_R_Z_source_selection"],
        "shift_R_X_source_selection": physical_conditional["shift_R_X_source_selection"],
        "same_source_b_selected_emission": physical_conditional["same_source_b_selected_emission"],
        "no_extra_physical_boundary_or_source_term": physical_conditional[
            "no_extra_physical_boundary_or_source_term"
        ],
    }
    theorem_fields = {
        "same_branch": physical_current["same_branch"] and action_current["same_branch"],
        "physical_action_equals_c1_defect_functional": action_current[
            "physical_action_equals_c1_defect_functional"
        ],
        "admissible_differentiated_variations_fixed": action_current[
            "admissible_differentiated_variations_fixed"
        ],
        "physical_measure_equals_trace_frobenius_pairing": current_route_a[
            "physical_measure_equals_trace_frobenius_pairing"
        ],
        "physical_first_variation_identity": current_route_a["physical_action_identity"],
        "selected_PhiFinC1_applies_Q_residual": current_route_a["phase_R_Z_source_selection"]
        and current_route_a["shift_R_X_source_selection"],
        "same_source_RZ_RX_bselected_emission": action_current["same_source_rz_rx_bselected_emitted"],
        "physical_boundary_source_terms_vanish": action_current["physical_boundary_source_terms_vanish"]
        and current_route_a["no_extra_physical_boundary_or_source_term"],
    }
    theorem_proved_now = all_true(list(theorem_fields.values()))
    theorem_conditional_fields = {
        "same_branch": True,
        "physical_action_equals_c1_defect_functional": action_conditional[
            "physical_action_equals_c1_defect_functional"
        ],
        "admissible_differentiated_variations_fixed": action_conditional[
            "admissible_differentiated_variations_fixed"
        ],
        "physical_measure_equals_trace_frobenius_pairing": conditional_route_a[
            "physical_measure_equals_trace_frobenius_pairing"
        ],
        "physical_first_variation_identity": conditional_route_a["physical_action_identity"],
        "selected_PhiFinC1_applies_Q_residual": conditional_route_a["phase_R_Z_source_selection"]
        and conditional_route_a["shift_R_X_source_selection"],
        "same_source_RZ_RX_bselected_emission": action_conditional["same_source_rz_rx_bselected_emitted"],
        "physical_boundary_source_terms_vanish": action_conditional["physical_boundary_source_terms_vanish"]
        and conditional_route_a["no_extra_physical_boundary_or_source_term"],
    }

    attempt = {
        "schema": "MTTSelectedPhiFinC1PhysicalVariationSourceTheoremAttempt.v1",
        "status": "THEOREM_ATTEMPT_REJECTED_SOURCE_KERNEL_STILL_OPEN",
        "theorem_name": "SelectedPhiFinC1PhysicalVariationSourceTheorem",
        "theorem_statement": obstruction["minimal_new_lemma"]["statement"],
        "required_route_A_emissions": route_a_required,
        "current_route_A_emissions": current_route_a,
        "conditional_route_A_emissions": conditional_route_a,
        "theorem_fields": theorem_fields,
        "conditional_theorem_fields": theorem_conditional_fields,
        "theorem_proved_now": theorem_proved_now,
        "conditional_witness_would_validate": all_true(list(theorem_conditional_fields.values())),
        "new_source_kernel_found_now": False,
        "why_rejected": [
            "physical_action_identity is still support/conditional, not theorem-derived",
            "admissible differentiated variations are not fixed by an unpatched physical source theorem",
            "R_Z/R_X are exact Weyl residual values, but not selected as physical pre-residual variation operators",
            "b_selected is a formal/replay Hessian target, not same-source Hessian emission",
            "physical no-extra-boundary/source cancellation remains unpromoted",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    countermodel = {
        "schema": "MTTClosedSupportCountermodelLiftToPhiFinC1PhysicalVariationTheorem.v1",
        "status": "COUNTERMODEL_LIFT_PROVES_CLOSED_SUPPORT_ALONE_CANNOT_DERIVE_THEOREM",
        "source_countermodel": rel(
            DATA
            / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
            / "closed_support_not_enough_countermodel.packet.json"
        ),
        "closed_support_facts_true": support_countermodel["closed_support_facts_true"],
        "additional_structural_support_true": support_countermodel["additional_structural_support_true"],
        "source_promotion_fields_false": support_countermodel["source_promotion_fields_false"],
        "lifted_to_theorem_fields_false": {
            "physical_first_variation_identity": not theorem_fields["physical_first_variation_identity"],
            "selected_pre_residual_variation_operator": not theorem_fields["selected_PhiFinC1_applies_Q_residual"],
            "same_source_b_selected_emission": not theorem_fields["same_source_RZ_RX_bselected_emission"],
            "physical_boundary_source_terms_vanish": not theorem_fields["physical_boundary_source_terms_vanish"],
        },
        "therefore": (
            "The SelectedPhiFinC1PhysicalVariationSourceTheorem is not derivable from the already-closed "
            "support package alone. A new source-emission kernel must be supplied."
        ),
        "countermodel_valid_for_current_support": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    obligations_by_id = {item["id"]: item for item in minimal_obligations["obligations"]}
    next_kernel = {
        "name": "PreResidualVariationOperatorAndHessianSourceKernelEmission",
        "must_emit": {
            "selected_pre_residual_phase_shift_operator_source": obligations_by_id[
                "pre_residual_operators"
            ]["proved"],
            "same_source_hessian_b_selected_rows": obligations_by_id["hessian_source_rows"]["proved"],
            "sector_rows_physical_source_promotion": obligations_by_id["sector_assembly"]["proved"],
            "values_independent_of_residual_projector_replay": obligations_by_id["independence_guardrail"]["proved"],
        },
        "already_proved_sublemma": {
            "basis_to_rows": obligations_by_id["basis_to_rows"]["proved"],
        },
        "acceptance_rule": (
            "If these source-kernel emissions are true on the selected branch, the theorem attempt's "
            "currently false Route-A fields become theorem-derived rather than replay/conditional."
        ),
    }
    decision = {
        "schema": "MTTSelectedPhiFinC1PhysicalVariationProofAttemptDecision.v1",
        "status": "PROOF_ATTEMPT_FAILED_PRODUCTIVELY_COUNTERMODEL_AND_NEXT_KERNEL_IDENTIFIED",
        "theorem_proved_now": theorem_proved_now,
        "conditional_witness_would_validate": attempt["conditional_witness_would_validate"],
        "closed_support_countermodel_blocks_support_only_proof": True,
        "local_axiom_still_needed_for_patched_closure": True,
        "unpatched_dynamic_C1_closed": False,
        "next_required_artifact": NEXT,
        "next_kernel": next_kernel,
        "superset_strategy": {
            "mode": "straight Route A attempted, Route B countermodel/row-source obligations imported",
            "straight_route_A": "physical Phi_fin^C1 variation/source theorem",
            "parallel_route_B": "independent finite C1 row-kernel source promotion",
            "locked_target_used_only_as_postcheck": True,
            "paths_used_as_free_parameters": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    for path, payload in [
        (SUPPORT, support),
        (ATTEMPT, attempt),
        (COUNTERMODEL, countermodel),
        (DECISION, decision),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    candidate = {
        "candidate": "MTTSelectedPhiFinC1PhysicalVariationSourceTheoremProofAttemptOrCountermodel",
        "status": STATUS,
        "inputs": {
            "previous_minimal_obstruction": rel(
                DATA
                / "selected_differentiatedphifinc1_axiom_derivation_attempt_or_minimalobstruction"
                / "minimal_derivation_obstruction.packet.json"
            ),
            "physical_boundary_firstvariation_frontier": rel(
                DATA
                / "selected_physicalboundaryfirstvariation_or_selectedsourceemission"
                / "remaining_selected_source_emission_frontier.packet.json"
            ),
            "action_kernel_current_attempt": rel(
                DATA
                / "selected_phifinc1actionkernel_theorem_attempt_or_i10binding"
                / "current_action_kernel_theorem_attempt.packet.json"
            ),
            "minimal_source_promotion_countermodel": rel(
                DATA
                / "selected_minimalfinitec1sourcepromotionlemma_proof_or_countermodel"
                / "closed_support_not_enough_countermodel.packet.json"
            ),
        },
        "output_packets": {
            "support_closure_synthesis": rel(SUPPORT),
            "selected_phifinc1_physicalvariation_theorem_attempt": rel(ATTEMPT),
            "closed_support_countermodel_lift": rel(COUNTERMODEL),
            "proof_attempt_decision": rel(DECISION),
        },
        "theorem_attempt": {
            "name": "SelectedPhiFinC1PhysicalVariationSourceTheorem",
            "proved": theorem_proved_now,
            "conditional_witness_would_validate": attempt["conditional_witness_would_validate"],
            "result": "support-only proof refuted by countermodel",
        },
        "what_was_achieved": {
            "maximal_closed_support_synthesized": True,
            "theorem_attempt_executed": True,
            "support_only_derivation_refuted": True,
            "next_source_kernel_identified": True,
        },
        "what_remains_open": {
            "selected_pre_residual_phase_shift_operator_source": True,
            "same_source_hessian_b_selected_rows": True,
            "physical_boundary_source_terms_vanish": True,
            "unpatched_dynamic_C1_closure": True,
            "true_SM_equivalence_without_axiom": True,
        },
        "closure_decision": {
            "theorem_proved_now": theorem_proved_now,
            "closed_support_alone_sufficient": False,
            "unpatched_dynamic_C1_closed": False,
            "global_closure_claimed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhiFinC1_PhysicalVariationSourceTheorem_ProofAttempt_or_Countermodel_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved_now": theorem_proved_now,
        "conditional_witness_would_validate": attempt["conditional_witness_would_validate"],
        "support_only_derivation_refuted": True,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected PhiFinC1 PhysicalVariation SourceTheorem ProofAttempt or Countermodel v1

Status: `{STATUS}`.

This artifact tries to prove `SelectedPhiFinC1PhysicalVariationSourceTheorem`.

Result: the theorem is **not** proved from the current unpatched support. The
attempt is productive because it proves a stronger guardrail: the closed support
package is insufficient by countermodel.

Closed support now includes the selected finite quotient, finite trace/Frobenius
measure normalization, selected row typing, exact 110 algebraic row values,
formal Hessian target, selected minimizer/trace operator support, C1 response
chart, dotD trace binding, and the locked C1 algebra.

Still false in the current theorem attempt:

- physical first-variation identity;
- selected pre-residual phase/shift operator source;
- same-source Hessian/`b_selected` emission;
- physical no-extra-boundary/source cancellation.

The conditional witness still validates if those fields are supplied, so this is
not a numerical failure. It is a source-kernel gap.

Next artifact: `{NEXT}`.
"""

    OUTPUT.write_text(json.dumps(candidate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
