"""Analyze the N=1 scalar phase rho_E solution space against coboundaries.

This is the first small-N Route C ansatz search after the promotion gate.  It
works over finite prime fields F_p for scalar phase exponents and compares:

  1. the finite corner path-independence solution space, and
  2. the source-key-compatible face-graph coboundary image.

If the two dimensions agree and every coboundary image vector satisfies the
corner equations, then every scalar phase solution is pure gauge on the
validator face graph.  Diagonal rank-three phases and constant-unitary
conjugates inherit the same obstruction componentwise.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from typing import Any

from solve_iwasawa_scalar_phase_mesh import (
    FaceKey,
    Node,
    all_closed_nodes,
    boundary_generators,
    build_linear_system,
    reduce_target,
)


@dataclass
class DisjointSet:
    parent: list[int]

    @classmethod
    def with_size(cls, size: int) -> "DisjointSet":
        return cls(list(range(size)))

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left != root_right:
            self.parent[root_right] = root_left


def rank_mod(matrix: list[list[int]], modulus: int, ncols: int) -> int:
    work = [
        [value % modulus for value in row]
        for row in matrix
        if any(value % modulus for value in row)
    ]
    rank = 0
    for col in range(ncols):
        pivot = None
        for row in range(rank, len(work)):
            if work[row][col] % modulus:
                pivot = row
                break
        if pivot is None:
            continue

        work[rank], work[pivot] = work[pivot], work[rank]
        inverse = pow(work[rank][col] % modulus, -1, modulus)
        work[rank] = [(value * inverse) % modulus for value in work[rank]]
        for row in range(len(work)):
            if row == rank:
                continue
            factor = work[row][col] % modulus
            if factor:
                work[row] = [
                    (work[row][idx] - factor * work[rank][idx]) % modulus
                    for idx in range(ncols)
                ]
        rank += 1
    return rank


def sources_by_face_key(mesh_n: int, unknown_order: list[FaceKey]) -> dict[FaceKey, list[Node]]:
    unknown_set = set(unknown_order)
    sources: dict[FaceKey, list[Node]] = {key: [] for key in unknown_order}
    for source in all_closed_nodes(mesh_n):
        for generator in boundary_generators(source, mesh_n):
            target = reduce_target(source, generator, mesh_n)
            key = (generator, target)
            if key in unknown_set:
                sources[key].append(source)
    missing = [key for key, key_sources in sources.items() if not key_sources]
    if missing:
        raise ValueError(f"face keys have no sources: {missing[:5]}")
    return sources


def source_key_components(
    mesh_n: int,
    sources: dict[FaceKey, list[Node]],
) -> tuple[dict[Node, int], int, dict[str, int]]:
    nodes = all_closed_nodes(mesh_n)
    node_index = {node: index for index, node in enumerate(nodes)}
    dsu = DisjointSet.with_size(len(nodes))

    for key_sources in sources.values():
        reference = node_index[key_sources[0]]
        for source in key_sources[1:]:
            dsu.union(reference, node_index[source])

    roots = sorted({dsu.find(index) for index in range(len(nodes))})
    root_index = {root: index for index, root in enumerate(roots)}
    node_component = {
        node: root_index[dsu.find(index)]
        for node, index in node_index.items()
    }

    sizes: dict[int, int] = {}
    for component in node_component.values():
        sizes[component] = sizes.get(component, 0) + 1
    histogram: dict[str, int] = {}
    for size in sizes.values():
        histogram[str(size)] = histogram.get(str(size), 0) + 1
    return node_component, len(roots), dict(sorted(histogram.items()))


def coboundary_matrix(
    unknown_order: list[FaceKey],
    sources: dict[FaceKey, list[Node]],
    node_component: dict[Node, int],
    component_count: int,
    modulus: int,
) -> list[list[int]]:
    matrix: list[list[int]] = []
    for key in unknown_order:
        _, target = key
        source = sources[key][0]
        row = [0] * component_count
        row[node_component[target]] = (row[node_component[target]] + 1) % modulus
        row[node_component[source]] = (row[node_component[source]] - 1) % modulus
        matrix.append(row)
    return matrix


def equation_image_residual_count(
    equation_rows: list[list[int]],
    image_matrix: list[list[int]],
    modulus: int,
) -> int:
    if not image_matrix:
        return 0
    component_count = len(image_matrix[0])
    failures = 0
    for equation in equation_rows:
        for component in range(component_count):
            value = sum(
                equation[face_index] * image_matrix[face_index][component]
                for face_index in range(len(image_matrix))
            )
            if value % modulus:
                failures += 1
    return failures


def analyze_modulus(mesh_n: int, modulus: int) -> dict[str, Any]:
    unknown_order, equation_rows, target_mismatches = build_linear_system(mesh_n, modulus)
    equation_rank = rank_mod(equation_rows, modulus, len(unknown_order))
    solution_dimension = len(unknown_order) - equation_rank
    sources = sources_by_face_key(mesh_n, unknown_order)
    node_component, component_count, component_histogram = source_key_components(
        mesh_n,
        sources,
    )
    image_matrix = coboundary_matrix(
        unknown_order,
        sources,
        node_component,
        component_count,
        modulus,
    )
    image_rank = rank_mod(image_matrix, modulus, component_count)
    residual_count = equation_image_residual_count(equation_rows, image_matrix, modulus)

    solution_equals_coboundary = (
        target_mismatches == 0
        and residual_count == 0
        and image_rank == solution_dimension
    )

    return {
        "field": f"F{modulus}",
        "modulus": modulus,
        "mesh_N": mesh_n,
        "closed_nodes": len(all_closed_nodes(mesh_n)),
        "unknown_face_values": len(unknown_order),
        "corner_equations": len(equation_rows),
        "target_mismatches": target_mismatches,
        "corner_equation_rank": equation_rank,
        "flat_solution_dimension": solution_dimension,
        "source_key_gauge_components": component_count,
        "source_key_component_size_histogram": component_histogram,
        "source_key_coboundary_rank": image_rank,
        "gauge_kernel_dimension": component_count - image_rank,
        "coboundary_image_equation_residual_count": residual_count,
        "coboundary_image_inside_flat_solution_space": residual_count == 0,
        "flat_solution_space_equals_source_key_coboundaries": solution_equals_coboundary,
        "rhoE_source_promotion_possible_in_scalar_phase_ansatz": not solution_equals_coboundary,
    }


def parse_moduli(value: str) -> list[int]:
    moduli = [int(part.strip()) for part in value.split(",") if part.strip()]
    if not moduli:
        raise argparse.ArgumentTypeError("expected at least one modulus")
    return moduli


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for divisor in range(2, int(value**0.5) + 1):
        if value % divisor == 0:
            return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mesh-N", type=int, default=1)
    parser.add_argument("--moduli", type=parse_moduli, default=[2, 3, 5, 7])
    args = parser.parse_args()
    if args.mesh_N < 1:
        raise SystemExit("--mesh-N must be positive")
    if args.mesh_N != 1:
        raise SystemExit("this obstruction analyzer is currently certified only for mesh N=1")
    if any(not is_prime(modulus) for modulus in args.moduli):
        raise SystemExit("this analyzer expects prime moduli so F_p linear algebra is valid")

    analyses = [analyze_modulus(args.mesh_N, modulus) for modulus in args.moduli]
    all_equal = all(
        entry["flat_solution_space_equals_source_key_coboundaries"]
        for entry in analyses
    )
    result = {
        "calculation": "IwasawaN1PhaseCoboundaryObstruction",
        "status": "OBSTRUCTION_PROVED_FOR_CERTIFIED_PRIME_PHASE_FIELDS"
        if all_equal
        else "OBSTRUCTION_NOT_PROVED_FOR_ALL_REQUESTED_FIELDS",
        "mesh_N": args.mesh_N,
        "moduli": args.moduli,
        "analyses": analyses,
        "global_verdict": {
            "scalar_phase_ansatz_source_promotion_blocked": all_equal,
            "diagonal_rank_three_phase_ansatz_blocked_componentwise": all_equal,
            "constant_unitary_conjugates_blocked": all_equal,
            "does_not_rule_out_genuinely_matrix_valued_selected_data": True,
            "does_not_rule_out_selected_D_E_response_promotion": True,
            "next_step": (
                "Search genuinely matrix-valued non-coboundary transition data "
                "or construct selected D_E/dotD response data that pass the "
                "promotion gate."
            ),
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
