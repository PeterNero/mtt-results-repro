"""Audit selected_psm_c1_02_unpatcheda1a_sourcecutset_or_routeb_rowsource."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "selected_psm_c1_02_unpatcheda1a_sourcecutset_or_routeb_rowsource"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
ROUTE_A = BASE / "route_a_unpatched_boundary_firstvariation_cutset.packet.json"
ROUTE_B = BASE / "route_b_row_source_independence_cutset.packet.json"
DUAL = BASE / "dual_validator_replay.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_UnpatchedA1aSourceCutset_or_RouteBRowSource_v1.md"
BUILD = ROOT / "scripts" / "build_selected_psm_c1_02_unpatcheda1a_sourcecutset_or_routeb_rowsource.py"

STATUS = "MTT_SELECTED_PSM_C1_02_UNPATCHED_A1A_CUTSET_REDUCED_TO_BOUNDARY_FIRSTVARIATION_OR_ROUTEB_ROWSOURCE"


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
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    dual = load(DUAL)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["active_routes"] == ["SOURCE-IDENTITY/SI-1u-A1a-UNPATCHED-I11", "SOURCE-IDENTITY/SI-1u-B2-ROWSOURCE"], "routes mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem missing")
    require(candidate["superset_strategy"]["paths_used_as_free_parameters"] is False, "superset used as knobs")

    require(route_a["status"] == "ROUTE_A_UNPATCHED_REDUCED_TO_THREE_PHYSICAL_SOURCE_FIELDS", "route A status mismatch")
    require(route_a["current_i10_rejected"] is True, "current I10 should reject")
    require(route_a["conditional_i10_passes"] is True, "conditional I10 should pass")
    require(route_a["unpatched_route_A_closed_now"] is False, "route A overclosed")
    remaining = route_a["remaining_physical_fields"]
    require(set(remaining.keys()) == {"physical_boundary_cancellation", "physical_first_variation_identity", "same_source_RZ_RX_bselected_emission"}, "route A cutset mismatch")

    require(route_b["status"] == "ROUTE_B_REDUCED_TO_ROW_SOURCE_INDEPENDENCE", "route B status mismatch")
    require(route_b["route_b_missing_field"] == "source_independent_of_residual_projector_replay", "route B missing field mismatch")
    require(route_b["selected_basis_independent_of_residual_projector"] is True, "basis independence missing")
    require(route_b["quadrature_rule_independent_of_locked_target"] is True, "quadrature independence missing")
    require(route_b["all_72_primitive_rows_executed"] is True, "72 rows missing")
    require(route_b["formal_110_rows_executed"] is True, "110 rows missing")
    require(route_b["exactness_or_error_certificates_attached"] is True, "exactness missing")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "route B overclosed")
    require(route_b["route_b_physicalsource_validator_rejects_now"] is True, "route B should reject")

    require(dual["current_route_A_rejects"] is True, "dual route A should reject")
    require(dual["conditional_route_A_passes"] is True, "dual conditional route A should pass")
    require(dual["current_route_B_rejects"] is True, "dual route B should reject")

    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-A1a-UNPATCHED-I11", "next primary mismatch")
    require(next_work["fallback"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2-ROWSOURCE", "fallback mismatch")
    require(cert["route_A_current_rejects"] is True, "cert route A current mismatch")
    require(cert["route_A_conditional_passes"] is True, "cert route A conditional mismatch")
    require(cert["route_B_current_rejects"] is True, "cert route B mismatch")
    require("SI-1u-A1a-UNPATCHED-I11" in note and "SI-1u-B2-ROWSOURCE" in note, "note labels missing")

    for item in [candidate, route_a, route_b, dual, cert]:
        guard(item)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
