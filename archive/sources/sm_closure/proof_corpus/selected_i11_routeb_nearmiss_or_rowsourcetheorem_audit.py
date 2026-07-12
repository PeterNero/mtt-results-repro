"""Audit selected_i11_routeb_nearmiss_or_rowsourcetheorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_i11_routeb_nearmiss_or_rowsourcetheorem"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
NEARMISS = PACKET_DIR / "route_b_strict_nearmiss.packet.json"
CONDITIONAL_ROUTEB = PACKET_DIR / "conditional_route_b_row_source_witness.packet.json"
I11_CURRENT = PACKET_DIR / "current_i11_after_routeb_nearmiss.packet.json"
I11_WITNESS = PACKET_DIR / "conditional_i11_after_routeb_witness.packet.json"
FRONTIER = PACKET_DIR / "remaining_routeb_rowsource_or_routea_frontier.packet.json"
NEARMISS_RESULT = PACKET_DIR / "route_b_nearmiss_validator_result.packet.json"
ROUTEB_WITNESS_RESULT = PACKET_DIR / "conditional_route_b_validator_result.packet.json"
I11_CURRENT_RESULT = PACKET_DIR / "current_i11_validator_result.packet.json"
I11_WITNESS_RESULT = PACKET_DIR / "conditional_i11_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_I11_RouteBNearMiss_or_RowSourceTheorem_v1.md"
PHYSICAL_VALIDATOR = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"
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
    nearmiss = load(NEARMISS)
    conditional_routeb = load(CONDITIONAL_ROUTEB)
    i11_current = load(I11_CURRENT)
    i11_witness = load(I11_WITNESS)
    frontier = load(FRONTIER)
    nearmiss_result = load(NEARMISS_RESULT)
    routeb_witness_result = load(ROUTEB_WITNESS_RESULT)
    i11_current_result = load(I11_CURRENT_RESULT)
    i11_witness_result = load(I11_WITNESS_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_I11_ROUTEB_NEARMISS_BUILT_ROWSOURCE_THEOREM_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["conditional_only"] is True, "candidate should be conditional")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(nearmiss["proved"] is True, "near-miss should be proved")
    require(nearmiss["route_b_missing_field"] == "source_independent_of_residual_projector_replay", "wrong missing field")
    route_b = nearmiss["strict_packet"]["route_B_independent_execution"]
    require(route_b["selected_basis_independent_of_residual_projector"] is True, "basis independence missing")
    require(route_b["quadrature_rule_independent_of_locked_target"] is True, "quadrature independence missing")
    require(route_b["all_72_primitive_rows_executed"] is True, "72 rows missing")
    require(route_b["formal_110_rows_executed"] is True, "110 rows missing")
    require(route_b["exactness_or_error_certificates_attached"] is True, "exactness missing")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "source independence overpromoted")

    require(conditional_routeb["route_B_independent_execution"]["source_independent_of_residual_projector_replay"] is True, "conditional routeB not filled")
    require(i11_current["c1_response_coordinate_map"] is False, "I11 current overpromoted")
    require(i11_witness["c1_response_coordinate_map"] is True, "I11 witness missing")
    require(nearmiss_result["returncode"] == 1, "near-miss should fail strict validator")
    require(routeb_witness_result["returncode"] == 0, "conditional Route B should pass")
    require(i11_current_result["returncode"] == 1, "current I11 should fail")
    require(i11_witness_result["returncode"] == 0, "conditional I11 should pass")
    require(validator_returncode(PHYSICAL_VALIDATOR, NEARMISS) == 1, "near-miss validator should fail")
    require(validator_returncode(PHYSICAL_VALIDATOR, CONDITIONAL_ROUTEB) == 0, "conditional Route B validator should pass")
    require(validator_returncode(I11_VALIDATOR, I11_CURRENT) == 1, "current I11 validator should fail")
    require(validator_returncode(I11_VALIDATOR, I11_WITNESS) == 0, "conditional I11 validator should pass")
    require(frontier["closed_now"]["route_B_all_72_rows_executed"] is True, "frontier should close 72 rows")
    require(frontier["still_open"]["route_B_missing_field"] == "source_independent_of_residual_projector_replay", "frontier missing wrong field")
    require(cert["route_B_all_other_strict_fields_closed"] is True, "cert should record near-miss")
    require("conditional Route B validates                     = True" in note, "note missing conditional Route B")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
