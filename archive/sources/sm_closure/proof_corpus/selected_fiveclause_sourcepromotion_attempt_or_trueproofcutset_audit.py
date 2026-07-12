"""Audit selected_fiveclause_sourcepromotion_attempt_or_trueproofcutset."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_fiveclause_sourcepromotion_attempt_or_trueproofcutset"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ATTEMPT = PACKET_DIR / "five_clause_source_promotion_attempt.packet.json"
CUTSET = PACKET_DIR / "true_proof_cutset.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "strict_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_finitec1_rowkernel_functional_packet.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FiveClause_SourcePromotionAttempt_or_TrueProofCutset_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    attempt = load(ATTEMPT)
    cutset = load(CUTSET)
    validator_result = load(VALIDATOR_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(ATTEMPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "MTT_SELECTED_FIVECLAUSE_SOURCEPROMOTION_ATTEMPT_BUILT_TRUEPROOFCUTSET_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "cutset theorem not proved")
    require(attempt["promotion_attempt"]["all_closed_support_imported"] is True, "support not imported")
    require(attempt["promotion_attempt"]["any_source_clause_promoted_now"] is False, "source clause overpromoted")
    require(attempt["promotion_attempt"]["source_clause_open_count"] == 5, "wrong open clause count")
    require(cutset["closed_support_not_blocking"]["all_110_values"] is True, "110 values not closed")
    require(cutset["closed_support_not_blocking"]["finite_trace_measure_normalization"] is True, "measure support missing")
    require(cutset["legal_exit_A"]["name"] == "physical Phi_fin^C1 action restriction theorem", "wrong Route A exit")
    require(cutset["legal_exit_B"]["name"] == "independent row-kernel source theorem", "wrong Route B exit")
    require(proc.returncode == 1, "validator should reject promotion attempt")
    require(validator_result["returncode"] == 1, "recorded validator should reject")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(cert["validator_rejects_promotion_attempt"] is True, "cert should record rejection")
    require("two legal exits" in note, "note missing legal exits")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
