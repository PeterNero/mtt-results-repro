"""Audit universal_crossuse_parameter_admissibility_theorem."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "universal_crossuse_parameter_admissibility_theorem"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
THEOREM = BASE / "crossuse_admissibility_theorem.packet.json"
ALPHA1_CASE = BASE / "alpha1_crossuse_case.packet.json"
PSM_BOUNDARY = BASE / "psm_c1_02_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_UniversalCrossUseParameterAdmissibilityTheorem_v1.md"
BUILD = ROOT / "scripts" / "build_universal_crossuse_parameter_admissibility_theorem.py"
STATUS = "MTT_UNIVERSAL_CROSSUSE_PARAMETER_ADMISSIBILITY_THEOREM_BUILT"


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
    theorem = load(THEOREM)
    alpha1_case = load(ALPHA1_CASE)
    psm_boundary = load(PSM_BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["selected_parameter_count_now"] == 0, "parameter overselected")
    require(candidate["provisional_parameter_admitted_now"] is False, "provisional parameter overadmitted")
    require(candidate["what_closes_now"]["PSM_C1_02_parameter_shortcut_blocked"] is True, "PSM shortcut not blocked")
    require(theorem["admission_criteria"]["shared_across_at_least_two_independent_source_paths"] is True, "cross-use criterion missing")
    require(theorem["admission_criteria"]["one_calibration_makes_rest_predictions"] is True, "prediction criterion missing")
    require(alpha1_case["admitted_now"] is False, "alpha1 overadmitted")
    require(alpha1_case["still_needs_for_B23_admission"]["at_least_two_independent_source_paths_use_same_primitive"] is True, "alpha1 cross-use need missing")
    require(psm_boundary["universal_parameter_shortcut_allowed_now"] is False, "PSM parameter shortcut allowed")
    require(psm_boundary["zero_parameter_route_remains_primary"] is True, "zero-parameter priority missing")
    require(next_work["primary"]["label"] == "UNIV-PARAM / CROSS-USE / B23-ALPHA1-AUDIT", "next label mismatch")
    require(cert["provisional_parameter_admitted_now"] is False, "cert overadmitted")
    require("fitting one calibrating observable converts the rest into predictions" in note, "note theorem missing")

    for packet in [candidate, theorem, alpha1_case, psm_boundary, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
