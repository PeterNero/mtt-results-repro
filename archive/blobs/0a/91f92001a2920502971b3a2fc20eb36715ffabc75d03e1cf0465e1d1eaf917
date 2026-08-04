"""Emit the finite Route C selected-connection solve scaffold.

The scaffold is not a selected solution. It is the executable problem layout
for the direct finite HYM/Strominger route identified by the source hunt.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from itertools import product
from typing import Any


GENERATORS = ("g1", "g2", "g3", "g4", "g5", "g6")
FAMILY_SECTORS = ("Q", "u", "d", "L", "e", "N")
SECTORS = FAMILY_SECTORS + ("H",)

Node = tuple[int, int, int, int, int, int]


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
    return list(product(range(n + 1), repeat=6))  # type: ignore[return-value]


def scalar_quotient_class_count(n: int) -> int:
    nodes = all_closed_nodes(n)
    index = {node: idx for idx, node in enumerate(nodes)}
    dsu = DisjointSet.with_size(len(nodes))
    for node in nodes:
        for _, target in boundary_targets(node, n):
            dsu.union(index[node], index[target])
    return len({dsu.find(idx) for idx in range(len(nodes))})


def mesh_counts(n: int) -> dict[str, int]:
    nodes = all_closed_nodes(n)
    boundary_face_incidences = 0
    unique_rho_targets: set[tuple[str, Node]] = set()
    multi_face_nodes = 0
    for node in nodes:
        targets = boundary_targets(node, n)
        boundary_face_incidences += len(targets)
        unique_rho_targets.update(targets)
        if len(targets) >= 2:
            multi_face_nodes += 1

    scalar_classes = scalar_quotient_class_count(n)
    return {
        "mesh_N": n,
        "closed_cell_nodes": len(nodes),
        "scalar_quotient_dofs_identity_smoke": scalar_classes,
        "rank3_bundle_dofs_identity_smoke": 3 * scalar_classes,
        "boundary_face_incidences": boundary_face_incidences,
        "unique_rho_boundary_matrices_table_ansatz": len(unique_rho_targets),
        "complex_rho_entries_table_ansatz": 9 * len(unique_rho_targets),
        "corner_nodes_with_multiple_boundary_faces": multi_face_nodes,
        "metric_real_entries_full_node_table": 9 * len(nodes),
    }


def build_scaffold(n: int) -> dict[str, Any]:
    counts = mesh_counts(n)
    return {
        "calculation": "IwasawaRouteCFiniteSelectedConnectionSolveScaffold",
        "status": "SCAFFOLD_ONLY_SELECTED_VALUES_OPEN",
        "mesh": counts,
        "purpose": (
            "Define the finite residual problem whose output can become a "
            "selected D_E source if all source, residual, gap, and guardrail "
            "gates pass."
        ),
        "unknown_blocks": {
            "branch_packet": {
                "shape": "one of the two orientation packets m=1/q=79/F or m=2/q=369/F*",
                "downstream_validator": "scripts/validate_iwasawa_route_c_residuals.py",
            },
            "rho_E": {
                "shape": "rank-three boundary transition matrices",
                "table_ansatz_complex_entries_at_mesh_N": counts[
                    "complex_rho_entries_table_ansatz"
                ],
                "downstream_validator": "scripts/validate_iwasawa_rhoE_mesh.py",
            },
            "Hermitian_metric": {
                "shape": "positive-definite Hermitian 3x3 metric on mesh nodes or an evaluable rule",
                "full_node_table_real_entries_at_mesh_N": counts[
                    "metric_real_entries_full_node_table"
                ],
                "downstream_validator": "scripts/validate_iwasawa_rhoE_metric.py",
            },
            "sector_projectors": {
                "sectors": list(SECTORS),
                "downstream_validator": "scripts/validate_iwasawa_sector_maps.py",
            },
            "A01_or_DE_action": {
                "shape": "finite non-invariant Dolbeault/HYM operator action on each sector basis",
                "downstream_validator": "scripts/validate_iwasawa_de_action.py",
            },
            "dotD_alpha1": {
                "shape": "selected primitive alpha1 derivative of the same finite operator",
                "downstream_validator": "scripts/validate_iwasawa_dotd_response.py",
            },
        },
        "residual_gates": [
            "branch packet m=1/q=79/F or m=2/q=369/F*",
            "antiunitary conjugate retained for comparison",
            "dotD required to be same-branch derivative",
            "rho_E cocycle/path independence",
            "Hermitian metric compatibility",
            "integrability F^(0,2)=0",
            "HYM primitivity J contraction F=0",
            "alpha1 Bianchi/Strominger residual",
            "MTT selection gradient residual",
            "positive selected Hessian/Riesz gap",
            "no observed flavor or Execution II benchmark inputs",
        ],
        "validator_pipeline": [
            {
                "stage": "source residuals",
                "command": "python scripts/validate_iwasawa_route_c_residuals.py <route-c-residuals.json>",
            },
            {
                "stage": "rho_E mesh gluing",
                "command": "python scripts/validate_iwasawa_rhoE_mesh.py <rhoE-mesh-data.json>",
            },
            {
                "stage": "rho_E Hermitian metric",
                "command": "python scripts/validate_iwasawa_rhoE_metric.py <rhoE-metric-data.json>",
            },
            {
                "stage": "sector projectors",
                "command": "python scripts/validate_iwasawa_sector_maps.py <rhoE-sector-data.json>",
            },
            {
                "stage": "D_E sector action",
                "command": "python scripts/validate_iwasawa_de_action.py <de-action-data.json>",
            },
            {
                "stage": "Riesz/gap",
                "command": "python scripts/validate_iwasawa_riesz_gap.py <riesz-gap-data.json>",
            },
            {
                "stage": "reduced Green",
                "command": "python scripts/validate_iwasawa_reduced_green.py <reduced-green-data.json>",
            },
            {
                "stage": "dotD response",
                "command": "python scripts/validate_iwasawa_dotd_response.py <dotd-response-data.json>",
            },
        ],
        "minimal_outputs_to_unblock_selected_D_E": [
            "route-c residual certificate with all residuals below tolerance",
            "rho_E mesh data",
            "Hermitian metric data",
            "sector projector data",
            "sector D_E action data",
            "Riesz/gap data",
            "reduced Green data",
            "dotD alpha1 response data",
        ],
        "guardrails": {
            "claims_selected_D_E_constructed": False,
            "uses_identity_rhoE_as_selected": False,
            "uses_diagnostic_h1_three_as_selected": False,
            "uses_execution_ii_benchmarks": False,
            "uses_observed_masses_or_mixings": False,
            "claims_full_sm_closure": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mesh-N", type=int, default=1)
    args = parser.parse_args()
    if args.mesh_N < 1:
        raise SystemExit("--mesh-N must be positive")
    print(json.dumps(build_scaffold(args.mesh_N), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
