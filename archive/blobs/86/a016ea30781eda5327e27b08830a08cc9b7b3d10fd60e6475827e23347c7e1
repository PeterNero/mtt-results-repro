"""Audit the final PSM-C1-02 selected source-ownership criterion artifact."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
SLUG = "selected_psm_c1_02_selectedphifinc1sourceemissiontheorem_or_finitec1rowsourceindependencetheorem"
BASE = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
BOUNDARY = BASE / "selected_source_ownership_frozen_boundary.packet.json"
ROUTE_A = BASE / "route_a_selected_phifinc1_source_emission_criterion.packet.json"
ROUTE_B = BASE / "route_b_selected_finite_c1_rowsource_independence_criterion.packet.json"
DECISION = BASE / "final_source_ownership_execution_decision.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_PSM_C1_02_SelectedPhiFinC1SourceEmissionTheorem_or_FiniteC1RowSourceIndependenceTheorem_v1.md"
)
BUILD = ROOT / "scripts" / "build_selected_psm_c1_02_selectedphifinc1sourceemissiontheorem_or_finitec1rowsourceindependencetheorem.py"

STATUS = (
    "MTT_SELECTED_PSM_C1_02_SELECTEDPHIFINC1SOURCEEMISSIONTHEOREM_OR_FINITEC1ROWSOURCEINDEPENDENCETHEOREM_"
    "BUILT_SOURCE_OWNERSHIP_CRITERIA_PROVED_GEOMETRIC_PREMISES_OPEN"
)
NEXT = "MTT_Selected_PSM_C1_02_SelectedSourceOwnershipPremiseExecution_v1"


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
    boundary = load(BOUNDARY)
    route_a = load(ROUTE_A)
    route_b = load(ROUTE_B)
    decision = load(DECISION)
    next_work = load(NEXT_WORK)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(candidate["theorem"]["name"] == "SelectedSourceOwnershipCriterionTheorem", "theorem name mismatch")
    require(candidate["theorem"]["proved"] is True, "criterion theorem not proved")
    require(candidate["closure_decision"]["SM_parity_closed_under_declared_standard"] is True, "SM parity boundary missing")
    require(candidate["closure_decision"]["finite_rows_closed_as_replay_postchecks"] is True, "finite rows not frozen")
    require(candidate["closure_decision"]["selected_source_ownership_criteria_proved"] is True, "criteria not proved")
    require(candidate["closure_decision"]["route_A_source_emission_theorem_proved_now"] is False, "Route A overclosed")
    require(candidate["closure_decision"]["route_B_row_source_independence_theorem_proved_now"] is False, "Route B overclosed")
    require(candidate["closure_decision"]["unpatched_PSM_C1_02_closed"] is False, "unpatched overclosed")
    require(candidate["guardrails_pass"] is True, "guardrails failed")

    require(boundary["status"] == "SOURCE_OWNERSHIP_BOUNDARY_LOCKED_NUMERIC_REPLAY_NOT_ACTIVE_BLOCKER", "boundary status mismatch")
    require(boundary["SM_parity_remains_frozen"] is True, "SM parity not frozen")
    require(all(boundary["closed_tiers"].values()), "not all boundary tiers closed")
    require(boundary["guardrails"]["paths_used_as_free_parameters"] is False, "paths as knobs")
    require(boundary["guardrails"]["closure_claimed"] is False, "boundary closure overclaim")

    require(route_a["status"] == "ROUTE_A_CRITERION_PROVED_PHYSICAL_SOURCE_PREMISES_OPEN", "Route A status mismatch")
    require(route_a["criterion_proved"] is True, "Route A criterion not proved")
    require(route_a["premises_satisfied_now"] is False, "Route A premises unexpectedly closed")
    require(len(route_a["current_missing_premises"]) == 4, "Route A missing premise count mismatch")
    require(route_a["conditional_certificate_valid"] is True, "Route A conditional cert missing")

    require(route_b["status"] == "ROUTE_B_CRITERION_PROVED_RESIDUAL_REPLAY_INDEPENDENCE_PREMISE_OPEN", "Route B status mismatch")
    require(route_b["criterion_proved"] is True, "Route B criterion not proved")
    require(route_b["premises_satisfied_now"] is False, "Route B premises unexpectedly closed")
    require(route_b["only_open_field_after_prior_reductions"] == "source_independent_of_residual_projector_replay", "Route B open field mismatch")

    require(decision["status"] == "FINAL_SOURCE_OWNERSHIP_EXECUTION_DECISION_OPEN_PREMISE_EXECUTION_REQUIRED", "decision status mismatch")
    require(decision["source_ownership_criterion_proved"] is True, "decision criterion missing")
    require(decision["route_A_selected_source_emission_theorem_proved_now"] is False, "decision Route A overclosed")
    require(decision["route_B_finite_C1_row_source_independence_theorem_proved_now"] is False, "decision Route B overclosed")
    require(decision["accepted_internal_scalar_rows_added"] == 0, "accepted rows overclaimed")
    require("another replay of the already closed 72/110 formal rows" in decision["not_allowed_as_next_progress"], "numeric replay guard missing")

    require(next_work["next_required_artifact"] == NEXT, "next work mismatch")
    require(cert["status"] == STATUS, "cert status mismatch")
    require(cert["source_ownership_criterion_proved"] is True, "cert criterion missing")
    require(cert["unpatched_closure_claimed"] is False, "cert unpatched overclaim")
    require("source-ownership analogue of the frozen SM-parity boundary" in note, "note missing SM-parity analogy")
    require("not theory knobs" in note, "note missing knob guard")

    for packet in [candidate, route_a, route_b, decision, cert]:
        guard(packet)

    print(f"PASS {CANDIDATE.name}: {candidate['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
