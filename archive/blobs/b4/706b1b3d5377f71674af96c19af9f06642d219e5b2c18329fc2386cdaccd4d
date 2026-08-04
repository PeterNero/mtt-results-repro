"""Build Higgs QCD precision-threshold row gate and correlation stress profile."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_higgsqcdprecisionthresholdrows_or_correlatedprofileupgrade"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
THRESHOLD_GATE = PACKET_DIR / "higgs_qcd_precision_threshold_row_gate.packet.json"
STRESS = PACKET_DIR / "higgs_qcd_correlation_stress_profile.packet.json"
DECISION = PACKET_DIR / "higgs_qcd_precision_promotion_decision_after_stress.packet.json"
UPDATED_TRUE = PACKET_DIR / "updated_true_equivalence_gate_after_qcd_stress_profile.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HiggsQCDPrecisionThresholdRows_or_CorrelatedProfileUpgrade_v1.md"

STATUS = "MTT_SELECTED_HIGGSQCDPRECISIONTHRESHOLDROWS_OR_CORRELATEDPROFILEUPGRADE_BUILT_STRESS_PROFILE_PRECISION_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def invert(matrix: list[list[float]]) -> list[list[float]]:
    n = len(matrix)
    aug = [[float(matrix[i][j]) for j in range(n)] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(aug[row][col]))
        if abs(aug[pivot][col]) < 1e-30:
            raise ValueError("singular covariance matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [value / scale for value in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            aug[row] = [aug[row][k] - factor * aug[col][k] for k in range(2 * n)]
    return [row[n:] for row in aug]


def matvec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def quad(vector: list[float], matrix: list[list[float]]) -> float:
    mv = matvec(matrix, vector)
    return sum(vector[i] * mv[i] for i in range(len(vector)))


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)

    previous = load(DATA / "selected_higgsqcdnonfitformulavalueexecution_or_forwardreplay.candidate.json")
    execution = load(
        DATA
        / "selected_higgsqcdnonfitformulavalueexecution_or_forwardreplay"
        / "higgs_qcd_nonfit_formula_execution.packet.json"
    )
    replay = load(
        DATA
        / "selected_higgsqcdnonfitformulavalueexecution_or_forwardreplay"
        / "higgs_qcd_forward_replay_after_nonfit_formula_execution.packet.json"
    )
    block = load(
        DATA
        / "selected_higgsqcdrepairvalues_or_profilecovarianceblock"
        / "qcd_diagonal_profile_block.packet.json"
    )
    previous_true = load(
        DATA
        / "selected_higgsqcdnonfitformulavalueexecution_or_forwardreplay"
        / "updated_true_equivalence_gate_after_nonfit_qcd_formula_replay.packet.json"
    )

    threshold_rows = [
        {
            "channel": "H_to_ss",
            "firstpass_formula_value_present": True,
            "precision_threshold_value_filled": False,
            "minimum_precision_terms": [
                "multi-loop m_s(2 GeV) to m_H running with threshold matching",
                "declared MSbar strange-mass and alpha_s covariance",
                "EW and mixed QCD/EW corrections",
                "forward replay after values are computed",
            ],
            "qasu3_requirement": "SM-parity attachment closed; actual no-knob Qa/SU3 still required for no-knob precision source closure",
        },
        {
            "channel": "H_to_gg",
            "firstpass_formula_value_present": True,
            "precision_threshold_value_filled": False,
            "minimum_precision_terms": [
                "finite top, bottom, and charm loop functions with interference",
                "NNLO/N3LO QCD K factors and threshold matching",
                "alpha_s and heavy-quark mass covariance",
                "forward replay after values are computed",
            ],
            "qasu3_requirement": "SM-parity attachment closed; actual no-knob Qa/SU3 still required for no-knob precision source closure",
        },
    ]

    threshold_gate = {
        "schema": "MTTHiggsQCDPrecisionThresholdRowGate.v1",
        "status": "PRECISION_THRESHOLD_ROW_GATE_BUILT_VALUES_OPEN",
        "rows": threshold_rows,
        "firstpass_nonfit_formula_values_available": execution["accepted_formula_value_count"] == 2,
        "precision_threshold_values_filled": False,
        "precision_threshold_values_promotable": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    channels = block["channels"]
    residuals = [float(value) for value in block["residual_vector_GeV"]]
    sigmas = [float(block["covariance_matrix_GeV2"][i][i]) ** 0.5 for i in range(len(channels))]
    rho_values = [-0.25, 0.0, 0.25, 0.50]
    stress_rows = []
    for rho in rho_values:
        covariance = []
        for i in range(len(channels)):
            row = []
            for j in range(len(channels)):
                row.append(sigmas[i] * sigmas[j] * (1.0 if i == j else rho))
            covariance.append(row)
        inverse = invert(covariance)
        chi_square = quad(residuals, inverse)
        stress_rows.append(
            {
                "rho": rho,
                "covariance_model": "equicorrelated QCD block stress test",
                "minimum_eigenvalue_positive_by_equicorrelation_bound": rho > -1.0 / (len(channels) - 1) and rho < 1.0,
                "diagonal_chi_square": chi_square,
                "accepted_as_full_correlated_profile": False,
                "accepted_as_correlation_stress_test": True,
            }
        )

    chi_values = [row["diagonal_chi_square"] for row in stress_rows]
    stress = {
        "schema": "MTTHiggsQCDCorrelationStressProfile.v1",
        "status": "QCD_CORRELATION_STRESS_PROFILE_BUILT_FULL_PROFILE_OPEN",
        "channels": channels,
        "rho_grid": rho_values,
        "rows": stress_rows,
        "summary": {
            "stress_models_checked": len(stress_rows),
            "all_models_psd_by_equicorrelation_bound": all(
                row["minimum_eigenvalue_positive_by_equicorrelation_bound"] for row in stress_rows
            ),
            "min_chi_square": min(chi_values),
            "max_chi_square": max(chi_values),
            "diagonal_chi_square": next(row["diagonal_chi_square"] for row in stress_rows if row["rho"] == 0.0),
            "accepted_as_correlation_stress_profile": True,
            "accepted_as_full_correlated_profile": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTHiggsQCDPrecisionPromotionDecisionAfterStress.v1",
        "status": "STRESS_PROFILE_BUILT_PRECISION_PROMOTION_STILL_REJECTED",
        "firstpass_formula_values_filled": True,
        "correlation_stress_profile_built": True,
        "full_correlated_profile_filled": False,
        "precision_threshold_values_filled": False,
        "values_promotable_to_precision_now": False,
        "blocked_by": [
            "H_to_ss precision threshold value not filled",
            "H_to_gg precision threshold value not filled",
            "stress profile is not an empirical full covariance/profile likelihood",
            "actual no-knob Qa/SU3 operator packet remains open",
        ],
        "replay_summary_import": replay["summary"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    updated_true = {
        "schema": "MTTUpdatedTrueEquivalenceGateAfterQCDStressProfile.v1",
        "status": "QCD_STRESS_PROFILE_BUILT_TRUE_EQUIVALENCE_STILL_OPEN",
        "previous_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "closed_now": previous_true["closed_now"] + [
            "Higgs QCD precision-threshold acceptance matrix",
            "equicorrelated QCD covariance stress profile",
        ],
        "remaining_true_equivalence_blockers": previous_true["remaining_true_equivalence_blockers"],
        "next_primary_value_gate": "fill actual precision H_to_ss/H_to_gg threshold formula values or empirical full correlated QCD covariance profile",
        "guardrails": {
            "stress_profile_not_full_profile_likelihood": True,
            "precision_threshold_values_filled": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHiggsQCDPrecisionThresholdRowsOrCorrelatedProfileUpgrade",
        "status": STATUS,
        "inputs": {
            "previous_candidate": rel(DATA / "selected_higgsqcdnonfitformulavalueexecution_or_forwardreplay.candidate.json"),
            "qcd_profile_block": rel(
                DATA
                / "selected_higgsqcdrepairvalues_or_profilecovarianceblock"
                / "qcd_diagonal_profile_block.packet.json"
            ),
            "firstpass_formula_execution": rel(
                DATA
                / "selected_higgsqcdnonfitformulavalueexecution_or_forwardreplay"
                / "higgs_qcd_nonfit_formula_execution.packet.json"
            ),
        },
        "output_packets": {
            "precision_threshold_row_gate": rel(THRESHOLD_GATE),
            "correlation_stress_profile": rel(STRESS),
            "precision_promotion_decision": rel(DECISION),
            "updated_true_equivalence_gate": rel(UPDATED_TRUE),
        },
        "theorem": {
            "name": "HiggsQCDCorrelationStressProfileAndPrecisionGateTheorem",
            "proved": True,
            "statement": (
                "Given the first-pass non-fit QCD formula replay and diagonal QCD profile block, the repo "
                "can construct a benchmark-independent precision-threshold acceptance matrix and an "
                "equicorrelated QCD covariance stress profile. This advances profile robustness checks, "
                "but it is not a full empirical correlated likelihood and does not promote precision QCD values."
            ),
        },
        "what_closes_now": {
            "precision_threshold_acceptance_matrix": True,
            "equicorrelated_QCD_stress_profile": True,
            "PSD_stress_grid_check": True,
            "precision_promotion_decision_recorded": True,
        },
        "what_remains_open": {
            "precision_H_to_ss_threshold_formula_value": True,
            "precision_H_to_gg_threshold_formula_value": True,
            "empirical_full_correlated_QCD_profile": True,
            "actual_QaSU3_operator_packet_no_knob": True,
            "true_SM_equivalence": True,
            "no_knob_closure": True,
        },
        "closure_decision": {
            "correlation_stress_profile_built": True,
            "full_correlated_profile_filled": False,
            "precision_threshold_values_filled": False,
            "values_promotable_to_precision_now": False,
            "true_SM_equivalence_closed": False,
            "no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    cert = {
        "certificate": "MTT_Selected_HiggsQCDPrecisionThresholdRows_or_CorrelatedProfileUpgrade_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "correlation_stress_profile_built": True,
        "full_correlated_profile_filled": False,
        "precision_threshold_values_filled": False,
        "values_promotable_to_precision_now": False,
        "true_SM_equivalence_closed": False,
        "no_knob_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_HiggsQCDPrecisionFormulaValues_or_EmpiricalFullProfile_v1",
    }

    note = f"""# MTT Selected HiggsQCDPrecisionThresholdRows or CorrelatedProfileUpgrade v1

Status: `{STATUS}`.

This artifact builds the precision-threshold acceptance gate for `H_to_ss` and
`H_to_gg`, then executes an equicorrelated QCD covariance stress profile over
the existing four-channel QCD block. The stress profile is a robustness check,
not a full empirical covariance/profile likelihood.

Precision QCD values, the empirical full correlated profile, true SM
equivalence, and no-knob Qa/SU3 remain open.
"""

    for path, payload in [
        (THRESHOLD_GATE, threshold_gate),
        (STRESS, stress),
        (DECISION, decision),
        (UPDATED_TRUE, updated_true),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
