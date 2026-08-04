"""Audit selected_i11_physicalsource_valueclosure_or_fiveclausegap."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_i11_physicalsource_valueclosure_or_fiveclausegap"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
VALUE = PACKET_DIR / "canonical_residual_bvalue_closure_sublemma.packet.json"
CURRENT = PACKET_DIR / "current_physical_source_valueclosure_trace_map_attempt.packet.json"
WITNESS = PACKET_DIR / "conditional_fiveclause_physical_source_witness.packet.json"
FRONTIER = PACKET_DIR / "remaining_five_physical_clause_frontier.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_I11_PhysicalSourceValueClosure_or_FiveClauseGap_v1.md"
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
    value = load(VALUE)
    current = load(CURRENT)
    witness = load(WITNESS)
    frontier = load(FRONTIER)
    current_result = load(CURRENT_RESULT)
    witness_result = load(WITNESS_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_I11_PHYSICALSOURCE_VALUES_CLOSED_FIVE_CLAUSES_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["conditional_only"] is True, "candidate should be conditional")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(value["proved"] is True, "value sublemma should be proved")
    require(value["R_Z"]["reconstruction_error_norm_sq"] < 1e-24, "R_Z not exact enough")
    require(value["R_X"]["reconstruction_error_norm_sq"] < 1e-24, "R_X not exact enough")
    require(value["b_selected_replay"]["same_source_emitted"] is False, "b_selected overpromoted")
    require(current["canonical_residual_values_closed"] is True, "residual values should close")
    require(current["b_selected_replay_fixed"] is True, "b replay target should close")
    require(current["five_physical_clauses_open"] is True, "five clauses should remain open")
    require(current["c1_response_coordinate_map"] is False, "coordinate source overpromoted")
    require(current["selected_normalization_boundary_clause"] is False, "boundary overpromoted")
    require(current["dynamic_c1_flags_verified"] is False, "dynamic flags overpromoted")
    require(current["free_axiom_patch_used"] is False, "free patch used")

    require(witness["conditional_only"] is True, "witness should be conditional")
    require(current_result["returncode"] == 1, "recorded current validator should fail")
    require(witness_result["returncode"] == 0, "recorded witness validator should pass")
    require(validator_returncode(CURRENT) == 1, "current validator should fail")
    require(validator_returncode(WITNESS) == 0, "witness validator should pass")

    require(frontier["closed_now"]["canonical_R_Z_R_X_values"] is True, "frontier should close residual values")
    require(frontier["closed_now"]["b_selected_replay_target"] is True, "frontier should close b replay")
    require(len(frontier["still_open"]["five_physical_clauses"]) == 5, "five physical clauses expected")
    require(frontier["still_open"]["route_b_independent_galerkin_replacement"]["independent_rows_executed_now"] is False, "Route B overpromoted")
    require(cert["canonical_residual_values_closed"] is True, "cert should record residual values")
    require("R_Z and R_X canonical values = True" in note, "note missing value closure")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
