from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "tt_gap_external_domain_vs_internal_aint_role_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(
        cert["status"] == "TT_NUMERIC_GAP_REFOCUSED_ON_INTERNAL_AINT_EXTERNAL_DOMAIN_REGULATOR",
        "unexpected status",
    )

    source = cert["source_tests"]
    decisions = cert["decisions"]
    roles = cert["role_separation"]
    closed = cert["closed_now"]
    guards = cert["guardrails"]

    require(source["qg_v4_external_internal_blocks_commute"] is True, "commuting blocks not sourced")
    require(source["qg_v4_positive_gap_above_coherent_zero_modes"] is True, "positive gap not sourced")
    require(source["qg_v4_defines_E_as_external_TT_lichnerowicz"] is True, "external E role not sourced")
    require(source["qg_v4_defines_lambda_as_internal_Aint_gap"] is True, "internal lambda role not sourced")
    require(source["qg_v4_pushforward_from_internal_projector_to_Y4"] is True, "P=I o Pi not sourced")
    require(source["qg_i_external_domain_is_bounded_chart"] is True, "external bounded chart not sourced")
    require(source["qg_ii_boundary_terms_are_well_posedness_constraint"] is True, "boundary role not sourced")

    require(roles["external_block_E"]["source_of_lambda_star"] is False, "external E must not source lambda")
    require(roles["internal_block_Aint"]["source_of_lambda_star"] is True, "Aint should source lambda")
    require(decisions["external_box_lowest_eigenvalue_is_selected_modal_gap"] is False, "box gap must not close")
    require(decisions["flat_T3_lambda_1_equals_1_closes_lambda_star"] is False, "T3 lambda=1 must not close")
    require(decisions["numeric_gap_refocused_on_selected_internal_Aint"] is True, "gap should refocus on Aint")
    require(all(closed.values()), "closed_now fields should be true")
    require(cert["next_gate"]["name"] == "Selected_Internal_Aint_Complement_Gap_Theorem", "wrong next gate")
    require("Selected_Internal_Aint_Complement_Gap_Theorem" in note, "note lost next gate")

    require(guards["claims_external_box_gap_is_lambda_star"] is False, "must not claim external gap")
    require(guards["claims_flat_T3_lambda_1_closes_gap"] is False, "must not claim T3 closes")
    require(guards["claims_domain_selection_irrelevant"] is False, "domain role must remain relevant")
    require(guards["claims_selected_internal_Aint_gap_computed"] is False, "must not claim Aint gap computed")
    require(guards["claims_full_GR_response_closed"] is False, "must not claim full GR response closed")

    print("AUDIT_PASS: TT numeric gap refocused on internal Aint; external domain kept as scaffold")


if __name__ == "__main__":
    main()
