from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "post_alpha_hym_projector_source_payload_fill_certificate.json"
STATUS = "POST_ALPHA_HYM_PROJECTOR_SOURCE_PAYLOAD_FUNCTIONAL_FILLED_FINITE_REPLAY_OPEN"
NEXT = "Selected_U1Y_RouteC_TransportClosed_BN_Basis_or_SymbolicProjectorReplay_v1"
SECTORS = ["Q", "u", "d", "L", "e", "N", "H"]
MATTER = ["Q", "u", "d", "L", "e", "N"]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def shape(matrix: list[list[int]], dim: int) -> bool:
    return len(matrix) == dim and all(len(row) == dim for row in matrix)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(cert["functional_selected_projectors"] is True, "functional projectors should be filled")
    require(cert["functional_selected_zero_mode_bases"] is True, "functional K_s should be filled")
    require(cert["functional_selected_rho_s"] is True, "functional rho_s should be filled")
    require(cert["finite_27mode_validator_replay_closed"] is False, "finite replay must remain open")
    require(cert["physical_dotD_alpha1_payload_extracted"] is False, "physical dotD must remain open")
    require(all(cert["checks"].values()), "all certificate checks should pass")

    require(packet["theorem"]["proved"] is True, "theorem should be proved")
    require(packet["theorem"]["closure_claimed"] is False, "packet should not claim closure")
    require(packet["status"] == STATUS, "packet status mismatch")
    require(packet["next_required_artifact"] == NEXT, "wrong next artifact")
    require(packet["same_source_id"].startswith("SM:selected_diagonal_End0_HYM_lane"), "wrong same-source id")
    require(packet["transport_operator"]["symbol"] == "U", "wrong transport symbol")
    require(packet["transport_operator"]["unitary_or_orthogonal"] is True, "transport should be unitary/orthogonal")

    payload = packet["functional_payload"]
    require(payload["status"] == "FUNCTIONAL_TRACE_PAYLOAD_FILLED_FINITE_VALIDATOR_REPLAY_OPEN", "payload status mismatch")
    require(payload["coherence_checks"]["no_observed_or_benchmark_inputs"] is True, "target data should be absent")
    require(payload["coherence_checks"]["no_lifted_selected_flags"] is True, "selected flags should not be lifted")

    for sector in SECTORS:
        dim = 1 if sector == "H" else 3
        projector = payload["sector_projectors"][sector]
        basis = payload["ordered_zero_mode_bases_K_s"][sector]
        action = payload["End0_action_on_zero_modes"][sector]
        require(projector["idempotent"] is True, f"{sector} projector should be idempotent")
        require(projector["selected_by_same_source"] is True, f"{sector} projector should be same-source selected")
        require(projector["finite_27_mode_replay_closed"] is False, f"{sector} finite replay should be open")
        require(basis["dimension_emitted"] == dim, f"{sector} emitted dimension mismatch")
        require(basis["dimension_required"] == dim, f"{sector} required dimension mismatch")
        require(len(basis["basis_vectors"]) == dim, f"{sector} basis length mismatch")
        require(basis["finite_27_mode_replay_closed"] is False, f"{sector} basis finite replay should be open")
        require(action["preserves_K_s"] is True, f"{sector} action should preserve K_s")
        require(action["same_source_action"] is True, f"{sector} action should be same-source")
        require(action["functional_selected_rho_s"] is True, f"{sector} rho_s should be functional selected")
        require(action["validator_ready_sector_packet"] is False, f"{sector} validator packet should be open")
        require(shape(action["rho_s_T1"], dim), f"{sector} T1 shape mismatch")
        require(shape(action["rho_s_T2"], dim), f"{sector} T2 shape mismatch")
        require(shape(action["rho_s_T3"], dim), f"{sector} T3 shape mismatch")

    for sector in MATTER:
        require(payload["End0_action_on_zero_modes"][sector]["target_model"] == "adjoint_triplet", f"{sector} model mismatch")
    require(payload["End0_action_on_zero_modes"]["H"]["target_model"] == "trivial_singlet", "H model mismatch")
    require(all(entry == 0 for matrix in ["rho_s_T1", "rho_s_T2", "rho_s_T3"] for row in payload["End0_action_on_zero_modes"]["H"][matrix] for entry in row), "H should be trivial")

    validator = payload["validator_boundary"]
    require(validator["finite_27_mode_validator_replay_closed"] is False, "validator replay should be open")
    require(validator["direct_truncated_relative_residual_from_T1T2_probe"] > 0, "truncation residual should witness open finite replay")
    require(validator["gauge_frame_residual_l2"] < 1e-12, "functional gauge frame residual should be tiny")

    require(all(packet["what_closes_now"].values()), "closure flags should be true")
    require(all(packet["what_remains_open"].values()), "open flags should remain true")
    require(all(packet["guardrails"].values()), "guardrails should hold")
    require(STATUS in note and NEXT in note and "finite 27-mode validator replay" in note, "note missing essentials")

    print("AUDIT_PASS: functional HYM projector/source payload filled; finite replay and physical dotD remain open")


if __name__ == "__main__":
    main()
