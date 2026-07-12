"""Audit the H radial action-norm value / H-lambda threshold-row cutset."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hradialactionnormvalue_or_hlambdathresholdrow"


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    candidate = read_json(f"candidate_data/{SLUG}.candidate.json")
    action = read_json(f"candidate_data/{SLUG}/h_radial_action_norm_value_contract.packet.json")
    bridge = read_json(f"candidate_data/{SLUG}/h_lambda_threshold_row_bridge_contract.packet.json")
    execution = read_json(f"candidate_data/{SLUG}/current_h_radial_value_payload_execution.packet.json")
    missing = read_json(f"candidate_data/{SLUG}/required_missing_object.packet.json")
    cert = read_json(f"certificates/{SLUG}_certificate.json")

    require(candidate["theorem"]["proved"] is True, "theorem must be proved")
    require(candidate["decision"]["radial_action_norm_value_contract_closed"] is True, "radial contract")
    require(candidate["decision"]["H_lambda_threshold_bridge_contract_closed"] is True, "H lambda bridge")
    require(candidate["decision"]["current_payload_execution_completed"] is True, "payload execution")
    require(candidate["decision"]["numeric_value_emitted"] is False, "numeric value overpromoted")
    require(candidate["decision"]["accepted_value_rows"] == 0, "accepted value rows must be zero")
    require(candidate["decision"]["controlled_one_parameter_tier_available"] is True, "controlled tier missing")
    require(
        candidate["decision"]["controlled_one_parameter_tier_promoted_to_strict"] is False,
        "controlled tier promoted to strict",
    )
    require(
        candidate["decision"]["frontier_reduced_to_two_split_slots_or_one_direct_scalar"] is True,
        "frontier reduction mismatch",
    )
    require(
        candidate["next_target"] == "MTT_Selected_HLambdaRowLocalOverlapAndScheme_or_DirectRadialHessianValue_v1",
        "next target mismatch",
    )

    require(action["decision"]["contract_closed"] is True, "action contract not closed")
    require(action["decision"]["numeric_radial_action_norm_value_emitted"] is False, "action value emitted")
    require(action["decision"]["accepted_radial_action_norm_value_rows"] == 0, "action rows accepted")
    require(action["selected_unit_ray"]["closed"] is True, "selected unit ray not closed")
    require("sqrt(Tr(H_tf^2)/2)" in action["selected_unit_ray"]["normalization_identity"], "norm identity missing")
    require("observed lambda_H replay" in action["required_value_payload"]["forbidden_sources"], "forbidden replay missing")
    require(action["currently_available"]["controlled_replay_counts_as_strict_source"] is False, "controlled replay strict")
    require(
        math.isclose(
            action["currently_available"]["controlled_replay_r_H_squared"],
            action["currently_available"]["controlled_replay_r_H_available"] ** 2,
            rel_tol=0,
            abs_tol=1e-9,
        ),
        "controlled r_H square mismatch",
    )

    require(bridge["decision"]["bridge_contract_closed"] is True, "bridge not closed")
    require(bridge["decision"]["selected_L_rowlocal_Omega_H_lambda"] is False, "L rowlocal emitted")
    require(bridge["decision"]["selected_T_scheme_Omega_H_lambda"] is False, "T scheme emitted")
    require(bridge["decision"]["selected_K_threshold_Omega_H_lambda_emitted"] is False, "K row emitted")
    require(bridge["decision"]["accepted_bridge_value_rows"] == 0, "bridge rows accepted")
    require(
        bridge["strict_H_row_postcheck_target"]["accepted_as_source_row"] is False,
        "Step72 target promoted as source",
    )
    require(
        bridge["strict_H_row_postcheck_target"]["source_value_tier"] == "admitted_replay_postcheck_only",
        "Step72 H target tier changed",
    )
    require(
        bridge["already_closed_subfields"]["D_fin_H_closed"] is True
        and bridge["already_closed_subfields"]["theta_exponent_1_over_3_closed"] is True,
        "closed H support subfields missing",
    )

    require(execution["decision"]["current_payload_execution_completed"] is True, "execution incomplete")
    require(execution["decision"]["accepted_value_rows"] == 0, "execution accepted rows")
    require(execution["decision"]["controlled_parameter_tier_kept_separate"] is True, "tier not separate")
    require(execution["not_closed"]["L_rowlocal_Omega_H_lambda"] is True, "L rowlocal should be open")
    require(execution["not_closed"]["T_scheme_Omega_H_lambda"] is True, "T scheme should be open")
    require(execution["not_closed"]["K_threshold_Omega_H_lambda"] is True, "K row should be open")
    require(execution["not_closed"]["A_H_radial_norm_value"] is True, "radial norm value should be open")
    require(execution["current_counts"]["strict_selected_K_source_row_count"] == 9, "strict K count")
    require(execution["current_counts"]["strict_selected_K_source_row_count_required"] == 10, "strict K required")
    require(execution["current_counts"]["accepted_numeric_radial_value_sources"] == 0, "numeric radial sources")

    require(
        missing["decision"]["frontier_reduced_to_two_split_slots_or_one_direct_scalar"] is True,
        "missing object frontier mismatch",
    )
    require(missing["decision"]["do_not_repeat_status_only_packets"] is True, "loop guard missing")
    require(
        missing["decision"]["next_packet_must_emit_numeric_source_or_formal_source_operator"] is True,
        "next packet requirement missing",
    )
    require(
        missing["minimal_legal_exits"]["split_H_lambda_exit"]["rows_needed"] == 2,
        "split exit row count",
    )
    require(
        missing["minimal_legal_exits"]["direct_H_lambda_exit"]["rows_needed"] == 1,
        "direct K exit row count",
    )
    require(
        missing["minimal_legal_exits"]["direct_radial_hessian_exit"]["rows_needed"] == 1,
        "direct radial exit row count",
    )

    require(cert["proved"] is True, "certificate proved")
    require(cert["checks"]["radial_action_norm_value_contract_closed"] is True, "cert action")
    require(cert["checks"]["H_lambda_threshold_bridge_contract_closed"] is True, "cert bridge")
    require(cert["checks"]["numeric_value_emitted"] is False, "cert numeric")
    require(cert["checks"]["accepted_value_rows"] == 0, "cert rows")
    require(cert["checks"]["controlled_tier_promoted_to_strict"] is False, "cert tier")

    print("selected_hradialactionnormvalue_or_hlambdathresholdrow audit: PASS")


if __name__ == "__main__":
    main()
