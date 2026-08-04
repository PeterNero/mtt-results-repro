"""Audit selected_latest_trueequivalencefrontier_or_valueemissioncutset."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_latest_trueequivalencefrontier_or_valueemissioncutset"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
FRONTIER = PACKET_DIR / "latest_true_equivalence_value_source_frontier.packet.json"
CUTSET = PACKET_DIR / "next_value_source_emission_cutset.packet.json"
NEXT_ACTIONS = PACKET_DIR / "next_actions_for_true_equivalence.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_LatestTrueEquivalenceFrontier_or_ValueEmissionCutset_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    frontier = load(FRONTIER)
    cutset = load(CUTSET)
    next_actions = load(NEXT_ACTIONS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_LATEST_TRUEEQUIVALENCE_FRONTIER_BUILT_VALUE_SOURCE_CUTSET_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "cutset theorem not proved")
    require(data["SM_parity_closed"] is True, "SM parity should remain closed")
    require(data["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(data["no_knob_closed"] is False, "no-knob overclaimed")
    require(data["closure_claimed"] is False, "unqualified closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(frontier["SM_parity_not_reopened"] is True, "SM parity reopened")
    require(frontier["bookkeeping_layer_closed"]["precision_value_table_contract"] is True, "precision contract missing")
    require(frontier["bookkeeping_layer_closed"]["actual_QaSU3_operator_upgrade_contract"] is True, "QaSU3 contract missing")
    require(frontier["bookkeeping_layer_closed"]["partial_precision_values_emitted"] is True, "partial values missing")
    require(frontier["bookkeeping_layer_closed"]["post_parity_source_upgrade_kernel_built"] is True, "source kernel missing")
    require(frontier["still_open"]["actual_QaSU3_operator_packet"] is True, "actual QaSU3 not open")
    require(frontier["still_open"]["full_nonHiggs_covariance_profile"] is True, "profile not open")
    require(frontier["still_open"]["precision_local_QFT_loop_values"] is True, "loop QFT not open")

    require("precision_value_route" in cutset["legal_routes"], "precision route missing")
    require("actual_source_route" in cutset["legal_routes"], "actual source route missing")
    require(len(cutset["forbidden_shortcuts"]) == 4, "forbidden shortcut count changed")
    require(cutset["closure_claimed"] is False, "cutset overclosed")

    require(next_actions["recommended_next"] == "MTT_Selected_FullProfileMatrixReconstruction_or_QaSU3ActualPacketSearch_v1", "wrong next artifact")
    require(next_actions["superset_strategy"]["uses_observed_constants_as_source_selectors"] is False, "observed selectors used")
    require(cert["bookkeeping_to_value_source_cutset_identified"] is True, "cert missing cutset")
    require("SM parity remains closed. True SM equivalence is not closed." in note, "note missing status")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
