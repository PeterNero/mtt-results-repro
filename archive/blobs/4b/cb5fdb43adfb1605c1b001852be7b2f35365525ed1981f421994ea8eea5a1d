"""Audit actual final source-emission fill after alpha1 bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_finalsourceemission_actualfill_or_nogowitness"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ATTEMPT = PACKET_DIR / "actual_source_emission_fill_attempt.packet.json"
WITNESS = PACKET_DIR / "actual_fill_nogo_witness_after_alpha1.packet.json"
FRONTIER = PACKET_DIR / "current_frontier_after_actual_fill_attempt.packet.json"
VALIDATION = PACKET_DIR / "strict_validator_result.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_FinalSourceEmissionActualFill_or_NoGoWitness_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1emission_or_independenthessianquadraturesource.py"

STATUS = "MTT_SELECTED_FINALSOURCEEMISSION_ACTUALFILL_BUILT_ALPHA1_CLOSED_SOURCE_PROMOTION_OPEN"
NEXT = "MTT_Selected_SameBranchPhiFinC1SourceEmission_or_IndependentHessianQuadratureExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    data = load(DATA)
    attempt = load(ATTEMPT)
    witness = load(WITNESS)
    frontier = load(FRONTIER)
    validation = load(VALIDATION)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(ATTEMPT)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    require(data["status"] == STATUS, "status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["SM_parity_closed"] is True, "SM parity reopened")
    require(data["true_SM_equivalence_closed"] is False, "true equivalence overclaimed")
    require(data["no_knob_closed"] is False, "no-knob overclaimed")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used")
    require(data["target_fitting_used"] is False, "target fitting used")

    closed = attempt["closed_before_this_attempt"]
    for key in [
        "SM_parity_closed_under_declared_standard",
        "static_source_frontier_reconciled",
        "same_branch_alpha1_derivative_closed",
        "honest_dotd_validator_replay_closed",
        "canonical_residual_values_emitted",
        "algebraic_residual_value_problem_closed",
    ]:
        require(closed[key] is True, f"closed gate missing: {key}")

    route_a = attempt["route_A_phifinc1_source_emission"]
    route_b = attempt["route_B_independent_hessian_quadrature_source"]
    require(route_a["alpha1_no_longer_missing"] is True, "alpha1 should be retired")
    require(route_a["same_branch"] is False, "Route A source overclosed")
    require(route_a["physical_phifin_c1_action_emitted"] is False, "Route A action overclosed")
    require(route_a["same_source_b_selected_emitted"] is False, "Route A b overclosed")
    require(route_b["alpha1_no_longer_missing"] is True, "Route B alpha1 flag missing")
    require(route_b["independent_hessian_quadrature_source_emitted"] is False, "Route B hessian overclosed")
    require(route_b["selected_b_vector_source"] is False, "Route B b overclosed")
    require(route_b["source_independent_of_residual_projector_replay"] is False, "Route B independence overclosed")

    require(proc.returncode == 1, "validator should reject actual fill")
    require(validation["exit_code"] == 1, "recorded validator should reject")
    require(witness["validator_rejects_actual_fill"] is True, "witness should reject")
    require(witness["alpha1_and_dotd_retired_as_blockers"] is True, "alpha1 blocker not retired")
    require(witness["canonical_residual_value_search_retired_as_blocker"] is True, "residual blocker not retired")
    require(witness["not_a_regression"]["SM_parity_remains_closed_under_declared_standard"] is True, "regression guard missing")

    for key in [
        "SM_parity_interface_standard",
        "static_Qa_SU3_SM_slot_source_frontier",
        "same_branch_alpha1_derivative",
        "honest_dotd_validator_replay",
        "canonical_R_Z_R_X_residual_values",
        "algebraic_b_replay_target",
    ]:
        require(frontier["closed_gates"][key] is True, f"frontier closed gate missing: {key}")
    for key, value in frontier["remaining_gates"].items():
        require(value is True, f"frontier open gate missing: {key}")

    require(cert["validator_rejects_actual_fill"] is True, "cert validator mismatch")
    require(cert["alpha1_dotd_retired_as_blockers"] is True, "cert alpha1 blocker missing")
    require(cert["same_branch_phifin_source_closed"] is False, "cert Route A overclosed")
    require(cert["independent_hessian_quadrature_source_closed"] is False, "cert Route B overclosed")
    require("This is progress, not regression" in note, "note missing progression guard")
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
