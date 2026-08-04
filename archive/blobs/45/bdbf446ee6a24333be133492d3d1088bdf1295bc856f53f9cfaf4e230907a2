"""Formulate the same-source fusion gate for the monad/GS/operator selector.

The previous audits show that several pieces are closed separately:

* terminal monad-difference arithmetic and conditional uniqueness,
* time-oriented m=1 finite gerbe representative,
* visible Green-Schwarz curvature row,
* Route C finite validator pipeline in lifted smoke mode.

This script prevents an invalid proof by patchwork.  It records the exact
single-source packet that would be sufficient to turn those pieces into a
selected monad-difference source with Pic0 resolved.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
CANDIDATES = ROOT / "candidate_data"

UNCONDITIONAL_MONAD = CERTS / "unconditional_selected_monad_difference_l2_source_attempt_certificate.json"
CONDITIONAL_MONAD = CERTS / "selected_monad_difference_l2_source_proof_attempt_certificate.json"
MONAD_SUFFICIENCY = CERTS / "monad_difference_l2_source_sufficiency_certificate.json"
ORDERED_SOURCE_GATE = CERTS / "visible_rank2_l2_ordered_source_promotion_gate_certificate.json"
SELECTOR_OBSTRUCTION = CERTS / "visible_rank2_l2_selector_obstruction_certificate.json"
TIME_GERBE = CERTS / "time_oriented_fixed_gerbe_representative_certificate.json"
GS_CURVATURE = CERTS / "time_oriented_m1_visible_green_schwarz_curvature_closure_certificate.json"
GS_SOURCE_ATTEMPT = CERTS / "time_oriented_m1_visible_gs_source_attempt_certificate.json"
HYM_OPERATOR_ATTEMPT = CERTS / "selected_hym_operator_source_attempt_certificate.json"
ROUTE_C_SMOKE = CERTS / "iwasawa_route_c_branch_smoke_attempt_certificate.json"
PROMOTION_GATE = CERTS / "iwasawa_selected_source_promotion_gate_certificate.json"

CANDIDATE = CANDIDATES / "same_source_monad_gs_operator_fusion_gate.candidate.json"
CERT = CERTS / "same_source_monad_gs_operator_fusion_gate_certificate.json"
TEMPLATE = CERTS / "same_source_monad_gs_operator_fusion.template.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def dig(data: dict[str, Any], *keys: str, default: Any = None) -> Any:
    current: Any = data
    for key in keys:
        if not isinstance(current, dict):
            return default
        current = current.get(key)
    return default if current is None else current


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build_template() -> dict[str, Any]:
    return {
        "schema": "SameSourceMonadGSOperatorFusionPacket.v1",
        "status": "OPEN_SAME_SOURCE_MONAD_GS_OPERATOR_FUSION_REQUIRED",
        "purpose": (
            "Supply one selected source whose data simultaneously select the "
            "L3-K2 ordered monad-difference source, resolve or quotient Pic0, "
            "realize the visible Green-Schwarz curvature row, and pass selected "
            "D_E/Riesz/Green/dotD promotion."
        ),
        "source_identity": {
            "source_certificate": None,
            "source_kind": None,
            "selected_by_mtt": None,
            "fixture_only": None,
            "no_observed_flavor_inputs": None,
            "uses_execution_ii_benchmarks": None,
            "same_source_for_ordered_L_pic0_GS_and_DE": None,
        },
        "ordered_source": {
            "visible_rank2_l2_ordered_source_packet": None,
            "source_lane_selector": None,
            "selected_L": None,
            "selected_L2": None,
            "standard_lattice_or_equivalent_selected": None,
            "base_factor_order_selected": None,
            "base_swap_broken_by_source": None,
            "pic0_resolution": None,
            "ordered_source_validator_passes": None,
        },
        "green_schwarz_and_gerbe": {
            "time_oriented_m1_representative_used": None,
            "antiunitary_q369_retained": None,
            "visible_green_schwarz_row_derived_from_same_source": None,
            "freed_witten_or_cycle_restrictions_verified_if_used": None,
            "projector_retention_verified": None,
        },
        "operator_response": {
            "iwasawa_selected_source_promotion_packet": None,
            "route_c_residuals_pass": None,
            "de_action_pass": None,
            "riesz_gap_pass": None,
            "reduced_green_pass": None,
            "dotd_response_pass": None,
            "selected_dotD_source_verified": None,
            "primitive_C1_contractions": None,
        },
        "forbidden_shortcuts": [
            "Do not combine monad arithmetic, gerbe labels, GS curvature, and Route C smoke data unless one source certificate binds them.",
            "Do not use lifted selected flags as proof.",
            "Do not use observed masses, mixings, or benchmark matrices to select the source.",
            "Do not treat curvature-only Green-Schwarz closure as a selected visible operator source.",
        ],
    }


def analyze() -> dict[str, Any]:
    unconditional = load(UNCONDITIONAL_MONAD)
    conditional = load(CONDITIONAL_MONAD)
    sufficiency = load(MONAD_SUFFICIENCY)
    ordered_gate = load(ORDERED_SOURCE_GATE)
    obstruction = load(SELECTOR_OBSTRUCTION)
    time_gerbe = load(TIME_GERBE)
    gs_curvature = load(GS_CURVATURE)
    gs_source = load(GS_SOURCE_ATTEMPT)
    hym_attempt = load(HYM_OPERATOR_ATTEMPT)
    route_c = load(ROUTE_C_SMOKE)
    promotion_gate = load(PROMOTION_GATE)

    lifted = dig(
        route_c,
        "calculation_results",
        "lifted_selected_flags_all_validators_pass",
        default={},
    )
    current_lifted_pass = bool(lifted.get("current_q79_orientation") is True)

    closed_constituents = {
        "monad_conditional_uniqueness_closed": dig(
            conditional,
            "conditional_uniqueness_theorem",
            "proved",
            default=False,
        )
        is True,
        "monad_sufficiency_after_selection_closed": dig(
            sufficiency,
            "relative_theorem",
            "proved",
            default=False,
        )
        is True,
        "unconditional_monad_selector_still_open": dig(
            unconditional,
            "unconditional_theorem_attempt",
            "proved",
            default=True,
        )
        is False,
        "ordered_source_gate_machine_checkable": ordered_gate.get("status")
        == "VISIBLE_RANK2_L2_ORDERED_SOURCE_PROMOTION_GATE_FORMULATED_SELECTION_OPEN",
        "selector_obstruction_requires_new_source": obstruction.get("no_breaking_source_available")
        is True,
        "time_oriented_m1_gerbe_representative_closed": dig(
            time_gerbe,
            "calculation_results",
            "time_oriented_torsion_label_m1_fixed",
            default=False,
        )
        is True,
        "visible_green_schwarz_curvature_row_closed": dig(
            gs_curvature,
            "calculation_results",
            "visible_green_schwarz_curvature_verified",
            default=False,
        )
        is True,
        "route_c_finite_pipeline_conditionally_passes": current_lifted_pass,
        "selected_source_promotion_gate_ready": dig(
            promotion_gate,
            "verdict",
            "promotion_gate_ready",
            default=False,
        )
        is True,
    }

    current_fusion_attempt = {
        "same_source_operator_source_verified": dig(
            hym_attempt,
            "operator_source",
            "selected_D_E_constructed",
            default=False,
        )
        is True,
        "selected_dotD_constructed": dig(
            hym_attempt,
            "operator_source",
            "selected_dotD_constructed",
            default=False,
        )
        is True,
        "selected_ordered_source_verified": False,
        "pic0_resolved_or_quotiented": False,
        "visible_green_schwarz_source_verified": dig(
            gs_source,
            "calculation_results",
            "visible_green_schwarz_source_verified",
            default=False,
        )
        is True,
        "projector_retention_verified": dig(
            gs_curvature,
            "calculation_results",
            "projector_retention_verified",
            default=False,
        )
        is True,
        "promotion_attempt_passes": dig(
            hym_attempt,
            "operator_source",
            "selected_source_promotion_validator",
            "exit_code",
            default=1,
        )
        == 0,
    }
    current_fusion_closes = all(current_fusion_attempt.values())

    result = {
        "calculation": "SameSourceMonadGSOperatorFusionGate",
        "status": "SAME_SOURCE_MONAD_GS_OPERATOR_FUSION_GATE_FORMULATED_SOURCE_OPEN",
        "inputs": {
            "unconditional_monad": UNCONDITIONAL_MONAD.name,
            "conditional_monad": CONDITIONAL_MONAD.name,
            "monad_sufficiency": MONAD_SUFFICIENCY.name,
            "ordered_source_gate": ORDERED_SOURCE_GATE.name,
            "selector_obstruction": SELECTOR_OBSTRUCTION.name,
            "time_oriented_fixed_gerbe": TIME_GERBE.name,
            "green_schwarz_curvature": GS_CURVATURE.name,
            "green_schwarz_source_attempt": GS_SOURCE_ATTEMPT.name,
            "selected_hym_operator_attempt": HYM_OPERATOR_ATTEMPT.name,
            "route_c_branch_smoke": ROUTE_C_SMOKE.name,
            "selected_source_promotion_gate": PROMOTION_GATE.name,
        },
        "template": str(TEMPLATE.relative_to(ROOT)),
        "closed_constituents": closed_constituents,
        "current_fusion_attempt": current_fusion_attempt,
        "current_fusion_closes_selected_monad_source": current_fusion_closes,
        "proof_implication": {
            "statement": (
                "A single packet satisfying SameSourceMonadGSOperatorFusionPacket.v1 "
                "would prove the missing source-lane selector and Pic0 rule for "
                "Selected_Monad_Difference_L2_Source.v1."
            ),
            "why": [
                "the ordered-source validator would certify L=(1,-2,0), L^2=(2,-4,0) with selected status",
                "the Pic0 field would be selected or quotient-irrelevant by the same source",
                "the visible Green-Schwarz row would be derived from that source rather than inserted",
                "the D_E/Riesz/Green/dotD promotion gate would supply the holonomy-sensitive response that current topology and curvature lack",
            ],
            "then_existing_theorems_apply": [
                "conditional uniqueness forces L3-K2 inside the terminal monad lane",
                "monad-difference sufficiency makes the strict ordered-source validator pass",
                "selector obstruction no longer applies because a new symmetry-breaking source is supplied",
            ],
        },
        "why_current_patchwork_is_not_a_proof": {
            "separate_constituents_do_not_define_same_source": True,
            "route_c_smoke_uses_lifted_flags_only": True,
            "green_schwarz_closure_is_curvature_level_only": True,
            "time_oriented_gerbe_label_lacks_selected_DE_dotD": True,
            "monad_table_is_candidate_not_selected_source": True,
            "pic0_remains_invisible_to_closed_topology_cohomology_curvature": True,
        },
        "minimal_next_packet": {
            "name": "SameSourceMonadGSOperatorFusionPacket.v1",
            "template": str(TEMPLATE.relative_to(ROOT)),
            "must_close": [
                "selected source identity",
                "ordered L3-K2 source status",
                "standard lattice/base ordering/base-swap breaking",
                "Pic0 selection or quotient rule",
                "visible Green-Schwarz row derived from the same source",
                "projector retention",
                "Route C residual, D_E, Riesz, Green, and dotD validators with honest selected flags",
                "primitive C1 contractions for the next flavor step",
            ],
        },
        "what_this_closes": {
            "same_source_fusion_gate_formulated": True,
            "invalid_patchwork_proof_blocked": True,
            "exact_single_packet_needed_for_selector_closure": True,
            "monad_pic0_blocker_connected_to_DE_response_gate": True,
        },
        "what_this_does_not_close": {
            "unconditional_Selected_Monad_Difference_L2_Source_v1": False,
            "selected_D_E_dotD": False,
            "Pic0_selection_or_quotient": False,
            "selected_visible_operator_source": False,
            "full_SM_closure": False,
        },
        "guardrails": {
            "claims_unconditional_monad_selector_proved": False,
            "claims_selected_visible_operator_source": False,
            "claims_selected_D_E_dotD": False,
            "claims_pic0_resolved": False,
            "uses_lifted_flags_as_proof": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
            "claims_full_SM_closure": False,
        },
        "verdict": {
            "honest_answer": (
                "We cannot close the selector by stitching together separately "
                "closed monad, gerbe, Green-Schwarz, and smoke-operator facts. "
                "The next proof object must be one same-source operator packet."
            ),
            "next_action": (
                "Fill SameSourceMonadGSOperatorFusionPacket.v1 from a selected "
                "typed Cech/monad transition source or finite HYM/Strominger "
                "solve, then rerun the ordered-source and selected-source "
                "promotion validators."
            ),
        },
    }
    return result


def main() -> int:
    report = analyze()
    write(TEMPLATE, build_template())
    write(CANDIDATE, report)
    certificate = {
        "certificate": "SameSourceMonadGSOperatorFusionGate",
        "status": report["status"],
        "analysis_script": "scripts/build_same_source_monad_gs_operator_fusion_gate.py",
        "candidate_data": str(CANDIDATE.relative_to(ROOT)),
        "template": report["template"],
        "closed_constituents": report["closed_constituents"],
        "current_fusion_attempt": report["current_fusion_attempt"],
        "current_fusion_closes_selected_monad_source": report[
            "current_fusion_closes_selected_monad_source"
        ],
        "proof_implication": report["proof_implication"],
        "why_current_patchwork_is_not_a_proof": report[
            "why_current_patchwork_is_not_a_proof"
        ],
        "minimal_next_packet": report["minimal_next_packet"],
        "what_this_closes": report["what_this_closes"],
        "what_this_does_not_close": report["what_this_does_not_close"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(CERT, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
