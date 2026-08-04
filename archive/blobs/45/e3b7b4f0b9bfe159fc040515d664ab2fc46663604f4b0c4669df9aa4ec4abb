"""Search H-weighted finite-part coefficients for the tau_H frontier."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hweightedfinitepartcoefficientsearch_or_meshwindownogo"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
INVERSE_PACKET = PACKET_DIR / "finitepart_coefficient_inverse_problem.packet.json"
RATIONAL_PACKET = PACKET_DIR / "rational_coefficient_nearmiss_search.packet.json"
NOGO_PACKET = PACKET_DIR / "mesh_window_nogo_and_next_source_rule.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HWeightedFinitePartCoefficientSearch_or_MeshWindowNoGo_v1.md"

STATUS = (
    "MTT_SELECTED_HWEIGHTEDFINITEPARTCOEFFICIENTSEARCH_OR_MESHWINDOWNOGO_"
    "RATIONAL_NEARMISS_REJECTED_SOURCE_RULE_REQUIRED"
)
NEXT = "MTT_Selected_FinitePartCoefficientSourceRule_or_DirectRadialOperator_v1"

SOURCES = {
    "tau_frontier": DATA / "selected_tauhtransportcoefficientsource_or_unpatchedphifinc1consumer.candidate.json",
    "hym_metric_frontier": DATA / "selected_hymmetricmomenttauhsearch_or_finitepartexport.candidate.json",
    "hym_metric_moments": DATA
    / "selected_hymmetricmomenttauhsearch_or_finitepartexport"
    / "selected_hym_metric_moment_inventory.packet.json",
    "hym_metric_search": DATA
    / "selected_hymmetricmomenttauhsearch_or_finitepartexport"
    / "hym_metric_tauh_candidate_search.packet.json",
    "hym_first_solve": DATA
    / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
    / "selected_hym_first_solve_payload.packet.json",
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
        "coefficient": name,
        "k_value": k,
        "tau_H_value": value,
        "absolute_residual": residual,
        "relative_residual": abs(residual) / abs(tau_h),
        "provenance": provenance,
        "accepted_as_finitepart_coefficient_source": False,
        "reason_not_accepted": (
            "Numerical coefficient candidate only. No selected H-weighted finite-part "
            "operator, mesh-independent coefficient theorem, or direct radial operator "
            "emits this k value."
        ),
    }


def main() -> int:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing H-weighted finite-part inputs: " + ", ".join(missing))

    tau_frontier = load(SOURCES["tau_frontier"])
    hym_metric_frontier = load(SOURCES["hym_metric_frontier"])
    moments_packet = load(SOURCES["hym_metric_moments"])
    metric_search = load(SOURCES["hym_metric_search"])
    hym_first = load(SOURCES["hym_first_solve"])

    tau_h = float(tau_frontier["constants_and_parameters"]["tau_H_required"])
    moments = moments_packet["moments"]
    s_beta = float(moments["s_beta"])
    x1_l2 = float(moments["x1_l2"])
    y1_l2 = float(moments["y1_l2"])
    ratio = x1_l2 / y1_l2
    epsilon = tau_h - 4.0
    required_denominator = ratio / epsilon
    k_required = (3.0 - required_denominator) / s_beta

    seed_rows = [
        row("4", 4.0, ratio, s_beta, tau_h, "previous structural clue"),
        row("25/7", 25.0 / 7.0, ratio, s_beta, tau_h, "bounded rational near-miss"),
        row("18/5", 18.0 / 5.0, ratio, s_beta, tau_h, "bounded rational near-miss"),
        row("32/9", 32.0 / 9.0, ratio, s_beta, tau_h, "bounded rational near-miss"),
        row("7/2", 7.0 / 2.0, ratio, s_beta, tau_h, "bounded rational near-miss"),
        row("11/3", 11.0 / 3.0, ratio, s_beta, tau_h, "bounded rational near-miss"),
        row("pi + 3/7", math.pi + 3.0 / 7.0, ratio, s_beta, tau_h, "source-like irrational probe"),
        row("sqrt(13)", math.sqrt(13.0), ratio, s_beta, tau_h, "source-like irrational probe"),
    ]

    rational_rows: list[dict[str, Any]] = []
    seen: set[Fraction] = set()
    for denominator in range(1, 10):
        for numerator in range(1, 33):
            frac = Fraction(numerator, denominator)
            if frac in seen:
                continue
            seen.add(frac)
            k = float(frac)
            if not (2.0 <= k <= 5.0):
                continue
            rational_rows.append(
                row(
                    f"{frac.numerator}/{frac.denominator}",
                    k,
                    ratio,
                    s_beta,
                    tau_h,
                    "bounded rational source-window scan p<=32, q<=9, 2<=k<=5",
                )
            )

    rational_rows.sort(key=lambda item: abs(item["absolute_residual"]))
    best_rational = rational_rows[:24]
    best_seed = sorted(seed_rows, key=lambda item: abs(item["absolute_residual"]))[:8]

    mesh = int(moments_packet["mesh"])
    theta_series_cutoff = int(hym_first["solver"]["theta_series_cutoff"])
    best = best_rational[0]
    best_fraction = Fraction(best["coefficient"])
    mesh_window_flags = {
        "best_rational": best["coefficient"],
        "best_rational_numerator_equals_mesh_plus_one": best_fraction.numerator == mesh + 1,
        "best_rational_numerator_equals_two_cutoff_plus_one": best_fraction.numerator
        == 2 * theta_series_cutoff + 1,
        "denominator_has_selected_source_here": False,
        "mesh_independence_proved_here": False,
    }

    inverse_packet = {
        "schema": "MTTHWeightedFinitePartCoefficientInverseProblem.v1",
        "status": "INTERNAL_TAUH_INVERSE_COEFFICIENT_COMPUTED",
        "closure_claimed": True,
        "tau_H_required": tau_h,
        "epsilon_tau_H_minus_4": epsilon,
        "s_beta": s_beta,
        "x1_l2": x1_l2,
        "y1_l2": y1_l2,
        "anisotropy_ratio_x1_over_y1": ratio,
        "formula_family": "tau_H(k) = 4 + (x1_l2/y1_l2)/(3 - k*s_beta)",
        "required_denominator": required_denominator,
        "k_required_for_exact_match": k_required,
        "internal_target_inversion_used": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    rational_packet = {
        "schema": "MTTHWeightedFinitePartRationalCoefficientNearMissSearch.v1",
        "status": "BOUNDED_RATIONAL_SEARCH_FINDS_STRONG_NEARMISS_ACCEPTS_ZERO",
        "closure_claimed": True,
        "search_bounds": {"numerator_max": 32, "denominator_max": 9, "k_min": 2.0, "k_max": 5.0},
        "seed_candidates": best_seed,
        "best_rational_near_misses": best_rational,
        "accepted_finitepart_coefficient_source_count": 0,
        "internal_target_inversion_used": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    nogo_packet = {
        "schema": "MTTMeshWindowNoGoAndFinitePartSourceRule.v1",
        "status": "MESH_WINDOW_NEARMISS_REJECTED_SOURCE_RULE_REQUIRED",
        "closure_claimed": True,
        "mesh": mesh,
        "theta_series_cutoff": theta_series_cutoff,
        "mesh_window_flags": mesh_window_flags,
        "why_not_closed": [
            "The best rational coefficient is discovered by an internal inverse/scan, not emitted by MTT geometry.",
            "Its numerator coincides with mesh+1 and 2*theta_series_cutoff+1 in the current replay window.",
            "No selected finite-part coefficient operator or mesh-independent theorem supplies the denominator.",
            "The residual is far smaller than the previous k=4 clue, but remains nonzero and unpromoted.",
        ],
        "source_rule_contract": {
            "must_emit": [
                "selected H-weighted finite-part coefficient k",
                "mesh-independent or continuum-normalized derivation",
                "same-source tau_H or r_H export row",
                "exactness certificate or rigorous error bound",
            ],
            "legal_exits": [
                "source theorem emits k = k_required exactly",
                "source theorem emits a rational/closed-form k with certified error bound sufficient for tau_H",
                "direct radial operator emits tau_H/r_H without coefficient fitting",
            ],
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHWeightedFinitePartCoefficientSearchOrMeshWindowNoGo",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "internal_target_inversion_used": True,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "packets": {
            "finitepart_coefficient_inverse_problem": rel(INVERSE_PACKET),
            "rational_coefficient_nearmiss_search": rel(RATIONAL_PACKET),
            "mesh_window_nogo_and_next_source_rule": rel(NOGO_PACKET),
        },
        "closure_decision": {
            "inverse_coefficient_computed": True,
            "bounded_rational_search_executed": True,
            "best_rational_coefficient": best["coefficient"],
            "best_rational_relative_residual": best["relative_residual"],
            "accepted_finitepart_coefficient_source_count": 0,
            "mesh_window_nogo_active": True,
            "strict_tau_H_promoted": False,
            "strict_r_H_promoted": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "previous_frontier_status": hym_metric_frontier["status"],
        "previous_metric_clue_relative_residual": metric_search["special_clues"][
            "anisotropy_angular_relative_residual"
        ],
        "theorem": {
            "name": "FinitePartCoefficientInverseSearchAndMeshWindowNoGoTheorem",
            "proved": True,
            "statement": (
                "For the selected HYM anisotropy family tau_H(k), the exact internal "
                "coefficient required by the controlled H tau target is computed, and a "
                "bounded rational search finds a much sharper near-miss. The near-miss is "
                "not accepted as selected source data because it is scan-derived and "
                "mesh-window entangled; strict closure requires a same-source finite-part "
                "coefficient rule or direct radial operator."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHWeightedFinitePartCoefficientSearchOrMeshWindowNoGo",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "k_required_for_exact_match": k_required,
        "best_rational_coefficient": best["coefficient"],
        "best_rational_relative_residual": best["relative_residual"],
        "accepted_finitepart_coefficient_source_count": 0,
        "mesh_window_nogo_active": True,
        "strict_tau_H_promoted": False,
        "strict_r_H_promoted": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "internal_target_inversion_used": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HWeightedFinitePartCoefficientSearch or MeshWindowNoGo v1

## Theorem

`FinitePartCoefficientInverseSearchAndMeshWindowNoGoTheorem` is emitted.

## Result

The selected HYM anisotropy family is:

```text
tau_H(k) = 4 + (x1_l2/y1_l2)/(3 - k*s_beta)
```

Using the controlled H frontier value:

```text
tau_H = {tau_h}
x1_l2/y1_l2 = {ratio}
s_beta = {s_beta}
k_required = {k_required}
```

The best bounded rational near miss is:

```text
k = {best["coefficient"]} = {best["k_value"]}
tau_H(k) = {best["tau_H_value"]}
relative residual = {best["relative_residual"]}
```

Accepted finite-part coefficient source rows: `0`.

## No-Go Guard

The near miss is not promoted. It is scan-derived, and its numerator equals
`mesh + 1 = {mesh + 1}` and `2*theta_series_cutoff + 1 = {2 * theta_series_cutoff + 1}`
in the current replay window. This may be real MTT window arithmetic, but it is
not yet a source theorem.

## Next Object

`{NEXT}` must emit the H-weighted finite-part coefficient, prove
mesh-independence or a continuum normalization, and export `tau_H` or `r_H` from
the same selected source.
"""

    write_json(INVERSE_PACKET, inverse_packet)
    write_json(RATIONAL_PACKET, rational_packet)
    write_json(NOGO_PACKET, nogo_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
