"""Audit const_ew_02_weak_mixing_common_anchor_obstruction."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_ew_02_weak_mixing_common_anchor_obstruction"
CANDIDATE = DATA / "const_ew_02_weak_mixing_common_anchor_obstruction.candidate.json"
DERIVATION = BASE / "ratio_from_difference_derivation.packet.json"
ANCHOR_TEST = BASE / "common_anchor_selection_test.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / "const_ew_02_weak_mixing_common_anchor_obstruction_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EW_02_WeakMixing_CommonAnchorObstruction_v1.md"
BUILD = ROOT / "scripts" / "build_const_ew_02_weak_mixing_common_anchor_obstruction.py"
STATUS = "MTT_CONST_EW_02_COMMON_ANCHOR_OBSTRUCTION_PROVED_VALUE_OPEN"


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
    derivation = load(DERIVATION)
    anchor_test = load(ANCHOR_TEST)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem not proved")
    require(candidate["what_closes_now"]["difference_data_insufficient_for_ratio_theorem"] is True, "obstruction not closed")
    require(candidate["what_closes_now"]["common_anchor_A0_identified_as_required_object"] is True, "A0 not identified")
    require(candidate["what_remains_open"]["numerical_sin2thetaW_prediction"] is True, "numerical angle closed too early")

    require(derivation["status"] == "DIFFERENCE_DATA_DOES_NOT_SELECT_RATIO", "derivation status mismatch")
    require(derivation["algebra"]["one_parameter_family"] == "s2W(A0,D)=(A0-D/2)/(2*A0)", "one-parameter formula mismatch")
    witness = derivation["sample_nonuniqueness_witness"]
    require(len(witness) == 4, "nonuniqueness witness size mismatch")
    require(len({round(row["s2_from_centered_internal_lambda12"], 12) for row in witness}) == 4, "lambda witness not varying")
    require(derivation["proof_result"].startswith("The weak-split packet fixes a difference class"), "proof result missing")

    require(anchor_test["status"] == "COMMON_ANCHOR_NOT_SELECTED_BY_CURRENT_SOURCE", "anchor test status mismatch")
    require(anchor_test["strict_no_knob_tests"]["same_branch_A0_packet_exists"] is False, "A0 packet closed too early")
    require(anchor_test["one_primitive_lane"]["not_no_knob_closure"] is True, "primitive lane overclaimed")

    require(next_work["primary"]["label"] == "CONST-EW-02 / WEAK-MIXING / B5-A0-SOURCE-SEARCH", "next primary mismatch")
    require("weak split" in next_work["source_terms_to_search"], "search term missing")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["A0_source_closed"] is False, "cert A0 overclaim")
    require(cert["physical_sin2thetaW_value_claimed"] is False, "cert angle overclaim")
    require("one-parameter family" in note, "note theorem missing")
    require("B5-A0-SOURCE-SEARCH" in note, "note next label missing")

    for packet in [candidate, derivation, anchor_test, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
