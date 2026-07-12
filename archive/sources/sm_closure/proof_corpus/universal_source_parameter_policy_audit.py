"""Audit universal_source_parameter_policy."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "universal_source_parameter_policy"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
POLICY = BASE / "universal_source_parameter_policy.packet.json"
CANDIDATES = BASE / "candidate_universal_parameters.packet.json"
GATES = BASE / "current_gate_mapping.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_UniversalSourceParameterPolicy_v1.md"
BUILD = ROOT / "scripts" / "build_universal_source_parameter_policy.py"
STATUS = "MTT_UNIVERSAL_SOURCE_PARAMETER_POLICY_BUILT_NO_PARAMETERS_SELECTED"


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
    policy = load(POLICY)
    candidates = load(CANDIDATES)
    gates = load(GATES)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["selected_parameter_count_now"] == 0, "selected parameter count must be zero")
    require(candidate["maximum_live_universal_parameters"] == 3, "max parameter count mismatch")
    require(candidate["theorem"]["proved"] is True, "policy theorem missing")
    require(candidate["what_closes_now"]["minimal_universal_parameter_tier_named"] is True, "tier not named")
    require(candidate["what_remains_open"]["select_any_universal_parameter"] is True, "selection should remain open")

    require(policy["label"] == "UNIV-PARAM / SOURCE-ANCHOR / UP-0", "policy label mismatch")
    require(policy["tiers"]["NO_KNOB_IDEAL"]["status"] == "PREFERRED_STRONGEST_TARGET", "no-knob tier mismatch")
    require(policy["tiers"]["ORDINARY_FITTED_KNOBS"]["status"] == "FORBIDDEN_AS_SOURCE_PROOF", "fitted knob tier mismatch")
    require(policy["maximum_live_universal_parameters"] == 3, "policy max mismatch")
    require(len(policy["admissibility_rules"]) >= 7, "admissibility rules incomplete")

    require(candidates["selected_parameter_count_now"] == 0, "candidate packet selected parameter")
    require(len(candidates["candidate_classes"]) == 5, "candidate class count mismatch")
    require(all(item["selected_now"] is False for item in candidates["candidate_classes"]), "candidate class overselected")

    require(gates["gate_mapping"]["PSM-C1-02 / SOURCE-IDENTITY / VPB-1-UNPATCHED"]["parameter_allowed_to_close_now"] is False, "PSM gate should not allow parameter closure now")
    require("UP-ABS-SCALE" in gates["gate_mapping"]["dimensionful absolute normalization"]["possible_universal_parameter_if_needed"], "absolute scale candidate missing")
    require(next_work["primary"]["label"] == "UNIV-PARAM / SOURCE-ANCHOR / UP-1", "next label mismatch")
    require(cert["selected_parameter_count_now"] == 0, "cert selected parameter count mismatch")
    require("No universal parameter is selected here" in note, "note guard missing")
    require("not fitted knobs" in note, "note fitted knob guard missing")

    for packet in [candidate, policy, candidates, gates, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
