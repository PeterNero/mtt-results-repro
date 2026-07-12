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
    candidate = load_json("candidate_data/selected_magprofilevaluefunctional_or_officialfullprofileworkspace.candidate.json")
    cert = load_json("certificates/selected_magprofilevaluefunctional_or_officialfullprofileworkspace_certificate.json")
    source_scalar = load_json("certificates/selected_magprofilesourcescalar_or_officialfullprofileworkspace_certificate.json")
    finite_replay = load_json("certificates/selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure_certificate.json")
    finite_execution = load_json("candidate_data/selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure/final_finite_replay_exactness_execution.packet.json")
    tail_rows = load_json("candidate_data/selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure/selected_finite_tail_source_rows.packet.json")
    direct_k = load_json("candidate_data/selected_strictpewdenominatorselectiontheorem_or_directkpromotion/promoted_direct_kthreshold_omega_h_lambda_row.packet.json")
    strict_pew = load_json("certificates/selected_strictpewdenominatorselectiontheorem_or_directkpromotion_certificate.json")
    common = load_json("candidate_data/selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution/versioned_common_scale_yukawa_higgs_values.packet.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_MagProfileValueFunctional_or_OfficialFullProfileWorkspace_v1.md").read_text(encoding="utf-8")

    status = "MTT_SELECTED_MAGPROFILEVALUEFUNCTIONAL_OR_OFFICIALFULLPROFILEWORKSPACE_BUILT_TEN_VALUE_PAYLOAD_ROWS_CLOSED_PRECISION_OPEN"
    next_artifact = "MTT_Selected_PrecisionLayerFullCovarianceOrInternalTransport_v1"

    require(candidate["status"] == status, "candidate status changed")
    require(cert["status"] == status, "certificate status changed")
    require(candidate["closure_claimed"] is False, "candidate overclaims full closure")
    require(cert["closure_claimed"] is False, "certificate overclaims full closure")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")
    require(candidate["target_fitting_used"] is False, "candidate target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "candidate observed selector used")

    require(source_scalar["accepted_strict_phase_antisymmetry_scalar_source_rows"] == 1, "source scalar not imported")
    require(source_scalar["finite_replay_yukawa_magnitude_closure_locked"] is True, "source scalar reopened Yukawa")
    require(finite_replay["accepted_finite_replay_yukawa_magnitude_rows"] == 9, "finite replay Yukawa rows changed")
    require(finite_replay["finite_replay_yukawa_exactness_closed"] is True, "finite replay Yukawa not closed")
    require(finite_replay["accepted_finite_tail_source_rows"] == 2, "finite tail row count changed")
    require(abs(finite_replay["actual_max_log_residual"] - 8.715792346058762e-14) < 1.0e-24, "finite replay residual changed")
    require(finite_execution["finite_replay_exactness_closed"] is True, "finite execution not closed")
    require(finite_execution["analytic_zero_residual"] is False, "analytic zero overclosed")
    require(len(tail_rows["rows"]) == 2, "tail row count changed")
    require(all(row["accepted_as_source_row"] is True for row in tail_rows["rows"]), "tail source row not accepted")

    require(strict_pew["accepted_global_strict_P_EW_source_rows"] == 1, "strict PEW row missing")
    require(strict_pew["accepted_global_direct_K_threshold_Omega_H_lambda_rows"] == 1, "direct K cert row missing")
    require(strict_pew["strict_zero_primitive_K_threshold_row_count"] == 10, "ten K threshold not closed")
    require(direct_k["status"] == "STRICT_DIRECT_K_THRESHOLD_OMEGA_H_LAMBDA_PROMOTED", "direct K row status changed")
    require(direct_k["last_row_payload_available"] is True, "direct K payload unavailable")
    require(abs(direct_k["lambda_H_value"] - 0.1260399999999988) < 1.0e-15, "direct K lambda value changed")

    vf = candidate["value_functional"]
    require(vf["row_count_required"] == 10, "required row count changed")
    require(vf["row_count_closed_at_value_payload_tier"] == 10, "ten-row value payload not closed")
    require(vf["charged_row_count"] == 9, "charged row count changed")
    require(vf["H_lambda_row_count"] == 1, "H row count changed")
    require(vf["accepted_internal_M_magprofile_value_rows"] == 10, "M_magprofile accepted value row count changed")
    require(vf["accepted_true_equivalence_precision_rows"] == 0, "true precision overclaimed")
    require(vf["full_covariance_profile_likelihood_closed"] is False, "full covariance overclosed")

    charged = candidate["charged_block"]
    require(charged["accepted_finite_replay_yukawa_magnitude_rows"] == 9, "charged rows changed")
    require(charged["finite_replay_yukawa_exactness_closed"] is True, "charged finite replay not closed")
    require(charged["analytic_zero_residual_closed"] is False, "charged analytic zero overclosed")
    require(abs(charged["actual_max_log_residual"] - 8.715792346058762e-14) < 1.0e-24, "charged residual changed")
    require(len(charged["charged_labels"]) == 9, "charged labels changed")
    require(len(charged["profile_values"]["abs_Y_u"]) == 3, "u profile count changed")
    require(len(charged["profile_values"]["abs_Y_d"]) == 3, "d profile count changed")
    require(len(charged["profile_values"]["abs_Y_e"]) == 3, "e profile count changed")

    h_block = candidate["H_lambda_block"]
    require(h_block["strict_P_EW_source_row_available"] is True, "H block lost PEW")
    require(h_block["strict_direct_K_threshold_Omega_H_lambda_rows"] == 1, "H direct K count changed")
    require(h_block["strict_zero_primitive_K_threshold_row_count"] == 10, "H ten K count changed")
    require(abs(h_block["lambda_H_value_from_direct_K_row"] - direct_k["lambda_H_value"]) < 1.0e-15, "H lambda mismatch")
    require(abs(h_block["common_scale_lambda_H_profile_value"] - common["derived_magnitudes"]["lambda_H"]) < 1.0e-15, "common lambda mismatch")
    require("true precision requires" in h_block["scale_scheme_mismatch_guard"], "scale guard missing")

    precision = candidate["precision_layer_status"]
    require(precision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(precision["true_precision_equivalence_closed"] is False, "true precision overclosed")
    require(precision["full_covariance_profile_likelihood_closed"] is False, "full covariance overclosed")
    require(precision["accepted_true_equivalence_precision_rows"] == 0, "precision rows overaccepted")
    require(precision["threshold_matching_source_rows_closed_at_admitted_external_tier"] is True, "threshold external tier lost")
    require(precision["mass_scheme_conversion_source_rows_closed_at_admitted_external_tier"] is True, "mass external tier lost")

    decision = candidate["decision"]
    require(decision["M_magprofile_value_functional_closed_at_split_profile_tier"] is True, "decision did not close value functional")
    require(decision["ten_value_payload_rows_closed"] is True, "decision did not close ten rows")
    require(decision["charged_value_rows_closed"] == 9, "decision charged count changed")
    require(decision["H_lambda_value_row_closed"] == 1, "decision H count changed")
    require(decision["replay_magnitudes_promoted_beyond_declared_tier"] is False, "decision overpromotes replay")
    require(decision["true_precision_equivalence_closed"] is False, "decision overcloses precision")
    require(decision["next_required_artifact"] == next_artifact, "next artifact changed")
    require(cert["next_required_artifact"] == next_artifact, "certificate next artifact changed")

    for key in [
        "does_not_reopen_27_matrix",
        "does_not_reopen_yukawa_magnitudes",
        "does_not_reopen_strict_PEW_directK_Kthreshold",
        "does_not_claim_full_covariance",
        "does_not_claim_true_precision_equivalence",
        "does_not_claim_analytic_zero_yukawa_residual",
        "does_not_use_observed_values_as_selectors",
    ]:
        require(candidate["guards"][key] is True, f"guard failed: {key}")

    for phrase in [
        "ten value-payload rows are closed",
        "8.715792346058762e-14",
        "not full true-precision equivalence",
        next_artifact,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "ten_value_payload_rows_closed": True,
                "accepted_internal_M_magprofile_value_rows": 10,
                "accepted_true_equivalence_precision_rows": 0,
                "next_required_artifact": next_artifact,
            },
            indent=2,
        )
    )
    print("selected MagProfile value functional / official full-profile workspace audit passed")


if __name__ == "__main__":
    main()
