"""Audit selected_i11_c1coordinatechart_or_physicalsourcegap."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_i11_c1coordinatechart_or_physicalsourcegap"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CHART = PACKET_DIR / "c1_response_coordinate_chart_sublemma.packet.json"
CURRENT = PACKET_DIR / "current_c1_coordinate_chart_trace_map_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_physical_source_trace_map_witness.packet.json"
FRONTIER = PACKET_DIR / "remaining_physical_source_boundary_firstvariation_frontier.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_I11_C1CoordinateChart_or_PhysicalSourceGap_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_i11_trace_map.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validator_returncode(path: Path) -> int:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return proc.returncode


def main() -> int:
    data = load(DATA)
    chart = load(CHART)
    current = load(CURRENT)
    witness = load(WITNESS)
    frontier = load(FRONTIER)
    current_result = load(CURRENT_RESULT)
    witness_result = load(WITNESS_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_I11_C1_COORDINATE_CHART_BUILT_PHYSICAL_SOURCE_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["conditional_only"] is True, "candidate should be conditional")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(chart["proved"] is True, "coordinate chart should be built")
    require(chart["coordinate_system"]["codomain_real_dimension"] == 72, "wrong chart dimension")
    require(chart["row_counts"]["total_rows"] == 110, "wrong row count")
    require(chart["source_execution_open"] is True, "source execution should remain open")
    require("selected A_selected emission" in chart["not_closed"], "A_selected should remain open")

    require(current["c1_coordinate_chart_built"] is True, "current should carry chart support")
    require(current["c1_response_coordinate_map"] is False, "source coordinate map overpromoted")
    require(current["selected_normalization_boundary_clause"] is False, "boundary overpromoted")
    require(current["dynamic_c1_flags_verified"] is False, "dynamic flags overpromoted")
    require(current["free_axiom_patch_used"] is False, "free patch used")
    require(witness["conditional_only"] is True, "witness should be conditional")
    require(current_result["returncode"] == 1, "recorded current validator should fail")
    require(witness_result["returncode"] == 0, "recorded witness validator should pass")
    require(validator_returncode(CURRENT) == 1, "current validator should fail")
    require(validator_returncode(WITNESS) == 0, "witness validator should pass")

    require(frontier["closed_now"]["c1_response_coordinate_chart"] is True, "frontier should close chart")
    require(frontier["still_open"]["selected_c1_response_coordinate_map_as_source"]["primitive_rows_executed"] is False, "primitive rows overpromoted")
    require(frontier["still_open"]["physical_boundary_cancellation"]["physical_verified"] is False, "boundary overpromoted")
    require(cert["c1_response_coordinate_chart_built"] is True, "cert should record chart")
    require("primitive rows = 72" in note, "note missing primitive count")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
