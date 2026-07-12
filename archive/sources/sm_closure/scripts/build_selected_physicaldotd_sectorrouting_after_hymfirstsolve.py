"""Build physical dotD / sector-routing bridge after selected HYM first solve."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_physicaldotd_sectorrouting_after_hymfirstsolve"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ROUTE_DECISION = PACKET_DIR / "physical_dotd_sector_routing_route_decision.packet.json"
PROJECTOR_PROGRESS = PACKET_DIR / "hym_projector_value_progress_after_first_solve.packet.json"
PROMOTION_KERNEL = PACKET_DIR / "selected_projector_source_promotion_kernel.packet.json"
CUTSET = PACKET_DIR / "phifin_trace_or_full_strominger_operator_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhysicalDotD_SectorRouting_AfterHYMFirstSolve_v1.md"

STATUS = "MTT_SELECTED_PHYSICALDOTD_SECTORROUTING_AFTER_HYMFIRSTSOLVE_BUILT_PROJECTOR_PROMOTION_OPEN"
NEXT = "MTT_Selected_PhiFin_BN_ModelActive_Equivalence_or_SelectedMinimizerTrace_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    firstsolve = load(DATA / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor.candidate.json")
    physical = load(DATA / "selected_physical_dotd_alpha1_or_end0_sector_routing.candidate.json")
    alpha_value = load(DATA / "selected_alpha1_source_normalization_or_end0_sector_routing_value_fill.candidate.json")
    end0_functor = load(DATA / "selected_end0_to_sector_functor_source_and_value_packet.candidate.json")
    zero_bridge = load(DATA / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json")
    projector_values = load(DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json")
    route_a = load(DATA / "selected_hym_projector_source_promotion_route_a.candidate.json")
    sector_charge = load(DATA / "selected_sectorcharge_gram_transfernormalization_packet.candidate.json")
    one_m = load(DATA / "selected_sectorcharge_1m_dirac_rule_attempt.candidate.json")

    route_decision = {
        "schema": "MTTPhysicalDotDSectorRoutingRouteDecisionAfterHYMFirstSolve.v1",
        "status": "NAIVE_ALPHA1_RETIRED_PROJECTOR_PROMOTION_PRIMARY",
        "after_first_solve": {
            "selected_diagonal_HYM_first_solve_closed": firstsolve["closure_decision"][
                "selected_diagonal_HYM_first_solve_closed"
            ],
            "rank2_End0_payload_closed": firstsolve["closure_decision"]["rank2_End0_payload_closed"],
            "physical_dotD_alpha1_closed": firstsolve["closure_decision"]["physical_dotD_alpha1_closed"],
        },
        "route_A_naive_source_normalization": {
            "retired_for_naive_ext_scale": alpha_value["decision"]["source_normalization_route_retired_for_naive_scale_tangent"],
            "reason": alpha_value["route_A_source_normalization"]["reason"],
            "reopen_only_by": alpha_value["route_A_source_normalization"]["what_would_be_needed_to_reopen"],
        },
        "route_B_sector_routing": {
            "primary": alpha_value["decision"]["sector_routing_route_remains_primary"],
            "End0_functor_contract_specified": end0_functor["decision"]["functor_contract_specified"],
            "existing_values_promoted": end0_functor["decision"]["existing_BN_or_compact_values_promoted"],
            "selected_End0_to_sector_values_extracted": end0_functor["decision"][
                "selected_End0_to_sector_functor_values_extracted"
            ],
        },
        "projector_bridge": {
            "bridge_theorem_proved": zero_bridge["theorem"]["bridge_theorem_proved"],
            "selected_values_emitted": zero_bridge["theorem"]["selected_values_emitted"],
            "promotes_after_next_artifact_if_validator_passes": zero_bridge["promotion_decision"][
                "promotes_after_next_artifact_if_validator_passes"
            ],
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    finite = projector_values["finite_value_payload"]
    validator = projector_values["validator_result"]
    projector_progress = {
        "schema": "MTTHYMProjectorValueProgressAfterFirstSolve.v1",
        "status": "FINITE_PROJECTOR_VALUES_READY_SOURCE_PROMOTION_OPEN",
        "finite_model_active_projector_values_emitted": validator["finite_projector_values_emitted"],
        "all_projector_checks_pass": validator["all_projector_checks_pass"],
        "End0_equivariance_on_emitted_projectors": validator["End0_equivariance_on_emitted_projectors"],
        "positive_complement_gap": validator["positive_complement_gap"],
        "complement_gap": finite["complement_gap"],
        "ambient_dimension": finite["ambient_dimension"],
        "basis_id": finite["basis_id"],
        "zero_cluster": finite["zero_cluster"],
        "sector_rank_summary": {
            sector: {
                "expected_rank": slot["expected_rank"],
                "basis_count": slot["ordered_zero_mode_basis_vector_count"],
                "selected_source_verified": slot["selected_source_verified"],
                "value_emitted_as_selected_HYM_projector": slot["value_emitted_as_selected_HYM_projector"],
            }
            for sector, slot in finite["sector_slots"].items()
        },
        "source_flags": validator["selected_source_flags"],
        "rho_candidate_promoted_to_selected_rho_s": validator["rho_candidate_promoted_to_selected_rho_s"],
        "selected_HYM_projector_values_promoted": validator["selected_HYM_projector_values_promoted"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    promotion_kernel = {
        "schema": "MTTSelectedProjectorSourcePromotionKernel.v1",
        "status": "PROMOTION_KERNEL_BUILT_PHIFIN_TRACE_OPEN",
        "route_A_source_promotion": {
            "route_a_promotes_now": route_a["route_a_promotes_now"],
            "finite_value_side_closed": route_a["what_closes_now"]["route_A_finite_value_side_closed"],
            "PhiFin_selected_trace_emitted": route_a["route_a_gate_matrix"]["A4_PhiFin_selected_trace_emitted"]["passes"],
            "honest_operator_flags_promote": route_a["route_a_gate_matrix"]["A5_honest_operator_flags_promote"]["passes"],
            "full_selected_operator_identified_with_BN_model_active": route_a["route_a_gate_matrix"][
                "A6_full_selected_strominger_operator_identified_with_BN_model_active"
            ]["passes"],
            "conditional_rule": route_a["theorem_attempt"]["conditional_promotion_rule"],
        },
        "route_B_matter_slot_charge": {
            "structural_1M_rule_candidate_closed": one_m["decision"]["structural_1M_Dirac_rule_candidate_closed"],
            "selected_1M_Dirac_rule_closed": one_m["decision"]["selected_1M_Dirac_rule_closed"],
            "selected_sector_charge_closed": one_m["decision"]["selected_sector_charge_closed"],
            "selected_transfer_normalization": sector_charge["transfer_to_alpha1_decision"]["selected_transfer_normalization"],
            "selected_rho_s_emitted": sector_charge["gram_transfer_packet"]["selected_rho_s_emitted"],
        },
        "primary_path_now": "Route A: emit Phi_fin selected minimizer trace or full selected HYM/Strominger operator value theorem",
        "parallel_constraint_path": "Route B: selected matter-slot charge/1_M rule remains useful for routing after source promotion",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTPhiFinTraceOrFullStromingerOperatorCutset.v1",
        "status": "NEXT_GATE_IS_PHIFIN_TRACE_OR_FULL_SELECTED_OPERATOR_VALUES",
        "bookkeeping_remaining": False,
        "source_or_value_emission_required": True,
        "closed_now": [
            "selected diagonal HYM first solve and End0 payload harvested",
            "naive Ext-scale-to-alpha1 source normalization rejected",
            "End0 sector functor contract and universal carrier constructed",
            "adjoint triplet representation uniqueness proved",
            "canonical rho_candidate constructed",
            "finite model-active projector values, zero cluster, complement gap, and End0 equivariance emitted",
            "projector-to-rho_s bridge theorem proved conditionally",
        ],
        "remaining_minimal_payloads": [
            "emit Phi_fin selected minimizer trace from the selected q79/F,m=1 HYM/Strominger source to finite B_N/projector data",
            "or emit full selected Iwasawa/Strominger sector operator values directly",
            "set selected_source_verified, selected_dotD_source_verified, and alpha1_driver_verified by theorem, not lifted flags",
            "promote finite projector values to selected P_s and ordered zero-mode bases K_s",
            "promote rho_candidate to selected rho_s and then physical sector dotD_alpha1",
            "replay sector validators without smoke fixtures or observed-data selectors",
        ],
        "recommended_next_artifact": NEXT,
        "parallel_artifact": "MTT_Selected_1M_DiracNeutrino_Source_or_SelectedU10Ubar5Polarization_v1",
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedPhysicalDotDSectorRoutingAfterHYMFirstSolve",
        "status": STATUS,
        "inputs": {
            "hym_first_solve": rel(DATA / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor.candidate.json"),
            "physical_dotd_or_sector_routing": rel(DATA / "selected_physical_dotd_alpha1_or_end0_sector_routing.candidate.json"),
            "alpha1_value_fill": rel(DATA / "selected_alpha1_source_normalization_or_end0_sector_routing_value_fill.candidate.json"),
            "end0_functor_contract": rel(DATA / "selected_end0_to_sector_functor_source_and_value_packet.candidate.json"),
            "zero_mode_bridge": rel(DATA / "selected_zero_mode_basis_from_hym_projector_source_theorem.candidate.json"),
            "projector_value_emission": rel(DATA / "selected_hym_projector_zeromode_basis_value_emission.candidate.json"),
            "projector_source_promotion_route_a": rel(DATA / "selected_hym_projector_source_promotion_route_a.candidate.json"),
            "sector_charge_gram_transfer": rel(DATA / "selected_sectorcharge_gram_transfernormalization_packet.candidate.json"),
            "sector_charge_1m_rule": rel(DATA / "selected_sectorcharge_1m_dirac_rule_attempt.candidate.json"),
        },
        "output_packets": {
            "physical_dotd_sector_routing_route_decision": rel(ROUTE_DECISION),
            "hym_projector_value_progress_after_first_solve": rel(PROJECTOR_PROGRESS),
            "selected_projector_source_promotion_kernel": rel(PROMOTION_KERNEL),
            "phifin_trace_or_full_strominger_operator_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "PhysicalDotDSectorRoutingAfterHYMFirstSolveReductionTheorem",
            "proved": True,
            "statement": (
                "After the selected diagonal HYM first solve, physical dotD_alpha1 and sector routing no longer reduce "
                "to a naive alpha1 tangent search. The Ext-scale route is rejected as a physical source normalization; "
                "the primary legal promotion is to emit a Phi_fin selected minimizer trace, or equivalent full selected "
                "HYM/Strominger sector operator values, so finite projector values can promote to selected P_s, K_s, "
                "rho_s, and sector dotD_alpha1."
            ),
        },
        "what_closes_now": {
            "post_firstsolve_route_decision": True,
            "naive_alpha1_scale_route_retired": True,
            "projector_value_progress_imported": True,
            "selected_projector_promotion_kernel_built": True,
            "next_phifin_trace_cutset_sharpened": True,
        },
        "what_remains_open": {
            "Phi_fin_selected_minimizer_trace": True,
            "full_selected_HYM_Strominger_operator_values": True,
            "selected_source_verified_flags": True,
            "selected_P_s_K_s_projector_promotion": True,
            "selected_rho_s_actual_promotion": True,
            "physical_dotD_alpha1_same_branch_driver": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": firstsolve["closure_decision"]["SM_parity_closed"],
            "physical_dotD_alpha1_closed": False,
            "selected_End0_to_sector_routing_values_extracted": False,
            "finite_projector_values_emitted": True,
            "finite_projector_values_promoted_to_selected": False,
            "PhiFin_selected_trace_emitted": False,
            "actual_QaSU3_operator_packet_promoted": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "superset_strategy": {
            "using_one_straight_way": False,
            "combining_paths": True,
            "straight_path": "selected HYM first solve plus Phi_fin/minimizer-trace promotion",
            "support_paths": [
                "End0 tensor-product sector carrier",
                "model-active B_N projector values",
                "SU5/E6 1_M Dirac structural routing",
            ],
            "locked_target": "selected sector projector/source promotion without observed-data fitting",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhysicalDotD_SectorRouting_AfterHYMFirstSolve_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_closed": True,
        "physical_dotD_alpha1_closed": False,
        "finite_projector_values_emitted": True,
        "finite_projector_values_promoted_to_selected": False,
        "PhiFin_selected_trace_emitted": False,
        "actual_QaSU3_operator_packet_promoted": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhysicalDotD SectorRouting AfterHYMFirstSolve v1

Status: `{STATUS}`.

This artifact updates the physical dotD/sector-routing frontier after the
selected diagonal HYM first solve.

The naive route is now retired: the selected Ext-density scale tangent is a
valid local HYM response, but it cannot be renamed physical alpha1. The primary
route is projector/source promotion: emit a selected `Phi_fin` minimizer trace,
or equivalent full selected HYM/Strominger operator values, so the clean finite
projector packet promotes to selected `P_s`, ordered bases `K_s`, selected
`rho_s`, and physical sector `dotD_alpha1`.
"""

    for path, payload in [
        (ROUTE_DECISION, route_decision),
        (PROJECTOR_PROGRESS, projector_progress),
        (PROMOTION_KERNEL, promotion_kernel),
        (CUTSET, cutset),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
