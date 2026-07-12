"""Audit the H radial/phase/trace source or finite-H action emission packet."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hradialphasetracesource_or_finitehactionemission"


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    candidate = read_json(f"candidate_data/{SLUG}.candidate.json")
    inventory = read_json(f"candidate_data/{SLUG}/radial_phase_trace_source_inventory.packet.json")
    polar = read_json(f"candidate_data/{SLUG}/polar_row_family_after_inventory.packet.json")
    action = read_json(f"candidate_data/{SLUG}/finite_h_action_emission_attempt.packet.json")
    cutset = read_json(f"candidate_data/{SLUG}/next_cutset_after_radial_phase_trace_attempt.packet.json")
    cert = read_json(f"certificates/{SLUG}_certificate.json")

    require(candidate["theorem"]["proved"] is True, "theorem must be marked proved")
    require(candidate["decision"]["selected_s_beta_polar_angle_closed"] is True, "selected s_beta must remain closed")
    require(candidate["decision"]["controlled_radial_support_available"] is True, "controlled radial support must be retained")
    require(
        candidate["decision"]["controlled_radial_support_accepted_as_strict_source"] is False,
        "controlled radial support must not be counted as strict no-knob source",
    )
    require(candidate["key_numbers"]["accepted_strict_polar_field_count"] == 0, "strict polar fields must remain zero")
    require(candidate["key_numbers"]["accepted_value_row_count"] == 0, "accepted value rows must remain zero")
    require(candidate["key_numbers"]["accepted_row_certificate_count"] == 0, "accepted row certificates must remain zero")

    require(
        inventory["status"] == "RADIAL_PHASE_TRACE_SOURCE_INVENTORY_EXECUTED_ZERO_STRICT_POLAR_FIELDS",
        "inventory status mismatch",
    )
    require(inventory["accepted_strict_field_count"] == 0, "inventory must accept zero strict fields")
    require(
        inventory["controlled_radial_support"]["accepted_as_strict_no_knob_source"] is False,
        "controlled radial lane must stay outside strict source count",
    )
    require(
        set(inventory["strict_field_emissions"].values()) == {False},
        "all strict field emissions must be false at this frontier",
    )

    require(polar["strict_execution"]["tracefree_threshold_block_executable"] is False, "tracefree block must not execute")
    require(polar["strict_execution"]["full_H_response_rows_executable"] is False, "full rows must not execute")
    require(len(polar["strict_execution"]["missing_fields"]) == 4, "four polar fields must remain missing")
    require(
        polar["controlled_execution"]["full_controlled_rows_executable"] is False,
        "controlled radial support alone must not execute full rows",
    )

    require(action["emission_result"]["selected_finite_H_action_emitted"] is False, "finite H action must not be emitted")
    require(action["emission_result"]["selected_second_variation_rows_emitted"] is False, "second variation rows must not emit")
    require(action["emission_result"]["accepted_value_row_count"] == 0, "action attempt must accept zero rows")

    require(
        cutset["next_frontier"] == "MTT_Selected_HPolarFieldsSource_or_DirectFiniteHActionRows_v1",
        "next frontier mismatch",
    )
    require(
        cert["status"]
        == "MTT_SELECTED_HRADIALPHASETRACESOURCE_OR_FINITEHACTIONEMISSION_EXECUTED_ZERO_STRICT_FIELDS_ACTION_OPEN",
        "certificate status mismatch",
    )
    require(cert["checks"]["strict_polar_fields_accepted_zero"] is True, "certificate strict-field check failed")

    print("selected_hradialphasetracesource_or_finitehactionemission audit: PASS")


if __name__ == "__main__":
    main()
