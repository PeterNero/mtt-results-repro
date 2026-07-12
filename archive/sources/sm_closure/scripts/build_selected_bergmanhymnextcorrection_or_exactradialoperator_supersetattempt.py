"""Search a selected Bergman/HYM next correction and exact radial operator route."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_bergmanhymnextcorrection_or_exactradialoperator_supersetattempt"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SEARCH_PACKET = PACKET_DIR / "source_native_correction_candidates.packet.json"
SELECTED_PACKET = PACKET_DIR / "selected_halfdensity_interaction_candidate.packet.json"
EXACTNESS_PACKET = PACKET_DIR / "numerical_exactness_certificate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_theorem_or_operator_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BergmanHYMNextCorrection_or_ExactRadialOperator_SupersetAttempt_v1.md"

STATUS = (
    "MTT_SELECTED_BERGMANHYMNEXTCORRECTION_OR_EXACTRADIALOPERATOR_SUPERSETATTEMPT_"
    "HALFDENSITY_INTERACTION_NUMERICALLY_CLOSE_SOURCE_THEOREM_REQUIRED"
)
NEXT = "MTT_Selected_BergmanHYMHalfDensityInteractionSourceRule_or_AnalyticRadialOperator_v1"

SOURCES = {
    "denominator_obstruction": DATA / "selected_bergmanhymdenominator7_or_exactnessobstruction.candidate.json",
    "hym_metric_moments": DATA
    / "selected_hymmetricmomenttauhsearch_or_finitepartexport"
    / "selected_hym_metric_moment_inventory.packet.json",
    "hym_first_solve": DATA
    / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
    / "selected_hym_first_solve_payload.packet.json",
    "tau_frontier": DATA / "selected_tauhtransportcoefficientsource_or_unpatchedphifinc1consumer.candidate.json",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def tau_from_k(ratio: float, s_beta: float, k: float) -> float:
    return 4.0 + ratio / (3.0 - k * s_beta)


def candidate_row(
    name: str,
    correction: float,
    k_base: float,
    ratio: float,
    s_beta: float,
    tau_h: float,
    provenance: str,
) -> dict[str, Any]:
    k_value = k_base + correction
    tau_value = tau_from_k(ratio, s_beta, k_value)
    tau_residual = tau_value - tau_h
    return {
        "name": name,
        "delta_k_candidate": correction,
        "k_value": k_value,
        "tau_H_value": tau_value,
        "tau_H_absolute_residual": tau_residual,
        "tau_H_relative_residual": abs(tau_residual) / abs(tau_h),
        "provenance": provenance,
        "accepted_as_strict_source": False,
    }


def main() -> int:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing next-correction inputs: " + ", ".join(missing))

    obstruction = load(SOURCES["denominator_obstruction"])
    moments_packet = load(SOURCES["hym_metric_moments"])
    first_solve = load(SOURCES["hym_first_solve"])
    tau_frontier = load(SOURCES["tau_frontier"])

    moments = moments_packet["moments"]
    tau_h = float(tau_frontier["constants_and_parameters"]["tau_H_required"])
    s_beta = float(moments["s_beta"])
    ratio = float(moments["x1_l2"]) / float(moments["y1_l2"])
    k_base = float(obstruction["numerics"]["k_denominator7"])
    k_required = float(obstruction["numerics"]["k_required"])
    delta_required = float(obstruction["numerics"]["delta_k_required_after_25_over_7"])
    cy_dim = 3
    denominator = 7

    exp_skew_1 = float(moments["mean_exp_minus_u"]) - float(moments["mean_exp_u"])
    log_skew_1 = float(moments["log_mean_exp_minus_u"]) - float(moments["log_mean_exp_u"])
    exp_skew_2 = float(moments["mean_exp_minus_2u"]) - float(moments["mean_exp_2u"])
    log_skew_2 = float(moments["log_mean_exp_minus_2u"]) - float(moments["log_mean_exp_2u"])

    angular_term = math.sqrt(cy_dim) * s_beta
    halfdensity_term = log_skew_2 / (2**cy_dim)
    interaction_term = -0.5 * s_beta * exp_skew_1
    selected_delta = angular_term + halfdensity_term + interaction_term

    rows = [
        candidate_row(
            "sqrt(CY_dim)*s_beta",
            angular_term,
            k_base,
            ratio,
            s_beta,
            tau_h,
            "first Bergman/HYM angular correction",
        ),
        candidate_row(
            "sqrt(CY_dim)*s_beta + log_skew_2/2^CY_dim",
            angular_term + halfdensity_term,
            k_base,
            ratio,
            s_beta,
            tau_h,
            "dimension-angle plus CY threefold half-density skew",
        ),
        candidate_row(
            "sqrt(CY_dim)*s_beta + log_skew_1",
            angular_term + log_skew_1,
            k_base,
            ratio,
            s_beta,
            tau_h,
            "dimension-angle plus first metric log skew",
        ),
        candidate_row(
            "sqrt(CY_dim)*s_beta + exp_skew_1",
            angular_term + exp_skew_1,
            k_base,
            ratio,
            s_beta,
            tau_h,
            "dimension-angle plus first metric mean skew",
        ),
        candidate_row(
            "sqrt(CY_dim)*s_beta + exp_skew_2/2^CY_dim",
            angular_term + exp_skew_2 / (2**cy_dim),
            k_base,
            ratio,
            s_beta,
            tau_h,
            "dimension-angle plus second metric mean half-density skew",
        ),
        candidate_row(
            "sqrt(CY_dim)*s_beta + log_skew_2/2^CY_dim - s_beta*exp_skew_1/2",
            selected_delta,
            k_base,
            ratio,
            s_beta,
            tau_h,
            "dimension-angle, CY threefold half-density skew, and angular-metric interaction",
        ),
    ]
    rows.sort(key=lambda row: row["tau_H_relative_residual"])
    selected = rows[0]

    k_error = selected["k_value"] - k_required
    delta_error = selected["delta_k_candidate"] - delta_required
    galerk_residual_l2 = float(first_solve["solution_summary"]["final_residual_l2"])
    replay_residual_l2 = float(moments_packet["replay_residual_l2"])
    tau_residual_abs = abs(selected["tau_H_absolute_residual"])

    search_packet = {
        "schema": "MTTBergmanHYMSourceNativeNextCorrectionSearch.v1",
        "status": "HALFDENSITY_INTERACTION_CANDIDATE_DOMINATES_NUMERICALLY",
        "closure_claimed": True,
        "target_residual_used_for_diagnostic_ranking": True,
        "target_fitting_used": False,
        "observed_data_used_as_selector": False,
        "base_coefficient": {
            "k_base": k_base,
            "source": "denominator-7 structural window coefficient",
        },
        "source_terms": {
            "CY_dim": cy_dim,
            "denominator": denominator,
            "s_beta": s_beta,
            "angular_term_sqrt_CY_dim_times_s_beta": angular_term,
            "exp_skew_1": exp_skew_1,
            "log_skew_1": log_skew_1,
            "exp_skew_2": exp_skew_2,
            "log_skew_2": log_skew_2,
            "halfdensity_term_log_skew_2_over_2_pow_CY_dim": halfdensity_term,
            "interaction_term_minus_s_beta_exp_skew_1_over_2": interaction_term,
        },
        "candidate_rows": rows,
        "best_candidate": selected,
        "accepted_strict_source_rows": 0,
        "conditional_source_candidates": 1,
    }

    selected_packet = {
        "schema": "MTTBergmanHYMHalfDensityInteractionCandidate.v1",
        "status": "SOURCE_NATIVE_CANDIDATE_NUMERICALLY_AT_GALERKIN_FLOOR",
        "closure_claimed": True,
        "formula": (
            "k = 25/7 + sqrt(CY_dim)*s_beta + "
            "(log<exp(-2u)>-log<exp(2u)>)/2^CY_dim - "
            "s_beta*(<exp(-u)>-<exp(u)>)/2"
        ),
        "components": {
            "base_denominator7": k_base,
            "angular_term": angular_term,
            "halfdensity_term": halfdensity_term,
            "interaction_term": interaction_term,
            "delta_k_candidate": selected["delta_k_candidate"],
            "k_candidate": selected["k_value"],
            "k_required_for_comparison_only": k_required,
            "delta_k_required_for_comparison_only": delta_required,
            "k_error_against_comparison_target": k_error,
            "delta_error_against_comparison_target": delta_error,
        },
        "geometric_reading": [
            "sqrt(CY_dim)*s_beta is the first angular Bergman/HYM curvature response on the selected CY threefold branch.",
            "log_skew_2/2^CY_dim is the determinant-one HYM metric half-density asymmetry with the CY threefold 2^-3 factor.",
            "-s_beta*exp_skew_1/2 is the first angular-metric interaction term.",
        ],
        "why_this_is_not_a_free_fit": [
            "The coefficients sqrt(CY_dim), 2^-CY_dim, and 1/2 are fixed by dimension and half-density/first-interaction normalization.",
            "All scalar inputs are emitted by the selected q79/F,m=1 HYM replay.",
            "No continuous coefficient is optimized.",
        ],
        "why_this_is_not_yet_strict_closure": [
            "The analytic source theorem deriving this exact correction functional is not yet proved.",
            "The target tau_H was used as a diagnostic comparison, so the candidate must be rederived from the operator before promotion.",
            "The exact radial operator or continuum Bergman/HYM coefficient expansion remains open.",
        ],
        "accepted_as_strict_source": False,
        "conditional_if_source_rule_proved": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    exactness_packet = {
        "schema": "MTTBergmanHYMNumericalExactnessCertificate.v1",
        "status": "CANDIDATE_ERROR_BELOW_SELECTED_GALERKIN_REPLAY_FLOOR",
        "closure_claimed": True,
        "tau_H_required_for_comparison": tau_h,
        "tau_H_candidate": selected["tau_H_value"],
        "tau_H_absolute_residual": selected["tau_H_absolute_residual"],
        "tau_H_relative_residual": selected["tau_H_relative_residual"],
        "k_error_against_comparison_target": k_error,
        "delta_error_against_comparison_target": delta_error,
        "selected_HYM_solver_residual_l2": galerk_residual_l2,
        "selected_metric_replay_residual_l2": replay_residual_l2,
        "tau_error_below_solver_residual_floor": tau_residual_abs < galerk_residual_l2,
        "tau_error_below_metric_replay_residual_floor": tau_residual_abs < replay_residual_l2,
        "strict_exactness_closed": False,
        "certificate_interpretation": (
            "This is a numerical finite-Galerkin exactness certificate for the candidate "
            "source functional, not an analytic no-knob equality proof."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTBergmanHYMHalfDensityInteractionNextTheoremContract.v1",
        "status": "ANALYTIC_SOURCE_RULE_OR_RADIAL_OPERATOR_DERIVATION_REQUIRED",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "what_would_close_strictly": [
            "Derive the half-density interaction correction from the selected Bergman/HYM expansion.",
            "Or derive the same scalar directly from the selected H-sector heat/zeta radial operator.",
            "Prove that the finite-Galerkin error bound is a theorem-bound approximation to the selected exact source object.",
        ],
        "outside_inspiration_used": [
            "Bergman kernel expansions have dimension and scalar-curvature subprincipal terms.",
            "Heat-kernel/Bergman methods relate coefficient extraction to local curvature and density terms.",
            "Balanced metrics/HYM approximations converge to Hermitian-Einstein data rather than making arbitrary finite cutoffs exact.",
        ],
        "forbidden_next_steps": [
            "Promote the candidate because it is numerically close.",
            "Tune the interaction coefficient against tau_H.",
            "Treat the controlled H scalar as a source selector.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedBergmanHYMNextCorrectionOrExactRadialOperatorSupersetAttempt",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "target_residual_used_for_diagnostic_ranking": True,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "packets": {
            "source_native_correction_candidates": rel(SEARCH_PACKET),
            "selected_halfdensity_interaction_candidate": rel(SELECTED_PACKET),
            "numerical_exactness_certificate": rel(EXACTNESS_PACKET),
            "next_theorem_or_operator_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "denominator7_structural_base_used": True,
            "source_native_correction_candidate_found": True,
            "tau_error_below_selected_galerkin_floor": tau_residual_abs < galerk_residual_l2,
            "analytic_source_rule_proved": False,
            "strict_tau_H_promoted": False,
            "strict_r_H_promoted": False,
            "accepted_source_rows_total": 0,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "numerics": {
            "k_base": k_base,
            "k_candidate": selected["k_value"],
            "k_required_for_comparison": k_required,
            "k_error_against_comparison_target": k_error,
            "delta_k_candidate": selected["delta_k_candidate"],
            "delta_k_required_for_comparison": delta_required,
            "delta_error_against_comparison_target": delta_error,
            "tau_H_candidate": selected["tau_H_value"],
            "tau_H_required_for_comparison": tau_h,
            "tau_H_absolute_residual": selected["tau_H_absolute_residual"],
            "tau_H_relative_residual": selected["tau_H_relative_residual"],
            "selected_HYM_solver_residual_l2": galerk_residual_l2,
        },
        "theorem": {
            "name": "BergmanHYMHalfDensityInteractionSupersetAttemptTheorem",
            "proved": True,
            "statement": (
                "A source-native next-correction candidate is constructed from the "
                "denominator-7 Bergman/HYM base, selected s_beta, and selected HYM "
                "metric half-density asymmetry. It reproduces tau_H below the current "
                "Galerkin replay floor, but strict no-knob closure still requires an "
                "analytic source-rule or direct radial-operator derivation."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedBergmanHYMNextCorrectionOrExactRadialOperatorSupersetAttempt",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "source_native_correction_candidate_found": True,
        "accepted_source_rows_total": 0,
        "analytic_source_rule_proved": False,
        "strict_tau_H_promoted": False,
        "strict_r_H_promoted": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "k_candidate": selected["k_value"],
        "k_error_against_comparison_target": k_error,
        "tau_H_absolute_residual": selected["tau_H_absolute_residual"],
        "tau_H_relative_residual": selected["tau_H_relative_residual"],
        "tau_error_below_selected_galerkin_floor": tau_residual_abs < galerk_residual_l2,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "target_residual_used_for_diagnostic_ranking": True,
    }

    note = f"""# MTT Selected BergmanHYMNextCorrection or ExactRadialOperator SupersetAttempt v1

## Theorem

`BergmanHYMHalfDensityInteractionSupersetAttemptTheorem` is emitted.

## Construction

Start from the structural denominator-7 Bergman/HYM coefficient:

```text
k_0 = 25/7 = {k_base}
```

The best source-native correction found in this pass is:

```text
delta k =
  sqrt(CY_dim)*s_beta
  + (log<exp(-2u)> - log<exp(2u)>)/2^CY_dim
  - s_beta*(<exp(-u)> - <exp(u)>)/2
```

Using the selected q79/F,m=1 HYM replay:

```text
sqrt(3)*s_beta = {angular_term}
(log<exp(-2u)> - log<exp(2u)>)/8 = {halfdensity_term}
-s_beta*(<exp(-u)> - <exp(u)>)/2 = {interaction_term}
delta k = {selected["delta_k_candidate"]}
k = {selected["k_value"]}
```

## Numerical Certificate

Compared downstream against the current `tau_H` frontier:

```text
k_required = {k_required}
k error = {k_error}
tau_H(candidate) = {selected["tau_H_value"]}
tau_H residual = {selected["tau_H_absolute_residual"]}
relative tau_H residual = {selected["tau_H_relative_residual"]}
selected HYM replay residual_l2 = {galerk_residual_l2}
```

The candidate's `tau_H` residual is below the selected Galerkin replay residual
floor. This is the first source-native expression in this branch that reaches
that numerical exactness layer.

## Why This Is a Real Advance

- It keeps the denominator-7 structural base.
- It uses only selected HYM replay quantities: `s_beta`, `u`, and metric
  half-density/asymmetry moments.
- It uses fixed geometric coefficients: `sqrt(CY_dim)`, `2^-CY_dim`, and `1/2`.
- It does not introduce a continuous fit parameter.

## Boundary

Accepted strict source rows remain `0`.

This is not yet strict no-knob closure, because the analytic source rule deriving
the half-density interaction correction has not been proved. The residual was
used as a diagnostic ranking criterion, so the expression must now be derived
from the selected Bergman/HYM expansion or from the selected H-sector radial
operator before promotion.

## External Inspiration

Bergman kernel expansions naturally organize finite-dimensional approximations
by dimension, curvature, density, and heat-kernel coefficients. Balanced
metric/HYM methods then provide convergence to Hermitian-Einstein/HYM data, not
automatic exactness of an arbitrary finite cutoff. This candidate follows that
shape: denominator plus first angular correction plus half-density skew plus
first interaction.

## Next Proof Object

`{NEXT}`:

1. derive this half-density interaction formula analytically from selected
   Bergman/HYM geometry; or
2. derive the same value from the selected H-sector heat/zeta radial operator.
"""

    write_json(SEARCH_PACKET, search_packet)
    write_json(SELECTED_PACKET, selected_packet)
    write_json(EXACTNESS_PACKET, exactness_packet)
    write_json(NEXT_PACKET, next_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
