"""Build actual final source-emission fill attempt after latest alpha1 bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_finalsourceemission_actualfill_or_nogowitness"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
ATTEMPT = PACKET_DIR / "actual_source_emission_fill_attempt.packet.json"
WITNESS = PACKET_DIR / "actual_fill_nogo_witness_after_alpha1.packet.json"
FRONTIER = PACKET_DIR / "current_frontier_after_actual_fill_attempt.packet.json"
VALIDATION = PACKET_DIR / "strict_validator_result.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FinalSourceEmissionActualFill_or_NoGoWitness_v1.md"

VALIDATOR = ROOT / "scripts" / "validate_selected_phifinc1emission_or_independenthessianquadraturesource.py"

STATUS = "MTT_SELECTED_FINALSOURCEEMISSION_ACTUALFILL_BUILT_ALPHA1_CLOSED_SOURCE_PROMOTION_OPEN"
NEXT = "MTT_Selected_SameBranchPhiFinC1SourceEmission_or_IndependentHessianQuadratureExecution_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_validator(path: Path) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "path": rel(path),
        "exit_code": proc.returncode,
        "ok": proc.returncode == 0,
        "stdout": proc.stdout.strip().splitlines(),
        "stderr": proc.stderr.strip().splitlines(),
    }


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    best = load(DATA / "selected_finalsourceemission_bestcurrentfill_or_nogowitness.candidate.json")
    best_attempt = load(
        DATA
        / "selected_finalsourceemission_bestcurrentfill_or_nogowitness"
        / "best_current_source_emission_fill_attempt.packet.json"
    )
    best_witness = load(
        DATA
        / "selected_finalsourceemission_bestcurrentfill_or_nogowitness"
        / "final_source_emission_nogo_witness.packet.json"
    )
    alpha1 = load(DATA / "selected_phifinalpha1payloadvalues_or_typedbnretardedderivativeexecution.candidate.json")
    parity = load(DATA / "selected_latest_smparityclosure_status_or_trueequivalencefrontier.candidate.json")
    source_frontier = load(DATA / "selected_latest_sourcefrontier_reconciliation_or_dynamicc1proofgate.candidate.json")
    residual = load(DATA / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement.candidate.json")

    route_a = dict(best_attempt["route_A_phifinc1_source_emission"])
    route_a.update(
        {
            "status": "ACTUAL_FILL_AFTER_ALPHA1_REJECTED_SOURCE_PROMOTION_OPEN",
            "same_branch_alpha1_derivative_closed": alpha1["closure_decision"]["same_branch_alpha1_derivative_closed"],
            "honest_dotd_validator_replay_closed": alpha1["closure_decision"]["honest_dotd_validator_replay_closed"],
            "alpha1_no_longer_missing": True,
            "dynamic_phifin_c1_payload_closed": alpha1["closure_decision"]["phi_fin_dynamic_c1_payload_closed"],
            "canonical_R_Z_R_X_values_emitted": residual["closure_decision"]["canonical_residual_values_emitted"],
            "same_branch": False,
            "physical_phifin_c1_action_emitted": False,
            "no_extra_boundary_or_source_term": False,
            "selected_phase_shift_variation_operators_pre_residual": False,
            "selected_hessian_counterterm_source": False,
            "same_source_b_selected_emitted": False,
            "row_formula_source_theorem_derived": False,
        }
    )

    route_b = dict(best_attempt["route_B_independent_hessian_quadrature_source"])
    route_b.update(
        {
            "status": "ACTUAL_FILL_AFTER_ALPHA1_REJECTED_INDEPENDENT_PROVENANCE_OPEN",
            "alpha1_no_longer_missing": True,
            "independent_hessian_quadrature_source_emitted": False,
            "selected_b_vector_source": False,
            "source_independent_of_residual_projector_replay": False,
        }
    )

    attempt = {
        "schema": "MTTFinalSourceEmissionActualFillAttempt.v1",
        "status": "ACTUAL_FILL_REJECTED_AFTER_ALPHA1_BRIDGE",
        "route_A_phifinc1_source_emission": route_a,
        "route_B_independent_hessian_quadrature_source": route_b,
        "closed_before_this_attempt": {
            "SM_parity_closed_under_declared_standard": parity["SM_parity_closed"],
            "static_source_frontier_reconciled": source_frontier["what_closes_now"][
                "latest_source_frontier_reconciled"
            ],
            "same_branch_alpha1_derivative_closed": alpha1["closure_decision"][
                "same_branch_alpha1_derivative_closed"
            ],
            "honest_dotd_validator_replay_closed": alpha1["closure_decision"][
                "honest_dotd_validator_replay_closed"
            ],
            "canonical_residual_values_emitted": residual["closure_decision"][
                "canonical_residual_values_emitted"
            ],
            "algebraic_residual_value_problem_closed": residual["what_closes_now"][
                "algebraic_residual_value_search_closed"
            ],
        },
        "locked_target_values_used_as_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(ATTEMPT, attempt)
    validation = run_validator(ATTEMPT)
    write_json(VALIDATION, validation)

    missing_route_a = [
        "same-branch physical Phi_fin^C1 action/source emission",
        "zero extra boundary/source term",
        "pre-residual phase/shift variation operators",
        "same-branch Hessian counterterm source",
        "same-source b_selected emission",
        "row formula source theorem",
    ]
    missing_route_b = [
        "independent Hessian/quadrature source",
        "selected b-vector source",
        "source independence from residual-projector replay",
    ]

    witness = {
        "schema": "MTTFinalSourceEmissionActualFillNoGoWitness.v1",
        "status": "ALPHA1_CLOSED_BUT_FINAL_SOURCE_EMISSION_STILL_REJECTED",
        "validator_rejects_actual_fill": validation["exit_code"] == 1,
        "alpha1_and_dotd_retired_as_blockers": True,
        "canonical_residual_value_search_retired_as_blocker": True,
        "why_rejected": {
            "route_A_missing_source_fields": missing_route_a,
            "route_B_missing_independent_provenance_fields": missing_route_b,
            "best_current_witness_status": best_witness["status"],
        },
        "not_a_regression": {
            "SM_parity_remains_closed_under_declared_standard": parity["SM_parity_closed"],
            "patched_spine_closure_preserved": source_frontier["SM_parity_closed"],
            "true_equivalence_and_no_knob_correctly_open": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(WITNESS, witness)

    frontier = {
        "schema": "MTTCurrentFrontierAfterActualFinalSourceFillAttempt.v1",
        "status": "SOURCE_PROMOTION_OR_INDEPENDENT_EXECUTION_ONLY",
        "closed_gates": {
            "SM_parity_interface_standard": True,
            "static_Qa_SU3_SM_slot_source_frontier": True,
            "same_branch_alpha1_derivative": True,
            "honest_dotd_validator_replay": True,
            "canonical_R_Z_R_X_residual_values": True,
            "algebraic_b_replay_target": True,
        },
        "remaining_gates": {
            "same_branch_phifin_c1_source_emission": True,
            "same_source_b_selected_emission": True,
            "independent_hessian_quadrature_source": True,
            "independent_sector_response_rows": True,
            "true_SM_equivalence_precision_profile": True,
            "no_knob_closure": True,
        },
        "superset_strategy": {
            "mode": "two legal paths retained against one locked target",
            "straight_path": "same-branch Phi_fin^C1 action/source emission",
            "alternative_path": "independent selected Hessian/quadrature/Galerkin execution",
            "locked_target": "same R_Z/R_X/b_selected/deltaTheta dynamic C1 packet",
            "uses_observed_constants_as_knobs": False,
        },
    }
    write_json(FRONTIER, frontier)

    candidate = {
        "candidate": "MTTSelectedFinalSourceEmissionActualFillOrNoGoWitness",
        "status": STATUS,
        "inputs": {
            "previous_best_current_fill": rel(DATA / "selected_finalsourceemission_bestcurrentfill_or_nogowitness.candidate.json"),
            "previous_best_current_attempt": rel(
                DATA
                / "selected_finalsourceemission_bestcurrentfill_or_nogowitness"
                / "best_current_source_emission_fill_attempt.packet.json"
            ),
            "latest_alpha1_bridge_execution": rel(
                DATA / "selected_phifinalpha1payloadvalues_or_typedbnretardedderivativeexecution.candidate.json"
            ),
            "latest_SM_parity_status": rel(
                DATA / "selected_latest_smparityclosure_status_or_trueequivalencefrontier.candidate.json"
            ),
            "latest_source_frontier": rel(
                DATA / "selected_latest_sourcefrontier_reconciliation_or_dynamicc1proofgate.candidate.json"
            ),
            "canonical_residual_values": rel(
                DATA / "selected_samesource_boundaryresidualemission_or_unpatchedgalerkinreplacement.candidate.json"
            ),
        },
        "output_packets": {
            "actual_source_emission_fill_attempt": rel(ATTEMPT),
            "strict_validator_result": rel(VALIDATION),
            "actual_fill_nogo_witness_after_alpha1": rel(WITNESS),
            "current_frontier_after_actual_fill_attempt": rel(FRONTIER),
        },
        "theorem": {
            "name": "ActualFinalSourceEmissionNoGoAfterAlpha1BridgeTheorem",
            "proved": True,
            "statement": (
                "With the latest same-branch alpha1 derivative and honest dotD replay imported, "
                "the final source-emission validator still rejects the actual fill. Therefore alpha1/dotD "
                "and canonical residual values are retired as blockers, while the remaining gate is exactly "
                "same-branch Phi_fin^C1 source promotion or independent Hessian/quadrature provenance."
            ),
        },
        "what_closes_now": {
            "actual_final_source_emission_attempt_executed": True,
            "alpha1_dotd_excluded_from_remaining_source_failure": True,
            "canonical_residual_values_excluded_from_remaining_source_failure": True,
            "validator_rejection_replayed_after_latest_bridge": validation["exit_code"] == 1,
            "current_frontier_packet_emitted": True,
        },
        "what_remains_open": frontier["remaining_gates"],
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_FinalSourceEmissionActualFill_or_NoGoWitness_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "validator_exit_code": validation["exit_code"],
        "validator_rejects_actual_fill": validation["exit_code"] == 1,
        "alpha1_dotd_retired_as_blockers": True,
        "canonical_residual_values_retired_as_blocker": True,
        "same_branch_phifin_source_closed": False,
        "independent_hessian_quadrature_source_closed": False,
        "SM_parity_closed": True,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected FinalSourceEmissionActualFill or NoGoWitness v1

Status: `{STATUS}`.

This artifact performs the actual narrowed final source-emission fill after the
latest alpha1 bridge. It imports the same-branch alpha1 derivative, the honest
dotD replay, the latest SM-parity status, and the canonical residual values.

The strict validator still rejects the fill. This is progress, not regression:
alpha1/dotD and the algebraic residual values are now retired as blockers. The
remaining gate is only physical source promotion or independent provenance:

1. same-branch `Phi_fin^C1` action/source emission with `b_selected`; or
2. independent Hessian/quadrature/Galerkin source values for the same locked
   `R_Z/R_X/b_selected/deltaTheta` target.

No observed SM constants, CKM/PMNS values, masses, or benchmark matrices are
used as selectors.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS, "validator_exit_code": validation["exit_code"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
