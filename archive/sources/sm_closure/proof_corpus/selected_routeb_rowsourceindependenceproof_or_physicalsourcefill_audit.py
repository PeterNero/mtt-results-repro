"""Audit selected_routeb_rowsourceindependenceproof_or_physicalsourcefill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill"
ATTEMPT = PACKET_DIR / "current_row_source_independence_attempt.packet.json"
DECISION = PACKET_DIR / "final_routeb_or_routea_decision.packet.json"
CERT = ROOT / "certificates" / "selected_routeb_rowsourceindependenceproof_or_physicalsourcefill_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_rowsource_independence.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteBRowSourceIndependenceProof_or_PhysicalSourceFill_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    attempt = load(ATTEMPT)
    decision = load(DECISION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(ATTEMPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "MTT_SELECTED_ROUTEB_ROWSOURCEINDEPENDENCEPROOF_BUILT_FINAL_SOURCE_TARGET_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(attempt["finite_weyl_trace_rule_feeds_all_rows"] is True, "trace rule not closed")
    require(attempt["sector_rows_assembled_from_primitive_rows"] is True, "sector rows not closed")
    require(attempt["hessian_source_rows_assembled_from_same_rows"] is True, "hessian rows not closed")
    require(attempt["selected_basis_feeds_72_primitive_rows"] is False, "basis-row source overclosed")
    require(attempt["no_residual_projector_replay_used_as_source"] is False, "residual source overclosed")
    require(attempt["row_formula_source_theorem_derived"] is False, "row formula theorem overclosed")
    require(attempt["source_independent_of_residual_projector_replay"] is False, "source independence overclosed")
    require(proc.returncode == 1, "validator should reject current attempt")
    require(any("source_independent_of_residual_projector_replay is not true" in line for line in proc.stderr.splitlines()), "missing source rejection")
    require(decision["route_B_all_other_strict_fields_closed"] is True, "not all other Route B fields closed")
    require(decision["route_B_promoted_now"] is False, "Route B overpromoted")
    require(cert["row_source_validator_built"] is True, "cert missing validator")
    require(cert["source_independence_closed"] is False, "cert source overclosed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("current attempt is rejected" in note, "note missing guardrail")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
