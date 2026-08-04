"""Audit selected_psm_c1_02_localprinciple_routea_validation_or_unpatcheda1aactualsource."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "selected_psm_c1_02_localprinciple_routea_validation_or_unpatcheda1aactualsource"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
LOCAL_PACKET = BASE / "local_principle_route_a_validating_packet.packet.json"
VALIDATION = BASE / "local_principle_route_a_validator_result.packet.json"
BOUNDARY = BASE / "unpatched_a1a_actual_source_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_LocalPrincipleRouteAValidation_or_UnpatchedA1aActualSource_v1.md"
VALIDATOR_SCRIPT = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"
BUILD = ROOT / "scripts" / "build_selected_psm_c1_02_localprinciple_routea_validation_or_unpatcheda1aactualsource.py"

STATUS = "MTT_SELECTED_PSM_C1_02_LOCAL_PRINCIPLE_ROUTE_A_VALIDATES_UNPATCHED_A1A_SOURCE_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard(packet: dict) -> None:
    require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
    require(packet.get("target_fitting_used") is False, "target fitting violation")


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
    packet = load(LOCAL_PACKET)
    validation = load(VALIDATION)
    boundary = load(BOUNDARY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    live = subprocess.run(
        [sys.executable, str(VALIDATOR_SCRIPT), str(LOCAL_PACKET)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem missing")
    require(candidate["what_closes_now"]["local_principle_route_A_strict_validator_pass"] is True, "local Route A did not pass")
    require(candidate["what_remains_open"]["unpatched_SI1u_A1a_actual_physical_action_source"] is True, "unpatched A1a overclosed")
    require(candidate["superset_strategy"]["paths_used_as_free_parameters"] is False, "superset used as knobs")

    route_a = packet["route_A_physical_source_certificate"]
    require(route_a["same_branch"] is True, "local Route A same_branch missing")
    require(route_a["physical_action_restricts_to_selected_finite_Weyl_quotient"] is True, "A1a local field missing")
    require(route_a["no_extra_physical_boundary_or_source_term"] is True, "A1b local field missing")
    require(route_a["phase_R_Z_source_selection"] is True, "R_Z local field missing")
    require(route_a["shift_R_X_source_selection"] is True, "R_X local field missing")
    require(route_a["same_source_b_selected_emission"] is True, "b local field missing")
    require(len(route_a["attached_same_branch_sources"]) >= 5, "source evidence incomplete")
    require(packet["promotion_allowed_now"] is True, "local promotion should be allowed")
    require(packet["unpatched_promotion_allowed_now"] is False, "unpatched promotion overclaimed")

    require(validation["ok"] is True and validation["exit_code"] == 0, "stored validation failed")
    require(live.returncode == 0, "live validation failed")
    require(boundary["local_principle_validates_route_A"] is True, "boundary local pass missing")
    require(boundary["unpatched_principle_derived_now"] is False, "unpatched principle overderived")
    require(boundary["independent_kernel_execution_supplied"] is False, "independent execution overclaimed")
    require(boundary["route_A_accepts_without_local_principle"] is False, "unpatched route A overaccepted")
    require(boundary["route_B_accepts_without_local_principle"] is False, "route B overaccepted")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-UNPATCHED", "next primary mismatch")
    require(next_work["fallback"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2", "fallback mismatch")
    require(cert["local_route_A_validator_pass"] is True, "cert local pass missing")
    require(cert["unpatched_A1a_actual_source_derived_now"] is False, "cert unpatched overderived")
    require(cert["route_B_independent_execution_supplied"] is False, "cert route B overclaimed")
    require("SI-1u-A1a-LOCAL" in note and "SI-1u-A1a-UNPATCHED" in note, "note labels missing")
    require("not knobs" in note, "note superset guard missing")

    for item in [candidate, packet, validation, boundary, cert]:
        guard(item)
        require(item.get("closure_claimed") is False, "closure overclaim")

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
