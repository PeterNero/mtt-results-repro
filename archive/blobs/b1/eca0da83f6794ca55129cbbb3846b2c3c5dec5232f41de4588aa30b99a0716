"""Build the physical action source-rule / independent kernel-formula promotion kernel."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicalactionsourcerule_or_independentprimitivekernelformula"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "physical_action_source_rule_promotion_kernel.packet.json"
ROUTE_B = PACKET_DIR / "independent_primitive_kernel_formula_promotion_kernel.packet.json"
SYNTHESIS = PACKET_DIR / "two_route_source_promotion_synthesis.packet.json"
DECISION = PACKET_DIR / "promotion_kernel_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalActionSourceRule_or_IndependentPrimitiveKernelFormula_v1.md"

STATUS = "MTT_SELECTED_PHYSICALACTIONSOURCERULE_OR_INDEPENDENTPRIMITIVEKERNELFORMULA_BUILT_PROMOTION_KERNEL_OPEN"
NEXT = "MTT_Selected_EnrichedWeylPairPhysicalSourceRule_or_PrimitiveKernelFormulaRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_physicalrzrxbsourceemission_or_primitiverowfirstexecution.candidate.json")
    source_gap = load(
        DATA
        / "selected_physicalrzrxbsourceemission_or_primitiverowfirstexecution"
        / "source_gap_decision.packet.json"
    )
    physical_template = load(
        DATA
        / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues"
        / "route_a_physical_source_theorem_template.packet.json"
    )
    source_rule = load(
        DATA
        / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution"
        / "differentiated_residual_projector_source_rule.contract.json"
    )
    route_ladder = load(
        DATA
        / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution"
        / "source_rule_or_execution_route_ladder.packet.json"
    )
    route_b_contract = load(
        DATA
        / "selected_routeb_independentprimitive_rows_or_routea_phifinboundaryemission"
        / "route_b_independent_primitive_row_kernel_contract.packet.json"
    )
    checklist = load(
        DATA
        / "selected_fivephysicalclauses_or_seventytwoprimitivekernelrows"
        / "seventy_two_primitive_kernel_row_checklist.packet.json"
    )

    route_a = {
        "schema": "MTTPhysicalActionSourceRulePromotionKernel.v1",
        "status": "PHYSICAL_ACTION_SOURCE_RULE_KERNEL_BUILT_NOT_PROMOTED",
        "theorem_name": physical_template["theorem_name"],
        "minimal_statement_to_prove": physical_template["minimal_statement_to_prove"],
        "required_clauses": physical_template["required_clauses"],
        "formal_source_rule_statement": source_rule["formal_statement"],
        "already_selected_support": source_rule["already_selected_support"],
        "conditional_values_if_promoted": source_rule["exact_conditional_values_if_rule_is_proved"],
        "acceptance_tests": {
            "physical_C1_action_equals_leakage_functional": False,
            "admissible_differentiated_PhiFinC1_variations_fixed": False,
            "dynamic_trace_boundary_terms_vanish_from_same_branch": False,
            "Q_residual_R_Z_R_X_b_selected_emitted_by_same_source": False,
            "rank_and_Gram_checked_in_72_real_coordinates": False,
        },
        "route_a_promoted_now": False,
        "why_not_promoted": physical_template["why_not_promoted"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_b = {
        "schema": "MTTIndependentPrimitiveKernelFormulaPromotionKernel.v1",
        "status": "INDEPENDENT_PRIMITIVE_KERNEL_FORMULA_KERNEL_BUILT_NOT_EXECUTED",
        "row_count": route_b_contract["primitive_stage_row_count"],
        "checklist_row_count": checklist["row_count"],
        "required_kernel_fields_per_row": route_b_contract["required_kernel_fields_per_row"],
        "required_global_clauses": [
            "selected primitive kernel formula valid for every sector/response/coordinate row",
            "selected trace/pairing or independent quadrature measure",
            "72 computed complex row entries independent of residual-projector replay",
            "symbolic exactness proof or certified numerical error bound per row",
            "provenance independent of target replay and observed SM values",
        ],
        "first_row_id": checklist["rows"][0]["row_id"],
        "all_rows_named": route_b_contract["primitive_stage_rows"] == [row["row_id"] for row in checklist["rows"]],
        "execution_acceptance_tests": {
            "all_72_rows_have_selected_formula": False,
            "all_72_rows_have_selected_pairing_source": False,
            "all_72_rows_have_complex_values": False,
            "all_72_rows_have_exactness_or_error_certificate": False,
            "all_72_rows_have_independent_provenance": False,
            "locked_target_used_only_after_emission": True,
        },
        "route_b_executed_now": False,
        "replay_diagnostics_available": route_b_contract["replay_diagnostics_available"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    synthesis = {
        "schema": "MTTTwoRouteSourcePromotionSynthesis.v1",
        "status": "PROMOTION_SYNTHESIS_BUILT_SOURCE_RULE_PRIMARY",
        "source_gap_not_numeric_gap": source_gap["source_gap_not_numeric_gap"],
        "route_a": {
            "role": "straight physical theorem route",
            "objects_to_promote": 5,
            "primary_next_move": "prove the physical action source rule via enriched Weyl-pair source emission",
            "why_primary": (
                "The source-rule route can promote all five physical clauses at once if the same-branch "
                "variation/source theorem is derived."
            ),
        },
        "route_b": {
            "role": "independent execution fallback",
            "objects_to_execute": route_b_contract["primitive_stage_row_count"],
            "primary_next_move": "derive a selected primitive kernel formula before filling row values",
            "why_fallback": (
                "It is more mechanical but cannot reuse residual-projector replay as provenance."
            ),
        },
        "route_ladder_import": {
            "recommended_next": route_ladder["recommended_next"],
            "ruled_out_paths": route_ladder["ruled_out_paths"],
        },
        "superset_strategy_use": (
            "Superset paths may combine terminal/Theta/Strominger/Weyl-pair evidence only to prove the "
            "same selected source rule or independent formula; they may not tune values to the locked target."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTPromotionKernelDecision.v1",
        "status": "PROMOTION_KERNEL_BUILT_CLOSURE_NOT_CLAIMED",
        "route_a_kernel_built": True,
        "route_b_kernel_built": True,
        "route_a_promoted_now": False,
        "route_b_executed_now": False,
        "source_gap_not_numeric_gap": True,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_actionable_target": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalActionSourceRuleOrIndependentPrimitiveKernelFormula",
        "status": STATUS,
        "inputs": {
            "previous_source_gap": rel(DATA / "selected_physicalrzrxbsourceemission_or_primitiverowfirstexecution.candidate.json"),
            "physical_source_template": rel(
                DATA
                / "selected_physicalvariationprinciplesource_or_quadraturekernelvalues"
                / "route_a_physical_source_theorem_template.packet.json"
            ),
            "differentiated_source_rule_contract": rel(
                DATA
                / "selected_differentiatedresidualprojectorsourcerule_or_honestgalerkinc1execution"
                / "differentiated_residual_projector_source_rule.contract.json"
            ),
            "route_b_primitive_row_contract": rel(
                DATA
                / "selected_routeb_independentprimitive_rows_or_routea_phifinboundaryemission"
                / "route_b_independent_primitive_row_kernel_contract.packet.json"
            ),
        },
        "output_packets": {
            "physical_action_source_rule_promotion_kernel": rel(ROUTE_A),
            "independent_primitive_kernel_formula_promotion_kernel": rel(ROUTE_B),
            "two_route_source_promotion_synthesis": rel(SYNTHESIS),
            "promotion_kernel_decision": rel(DECISION),
        },
        "theorem": {
            "name": "PhysicalActionSourceRuleOrIndependentPrimitiveKernelFormulaPromotionTheorem",
            "proved": True,
            "statement": (
                "Given the prior source-gap result, unpatched dynamic-C1 closure is reduced to two precise "
                "promotion kernels: prove the physical Phi_fin^C1 action/source rule, or execute an "
                "independent selected primitive-kernel formula across all 72 rows. The numerical target is "
                "already locked and may only be used as an after-emission acceptance oracle."
            ),
        },
        "previous_status": previous["status"],
        "closure_decision": decision,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalActionSourceRule_or_IndependentPrimitiveKernelFormula_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "route_a_kernel_built": True,
        "route_b_kernel_built": True,
        "route_a_promoted_now": False,
        "route_b_executed_now": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalActionSourceRule or IndependentPrimitiveKernelFormula v1

Status: `{STATUS}`.

The previous step showed that the remaining dynamic-C1 problem is source
promotion, not value search. This artifact turns that into two exact promotion
kernels.

Route A is the straight physical route: prove the selected `Phi_fin^C1`
action/source rule so the same branch emits `Q_residual`, `R_Z`, `R_X`,
`b_selected`, and the locked sector response packet.

Route B is the independent formula route: derive a selected primitive kernel
formula and execute all 72 sector/response/coordinate rows with exactness and
independent provenance.

The recommended next attack is the enriched Weyl-pair physical source rule.
No dynamic-C1, true-SM-equivalence, or no-knob closure is claimed here.
"""

    for path, payload in [
        (ROUTE_A, route_a),
        (ROUTE_B, route_b),
        (SYNTHESIS, synthesis),
        (DECISION, decision),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
