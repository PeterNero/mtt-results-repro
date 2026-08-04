"""Validate Hermitian metric compatibility for Iwasawa rho_E data.

For the section convention s(gamma*z)=rho_E(gamma,z)s(z), a Hermitian metric H
is compatible with a boundary face transition when

    rho_E(gamma,z)^* H(gamma*z) rho_E(gamma,z) = H(z).

Exit codes:
  0: complete finite-mesh metric candidate passes implemented checks
  1: complete candidate fails a mathematical/schema check
  2: candidate is incomplete/open rather than mathematically failed
"""

from __future__ import annotations

import itertools
import json
import math
import sys
from pathlib import Path
from typing import Any


GENERATORS = ("g1", "g2", "g3", "g4", "g5", "g6")
TOL = 1e-9

Node = tuple[int, int, int, int, int, int]
Matrix = list[list[complex]]


class IncompleteData(ValueError):
    """Raised when a required metric or transition value is still open."""


def parse_complex(value: Any) -> complex:
    if isinstance(value, (int, float)):
        return complex(float(value), 0.0)
    if (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(part, (int, float)) for part in value)
    ):
        return complex(float(value[0]), float(value[1]))
    raise ValueError(f"invalid complex entry {value!r}")


def parse_matrix(entry: Any) -> Matrix:
    matrix_data = entry.get("matrix") if isinstance(entry, dict) else entry
    if not isinstance(matrix_data, list) or len(matrix_data) != 3:
        raise ValueError("matrix must have three rows")
    matrix: Matrix = []
    for row in matrix_data:
        if not isinstance(row, list) or len(row) != 3:
            raise ValueError("matrix must be 3x3")
        matrix.append([parse_complex(value) for value in row])
    return matrix


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(3))
            for j in range(3)
        ]
        for i in range(3)
    ]


def adjoint(matrix: Matrix) -> Matrix:
    return [[matrix[j][i].conjugate() for j in range(3)] for i in range(3)]


def max_abs_diff(left: Matrix, right: Matrix) -> float:
    return max(abs(left[i][j] - right[i][j]) for i in range(3) for j in range(3))


def node_key(node: Node) -> str:
    return ",".join(str(value) for value in node)


def boundary_targets(node: Node, n: int) -> list[tuple[str, Node]]:
    x1, x2, y1, y2, t1, t2 = node
    targets: list[tuple[str, Node]] = []
    if x1 == n:
        targets.append(("g1", (0, x2, y1, y2, (t1 - y1) % n, (t2 - y2) % n)))
    if x2 == n:
        targets.append(("g2", (x1, 0, y1, y2, (t1 + y2) % n, (t2 - y1) % n)))
    if y1 == n:
        targets.append(("g3", (x1, x2, 0, y2, t1, t2)))
    if y2 == n:
        targets.append(("g4", (x1, x2, y1, 0, t1, t2)))
    if t1 == n:
        targets.append(("g5", (x1, x2, y1, y2, 0, t2)))
    if t2 == n:
        targets.append(("g6", (x1, x2, y1, y2, t1, 0)))
    return targets


def all_closed_nodes(n: int) -> list[Node]:
    return list(itertools.product(range(n + 1), repeat=6))  # type: ignore[return-value]


def validate_mesh_n(value: Any) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise IncompleteData("MISSING mesh_N positive integer")
    return value


def is_hermitian(matrix: Matrix) -> bool:
    return max_abs_diff(matrix, adjoint(matrix)) <= TOL


def is_positive_definite_hermitian(matrix: Matrix) -> bool:
    if not is_hermitian(matrix):
        return False
    lower = [[0.0 + 0.0j for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(i + 1):
            value = matrix[i][j] - sum(
                lower[i][k] * lower[j][k].conjugate() for k in range(j)
            )
            if i == j:
                if abs(value.imag) > TOL or value.real <= TOL:
                    return False
                lower[i][j] = complex(math.sqrt(value.real), 0.0)
            else:
                if abs(lower[j][j]) <= TOL:
                    return False
                lower[i][j] = value / lower[j][j]
    return True


class MatrixResolver:
    def __init__(self, data: dict[str, Any], label: str) -> None:
        self.data = data
        self.label = label
        self.seen: dict[tuple[str, Node], Matrix] = {}

    def generator_matrix(self, generator: str, target: Node) -> Matrix:
        key = (generator, target)
        if key in self.seen:
            return self.seen[key]

        entry = self.data.get(generator)
        if entry is None:
            raise IncompleteData(f"MISSING generator entry: {generator}")

        selected = select_matrix_entry(entry, target, f"{generator} matrix")
        matrix = parse_matrix(selected)
        self.seen[key] = matrix
        return matrix


class MetricResolver:
    def __init__(self, metric_data: Any) -> None:
        if not isinstance(metric_data, dict):
            raise IncompleteData("MISSING metric_data object")
        self.metric_data = metric_data
        self.seen: dict[Node, Matrix] = {}

    def metric(self, node: Node) -> Matrix:
        if node in self.seen:
            return self.seen[node]
        selected = select_matrix_entry(self.metric_data, node, "metric_data")
        matrix = parse_matrix(selected)
        self.seen[node] = matrix
        return matrix


def select_matrix_entry(entry: Any, node: Node, label: str) -> Any:
    if not isinstance(entry, dict):
        return entry

    values = entry.get("values")
    key = node_key(node)
    if isinstance(values, dict) and key in values:
        return values[key]
    if "matrix" in entry:
        return entry
    raise IncompleteData(f"MISSING {label} at node {key}")


def load_candidate(
    path: Path,
) -> tuple[int, str, int | None, MatrixResolver | None, MetricResolver | None]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("rank") != 3:
        return 2, "MISSING rank=3 bundle declaration", None, None, None

    generator_data = data.get("generator_data")
    if not isinstance(generator_data, dict):
        return 2, "MISSING generator_data object", None, None, None

    missing = [name for name in GENERATORS if generator_data.get(name) is None]
    if missing:
        return 2, f"MISSING generator entries: {', '.join(missing)}", None, None, None

    try:
        n = validate_mesh_n(data.get("mesh_N"))
        metric_resolver = MetricResolver(data.get("metric_data"))
    except IncompleteData as exc:
        return 2, str(exc), None, None, None

    return (
        0,
        f"loaded finite mesh_N={n} transition and metric data",
        n,
        MatrixResolver(generator_data, "generator_data"),
        metric_resolver,
    )


def validate_metrics(metric_resolver: MetricResolver) -> list[str]:
    failures: list[str] = []
    for node, metric in sorted(metric_resolver.seen.items()):
        if not is_hermitian(metric):
            failures.append(f"metric at {node_key(node)} is not Hermitian")
        elif not is_positive_definite_hermitian(metric):
            failures.append(f"metric at {node_key(node)} is not positive definite")
    return failures


def validate_metric_compatibility(
    n: int,
    rho: MatrixResolver,
    metrics: MetricResolver,
) -> list[str]:
    failures: list[str] = []
    for source in all_closed_nodes(n):
        for generator, target in boundary_targets(source, n):
            rho_matrix = rho.generator_matrix(generator, target)
            source_metric = metrics.metric(source)
            target_metric = metrics.metric(target)
            transported = matmul(matmul(adjoint(rho_matrix), source_metric), rho_matrix)
            diff = max_abs_diff(transported, target_metric)
            if diff > TOL:
                failures.append(
                    "metric compatibility failed at "
                    f"{node_key(source)} --{generator}--> {node_key(target)} "
                    f"max_abs_diff={diff:.3e}"
                )
    failures.extend(validate_metrics(metrics))
    return failures


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_iwasawa_rhoE_metric.py <rhoE-metric-data.json>")
        return 1

    path = Path(argv[1])
    try:
        code, message, n, rho, metrics = load_candidate(path)
        print(message)
        if code != 0:
            return code
        assert n is not None
        assert rho is not None
        assert metrics is not None
        failures = validate_metric_compatibility(n, rho, metrics)
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID finite-mesh rho_E metric data: {exc}")
        return 1

    if failures:
        print("rho_E metric validation FAIL")
        for failure in failures[:50]:
            print(f"- {failure}")
        if len(failures) > 50:
            print(f"- ... {len(failures) - 50} more failures")
        return 1

    print("rho_E metric validation PASS")
    print("Hermitian metrics are positive definite and compatible on boundary faces")
    print("selected rho_E origin, sector maps, and selected D_E remain separate checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
