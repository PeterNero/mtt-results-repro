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
    candidate = load_json("candidate_data/selected_magprofilesourcescalar_or_officialfullprofileworkspace.candidate.json")
    cert = load_json("certificates/selected_magprofilesourcescalar_or_officialfullprofileworkspace_certificate.json")
    old_gate = load_json("certificates/selected_magnitudebearingnormalizationfunctional_or_officialfullprofileworkspace_certificate.json")
    strict_phase = load_json("certificates/selected_strictphaseantisymmetryscalarderivation_or_noknobyukawaexactness_certificate.json")
    finite_replay = load_json("certificates/selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure_certificate.json")
    derivation = load_json("candidate_data/selected_strictphaseantisymmetryscalarderivation_or_noknobyukawaexactness/strict_phase_antisymmetry_scalar_derivation.packet.json")
    replay = load_json("candidate_data/selected_strictphaseantisymmetryscalarderivation_or_noknobyukawaexactness/strict_scalar_yukawa_replay.packet.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_MagProfileSourceScalar_or_OfficialFullProfileWorkspace_v1.md").read_text(encoding="utf-8")

    status = "MTT_SELECTED_MAGPROFILESOURCESCALAR_OR_OFFICIALFULLPROFILEWORKSPACE_BUILT_PHASE_SOURCE_PROMOTED_MAGNITUDE_REPLAY_LOCKED"
    next_artifact = "MTT_Selected_MagProfileValueFunctional_or_OfficialFullProfileWorkspace_v1"

    require(candidate["status"] == status, "candidate status changed")
    require(cert["status"] == status, "certificate status changed")
    require(candidate["closure_claimed"] is False, "candidate overclaims full closure")
    require(cert["closure_claimed"] is False, "certificate overclaims full closure")
    require(candidate["theorem"]["proved"] is True, "promotion theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")
    require(candidate["target_fitting_used"] is False, "candidate target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "candidate observed selector used")
    require(cert["target_fitting_used"] is False, "certificate target fitting used")
    require(cert["observed_data_used_as_selector"] is False, "certificate observed selector used")

    require(old_gate["M_magprofile_promotion_gate_closed"] is True, "old M_magprofile gate not closed")
    require(old_gate["phase_split_scalar_source_selected"] is False, "old gate no longer records stale open clause")
    require(strict_phase["strict_phase_antisymmetry_scalar_source_theorem_proved"] is True, "strict phase theorem not proved")
    require(strict_phase["accepted_strict_phase_antisymmetry_scalar_source_rows"] == 1, "strict phase source row count changed")
    require(strict_phase["fitted_phase_split_retired_as_source_input"] is True, "fitted split not retired")
    require(strict_phase["accepted_exact_yukawa_magnitude_rows"] == 0, "strict phase overaccepts exact magnitude rows")
    require(finite_replay["accepted_finite_replay_yukawa_magnitude_rows"] == 9, "finite replay magnitude rows not locked")
    require(finite_replay["finite_replay_yukawa_exactness_closed"] is True, "finite replay Yukawa not closed")
    require(abs(finite_replay["actual_max_log_residual"] - 8.715792346058762e-14) < 1.0e-24, "finite replay residual changed")

    promo = candidate["promotion_result"]
    require(promo["previous_gate_closed"] is True, "previous gate not imported")
    require(promo["stale_clause_superseded"] is True, "stale clause not superseded")
    require(promo["strict_phase_antisymmetry_scalar_source_theorem_proved"] is True, "promotion lost strict theorem")
    require(promo["accepted_strict_phase_antisymmetry_scalar_source_rows"] == 1, "promotion source row count changed")
    require(promo["fitted_phase_split_retired_as_source_input"] is True, "promotion did not retire fit")
    require(promo["q64_sbeta_scalar_uses_only_selected_inputs"] is True, "promotion lost selected-input guard")
    require(promo["delta_c2_formula"] == "-((q64+1)/q64) * s_beta", "delta formula changed")
    require(abs(promo["delta_c2_value"] - (-0.005014489499673223)) < 1.0e-18, "delta value changed")
    require(abs(promo["residual_operator_coefficient"] - (-4.402222824618228e-08)) < 1.0e-20, "coefficient changed")
    require(promo["target_fitting_used"] is False, "promotion target fitting used")
    require(promo["observed_yukawa_values_used_to_select_scalar"] is False, "promotion observed selector used")

    require(derivation["all_derivation_clauses_closed"] is True, "derivation clauses not closed")
    require(derivation["source_status"]["strict_phase_antisymmetry_scalar_source_theorem_proved"] is True, "derivation source theorem false")
    require(derivation["source_status"]["free_scalar_parameter_introduced"] is False, "free scalar introduced")
    require(derivation["source_status"]["observed_yukawa_values_used_to_select_scalar"] is False, "observed values selected scalar")

    value_status = candidate["value_payload_status_after_promotion"]
    require(value_status["replay_profile_scalar_label_count_available"] == 10, "profile label count changed")
    require(value_status["accepted_internal_source_scalar_rows"] == 1, "internal source scalar count changed")
    require(value_status["accepted_finite_replay_yukawa_magnitude_rows"] == 9, "finite replay Yukawa magnitude rows not retained")
    require(value_status["finite_replay_yukawa_exactness_closed"] is True, "finite replay Yukawa closure lost")
    require(value_status["accepted_analytic_zero_yukawa_rows"] == 0, "analytic zero rows overaccepted")
    require(value_status["global_true_SM_no_knob_closure"] is False, "global no-knob overclosed")
    require(value_status["accepted_internal_M_magprofile_value_rows"] == 0, "M_magprofile value rows overaccepted")
    require(value_status["accepted_true_equivalence_precision_rows"] == 0, "true-equivalence rows overaccepted")
    require(value_status["M_magprofile_final_source_functional_closed"] is False, "M_magprofile final source overclosed")

    residual = candidate["residual_exactness_status"]
    require(residual["strict_phase_scalar_only_replay_executed"] is True, "strict scalar replay not executed")
    require(residual["strict_phase_scalar_only_residual_is_not_current_blocker"] is True, "phase-only residual reopened")
    require(residual["finite_tail_rows_have_already_closed_finite_replay_yukawa"] is True, "finite tail closure not imported")
    require(residual["family_shape_Q"] == [-2.0, 3.0, -1.0], "family shape changed")
    require(residual["sector_operator_vector"] == [27.0, 6.0, 26.0], "operator vector changed")
    require(abs(residual["remaining_max_abs_log_residual"] - 7.959463247076742e-09) < 1.0e-20, "residual changed")
    require(residual["ultratight_error_certificate_accepted"] is True, "bounded certificate lost")
    require(abs(residual["finite_replay_yukawa_actual_max_log_residual"] - 8.715792346058762e-14) < 1.0e-24, "finite replay residual changed")
    require(residual["finite_replay_yukawa_exactness_closed"] is True, "finite replay not closed")
    require(residual["analytic_zero_residual_closed"] is False, "analytic zero overclosed")
    require(replay["exact_zero_residual"] is False, "replay overclosed exactness")

    decision = candidate["decision"]
    require(decision["MagProfileSourceScalar_promotion_closed"] is True, "promotion decision not closed")
    require(decision["old_phase_split_unselected_blocker_retired"] is True, "old blocker not retired")
    require(decision["finite_replay_yukawa_magnitude_closure_locked"] is True, "finite replay magnitude closure reopened")
    require(decision["M_magprofile_value_functional_closed"] is False, "M_magprofile value functional overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(decision["full_no_knob_closed"] is False, "full no-knob overclosed")
    require(decision["next_required_artifact"] == next_artifact, "next artifact changed")
    require(cert["next_required_artifact"] == next_artifact, "certificate next artifact changed")

    for key in [
        "replay_magnitudes_promoted_to_no_knob_source_rows",
        "target_fitted_residual_scalar_promoted",
        "bounded_error_promoted_to_exact_equality",
        "common_scale_profile_values_used_as_selector",
        "official_likelihood_workspace_imported",
    ]:
        require(candidate["guards"][key] is False, f"candidate guard overclosed: {key}")
        require(cert[key] is False, f"certificate guard overclosed: {key}")

    for phrase in [
        "one internal source scalar row is promoted",
        "finite-replay Yukawa",
        "8.715792346058762e-14",
        "7.959463247076742e-09",
        next_artifact,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "old_phase_split_unselected_blocker_retired": True,
                "accepted_strict_phase_antisymmetry_scalar_source_rows": 1,
                "accepted_finite_replay_yukawa_magnitude_rows": 9,
                "finite_replay_yukawa_exactness_closed": True,
                "remaining_max_abs_log_residual": residual["remaining_max_abs_log_residual"],
                "next_required_artifact": next_artifact,
            },
            indent=2,
        )
    )
    print("selected MagProfile source scalar / official full-profile workspace audit passed")


if __name__ == "__main__":
    main()
