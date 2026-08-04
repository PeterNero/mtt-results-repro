from __future__ import annotations

from fractions import Fraction
from itertools import permutations
from typing import Iterable


Q = Fraction
G = tuple[Fraction, Fraction]
Matrix = list[list[Fraction]]
GMatrix = list[list[G]]


def eye(n: int) -> Matrix:
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def zeros(rows: int, cols: int) -> Matrix:
    return [[Fraction(0) for _ in range(cols)] for _ in range(rows)]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def sub(a: Matrix, b: Matrix) -> Matrix:
    return [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c: Fraction, a: Matrix) -> Matrix:
    return [[c * x for x in row] for row in a]


def mul(a: Matrix, b: Matrix) -> Matrix:
    bt = transpose(b)
    return [[sum((x * y for x, y in zip(row, col)), Fraction(0)) for col in bt] for row in a]


def block_diag(a: Matrix, b: Matrix) -> Matrix:
    out = zeros(len(a) + len(b), len(a[0]) + len(b[0]))
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            out[i][j] = value
    for i, row in enumerate(b):
        for j, value in enumerate(row):
            out[len(a) + i][len(a[0]) + j] = value
    return out


def rank(a: Matrix) -> int:
    work = [row[:] for row in a]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if work[r][col] != 0), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        divisor = work[pivot_row][col]
        work[pivot_row] = [value / divisor for value in work[pivot_row]]
        for r in range(rows):
            if r == pivot_row or work[r][col] == 0:
                continue
            factor = work[r][col]
            work[r] = [x - factor * y for x, y in zip(work[r], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def permutation_matrix(perm: Iterable[int]) -> Matrix:
    values = list(perm)
    out = zeros(len(values), len(values))
    for column, row in enumerate(values):
        out[row][column] = Fraction(1)
    return out


def reynolds_two_copy_s3() -> Matrix:
    total = zeros(6, 6)
    for representation in two_copy_s3_representations():
        total = add(total, representation)
    return scale(Fraction(1, 6), total)


def two_copy_s3_representations() -> list[Matrix]:
    return [block_diag(permutation_matrix(perm), permutation_matrix(perm)) for perm in permutations(range(3))]


def commutant_dimension(operators: list[Matrix]) -> int:
    if not operators:
        raise ValueError("at least one operator is required")
    n = len(operators[0])
    constraints: Matrix = []
    for operator in operators:
        for i in range(n):
            for j in range(n):
                row = [Fraction(0) for _ in range(n * n)]
                for k in range(n):
                    row[i * n + k] += operator[k][j]
                    row[k * n + j] -= operator[i][k]
                constraints.append(row)
    return n * n - rank(constraints)


def jde() -> Matrix:
    i3 = eye(3)
    z3 = zeros(3, 3)
    return [
        *(z3[r] + [-x for x in i3[r]] for r in range(3)),
        *(i3[r] + z3[r] for r in range(3)),
    ]


def jfm() -> Matrix:
    return [
        [Q(0), Q(0), Q(0), Q(-1)],
        [Q(0), Q(0), Q(-1), Q(0)],
        [Q(0), Q(1), Q(0), Q(0)],
        [Q(1), Q(0), Q(0), Q(0)],
    ]


def g_add(x: G, y: G) -> G:
    return x[0] + y[0], x[1] + y[1]


def g_mul(x: G, y: G) -> G:
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def g_conj(x: G) -> G:
    return x[0], -x[1]


def g_scale(c: Fraction, x: G) -> G:
    return c * x[0], c * x[1]


def g_transpose_conjugate(a: GMatrix) -> GMatrix:
    return [[g_conj(value) for value in row] for row in zip(*a)]


def g_mul_matrix(a: GMatrix, b: GMatrix) -> GMatrix:
    bt = list(zip(*b))
    out: GMatrix = []
    for row in a:
        out_row: list[G] = []
        for col in bt:
            value: G = (Fraction(0), Fraction(0))
            for x, y in zip(row, col):
                value = g_add(value, g_mul(x, y))
            out_row.append(value)
        out.append(out_row)
    return out


def g_eye(n: int) -> GMatrix:
    return [
        [(Fraction(int(row == column)), Fraction(0)) for column in range(n)]
        for row in range(n)
    ]


def g_zeros(rows: int, columns: int) -> GMatrix:
    return [[(Fraction(0), Fraction(0)) for _ in range(columns)] for _ in range(rows)]


def g_from_rational_matrix(a: Matrix) -> GMatrix:
    return [[(value, Fraction(0)) for value in row] for row in a]


def g_add_matrix(a: GMatrix, b: GMatrix) -> GMatrix:
    return [[g_add(x, y) for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def g_sub_matrix(a: GMatrix, b: GMatrix) -> GMatrix:
    return [
        [g_add(x, g_scale(Fraction(-1), y)) for x, y in zip(ar, br)]
        for ar, br in zip(a, b)
    ]


def g_scale_matrix(c: G, a: GMatrix) -> GMatrix:
    return [[g_mul(c, value) for value in row] for row in a]


def g_kronecker(a: GMatrix, b: GMatrix) -> GMatrix:
    output = g_zeros(len(a) * len(b), len(a[0]) * len(b[0]))
    for left_row, left_values in enumerate(a):
        for left_column, left_value in enumerate(left_values):
            for right_row, right_values in enumerate(b):
                for right_column, right_value in enumerate(right_values):
                    output[left_row * len(b) + right_row][
                        left_column * len(b[0]) + right_column
                    ] = g_mul(left_value, right_value)
    return output


def g_rank(a: GMatrix) -> int:
    rows = len(a)
    columns = len(a[0]) if rows else 0
    realification = zeros(2 * rows, 2 * columns)
    for row in range(rows):
        for column in range(columns):
            real, imag = a[row][column]
            realification[row][column] = real
            realification[row][columns + column] = -imag
            realification[rows + row][column] = imag
            realification[rows + row][columns + column] = real
    real_rank = rank(realification)
    if real_rank % 2:
        raise ValueError("complex matrix realification has odd rational rank")
    return real_rank // 2


def gaussian_matrix_strings(a: GMatrix) -> list[list[str]]:
    def render(value: G) -> str:
        real, imag = value
        if imag == 0:
            return str(real)
        if real == 0:
            return f"{imag}i"
        sign = "+" if imag > 0 else ""
        return f"{real}{sign}{imag}i"

    return [[render(value) for value in row] for row in a]


def complex_polarizations(j: Matrix) -> tuple[GMatrix, GMatrix]:
    n = len(j)
    plus: GMatrix = []
    minus: GMatrix = []
    for r in range(n):
        plus_row: list[G] = []
        minus_row: list[G] = []
        for c in range(n):
            identity = Fraction(int(r == c))
            plus_row.append((identity / 2, -j[r][c] / 2))
            minus_row.append((identity / 2, j[r][c] / 2))
        plus.append(plus_row)
        minus.append(minus_row)
    return plus, minus


def fraction_matrix_strings(a: Matrix) -> list[list[str]]:
    return [[str(value) for value in row] for row in a]
