"""Audit const_em_01_alpha1_dimensional_anchor_packet_gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_em_01_alpha1_dimensional_anchor_packet_gate"
CANDIDATE = DATA / "const_em_01_alpha1_dimensional_anchor_packet_gate.candidate.json"
ACCEPTANCE = BASE / "acceptance_criteria.packet.json"
ROUTES = BASE / "route_matrix.packet.json"
PROMOTION = BASE / "promotion_tests.packet.json"
CERT = ROOT / "certificates" / "const_em_01_alpha1_dimensional_anchor_packet_gate_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EM_01_Alpha1_DimensionalAnchorPacketGate_v1.md"
BUILD = ROOT / "scripts" / "build_const_em_01_alpha1_dimensional_anchor_packet_gate.py"
STATUS = "MTT_CONST_EM_01_DIMENSIONAL_ANCHOR_PACKET_GATE_BUILT_VALUE_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    acceptance = load(ACCEPTANCE)
    routes = load(ROUTES)
    promotion = load(PROMOTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "gate theorem not proved")
    require(candidate["what_closes_now"]["acceptance_gate"] is True, "acceptance gate not closed")
    require(candidate["what_closes_now"]["route_selection_for_next_attack"] == "m_theory_modal_gap_planck_anchor", "route mismatch")
    require(candidate["what_remains_open"]["dimensionful_anchor_value"] is True, "dimensionful value closed too early")
    require(candidate["what_remains_open"]["alpha_phys_value"] is True, "alpha_phys closed too early")
    require(candidate["what_remains_open"]["K_phys_value"] is True, "K_phys closed too early")

    require(all(acceptance["import_checks"].values()), "import check failed")
    required = acceptance["required_fields"]
    require(required["source_certification.selected_by_mtt"] is True, "selected_by_mtt criterion missing")
    require(required["source_certification.computed_before_target_comparison"] is True, "pre-target criterion missing")
    require(required["map_to_alpha_phys.alpha_phys_value"] == "computed from the selected anchor, not backsolved", "alpha criterion mismatch")
    require("observed_alpha_EM_or_weak_angle" in acceptance["forbidden_inputs_absent_must_be_true"], "EW backsolve guard missing")

    require(routes["selected_route_for_next_attack"] == "m_theory_modal_gap_planck_anchor", "route packet mismatch")
    require(routes["superset_strategy"]["locked_target"] == "a single selected dimensional anchor packet, not separately tuned constants", "superset lock missing")
    require("individual constants alpha1 gate" in routes["superset_strategy"]["combined_paths"], "alpha1 path missing")

    current = promotion["current_packet"]
    require(current["structural_slot_filled"] is True, "structural slot missing")
    require(current["value_present"] is False, "value present unexpectedly")
    require(current["selected_by_mtt"] is False, "selected_by_mtt closed unexpectedly")
    require(current["computed_before_target_comparison"] is False, "pre-target closed unexpectedly")
    require(current["alpha_phys_value_present"] is False, "alpha_phys value present unexpectedly")
    require(promotion["promotion_now"] is False, "promotion overclaimed")

    require(cert["physical_value_claimed"] is False, "cert physical value overclaim")
    require(cert["alpha_phys_value_claimed"] is False, "cert alpha overclaim")
    require(cert["K_phys_value_claimed"] is False, "cert K overclaim")
    require("They are not independent knobs." in note, "superset guard note missing")

    for packet in [candidate, acceptance, routes, promotion, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
