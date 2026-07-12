"""Audit PSM-C1-02 physical boundary/first-variation or Route-B row-source gate."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "selected_psm_c1_02_physicalboundaryfirstvariation_or_routebrowsourceindependence"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
ROUTE_A = BASE / "route_a_i11_boundary_firstvariation_replay.packet.json"
ROUTE_B = BASE / "route_b_rowsource_independence_replay.packet.json"
COMMON = BASE / "common_source_promotion_final_obstruction.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_PhysicalBoundaryFirstVariation_or_RouteBRowSourceIndependence_v1.md"
BUILD = ROOT / "scripts" / "build_selected_psm_c1_02_physicalboundaryfirstvariation_or_routebrowsourceindependence.py"

STATUS = (
    "MTT_SELECTED_PSM_C1_02_PHYSICALBOUNDARYFIRSTVARIATION_OR_ROUTEBROWSOURCEINDEPENDENCE_"
    "BUILT_FINAL_UNPATCHED_SOURCE_GATE_OPEN"
)
NEXT = "MTT_Selected_PSM_C1_02_RouteA_SelectedPhiFinC1SourceEmission_or_RouteB_ActualRowSourceIndependenceFill_v1"


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
    common = load(COMMON)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem missing")
    require(candidate["closure_decision"]["SM_parity_closed_under_declared_standard"] is True, "SM parity boundary missing")
    require(candidate["closure_decision"]["local_principle_route_A_validates"] is True, "local route should validate")
    require(candidate["closure_decision"]["route_A_unpatched_closed"] is False, "route A overclosed")
    require(candidate["closure_decision"]["route_B_row_source_independence_closed"] is False, "route B overclosed")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(candidate["superset_strategy"]["paths_used_as_free_parameters"] is False, "superset used as knobs")

    require(route_a["status"] == "ROUTE_A_I11_BOUNDARY_FIRSTVARIATION_REPLAYED_SOURCE_EMISSION_OPEN", "route A status mismatch")
    require(route_a["current_physical_source_validator_rejects"] is True, "route A current should reject")
    require(route_a["conditional_physical_source_witness_validates"] is True, "route A conditional should pass")
    require(route_a["local_principle_route_A_validates"] is True, "local route A not imported")
    require(route_a["local_principle_is_unpatched_proof"] is False, "local route overpromoted")
    require(route_a["route_A_unpatched_closed_now"] is False, "route A overclosed")
    require(len(route_a["required_unpatched_source_fields"]) == 6, "route A six-field target mismatch")

    require(route_b["status"] == "ROUTE_B_FINAL_ROW_SOURCE_INDEPENDENCE_GATE_REPLAYED_OPEN", "route B status mismatch")
    require(route_b["strict_row_source_validator_built"] is True, "route B validator missing")
    require(route_b["route_B_all_other_strict_fields_closed"] is True, "route B strict fields missing")
    require(route_b["remaining_route_B_field"] == "source_independent_of_residual_projector_replay", "route B field mismatch")
    require(route_b["route_B_promoted_now"] is False, "route B overpromoted")
    require(route_b["current_attempt_validates"] is False, "route B current should fail")

    require(common["SM_parity_remains_closed"] is True, "common SM parity boundary missing")
    require(common["local_principle_counts_as_true_no_knob"] is False, "local route overclaimed no-knob")
    require(common["unpatched_source_promotion_closed"] is False, "common overclosed")
    require(common["route_A_final_theorem"]["conditional_witness_validates"] is True, "common route A conditional missing")
    require(common["route_B_final_theorem"]["only_open_field"] == "source_independent_of_residual_projector_replay", "common route B field mismatch")
    require(common["superset_policy"]["paths_used_as_free_parameters"] is False, "common superset knob violation")

    require(next_work["next_required_artifact"] == NEXT, "next work mismatch")
    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / ROUTE-A-FINAL", "next primary mismatch")
    require(next_work["fallback"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / ROUTE-B-FINAL", "next fallback mismatch")

    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["route_A_current_rejects"] is True, "cert route A current mismatch")
    require(cert["route_A_conditional_passes"] is True, "cert route A conditional mismatch")
    require(cert["route_B_all_other_strict_fields_closed"] is True, "cert route B fields mismatch")
    require(cert["route_B_row_source_independence_closed"] is False, "cert route B overclosed")
    require("SelectedPhiFinC1PhysicalSourceEmissionTheorem" in note, "note missing route A theorem")
    require("SelectedFiniteC1RowSourceIndependenceTheorem" in note, "note missing route B theorem")

    for packet in [candidate, route_a, route_b, common, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
