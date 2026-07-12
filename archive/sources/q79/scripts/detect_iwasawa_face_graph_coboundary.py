"""Detect whether finite-mesh rho_E data are a face-graph coboundary.

For a supplied finite table, this diagnostic tries to find node gauges U(node)
such that every boundary face transition satisfies

    rho_E(source -> target) = U(source)^(-1) U(target).

For unitary tables this is U(source)^* U(target).  Passing this diagnostic does
not mean the data are selected; it means the finite face graph alone sees only a
gauge-trivial flat table.  Failing it gives a finite graph obstruction that must
still be checked by the ordinary mesh/metric/sector validators.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import deque
from pathlib import Path
from typing import Any


GENERATORS = ("g1", "g2", "g3", "g4", "g5", "g6")
TOL = 1e-8

Node = tuple[int, int, int, int, int, int]
Matrix = list[list[complex]]


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
    return [[parse_complex(value) for value in row] for row in matrix_data]


def node_key(node: Node) -> str:
    return ",".join(str(value) for value in node)


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


def identity_matrix() -> Matrix:
    return [
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j],
    ]


def max_abs_diff(left: Matrix, right: Matrix) -> float:
    return max(abs(left[i][j] - right[i][j]) for i in range(3) for j in range(3))


def matrix_inverse(matrix: Matrix) -> Matrix:
    size = len(matrix)
    work = [
        matrix[row][:]
        + [1.0 + 0.0j if row == col else 0.0 + 0.0j for col in range(size)]
        for row in range(size)
    ]
    for col in range(size):
        pivot = None
        for row in range(col, size):
            if abs(work[row][col]) > 1e-12:
                pivot = row
                break
        if pivot is None:
            raise ValueError("matrix is singular")
        work[col], work[pivot] = work[pivot], work[col]
        scale = work[col][col]
        work[col] = [value / scale for value in work[col]]
        for row in range(size):
            if row == col:
                continue
            factor = work[row][col]
            if abs(factor) > 1e-12:
                work[row] = [
                    work[row][idx] - factor * work[col][idx]
                    for idx in range(2 * size)
                ]
    return [row[size:] for row in work]


def all_closed_nodes(n: int) -> list[Node]:
    return list(itertools.product(range(n + 1), repeat=6))  # type: ignore[return-value]


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


class MatrixResolver:
    def __init__(self, generator_data: dict[str, Any]) -> None:
        self.generator_data = generator_data
        self.unique_keys: set[tuple[str, Node]] = set()

    def matrix(self, generator: str, target: Node) -> Matrix:
        entry = self.generator_data.get(generator)
        if entry is None:
            raise ValueError(f"missing generator {generator}")
        selected: Any
        if isinstance(entry, dict):
            values = entry.get("values")
            target_key = node_key(target)
            if isinstance(values, dict) and target_key in values:
                selected = values[target_key]
            elif "matrix" in entry:
                selected = entry
            else:
                raise ValueError(f"missing {generator} matrix at {target_key}")
        else:
            selected = entry
        self.unique_keys.add((generator, target))
        return parse_matrix(selected)


def load_candidate(path: Path) -> tuple[int, MatrixResolver]:
    data = json.loads(path.read_text(encoding="utf-8"))
    mesh_n = data.get("mesh_N")
    if not isinstance(mesh_n, int) or isinstance(mesh_n, bool) or mesh_n < 1:
        raise ValueError("mesh_N must be a positive integer")
    generator_data = data.get("generator_data")
    if not isinstance(generator_data, dict):
        raise ValueError("missing generator_data object")
    missing = [name for name in GENERATORS if generator_data.get(name) is None]
    if missing:
        raise ValueError(f"missing generator entries: {', '.join(missing)}")
    return mesh_n, MatrixResolver(generator_data)


def build_edges(mesh_n: int, resolver: MatrixResolver) -> list[tuple[Node, Node, str, Matrix]]:
    edges: list[tuple[Node, Node, str, Matrix]] = []
    for source in all_closed_nodes(mesh_n):
        for generator, target in boundary_targets(source, mesh_n):
            edges.append((source, target, generator, resolver.matrix(generator, target)))
    return edges


def detect(path: Path) -> dict[str, object]:
    mesh_n, resolver = load_candidate(path)
    nodes = all_closed_nodes(mesh_n)
    edges = build_edges(mesh_n, resolver)
    adjacency: dict[Node, list[tuple[Node, Matrix, bool]]] = {node: [] for node in nodes}
    inverse_failures = 0
    for source, target, _, matrix in edges:
        adjacency[source].append((target, matrix, True))
        try:
            inverse = matrix_inverse(matrix)
        except ValueError:
            inverse_failures += 1
            inverse = adjoint(matrix)
        adjacency[target].append((source, inverse, False))

    gauges: dict[Node, Matrix] = {}
    component_count = 0
    max_consistency_error = 0.0
    inconsistency_count = 0
    max_unitarity_error = 0.0
    identity = identity_matrix()

    for node in nodes:
        if node in gauges:
            continue
        component_count += 1
        gauges[node] = identity
        queue: deque[Node] = deque([node])
        while queue:
            current = queue.popleft()
            current_gauge = gauges[current]
            for neighbor, transport, _ in adjacency[current]:
                proposed = matmul(current_gauge, transport)
                if neighbor not in gauges:
                    gauges[neighbor] = proposed
                    queue.append(neighbor)
                    continue
                diff = max_abs_diff(proposed, gauges[neighbor])
                max_consistency_error = max(max_consistency_error, diff)
                if diff > TOL:
                    inconsistency_count += 1

    edge_residual_max = 0.0
    for source, target, _, matrix in edges:
        reconstructed = matmul(matrix_inverse(gauges[source]), gauges[target])
        edge_residual_max = max(edge_residual_max, max_abs_diff(reconstructed, matrix))
        max_unitarity_error = max(
            max_unitarity_error,
            max_abs_diff(matmul(adjoint(matrix), matrix), identity),
        )

    pure_gauge = (
        inverse_failures == 0
        and inconsistency_count == 0
        and max_consistency_error <= TOL
        and edge_residual_max <= TOL
    )
    return {
        "calculation": "IwasawaFaceGraphCoboundaryDiagnostic",
        "candidate": str(path),
        "mesh_N": mesh_n,
        "closed_nodes": len(nodes),
        "face_incidences": len(edges),
        "unique_face_keys": len(resolver.unique_keys),
        "graph_connected_components": component_count,
        "inverse_failures": inverse_failures,
        "inconsistency_count": inconsistency_count,
        "max_consistency_error": max_consistency_error,
        "max_edge_reconstruction_error": edge_residual_max,
        "max_transition_unitarity_error": max_unitarity_error,
        "face_graph_coboundary": pure_gauge,
        "verdict": {
            "finite_table_is_pure_gauge_on_face_graph": pure_gauge,
            "finite_table_has_graph_holonomy_obstruction": not pure_gauge,
            "diagnostic_proves_selected_nontrivial_bundle": False,
            "next_step": "Require selected Cech/monad or HYM/Strominger source data; finite face-graph coboundary status alone is not SM closure.",
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("candidate", type=Path, help="finite rho_E candidate JSON")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print(json.dumps(detect(args.candidate), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
