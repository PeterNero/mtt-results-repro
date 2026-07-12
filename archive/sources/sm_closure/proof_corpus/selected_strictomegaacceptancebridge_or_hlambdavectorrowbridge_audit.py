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
    candidate = load_json("candidate_data/selected_strictomegaacceptancebridge_or_hlambdavectorrowbridge.candidate.json")
    cert = load_json("certificates/selected_strictomegaacceptancebridge_or_hlambdavectorrowbridge_certificate.json")
    lt_bridge = load_json("certificates/selected_lrowlocaltschemelambdah_sourceexecution_or_officiallikelihoodworkspace_certificate.json")
    vector = load_json("certificates/selected_rthetathresholdresponsevectoremitter_or_officiallikelihoodworkspace_certificate.json")
    step69 = load_json("candidate_data/selected_step69_hymthresholdprefactorrows_or_omegascalarexecution/step69_prefactor_solution_formula_rows.packet.json")
    step70 = load_json("candidate_data/selected_step70_heattorsionprefactorbackimport_or_rowlocalfrontier/step70_prefactor_slot_factorization.packet.json")
    step72 = load_json("candidate_data/selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance/step72_strict_rowlocal_omega_acceptance_predicate.packet.json")
    ten_k = load_json("candidate_data/selected_lambdahlastrowpayload_or_strictdirectkclosure/ten_kthreshold_ledger_current_standard.packet.json")
    direct_h = load_json("candidate_data/selected_strictpewdenominatorselectiontheorem_or_directkpromotion/promoted_direct_kthreshold_omega_h_lambda_row.packet.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims full closure")
    require(cert["closure_claimed"] is False, "certificate overclaims full closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require(candidate["target_fitting_used"] is False, "target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector used")

    require(lt_bridge["charged_L_rowlocal_subfields_closed"] is True, "charged L bridge not closed")
    require(lt_bridge["charged_T_scheme_subfields_closed"] is True, "charged T bridge not closed")
    require(lt_bridge["charged_K_threshold_row_count"] == 9, "charged K count changed")
    require(lt_bridge["global_direct_K_threshold_Omega_H_lambda_row_count"] == 1, "H direct K support missing")
    require(vector["vector_emitter_factorization_closed"] is True, "vector factorization not closed")
    require(vector["all_rows_have_D_fin_and_theta_weight"] is True, "D/theta support lost")

    require(step69["formula_row_count"] == 10, "Step69 formula row count changed")
    require(step69["accepted_formula_skeleton_row_count"] == 10, "Step69 formula skeleton count changed")
    require(step69["accepted_full_omega_source_row_count"] == 0, "Step69 unexpectedly accepted Omega rows")
    require(step70["factor_row_count"] == 10, "Step70 factor row count changed")
    require(step70["accepted_factorization_row_count"] == 10, "Step70 factorization count changed")
    require(step70["accepted_finite_heat_torsion_subsource_count"] == 2, "Step70 D_fin support changed")
    require(step72["strict_acceptance_result"]["accepted_omega_source_row_count"] == 0, "Step72 unexpectedly accepted Omega rows")
    require(step72["strict_acceptance_result"]["accepted_internal_scalar_value_row_count"] == 0, "Step72 unexpectedly accepted scalar rows")

    require(ten_k["accepted_full_ten_row_K_threshold_row_count_under_current_standard"] == 10, "ten K current-standard count changed")
    require(ten_k["charged_K_threshold_rows"] == 9, "ten K charged count changed")
    require(ten_k["H_lambda_K_threshold_rows_under_oneprimitive"] == 1, "ten K H count changed")
    require(direct_h["combined_kernel_row_id"] == "K_threshold.Omega_H.lambda", "direct H row id changed")
    require(direct_h["strict_direct_K_threshold_Omega_H_lambda_rows"] == 1, "direct H row not promoted")
    require(direct_h["strict_zero_primitive_K_threshold_row_count"] == 10, "direct H strict K count changed")

    step69_ids = {row["omega_id"] for row in step69["formula_rows"]}
    step70_ids = {row["omega_id"] for row in step70["factor_rows"]}
    ten_k_ids = {row["omega_id"] for row in ten_k["rows"]}
    require(len(step69_ids) == 10, "Step69 omega ids not ten")
    require(step69_ids == step70_ids == ten_k_ids, "omega id sets do not align")
    require("Omega_H.lambda" in step69_ids, "H lambda omega id missing")

    algebra = candidate["algebraic_bridge"]
    require(algebra["combined_K_to_Omega_formula_rows_closed"] is True, "algebraic bridge not closed")
    require(algebra["combined_K_to_Omega_formula_row_count"] == 10, "algebraic bridge count changed")
    require(algebra["charged_K_threshold_rows_available"] == 9, "candidate charged K count changed")
    require(algebra["H_direct_K_threshold_row_available"] == 1, "candidate H direct K count changed")
    require(algebra["ten_K_threshold_rows_available"] == 10, "candidate ten K count changed")
    require(algebra["H_row_purpose_bridge_closed_at_formula_level"] is True, "H row-purpose formula bridge not closed")
    require(algebra["strict_direct_K_threshold_Omega_H_lambda_rows"] == 1, "candidate direct K row count changed")
    require(algebra["strict_zero_primitive_K_threshold_row_count"] == 10, "candidate strict K count changed")

    split = candidate["acceptance_split"]
    require(split["accepted_algebraic_omega_source_formula_row_count"] == 10, "algebraic formula row acceptance count changed")
    require(split["accepted_profile_value_payload_row_count"] == 0, "candidate overaccepts profile value payloads")
    require(split["accepted_internal_scalar_value_row_count"] == 0, "candidate overaccepts scalar rows")
    require(split["accepted_true_equivalence_precision_rows"] == 0, "candidate overclaims true precision")
    require(split["strict_omega_acceptance_closed_for_final_scalar_values"] is False, "candidate overcloses final scalar values")
    require(split["official_likelihood_workspace_imported"] is False, "candidate overimports official workspace")

    frontier = candidate["frontier_reduction"]
    require(frontier["remaining_payload_count"] == 2, "remaining payload count changed")
    require(frontier["preferred_next_artifact"] == cert["next_required_artifact"], "next artifact mismatch")

    for key in [
        "combined_K_to_Omega_formula_rows_closed",
        "H_row_purpose_bridge_closed_at_formula_level",
    ]:
        require(cert[key] is True, f"certificate lost true field: {key}")
    for key in [
        "strict_omega_acceptance_closed_for_final_scalar_values",
        "official_likelihood_workspace_imported",
        "replay_target_table_used_as_selector",
        "admitted_external_replay_promoted_to_internal_rows",
        "global_directK_row_reopened",
        "locked_K_threshold_ledger_reopened",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(cert[key] is False, f"certificate overcloses/reopens: {key}")
    require(cert["accepted_algebraic_omega_source_formula_row_count"] == 10, "certificate algebraic row count changed")
    require(cert["accepted_profile_value_payload_row_count"] == 0, "certificate overaccepts profile payloads")
    require(cert["accepted_internal_scalar_value_row_count"] == 0, "certificate overaccepts scalar rows")
    require(cert["accepted_true_equivalence_precision_rows"] == 0, "certificate overclaims true precision")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "combined_K_to_Omega_formula_rows_closed": "10/10",
                "H_row_purpose_bridge_closed_at_formula_level": True,
                "accepted_algebraic_omega_source_formula_row_count": 10,
                "accepted_internal_scalar_value_row_count": 0,
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected strict Omega acceptance / H-lambda vector bridge audit passed")


if __name__ == "__main__":
    main()
