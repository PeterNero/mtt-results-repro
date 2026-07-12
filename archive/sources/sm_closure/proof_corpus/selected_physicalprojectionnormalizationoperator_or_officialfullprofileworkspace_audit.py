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
    candidate = load_json("candidate_data/selected_physicalprojectionnormalizationoperator_or_officialfullprofileworkspace.candidate.json")
    cert = load_json("certificates/selected_physicalprojectionnormalizationoperator_or_officialfullprofileworkspace_certificate.json")
    identity = load_json("certificates/selected_internalvrthetavaluepayloadoperator_or_officialfullprofileworkspace_certificate.json")
    evaluator = load_json("certificates/selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation_certificate.json")
    gate = load_json("candidate_data/selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation/rtheta_value_evaluator_execution_gate.packet.json")
    recheck = load_json("candidate_data/selected_rtheta_valueevaluatorexecution_or_thresholdresponseinstantiation/rtheta_coefficient_value_recheck_after_pi_closure.packet.json")
    weights = load_json("candidate_data/selected_thresholdresponserows_or_sectorprojectionweightsexecution/source_normalized_sector_projection_weights.packet.json")
    step69 = load_json("candidate_data/selected_step69_hymthresholdprefactorrows_or_omegascalarexecution/step69_prefactor_solution_formula_rows.packet.json")
    threshold_profile = load_json("certificates/selected_thresholdmatchingmassschemerowemission_or_profileworkspaceexit_certificate.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(cert["closure_claimed"] is False, "certificate overclaims closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require(candidate["target_fitting_used"] is False, "target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector used")

    require(identity["selected_physical_projection_normalization_operator_N_phys_closed"] is False, "previous identity packet overclosed N_phys")
    require(evaluator["Pi_Rtheta_closed"] is True, "later Pi_Rtheta closure not imported")
    require(evaluator["selected_dynamic_operator_source_owner_closed"] is True, "dynamic source owner not closed")
    require(evaluator["selected_threshold_response_functional_instantiated"] is False, "threshold response unexpectedly instantiated")
    require(evaluator["accepted_coefficient_value_count"] == 0, "evaluator overaccepts coefficient values")
    require(gate["coefficient_functional_skeleton_closed"] is True, "coefficient skeleton not closed")
    require(gate["source_normalized_projection_weights_closed"] is True, "source-normalized weights not closed")
    require(gate["magnitude_bearing_projection_weights_closed"] is False, "gate overcloses magnitude weights")
    require(gate["selected_threshold_response_functional_instantiated"] is False, "gate overinstantiates threshold response")
    require(recheck["accepted_coefficient_value_count"] == 0, "recheck overaccepts coefficients")
    require(recheck["lambda_H_value_selected"] is False, "recheck overselects lambda_H")
    require(recheck["selected_value_evaluator_closed"] is False, "recheck overcloses evaluator")

    split = candidate["N_phys_split"]
    require(split["Pi_Rtheta_projection_kernel_closed"] is True, "N_phys lost Pi_Rtheta closure")
    require(split["source_normalized_projection_weights_closed"] is True, "N_phys lost source weights")
    require(split["source_normalized_weight_value"] == 1.0, "source weight value changed")
    require(split["magnitude_bearing_projection_weights_closed"] is False, "N_phys overcloses magnitude weights")
    require(split["selected_threshold_response_functional_instantiated"] is False, "N_phys overinstantiates threshold response")
    require(split["accepted_as_final_physical_value_payload_operator"] is False, "N_phys overaccepted final operator")

    ten = candidate["ten_slot_transport_recheck"]
    require(step69["formula_row_count"] == 10, "Step69 formula row count changed")
    require(len({row["scalar_label"] for row in step69["formula_rows"]}) == 10, "scalar labels not ten")
    require(ten["slot_count"] == 10, "ten-slot recheck slot count changed")
    require(ten["omega_source_formula_rows_available"] == 10, "Omega rows not available")
    require(ten["scalar_label_rows_available"] == 10, "scalar labels not available")
    require(ten["projection_and_unit_normalization_ready_for_all_slots"] is True, "projection/unit readiness not closed")
    require(ten["magnitude_profile_value_payload_ready_for_all_slots"] is False, "magnitude/profile overready")
    require(ten["accepted_physical_scalar_value_rows"] == 0, "physical scalar rows overaccepted")

    sectors = candidate["sector_weight_recheck"]
    require(weights["source_projection_weights_closed"] is True, "source projection weights not closed")
    require(weights["magnitude_bearing_projection_weights_closed"] is False, "weights overclose magnitude-bearing rows")
    require(len(weights["sector_weights"]) == sectors["source_normalized_sector_count"], "sector count mismatch")
    require(all(row["source_normalized_weight"] == 1.0 for row in weights["sector_weights"]), "non-unit source weight found")
    require(all(row["magnitude_bearing_weight"] is None for row in weights["sector_weights"]), "magnitude-bearing weight unexpectedly present")
    require(sectors["unit_weight_rows_closed"] == 4, "unit weight row count changed")
    require(sectors["magnitude_bearing_weight_rows_closed"] == 0, "magnitude weight row count changed")

    require(threshold_profile["accepted_diagonal_profile_theorem_closed"] is True, "diagonal profile support not closed")
    require(threshold_profile["full_covariance_profile_likelihood_closed"] is False, "threshold/profile overcloses full covariance")
    require(threshold_profile["accepted_internal_selected_Rtheta_threshold_mass_row_count"] == 0, "threshold/profile overaccepts internal rows")

    decision = candidate["decision"]
    require(decision["N_phys_projection_unit_spine_closed"] is True, "decision lost N_phys spine closure")
    require(decision["N_phys_final_value_operator_closed"] is False, "decision overcloses N_phys final operator")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "decision overaccepts scalar rows")
    require(decision["preferred_next_artifact"] == cert["next_required_artifact"], "next artifact mismatch")

    require(cert["N_phys_projection_unit_spine_closed"] is True, "certificate lost N_phys spine closure")
    require(cert["N_phys_final_value_operator_closed"] is False, "certificate overcloses final N_phys")
    require(cert["Pi_Rtheta_projection_kernel_closed"] is True, "certificate lost Pi_Rtheta")
    require(cert["source_normalized_projection_weights_closed"] is True, "certificate lost source weights")
    require(cert["magnitude_bearing_projection_weights_closed"] is False, "certificate overcloses magnitude weights")
    require(cert["selected_threshold_response_functional_instantiated"] is False, "certificate overinstantiates threshold response")
    require(cert["ten_slot_transport_recheck_closed"] is True, "certificate lost ten-slot recheck")
    require(cert["accepted_internal_scalar_value_row_count"] == 0, "certificate overaccepts scalar rows")
    require(cert["accepted_true_equivalence_precision_rows"] == 0, "certificate overclaims true precision")

    for key in [
        "older_Pi_Rtheta_open_status_reopened",
        "unit_source_weights_promoted_to_magnitude_values",
        "admitted_external_threshold_mass_rows_promoted_to_internal_no_knob_rows",
        "diagonal_profile_promoted_to_full_covariance",
        "official_likelihood_workspace_imported",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(cert[key] is False, f"certificate overcloses/reopens: {key}")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "N_phys_projection_unit_spine_closed": True,
                "Pi_Rtheta_projection_kernel_closed": True,
                "unit_weight_rows_closed": 4,
                "magnitude_bearing_weight_rows_closed": 0,
                "accepted_internal_scalar_value_row_count": 0,
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected physical projection-normalization operator / official full-profile workspace audit passed")


if __name__ == "__main__":
    main()
