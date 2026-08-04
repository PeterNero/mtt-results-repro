"""Audit selected_psm_c1_02_selectedfinitec1_variationalbridge_or_sourcepromotionlemma."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "selected_psm_c1_02_selectedfinitec1_variationalbridge_or_sourcepromotionlemma"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
SUPPORT = BASE / "closed_support_import.packet.json"
LOCAL_THEOREM = BASE / "local_premise_source_promotion_theorem.packet.json"
UNPATCHED_GATE = BASE / "unpatched_source_promotion_gate.packet.json"
TWO_ROUTE = BASE / "two_route_next_cutset.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_SelectedFiniteC1VariationalProjectionBridge_or_SourcePromotionLemma_v1.md"
BUILD = ROOT / "scripts" / "build_selected_psm_c1_02_selectedfinitec1_variationalbridge_or_sourcepromotionlemma.py"

STATUS = "MTT_SELECTED_PSM_C1_02_LOCAL_SOURCE_PROMOTION_CLOSED_UNPATCHED_GATE_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def guard_no_selector(packet: dict) -> None:
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
    support = load(SUPPORT)
    local_theorem = load(LOCAL_THEOREM)
    unpatched_gate = load(UNPATCHED_GATE)
    two_route = load(TWO_ROUTE)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["proved"] is True, "theorem missing")
    require(candidate["what_closes_now"]["SelectedFiniteC1SourcePromotionLemma_under_explicit_local_principle"] is True, "local source lemma not closed")
    require(candidate["what_closes_now"]["source_promotion_as_unpatched_no_knob_theorem"] is False, "unpatched overclaim")
    require(candidate["local_premise_closure_claimed"] is True, "local closure missing")
    require(candidate["closure_claimed"] is False, "candidate overclaims global closure")

    require(support["closed_finite_support"]["finite_variational_euler_projection"] is True, "finite variational support missing")
    require(support["closed_finite_support"]["unique_quadratic_defect_functional_up_to_scale"] is True, "defect uniqueness missing")
    require(support["closed_finite_support"]["algebraic_finite_trace_boundary_closed"] is True, "finite boundary support missing")
    require(support["not_enough_for_unpatched_source_promotion"]["source_map_selected_by_MTT_now"] is False, "countermodel source field mismatch")

    require(local_theorem["status"] == "LOCAL_PREMISE_SOURCE_PROMOTION_THEOREM_PROVED", "local theorem status mismatch")
    require(local_theorem["derived_from_local_premise"]["SelectedFiniteC1VariationalProjectionBridge_local"] is True, "local bridge missing")
    require(local_theorem["derived_from_local_premise"]["SelectedFiniteC1SourcePromotionLemma_local"] is True, "local source lemma missing")
    require(local_theorem["guardrails"]["explicit_local_premise_not_unpatched_theorem"] is True, "local premise guard missing")
    require(local_theorem["closure_claimed"] is True, "local theorem closure should be claimed")
    require(local_theorem["closure_scope"] == "LOCAL_PREMISE_ONLY", "local closure scope mismatch")

    require(unpatched_gate["proved_now"] is False, "unpatched gate overproved")
    require(unpatched_gate["closure_claimed"] is False, "unpatched closure overclaim")
    require("derive SelectedWeylVariationActionPrinciple" in unpatched_gate["must_add_one_of"][0], "Route A next object missing")
    require("independent Route-B" in unpatched_gate["must_add_one_of"][1], "Route B next object missing")

    require(two_route["superset_strategy"]["paths_used_as_free_parameters"] is False, "superset knob violation")
    require(two_route["superset_strategy"]["locked_target"] == "same R_Z/R_X/b_selected source packet and same finite row-kernel functional", "locked target mismatch")
    require(next_work["primary"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / VPB-1-UNPATCHED", "next primary mismatch")
    require(next_work["fallback"]["label"] == "PSM-C1-02 / SOURCE-IDENTITY / SI-1u-B2-ROWSOURCE-INDEPENDENT", "next fallback mismatch")
    require(cert["local_premise_source_promotion_closed"] is True, "cert local closure missing")
    require(cert["unpatched_source_promotion_closed"] is False, "cert unpatched overclaim")
    require("conditional closure" in note, "note conditional closure missing")
    require("not yet unpatched/no-knob closure" in note, "note no-knob guard missing")

    for item in [candidate, support, local_theorem, unpatched_gate, two_route, cert]:
        guard_no_selector(item)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
