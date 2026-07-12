"""Audit selected_physicalsourcecertificatefill_or_routebindependentrunexecution."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "selected_physicalsourcecertificatefill_or_routebindependentrunexecution.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / "selected_physicalsourcecertificatefill_or_routebindependentrunexecution"
ATTEMPT = PACKET_DIR / "current_fill_attempt.packet.json"
VALIDATOR_PACKET = PACKET_DIR / "promotion_acceptance_validator.packet.json"
CERT = ROOT / "certificates" / "selected_physicalsourcecertificatefill_or_routebindependentrunexecution_certificate.json"
VALIDATOR_SCRIPT = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhysicalSourceCertificateFill_or_RouteBIndependentRunExecution_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    attempt = load(ATTEMPT)
    validator = load(VALIDATOR_PACKET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR_SCRIPT), str(ATTEMPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == "MTT_SELECTED_PHYSICALSOURCECERTIFICATEFILL_OR_ROUTEBINDEPENDENTRUNEXECUTION_BUILT_STRICT_VALIDATOR_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["decision"]["strict_validator_built"] is True, "validator not built")
    require(data["decision"]["strict_validator_accepts_current_attempt"] is False, "attempt unexpectedly accepted")
    require(attempt["promotion_allowed_now"] is False, "attempt overpromoted")
    require(proc.returncode == 1, "validator should reject current attempt")
    require(any("neither Route A nor Route B validates" in line for line in proc.stderr.splitlines()), "missing rejection reason")
    require(validator["current_attempt_rejected_as_expected"] is True, "validator packet mismatch")
    require(cert["current_attempt_rejected_as_expected"] is True, "cert mismatch")
    require(cert["route_A_filled_now"] is False, "Route A overfilled")
    require(cert["route_B_executed_now"] is False, "Route B overexecuted")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")
    require("hard acceptance gate" in note, "note missing validator role")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
