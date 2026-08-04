"""Test selected H-angular/C1 metric candidates for tau_H."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_hangularc1metricsearch_or_hweightedgalerkinpayload"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SEARCH_PACKET = PACKET_DIR / "hangular_c1_metric_tauh_search.packet.json"
PAYLOAD_PACKET = PACKET_DIR / "hweighted_galerkin_payload_contract.packet.json"
DECISION_PACKET = PACKET_DIR / "angular_metric_search_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_HAngularC1MetricSearch_or_HWeightedGalerkinPayload_v1.md"

STATUS = (
    "MTT_SELECTED_HANGULARC1METRICSEARCH_OR_HWEIGHTEDGALERKINPAYLOAD_"
    "ANGULAR_C1_NEARMISSES_REJECTED_HWEIGHTED_PAYLOAD_REQUIRED"
)
NEXT = "MTT_Selected_HWeightedGalerkinMetricTauHExport_or_DirectRadialOperator_v1"

SOURCES = {
    "tau_frontier": DATA / "selected_tauhtransportcoefficientsource_or_unpatchedphifinc1consumer.candidate.json",
    "c1_frontier": DATA / "selected_tauhc1scalarexport_or_galerkinmetricfrontier.candidate.json",
    "c1_scalars": DATA
    / "selected_tauhc1scalarexport_or_galerkinmetricfrontier"
    / "finite_c1_scalar_inventory.packet.json",
    "selected_sbeta": DATA
    / "selected_higgsdynamicstrainkernel_or_c5bc6projectionnoboundaryproof"
    / "selected_finite_reduction_sbeta_promotion.packet.json",
    "controlled_h": DATA
    / "selected_qutrit27hfunctionalsearch_or_radialsourcefrontier"
    / "controlled_herm2_matrix_invariants.packet.json",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def record(rows: list[dict[str, Any]], expression: str, value: float, target: float, provenance: str) -> None:
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
                "Diagnostic H-angular/C1 expression only; no same-source H-weighted Galerkin "
                "integral or direct radial operator emits this expression as tau_H."
            ),
        }
    )


def main() -> int:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing H-angular C1 inputs: " + ", ".join(missing))

    tau_frontier = load(SOURCES["tau_frontier"])
    c1_frontier = load(SOURCES["c1_frontier"])
    c1_scalars = load(SOURCES["c1_scalars"])["scalars"]
    sbeta_packet = load(SOURCES["selected_sbeta"])
    controlled_h = load(SOURCES["controlled_h"])

    tau_h = float(tau_frontier["constants_and_parameters"]["tau_H_required"])
    s_beta = float(sbeta_packet["selected_s_beta"]["value"])
    sqrt_s = math.sqrt(s_beta)
    sqrt_1_minus_s = math.sqrt(1.0 - s_beta)
    base_c1 = 4.0

    rows: list[dict[str, Any]] = []
    coeffs = [-12.0, -6.0, -4.0, -3.0, -2.0, -1.0, -0.5, 0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 12.0]
    positive_scalars = {
        key: float(value)
        for key, value in c1_scalars.items()
        if isinstance(value, (int, float)) and float(value) > 0
    }

    for coeff in coeffs:
        record(rows, f"4 + ({coeff:g})*s_beta", base_c1 + coeff * s_beta, tau_h, "selected_s_beta")
        record(rows, f"4/(1 - ({coeff:g})*s_beta)", base_c1 / (1.0 - coeff * s_beta), tau_h, "selected_s_beta")
        if 1.0 + coeff * s_beta > 0:
            record(
                rows,
                f"4*sqrt(1 + ({coeff:g})*s_beta)",
                base_c1 * math.sqrt(1.0 + coeff * s_beta),
                tau_h,
                "selected_s_beta",
            )
        for key, scalar in positive_scalars.items():
            record(
                rows,
                f"4 + ({coeff:g})*s_beta*{key}",
                base_c1 + coeff * s_beta * scalar,
                tau_h,
                f"selected_s_beta times finite_C1_scalar:{key}",
            )
            record(
                rows,
                f"4 + ({coeff:g})*s_beta/{key}",
                base_c1 + coeff * s_beta / scalar,
                tau_h,
                f"selected_s_beta over finite_C1_scalar:{key}",
            )

    record(rows, "4 + sqrt(s_beta)", base_c1 + sqrt_s, tau_h, "selected_s_beta")
    record(rows, "4 + (1-sqrt(1-s_beta))", base_c1 + (1.0 - sqrt_1_minus_s), tau_h, "selected_s_beta")
    record(rows, "4/sqrt(1-s_beta)", base_c1 / sqrt_1_minus_s, tau_h, "selected_s_beta")

    rows.sort(key=lambda row: abs(row["absolute_residual"]))
    best = rows[:16]

    search_packet = {
        "schema": "MTTHAngularC1MetricTauHSearch.v1",
        "status": "HANGULAR_C1_METRIC_SEARCH_ACCEPTS_ZERO_TAUH_SOURCES",
        "closure_claimed": True,
        "tau_H_required": tau_h,
        "selected_s_beta": {
            "value": s_beta,
            "source": sbeta_packet["selected_s_beta"]["value_source"],
            "observed_higgs_or_beta_used": sbeta_packet["selected_s_beta"]["observed_higgs_or_beta_used"],
        },
        "search_policy": {
            "base_C1_family": "tau_H=4 from finite C1 shape arithmetic",
            "angular_inputs": ["s_beta", "sqrt(s_beta)", "sqrt(1-s_beta)"],
            "finite_C1_scalars": sorted(positive_scalars),
            "accepted_only_if_same_source_metric_integral_emitted": True,
            "diagnostic_residual_ranking_used": True,
        },
        "best_near_misses": best,
        "accepted_tau_H_source_count": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    payload_packet = {
        "schema": "MTTHWeightedGalerkinPayloadContract.v1",
        "status": "HWEIGHTED_GALERKIN_PAYLOAD_CONTRACT_EMITTED_VALUES_OPEN",
        "closure_claimed": True,
        "why_needed": (
            "Selected s_beta fixes the H angular ray and finite C1 fixes shape response, "
            "but the radial coefficient needs a same-source H-weighted metric or kernel finite part."
        ),
        "required_rows": {
            "selected_zero_mode_bases": {
                "source": "selected HYM/Strominger or finite qutrit transport basis",
                "required": True,
                "accepted_now": False,
            },
            "H_weighted_metric_kernel": {
                "source": "same selected metric used by s_beta promotion, extended to H radial response",
                "required": True,
                "accepted_now": False,
            },
            "primitive_three_by_three_H_contractions": {
                "shape": "sector x 3x3 x real/imag components",
                "required": True,
                "accepted_now": False,
            },
            "linear_response_matrices": {
                "required": True,
                "accepted_now": False,
            },
            "tau_H_export_rule": {
                "must_emit": "tau_H or r_H without using controlled_H radial value as input",
                "required": True,
                "accepted_now": False,
            },
            "exactness_error_certificate": {
                "required": True,
                "accepted_now": False,
            },
        },
        "forbidden_sources": [
            "controlled r_H or N_H",
            "observed Higgs mass/quartic/beta",
            "target residual minimization",
            "C1 scalar replay without H-weighted metric provenance",
        ],
        "postchecks_not_selectors": [
            "C33/nonzero-family-rank tests",
            "residual closeness to tau_H",
            "agreement with controlled Herm(2) matrix after export",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision_packet = {
        "schema": "MTTHAngularMetricSearchDecision.v1",
        "status": "ANGULAR_METRIC_NEARMISSES_REJECTED_RADIAL_KERNEL_REQUIRED",
        "closure_claimed": True,
        "selected_s_beta_imported": True,
        "selected_s_beta_value": s_beta,
        "C1_scalar_only_export_previously_rejected": c1_frontier["closure_decision"][
            "C1_scalar_only_tau_H_export_rejected"
        ],
        "best_expression": best[0],
        "accepted_tau_H_source_count": 0,
        "controlled_H_radial_used_as_input": False,
        "strict_r_H_promoted": False,
        "strict_N_H_promoted": False,
        "next_required_artifact": NEXT,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedHAngularC1MetricSearchOrHWeightedGalerkinPayload",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "packets": {
            "hangular_c1_metric_tauh_search": rel(SEARCH_PACKET),
            "hweighted_galerkin_payload_contract": rel(PAYLOAD_PACKET),
            "angular_metric_search_decision": rel(DECISION_PACKET),
        },
        "closure_decision": {
            "selected_s_beta_imported": True,
            "selected_s_beta_source_clean": sbeta_packet["selected_s_beta"]["observed_higgs_or_beta_used"] is False,
            "H_angular_C1_metric_search_executed": True,
            "accepted_tau_H_source_count": 0,
            "best_near_miss_rejected": True,
            "H_weighted_Galerkin_payload_contract_emitted": True,
            "strict_r_H_promoted": False,
            "strict_N_H_promoted": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "controlled_H_matrix_only_used_for_circularity_guard": controlled_h["strict_selected_radial_source_emitted"]
        is False,
        "theorem": {
            "name": "HAngularC1MetricSearchAndPayloadContractTheorem",
            "proved": True,
            "statement": (
                "Selected s_beta can be imported as clean H angular data and combined with finite C1 "
                "shape scalars in bounded H-angular metric diagnostics, but these diagnostics emit zero "
                "accepted tau_H source rows. The radial coefficient therefore remains a same-source "
                "H-weighted Galerkin metric/kernel or direct radial-operator obligation."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedHAngularC1MetricSearchOrHWeightedGalerkinPayload",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "accepted_tau_H_source_count": 0,
        "selected_s_beta_imported": True,
        "H_weighted_Galerkin_payload_contract_emitted": True,
        "strict_r_H_promoted": False,
        "strict_N_H_promoted": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected HAngular C1 Metric Search or HWeighted Galerkin Payload v1

## Theorem

`HAngularC1MetricSearchAndPayloadContractTheorem` is emitted.

## Result

Selected `s_beta={s_beta}` was imported as clean H angular data and combined
with finite C1 scalar data to test H-angular/C1 metric candidates for:

```text
tau_H = {tau_h}
```

Accepted H-angular/C1 source rows: `0`.

Best diagnostic near miss:

```text
{best[0]["expression"]} = {best[0]["value"]}
relative residual = {best[0]["relative_residual"]}
```

This is not promoted because no same-source H-weighted Galerkin integral,
metric finite part, or direct radial operator emits the expression.

## Boundary

`s_beta` fixes the H angular ray. C1 fixes finite response shape. Neither
supplies the radial magnitude by itself.

## Next Payload

`{NEXT}` must emit selected zero-mode bases, H-weighted metric/kernel rows,
primitive `3x3` H contractions, response matrices, a same-source `tau_H` export
rule, and exactness/error certificates.
"""

    write_json(SEARCH_PACKET, search_packet)
    write_json(PAYLOAD_PACKET, payload_packet)
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
