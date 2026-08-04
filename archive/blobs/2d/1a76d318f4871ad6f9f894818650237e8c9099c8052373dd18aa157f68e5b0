from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79tracesplitclncarrierandworldinworldbridge"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}_certificate.json"


Matrix = list[list[Fraction]]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode_matrix(matrix: list[list[str]]) -> Matrix:
    return [[Fraction(entry) for entry in row] for row in matrix]


def identity(size: int) -> Matrix:
    return [
        [Fraction(int(row == column)) for column in range(size)]
        for row in range(size)
    ]


def zero(rows: int, columns: int) -> Matrix:
    return [[Fraction(0) for _ in range(columns)] for _ in range(rows)]


def add(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[row][column] + right[row][column] for column in range(len(left[0]))]
        for row in range(len(left))
    ]


def subtract(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[row][column] - right[row][column] for column in range(len(left[0]))]
        for row in range(len(left))
    ]


def multiply(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(
                (left[row][index] * right[index][column] for index in range(len(right))),
                Fraction(0),
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def transpose(matrix: Matrix) -> Matrix:
    return [list(column) for column in zip(*matrix)]


def scale(value: Fraction, matrix: Matrix) -> Matrix:
    return [[value * entry for entry in row] for row in matrix]


def determinant(matrix: Matrix) -> Fraction:
    work = [row[:] for row in matrix]
    result = Fraction(1)
    for column in range(len(work)):
        pivot = next(
            (row for row in range(column, len(work)) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            result *= -1
        value = work[column][column]
        result *= value
        for row in range(column + 1, len(work)):
            coefficient = work[row][column] / value
            for index in range(column, len(work)):
                work[row][index] -= coefficient * work[column][index]
    return result


def rank(matrix: Matrix) -> int:
    work = [row[:] for row in matrix]
    pivot_row = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(pivot_row, len(work)) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        divisor = work[pivot_row][column]
        work[pivot_row] = [entry / divisor for entry in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row:
                continue
            coefficient = work[row][column]
            if coefficient:
                work[row] = [
                    work[row][index] - coefficient * work[pivot_row][index]
                    for index in range(len(work[0]))
                ]
        pivot_row += 1
    return pivot_row


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def permutation_matrix(permutation: tuple[int, ...]) -> Matrix:
    matrix = zero(3, 3)
    for row, column in enumerate(permutation):
        matrix[row][column] = Fraction(1)
    return matrix


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    packet_path = ROOT / candidate["packet"]
    packet = load(packet_path)

    if candidate["artifact"] != "FoundationalBridge-FB1":
        raise AssertionError("foundational bridge artifact label changed")
    if candidate["closure_claimed"] or certificate["closure_claimed"]:
        raise AssertionError("trace-split bridge overclaims physical closure")
    if sha256(packet_path) != candidate["packet_sha256"]:
        raise AssertionError("trace-split bridge packet hash mismatch")
    if sha256(ROOT / candidate["note"]) != candidate["note_sha256"]:
        raise AssertionError("trace-split bridge note hash mismatch")
    if sha256(CANDIDATE) != certificate["candidate_sha256"]:
        raise AssertionError("trace-split bridge candidate hash mismatch")
    for authority in packet["authority"]:
        if sha256(ROOT / authority["path"]) != authority["sha256"]:
            raise AssertionError(f"authority mismatch: {authority['path']}")

    matrices = packet["exact_matrices"]
    p_trace = decode_matrix(matrices["p_trace_rank1"])
    p_zero = decode_matrix(matrices["p_trace_zero_rank2"])
    p_full = decode_matrix(matrices["p_full_rank3"])
    trace_zero_basis = decode_matrix(matrices["trace_zero_basis_columns"])
    reuse_basis = decode_matrix(matrices["unit_plus_trace_zero_reuse_basis"])
    lane_projectors = [decode_matrix(value) for value in matrices["six_lane_projectors"]]

    if multiply(p_trace, p_trace) != p_trace:
        raise AssertionError("rank-one trace projector is not idempotent")
    if multiply(p_zero, p_zero) != p_zero:
        raise AssertionError("rank-two trace-zero projector is not idempotent")
    if multiply(p_trace, p_zero) != zero(3, 3):
        raise AssertionError("trace and trace-zero projectors are not orthogonal")
    if add(p_trace, p_zero) != p_full:
        raise AssertionError("trace decomposition does not sum to the full carrier")
    if [rank(p_trace), rank(p_zero), rank(p_full)] != [1, 2, 3]:
        raise AssertionError("q79 trace-split rank signature changed")
    if multiply([[Fraction(1), Fraction(1), Fraction(1)]], trace_zero_basis) != zero(1, 2):
        raise AssertionError("stored trace-zero basis left the trace kernel")
    if determinant(reuse_basis) == 0:
        raise AssertionError("unit plus trace-zero basis is not a decomposition")

    for permutation in itertools.permutations(range(3)):
        raw = permutation_matrix(permutation)
        oriented = scale(Fraction(permutation_sign(permutation)), raw)
        if determinant(oriented) != 1:
            raise AssertionError("signed sheet action left SO(3)")
        if multiply(transpose(oriented), oriented) != identity(3):
            raise AssertionError("signed sheet action is not orthogonal")
        if multiply(oriented, p_trace) != multiply(p_trace, oriented):
            raise AssertionError("trace line is not monodromy invariant")
        if multiply(oriented, p_zero) != multiply(p_zero, oriented):
            raise AssertionError("trace-zero plane is not monodromy invariant")

    if [rank(projector) for projector in lane_projectors] != [1, 2, 3]:
        raise AssertionError("six-carrier block ranks changed")
    for left in range(3):
        if multiply(lane_projectors[left], lane_projectors[left]) != lane_projectors[left]:
            raise AssertionError("six-carrier block projector lost idempotence")
        for right in range(3):
            if left != right and multiply(lane_projectors[left], lane_projectors[right]) != zero(6, 6):
                raise AssertionError("six-carrier block projectors are not orthogonal")
    if add(add(lane_projectors[0], lane_projectors[1]), lane_projectors[2]) != identity(6):
        raise AssertionError("six-carrier block projectors do not resolve identity")

    theorem = packet["exact_q79_carrier_theorem"]
    if theorem["rank_signature"] != [1, 2, 3] or theorem["total_rank"] != 6:
        raise AssertionError("stored CLN rank theorem changed")
    if theorem["fitted_continuous_parameters_added"] != 0:
        raise AssertionError("trace-split theorem added a hidden fit parameter")
    if packet["monodromy_and_orientation_theorem"]["global_ordered_sheet_flag_selected"]:
        raise AssertionError("connected q79 cover was silently ordered")
    if packet["physical_bridge_contract"]["full_bridge_closed"]:
        raise AssertionError("world-in-world physical bridge was silently closed")
    if packet["physical_bridge_contract"]["closed_count"] != 0:
        raise AssertionError("unfilled bridge value fields were promoted")

    print("q79 trace-split CLN/world-in-world bridge audit: PASS")
    print("closed: finite-flat trace carrier ranks 1+2+3=6 with common-circle factor")
    print("closed: all six signed S3 sheet actions are orthogonal with determinant +1")
    print("closed: transitive cover forbids a global ordered sheet flag")
    print("open: Spin lift, selected Q/Hessian, branch continuation, and HYM intertwiner")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
