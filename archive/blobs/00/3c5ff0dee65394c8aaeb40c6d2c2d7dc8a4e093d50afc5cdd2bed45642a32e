"""Audit selected_i11firstvariationcertificate_fill_or_quadraturetable."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_i11firstvariationcertificate_fill_or_quadraturetable"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TEMPLATE = PACKET_DIR / "i11_first_variation_certificate.strict_template.json"
CURRENT = PACKET_DIR / "current_i11_first_variation_certificate_attempt.packet.json"
NORMALIZATION = PACKET_DIR / "normalization_compatibility_sublemma.packet.json"
WITNESS = PACKET_DIR / "conditional_i11_certificate_witness.packet.json"
FRONTIER = PACKET_DIR / "remaining_i11_first_variation_frontier.packet.json"
I10_BRIDGE = PACKET_DIR / "conditional_i10_binding_bridge.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_validator_result.packet.json"
WITNESS_RESULT = PACKET_DIR / "conditional_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_I11FirstVariationCertificate_Fill_or_QuadratureTable_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_i11_firstvariation_certificate.py"


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
    template = load(TEMPLATE)
    current = load(CURRENT)
    norm = load(NORMALIZATION)
    witness = load(WITNESS)
    frontier = load(FRONTIER)
    i10_bridge = load(I10_BRIDGE)
    current_result = load(CURRENT_RESULT)
    witness_result = load(WITNESS_RESULT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == "MTT_SELECTED_I11FIRSTVARIATIONCERTIFICATE_FILL_BUILT_NORMALIZATION_CLOSED_REST_OPEN", "status mismatch")
    require(data["theorem"]["proved"] is True, "frontier theorem not proved")
    require(data["conditional_only"] is True, "candidate should be conditional")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(len(template["required_fields"]) == 5, "template field count mismatch")
    require(norm["proved"] is True, "normalization sublemma should be proved")
    require(current["normalization_compatibility"] is True, "current should close normalization")
    require(current["selected_trace_map"] is False, "selected trace map overpromoted")
    require(current["first_variation_identity"] is False, "first variation overpromoted")
    require(current["hessian_or_coercivity"] is False, "coercivity overpromoted")
    require(current["boundary_cancellation"] is False, "boundary overpromoted")
    require(current["free_axiom_patch_used"] is False, "free patch used")

    for field in template["required_fields"]:
        require(witness[field] is True, f"witness missing {field}")
    require(witness["conditional_only"] is True, "witness should be conditional")
    require(current_result["returncode"] == 1, "recorded current validator should fail")
    require(witness_result["returncode"] == 0, "recorded witness validator should pass")
    require(validator_returncode(CURRENT) == 1, "current validator should fail")
    require(validator_returncode(WITNESS) == 0, "witness validator should pass")

    require(len(frontier["still_open"]) == 4, "four I11 fields should remain open")
    require(frontier["closed_now"]["normalization_compatibility"] is True, "frontier should close normalization")
    require(i10_bridge["validation_returncode"] == 0, "I10 bridge should validate conditionally")
    require(cert["normalization_compatibility_proved"] is True, "cert should record normalization")
    require(cert["current_attempt_rejected"] is True, "cert should record rejection")
    require(cert["conditional_witness_passes"] is True, "cert should record witness")
    require("normalization compatibility proved = True" in note, "note missing normalization statement")
    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
