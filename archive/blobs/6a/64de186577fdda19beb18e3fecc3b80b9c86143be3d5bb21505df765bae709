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
    candidate = load_json("candidate_data/selected_omegavaluepayloadtransport_or_officiallikelihoodworkspace.candidate.json")
    cert = load_json("certificates/selected_omegavaluepayloadtransport_or_officiallikelihoodworkspace_certificate.json")
    omega = load_json("certificates/selected_strictomegaacceptancebridge_or_hlambdavectorrowbridge_certificate.json")
    profile = load_json("candidate_data/selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution/profile_likelihood_execution_summary.packet.json")
    promotion = load_json("candidate_data/selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution/precision_promotion_gate.packet.json")
    direct = load_json("certificates/selected_fullcovarianceprofileworkspace_or_internalrthetavaluerowsemission_certificate.json")
    contracted = load_json("certificates/selected_acceptedfulllikelihoodfunction_or_rthetacoefficientvaluerows_certificate.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims full closure")
    require(cert["closure_claimed"] is False, "certificate overclaims full closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require(candidate["target_fitting_used"] is False, "target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector used")

    require(omega["combined_K_to_Omega_formula_rows_closed"] is True, "Omega bridge not closed")
    require(omega["combined_K_to_Omega_formula_row_count"] == 10, "Omega bridge row count changed")
    require(omega["H_row_purpose_bridge_closed_at_formula_level"] is True, "H row-purpose bridge not closed")
    require(omega["accepted_algebraic_omega_source_formula_row_count"] == 10, "Omega algebraic row count changed")
    require(omega["accepted_profile_value_payload_row_count"] == 0, "previous bridge overaccepted profile values")
    require(omega["accepted_internal_scalar_value_row_count"] == 0, "previous bridge overaccepted scalar values")

    contract = candidate["transport_acceptance_contract"]
    require(contract["contract_closed"] is True, "transport contract not closed")
    require(contract["required_omega_source_formula_rows"] == 10, "required Omega row count changed")
    require(contract["available_omega_source_formula_rows"] == 10, "available Omega row count changed")
    require(contract["accepted_algebraic_omega_source_formula_rows"] == 10, "accepted algebraic count changed")
    require(len(contract["physical_transport_routes"]) == 2, "transport route count changed")

    current = candidate["current_execution_result"]
    require(current["old_L_T_H_formula_blocker_retired"] is True, "old formula blocker not retired")
    require(current["combined_K_to_Omega_formula_rows_closed"] is True, "candidate lost K-to-Omega closure")
    require(current["H_row_purpose_bridge_closed_at_formula_level"] is True, "candidate lost H formula bridge")
    require(current["diagonal_profile_likelihood_executed"] is True, "candidate did not import diagonal profile")
    require(current["coarse_diagonal_profile_passes"] is True, "candidate did not import coarse pass")
    require(current["accepted_as_full_covariance_profile"] is False, "candidate overpromotes full covariance")
    require(current["official_machine_readable_likelihood_imported"] is False, "candidate overimports official likelihood")
    require(current["selected_internal_V_Rtheta_value_payload_operator_closed"] is False, "candidate overcloses V_Rtheta")
    require(current["accepted_profile_value_payload_row_count"] == 0, "candidate overaccepts profile payloads")
    require(current["accepted_internal_scalar_value_row_count"] == 0, "candidate overaccepts scalar rows")
    require(current["accepted_true_equivalence_precision_rows"] == 0, "candidate overclaims true precision")

    require(profile["what_this_closes"]["diagonal_profile_likelihood_executed"] is True, "profile execution not closed")
    require(profile["profile_summary"]["passes_coarse_diagonal_profile"] is True, "coarse diagonal profile no longer passes")
    require(profile["profile_summary"]["accepted_as_full_covariance_profile"] is False, "profile summary overclaims full covariance")
    require(profile["accepted_for_true_precision_equivalence"] is False, "profile summary overclaims true precision")
    require(promotion["promotion_decision"]["accepted_for_diagonal_profile_execution"] is True, "promotion gate lost diagonal profile acceptance")
    require(promotion["promotion_decision"]["accepted_for_true_precision_equivalence"] is False, "promotion gate overclaims true precision")
    require(promotion["promotion_tests"]["full_correlated_covariance_profile_emitted"] is False, "promotion gate overemits full covariance")

    require(direct["full_covariance_profile_likelihood_closed"] is False, "direct execution overcloses full covariance")
    require(direct["accepted_as_official_profile_workspace"] is False, "direct execution overaccepts official workspace")
    require(direct["selected_Rtheta_source_rows_closed"] is False, "direct execution overcloses Rtheta source rows")
    require(direct["Rtheta_coefficient_values_closed"] is False, "direct execution overcloses Rtheta values")
    require(contracted["accepted_full_likelihood_function_or_workspace_closed"] is False, "contracted payload overcloses full likelihood")
    require(contracted["selected_Rtheta_source_rows_closed"] is False, "contracted payload overcloses Rtheta source rows")
    require(contracted["selected_Rtheta_coefficient_values_closed"] is False, "contracted payload overcloses Rtheta coefficient values")

    routes = candidate["route_evaluation"]
    require(routes["route_A_official_or_full_covariance_profile_workspace"]["accepted"] is False, "route A overaccepted")
    require(routes["route_B_selected_internal_V_Rtheta_value_payload_operator"]["accepted"] is False, "route B overaccepted")
    require(cert["transport_acceptance_contract_closed"] is True, "certificate lost transport contract")
    require(cert["old_L_T_H_formula_blocker_retired"] is True, "certificate did not retire old formula blocker")
    require(cert["route_count"] == 2, "certificate route count changed")
    require(cert["route_A_accepted"] is False, "certificate overaccepts route A")
    require(cert["route_B_accepted"] is False, "certificate overaccepts route B")
    require(cert["accepted_profile_value_payload_row_count"] == 0, "certificate overaccepts profile payloads")
    require(cert["accepted_internal_scalar_value_row_count"] == 0, "certificate overaccepts scalar rows")
    require(cert["accepted_true_equivalence_precision_rows"] == 0, "certificate overclaims true precision")
    require(cert["remaining_payload_count"] == 2, "remaining payload count changed")
    require(cert["next_required_artifact"] == candidate["frontier_reduction"]["preferred_next_artifact"], "next artifact mismatch")

    for key in [
        "replay_target_table_used_as_selector",
        "diagonal_profile_promoted_to_full_covariance",
        "algebraic_formula_rows_promoted_to_physical_values",
        "official_likelihood_workspace_imported",
        "global_directK_row_reopened",
        "locked_K_threshold_ledger_reopened",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(cert[key] is False, f"certificate overcloses/reopens: {key}")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "transport_acceptance_contract_closed": True,
                "available_omega_source_formula_rows": "10/10",
                "old_L_T_H_formula_blocker_retired": True,
                "route_A_accepted": False,
                "route_B_accepted": False,
                "accepted_internal_scalar_value_row_count": 0,
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected Omega value-payload transport / official likelihood workspace audit passed")


if __name__ == "__main__":
    main()
