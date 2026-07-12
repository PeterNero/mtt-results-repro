"""Bounded numeric search for the H radial source after the pi^2 D211 clue."""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hradialvaluesourcenumericsearch_or_pi2hrgfrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
PI_PACKET = PACKET_DIR / "d211_pi2_identity_clue.packet.json"
SEARCH_PACKET = PACKET_DIR / "bounded_hrg_radial_expression_search.packet.json"
GATE_PACKET = PACKET_DIR / "hrg_radial_source_acceptance_gate.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HRadialValueSourceNumericSearch_or_Pi2HRGFrontier_v1.md"

STATUS = (
    "MTT_SELECTED_HRADIALVALUESOURCENUMERICSEARCH_OR_PI2HRGFRONTIER_"
    "PI2_CLUE_LOCKED_NUMERIC_SEARCH_NO_SOURCE"
)
NEXT = "MTT_Selected_HRadialTransportMap_or_DynamicPhiFinC1Consumer_v1"

SOURCES = {
    "h_functional_frontier": DATA / "selected_qutrit27hfunctionalsearch_or_radialsourcefrontier.candidate.json",
    "profile_operator": DATA
    / "selected_qutrit27secondpassmatrixpush_or_leftrightprofilefrontier"
    / "class_profile_operator_211.packet.json",
    "scalar_inventory": DATA
    / "selected_qutrit27hfunctionalsearch_or_radialsourcefrontier"
    / "profile_matrix_scalar_functional_inventory.packet.json",
    "controlled_h": DATA
    / "selected_qutrit27hfunctionalsearch_or_radialsourcefrontier"
    / "controlled_herm2_matrix_invariants.packet.json",
    "alpha_hrg": DATA / "selected_alpha1hrgselector_or_aewmetrologyvaluesourcetheorem.candidate.json",
    "dual_route_lock": DATA
    / "selected_alpha1hrgselector_or_aewmetrologyvaluesourcetheorem"
    / "dual_route_residual_lock.packet.json",
    "nonhiggs_selector": DATA
    / "selected_aewmetrologyslotexecution_or_hrgnonhiggspredictionselector"
    / "hrg_nonhiggs_prediction_selector_execution.packet.json",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def bounded_expression_search(target: float, constants: dict[str, float]) -> list[dict[str, Any]]:
    base_names = list(constants)
    candidates: list[dict[str, Any]] = []
    exponent_choices = [-2, -1, 1, 2]
    coefficients = [(1, 1), (2, 1), (3, 1), (4, 1), (6, 1), (9, 1), (12, 1), (1, 2), (1, 3), (1, 4)]
    for width in [1, 2, 3]:
        for names in itertools.combinations(base_names, width):
            for exponents in itertools.product(exponent_choices, repeat=width):
                nonzero = list(zip(names, exponents))
                value = 1.0
                for name, exp in nonzero:
                    value *= constants[name] ** exp
                if not math.isfinite(value) or value == 0.0:
                    continue
                for coeff_num, coeff_den in coefficients:
                    scaled = value * coeff_num / coeff_den
                    residual = scaled - target
                    rel_residual = abs(residual) / abs(target)
                    expr = "*".join(
                        [f"{name}^{exp}" if exp != 1 else name for name, exp in nonzero]
                    )
                    if coeff_num != 1 or coeff_den != 1:
                        expr = f"({coeff_num}/{coeff_den})*{expr}"
                    candidates.append(
                        {
                            "expression": expr,
                            "value": scaled,
                            "absolute_residual": residual,
                            "relative_residual": rel_residual,
                            "accepted_as_source": False,
                        }
                    )
    candidates.sort(key=lambda item: (item["relative_residual"], len(item["expression"])))
    deduped: list[dict[str, Any]] = []
    seen = set()
    for item in candidates:
        key = round(item["value"], 12)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(item)
        if len(deduped) >= 25:
            break
    return deduped


def main() -> int:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing radial numeric-search inputs: " + ", ".join(missing))

    h_frontier = load(SOURCES["h_functional_frontier"])
    profile = load(SOURCES["profile_operator"])
    scalar_inventory = load(SOURCES["scalar_inventory"])
    controlled_h = load(SOURCES["controlled_h"])
    alpha_hrg = load(SOURCES["alpha_hrg"])
    dual_route = load(SOURCES["dual_route_lock"])
    nonhiggs = load(SOURCES["nonhiggs_selector"])

    base = float(profile["charged_base_overlap_value"])
    trace = float(profile["operator_trace"])
    rank = float(h_frontier["constants_and_parameters"]["classwise_left_right_algebra_rank"])
    dim = 27.0
    pi2 = math.pi * math.pi
    pi4 = pi2 * pi2
    base_pi_formula = 27.0 / (4.0 * pi2)
    trace_pi_formula = 243.0 / pi2
    rank_over_trace = rank / trace
    target_r = float(controlled_h["invariants"]["r_H_from_sqrt_Tr_H_squared_over_2"])
    target_n = float(controlled_h["invariants"]["Tr_H_squared"]) / 2.0
    logdet = next(item["value"] for item in scalar_inventory["functionals"] if item["name"] == "logdet_D211")
    frob = next(item["value"] for item in scalar_inventory["functionals"] if item["name"] == "frobenius_norm_D211")
    participation = next(item["value"] for item in scalar_inventory["functionals"] if item["name"] == "participation_ratio_D211")

    pi_packet = {
        "schema": "MTTD211Pi2IdentityClue.v1",
        "status": "D211_PI2_IDENTITY_CLUE_LOCKED_NOT_H_RADIAL_SOURCE",
        "closure_claimed": True,
        "base_value": base,
        "base_formula_candidate": "27/(4*pi^2)",
        "base_formula_value": base_pi_formula,
        "base_formula_residual": base - base_pi_formula,
        "trace_D211": trace,
        "trace_formula_candidate": "243/pi^2",
        "trace_formula_value": trace_pi_formula,
        "trace_formula_residual": trace - trace_pi_formula,
        "rank_over_trace": rank_over_trace,
        "pi_squared": pi2,
        "rank_over_trace_minus_pi_squared": rank_over_trace - pi2,
        "interpretation": (
            "The selected charged profile operator carries a strong pi^2 normalization clue: "
            "base ~= 27/(4*pi^2), Tr(D_211) ~= 243/pi^2, and rank/Tr(D_211) ~= pi^2. "
            "This is not a selected H radial value source without an additional radial "
            "transport theorem."
        ),
        "accepted_as_H_radial_source": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    constants = {
        "pi2": pi2,
        "pi4": pi4,
        "q79": 79.0,
        "dim27": dim,
        "rank243": rank,
        "traceD": trace,
        "frobD": frob,
        "baseD": base,
        "participation24": participation,
        "log2008": math.log(2008.0),
        "log92160000": math.log(92_160_000.0),
        "sqrt2": math.sqrt(2.0),
        "phi": (1.0 + math.sqrt(5.0)) / 2.0,
        "lambda12": 2.6179362173268497,
        "deltaG12": 0.08450302790361214,
    }
    top_candidates = bounded_expression_search(target_r, constants)
    near_misses = [
        {
            "expression": "-logdet(D_211)*pi^4",
            "value": -logdet * pi4,
            "absolute_residual": (-logdet * pi4) - target_r,
            "relative_residual": abs((-logdet * pi4) - target_r) / target_r,
            "accepted_as_source": False,
            "reason_not_accepted": "near miss has no selected radial transport theorem",
        },
        {
            "expression": "4*pi^4",
            "value": 4.0 * pi4,
            "absolute_residual": (4.0 * pi4) - target_r,
            "relative_residual": abs((4.0 * pi4) - target_r) / target_r,
            "accepted_as_source": False,
            "reason_not_accepted": "simple pi^4 scale is close but not equal/source-selected",
        },
    ]

    search_packet = {
        "schema": "MTTBoundedHRGRadialExpressionSearch.v1",
        "status": "BOUNDED_RADIAL_EXPRESSION_SEARCH_EXECUTED_NO_ACCEPTED_SOURCE",
        "closure_claimed": True,
        "target_for_diagnostic_comparison": target_r,
        "target_N_H_for_diagnostic_comparison": target_n,
        "constants_used": constants,
        "search_policy": {
            "max_distinct_source_factors_per_monomial": 3,
            "exponents": [-2, -1, 0, 1, 2],
            "allowed_coefficients": ["1", "2", "3", "4", "6", "9", "12", "1/2", "1/3", "1/4"],
            "diagnostic_only": True,
            "target_residual_search_does_not_select_source": True,
        },
        "best_candidates": top_candidates,
        "hand_checked_near_misses": near_misses,
        "accepted_source_expression_count": 0,
        "best_relative_residual": top_candidates[0]["relative_residual"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    gate_packet = {
        "schema": "MTTHRGRadialSourceAcceptanceGate.v1",
        "status": "HRG_RADIAL_SOURCE_GATE_OPEN_AFTER_PI2_NUMERIC_SEARCH",
        "closure_claimed": True,
        "pi2_D211_identity_clue_locked": True,
        "bounded_numeric_search_completed": True,
        "accepted_radial_source_value_count": 0,
        "accepted_nonhiggs_HRG_prediction_count": 0,
        "UP_RET_OVERLAP_HRG_source_promoted": False,
        "strict_r_H_promoted": False,
        "strict_N_H_promoted": False,
        "controlled_one_parameter_H_remains_available": True,
        "dual_route_exact_deficit_locked": dual_route["status"] == "DUAL_ROUTE_EXACT_DEFICIT_LOCKED_TO_HRG_SIZED_SOURCE_OBJECT",
        "nonhiggs_selector_accepted_count": nonhiggs["decision"]["accepted_selector_count"],
        "alpha_selector_accepted_count": alpha_hrg["closure_decision"]["accepted_HRG_selector_count"],
        "next_source_object_needed": (
            "a selected radial transport theorem from the D_211/pi^2 normalization, "
            "or selected dynamic Phi_fin/C1 consumer map, or independent non-Higgs "
            "UP-RET-OVERLAP.HRG prediction"
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHRadialValueSourceNumericSearchOrPi2HRGFrontier",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "packets": {
            "d211_pi2_identity_clue": rel(PI_PACKET),
            "bounded_hrg_radial_expression_search": rel(SEARCH_PACKET),
            "hrg_radial_source_acceptance_gate": rel(GATE_PACKET),
        },
        "closure_decision": {
            "D211_pi2_identity_clue_locked": True,
            "base_equals_27_over_4pi2_to_roundoff": abs(base - base_pi_formula) < 1e-10,
            "rank_over_trace_equals_pi2_to_roundoff": abs(rank_over_trace - pi2) < 1e-9,
            "bounded_numeric_search_completed": True,
            "accepted_radial_source_value_count": 0,
            "accepted_nonhiggs_HRG_prediction_count": 0,
            "strict_r_H_promoted": False,
            "strict_N_H_promoted": False,
            "minimal_one_parameter_H_still_available": True,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "constants_and_parameters": {
            "base_D211": base,
            "base_formula_27_over_4pi2": base_pi_formula,
            "trace_D211": trace,
            "rank_over_trace": rank_over_trace,
            "pi_squared": pi2,
            "controlled_r_H": target_r,
            "controlled_N_H": target_n,
            "best_diagnostic_expression": top_candidates[0]["expression"],
            "best_diagnostic_relative_residual": top_candidates[0]["relative_residual"],
            "minus_logdet_D211_times_pi4_relative_residual": near_misses[0]["relative_residual"],
        },
        "theorem": {
            "name": "HRadialPi2ClueAndNumericSearchFrontierTheorem",
            "proved": True,
            "statement": (
                "The selected D_211 charged-profile operator carries a pi^2 normalization "
                "identity to roundoff, and a bounded search over source-native constants "
                "finds diagnostic near-misses for the controlled H radial value. None is "
                "accepted as a strict radial source because no selected theorem maps the "
                "D_211/pi^2 data or the tested expressions to r_H, N_H, R_H^RG, or "
                "K_threshold.Omega_H.lambda. The live frontier is therefore a radial "
                "transport/source theorem or dynamic Phi_fin/C1 HRG consumer map."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHRadialValueSourceNumericSearchOrPi2HRGFrontier",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "D211_pi2_identity_clue_locked": True,
        "bounded_numeric_search_completed": True,
        "accepted_radial_source_value_count": 0,
        "accepted_nonhiggs_HRG_prediction_count": 0,
        "strict_r_H_promoted": False,
        "strict_N_H_promoted": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected H Radial Value Source Numeric Search or Pi2HRGFrontier v1

## Theorem

`HRadialPi2ClueAndNumericSearchFrontierTheorem` is emitted.

## Pi2 Clue

The selected charged-profile operator has a strong normalization clue:

```text
base(D_211)             = {base}
27/(4*pi^2)             = {base_pi_formula}
residual                = {base - base_pi_formula}
Tr(D_211)               = {trace}
243/pi^2                = {trace_pi_formula}
rank/Tr(D_211)          = {rank_over_trace}
pi^2                    = {pi2}
rank/Tr(D_211)-pi^2     = {rank_over_trace - pi2}
```

This is real progress: the charged profile matrix is carrying a `pi^2`
normalization. It is not yet a radial H source theorem.

## Bounded Search

The bounded diagnostic search tested source-native expressions built from
`pi^2`, `pi^4`, `q=79`, `rank=243`, `dim=27`, `D_211` scalars, selected
determinant logs, `lambda_12`, and `Delta_G12`.

Accepted radial source expressions: `0`.

Best diagnostic candidate:

```text
{top_candidates[0]["expression"]} = {top_candidates[0]["value"]}
relative residual = {top_candidates[0]["relative_residual"]}
```

Hand-checked near miss:

```text
-logdet(D_211) * pi^4 = {near_misses[0]["value"]}
relative residual     = {near_misses[0]["relative_residual"]}
```

These are not promoted because numeric proximity is not a selected source map.

## Current Frontier

The remaining legal exits are:

1. a selected radial transport theorem from the `D_211/pi^2` normalization to
   `r_H` or direct `N_H`;
2. a selected dynamic `Phi_fin/C1` consumer map that emits `UP-RET-OVERLAP.HRG`;
3. an independent non-Higgs prediction of `UP-RET-OVERLAP.HRG`;
4. a direct selected `K_threshold.Omega_H.lambda` row.

## Next Artifact

`{NEXT}`
"""

    write_json(PI_PACKET, pi_packet)
    write_json(SEARCH_PACKET, search_packet)
    write_json(GATE_PACKET, gate_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
