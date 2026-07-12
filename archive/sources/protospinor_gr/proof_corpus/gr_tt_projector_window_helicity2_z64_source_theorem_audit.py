from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "gr_tt_projector_window_helicity2_z64_source_theorem_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(cert["status"] == "HELICITY2_FUNCTOR_READY_SOURCE_IDENTITY_OPEN", "unexpected status")
    source = cert["source_tests"]
    partial = cert["partial_closures"]
    decision = cert["theorem_decision"]
    guards = cert["guardrails"]

    require(source["qg_defines_TT_projected_graviton_operator"] is True, "QG TT operator source missing")
    require(source["qg_defines_SPT_projector_window"] is True, "QG SPT window source missing")
    require(source["constructive_qg_defines_physical_TT_sector"] is True, "constructive TT source missing")
    require(source["central_circle_gravity_bookkeeping_sourced"] is True, "central gravity source missing")
    require(source["central_circle_unique_shared_channel_sourced"] is True, "central shared channel source missing")
    require(source["z64_projector_retains_finite_character_carrier"] is True, "Z64 character carrier source missing")
    require(source["z64_projector_character_spectrum_sourced"] is True, "Z64 character spectrum source missing")
    require(source["z64_projector_selects_dstar_tower"] is True, "Z64 dstar source missing")

    require(
        source["source_states_TT_plus_cross_use_central_circle_helicity2_character_fiber"] is False,
        "TT helicity2 central fiber unexpectedly sourced",
    )
    require(
        source["source_states_selected_GR_TT_projector_window_equals_dstar_tensor_k2_pair"] is False,
        "projector/window equality unexpectedly sourced",
    )
    require(
        source["source_states_order32_helicity2_is_allowed_as_GR_TT_subfiber_of_Z64"] is False,
        "order32 physical subfiber unexpectedly sourced",
    )

    require(partial["TT_helicity2_carrier_functor_constructed"] is True, "functor should be constructed")
    require(partial["compression_to_15_I2_closed"] is True, "compression should close")
    require(partial["retarded_kernel_preserves_helicity2_plane"] is True, "kernel should preserve plane")
    require(
        partial["order32_subcharacter_is_mathematically_inside_Z64_carrier"] is True,
        "order32 subcharacter should be mathematically inside carrier",
    )
    require(partial["qg_selects_TT_SPT_projector_window_in_general"] is True, "QG TT window not generally sourced")
    require(partial["central_circle_is_gravity_shared_channel"] is True, "central gravity channel not sourced")

    require(decision["source_identity_closed"] is False, "source identity must remain open")
    require("do not explicitly identify" in decision["why_not_closed"], "decision should explain missing identity")
    require("lambda_GR_TT = 15" in decision["if_missing_source_lemma_is_added"]["consequence"], "lost consequence")
    require(decision["status_if_no_new_source"] == cert["status"], "status mismatch")

    require("selected GR TT A_int projector/window" in note, "note lost missing identity")
    require("lambda_GR,TT = 15" in note, "note lost conditional consequence")

    require(guards["claims_source_identity_closed"] is False, "must not claim source identity")
    require(guards["claims_full_GR_TT_gap_15"] is False, "must not claim full GR gap")
    require(guards["claims_order32_is_primitive_order64"] is False, "must not claim primitive order")
    require(guards["claims_physical_dimensionful_gap"] is False, "must not claim physical gap")
    require(guards["claims_Newton_or_Planck_prediction"] is False, "must not claim Newton/Planck")

    print("AUDIT_PASS: source theorem searched; helicity2 functor ready, source identity open")


if __name__ == "__main__":
    main()
