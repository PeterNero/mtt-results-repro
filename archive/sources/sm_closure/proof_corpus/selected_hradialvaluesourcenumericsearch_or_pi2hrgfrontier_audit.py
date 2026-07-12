"""Audit H radial value-source numeric search / pi2 HRG frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_hradialvaluesourcenumericsearch_or_pi2hrgfrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PI_PACKET = PACKET_DIR / "d211_pi2_identity_clue.packet.json"
SEARCH = PACKET_DIR / "bounded_hrg_radial_expression_search.packet.json"
GATE = PACKET_DIR / "hrg_radial_source_acceptance_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_HRadialValueSourceNumericSearch_or_Pi2HRGFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_HRADIALVALUESOURCENUMERICSEARCH_OR_PI2HRGFRONTIER_"
    "PI2_CLUE_LOCKED_NUMERIC_SEARCH_NO_SOURCE"
)
NEXT = "MTT_Selected_HRadialTransportMap_or_DynamicPhiFinC1Consumer_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict, label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    pi_packet = load(PI_PACKET)
    search = load(SEARCH)
    gate = load(GATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", data),
        ("pi_packet", pi_packet),
        ("search", search),
        ("gate", gate),
        ("certificate", cert),
    ]:
        guard(packet, label)

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "certificate status")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "certificate next")
    require(data["theorem"]["proved"] is True, "theorem")
    require(data["full_no_knob_closure_claimed"] is False, "no-knob overclaim")
    require(data["true_SM_equivalence_claimed"] is False, "true SM overclaim")

    require(abs(pi_packet["base_formula_residual"]) < 1e-10, "base pi2 residual")
    require(abs(pi_packet["trace_formula_residual"]) < 1e-10, "trace pi2 residual")
    require(abs(pi_packet["rank_over_trace_minus_pi_squared"]) < 1e-9, "rank/trace pi2 residual")
    require(pi_packet["accepted_as_H_radial_source"] is False, "pi2 overpromoted")

    require(search["accepted_source_expression_count"] == 0, "source expression overaccepted")
    require(len(search["best_candidates"]) == 25, "best candidate list")
    require(search["search_policy"]["diagnostic_only"] is True, "search not diagnostic")
    require(search["search_policy"]["target_residual_search_does_not_select_source"] is True, "target search selector")
    require(search["hand_checked_near_misses"][0]["accepted_as_source"] is False, "near miss overaccepted")

    require(gate["pi2_D211_identity_clue_locked"] is True, "gate pi2")
    require(gate["bounded_numeric_search_completed"] is True, "gate search")
    require(gate["accepted_radial_source_value_count"] == 0, "gate radial overaccept")
    require(gate["accepted_nonhiggs_HRG_prediction_count"] == 0, "gate nonhiggs overaccept")
    require(gate["UP_RET_OVERLAP_HRG_source_promoted"] is False, "HRG overpromoted")
    require(gate["strict_r_H_promoted"] is False, "rH overpromoted")
    require(gate["strict_N_H_promoted"] is False, "NH overpromoted")

    decision = data["closure_decision"]
    require(decision["D211_pi2_identity_clue_locked"] is True, "decision pi2")
    require(decision["base_equals_27_over_4pi2_to_roundoff"] is True, "decision base")
    require(decision["rank_over_trace_equals_pi2_to_roundoff"] is True, "decision rank trace")
    require(decision["accepted_radial_source_value_count"] == 0, "decision radial")
    require(decision["strict_r_H_promoted"] is False, "decision rH")
    require(decision["strict_N_H_promoted"] is False, "decision NH")

    for phrase in [
        "HRadialPi2ClueAndNumericSearchFrontierTheorem",
        "base(D_211)",
        "rank/Tr(D_211)",
        "Accepted radial source expressions: `0`",
        "numeric proximity is not a selected source map",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print("AUDIT_PASS: D211/pi2 clue locked; bounded HRG radial numeric search has zero accepted source expressions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
