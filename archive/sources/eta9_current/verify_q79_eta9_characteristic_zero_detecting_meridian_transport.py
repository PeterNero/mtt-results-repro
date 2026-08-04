from __future__ import annotations

import hashlib
import json
from array import array
from collections import Counter
from decimal import Decimal, ROUND_HALF_EVEN
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.sparse.csgraph import connected_components, maximum_bipartite_matching

import build_q79_eta9_characteristic_zero_three_block_chart_oracle as oracle
import build_q79_eta9_family_macaulay_update as family_update


ROOT = Path(__file__).resolve().parent
PACKET = ROOT / "q79_eta9_characteristic_zero_detecting_meridian_transport.packet.json"
MACAULAY = ROOT / "q79_eta9_original_jacobian_macaulay_H02.packet.json"
CSC = ROOT / "q79_eta9_original_jacobian_macaulay_H02_csc.packet.json"
FACTOR = ROOT / "q79_eta9_original_jacobian_coordinate_factorization_H02.packet.json"


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while block := handle.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def array_hash(values: np.ndarray, dtype: str) -> str:
    canonical = np.ascontiguousarray(values, dtype=np.dtype(dtype))
    digest = hashlib.sha256()
    digest.update(np.asarray(canonical.shape, dtype="<i8").tobytes())
    digest.update(canonical.tobytes(order="C"))
    return digest.hexdigest()


def pattern_hash(pattern: sparse.csr_matrix) -> str:
    canonical = pattern.copy().tocsr()
    canonical.sort_indices()
    digest = hashlib.sha256()
    digest.update(np.asarray(canonical.shape, dtype="<i8").tobytes())
    digest.update(np.asarray(canonical.indptr, dtype="<i8").tobytes())
    digest.update(np.asarray(canonical.indices, dtype="<i4").tobytes())
    return digest.hexdigest()


def topological_order(component_count: int, sources: np.ndarray, targets: np.ndarray) -> list[int]:
    successors: list[set[int]] = [set() for _ in range(component_count)]
    indegree = [0] * component_count
    for source, target in zip(sources.tolist(), targets.tolist(), strict=True):
        if source == target or target in successors[source]:
            continue
        successors[source].add(target)
        indegree[target] += 1
    ready = sorted(index for index, degree in enumerate(indegree) if degree == 0)
    order: list[int] = []
    while ready:
        source = ready.pop(0)
        order.append(source)
        for target in sorted(successors[source]):
            indegree[target] -= 1
            if indegree[target] == 0:
                ready.append(target)
                ready.sort()
    require(len(order) == component_count, "replay condensation DAG")
    return order


def replay_h02() -> dict[str, object]:
    macaulay = load(MACAULAY)
    csc = load(CSC)
    factor = load(FACTOR)
    generators0, _, _ = oracle.exact_generators(
        load(oracle.BASE), load(oracle.GLOBAL_F0), load(oracle.B89)
    )
    target = [
        tuple(int(value) for value in exponent)
        for exponent in macaulay["target_monomial_basis"]["exponent_vectors"]
    ]
    target_lookup = {exponent: row for row, exponent in enumerate(target)}
    quotient = {int(row) for row in csc["binary"]["quotient_unit_rows"]}
    complement = [row for row in range(len(target)) if row not in quotient]
    complement_lookup = {ambient: local for local, ambient in enumerate(complement)}
    selected = [
        int(column)
        for column in factor["exact_coordinate_identity"][
            "selected_original_Jacobian_columns"
        ]
    ]
    descriptors = family_update.selected_column_data(macaulay, selected)
    dimension = len(complement)

    rows = array("i")
    columns = array("i")
    variable_rows = array("i")
    variable_columns = array("i")
    variable_weights = bytearray()
    for column, descriptor in enumerate(descriptors):
        for ambient_row, coefficients in oracle.exact_column(
            descriptor, generators0, target_lookup
        ).items():
            row = complement_lookup.get(ambient_row)
            if row is None:
                continue
            rows.append(row)
            columns.append(column)
            weight = sum(value != 0 for value in coefficients[1:])
            if weight:
                variable_rows.append(row)
                variable_columns.append(column)
                variable_weights.append(weight)

    row_values = np.frombuffer(rows, dtype=np.int32)
    column_values = np.frombuffer(columns, dtype=np.int32)
    pattern = sparse.csr_matrix(
        (np.ones(row_values.size, dtype=np.uint8), (row_values, column_values)),
        shape=(dimension, dimension),
    )
    pattern.sum_duplicates()
    pattern.data[:] = 1
    matching = maximum_bipartite_matching(pattern, perm_type="column").astype(np.int32)
    require(np.count_nonzero(matching < 0) == 0, "replay perfect matching")

    edge_rows, edge_columns = pattern.nonzero()
    graph_sources = matching[edge_rows]
    graph_targets = edge_columns.astype(np.int32)
    graph = sparse.csr_matrix(
        (np.ones(graph_sources.size, dtype=np.uint8), (graph_sources, graph_targets)),
        shape=(dimension, dimension),
    )
    component_count, component_by_column = connected_components(
        graph, directed=True, connection="strong"
    )
    component_by_column = component_by_column.astype(np.int32)
    component_by_row = component_by_column[matching]
    component_sizes = np.bincount(
        component_by_column, minlength=component_count
    ).astype(np.int32)
    order = topological_order(
        component_count,
        component_by_column[graph_sources],
        component_by_column[graph_targets],
    )
    positions = np.empty(component_count, dtype=np.int32)
    for position, component in enumerate(order):
        positions[component] = position
    backward = int(
        np.count_nonzero(
            positions[component_by_column[graph_sources]]
            > positions[component_by_column[graph_targets]]
        )
    )

    core = int(np.argmax(component_sizes))
    gamma_rows = np.frombuffer(variable_rows, dtype=np.int32)
    gamma_columns = np.frombuffer(variable_columns, dtype=np.int32)
    gamma_weights = np.frombuffer(variable_weights, dtype=np.uint8)
    internal = (
        (component_by_row[gamma_rows] == core)
        & (component_by_column[gamma_columns] == core)
    )
    active_rows = np.unique(gamma_rows[internal]).astype(np.int32)
    active_columns = np.unique(gamma_columns[internal]).astype(np.int32)
    all_active_rows = np.unique(gamma_rows).astype(np.int32)
    histogram = Counter(int(value) for value in component_sizes)
    return {
        "ambient_dimension": len(target),
        "quotient_identity_dimension": len(quotient),
        "complement_shape": [dimension, dimension],
        "exact_pattern_nonzero_entries": int(pattern.nnz),
        "perfect_matching_size": int(np.count_nonzero(matching >= 0)),
        "irreducible_components": int(component_count),
        "largest_component_dimension": int(component_sizes[core]),
        "largest_component_label": core,
        "largest_component_topological_position": int(positions[core]),
        "largest_component_sizes": [
            int(value) for value in sorted(component_sizes.tolist(), reverse=True)[:20]
        ],
        "singleton_components": int(histogram[1]),
        "non_singleton_components": int(component_count - histogram[1]),
        "backward_pattern_edges": backward,
        "gamma_dependent_entries": int(gamma_rows.size),
        "gamma_dependent_rows_all_components": int(all_active_rows.size),
        "gamma_dependent_singleton_rows": int(
            np.count_nonzero(component_sizes[component_by_row[all_active_rows]] == 1)
        ),
        "core_gamma_dependent_rows": int(active_rows.size),
        "core_gamma_dependent_columns": int(active_columns.size),
        "core_combined_power_update_shape": [
            int(component_sizes[core]),
            5 * int(active_columns.size),
        ],
        "core_combined_power_update_nonzero_entries": int(
            gamma_weights[internal].sum(dtype=np.int64)
        ),
        "hashes": {
            "exact_complement_pattern_sha256": pattern_hash(pattern),
            "matching_column_by_row_sha256": array_hash(matching, "<i4"),
            "component_by_column_sha256": array_hash(component_by_column, "<i4"),
            "component_by_row_sha256": array_hash(component_by_row, "<i4"),
            "component_sizes_sha256": array_hash(component_sizes, "<i4"),
            "topological_component_order_sha256": array_hash(
                np.asarray(order, dtype=np.int32), "<i4"
            ),
            "active_core_rows_sha256": array_hash(active_rows, "<i4"),
            "active_core_columns_sha256": array_hash(active_columns, "<i4"),
        },
    }


def main() -> None:
    packet = load(PACKET)
    require(packet["schema"] == "MTTQ79Eta9CharacteristicZeroDetectingMeridianTransport.v1", "schema")
    require(packet["controlling_blocker"] == "B.ETA9.01", "blocker")
    require(all(packet["checks"].values()), "declared checks")
    for dependency in packet["inputs"].values():
        path = ROOT / dependency["path"]
        require(path.is_file(), f"input exists: {path.name}")
        require(sha256(path) == dependency["sha256"], f"input hash: {path.name}")

    replay = replay_h02()
    require(
        replay == packet["H02_exact_DM_and_Woodbury_reduction"],
        "independent H02 DM/Woodbury replay",
    )
    require(replay["complement_shape"] == [42458, 42458], "H02 complement")
    require(replay["irreducible_components"] == 17692, "H02 components")
    require(replay["largest_component_dimension"] == 24767, "H02 core")
    require(replay["singleton_components"] == 17691, "H02 scalar blocks")
    require(replay["core_gamma_dependent_rows"] == 15158, "H02 reduced rows")

    archimedean = load(ROOT / packet["inputs"]["Archimedean_embedding_boundary"]["path"])
    anchors = packet["all_embedding_integer_anchor_certificate"]["anchors"]
    independently_selected = []
    for embedding in archimedean["field"]["certified_embeddings"]:
        interval = embedding["gamma_real_interval_decimal"]
        midpoint = (Decimal(interval[0]) + Decimal(interval[1])) / 2
        quotient = ((midpoint - Decimal(3)) / Decimal(11)).to_integral_value(
            rounding=ROUND_HALF_EVEN
        )
        independently_selected.append(3 + 11 * int(quotient))
    require(independently_selected == [-19, -8, 3, 3, 3, 3], "embedding anchors")
    require(
        [row["integer_anchor"] for row in anchors] == independently_selected,
        "packet anchor replay",
    )
    require(all(row["anchor_mod11"] == 3 for row in anchors), "anchor residues")

    chart = load(ROOT / packet["inputs"]["characteristic_zero_three_block_chart"]["path"])
    require(chart["block_audits"]["H02"]["selected_minor_determinant_mod11"] == 2, "anchor determinant residue")
    require(chart["block_audits"]["H02"]["exact_C0_is_invertible_over_Q_gamma"] is True, "generic H02 invertibility")
    require(packet["readiness"]["detecting_meridian_word"].startswith("OPEN"), "meridian remains open")
    require(packet["readiness"]["integral_rank1509_representative"] == "OPEN", "integral representative remains open")
    require(packet["readiness"]["certified_248_coordinate_period_image"] == "OPEN", "period image remains open")
    require(packet["readiness"]["physical_Deligne_row"] == "OPEN", "Deligne row remains open")
    require(packet["readiness"]["U_eta9_or_nonzero_obstruction"] == "OPEN", "final decision remains open")
    require(packet["readiness"]["B_ETA9_01"] == "OPEN", "blocker remains open")

    identity = packet["construction_identity"]["payload"]
    expected_hash = hashlib.sha256(
        json.dumps(identity, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("ascii")
    ).hexdigest()
    require(expected_hash == packet["construction_identity"]["sha256"], "construction identity")
    print("Q79_ETA9_CHARACTERISTIC_ZERO_DETECTING_MERIDIAN_TRANSPORT_REPLAY_PASS")
    print("H02=42458 DM=17692 core=24767 kernel=15158; meridian/period/Deligne=OPEN")


if __name__ == "__main__":
    main()
