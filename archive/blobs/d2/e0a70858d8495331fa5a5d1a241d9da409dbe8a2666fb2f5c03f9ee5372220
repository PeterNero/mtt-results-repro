"""Build the U1/SU2 source-response or normalization-index run.

This is an inverse/discovery computation.  It iterates rational U1/SU2
normalization-index weights against the existing electroweak diagnostic
witness, but promotion is allowed only for independently source-selected
indices.  Numerical closeness alone is recorded as a clue and rejected as
proof data.
"""

from __future__ import annotations

import json
import math
import subprocess
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
PROOF = ROOT / "proof_corpus"

PREVIOUS = DATA / "u1_su2_internal_overlap_payload_template_or_k_gauge_source_fill.candidate.json"
NONSM = TEXPAPERS / "mtt-nonsm-constants-no-knob"
OLD_WEIGHT_CERT = NONSM / "certificates" / "u1_su2_operator_weight_candidate_gate_certificate.json"
OLD_WEIGHT_SCRIPT = NONSM / "scripts" / "compute_u1_su2_operator_weight_candidates.py"
HYPERCHARGE_CERT = NONSM / "certificates" / "selected_hypercharge_normalized_threshold_interface_certificate.json"
BLOCK_CERT = NONSM / "certificates" / "selected_qaqcsu2_gauge_threshold_operator_blocks_certificate.json"
C1_CERT = NONSM / "certificates" / "selected_electroweak_c1_response_interface_certificate.json"

OUTPUT_DATA = DATA / "u1_su2_source_response_or_normalization_index_run.candidate.json"
OUTPUT_CERT = CERTS / "u1_su2_source_response_or_normalization_index_run_certificate.json"
OUTPUT_NOTE = PROOF / "Selected_U1_SU2_Source_Response_or_Normalization_Index_Run_v1.md"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_old_weight_script() -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, str(OLD_WEIGHT_SCRIPT)],
        cwd=NONSM,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return json.loads(proc.stdout)


def as_label(frac: Fraction) -> str:
    return f"{frac.numerator}/{frac.denominator}"


def weight_row(
    *,
    name: str,
    u1_weight: Fraction,
    su2_weight: Fraction,
    u1_piece: float,
    su2_piece: float,
    target_lambda: float,
    source_prior: str,
    rationale: str,
) -> dict[str, Any]:
    lambda_12 = float(u1_weight) * u1_piece - float(su2_weight) * su2_piece
    residual = lambda_12 - target_lambda
    promotable = source_prior == "SOURCE_SELECTED"
    return {
        "name": name,
        "weights": {"U1": as_label(u1_weight), "SU2": as_label(su2_weight)},
        "lambda_12": lambda_12,
        "residual_lambda_12": residual,
        "absolute_residual_lambda_12": abs(residual),
        "source_prior": source_prior,
        "rationale": rationale,
        "promotable": promotable,
        "status": "PROMOTABLE" if promotable else "DIAGNOSTIC_NOT_PROOF",
    }


def rational_scan(
    *,
    u1_piece: float,
    su2_piece: float,
    target_lambda: float,
    max_denominator: int,
    top_k: int,
) -> list[dict[str, Any]]:
    rationals = sorted(
        {
            Fraction(n, d)
            for d in range(1, max_denominator + 1)
            for n in range(0, 2 * max_denominator + 1)
            if Fraction(n, d) <= 2
        }
    )
    rows: list[tuple[float, Fraction, Fraction, float]] = []
    for u1_weight in rationals:
        for su2_weight in rationals:
            lambda_12 = float(u1_weight) * u1_piece - float(su2_weight) * su2_piece
            rows.append((abs(lambda_12 - target_lambda), u1_weight, su2_weight, lambda_12))
    rows.sort(key=lambda row: row[0])
    return [
        {
            "rank": rank,
            "weights": {"U1": as_label(u1_weight), "SU2": as_label(su2_weight)},
            "lambda_12": lambda_12,
            "absolute_residual_lambda_12": residual,
            "source_prior": "NONE_FOUND_IN_CURRENT_SOURCE",
            "promotable": False,
            "status": "TARGET_NEAR_HIT_REJECTED_UNLESS_SOURCE_SELECTED",
        }
        for rank, (residual, u1_weight, su2_weight, lambda_12) in enumerate(rows[:top_k], start=1)
    ]


def build() -> tuple[dict[str, Any], dict[str, Any], str]:
    previous = load(PREVIOUS)
    old_cert = load(OLD_WEIGHT_CERT)
    old_run = run_old_weight_script()
    hypercharge = load(HYPERCHARGE_CERT)
    block = load(BLOCK_CERT)
    c1 = load(C1_CERT)

    u1_piece = float(old_run["input_finite_parts"]["U1_circle"])
    su2_piece = float(old_run["input_finite_parts"]["SU2_effective_sphere"])
    target_lambda = float(old_run["target_witness"]["lambda_12"])

    source_prior_candidates = [
        weight_row(
            name="GUT_hypercharge_3_5",
            u1_weight=Fraction(3, 5),
            su2_weight=Fraction(1, 1),
            u1_piece=u1_piece,
            su2_piece=su2_piece,
            target_lambda=target_lambda,
            source_prior="SOURCE_MOTIVATED_NOT_SELECTED",
            rationale="standard hypercharge normalization candidate; current MTT source does not select it as the threshold weight",
        ),
        weight_row(
            name="complex_nesting_or_shared_circle_2_3",
            u1_weight=Fraction(2, 3),
            su2_weight=Fraction(1, 1),
            u1_piece=u1_piece,
            su2_piece=su2_piece,
            target_lambda=target_lambda,
            source_prior="MOTIVATED_BY_PRIOR_DISCUSSION_NOT_SOURCE_SELECTED",
            rationale="near hit with plausible complex-nesting/shared-circle story; no source theorem currently selects it",
        ),
    ]
    diagnostic_imported_hits = [
        weight_row(
            name="best_small_rational_old_scan_5_9_7_5",
            u1_weight=Fraction(5, 9),
            su2_weight=Fraction(7, 5),
            u1_piece=u1_piece,
            su2_piece=su2_piece,
            target_lambda=target_lambda,
            source_prior="TARGET_DISCOVERED_ONLY",
            rationale="best old bounded-scan hit; rejected because it is discovered from the diagnostic target",
        ),
    ]
    bounded_scan = rational_scan(
        u1_piece=u1_piece,
        su2_piece=su2_piece,
        target_lambda=target_lambda,
        max_denominator=24,
        top_k=12,
    )

    promotable_rows = [row for row in source_prior_candidates + diagnostic_imported_hits + bounded_scan if row["promotable"]]
    best_source_motivated = min(source_prior_candidates, key=lambda row: row["absolute_residual_lambda_12"])
    best_imported_diagnostic = min(diagnostic_imported_hits, key=lambda row: row["absolute_residual_lambda_12"])
    best_scan = bounded_scan[0]

    closure_attempt = {
        "normalization_index_domain": "rational U1/SU2 weights in [0,2] with denominator <= 24, plus source-prior candidates",
        "diagnostic_target_role": old_run["target_witness"]["role"],
        "target_witness_lambda_12": target_lambda,
        "input_scalar_proxy_pieces": old_run["input_finite_parts"],
        "source_prior_candidates": source_prior_candidates,
        "diagnostic_imported_hits": diagnostic_imported_hits,
        "bounded_rational_scan_top_hits": bounded_scan,
        "best_source_motivated_candidate": best_source_motivated,
        "best_imported_diagnostic_hit": best_imported_diagnostic,
        "best_target_near_hit": best_scan,
        "promotable_rows": promotable_rows,
        "source_obstructions": {
            "hypercharge_interface_status": hypercharge["status"],
            "hypercharge_determinant_amplitudes_selected": hypercharge["verdict"]["determinant_amplitudes_selected"],
            "operator_block_status": block["status"],
            "selected_operator_values_closed": block["verdict"]["selected_operator_values_closed"],
            "selected_spectra_closed": block["verdict"]["selected_spectra_closed"],
            "c1_interface_status": c1["status"],
            "numeric_electroweak_closure": c1["verdict"]["numeric_electroweak_closure"],
        },
    }

    decision = {
        "normalization_index_run_executed": True,
        "best_source_motivated_index": best_source_motivated["name"],
        "best_source_motivated_residual": best_source_motivated["absolute_residual_lambda_12"],
        "best_imported_diagnostic_weights": best_imported_diagnostic["weights"],
        "best_imported_diagnostic_residual": best_imported_diagnostic["absolute_residual_lambda_12"],
        "best_target_near_hit_weights": best_scan["weights"],
        "best_target_near_hit_residual": best_scan["absolute_residual_lambda_12"],
        "promotable_index_found": bool(promotable_rows),
        "I_1_filled": False,
        "I_2_filled": False,
        "K_gauge_filled": False,
        "measured_electroweak_closure": False,
        "can_close_now": False,
        "reason_not_closed": "All close rational indices are target-discovered or source-motivated only; no current source selects the U1/SU2 threshold weights, spectra, or K_gauge.",
        "next_required_object": "Selected_U1_SU2_Threshold_Index_Source_Selector_or_Operator_Spectrum_v1",
    }

    candidate = {
        "candidate": "SelectedU1SU2SourceResponseOrNormalizationIndexRun",
        "status": "U1_SU2_NORMALIZATION_INDEX_ITERATED_NO_PROMOTABLE_SOURCE_INDEX",
        "inputs": {
            "previous_gate": str(PREVIOUS.relative_to(ROOT)),
            "old_weight_gate": str(OLD_WEIGHT_CERT),
            "old_weight_gate_status": old_cert["status"],
            "hypercharge_threshold_interface": str(HYPERCHARGE_CERT),
            "operator_block_scaffold": str(BLOCK_CERT),
            "target_fitting_used": True,
            "target_fitting_role": "DISCOVERY_ONLY_DIAGNOSTIC_SCAN",
        },
        "closure_attempt": closure_attempt,
        "decision": decision,
        "guardrails": [
            "Do not promote the best rational scan hit without source selection.",
            "Do not promote 2/3 from numerical closeness or informal complex-nesting intuition.",
            "Do not promote 3/5 unless the MTT branch selects GUT-style hypercharge normalization as the threshold weight.",
            "Do not compare to measured electroweak closure until selected spectra, weights, mu_match, and RGE scheme are supplied.",
        ],
        "closure_claimed": True,
        "closure_scope": "normalization_index_iteration_and_no_promotable_current_source_index",
        "target_fitting_used": True,
        "target_fitting_role": "DISCOVERY_ONLY_DIAGNOSTIC_SCAN",
    }

    certificate = {
        "certificate": "SelectedU1SU2SourceResponseOrNormalizationIndexRun",
        "status": candidate["status"],
        "candidate_path": str(OUTPUT_DATA.relative_to(ROOT)),
        "what_closes": {
            "normalization_index_iteration": True,
            "source_prior_candidates_tested": True,
            "bounded_rational_scan_executed": True,
            "current_source_no_promotable_index_no_go": True,
        },
        "what_remains_open": {
            "selected_hypercharge_threshold_weight": True,
            "selected_SU2_threshold_weight": True,
            "selected_operator_spectra": True,
            "K_gauge_anchor": True,
            "forward_replay_without_gauge_targets": True,
            "measured_electroweak_closure": True,
        },
        "next_required_object": decision["next_required_object"],
        "closure_scope": candidate["closure_scope"],
        "target_fitting_used": True,
        "target_fitting_role": "DISCOVERY_ONLY_DIAGNOSTIC_SCAN",
    }
    return candidate, certificate, render_note(candidate)


def render_note(candidate: dict[str, Any]) -> str:
    attempt = candidate["closure_attempt"]
    decision = candidate["decision"]
    source_rows = "\n".join(
        f"- `{row['name']}`: U1={row['weights']['U1']}, SU2={row['weights']['SU2']}, "
        f"lambda_12={row['lambda_12']:.15g}, residual={row['absolute_residual_lambda_12']:.6g}, "
        f"source_prior={row['source_prior']}"
        for row in attempt["source_prior_candidates"]
    )
    scan_rows = "\n".join(
        f"- #{row['rank']}: U1={row['weights']['U1']}, SU2={row['weights']['SU2']}, "
        f"lambda_12={row['lambda_12']:.15g}, residual={row['absolute_residual_lambda_12']:.6g}"
        for row in attempt["bounded_rational_scan_top_hits"][:8]
    )
    obstructions = "\n".join(f"- `{key}` = {value}" for key, value in attempt["source_obstructions"].items())
    guardrails = "\n".join(f"- {item}" for item in candidate["guardrails"])
    return f"""# Selected U1/SU2 Source Response or Normalization Index Run v1

## Result

The normalization-index run has now been executed as a discovery-only scan.
It does not close electroweak coupling prediction.

The strongest source-motivated near hit remains:

```text
{decision["best_source_motivated_index"]}
residual = {decision["best_source_motivated_residual"]}
```

The strongest bounded rational target-near hit is:

```text
U1 = {decision["best_target_near_hit_weights"]["U1"]}
SU2 = {decision["best_target_near_hit_weights"]["SU2"]}
residual = {decision["best_target_near_hit_residual"]}
```

That hit is rejected as proof data because it is target-discovered and has no
current source selector.

## Input Pieces

```text
U1 circle finite part = {attempt["input_scalar_proxy_pieces"]["U1_circle"]}
SU2 effective sphere finite part = {attempt["input_scalar_proxy_pieces"]["SU2_effective_sphere"]}
diagnostic target lambda_12 = {attempt["target_witness_lambda_12"] if "target_witness_lambda_12" in attempt else "see candidate JSON"}
target role = {attempt["diagnostic_target_role"]}
```

## Source-Prior Candidates

{source_rows}

## Bounded Rational Scan

{scan_rows}

## Source Obstructions

{obstructions}

## Decision

```text
normalization_index_run_executed = true
promotable_index_found = {str(decision["promotable_index_found"]).lower()}
I_1_filled = false
I_2_filled = false
K_gauge_filled = false
measured_electroweak_closure = false
can_close_now = false
```

Reason:

```text
{decision["reason_not_closed"]}
```

## Guardrails

{guardrails}

## Next Required Object

```text
{decision["next_required_object"]}
```
"""


def main() -> None:
    candidate, certificate, note = build()
    data_text = json.dumps(candidate, indent=2, sort_keys=True)
    cert_text = json.dumps(certificate, indent=2, sort_keys=True)
    if "--write" in sys.argv:
        OUTPUT_DATA.write_text(data_text + "\n", encoding="utf-8")
        OUTPUT_CERT.write_text(cert_text + "\n", encoding="utf-8")
        OUTPUT_NOTE.write_text(note, encoding="utf-8")
    print(cert_text)


if __name__ == "__main__":
    main()
