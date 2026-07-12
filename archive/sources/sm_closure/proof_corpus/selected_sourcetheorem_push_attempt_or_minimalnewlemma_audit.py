"""Audit selected_sourcetheorem_push_attempt_or_minimalnewlemma."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_sourcetheorem_push_attempt_or_minimalnewlemma"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ROUTE_A = PACKET_DIR / "route_a_phifinc1_action_source_theorem_push.packet.json"
ROUTE_B = PACKET_DIR / "route_b_independent_rowkernel_source_theorem_push.packet.json"
LEMMA = PACKET_DIR / "minimal_selected_finitec1_source_promotion_lemma.packet.json"
WITNESS = PACKET_DIR / "conditional_route_b_validator_witness.packet.json"
VALIDATOR_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CURRENT_VALIDATOR_RESULT = PACKET_DIR / "current_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SourceTheorem_PushAttempt_or_MinimalNewLemma_v1.md"
CURRENT = (
    ROOT
    / "candidate_data"
    / "selected_physicalphifinc1action_or_independentrowkernelsource_theorem"
    / "current_two_exit_source_attempt.packet.json"
)
VALIDATOR = ROOT / "scripts" / "validate_selected_physicalphifinc1_action_or_independent_rowkernel_source.py"


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
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    lemma = load(LEMMA)
    witness = load(WITNESS)
    conditional_result = load(VALIDATOR_RESULT)
    current_result = load(CURRENT_VALIDATOR_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_SOURCETHEOREM_PUSH_BUILT_MINIMAL_CONDITIONAL_LEMMA", "status mismatch")
    require(data["theorem"]["proved"] is True, "conditional sufficiency theorem not marked proved")
    require(data["conditional_only"] is True, "candidate must be conditional only")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(route_a["can_validate_now"] is False, "Route A should not validate now")
    require(route_a["closure_claimed"] is False, "Route A closure overclaimed")
    require(route_b["can_validate_now"] is False, "Route B should not validate now")
    require(len(route_b["currently_failed_fields"]) == 5, "Route B failed-field count mismatch")
    require(route_b["closure_claimed"] is False, "Route B closure overclaimed")

    require(lemma["proved_here"] is False, "minimal lemma should not be proved here")
    require(lemma["conditional_only"] is True, "minimal lemma should be conditional")
    require(lemma["sufficient_for_strict_validator"] is True, "minimal lemma should be sufficient")
    require(len(lemma["proof_obligations"]) == 5, "minimal lemma obligation count mismatch")

    route_b_witness = witness["route_B_independent_rowkernel_source"]
    require(route_b_witness["same_branch"] is True, "witness Route B same branch missing")
    require(len(route_b_witness["attached_source_evidence"]) >= 5, "witness evidence count too low")
    require(witness["conditional_only"] is True, "witness should be conditional only")
    require(witness["closure_claimed"] is False, "witness closure overclaimed")

    require(current_result["returncode"] == 1, "recorded current validator should fail")
    require(conditional_result["returncode"] == 0, "recorded conditional validator should pass")
    require(validator_returncode(CURRENT) == 1, "current validator should still fail")
    require(validator_returncode(WITNESS) == 0, "conditional witness should pass")

    require(data["what_closes_now"]["conditional_validator_witness_passes"] is True, "candidate should record passing witness")
    require(data["what_closes_now"]["current_validator_still_fails"] is True, "candidate should record failing current packet")
    require(cert["conditional_validator_witness_passes"] is True, "cert should record passing witness")
    require(cert["current_validator_still_fails"] is True, "cert should record failing current packet")
    require(cert["closure_claimed"] is False, "cert closure overclaimed")
    require("conditional sufficiency" in note, "note missing conditional sufficiency statement")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
