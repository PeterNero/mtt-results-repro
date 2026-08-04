"""Construct a noncommuting pure-gauge finite-mesh rho_E prototype.

The finite-mesh rho_E validator keys transition values by (generator,target).
For a pure-gauge table

    rho(source -> target) = U(source)^* U(target),

this is well-defined only if all source nodes that reduce to the same
(generator,target) key have the same gauge value.  This script computes that
source-equivalence relation and assigns block-unitary gauges from a small
noncommuting subgroup that preserves one rank-one line.

The output is a genuine noncommuting finite transition-table prototype, but it
is pure gauge and unselected.  It tests the validator stack; it does not prove
physical family mixing.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from pathlib import Path


GENERATORS = ("g1", "g2", "g3", "g4", "g5", "g6")
FAMILY_SECTORS = ("Q", "u", "d", "L", "e", "N")
TOL = 1e-9

Node = tuple[int, int, int, int, int, int]
FaceKey = tuple[str, Node]
Matrix = list[list[complex]]


class DisjointSet:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            self.parent[right_root] = left_root


def node_key(node: Node) -> str:
    return ",".join(str(value) for value in node)


def all_closed_nodes(n: int) -> list[Node]:
    return list(itertools.product(range(n + 1), repeat=6))  # type: ignore[return-value]


def boundary_targets(node: Node, n: int) -> list[FaceKey]:
    x1, x2, y1, y2, t1, t2 = node
    targets: list[FaceKey] = []
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


def zero_matrix() -> Matrix:
    return [[0.0 + 0.0j for _ in range(3)] for _ in range(3)]


def identity_matrix() -> Matrix:
    return [
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j],
    ]


def offdiag_abs(matrix: Matrix) -> float:
    return max(abs(matrix[i][j]) for i in range(3) for j in range(3) if i != j)


def commutator(left: Matrix, right: Matrix) -> Matrix:
    left_right = matmul(left, right)
    right_left = matmul(right, left)
    return [
        [left_right[i][j] - right_left[i][j] for j in range(3)]
        for i in range(3)
    ]


def serialize_complex(value: complex) -> int | float | list[float]:
    real = 0.0 if abs(value.real) < 1e-14 else round(value.real, 15)
    imag = 0.0 if abs(value.imag) < 1e-14 else round(value.imag, 15)
    if imag == 0.0:
        if abs(real - round(real)) < 1e-14:
            return int(round(real))
        return real
    return [real, imag]


def serialize_matrix(matrix: Matrix) -> dict[str, list[list[int | float | list[float]]]]:
    return {
        "matrix": [
            [serialize_complex(value) for value in row]
            for row in matrix
        ]
    }


def pauli_block_group() -> list[Matrix]:
    identity = identity_matrix()
    swap = [
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j],
        [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
    ]
    sign = [
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 0.0 + 0.0j, -1.0 + 0.0j],
    ]
    return [identity, swap, sign, matmul(swap, sign)]


def source_equivalence(mesh_n: int) -> tuple[list[Node], dict[FaceKey, list[Node]], DisjointSet]:
    nodes = all_closed_nodes(mesh_n)
    node_index = {node: index for index, node in enumerate(nodes)}
    disjoint = DisjointSet(len(nodes))
    key_sources: dict[FaceKey, list[Node]] = {}

    for node in nodes:
        for key in boundary_targets(node, mesh_n):
            key_sources.setdefault(key, []).append(node)

    for sources in key_sources.values():
        first = node_index[sources[0]]
        for source in sources[1:]:
            disjoint.union(first, node_index[source])

    return nodes, key_sources, disjoint


def sector_maps() -> dict[str, dict[str, object]]:
    identity = serialize_matrix(identity_matrix())
    maps: dict[str, dict[str, object]] = {
        sector: {
            "kind": "family",
            "dimension": 3,
            "projector": identity,
        }
        for sector in FAMILY_SECTORS
    }
    maps["H"] = {
        "kind": "single_higgs_carrier",
        "dimension": 1,
        "projector": serialize_matrix(
            [
                [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
            ]
        ),
    }
    return maps


def construct(mesh_n: int) -> tuple[dict[str, object], dict[str, object]]:
    nodes, key_sources, disjoint = source_equivalence(mesh_n)
    node_index = {node: index for index, node in enumerate(nodes)}
    roots = sorted({disjoint.find(node_index[node]) for node in nodes})
    root_index = {root: index for index, root in enumerate(roots)}
    component_sizes = Counter(
        disjoint.find(node_index[node])
        for node in nodes
    )
    component_size_histogram = Counter(component_sizes.values())

    group = pauli_block_group()
    node_gauge = {
        node: group[root_index[disjoint.find(node_index[node])] % len(group)]
        for node in nodes
    }

    generator_data: dict[str, dict[str, dict[str, object]]] = {
        generator: {"values": {}} for generator in GENERATORS
    }
    face_matrices: list[tuple[str, Matrix]] = []
    for (generator, target), sources in sorted(
        key_sources.items(),
        key=lambda item: (item[0][0], item[0][1]),
    ):
        source = sources[0]
        matrix = matmul(adjoint(node_gauge[source]), node_gauge[target])
        generator_data[generator]["values"][node_key(target)] = serialize_matrix(matrix)
        face_matrices.append((generator, matrix))

    identity = identity_matrix()
    nonidentity_by_generator = Counter(
        generator
        for generator, matrix in face_matrices
        if max_abs_diff(matrix, identity) > TOL
    )
    offdiag_by_generator = Counter(
        generator
        for generator, matrix in face_matrices
        if offdiag_abs(matrix) > TOL
    )
    max_commutator = 0.0
    for index, (_, left) in enumerate(face_matrices):
        for _, right in face_matrices[index + 1 :]:
            max_commutator = max(
                max_commutator,
                max_abs_diff(commutator(left, right), zero_matrix()),
            )

    candidate: dict[str, object] = {
        "prototype": "IwasawaPureGaugeNonabelianMeshRhoE",
        "status": "PROTOTYPE_UNSELECTED",
        "rank": 3,
        "mesh_N": mesh_n,
        "generator_data": generator_data,
        "metric_data": {"matrix": [[1, 0, 0], [0, 1, 0], [0, 0, 1]]},
        "sector_projection_maps": sector_maps(),
        "guardrails": {
            "claims_selected_rho_E": False,
            "claims_selected_D_E": False,
            "claims_physical_family_mixing": False,
            "uses_observed_flavor_data": False,
        },
    }
    summary: dict[str, object] = {
        "calculation": "IwasawaPureGaugeNonabelianMeshRhoEPrototypeConstruct",
        "mesh_N": mesh_n,
        "rank": 3,
        "closed_nodes": len(nodes),
        "face_keys": len(key_sources),
        "source_equivalence_components": len(roots),
        "component_size_histogram": {
            str(size): count for size, count in sorted(component_size_histogram.items())
        },
        "face_keys_by_generator": dict(sorted(Counter(key[0] for key in key_sources).items())),
        "nonidentity_face_values": sum(nonidentity_by_generator.values()),
        "nonidentity_by_generator": dict(sorted(nonidentity_by_generator.items())),
        "offdiagonal_face_values": sum(offdiag_by_generator.values()),
        "offdiagonal_by_generator": dict(sorted(offdiag_by_generator.items())),
        "max_pairwise_commutator_abs": max_commutator,
        "gauge_group": "block diag(1, <Pauli X,Z>)",
        "higgs_projector": "diag(1,0,0), the common invariant line",
        "verdict": {
            "noncommuting_face_matrices_exist": max_commutator > 1e-8,
            "pure_gauge_flat_cocycle": True,
            "common_rank_one_higgs_line_preserved": True,
            "candidate_is_selected_rho_E": False,
            "candidate_proves_physical_family_mixing": False,
            "next_step": "Replace pure-gauge noncommuting tables by selected nonabelian Cech/monad or HYM/Strominger transition data with a nontrivial D_E response.",
        },
    }
    return summary, candidate


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mesh-N", type=int, default=1, help="closed-cell subdivision N")
    parser.add_argument(
        "--emit-candidate",
        type=Path,
        help="optional path for the generated nonabelian rho_E/metric/sector prototype JSON",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.mesh_N < 1:
        raise SystemExit("mesh_N must be positive")

    summary, candidate = construct(args.mesh_N)
    if args.emit_candidate:
        args.emit_candidate.write_text(
            json.dumps(candidate, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
