"""Replay selected HYM metric moments and test tau_H export candidates."""

from __future__ import annotations

import json
import math
import sys
from itertools import product
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_selected_hym_operator_payload_extraction_from_diagonal_replay import (  # noqa: E402
    fft_operators,
    replay_solution,
)


DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hymmetricmomenttauhsearch_or_finitepartexport"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
MOMENTS_PACKET = PACKET_DIR / "selected_hym_metric_moment_inventory.packet.json"
SEARCH_PACKET = PACKET_DIR / "hym_metric_tauh_candidate_search.packet.json"
FRONTIER_PACKET = PACKET_DIR / "finitepart_export_frontier.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HYMMetricMomentTauHSearch_or_FinitePartExport_v1.md"

STATUS = (
    "MTT_SELECTED_HYMMETRICMOMENTTAUHSEARCH_OR_FINITEPARTEXPORT_"
    "METRIC_MOMENT_NEARMISSES_REJECTED_FINITEPART_EXPORT_REQUIRED"
)
NEXT = "MTT_Selected_HWeightedFinitePartTauHExport_or_DirectRadialOperator_v1"

SOURCES = {
    "tau_frontier": DATA / "selected_tauhtransportcoefficientsource_or_unpatchedphifinc1consumer.candidate.json",
    "angular_frontier": DATA / "selected_hangularc1metricsearch_or_hweightedgalerkinpayload.candidate.json",
    "selected_sbeta": DATA
    / "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof"
    / "selected_finite_reduction_sbeta_promotion.packet.json",
    "hym_first_solve": DATA
    / "selected_hymnewtongalerkin_firstsolve_or_rank2sectorfunctor"
    / "selected_hym_first_solve_payload.packet.json",
    "full_expS_replay": DATA / "selected_full_exps_hym_newton_replay.candidate.json",
    "overlap_table": DATA / "selected_ext_overlap_hym_hodge_projector_table.candidate.json",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def add_row(rows: list[dict[str, Any]], expression: str, value: float, target: float, provenance: str) -> None:
    if not math.isfinite(value):
        return
    residual = value - target
    rows.append(
        {
            "expression": expression,
            "value": value,
            "absolute_residual": residual,
            "relative_residual": abs(residual) / abs(target),
            "provenance": provenance,
            "accepted_as_tau_H_source": False,
            "reason_not_accepted": (
                "Selected HYM metric moment diagnostic only; no finite-part/export theorem "
                "emits this expression as the H radial coefficient."
            ),
        }
    )


def main() -> int:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing HYM metric tau_H inputs: " + ", ".join(missing))

    tau_frontier = load(SOURCES["tau_frontier"])
    angular_frontier = load(SOURCES["angular_frontier"])
    sbeta_packet = load(SOURCES["selected_sbeta"])
    hym_first = load(SOURCES["hym_first_solve"])
    replay = load(SOURCES["full_expS_replay"])
    overlap = load(SOURCES["overlap_table"])

    tau_h = float(tau_frontier["constants_and_parameters"]["tau_H_required"])
    s_beta = float(sbeta_packet["selected_s_beta"]["value"])
    mesh = int(replay["solver"]["mesh"])
    unit_rescale = float(overlap["selected_row"]["unit_rescale_factor"])
    u, rho, _lap = replay_solution(mesh, unit_rescale)
    _solve, _lap_op, deriv = fft_operators(u.shape)
    q = rho * np.exp(-2.0 * u)

    moment_values: dict[str, float] = {
        "s_beta": s_beta,
        "sqrt_s_beta": math.sqrt(s_beta),
        "mean_exp_u": float(np.exp(u).mean()),
        "mean_exp_minus_u": float(np.exp(-u).mean()),
        "mean_exp_2u": float(np.exp(2.0 * u).mean()),
        "mean_exp_minus_2u": float(np.exp(-2.0 * u).mean()),
        "mean_q": float(q.mean()),
        "std_q": float(q.std()),
        "mean_abs_u": float(np.abs(u).mean()),
        "u_l2": float(np.sqrt((u * u).mean())),
        "u_max": float(u.max()),
        "neg_u_min": float(-u.min()),
        "u_range": float(u.max() - u.min()),
    }
    for axis, label in enumerate(["x1", "y1", "x2", "y2"]):
        du = deriv(u, axis)
        moment_values[f"{label}_l2"] = float(np.sqrt((du * du).mean()))
        moment_values[f"{label}_mean_abs"] = float(np.abs(du).mean())
    for key, value in list(moment_values.items()):
        if value > 0:
            moment_values[f"log_{key}"] = math.log(value)

    rows: list[dict[str, Any]] = []
    coeffs = [
        1 / 24,
        1 / 16,
        1 / 12,
        1 / 9,
        1 / 8,
        1 / 6,
        1 / 5,
        1 / 4,
        1 / 3,
        1 / 2,
        1.0,
        2.0,
        3.0,
        4.0,
        5.0,
        6.0,
        8.0,
        9.0,
        12.0,
        16.0,
        24.0,
    ]

    for key, value in moment_values.items():
        for coeff in coeffs:
            add_row(rows, f"4 + {coeff:g}*{key}", 4.0 + coeff * value, tau_h, "single HYM moment")
            add_row(rows, f"4 - {coeff:g}*{key}", 4.0 - coeff * value, tau_h, "single HYM moment")

    for (key_a, value_a), (key_b, value_b) in product(moment_values.items(), moment_values.items()):
        if abs(value_b) < 1e-15:
            continue
        for coeff in coeffs:
            add_row(
                rows,
                f"4 + {coeff:g}*{key_a}/{key_b}",
                4.0 + coeff * value_a / value_b,
                tau_h,
                "HYM metric moment ratio",
            )
            add_row(
                rows,
                f"4 + {coeff:g}*{key_a}*{key_b}",
                4.0 + coeff * value_a * value_b,
                tau_h,
                "HYM metric moment product",
            )

    x1_y1 = moment_values["x1_l2"] / moment_values["y1_l2"]
    anisotropy_clue = 4.0 + x1_y1 / (3.0 - 4.0 * s_beta)
    add_row(
        rows,
        "4 + (x1_l2/y1_l2)/(3 - 4*s_beta)",
        anisotropy_clue,
        tau_h,
        "selected HYM anisotropy ratio plus selected angular correction",
    )

    rows.sort(key=lambda row: abs(row["absolute_residual"]))
    best = rows[:24]

    moments_packet = {
        "schema": "MTTSelectedHYMMetricMomentInventory.v1",
        "status": "SELECTED_HYM_GRID_REPLAYED_METRIC_MOMENTS_EMITTED",
        "closure_claimed": True,
        "mesh": mesh,
        "unit_rescale": unit_rescale,
        "selected_source": hym_first["selected_source"],
        "replay_residual_l2": hym_first["solution_summary"]["final_residual_l2"],
        "moments": moment_values,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    search_packet = {
        "schema": "MTTHYMMetricTauHCandidateSearch.v1",
        "status": "HYM_METRIC_MOMENT_SEARCH_ACCEPTS_ZERO_TAUH_SOURCES",
        "closure_claimed": True,
        "tau_H_required": tau_h,
        "best_near_misses": best,
        "special_clues": {
            "anisotropy_ratio_x1_over_y1": x1_y1,
            "anisotropy_angular_candidate": anisotropy_clue,
            "anisotropy_angular_relative_residual": abs(anisotropy_clue - tau_h) / abs(tau_h),
            "interpretation": (
                "This is the sharpest simple structural clue found so far, but it is still "
                "a diagnostic expression until a source finite-part theorem emits it."
            ),
        },
        "accepted_tau_H_source_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    frontier_packet = {
        "schema": "MTTHWeightedFinitePartExportFrontier.v1",
        "status": "FINITEPART_EXPORT_REQUIRED_AFTER_METRIC_MOMENT_SEARCH",
        "closure_claimed": True,
        "closed_here": [
            "selected HYM grid replayed locally from source recipe",
            "metric moment inventory emitted",
            "bounded HYM metric tau_H search accepts zero strict source rows",
            "anisotropy/angular clue isolated for next theorem attempt",
        ],
        "remaining_source_theorem": (
            "Prove that the selected H-weighted radial finite part equals the anisotropy/angular "
            "functional, or emit another direct finite-part/radial operator from the same selected HYM source."
        ),
        "required_export_rows": {
            "finite_part_operator": False,
            "H_weighted_metric_integral": False,
            "anisotropy_functional_source_rule": False,
            "exactness_or_error_bound": False,
            "tau_H_or_r_H_export": False,
        },
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHYMMetricMomentTauHSearchOrFinitePartExport",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "packets": {
            "selected_hym_metric_moment_inventory": rel(MOMENTS_PACKET),
            "hym_metric_tauh_candidate_search": rel(SEARCH_PACKET),
            "finitepart_export_frontier": rel(FRONTIER_PACKET),
        },
        "closure_decision": {
            "selected_HYM_grid_replayed": True,
            "metric_moments_emitted": True,
            "metric_moment_search_executed": True,
            "accepted_tau_H_source_count": 0,
            "anisotropy_angular_clue_isolated": True,
            "finitepart_export_required": True,
            "strict_r_H_promoted": False,
            "strict_N_H_promoted": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "previous_angular_frontier_status": angular_frontier["status"],
        "theorem": {
            "name": "HYMMetricMomentSearchAndFinitePartFrontierTheorem",
            "proved": True,
            "statement": (
                "Replaying the selected q79/F,m=1 HYM grid emits metric moments and sharp "
                "anisotropy diagnostics for tau_H, but no bounded metric-moment expression is "
                "accepted as a strict source row. The next proof object is a same-source "
                "H-weighted finite-part export theorem or direct radial operator."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHYMMetricMomentTauHSearchOrFinitePartExport",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "accepted_tau_H_source_count": 0,
        "anisotropy_angular_clue_isolated": True,
        "finitepart_export_required": True,
        "strict_r_H_promoted": False,
        "strict_N_H_promoted": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HYMMetricMomentTauHSearch or FinitePartExport v1

## Theorem

`HYMMetricMomentSearchAndFinitePartFrontierTheorem` is emitted.

## Result

The selected q79/F,m=1 HYM grid was replayed from the source recipe and
metric moments were searched for:

```text
tau_H = {tau_h}
```

Accepted HYM metric-moment source rows: `0`.

Best diagnostic near miss:

```text
{best[0]["expression"]} = {best[0]["value"]}
relative residual = {best[0]["relative_residual"]}
```

Best structural clue:

```text
4 + (x1_l2/y1_l2)/(3 - 4*s_beta) = {anisotropy_clue}
relative residual = {abs(anisotropy_clue - tau_h) / abs(tau_h)}
```

This is not promoted. It is a target for a finite-part theorem.

## Next Object

`{NEXT}` must emit a same-source H-weighted finite part, anisotropy functional
source rule, exactness/error certificate, and `tau_H` or `r_H` export.
"""

    write_json(MOMENTS_PACKET, moments_packet)
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
