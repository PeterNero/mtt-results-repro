from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "selected_phifin_alpha1_payload_value_emission_certificate.json"
STATUS = "SELECTED_PHIFIN_ALPHA1_PAYLOAD_PREFIX_IMPORTED_DOTD_VALUES_SOURCE_DRIVER_OPEN"
NEXT = "Selected_dotD_alpha1_Source_and_Driver_Theorem_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == STATUS, "unexpected status")
    require(cert["closure_claimed"] is False, "must not claim closure")
    require(all(cert["checks"].values()), "all certificate checks should pass")
    require(all(cert["what_closes_now"].values()), "closure prefix should be true")
    require(all(cert["what_remains_open"].values()), "all blockers should remain open")
    require(cert["next_required_artifact"] == NEXT, "wrong next artifact")

    prefix = packet["imported_closed_prefix"]
    require(prefix["same_basis_dotD_values_available"] is True, "dotD value prefix missing")
    require(prefix["basis_id"] == "F3xF3_gerbe_twisted_fourier_N1_rank3", "wrong basis")
    require(prefix["dotD_alpha1_value_matrices_emitted"] is True, "dotD matrices should be present")
    require(prefix["sector_projectors_clean"] is True, "projectors should be clean")
    require(prefix["dotD_alpha1_has_nonzero_entries"] is True, "dotD should be nonzero")

    for sector, slot in prefix["sector_shape_checks"].items():
        require(slot["projector_rank_matches_expected"] is True, f"{sector} rank mismatch")
        require(slot["dotD_alpha1_matrix_shape"] == [27, 27], f"{sector} dotD shape mismatch")
        require(slot["dotD_alpha1_nonzero_entries"] > 0, f"{sector} dotD should be nonzero")
        require(slot["selected_dotD_source_verified"] is False, f"{sector} dotD source must remain false")
        require(slot["alpha1_driver_verified"] is False, f"{sector} alpha1 driver must remain false")

    boundary = packet["honest_replay_boundary"]
    require(boundary["closed"] is True, "honest replay boundary should be exact")
    require(boundary["exit_code"] == 1, "honest replay should fail by open flags")
    require(
        boundary["fails_only_by_source_driver_flags"] is True,
        "failure should be only source/driver flags",
    )

    status = packet["payload_emission_status"]
    require(status["SelectedPhiFinAlpha1Payload_fully_emitted"] is False, "payload must remain open")
    require(status["dotD_alpha1_value_matrices_emitted_as_unpromoted_prefix"] is True, "prefix missing")
    require(status["selected_dotD_source_theorem_proved"] is False, "dotD theorem must remain open")
    require(status["same_branch_alpha1_driver_theorem_proved"] is False, "alpha1 theorem must remain open")
    require(status["A_selected_emitted"] is False, "A_selected must not be emitted")
    require(status["b_selected_emitted"] is False, "b_selected must not be emitted")
    require(status["sector_response_matrices_emitted"] is False, "sector C1 response must not be emitted")
    require(status["evaluated_grad_V_C1_alpha1_source_vector"] is None, "source vector must be null")

    require(all(packet["guardrails"].values()), "guardrails must all hold")
    require(STATUS in note and NEXT in note and "selected_dotD_source_verified = false" in note, "note missing essentials")

    print("AUDIT_PASS: PhiFin alpha1 payload prefix imported; source/driver theorem remains open")


if __name__ == "__main__":
    main()
