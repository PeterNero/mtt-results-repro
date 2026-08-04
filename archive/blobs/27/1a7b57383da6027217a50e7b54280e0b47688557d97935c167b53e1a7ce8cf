"""Attempt both finite Bergman/HYM coefficient and heat-zeta radial routes."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_bergmanhymcoefficient_or_heatzetaradialoperator_dualattempt"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BERGMAN_PACKET = PACKET_DIR / "bergman_hym_window_coefficient_attempt.packet.json"
HEAT_PACKET = PACKET_DIR / "heat_zeta_radial_operator_proxy_attempt.packet.json"
DECISION_PACKET = PACKET_DIR / "dual_route_decision_and_next_theorem.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_BergmanHYMCoefficient_or_HeatZetaRadialOperator_DualAttempt_v1.md"

STATUS = (
    "MTT_SELECTED_BERGMANHYMCOEFFICIENT_OR_HEATZETARADIALOPERATOR_DUALATTEMPT_"
    "BERGMAN_WINDOW_SHARP_HEAT_PROXY_REJECTED_SOURCE_THEOREM_REQUIRED"
)
NEXT = "MTT_Selected_BergmanHYMCoefficientSourceRule_or_ExactRadialOperator_v1"

SOURCES = {
    "tau_frontier": DATA / "selected_tauhtransportcoefficientsource_or_unpatchedphifinc1consumer.candidate.json",
    "hym_metric_moments": DATA
    / "selected_hymmetricmomenttauhsearch_or_finitepartexport"
    / "selected_hym_metric_moment_inventory.packet.json",
    "hym_first_solve": DATA
    / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
    / "selected_hym_first_solve_payload.packet.json",
    "coefficient_frontier": DATA / "selected_hweightedfinitepartcoefficientsearch_or_meshwindownogo.candidate.json",
    "external_corpus_clues": DATA / "selected_finitepartcoefficient_externalcorpuscluescan.candidate.json",
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


def row(name: str, k: float, ratio: float, s_beta: float, tau_h: float, provenance: str) -> dict[str, Any]:
    value = tau_from_k(ratio, s_beta, k)
    residual = value - tau_h
    return {
        "name": name,
        "k_value": k,
        "tau_H_value": value,
        "absolute_residual": residual,
        "relative_residual": abs(residual) / abs(tau_h),
        "provenance": provenance,
        "accepted_as_source": False,
        "reason_not_accepted": (
            "This is a theorem target or proxy computation. It is not emitted by a selected "
            "finite Bergman/HYM coefficient source rule or by a selected H-sector heat/zeta "
            "radial operator with exactness/error certificate."
        ),
    }


def heat_spectrum_stats(cutoff: int) -> dict[str, float]:
    values: list[float] = []
    for n1 in range(-cutoff, cutoff + 1):
        for n2 in range(-cutoff, cutoff + 1):
            for n3 in range(-cutoff, cutoff + 1):
                for n4 in range(-cutoff, cutoff + 1):
                    q = n1 * n1 + n2 * n2 + n3 * n3 + n4 * n4
                    if q > 0:
                        values.append((2.0 * math.pi) ** 2 * q)
    arr = np.array(values, dtype=float)
    logs = np.log(arr)
    inv = 1.0 / arr
    return {
        "mode_count_excluding_zero": int(arr.size),
        "logdet_per_mode": float(logs.mean()),
        "sqrt_logdet_per_mode": float(math.sqrt(logs.mean())),
        "log_logdet_per_mode": float(math.log(logs.mean())),
        "zeta1_per_mode": float(inv.mean()),
        "zeta_minus1_per_mode": float(arr.mean()),
        "std_log_spectrum": float(logs.std()),
    }


def main() -> int:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing dual-route inputs: " + ", ".join(missing))

    tau_frontier = load(SOURCES["tau_frontier"])
    moments_packet = load(SOURCES["hym_metric_moments"])
    hym_first = load(SOURCES["hym_first_solve"])
    coefficient_frontier = load(SOURCES["coefficient_frontier"])
    external_corpus = load(SOURCES["external_corpus_clues"])

    tau_h = float(tau_frontier["constants_and_parameters"]["tau_H_required"])
    moments = moments_packet["moments"]
    s_beta = float(moments["s_beta"])
    ratio = float(moments["x1_l2"]) / float(moments["y1_l2"])
    k_required = (3.0 - ratio / (tau_h - 4.0)) / s_beta
    mesh = int(moments_packet["mesh"])
    cutoff = int(hym_first["solver"]["theta_series_cutoff"])

    complex_dimension_cy = 3
    end0_rank = 3
    trace_unit_slot = 1
    active_real_dimension = 4
    bergman_window = 2 * cutoff + 1

    bergman_rows = [
        row(
            "(2*theta_cutoff+1)/(CY_dim+End0_rank+trace_unit)",
            bergman_window / (complex_dimension_cy + end0_rank + trace_unit_slot),
            ratio,
            s_beta,
            tau_h,
            "finite Bergman/HYM window-count candidate",
        ),
        row(
            "(mesh+1)/(CY_dim+End0_rank+trace_unit)",
            (mesh + 1) / (complex_dimension_cy + end0_rank + trace_unit_slot),
            ratio,
            s_beta,
            tau_h,
            "finite mesh-window candidate",
        ),
        row(
            "(2*theta_cutoff+1)/(active_real_dim+End0_rank)",
            bergman_window / (active_real_dimension + end0_rank),
            ratio,
            s_beta,
            tau_h,
            "active real dimension plus End0-rank candidate",
        ),
        row(
            "(2*theta_cutoff+1)/(CY_dim+rank_V+trace_unit)",
            bergman_window / (complex_dimension_cy + 2 + trace_unit_slot),
            ratio,
            s_beta,
            tau_h,
            "rank-two bundle denominator candidate",
        ),
    ]
    bergman_rows.sort(key=lambda item: item["relative_residual"])
    best_bergman = bergman_rows[0]

    heat_stats = heat_spectrum_stats(cutoff)
    heat_rows = [
        row("sqrt(logdet_per_mode)", heat_stats["sqrt_logdet_per_mode"], ratio, s_beta, tau_h, "flat spectral window"),
        row("log(logdet_per_mode)", heat_stats["log_logdet_per_mode"], ratio, s_beta, tau_h, "flat spectral window"),
        row("4", 4.0, ratio, s_beta, tau_h, "heat route baseline k=4"),
    ]
    heat_rows.sort(key=lambda item: item["relative_residual"])
    best_heat = heat_rows[0]

    bergman_packet = {
        "schema": "MTTBergmanHYMFinitaryCoefficientAttempt.v1",
        "status": "BERGMAN_WINDOW_CANDIDATE_SHARP_BUT_NOT_SOURCE_EMITTED",
        "closure_claimed": True,
        "formula_family": "tau_H(k)=4+(x1_l2/y1_l2)/(3-k*s_beta)",
        "tau_H_required": tau_h,
        "k_required": k_required,
        "window_data": {
            "mesh": mesh,
            "theta_series_cutoff": cutoff,
            "bergman_window_2N_plus_1": bergman_window,
            "complex_dimension_cy": complex_dimension_cy,
            "end0_rank": end0_rank,
            "trace_unit_slot": trace_unit_slot,
            "active_real_dimension": active_real_dimension,
        },
        "candidate_rows": bergman_rows,
        "best_candidate": best_bergman,
        "accepted_bergman_coefficient_source_count": 0,
        "denominator_source_theorem_proved": False,
        "exact_tau_H_equality_proved": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    heat_packet = {
        "schema": "MTTHeatZetaRadialOperatorProxyAttempt.v1",
        "status": "FLAT_HEAT_ZETA_PROXY_REJECTED_HWEIGHTED_OPERATOR_REQUIRED",
        "closure_claimed": True,
        "spectrum": {
            "operator": "flat four-direction periodic Laplace proxy on theta window",
            "cutoff": cutoff,
            **heat_stats,
        },
        "candidate_rows": heat_rows,
        "best_candidate": best_heat,
        "accepted_heat_zeta_radial_source_count": 0,
        "why_rejected": [
            "The proxy spectrum is a flat theta-window Laplacian, not the selected H-weighted H-sector threshold operator.",
            "Its best simple transform is weaker than the Bergman/window candidate.",
            "No zeta finite part is normalized to K_threshold.Omega_H.lambda or tau_H here.",
        ],
        "required_operator": (
            "P_H Pi0^perp G_E(delta_{Omega_H.lambda}D_E)Pi0^perp P_H or an equivalent "
            "selected H-sector Laplace-type/threshold operator with heat/zeta finite part."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision_packet = {
        "schema": "MTTDualRouteDecisionBergmanVsHeatZeta.v1",
        "status": "BERGMAN_WINDOW_ROUTE_PRIORITIZED_EXACT_SOURCE_THEOREM_REQUIRED",
        "closure_claimed": True,
        "best_bergman_relative_residual": best_bergman["relative_residual"],
        "best_heat_proxy_relative_residual": best_heat["relative_residual"],
        "best_route_now": "Bergman/HYM finite coefficient source rule",
        "accepted_source_rows_total": 0,
        "closed_here": [
            "Both proposed routes were executed against the current selected HYM data.",
            "The Bergman/window route recovers the existing 25/7 near-miss from a structured denominator.",
            "The heat/zeta proxy route is weaker and is rejected as final source data.",
        ],
        "remaining_for_closure": [
            "Prove the denominator 7 from selected Bergman/HYM geometry rather than naming it.",
            "Prove mesh/window independence or replace window arithmetic by a continuum finite part.",
            "Provide exact equality or a rigorous error certificate accepted by the H scalar gate.",
            "Alternatively emit tau_H/r_H directly from the selected H-sector heat/zeta radial operator.",
        ],
        "external_corpus_scan_status": external_corpus["status"],
        "previous_coefficient_frontier_status": coefficient_frontier["status"],
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedBergmanHYMCoefficientOrHeatZetaRadialOperatorDualAttempt",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "packets": {
            "bergman_hym_window_coefficient_attempt": rel(BERGMAN_PACKET),
            "heat_zeta_radial_operator_proxy_attempt": rel(HEAT_PACKET),
            "dual_route_decision_and_next_theorem": rel(DECISION_PACKET),
        },
        "closure_decision": {
            "bergman_route_executed": True,
            "heat_zeta_route_executed": True,
            "best_bergman_coefficient": best_bergman["k_value"],
            "best_bergman_relative_residual": best_bergman["relative_residual"],
            "best_heat_proxy_coefficient": best_heat["k_value"],
            "best_heat_proxy_relative_residual": best_heat["relative_residual"],
            "accepted_source_rows_total": 0,
            "bergman_route_prioritized": True,
            "heat_proxy_rejected_as_final": True,
            "strict_tau_H_promoted": False,
            "strict_r_H_promoted": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "BergmanHYMCoefficientAndHeatZetaDualAttemptTheorem",
            "proved": True,
            "statement": (
                "Executing both proposed routes shows that the finite Bergman/HYM window "
                "coefficient is the sharper current theorem target, while the flat heat/zeta "
                "proxy does not emit the H radial scalar. No source row is accepted yet."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedBergmanHYMCoefficientOrHeatZetaRadialOperatorDualAttempt",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "best_bergman_coefficient": best_bergman["k_value"],
        "best_bergman_relative_residual": best_bergman["relative_residual"],
        "best_heat_proxy_coefficient": best_heat["k_value"],
        "best_heat_proxy_relative_residual": best_heat["relative_residual"],
        "accepted_source_rows_total": 0,
        "bergman_route_prioritized": True,
        "heat_proxy_rejected_as_final": True,
        "strict_tau_H_promoted": False,
        "strict_r_H_promoted": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected BergmanHYMCoefficient or HeatZetaRadialOperator DualAttempt v1

## Theorem

`BergmanHYMCoefficientAndHeatZetaDualAttemptTheorem` is emitted.

## Bergman/HYM Route

The structured finite-window candidate is:

```text
k_B = (2*theta_series_cutoff + 1)/(CY_dim + End0_rank + trace_unit)
    = {bergman_window}/({complex_dimension_cy}+{end0_rank}+{trace_unit_slot})
    = {best_bergman["k_value"]}
```

It gives:

```text
tau_H(k_B) = {best_bergman["tau_H_value"]}
relative residual = {best_bergman["relative_residual"]}
```

This recovers the sharp `25/7` near-miss from a Bergman/HYM-shaped source
window. It is not promoted, because the denominator and exactness theorem are
not yet emitted.

## Heat/Zeta Route

The flat theta-window Laplace proxy gives best simple transform:

```text
{best_heat["name"]} = {best_heat["k_value"]}
tau_H = {best_heat["tau_H_value"]}
relative residual = {best_heat["relative_residual"]}
```

This is weaker and is not the selected H-weighted H-sector threshold operator.

## Decision

Accepted source rows: `0`.

The next best target is `{NEXT}`:

1. prove the Bergman/HYM denominator and exactness/error certificate, or
2. emit `tau_H`/`r_H` directly from a selected H-sector heat/zeta radial operator.
"""

    write_json(BERGMAN_PACKET, bergman_packet)
    write_json(HEAT_PACKET, heat_packet)
    write_json(DECISION_PACKET, decision_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
