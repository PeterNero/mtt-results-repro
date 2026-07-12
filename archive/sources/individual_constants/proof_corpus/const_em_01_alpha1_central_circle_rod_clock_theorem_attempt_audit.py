"""Audit const_em_01_alpha1_central_circle_rod_clock_theorem_attempt."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
BASE = DATA / "const_em_01_alpha1_central_circle_rod_clock_theorem_attempt"
CANDIDATE = DATA / "const_em_01_alpha1_central_circle_rod_clock_theorem_attempt.candidate.json"
SOURCE = BASE / "central_circle_source_read.packet.json"
THEOREM = BASE / "rod_clock_theorem_attempt.packet.json"
PROMOTION = BASE / "promotion_verdict.packet.json"
CERT = ROOT / "certificates" / "const_em_01_alpha1_central_circle_rod_clock_theorem_attempt_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_CONST_EM_01_Alpha1_CentralCircleRodClockTheoremAttempt_v1.md"
BUILD = ROOT / "scripts" / "build_const_em_01_alpha1_central_circle_rod_clock_theorem_attempt.py"
STATUS = "MTT_CONST_EM_01_CENTRAL_CIRCLE_ROD_CLOCK_ATTEMPT_SUPPORT_CLOSED_VALUE_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")
    require(packet.get("closure_claimed") is False, "closure overclaim")


def close(a: float, b: float, tol: float = 1e-14) -> bool:
    return abs(a - b) < tol


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
    source = load(SOURCE)
    theorem = load(THEOREM)
    promotion = load(PROMOTION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "support theorem not proved")
    require(candidate["what_closes_now"]["central_circle_support_for_rod_clock_channel"] is True, "support not closed")
    require(candidate["what_closes_now"]["strict_no_knob_L0_E0_value"] is False, "strict value overclaimed")
    require(candidate["what_closes_now"]["one_primitive_extension_ready"] is True, "one primitive not ready")
    require(candidate["what_remains_open"]["source_selected_L0_or_E0"] is True, "L0/E0 not open")

    require(all(source["source_checks"].values()), "source checks failed")
    require(source["support"]["same_source_candidate_for_L0_E0"] is True, "same-source support missing")
    require(source["limitations"]["interpretive_synthesis_flag"] is True, "interpretive flag missing")
    require(source["limitations"]["absolute_L0_or_E0_value_present"] is False, "absolute value unexpectedly present")

    chain = theorem["dimensionless_chain_replayed"]
    require(close(chain["tau_int"], math.log(448) / 15), "tau mismatch")
    require(close(chain["sqrt_tau_int"], math.sqrt(math.log(448) / 15)), "sqrt tau mismatch")
    require("does not emit a numeric absolute physical value" in theorem["failed_promotion_step"], "promotion failure not explicit")
    require("selected physical L0 or E0 value" in theorem["promotion_conditions_not_met"], "missing promotion condition")

    require(promotion["support_closed"] is True, "promotion support not closed")
    require(promotion["strict_no_knob_L0_E0_value_selected"] is False, "promotion overclaimed")
    require(promotion["one_primitive_extension_still_ready"] is True, "primitive readiness missing")
    require(promotion["recommended_next"]["label"] == "CONST-EM-01 / ALPHA1-PHYSICAL-ANCHOR / A10-UNIVERSAL-PRIMITIVE-OR-NOGO", "next label mismatch")

    require(cert["support_closed"] is True, "cert support not closed")
    require(cert["strict_no_knob_L0_E0_value_selected"] is False, "cert strict value overclaim")
    require(cert["one_primitive_extension_ready"] is True, "cert primitive missing")
    require("strict no-knob physical `alpha_phys` remains open" in note, "note boundary missing")

    for packet in [candidate, source, theorem, promotion, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
