"""Audit transport replay import and U10/Ubar5/1M source frontier."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_transportreplay_imported_or_u10ubar5_1m_source"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FRONTIER = PACKET_DIR / "u10_ubar5_1m_remaining_source_frontier.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TransportReplay_Imported_or_U10Ubar5_1M_Source_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    frontier = load(FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_TRANSPORTREPLAY_IMPORTED_BUILT_U10UBAR5_1M_SOURCE_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["SM_parity_closed"] is True, "SM parity reopened")
    require(data["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(data["no_knob_closed"] is False, "no-knob overclaimed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(frontier["transport_closed_validator_replay_imported"] is True, "transport replay not imported")
    require(frontier["validator_ready_sector_rho_s_packet_imported"] is True, "rho_s validator packet not imported")
    require(frontier["projector_riesz_green_source_verified"] is True, "projector/Riesz/Green not verified")
    require(frontier["structural_1M_rule_candidate_available"] is True, "1M structural candidate absent")
    require(frontier["route_A_finite_polarization_support"] is True, "route A support absent")
    require(frontier["route_B_projector_support"] is True, "route B support absent")
    require(frontier["retired_now"]["transport_closed_finite_validator_replay"] is True, "transport not retired")

    still = frontier["still_open"]
    require(still["selected_U10_clock_source"] is True, "U10 overclosed")
    require(still["selected_Ubar5_shift_source"] is True, "Ubar5 overclosed")
    require(still["selected_1M_Dirac_neutrino_shift_source"] is True, "1M source overclosed")
    require(still["selected_ordered_matter_slot_packet"] is True, "matter slot overclosed")
    require(still["selected_dynamic_PhiFin_C1_payload"] is True, "dynamic PhiFin overclosed")
    require(still["actual_QaSU3_operator_packet"] is True, "Qa/SU3 overclosed")

    require(cert["transport_replay_imported_as_closed"] is True, "cert missing transport import")
    require(cert["sector_source_frontier_narrowed_to_U10_Ubar5_1M"] is True, "cert missing narrowed frontier")
    require(data["next_required_artifact"] == "MTT_Selected_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1", "wrong next artifact")
    require("no longer transport closure" in note, "note missing transport guard")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
