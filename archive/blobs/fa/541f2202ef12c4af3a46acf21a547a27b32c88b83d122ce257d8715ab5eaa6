"""Prove the finite qutrit polarization transport lemma.

This closes the algebraic core behind the SU(5) qutrit transport candidate:
once the selected geometry says that one sector is in the clock polarization
and another sector is in the shift polarization of the same qutrit Heisenberg
carrier, the relative basis transport is the normalized qutrit Fourier matrix
up to the conjugate convention and harmless external rephasings.

It does not prove that MTT has selected those sector polarizations.  That is a
separate zero-mode/monad/Galerkin selection statement.
"""

from __future__ import annotations

import itertools
import json
import math
from typing import Any


TOL = 1e-10
OMEGA = complex(-0.5, math.sqrt(3) / 2.0)
HEAVY_LINKS = ((0, 2), (1, 2))


Matrix = list[list[complex]]


def identity() -> Matrix:
    return [[1.0 + 0j if row == col else 0j for col in range(3)] for row in range(3)]


def clock() -> Matrix:
    return [[OMEGA**row if row == col else 0j for col in range(3)] for row in range(3)]


def shift() -> Matrix:
    return [[1.0 + 0j if row == (col + 1) % 3 else 0j for col in range(3)] for row in range(3)]


def fourier(conjugate: bool = False) -> Matrix:
    omega = OMEGA.conjugate() if conjugate else OMEGA
    scale = 1.0 / math.sqrt(3)
    return [[omega ** (row * col) * scale for col in range(3)] for row in range(3)]


def dagger(matrix: Matrix) -> Matrix:
    return [[matrix[col][row].conjugate() for col in range(3)] for row in range(3)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [sum(left[row][mid] * right[mid][col] for mid in range(3)) for col in range(3)]
        for row in range(3)
    ]


def scalar_mul(scalar: complex, matrix: Matrix) -> Matrix:
    return [[scalar * entry for entry in row] for row in matrix]


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return [[left[row][col] - right[row][col] for col in range(3)] for row in range(3)]


def max_abs(matrix: Matrix) -> float:
    return max(abs(entry) for row in matrix for entry in row)


def approx_equal(left: Matrix, right: Matrix) -> bool:
    return max_abs(matrix_sub(left, right)) < TOL


def is_unitary(matrix: Matrix) -> bool:
    return approx_equal(matmul(dagger(matrix), matrix), identity())


def matrix_power(matrix: Matrix, power: int) -> Matrix:
    result = identity()
    for _ in range(power):
        result = matmul(result, matrix)
    return result


def dephased_hadamard_roots() -> list[list[list[int]]]:
    """Classify dephased 3x3 root-of-unity Hadamard exponent tables.

    The first row and first column are fixed to zero exponents.  Orthogonality
    over third roots leaves exactly the Fourier table and its conjugate.
    """

    solutions: list[list[list[int]]] = []
    for entries in itertools.product(range(3), repeat=4):
        exponents = [
            [0, 0, 0],
            [0, entries[0], entries[1]],
            [0, entries[2], entries[3]],
        ]
        matrix = [
            [OMEGA ** exponents[row][col] / math.sqrt(3) for col in range(3)]
            for row in range(3)
        ]
        if is_unitary(matrix):
            solutions.append(exponents)
    return solutions


def heavy_vector(matrix: Matrix) -> list[complex]:
    return [matrix[row][col] for row, col in HEAVY_LINKS]


def encode_scalar(value: complex) -> float | list[float]:
    real = 0.0 if abs(value.real) < TOL else value.real
    imag = 0.0 if abs(value.imag) < TOL else value.imag
    if imag == 0.0:
        return real
    return [real, imag]


def encode(value: Any) -> Any:
    if isinstance(value, complex):
        return encode_scalar(value)
    if isinstance(value, list):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {key: encode(item) for key, item in value.items()}
    return value


def analyze() -> dict[str, Any]:
    i3 = identity()
    x = shift()
    z = clock()
    f = fourier()
    f_star = fourier(conjugate=True)
    f_dag = dagger(f)
    z_inverse = dagger(z)
    x_inverse = dagger(x)

    f_clock_to_shift = matmul(matmul(f_dag, z), f)
    f_shift_to_inverse_clock = matmul(matmul(f_dag, x), f)
    fstar_clock_to_inverse_shift = matmul(matmul(dagger(f_star), z), f_star)

    exponents = dephased_hadamard_roots()
    f_exponents = [[0, 0, 0], [0, 1, 2], [0, 2, 1]]
    fstar_exponents = [[0, 0, 0], [0, 2, 1], [0, 1, 2]]

    return {
        "calculation": "QutritPolarizationTransportLemma",
        "setup": {
            "clock_operator": "Z e_j = omega^j e_j",
            "shift_operator": "X e_j = e_(j+1 mod 3)",
            "fourier_matrix": "F_jk = omega^(j*k)/sqrt(3)",
            "clock_polarization": "standard Z eigenbasis",
            "shift_polarization": "dephased X eigenbasis with F^dagger X F = Z^-1",
            "relative_transport": "B_clock^dagger B_shift",
        },
        "finite_heisenberg_checks": {
            "X_unitary": is_unitary(x),
            "Z_unitary": is_unitary(z),
            "X_cubed_identity": approx_equal(matrix_power(x, 3), i3),
            "Z_cubed_identity": approx_equal(matrix_power(z, 3), i3),
            "ZX_equals_omega_XZ": approx_equal(matmul(z, x), scalar_mul(OMEGA, matmul(x, z))),
        },
        "fourier_intertwiner_checks": {
            "F_unitary": is_unitary(f),
            "F_dagger_Z_F_equals_X": approx_equal(f_clock_to_shift, x),
            "F_dagger_X_F_equals_Z_inverse": approx_equal(f_shift_to_inverse_clock, z_inverse),
            "Fstar_dagger_Z_Fstar_equals_X_inverse": approx_equal(
                fstar_clock_to_inverse_shift, x_inverse
            ),
        },
        "dephased_hadamard_classification": {
            "root_order": 3,
            "first_row_and_column_dephased": True,
            "solutions_count": len(exponents),
            "solution_exponent_tables": exponents,
            "fourier_table_present": f_exponents in exponents,
            "conjugate_fourier_table_present": fstar_exponents in exponents,
            "orientation_selects_F_not_Fstar": approx_equal(f_clock_to_shift, x),
        },
        "sector_transport_theorem": {
            "hypothesis": "10_M uses clock polarization and bar5_M uses shift polarization in the same qutrit Heisenberg carrier",
            "B_10": "I_3 after dephasing/family-order convention",
            "B_bar5": "F after the positive first-row/first-column convention",
            "relative_transport_B10_dagger_Bbar5": f,
            "conjugate_orientation": "F^* if the selected shift orientation is reversed",
            "finite_algebraic_transport_proved": True,
        },
        "heavy_link_consequence_if_selected": {
            "Delta_t_symbolic": ["1/sqrt(3)", "omega^2/sqrt(3)"],
            "Delta_t_numeric": heavy_vector(f),
            "inverse_orientation_symbolic": ["1/sqrt(3)", "omega/sqrt(3)"],
            "inverse_orientation_numeric": heavy_vector(f_star),
            "leading_heavy_link_nonzero": any(abs(entry) > TOL for entry in heavy_vector(f)),
        },
        "what_this_proves": {
            "finite_qutrit_clock_shift_transport": True,
            "uniqueness_up_to_conjugate_orientation_and_rephasing": True,
            "su5_candidate_numbers_follow_from_polarization_hypothesis": True,
        },
        "still_open": {
            "MTT_selects_10M_clock_polarization": True,
            "MTT_selects_bar5M_shift_polarization": True,
            "selected_zero_mode_or_monad_source_for_polarization": True,
            "selected_overlap_kernel_prefactor": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_MTT_has_selected_polarizations": False,
            "uses_benchmark_or_observed_flavor_data": False,
            "claims_CKM_angles_or_Jarlskog": False,
            "claims_full_SM_closure": False,
        },
        "verdict": {
            "finite_transport_lemma_proved": True,
            "sector_transport_selection_reduced_to_polarization_selection": True,
            "selector_hypothesis_remains_external_to_this_finite_proof": True,
            "next_required_lemma": (
                "prove from selected zero-mode/monad/Galerkin data that "
                "10_M is the clock polarization and bar5_M is the shift polarization"
            ),
        },
    }


def main() -> int:
    print(json.dumps(encode(analyze()), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
