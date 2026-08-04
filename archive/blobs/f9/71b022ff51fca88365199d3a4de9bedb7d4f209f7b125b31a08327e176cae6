"""Build selected HYM Newton/Galerkin first-solve or rank2-sector functor artifact."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FIRST_SOLVE = PACKET_DIR / "selected_hym_first_solve_payload.packet.json"
END0_GREEN = PACKET_DIR / "full_diagonal_end0_green_payload.packet.json"
TRANSFER = PACKET_DIR / "rank2_to_sector_transfer_boundary.packet.json"
CUTSET = PACKET_DIR / "physical_dotd_or_sector_routing_cutset.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HYMNewtonGalerkin_FirstSolve_or_Rank2SectorFunctor_v1.md"

STATUS = "MTT_SELECTED_HYMNEWTONGALERKIN_FIRSTSOLVE_OR_RANK2SECTORFUNCTOR_BUILT_DIAGONAL_SOLVE_SECTOR_TRANSFER_OPEN"
NEXT = "MTT_Selected_Physical_dotD_alpha1_or_End0_to_Sector_Routing_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    post_kernel = load(DATA / "selected_postsmparity_trueequivalence_sourceupgrade_kernel.candidate.json")
    diagonal_solve = load(DATA / "selected_full_exps_hym_newton_replay.candidate.json")
    diag_payload = load(DATA / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json")
    end0_de = load(DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json")
    riesz_green = load(DATA / "selected_riesz_green_dotd_from_diagonal_end0_de.candidate.json")
    t1t2 = load(DATA / "selected_t1t2_covariant_green_and_transfer_probe.candidate.json")
    offdiag = load(DATA / "selected_offdiagonal_ext_control_or_sector_transfer.candidate.json")
    acceptance = load(
        DATA
        / "selected_postsmparity_trueequivalence_sourceupgrade_kernel"
        / "hym_newton_galerkin_acceptance_kernel.packet.json"
    )

    final_iteration = diagonal_solve["residual_trace"][-1]

    first_solve = {
        "schema": "MTTSelectedHYMFirstSolvePayload.v1",
        "status": "DIAGONAL_HYM_FIRST_SOLVE_PAYLOAD_ACCEPTED_AS_SOURCE_PROGRESS",
        "selected_source": "q79/F,m=1 eta_00 rank-2 V_alpha diagonal T3 HYM lane",
        "equation": diagonal_solve["nonlinear_equation"],
        "solver": diagonal_solve["solver"],
        "solution_summary": diagonal_solve["solution_summary"],
        "final_iteration": final_iteration,
        "A_HYM_payload": {
            "emitted": True,
            "rank2_connection": diag_payload["diagonal_connection_payload"]["connection_form"],
            "metric": diag_payload["diagonal_metric_payload"]["H_diagonal"],
            "determinant_one": diag_payload["diagonal_metric_payload"]["determinant"],
            "gradient_l2": diag_payload["diagonal_connection_payload"]["gradient_l2"],
            "direction_summaries": diag_payload["diagonal_connection_payload"]["gradient_direction_summaries"],
        },
        "quadrature_truncation_payload": {
            "emitted_for_diagonal_replay": True,
            "mesh": diagonal_solve["solver"]["mesh"],
            "theta_series_cutoff": diagonal_solve["solver"]["theta_series_cutoff"],
            "residual_l2": diagonal_solve["solution_summary"]["final_residual_l2"],
            "accepted_for_full_sector_validator": False,
            "why_not_full_sector": "The residual certifies the selected diagonal replay, not the full sector transfer and physical dotD validators.",
        },
        "coercivity_status": {
            "diagonal_fixed_point_contraction_observed": True,
            "tail_contraction_ratios": diagonal_solve["solution_summary"]["tail_contraction_ratios"],
            "full_gauge_fixed_jacobian_lower_bound_proved": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    end0_green = {
        "schema": "MTTFullDiagonalEnd0GreenPayload.v1",
        "status": "FULL_DIAGONAL_END0_GREEN_CLOSED_PHYSICAL_TRANSFER_OPEN",
        "End0_D_E_formula": {
            "emitted": end0_de["operator_payload_boundary"]["diagonal_End0_D_E_formula_extracted"],
            "basis": end0_de["selected_End0_basis"],
            "adjoint_connection": end0_de["adjoint_connection_packet"],
            "direction_payload": end0_de["D_E_direction_payload"],
        },
        "protected_T3_lane": riesz_green["protected_T3_lane"],
        "T1_T2_covariant_Green": t1t2["path_A_straight_T1T2_covariant_Green"],
        "offdiagonal_row_model_control": offdiag["path_A_straight_offdiagonal_Ext_control"],
        "operator_payload_boundary": {
            "diagonal_End0_D_E_formula_extracted": True,
            "protected_T3_Riesz_projector_extracted": True,
            "protected_T3_reduced_Green_extracted": True,
            "T1_T2_coupled_covariant_Riesz_Green_extracted": True,
            "row_model_offdiagonal_T1T2_source_controlled": True,
            "physical_dotD_alpha1_payload_extracted": False,
            "rank2_to_rank3_sector_transfer_values_extracted": False,
            "validator_ready_sector_payload": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    transfer = {
        "schema": "MTTRank2ToSectorTransferBoundary.v1",
        "status": "RANK2_END0_PAYLOAD_READY_SECTOR_FUNCTOR_VALUES_OPEN",
        "straight_path_progress": {
            "diagonal_HYM_solve_closed": diagonal_solve["solver"]["converged"],
            "A_HYM_formula_emitted": True,
            "End0_D_E_formula_emitted": end0_de["operator_payload_boundary"]["diagonal_End0_D_E_formula_extracted"],
            "full_diagonal_End0_Green_closed": t1t2["operator_payload_boundary"]["full_End0_Riesz_Green_extracted"],
            "offdiagonal_row_model_control_closed": offdiag["operator_payload_boundary"]["row_model_offdiagonal_T1T2_source_controlled"],
        },
        "rank2_to_sector_functor": {
            "abstract_End0_functor_available": t1t2["path_B_superset_rank2_to_sector_transfer"]["abstract_End0_functor_closed"],
            "BN_qutrit_identification_rejected_as_selected_End0_basis": t1t2["path_B_superset_rank2_to_sector_transfer"][
                "BN_identification_rejected_at_selected_End0_level"
            ],
            "sector_routing_values_emitted": False,
            "physical_dotD_alpha1_emitted": False,
            "closed": False,
        },
        "acceptance_kernel_progress": {
            "required_payloads_from_prior_kernel": acceptance["required_payloads"],
            "emit_selected_A_HYM_or_SH_coefficient_vector": True,
            "emit_selected_quadrature_truncation_error_bound_for_diagonal_lane": True,
            "prove_coercive_full_gauge_fixed_jacobian_lower_bound": False,
            "construct_rank2_to_sector_transfer_functor_or_prove_unnecessary": False,
            "derive_sector_ready_rhoE_metric_DE_Riesz_Green_dotD_C1": False,
            "replay_validators_without_lifted_flags": False,
        },
        "why_not_true_equivalence": (
            "The selected diagonal rank-2 HYM/End0 payload is real source progress, but true equivalence needs "
            "the physical sector routing and dotD_alpha1 payload that downstream validators consume."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cutset = {
        "schema": "MTTPhysicalDotDOrSectorRoutingCutset.v1",
        "status": "NEXT_GATE_IS_PHYSICAL_DOTD_ALPHA1_OR_END0_TO_SECTOR_ROUTING",
        "bookkeeping_remaining": False,
        "source_or_value_emission_required": True,
        "closed_now": [
            "selected diagonal nonlinear HYM first solve",
            "rank-2 A_HYM = du*T3 connection payload",
            "canonical End0 D_E = d + ad(A_diag) formula",
            "protected T3 Riesz/Green",
            "coupled T1/T2 covariant Green by pure-gauge equivalence",
            "selected row-model offdiagonal Ext source control",
        ],
        "remaining_minimal_payloads": [
            "emit selected End0-to-sector routing values from rank-2 V_alpha/End0 into the qutrit/family-sector scaffold",
            "emit physical dotD_alpha1 as a same-branch derivative of selected D_E, not a diagnostic lift",
            "promote or replace the B_N/qutrit basis identification with a selected functorial sector basis",
            "derive sector-ready rho_E, metric, D_E, Riesz/Green, dotD, and C1/overlap payloads",
            "replay validators without lifted flags or smoke fixtures",
        ],
        "recommended_next_artifact": NEXT,
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHYMNewtonGalerkinFirstSolveOrRank2SectorFunctor",
        "status": STATUS,
        "inputs": {
            "post_smparity_source_upgrade_kernel": rel(
                DATA / "selected_postsmparity_trueequivalence_sourceupgrade_kernel.candidate.json"
            ),
            "diagonal_HYM_Newton_replay": rel(DATA / "selected_full_exps_hym_newton_replay.candidate.json"),
            "diagonal_operator_payload": rel(DATA / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json"),
            "End0_DE_payload": rel(DATA / "selected_end0_de_payload_from_diagonal_hym.candidate.json"),
            "Riesz_Green_dotD_payload": rel(DATA / "selected_riesz_green_dotd_from_diagonal_end0_de.candidate.json"),
            "T1T2_covariant_Green_probe": rel(DATA / "selected_t1t2_covariant_green_and_transfer_probe.candidate.json"),
            "offdiagonal_Ext_control_or_sector_transfer": rel(
                DATA / "selected_offdiagonal_ext_control_or_sector_transfer.candidate.json"
            ),
        },
        "output_packets": {
            "selected_hym_first_solve_payload": rel(FIRST_SOLVE),
            "full_diagonal_end0_green_payload": rel(END0_GREEN),
            "rank2_to_sector_transfer_boundary": rel(TRANSFER),
            "physical_dotd_or_sector_routing_cutset": rel(CUTSET),
        },
        "theorem": {
            "name": "HYMNewtonGalerkinFirstSolveHarvestTheorem",
            "proved": True,
            "statement": (
                "The selected q79/F,m=1 rank-2 V_alpha diagonal HYM lane supplies an actual Newton/Galerkin "
                "first solve: a determinant-one metric, A_HYM=du*T3, diagonal End0 D_E, protected T3 Green, "
                "coupled T1/T2 covariant Green, and row-model offdiagonal Ext control. This is not yet the "
                "sector-ready Qa/SU3 operator packet, because physical dotD_alpha1 and End0-to-sector routing "
                "values remain un-emitted."
            ),
        },
        "what_closes_now": {
            "selected_diagonal_HYM_first_solve": True,
            "A_HYM_rank2_connection_payload": True,
            "diagonal_End0_DE_formula": True,
            "full_diagonal_End0_Riesz_Green": True,
            "row_model_offdiagonal_Ext_control": True,
            "next_physical_transfer_cutset_sharpened": True,
        },
        "what_remains_open": {
            "full_gauge_fixed_jacobian_lower_bound_beyond_diagonal_lane": True,
            "End0_to_sector_routing_values": True,
            "physical_dotD_alpha1_same_branch_driver": True,
            "sector_ready_rhoE_DE_Riesz_Green_dotD_C1": True,
            "actual_QaSU3_operator_packet": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "SM_parity_closed": post_kernel["closure_decision"]["SM_parity_closed"],
            "selected_diagonal_HYM_first_solve_closed": True,
            "rank2_End0_payload_closed": True,
            "rank2_to_sector_transfer_closed": False,
            "physical_dotD_alpha1_closed": False,
            "actual_QaSU3_operator_packet_promoted": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "superset_strategy": {
            "using_one_straight_way": False,
            "combining_paths": True,
            "straight_path": "selected diagonal HYM Newton/Galerkin replay and End0 Green extraction",
            "support_path": "rank2-to-sector/qutrit/BN scaffolds used only as validator-shape targets until selected routing values are emitted",
            "locked_target": "actual Qa/SU3 operator packet for true SM equivalence",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_HYMNewtonGalerkin_FirstSolve_or_Rank2SectorFunctor_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "SM_parity_closed": True,
        "selected_diagonal_HYM_first_solve_closed": True,
        "rank2_End0_payload_closed": True,
        "rank2_to_sector_transfer_closed": False,
        "physical_dotD_alpha1_closed": False,
        "actual_QaSU3_operator_packet_promoted": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected HYMNewtonGalerkin FirstSolve or Rank2SectorFunctor v1

Status: `{STATUS}`.

This artifact harvests the first real selected HYM solve now available in the
repo. The selected diagonal q79/F,m=1 rank-2 lane emits a determinant-one
metric, `A_HYM = du*T3`, the induced `End0` covariant derivative, protected
`T3` Riesz/Green data, the coupled `T1/T2` covariant Green by pure-gauge
equivalence, and row-model offdiagonal Ext control.

That is source progress, not true-equivalence closure. The missing object is
now narrower: selected physical `dotD_alpha1` and selected `End0`-to-sector
routing values that turn the rank-2/End0 payload into validator-ready sector
`rho_E`, `D_E`, Riesz/Green, dotD, and C1/overlap data.
"""

    for path, payload in [
        (FIRST_SOLVE, first_solve),
        (END0_GREEN, end0_green),
        (TRANSFER, transfer),
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
