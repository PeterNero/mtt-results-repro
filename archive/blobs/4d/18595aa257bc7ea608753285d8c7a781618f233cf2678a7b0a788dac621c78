from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "tt_helicity2_z64_carrier_functor_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(
        cert["status"] == "TT_HELICITY2_Z64_CARRIER_FUNCTOR_CONSTRUCTED_SOURCE_IDENTITY_OPEN",
        "unexpected status",
    )

    source = cert["source_tests"]
    checks = cert["numerical_checks"]
    functor = cert["constructed_functor"]
    verdict = cert["verdict"]
    guards = cert["guardrails"]

    require(source["TT_spin2_rotation_sourced"] is True, "TT spin-2 source missing")
    require(source["QG_spin2_propagator_sourced"] is True, "QG spin-2 source missing")
    require(source["central_circle_gravity_channel_sourced"] is True, "central-circle gravity source missing")
    require(source["Z64_group_algebra_carrier_sourced"] is True, "Z64 carrier source missing")
    require(source["Z64_shift_sourced"] is True, "Z64 shift source missing")
    require(source["Z64_selected_tower_lambda15_sourced"] is True, "Z64 tower lambda source missing")
    require(
        source["source_explicitly_identifies_TT_helicity2_with_Z64_k2"] is False,
        "source identity unexpectedly closed",
    )
    require(
        source["source_explicitly_states_projector_window_equality_for_this_functor"] is False,
        "projector/window equality unexpectedly sourced",
    )

    require(checks["N"] == 64, "wrong finite circle")
    require(checks["helicity"] == 2, "wrong helicity")
    require(checks["character_label_k"] == 2, "wrong character label")
    require(checks["character_order"] == 32, "helicity-2 character should have order 32 on Z64")
    require(checks["orthonormal_to_tolerance"] is True, "real character pair is not orthonormal")
    require(checks["retarded_kernel_preserves_real_pair"] is True, "retarded kernel should preserve pair")
    require(checks["compression_equals_15_I2"] is True, "compression should be 15 I2")
    require(abs(checks["gram"]["cos_cos"] - 1.0) < 1e-12, "cos norm mismatch")
    require(abs(checks["gram"]["sin_sin"] - 1.0) < 1e-12, "sin norm mismatch")
    require(abs(checks["gram"]["cos_sin"]) < 1e-12, "cos/sin not orthogonal")

    require(functor["isometry_in_canonical_group_algebra_inner_product"] is True, "functor isometry failed")
    require("TT_plus" in functor["map"], "TT_plus not mapped")
    require("TT_cross" in functor["map"], "TT_cross not mapped")

    require(verdict["canonical_helicity2_carrier_functor_constructed"] is True, "carrier functor not constructed")
    require(verdict["algebraic_compression_to_15_I2_closed"] is True, "compression not closed")
    require(verdict["retarded_kernel_preserves_functor_image"] is True, "kernel invariance not closed")
    require(verdict["functor_lands_in_Z64_carrier"] is True, "functor should land in Z64 carrier")
    require(verdict["functor_uses_primitive_order64_character"] is False, "must not claim primitive k")
    require(verdict["full_source_certified_GR_TT_Z64_identity_closed"] is False, "must not overclose source identity")
    require("not primitive order `64`" in note, "note lost order caveat")
    require("U_TT^* L_64 U_TT = 15 I_2" in note, "note lost compression")

    require(guards["claims_full_source_certified_GR_TT_gap_15"] is False, "must not claim full source closure")
    require(guards["claims_helicity2_character_is_primitive_Z64"] is False, "must not claim primitive Z64")
    require(guards["claims_projector_window_equality_sourced"] is False, "must not claim projector/window")
    require(guards["claims_physical_dimensionful_gap"] is False, "must not claim physical gap")
    require(guards["claims_Newton_or_Planck_prediction"] is False, "must not claim Newton/Planck")

    print("AUDIT_PASS: helicity-2 Z64 carrier functor constructed; source identity remains open")


if __name__ == "__main__":
    main()
