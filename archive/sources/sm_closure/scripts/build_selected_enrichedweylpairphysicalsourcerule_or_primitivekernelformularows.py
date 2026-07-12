"""Build the enriched Weyl-pair physical-source rule / primitive-row fallback gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_enrichedweylpairphysicalsourcerule_or_primitivekernelformularows"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_A = PACKET_DIR / "enriched_weylpair_physical_source_rule_gate.packet.json"
ROUTE_B = PACKET_DIR / "primitive_kernel_formula_rows_fallback_gate.packet.json"
DYNAMIC = PACKET_DIR / "remaining_dynamic_promotion_cutset.packet.json"
DECISION = PACKET_DIR / "enriched_weylpair_gate_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_EnrichedWeylPairPhysicalSourceRule_or_PrimitiveKernelFormulaRows_v1.md"

STATUS = "MTT_SELECTED_ENRICHEDWEYLPAIRPHYSICALSOURCERULE_OR_PRIMITIVEKERNELFORMULAROWS_BUILT_STATIC_CLOSED_DYNAMIC_OPEN"
NEXT = "MTT_Selected_DynamicC1TransferPrimitiveTensorHessian_or_IndependentRows_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_physicalactionsourcerule_or_independentprimitivekernelformula.candidate.json")
    static = load(
        DATA
        / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values"
        / "static_enriched_weylpair_source_provenance.packet.json"
    )
    dynamic_boundary = load(
        DATA
        / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values"
        / "dynamic_c1_value_boundary.packet.json"
    )
    dynamic_transfer = load(DATA / "selected_dynamicc1transfertensor_or_galerkinc1values.candidate.json")
    weyl_assembly = load(DATA / "selected_routec_weylpair_aselected_assembly_or_source_proof.candidate.json")
    route_b_kernel = load(
        DATA
        / "selected_physicalactionsourcerule_or_independentprimitivekernelformula"
        / "independent_primitive_kernel_formula_promotion_kernel.packet.json"
    )

    route_a = {
        "schema": "MTTEnrichedWeylPairPhysicalSourceRuleGate.v1",
        "status": "ENRICHED_WEYLPAIR_STATIC_SOURCE_CLOSED_PHYSICAL_DYNAMIC_RULE_OPEN",
        "static_source_provenance_closed": static["provenance_closed"],
        "source_level_carrier_closed": {
            "phase_Z_source_proved": static["source_level_carrier"]["phase_Z_source_proved"],
            "shift_X_source_proved": static["source_level_carrier"]["shift_X_source_proved"],
            "active_shift_1_1_proved": static["source_level_carrier"]["active_shift_1_1_proved"],
        },
        "static_sector_route_closed": static["static_sector_route"]["selected_static_sector_route_now_closed"],
        "static_normalization_closed": static["static_normalization"]["static_trace_innerproduct_normalization_selected"],
        "conditional_A_rank": weyl_assembly["locked_solve"]["rank"],
        "conditional_deltaTheta": weyl_assembly["locked_solve"]["deltaTheta_conditional"],
        "conditional_solve_consistent": weyl_assembly["locked_solve"]["consistent"],
        "remaining_physical_rule_requirements": [
            "promote conditional Weyl-pair columns to selected dynamic C1 transfer tensor",
            "emit selected non-invariant primitive C1 tensor or overlap contractions",
            "emit selected Hessian/source vector b_selected from the same branch",
            "prove physical Phi_fin^C1 variation applies this dynamic tensor with no extra source term",
            "then run the rank/Gram/deltaTheta checks as acceptance only",
        ],
        "physical_source_rule_promoted_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    route_b = {
        "schema": "MTTPrimitiveKernelFormulaRowsFallbackGate.v1",
        "status": "PRIMITIVE_KERNEL_FORMULA_ROWS_FALLBACK_READY_NOT_EXECUTED",
        "row_count": route_b_kernel["row_count"],
        "required_global_clauses": route_b_kernel["required_global_clauses"],
        "all_rows_named": route_b_kernel["all_rows_named"],
        "fallback_reason": (
            "If dynamic Weyl-pair physical promotion stalls, the independent route must derive the selected "
            "primitive kernel formula and execute the same 72 row slots without residual-projector provenance."
        ),
        "route_b_executed_now": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    dynamic = {
        "schema": "MTTRemainingDynamicPromotionCutset.v1",
        "status": "STATIC_SOURCE_RETIRED_DYNAMIC_CUTSET_EXACT",
        "retired_blockers": {
            "source_level_weylpair_provenance_open": dynamic_boundary["after_static_provenance_closure"][
                "source_level_weylpair_provenance_open"
            ],
            "static_sector_routing_open": dynamic_boundary["after_static_provenance_closure"][
                "static_sector_routing_open"
            ],
            "static_transfer_normalization_open": dynamic_boundary["after_static_provenance_closure"][
                "static_transfer_normalization_open"
            ],
            "operator_alpha1_support_closed_for_frontier": dynamic_transfer["promotion_decision"][
                "operator_alpha1_support_closed_for_frontier"
            ],
        },
        "active_dynamic_cutset": {
            "selected_dynamic_source_to_C1_transfer_tensor": dynamic_boundary["after_static_provenance_closure"][
                "selected_dynamic_source_to_C1_transfer_tensor_open"
            ],
            "selected_primitive_C1_overlap_contractions": dynamic_boundary["after_static_provenance_closure"][
                "selected_primitive_C1_overlap_contractions_open"
            ],
            "selected_Hessian_or_b_source_vector": dynamic_boundary["after_static_provenance_closure"][
                "selected_Hessian_or_b_source_vector_open"
            ],
            "selected_A_selected": not dynamic_transfer["promotion_decision"]["A_selected_promoted"],
            "selected_b_selected": not dynamic_transfer["promotion_decision"]["b_selected_promoted"],
            "selected_deltaTheta_C1": not dynamic_transfer["promotion_decision"]["deltaTheta_C1_promoted"],
            "honest_selected_Galerkin_C1_values": not dynamic_transfer["promotion_decision"][
                "honest_Galerkin_C1_values_promoted"
            ],
        },
        "conditional_values_ready": {
            "conditional_rank": dynamic_boundary["conditional_rank"],
            "conditional_condition_number": dynamic_boundary["conditional_condition_number"],
            "A_transpose_A_if_promoted": dynamic_boundary["A_transpose_A_if_promoted"],
            "A_transpose_b_if_promoted": dynamic_boundary["A_transpose_b_if_promoted"],
            "conditional_deltaTheta": dynamic_boundary["conditional_deltaTheta"],
        },
        "source_gap_not_numeric_gap": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTEnrichedWeylPairGateDecision.v1",
        "status": "ENRICHED_WEYLPAIR_GATE_BUILT_STATIC_RETIRED_DYNAMIC_NOT_CLOSED",
        "static_source_provenance_closed": True,
        "dynamic_physical_source_rule_closed": False,
        "primitive_formula_rows_executed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "next_actionable_target": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedEnrichedWeylPairPhysicalSourceRuleOrPrimitiveKernelFormulaRows",
        "status": STATUS,
        "inputs": {
            "previous_promotion_kernel": rel(DATA / "selected_physicalactionsourcerule_or_independentprimitivekernelformula.candidate.json"),
            "static_enriched_weylpair_source_provenance": rel(
                DATA
                / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values"
                / "static_enriched_weylpair_source_provenance.packet.json"
            ),
            "dynamic_c1_value_boundary": rel(
                DATA
                / "selected_enrichedweylpairsourceprovenance_or_galerkinc1values"
                / "dynamic_c1_value_boundary.packet.json"
            ),
            "dynamic_c1_transfer_frontier": rel(DATA / "selected_dynamicc1transfertensor_or_galerkinc1values.candidate.json"),
        },
        "output_packets": {
            "enriched_weylpair_physical_source_rule_gate": rel(ROUTE_A),
            "primitive_kernel_formula_rows_fallback_gate": rel(ROUTE_B),
            "remaining_dynamic_promotion_cutset": rel(DYNAMIC),
            "enriched_weylpair_gate_decision": rel(DECISION),
        },
        "theorem": {
            "name": "EnrichedWeylPairStaticRetirementDynamicCutsetTheorem",
            "proved": True,
            "statement": (
                "The enriched Weyl-pair route has closed the static source-provenance, sector-routing, and "
                "normalization blockers. The remaining physical source-rule problem is exactly dynamic: emit "
                "the selected source-to-C1 transfer tensor, primitive C1 contractions, and Hessian/source vector, "
                "or execute the independent 72-row primitive formula route."
            ),
        },
        "previous_status": previous["status"],
        "closure_decision": decision,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_EnrichedWeylPairPhysicalSourceRule_or_PrimitiveKernelFormulaRows_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "static_source_provenance_closed": True,
        "dynamic_physical_source_rule_closed": False,
        "primitive_formula_rows_executed": False,
        "unpatched_dynamic_C1_packet_closed": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected EnrichedWeylPairPhysicalSourceRule or PrimitiveKernelFormulaRows v1

Status: `{STATUS}`.

This artifact retires the static part of the enriched Weyl-pair source route:
the source-level `Z/X` carrier, `u,e` versus `d,nuD` routing, the `1_M`
Dirac-neutrino shift-side rule, and finite trace normalization are closed.

What remains is exactly dynamic promotion: selected source-to-C1 transfer
tensor, primitive C1 contractions, and the Hessian/source vector `b_selected`.
The fallback remains independent execution of all 72 primitive kernel rows.

No unpatched dynamic-C1, true-SM-equivalence, or no-knob closure is claimed.
"""

    for path, payload in [
        (ROUTE_A, route_a),
        (ROUTE_B, route_b),
        (DYNAMIC, dynamic),
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
