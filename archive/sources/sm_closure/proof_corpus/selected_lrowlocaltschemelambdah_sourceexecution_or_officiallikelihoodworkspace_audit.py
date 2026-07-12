from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    candidate = load_json("candidate_data/selected_lrowlocaltschemelambdah_sourceexecution_or_officiallikelihoodworkspace.candidate.json")
    cert = load_json("certificates/selected_lrowlocaltschemelambdah_sourceexecution_or_officiallikelihoodworkspace_certificate.json")
    previous = load_json("certificates/selected_rthetathresholdresponsevectoremitter_or_officiallikelihoodworkspace_certificate.json")
    qsel = load_json("candidate_data/selected_retardedoverlapspectralpairing_or_independentquadraturevalues/independent_qsel_quadrature_values.packet.json")
    tscheme = load_json("candidate_data/selected_thresholddeltarows_or_lambdahpayloadexecution/charged_source_native_tscheme_rows.packet.json")
    charged_k = load_json("candidate_data/selected_tschemenulldelta_reconciliation_or_lambdahlastrow/accepted_charged_kthreshold_rows_current.packet.json")
    charged_cert = load_json("certificates/selected_tschemenulldelta_reconciliation_or_lambdahlastrow_certificate.json")
    lambda_cert = load_json("certificates/selected_lambdahlastrowpayload_or_strictdirectkclosure_certificate.json")
    directk_cert = load_json("certificates/selected_strictpewdenominatorselectiontheorem_or_directkpromotion_certificate.json")
    step72 = load_json("candidate_data/selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance/step72_strict_rowlocal_omega_acceptance_predicate.packet.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims full closure")
    require(cert["closure_claimed"] is False, "certificate overclaims full closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require(candidate["target_fitting_used"] is False, "target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector used")
    require(cert["target_fitting_used"] is False, "certificate target fitting used")
    require(cert["observed_data_used_as_selector"] is False, "certificate observed selector used")

    require(previous["vector_emitter_factorization_closed"] is True, "previous vector factorization not closed")
    require(previous["accepted_vector_emitter_count"] == 0, "previous vector already accepted unexpectedly")
    require(previous["next_required_artifact"] == "MTT_Selected_LRowlocalTSchemeLambdaH_SourceExecution_or_OfficialLikelihoodWorkspace_v1", "previous next artifact changed")

    require(qsel["accepted_selected_Q_sel_quadrature_value_count"] == 9, "Q_sel row count changed")
    require(qsel["accepted_strict_L_rowlocal_row_count"] == 9, "strict L_rowlocal count changed")
    require(set(qsel["distinct_L_rowlocal_values"]) == {1.367835979172, 0.683917989586}, "distinct L values changed")

    require(tscheme["selected_T_scheme_source_row_count"] == 9, "T_scheme row count changed")
    for row in tscheme["rows"]:
        require(row["selected_as_source_native_T_scheme_row"] is True, f"T row not selected: {row['omega_id']}")
        require(row["T_scheme_source_native"] == 1.0, f"T row not unity: {row['omega_id']}")

    require(charged_k["accepted_selected_charged_K_threshold_row_count"] == 9, "charged K row count changed")
    require(charged_k["accepted_selected_T_scheme_source_row_count"] == 9, "charged K T count changed")
    require(charged_k["accepted_strict_Lrowlocal_row_count"] == 9, "charged K L count changed")
    charged_omega_ids = [row["omega_id"] for row in charged_k["rows"]]
    require(charged_omega_ids == candidate["charged_subfield_execution"]["imported_omega_ids"], "imported omega ids mismatch")
    for row in charged_k["rows"]:
        require(row["accepted_as_strict_L_rowlocal_row"] is True, f"K row lacks L: {row['omega_id']}")
        require(row["accepted_as_selected_T_scheme_source_row"] is True, f"K row lacks T: {row['omega_id']}")
        require(row["accepted_as_selected_charged_K_threshold_row"] is True, f"K row not accepted: {row['omega_id']}")
        require(row["selected_T_scheme_source_native"] == 1.0, f"K row T not unity: {row['omega_id']}")
        require(row["formula"] == "K_threshold_i = L_rowlocal_i * T_scheme_i = L_rowlocal_i", f"K row formula changed: {row['omega_id']}")

    require(charged_cert["accepted_selected_T_scheme_source_row_count"] == 9, "charged cert T count changed")
    require(charged_cert["accepted_selected_charged_K_threshold_row_count"] == 9, "charged cert K count changed")
    require(charged_cert["accepted_strict_Lrowlocal_row_count"] == 9, "charged cert L count changed")

    require(lambda_cert["accepted_H_lambda_K_threshold_row_count_under_current_standard"] == 1, "H lambda current-standard row missing")
    require(lambda_cert["accepted_full_ten_row_K_threshold_row_count_under_current_standard"] == 10, "current-standard ten K not closed")
    require(lambda_cert["H_specific_parameter_count"] == 0, "H-specific parameter count changed")
    require(directk_cert["accepted_global_direct_K_threshold_Omega_H_lambda_rows"] == 1, "global direct-K row missing")
    require(directk_cert["strict_zero_primitive_K_threshold_row_count"] == 10, "strict zero-primitive K count changed")

    require(step72["strict_acceptance_result"]["accepted_omega_source_row_count"] == 0, "Step72 already accepted Omega rows unexpectedly")
    require(step72["strict_acceptance_result"]["accepted_internal_scalar_value_row_count"] == 0, "Step72 already accepted scalar rows unexpectedly")
    require(step72["strict_acceptance_predicate"]["ten_rowlocal_overlap_rows_required"] is True, "Step72 predicate changed")

    exec_block = candidate["charged_subfield_execution"]
    require(exec_block["charged_L_rowlocal_subfields_closed"] is True, "charged L subfields not closed")
    require(exec_block["charged_L_rowlocal_subfield_count"] == 9, "candidate L count changed")
    require(exec_block["charged_T_scheme_subfields_closed"] is True, "charged T subfields not closed")
    require(exec_block["charged_T_scheme_subfield_count"] == 9, "candidate T count changed")
    require(exec_block["charged_T_scheme_value"] == 1.0, "candidate T value changed")
    require(exec_block["charged_K_threshold_rows_available"] is True, "charged K rows not available")
    require(exec_block["charged_K_threshold_row_count"] == 9, "candidate K count changed")
    require(exec_block["charged_rows_imported_into_Rtheta_vector_contract"] is True, "charged rows not imported into vector contract")

    h_status = candidate["H_lambda_status"]
    require(h_status["global_direct_K_threshold_Omega_H_lambda_row_locked"] is True, "global H row not locked")
    require(h_status["global_direct_K_threshold_Omega_H_lambda_row_count"] == 1, "global H row count changed")
    require(h_status["global_ten_K_threshold_ledger_locked"] is True, "global ten K ledger not locked")
    require(h_status["strict_zero_primitive_K_threshold_row_count"] == 10, "candidate strict K count changed")
    require(h_status["H_lambda_support_available"] is True, "H lambda support not available")
    require(h_status["H_lambda_Rtheta_vector_slot_bridge_closed"] is False, "candidate overcloses H/Rtheta bridge")
    require(h_status["H_specific_parameter_count"] == 0, "candidate H-specific parameter count changed")

    omega = candidate["strict_omega_acceptance_status"]
    require(omega["D_fin_and_theta_support_closed_from_previous_frontier"] is True, "D/theta support lost")
    require(omega["charged_L_and_T_support_now_closed"] is True, "charged L/T support not closed")
    require(omega["strict_Omega_acceptance_closed"] is False, "candidate overcloses Omega acceptance")
    require(omega["accepted_vector_emitter_count"] == 0, "candidate overaccepts vector emitter")
    require(omega["accepted_omega_source_row_count"] == 0, "candidate overaccepts Omega rows")
    require(omega["accepted_internal_scalar_value_row_count"] == 0, "candidate overaccepts scalar rows")

    frontier = candidate["frontier_reduction"]
    require("selected_L_rowlocal_i for nine charged rows" in frontier["now_closed_subfields"], "frontier did not close charged L")
    require("selected_T_scheme_i for nine charged rows" in frontier["now_closed_subfields"], "frontier did not close charged T")
    require(frontier["remaining_payload_count"] == 2, "remaining payload count changed")
    require(frontier["preferred_next_artifact"] == cert["next_required_artifact"], "next artifact mismatch")

    for key in [
        "charged_L_rowlocal_subfields_closed",
        "charged_T_scheme_subfields_closed",
        "charged_K_threshold_rows_available",
        "charged_rows_imported_into_Rtheta_vector_contract",
        "global_direct_K_threshold_Omega_H_lambda_row_locked",
        "global_ten_K_threshold_ledger_locked",
        "H_lambda_support_available",
        "D_fin_and_theta_support_closed_from_previous_frontier",
    ]:
        require(cert[key] is True, f"certificate lost true field: {key}")
    for key in [
        "H_lambda_Rtheta_vector_slot_bridge_closed",
        "strict_Omega_acceptance_closed",
        "admitted_external_replay_promoted_to_internal_rows",
        "global_directK_row_reopened",
        "locked_K_threshold_ledger_reopened",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(cert[key] is False, f"certificate overcloses/reopens: {key}")
    require(cert["charged_L_rowlocal_subfield_count"] == 9, "certificate L count changed")
    require(cert["charged_T_scheme_subfield_count"] == 9, "certificate T count changed")
    require(cert["charged_T_scheme_value"] == 1.0, "certificate T value changed")
    require(cert["charged_K_threshold_row_count"] == 9, "certificate charged K count changed")
    require(cert["global_direct_K_threshold_Omega_H_lambda_row_count"] == 1, "certificate H row count changed")
    require(cert["strict_zero_primitive_K_threshold_row_count"] == 10, "certificate strict K count changed")
    require(cert["H_specific_parameter_count"] == 0, "certificate H-specific count changed")
    require(cert["accepted_vector_emitter_count"] == 0, "certificate overaccepts emitter")
    require(cert["accepted_omega_source_row_count"] == 0, "certificate overaccepts Omega")
    require(cert["accepted_internal_scalar_value_row_count"] == 0, "certificate overaccepts scalar")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "charged_L_rowlocal_subfields_closed": "9/9",
                "charged_T_scheme_subfields_closed": "9/9",
                "charged_K_threshold_rows_available": "9/9",
                "global_direct_K_threshold_Omega_H_lambda_row_locked": True,
                "strict_Omega_acceptance_closed": False,
                "accepted_omega_source_row_count": 0,
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected Lrowlocal/Tscheme/lambdaH source execution audit passed")


if __name__ == "__main__":
    main()
