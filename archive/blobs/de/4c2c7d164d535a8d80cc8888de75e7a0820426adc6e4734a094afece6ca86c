"""Audit selected_routeb_bestcurrentpayloadfill_or_independentsourcegap."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_routeb_bestcurrentpayloadfill_or_independentsourcegap"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ATTEMPT = PACKET_DIR / "routeb_best_current_payload_fill_attempt.packet.json"
GAP = PACKET_DIR / "routeb_independent_source_gap.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "strict_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
VALIDATOR = ROOT / "scripts" / "validate_selected_routeb_independent_quadrature_payload.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_RouteB_BestCurrentPayloadFill_or_IndependentSourceGap_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    attempt = load(ATTEMPT)
    gap = load(GAP)
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

    require(data["status"] == "MTT_SELECTED_ROUTEB_BESTCURRENTPAYLOADFILL_BUILT_INDEPENDENTSOURCE_GAP_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "source-gap theorem not proved")
    require(attempt["row_count"] == 110, "attempt row count mismatch")
    require(attempt["support_imported"]["primitive_replay_rows"] == 72, "primitive replay count mismatch")
    require(attempt["support_imported"]["independent_primitive_rows"] == 0, "independent primitive count should remain zero")
    require(gap["current_support"]["all_110_rows_present"] is True, "110 row support not present")
    require(gap["current_support"]["formal_hessian_target_present"] is True, "formal Hessian target missing")
    require(gap["validator_rejects_best_current_fill"] is True, "gap should record rejection")
    require(proc.returncode == 1, "strict validator should reject best current fill")
    require(validator_result["returncode"] == 1, "recorded validator result should reject")
    require(validator_result["independent_source_errors"] >= 110, "expected source errors missing")
    require(data["validator_rejects_best_current_fill"] is True, "candidate should record rejection")
    require(cert["validator_rejects_best_current_fill"] is True, "cert should record rejection")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("not row enumeration or target linear algebra" in note, "note missing frontier statement")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
