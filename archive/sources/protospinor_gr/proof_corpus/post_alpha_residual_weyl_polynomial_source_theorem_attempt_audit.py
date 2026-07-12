from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_residual_weyl_polynomial_source_theorem_attempt_certificate.json"
STATUS = "POST_ALPHA_RESIDUAL_WEYL_POLYNOMIAL_SOURCE_THEOREM_ATTEMPT_IMPORTED_PROJECTOR_SELECTION_OPEN"
NEXT = "MTT_Selected_CanonicalResidualProjector_or_HonestGalerkinC1_ValueFill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "closure overclaimed")
    require(cert["theorem"]["proved"] is True, "Weyl-polynomial theorem should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")

    decision = packet["source_candidate_summary"]["promotion_decision"]
    for key in [
        "Lane_A_promoted",
        "canonical_residual_projector_promoted",
        "residual_weyl_polynomial_selected_as_dynamic_response",
        "SM_parity_dynamic_packet_closed",
        "no_knob_flavor_constants_closed",
    ]:
        require(decision[key] is False, f"promotion overclaimed: {key}")

    weyl = packet["residual_weyl_polynomial_decomposition"]
    require(weyl["status"] == "EXACT_LOW_DEGREE_WEYL_POLYNOMIAL_DECOMPOSITION_COMPUTED", "Weyl status drift")
    require(weyl["decompositions"]["R_X"]["coefficient_count"] == 3, "R_X coefficient count drift")
    require(weyl["decompositions"]["R_Z"]["coefficient_count"] == 6, "R_Z coefficient count drift")
    require(weyl["decompositions"]["R_X"]["norm_sq"] == 2.0, "R_X norm drift")
    require(weyl["decompositions"]["R_Z"]["norm_sq"] == 4.0, "R_Z norm drift")
    require(weyl["decompositions"]["R_X"]["reconstruction_error_norm_sq"] < 1e-24, "R_X reconstruction drift")
    require(weyl["decompositions"]["R_Z"]["reconstruction_error_norm_sq"] < 1e-24, "R_Z reconstruction drift")

    gate = packet["canonical_residual_projector_selection_gate"]
    require(gate["status"] == "CANONICAL_PROJECTOR_IDENTIFIED_SELECTION_THEOREM_OPEN", "projector gate drift")
    require(gate["if_projector_selection_theorem_is_supplied"]["SM_parity_dynamic_packet_closes"] is True, "parity implication missing")
    require(gate["if_projector_selection_theorem_is_supplied"]["no_knob_flavor_constants_derived"] is False, "no-knob overclaim")
    require(STATUS in note and NEXT in note and "exact qutrit Weyl polynomials" in note, "note missing essentials")
    print("AUDIT_PASS: residual Weyl-polynomial source theorem attempt imported; projector selection remains open")


if __name__ == "__main__":
    main()
