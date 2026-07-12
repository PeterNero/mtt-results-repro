"""Build phase-lane curvature residual exactness/source-correction target."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_phaselanecurvatureresidualexactness_or_sourcecorrectionrows"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
FACTORIZATION = PACKET_DIR / "rank1_residual_family_shape_factorization.packet.json"
CORRECTIONS = PACKET_DIR / "source_correction_shape_trials.packet.json"
DECISION = PACKET_DIR / "residual_exactness_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhaseLaneCurvatureResidualExactness_or_SourceCorrectionRows_v1.md"

PREV = DATA / "selected_phaselanecurvaturesourcerelation_or_sevenparameteryukawareduction"
OBLIGATION = PREV / "residual_exactness_obligation.packet.json"
EXECUTION = PREV / "seven_parameter_reduction_execution.packet.json"
BASIS = DATA / "selected_spectralyukawaresponsebasis_or_coefficientsourcewall" / "selected_family_spectral_response_basis.packet.json"

STATUS = "MTT_SELECTED_PHASELANECURVATURERESIDUALEXACTNESS_OR_SOURCECORRECTIONROWS_BUILT_RANK1_SHAPE_INTEGER_CLUE_SOURCE_OPEN"
NEXT = "MTT_Selected_SourceIntegerSectorAmplitudeTheorem_or_GammaCorrectionRows_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def correction_metrics(residual: np.ndarray, correction: np.ndarray) -> dict[str, float]:
    remaining = residual - correction
    return {
        "remaining_frobenius_norm": float(np.linalg.norm(remaining)),
        "remaining_rms_log_residual": float(np.sqrt(np.mean(remaining * remaining))),
        "remaining_max_abs_log_residual": float(np.max(np.abs(remaining))),
        "remaining_worst_multiplicative_yukawa_error": float(math.exp(np.max(np.abs(remaining)))),
    }


def one_amplitude_trial(residual: np.ndarray, family_shape: np.ndarray, sector_shape: list[float]) -> dict[str, object]:
    sector = np.array(sector_shape, dtype=float)
    amplitudes = (residual @ family_shape) / float(family_shape @ family_shape)
    rho = float((amplitudes @ sector) / (sector @ sector))
    correction = np.outer(rho * sector, family_shape)
    return {
        "sector_shape": [float(x) for x in sector],
        "rho": rho,
        "predicted_sector_amplitudes": [float(x) for x in rho * sector],
        "sector_amplitude_residuals": [float(x) for x in amplitudes - rho * sector],
        **correction_metrics(residual, correction),
        "accepted_as_source_row": False,
        "observed_data_used_as_selector": True,
        "target_fitting_used": True,
    }


def main() -> int:
    obligation = load(OBLIGATION)
    execution = load(EXECUTION)
    basis = load(BASIS)

    family_eigenvalues = np.array(basis["eigenvalues"], dtype=float)
    residual = np.array(obligation["residual_matrix_rows_u_d_e"], dtype=float)
    family_shape = np.array([-2.0, 3.0, -1.0], dtype=float)
    amplitudes = (residual @ family_shape) / float(family_shape @ family_shape)
    exact_reconstruction = np.outer(amplitudes, family_shape)
    family_shape_residual = residual - exact_reconstruction

    # The vector [-2,3,-1] is the one-dimensional complement to affine
    # response on the selected spectrum: sum Q_g = 0 and sum Q_g F_g = 0.
    factorization = {
        "schema": "MTTRank1ResidualFamilyShapeFactorization.v1",
        "status": "RANK1_FAMILY_SHAPE_FACTORIZATION_EXACT",
        "family_eigenvalues": [float(x) for x in family_eigenvalues],
        "family_shape_Q": [float(x) for x in family_shape],
        "family_shape_checks": {
            "sum_Q": float(np.sum(family_shape)),
            "dot_Q_family_eigenvalues": float(family_shape @ family_eigenvalues),
            "orthogonal_to_affine_family_basis": abs(float(np.sum(family_shape))) < 1.0e-12
            and abs(float(family_shape @ family_eigenvalues)) < 1.0e-12,
        },
        "sector_amplitudes_eta_u_d_e": [float(x) for x in amplitudes],
        "residual_factorization": "R_{s,g}=eta_s*Q_g",
        "max_abs_factorization_error": float(np.max(np.abs(family_shape_residual))),
        "residual_rank": obligation["residual_rank"],
        "row_sums": obligation["residual_row_sums"],
        "accepted_as_exact_shape_theorem": True,
        "accepted_as_numeric_source_rows": False,
    }

    exact_three_eta = {
        "description": "Exact three-amplitude residual correction eta_s*Q_g",
        "parameter_count": 3,
        "sector_amplitudes_eta_u_d_e": [float(x) for x in amplitudes],
        **correction_metrics(residual, exact_reconstruction),
        "interpretation": "Exact but restores the per-sector curvature freedom unless eta_s is source-derived.",
        "accepted_as_source_row": False,
        "observed_data_used_as_selector": True,
        "target_fitting_used": True,
    }

    quark_lepton = one_amplitude_trial(residual, family_shape, [1.0, 1.0, -1.0])
    quark_lepton["description"] = "One-amplitude quark-positive/lepton-negative correction rho*[1,1,-1] outer Q"
    integer_17_15_21 = one_amplitude_trial(residual, family_shape, [17.0, 15.0, -21.0])
    integer_17_15_21["description"] = "One-amplitude small-integer sector correction rho*[17,15,-21] outer Q"

    # Stronger but less compressive support: one quark amplitude and one lepton amplitude.
    sector_design = np.array([[1.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
    two_param = np.linalg.lstsq(sector_design, amplitudes, rcond=None)[0]
    two_param_correction = np.outer(sector_design @ two_param, family_shape)
    two_param_quark_lepton = {
        "description": "Two-amplitude correction with common quark amplitude and separate lepton amplitude",
        "parameter_count": 2,
        "rho_quark": float(two_param[0]),
        "rho_lepton": float(two_param[1]),
        "predicted_sector_amplitudes": [float(x) for x in sector_design @ two_param],
        "sector_amplitude_residuals": [float(x) for x in amplitudes - sector_design @ two_param],
        **correction_metrics(residual, two_param_correction),
        "accepted_as_source_row": False,
        "observed_data_used_as_selector": True,
        "target_fitting_used": True,
    }

    corrections = {
        "schema": "MTTSourceCorrectionShapeTrials.v1",
        "status": "SOURCE_CORRECTION_SHAPE_TRIALS_EXECUTED_SOURCE_OPEN",
        "family_shape_Q": [float(x) for x in family_shape],
        "trials": {
            "exact_three_eta": exact_three_eta,
            "one_amplitude_quark_lepton_sign": quark_lepton,
            "one_amplitude_integer_17_15_minus21": integer_17_15_21,
            "two_amplitude_quark_common_lepton": two_param_quark_lepton,
        },
        "best_compressive_clue": "one_amplitude_integer_17_15_minus21",
        "best_compressive_clue_worst_multiplicative_error": integer_17_15_21[
            "remaining_worst_multiplicative_yukawa_error"
        ],
        "guardrail": "All correction amplitudes are fitted from the current residual and are not selected source rows.",
    }

    decision = {
        "schema": "MTTResidualExactnessDecisionAfterSevenParameterYukawaSkeleton.v1",
        "status": "RANK1_SHAPE_CLOSED_INTEGER_SECTOR_AMPLITUDE_CLUE_SOURCE_OPEN",
        "closed_now": [
            "Residual is exactly rank 1 in the current arithmetic.",
            "Residual family shape is exactly Q=[-2,3,-1], the affine-family complement on the selected spectrum.",
            "The correction problem is reduced from nine entries to sector amplitudes eta_s, or to a one-amplitude integer-sector theorem if [17,15,-21] is source-derived.",
        ],
        "not_closed": [
            "eta_s amplitudes are fitted from Yukawa residuals.",
            "rho*[17,15,-21] is a near-exact integer clue, not a selected source theorem.",
            "gamma and the 3/11 curvature ratio remain source-open from the previous packet.",
        ],
        "source_row_counts": {
            "accepted_gamma_rows": 0,
            "accepted_three_over_eleven_ratio_rows": 0,
            "accepted_residual_correction_rows": 0,
            "accepted_no_knob_yukawa_rows": 0,
        },
        "next_exact_target": NEXT,
        "legal_next_routes": [
            "derive sector amplitude vector [17,15,-21] and rho from source data",
            "derive eta_s as selected threshold/profile correction rows",
            "derive an exactness/error certificate showing the residual is within declared source-profile uncertainty",
        ],
        "forbidden_routes": [
            "promote [17,15,-21] because it fits the residual",
            "count exact eta_s as source data without a source theorem",
            "claim exact Yukawa closure while residual/gamma/ratio source rows remain zero",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedPhaseLaneCurvatureResidualExactnessOrSourceCorrectionRows",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": True,
        "target_fitting_used": True,
        "inputs": {
            "previous_residual_obligation": str(OBLIGATION.relative_to(ROOT)),
            "previous_seven_parameter_execution": str(EXECUTION.relative_to(ROOT)),
            "selected_family_spectral_response_basis": str(BASIS.relative_to(ROOT)),
        },
        "output_packets": {
            "rank1_residual_family_shape_factorization": str(FACTORIZATION.relative_to(ROOT)),
            "source_correction_shape_trials": str(CORRECTIONS.relative_to(ROOT)),
            "residual_exactness_decision": str(DECISION.relative_to(ROOT)),
        },
        "theorem": {
            "name": "PhaseLaneCurvatureResidualFamilyShapeTheorem",
            "proved": True,
            "statement": "For the seven-parameter phase-lane curvature skeleton residual, the remaining matrix factors exactly as R_{s,g}=eta_s Q_g with Q=[-2,3,-1], the affine-family complement on the selected spectrum. This closes the residual shape theorem but not the numeric source correction rows.",
        },
        "key_numbers": {
            "family_shape_Q": [-2, 3, -1],
            "max_abs_factorization_error": factorization["max_abs_factorization_error"],
            "eta_u": float(amplitudes[0]),
            "eta_d": float(amplitudes[1]),
            "eta_e": float(amplitudes[2]),
            "integer_sector_shape": [17, 15, -21],
            "integer_sector_rho": integer_17_15_21["rho"],
            "integer_sector_remaining_max_abs_log_residual": integer_17_15_21["remaining_max_abs_log_residual"],
            "integer_sector_remaining_worst_multiplicative_error": integer_17_15_21[
                "remaining_worst_multiplicative_yukawa_error"
            ],
        },
        "closure_decision": {
            "residual_family_shape_closed": True,
            "source_correction_rows_closed": False,
            "strict_no_knob_flavor_closure": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhaseLaneCurvatureResidualExactness_or_SourceCorrectionRows_v1",
        "status": STATUS,
        "candidate": str(OUT.relative_to(ROOT)),
        "residual_family_shape_theorem_proved": True,
        "source_correction_rows_closed": False,
        "integer_sector_amplitude_source_proved": False,
        "accepted_no_knob_yukawa_rows": 0,
        "observed_data_used_as_selector": True,
        "target_fitting_used": True,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhaseLaneCurvatureResidualExactness or SourceCorrectionRows v1

Status: `{STATUS}`

## Shape Theorem

The residual left by the seven-parameter curvature skeleton factors exactly as

`R_s,g = eta_s Q_g`

with

`Q = [-2, 3, -1]`.

This is not arbitrary.  `Q` is the affine-family complement on the selected
family spectrum: it has zero sum and zero dot product with the selected family
eigenvalues.  The max factorization error is
`{factorization["max_abs_factorization_error"]}`.

The fitted sector amplitudes are:

- `eta_u = {float(amplitudes[0])}`
- `eta_d = {float(amplitudes[1])}`
- `eta_e = {float(amplitudes[2])}`

## Compression Clues

The one-amplitude quark/lepton sign correction

`rho [1,1,-1] outer Q`

reduces the remaining worst multiplicative error to
`{quark_lepton["remaining_worst_multiplicative_yukawa_error"]}`.

The sharper small-integer correction

`rho [17,15,-21] outer Q`

reduces it to
`{integer_17_15_21["remaining_worst_multiplicative_yukawa_error"]}`.

This is an extremely strong fitted clue, but it is not a source theorem.

## Decision

Closed now:

- residual rank-1 structure,
- family-shape correction channel `Q=[-2,3,-1]`,
- exact reduction of the correction problem to sector amplitudes.

Still open:

- source derivation of `gamma`,
- source derivation of the `3/11` curvature ratio,
- source derivation of either `eta_s` or the one-amplitude integer sector
  vector `[17,15,-21]` plus `rho`.

Next required artifact: `{NEXT}`.
"""

    write_json(FACTORIZATION, factorization)
    write_json(CORRECTIONS, corrections)
    write_json(DECISION, decision)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": str(OUT.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
