"""Run a diagnostic finite Hodge pipeline on an integrable h1=3 Iwasawa candidate.

This is intentionally not a selected MTT operator.  It checks that the finite
spectral/Galerkin extraction code path works once a valid differential is
supplied.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

from iwasawa_dolbeault_complex_extraction_audit import (
    build_map,
    cohomology_dimensions,
    composition_nonzero_counts,
    rank,
    ranks,
)


ROOT = Path(__file__).resolve().parent
CERT_DIR = ROOT.parent / "certificates"
CERT = CERT_DIR / "iwasawa_diagnostic_h1_three_spectral_pipeline_certificate.json"
PAPER = ROOT / "Iwasawa_Diagnostic_H1_Three_Spectral_Pipeline_v1.md"


DIAGNOSTIC_A01 = [
    (0, 1, Fraction(1), (1,)),
    (0, 2, Fraction(1), (1,)),
    (1, 2, Fraction(1), (1,)),
]


@dataclass(frozen=True)
class Gate:
    label: str
    status: str
    detail: str


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]


def matmul(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    if not left or not right:
        return []
    rows = len(left)
    mids = len(right)
    cols = len(right[0])
    return [
        [
            sum(left[row][mid] * right[mid][col] for mid in range(mids))
            for col in range(cols)
        ]
        for row in range(rows)
    ]


def matadd(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [
        [left[row][col] + right[row][col] for col in range(len(left[0]))]
        for row in range(len(left))
    ]


def identity(size: int) -> list[list[Fraction]]:
    return [
        [Fraction(1 if row == col else 0) for col in range(size)]
        for row in range(size)
    ]


def rref(matrix: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivots: list[int] = []
    pivot_row = 0
    for col in range(cols):
        pivot = None
        for row in range(pivot_row, rows):
            if work[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or work[row][col] == 0:
                continue
            factor = work[row][col]
            work[row] = [
                work[row][idx] - factor * work[pivot_row][idx]
                for idx in range(cols)
            ]
        pivots.append(col)
        pivot_row += 1
        if pivot_row == rows:
            break
    return work, pivots


def nullspace(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    reduced, pivots = rref(matrix)
    cols = len(matrix[0]) if matrix else 0
    pivot_set = set(pivots)
    free_cols = [col for col in range(cols) if col not in pivot_set]
    basis: list[list[Fraction]] = []
    for free_col in free_cols:
        vector = [Fraction(0) for _ in range(cols)]
        vector[free_col] = Fraction(1)
        for row, pivot_col in enumerate(pivots):
            vector[pivot_col] = -reduced[row][free_col]
        basis.append(vector)
    return basis


def inverse(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    size = len(matrix)
    work = [matrix[row][:] + identity(size)[row] for row in range(size)]
    pivot_row = 0
    for col in range(size):
        pivot = None
        for row in range(pivot_row, size):
            if work[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            raise ValueError("matrix is singular")
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(size):
            if row == pivot_row or work[row][col] == 0:
                continue
            factor = work[row][col]
            work[row] = [
                work[row][idx] - factor * work[pivot_row][idx]
                for idx in range(2 * size)
            ]
        pivot_row += 1
    return [row[size:] for row in work]


def columns_to_matrix(columns: list[list[Fraction]]) -> list[list[Fraction]]:
    if not columns:
        return []
    return [
        [columns[col][row] for col in range(len(columns))]
        for row in range(len(columns[0]))
    ]


def is_zero(matrix: list[list[Fraction]]) -> bool:
    return all(value == 0 for row in matrix for value in row)


def equal_matrix(left: list[list[Fraction]], right: list[list[Fraction]]) -> bool:
    return left == right


def degree_one_labels() -> list[str]:
    return [
        f"fiber{fiber}_baromega{form}"
        for fiber in (1, 2, 3)
        for form in (1, 2, 3)
    ]


def representative_summary(null_vectors: list[list[Fraction]]) -> list[dict[str, str]]:
    labels = degree_one_labels()
    reps: list[dict[str, str]] = []
    for vector in null_vectors:
        terms = []
        for label, coefficient in zip(labels, vector):
            if coefficient == 0:
                continue
            if coefficient == 1:
                terms.append(label)
            elif coefficient == -1:
                terms.append(f"-{label}")
            else:
                terms.append(f"{coefficient}*{label}")
        reps.append({"representative": " + ".join(terms) if terms else "0"})
    return reps


def contains_all(text: str, needles: list[str]) -> bool:
    return all(needle in text for needle in needles)


def main() -> None:
    cert = load_json(CERT)
    paper = read(PAPER)

    d0 = build_map(0, DIAGNOSTIC_A01)
    d1 = build_map(1, DIAGNOSTIC_A01)
    rank_values = ranks(DIAGNOSTIC_A01)
    cohomology = cohomology_dimensions(rank_values)
    counts = composition_nonzero_counts(DIAGNOSTIC_A01)
    laplacian_1 = matadd(matmul(d0, transpose(d0)), matmul(transpose(d1), d1))
    lap_rank = rank(laplacian_1)
    null_vectors = nullspace(laplacian_1)
    n_matrix = columns_to_matrix(null_vectors)
    gram = matmul(transpose(n_matrix), n_matrix)
    projector = matmul(matmul(n_matrix, inverse(gram)), transpose(n_matrix))

    projector_idempotent = equal_matrix(matmul(projector, projector), projector)
    projector_self_adjoint = equal_matrix(transpose(projector), projector)
    kernel_residual_zero = is_zero(matmul(laplacian_1, n_matrix))
    projected_residual_zero = is_zero(matmul(laplacian_1, projector))
    reps = [item["representative"] for item in representative_summary(null_vectors)]

    computed = cert.get("computed_finite_complex", {})
    hodge = cert.get("computed_hodge_pipeline", {})
    achieves = cert.get("what_this_achieves", {})
    guardrails = cert.get("guardrails", {})
    verdict = cert.get("verdict", {})

    gates = [
        Gate(
            "certificate status",
            "DIAGNOSTIC"
            if cert.get("status") == "DIAGNOSTIC_H1_THREE_SPECTRAL_PIPELINE_WORKS_NOT_SELECTED"
            else "FAIL",
            str(cert.get("status")),
        ),
        Gate(
            "candidate explicitly not selected",
            "PASS"
            if cert.get("diagnostic_operator", {}).get("selected") is False
            and cert.get("diagnostic_operator", {}).get("non_invariant") is False
            else "FAIL",
            str(cert.get("diagnostic_operator", {})),
        ),
        Gate(
            "integrability",
            "PASS"
            if counts == [0, 0] == computed.get("composition_nonzero_counts")
            else "FAIL",
            str(counts),
        ),
        Gate(
            "ranks",
            "PASS" if rank_values == [2, 4, 2] == computed.get("map_ranks") else "FAIL",
            str(rank_values),
        ),
        Gate(
            "cohomology",
            "PASS"
            if cohomology == [1, 3, 3, 1]
            and computed.get("cohomology_dimensions", {}).get("h1") == 3
            else "FAIL",
            str(cohomology),
        ),
        Gate(
            "degree-one Laplacian",
            "PASS"
            if len(laplacian_1) == 9
            and lap_rank == 6 == hodge.get("laplacian_rank")
            else "FAIL",
            f"dimension={len(laplacian_1)}, rank={lap_rank}",
        ),
        Gate(
            "kernel dimension",
            "PASS"
            if len(null_vectors) == 3 == hodge.get("kernel_dimension")
            else "FAIL",
            str(len(null_vectors)),
        ),
        Gate(
            "projector exact",
            "PASS"
            if projector_idempotent
            and projector_self_adjoint
            and hodge.get("exact_kernel_projector_constructed") is True
            and hodge.get("projector_idempotent_exact") is True
            and hodge.get("projector_self_adjoint_exact") is True
            else "FAIL",
            f"idempotent={projector_idempotent}, self_adjoint={projector_self_adjoint}",
        ),
        Gate(
            "residuals zero",
            "PASS"
            if kernel_residual_zero
            and projected_residual_zero
            and hodge.get("kernel_residual_zero") is True
            else "FAIL",
            f"kernel={kernel_residual_zero}, projector={projected_residual_zero}",
        ),
        Gate(
            "representatives recorded",
            "PASS" if reps == hodge.get("representatives") else "FAIL",
            str(reps),
        ),
        Gate(
            "non-invariant truncation still open",
            "OPEN"
            if hodge.get("non_invariant_truncation_error_certified") is False
            else "FAIL",
            "diagnostic invariant finite complex only",
        ),
        Gate(
            "achievement limited",
            "PASS"
            if achieves.get("proves_pipeline_can_extract_three_modes_when_valid_D_is_given") is True
            and achieves.get("proves_selected_MTT_D_E_exists") is False
            and achieves.get("proves_selected_H1_E_representatives") is False
            and achieves.get("proves_SM_matrices") is False
            else "FAIL",
            str(achieves),
        ),
        Gate(
            "guardrails",
            "PASS"
            if guardrails.get("claims_diagnostic_candidate_is_selected") is False
            and guardrails.get("uses_sparse_candidate_as_hym_proof") is False
            and guardrails.get("uses_pipeline_output_as_family_proof") is False
            and guardrails.get("claims_full_sm_closure") is False
            else "FAIL",
            str(guardrails),
        ),
        Gate(
            "verdict",
            "PASS"
            if verdict.get("diagnostic_pipeline_closed") is True
            and verdict.get("selected_spectral_branch_still_open") is True
            and "selected D_E" in verdict.get("next_step", "")
            else "FAIL",
            str(verdict),
        ),
        Gate(
            "paper records diagnostic nature",
            "PASS"
            if contains_all(
                paper,
                [
                    "not a proof-source substitution",
                    "dim ker(L_1) = 3",
                    "P_ker^2 = P_ker",
                    "does not close the MTT branch",
                    "replace this diagnostic candidate by a selected D_E",
                ],
            )
            else "FAIL",
            str(PAPER),
        ),
    ]

    print("Iwasawa diagnostic h1=3 spectral pipeline audit")
    print("===============================================")
    print()
    print(f"composition_nonzero_counts={counts}")
    print(f"map_ranks={rank_values}")
    print(f"cohomology_dimensions={cohomology}")
    print(f"laplacian_1_rank={lap_rank}")
    print(f"kernel_dimension={len(null_vectors)}")
    print(f"representatives={representative_summary(null_vectors)}")
    print()
    width = max(len(gate.label) for gate in gates)
    status_width = max(len(gate.status) for gate in gates)
    for gate in gates:
        print(f"{gate.label:{width}s}  {gate.status:{status_width}s}  {gate.detail}")

    failures = [gate for gate in gates if gate.status == "FAIL"]
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
