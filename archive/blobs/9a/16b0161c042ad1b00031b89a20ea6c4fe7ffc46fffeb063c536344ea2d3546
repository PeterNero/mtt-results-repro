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
    candidate = load_json("candidate_data/selected_precisionlayerfullcovariance_or_internaltransport.candidate.json")
    cert = load_json("certificates/selected_precisionlayerfullcovariance_or_internaltransport_certificate.json")
    magprofile = load_json("certificates/selected_magprofilevaluefunctional_or_officialfullprofileworkspace_certificate.json")
    threshold_profile = load_json("certificates/selected_thresholdmatchingmassschemerowemission_or_profileworkspaceexit_certificate.json")
    precision = load_json("certificates/selected_precisionequivalencerows_or_truesmclosureaudit_certificate.json")
    transport = load_json("certificates/selected_precisiontransportcovariancerows_or_finaltruesmaudit_certificate.json")
    correlated = load_json("certificates/selected_correlatedthresholdprofilematrix_or_yukawahiggsprecisionpromotion_certificate.json")
    threshold_values = load_json("certificates/selected_thresholdmassschemevalues_or_correlatedlikelihoodsourceimport_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_PrecisionLayerFullCovarianceOrInternalTransport_v1.md").read_text(encoding="utf-8")

    status = "MTT_SELECTED_PRECISIONLAYERFULLCOVARIANCE_OR_INTERNALTRANSPORT_BUILT_DIAGONAL_PRECISION_TIER_CLOSED_FULL_COVARIANCE_OPEN"
    next_artifact = "MTT_Selected_PrecisionTransportValueObject_or_FinalTrueSMEquivalence_v1"

    require(candidate["status"] == status, "candidate status changed")
    require(cert["status"] == status, "certificate status changed")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(cert["closure_claimed"] is False, "certificate overclaims closure")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")
    require(candidate["target_fitting_used"] is False, "candidate target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "candidate observed selector used")

    require(magprofile["ten_value_payload_rows_closed"] is True, "value payload not closed")
    require(magprofile["accepted_internal_M_magprofile_value_rows"] == 10, "value payload row count changed")
    require(magprofile["accepted_true_equivalence_precision_rows"] == 0, "magprofile overclaims precision")

    closed = candidate["closed_now"]
    require(closed["M_magprofile_value_payload_rows"] == 10, "closed payload count changed")
    require(closed["M_magprofile_value_payload_closed_at_split_profile_tier"] is True, "payload tier not closed")
    require(closed["threshold_matching_source_rows_closed_at_admitted_external_tier"] is True, "threshold tier not closed")
    require(closed["mass_scheme_conversion_source_rows_closed_at_admitted_external_tier"] is True, "mass tier not closed")
    require(closed["accepted_external_threshold_row_count"] == 7, "threshold row count changed")
    require(closed["accepted_external_mass_scheme_row_count"] == 3, "mass row count changed")
    require(closed["accepted_diagonal_profile_theorem_closed"] is True, "diagonal theorem not closed")
    require(closed["post_pi_external_profile_readiness"] == "8/9", "readiness changed")
    require(closed["precision_transport_covariance_easy_wins_closed"] is True, "easy wins not closed")
    require(closed["easy_win_subgate_count_closed"] == 19, "easy win count changed")
    require(closed["full_8x8_covariance_target_shape_fixed"] is True, "8x8 target not fixed")
    require(closed["full_covariance_matrix_shape"] == [8, 8], "covariance shape changed")
    require(closed["full_covariance_symmetric_unique_entries"] == 36, "unique covariance count changed")

    require(threshold_profile["threshold_matching_source_rows_closed"] is True, "threshold profile source rows not closed")
    require(threshold_profile["mass_scheme_conversion_source_rows_closed"] is True, "mass profile source rows not closed")
    require(threshold_profile["accepted_external_threshold_row_count"] == 7, "threshold external count changed")
    require(threshold_profile["accepted_external_mass_scheme_row_count"] == 3, "mass external count changed")
    require(threshold_profile["accepted_diagonal_profile_theorem_closed"] is True, "diagonal profile theorem not closed")
    require(threshold_profile["full_covariance_profile_likelihood_closed"] is False, "threshold profile overclosed covariance")

    require(transport["precision_transport_covariance_easy_wins_closed"] is True, "transport easy wins not closed")
    require(transport["easy_win_subgate_count_closed"] == 19, "transport easy win count changed")
    require(transport["full_8x8_covariance_target_shape_fixed"] is True, "transport 8x8 target lost")
    require(transport["full_covariance_matrix_shape_fixed"] == [8, 8], "transport covariance shape changed")
    require(transport["full_covariance_symmetric_unique_entries"] == 36, "transport covariance entries changed")

    require(correlated["what_closes"]["surrogate_correlated_threshold_profile_matrix_emitted"] is True, "surrogate matrix not emitted")
    require(correlated["what_remains_open"]["published_or_reconstructed_profile_likelihood"] is True, "published likelihood no longer open")
    require(threshold_values["what_closes"]["threshold_mass_scheme_residual_values_emitted"] is True, "residual values not emitted")
    require(threshold_values["what_remains_open"]["published_or_reconstructed_profile_likelihood"] is True, "threshold values overclose likelihood")

    not_closed = candidate["not_closed"]
    for key in [
        "full_covariance_profile_likelihood_closed",
        "accepted_precision_profile_import_closed_somewhere",
        "profile_likelihood_imported_somewhere",
        "selected_internal_Rtheta_threshold_mass_derivation_closed",
        "selected_threshold_response_functional_value_instantiated",
        "multi_loop_RG_values_closed",
        "local_QFT_precision_observable_values_closed",
        "actual_dynamic_qasu3_operator_payload_closed",
        "true_precision_equivalence_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(not_closed[key] is False, f"not_closed overclosed: {key}")
    require(not_closed["accepted_true_equivalence_precision_rows"] == 0, "true precision rows overaccepted")
    require(precision["accepted_true_equivalence_precision_rows"] == 0, "precision cert overclaims true rows")

    remaining = candidate["remaining_exact_object"]
    require(remaining["name"] == "PrecisionTransportValueObject", "remaining object changed")
    require(remaining["required_shape"] == "8x8 covariance/profile value object plus scheme/scale transport into one common coordinate system", "required shape changed")
    require(remaining["required_symmetric_unique_entries"] == 36, "required covariance entries changed")
    require(remaining["current_available_full_covariance_entries"] == 0, "full covariance entries overaccepted")
    require(remaining["current_available_diagonal_profile_rows"] == 6, "diagonal row count changed")
    require(remaining["current_external_threshold_mass_rows"] == 10, "external threshold/mass row count changed")

    decision = candidate["decision"]
    require(decision["value_payload_layer_solved"] is True, "decision lost payload closure")
    require(decision["diagonal_precision_tier_closed"] is True, "decision lost diagonal precision")
    require(decision["full_precision_layer_solved"] is False, "decision overclosed full precision")
    require(decision["accepted_true_equivalence_precision_rows"] == 0, "decision overaccepted precision rows")
    require(decision["remaining_frontier_is_exactly_precision_transport_value_object"] is True, "decision frontier not exact")
    require(decision["next_required_artifact"] == next_artifact, "next artifact changed")
    require(cert["next_required_artifact"] == next_artifact, "certificate next artifact changed")

    for key in [
        "does_not_reopen_value_payload",
        "does_not_reopen_yukawa_magnitudes",
        "does_not_promote_diagonal_profile_to_full_covariance",
        "does_not_promote_external_rows_to_internal_no_knob_rows",
        "does_not_claim_true_precision_equivalence",
        "does_not_use_observed_values_as_selectors",
    ]:
        require(candidate["guards"][key] is True, f"guard failed: {key}")

    for phrase in [
        "value-payload layer is no longer the active blocker",
        "diagonal/readiness precision tier: closed",
        "Current full covariance entries accepted: `0`",
        next_artifact,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "value_payload_layer_solved": True,
                "diagonal_precision_tier_closed": True,
                "accepted_true_equivalence_precision_rows": 0,
                "remaining_exact_object": "PrecisionTransportValueObject",
                "next_required_artifact": next_artifact,
            },
            indent=2,
        )
    )
    print("selected precision layer full covariance / internal transport audit passed")


if __name__ == "__main__":
    main()
