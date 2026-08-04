"""Audit PhiFinC1 source-emission / finite-row independence theorem frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phifinc1sourceemissionorfiniterowindependencetheorem"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CRITERIA = PACKET_DIR / "source_ownership_acceptance_criteria.packet.json"
PREMISES = PACKET_DIR / "remaining_source_ownership_premises.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFinC1SourceEmissionOrFiniteRowIndependenceTheorem_v1.md"

STATUS = (
    "MTT_SELECTED_PHIFINC1SOURCEEMISSIONORFINITEROWINDEPENDENCETHEOREM_"
    "CRITERIA_PROVED_PREMISES_OPEN"
)
NEXT_ARTIFACT = "MTT_Selected_PSM_C1_02_SelectedSourceOwnershipPremiseExecution_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def guard(packet: dict[str, Any], label: str) -> None:
    require(packet.get("closure_claimed") is True, f"{label} closure")
    require(packet.get("observed_data_used_as_selector") is False, f"{label} observed selector")
    require(packet.get("target_fitting_used") is False, f"{label} target fitting")


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    criteria = load(CRITERIA)
    premises = load(PREMISES)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    for label, packet in [
        ("candidate", candidate),
        ("criteria", criteria),
        ("premises", premises),
        ("cert", cert),
    ]:
        guard(packet, label)

    require(candidate["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(candidate["theorem"]["proved"] is True, "candidate theorem")
    require(candidate["theorem"]["name"] == "PhiFinC1SourceEmissionOrFiniteRowIndependenceTheorem", "theorem name")
    require(cert["theorem_proved"] is True, "cert theorem")
    require(candidate["next_required_artifact"] == NEXT_ARTIFACT, "candidate next")
    require(premises["next_required_artifact"] == NEXT_ARTIFACT, "premises next")
    require(cert["next_required_artifact"] == NEXT_ARTIFACT, "cert next")

    require(criteria["status"] == "ROUTE_A_AND_ROUTE_B_ACCEPTANCE_CRITERIA_PROVED", "criteria status")
    require(criteria["selected_source_ownership_criteria_proved"] is True, "ownership criteria")
    require(criteria["route_A_acceptance_criterion_proved"] is True, "route A criterion")
    require(criteria["route_B_acceptance_criterion_proved"] is True, "route B criterion")
    require(criteria["source_ownership_boundary_frozen_like_SM_parity"] is True, "boundary frozen")
    require(criteria["finite_rows_closed_as_replay_postchecks"] is True, "finite row replay")
    require(criteria["local_principle_route_A_validates"] is True, "local principle")
    require(criteria["strict_row_source_independence_validator_built"] is True, "route B validator")

    require(premises["status"] == "SOURCE_OWNERSHIP_PREMISES_OPEN", "premises status")
    require(premises["remaining_premise_count"] == 2, "premise count")
    require(premises["remaining_premises"] == [
        "PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma",
        "independent_finite_C1_row_formula_source_theorem",
    ], "premise names")
    require(premises["route_A_source_emission_theorem_proved_now"] is False, "route A theorem overclaim")
    require(premises["route_B_row_source_independence_theorem_proved_now"] is False, "route B theorem overclaim")
    require(premises["unpatched_PSM_C1_02_closed"] is False, "unpatched overclosed")
    require(premises["true_SM_equivalence_closed"] is False, "true SM overclosed")

    decision = candidate["closure_decision"]
    require(decision["PhiFinC1_source_emission_or_finite_row_independence_frontier_attacked"] is True, "decision attacked")
    require(decision["selected_source_ownership_criteria_proved"] is True, "decision ownership")
    require(decision["route_A_acceptance_criterion_proved"] is True, "decision route A")
    require(decision["route_B_acceptance_criterion_proved"] is True, "decision route B")
    require(decision["finite_rows_closed_as_replay_postchecks"] is True, "decision finite replay")
    require(decision["source_ownership_boundary_frozen_like_SM_parity"] is True, "decision boundary")
    require(decision["strict_row_source_independence_validator_built"] is True, "decision validator")
    require(decision["remaining_source_ownership_premise_count"] == 2, "decision premise count")
    require(decision["accepted_true_equivalence_precision_rows"] == 0, "decision true rows")
    for key in [
        "route_A_source_emission_theorem_proved_now",
        "route_B_row_source_independence_theorem_proved_now",
        "actual_dynamic_QaSU3_payload_values_closed",
        "true_SM_equivalence_closed",
        "full_no_knob_closed",
    ]:
        require(decision[key] is False, f"{key} overclosed")

    for phrase in [
        "selected source ownership criteria proved         true",
        "Route A acceptance criterion proved               true",
        "Route B acceptance criterion proved               true",
        "remaining source-ownership premises               2",
        "PhysicalPhiFinC1FiniteQuotientNoExtraBoundarySourceLemma",
        "independent_finite_C1_row_formula_source_theorem",
        NEXT_ARTIFACT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
