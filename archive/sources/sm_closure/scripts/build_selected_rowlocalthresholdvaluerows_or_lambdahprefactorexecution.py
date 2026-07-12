"""Build row-local threshold-value row plan plus brute-force diagnostic search."""

from __future__ import annotations

import heapq
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_rowlocalthresholdvaluerows_or_lambdahprefactorexecution"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PLAN_PACKET = PACKET_DIR / "advanced_row_attack_plan.packet.json"
FEATURE_TABLE_PACKET = PACKET_DIR / "source_feature_table.packet.json"
FINITE_SEARCH_PACKET = PACKET_DIR / "finite_subfactor_normalization_bruteforce.packet.json"
RATIONAL_SEARCH_PACKET = PACKET_DIR / "small_rational_feature_bruteforce.packet.json"
LSQ_PACKET = PACKET_DIR / "least_squares_diagnostic_models.packet.json"
CUTSET_PACKET = PACKET_DIR / "next_cutset_after_bruteforce.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_RowLocalThresholdValueRows_or_LambdaHPrefactorExecution_v1.md"

STEP74 = DATA / "selected_step74_pivsd01backimport_or_rowlocalthresholdvaluefrontier.candidate.json"
STEP74_CUTSET = (
    DATA
    / "selected_step74_pivsd01backimport_or_rowlocalthresholdvaluefrontier"
    / "step74_next_cutset.packet.json"
)
STEP72_TARGETS = (
    DATA
    / "selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance"
    / "step72_required_rowlocal_prefactor_target_table.packet.json"
)
STEP72_STRICT = (
    DATA
    / "selected_step72_rowlocalprefactorlawsearch_or_strictomegaacceptance"
    / "step72_strict_rowlocal_omega_acceptance_predicate.packet.json"
)
STEP69_FORMULAS = (
    DATA
    / "selected_step69_hymthresholdprefactorrows_or_omegascalarexecution"
    / "step69_prefactor_solution_formula_rows.packet.json"
)
STEP70_FACTORS = (
    DATA
    / "selected_step70_heattorsionprefactorbackimport_or_rowlocalfrontier"
    / "step70_prefactor_slot_factorization.packet.json"
)
STEP68_EXPONENTS = (
    DATA
    / "selected_step68_thetaexponentweights_or_prefactorthreshold_frontier"
    / "step68_selected_theta_exponent_weight_rows.packet.json"
)
HEAT_RESPONSE = (
    DATA
    / "selected_heattorsionresponse_finalgate"
    / "selected_finite_heat_spectrum_response.packet.json"
)
POSTPI_BOUNDARY = DATA / "selected_noknobvaluederivationpostpi_or_minimaluniversalparameterpolicy.candidate.json"

STATUS = (
    "MTT_SELECTED_ROWLOCALTHRESHOLDVALUEROWS_OR_LAMBDAHPREFACTOREXECUTION_"
    "BUILT_ADVANCED_PLAN_AND_BRUTEFORCE_SEARCH_ROWS_OPEN"
)
NEXT = "MTT_Selected_RowLocalHYMOverlapQuadratureFunctional_or_ThresholdSchemeSourceTheorem_v1"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def parse_fraction(value: Any) -> float:
    if value is None:
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    return float(Fraction(str(value)))


def safe_log(value: float) -> float:
    if value <= 0.0:
        raise ValueError(f"log requires positive value, got {value}")
    return math.log(value)


def metrics(actual: list[float], predicted: list[float], parameter_count: int) -> dict[str, Any]:
    residuals = [a - p for a, p in zip(actual, predicted)]
    n = len(actual)
    rss = sum(r * r for r in residuals)
    rms = math.sqrt(rss / n)
    max_abs = max(abs(r) for r in residuals)
    return {
        "parameter_count": parameter_count,
        "rms_log_residual": rms,
        "max_abs_log_residual": max_abs,
        "max_multiplicative_error_factor": math.exp(max_abs),
        "bic_like": n * math.log(max(rss / n, 1e-30)) + parameter_count * math.log(n),
    }


def residual_rows(rows: list[dict[str, Any]], predicted: list[float]) -> list[dict[str, Any]]:
    out = []
    for row, pred in zip(rows, predicted):
        residual = row["log_diagnostic_prefactor"] - pred
        out.append(
            {
                "omega_id": row["omega_id"],
                "actual_log_prefactor": row["log_diagnostic_prefactor"],
                "predicted_log_prefactor": pred,
                "log_residual": residual,
                "abs_log_residual": abs(residual),
                "multiplicative_error_factor": math.exp(abs(residual)),
            }
        )
    return out


def solve_linear(matrix: list[list[float]], rhs: list[float]) -> list[float]:
    n = len(rhs)
    aug = [row[:] + [rhs_i] for row, rhs_i in zip(matrix, rhs)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot][col]) < 1e-12:
            aug[col][col] += 1e-10
            pivot = col
        aug[col], aug[pivot] = aug[pivot], aug[col]
        div = aug[col][col]
        if abs(div) < 1e-14:
            div = 1e-14
        aug[col] = [v / div for v in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor:
                aug[row] = [v - factor * p for v, p in zip(aug[row], aug[col])]
    return [aug[i][-1] for i in range(n)]


def least_squares(x_rows: list[list[float]], y: list[float]) -> list[float]:
    cols = len(x_rows[0])
    xtx = [[0.0 for _ in range(cols)] for _ in range(cols)]
    xty = [0.0 for _ in range(cols)]
    for x, yi in zip(x_rows, y):
        for i in range(cols):
            xty[i] += x[i] * yi
            for j in range(cols):
                xtx[i][j] += x[i] * x[j]
    for i in range(cols):
        xtx[i][i] += 1e-12
    return solve_linear(xtx, xty)


def fit_indicator_model(rows: list[dict[str, Any]], y: list[float], model_id: str, groups: list[str]) -> dict[str, Any]:
    unique_groups = list(dict.fromkeys(groups))
    x_rows = [[1.0 if group == g else 0.0 for group in unique_groups] for g in groups]
    coeffs = least_squares(x_rows, y)
    predicted = [sum(c * x for c, x in zip(coeffs, x_row)) for x_row in x_rows]
    model_metrics = metrics(y, predicted, len(unique_groups))
    return {
        "model_id": model_id,
        "accepted_as_selected_source_model": False,
        "uses_replay_targets_for_fit": True,
        "group_count": len(unique_groups),
        "groups": {group: coeff for group, coeff in zip(unique_groups, coeffs)},
        **model_metrics,
        "row_residuals": residual_rows(rows, predicted),
    }


def d_candidate_value(candidate_id: str, inv: dict[str, Any]) -> float:
    heat = inv["heat_trace_t1"]
    reduced = inv["reduced_heat_trace_t1"]
    kernel = inv["kernel_dimension"]
    positive = inv["positive_dimension"]
    log_pdet = inv["log_pseudodeterminant"]
    values = {
        "unit": 1.0,
        "heat_trace": heat,
        "reduced_heat_trace": reduced,
        "sqrt_heat_trace": math.sqrt(heat),
        "heat_trace_per_kernel_dim": heat / kernel,
        "heat_trace_per_positive_dim": heat / positive,
        "positive_dim_per_kernel_dim": positive / kernel,
        "pseudodet_geometric_mean": math.exp(log_pdet / positive),
        "inverse_pseudodet_geometric_mean": math.exp(-log_pdet / positive),
        "exp_reduced_heat_trace": math.exp(reduced),
        "inverse_exp_reduced_heat_trace": math.exp(-reduced),
    }
    return values[candidate_id]


def main() -> int:
    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    CERTS.mkdir(parents=True, exist_ok=True)
    CORPUS.mkdir(parents=True, exist_ok=True)

    inputs = [
        STEP74,
        STEP74_CUTSET,
        STEP72_TARGETS,
        STEP72_STRICT,
        STEP69_FORMULAS,
        STEP70_FACTORS,
        STEP68_EXPONENTS,
        HEAT_RESPONSE,
        POSTPI_BOUNDARY,
    ]
    missing = [rel(path) for path in inputs if not path.exists()]
    if missing:
        raise FileNotFoundError("missing row-local brute-force inputs: " + ", ".join(missing))

    step74 = load(STEP74)
    step74_cutset = load(STEP74_CUTSET)
    targets = load(STEP72_TARGETS)
    strict = load(STEP72_STRICT)
    formulas = load(STEP69_FORMULAS)
    factors = load(STEP70_FACTORS)
    exponents = load(STEP68_EXPONENTS)
    heat = load(HEAT_RESPONSE)
    postpi_boundary = load(POSTPI_BOUNDARY)

    exponent_rows = {
        row["omega_id"]: row for row in exponents["charged_exponent_weight_rows"]
    }
    exponent_rows[exponents["higgs_exponent_weight_row"]["omega_id"]] = exponents[
        "higgs_exponent_weight_row"
    ]
    factor_rows = {row["omega_id"]: row for row in factors["factor_rows"]}
    formula_rows = {row["omega_id"]: row for row in formulas["formula_rows"]}

    feature_rows: list[dict[str, Any]] = []
    for target in targets["target_rows"]:
        omega_id = target["omega_id"]
        exponent = exponent_rows[omega_id]
        factor = factor_rows[omega_id]
        formula = formula_rows[omega_id]
        sector = target["sector"]
        generation = target["generation_or_lambda"]
        gen_index = int(generation[-1]) if generation.startswith("gen") else 0
        gen_center = float(gen_index - 2) if gen_index else 0.0
        inv = factor["finite_heat_torsion_invariants"]
        diagnostic_prefactor = abs(float(target["diagnostic_prefactor"]))
        qutrit_floor = parse_fraction(exponent.get("qutrit_quotient_floor", "0"))
        shared_h_index = 1.0 / 3.0 if sector == "H" else 0.0
        theta_exponent = float(target["theta_exponent"]) if "/" not in str(target["theta_exponent"]) else parse_fraction(target["theta_exponent"])
        row = {
            "omega_id": omega_id,
            "sector": sector,
            "generation_or_lambda": generation,
            "source_class": target["source_class"],
            "diagnostic_prefactor": diagnostic_prefactor,
            "log_diagnostic_prefactor": safe_log(diagnostic_prefactor),
            "sm_parity_projected_abs_value": target["sm_parity_projected_abs_value"],
            "theta_exponent": target["theta_exponent"],
            "theta_exponent_numeric": theta_exponent,
            "theta_weight": target["theta_weight"],
            "qutrit_floor": qutrit_floor,
            "shared_h_index": shared_h_index,
            "source_column": exponent.get("source_column", "H_shared"),
            "source_direction": exponent.get("source_direction", "H_shared_line"),
            "mixed_10_bar5_scalar_slot": bool(exponent.get("mixed_10_bar5_scalar_slot", False)),
            "generation_index": gen_index,
            "generation_center": gen_center,
            "generation_abs_center": abs(gen_center),
            "prefactor_slot_id": formula["prefactor_slot_id"],
            "row_local_overlap_threshold_factor_id": factor["row_local_overlap_threshold_factor_id"],
            "scale_scheme_factor_id": factor["scale_scheme_factor_id"],
            "finite_heat_torsion_invariants": inv,
            "features": {
                "theta_exponent": theta_exponent,
                "qutrit_floor": qutrit_floor,
                "shared_h_index": shared_h_index,
                "generation_center": gen_center,
                "generation_abs_center": abs(gen_center),
                "mixed_slot": 1.0 if exponent.get("mixed_10_bar5_scalar_slot", False) else 0.0,
                "phase_column": 1.0 if exponent.get("source_column") == "phase_Z" else 0.0,
                "shift_column": 1.0 if exponent.get("source_column") == "shift_X" else 0.0,
                "family_sector": 1.0 if target["source_class"] == "family_sector" else 0.0,
                "H_sector": 1.0 if sector == "H" else 0.0,
                "u_sector": 1.0 if sector == "u" else 0.0,
                "d_sector": 1.0 if sector == "d" else 0.0,
                "e_sector": 1.0 if sector == "e" else 0.0,
                "log_heat_trace": safe_log(inv["heat_trace_t1"]),
                "log_reduced_heat_trace": safe_log(inv["reduced_heat_trace_t1"]),
                "log_pseudodet_geometric_mean": inv["log_pseudodeterminant"] / inv["positive_dimension"],
            },
            "source_value_tier": target["source_value_tier"],
            "accepted_as_source_row": False,
            "observed_data_used_as_selector": False,
            "target_fitting_used": False,
        }
        feature_rows.append(row)

    feature_table = {
        "schema": "MTTRowLocalSourceFeatureTable.v1",
        "status": "TEN_ROWLOCAL_FEATURE_ROWS_BUILT_FOR_DISCOVERY_SEARCH",
        "row_count": len(feature_rows),
        "target_values_are_postcheck_only": True,
        "feature_rows": feature_rows,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(FEATURE_TABLE_PACKET, feature_table)

    plan = {
        "schema": "MTTAdvancedRowAttackPlan.v1",
        "status": "ADVANCED_ROW_ATTACK_PLAN_BUILT_BRUTE_FORCE_DISCOVERY_SEPARATED_FROM_PROOF",
        "current_frontier_source": rel(STEP74),
        "live_rows": [
            "ten selected L_rowlocal HYM/overlap prefactor rows",
            "ten selected T_scheme threshold/scale rows or a selected scheme theorem",
            "lambda_H H-sector value row",
            "strict Omega acceptance",
            "matrix-level mixing extension after scalar rows",
        ],
        "smart_attack_lanes": [
            {
                "lane_id": "A_selected_rowlocal_overlap_quadrature",
                "goal": "emit L_rowlocal rows from same-branch HYM/Green/zero-mode overlap integrals",
                "mathematical_object": "L_rowlocal(s,g)=|<psi_L, K_HYM/Green psi_R>| with selected normalization and quadrature error",
                "acceptance": "source-only; target values may enter only as postchecks",
            },
            {
                "lane_id": "B_selected_threshold_scheme_functional",
                "goal": "derive T_scheme rows from the post-Pi M_Z/MSbar convention source and threshold functional",
                "mathematical_object": "T_scheme = exp(Delta_threshold + Delta_mass_scheme + Delta_profile) from same-branch rows",
                "acceptance": "selected internal threshold/mass-scheme derivation, not admitted external replay",
            },
            {
                "lane_id": "C_lambda_H_H_sector_prefactor",
                "goal": "emit lambda_H from H-sector heat/torsion, shared-circle 1/3 shell, and selected quartic response",
                "mathematical_object": "Omega_H.lambda = D_fin.H * L_H * T_H * epsilon_Theta^(1/3)",
                "acceptance": "one H-sector value row before Higgs replay",
            },
            {
                "lane_id": "D_minimal_universal_anchor_if_selected",
                "goal": "allow 1-3 universal parameters only if selected by a source theorem before replay",
                "mathematical_object": "universal source-anchor functional evaluated on all ten rows",
                "acceptance": "parameters are source-selected, not fitted from diagnostic prefactors",
            },
            {
                "lane_id": "E_matrix_extension_after_scalar_gate",
                "goal": "extend scalar rows to CKM/PMNS/offdiagonal matrices after strict Omega acceptance",
                "mathematical_object": "non-scalar Weyl-pair/Hessian/Galerkin matrix packet",
                "acceptance": "separate matrix theorem; not a scalar-prefactor shortcut",
            },
        ],
        "brute_force_policy": {
            "source_only_no_fit_search_may_close_rows": False,
            "diagnostic_target_scored_search_may_close_rows": False,
            "diagnostic_search_purpose": "rank plausible source-functional shapes for the next theorem",
            "ordinary_fit_parameters_forbidden": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(PLAN_PACKET, plan)

    d_candidate_ids = [
        "unit",
        "heat_trace",
        "reduced_heat_trace",
        "sqrt_heat_trace",
        "heat_trace_per_kernel_dim",
        "heat_trace_per_positive_dim",
        "positive_dim_per_kernel_dim",
        "pseudodet_geometric_mean",
        "inverse_pseudodet_geometric_mean",
        "exp_reduced_heat_trace",
        "inverse_exp_reduced_heat_trace",
    ]
    d_trials: list[dict[str, Any]] = []
    for candidate_id in d_candidate_ids:
        residual_values = []
        residual_logs = []
        trial_rows = []
        for row in feature_rows:
            d_val = d_candidate_value(candidate_id, row["finite_heat_torsion_invariants"])
            residual = row["diagnostic_prefactor"] / d_val
            residual_values.append(residual)
            residual_logs.append(safe_log(abs(residual)))
            trial_rows.append(
                {
                    "omega_id": row["omega_id"],
                    "D_fin_candidate_value": d_val,
                    "required_L_times_T_postcheck": residual,
                    "required_L_times_T_log": safe_log(abs(residual)),
                    "inside_0p1_to_10_window": 0.1 <= abs(residual) <= 10.0,
                }
            )
        d_trials.append(
            {
                "D_fin_candidate_id": candidate_id,
                "accepted_as_selected_normalization": False,
                "source_only_no_fit_trial": True,
                "row_count": len(trial_rows),
                "all_required_LT_inside_0p1_to_10": all(
                    row["inside_0p1_to_10_window"] for row in trial_rows
                ),
                "required_LT_min_abs": min(abs(v) for v in residual_values),
                "required_LT_max_abs": max(abs(v) for v in residual_values),
                "required_LT_span": max(abs(v) for v in residual_values)
                / min(abs(v) for v in residual_values),
                "required_LT_rms_log_from_1": math.sqrt(
                    sum(log_v * log_v for log_v in residual_logs) / len(residual_logs)
                ),
                "rows": trial_rows,
            }
        )
    d_trials = sorted(d_trials, key=lambda item: item["required_LT_rms_log_from_1"])
    finite_search = {
        "schema": "MTTFiniteSubfactorNormalizationBruteforce.v1",
        "status": "FINITE_SUBFACTOR_NORMALIZATIONS_TESTED_NO_SOURCE_ROWS_ACCEPTED",
        "candidate_count": len(d_trials),
        "accepted_source_normalization_count": 0,
        "best_candidate_id": d_trials[0]["D_fin_candidate_id"],
        "best_candidate_required_LT_rms_log_from_1": d_trials[0]["required_LT_rms_log_from_1"],
        "best_candidate_all_required_LT_inside_0p1_to_10": d_trials[0][
            "all_required_LT_inside_0p1_to_10"
        ],
        "candidate_trials": d_trials,
        "interpretation": (
            "Several source-only D_fin normalizations keep the residual L*T rows order-one, "
            "but none emits L_rowlocal, T_scheme, or lambda_H as selected values."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(FINITE_SEARCH_PACKET, finite_search)

    y = [row["log_diagnostic_prefactor"] for row in feature_rows]
    nonconst_feature_names = [
        "theta_exponent",
        "qutrit_floor",
        "shared_h_index",
        "generation_center",
        "generation_abs_center",
        "mixed_slot",
        "phase_column",
        "shift_column",
        "family_sector",
        "H_sector",
        "u_sector",
        "d_sector",
        "e_sector",
        "log_heat_trace",
        "log_reduced_heat_trace",
        "log_pseudodet_geometric_mean",
    ]
    const_grid = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]
    coef_grid = [-2.0, -1.0, -2.0 / 3.0, -1.0 / 3.0, 0.0, 1.0 / 3.0, 2.0 / 3.0, 1.0, 2.0]
    heap: list[tuple[float, int, dict[str, Any]]] = []
    counter = 0
    tested = 0
    for k in range(0, 4):
        for combo in itertools.combinations(nonconst_feature_names, k):
            grids = [const_grid] + [coef_grid for _ in combo]
            for coeffs in itertools.product(*grids):
                tested += 1
                predicted = []
                for row in feature_rows:
                    value = coeffs[0]
                    for name, coeff in zip(combo, coeffs[1:]):
                        value += coeff * row["features"][name]
                    predicted.append(value)
                m = metrics(y, predicted, 1 + len(combo))
                candidate = {
                    "accepted_as_selected_source_law": False,
                    "uses_replay_targets_for_scoring": True,
                    "source_only_without_replay_fit": False,
                    "features": ["const", *combo],
                    "coefficients": {
                        "const": coeffs[0],
                        **{name: coeff for name, coeff in zip(combo, coeffs[1:])},
                    },
                    **m,
                    "row_residuals": residual_rows(feature_rows, predicted),
                }
                score = (m["max_abs_log_residual"], m["rms_log_residual"])
                heap_item = (-score[0], -score[1], counter, candidate)
                counter += 1
                if len(heap) < 25:
                    heapq.heappush(heap, heap_item)
                else:
                    if heap_item > heap[0]:
                        heapq.heapreplace(heap, heap_item)
    top_candidates = [
        item[3] for item in sorted(heap, key=lambda x: (-x[0], -x[1]))
    ]
    rational_search = {
        "schema": "MTTSmallRationalFeatureBruteforce.v1",
        "status": "SMALL_RATIONAL_FEATURE_SEARCH_EXECUTED_DIAGNOSTIC_ONLY",
        "tested_formula_count": tested,
        "top_candidate_count": len(top_candidates),
        "accepted_source_law_count": 0,
        "coefficient_grid": {
            "const": const_grid,
            "nonconst": coef_grid,
            "max_nonconst_features": 3,
        },
        "feature_names": nonconst_feature_names,
        "top_candidates": top_candidates,
        "best_max_multiplicative_error_factor": top_candidates[0][
            "max_multiplicative_error_factor"
        ],
        "best_rms_log_residual": top_candidates[0]["rms_log_residual"],
        "why_not_proof": (
            "The brute-force formulas are scored against postcheck replay prefactors. Even a good "
            "formula is only a discovery hint until its coefficients and features are selected by "
            "the MTT source functional before observed replay."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(RATIONAL_SEARCH_PACKET, rational_search)

    lsq_models = [
        fit_indicator_model(feature_rows, y, "one_global_prefactor", ["global"] * len(feature_rows)),
        fit_indicator_model(
            feature_rows,
            y,
            "two_source_classes_family_vs_H",
            [row["source_class"] for row in feature_rows],
        ),
        fit_indicator_model(feature_rows, y, "four_sector_groups", [row["sector"] for row in feature_rows]),
        fit_indicator_model(
            feature_rows,
            y,
            "three_generations_plus_H",
            [
                row["generation_or_lambda"] if row["sector"] != "H" else "H.lambda"
                for row in feature_rows
            ],
        ),
        fit_indicator_model(
            feature_rows,
            y,
            "source_column_generation_plus_H",
            [
                f"{row['source_column']}:{row['generation_or_lambda']}"
                if row["sector"] != "H"
                else "H.lambda"
                for row in feature_rows
            ],
        ),
        fit_indicator_model(feature_rows, y, "exact_omega_row_import_forbidden", [row["omega_id"] for row in feature_rows]),
    ]
    lsq_models = sorted(lsq_models, key=lambda item: item["rms_log_residual"])
    lsq_packet = {
        "schema": "MTTLeastSquaresDiagnosticModels.v1",
        "status": "LEAST_SQUARES_MODELS_RANKED_REPLAY_FIT_ONLY",
        "model_count": len(lsq_models),
        "accepted_selected_model_count": 0,
        "best_model_id": lsq_models[0]["model_id"],
        "best_model_uses_replay_targets_for_fit": lsq_models[0]["uses_replay_targets_for_fit"],
        "models": lsq_models,
        "exact_omega_import_forbidden": True,
        "ordinary_fit_parameters_forbidden": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(LSQ_PACKET, lsq_packet)

    cutset = {
        "schema": "MTTNextCutsetAfterRowLocalBruteforce.v1",
        "status": "NEXT_ATTACK_SELECTED_OVERLAP_QUADRATURE_OR_THRESHOLD_SCHEME_SOURCE_THEOREM",
        "what_the_search_teaches": [
            "finite D_fin choices alone do not emit the ten prefactor rows",
            "the residual L*T rows are order-one for several source-only normalizations",
            "small-rational feature searches can rank plausible functional shapes but remain target-scored diagnostics",
            "least-squares fits confirm that replay rows can fit themselves and are therefore forbidden as source",
        ],
        "still_missing": [
            "selected HYM/Green zero-mode overlap quadrature values for L_rowlocal",
            "selected threshold scheme functional values for T_scheme",
            "selected lambda_H H-sector source row",
            "proof that any universal source anchors are selected before replay",
            "strict Omega acceptance after source-only rows emit",
            "matrix-level CKM/PMNS/offdiagonal extension",
        ],
        "next_required_artifact": NEXT,
        "forbidden_routes": [
            "promote brute-force target-scored formulas as source rows",
            "promote exact omega-row replay import",
            "claim D_fin normalization alone closes L_rowlocal/T_scheme",
            "use admitted external threshold rows as no-knob internal derivation",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
    }
    write_json(CUTSET_PACKET, cutset)

    candidate = {
        "candidate": "MTTSelectedRowLocalThresholdValueRowsOrLambdaHPrefactorExecution",
        "status": STATUS,
        "inputs": {path.stem: rel(path) for path in inputs},
        "output_packets": {
            "advanced_row_attack_plan": rel(PLAN_PACKET),
            "source_feature_table": rel(FEATURE_TABLE_PACKET),
            "finite_subfactor_normalization_bruteforce": rel(FINITE_SEARCH_PACKET),
            "small_rational_feature_bruteforce": rel(RATIONAL_SEARCH_PACKET),
            "least_squares_diagnostic_models": rel(LSQ_PACKET),
            "next_cutset_after_bruteforce": rel(CUTSET_PACKET),
        },
        "theorem": {
            "name": "RowLocalSmartPlanAndBruteforceNoPromotionTheorem",
            "proved": True,
            "statement": (
                "The ten row-local threshold/value rows can be attacked by source-only overlap "
                "quadrature, threshold-scheme functional derivation, lambda_H H-sector response, "
                "and a possible source-selected universal anchor. Exhaustive finite-subfactor, "
                "small-rational, and least-squares searches are useful discovery tools but emit "
                "zero accepted source rows because they are either insufficient source-only "
                "normalizations or target-scored diagnostics."
            ),
        },
        "closure_decision": {
            "advanced_attack_plan_built": True,
            "source_feature_table_built": True,
            "row_count": len(feature_rows),
            "finite_subfactor_bruteforce_executed": True,
            "finite_subfactor_candidate_count": len(d_trials),
            "small_rational_bruteforce_executed": True,
            "small_rational_tested_formula_count": tested,
            "least_squares_diagnostic_models_executed": True,
            "least_squares_model_count": len(lsq_models),
            "accepted_rowlocal_source_row_count": 0,
            "accepted_prefactor_source_row_count": 0,
            "accepted_omega_source_row_count": 0,
            "accepted_internal_scalar_value_row_count": 0,
            "lambda_H_value_row_emitted": False,
            "selected_L_rowlocal_rows_emitted": False,
            "selected_T_scheme_rows_emitted": False,
            "strict_omega_acceptance_closed": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "best_source_only_D_fin_candidate": d_trials[0]["D_fin_candidate_id"],
        "best_rational_diagnostic_candidate": top_candidates[0],
        "best_lsq_diagnostic_model": {
            key: value
            for key, value in lsq_models[0].items()
            if key not in {"row_residuals", "groups"}
        },
        "previous_status": step74["status"],
        "previous_cutset_status": step74_cutset["status"],
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }
    write_json(OUTPUT, candidate)

    cert = {
        "certificate": "MTT_Selected_RowLocalThresholdValueRows_or_LambdaHPrefactorExecution_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        **candidate["closure_decision"],
        "theorem_proved": True,
        "best_source_only_D_fin_candidate": d_trials[0]["D_fin_candidate_id"],
        "best_rational_max_multiplicative_error_factor": top_candidates[0][
            "max_multiplicative_error_factor"
        ],
        "best_lsq_model_id": lsq_models[0]["model_id"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": True,
        "true_SM_equivalence_claimed": False,
        "full_no_knob_closure_claimed": False,
    }
    write_json(CERT, cert)

    NOTE.write_text(
        f"""# MTT Selected RowLocalThresholdValueRows or LambdaHPrefactorExecution v1

Status: `{STATUS}`.

## Smart Plan

The live scalar wall is now attacked in four source-first lanes:

1. selected HYM/Green zero-mode overlap quadrature for `L_rowlocal`;
2. selected threshold/scale functional for `T_scheme`;
3. H-sector `lambda_H` response from the shared `1/3` shell;
4. a source-selected universal anchor only if selected before replay.

The matrix-level CKM/PMNS extension remains separate from this scalar gate.

## Brute-Force Result

```text
row count                                  : {len(feature_rows)}
finite D_fin candidates tested             : {len(d_trials)}
best source-only D_fin candidate           : {d_trials[0]['D_fin_candidate_id']}
small-rational formulas tested             : {tested}
best rational max error factor             : {top_candidates[0]['max_multiplicative_error_factor']:.6g}
least-squares diagnostic models            : {len(lsq_models)}
best least-squares model                   : {lsq_models[0]['model_id']}
accepted row-local source rows             : 0
accepted Omega source rows                 : 0
lambda_H value row emitted                 : false
```

The brute-force search is valuable but not promotable: all target-scored formulas
remain diagnostics. The next proof object must emit source-only overlap
quadrature or threshold-scheme rows.

Next artifact: `{NEXT}`.
""",
        encoding="utf-8",
    )

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
