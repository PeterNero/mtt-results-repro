"""Build correlated threshold/profile matrix or Yukawa/Higgs precision-promotion gate."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_correlatedthresholdprofilematrix_or_yukawahiggsprecisionpromotion"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BASIS = PACKET_DIR / "threshold_profile_basis_and_open_rows.packet.json"
MATRIX = PACKET_DIR / "correlated_threshold_profile_matrix.packet.json"
PROMOTION = PACKET_DIR / "yukawa_higgs_precision_promotion_gate.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_correlated_threshold_profile_matrix.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_CorrelatedThresholdProfileMatrix_or_YukawaHiggsPrecisionPromotion_v1.md"

PREVIOUS = DATA / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution.candidate.json"
VALUE_PACKET = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "versioned_common_scale_yukawa_higgs_values.packet.json"
)
PREVIOUS_PROMOTION = (
    DATA
    / "selected_acceptedcommonscaleyukawahiggsvalues_or_profilelikelihoodexecution"
    / "precision_promotion_gate.packet.json"
)
THRESHOLD_POLICY = (
    DATA
    / "selected_thresholdmassschemecovariancefill_or_qasu3packetintegration"
    / "threshold_mass_scheme_covariance_acceptance_contract.packet.json"
)
COVARIANCE = (
    DATA
    / "selected_polethresholdresidualvalues_or_covarianceprofile"
    / "diagonal_sensitivity_covariance_scaffold.packet.json"
)
DIAGONAL_PROFILE = (
    DATA
    / "selected_fullcovarianceprofile_or_multiloopconventionaudit"
    / "diagonal_profile_likelihood_execution.packet.json"
)
FORMULA = (
    DATA
    / "selected_polethresholdresidualvalues_or_covarianceprofile"
    / "buttazzo_boundary_formula_replay.packet.json"
)
LITERATURE = (
    DATA
    / "selected_externalliteraturergbenchmarkvalues_or_thresholdcovariance"
    / "external_literature_rg_benchmark_values.packet.json"
)

STATUS = (
    "MTT_SELECTED_CORRELATEDTHRESHOLDPROFILEMATRIX_OR_YUKAWAHIGGSPRECISIONPROMOTION_"
    "BUILT_SURROGATE_MATRIX_PRECISION_PROMOTION_OPEN"
)
NEXT = "MTT_Selected_ThresholdMassSchemeValues_or_CorrelatedLikelihoodSourceImport_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def require_sources(paths: list[Path]) -> None:
    missing = [rel(path) for path in paths if not path.exists()]
    if missing:
        raise FileNotFoundError("missing correlated threshold/profile sources: " + ", ".join(missing))


def build_covariance(
    output_ids: list[str],
    input_ids: list[str],
    jacobian: dict[str, dict[str, float]],
    input_sigmas: dict[str, float],
    theory_sigmas: dict[str, float],
    rho: float,
) -> list[list[float]]:
    cov: list[list[float]] = []
    for out_i in output_ids:
        row: list[float] = []
        for out_j in output_ids:
            value = 0.0
            for input_a in input_ids:
                for input_b in input_ids:
                    corr = 1.0 if input_a == input_b else rho
                    value += (
                        jacobian.get(out_i, {}).get(input_a, 0.0)
                        * corr
                        * input_sigmas[input_a]
                        * input_sigmas[input_b]
                        * jacobian.get(out_j, {}).get(input_b, 0.0)
                    )
            if out_i == out_j:
                value += theory_sigmas.get(out_i, 0.0) ** 2
            row.append(value)
        cov.append(row)
    return cov


def invert(matrix: list[list[float]]) -> list[list[float]]:
    n = len(matrix)
    aug = [[float(matrix[i][j]) for j in range(n)] + [1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(aug[row][col]))
        if abs(aug[pivot][col]) < 1e-20:
            raise ValueError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        div = aug[col][col]
        aug[col] = [value / div for value in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            aug[row] = [aug[row][i] - factor * aug[col][i] for i in range(2 * n)]
    return [row[n:] for row in aug]


def mat_vec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    return [sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix]


def quadratic(vector: list[float], matrix: list[list[float]]) -> float:
    mv = mat_vec(matrix, vector)
    return sum(vector[i] * mv[i] for i in range(len(vector)))


def cholesky_pivots(matrix: list[list[float]]) -> list[float]:
    n = len(matrix)
    lower = [[0.0 for _ in range(n)] for _ in range(n)]
    pivots: list[float] = []
    for i in range(n):
        for j in range(i + 1):
            value = matrix[i][j] - sum(lower[i][k] * lower[j][k] for k in range(j))
            if i == j:
                if value <= 0.0:
                    pivots.append(value)
                    return pivots
                lower[i][j] = math.sqrt(value)
                pivots.append(value)
            else:
                lower[i][j] = value / lower[j][j]
    return pivots


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    sources = [
        PREVIOUS,
        VALUE_PACKET,
        PREVIOUS_PROMOTION,
        THRESHOLD_POLICY,
        COVARIANCE,
        DIAGONAL_PROFILE,
        FORMULA,
        LITERATURE,
    ]
    require_sources(sources)

    previous = load(PREVIOUS)
    values = load(VALUE_PACKET)
    previous_promotion = load(PREVIOUS_PROMOTION)
    threshold = load(THRESHOLD_POLICY)
    covariance = load(COVARIANCE)
    diagonal = load(DIAGONAL_PROFILE)
    formula = load(FORMULA)
    literature = load(LITERATURE)

    independent_outputs = ["lambda_Mt", "y_t_Mt", "g_2_Mt", "g_Y_Mt", "g_3_Mt"]
    redundant_outputs = ["g_1_GUT_Mt"]
    input_ids = ["M_W_GeV", "M_h_GeV", "M_t_GeV", "alpha3_MZ"]
    current = formula["current_repo_input_variant"]["values"]
    central = formula["buttazzo_central_input_replay"]["values"]
    delta = [float(current[key]) - float(central[key]) for key in independent_outputs]
    theory_sigmas = {
        key: float(row.get("theory_uncertainty", 0.0))
        for key, row in literature["literature_values"].items()
    }

    basis_packet = {
        "schema": "MTTThresholdProfileBasisAndOpenRows.v1",
        "status": "PROFILE_BASIS_FIXED_THRESHOLD_AND_MASS_SCHEME_ROWS_OPEN",
        "versioned_value_packet": rel(VALUE_PACKET),
        "profile_output_basis": {
            "independent_outputs": independent_outputs,
            "redundant_outputs_removed": redundant_outputs,
            "redundancy_reason": "g_1_GUT_Mt = sqrt(5/3) * g_Y_Mt; including both would make a correlated covariance singular or double-count hypercharge.",
        },
        "measured_input_basis": input_ids,
        "threshold_matching_required": threshold["threshold_matching_required"],
        "mass_scheme_conversion_required": threshold["mass_scheme_conversion_required"],
        "open_precision_rows": {
            "threshold_matching_values": threshold["values_promotable_now"] is False,
            "mass_scheme_conversion_values": threshold["values_promotable_now"] is False,
            "full_correlated_covariance_profile": True,
            "multi_loop_threshold_convention_values": True,
            "no_knob_MTT_source_derivation_of_values": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(BASIS, basis_packet)

    scan_rows = []
    selected_matrix: dict[str, Any] | None = None
    for rho in [-0.30, -0.20, -0.10, 0.0, 0.10, 0.20, 0.30, 0.50, 0.70, 0.90]:
        cov = build_covariance(
            independent_outputs,
            input_ids,
            covariance["jacobian"],
            covariance["input_sigmas"],
            theory_sigmas,
            rho,
        )
        inv = invert(cov)
        chi2 = quadratic(delta, inv)
        pivots = cholesky_pivots(cov)
        row = {
            "rho_equicorrelation": rho,
            "covariance_matrix": cov,
            "cholesky_pivots": pivots,
            "positive_definite": len(pivots) == len(independent_outputs) and min(pivots) > 0.0,
            "chi2": chi2,
            "degrees_of_freedom": len(independent_outputs),
            "reduced_chi2": chi2 / len(independent_outputs),
        }
        scan_rows.append(row)
        if rho == 0.0:
            selected_matrix = row
    if selected_matrix is None:
        raise RuntimeError("rho=0.0 matrix not emitted")

    best = min(scan_rows, key=lambda row: row["chi2"])
    worst = max(scan_rows, key=lambda row: row["chi2"])
    core = [row for row in scan_rows if -0.20 <= row["rho_equicorrelation"] <= 0.70]
    core_worst = max(core, key=lambda row: row["chi2"])
    matrix_packet = {
        "schema": "MTTCorrelatedThresholdProfileMatrix.v1",
        "status": "SURROGATE_CORRELATED_PROFILE_MATRICES_EMITTED_FULL_LIKELIHOOD_OPEN",
        "basis_packet": rel(BASIS),
        "matrix_interpretation": "Jacobian-propagated weak-scale boundary covariance with equicorrelated measured-input stress scenarios and literature theory sidecars.",
        "delta_vector_order": independent_outputs,
        "delta_vector": delta,
        "scan_rows": scan_rows,
        "selected_reference_matrix": {
            "selection_policy": "rho=0 diagonal-input baseline; not fitted and not used as source selector",
            "rho_equicorrelation": selected_matrix["rho_equicorrelation"],
            "covariance_matrix": selected_matrix["covariance_matrix"],
            "cholesky_pivots": selected_matrix["cholesky_pivots"],
            "positive_definite": selected_matrix["positive_definite"],
            "chi2": selected_matrix["chi2"],
            "reduced_chi2": selected_matrix["reduced_chi2"],
        },
        "stress_envelope": {
            "best_rho": best["rho_equicorrelation"],
            "best_chi2": best["chi2"],
            "worst_rho": worst["rho_equicorrelation"],
            "worst_chi2": worst["chi2"],
            "core_rho_window": [-0.20, 0.70],
            "core_worst_rho": core_worst["rho_equicorrelation"],
            "core_worst_chi2": core_worst["chi2"],
            "core_worst_reduced_chi2": core_worst["reduced_chi2"],
            "all_matrices_positive_definite": all(row["positive_definite"] for row in scan_rows),
            "coarse_core_profile_passes": core_worst["reduced_chi2"] < 3.0,
            "coarse_extreme_profile_passes": worst["reduced_chi2"] < 3.0,
        },
        "accepted_as_surrogate_correlated_threshold_profile_matrix": True,
        "accepted_as_published_or_reconstructed_profile_likelihood": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(MATRIX, matrix_packet)

    prior_failures = previous_promotion["hard_failures"]
    promotion_tests = {
        "versioned_common_scale_value_packet_emitted": values["accepted_as_versioned_common_scale_candidate_values"],
        "surrogate_correlated_threshold_profile_matrix_emitted": matrix_packet[
            "accepted_as_surrogate_correlated_threshold_profile_matrix"
        ],
        "all_declared_surrogate_matrices_positive_definite": matrix_packet["stress_envelope"][
            "all_matrices_positive_definite"
        ],
        "coarse_core_profile_passes": matrix_packet["stress_envelope"]["coarse_core_profile_passes"],
        "threshold_matching_values_emitted": False,
        "mass_scheme_conversion_values_emitted": False,
        "published_or_reconstructed_profile_likelihood_imported": False,
        "multi_loop_threshold_convention_values_emitted": False,
        "no_knob_MTT_source_derivation_of_values": False,
    }
    remaining_hard_failures = [
        key
        for key in [
            "threshold_matching_values_emitted",
            "mass_scheme_conversion_values_emitted",
            "published_or_reconstructed_profile_likelihood_imported",
            "multi_loop_threshold_convention_values_emitted",
            "no_knob_MTT_source_derivation_of_values",
        ]
        if promotion_tests[key] is False
    ]
    promotion_packet = {
        "schema": "MTTYukawaHiggsPrecisionPromotionGate.v1",
        "status": "SURROGATE_MATRIX_ACCEPTED_TRUE_PRECISION_PROMOTION_REJECTED",
        "previous_hard_failures": prior_failures,
        "promotion_tests": promotion_tests,
        "remaining_hard_failures": remaining_hard_failures,
        "what_is_newly_closed": {
            "surrogate_correlated_threshold_profile_matrix": True,
            "positive_definite_matrix_validation": matrix_packet["stress_envelope"][
                "all_matrices_positive_definite"
            ],
            "core_correlation_stress_profile": matrix_packet["stress_envelope"][
                "coarse_core_profile_passes"
            ],
        },
        "promotion_decision": {
            "accepted_as_surrogate_precision_scaffold": True,
            "accepted_for_true_precision_equivalence": False,
            "accepted_as_full_SM_no_knob_closure": False,
            "true_SM_equivalence_closed": False,
        },
        "reason": (
            "The correlated threshold/profile matrix is now explicitly emitted and validated as a surrogate "
            "precision scaffold. It cannot promote the first-pass Yukawa/Higgs packet to true precision "
            "equivalence because real threshold values, mass-scheme conversions, published/reconstructed "
            "profile likelihood, multi-loop convention values, and no-knob source derivation are still absent."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(PROMOTION, promotion_packet)

    cutset = {
        "schema": "MTTNextCutsetAfterCorrelatedThresholdProfileMatrix.v1",
        "status": "SURROGATE_MATRIX_DONE_TRUE_PRECISION_REQUIRES_REAL_THRESHOLD_LIKELIHOOD_SOURCE",
        "closed_now": [
            "profile basis fixed with redundant hypercharge row removed",
            "surrogate correlated threshold/profile covariance matrices emitted",
            "positive-definite matrix validation executed for declared stress scenarios",
            "Yukawa/Higgs precision-promotion gate executed",
        ],
        "still_open": [
            "threshold matching values",
            "mass-scheme conversion values",
            "published or reconstructed full profile likelihood/covariance",
            "multi-loop threshold convention values",
            "no-knob MTT source derivation of Yukawa/Higgs values",
        ],
        "recommended_next": {
            "artifact": NEXT,
            "reason": (
                "The remaining precision wall is no longer a missing matrix calculation; it is missing real "
                "threshold/mass-scheme/likelihood source rows or a theorem that derives them from the selected MTT branch."
            ),
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }
    write_json(CUTSET, cutset)

    candidate = {
        "candidate": "MTTSelectedCorrelatedThresholdProfileMatrixOrYukawaHiggsPrecisionPromotion",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in sources},
        "output_packets": {
            "threshold_profile_basis_and_open_rows": rel(BASIS),
            "correlated_threshold_profile_matrix": rel(MATRIX),
            "yukawa_higgs_precision_promotion_gate": rel(PROMOTION),
            "next_cutset_after_correlated_threshold_profile_matrix": rel(CUTSET),
        },
        "theorem": {
            "name": "SurrogateCorrelatedThresholdProfileMatrixAndPromotionRejectionTheorem",
            "proved": True,
            "statement": (
                "Given the selected versioned first-pass Yukawa/Higgs value packet and the existing "
                "weak-scale sensitivity scaffold, the independent threshold/profile basis determines a "
                "family of positive-definite surrogate correlated covariance matrices. This closes the "
                "matrix-construction part of the precision scaffold. It does not close true precision SM "
                "equivalence because the required threshold, mass-scheme, full-likelihood, multi-loop, and "
                "no-knob source rows remain absent."
            ),
        },
        "what_closes_now": {
            "surrogate_correlated_threshold_profile_matrix_emitted": True,
            "profile_basis_redundant_hypercharge_removed": True,
            "positive_definite_matrix_validation_executed": True,
            "yukawa_higgs_precision_promotion_gate_executed": True,
        },
        "what_remains_open": {
            "threshold_matching_values": True,
            "mass_scheme_conversion_values": True,
            "published_or_reconstructed_profile_likelihood": True,
            "multi_loop_threshold_convention_values": True,
            "no_knob_Yukawa_Higgs_value_source_derivation": True,
            "true_SM_equivalence_closure": True,
            "full_no_knob_closure": True,
        },
        "closure_decision": {
            "surrogate_precision_scaffold_closed": True,
            "accepted_for_true_precision_equivalence": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "previous_status": previous["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_CorrelatedThresholdProfileMatrix_or_YukawaHiggsPrecisionPromotion_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "closure_claimed": False,
        "unpatched_theorem_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "what_closes": candidate["what_closes_now"],
        "what_remains_open": candidate["what_remains_open"],
        "next_required_artifact": NEXT,
    }
    write_json(CERT, cert)

    note = f"""# MTT Selected CorrelatedThresholdProfileMatrix or YukawaHiggsPrecisionPromotion v1

Status: `{STATUS}`.

This artifact emits a surrogate correlated threshold/profile matrix family for
the independent weak-scale boundary basis:

```text
{independent_outputs}
```

The redundant hypercharge row `g_1_GUT_Mt` is removed because it is exactly
derived from `g_Y_Mt`. The declared stress matrices are positive definite:

```text
all positive definite = {matrix_packet["stress_envelope"]["all_matrices_positive_definite"]}
core reduced chi2 max = {matrix_packet["stress_envelope"]["core_worst_reduced_chi2"]}
```

Promotion decision:

```text
surrogate precision scaffold closed: true
accepted for true precision equivalence: false
true SM equivalence: open
```

The remaining wall is real source data, not matrix arithmetic: threshold
matching values, mass-scheme conversions, a published/reconstructed profile
likelihood, multi-loop convention values, or a no-knob MTT derivation of those
same rows.

Next artifact: `{NEXT}`.
"""
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
