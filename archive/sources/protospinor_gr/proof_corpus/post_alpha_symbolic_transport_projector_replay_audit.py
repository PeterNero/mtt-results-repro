from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_symbolic_transport_projector_replay_certificate.json"
STATUS = "POST_ALPHA_SYMBOLIC_TRANSPORT_PROJECTOR_REPLAY_CLOSED_DOTD_OPEN"
NEXT = "Selected_U1Y_RouteC_dotD_alpha1_TransportDerivative_and_Driver_v1"
SECTORS = ["Q", "u", "d", "L", "e", "N", "H"]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim full closure")
    require(cert["symbolic_transport_projector_replay_accepted"] is True, "symbolic replay should be accepted")
    require(cert["projector_riesz_green_replay_closed"] is True, "stationary replay should close")
    require(cert["selected_rho_s_validator_ready"] is True, "rho_s should be validator-ready")
    require(cert["transport_closed_raw_finite_basis"] is False, "raw finite basis must not be claimed transport-closed")
    require(cert["selected_dotD_source_verified"] is False, "dotD should remain open")
    require(cert["alpha1_driver_verified"] is False, "alpha1 driver should remain open")
    require(all(cert["checks"].values()), "all certificate checks should pass")

    require(packet["theorem"]["proved"] is True, "theorem should be proved")
    require(packet["theorem"]["closure_claimed"] is False, "packet should not claim closure")
    require(packet["status"] == STATUS, "status mismatch")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")

    replay = packet["symbolic_replay_values"]
    acceptance = replay["symbolic_acceptance"]
    result = replay["validator_result"]
    require(replay["status"] == "PROJECTOR_RIESZ_GREEN_REPLAY_CLOSED_DOTD_OPEN", "replay status mismatch")
    require(acceptance["validator_extension"] == "exact_symbolic_transport_conjugation", "wrong validator extension")
    require(acceptance["accepts_function_space_conjugation"] is True, "functional conjugation should be accepted")
    require(acceptance["requires_unitary_or_orthogonal_transport"] is True, "unitary transport should be required")
    require(acceptance["raw_direct_truncated_relative_residual"] > 0.01, "raw aliasing residual should remain nonzero")
    require(acceptance["rejects_raw_finite_aliasing_as_failure"] is True, "raw aliasing should be bypassed by theorem, not denied")
    require(acceptance["gauge_frame_residual_l2"] < acceptance["gauge_frame_residual_tolerance"], "gauge frame replay should pass")
    require(all(acceptance["requires_functional_identities"].values()), "functional identities should be required")
    require(result["all_sector_projector_riesz_green_replays_pass"] is True, "all sector replay should pass")
    require(result["selected_dotD_source_verified"] is False, "dotD result should be open")

    require(sorted(replay["sector_replay_slots"]) == sorted(SECTORS), "wrong sectors")
    for sector, slot in replay["sector_replay_slots"].items():
        require(slot["finite_raw_truncation_replay_used"] is False, f"{sector} should not use raw truncation replay")
        require(slot["selected_projector_source_verified"] is True, f"{sector} projector source should be verified")
        require(slot["selected_green_operator_valid"] is True, f"{sector} Green operator should be valid")
        require(slot["selected_riesz_projector_valid"] is True, f"{sector} Riesz projector should be valid")
        require(slot["validator_ready_rho_s"] is True, f"{sector} rho_s should be ready")

    boundary = replay["dotd_boundary"]
    require(boundary["selected_dotD_source_verified"] is False, "boundary dotD should be open")
    require(boundary["alpha1_driver_verified"] is False, "boundary driver should be open")
    require("dU/dalpha" in boundary["next_required_terms"][0], "boundary should name dU/dalpha")

    require(all(packet["what_closes_now"].values()), "closure flags should pass")
    require(all(packet["what_remains_open"].values()), "open flags should remain")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "raw finite 27-mode" in note, "note missing essentials")

    print("AUDIT_PASS: symbolic transport projector/Riesz/Green replay closed; dotD and alpha1 driver remain open")


if __name__ == "__main__":
    main()
