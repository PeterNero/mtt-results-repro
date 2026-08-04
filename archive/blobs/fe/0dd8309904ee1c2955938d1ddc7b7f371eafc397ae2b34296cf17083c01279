"""Audit selected_latest_smparityclosure_status_or_trueequivalencefrontier."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_latest_smparityclosure_status_or_trueequivalencefrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
LATEST = PACKET_DIR / "latest_smparity_closure_status.packet.json"
TRUE_FRONTIER = PACKET_DIR / "true_equivalence_and_noknob_frontier.packet.json"
NEXT_ACTIONS = PACKET_DIR / "next_actions_after_smparity_closure.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_LatestSMParityClosureStatus_or_TrueEquivalenceFrontier_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    latest = load(LATEST)
    true_frontier = load(TRUE_FRONTIER)
    next_actions = load(NEXT_ACTIONS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_LATEST_SMPARITYCLOSURE_STATUS_BUILT_TRUE_EQUIVALENCE_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "latest theorem not proved")
    require(data["SM_parity_closed"] is True, "SM parity should be closed")
    require(data["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(data["no_knob_closed"] is False, "no-knob overclaimed")
    require(data["closure_claimed"] is False, "unqualified closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(latest["SM_parity_closed"] is True, "latest packet missing SM parity closure")
    require(latest["patched_dynamic_C1_retired"] is True, "patched dynamic C1 not retired")
    require(latest["accepted_RG_transport_for_SM_parity"] is True, "RG transport not accepted")
    require(latest["selected_SM_packet_certificate_integrated_for_SM_parity"] is True, "SM packet not integrated")
    require(latest["not_claimed"]["actual_selected_QaSU3_no_knob_packet"] is True, "QaSU3 no-knob overclaimed")
    require(latest["not_claimed"]["true_precision_SM_equivalence"] is True, "precision equivalence overclaimed")
    require(latest["not_claimed"]["full_no_knob_closure"] is True, "full no-knob overclaimed")

    require(true_frontier["true_SM_equivalence_closed"] is False, "true frontier overclosed")
    require(true_frontier["no_knob_closed"] is False, "no-knob frontier overclosed")
    require(true_frontier["precision_suite_built"] is True, "precision suite not built")
    require(true_frontier["no_knob_open"]["actual_QaSU3_operator_packet_upgrade"] is True, "QaSU3 upgrade not open")
    require(true_frontier["no_knob_open"]["unpatched_dynamic_C1_measure_derivation"] is True, "unpatched C1 not open")

    require(next_actions["superset_strategy"]["uses_observed_constants_as_selectors"] is False, "observed constants used as selectors")
    require(len(next_actions["recommended_primary_path"]) == 4, "primary path count changed")
    require(len(next_actions["recommended_no_knob_path"]) == 3, "no-knob path count changed")
    require(cert["SM_parity_closed_under_declared_standard"] is True, "cert missing SM parity closure")
    require(cert["true_SM_equivalence_closed"] is False, "cert true equivalence overclaimed")
    require(cert["no_knob_closed"] is False, "cert no-knob overclaimed")
    require("SM parity is closed under the declared parity-interface standard" in note, "note missing closure statement")
    require("not** a claim" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
