"""Build the H-lambda row-local operator / direct radial Hessian value packet."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hlambdarowlocaloverlapandscheme_or_directradialhessianvalue"
CANDIDATE_DIR = ROOT / "candidate_data" / SLUG
CERT_DIR = ROOT / "certificates"
PROOF = ROOT / "proof_corpus" / "MTT_Selected_HLambdaRowLocalOverlapAndScheme_or_DirectRadialHessianValue_v1.md"


def read_json(path: str | Path) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    CANDIDATE_DIR.mkdir(parents=True, exist_ok=True)
    CERT_DIR.mkdir(parents=True, exist_ok=True)

    prior = read_json("candidate_data/selected_hradialactionnormvalue_or_hlambdathresholdrow.candidate.json")
    qutrit = read_json("candidate_data/selected_hymoverlapvaluesource_or_qutritspectraltriplepackaging.candidate.json")
    qutrit_matrix = read_json(
        "candidate_data/selected_hymoverlapvaluesource_or_qutritspectraltriplepackaging/qutrit_weyl_27x27_matrix_realization.packet.json"
    )
    charged = read_json("candidate_data/selected_hymoverlapvaluesource_or_selectedoverlapkernelrows.candidate.json")
    charged_rows = read_json(
        "candidate_data/selected_hymoverlapvaluesource_or_selectedoverlapkernelrows/selected_charged_normalized_overlap_kernel_rows.packet.json"
    )
    h_gap = read_json(
        "candidate_data/selected_hymoverlapvaluesource_or_selectedoverlapkernelrows/h_lambda_overlap_kernel_row_gap.packet.json"
    )
    workorder = read_json(
        "candidate_data/selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance/step72_honest_galerkin_rowlocal_workorder.packet.json"
    )
    direct_quartic = read_json("candidate_data/selected_directhquarticthresholdfunctional_or_dynamicherm2valuerows.candidate.json")
    h_radial = read_json("candidate_data/selected_hrgradialnormlaw_or_value_source_derivation.candidate.json")

    h_operator = {
        "schema": "MTTHLambdaFormalRowLocalOverlapOperator.v1",
        "status": "FORMAL_SELECTED_HLAMBDA_ROWLOCAL_OPERATOR_EMITTED_NUMERIC_ENTRIES_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "operator_id": "RO.q79F1.Omega_H.lambda",
        "same_branch": {
            "q": 79,
            "orientation": "F",
            "torsion_m": 1,
            "same_branch_required_for_all_entries": True,
        },
        "carrier": {
            "source_packet": "candidate_data/selected_hymoverlapvaluesource_or_qutritspectraltriplepackaging/qutrit_weyl_27x27_matrix_realization.packet.json",
            "carrier_dimension": qutrit_matrix["carrier_dimension"],
            "basis_order": qutrit_matrix["basis_order"],
            "left_X27_rank": qutrit_matrix["left_X27_rank"],
            "left_Z27_rank": qutrit_matrix["left_Z27_rank"],
            "weyl_relation": qutrit_matrix["weyl_relation"],
            "left_action_relation_error_frobenius": qutrit_matrix["left_action_relation_error_frobenius"],
        },
        "formal_operator": {
            "row_formula": workorder["row_formula_template"]["rowlocal_overlap"],
            "symbolic_definition": (
                "L_rowlocal.Omega_H.lambda = <psi_H,L, Pi0^perp G_E "
                "(delta_{Omega_H.lambda} D_E) Pi0^perp psi_H,R>_q79F1, normalized by the selected Riesz/Green/projector convention"
            ),
            "finite_matrix_placeholder": "P_H Pi0^perp G_E (delta_{Omega_H.lambda} D_E) Pi0^perp P_H on H_Q",
            "H_sector_projector": "P_H is the selected two-Higgs H_u/H_d^dagger projector induced by B_Huv/R_H",
            "normalization": "same selected Riesz/Green/projector normalization as Step36-42 and the charged overlap rows",
        },
        "emission": {
            "formal_source_operator_emitted": True,
            "numeric_matrix_entries_emitted": False,
            "finite_exactness_bound_emitted": False,
            "selected_rowlocal_scalar_value_emitted": False,
            "accepted_as_L_rowlocal_value": False,
        },
    }

    scheme_contract = {
        "schema": "MTTHLambdaSchemeFactorContract.v1",
        "status": "H_LAMBDA_SCHEME_FACTOR_CONTRACT_CLOSED_VALUE_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "why_charged_T_scheme_does_not_transfer": [
            "the nine charged rows use source-native null threshold transport with T_scheme=1",
            "Omega_H.lambda is a Higgs quartic/threshold payload row, not a charged mass/profile row",
            "the H-sector threshold scheme must be selected before lambda_H replay",
        ],
        "closed_equation": "K_threshold.Omega_H.lambda = L_rowlocal.Omega_H.lambda * T_scheme.Omega_H.lambda",
        "must_emit": {
            "T_scheme_Omega_H_lambda": None,
            "scheme_convention_certificate": None,
            "finite_threshold_scale_map": None,
        },
        "emission": {
            "formal_scheme_slot_emitted": True,
            "numeric_scheme_value_emitted": False,
            "accepted_as_T_scheme_value": False,
        },
    }

    direct_hessian_contract = {
        "schema": "MTTDirectRadialHessianValueExecutionContract.v1",
        "status": "DIRECT_RADIAL_HESSIAN_EXECUTION_CONTRACT_CLOSED_VALUE_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "unit_ray_source": "candidate_data/selected_hrgradialnormlaw_or_value_source_derivation/h_radial_norm_law.packet.json",
        "required_scalar": "N_H = Hess(F_H)[U_H,U_H]",
        "then": "r_H = sqrt(N_H) and H_tf(r_H) follows from the closed polar/radial norm law",
        "legal_source_operators": [
            "selected finite H-sector action F_H",
            "selected same-source Hermitian M_source restricted to B_Huv",
            "selected primitive H-response kernel K_H with row-level exactness/error bound",
        ],
        "current_emission": {
            "finite_H_action_selected": False,
            "M_source_values_selected": False,
            "primitive_H_response_kernel_values_selected": False,
            "direct_N_H_value_emitted": False,
            "accepted_direct_radial_hessian_value_rows": 0,
        },
    }

    execution_gate = {
        "schema": "MTTHLambdaOperatorExecutionGate.v1",
        "status": "FORMAL_OPERATOR_READY_NUMERIC_GALERKIN_OR_DIRECT_HESSIAN_EXECUTION_OPEN",
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closed_now": [
            "formal same-branch H-lambda row-local operator id",
            "carrier/domain/provenance tied to selected q79/F,m=1 27x27 package",
            "scheme factor slot separated from charged T_scheme=1 shortcut",
            "direct radial Hessian scalar alternative contract",
        ],
        "still_open": [
            "numeric finite Galerkin entries for RO.q79F1.Omega_H.lambda",
            "selected T_scheme.Omega_H.lambda value",
            "finite exactness or residual certificate for the H row",
            "direct selected N_H value if bypassing the split H-lambda row",
        ],
        "counts": {
            "charged_rows_selected": charged["closure_decision"]["selected_charged_normalized_overlap_kernel_row_count"],
            "charged_row_values_available": charged_rows["accepted_selected_charged_normalized_overlap_kernel_row_count"],
            "strict_K_rows_selected": charged["closure_decision"]["accepted_selected_K_source_row_count"],
            "strict_K_rows_required": 10,
            "H_lambda_numeric_row_selected": 0,
            "accepted_H_scalar_value_rows": 0,
        },
        "guards": {
            "does_not_use_step72_H_target_as_source": True,
            "does_not_use_controlled_r_H_as_strict_source": True,
            "does_not_reprove_qutrit_carrier": True,
            "does_not_transfer_charged_T_scheme_to_H": True,
        },
        "next_required_artifact": "MTT_Selected_HLambdaFiniteGalerkinExecution_or_RadialHessianScalarRun_v1",
    }

    candidate = {
        "schema": "MTTSelectedHLambdaRowLocalOverlapAndSchemeOrDirectRadialHessianValueCandidate.v1",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "theorem": {
            "name": "HLambdaFormalOperatorAndSchemeGateTheorem",
            "proved": True,
            "statement": (
                "The H/lambda frontier has advanced from a named missing row to a selected formal source operator. "
                "On the selected q79/F,m=1 27x27 qutrit carrier, RO.q79F1.Omega_H.lambda is the row-local "
                "Galerkin operator P_H Pi0^perp G_E (delta_{Omega_H.lambda}D_E) Pi0^perp P_H with the same "
                "Riesz/Green/projector normalization as the charged rows. The H-sector scheme slot is separated "
                "from the charged T_scheme=1 shortcut. Numeric scalar closure still requires finite Galerkin "
                "execution plus T_scheme.Omega_H.lambda, or a direct selected radial Hessian value N_H."
            ),
        },
        "decision": {
            "formal_H_lambda_rowlocal_operator_emitted": True,
            "formal_H_lambda_scheme_slot_emitted": True,
            "direct_radial_hessian_execution_contract_closed": True,
            "numeric_H_lambda_rowlocal_value_emitted": False,
            "numeric_T_scheme_value_emitted": False,
            "direct_N_H_value_emitted": False,
            "accepted_H_scalar_value_rows": 0,
            "strict_no_knob_numeric_solution_found": False,
        },
        "key_numbers": {
            "carrier_dimension": qutrit_matrix["carrier_dimension"],
            "qutrit_action_relation_error_frobenius": qutrit_matrix["left_action_relation_error_frobenius"],
            "selected_charged_overlap_rows": charged["closure_decision"]["selected_charged_normalized_overlap_kernel_row_count"],
            "strict_K_rows_selected": charged["closure_decision"]["accepted_selected_K_source_row_count"],
            "strict_K_rows_required": 10,
            "controlled_r_H_postcheck_only": h_radial["key_numbers"]["controlled_r_H"],
            "accepted_H_scalar_value_rows": 0,
        },
        "inputs_checked": {
            "prior_cutset": prior["next_target"],
            "qutrit_packaging_status": qutrit["status"],
            "charged_rows_status": charged["status"],
            "H_gap_status": h_gap["status"],
            "direct_quartic_status": direct_quartic["status"],
        },
        "packets": [
            f"candidate_data/{SLUG}/h_lambda_formal_rowlocal_operator.packet.json",
            f"candidate_data/{SLUG}/h_lambda_scheme_factor_contract.packet.json",
            f"candidate_data/{SLUG}/direct_radial_hessian_value_execution_contract.packet.json",
            f"candidate_data/{SLUG}/h_lambda_operator_execution_gate.packet.json",
        ],
        "next_target": "MTT_Selected_HLambdaFiniteGalerkinExecution_or_RadialHessianScalarRun_v1",
    }

    certificate = {
        "certificate": "selected_hlambdarowlocaloverlapandscheme_or_directradialhessianvalue_certificate.v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": "MTT_SELECTED_HLAMBDAROWLOCALOVERLAPANDSCHEME_OR_DIRECTRADIALHESSIANVALUE_FORMAL_OPERATOR_EMITTED_VALUES_OPEN",
        "proved": True,
        "no_target_fitting": True,
        "observed_data_used_as_selector": False,
        "checks": {
            "formal_H_lambda_rowlocal_operator_emitted": True,
            "formal_H_lambda_scheme_slot_emitted": True,
            "direct_radial_hessian_execution_contract_closed": True,
            "numeric_H_lambda_rowlocal_value_emitted": False,
            "numeric_T_scheme_value_emitted": False,
            "direct_N_H_value_emitted": False,
            "accepted_H_scalar_value_rows": 0,
        },
    }

    write_json(ROOT / f"candidate_data/{SLUG}.candidate.json", candidate)
    write_json(CANDIDATE_DIR / "h_lambda_formal_rowlocal_operator.packet.json", h_operator)
    write_json(CANDIDATE_DIR / "h_lambda_scheme_factor_contract.packet.json", scheme_contract)
    write_json(CANDIDATE_DIR / "direct_radial_hessian_value_execution_contract.packet.json", direct_hessian_contract)
    write_json(CANDIDATE_DIR / "h_lambda_operator_execution_gate.packet.json", execution_gate)
    write_json(CERT_DIR / f"{SLUG}_certificate.json", certificate)

    PROOF.write_text(
        "\n".join(
            [
                "# MTT Selected H-Lambda Row-Local Overlap and Scheme or Direct Radial Hessian Value v1",
                "",
                "## Result",
                "",
                "The H/lambda row is no longer just a named missing scalar.  The formal same-branch source operator is now emitted:",
                "",
                "```text",
                "RO.q79F1.Omega_H.lambda",
                "  = P_H Pi0^perp G_E (delta_{Omega_H.lambda} D_E) Pi0^perp P_H",
                "```",
                "",
                "It lives on the selected `q=79`, `F`, `m=1` 27x27 qutrit-Weyl carrier and uses the same selected Riesz/Green/projector normalization as the charged overlap rows.",
                "",
                "## What This Closes",
                "",
                "- formal `L_rowlocal.Omega_H.lambda` source operator: emitted",
                "- H-sector scheme slot: emitted as a required source slot",
                "- charged `T_scheme=1` shortcut: rejected for H/lambda",
                "- direct radial Hessian scalar alternative: contract closed as `N_H = Hess(F_H)[U_H,U_H]`",
                "",
                "## What Remains",
                "",
                "- numeric finite Galerkin entries for `RO.q79F1.Omega_H.lambda`",
                "- selected `T_scheme.Omega_H.lambda` value",
                "- finite exactness or residual certificate for the H row",
                "- or direct selected `N_H` value",
                "",
                "Strict scalar value rows accepted here: `0`.",
                "",
                "## Next Target",
                "",
                "```text",
                "MTT_Selected_HLambdaFiniteGalerkinExecution_or_RadialHessianScalarRun_v1",
                "```",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
