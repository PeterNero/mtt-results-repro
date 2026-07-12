"""Audit the initial individual constants frontier ledger."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "constant_frontier_ledger"
CANDIDATE = DATA / "constant_frontier_ledger.candidate.json"
TARGETS = BASE / "individual_constant_targets.packet.json"
FIRST = BASE / "first_attack_alpha1.packet.json"
UNIV = BASE / "universal_parameter_policy_import.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / "constant_frontier_ledger_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_IndividualConstants_FrontierLedger_v1.md"
BUILD = ROOT / "scripts" / "build_constant_frontier_ledger.py"

STATUS = "MTT_INDIVIDUAL_CONSTANTS_FRONTIER_LEDGER_BUILT_ALPHA1_FIRST"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def main() -> int:
    proc = subprocess.run(
        [sys.executable, str(BUILD)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        print(proc.stdout)
        return 1

    candidate = load(CANDIDATE)
    targets = load(TARGETS)
    first = load(FIRST)
    univ = load(UNIV)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["what_closes_now"]["alpha1_selected_as_first_attack"] is True, "alpha1 not selected first")
    require(candidate["what_remains_open"]["alpha1_value_derivation"] is True, "alpha1 value should remain open")
    require(candidate["recommendation"] == "Attack CONST-EM-01 / ALPHA1-SOURCE-STRENGTH first.", "recommendation mismatch")

    require(targets["targets"][0]["label"] == "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH", "first target mismatch")
    require(targets["targets"][0]["readiness"] == "HIGHEST", "alpha1 readiness mismatch")
    require(all(item["value_claimed_now"] is False for item in targets["targets"]), "target value overclaim")

    require(first["label"] == "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH", "first packet label mismatch")
    require(first["value_claimed_now"] is False, "alpha1 value overclaimed")
    require(first["imported_support"]["sm_parity_universal_policy"] is True, "universal policy not imported")
    require(first["imported_support"]["sm_parity_alpha1_strength_theorem"] is True, "alpha1 strength theorem not found")

    require(univ["source_present"] is True, "universal policy source missing")
    require(univ["selected_parameter_count_now"] == 0, "universal parameter count must start at zero")
    require(next_work["primary"]["label"] == "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH / A1", "next label mismatch")
    require(cert["first_attack"] == "CONST-EM-01 / ALPHA1-SOURCE-STRENGTH", "cert first attack mismatch")
    require("No constant value is claimed here" in note, "note guard missing")

    for packet in [candidate, targets, first, univ, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
