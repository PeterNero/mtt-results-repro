from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_residual_projector_source_rule_contract_certificate.json"
STATUS = "POST_ALPHA_RESIDUAL_PROJECTOR_SOURCE_RULE_CONTRACT_IMPORTED_VALUES_OPEN"
NEXT = "MTT_Selected_WeylPairSourceEmission_or_HonestGalerkinC1Execution_ValueRun_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["theorem"]["proved"] is True, "source-rule contract theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed import checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")

    decision = cert["frontier_decision"]
    require(decision["frontier_is_three_route_value_emission_contract"] is True, "wrong frontier")
    require(decision["recommended_primary_route"] == "B_enriched_weylpair_basis_transport_or_vertex_source", "wrong primary route")
    require(decision["conditional_values_promoted"] is False, "conditional values promoted")
    require(decision["next_required_artifact"] == NEXT, "wrong next artifact")

    routes = cert["legal_routes"]
    require(set(routes) == {
        "A_differentiated_residual_projector_rule",
        "B_enriched_weylpair_basis_transport_or_vertex_source",
        "C_honest_selected_Galerkin_C1_execution",
    }, "route set drift")
    require(routes["B_enriched_weylpair_basis_transport_or_vertex_source"]["recommended_primary"] is True, "route B should be primary")
    require(routes["B_enriched_weylpair_basis_transport_or_vertex_source"]["algebraically_sufficient"] is True, "route B sufficiency lost")
    require(routes["C_honest_selected_Galerkin_C1_execution"]["selected_source_verified"] is False, "honest Galerkin promoted")

    support = packet["already_selected_support"]
    require(support["canonical_Q_residual_available"] is True, "Q_residual support lost")
    require(support["Q_residual_rank"] == 6, "Q_residual rank drift")
    require(support["alpha1_dotD_driver_verified"] is True, "alpha1/dotD support lost")

    conditional = packet["conditional_values_if_rule_or_execution_closes"]
    require(conditional["selected_now"] is False, "conditional values selected")
    require(conditional["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "wrong A^T A")
    require(conditional["A_transpose_b"] == [12.0, 12.0], "wrong A^T b")
    require(conditional["deltaTheta_C1"] == [1.0, 1.0], "wrong DeltaTheta")
    require(conditional["rank"] == 2, "rank drift")

    require(packet["recommended_next_route"] == "B_enriched_weylpair_basis_transport_or_vertex_source", "recommended route drift")
    require("zero_mode_bases" in packet["honest_galerkin_required_outputs"], "honest execution outputs lost")
    require("using observed SM flavor data or benchmark matrices as selectors" in packet["ruled_out_paths"], "observed selector ban lost")
    require(STATUS in note and NEXT in note and "Route B is ranked primary" in note, "note missing essentials")
    print("AUDIT_PASS: residual projector source-rule contract imported; route B is primary but unpromoted")


if __name__ == "__main__":
    main()
