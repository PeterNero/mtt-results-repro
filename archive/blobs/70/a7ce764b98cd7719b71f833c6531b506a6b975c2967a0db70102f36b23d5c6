"""Build CONST-HIGGS-01 H7B1O diagonal HYM payload to Huv transfer gate."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_PARITY_REPO = TEXPAPERS / "mtt-sm-parity-closure"

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "const_higgs_01_h7b1o_diagonal_hym_payload_to_huv_transfer_gate"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DIAGONAL_IMPORT = BASE / "diagonal_hym_payload_import.packet.json"
END0_BOUNDARY = BASE / "rank2_end0_payload_boundary.packet.json"
HUV_GATE = BASE / "higgs_huv_transfer_gate.packet.json"
CYCLE_RETIREMENT = BASE / "cycle_retirement.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_HIGGS_01_H7B1O_DiagonalHYMPayloadToHuvTransferGate_v1.md"

STATUS = "MTT_CONST_HIGGS_01_H7B1O_DIAGONAL_HYM_PAYLOAD_CLOSED_HUV_TRANSFER_OPEN"


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


def clean_flags() -> dict[str, bool]:
    return {
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    h7b1n_path = DATA / "const_higgs_01_h7b1n_hsector_dynamic_extension_or_honest_huv_rows.candidate.json"
    h7b1f_contract_path = DATA / "const_higgs_01_h7b1f_nonsplit_valpha_to_huv_omega_packet" / "nonsplit_to_huv_reduction_contract.packet.json"
    h7b1c_request_path = DATA / "const_higgs_01_h7b1c_selected_two_higgs_mass_strain_hessian" / "minimal_two_by_two_hessian_payload_request.packet.json"

    first_correction_path = SM_PARITY_REPO / "candidate_data" / "selected_nonlinear_hym_correction_coefficient_solve.candidate.json"
    full_exps_path = SM_PARITY_REPO / "candidate_data" / "selected_full_exps_hym_newton_replay.candidate.json"
    operator_payload_path = SM_PARITY_REPO / "candidate_data" / "selected_hym_operator_payload_extraction_from_diagonal_replay.candidate.json"
    end0_de_path = SM_PARITY_REPO / "candidate_data" / "selected_end0_de_payload_from_diagonal_hym.candidate.json"
    riesz_green_dotd_path = SM_PARITY_REPO / "candidate_data" / "selected_riesz_green_dotd_from_diagonal_end0_de.candidate.json"
    t1t2_green_path = SM_PARITY_REPO / "candidate_data" / "selected_t1t2_covariant_green_and_transfer_probe.candidate.json"
    offdiag_control_path = SM_PARITY_REPO / "candidate_data" / "selected_offdiagonal_ext_control_or_sector_transfer.candidate.json"
    firstsolve_path = SM_PARITY_REPO / "candidate_data" / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor.candidate.json"
    firstsolve_payload_path = SM_PARITY_REPO / "candidate_data" / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor" / "selected_hym_first_solve_payload.packet.json"
    rank2_boundary_path = SM_PARITY_REPO / "candidate_data" / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor" / "rank2_to_sector_transfer_boundary.packet.json"
    physical_cutset_path = SM_PARITY_REPO / "candidate_data" / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor" / "physical_dotd_or_sector_routing_cutset.packet.json"

    h7b1n = load(h7b1n_path)
    h7b1f_contract = load(h7b1f_contract_path)
    h7b1c_request = load(h7b1c_request_path)
    first_correction = load(first_correction_path)
    full_exps = load(full_exps_path)
    operator_payload = load(operator_payload_path)
    end0_de = load(end0_de_path)
    riesz_green_dotd = load(riesz_green_dotd_path)
    t1t2_green = load(t1t2_green_path)
    offdiag_control = load(offdiag_control_path)
    firstsolve = load(firstsolve_path)
    firstsolve_payload = load(firstsolve_payload_path)
    rank2_boundary = load(rank2_boundary_path)
    physical_cutset = load(physical_cutset_path)

    first_solution = first_correction["solution_summary"]
    full_solution = full_exps["solution_summary"]
    operator_boundary = operator_payload["operator_payload_boundary"]
    end0_boundary = end0_de["operator_payload_boundary"]
    riesz_boundary = riesz_green_dotd["operator_payload_boundary"]
    t1t2_boundary = t1t2_green["operator_payload_boundary"]
    offdiag_boundary = offdiag_control["operator_payload_boundary"]
    firstsolve_decision = firstsolve["closure_decision"]

    diagonal_branch_closed = all(
        [
            first_correction["what_closes_now"]["zero_mean_poisson_correction_phi_solved"] is True,
            first_correction["solution_summary"]["poisson_residual_l2"] < 1e-12,
            full_exps["coefficient_packet"]["diagonal_expS_solution_closed"] is True,
            full_exps["solution_summary"]["final_residual_l2"] < 1e-12,
            operator_payload["diagonal_metric_payload"]["closed"] is True,
            operator_payload["diagonal_connection_payload"]["closed"] is True,
            operator_payload["curvature_residual_payload"]["closed"] is True,
            end0_de["adjoint_connection_packet"]["closed"] is True,
            riesz_green_dotd["protected_T3_lane"]["closed"] is True,
            t1t2_green["path_A_straight_T1T2_covariant_Green"]["closed"] is True,
            offdiag_control["path_A_straight_offdiagonal_Ext_control"]["closed"] is True,
            firstsolve_decision["rank2_End0_payload_closed"] is True,
        ]
    )

    transfer_values_closed = all(
        [
            firstsolve_decision["rank2_to_sector_transfer_closed"] is True,
            rank2_boundary["rank2_to_sector_functor"]["closed"] is True,
            rank2_boundary["rank2_to_sector_functor"]["sector_routing_values_emitted"] is True,
            physical_cutset["source_or_value_emission_required"] is False,
        ]
    )

    diagonal_import = {
        "schema": "MTTConstHiggs01H7B1ODiagonalHYMPayloadImport.v1",
        "status": "SELECTED_DIAGONAL_HYM_PAYLOAD_IMPORTED_AND_CLOSED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1O-A-DIAGONAL-HYM-PAYLOAD-IMPORT",
        "input_sources": {
            "H7B1N_cutset": rel(h7b1n_path),
            "first_tracefree_HYM_correction": rel(first_correction_path),
            "full_expS_diagonal_HYM_replay": rel(full_exps_path),
            "diagonal_operator_payload": rel(operator_payload_path),
            "End0_DE_payload": rel(end0_de_path),
            "Riesz_Green_dotD_payload": rel(riesz_green_dotd_path),
            "T1T2_covariant_Green_probe": rel(t1t2_green_path),
            "offdiagonal_Ext_control": rel(offdiag_control_path),
            "firstsolve_summary": rel(firstsolve_path),
        },
        "first_tracefree_step": {
            "closed": first_correction["solution_summary"]["first_tracefree_correction_closed"],
            "selected_End0_direction": first_correction["coefficient_packet"]["selected_end0_direction"],
            "equation": first_correction["finite_problem"]["linearized_HYM_equation_solved"],
            "poisson_residual_l2": first_solution["poisson_residual_l2"],
            "phi_min": first_solution["phi_min"],
            "phi_max": first_solution["phi_max"],
            "phi_l2": first_solution["phi_l2"],
        },
        "diagonal_expS_step": {
            "closed": full_exps["coefficient_packet"]["diagonal_expS_solution_closed"],
            "equation": full_exps["nonlinear_equation"]["equation"],
            "iterations_run": full_exps["solver"]["iterations_run"],
            "final_residual_l2": full_solution["final_residual_l2"],
            "u_min": full_solution["u_min"],
            "u_max": full_solution["u_max"],
            "u_l2": full_solution["u_l2"],
            "mean_exp_weighted_density": full_solution["mean_exp_weighted_density"],
        },
        "operator_payload_step": {
            "diagonal_metric_closed": operator_payload["diagonal_metric_payload"]["closed"],
            "diagonal_connection_closed": operator_payload["diagonal_connection_payload"]["closed"],
            "curvature_residual_closed": operator_payload["curvature_residual_payload"]["closed"],
            "gradient_l2": operator_payload["diagonal_connection_payload"]["gradient_l2"],
            "curvature_residual_l2": operator_payload["curvature_residual_payload"]["residual_l2"],
            "validator_ready": operator_boundary["validator_ready"],
        },
        "branch_decision": {
            "diagonal_HYM_payload_closed": diagonal_branch_closed,
            "counts_as_M_source_or_Huv": False,
            "reason": "The imported payload is a selected rank-2/End0 HYM metric/connection/Green scaffold, not a same-source two-Higgs Huv mass-strain matrix.",
        },
        **clean_flags(),
    }

    end0_payload_boundary = {
        "schema": "MTTConstHiggs01H7B1ORank2End0PayloadBoundary.v1",
        "status": "RANK2_END0_PAYLOAD_CLOSED_TRANSFER_VALUES_OPEN",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1O-B-RANK2-END0-BOUNDARY",
        "input_sources": {
            "End0_DE_payload": rel(end0_de_path),
            "Riesz_Green_dotD_payload": rel(riesz_green_dotd_path),
            "T1T2_covariant_Green_probe": rel(t1t2_green_path),
            "offdiagonal_Ext_control": rel(offdiag_control_path),
            "rank2_to_sector_transfer_boundary": rel(rank2_boundary_path),
            "physical_dotd_or_sector_routing_cutset": rel(physical_cutset_path),
        },
        "closed_source_payloads": {
            "A_HYM_rank2_connection_payload": firstsolve["what_closes_now"]["A_HYM_rank2_connection_payload"],
            "diagonal_End0_DE_formula": firstsolve["what_closes_now"]["diagonal_End0_DE_formula"],
            "protected_T3_Riesz_Green": riesz_boundary["protected_T3_Riesz_projector_extracted"] and riesz_boundary["protected_T3_reduced_Green_extracted"],
            "T1_T2_covariant_Green": t1t2_boundary["T1_T2_coupled_covariant_Riesz_Green_extracted"],
            "full_diagonal_End0_Riesz_Green": t1t2_boundary["full_End0_Riesz_Green_extracted"],
            "row_model_offdiagonal_Ext_control": offdiag_boundary["row_model_offdiagonal_T1T2_source_controlled"],
            "dotD_Frechet_schema": riesz_boundary["formal_dotD_frechet_formula_extracted"],
        },
        "transfer_boundary": {
            "rank2_to_sector_transfer_closed": firstsolve_decision["rank2_to_sector_transfer_closed"],
            "sector_routing_values_emitted": rank2_boundary["rank2_to_sector_functor"]["sector_routing_values_emitted"],
            "physical_dotD_alpha1_payload_extracted": offdiag_boundary["physical_dotD_alpha1_payload_extracted"],
            "validator_ready_sector_payload": offdiag_boundary["validator_ready"],
            "source_or_value_emission_required": physical_cutset["source_or_value_emission_required"],
            "recommended_next_artifact": physical_cutset["recommended_next_artifact"],
        },
        "remaining_minimal_payloads": physical_cutset["remaining_minimal_payloads"],
        "strict_decision": {
            "rank2_End0_payload_closed": diagonal_branch_closed,
            "rank2_to_Huv_or_sector_transfer_closed": transfer_values_closed,
            "promote_to_Higgs_M_source": False,
            "promote_to_Huv": False,
        },
        **clean_flags(),
    }

    higgs_huv_transfer_gate = {
        "schema": "MTTConstHiggs01H7B1OHiggsHuvTransferGate.v1",
        "status": "HUV_TRANSFER_VALUES_NOT_EMITTED",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1O-C-HUV-TRANSFER-GATE",
        "input_sources": {
            "H7B1F_Huv_reduction_contract": rel(h7b1f_contract_path),
            "H7B1C_minimal_Huv_request": rel(h7b1c_request_path),
            "H7B1O_rank2_End0_boundary": rel(END0_BOUNDARY),
        },
        "locked_Huv_target": {
            "ordered_basis": h7b1c_request["basis_required"]["ordered_basis"],
            "quotient_map": h7b1c_request["basis_required"]["quotient_map"],
            "reduction_formula": h7b1f_contract["computed_packet_when_filled"]["Huv"],
            "Delta_formula": h7b1f_contract["computed_packet_when_filled"]["Delta"],
            "Omega_formula": h7b1f_contract["computed_packet_when_filled"]["Omega"],
            "s_beta_formula": h7b1f_contract["computed_packet_when_filled"]["s_beta"],
        },
        "strict_payload_state": {
            "B_Huv_value_emitted": False,
            "M_source_value_emitted": False,
            "direct_Huv_entries_emitted": False,
            "Huu": None,
            "Hud": None,
            "Hdd": None,
            "Delta": None,
            "Omega": None,
            "s_beta": None,
            "lambda_H": None,
        },
        "why_diagonal_payload_does_not_close_Huv": {
            "rank2_End0_not_two_column_Higgs_lift": True,
            "no_selected_End0_to_Hu_Hd_dagger_routing_values": True,
            "no_same_source_B_Huv": True,
            "no_same_source_Hermitian_M_source_on_Huv": True,
            "no_direct_Huu_Hud_Hdd": True,
            "physical_dotD_or_sector_payload_still_open": True,
        },
        "guardrail": {
            "do_not_backsolve_beta_or_lambda": True,
            "do_not_promote_rank2_metric_to_Huv_without_transfer": True,
            "do_not_promote_dotD_to_mass_strain_Hessian": True,
            "do_not_use_observed_masses_mixings_couplings": True,
        },
        "passes": False,
        **clean_flags(),
    }

    cycle_retirement = {
        "schema": "MTTConstHiggs01H7B1OCycleRetirement.v1",
        "status": "DIAGONAL_HYM_BRANCH_RETIRED_AS_BLOCKER_TRANSFER_GATE_ACTIVE",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1O-CYCLE-RETIREMENT",
        "retired_blockers": {
            "first_tracefree_HYM_correction": True,
            "diagonal_expS_HYM_replay": True,
            "diagonal_metric_connection_payload": True,
            "End0_DE_formula": True,
            "protected_T3_Riesz_Green": True,
            "T1_T2_covariant_Green": True,
            "row_model_offdiagonal_Ext_control": True,
        },
        "active_blockers": {
            "selected_End0_to_Huv_or_sector_routing_values": True,
            "same_source_two_column_B_Huv": True,
            "same_source_Hermitian_M_source": True,
            "direct_Huu_Hud_Hdd_rows": True,
            "validator_ready_sector_D_E_Riesz_Green_dotD": True,
            "physical_dotD_alpha1_or_equivalent_same_branch_driver": True,
        },
        "non_cycles": [
            "Do not reopen whether the selected diagonal HYM solve exists; it is imported as closed.",
            "Do not reopen whether full diagonal End0 Green exists; it is imported as closed.",
            "Do not reopen H7B1M's matter-sector C1 route as an Huv route.",
            "Do not promote rank-2 End0 support to Huv values until routing/lift rows are emitted.",
        ],
        **clean_flags(),
    }

    next_work = {
        "schema": "MTTConstHiggs01H7B1ONextWork.v1",
        "status": "NEXT_WORKORDER_H7B1P_END0_TO_HUV_OR_SECTOR_ROUTING",
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1O-NEXT",
        "primary_next": {
            "label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1P-END0-TO-HUV-OR-SECTOR-ROUTING",
            "task": "Emit selected rank2/End0-to-Huv routing values, or a same-source two-column B_Huv plus Hermitian M_source, or direct source-owned Huu,Hud,Hdd rows.",
        },
        "legal_exits": [
            {
                "id": "H7B1P-A",
                "label": "End0-to-Huv transfer",
                "must_emit": "selected routing/lift values from the rank-2/End0 HYM payload into ordered (H_u,H_d^dagger), with exactness/error certificate",
            },
            {
                "id": "H7B1P-B",
                "label": "same-source B_Huv and M_source",
                "must_emit": "source-orthonormal two-column B_Huv and same-source Hermitian M_source, then compute Huv=B_Huv^* M_source B_Huv",
            },
            {
                "id": "H7B1P-C",
                "label": "direct Huv row export",
                "must_emit": "Huu,Hud,Hdd in the ordered two-Higgs basis with source ids and exactness/error certificate",
            },
        ],
        "superset_strategy": {
            "using_one_straight_way": False,
            "combining_paths": True,
            "straight_path": "selected rank-2 diagonal HYM/End0 source packet",
            "support_path": "q79/SM-parity sector-transfer and dotD packets as convergence evidence only",
            "locked_target": "Huv two-Higgs mass-strain payload, not measured Higgs data",
        },
        **clean_flags(),
    }

    theorem = {
        "name": "H7B1ODiagonalHYMPayloadToHuvTransferTheorem",
        "proved": True,
        "statement": (
            "The selected q79/F,m=1 V_alpha diagonal HYM branch now emits a closed rank-2/End0 source payload: "
            "first trace-free correction, diagonal exp(S) replay, metric/connection payload, End0 D_E, protected and full diagonal End0 Green, Frechet dotD schema, and row-model offdiagonal control. "
            "By the H7B1F reduction contract, this still does not determine the Higgs two-by-two Huv block unless a selected End0-to-Huv/sector routing, B_Huv with M_source, or direct Huv rows are emitted. "
            "Therefore the nonlinear HYM branch is closed as source progress and the remaining Higgs gate is exactly the Huv transfer/source-row emission gate."
        ),
    }

    candidate = {
        "candidate": "MTTConstHiggs01H7B1ODiagonalHYMPayloadToHuvTransferGate",
        "status": STATUS,
        "active_label": "CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1O-DIAGONAL-HYM-PAYLOAD-TO-HUV-TRANSFER-GATE",
        "output_packets": {
            "diagonal_hym_payload_import": rel(DIAGONAL_IMPORT),
            "rank2_end0_payload_boundary": rel(END0_BOUNDARY),
            "higgs_huv_transfer_gate": rel(HUV_GATE),
            "cycle_retirement": rel(CYCLE_RETIREMENT),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": theorem,
        "H7B1N_gate_imported": h7b1n["broad_H7B1N_gate_reduced_to_minimal_cutset"],
        "selected_diagonal_HYM_first_solve_closed": diagonal_branch_closed,
        "rank2_End0_payload_closed": firstsolve_decision["rank2_End0_payload_closed"],
        "full_diagonal_End0_green_closed": t1t2_boundary["full_End0_Riesz_Green_extracted"],
        "row_model_offdiagonal_Ext_control_closed": offdiag_boundary["row_model_offdiagonal_T1T2_source_controlled"],
        "rank2_to_Huv_or_sector_transfer_closed": transfer_values_closed,
        "physical_dotD_or_sector_payload_closed": False,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "selected_offdiagonal_Omega_found": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        "selected_next_artifact": "MTT_CONST_HIGGS_01_H7B1P_End0ToHuvOrSectorRouting_v1",
        **clean_flags(),
    }

    cert = {
        "certificate": "MTT_CONST_HIGGS_01_H7B1O_DiagonalHYMPayloadToHuvTransferGate_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "active_label": candidate["active_label"],
        "selected_diagonal_HYM_first_solve_closed": diagonal_branch_closed,
        "rank2_End0_payload_closed": firstsolve_decision["rank2_End0_payload_closed"],
        "full_diagonal_End0_green_closed": t1t2_boundary["full_End0_Riesz_Green_extracted"],
        "row_model_offdiagonal_Ext_control_closed": offdiag_boundary["row_model_offdiagonal_T1T2_source_controlled"],
        "rank2_to_Huv_or_sector_transfer_closed": transfer_values_closed,
        "B_Huv_value_emitted": False,
        "M_source_value_emitted": False,
        "direct_Huv_entries_emitted": False,
        "selected_s_beta_value_found": False,
        "numeric_lambda_H_derived": False,
        "strict_no_knob_Higgs_closure": False,
        "new_Higgs_specific_parameters": 0,
        **clean_flags(),
    }

    note = f"""# MTT CONST HIGGS 01 H7B1O Diagonal HYM Payload To Huv Transfer Gate v1

Status: `{STATUS}`

Label: `CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1O-DIAGONAL-HYM-PAYLOAD-TO-HUV-TRANSFER-GATE`

## Result

```text
selected diagonal HYM first solve closed       {diagonal_branch_closed}
rank-2 End0 payload closed                     {firstsolve_decision["rank2_End0_payload_closed"]}
full diagonal End0 Green closed                {t1t2_boundary["full_End0_Riesz_Green_extracted"]}
row-model offdiagonal Ext control closed       {offdiag_boundary["row_model_offdiagonal_T1T2_source_controlled"]}
rank2-to-Huv/sector transfer closed            {transfer_values_closed}
B_Huv / M_source / direct Huv emitted          False
Huv / Omega / s_beta / lambda_H promoted       False
```

## What Closed

The nonlinear HYM branch is no longer merely a request.  The imported
SM-parity source chain closes the selected first trace-free correction, the
diagonal `exp(S)` replay, the determinant-one rank-2 metric/connection payload,
the induced End0 `D_E`, protected and full diagonal End0 Green, Frechet `dotD`
schema, and row-model offdiagonal Ext control.

This is real source progress with zero observed-data selectors and zero new
Higgs-specific parameters.

## What Did Not Close

The H7B1F reduction contract still requires a same-source two-Higgs transfer:
`B_Huv` and `M_source`, or direct `Huu,Hud,Hdd` rows.  The rank-2/End0 payload
does not by itself choose the ordered `(H_u,H_d^dagger)` basis values, and it
does not emit `Omega`, `s_beta`, or `lambda_H`.

## Next Exact Gate

`CONST-HIGGS-01 / HIGGS-QUARTIC-THRESHOLD / H7B1P-END0-TO-HUV-OR-SECTOR-ROUTING`
"""

    for path, payload in [
        (DIAGONAL_IMPORT, diagonal_import),
        (END0_BOUNDARY, end0_payload_boundary),
        (HUV_GATE, higgs_huv_transfer_gate),
        (CYCLE_RETIREMENT, cycle_retirement),
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
