"""Audit selected_psm_c1_02_physicalsourcecertificatefill_or_routebindependentrunexecution."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "selected_psm_c1_02_physicalsourcecertificatefill_or_routebindependentrunexecution"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
PROBE = BASE / "route_a_a1a_physical_action_restriction_source_probe.packet.json"
VALIDATOR_REPLAY = BASE / "strict_route_a_route_b_validator_replay.packet.json"
ROUTE_B_READY = BASE / "route_b_replacement_readiness.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_PhysicalSourceCertificateFill_or_RouteBIndependentRunExecution_v1.md"
VALIDATOR_SCRIPT = ROOT / "scripts" / "validate_selected_physicalsourcecertificate_or_routeb.py"
STRICT_FILL = DATA / "selected_physicalsourcecertificatefill_or_routebindependentrunexecution" / "current_fill_attempt.packet.json"
BUILD = ROOT / "scripts" / "build_selected_psm_c1_02_physicalsourcecertificatefill_or_routebindependentrunexecution.py"

STATUS = "MTT_SELECTED_PSM_C1_02_SI1U_A1A_PHYSICAL_ACTION_RESTRICTION_SOURCE_PROBED_STRICT_VALIDATOR_OPEN"


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
    probe = load(PROBE)
    replay = load(VALIDATOR_REPLAY)
    route_b = load(ROUTE_B_READY)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    validator_proc = subprocess.run(
        [sys.executable, str(VALIDATOR_SCRIPT), str(STRICT_FILL)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_routes"] == ["SOURCE-IDENTITY/SI-1u-A1a", "SOURCE-IDENTITY/SI-1u-B2"], "routes mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem missing")
    require(candidate["superset_strategy"]["not_knobs"] is True, "superset guard missing")

    require(probe["status"] == "SI1U_A1A_SUPPORT_ONLY_PROBED_PHYSICAL_SOURCE_NOT_FILLED", "probe status mismatch")
    require(all(probe["closed_support"].values()), "closed support should all be true")
    require(probe["accepted_same_branch_sources_found"] == [], "unexpected same-branch source")
    require(probe["same_branch_physical_action_restriction_emitted"] is False, "A1a overfilled")
    require(probe["field_filled_now"] is False, "field filled unexpectedly")
    require(probe["support_only_not_sufficient"] is True, "support-only guard missing")

    require(replay["exit_code"] == 1, "validator replay should reject")
    require(replay["ok"] is False, "validator replay unexpectedly ok")
    require(any("physical_action_restricts_to_selected_finite_Weyl_quotient" in line for line in replay["stderr"]), "missing A1a validator error")
    require(validator_proc.returncode == 1, "live validator should reject")

    require(route_b["all_72_primitive_rows_executed"] is True, "route B rows missing")
    require(route_b["formal_110_rows_executed"] is True, "route B formal replay missing")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "route B source independence overclaimed")
    require(route_b["exactness_or_error_certificates_attached"] is False, "route B exactness overclaimed")
    require(route_b["ready_now"] is False, "route B overready")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-ACTUAL", "next primary mismatch")
    require(next_work["fallback"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2", "fallback mismatch")

    require(cert["strict_validator_rejects_current_packet"] is True, "cert validator mismatch")
    require(cert["SI1u_A1a_field_filled_now"] is False, "cert overfilled")
    require(cert["route_B_ready_now"] is False, "cert route B overready")
    require("Status label: `PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a`" in note, "note label missing")
    require("not knobs" in note, "note superset guard missing")

    for packet in [candidate, probe, replay, route_b, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
