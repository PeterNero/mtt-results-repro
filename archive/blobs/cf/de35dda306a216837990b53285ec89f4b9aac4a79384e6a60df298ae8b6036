from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "gr_tt_exact_branch_identity_final_gate_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(
        cert["status"] == "EXACT_BRANCH_GR_GAP_THEOREM_AVAILABLE_FULL_GR_IDENTITY_OPEN",
        "unexpected status",
    )
    source = cert["source_tests"]
    guards = cert["guardrails"]
    options = cert["theorem_options"]

    require(source["gr_uses_coherent_projection_pushforward"] is True, "GR projection source missing")
    require(source["gr_selects_low_frequency_large_scale_limit"] is True, "GR low-frequency source missing")
    require(source["gr_string_says_same_upstairs_projector_gap"] is True, "same projector/gap source missing")
    require(source["central_circle_links_gravity_bookkeeping"] is True, "central-circle gravity source missing")
    require(source["gr_source_names_exact_z64_branch"] is False, "GR source unexpectedly names Z64")
    require(source["gr_source_maps_TT_closure_strain_to_z64_tower"] is False, "GR TT/Z64 map unexpectedly sourced")
    require(source["central_source_maps_TT_operator_to_z64_tower"] is False, "central TT/Z64 operator map unexpectedly sourced")

    require(options["exact_branch_GR_theorem"]["status"] == "AVAILABLE", "exact branch theorem should be available")
    require(options["unconditional_full_GR_TT_gap_theorem"]["status"] == "NOT_CLOSED", "full GR must remain open")
    require(cert["closed_now"]["exact_branch_internal_gap_closed"] is True, "exact gap should be closed")
    require(cert["not_closed"]["unconditional_full_GR_TT_gap"] is True, "full GR gap must remain open")
    require("P_GR,TT A_int P_GR,TT" in note, "note lost final map")

    require(guards["claims_full_GR_TT_gap_15"] is False, "must not claim full GR gap")
    require(guards["claims_GR_TT_equals_Z64_without_map"] is False, "must not claim identity without map")
    require(guards["claims_physical_dimensionful_gap"] is False, "must not claim physical gap")
    require(guards["claims_Newton_or_Planck_prediction"] is False, "must not claim Newton/Planck")

    print("AUDIT_PASS: exact-branch GR gap theorem available; full GR identity remains open")


if __name__ == "__main__":
    main()
