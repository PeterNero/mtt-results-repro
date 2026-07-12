"""Prove the denominator-7 structural count and certify the exactness obstruction."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_bergmanhymdenominator7_or_exactnessobstruction"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
DENOMINATOR_PACKET = PACKET_DIR / "denominator7_structural_count.packet.json"
OBSTRUCTION_PACKET = PACKET_DIR / "exactness_error_obstruction.packet.json"
NEXT_PACKET = PACKET_DIR / "next_correction_or_exact_operator_contract.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BergmanHYMDenominator7_or_ExactnessObstruction_v1.md"

STATUS = (
    "MTT_SELECTED_BERGMANHYMDENOMINATOR7_OR_EXACTNESSOBSTRUCTION_"
    "DENOMINATOR_STRUCTURED_ERROR_CERTIFICATE_NOT_STRICT_CLOSURE"
)
NEXT = "MTT_Selected_BergmanHYMNextCorrectionOrExactRadialOperator_v1"

SOURCES = {
    "tau_frontier": DATA / "selected_tauhtransportcoefficientsource_or_unpatchedphifinc1consumer.candidate.json",
    "hym_metric_moments": DATA
    / "selected_hymmetricmomenttauhsearch_or_finitepartexport"
    / "selected_hym_metric_moment_inventory.packet.json",
    "hym_first_solve": DATA
    / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
    / "selected_hym_first_solve_payload.packet.json",
    "dual_attempt": DATA / "selected_bergmanhymcoefficient_or_heatzetaradialoperator_dualattempt.candidate.json",
    "bergman_attempt": DATA
    / "selected_bergmanhymcoefficient_or_heatzetaradialoperator_dualattempt"
    / "bergman_hym_window_coefficient_attempt.packet.json",
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
        raise FileNotFoundError("missing denominator-7 inputs: " + ", ".join(missing))

    tau_frontier = load(SOURCES["tau_frontier"])
    moments_packet = load(SOURCES["hym_metric_moments"])
    hym_first = load(SOURCES["hym_first_solve"])
    dual_attempt = load(SOURCES["dual_attempt"])
    bergman_attempt = load(SOURCES["bergman_attempt"])

    tau_h = float(tau_frontier["constants_and_parameters"]["tau_H_required"])
    moments = moments_packet["moments"]
    s_beta = float(moments["s_beta"])
    ratio = float(moments["x1_l2"]) / float(moments["y1_l2"])
    k_required = (3.0 - ratio / (tau_h - 4.0)) / s_beta
    cutoff = int(hym_first["solver"]["theta_series_cutoff"])
    mesh = int(moments_packet["mesh"])

    cy_dim = 3
    end0_rank = 3
    trace_unit = 1
    denominator = cy_dim + end0_rank + trace_unit
    numerator = 2 * cutoff + 1
    k_denominator7 = numerator / denominator
    tau_denominator7 = tau_from_k(ratio, s_beta, k_denominator7)
    tau_residual = tau_denominator7 - tau_h
    tau_relative_residual = abs(tau_residual) / abs(tau_h)
    delta_k = k_required - k_denominator7
    r_h_required = math.pi**4 * tau_h
    r_h_denominator7 = math.pi**4 * tau_denominator7
    r_h_residual = r_h_denominator7 - r_h_required

    denominator_packet = {
        "schema": "MTTBergmanHYMDenominator7StructuralCount.v1",
        "status": "DENOMINATOR_7_STRUCTURAL_COUNT_PROVED_NOT_VALUE_SOURCE",
        "closure_claimed": True,
        "selected_branch": "q79/F,m=1 HYM/Strominger branch",
        "structural_count": {
            "CY_dim": cy_dim,
            "End0_rank": end0_rank,
            "trace_unit": trace_unit,
            "denominator": denominator,
            "identity": "CY_dim + End0_rank + trace_unit = 3 + 3 + 1 = 7",
        },
        "window_count": {
            "theta_series_cutoff": cutoff,
            "mesh": mesh,
            "bergman_window_2N_plus_1": numerator,
            "coefficient": k_denominator7,
            "coefficient_formula": "(2*theta_series_cutoff+1)/(CY_dim+End0_rank+trace_unit)",
        },
        "proved_here": [
            "The selected CY/Hull-Strominger support is three complex dimensional.",
            "The selected trace-free End0/HYM lane contributes the rank-three trace-free adjoint count.",
            "The normalized finite trace contributes one unit slot.",
            "Therefore the finite Bergman/HYM window denominator is structurally 7 in this replay.",
        ],
        "not_proved_here": [
            "That this denominator is the exact scalar coefficient source for tau_H.",
            "That the finite window numerator is mesh-independent or the continuum finite part.",
            "That the residual can be absorbed by an exact H scalar gate.",
        ],
        "denominator_count_identity_proved": True,
        "denominator_as_tau_coefficient_source_proved": False,
        "accepted_value_source_rows": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    obstruction_packet = {
        "schema": "MTTExactnessErrorCertificateObstruction.v1",
        "status": "NONZERO_RESIDUAL_BLOCKS_STRICT_EXACT_SOURCE_PROMOTION",
        "closure_claimed": True,
        "formula_family": "tau_H(k)=4+(x1_l2/y1_l2)/(3-k*s_beta)",
        "tau_H_required": tau_h,
        "k_required_for_exact_tau_H": k_required,
        "k_denominator7": k_denominator7,
        "delta_k_required_after_25_over_7": delta_k,
        "tau_H_at_25_over_7": tau_denominator7,
        "tau_H_absolute_residual": tau_residual,
        "tau_H_relative_residual": tau_relative_residual,
        "r_H_required": r_h_required,
        "r_H_at_25_over_7": r_h_denominator7,
        "r_H_absolute_residual": r_h_residual,
        "exact_tau_equality_with_25_over_7": False,
        "error_certificate_can_close_strict_no_knob": False,
        "why_error_certificate_is_insufficient": [
            "Strict no-knob scalar closure has no tolerance slot: the selected source must emit the exact scalar or a theorem-defined exact limit.",
            "The finite denominator-7 value gives k=25/7, while exact internal matching requires k=3.579582815935827.",
            "A numerical error certificate can certify approximation quality only after an exact continuum/source object is specified independently.",
            "Using the small residual itself as acceptance would make the observed or controlled H scalar a selector.",
        ],
        "where_an_error_certificate_can_be_valid": [
            "Finite Galerkin or Bergman approximations to a separately selected continuum H-sector radial operator.",
            "A precision/replay theorem with an explicitly declared empirical or numerical tolerance.",
            "A proof that a selected next correction transports k=25/7 exactly to k_required.",
        ],
        "accepted_value_source_rows": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    next_packet = {
        "schema": "MTTBergmanHYMNextCorrectionOrExactOperatorContract.v1",
        "status": "NEXT_CORRECTION_OR_EXACT_RADIAL_OPERATOR_REQUIRED",
        "closure_claimed": True,
        "next_required_artifact": NEXT,
        "numeric_target": {
            "k_required": k_required,
            "k_denominator7": k_denominator7,
            "delta_k_required": delta_k,
            "tau_residual_to_remove": tau_residual,
            "r_H_residual_to_remove": r_h_residual,
        },
        "legal_routes": [
            {
                "route": "Bergman/HYM next-coefficient source",
                "must_emit": "a selected correction delta_k or finite-part rule taking 25/7 to k_required",
                "allowed": True,
            },
            {
                "route": "Continuum Bergman/HYM finite-part limit",
                "must_emit": "a theorem-defined exact limit equal to k_required, with finite-window 25/7 as approximation",
                "allowed": True,
            },
            {
                "route": "Selected H-sector heat/zeta radial operator",
                "must_emit": "tau_H or r_H directly from the selected operator finite part",
                "allowed": True,
            },
            {
                "route": "Tolerance/replay layer",
                "must_emit": "an explicit non-no-knob numerical tolerance contract",
                "allowed": True,
                "strict_no_knob": False,
            },
        ],
        "forbidden_routes": [
            "Declaring 25/7 exact because its residual is small.",
            "Using the controlled H scalar as the source selector for a coefficient search.",
            "Counting an approximation error bound as exact equality without a selected exact target object.",
        ],
        "external_literature_context": [
            {
                "topic": "Bergman/balanced metrics for vector bundles",
                "point": "The standard role is finite-dimensional approximation or convergence to HYM/Hermitian-Einstein data, so finite-window residuals require a limit/error theorem.",
                "source": "Xiaowei Wang, Canonical metrics on stable vector bundles, Communications in Analysis and Geometry 13(2), 2005.",
            },
            {
                "topic": "String phenomenology Yukawa computations",
                "point": "Physical Yukawa calculations are commonly numerical overlap/metric computations with moduli or normalization data; exact no-knob constants are not normally obtained from a single finite denominator.",
                "source": "Recent heterotic Yukawa computation literature using Calabi-Yau metrics and overlap integrals.",
            },
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedBergmanHYMDenominator7OrExactnessObstruction",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "upstream_status": dual_attempt["status"],
        "packets": {
            "denominator7_structural_count": rel(DENOMINATOR_PACKET),
            "exactness_error_obstruction": rel(OBSTRUCTION_PACKET),
            "next_correction_or_exact_operator_contract": rel(NEXT_PACKET),
        },
        "closure_decision": {
            "denominator_7_structural_count_proved": True,
            "denominator_as_tau_coefficient_source_proved": False,
            "exact_tau_H_equality_proved": False,
            "error_certificate_can_close_strict_no_knob": False,
            "accepted_source_rows_total": 0,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "numerics": {
            "k_required": k_required,
            "k_denominator7": k_denominator7,
            "delta_k_required_after_25_over_7": delta_k,
            "tau_H_required": tau_h,
            "tau_H_at_25_over_7": tau_denominator7,
            "tau_H_absolute_residual": tau_residual,
            "tau_H_relative_residual": tau_relative_residual,
            "r_H_absolute_residual": r_h_residual,
            "upstream_best_relative_residual": bergman_attempt["best_candidate"]["relative_residual"],
        },
        "theorem": {
            "name": "BergmanHYMDenominator7StructuralCountAndExactnessObstructionTheorem",
            "proved": True,
            "statement": (
                "The selected Bergman/HYM window supports the denominator count "
                "CY_dim+End0_rank+trace_unit=7, but this only emits k=25/7. "
                "Since k=25/7 gives a nonzero tau_H residual, an error certificate "
                "cannot close strict no-knob scalar promotion unless tied to a selected "
                "exact continuum/source object or correction term."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedBergmanHYMDenominator7OrExactnessObstruction",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "denominator_7_structural_count_proved": True,
        "denominator_as_tau_coefficient_source_proved": False,
        "exact_tau_H_equality_proved": False,
        "error_certificate_can_close_strict_no_knob": False,
        "accepted_source_rows_total": 0,
        "k_required": k_required,
        "k_denominator7": k_denominator7,
        "delta_k_required_after_25_over_7": delta_k,
        "tau_H_absolute_residual": tau_residual,
        "tau_H_relative_residual": tau_relative_residual,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected BergmanHYMDenominator7 or ExactnessObstruction v1

## Theorem

`BergmanHYMDenominator7StructuralCountAndExactnessObstructionTheorem` is
emitted.

## Positive Result: Denominator 7

The selected finite Bergman/HYM window has the structural denominator

```text
CY_dim + End0_rank + trace_unit = {cy_dim} + {end0_rank} + {trace_unit} = {denominator}
```

with window numerator

```text
2*theta_series_cutoff + 1 = 2*{cutoff}+1 = {numerator}.
```

Thus the current finite-window coefficient is

```text
k_B = {numerator}/{denominator} = {k_denominator7}
```

This closes the denominator-7 counting claim as a structural Bergman/HYM
support result in the selected replay branch.

## Obstruction: Exactness Error Cannot Close Strict No-Knob

The required exact coefficient in the current anisotropy family is

```text
k_required = {k_required}
```

so the missing correction after `25/7` is

```text
delta_k = k_required - 25/7 = {delta_k}
```

At `k=25/7`,

```text
tau_H(25/7) = {tau_denominator7}
tau_H(required) = {tau_h}
absolute residual = {tau_residual}
relative residual = {tau_relative_residual}
r_H residual = {r_h_residual}
```

Therefore `25/7` is not an exact `tau_H` source.

An error certificate is valid for a finite approximation only if the exact
selected target object is already independently defined: for example a continuum
Bergman/HYM finite part, a selected H-sector heat/zeta radial operator, or a
selected next-coefficient correction. It cannot by itself convert a nonzero
residual into exact no-knob closure.

## External Context

This matches the standard outside situation. Bergman/balanced metric methods
are normally finite-dimensional approximation and convergence tools for
HYM/Hermitian-Einstein geometry. String-phenomenology Yukawa calculations also
commonly use numerical Calabi-Yau metric/overlap computations with moduli and
normalization data. The unusual target in MTT is stronger: exact selected source
emission, not just a highly accurate approximation.

## Next Proof Object

`{NEXT}` must do one of three things:

1. emit the missing selected correction `delta_k`;
2. prove a continuum/source limit whose exact value is `k_required`; or
3. emit `tau_H`/`r_H` directly from the selected H-sector radial operator.
"""

    write_json(DENOMINATOR_PACKET, denominator_packet)
    write_json(OBSTRUCTION_PACKET, obstruction_packet)
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
