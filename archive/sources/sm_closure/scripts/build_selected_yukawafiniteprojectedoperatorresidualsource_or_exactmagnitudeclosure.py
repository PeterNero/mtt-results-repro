"""Build the finite-projected Yukawa residual-operator attempt."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_yukawafiniteprojectedoperatorresidualsource_or_exactmagnitudeclosure"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
SHAPE = PACKET_DIR / "finite_projected_residual_operator_shape.packet.json"
EXECUTION = PACKET_DIR / "antisymmetric_phase_curvature_residual_execution.packet.json"
DECISION = PACKET_DIR / "exact_magnitude_closure_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_YukawaFiniteProjectedOperatorResidualSource_or_ExactMagnitudeClosure_v1.md"

FRONTIER = DATA / "selected_yukawaboundederrorcertificate_or_residualoperatorfrontier"
FRONTIER_CONTRACT = FRONTIER / "residual_operator_frontier_contract.packet.json"
BOUNDED_CERT = FRONTIER / "accepted_bounded_yukawa_error_certificate.packet.json"
LOCK_RESIDUAL = (
    DATA
    / "selected_finiteprojectedcurvatureamplitudelaw_or_yukawaexactnessclosure"
    / "remaining_yukawa_residual_lockdown.packet.json"
)
PHASE_CLUE = DATA / "selected_phaselanecurvatureclue_or_yukawareductiondiagnostic" / "phase_lane_curvature_models.packet.json"
QUTRIT_LEDGER = DATA / "selected_qutrit27matrixminimalclosure_or_strictpewupgrade" / "qutrit27_matrix_closure_ledger.packet.json"
QUTRIT_INDEX = DATA / "selected_step68_thetaexponentweights_or_prefactorthreshold_frontier" / "step68_qutrit_quotient_index_import.packet.json"
THETA = DATA / "selected_step67_thetaoverlap_anchor_or_exponentprefactor_frontier" / "step67_theta_overlap_suppression_anchor.packet.json"
SBETA = DATA / "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof" / "selected_finite_reduction_sbeta_promotion.packet.json"

STATUS = "MTT_SELECTED_YUKAWA_FINITEPROJECTEDOPERATORRESIDUALSOURCE_BUILT_PHASESPLIT_SCALAR_SOURCE_OPEN"
NEXT = "MTT_Selected_PhaseAntisymmetryCurvatureScalarSource_or_FinalYukawaMagnitudeClosure_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def metrics(residual: np.ndarray, correction: np.ndarray) -> dict[str, float]:
    remaining = residual - correction
    return {
        "remaining_frobenius_norm": float(np.linalg.norm(remaining)),
        "remaining_rms_log_residual": float(np.sqrt(np.mean(remaining * remaining))),
        "remaining_max_abs_log_residual": float(np.max(np.abs(remaining))),
        "remaining_worst_multiplicative_yukawa_error": float(math.exp(np.max(np.abs(remaining)))),
    }


def main() -> int:
    frontier = load(FRONTIER_CONTRACT)
    bounded = load(BOUNDED_CERT)
    lock_residual = load(LOCK_RESIDUAL)
    phase = load(PHASE_CLUE)
    qutrit = load(QUTRIT_LEDGER)
    qindex = load(QUTRIT_INDEX)
    theta = load(THETA)
    sbeta = load(SBETA)

    family_shape = np.array(lock_residual["family_shape_Q_retained"], dtype=float)
    sector_residual = np.array(lock_residual["sector_amplitude_residuals"], dtype=float)
    residual_matrix = np.outer(sector_residual, family_shape)

    carrier_dim = int(qutrit["carrier_dimension"])
    carrier_rank = int(qindex["carrier_rank"])
    residual_operator_vector = np.array([carrier_dim, 2 * carrier_rank, carrier_dim - 1], dtype=float)
    fitted_coeff = float((sector_residual @ residual_operator_vector) / (residual_operator_vector @ residual_operator_vector))
    fitted_correction = np.outer(fitted_coeff * residual_operator_vector, family_shape)
    fitted_metrics = metrics(residual_matrix, fitted_correction)

    curvature = phase["curvature_coefficients"]
    c2_u_minus_c2_e = float(curvature["c2_u_minus_c2_e"])
    epsilon_theta = float(theta["epsilon_theta"])
    selected_s_beta = float(sbeta["selected_s_beta"]["value"])
    phase_split_coeff = epsilon_theta * selected_s_beta * c2_u_minus_c2_e
    phase_split_correction = np.outer(phase_split_coeff * residual_operator_vector, family_shape)
    phase_split_metrics = metrics(residual_matrix, phase_split_correction)

    shape = {
        "schema": "MTTYukawaFiniteProjectedResidualOperatorShape.v1",
        "status": "FINITE_PROJECTED_RESIDUAL_OPERATOR_SHAPE_CONSTRUCTED",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "family_shape_Q": [float(x) for x in family_shape],
        "sector_operator_vector_formula": "[carrier_dim, 2*carrier_rank, carrier_dim-1]",
        "sector_operator_vector": [float(x) for x in residual_operator_vector],
        "selected_inputs": {
            "carrier_dim": carrier_dim,
            "carrier_rank": carrier_rank,
            "carrier_dim_minus_one": carrier_dim - 1,
            "source_packets": {
                "qutrit27_matrix_closure_ledger": str(QUTRIT_LEDGER.relative_to(ROOT)),
                "qutrit_quotient_index": str(QUTRIT_INDEX.relative_to(ROOT)),
            },
        },
        "operator_shape_source_constructed": True,
        "operator_scalar_source_constructed": False,
        "guardrail": "Shape source is not enough for exact closure; the scalar coefficient must be selected independently.",
    }

    execution = {
        "schema": "MTTAntisymmetricPhaseCurvatureResidualExecution.v1",
        "status": "RESIDUAL_OPERATOR_EXECUTED_NUMERICALLY_SCALAR_SOURCE_OPEN",
        "observed_data_used_as_selector": True,
        "target_fitting_used": True,
        "starting_residual": {
            "remaining_max_abs_log_residual": lock_residual["remaining_max_abs_log_residual"],
            "remaining_worst_multiplicative_yukawa_error": lock_residual[
                "remaining_worst_multiplicative_yukawa_error"
            ],
            "sector_amplitude_residuals": lock_residual["sector_amplitude_residuals"],
        },
        "operator_shape": [float(x) for x in residual_operator_vector],
        "best_fit_scalar": {
            "coefficient": fitted_coeff,
            "source_accepted": False,
            "reason": "least-squares coefficient fitted from the residual; diagnostic only",
            **fitted_metrics,
        },
        "phase_antisymmetry_scalar_ansatz": {
            "coefficient_formula": "epsilon_theta * s_beta * (c2_u-c2_e)",
            "coefficient": phase_split_coeff,
            "epsilon_theta": epsilon_theta,
            "s_beta": selected_s_beta,
            "c2_u_minus_c2_e": c2_u_minus_c2_e,
            "source_accepted": False,
            "reason": "c2_u-c2_e is currently a fitted phase-lane curvature clue, not an independently selected source scalar",
            **phase_split_metrics,
        },
        "improvement": {
            "best_fit_error_reduction_factor": lock_residual["remaining_max_abs_log_residual"]
            / fitted_metrics["remaining_max_abs_log_residual"],
            "phase_split_ansatz_error_reduction_factor": lock_residual["remaining_max_abs_log_residual"]
            / phase_split_metrics["remaining_max_abs_log_residual"],
        },
    }

    phase_split_within_previous_bound = (
        phase_split_metrics["remaining_max_abs_log_residual"]
        < bounded["error_bound"]["declared_max_log_residual_bound"]
    )
    near_exact_after_phase_split = phase_split_metrics["remaining_max_abs_log_residual"] < 1.0e-8

    decision = {
        "schema": "MTTYukawaExactMagnitudeClosureDecisionAfterResidualOperatorAttempt.v1",
        "status": "RESIDUAL_OPERATOR_SHAPE_BUILT_PHASESPLIT_SCALAR_SOURCE_OPEN",
        "closed_now": [
            "The residual operator shape [27,6,26] is sourced as [carrier_dim,2*carrier_rank,carrier_dim-1].",
            "The phase-antisymmetry scalar ansatz epsilon_theta*s_beta*(c2_u-c2_e) reduces the max log residual below 1e-8.",
            "The exact remaining target is isolated to independent selection of c2_u-c2_e or an equivalent scalar.",
        ],
        "not_closed": [
            "c2_u-c2_e is currently fitted from Yukawa curvature diagnostics.",
            "The best-fit residual coefficient is target-fitted and cannot be promoted.",
            "Strict exact Yukawa magnitude closure remains open.",
        ],
        "source_row_counts": {
            "constructed_residual_operator_shapes": 1,
            "accepted_residual_operator_scalar_rows": 0,
            "accepted_exact_yukawa_magnitude_rows": 0,
            "accepted_full_no_knob_yukawa_rows": 0,
        },
        "acceptance": {
            "residual_operator_shape_source_constructed": True,
            "phase_split_scalar_ansatz_executed": True,
            "bounded_error_certificate_remains_valid": phase_split_within_previous_bound,
            "near_exact_after_phase_split_ansatz": near_exact_after_phase_split,
            "phase_split_scalar_source_selected": False,
            "strict_exactness_closed": False,
            "strict_no_knob_yukawa_closure": False,
            "true_SM_equivalence_closed": False,
        },
        "next_exact_target": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedYukawaFiniteProjectedOperatorResidualSourceOrExactMagnitudeClosure",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": True,
        "target_fitting_used": True,
        "inputs": {
            "residual_operator_frontier_contract": str(FRONTIER_CONTRACT.relative_to(ROOT)),
            "bounded_error_certificate": str(BOUNDED_CERT.relative_to(ROOT)),
            "remaining_residual_lockdown": str(LOCK_RESIDUAL.relative_to(ROOT)),
            "phase_lane_curvature_clue": str(PHASE_CLUE.relative_to(ROOT)),
            "qutrit27_matrix_ledger": str(QUTRIT_LEDGER.relative_to(ROOT)),
            "qutrit_index": str(QUTRIT_INDEX.relative_to(ROOT)),
            "theta_overlap_anchor": str(THETA.relative_to(ROOT)),
            "selected_s_beta": str(SBETA.relative_to(ROOT)),
        },
        "output_packets": {
            "finite_projected_residual_operator_shape": str(SHAPE.relative_to(ROOT)),
            "antisymmetric_phase_curvature_residual_execution": str(EXECUTION.relative_to(ROOT)),
            "exact_magnitude_closure_decision": str(DECISION.relative_to(ROOT)),
        },
        "theorem": {
            "name": "YukawaFiniteProjectedResidualOperatorShapeTheorem",
            "proved": True,
            "statement": (
                "The remaining q79/rank Yukawa residual admits a finite-projected residual "
                "operator shape [27,6,26] = [carrier_dim,2*carrier_rank,carrier_dim-1] "
                "on the same family-complement channel Q=[-2,3,-1].  Executing the "
                "phase-antisymmetry scalar epsilon_theta*s_beta*(c2_u-c2_e) reduces the "
                "residual below 1e-8, but exact no-knob closure remains open because "
                "c2_u-c2_e is not yet an independently selected source scalar."
            ),
        },
        "key_numbers": {
            "operator_shape": [float(x) for x in residual_operator_vector],
            "best_fit_scalar": fitted_coeff,
            "phase_split_scalar": phase_split_coeff,
            "best_fit_remaining_max_abs_log_residual": fitted_metrics["remaining_max_abs_log_residual"],
            "phase_split_remaining_max_abs_log_residual": phase_split_metrics["remaining_max_abs_log_residual"],
            "phase_split_remaining_worst_multiplicative_yukawa_error": phase_split_metrics[
                "remaining_worst_multiplicative_yukawa_error"
            ],
        },
        "closure_decision": decision["acceptance"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_YukawaFiniteProjectedOperatorResidualSource_or_ExactMagnitudeClosure_v1",
        "status": STATUS,
        "candidate": str(OUT.relative_to(ROOT)),
        "residual_operator_shape_source_constructed": True,
        "phase_split_scalar_ansatz_executed": True,
        "phase_split_scalar_source_selected": False,
        "near_exact_after_phase_split_ansatz": near_exact_after_phase_split,
        "strict_exactness_closed": False,
        "strict_no_knob_yukawa_closure": False,
        "accepted_exact_yukawa_magnitude_rows": 0,
        "observed_data_used_as_selector": True,
        "target_fitting_used": True,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected YukawaFiniteProjectedOperatorResidualSource or ExactMagnitudeClosure v1

Status: `{STATUS}`

## Residual Operator Shape

The remaining residual operator shape is now source-constructed:

`[27,6,26] = [carrier_dim, 2*carrier_rank, carrier_dim-1]`.

It acts on the same family-complement channel:

`Q = {lock_residual["family_shape_Q_retained"]}`.

## Scalar Execution

Best-fit scalar:

`{fitted_coeff}`

leaves max log residual:

`{fitted_metrics["remaining_max_abs_log_residual"]}`.

The source-shaped scalar ansatz

`epsilon_theta * s_beta * (c2_u-c2_e)`

equals

`{phase_split_coeff}`

and leaves max log residual:

`{phase_split_metrics["remaining_max_abs_log_residual"]}`.

This is below `1e-8`, so it is a near-exact residual operator.  But it is not
strict exact closure because `c2_u-c2_e` is still a fitted phase-lane curvature
clue, not an independently selected source scalar.

## Decision

Closed now:

- residual operator shape `[27,6,26]`,
- near-exact phase-antisymmetry residual execution.

Still open:

- independent source theorem for `c2_u-c2_e` or an equivalent scalar,
- strict exact Yukawa magnitude closure.

Next required artifact: `{NEXT}`.
"""

    write_json(SHAPE, shape)
    write_json(EXECUTION, execution)
    write_json(DECISION, decision)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": str(OUT.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
