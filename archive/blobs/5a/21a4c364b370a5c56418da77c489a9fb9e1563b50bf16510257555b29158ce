"""Audit PSM-C1-02 final Route-A source emission / Route-B row-source fill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "selected_psm_c1_02_routea_selectedphifinc1sourceemission_or_routeb_actualrowsourceindependencefill"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
ROUTE_A = BASE / "route_a_selected_phifinc1_source_emission_attempt.packet.json"
ROUTE_B = BASE / "route_b_actual_row_source_independence_attempt.packet.json"
FINAL = BASE / "final_unpatched_source_promotion_decision.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_PSM_C1_02_RouteA_SelectedPhiFinC1SourceEmission_or_RouteB_ActualRowSourceIndependenceFill_v1.md"
)
BUILD = ROOT / "scripts" / "build_selected_psm_c1_02_routea_selectedphifinc1sourceemission_or_routeb_actualrowsourceindependencefill.py"

STATUS = (
    "MTT_SELECTED_PSM_C1_02_ROUTEA_SELECTEDPHIFINC1SOURCEEMISSION_OR_ROUTEB_ACTUALROWSOURCEINDEPENDENCEFILL_"
    "BUILT_FINAL_ACTUAL_ATTEMPTS_REJECT_SOURCE_THEOREM_OR_ROWSOURCE_THEOREM_OPEN"
)
NEXT = "MTT_Selected_PSM_C1_02_SelectedPhiFinC1SourceEmissionTheorem_or_FiniteC1RowSourceIndependenceTheorem_v1"


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
    final = load(FINAL)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem missing")
    require(candidate["closure_decision"]["SM_parity_closed_under_declared_standard"] is True, "SM parity boundary missing")
    require(candidate["closure_decision"]["local_principle_route_A_validates"] is True, "local route missing")
    require(candidate["closure_decision"]["route_A_actual_attempt_rejected"] is True, "Route A should reject")
    require(candidate["closure_decision"]["route_B_actual_attempt_rejected"] is True, "Route B should reject")
    require(candidate["closure_decision"]["unpatched_PSM_C1_02_closed"] is False, "unpatched overclosed")
    require(candidate["superset_strategy"]["paths_used_as_free_parameters"] is False, "superset knob violation")

    require(route_a["status"] == "ROUTE_A_SELECTED_PHIFINC1_SOURCE_EMISSION_ATTEMPT_REJECTED", "Route A status mismatch")
    require(route_a["current_attempt_rejected"] is True, "Route A current should reject")
    require(route_a["local_principle_route_A_validates"] is True, "Route A local route missing")
    require(route_a["local_principle_is_unpatched_proof"] is False, "Route A local overclaim")
    require(route_a["unpatched_route_A_closed_now"] is False, "Route A overclosed")
    require(len(route_a["remaining_route_A_fields"]) == 7, "Route A remaining fields mismatch")

    require(route_b["status"] == "ROUTE_B_ACTUAL_ROWSOURCE_INDEPENDENCE_ATTEMPT_REJECTED", "Route B status mismatch")
    require(route_b["current_attempt_rejected"] is True, "Route B current should reject")
    require(route_b["route_B_all_other_strict_fields_closed"] is True, "Route B strict fields missing")
    require(route_b["remaining_route_B_field"] == "source_independent_of_residual_projector_replay", "Route B field mismatch")
    require(route_b["unpatched_route_B_closed_now"] is False, "Route B overclosed")

    require(final["status"] == "FINAL_ACTUAL_ATTEMPTS_REJECT_THEOREM_TARGETS_SHARP", "final status mismatch")
    require(final["SM_parity_remains_closed"] is True, "final SM boundary missing")
    require(final["local_principle_is_no_knob_closure"] is False, "final local overclaim")
    require(final["route_A_actual_attempt_rejected"] is True, "final Route A mismatch")
    require(final["route_B_actual_attempt_rejected"] is True, "final Route B mismatch")
    require(final["unpatched_source_promotion_closed"] is False, "final overclosed")
    require(final["remaining_exact_theorems"]["route_A"] == "SelectedPhiFinC1PhysicalSourceEmissionTheorem", "final Route A theorem mismatch")
    require(final["remaining_exact_theorems"]["route_B"] == "SelectedFiniteC1RowSourceIndependenceTheorem", "final Route B theorem mismatch")

    require(next_work["next_required_artifact"] == NEXT, "next mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["route_A_actual_attempt_rejected"] is True, "cert Route A mismatch")
    require(cert["route_B_actual_attempt_rejected"] is True, "cert Route B mismatch")
    require(cert["local_principle_route_A_validates"] is True, "cert local route mismatch")
    require("source ownership" in note, "note missing source ownership")

    for packet in [candidate, route_a, route_b, final, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
