"""Audit independent quadrature rule/Hessian b-source derivation attempt."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_independentquadratureruleandhessianbsource_or_routeaactionidentity"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DERIVATION = PACKET_DIR / "derivation_attempt.packet.json"
PARTIAL_VALIDATION = PACKET_DIR / "partial_measure_quadrature_source_id_validator_result.packet.json"
CONDITIONAL_VALIDATION = PACKET_DIR / "conditional_source_identity_validator_result.packet.json"
OBSTRUCTION = PACKET_DIR / "remaining_derivation_obstruction.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_IndependentQuadratureRuleAndHessianBSource_or_RouteAActionIdentity_v1.md"

STATUS = "MTT_SELECTED_INDEPENDENT_QUADRATURE_RULE_AND_HESSIAN_BSOURCE_DERIVATION_ATTEMPT_REDUCED_TO_SOURCE_IDENTITY"


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
    derivation = load(DERIVATION)
    partial = load(PARTIAL_VALIDATION)
    conditional = load(CONDITIONAL_VALIDATION)
    obstruction = load(OBSTRUCTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "unexpected candidate status")
    require(cert["status"] == STATUS, "unexpected certificate status")
    require(candidate["closure_claimed"] is False, "candidate overclaims closure")
    require(candidate["target_fitting_used"] is False, "candidate uses target fitting")
    result = derivation["derivation_result"]
    require(result["selected_measure_pairing_as_source"] is False, "measure overpromoted")
    require(result["selected_independent_quadrature_rule_as_source"] is False, "quadrature overpromoted")
    require(result["selected_hessian_b_source"] is False, "hessian/b overpromoted")
    require(partial["ok"] is False and partial["exit_code"] == 1, "partial packet should fail")
    require(
        any("theorem_derived must be true" in line for line in partial["stderr"]),
        "partial failure should be theorem-derived gate",
    )
    require(conditional["ok"] is True, "conditional source identity witness should pass")
    require(obstruction["partial_validator_ok"] is False, "obstruction should keep partial open")
    require(obstruction["conditional_validator_ok"] is True, "obstruction should keep conditional pass")
    require("SelectedFiniteC1SourceIdentityTheorem" in obstruction["minimal_missing_clause_family"]["name"], "wrong missing theorem")
    require("does not yet derive" in note, "note missing failed derivation")
    require("conditional witness" in note, "note missing conditional witness")

    print(proc.stdout.strip())
    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
