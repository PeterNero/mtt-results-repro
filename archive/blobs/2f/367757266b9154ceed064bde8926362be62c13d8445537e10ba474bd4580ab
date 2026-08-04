from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_dotd_alpha1_driver_bridge_certificate.json"
STATUS = "POST_ALPHA_DOTD_ALPHA1_DRIVER_REPLAY_CLOSED_PRIMITIVE_C1_LAMBDA_OPEN"
NEXT = "Selected_U1Y_RouteC_Primitive_C1_Contractions_or_Lambda12_Gate_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim full closure")
    require(cert["selected_dotD_source_verified"] is True, "dotD source should close")
    require(cert["alpha1_driver_verified"] is True, "alpha1 driver should close")
    require(cert["honest_dotD_alpha1_replay"] is True, "honest dotD replay should close")
    require(cert["primitive_C1_contractions_closed"] is False, "primitive C1 should remain open")
    require(cert["lambda12_computable"] is False, "lambda12 should remain open")
    require(all(cert["checks"].values()), "all certificate checks should pass")

    require(packet["theorem"]["proved"] is True, "theorem should be proved")
    require(packet["theorem"]["closure_claimed"] is False, "packet should not claim closure")
    require(packet["status"] == STATUS, "packet status mismatch")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(packet["dotd_transport_derivative"]["dU_dalpha"] == "-(du/dalpha) ad(T3) U", "wrong derivative")
    require(packet["dotd_transport_derivative"]["identity"] == "D_sel(delta psi)+dotD_h psi_sel=0", "wrong dotD identity")

    promoted = packet["promoted_alpha1_value"]
    replay = packet["honest_dotd_replay"]
    require(promoted["N_alpha1_h_ext"] == 1.0, "wrong N_alpha1 value")
    require(promoted["lambda_alpha1"] == 1.0, "wrong lambda_alpha1 support value")
    require(promoted["du_dalpha1"] == "h_ext", "wrong alpha1 derivative")
    require(promoted["selected_value_emitted_by_this_theorem"] is True, "selected alpha1 value missing")
    require(promoted["tangent_residual_l2"] == 0.0, "tangent residual should vanish")
    require(replay["selected_dotD_source_verified"] is True, "replay dotD source missing")
    require(replay["alpha1_driver_verified"] is True, "replay alpha1 driver missing")
    require(replay["honest_dotD_validator_closed"] is True, "honest replay missing")
    require("not diagnostic flags" in replay["why_not_lifted_flags"], "lifted-flag guard missing")

    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "not a primitive-C1 or Yukawa closure" in note, "note missing essentials")

    print("AUDIT_PASS: post-alpha dotD_alpha1 driver bridge closed; primitive C1/lambda remain open")


if __name__ == "__main__":
    main()
