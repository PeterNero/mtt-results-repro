"""Audit selected_finitec1_rowkernelfunctional_candidate_or_sourceclausefailure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finitec1_rowkernelfunctional_candidate_or_sourceclausefailure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PACKET = PACKET_DIR / "finite_c1_rowkernel_functional_candidate.packet.json"
CLAUSES = PACKET_DIR / "source_clause_failure_certificate.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "strict_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_finitec1_rowkernel_functional_packet.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiniteC1_RowKernelFunctional_Candidate_or_SourceClauseFailure_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    packet = load(PACKET)
    clauses = load(CLAUSES)
    validator_result = load(VALIDATOR_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(PACKET)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "MTT_SELECTED_FINITEC1_ROWKERNELFUNCTIONAL_CANDIDATE_BUILT_SOURCE_CLAUSES_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "candidate failure theorem not proved")
    require(packet["row_values"]["counts"]["primitive"] == 72, "primitive count mismatch")
    require(packet["row_values"]["counts"]["hessian"] == 2, "hessian count mismatch")
    require(packet["row_values"]["counts"]["sector"] == 36, "sector count mismatch")
    require(packet["row_values"]["values_filled"] is True, "values should be filled")
    require(packet["row_values"]["values_promoted_as_source"] is False, "values overpromoted")
    require(all(node["source_emitted"] is False for node in packet["source_clauses"].values()), "source clause overemitted")
    require(clauses["validator_rejects_candidate_packet"] is True, "clause certificate should reject")
    require(proc.returncode == 1, "strict validator should reject candidate packet")
    require(validator_result["returncode"] == 1, "recorded validator result should reject")
    require(validator_result["source_clause_errors"] == 5, "expected five source clause errors")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(cert["validator_rejects_candidate_packet"] is True, "cert should record rejection")
    require("filled candidate object" in note, "note missing candidate statement")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
