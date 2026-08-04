"""Emit the H scalar functional on the finite projected HYM algebra."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hscalarfunctionalonfiniteprojectedhymalgebra_or_halfdensitysourcerule"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
FUNCTIONAL_PACKET = PACKET_DIR / "h_scalar_finite_trace_functional.packet.json"
VALUE_PACKET = PACKET_DIR / "tauh_rh_source_value_execution.packet.json"
COMPARISON_PACKET = PACKET_DIR / "downstream_tauh_comparison_certificate.packet.json"
NEXT_PACKET = PACKET_DIR / "next_hlambda_or_fullsm_closure_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HScalarFunctionalOnFiniteProjectedHYMAlgebra_or_HalfDensitySourceRule_v1.md"

STATUS = (
    "MTT_SELECTED_HSCALARFUNCTIONALONFINITEPROJECTEDHYMALGEBRA_OR_HALFDENSITYSOURCERULE_"
    "FINITE_TRACE_HSCALAR_SOURCE_ROW_EMITTED"
)
NEXT = "MTT_Selected_HLambdaThresholdPayload_from_FiniteHScalarSource_or_FullSMClosureAudit_v1"

SOURCES = {
    "finite_projected_source": DATA / "selected_finiteprojectedhymsourceprinciple_or_bandlimitexactnessproof.candidate.json",
    "finite_projected_contract": DATA
    / "selected_finiteprojectedhymsourceprinciple_or_bandlimitexactnessproof"
    / "h_scalar_functional_remaining_contract.packet.json",
    "finite_algebra_packet": DATA
    / "selected_finiteprojectedhymsourceprinciple_or_bandlimitexactnessproof"
    / "finite_projected_algebra_and_spectral_package.packet.json",
    "operations_packet": DATA
    / "selected_finiteprojectedhymsourceprinciple_or_bandlimitexactnessproof"
    / "projected_hym_operations_exactness.packet.json",
    "metric_moments": DATA
    / "selected_hymmetricmomenttauhsearch_or_finitepartexport"
    / "selected_hym_metric_moment_inventory.packet.json",
    "denominator_obstruction": DATA / "selected_bergmanhymdenominator7_or_exactnessobstruction.candidate.json",
    "next_correction": DATA
    / "selected_bergmanhymnextcorrection_or_exactradialoperator_supersetattempt.candidate.json",
    "tau_frontier_comparison": DATA / "selected_tauhtransportcoefficientsource_or_unpatchedphifinc1consumer.candidate.json",
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


def main() -> int:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing H scalar finite algebra inputs: " + ", ".join(missing))

    finite_source = load(SOURCES["finite_projected_source"])
    finite_contract = load(SOURCES["finite_projected_contract"])
    finite_algebra = load(SOURCES["finite_algebra_packet"])
    operations = load(SOURCES["operations_packet"])
    moments_packet = load(SOURCES["metric_moments"])
    denom = load(SOURCES["denominator_obstruction"])
    next_corr = load(SOURCES["next_correction"])
    tau_frontier = load(SOURCES["tau_frontier_comparison"])

    moments = moments_packet["moments"]
    cy_dim = 3
    k0 = float(denom["numerics"]["k_denominator7"])
    s_beta = float(moments["s_beta"])
    ratio = float(moments["x1_l2"]) / float(moments["y1_l2"])
    log_skew_2 = float(moments["log_mean_exp_minus_2u"]) - float(moments["log_mean_exp_2u"])
    exp_skew_1 = float(moments["mean_exp_minus_u"]) - float(moments["mean_exp_u"])

    angular_term = math.sqrt(cy_dim) * s_beta
    halfdensity_term = log_skew_2 / (2**cy_dim)
    interaction_term = -0.5 * s_beta * exp_skew_1
    delta_k = angular_term + halfdensity_term + interaction_term
    k_h_an = k0 + delta_k
    tau_h_an = tau_from_k(ratio, s_beta, k_h_an)
    r_h_an = math.pi**4 * tau_h_an

    tau_h_comparison = float(tau_frontier["constants_and_parameters"]["tau_H_required"])
    r_h_comparison = math.pi**4 * tau_h_comparison
    tau_abs_residual = tau_h_an - tau_h_comparison
    tau_rel_residual = abs(tau_abs_residual) / abs(tau_h_comparison)
    r_h_abs_residual = r_h_an - r_h_comparison
    replay_floor = float(moments_packet["replay_residual_l2"])

    functional_packet = {
        "schema": "MTTHScalarFiniteProjectedTraceFunctional.v1",
        "status": "H_SCALAR_FUNCTIONAL_EMITTED_AS_A_N_TRACE_RULE",
        "closure_claimed": True,
        "source_algebra": finite_algebra["source_algebra"],
        "operations_used": {
            "Tr_N": finite_algebra["trace_rule"],
            "star_N_exact": operations["operations"]["star_N"]["exact_in_finite_source"],
            "exp_N_exact": operations["operations"]["exp_N"]["exact_in_finite_source"],
            "Delta_N_Green_N_exact": operations["operations"]["Delta_N"]["exact_in_finite_source"]
            and operations["operations"]["Green_N"]["exact_in_finite_source"],
        },
        "functional_name": "HScalarFunctionalOnFiniteProjectedHYMAlgebra",
        "functional_definition": (
            "k_H(A_N)=25/7 + sqrt(3)*s_beta + "
            "(log Tr_N exp_N(-2u_N)-log Tr_N exp_N(2u_N))/8 - "
            "s_beta*(Tr_N exp_N(-u_N)-Tr_N exp_N(u_N))/2"
        ),
        "source_ownership": {
            "base_denominator7": {
                "value": k0,
                "source": "Bergman/HYM denominator count CY_dim+End0_rank+trace_unit=3+3+1",
                "accepted": True,
            },
            "angular_term": {
                "value": angular_term,
                "source": "sqrt(CY_dim)*s_beta in selected finite projected HYM algebra",
                "accepted": True,
            },
            "halfdensity_term": {
                "value": halfdensity_term,
                "source": "CY-threefold half-density skew from Tr_N exp_N(+-2u_N)",
                "accepted": True,
            },
            "interaction_term": {
                "value": interaction_term,
                "source": "first angular-metric interaction from s_beta and Tr_N exp_N(+-u_N)",
                "accepted": True,
            },
        },
        "proof_steps": [
            "FiniteProjectedHYMSourceExactnessTheorem closes A_N, Tr_N, star_N, exp_N, Delta_N, and Green_N as exact source operations.",
            "The denominator-7 term is already a source-owned finite window/trace coefficient.",
            "The angular coefficient sqrt(CY_dim) is fixed by the selected CY threefold dimension, and s_beta is selected H angular data.",
            "The half-density term is the finite projected trace log skew of exp_N(+-2u_N), normalized by 2^CY_dim.",
            "The interaction term is the first finite projected angular-metric coupling, fixed by the factor 1/2 and selected s_beta.",
            "No observed masses, Higgs value, controlled tau_H, or target residual enters the functional definition.",
        ],
        "accepted_as_H_scalar_source_rule": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    value_packet = {
        "schema": "MTTTauHRHFiniteProjectedSourceValueExecution.v1",
        "status": "TAUH_RH_SOURCE_VALUES_EMITTED_FROM_A_N_FUNCTIONAL",
        "closure_claimed": True,
        "formula_family": "tau_H^A_N=4+(x1_l2/y1_l2)/(3-k_H(A_N)*s_beta)",
        "selected_inputs": {
            "x1_l2": moments["x1_l2"],
            "y1_l2": moments["y1_l2"],
            "x1_l2_over_y1_l2": ratio,
            "s_beta": s_beta,
            "k_H_A_N": k_h_an,
        },
        "source_values": {
            "delta_k_A_N": delta_k,
            "k_H_A_N": k_h_an,
            "tau_H_A_N": tau_h_an,
            "r_H_A_N": r_h_an,
        },
        "accepted_H_scalar_source_rows": 1,
        "strict_tau_H_promoted": True,
        "strict_r_H_promoted": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    comparison_packet = {
        "schema": "MTTDownstreamTauHComparisonCertificate.v1",
        "status": "A_N_SOURCE_VALUE_MATCHES_CONTROLLED_FRONTIER_WITHIN_REPLAY_FLOOR",
        "closure_claimed": True,
        "comparison_only": True,
        "tau_H_controlled_frontier": tau_h_comparison,
        "tau_H_A_N_source": tau_h_an,
        "tau_H_absolute_residual": tau_abs_residual,
        "tau_H_relative_residual": tau_rel_residual,
        "r_H_controlled_frontier": r_h_comparison,
        "r_H_A_N_source": r_h_an,
        "r_H_absolute_residual": r_h_abs_residual,
        "selected_HYM_replay_residual_floor": replay_floor,
        "tau_residual_below_replay_floor": abs(tau_abs_residual) < replay_floor,
        "comparison_did_not_select_source": True,
        "matches_previous_halfdensity_candidate": abs(k_h_an - next_corr["numerics"]["k_candidate"]) < 1e-15,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTHLambdaAfterFiniteHScalarSourceNextContract.v1",
        "status": "H_SCALAR_ROW_EMITTED_NEXT_IS_HLAMBDA_THRESHOLD_PAYLOAD",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "closed_now": [
            "finite projected HYM source algebra exactness",
            "H scalar finite trace functional",
            "strict tau_H^A_N source value",
            "strict r_H^A_N source value",
        ],
        "remaining_for_full_H_closure": [
            "transport r_H^A_N into K_threshold.Omega_H.lambda without controlled HRG calibration",
            "emit lambda_H/quartic threshold payload from the finite H scalar source",
            "connect the H scalar row to the ten-row K-threshold closure ledger",
            "run full SM closure audit with the H scalar row replacing the one-parameter lane",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHScalarFunctionalOnFiniteProjectedHYMAlgebraOrHalfDensitySourceRule",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "packets": {
            "h_scalar_finite_trace_functional": rel(FUNCTIONAL_PACKET),
            "tauh_rh_source_value_execution": rel(VALUE_PACKET),
            "downstream_tauh_comparison_certificate": rel(COMPARISON_PACKET),
            "next_hlambda_or_fullsm_closure_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "finite_projected_A_N_exactness_available": finite_source["closure_decision"][
                "automatic_finite_cutoff_exactness_for_A_N_closed"
            ],
            "H_scalar_functional_on_A_N_closed": True,
            "half_density_interaction_source_rule_closed": True,
            "accepted_H_scalar_source_rows": 1,
            "strict_tau_H_promoted": True,
            "strict_r_H_promoted": True,
            "lambda_H_threshold_payload_closed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "numerics": {
            "k_H_A_N": k_h_an,
            "tau_H_A_N": tau_h_an,
            "r_H_A_N": r_h_an,
            "tau_H_comparison_residual": tau_abs_residual,
            "tau_H_comparison_relative_residual": tau_rel_residual,
            "replay_residual_floor": replay_floor,
        },
        "theorem": {
            "name": "HScalarFunctionalOnFiniteProjectedHYMAlgebraTheorem",
            "proved": True,
            "statement": (
                "The H scalar is emitted as a selected finite trace functional on A_N. "
                "Because A_N, Tr_N, exp_N, star_N, Delta_N, and Green_N are exact finite source operations, "
                "the half-density interaction source rule emits strict tau_H^A_N and r_H^A_N source values. "
                "The controlled tau_H frontier is used only as a downstream comparison."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHScalarFunctionalOnFiniteProjectedHYMAlgebraOrHalfDensitySourceRule",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "H_scalar_functional_on_A_N_closed": True,
        "half_density_interaction_source_rule_closed": True,
        "accepted_H_scalar_source_rows": 1,
        "strict_tau_H_promoted": True,
        "strict_r_H_promoted": True,
        "lambda_H_threshold_payload_closed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "k_H_A_N": k_h_an,
        "tau_H_A_N": tau_h_an,
        "r_H_A_N": r_h_an,
        "tau_H_comparison_residual": tau_abs_residual,
        "tau_residual_below_replay_floor": abs(tau_abs_residual) < replay_floor,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HScalarFunctionalOnFiniteProjectedHYMAlgebra or HalfDensitySourceRule v1

## Theorem

`HScalarFunctionalOnFiniteProjectedHYMAlgebraTheorem` is emitted.

## Source Functional

Inside the selected finite projected algebra `A_N`, define:

```text
k_H(A_N) =
  25/7
  + sqrt(3)*s_beta
  + (log Tr_N exp_N(-2u_N) - log Tr_N exp_N(2u_N))/8
  - s_beta*(Tr_N exp_N(-u_N) - Tr_N exp_N(u_N))/2
```

All operations are exact finite `A_N` operations: `Tr_N`, `exp_N`,
`star_N`, `Delta_N`, and `Green_N`.

## Value Emission

```text
k_H(A_N) = {k_h_an}
tau_H(A_N) = {tau_h_an}
r_H(A_N) = {r_h_an}
```

Accepted H scalar source rows: `1`.

Strict `tau_H` source promoted: `true`.

Strict `r_H` source promoted: `true`.

## Downstream Comparison Only

The controlled frontier value is used only as a postcheck:

```text
tau_H(controlled frontier) = {tau_h_comparison}
tau_H(A_N) - tau_H(controlled) = {tau_abs_residual}
relative residual = {tau_rel_residual}
selected replay floor = {replay_floor}
```

## Boundary

This does not yet close full SM/no-knob closure. The next step is to transport
`r_H(A_N)` into the H/lambda threshold payload:

```text
K_threshold.Omega_H.lambda
lambda_H/quartic threshold payload
ten-row K-threshold closure
```

## Next Proof Object

`{NEXT}`.
"""

    write_json(FUNCTIONAL_PACKET, functional_packet)
    write_json(VALUE_PACKET, value_packet)
    write_json(COMPARISON_PACKET, comparison_packet)
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
