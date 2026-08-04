"""Audit Route-A physical action proof or Route-B independent row-source table attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_routea_physicalactionidentityproof_or_routeb_independentrowsourcetable"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CURRENT_TABLE = PACKET_DIR / "route_b_current_110_row_source_table_attempt.packet.json"
PROVENANCE = PACKET_DIR / "route_b_row_provenance_audit.packet.json"
SCHEMA = PACKET_DIR / "independent_row_source_table_required_schema.packet.json"
VALIDATION = PACKET_DIR / "two_exit_current_after_table_validator_result.packet.json"
DECISION = PACKET_DIR / "routea_or_routeb_next_decision.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteA_PhysicalActionIdentityProof_or_RouteB_IndependentRowSourceTable_v1.md"

STATUS = "MTT_SELECTED_ROUTEA_ACTIONIDENTITY_OR_ROUTEB_ROWSOURCETABLE_BUILT_TABLE_PROVENANCE_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    proc = subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, text=True, capture_output=True)
    if proc.returncode:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        return proc.returncode

    candidate = load(CANDIDATE)
    table = load(CURRENT_TABLE)
    provenance = load(PROVENANCE)
    schema = load(SCHEMA)
    validation = load(VALIDATION)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "unexpected candidate status")
    require(cert["status"] == STATUS, "unexpected certificate status")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(candidate["target_fitting_used"] is False, "candidate uses target fitting")
    require(table["row_count"] == 110, "Route B table row count mismatch")
    require(table["all_rows_present"] is True, "Route B table shape not complete")
    require(table["independent_source_emitted_count"] == 0, "current rows unexpectedly independent")
    require(table["residual_replay_dependency_count"] == 108, "primitive/sector replay count mismatch")
    require(provenance["passes_independent_source_requirement"] is False, "provenance overpasses")
    require(provenance["failures"]["rows_still_residual_replay_backed"] == 108, "replay failure count mismatch")
    require(provenance["failures"]["rows_without_independent_source_emission"] == 110, "independence failure count mismatch")
    require(schema["required_row_count"] == 110, "replacement schema count mismatch")
    require(schema["row_families"]["primitive_contractions"]["required_count"] == 72, "primitive schema count mismatch")
    require(schema["row_families"]["hessian_source"]["required_count"] == 2, "hessian schema count mismatch")
    require(schema["row_families"]["sector_response"]["required_count"] == 36, "sector schema count mismatch")
    require(validation["ok"] is False and validation["exit_code"] == 1, "strict validator should still reject")
    require(decision["route_B_table_shape_ready"] is True, "decision lost table shape")
    require(decision["route_B_table_independent"] is False, "decision overpromotes Route B")
    require(decision["closure_claimed"] is False, "decision overclaims closure")
    require("complete as a postcheck object" in note, "note missing postcheck distinction")
    require("replacement schema" in note, "note missing next target")

    print(proc.stdout.strip())
    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
