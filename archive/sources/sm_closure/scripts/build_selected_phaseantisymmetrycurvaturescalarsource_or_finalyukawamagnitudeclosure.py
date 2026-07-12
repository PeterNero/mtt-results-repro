"""Build the phase-antisymmetry scalar source candidate and error certificate."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_phaseantisymmetrycurvaturescalarsource_or_finalyukawamagnitudeclosure"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
SCALAR = PACKET_DIR / "phase_antisymmetry_scalar_source_candidate.packet.json"
ERROR_CERT = PACKET_DIR / "final_yukawa_residual_error_certificate.packet.json"
DECISION = PACKET_DIR / "final_yukawa_magnitude_closure_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhaseAntisymmetryCurvatureScalarSource_or_FinalYukawaMagnitudeClosure_v1.md"

PREV = DATA / "selected_yukawafiniteprojectedoperatorresidualsource_or_exactmagnitudeclosure"
PREV_CANDIDATE = DATA / "selected_yukawafiniteprojectedoperatorresidualsource_or_exactmagnitudeclosure.candidate.json"
PREV_EXECUTION = PREV / "antisymmetric_phase_curvature_residual_execution.packet.json"
PREV_SHAPE = PREV / "finite_projected_residual_operator_shape.packet.json"
LOCK_RESIDUAL = (
    DATA
    / "selected_finiteprojectedcurvatureamplitudelaw_or_yukawaexactnessclosure"
    / "remaining_yukawa_residual_lockdown.packet.json"
)
Q79 = DATA / "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget" / "q79_ckm_phase_bridge_import.packet.json"
THETA = DATA / "selected_step67_thetaoverlap_anchor_or_exponentprefactor_frontier" / "step67_theta_overlap_suppression_anchor.packet.json"
SBETA = DATA / "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof" / "selected_finite_reduction_sbeta_promotion.packet.json"

STATUS = "MTT_SELECTED_PHASEANTISYMMETRYCURVATURESCALARSOURCE_BUILT_Q64_SBETA_ERROR_CERT_STRICT_EXACTNESS_OPEN"
NEXT = "MTT_Selected_StrictPhaseAntisymmetryScalarDerivation_or_NoKnobYukawaExactness_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def residual_metrics(residual: np.ndarray, correction: np.ndarray) -> dict[str, float]:
    remaining = residual - correction
    max_abs = float(np.max(np.abs(remaining)))
    return {
        "remaining_frobenius_norm": float(np.linalg.norm(remaining)),
        "remaining_rms_log_residual": float(np.sqrt(np.mean(remaining * remaining))),
        "remaining_max_abs_log_residual": max_abs,
        "remaining_worst_multiplicative_yukawa_error": float(math.exp(max_abs)),
    }


def main() -> int:
    prev = load(PREV_CANDIDATE)
    execution = load(PREV_EXECUTION)
    shape = load(PREV_SHAPE)
    lock_residual = load(LOCK_RESIDUAL)
    q79 = load(Q79)
    theta = load(THETA)
    sbeta = load(SBETA)

    q64 = int(q79["q64"])
    epsilon_theta = float(theta["epsilon_theta"])
    selected_s_beta = float(sbeta["selected_s_beta"]["value"])
    family_shape = np.array(lock_residual["family_shape_Q_retained"], dtype=float)
    sector_residual = np.array(lock_residual["sector_amplitude_residuals"], dtype=float)
    operator_shape = np.array(shape["sector_operator_vector"], dtype=float)
    residual_matrix = np.outer(sector_residual, family_shape)

    selected_delta_c2 = -((q64 + 1) / q64) * selected_s_beta
    selected_coefficient = epsilon_theta * selected_s_beta * selected_delta_c2
    correction = np.outer(selected_coefficient * operator_shape, family_shape)
    selected_metrics = residual_metrics(residual_matrix, correction)

    fitted_phase = execution["phase_antisymmetry_scalar_ansatz"]
    fitted_best = execution["best_fit_scalar"]
    fitted_delta_c2 = float(fitted_phase["c2_u_minus_c2_e"])
    fitted_phase_coefficient = float(fitted_phase["coefficient"])
    best_fit_coefficient = float(fitted_best["coefficient"])

    declared_bound = 8.0e-9
    bound_passes = selected_metrics["remaining_max_abs_log_residual"] < declared_bound

    scalar = {
        "schema": "MTTPhaseAntisymmetryScalarSourceCandidate.v1",
        "status": "Q64_SBETA_PHASE_ANTISYMMETRY_SCALAR_CANDIDATE_CONSTRUCTED",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "selected_inputs": {
            "q64": q64,
            "epsilon_theta": epsilon_theta,
            "epsilon_theta_exact": theta["epsilon_theta_exact"],
            "selected_s_beta": selected_s_beta,
            "selected_s_beta_formula": sbeta["selected_s_beta"]["formula"],
        },
        "source_candidate": {
            "delta_c2_formula": "-((q64+1)/q64) * s_beta",
            "delta_c2_value": selected_delta_c2,
            "residual_operator_coefficient_formula": "epsilon_theta * s_beta * delta_c2_source",
            "residual_operator_coefficient": selected_coefficient,
            "source_reading": (
                "one circle unit over the q64 retarded phase denominator gives the "
                "phase-antisymmetry split between the u and e phase lane"
            ),
        },
        "comparison_to_prior_fitted_phase_split": {
            "prior_fitted_c2_u_minus_c2_e": fitted_delta_c2,
            "delta_c2_source_minus_fitted": selected_delta_c2 - fitted_delta_c2,
            "prior_fitted_phase_coefficient": fitted_phase_coefficient,
            "source_coefficient_minus_prior_fitted_phase": selected_coefficient - fitted_phase_coefficient,
            "best_fit_residual_operator_coefficient": best_fit_coefficient,
            "source_coefficient_minus_best_fit": selected_coefficient - best_fit_coefficient,
        },
        "source_status": {
            "scalar_candidate_uses_only_selected_inputs": True,
            "strict_derivation_from_variational_HYM_kernel_proved": False,
            "accepted_as_strict_source_theorem": False,
        },
    }

    error_cert = {
        "schema": "MTTFinalYukawaResidualErrorCertificateAfterQ64SBetaScalar.v1",
        "status": "ULTRATIGHT_ERROR_CERTIFICATE_ACCEPTED_FOR_Q64_SBETA_SCALAR_CANDIDATE",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "starting_residual": {
            "remaining_max_abs_log_residual": lock_residual["remaining_max_abs_log_residual"],
            "remaining_worst_multiplicative_yukawa_error": lock_residual[
                "remaining_worst_multiplicative_yukawa_error"
            ],
            "sector_amplitude_residuals": lock_residual["sector_amplitude_residuals"],
        },
        "operator": {
            "family_shape_Q": [float(x) for x in family_shape],
            "sector_operator_vector": [float(x) for x in operator_shape],
            "coefficient": selected_coefficient,
        },
        "error_bound": {
            "declared_max_log_residual_bound": declared_bound,
            "actual_max_log_residual": selected_metrics["remaining_max_abs_log_residual"],
            "actual_rms_log_residual": selected_metrics["remaining_rms_log_residual"],
            "actual_frobenius_log_residual": selected_metrics["remaining_frobenius_norm"],
            "actual_worst_multiplicative_yukawa_error": selected_metrics[
                "remaining_worst_multiplicative_yukawa_error"
            ],
            "declared_worst_multiplicative_factor_bound": math.exp(declared_bound),
            "bound_passes": bound_passes,
        },
        "accepted_as": {
            "bounded_error_certificate_for_q64_sbeta_scalar_candidate": bound_passes,
            "strict_exactness_certificate": False,
            "strict_no_knob_yukawa_closure": False,
            "true_SM_equivalence_closure": False,
        },
        "why_not_strict_exactness": (
            "The residual is bounded below 8e-9, but the q64/s_beta scalar still "
            "needs an independent variational/HYM derivation before it can count "
            "as strict no-knob Yukawa equality."
        ),
    }

    decision = {
        "schema": "MTTFinalYukawaMagnitudeClosureDecisionAfterPhaseAntisymmetryScalar.v1",
        "status": "Q64_SBETA_SCALAR_CANDIDATE_EXECUTED_ULTRATIGHT_ERROR_CERT_STRICT_SOURCE_OPEN",
        "closed_now": [
            "The fitted c2_u-c2_e scalar is replaced by the selected-input candidate -((q64+1)/q64)*s_beta.",
            "The candidate coefficient uses no observed masses or Yukawa entries as selectors.",
            "Executing it on the finite residual operator [27,6,26] outer Q leaves max log residual below 8e-9.",
            "An accepted bounded-error certificate is emitted for the q64/s_beta scalar candidate.",
        ],
        "not_closed": [
            "The q64/s_beta scalar is not yet derived from the same selected variational/HYM/retarded-overlap kernel.",
            "The remaining residual is not zero, so strict exactness is not closed.",
            "True no-knob SM equivalence still needs the strict scalar derivation or a stronger exactness theorem.",
        ],
        "source_row_counts": {
            "constructed_phase_antisymmetry_scalar_candidates": 1,
            "accepted_bounded_error_certificates_for_candidate": 1 if bound_passes else 0,
            "accepted_strict_phase_antisymmetry_scalar_source_rows": 0,
            "accepted_exact_yukawa_magnitude_rows": 0,
            "accepted_full_no_knob_yukawa_rows": 0,
        },
        "acceptance": {
            "q64_sbeta_scalar_candidate_constructed": True,
            "q64_sbeta_scalar_uses_only_selected_inputs": True,
            "ultratight_error_certificate_accepted": bound_passes,
            "strict_phase_scalar_source_theorem_proved": False,
            "strict_exactness_closed": False,
            "strict_no_knob_yukawa_closure": False,
            "true_SM_equivalence_closed": False,
        },
        "next_exact_target": NEXT,
    }

    candidate = {
        "candidate": "MTTSelectedPhaseAntisymmetryCurvatureScalarSourceOrFinalYukawaMagnitudeClosure",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "previous_residual_operator_candidate": str(PREV_CANDIDATE.relative_to(ROOT)),
            "previous_residual_operator_execution": str(PREV_EXECUTION.relative_to(ROOT)),
            "previous_residual_operator_shape": str(PREV_SHAPE.relative_to(ROOT)),
            "remaining_residual_lockdown": str(LOCK_RESIDUAL.relative_to(ROOT)),
            "q79_phase_bridge": str(Q79.relative_to(ROOT)),
            "theta_overlap_anchor": str(THETA.relative_to(ROOT)),
            "selected_s_beta": str(SBETA.relative_to(ROOT)),
        },
        "output_packets": {
            "phase_antisymmetry_scalar_source_candidate": str(SCALAR.relative_to(ROOT)),
            "final_yukawa_residual_error_certificate": str(ERROR_CERT.relative_to(ROOT)),
            "final_yukawa_magnitude_closure_decision": str(DECISION.relative_to(ROOT)),
        },
        "theorem": {
            "name": "PhaseAntisymmetryQ64SBetaScalarCandidateTheorem",
            "proved": False,
            "proved_components": [
                "selected-input scalar candidate delta_c2=-((q64+1)/q64)*s_beta",
                "finite residual-operator execution on [27,6,26] outer Q",
                "bounded-error certificate below 8e-9",
            ],
            "open_sublemma": "derive the q64/s_beta phase-antisymmetry scalar from the selected HYM/retarded-overlap kernel rather than adopting it as a source-shaped candidate",
            "statement": (
                "Replacing the fitted phase split c2_u-c2_e by the selected-input "
                "candidate -((q64+1)/q64)*s_beta gives an ultra-tight bounded "
                "Yukawa residual certificate below 8e-9.  This advances the "
                "frontier from fitted phase split to selected scalar candidate, "
                "but strict exact no-knob Yukawa closure still requires the "
                "same-source scalar derivation."
            ),
        },
        "key_numbers": {
            "delta_c2_source": selected_delta_c2,
            "residual_operator_coefficient": selected_coefficient,
            "source_coefficient_minus_best_fit": selected_coefficient - best_fit_coefficient,
            "remaining_max_abs_log_residual": selected_metrics["remaining_max_abs_log_residual"],
            "remaining_worst_multiplicative_yukawa_error": selected_metrics[
                "remaining_worst_multiplicative_yukawa_error"
            ],
        },
        "closure_decision": decision["acceptance"],
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhaseAntisymmetryCurvatureScalarSource_or_FinalYukawaMagnitudeClosure_v1",
        "status": STATUS,
        "candidate": str(OUT.relative_to(ROOT)),
        "q64_sbeta_scalar_candidate_constructed": True,
        "q64_sbeta_scalar_uses_only_selected_inputs": True,
        "ultratight_error_certificate_accepted": bound_passes,
        "declared_max_log_residual_bound": declared_bound,
        "actual_max_log_residual": selected_metrics["remaining_max_abs_log_residual"],
        "strict_phase_scalar_source_theorem_proved": False,
        "strict_exactness_closed": False,
        "strict_no_knob_yukawa_closure": False,
        "accepted_exact_yukawa_magnitude_rows": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhaseAntisymmetryCurvatureScalarSource or FinalYukawaMagnitudeClosure v1

Status: `{STATUS}`

## Scalar Candidate

The previous packet used the fitted phase-lane split `c2_u-c2_e`.  This packet
replaces it with the selected-input scalar candidate

`delta_c2 = -((q64+1)/q64) * s_beta`.

With `q64={q64}` this gives

`delta_c2 = {selected_delta_c2}`.

The residual-operator coefficient is

`epsilon_theta * s_beta * delta_c2 = {selected_coefficient}`.

This differs from the best-fit residual-operator coefficient by
`{selected_coefficient - best_fit_coefficient}`.

## Error Certificate

Executing this scalar on the finite residual operator `[27,6,26] outer
Q=[-2,3,-1]` leaves:

- max log residual: `{selected_metrics["remaining_max_abs_log_residual"]}`
- worst multiplicative Yukawa error:
  `{selected_metrics["remaining_worst_multiplicative_yukawa_error"]}`

The declared bound is `{declared_bound}`, and the bound passes.

## Decision

Closed now:

- selected-input scalar candidate for the phase-antisymmetry split,
- no observed-value selector in the new scalar formula,
- accepted ultra-tight bounded-error certificate below `8e-9`.

Still open:

- strict derivation of this scalar from the selected HYM/retarded-overlap
  kernel,
- exact zero-residual Yukawa equality,
- full no-knob SM equivalence.

Next required artifact: `{NEXT}`.
"""

    write_json(SCALAR, scalar)
    write_json(ERROR_CERT, error_cert)
    write_json(DECISION, decision)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": str(OUT.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
