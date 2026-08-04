from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parent
PRIME = 11
FACTOR_MAGIC = b"MTTFAC1\0"


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while block := handle.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def record(path: Path) -> dict[str, object]:
    return {"path": str(path), "sha256": sha256(path), "bytes": path.stat().st_size}


def parse_scalars(path: Path) -> dict[str, str]:
    scalars: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line == "END_CERTIFICATE":
            continue
        label, value = line.split(" ", 1)
        scalars[label] = value
    return scalars


def take_array(
    raw: np.memmap,
    offset: int,
    dtype: str,
    count: int,
) -> tuple[np.ndarray, int]:
    array = np.ndarray(shape=(count,), dtype=dtype, buffer=raw, offset=offset)
    return array, offset + array.nbytes


def read_factorization(path: Path) -> tuple[dict[str, int], dict[str, np.ndarray]]:
    raw = np.memmap(path, dtype=np.uint8, mode="r")
    require(bytes(raw[:8]) == FACTOR_MAGIC, "factorization magic")
    offset = 8
    header_array, offset = take_array(raw, offset, "<u8", 8)
    labels = (
        "rows",
        "matrix_columns",
        "matrix_nonzeros",
        "quotient_units",
        "certified_image_rank",
        "selected_columns",
        "basis_terms",
        "transcript_terms",
    )
    header = {label: int(value) for label, value in zip(labels, header_array, strict=True)}
    rows = header["rows"]
    selected = header["selected_columns"]
    basis_terms = header["basis_terms"]
    transcript_terms = header["transcript_terms"]
    arrays: dict[str, np.ndarray] = {}
    arrays["selected_augmented_columns"], offset = take_array(raw, offset, "<u4", selected)
    arrays["pivot_original_rows"], offset = take_array(raw, offset, "<u4", selected)
    arrays["pivot_priority_rows"], offset = take_array(raw, offset, "<u4", selected)
    arrays["pivot_coefficients"], offset = take_array(raw, offset, "u1", selected)
    arrays["original_to_priority"], offset = take_array(raw, offset, "<u4", rows)
    arrays["basis_indptr"], offset = take_array(raw, offset, "<u8", selected + 1)
    arrays["basis_rows"], offset = take_array(raw, offset, "<u4", basis_terms)
    arrays["basis_data"], offset = take_array(raw, offset, "u1", basis_terms)
    arrays["transcript_indptr"], offset = take_array(raw, offset, "<u8", selected + 1)
    arrays["transcript_basis_indices"], offset = take_array(
        raw, offset, "<u4", transcript_terms
    )
    arrays["transcript_data"], offset = take_array(raw, offset, "u1", transcript_terms)
    require(offset == raw.size, "factorization byte count")
    arrays["_raw"] = raw
    return header, arrays


def permutation_sign_mod11(permutation: np.ndarray) -> int:
    size = permutation.size
    visited = np.zeros(size, dtype=np.bool_)
    cycles = 0
    for start in range(size):
        if visited[start]:
            continue
        cycles += 1
        current = start
        while not visited[current]:
            visited[current] = True
            current = int(permutation[current])
    return 1 if (size - cycles) % 2 == 0 else PRIME - 1


def validate(target: str) -> dict[str, object]:
    csc_packet_path = ROOT / f"q79_eta9_original_jacobian_macaulay_{target}_csc.packet.json"
    csc_packet = json.loads(csc_packet_path.read_text(encoding="utf-8"))
    require(all(csc_packet["checks"].values()), "CSC packet checks")
    csc_path = Path(csc_packet["binary"]["path"])
    require(sha256(csc_path) == csc_packet["binary"]["sha256"], "CSC hash")

    exact_path = ROOT / f"q79_eta9_original_jacobian_coordinate_factorization_{target}.exact.out"
    factor_path = ROOT / f"q79_eta9_original_jacobian_coordinate_factorization_{target}.factor.bin"
    exact = parse_scalars(exact_path)
    header, arrays = read_factorization(factor_path)

    require(
        exact["SCHEMA"]
        == "MTTQ79Eta9OriginalJacobianCoordinateFactorizationExactOutput.v1",
        "exact-output schema",
    )
    require(
        exact["STATUS"] == "EXACT_GF11_FULL_AUGMENTED_COORDINATE_FACTORIZATION_FOUND",
        "exact-output status",
    )
    require(int(exact["FIELD_PRIME"]) == PRIME, "field prime")
    scalar_labels = {
        "ROWS": "rows",
        "MATRIX_COLUMNS": "matrix_columns",
        "MATRIX_NONZEROS": "matrix_nonzeros",
        "QUOTIENT_UNIT_COLUMNS": "quotient_units",
        "CERTIFIED_JACOBIAN_IMAGE_RANK": "certified_image_rank",
        "AUGMENTED_RANK": "selected_columns",
        "MINOR_SIZE": "selected_columns",
        "BASIS_TERMS": "basis_terms",
        "TRANSCRIPT_TERMS": "transcript_terms",
    }
    for scalar_label, header_label in scalar_labels.items():
        require(int(exact[scalar_label]) == header[header_label], scalar_label)

    rows = header["rows"]
    quotient_units = header["quotient_units"]
    image_rank = header["certified_image_rank"]
    require(quotient_units + image_rank == rows, "rank complement")
    require(header["selected_columns"] == rows, "square selected coordinate system")

    selected = arrays["selected_augmented_columns"]
    pivot_original = arrays["pivot_original_rows"]
    pivot_priority = arrays["pivot_priority_rows"]
    pivot_coefficients = arrays["pivot_coefficients"]
    original_to_priority = arrays["original_to_priority"]
    require(
        np.array_equal(selected[:quotient_units], np.arange(quotient_units, dtype=np.uint32)),
        "all quotient units selected first",
    )
    selected_matrix_columns = selected[quotient_units:].astype(np.int64) - quotient_units
    require(selected_matrix_columns.size == image_rank, "selected image-column count")
    require(
        np.all((selected_matrix_columns >= 0) & (selected_matrix_columns < header["matrix_columns"])),
        "selected image-column bounds",
    )
    require(np.unique(selected).size == rows, "selected columns distinct")
    require(np.array_equal(np.sort(pivot_original), np.arange(rows)), "original pivots permute rows")
    require(np.array_equal(np.sort(pivot_priority), np.arange(rows)), "priority pivots permute rows")
    require(
        np.array_equal(np.sort(original_to_priority), np.arange(rows)),
        "row-priority map is a permutation",
    )
    require(
        np.array_equal(original_to_priority[pivot_original], pivot_priority),
        "original and priority pivots agree",
    )
    require(np.all((pivot_coefficients > 0) & (pivot_coefficients < PRIME)), "nonzero pivots")

    basis_indptr = arrays["basis_indptr"]
    basis_rows = arrays["basis_rows"]
    basis_data = arrays["basis_data"]
    require(basis_indptr[0] == 0 and basis_indptr[-1] == basis_rows.size, "basis pointers")
    require(np.all(basis_indptr[:-1] < basis_indptr[1:]), "nonempty basis columns")
    require(np.all((basis_data > 0) & (basis_data < PRIME)), "basis GF11 data")
    basis_first = basis_indptr[:-1].astype(np.int64)
    require(np.array_equal(basis_rows[basis_first], pivot_priority), "basis leading rows")
    require(np.all(basis_data[basis_first] == 1), "monic basis pivots")
    for column in range(rows):
        start = int(basis_indptr[column])
        stop = int(basis_indptr[column + 1])
        require(np.all(basis_rows[start:stop] >= pivot_priority[column]), "basis echelon support")
        require(
            stop - start == 1 or np.all(basis_rows[start : stop - 1] < basis_rows[start + 1 : stop]),
            "strictly increasing basis rows",
        )

    transcript_indptr = arrays["transcript_indptr"]
    transcript_indices = arrays["transcript_basis_indices"]
    transcript_data = arrays["transcript_data"]
    require(
        transcript_indptr[0] == 0 and transcript_indptr[-1] == transcript_indices.size,
        "transcript pointers",
    )
    require(np.all(transcript_indptr[:-1] <= transcript_indptr[1:]), "transcript monotonicity")
    require(np.all((transcript_data > 0) & (transcript_data < PRIME)), "transcript GF11 data")
    transcript_lengths = np.diff(transcript_indptr).astype(np.int64)
    transcript_columns = np.repeat(np.arange(rows, dtype=np.int32), transcript_lengths)
    require(np.all(transcript_indices < transcript_columns), "strictly prior transcript pivots")

    basis = sparse.csc_matrix(
        (
            basis_data.astype(np.int32),
            basis_rows,
            basis_indptr.astype(np.int64),
        ),
        shape=(rows, rows),
    )
    relation = sparse.coo_matrix(
        (
            np.concatenate([transcript_data.astype(np.int32), pivot_coefficients.astype(np.int32)]),
            (
                np.concatenate([transcript_indices, np.arange(rows, dtype=np.int32)]),
                np.concatenate([transcript_columns, np.arange(rows, dtype=np.int32)]),
            ),
        ),
        shape=(rows, rows),
    ).tocsc()

    matrix_path = Path(csc_packet["inputs"]["Macaulay_matrix"]["path"])
    matrix = sparse.load_npz(matrix_path).tocsc().astype(np.int32)
    quotient_rows = np.asarray(csc_packet["binary"]["quotient_unit_rows"], dtype=np.int32)
    quotient_matrix = sparse.csc_matrix(
        (
            np.ones(quotient_units, dtype=np.int32),
            (quotient_rows, np.arange(quotient_units, dtype=np.int32)),
        ),
        shape=(rows, quotient_units),
    )
    selected_source = sparse.hstack(
        [quotient_matrix, matrix[:, selected_matrix_columns]], format="csc"
    )
    priority_to_original = np.argsort(original_to_priority)
    selected_source_priority = selected_source[priority_to_original, :]
    reconstructed = (basis @ relation).tocsc()
    reconstructed.data %= PRIME
    reconstructed.eliminate_zeros()
    residual = (reconstructed - selected_source_priority).tocsc()
    residual.data %= PRIME
    residual.eliminate_zeros()
    require(residual.nnz == 0, "exact factorization identity B R = C")

    determinant = permutation_sign_mod11(pivot_original)
    for value in pivot_coefficients:
        determinant = determinant * int(value) % PRIME
    require(determinant == int(exact["MINOR_DETERMINANT_MOD11"]) != 0, "minor determinant")

    processed_columns = int(exact["PROCESSED_MATRIX_COLUMNS"])
    require(exact["COLUMN_ORDER"] == "nnz", "column order")
    column_sizes = np.diff(matrix.indptr)
    schedule = sorted(
        range(matrix.shape[1]), key=lambda column: (int(column_sizes[column]), column)
    )
    require(
        set(int(column) for column in selected_matrix_columns).issubset(schedule[:processed_columns]),
        "selected columns in processed schedule prefix",
    )

    checks = {
        "all_B103_standard_monomial_quotient_units_are_selected": True,
        "the_selected_original_Jacobian_columns_have_the_certified_image_rank": True,
        "the_selected_augmented_coordinate_system_is_square": True,
        "the_pivot_rows_are_an_exact_permutation_of_all_ambient_rows": True,
        "the_normalized_basis_is_in_sparse_echelon_form": True,
        "the_relation_transcript_is_strictly_triangular_with_nonzero_diagonal": True,
        "the_exact_sparse_identity_B_times_R_equals_the_selected_source_matrix": True,
        "the_selected_minor_determinant_is_independently_recomputed_and_nonzero": True,
        "the_factorization_is_a_reusable_exact_coordinate_solver_over_GF11": True,
        "no_characteristic_zero_connection_monodromy_or_period_is_inferred": True,
    }
    return {
        "schema": "MTTQ79Eta9OriginalJacobianCoordinateFactorization.v1",
        "date": "2026-07-22",
        "status": "EXACT_GF11_B103_QUOTIENT_PLUS_ORIGINAL_JACOBIAN_COORDINATE_SOLVER_CERTIFIED",
        "target_Hodge_block": target,
        "field": "GF(11)",
        "inputs": {
            "CSC_packet": record(csc_packet_path),
            "CSC_binary": record(csc_path),
            "exact_output": record(exact_path),
            "factorization_binary": record(factor_path),
            "factorizer_source": record(
                ROOT / "compute_q79_eta9_original_jacobian_coordinate_factorization.cpp"
            ),
            "factorizer_executable": record(
                ROOT / "compute_q79_eta9_original_jacobian_coordinate_factorization"
            ),
        },
        "dimensions": {
            "ambient_rows": rows,
            "B103_quotient_units": quotient_units,
            "selected_original_Jacobian_image_columns": image_rank,
            "available_original_Jacobian_columns": header["matrix_columns"],
            "processed_original_Jacobian_columns": processed_columns,
            "basis_terms": header["basis_terms"],
            "triangular_transcript_terms": header["transcript_terms"],
        },
        "exact_coordinate_identity": {
            "formula": "C_selected = B_echelon R_triangular over GF(11)",
            "residual_nonzeros": int(residual.nnz),
            "minor_determinant_mod11": determinant,
            "selected_augmented_columns": selected.tolist(),
            "selected_original_Jacobian_columns": selected_matrix_columns.tolist(),
        },
        "coordinate_solver_contract": {
            "decompose": (
                "For any ambient coefficient vector y, solve B g=y by echelon reduction, "
                "then solve R x=g by exact back substitution."
            ),
            "quotient_coordinates": f"the first {quotient_units} entries of x",
            "Jacobian_preimage_coordinates": f"the final {image_rank} entries of x",
            "uniqueness": "follows from the nonzero selected minor determinant",
        },
        "checks": checks,
        "theorem": {
            "name": f"q79 eta9 {target} B103-Jacobian Coordinate Decomposition Theorem",
            "statement": (
                f"At the selected GF(11) good fiber in Cox degree {target}, the B103 "
                "standard-monomial representatives and a selected basis of the original "
                "Jacobian image form a direct-sum coordinate basis of the complete ambient "
                "homogeneous component."
            ),
            "tier": "exact finite-field computational theorem",
        },
        "guardrails": [
            "This certifies exact selected-good-fiber coordinates, not characteristic-zero transport.",
            "The factorization selects image columns algorithmically; it does not add source parameters.",
            "Connection, monodromy and period claims require the recursive return execution.",
        ],
        "next_required_object": (
            "Use this exact coordinate solver on the recursively returned pole numerator rows and "
            "retain both quotient coordinates and lower-pole Jacobian preimages."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", choices=("H02", "H11", "H20"), required=True)
    args = parser.parse_args()
    packet = validate(args.target)
    require(all(packet["checks"].values()), "factorization checks")
    output = ROOT / f"q79_eta9_original_jacobian_coordinate_factorization_{args.target}.packet.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(f"Q79_ETA9_ORIGINAL_JACOBIAN_COORDINATE_FACTORIZATION_{args.target}_BIND_PASS")
    print(f"packet_sha256={sha256(output)}")


if __name__ == "__main__":
    main()
