from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_independent_long_residual_weyl_polynomial_source_theorem_attempt_certificate.json"
STATUS = "POST_ALPHA_INDEPENDENT_LONG_RESIDUAL_WEYL_POLYNOMIAL_SOURCE_THEOREM_ATTEMPT_REANCHORED_PROJECTOR_SELECTION_OPEN"
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
    require(cert["theorem"]["proved"] is True, "long-chain Weyl attempt should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")
    previous = packet["fresh_previous_certificate"]
    require(previous["frontier_decision"]["next_required_artifact"].endswith("ValueFill_v1"), "previous frontier drift")
    weyl = packet["residual_weyl_polynomial_decomposition"]
    require(weyl["decompositions"]["R_X"]["coefficient_count"] == 3, "R_X coefficient count drift")
    require(weyl["decompositions"]["R_Z"]["coefficient_count"] == 6, "R_Z coefficient count drift")
    require(weyl["decompositions"]["R_X"]["norm_sq"] == 2.0, "R_X norm drift")
    require(weyl["decompositions"]["R_Z"]["norm_sq"] == 4.0, "R_Z norm drift")
    gate = packet["canonical_residual_projector_selection_gate"]
    require(gate["status"] == "CANONICAL_PROJECTOR_IDENTIFIED_SELECTION_THEOREM_OPEN", "projector gate drift")
    require(gate["if_projector_selection_theorem_is_supplied"]["SM_parity_dynamic_packet_closes"] is True, "SM implication missing")
    require(gate["if_projector_selection_theorem_is_supplied"]["no_knob_flavor_constants_derived"] is False, "no-knob overclaim")
    require(STATUS in note and NEXT in note, "note missing essentials")
    print("AUDIT_PASS: reanchored long-chain residual Weyl compression imported; projector selection remains open")


if __name__ == "__main__":
    main()
