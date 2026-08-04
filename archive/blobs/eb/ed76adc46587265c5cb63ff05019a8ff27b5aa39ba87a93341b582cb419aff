from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

STATUS = (
    "MTT_SELECTED_PRECISIONTRANSPORTVALUEOBJECT_OR_FINALTRUESMEQUIVALENCE_"
    "PRODUCT_CROSS_BLOCK_CLOSED_STRICT_PRECISION_OPEN"
)
NEXT = "MTT_Selected_ProductPrecisionWorkspaceAcceptance_or_InternalTransportPromotion_v1"


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def cholesky_positive_definite(matrix: list[list[float]], tol: float = 0.0) -> bool:
    n = len(matrix)
    lower = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            value = matrix[i][j] - sum(lower[i][k] * lower[j][k] for k in range(j))
            if i == j:
                if value <= tol:
                    return False
                lower[i][j] = value**0.5
            else:
                lower[i][j] = value / lower[j][j]
    return True


def main() -> None:
    candidate = load("candidate_data/selected_precisiontransportvalueobject_or_finaltruesmequivalence.candidate.json")
    packet = load(
        "candidate_data/selected_precisiontransportvalueobject_or_finaltruesmequivalence/"
        "product_precision_transport_value_object.packet.json"
    )
    cert = load("certificates/selected_precisiontransportvalueobject_or_finaltruesmequivalence_certificate.json")
    bridge = load(
        "candidate_data/selected_externalprofiletofullcovariancebridge_or_selectedsourcerows/"
        "external_profile_full_covariance_bridge.packet.json"
    )
    target_lock = load(
        "candidate_data/selected_precisiontransportcovariancerows_or_finaltruesmaudit/"
        "full_covariance_target_lock.packet.json"
    )
    bct = load("candidate_data/selected_charmtablesubstitution_or_selectedrthetarowsdecision/bct_empirical_table_substituted_profile.packet.json")
    wzh = load("candidate_data/selected_correlatedthresholdprofilematrix_or_yukawahiggsprecisionpromotion/correlated_threshold_profile_matrix.packet.json")
    precision_split = load("certificates/selected_precisionlayerfullcovariance_or_internaltransport_certificate.json")
    note = (ROOT / "proof_corpus" / "MTT_Selected_PrecisionTransportValueObject_or_FinalTrueSMEquivalence_v1.md").read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status changed")
    require(cert["status"] == STATUS, "certificate status changed")
    require(candidate["closure_claimed"] is False, "candidate overclaims final closure")
    require(cert["closure_claimed"] is False, "certificate overclaims final closure")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem flag missing")
    require(candidate["target_fitting_used"] is False, "target fitting used")
    require(candidate["observed_data_used_as_selector"] is False, "observed selector used")

    require(bridge["full_covariance_target"]["hard_missing_entries_for_published_or_reconstructed_likelihood"] == 15, "bridge predecessor no longer records old gap")
    require(target_lock["BCT_WZH_cross_covariance_entries_missing"] == 15, "target lock predecessor no longer records old gap")
    require(bct["passes_95pct_profile_gate"] is True, "BCT profile gate not passed")
    require(wzh["accepted_as_surrogate_correlated_threshold_profile_matrix"] is True, "WZH surrogate matrix not accepted")
    require(wzh["accepted_as_published_or_reconstructed_profile_likelihood"] is False, "WZH unexpectedly promoted")
    require(precision_split["remaining_frontier_is_exactly_precision_transport_value_object"] is True, "precision split frontier changed")

    closed = candidate["closed_now"]
    require(closed["precision_transport_value_object_emitted_at_product_workspace_tier"] is True, "product object not emitted")
    require(closed["BCT_WZH_cross_covariance_entries_closed"] == 15, "cross entries not closed")
    require(closed["BCT_WZH_cross_covariance_entries_missing_after_successor"] == 0, "cross entries still missing")
    require(closed["cross_block_entry_value"] == 0.0, "cross value changed")
    require(closed["symmetric_unique_entries_present_in_product_workspace"] == 36, "unique entry count changed")
    require(closed["BCT_block_unique_entries"] == 6, "BCT unique count changed")
    require(closed["WZH_block_unique_entries"] == 15, "WZH unique count changed")
    require(closed["BCT_WZH_cross_block_unique_entries"] == 15, "cross unique count changed")

    rule = candidate["product_profile_rule"]
    require(rule["introduces_free_parameter"] is False, "product rule introduces parameter")
    require(rule["uses_observed_values_as_selector"] is False, "product rule uses observed selector")
    require(rule["cross_block_entries_are_placeholders"] is False, "cross zeros are placeholders")

    matrix = packet["covariance_matrix"]
    require(packet["basis_order"] == [
        "bottom_MSbar_native_scale_transport",
        "charm_MSbar_native_scale_transport",
        "tau_pole_rest_to_running_lepton",
        "lambda_Mt",
        "y_t_Mt",
        "g_2_Mt",
        "g_Y_Mt",
        "g_3_Mt",
    ], "basis order changed")
    require(len(matrix) == 8 and all(len(row) == 8 for row in matrix), "matrix shape")
    for i, row in enumerate(matrix):
        require(row[i] > 0.0, f"nonpositive diagonal {i}")
        for j, value in enumerate(row):
            require(abs(value - matrix[j][i]) <= 1e-20, "matrix not symmetric")
    for i in range(3):
        for j in range(3, 8):
            require(matrix[i][j] == 0.0 and matrix[j][i] == 0.0, "cross entry not zero")
    require(cholesky_positive_definite(matrix), "product matrix not positive definite")

    diagnostics = packet["diagnostics"]
    require(diagnostics["matrix_shape"] == [8, 8], "diagnostic shape")
    require(diagnostics["symmetric_unique_entries"] == 36, "diagnostic unique count")
    require(diagnostics["BCT_WZH_cross_covariance_entries_closed"] == 15, "diagnostic cross closed")
    require(diagnostics["BCT_WZH_cross_covariance_entries_missing"] == 0, "diagnostic cross missing")
    require(diagnostics["nonzero_BCT_WZH_cross_entries"] == 0, "diagnostic cross nonzero")
    require(diagnostics["positive_definite"] is True, "diagnostic positive definite")
    require(diagnostics["accepted_as_product_precision_transport_value_object"] is True, "diagnostic product object")
    require(diagnostics["accepted_as_published_or_reconstructed_joint_likelihood"] is False, "diagnostic likelihood overclaim")
    require(diagnostics["accepted_as_final_true_precision_equivalence"] is False, "diagnostic true precision overclaim")

    not_closed = candidate["not_closed"]
    for key in [
        "published_or_reconstructed_joint_BCT_WZH_likelihood_imported",
        "WZH_block_promoted_from_surrogate_to_published_likelihood",
        "BCT_empirical_replay_promoted_to_no_knob_source",
        "selected_internal_Rtheta_threshold_mass_derivation_closed",
        "selected_threshold_response_functional_value_instantiated",
        "true_precision_equivalence_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(not_closed[key] is False, f"overclosed {key}")
    require(not_closed["accepted_true_equivalence_precision_rows"] == 0, "true precision rows overclaimed")

    decision = candidate["decision"]
    require(decision["old_missing_15_cross_entries_retired"] is True, "old cross gap not retired")
    require(decision["cross_block_hard_block_solved"] is True, "cross block not solved")
    require(decision["product_workspace_is_final_published_likelihood"] is False, "product workspace overpromoted")
    require(decision["product_workspace_is_selected_precision_transport_value_object"] is True, "product object not selected")
    require(decision["strict_final_precision_layer_solved"] is False, "strict final precision overclosed")
    require(decision["accepted_true_equivalence_precision_rows"] == 0, "decision true rows overclaimed")
    require(decision["next_required_artifact"] == NEXT, "next artifact changed")
    require(cert["next_required_artifact"] == NEXT, "certificate next changed")

    for key in [
        "does_not_reopen_27_matrix",
        "does_not_reopen_yukawa_magnitudes",
        "does_not_reopen_M_magprofile_value_payload",
        "does_not_replace_published_likelihood_with_unlabelled_surrogate",
        "does_not_infer_nonzero_cross_correlation_without_joint_likelihood",
        "does_not_claim_true_precision_equivalence",
        "does_not_use_observed_values_as_selectors",
    ]:
        require(candidate["guards"][key] is True, f"guard failed {key}")

    for phrase in [
        "BCT-WZH cross entries closed                                   : 15/15",
        "BCT-WZH cross entries missing after successor                  : 0",
        "accepted true-equivalence precision rows                       : 0",
        "The active blocker is therefore no longer",
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(
        json.dumps(
            {
                "candidate": cert["candidate"],
                "status": cert["status"],
                "BCT_WZH_cross_covariance_entries_closed": 15,
                "BCT_WZH_cross_covariance_entries_missing_after_successor": 0,
                "product_precision_transport_value_object_emitted": True,
                "accepted_true_equivalence_precision_rows": 0,
                "next_required_artifact": NEXT,
            },
            indent=2,
        )
    )
    print("selected PrecisionTransportValueObject product cross-block audit passed")


if __name__ == "__main__":
    main()
