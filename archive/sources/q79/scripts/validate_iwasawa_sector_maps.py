"""Validate sector projection maps for Iwasawa rho_E data.

This validator covers the finite-projector format used by the current
proof-repro contracts: each SM slot supplies a Hermitian idempotent projector
on the rank-three family fiber and, when rho_E data are supplied, the projector
must be invariant under the boundary face transitions.

Exit codes:
  0: complete sector-map candidate passes implemented checks
  1: complete candidate fails a mathematical/schema check
  2: candidate is incomplete/open rather than mathematically failed
"""

from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path
from typing import Any


GENERATORS = ("g1", "g2", "g3", "g4", "g5", "g6")
FAMILY_SECTORS = ("Q", "u", "d", "L", "e", "N")
SECTORS = FAMILY_SECTORS + ("H",)
EXPECTED_DIMENSION = {sector: 3 for sector in FAMILY_SECTORS} | {"H": 1}
EXPECTED_KIND = {sector: "family" for sector in FAMILY_SECTORS} | {
    "H": "single_higgs_carrier"
}
TOL = 1e-9

Node = tuple[int, int, int, int, int, int]
Matrix = list[list[complex]]


class IncompleteData(ValueError):
    """Raised when a required sector-map or rho_E value is still open."""


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


def matrix_rank(matrix: Matrix) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = None
        for row in range(rank, rows):
            if abs(work[row][col]) > TOL:
                pivot = row
                break
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][col]
        work[rank] = [value / scale for value in work[rank]]
        for row in range(rows):
            if row == rank or abs(work[row][col]) <= TOL:
                continue
            factor = work[row][col]
            work[row] = [
                work[row][idx] - factor * work[rank][idx]
                for idx in range(cols)
            ]
        rank += 1
        if rank == rows:
            break
    return rank


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


class RhoResolver:
    def __init__(self, generator_data: dict[str, Any]) -> None:
        self.generator_data = generator_data
        self.seen: dict[tuple[str, Node], Matrix] = {}

    def matrix(self, generator: str, target: Node) -> Matrix:
        key = (generator, target)
        if key in self.seen:
            return self.seen[key]

        entry = self.generator_data.get(generator)
        if entry is None:
            raise IncompleteData(f"MISSING generator entry: {generator}")
        matrix = parse_matrix(select_matrix_entry(entry, target, f"{generator} matrix"))
        self.seen[key] = matrix
        return matrix


def parse_sector_projector(sector: str, entry: Any) -> tuple[int, str, Matrix]:
    if entry is None:
        raise IncompleteData(f"MISSING sector projection entry: {sector}")
    if not isinstance(entry, dict):
        raise ValueError(f"sector {sector} entry must be an object")

    dimension = entry.get("dimension", entry.get("required_kernel_dimension"))
    kind = entry.get("kind")
    projector_entry = entry.get("projector", entry.get("projection_matrix", entry))

    if dimension != EXPECTED_DIMENSION[sector]:
        raise ValueError(
            f"sector {sector} dimension {dimension!r} != expected "
            f"{EXPECTED_DIMENSION[sector]}"
        )
    if kind != EXPECTED_KIND[sector]:
        raise ValueError(
            f"sector {sector} kind {kind!r} != expected {EXPECTED_KIND[sector]!r}"
        )
    return int(dimension), str(kind), parse_matrix(projector_entry)


def load_candidate(
    path: Path,
) -> tuple[int, str, int | None, RhoResolver | None, dict[str, Matrix] | None]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("rank") != 3:
        return 2, "MISSING rank=3 bundle declaration", None, None, None

    sector_maps = data.get("sector_projection_maps")
    if not isinstance(sector_maps, dict):
        return 2, "MISSING sector_projection_maps object", None, None, None

    missing_sectors = [sector for sector in SECTORS if sector_maps.get(sector) is None]
    if missing_sectors:
        return (
            2,
            f"MISSING sector projection entries: {', '.join(missing_sectors)}",
            None,
            None,
            None,
        )

    generator_data = data.get("generator_data")
    if not isinstance(generator_data, dict):
        return 2, "MISSING generator_data object", None, None, None

    missing_generators = [
        generator for generator in GENERATORS if generator_data.get(generator) is None
    ]
    if missing_generators:
        return (
            2,
            f"MISSING generator entries: {', '.join(missing_generators)}",
            None,
            None,
            None,
        )

    try:
        n = validate_mesh_n(data.get("mesh_N"))
        projectors = {
            sector: parse_sector_projector(sector, sector_maps[sector])[2]
            for sector in SECTORS
        }
    except IncompleteData as exc:
        return 2, str(exc), None, None, None

    return (
        0,
        f"loaded finite mesh_N={n} rho_E and sector projection data",
        n,
        RhoResolver(generator_data),
        projectors,
    )


def validate_projectors(projectors: dict[str, Matrix]) -> list[str]:
    failures: list[str] = []
    for sector, projector in projectors.items():
        if max_abs_diff(projector, adjoint(projector)) > TOL:
            failures.append(f"sector {sector} projector is not Hermitian")
        if max_abs_diff(matmul(projector, projector), projector) > TOL:
            failures.append(f"sector {sector} projector is not idempotent")
        rank = matrix_rank(projector)
        expected = EXPECTED_DIMENSION[sector]
        if rank != expected:
            failures.append(f"sector {sector} projector rank {rank} != dimension {expected}")
    return failures


def validate_rho_invariance(
    n: int,
    rho: RhoResolver,
    projectors: dict[str, Matrix],
) -> list[str]:
    failures: list[str] = []
    for source in all_closed_nodes(n):
        for generator, target in boundary_targets(source, n):
            rho_matrix = rho.matrix(generator, target)
            for sector, projector in projectors.items():
                diff = max_abs_diff(
                    matmul(rho_matrix, projector),
                    matmul(projector, rho_matrix),
                )
                if diff > TOL:
                    failures.append(
                        f"sector {sector} not rho_E-invariant at "
                        f"{node_key(source)} --{generator}--> {node_key(target)} "
                        f"max_abs_diff={diff:.3e}"
                    )
    return failures


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_iwasawa_sector_maps.py <rhoE-sector-data.json>")
        return 1

    path = Path(argv[1])
    try:
        code, message, n, rho, projectors = load_candidate(path)
        print(message)
        if code != 0:
            return code
        assert n is not None
        assert rho is not None
        assert projectors is not None
        failures = validate_projectors(projectors)
        failures.extend(validate_rho_invariance(n, rho, projectors))
    except IncompleteData as exc:
        print(str(exc))
        return 2
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID sector projection data: {exc}")
        return 1

    if failures:
        print("sector projection validation FAIL")
        for failure in failures[:50]:
            print(f"- {failure}")
        if len(failures) > 50:
            print(f"- ... {len(failures) - 50} more failures")
        return 1

    print("sector projection validation PASS")
    print("sector projectors are well-formed and invariant under supplied rho_E data")
    print("selected origin, D_E action, and overlap matrices remain separate checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
