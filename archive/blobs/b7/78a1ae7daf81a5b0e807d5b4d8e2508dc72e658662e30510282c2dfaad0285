from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "gr_tt_helicity2_z64_uniqueness_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(
        cert["status"] == "UNIQUE_HELICITY2_Z64_WINDOW_PROVED_CHARACTER_WINDOW_PREMISE_OPEN",
        "unexpected status",
    )
    checks = cert["uniqueness_checks"]
    theorem = cert["theorem"]
    premises = cert["remaining_premises"]
    closure = cert["closure_if_premises"]
    guards = cert["guardrails"]

    require(checks["finite_carrier_is_Z64"] is True, "carrier should be Z64")
    require(checks["real_two_dimensional_character_planes_count"] == 31, "Z64 should have 31 real 2D planes")
    require(checks["spin2_character_label"] == 2, "spin label should be 2")
    require(checks["spin2_plane_unique_up_to_conjugation"] is True, "spin2 plane should be unique")
    require(checks["selected_plane"]["character_pair"] == [2, 62], "wrong selected character pair")
    require(checks["selected_plane_order"] == 32, "spin2 plane should have order 32")
    require(checks["competitor_count"] == 30, "wrong competitor count")
    require(
        checks["all_other_real_planes_have_wrong_rotation_weight"] is True,
        "competitors should have wrong weight",
    )
    require(checks["compression_to_15_I2_already_verified"] is True, "compression should be verified")
    require(checks["retarded_kernel_invariance_already_verified"] is True, "retarded invariance should be verified")

    require(theorem["closed"] is True, "uniqueness theorem should close")
    require("only plane with spin-2 rotation weight" in theorem["statement"], "theorem statement weakened")
    require(
        premises["same_central_circle_angle_for_GR_TT_response"]["status"]
        == "SOURCE_COMPATIBLE_BUT_NOT_EXPLICITLY_CERTIFIED",
        "angle premise status wrong",
    )
    require(
        premises["selected_GR_TT_Aint_projector_window_is_a_central_circle_character_subfiber"]["status"]
        == "SOURCE_COMPATIBLE_BUT_NOT_EXPLICITLY_CERTIFIED",
        "character-window premise status wrong",
    )
    require(
        closure["if_both_remaining_premises_are_accepted"]["lambda_GR_TT"] == 15.0,
        "conditional lambda should be 15",
    )
    require(
        closure["without_those_premises"]["status"] == cert["status"],
        "open status mismatch",
    )

    require("lambda_GR,TT = 15" in note, "note lost conditional lambda")
    require("The representation-theoretic part is now closed" in note, "note lost closure boundary")

    require(guards["claims_remaining_premises_sourced"] is False, "must not claim premises sourced")
    require(guards["claims_unconditional_full_GR_TT_gap_15"] is False, "must not claim unconditional gap")
    require(guards["claims_order32_is_primitive_order64"] is False, "must not claim primitive order")
    require(guards["claims_physical_dimensionful_gap"] is False, "must not claim physical gap")
    require(guards["claims_Newton_or_Planck_prediction"] is False, "must not claim Newton/Planck")

    print("AUDIT_PASS: unique helicity-2 Z64 window proved; character-window premise remains open")


if __name__ == "__main__":
    main()
