from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_independent_canonical_residual_projector_or_honest_galerkin_c1_valuefill_certificate.json"
STATUS = "POST_ALPHA_INDEPENDENT_CANONICAL_RESIDUAL_PROJECTOR_OR_HONEST_GALERKIN_C1_VALUEFILL_IMPORTED_APPLICATION_OPEN"
NEXT = "MTT_Selected_PhiFinC1ResidualProjectorApplication_or_HonestGalerkinExecution_ValueFill_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "closure overclaimed")
    require(cert["theorem"]["proved"] is True, "long-chain canonical projector import should be proved")
    require(all(cert["what_closes_now"].values()), "closed checks should pass")
    require(all(cert["what_remains_open"].values()), "open gates should remain open")
    require(all(cert["guardrails"].values()), "guardrails should hold")
    require(cert["frontier_decision"]["next_required_artifact"] == NEXT, "wrong next artifact")

    projector = packet["canonical_fixedfiber_residual_projector"]
    require(projector["selected_as_canonical_mathematical_projector"] is True, "canonical projector not selected")
    require(projector["selected_as_physical_C1_transfer_application"] is False, "physical application overclaimed")
    require(projector["operator_checks"]["fixed_projector_rank"] == 3, "fixed rank drift")
    require(projector["operator_checks"]["residual_projector_rank"] == 6, "residual rank drift")
    require(projector["operator_checks"]["residual_projector_idempotence_norm_sq"] < 1e-24, "residual idempotence drift")
    require(projector["operator_checks"]["orthogonal_complement_product_norm_sq"] < 1e-24, "orthogonal complement drift")

    replay = packet["projector_application_value_replay"]
    require(replay["physical_application_claimed"] is False, "replay overclaimed as physical")
    require(replay["matches_stored_residual_packet"] is True, "stored residual replay mismatch")
    require(replay["phase_replay"]["residual_norm_sq"] == 4.0, "phase residual norm drift")
    require(abs(replay["shift_replay"]["residual_norm_sq"] - 2.0) < 1e-12, "shift residual norm drift")

    cutset = packet["projector_or_galerkin_cutset_decision"]
    require(cutset["SM_parity_dynamic_packet_closed"] is False, "SM parity overclaimed")
    require(cutset["no_knob_flavor_constants_closed"] is False, "no-knob overclaimed")
    lane_a = cutset["if_lane_A_application_theorem_is_supplied"]
    require(lane_a["A_transpose_A"] == [[12.0, 0.0], [0.0, 12.0]], "A^T A drift")
    require(lane_a["A_transpose_b"] == [12.0, 12.0], "A^T b drift")
    require(lane_a["deltaTheta_C1"] == [1.0, 1.0], "deltaTheta drift")
    require(lane_a["SM_parity_dynamic_packet_would_close"] is True, "Lane A implication missing")
    require(lane_a["no_knob_flavor_constants_would_close"] is False, "Lane A no-knob overclaim")

    require(STATUS in note and NEXT in note and "canonical mathematical residual projector" in note, "note missing essentials")
    print("AUDIT_PASS: long-chain canonical residual projector imported; physical C1 application remains open")


if __name__ == "__main__":
    main()
