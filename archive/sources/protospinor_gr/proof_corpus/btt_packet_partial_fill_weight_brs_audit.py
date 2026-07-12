from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "btt_packet_partial_fill_weight_brs_certificate.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    packet = json.loads(Path(cert["partial_packet_written"]).read_text(encoding="utf-8"))
    note = Path(cert["note_written"]).read_text(encoding="utf-8")

    require(
        cert["status"] == "BTT_PACKET_PARTIALLY_FILLED_WEIGHT2_BRS_CLOSED_EXACT_IMAGE_OPEN",
        "unexpected status",
    )
    source = cert["source_tests"]
    proof = cert["polarization_weight_proof"]
    closed = cert["closed_properties"]
    open_props = cert["still_open_properties"]
    guards = cert["guardrails"]

    require(source["qg_tt_two_point_physical_and_gauge_invariant"] is True, "QG TT physical source missing")
    require(source["qg_pure_gauge_removed_by_bv"] is True, "BV gauge removal source missing")
    require(source["qg_brs_physical_observables_gauge_independent"] is True, "BRST source missing")
    require(source["fcp_linearized_filter_has_tt_projectors"] is True, "TT projector source missing")
    require(
        source["fcp_filter_acts_on_spin2_not_diffeomorphism_modes"] is True,
        "spin-2 not diffeomorphism source missing",
    )

    require(proof["representation_check_Rtheta_Rphi_equals_Rtheta_plus_phi"] is True, "bad SO(2) representation")
    require(proof["nontrivial_spin2_not_spin1_check"] is True, "weight-2 check failed")
    require(proof["central_circle_weight"] == 2, "weight must be 2")

    require(closed["B_TT_central_circle_weight"] == 2, "closed packet weight mismatch")
    require(closed["B_TT_BRST_quotient_compatible"] is True, "BRST property should close")
    require(open_props["B_TT_image_in_retained_exact_branch"] is None, "exact image must remain open")
    require(open_props["same_central_circle_angle_as_Z64_carrier"] is None, "same angle must remain open")
    require(packet["closed_properties"] == closed, "packet should carry closed properties")
    require("same central-circle angle" in note, "note should preserve same-angle gate")

    require(guards["claims_BTT_exact_image_computed"] is False, "must not claim exact image")
    require(guards["claims_same_angle_with_Z64_closed"] is False, "must not claim same angle")
    require(guards["claims_unconditional_lambda_GR_TT_15"] is False, "must not overclose lambda")
    require(guards["uses_observed_GR_data"] is False, "must not use observed GR")

    print("AUDIT_PASS: BTT packet partially filled; weight 2 and BRST closed, exact image open")


if __name__ == "__main__":
    main()
