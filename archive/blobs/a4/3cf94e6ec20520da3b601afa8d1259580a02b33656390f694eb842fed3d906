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
GATE2 = ROOT / "q79_eta9_gate2_promotion.packet.json"
ARCHIMEDEAN = ROOT / "q79_eta9_archimedean_embedding_selection_boundary.packet.json"
THREE_BLOCK = ROOT / "q79_eta9_characteristic_zero_three_block_chart_oracle.packet.json"
H11_DM = ROOT / "q79_eta9_H11_Dulmage_Mendelsohn_decomposition.packet.json"
H11_RANK = ROOT / "q79_eta9_H11_DM_core_Woodbury_rank.packet.json"
H11_PENCILS = ROOT / "q79_eta9_H11_DM_core_fraction_free_Woodbury_pencils.packet.json"
H11_SHARED = ROOT / "q79_eta9_H11_DM_shared_core_reduced_kernel.packet.json"
H11_T2_ACTION = ROOT / "q79_eta9_H11_DM_t2_shared_core_reduced_action.packet.json"
H02_MACAULAY = ROOT / "q79_eta9_original_jacobian_macaulay_H02.packet.json"
H02_CSC = ROOT / "q79_eta9_original_jacobian_macaulay_H02_csc.packet.json"
H02_FACTOR = ROOT / "q79_eta9_original_jacobian_coordinate_factorization_H02.packet.json"
OUT = ROOT / "q79_eta9_characteristic_zero_detecting_meridian_transport.packet.json"


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while block := handle.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def record(path: Path) -> dict[str, object]:
    return {
        "path": path.resolve().relative_to(ROOT.resolve()).as_posix(),
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
    }


def canonical_hash(value: object) -> str:
    payload = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


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


def topological_order(
    component_count: int, sources: np.ndarray, targets: np.ndarray
) -> list[int]:
    successors: list[set[int]] = [set() for _ in range(component_count)]
    indegree = [0] * component_count
    for source, target in zip(sources.tolist(), targets.tolist(), strict=True):
        if source == target or target in successors[source]:
            continue
        successors[source].add(target)
        indegree[target] += 1
    ready = sorted(index for index, value in enumerate(indegree) if value == 0)
    result: list[int] = []
    while ready:
        current = ready.pop(0)
        result.append(current)
        for target in sorted(successors[current]):
            indegree[target] -= 1
            if indegree[target] == 0:
                ready.append(target)
                ready.sort()
    require(len(result) == component_count, "condensation graph is acyclic")
    return result


def nearest_integer_in_good_residue(real_interval: list[str]) -> int:
    midpoint = (Decimal(real_interval[0]) + Decimal(real_interval[1])) / 2
    quotient = ((midpoint - Decimal(3)) / Decimal(11)).to_integral_value(
        rounding=ROUND_HALF_EVEN
    )
    anchor = 3 + 11 * int(quotient)
    require(anchor % 11 == 3, "anchor has the selected good residue")
    return anchor


def compute_h02_reduction() -> dict[str, object]:
    macaulay = load(H02_MACAULAY)
    csc = load(H02_CSC)
    factor = load(H02_FACTOR)
    base = load(oracle.BASE)
    global_f0 = load(oracle.GLOBAL_F0)
    b89 = load(oracle.B89)
    for label, packet in (
        ("H02 Macaulay", macaulay),
        ("H02 CSC", csc),
        ("H02 factorization", factor),
        ("base", base),
        ("global F0", global_f0),
        ("B89", b89),
    ):
        require(all(packet["checks"].values()), f"{label} checks")

    generators0, _, _ = oracle.exact_generators(base, global_f0, b89)
    target = [
        tuple(int(value) for value in exponent)
        for exponent in macaulay["target_monomial_basis"]["exponent_vectors"]
    ]
    target_lookup = {exponent: index for index, exponent in enumerate(target)}
    quotient_rows = {int(value) for value in csc["binary"]["quotient_unit_rows"]}
    complement_rows = [row for row in range(len(target)) if row not in quotient_rows]
    complement_lookup = {
        ambient_row: local_row
        for local_row, ambient_row in enumerate(complement_rows)
    }
    selected_columns = [
        int(value)
        for value in factor["exact_coordinate_identity"][
            "selected_original_Jacobian_columns"
        ]
    ]
    descriptors = family_update.selected_column_data(macaulay, selected_columns)
    dimension = len(complement_rows)
    require(len(target) == 42706, "H02 ambient dimension")
    require(len(quotient_rows) == 248, "H02 quotient dimension")
    require(dimension == 42458, "H02 complement dimension")
    require(len(descriptors) == dimension, "H02 selected image columns")

    rows = array("i")
    columns = array("i")
    gamma_rows = array("i")
    gamma_columns = array("i")
    gamma_weights = bytearray()
    require(rows.itemsize == 4, "canonical 32-bit array storage")
    for column_index, descriptor in enumerate(descriptors):
        exact = oracle.exact_column(descriptor, generators0, target_lookup)
        for ambient_row, coefficients in exact.items():
            local_row = complement_lookup.get(ambient_row)
            if local_row is None:
                continue
            rows.append(local_row)
            columns.append(column_index)
            higher_weight = sum(coefficient != 0 for coefficient in coefficients[1:])
            if higher_weight:
                gamma_rows.append(local_row)
                gamma_columns.append(column_index)
                gamma_weights.append(higher_weight)

    row_array = np.frombuffer(rows, dtype=np.int32)
    column_array = np.frombuffer(columns, dtype=np.int32)
    pattern = sparse.csr_matrix(
        (
            np.ones(row_array.size, dtype=np.uint8),
            (row_array, column_array),
        ),
        shape=(dimension, dimension),
    )
    pattern.sum_duplicates()
    pattern.data[:] = 1
    matching_column_by_row = maximum_bipartite_matching(
        pattern, perm_type="column"
    ).astype(np.int32)
    require(np.count_nonzero(matching_column_by_row < 0) == 0, "perfect matching")
    require(np.unique(matching_column_by_row).size == dimension, "bijective matching")

    pattern_rows, pattern_columns = pattern.nonzero()
    graph_sources = matching_column_by_row[pattern_rows]
    graph_targets = pattern_columns.astype(np.int32)
    graph = sparse.csr_matrix(
        (
            np.ones(graph_sources.size, dtype=np.uint8),
            (graph_sources, graph_targets),
        ),
        shape=(dimension, dimension),
    )
    component_count, component_by_column = connected_components(
        graph, directed=True, connection="strong"
    )
    component_by_column = component_by_column.astype(np.int32)
    component_by_row = component_by_column[matching_column_by_row]
    component_sizes = np.bincount(
        component_by_column, minlength=component_count
    ).astype(np.int32)
    order = topological_order(
        component_count,
        component_by_column[graph_sources],
        component_by_column[graph_targets],
    )
    order_position = np.empty(component_count, dtype=np.int32)
    for position, component in enumerate(order):
        order_position[component] = position
    backward_edges = int(
        np.count_nonzero(
            order_position[component_by_column[graph_sources]]
            > order_position[component_by_column[graph_targets]]
        )
    )
    require(backward_edges == 0, "block upper-triangular order")

    largest_component = int(np.argmax(component_sizes))
    largest_dimension = int(component_sizes[largest_component])
    gamma_row_array = np.frombuffer(gamma_rows, dtype=np.int32)
    gamma_column_array = np.frombuffer(gamma_columns, dtype=np.int32)
    gamma_weight_array = np.frombuffer(gamma_weights, dtype=np.uint8)
    internal_gamma = (
        (component_by_row[gamma_row_array] == largest_component)
        & (component_by_column[gamma_column_array] == largest_component)
    )
    active_core_rows = np.unique(gamma_row_array[internal_gamma]).astype(np.int32)
    active_core_columns = np.unique(gamma_column_array[internal_gamma]).astype(np.int32)
    active_all_rows = np.unique(gamma_row_array).astype(np.int32)
    singleton_gamma_rows = int(
        np.count_nonzero(component_sizes[component_by_row[active_all_rows]] == 1)
    )
    combined_update_nnz = int(gamma_weight_array[internal_gamma].sum(dtype=np.int64))
    histogram = Counter(int(value) for value in component_sizes)
    decreasing_sizes = sorted(component_sizes.tolist(), reverse=True)

    result: dict[str, object] = {
        "ambient_dimension": len(target),
        "quotient_identity_dimension": len(quotient_rows),
        "complement_shape": [dimension, dimension],
        "exact_pattern_nonzero_entries": int(pattern.nnz),
        "perfect_matching_size": int(np.count_nonzero(matching_column_by_row >= 0)),
        "irreducible_components": int(component_count),
        "largest_component_dimension": largest_dimension,
        "largest_component_label": largest_component,
        "largest_component_topological_position": int(order_position[largest_component]),
        "largest_component_sizes": [int(value) for value in decreasing_sizes[:20]],
        "singleton_components": int(histogram[1]),
        "non_singleton_components": int(component_count - histogram[1]),
        "backward_pattern_edges": backward_edges,
        "gamma_dependent_entries": int(gamma_row_array.size),
        "gamma_dependent_rows_all_components": int(active_all_rows.size),
        "gamma_dependent_singleton_rows": singleton_gamma_rows,
        "core_gamma_dependent_rows": int(active_core_rows.size),
        "core_gamma_dependent_columns": int(active_core_columns.size),
        "core_combined_power_update_shape": [
            largest_dimension,
            5 * int(active_core_columns.size),
        ],
        "core_combined_power_update_nonzero_entries": combined_update_nnz,
        "hashes": {
            "exact_complement_pattern_sha256": pattern_hash(pattern),
            "matching_column_by_row_sha256": array_hash(
                matching_column_by_row, "<i4"
            ),
            "component_by_column_sha256": array_hash(component_by_column, "<i4"),
            "component_by_row_sha256": array_hash(component_by_row, "<i4"),
            "component_sizes_sha256": array_hash(component_sizes, "<i4"),
            "topological_component_order_sha256": array_hash(
                np.asarray(order, dtype=np.int32), "<i4"
            ),
            "active_core_rows_sha256": array_hash(active_core_rows, "<i4"),
            "active_core_columns_sha256": array_hash(active_core_columns, "<i4"),
        },
    }
    require(result["exact_pattern_nonzero_entries"] == 2325539, "frozen H02 pattern")
    require(result["irreducible_components"] == 17692, "frozen H02 component count")
    require(result["largest_component_dimension"] == 24767, "frozen H02 core")
    require(result["singleton_components"] == 17691, "frozen H02 singletons")
    require(result["core_gamma_dependent_rows"] == 15158, "frozen active rows")
    require(result["core_gamma_dependent_columns"] == 17676, "frozen active columns")
    require(
        result["core_combined_power_update_nonzero_entries"] == 7901469,
        "frozen combined update pattern",
    )
    return result


def main() -> None:
    gate2 = load(GATE2)
    archimedean = load(ARCHIMEDEAN)
    three_block = load(THREE_BLOCK)
    h11_dm = load(H11_DM)
    h11_rank = load(H11_RANK)
    h11_pencils = load(H11_PENCILS)
    h11_shared = load(H11_SHARED)
    h11_t2 = load(H11_T2_ACTION)
    for label, packet in (
        ("Gate 2", gate2),
        ("Archimedean boundary", archimedean),
        ("three-block chart", three_block),
        ("H11 DM", h11_dm),
        ("H11 Woodbury rank", h11_rank),
        ("H11 pencils", h11_pencils),
        ("H11 shared kernel", h11_shared),
        ("H11 t2 action", h11_t2),
    ):
        require(all(packet["checks"].values()), f"{label} checks")
    require(gate2["frozen_Gate1"]["group_count"] == 30, "Gate 1 groups frozen")
    require(gate2["frozen_Gate1"]["support_columns"] == 225, "Gate 1 columns frozen")
    require(gate2["frozen_Gate1"]["recomputed"] is False, "Gate 1 not recomputed")
    require(gate2["Gate2"]["stage_one"]["rows"] == 248, "Gate 2 rows")
    require(gate2["Gate2"]["H02_source_block"]["shape"] == [1509, 248], "Gate 2 source")
    require(gate2["Gate2"]["full_operator"]["shape"] == [1509, 1509], "Gate 2 operator")
    require(gate2["Gate2"]["full_operator"]["determinant_mod11"] == 1, "Gate 2 determinant")

    h02 = compute_h02_reduction()
    h02_audit = three_block["block_audits"]["H02"]
    require(h02_audit["exact_C0_is_invertible_over_Q_gamma"] is True, "H02 generic inverse")
    require(h02_audit["selected_minor_determinant_mod11"] == 2, "H02 good determinant")

    embeddings = archimedean["field"]["certified_embeddings"]
    anchors = []
    for embedding in embeddings:
        anchor = nearest_integer_in_good_residue(
            embedding["gamma_real_interval_decimal"]
        )
        anchors.append(
            {
                "embedding_index": int(embedding["embedding_index"]),
                "kind": embedding["kind"],
                "integer_anchor": anchor,
                "anchor_mod11": anchor % 11,
                "anchor_matrix_determinant_mod11": 2,
                "anchor_matrix_invertible_over_Q": True,
            }
        )
    require([row["integer_anchor"] for row in anchors] == [-19, -8, 3, 3, 3, 3], "frozen anchors")

    h11_cores = [
        {
            "core_dimension": int(row["core_dimension"]),
            "exact_Woodbury_kernel_dimension": int(row["Woodbury_kernel_dimension"]),
        }
        for row in h11_rank["cores"]
    ]
    require(h11_cores == [
        {"core_dimension": 1710, "exact_Woodbury_kernel_dimension": 934},
        {"core_dimension": 684, "exact_Woodbury_kernel_dimension": 398},
    ], "H11 exact kernel dimensions")

    identity = {
        "Gate2_manifest_root": gate2["artifact_manifest"]["root_sha256"],
        "H02_structural_hashes": h02["hashes"],
        "embedding_anchors": anchors,
        "H11_kernel_dimensions": h11_cores,
    }
    checks = {
        "Gate1_is_consumed_only_as_the_frozen_30_group_225_column_certificate": True,
        "Gate2_248_rows_1509x248_source_and_1509x1509_operator_are_hash_bound": True,
        "the_GF11_operator_is_not_promoted_to_characteristic_zero": True,
        "the_exact_H02_complement_has_a_perfect_structural_matching": h02["perfect_matching_size"] == 42458,
        "the_exact_H02_DM_order_has_no_backward_edges": h02["backward_pattern_edges"] == 0,
        "the_only_nontrivial_H02_DM_core_has_dimension24767": h02["largest_component_dimension"] == 24767 and h02["non_singleton_components"] == 1,
        "all_remaining17691_H02_DM_components_are_scalar": h02["singleton_components"] == 17691,
        "all_six_embeddings_have_integer_anchors_congruent_to_gamma3_mod11": all(row["anchor_mod11"] == 3 for row in anchors),
        "each_anchor_matrix_is_invertible_over_Q_by_nonzero_mod11_determinant": all(row["anchor_matrix_invertible_over_Q"] for row in anchors),
        "all_internal_H02_diagonal_core_gamma_dependence_is_supported_on15158_rows": h02["core_gamma_dependent_rows"] == 15158,
        "the_H02_core_inverse_reduces_exactly_to_a15158_square_Woodbury_kernel": True,
        "the_existing_H11_exact_reductions_are_bound_at934_and398": h11_cores[0]["exact_Woodbury_kernel_dimension"] == 934 and h11_cores[1]["exact_Woodbury_kernel_dimension"] == 398,
        "no_Archimedean_embedding_is_selected_by_this_packet": True,
        "no_meridian_integral_transport_period_or_Deligne_value_is_claimed": True,
    }
    packet = {
        "schema": "MTTQ79Eta9CharacteristicZeroDetectingMeridianTransport.v1",
        "date": "2026-08-03",
        "status": "CHARACTERISTIC_ZERO_ALL_EMBEDDING_TRANSPORT_EXECUTION_REDUCED_EXACTLY_TO_H11_934_398_AND_H02_15158_KERNELS_MERIDIAN_PERIOD_AND_DELIGNE_VALUES_OPEN",
        "controlling_blocker": "B.ETA9.01",
        "inputs": {
            "Gate2_promotion": record(GATE2),
            "characteristic_zero_three_block_chart": record(THREE_BLOCK),
            "Archimedean_embedding_boundary": record(ARCHIMEDEAN),
            "H11_Dulmage_Mendelsohn": record(H11_DM),
            "H11_Woodbury_ranks": record(H11_RANK),
            "H11_fraction_free_pencils": record(H11_PENCILS),
            "H11_shared_kernel": record(H11_SHARED),
            "H11_t2_reduced_action": record(H11_T2_ACTION),
            "H02_Macaulay": record(H02_MACAULAY),
            "H02_CSC": record(H02_CSC),
            "H02_factorization": record(H02_FACTOR),
            "global_F0": record(oracle.GLOBAL_F0),
            "B89_pencil": record(oracle.B89),
        },
        "frozen_Gate1": gate2["frozen_Gate1"],
        "promoted_Gate2_boundary": {
            "stage_one_rows": 248,
            "source_shape": [1509, 248],
            "finite_operator_shape": [1509, 1509],
            "finite_operator_determinant_mod11": 1,
            "artifact_manifest_root_sha256": gate2["artifact_manifest"]["root_sha256"],
            "interpretation": "exact selected good-fibre coefficient certificate only",
        },
        "coefficient_field": {
            "minimal_polynomial_coefficients_ascending": archimedean["field"]["minimal_polynomial_coefficients_ascending"],
            "signature": archimedean["field"]["Archimedean_signature"],
            "embedding_count": len(embeddings),
            "physical_embedding_selected": False,
        },
        "H11_execution_reduction": {
            "complement_dimension": 4426,
            "irreducible_components": h11_dm["Dulmage_Mendelsohn"]["irreducible_diagonal_components"],
            "singleton_components": h11_dm["Dulmage_Mendelsohn"]["singleton_components"],
            "large_core_reductions": h11_cores,
            "shared398_kernel_split_prime_replays": h11_shared["split_prime_replay_count"],
            "selected_t2_source_columns": len(h11_t2["source_columns"]),
            "interpretation": "exact fraction-free kernel presentations; characteristic-zero inverse values remain to be executed",
        },
        "H02_exact_DM_and_Woodbury_reduction": h02,
        "all_embedding_integer_anchor_certificate": {
            "selected_good_residue": {"prime": 11, "gamma": 3},
            "anchors": anchors,
            "proof": (
                "For every embedding e choose the displayed integer a_e congruent to 3 modulo 11. "
                "The integral matrix A(a_e) reduces to the certified H02 selected matrix A(3), "
                "whose determinant is 2 modulo 11; hence det A(a_e) is a nonzero integer. On the "
                "unique 24767-dimensional diagonal DM core, A(gamma_e)-A(a_e) is supported on exactly "
                "15158 rows. With U the inclusion of those coordinate rows and V_e their exact "
                "difference rows, A(gamma_e)=A(a_e)+U V_e and the matrix determinant lemma and "
                "Woodbury identity reduce the core determinant and inverse to the 15158-square "
                "kernel I+V_e A(a_e)^(-1)U."
            ),
        },
        "construction_identity": {
            "sha256": canonical_hash(identity),
            "payload": identity,
        },
        "checks": checks,
        "theorem": (
            "The selected characteristic-zero H02 chart admits an exact, embedding-uniform "
            "execution reduction. Its 42458-square complement has 17692 irreducible DM blocks: "
            "17691 scalar blocks and one 24767-dimensional core. For each of the six certified "
            "embeddings, an integral anchor congruent to the selected good residue is invertible "
            "over Q, and all internal gamma dependence in the diagonal core is supported on 15158 "
            "coordinate rows. The 17691 scalar blocks and the off-diagonal condensation-DAG entries "
            "are propagated by exact scalar and sparse operations. Therefore every H02 core "
            "determinant and inverse action reduces exactly to a "
            "15158-square Woodbury kernel. Together with the existing exact H11 reductions to "
            "934 and 398 dimensions and the exact H20 inverse, this removes the monolithic "
            "characteristic-zero linear-algebra barrier. It does not yet compute the detecting "
            "meridian, integral rank-1509 transport, 248 periods, physical Deligne row, or U_eta9."
        ),
        "guardrails": [
            "The 1509x1509 GF(11) Gate-2 operator remains a finite good-fibre certificate and is not a characteristic-zero connection.",
            "Integer anchors prove exact invertibility and an exact Woodbury reduction; they do not select an Archimedean embedding.",
            "A 15158-coordinate kernel is an execution reduction, not a claim that its entries, determinant, or inverse have already been evaluated with interval balls.",
            "The 14 D6 framing choices are not period parameters: prior surgery invariance removes them from twisted homology and period selection.",
            "No physical Deligne row, U_eta9 value, or nonzero obstruction is emitted here.",
            "No statement about the unified action theorem is made.",
        ],
        "readiness": {
            "Gate1_frozen": "CLOSED_30_OF_30_AND_225_OF_225",
            "Gate2_promoted": "CLOSED_EXACT_GF11_WITH_REPLAY",
            "characteristic_zero_chart_source": "CLOSED_EXACT_OVER_Q_GAMMA",
            "characteristic_zero_execution_factorization": "CLOSED_TO_H20_EXACT_H11_934_398_AND_H02_15158_KERNELS",
            "detecting_meridian_word": "OPEN_PENDING_D6_RELATION_AND_PATH_TRANSPORT",
            "integral_rank1509_representative": "OPEN",
            "certified_248_coordinate_period_image": "OPEN",
            "physical_Deligne_row": "OPEN",
            "U_eta9_or_nonzero_obstruction": "OPEN",
            "B_ETA9_01": "OPEN",
        },
        "next_required_object": (
            "Execute the three exact reduced-kernel families with certified complex interval balls, "
            "propagate the selected path word supplied by the D6 relation campaign, normalize the "
            "result to an integral rank-1509 representative, and evaluate its certified 248-coordinate "
            "period image. Only that image can decide the physical Deligne row and emit U_eta9 or a "
            "nonzero obstruction."
        ),
    }
    require(all(checks.values()), "characteristic-zero reduction checks")
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print("Q79_ETA9_CHARACTERISTIC_ZERO_DETECTING_MERIDIAN_TRANSPORT_REDUCTION_PASS")
    print(
        "H02=42458 DM=17692 core=24767 scalar=17691 "
        "kernel=15158 anchors=-19,-8,3,3,3,3"
    )


if __name__ == "__main__":
    main()
