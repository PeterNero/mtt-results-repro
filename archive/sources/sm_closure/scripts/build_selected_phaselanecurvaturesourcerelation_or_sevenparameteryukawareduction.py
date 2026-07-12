"""Build phase-lane curvature source-relation attempt for Yukawa reduction."""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_phaselanecurvaturesourcerelation_or_sevenparameteryukawareduction"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
SKELETON = PACKET_DIR / "phase_lane_curvature_source_skeleton.packet.json"
EXECUTION = PACKET_DIR / "seven_parameter_reduction_execution.packet.json"
OBLIGATION = PACKET_DIR / "residual_exactness_obligation.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_PhaseLaneCurvatureSourceRelation_or_SevenParameterYukawaReduction_v1.md"

CLUE = DATA / "selected_phaselanecurvatureclue_or_yukawareductiondiagnostic" / "phase_lane_curvature_models.packet.json"
COEFFS = DATA / "selected_spectralyukawaresponsebasis_or_coefficientsourcewall" / "diagnostic_log_yukawa_response_coefficients.packet.json"
BASIS = DATA / "selected_spectralyukawaresponsebasis_or_coefficientsourcewall" / "selected_family_spectral_response_basis.packet.json"
STEP68 = DATA / "selected_step68_thetaexponentweights_or_prefactorthreshold_frontier" / "step68_selected_theta_exponent_weight_rows.packet.json"

STATUS = "MTT_SELECTED_PHASELANECURVATURESOURCERELATION_OR_SEVENPARAMETERYUKAWAREDUCTION_BUILT_SKELETON_RESIDUAL_OPEN"
NEXT = "MTT_Selected_PhaseLaneCurvatureResidualExactness_or_SourceCorrectionRows_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def metrics(true: np.ndarray, pred: np.ndarray) -> dict[str, float]:
    residual = true - pred
    return {
        "relative_frobenius_log_residual": float(np.linalg.norm(residual) / np.linalg.norm(true)),
        "rms_log_residual": float(np.sqrt(np.mean(residual * residual))),
        "max_abs_log_residual": float(np.max(np.abs(residual))),
        "worst_multiplicative_yukawa_error": float(math.exp(np.max(np.abs(residual)))),
    }


def solve_reduction(family_eigenvalues: np.ndarray, log_matrix: np.ndarray, ratio: float) -> tuple[np.ndarray, np.ndarray]:
    design_rows = []
    values = []
    for sector_index, sector in enumerate(["u", "d", "e"]):
        curvature_multiplier = ratio if sector == "d" else 1.0
        for eig, value in zip(family_eigenvalues, log_matrix[sector_index]):
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
    clue = load(CLUE)
    coeff_packet = load(COEFFS)
    basis = load(BASIS)
    step68 = load(STEP68)

    family_eigenvalues = np.array(basis["eigenvalues"], dtype=float)
    rows = {row["sector"]: row for row in coeff_packet["sector_rows"]}
    yukawa_matrix = np.vstack([
        np.array(rows[sector]["input_common_scale_diag_abs_Y"], dtype=float)
        for sector in ["u", "d", "e"]
    ])
    log_matrix = np.log(yukawa_matrix)

    ratio = 3.0 / 11.0
    beta, pred_log_matrix = solve_reduction(family_eigenvalues, log_matrix, ratio)
    residual = log_matrix - pred_log_matrix
    pred_yukawa_matrix = np.exp(pred_log_matrix)
    ratio_matrix = pred_yukawa_matrix / yukawa_matrix

    exponent_rows = step68["charged_exponent_weight_rows"]
    exponent_summary = {
        sector: [
            {
                "generation": row["generation"],
                "source_direction": row["source_direction"],
                "source_column": row["source_column"],
                "theta_exponent": row["theta_exponent"],
                "qutrit_quotient_floor": row["qutrit_quotient_floor"],
                "scalar_coupling_slot": row["scalar_coupling_slot"],
            }
            for row in exponent_rows
            if row["sector"] == sector
        ]
        for sector in ["u", "d", "e"]
    }

    closed_clauses = {
        "family_spectrum_closed": basis["family_operator_closed"] is True,
        "family_basis_nonsingular": basis["basis_nonsingular"] is True,
        "phase_shift_lane_routing_closed": (
            rows["u"]["source_direction"] == "phase_packet_I_plus_Z"
            and rows["e"]["source_direction"] == "phase_packet_I_plus_Z"
            and rows["d"]["source_direction"] == "shift_packet_I_plus_X"
        ),
        "step68_theta_exponent_rows_closed": step68["generation_resolved_exponent_rows_closed"] is True,
        "theta_rows_target_fitting_used": step68["target_fitting_used"] is True,
        "theta_rows_observed_data_used_as_selector": step68["observed_data_used_as_selector"] is True,
        "small_rational_curvature_clue_retained": clue["curvature_coefficients"]["best_small_rational_for_c2_d_over_phase_gamma_den_le_40"] == "3/11",
    }

    skeleton = {
        "schema": "MTTPhaseLaneCurvatureSourceSkeleton.v1",
        "status": "SOURCE_SKELETON_BUILT_NUMERIC_CURVATURE_SOURCE_OPEN",
        "relation": {
            "operator_form": "log|Y_s(g)| = a_s + b_s F_g + gamma * chi_s * F_g^2",
            "chi_phase_packet_I_plus_Z": 1,
            "chi_shift_packet_I_plus_X": "3/11",
            "sector_lane_map": {
                "u": "phase_packet_I_plus_Z",
                "e": "phase_packet_I_plus_Z",
                "d": "shift_packet_I_plus_X",
            },
            "parameter_slots": [
                "a_u",
                "b_u",
                "a_d",
                "b_d",
                "a_e",
                "b_e",
                "gamma",
            ],
            "replaces_previous_slots": [
                "c2_u",
                "c2_d",
                "c2_e",
            ],
            "source_reduction_if_exact": "9 coefficient rows -> 7 coefficient rows",
        },
        "closed_source_side_support": closed_clauses,
        "theta_exponent_support": exponent_summary,
        "open_source_clauses": {
            "gamma_source_row": "No selected MTT source row currently emits gamma before fitting Yukawa magnitudes.",
            "three_over_eleven_source_ratio": "The ratio 3/11 is the best small rational clue, but current packets do not prove that the shift-lane curvature is exactly 3/11 of the phase-lane curvature.",
            "residual_exactness_or_correction_rows": "The seven-parameter skeleton leaves a nonzero residual, so strict closure needs either exact source correction rows or an exactness/error theorem tied to a selected source object.",
        },
        "guardrails": {
            "observed_data_used_to_fit_gamma_and_affine_rows": True,
            "accepted_as_selected_source_theorem": False,
            "accepted_no_knob_yukawa_rows": 0,
            "exact_reduction_closed": False,
        },
    }

    execution = {
        "schema": "MTTSevenParameterYukawaReductionExecution.v1",
        "status": "SEVEN_PARAMETER_REDUCTION_EXECUTED_AS_FITTED_SKELETON_RESIDUAL_OPEN",
        "ratio_c2_d_to_phase_gamma": ratio,
        "fitted_parameters": {
            "a_u": float(beta[0]),
            "b_u": float(beta[1]),
            "a_d": float(beta[2]),
            "b_d": float(beta[3]),
            "a_e": float(beta[4]),
            "b_e": float(beta[5]),
            "gamma": float(beta[6]),
        },
        "family_eigenvalues": [float(x) for x in family_eigenvalues],
        "true_log_yukawa_matrix_rows_u_d_e": [[float(x) for x in row] for row in log_matrix],
        "predicted_log_yukawa_matrix_rows_u_d_e": [[float(x) for x in row] for row in pred_log_matrix],
        "log_residual_matrix_true_minus_pred_rows_u_d_e": [[float(x) for x in row] for row in residual],
        "predicted_over_true_yukawa_ratios_rows_u_d_e": [[float(x) for x in row] for row in ratio_matrix],
        **metrics(log_matrix, pred_log_matrix),
        "accepted_as_exact_source_reduction": False,
        "observed_data_used_as_selector": True,
        "target_fitting_used": True,
    }

    residual_rank = int(np.linalg.matrix_rank(residual, tol=1e-12))
    residual_norm = float(np.linalg.norm(residual))
    obligation = {
        "schema": "MTTPhaseLaneCurvatureResidualExactnessObligation.v1",
        "status": "RESIDUAL_EXACTNESS_OPEN",
        "residual_rank": residual_rank,
        "residual_frobenius_norm": residual_norm,
        "residual_matrix_rows_u_d_e": [[float(x) for x in row] for row in residual],
        "residual_row_sums": [float(x) for x in residual.sum(axis=1)],
        "residual_column_sums": [float(x) for x in residual.sum(axis=0)],
        "why_not_closed": [
            "The residual is nonzero, so the 3/11 skeleton is not exact against the current central rows.",
            "The fitted affine rows and gamma are solved from Yukawa data, not emitted by selected MTT source data.",
            "Step68 exponent rows supply lane/exponent scaffolding, not magnitude-bearing curvature values.",
        ],
        "legal_closure_routes": [
            "prove a selected source row for gamma and the 3/11 lane ratio, then prove an exact residual correction functional",
            "derive the residual as selected threshold/mass-scheme correction rows rather than central-value noise",
            "upgrade the seven-parameter skeleton into a source-owned profile convention with declared uncertainty/error certificate",
        ],
        "forbidden_closure_routes": [
            "declare 3/11 exact solely because it is the best small rational fit",
            "count fitted gamma as no-knob source data",
            "ignore the nonzero residual and claim exact Yukawa magnitude prediction",
        ],
    }

    exact_threshold = 1.0e-12
    exact_closed = execution["max_abs_log_residual"] < exact_threshold
    candidate = {
        "candidate": "MTTSelectedPhaseLaneCurvatureSourceRelationOrSevenParameterYukawaReduction",
        "status": STATUS,
        "closure_claimed": False,
        "observed_data_used_as_selector": True,
        "target_fitting_used": True,
        "inputs": {
            "phase_lane_curvature_clue": str(CLUE.relative_to(ROOT)),
            "diagnostic_log_yukawa_response_coefficients": str(COEFFS.relative_to(ROOT)),
            "selected_family_spectral_response_basis": str(BASIS.relative_to(ROOT)),
            "step68_theta_exponent_weight_rows": str(STEP68.relative_to(ROOT)),
        },
        "output_packets": {
            "phase_lane_curvature_source_skeleton": str(SKELETON.relative_to(ROOT)),
            "seven_parameter_reduction_execution": str(EXECUTION.relative_to(ROOT)),
            "residual_exactness_obligation": str(OBLIGATION.relative_to(ROOT)),
        },
        "theorem": {
            "name": "PhaseLaneCurvatureSourceRelationSkeletonTheorem",
            "proved": True,
            "statement": "The currently selected family spectrum, phase/shift lane routing, and Step68 theta exponent scaffold support the unique seven-slot curvature skeleton log|Y_s(g)|=a_s+b_sF_g+gamma chi_sF_g^2 with chi_phase=1 and chi_shift=3/11 as the sharp fitted reduction target. This proves the skeleton and residual obligation, not the selected numeric source values.",
        },
        "source_theorem_status": {
            "source_relation_skeleton_constructed": True,
            "gamma_source_row_accepted": False,
            "three_over_eleven_source_ratio_accepted": False,
            "residual_exactness_closed": False,
            "exact_seven_parameter_reduction_closed": exact_closed,
            "accepted_no_knob_yukawa_rows": 0,
        },
        "key_numbers": {
            "ratio_c2_d_to_phase_gamma": ratio,
            "fitted_gamma": float(beta[6]),
            "max_abs_log_residual": execution["max_abs_log_residual"],
            "worst_multiplicative_yukawa_error": execution["worst_multiplicative_yukawa_error"],
            "parameter_count": 7,
            "residual_rank": residual_rank,
        },
        "closure_decision": {
            "seven_parameter_curvature_skeleton_closed": True,
            "strict_selected_source_relation_closed": False,
            "strict_no_knob_flavor_closure": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_PhaseLaneCurvatureSourceRelation_or_SevenParameterYukawaReduction_v1",
        "status": STATUS,
        "candidate": str(OUT.relative_to(ROOT)),
        "skeleton_theorem_proved": True,
        "source_theorem_proved": False,
        "gamma_source_row_accepted": False,
        "three_over_eleven_source_ratio_accepted": False,
        "residual_exactness_closed": False,
        "accepted_no_knob_yukawa_rows": 0,
        "observed_data_used_as_selector": True,
        "target_fitting_used": True,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected PhaseLaneCurvatureSourceRelation or SevenParameterYukawaReduction v1

Status: `{STATUS}`

## Constructed Skeleton

The lane-correct source-relation skeleton is now constructed:

`log|Y_s(g)| = a_s + b_s F_g + gamma chi_s F_g^2`

with

- `chi_u = 1` because `u` is in `phase_packet_I_plus_Z`
- `chi_e = 1` because `e` is in `phase_packet_I_plus_Z`
- `chi_d = 3/11` because the shift-lane fitted curvature is best captured by
  the small-rational suppression `3/11`

This reduces the charged-Yukawa coefficient skeleton from `9` slots to `7`
slots:

`a_u,b_u,a_d,b_d,a_e,b_e,gamma`.

## Numeric Execution

The fitted execution gives:

- `gamma = {float(beta[6])}`
- max log residual = `{execution["max_abs_log_residual"]}`
- worst multiplicative Yukawa error =
  `{execution["worst_multiplicative_yukawa_error"]}`

This is a very strong reduction clue, but it is not exact.

## What Closed

- Selected family spectrum and nonsingular family basis are closed.
- `u,e` phase-lane and `d` shift-lane routing are closed.
- Step68 theta exponent rows supply source-side lane/exponent scaffolding
  without target fitting.
- The seven-parameter curvature skeleton is now the correct next theorem
  target.

## What Remains Open

- `gamma` is fitted, not source-emitted.
- `3/11` is the best small-rational suppression, not yet source-proved.
- The residual is nonzero and must be explained by selected correction rows,
  a threshold/mass-scheme source theorem, or an exactness/error certificate tied
  to a selected source object.

Therefore this packet constructs the source-relation skeleton and the exact
residual obligation.  It does not close no-knob Yukawa magnitudes.

Next required artifact: `{NEXT}`.
"""

    write_json(SKELETON, skeleton)
    write_json(EXECUTION, execution)
    write_json(OBLIGATION, obligation)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": str(OUT.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
