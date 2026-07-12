"""Audit selected_physicalboundaryfirstvariation_or_selectedsourceemission."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_physicalboundaryfirstvariation_or_selectedsourceemission"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CURRENT = PACKET_DIR / "current_physical_boundary_firstvariation_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_physical_source_emission_witness.packet.json"
I11_BRIDGE = PACKET_DIR / "conditional_i11_trace_map_bridge.packet.json"
FRONTIER = PACKET_DIR / "remaining_selected_source_emission_frontier.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_physical_source_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_physical_source_validator_result.packet.json"
I11_BRIDGE_RESULT = PACKET_DIR / "conditional_i11_trace_map_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalBoundaryFirstVariation_or_SelectedSourceEmission_v1.md"
PHYSICAL_VALIDATOR = ROOT / "scripts" / "validate_selected_physical_boundary_firstvariation_source.py"
I11_VALIDATOR = ROOT / "scripts" / "validate_selected_i11_trace_map.py"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validator_returncode(validator: Path, path: Path) -> int:
    proc = subprocess.run(
        [sys.executable, str(validator), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return proc.returncode


def main() -> int:
    data = load(DATA)
    current = load(CURRENT)
    witness = load(WITNESS)
    i11_bridge = load(I11_BRIDGE)
    frontier = load(FRONTIER)
    current_result = load(CURRENT_RESULT)
    witness_result = load(WITNESS_RESULT)
    i11_bridge_result = load(I11_BRIDGE_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_PHYSICALBOUNDARYFIRSTVARIATION_GATE_BUILT_SOURCE_EMISSION_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "gate theorem not proved")
    require(data["conditional_only"] is True, "candidate should be conditional")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(current["same_branch"] is True, "current same_branch missing")
    require(current["theorem_derived"] is False, "current overclosed theorem")
    require(current["physical_first_variation_identity"] is False, "current overclosed first variation")
    require(current["physical_measure_equals_trace_frobenius_pairing"] is False, "current overclosed measure")
    require(current["phase_R_Z_source_selection"] is False, "current overclosed R_Z")
    require(current["shift_R_X_source_selection"] is False, "current overclosed R_X")
    require(current["same_source_b_selected_emission"] is False, "current overclosed b")
    require(current["no_extra_physical_boundary_or_source_term"] is False, "current overclosed boundary")
    require(current["locked_target_values_used_as_source"] is False, "current uses locked target")
    require(current["residual_projector_replay_used_as_source"] is False, "current uses residual replay")
    require(current["benchmark_values_used_as_source"] is False, "current uses benchmark")
    require(len(current["attached_source_evidence"]) >= 6, "current evidence too short")

    for key in [
        "theorem_derived",
        "physical_first_variation_identity",
        "physical_measure_equals_trace_frobenius_pairing",
        "phase_R_Z_source_selection",
        "shift_R_X_source_selection",
        "same_source_b_selected_emission",
        "no_extra_physical_boundary_or_source_term",
    ]:
        require(witness[key] is True, f"witness missing {key}")
    require(witness["conditional_only"] is True, "witness should be conditional")

    require(i11_bridge["selected_normalization_boundary_clause"] is True, "I11 bridge missing boundary")
    require(i11_bridge["dynamic_c1_flags_verified"] is True, "I11 bridge missing dynamic flags")
    require(i11_bridge["conditional_only"] is True, "I11 bridge should be conditional")

    require(current_result["returncode"] == 1, "recorded current physical validator should fail")
    require(witness_result["returncode"] == 0, "recorded witness physical validator should pass")
    require(i11_bridge_result["returncode"] == 0, "recorded I11 bridge validator should pass")
    require(validator_returncode(PHYSICAL_VALIDATOR, CURRENT) == 1, "current physical validator should fail")
    require(validator_returncode(PHYSICAL_VALIDATOR, WITNESS) == 0, "witness physical validator should pass")
    require(validator_returncode(I11_VALIDATOR, I11_BRIDGE) == 0, "I11 bridge validator should pass")

    require(frontier["closed_now"]["strict_physical_source_validator_built"] is True, "frontier missing validator")
    require(frontier["route_A_remaining_theorem"]["name"] == "SelectedPhiFinC1PhysicalSourceEmissionTheorem", "wrong Route A theorem")
    require(frontier["route_B_remaining_execution"]["name"] == "SelectedIndependentGalerkinRowsExecution", "wrong Route B execution")
    require(frontier["superset_strategy"]["uses_observed_constants"] is False, "frontier uses observed constants")
    require(data["what_remains_open"]["SelectedPhiFinC1PhysicalSourceEmissionTheorem"] is True, "candidate missing Route A open")
    require(data["what_remains_open"]["SelectedIndependentGalerkinRowsExecution"] is True, "candidate missing Route B open")
    require(cert["conditional_i11_trace_map_bridge_passes"] is True, "cert missing I11 pass")
    require("Route A now requires one theorem-derived" in note, "note missing Route A theorem")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
