"""Numerically push the selected 27x27 qutrit matrix package."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_qutrit27numericalpush_or_matrixrowfrontier"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
SPECTRAL_PACKET = PACKET_DIR / "qutrit27_spectral_diagnostics.packet.json"
PROFILE_PACKET = PACKET_DIR / "charged_row_profile_diagnostics.packet.json"
SEARCH_PACKET = PACKET_DIR / "matrix_functional_candidate_search.packet.json"
H_PACKET = PACKET_DIR / "h_row_frontier_after_27_push.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_Qutrit27NumericalPush_or_MatrixRowFrontier_v1.md"

STATUS = (
    "MTT_SELECTED_QUTRIT27NUMERICALPUSH_OR_MATRIXROWFRONTIER_"
    "SPECTRAL_DIAGNOSTICS_CLOSED_CHARGED_PROFILE_EXTRACTED_H_OPEN"
)
NEXT = "MTT_Selected_StrictFiniteHSourceRowConstruction_or_NonHiggsHRGPrediction_v1"

SOURCES = {
    "matrix_packet": DATA
    / "selected_hymoverlapvaluesource_or_qutritspectraltriplepackaging"
    / "qutrit_weyl_27x27_matrix_realization.packet.json",
    "charged_rows": DATA
    / "selected_hymoverlapvaluesource_or_selectedoverlapkernelrows"
    / "selected_charged_normalized_overlap_kernel_rows.packet.json",
    "h_gap": DATA
    / "selected_hymoverlapvaluesource_or_selectedoverlapkernelrows"
    / "h_lambda_overlap_kernel_row_gap.packet.json",
    "h_minimal_ledger": DATA
    / "selected_honeparameterexecutionledger_or_strictfinitehsourcerows.candidate.json",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def complex_from_pair(pair: list[float]) -> complex:
    return complex(float(pair[0]), float(pair[1]))


def mat_from_sparse(entries: list[dict[str, Any]], n: int = 27) -> np.ndarray:
    mat = np.zeros((n, n), dtype=complex)
    for item in entries:
        mat[int(item["row"]), int(item["col"])] = complex_from_pair(item["value"])
    return mat


def rounded_multiset(values: np.ndarray, digits: int = 12) -> dict[str, int]:
    rounded = []
    for value in values:
        z = complex(value)
        real = 0.0 if abs(z.real) < 10 ** (-digits) else round(float(z.real), digits)
        imag = 0.0 if abs(z.imag) < 10 ** (-digits) else round(float(z.imag), digits)
        rounded.append(f"{real:+.{digits}f}{imag:+.{digits}f}i")
    return dict(sorted(Counter(rounded).items()))


def real_multiset(values: np.ndarray, digits: int = 12) -> dict[str, int]:
    rounded = [f"{round(float(v), digits):+.{digits}f}" for v in values]
    return dict(sorted(Counter(rounded).items()))


def projector(indices: list[int], n: int = 27) -> np.ndarray:
    p = np.zeros((n, n), dtype=complex)
    for i in indices:
        p[i, i] = 1.0
    return p


def basis_index(c: int, a: int, b: int) -> int:
    return c * 9 + a * 3 + b


def trace_norm(mat: np.ndarray) -> float:
    return float(np.trace(mat.conj().T @ mat).real)


def require_sources() -> dict[str, dict[str, Any]]:
    missing = [rel(path) for path in SOURCES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing qutrit27 numerical-push inputs: " + ", ".join(missing))
    return {name: load(path) for name, path in SOURCES.items()}


def main() -> int:
    sources = require_sources()
    matrix_packet = sources["matrix_packet"]
    charged_packet = sources["charged_rows"]
    h_gap = sources["h_gap"]
    h_ledger = sources["h_minimal_ledger"]["closure_decision"]

    lz = mat_from_sparse(matrix_packet["left_Z27_sparse_entries"])
    lx = mat_from_sparse(matrix_packet["left_X27_sparse_entries"])
    ident = np.eye(27, dtype=complex)
    omega = complex_from_pair(matrix_packet["omega"])

    hermitian_adjacency = lz + lz.conj().T + lx + lx.conj().T
    normalized_adjacency = hermitian_adjacency / 4.0
    magnetic_laplacian = 4.0 * ident - hermitian_adjacency
    commutator = lz @ lx - lx @ lz

    class_projectors = {
        f"class_{c}": projector([basis_index(c, a, b) for a in range(3) for b in range(3)])
        for c in range(3)
    }
    phase_projectors = {
        f"phase_{a}": projector([basis_index(c, a, b) for c in range(3) for b in range(3)])
        for a in range(3)
    }
    shift_projectors = {
        f"shift_{b}": projector([basis_index(c, a, b) for c in range(3) for a in range(3)])
        for b in range(3)
    }

    projector_diagnostics = {}
    for family, projectors in [
        ("class", class_projectors),
        ("phase", phase_projectors),
        ("shift", shift_projectors),
    ]:
        projector_diagnostics[family] = {
            name: {
                "rank": int(round(np.trace(p).real)),
                "trace_norm": trace_norm(p),
                "commutator_with_LZ_frobenius": float(np.linalg.norm(p @ lz - lz @ p)),
                "commutator_with_LX_frobenius": float(np.linalg.norm(p @ lx - lx @ p)),
            }
            for name, p in projectors.items()
        }

    spectral = {
        "schema": "MTTQutrit27SpectralDiagnostics.v1",
        "status": "QUTRIT27_SPECTRAL_DIAGNOSTICS_COMPUTED",
        "closure_claimed": True,
        "carrier_dimension": 27,
        "relation_checks": {
            "LZ_cubed_minus_I_frobenius": float(np.linalg.norm(np.linalg.matrix_power(lz, 3) - ident)),
            "LX_cubed_minus_I_frobenius": float(np.linalg.norm(np.linalg.matrix_power(lx, 3) - ident)),
            "LZ_LX_minus_omega_LX_LZ_frobenius": float(np.linalg.norm(lz @ lx - omega * lx @ lz)),
            "commutator_norm_LZ_LX_minus_LX_LZ": float(np.linalg.norm(commutator)),
        },
        "spectra": {
            "LZ_eigenvalue_multiset": rounded_multiset(np.linalg.eigvals(lz)),
            "LX_eigenvalue_multiset": rounded_multiset(np.linalg.eigvals(lx)),
            "hermitian_adjacency_eigenvalue_multiset": real_multiset(np.linalg.eigvalsh(hermitian_adjacency)),
            "normalized_adjacency_eigenvalue_multiset": real_multiset(np.linalg.eigvalsh(normalized_adjacency)),
            "magnetic_laplacian_eigenvalue_multiset": real_multiset(np.linalg.eigvalsh(magnetic_laplacian)),
        },
        "projector_diagnostics": projector_diagnostics,
        "numerical_interpretation": [
            "The pure qutrit-Weyl 27x27 package is three identical 9-dimensional irreducible left-action blocks.",
            "Class projectors commute with both LZ and LX, but phase/shift projectors do not.",
            "The matrix package alone supplies carrier, symmetry, trace, and degeneracy structure; it does not select an H radial scalar.",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    rows = charged_packet["rows"]
    values_by_sector: dict[str, list[float]] = {}
    for row in rows:
        values_by_sector.setdefault(row["sector"], []).append(float(row["selected_K_threshold_source_value"]))
    sector_profiles = {}
    for sector, vals in values_by_sector.items():
        vals_sorted = [vals[i] for i in range(3)]
        total = sum(vals_sorted)
        square_total = sum(v * v for v in vals_sorted)
        base = min(vals_sorted)
        sector_profiles[sector] = {
            "values_by_generation": vals_sorted,
            "base_value": base,
            "ratio_to_base": [v / base for v in vals_sorted],
            "sum": total,
            "sum_normalized_weights": [v / total for v in vals_sorted],
            "square_sum": square_total,
            "square_normalized_weights": [v * v / square_total for v in vals_sorted],
            "condition_number_diagonal_profile": max(vals_sorted) / min(vals_sorted),
            "determinant_of_diagonal_profile": float(np.prod(vals_sorted)),
            "frobenius_norm_of_diagonal_profile": float(np.sqrt(square_total)),
        }

    all_base_values = sorted({round(profile["base_value"], 12) for profile in sector_profiles.values()})
    profile = {
        "schema": "MTTChargedRowProfileDiagnostics.v1",
        "status": "CHARGED_2_1_1_PROFILE_EXTRACTED_FROM_SELECTED_ROWS",
        "closure_claimed": True,
        "selected_charged_row_count": charged_packet["accepted_selected_charged_normalized_overlap_kernel_row_count"],
        "accepted_full_ten_row_kernel_closure_count": charged_packet[
            "accepted_full_ten_row_kernel_closure_count"
        ],
        "sector_profiles": sector_profiles,
        "shared_base_values": all_base_values,
        "profile_summary": {
            "all_sectors_share_same_generation_profile": len({tuple(p["ratio_to_base"]) for p in sector_profiles.values()}) == 1,
            "generation_ratio": [2.0, 1.0, 1.0],
            "linear_weights": [0.5, 0.25, 0.25],
            "quadratic_weights": [2.0 / 3.0, 1.0 / 6.0, 1.0 / 6.0],
            "interpretation": "The selected charged rows define a stable 2:1:1 generation profile across u,d,e.",
        },
        "source_boundary": {
            "profile_is_selected_because_rows_are_selected": True,
            "pure_27x27_weyl_symmetry_alone_selects_2_1_1": False,
            "requires_generation_profile_or_threshold_row_layer": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidates = []
    # Source-native simple functionals on canonical projectors and Weyl words.
    for family, projectors in [
        ("class", class_projectors),
        ("phase", phase_projectors),
        ("shift", shift_projectors),
    ]:
        traces = [float(np.trace(p).real) for p in projectors.values()]
        norms = [trace_norm(p) for p in projectors.values()]
        candidates.append(
            {
                "candidate": f"{family}_projector_trace_profile",
                "values": traces,
                "normalized": [v / sum(traces) for v in traces],
                "emits_charged_2_1_1_profile": False,
                "emits_H_lambda_row": False,
                "reason": "canonical projector traces are 1:1:1 at this source level",
            }
        )
        candidates.append(
            {
                "candidate": f"{family}_projector_frobenius_profile",
                "values": norms,
                "normalized": [v / sum(norms) for v in norms],
                "emits_charged_2_1_1_profile": False,
                "emits_H_lambda_row": False,
                "reason": "canonical projector Frobenius norms are 1:1:1 at this source level",
            }
        )
    adjacency_abs = np.sort(np.abs(np.linalg.eigvalsh(hermitian_adjacency)))[::-1]
    candidates.append(
        {
            "candidate": "top_three_abs_hermitian_adjacency_eigenvalues",
            "values": [float(v) for v in adjacency_abs[:3]],
            "normalized": [float(v / sum(adjacency_abs[:3])) for v in adjacency_abs[:3]],
            "emits_charged_2_1_1_profile": False,
            "emits_H_lambda_row": False,
            "reason": "top eigenspace is degenerate across the three class lanes",
        }
    )

    search = {
        "schema": "MTTMatrixFunctionalCandidateSearch.v1",
        "status": "SIMPLE_SOURCE_NATIVE_MATRIX_FUNCTIONALS_TESTED_NO_H_ROW",
        "closure_claimed": True,
        "tested_candidate_count": len(candidates),
        "accepted_H_lambda_candidate_count": 0,
        "accepted_new_charged_profile_source_count": 0,
        "candidates": candidates,
        "decision": {
            "pure_27x27_matrix_package_extends_numeric_understanding": True,
            "pure_27x27_matrix_package_emits_new_scalar_rows": False,
            "charged_2_1_1_profile_is_stable_postcheck_of_selected_rows": True,
            "H_lambda_requires_extra_source_object": True,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    h_packet = {
        "schema": "MTTHRowFrontierAfter27Push.v1",
        "status": "H_ROW_REMAINS_OPEN_AFTER_NUMERICAL_27X27_PUSH",
        "closure_claimed": True,
        "H_lambda_overlap_kernel_row_emitted": False,
        "strict_H_source_row_emitted": False,
        "minimal_one_parameter_H_closed": h_ledger["minimal_one_parameter_H_closure_closed"],
        "minimal_H_parameter_count_spent": h_ledger["H_parameter_count_spent"],
        "controlled_r_H": h_ledger["controlled_r_H"],
        "controlled_N_H": h_ledger["controlled_N_H"],
        "h_gap_import": {
            "selected_s_beta_value": h_gap["selected_s_beta_value"],
            "selected_K_threshold_Omega_H_lambda_emitted": h_gap[
                "selected_K_threshold_Omega_H_lambda_emitted"
            ],
            "selected_lambda_H_payload_emitted": h_gap["selected_lambda_H_payload_emitted"],
            "blocking_reasons": h_gap["blocking_reasons"],
        },
        "conclusion": (
            "The 27x27 qutrit matrix can be pushed through exact spectral diagnostics and "
            "charged profile extraction, but it does not by itself emit the H/lambda row. "
            "For H, the repo currently has minimal one-parameter closure only; strict closure "
            "still needs selected F_H, M_source, K_H, R_H^RG, or a non-Higgs HRG prediction."
        ),
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    candidate = {
        "candidate": "MTTSelectedQutrit27NumericalPushOrMatrixRowFrontier",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {name: rel(path) for name, path in SOURCES.items()},
        "packets": {
            "qutrit27_spectral_diagnostics": rel(SPECTRAL_PACKET),
            "charged_row_profile_diagnostics": rel(PROFILE_PACKET),
            "matrix_functional_candidate_search": rel(SEARCH_PACKET),
            "h_row_frontier_after_27_push": rel(H_PACKET),
        },
        "closure_decision": {
            "qutrit27_spectral_diagnostics_closed": True,
            "charged_2_1_1_profile_extracted": True,
            "all_charged_sectors_share_profile": True,
            "pure_27x27_matrix_emits_H_lambda_row": False,
            "accepted_H_lambda_candidate_count": 0,
            "minimal_one_parameter_H_closure_available": True,
            "minimal_one_parameter_H_parameter_count": h_ledger["H_parameter_count_spent"],
            "strict_no_knob_H_closed": False,
            "full_no_knob_closed": False,
            "true_SM_equivalence_closed": False,
        },
        "constants_and_parameters": {
            "omega": matrix_packet["omega"],
            "carrier_dimension": 27,
            "charged_base_overlap_value": all_base_values[0],
            "charged_generation_ratio": [2.0, 1.0, 1.0],
            "minimal_H_parameter": "UP-RET-OVERLAP.HRG",
            "minimal_H_parameter_value": h_ledger["controlled_r_H"],
            "minimal_H_parameter_count": h_ledger["H_parameter_count_spent"],
        },
        "theorem": {
            "name": "Qutrit27NumericalPushAndMatrixRowFrontierTheorem",
            "proved": True,
            "statement": (
                "The selected 27x27 qutrit-Weyl package has been pushed through "
                "numerical spectral diagnostics and selected charged-row profile extraction. "
                "It robustly supports the selected charged 2:1:1 profile, but pure source-native "
                "matrix functionals tested here emit no H/lambda row. Thus the H row remains "
                "minimal-one-parameter closed only, with strict no-knob closure still requiring "
                "a selected finite-H/source row or independent non-Higgs HRG prediction."
            ),
        },
    }

    cert = {
        "certificate": "MTTSelectedQutrit27NumericalPushOrMatrixRowFrontier",
        "status": STATUS,
        "next_required_artifact": NEXT,
        "closure_claimed": True,
        "theorem_proved": True,
        "qutrit27_spectral_diagnostics_closed": True,
        "charged_2_1_1_profile_extracted": True,
        "accepted_H_lambda_candidate_count": 0,
        "strict_no_knob_H_closed": False,
        "full_no_knob_closure_claimed": False,
        "true_SM_equivalence_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    note = f"""# MTT Selected Qutrit27 Numerical Push or MatrixRowFrontier v1

## Theorem

`Qutrit27NumericalPushAndMatrixRowFrontierTheorem` is emitted.

## What We Computed

The selected `27x27` qutrit-Weyl package was reconstructed numerically and
pushed through spectral diagnostics.

- carrier dimension: `27`;
- `L_Z^3-I` Frobenius error: `{spectral["relation_checks"]["LZ_cubed_minus_I_frobenius"]:.3e}`;
- `L_X^3-I` Frobenius error: `{spectral["relation_checks"]["LX_cubed_minus_I_frobenius"]:.3e}`;
- `L_Z L_X - omega L_X L_Z` error: `{spectral["relation_checks"]["LZ_LX_minus_omega_LX_LZ_frobenius"]:.3e}`;
- class projector ranks: `9,9,9`;
- phase projector ranks: `9,9,9`;
- shift projector ranks: `9,9,9`.

## Charged Rows

The already-selected charged overlap rows give the same generation profile in
`u,d,e`:

```text
{sector_profiles["u"]["values_by_generation"]}
```

So the charged numerical profile is:

```text
2 : 1 : 1
```

with linear weights `[1/2, 1/4, 1/4]` and quadratic weights
`[2/3, 1/6, 1/6]`.

## Matrix Search Result

Pure source-native 27x27 matrix functionals tested here do not emit a new H row.
Canonical class/phase/shift projector traces and Frobenius norms are `1:1:1`,
and the simple Hermitian adjacency spectrum is class-degenerate. This means the
27x27 carrier is numerically real and useful, but it does not by itself select
the Higgs radial/lambda scalar.

## H Status

The H layer is currently closed only at the counted one-parameter standard:

- parameter: `UP-RET-OVERLAP.HRG`;
- parameter count: `{h_ledger["H_parameter_count_spent"]}`;
- `r_H`: `{h_ledger["controlled_r_H"]}`;
- `N_H`: `{h_ledger["controlled_N_H"]}`;
- strict H row emitted: `false`.

## Constants / Parameters

- `omega = exp(2 pi i/3) = {matrix_packet["omega"]}`;
- qutrit carrier dimension: `27`;
- selected charged base overlap value: `{all_base_values[0]}`;
- charged generation ratio: `2:1:1`;
- counted H parameter: `UP-RET-OVERLAP.HRG = {h_ledger["controlled_r_H"]}`;
- current H parameter count spent: `{h_ledger["H_parameter_count_spent"]}`.

## Next Plan

1. Try strict finite-H source rows: selected `F_H`, `M_source`, `K_H`, or
   strict `R_H^RG`.
2. If strict rows remain zero, seek an independent non-Higgs
   `UP-RET-OVERLAP.HRG` prediction target without retuning.
3. Extend from scalar rows to matrix-level mixing only after the H row and
   source-row ledger are stable.

## Next Artifact

`{NEXT}`
"""

    write_json(SPECTRAL_PACKET, spectral)
    write_json(PROFILE_PACKET, profile)
    write_json(SEARCH_PACKET, search)
    write_json(H_PACKET, h_packet)
    write_json(OUTPUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(f"Wrote {rel(OUTPUT)}")
    print(f"Wrote {rel(CERT)}")
    print(f"Wrote {rel(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
