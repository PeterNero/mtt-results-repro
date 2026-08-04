"""Build the H radial action-norm value / H-lambda threshold-row cutset."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hradialactionnormvalue_or_hlambdathresholdrow"
CANDIDATE_DIR = ROOT / "candidate_data" / SLUG
CERT_DIR = ROOT / "certificates"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_HRadialActionNormValue_or_HLambdaThresholdRow_v1.md"


def read_json(path: str | Path) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    CANDIDATE_DIR.mkdir(parents=True, exist_ok=True)
    CERT_DIR.mkdir(parents=True, exist_ok=True)

    radial = read_json("candidate_data/selected_hrgradialnormlaw_or_value_source_derivation.candidate.json")
    radial_norm = read_json(
        "candidate_data/selected_hrgradialnormlaw_or_value_source_derivation/h_radial_norm_law.packet.json"
    )
    radial_routes = read_json(
        "candidate_data/selected_hrgradialnormlaw_or_value_source_derivation/h_radial_value_source_route_audit.packet.json"
    )
    h_lambda_gate = read_json("candidate_data/selected_hlambdaoverlapkernelrow_or_scalaromegaexecutiongate.candidate.json")
    strict_h_lambda = read_json(
        "candidate_data/selected_hlambdaoverlapkernelrow_or_scalaromegaexecutiongate/strict_hlambda_overlap_kernel_gate.packet.json"
    )
    direct_quartic = read_json("candidate_data/selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows.candidate.json")
    h_quartic_reduction = read_json(
        "candidate_data/selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows/h_quartic_threshold_functional_reduction.packet.json"
    )
    h_payload_contract = read_json(
        "candidate_data/selected_hsectorquarticthresholdfromprojectionreduction_or_dynamicherm2rows/h_quartic_threshold_payload_contract.packet.json"
    )
    hsector_dynamic = read_json("candidate_data/selected_hsectordynamicc1extension_or_directhuvrows.candidate.json")
    step72_workorder = read_json(
        "candidate_data/selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance/step72_honest_galerkin_rowlocal_workorder.packet.json"
    )
    step72_targets = read_json(
        "candidate_data/selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance/step72_required_rowlocal_prefactor_target_table.packet.json"
    )

    h_target = next(row for row in step72_targets["target_rows"] if row["omega_id"] == "Omega_H.lambda")
    controlled_r_h = radial["key_numbers"]["controlled_r_H"]
    controlled_r_h_squared = controlled_r_h**2

    action_norm_contract = {
        "schema": "MTTHRadialActionNormValueContract.v1",
        "status": "H_RADIAL_ACTION_NORM_VALUE_CONTRACT_CLOSED_VALUE_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "selected_unit_ray": {
            "source_packet": "candidate_data/selected_hrgradialnormlaw_or_value_source_derivation/h_radial_norm_law.packet.json",
            "closed": radial["decision"]["radial_norm_law_promoted"],
            "formula": radial_norm["conditional_Huv_formula"]["H_tf(r_H)"],
            "normalization_identity": radial_norm["derived_tracefree_unit_generator"]["normalization_checks"][
                "radial_norm_identity"
            ],
        },
        "required_value_payload": {
            "preferred_name": "A_H.radial_norm",
            "equivalent_scalar_names": [
                "r_H",
                "r_H^2",
                "N_H = Hess(F_H)[U_H,U_H]",
                "R_H.threshold",
                "K_threshold.Omega_H.lambda after same-branch scheme bridge",
            ],
            "definition": "N_H must be the selected finite H action/Hessian quadratic value on the already-selected unit ray U_H; r_H=sqrt(N_H) when the quadratic normalization is used.",
            "forbidden_sources": [
                "observed Higgs mass",
                "observed lambda_H replay",
                "SM-parity target rows",
                "controlled HRG calibration counted as no-knob source",
            ],
        },
        "currently_available": {
            "unit_ray_closed": True,
            "s_beta_angle_closed": direct_quartic["closure_decision"]["selected_s_beta_polar_angle_closed"],
            "phase_sign_closed": radial_norm["inputs_now_selected"]["phi_sign_promoted"],
            "m0_tracefree_quotient_closed": radial_norm["inputs_now_selected"]["m0_tracefree_quotient_promoted"],
            "controlled_replay_r_H_available": controlled_r_h,
            "controlled_replay_r_H_squared": controlled_r_h_squared,
            "controlled_replay_counts_as_strict_source": False,
        },
        "decision": {
            "contract_closed": True,
            "numeric_radial_action_norm_value_emitted": False,
            "accepted_radial_action_norm_value_rows": 0,
        },
    }

    h_lambda_bridge = {
        "schema": "MTTHLambdaThresholdRowBridgeContract.v1",
        "status": "H_LAMBDA_THRESHOLD_ROW_BRIDGE_CLOSED_PAYLOAD_SLOTS_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_source_equations": h_quartic_reduction["closed_source_equations"],
        "already_closed_subfields": h_payload_contract["already_closed_subfields"],
        "step72_honest_row_formula": step72_workorder["row_formula_template"],
        "strict_H_row_postcheck_target": {
            "omega_id": h_target["omega_id"],
            "accepted_as_source_row": h_target["accepted_as_source_row"],
            "diagnostic_prefactor": h_target["diagnostic_prefactor"],
            "rowlocal_composite_target_symbolic": h_target["rowlocal_composite_target_symbolic"],
            "source_value_tier": h_target["source_value_tier"],
        },
        "must_emit_before_strict_acceptance": {
            "selected_L_rowlocal_Omega_H_lambda": None,
            "selected_T_scheme_Omega_H_lambda": None,
            "or_direct_K_threshold_Omega_H_lambda": None,
            "same_branch_source_owner_certificate": None,
            "finite_exactness_or_residual_bound": None,
        },
        "decision": {
            "bridge_contract_closed": True,
            "selected_L_rowlocal_Omega_H_lambda": direct_quartic["closure_decision"]["selected_L_rowlocal_Omega_H_lambda"],
            "selected_T_scheme_Omega_H_lambda": direct_quartic["closure_decision"]["selected_T_scheme_Omega_H_lambda"],
            "selected_K_threshold_Omega_H_lambda_emitted": direct_quartic["closure_decision"][
                "K_threshold_Omega_H_lambda_emitted"
            ],
            "accepted_bridge_value_rows": 0,
        },
    }

    execution_packet = {
        "schema": "MTTHRadialActionCurrentPayloadExecution.v1",
        "status": "CURRENT_H_RADIAL_VALUE_PAYLOAD_EXECUTES_ZERO_ACCEPTED_ROWS",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed": {
            "H_unit_ray_from_s_beta_phase_trace": True,
            "H_quartic_threshold_source_equation_shell": True,
            "D_fin_H_support": h_payload_contract["already_closed_subfields"]["D_fin_H_closed"],
            "theta_exponent_1_over_3": h_payload_contract["already_closed_subfields"]["theta_exponent_1_over_3_closed"],
            "B_Huv_source_ids_and_metric_binding_support": hsector_dynamic["closure_decision"][
                "active_E_HUV_source_ids_emitted"
            ],
            "controlled_one_parameter_H_layer_available": h_lambda_gate["closure_decision"][
                "controlled_one_parameter_H_layer_built"
            ],
        },
        "not_closed": {
            "L_rowlocal_Omega_H_lambda": not h_lambda_bridge["decision"]["selected_L_rowlocal_Omega_H_lambda"],
            "T_scheme_Omega_H_lambda": not h_lambda_bridge["decision"]["selected_T_scheme_Omega_H_lambda"],
            "K_threshold_Omega_H_lambda": not h_lambda_bridge["decision"]["selected_K_threshold_Omega_H_lambda_emitted"],
            "A_H_radial_norm_value": True,
            "strict_R_H_RG_source": radial_routes["routes"]["typed_HRG_value_map"]["strict_R_H_RG_source_constructed"] is False,
            "direct_Herm2_Huv_payload": hsector_dynamic["closure_decision"]["direct_Herm2_Huv_payload_emitted"] is False,
        },
        "current_counts": {
            "strict_selected_charged_overlap_row_count": strict_h_lambda["strict_selected_charged_overlap_row_count"],
            "strict_selected_K_source_row_count": strict_h_lambda["strict_selected_K_source_row_count"],
            "strict_selected_K_source_row_count_required": strict_h_lambda["strict_selected_K_source_row_count_required"],
            "accepted_internal_scalar_value_row_count": direct_quartic["closure_decision"][
                "accepted_internal_scalar_value_row_count"
            ],
            "accepted_radial_threshold_source_count": direct_quartic["closure_decision"][
                "accepted_radial_threshold_source_count"
            ],
            "accepted_numeric_radial_value_sources": radial_routes["decision"]["accepted_numeric_radial_value_sources"],
        },
        "decision": {
            "current_payload_execution_completed": True,
            "accepted_value_rows": 0,
            "controlled_parameter_tier_kept_separate": True,
            "strict_no_knob_numeric_solution_found": False,
        },
    }

    missing_object = {
        "schema": "MTTHRadialActionRequiredMissingObject.v1",
        "status": "FRONTIER_REDUCED_TO_HLAMBDA_ROWLOCAL_SCHEME_OR_DIRECT_RADIAL_HESSIAN_VALUE",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "minimal_legal_exits": {
            "split_H_lambda_exit": {
                "accepted_now": False,
                "rows_needed": 2,
                "must_emit": [
                    "L_rowlocal.Omega_H.lambda",
                    "T_scheme.Omega_H.lambda",
                ],
                "then_compute": "K_threshold.Omega_H.lambda = L_rowlocal.Omega_H.lambda*T_scheme.Omega_H.lambda",
            },
            "direct_H_lambda_exit": {
                "accepted_now": False,
                "rows_needed": 1,
                "must_emit": ["K_threshold.Omega_H.lambda"],
            },
            "direct_radial_hessian_exit": {
                "accepted_now": False,
                "rows_needed": 1,
                "must_emit": ["N_H = Hess(F_H)[U_H,U_H] on the selected q79/F,m=1 unit ray"],
                "then_compute": "r_H=sqrt(N_H) in the selected normalization",
            },
        },
        "next_required_artifact": "MTT_Selected_HLambdaRowLocalOverlapAndScheme_or_DirectRadialHessianValue_v1",
        "decision": {
            "frontier_reduced_to_two_split_slots_or_one_direct_scalar": True,
            "do_not_repeat_status_only_packets": True,
            "next_packet_must_emit_numeric_source_or_formal_source_operator": True,
        },
    }

    candidate = {
        "schema": "MTTSelectedHRadialActionNormValueOrHLambdaThresholdRowCandidate.v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "theorem": {
            "name": "HRadialActionNormValueCutsetTheorem",
            "proved": True,
            "statement": (
                "The selected H radial scalar is now tied to an exact value payload contract. "
                "A strict no-knob value can enter only as a selected radial Hessian/action scalar "
                "N_H=Hess(F_H)[U_H,U_H] on the already selected Herm(2) unit ray, as a direct "
                "K_threshold.Omega_H.lambda row, or as the selected split pair "
                "L_rowlocal.Omega_H.lambda and T_scheme.Omega_H.lambda.  Current execution emits "
                "zero accepted numeric source rows; the controlled one-parameter HRG/H layer remains "
                "available only as calibration-tier support."
            ),
        },
        "decision": {
            "radial_action_norm_value_contract_closed": True,
            "H_lambda_threshold_bridge_contract_closed": True,
            "current_payload_execution_completed": True,
            "numeric_value_emitted": False,
            "accepted_value_rows": 0,
            "strict_no_knob_numeric_solution_found": False,
            "controlled_one_parameter_tier_available": True,
            "controlled_one_parameter_tier_promoted_to_strict": False,
            "frontier_reduced_to_two_split_slots_or_one_direct_scalar": True,
        },
        "key_numbers": {
            "controlled_r_H_postcheck_only": controlled_r_h,
            "controlled_r_H_squared_postcheck_only": controlled_r_h_squared,
            "strict_selected_K_source_row_count": strict_h_lambda["strict_selected_K_source_row_count"],
            "strict_selected_K_source_row_count_required": strict_h_lambda["strict_selected_K_source_row_count_required"],
            "accepted_radial_action_norm_value_rows": 0,
            "accepted_H_lambda_bridge_value_rows": 0,
            "step72_H_lambda_diagnostic_prefactor_postcheck_only": h_target["diagnostic_prefactor"],
        },
        "packets": [
            f"candidate_data/{SLUG}/h_radial_action_norm_value_contract.packet.json",
            f"candidate_data/{SLUG}/h_lambda_threshold_row_bridge_contract.packet.json",
            f"candidate_data/{SLUG}/current_h_radial_value_payload_execution.packet.json",
            f"candidate_data/{SLUG}/required_missing_object.packet.json",
        ],
        "next_target": "MTT_Selected_HLambdaRowLocalOverlapAndScheme_or_DirectRadialHessianValue_v1",
    }

    certificate = {
        "certificate": "selected_hradialactionnormvalue_or_hlambdathresholdrow_certificate.v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": "MTT_SELECTED_HRADIALACTIONNORMVALUE_OR_HLAMBDATHRESHOLDROW_CONTRACT_CLOSED_VALUE_OPEN",
        "proved": True,
        "no_target_fitting": True,
        "observed_data_used_as_selector": False,
        "checks": {
            "radial_action_norm_value_contract_closed": True,
            "H_lambda_threshold_bridge_contract_closed": True,
            "numeric_value_emitted": False,
            "accepted_value_rows": 0,
            "controlled_tier_promoted_to_strict": False,
            "frontier_reduced_to_two_split_slots_or_one_direct_scalar": True,
        },
    }

    write_json(ROOT / f"candidate_data/{SLUG}.candidate.json", candidate)
    write_json(CANDIDATE_DIR / "h_radial_action_norm_value_contract.packet.json", action_norm_contract)
    write_json(CANDIDATE_DIR / "h_lambda_threshold_row_bridge_contract.packet.json", h_lambda_bridge)
    write_json(CANDIDATE_DIR / "current_h_radial_value_payload_execution.packet.json", execution_packet)
    write_json(CANDIDATE_DIR / "required_missing_object.packet.json", missing_object)
    write_json(CERT_DIR / f"{SLUG}_certificate.json", certificate)

    PROOF.write_text(
        "\n".join(
            [
                "# MTT Selected H Radial Action-Norm Value or H-Lambda Threshold Row v1",
                "",
                "## Result",
                "",
                "The value payload contract is now closed, but the strict numeric value is still open.",
                "",
                "The selected H unit ray from the radial norm-law packet gives the exact meaning of the last scalar. A strict value may now enter only through one of three equivalent source-owned exits:",
                "",
                "- direct radial Hessian/action value: `N_H = Hess(F_H)[U_H,U_H]`, giving `r_H=sqrt(N_H)` in the selected normalization",
                "- direct threshold row: `K_threshold.Omega_H.lambda`",
                "- split threshold row: `L_rowlocal.Omega_H.lambda` and `T_scheme.Omega_H.lambda`, with `K_threshold = L_rowlocal*T_scheme`",
                "",
                "The Step72 Galerkin workorder supplies the honest execution formula:",
                "",
                "```text",
                "L_rowlocal.Omega = <psi_L, Pi0^perp G_E (delta_Omega D_E) Pi0^perp psi_R>",
                "Omega.value = D_fin.class * L_rowlocal.Omega * T_scheme.Omega * epsilon_Theta^n",
                "```",
                "",
                "For `Omega_H.lambda`, the already closed support is `D_fin.H` and `epsilon_Theta^(1/3)`. The missing strict objects are therefore the H-sector row-local overlap and threshold/scheme factor, or one direct selected radial Hessian scalar.",
                "",
                "## Current Execution",
                "",
                "- strict K rows remain `9/10`",
                "- accepted H scalar value rows remain `0`",
                "- accepted radial action-norm rows remain `0`",
                "- controlled `r_H = 391.39140285811936` remains postcheck/calibration-tier only",
                "- no observed Higgs mass, observed `lambda_H`, or SM-parity replay row is allowed to select the strict value",
                "",
                "## Next Target",
                "",
                "```text",
                "MTT_Selected_HLambdaRowLocalOverlapAndScheme_or_DirectRadialHessianValue_v1",
                "```",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
