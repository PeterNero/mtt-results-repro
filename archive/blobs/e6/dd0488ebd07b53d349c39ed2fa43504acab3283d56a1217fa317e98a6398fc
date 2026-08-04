"""Audit selected_sectorcharge_1mdirac_sourceemission_or_transportclosedvalidatorreplay."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_sectorcharge_1mdirac_sourceemission_or_transportclosedvalidatorreplay"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_DECISION = PACKET_DIR / "sector_source_or_transport_replay_route_decision.packet.json"
SOURCE_TEMPLATE = PACKET_DIR / "u10_ubar5_1m_samebranch_source_emission_template.packet.json"
LIVE_FRONTIER = PACKET_DIR / "live_sector_source_frontier_after_transport_replay.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SectorCharge_1MDirac_SourceEmission_or_TransportClosedValidatorReplay_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    route = load(ROUTE_DECISION)
    template = load(SOURCE_TEMPLATE)
    frontier = load(LIVE_FRONTIER)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_SECTORCHARGE_1MDIRAC_SOURCEEMISSION_OR_TRANSPORTCLOSEDVALIDATORREPLAY_BUILT_TRANSPORT_REPLAY_CLOSED_SOURCE_EMISSION_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["SM_parity_closed"] is True, "SM parity regressed")
    require(data["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(data["no_knob_closed"] is False, "no-knob overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["closure_claimed"] is False, "closure overclaimed")

    require(route["route_B_transport_closed_validator_replay"]["closed_now"] is True, "transport replay not closed")
    require(route["route_B_transport_closed_validator_replay"]["selected_rho_s_validator_ready"] is True, "rho_s replay not ready")
    require(route["route_B_transport_closed_validator_replay"]["dotD_alpha1_included"] is False, "dotD alpha1 overincluded")
    require(route["route_A_sector_source_emission"]["closed_now"] is False, "route A overclosed")
    require(route["route_A_sector_source_emission"]["structural_1M_rule_available"] is True, "1M support missing")
    require(route["route_A_sector_source_emission"]["q79_U10_Ubar5_support_closed"] is True, "q79 support missing")

    require(template["must_emit"]["selected_U10_clock_source"]["source_closed"] is False, "U10 overclosed")
    require(template["must_emit"]["selected_Ubar5_shift_source"]["source_closed"] is False, "Ubar5 overclosed")
    require(template["must_emit"]["selected_1M_Dirac_neutrino_shift_source"]["source_closed"] is False, "1M overclosed")
    require(template["must_emit"]["selected_overlap_transfer_normalization"]["static_tier_closed"] is True, "static normalization not closed")
    require(template["must_emit"]["selected_overlap_transfer_normalization"]["dynamic_tier_closed"] is False, "dynamic normalization overclosed")
    require(len(template["forbidden_shortcuts"]) == 4, "forbidden shortcuts changed")

    require(frontier["static_source_tier_closed"] is True, "static tier not closed")
    require(frontier["transport_closed_projector_riesz_green_rhos_closed"] is True, "transport replay not closed in frontier")
    require("dynamic PhiFin^C1/primitive C1 payload with A_selected and b_selected" in frontier["remaining_source_payloads"], "dynamic C1 missing")
    require(cert["transport_closed_validator_replay_route_resolved"] is True, "cert route flag missing")
    require(cert["samebranch_source_emission_open"] is True, "cert source-open flag missing")
    require(data["next_required_artifact"] == "MTT_Selected_U10Ubar5_1M_SourcePromotion_SameBranch_Emission_v1", "wrong next artifact")
    require("No observed constants" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
