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
    candidate = load_json("candidate_data/selected_magnitudebearingnormalizationfunctional_or_officialfullprofileworkspace.candidate.json")
    cert = load_json("certificates/selected_magnitudebearingnormalizationfunctional_or_officialfullprofileworkspace_certificate.json")
    nphys = load_json("certificates/selected_physicalprojectionnormalizationoperator_or_officialfullprofileworkspace_certificate.json")
    finite_replay = load_json("certificates/selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure_certificate.json")
    common = load_json("candidate_data/selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution/versioned_common_scale_yukawa_higgs_values.packet.json")
    promotion = load_json("candidate_data/selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution/precision_promotion_gate.packet.json")
    residual = load_json("candidate_data/selected_yukawafiniteprojectedoperatorresidualsource_or_exactmagnitudeclosure.candidate.json")
    weights = load_json("candidate_data/selected_thresholdresponserows_or_sectorprojectionweightsexecution/source_normalized_sector_projection_weights.packet.json")

    require(candidate["status"] == cert["status"], "candidate/certificate status mismatch")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(cert["closure_claimed"] is False, "certificate overclaims closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem not proved")
    require(candidate["target_fitting_used"] is False, "candidate target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector used")

    require(nphys["N_phys_projection_unit_spine_closed"] is True, "N_phys spine not closed")
    require(nphys["N_phys_final_value_operator_closed"] is False, "N_phys final operator overclosed")
    require(nphys["magnitude_bearing_projection_weights_closed"] is False, "N_phys overcloses magnitude weights")
    require(finite_replay["accepted_finite_replay_yukawa_magnitude_rows"] == 9, "finite replay Yukawa row count changed")
    require(finite_replay["finite_replay_yukawa_exactness_closed"] is True, "finite replay exactness not closed")
    require(finite_replay["global_true_SM_no_knob_closure"] is False, "finite replay overclaims no-knob")
    require(common["accepted_as_versioned_common_scale_candidate_values"] is True, "common-scale values not emitted")
    require(common["accepted_for_profile_execution_input"] is True, "common-scale profile input unavailable")
    require(common["accepted_as_no_knob_MTT_prediction"] is False, "common-scale overclaims no-knob")
    require(common["accepted_for_true_precision_equivalence"] is False, "common-scale overclaims true precision")
    require(len(common["derived_magnitudes"]["diag_abs_Y_u"]) == 3, "u magnitude count changed")
    require(len(common["derived_magnitudes"]["diag_abs_Y_d"]) == 3, "d magnitude count changed")
    require(len(common["derived_magnitudes"]["diag_abs_Y_e"]) == 3, "e magnitude count changed")
    require("lambda_H" in common["derived_magnitudes"], "lambda_H magnitude missing")
    require(promotion["promotion_tests"]["coarse_diagonal_profile_passes"] is True, "coarse profile no longer passes")
    require(promotion["promotion_decision"]["accepted_for_true_precision_equivalence"] is False, "promotion overclaims true precision")
    require(weights["magnitude_bearing_projection_weights_closed"] is False, "unit weights overclose magnitudes")
    require(residual["target_fitting_used"] is True, "residual attempt no longer records fitting")
    require(residual["closure_decision"]["phase_split_scalar_source_selected"] is False, "phase split scalar overselected")
    require(residual["closure_decision"]["strict_no_knob_yukawa_closure"] is False, "residual attempt overcloses no-knob")

    gate = candidate["M_magprofile_promotion_gate"]
    require(gate["gate_closed"] is True, "promotion gate not closed")
    require(gate["required_scalar_label_count"] == 10, "required scalar count changed")
    require(gate["replay_profile_scalar_label_count_available"] == 10, "available scalar count changed")
    require(gate["finite_replay_charged_yukawa_rows_available"] == 9, "finite replay rows not imported")
    require(gate["common_scale_charged_magnitude_rows_available"] == 9, "common charged count changed")
    require(gate["common_scale_lambda_H_row_available"] == 1, "lambda_H row not imported")
    require(gate["accepted_as_no_knob_MTT_prediction"] is False, "gate overclaims no-knob")
    require(gate["selected_source_functional_closed"] is False, "gate overcloses source functional")
    require(gate["accepted_physical_payload_row_count"] == 0, "gate overaccepts payload rows")

    rejection = candidate["strict_source_rejection"]
    require(rejection["finite_replay_rows_are_profile_tier"] is True, "finite replay tier guard missing")
    require(rejection["common_scale_values_are_profile_input_only"] is True, "common-scale tier guard missing")
    require(rejection["unit_source_weights_are_not_magnitude_values"] is True, "unit-weight guard missing")
    require(rejection["finite_projected_residual_attempt_target_fitting_used"] is True, "residual fitting guard missing")
    require(rejection["phase_split_scalar_source_selected"] is False, "phase split scalar overselected")
    require(rejection["official_full_profile_workspace_imported"] is False, "official workspace overimported")

    inventory = candidate["value_inventory"]
    require(len(inventory["charged_yukawa_magnitude_labels"]) == 9, "charged label count changed")
    require(inventory["accepted_replay_or_profile_label_count"] == 10, "replay/profile label count changed")
    require(inventory["accepted_internal_no_knob_label_count"] == 0, "internal no-knob label count changed")

    decision = candidate["decision"]
    require(decision["M_magprofile_promotion_gate_closed"] is True, "decision lost gate closure")
    require(decision["M_magprofile_final_source_functional_closed"] is False, "decision overcloses source functional")
    require(decision["accepted_internal_scalar_value_row_count"] == 0, "decision overaccepts scalar rows")
    require(decision["preferred_next_artifact"] == cert["next_required_artifact"], "next artifact mismatch")

    require(cert["M_magprofile_promotion_gate_closed"] is True, "certificate lost gate closure")
    require(cert["M_magprofile_final_source_functional_closed"] is False, "certificate overcloses final source functional")
    require(cert["replay_profile_scalar_label_count_available"] == 10, "certificate scalar count changed")
    require(cert["accepted_internal_no_knob_label_count"] == 0, "certificate overaccepts no-knob labels")
    require(cert["accepted_internal_scalar_value_row_count"] == 0, "certificate overaccepts scalar rows")
    require(cert["accepted_true_equivalence_precision_rows"] == 0, "certificate overclaims true precision")

    for key in [
        "replay_magnitudes_promoted_to_no_knob_source_rows",
        "common_scale_profile_values_used_as_selector",
        "target_fitted_residual_scalar_promoted",
        "unit_source_weights_promoted_to_magnitude_values",
        "diagonal_profile_promoted_to_full_covariance",
        "official_likelihood_workspace_imported",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(cert[key] is False, f"certificate overcloses: {key}")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "M_magprofile_promotion_gate_closed": True,
                "replay_profile_scalar_label_count_available": 10,
                "accepted_internal_no_knob_label_count": 0,
                "phase_split_scalar_source_selected": False,
                "next_required_artifact": cert["next_required_artifact"],
            },
            indent=2,
        )
    )
    print("selected magnitude-bearing normalization functional / official full-profile workspace audit passed")


if __name__ == "__main__":
    main()
