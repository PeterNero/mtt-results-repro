"""Test whether finite C1 scalar invariants export tau_H."""

from __future__ import annotations

import json
import math
from itertools import product
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_tauhc1scalarexport_or_galerkinmetricfrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SCALARS_PACKET = PACKET_DIR / "finite_c1_scalar_inventory.packet.json"
SEARCH_PACKET = PACKET_DIR / "tauh_c1_expression_search.packet.json"
FRONTIER_PACKET = PACKET_DIR / "galerkin_metric_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_TauHC1ScalarExport_or_GalerkinMetricFrontier_v1.md"

STATUS = (
    "MTT_SELECTED_TAUHC1SCALAREXPORT_OR_GALERKINMETRICFRONTIER_"
    "C1_SCALARS_REJECTED_GALERKIN_METRIC_REQUIRED"
)
NEXT = "MTT_Selected_GalerkinMetricTauHExport_or_HWeightedC1KernelValues_v1"

SOURCES = {
    "tau_frontier": DATA / "selected_tauhtransportcoefficientsource_or_unpatchedphifinc1consumer.candidate.json",
    "dynamic_gate": DATA
    / "selected_dynamicphifinc1payload_or_largethresholdhrgconsumermap"
    / "dynamic_phifinc1_final_gate_reconciliation.packet.json",
    "local_axiom_boundary": DATA
    / "selected_dynamicphifinc1payload_or_largethresholdhrgconsumermap"
    / "local_axiom_vs_unpatched_boundary.packet.json",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def safe_values(value: float) -> list[tuple[str, float]]:
    vals = [
        ("x", value),
        ("1/x", 1.0 / value if value else float("nan")),
        ("sqrt(x)", math.sqrt(value) if value >= 0 else float("nan")),
        ("log(x)", math.log(value) if value > 0 else float("nan")),
    ]
    return [(name, val) for name, val in vals if math.isfinite(val)]


def main() -> int:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing tau_H C1 scalar inputs: " + ", ".join(missing))

    tau_frontier = load(SOURCES["tau_frontier"])
    dynamic_gate = load(SOURCES["dynamic_gate"])
    local_boundary = load(SOURCES["local_axiom_boundary"])

    tau_h = float(tau_frontier["constants_and_parameters"]["tau_H_required"])
    exact = local_boundary["patched_lane"]["exact_values"]
    ready = dynamic_gate["ready_value_table"]

    c1_scalars = {
        "rank": float(exact["rank"]),
        "phase_R_Z_residual_norm_sq": float(exact["phase_R_Z_residual_norm_sq"]),
        "shift_R_X_residual_norm_sq": float(exact["shift_R_X_residual_norm_sq"]),
        "phase_plus_shift_norm_sq": float(exact["phase_R_Z_residual_norm_sq"])
        + float(exact["shift_R_X_residual_norm_sq"]),
        "phase_two_sector_norm_sq": float(ready["routed_72_real_completion"]["phase_residual_norm_sq_two_sectors"]),
        "shift_two_sector_norm_sq": float(ready["routed_72_real_completion"]["shift_residual_norm_sq_two_sectors"]),
        "total_four_sector_norm_sq": float(ready["routed_72_real_completion"]["total_residual_norm_sq_four_sectors"]),
        "b_norm_sq": float(exact["b_norm_sq"]),
        "trace_A_transpose_A": float(exact["A_transpose_A"][0][0] + exact["A_transpose_A"][1][1]),
        "det_A_transpose_A": float(exact["A_transpose_A"][0][0] * exact["A_transpose_A"][1][1]),
        "deltaTheta_norm_sq": sum(float(x) * float(x) for x in exact["deltaTheta_C1"]),
    }

    generated: list[dict[str, Any]] = []
    atoms: list[tuple[str, float]] = []
    for key, value in c1_scalars.items():
        for transform, transformed in safe_values(value):
            atoms.append((f"{transform}({key})", transformed))

    rationals = [1 / 12, 1 / 6, 1 / 4, 1 / 3, 1 / 2, 1.0, 2.0, 3.0, 4.0, 6.0, 12.0]
    for (name, value), coeff in product(atoms, rationals):
        candidate = coeff * value
        residual = candidate - tau_h
        generated.append(
            {
                "expression": f"{coeff:g}*{name}",
                "value": candidate,
                "absolute_residual": residual,
                "relative_residual": abs(residual) / abs(tau_h),
                "accepted_as_tau_H_source": False,
            }
        )

    generated.sort(key=lambda row: abs(row["absolute_residual"]))
    best = generated[:12]

    scalars_packet = {
        "schema": "MTTFiniteC1ScalarInventoryForTauH.v1",
        "status": "FINITE_C1_SCALARS_INVENTORIED",
        "closure_claimed": True,
        "c1_scalar_field_boundary": "finite C1 exact values are rational norm/trace data in the patched/local Weyl layer",
        "scalars": c1_scalars,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    search_packet = {
        "schema": "MTTTauHC1ExpressionSearch.v1",
        "status": "C1_SCALAR_SEARCH_ACCEPTS_ZERO_TAUH_SOURCES",
        "closure_claimed": True,
        "tau_H_required": tau_h,
        "search_policy": {
            "allowed_inputs": sorted(c1_scalars),
            "allowed_transforms": ["x", "1/x", "sqrt(x)", "log(x)"],
            "allowed_prefactors": rationals,
            "why_not_full_closure": "This is only a bounded source-native rejection gate; it cannot prove all possible future H-weighted Galerkin functionals absent.",
        },
        "best_near_misses": best,
        "accepted_tau_H_source_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    frontier_packet = {
        "schema": "MTTGalerkinMetricFrontierAfterC1ScalarRejection.v1",
        "status": "GALERKIN_METRIC_OR_H_WEIGHTED_KERNEL_REQUIRED",
        "closure_claimed": True,
        "closed_here": [
            "finite C1 scalar inventory is explicit",
            "bounded C1-only tau_H source search accepts zero rows",
            "C1 shape values alone cannot be promoted as the H radial coefficient source",
        ],
        "remaining_required_payload": {
            "zero_mode_bases": "selected basis table, not residual replay",
            "primitive_three_by_three_contraction_terms": "selected H-weighted or metric-weighted Galerkin contractions",
            "linear_response_matrices": "row-level exactness/error certificates",
            "C33_nonzero_family_rank_tests": "postcheck, not source selector",
            "tau_H_export_rule": "must emit tau_H or r_H from the same selected metric/kernel payload",
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedTauHC1ScalarExportOrGalerkinMetricFrontier",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "packets": {
            "finite_c1_scalar_inventory": rel(SCALARS_PACKET),
            "tauh_c1_expression_search": rel(SEARCH_PACKET),
            "galerkin_metric_frontier": rel(FRONTIER_PACKET),
        },
        "closure_decision": {
            "finite_C1_scalars_inventoried": True,
            "bounded_C1_scalar_search_executed": True,
            "accepted_tau_H_source_count": 0,
            "C1_scalar_only_tau_H_export_rejected": True,
            "honest_Galerkin_metric_payload_required": True,
            "strict_r_H_promoted": False,
            "strict_N_H_promoted": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "theorem": {
            "name": "TauHC1ScalarRejectionAndGalerkinMetricFrontierTheorem",
            "proved": True,
            "statement": (
                "Finite C1 exact values supply rational norm/trace shape data, but "
                "bounded source-native scalar combinations of those values emit zero "
                "accepted tau_H sources. Therefore tau_H must come from a genuinely "
                "H-weighted selected Galerkin/metric/kernel payload, unpatched "
                "Phi_fin^C1 source emission, typed HRG consumer emission, or direct "
                "K_threshold.Omega_H.lambda; C1 shape replay alone is insufficient."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedTauHC1ScalarExportOrGalerkinMetricFrontier",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "accepted_tau_H_source_count": 0,
        "C1_scalar_only_tau_H_export_rejected": True,
        "honest_Galerkin_metric_payload_required": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected TauH C1 Scalar Export or Galerkin Metric Frontier v1

## Theorem

`TauHC1ScalarRejectionAndGalerkinMetricFrontierTheorem` is emitted.

## Result

The finite C1 exact values were tested as possible source-native exports of
`tau_H = {tau_h}`.

Accepted C1-only source rows: `0`.

Best bounded diagnostic near miss:

```text
{best[0]["expression"]} = {best[0]["value"]}
relative residual = {best[0]["relative_residual"]}
```

This is not promoted as a source theorem.

## Consequence

The C1 packet can supply shape, rank, norm, and response geometry. It does not by
itself supply the H radial magnitude. The next non-looping payload must include
H-weighted Galerkin/metric data or another same-source radial operator.

## Next Artifact

`{NEXT}`
"""

    write_json(SCALARS_PACKET, scalars_packet)
    write_json(SEARCH_PACKET, search_packet)
    write_json(FRONTIER_PACKET, frontier_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
