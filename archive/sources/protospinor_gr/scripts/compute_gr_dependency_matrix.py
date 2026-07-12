from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "certificates" / "protospinor_gr_response_dependency_certificate.json"
OUTPUT = ROOT / "certificates" / "gr_dependency_matrix_certificate.json"


def transitive_reachability(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    reach = [row[:] for row in matrix]
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] = int(bool(reach[i][j] or reach[k][j]))
    return reach


def main() -> None:
    cert = json.loads(INPUT.read_text(encoding="utf-8"))
    rows = cert["dependency_rows"]
    ids = [row["id"] for row in rows]

    external_nodes = sorted(
        {
            dep
            for row in rows
            for dep in row["depends_on"]
            if dep not in ids
        }
    )
    nodes = ids + external_nodes
    index = {node: i for i, node in enumerate(nodes)}

    adjacency = [[0 for _ in nodes] for _ in nodes]
    for row in rows:
        src = index[row["id"]]
        for dep in row["depends_on"]:
            adjacency[src][index[dep]] = 1

    reach = transitive_reachability(adjacency)
    gr_idx = index["full_GR_numeric_closure"]
    reachable_from_gr = [
        nodes[j] for j, value in enumerate(reach[gr_idx]) if value and nodes[j] != "full_GR_numeric_closure"
    ]

    row_status = {
        row["id"]: {
            "closed": bool(row["closed"]),
            "kind": row["kind"],
            "depends_on": row["depends_on"],
        }
        for row in rows
    }
    reachable_closed = [
        node
        for node in reachable_from_gr
        if node in row_status and row_status[node]["closed"]
    ]
    reachable_open = [
        node
        for node in reachable_from_gr
        if node not in row_status or not row_status[node]["closed"]
    ]

    matrix_cert = {
        "certificate": "GRDependencyMatrixCertificate",
        "status": "GR_DEPENDENCY_MATRIX_BUILT_FULL_GR_REACHES_OPEN_RESPONSE_GATES",
        "source_certificate": str(INPUT),
        "node_order": nodes,
        "adjacency_matrix": adjacency,
        "transitive_reachability_matrix": reach,
        "full_GR_numeric_closure_reachable_nodes": reachable_from_gr,
        "reachable_closed_nodes": reachable_closed,
        "reachable_open_nodes": reachable_open,
        "counts": {
            "nodes": len(nodes),
            "edges": sum(sum(row) for row in adjacency),
            "reachable_from_full_GR": len(reachable_from_gr),
            "reachable_closed_dependency_rows": len(reachable_closed),
            "reachable_open_or_external_nodes": len(reachable_open),
        },
        "interpretation": {
            "closed_dependency": "The GR theorem target already rests on the closed protospinor binary loop and selected internal rho_UV branch.",
            "open_dependency": "The same target also reaches open chart, time-ordering, source, finite C1, Hessian, stress-response, and normalization gates.",
            "consequence": "This numerically verifies dependency structure, not full GR closure.",
        },
        "guardrails": {
            "claims_full_GR_numeric_closure": False,
            "counts_graph_reachability_as_physical_derivation": False,
            "uses_observed_GR_data": False,
        },
    }
    OUTPUT.write_text(json.dumps(matrix_cert, indent=2), encoding="utf-8")
    print(json.dumps({"wrote": str(OUTPUT), "status": matrix_cert["status"]}, indent=2))


if __name__ == "__main__":
    main()

