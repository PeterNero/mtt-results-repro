"""Build phase-lane Yukawa curvature clue diagnostic."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_phaselanecurvatureclue_or_yukawareductiondiagnostic"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
CURVATURE_PACKET = PACKET_DIR / "phase_lane_curvature_models.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhaseLaneCurvatureClue_or_YukawaReductionDiagnostic_v1.md"

COEFFS = DATA / "selected_spectralyukawaresponsebasis_or_coefficientsourcewall" / "diagnostic_log_yukawa_response_coefficients.packet.json"
BASIS = DATA / "selected_spectralyukawaresponsebasis_or_coefficientsourcewall" / "selected_family_spectral_response_basis.packet.json"

STATUS = "MTT_SELECTED_PHASELANECURVATURECLUE_OR_YUKAWAREDUCTIONDIAGNOSTIC_BUILT_FITTED_CLUE_SOURCE_OPEN"
NEXT = "MTT_Selected_PhaseLaneCurvatureSourceRelation_or_SevenParameterYukawaReduction_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def metrics(true: np.ndarray, pred: np.ndarray) -> dict[str, float]:
    residual = true - pred
    return {
        "relative_frobenius_log_residual": float(np.linalg.norm(residual) / np.linalg.norm(true)),
        "rms_log_residual": float(np.sqrt(np.mean(residual * residual))),
        "max_abs_log_residual": float(np.max(np.abs(residual))),
        "worst_multiplicative_yukawa_error": float(math.exp(np.max(np.abs(residual)))),
    }


def fixed_gamma_fit(family_eigenvalues: np.ndarray, log_row: np.ndarray, gamma: float) -> tuple[np.ndarray, np.ndarray]:
    linear_design = np.vstack([np.ones(3), family_eigenvalues]).T
    adjusted = log_row - gamma * family_eigenvalues**2
    ab = np.linalg.lstsq(linear_design, adjusted, rcond=None)[0]
    return ab, linear_design @ ab + gamma * family_eigenvalues**2


def solve_ratio_model(family_eigenvalues: np.ndarray, log_rows: dict[str, np.ndarray], ratio: float) -> tuple[np.ndarray, np.ndarray]:
    sectors = ["u", "d", "e"]
    design_rows = []
    values = []
    for sector_index, sector in enumerate(sectors):
        curvature_multiplier = ratio if sector == "d" else 1.0
        for eig, value in zip(family_eigenvalues, log_rows[sector]):
            row = [0.0] * 7
            row[2 * sector_index] = 1.0
            row[2 * sector_index + 1] = float(eig)
            row[6] = float(curvature_multiplier * eig * eig)
            design_rows.append(row)
            values.append(float(value))
    design = np.array(design_rows, dtype=float)
    y = np.array(values, dtype=float)
    beta = np.linalg.lstsq(design, y, rcond=None)[0]
    return beta, (design @ beta).reshape(3, 3)


def main() -> int:
    coeff_packet = json.loads(COEFFS.read_text(encoding="utf-8"))
    basis_packet = json.loads(BASIS.read_text(encoding="utf-8"))

    family_eigenvalues = np.array(basis_packet["eigenvalues"], dtype=float)
    sector_rows = {row["sector"]: row for row in coeff_packet["sector_rows"]}
    coefficients = {
        sector: np.array(row["coefficient_values_c0_c1_c2"], dtype=float)
        for sector, row in sector_rows.items()
    }
    yukawas = {
        sector: np.array(row["input_common_scale_diag_abs_Y"], dtype=float)
        for sector, row in sector_rows.items()
    }
    log_rows = {sector: np.log(values) for sector, values in yukawas.items()}
    log_matrix = np.vstack([log_rows[sector] for sector in ["u", "d", "e"]])
    yukawa_matrix = np.vstack([yukawas[sector] for sector in ["u", "d", "e"]])

    c2_u = float(coefficients["u"][2])
    c2_d = float(coefficients["d"][2])
    c2_e = float(coefficients["e"][2])
    phase_gamma_average = float((c2_u + c2_e) / 2.0)
    phase_curvature_difference = float(c2_u - c2_e)
    d_over_phase = float(c2_d / phase_gamma_average)
    phase_over_d = float(phase_gamma_average / c2_d)

    # Eight-parameter clue: u/e share one phase curvature; d remains exact.
    eight_param_pred_rows: list[np.ndarray] = []
    eight_param_details: dict[str, object] = {}
    for sector in ["u", "e"]:
        ab, pred = fixed_gamma_fit(family_eigenvalues, log_rows[sector], phase_gamma_average)
        eight_param_pred_rows.append(pred)
        eight_param_details[sector] = {
            "a_b_coefficients": [float(x) for x in ab],
            "predicted_over_true_yukawa_ratios": [float(x) for x in np.exp(pred) / yukawas[sector]],
        }
    quadratic_design = np.vstack([np.ones(3), family_eigenvalues, family_eigenvalues**2]).T
    d_exact = quadratic_design @ np.linalg.lstsq(quadratic_design, log_rows["d"], rcond=None)[0]
    eight_param_true = np.vstack([log_rows["u"], log_rows["e"], log_rows["d"]])
    eight_param_pred = np.vstack([eight_param_pred_rows[0], eight_param_pred_rows[1], d_exact])

    # Seven-parameter source-shape clue: u/e share gamma, d curvature is (3/11) gamma.
    ratio = 3.0 / 11.0
    seven_beta, seven_pred = solve_ratio_model(family_eigenvalues, log_rows, ratio)
    continuous_best_beta, continuous_best_pred = solve_ratio_model(family_eigenvalues, log_rows, d_over_phase)

    rational_scan = []
    for q in range(1, 41):
        for p in range(1, 41):
            r = p / q
            beta, pred = solve_ratio_model(family_eigenvalues, log_rows, r)
            m = metrics(log_matrix, pred)
            rational_scan.append(
                {
                    "p": p,
                    "q": q,
                    "ratio": float(r),
                    "gamma": float(beta[6]),
                    **m,
                }
            )
    rational_scan.sort(key=lambda item: item["rms_log_residual"])
    best_rationals = rational_scan[:10]

    curvature_packet = {
        "schema": "MTTPhaseLaneYukawaCurvatureClue.v1",
        "status": "PHASE_LANE_CURVATURE_CLUE_BUILT_SOURCE_OPEN",
        "source_split_used": {
            "phase_packet_I_plus_Z": ["u", "e"],
            "shift_packet_I_plus_X": ["d"],
            "corpus_support": [
                "selected_yukawaprojectionkernel_readiness_or_thresholdresponsefrontier_audit.py checks u/e phase and d shift routing",
                "paper_appendix_drafts selected-source I8 records phase_packet u,e and shift_packet d,nuD",
            ],
        },
        "curvature_coefficients": {
            "c2_u": c2_u,
            "c2_d": c2_d,
            "c2_e": c2_e,
            "phase_gamma_average_c2_u_e": phase_gamma_average,
            "c2_u_minus_c2_e": phase_curvature_difference,
            "c2_d_over_phase_gamma": d_over_phase,
            "phase_gamma_over_c2_d": phase_over_d,
            "best_small_rational_for_c2_d_over_phase_gamma_den_le_40": str(Fraction(d_over_phase).limit_denominator(40)),
            "best_small_rational_for_phase_gamma_over_c2_d_den_le_40": str(Fraction(phase_over_d).limit_denominator(40)),
        },
        "model_tests": {
            "quark_only_second_order_with_e_linear": {
                "parameter_count": 8,
                "status": "REJECTED_AS_STRONG_NUMERICAL_MODEL",
                "worst_multiplicative_yukawa_error": 5.366435997095622,
                "reason": "Making e first-order on the same selected family spectrum misses the charged lepton row by a factor over 5.",
            },
            "phase_lane_shared_curvature_d_exact": {
                "parameter_count": 8,
                "status": "VERY_STRONG_FITTED_CLUE_NOT_SOURCE",
                "shared_phase_gamma": phase_gamma_average,
                **metrics(eight_param_true, eight_param_pred),
                "details": eight_param_details,
            },
            "phase_lane_shared_curvature_shift_ratio_3_over_11": {
                "parameter_count": 7,
                "status": "VERY_STRONG_FITTED_CLUE_NOT_SOURCE",
                "ratio_c2_d_to_phase_gamma": ratio,
                "gamma": float(seven_beta[6]),
                **metrics(log_matrix, seven_pred),
                "predicted_over_true_yukawa_ratios_rows_u_d_e": [
                    [float(x) for x in row]
                    for row in (np.exp(seven_pred) / yukawa_matrix)
                ],
            },
            "continuous_ratio_best_fit_reference": {
                "parameter_count": 7,
                "status": "TARGET_FITTED_REFERENCE_ONLY",
                "ratio_c2_d_to_phase_gamma": d_over_phase,
                "gamma": float(continuous_best_beta[6]),
                **metrics(log_matrix, continuous_best_pred),
            },
            "best_small_rational_scan_denominator_le_40": best_rationals,
        },
        "decision": {
            "quark_only_second_order_supported": False,
            "phase_lane_second_order_supported_as_fitted_clue": True,
            "seven_parameter_near_reduction_supported_as_fitted_clue": True,
            "accepted_as_selected_source_theorem": False,
            "accepted_no_knob_yukawa_rows": 0,
            "observed_data_used_as_selector": True,
            "target_fitting_used": True,
            "next_required_artifact": NEXT,
        },
    }

    candidate = {
        "candidate": "MTTSelectedPhaseLaneCurvatureClueOrYukawaReductionDiagnostic",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": True,
        "target_fitting_used": True,
        "inputs": {
            "diagnostic_log_yukawa_response_coefficients": str(COEFFS.relative_to(ROOT)),
            "selected_family_spectral_response_basis": str(BASIS.relative_to(ROOT)),
        },
        "output_packets": {
            "phase_lane_curvature_models": str(CURVATURE_PACKET.relative_to(ROOT)),
        },
        "theorem_target": {
            "name": "PhaseLaneCurvatureSourceRelationTarget",
            "proved": False,
            "fitted_statement": "The fitted coefficient data strongly prefer a phase-lane curvature relation: u and e share c2 to about 0.15 percent in Yukawa magnitude, while d is consistent with a weaker shift-lane curvature close to (3/11) times the phase curvature. This is a diagnostic target, not a selected source theorem.",
        },
        "key_numbers": {
            "c2_u": c2_u,
            "c2_d": c2_d,
            "c2_e": c2_e,
            "phase_gamma_average": phase_gamma_average,
            "c2_u_minus_c2_e": phase_curvature_difference,
            "c2_d_over_phase_gamma": d_over_phase,
            "best_small_rational_c2_d_over_phase_gamma": "3/11",
            "phase_shared_curvature_worst_multiplicative_error": curvature_packet["model_tests"]["phase_lane_shared_curvature_d_exact"]["worst_multiplicative_yukawa_error"],
            "seven_parameter_3_over_11_worst_multiplicative_error": curvature_packet["model_tests"]["phase_lane_shared_curvature_shift_ratio_3_over_11"]["worst_multiplicative_yukawa_error"],
        },
        "closure_decision": {
            "quark_only_second_order_rejected_as_fit": True,
            "phase_lane_curvature_clue_retained": True,
            "seven_parameter_yukawa_near_reduction_retained": True,
            "strict_no_knob_flavor_closure": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhaseLaneCurvatureClue_or_YukawaReductionDiagnostic_v1",
        "status": STATUS,
        "candidate": str(OUT.relative_to(ROOT)),
        "theorem_target_proved": False,
        "phase_lane_curvature_clue_retained": True,
        "seven_parameter_near_reduction_retained": True,
        "accepted_as_selected_source_theorem": False,
        "accepted_no_knob_yukawa_rows": 0,
        "observed_data_used_as_selector": True,
        "target_fitting_used": True,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhaseLaneCurvatureClue or YukawaReductionDiagnostic v1

Status: `{STATUS}`

This is a fitted diagnostic, not a selected-source proof.

## Finding

The earlier blanket statement "all charged sectors are second order" is only
an interpolation-domain statement.  The more physical clue is lane-specific:

- phase lane: `u,e` via `phase_packet_I_plus_Z`
- shift lane: `d` via `shift_packet_I_plus_X`

The fitted quadratic curvatures are:

- `c2_u = {c2_u}`
- `c2_e = {c2_e}`
- `c2_d = {c2_d}`

The phase-lane average is

`gamma_phase = {phase_gamma_average}`

with

`c2_u - c2_e = {phase_curvature_difference}`.

Forcing `u` and `e` to share one phase curvature gives worst multiplicative
Yukawa error

`{curvature_packet["model_tests"]["phase_lane_shared_curvature_d_exact"]["worst_multiplicative_yukawa_error"]}`.

The shift-lane curvature ratio is

`c2_d / gamma_phase = {d_over_phase}`

whose best small rational with denominator <= 40 is `3/11`.  The
seven-parameter model

`c2_u = c2_e = gamma`, `c2_d = (3/11) gamma`

has worst multiplicative Yukawa error

`{curvature_packet["model_tests"]["phase_lane_shared_curvature_shift_ratio_3_over_11"]["worst_multiplicative_yukawa_error"]}`.

## Decision

This rejects the simple "quarks only are second order, leptons are first order"
fit on the current selected family spectrum.  The better clue is:

`phase packet = strong second-order curvature`

`shift packet = weaker curvature close to 3/11 of phase curvature`

This can reduce the fitted charged-Yukawa description from 9 exact coefficients
to a very accurate 7-parameter near-law, but it is not exact and it uses the
observed/profile Yukawa rows as fitted data.  It must not be promoted as a
no-knob result until the ratio and curvature are emitted by selected MTT source
data before empirical replay.

Next required artifact: `{NEXT}`.
"""

    write_json(CURVATURE_PACKET, curvature_packet)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": str(OUT.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
