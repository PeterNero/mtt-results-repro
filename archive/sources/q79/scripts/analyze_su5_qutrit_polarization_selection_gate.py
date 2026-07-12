"""Analyze the remaining SU(5) qutrit polarization-selection gate.

The finite qutrit transport lemma proves that clock and shift polarizations are
related by the qutrit Fourier matrix.  The remaining selector would have to
come from selected zero-mode, monad/Cech, Galerkin, or gerbe data proving:

    10_M   = clock-polarized qutrit sector,
    bar5_M = shift-polarized qutrit sector.

This script checks the current certificates and tests a tempting shortcut: the
SU(3) identity wedge2(E) ~= E^*.  That identity supplies the expected dual
representation, but its natural Hodge transport is monomial.  Since diagonal
rephasings and family permutations preserve zero support, it cannot be the
dense qutrit Fourier transport.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATES = ROOT / "certificates"
TOL = 1e-10
OMEGA = complex(-0.5, math.sqrt(3) / 2.0)
PAIRS = ((0, 1), (0, 2), (1, 2))

Matrix = list[list[complex]]


def load_json(name: str) -> dict[str, Any]:
    path = CERTIFICATES / name
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def identity() -> Matrix:
    return [[1.0 + 0j if row == col else 0j for col in range(3)] for row in range(3)]


def clock() -> Matrix:
    return [[OMEGA**row if row == col else 0j for col in range(3)] for row in range(3)]


def shift() -> Matrix:
    return [[1.0 + 0j if row == (col + 1) % 3 else 0j for col in range(3)] for row in range(3)]


def fourier() -> Matrix:
    scale = 1.0 / math.sqrt(3)
    return [[OMEGA ** (row * col) * scale for col in range(3)] for row in range(3)]


def dagger(matrix: Matrix) -> Matrix:
    return [[matrix[col][row].conjugate() for col in range(3)] for row in range(3)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [sum(left[row][mid] * right[mid][col] for mid in range(3)) for col in range(3)]
        for row in range(3)
    ]


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return [[left[row][col] - right[row][col] for col in range(3)] for row in range(3)]


def max_abs(matrix: Matrix) -> float:
    return max(abs(entry) for row in matrix for entry in row)


def approx_equal(left: Matrix, right: Matrix) -> bool:
    return max_abs(matrix_sub(left, right)) < TOL


def matrix_power(matrix: Matrix, power: int) -> Matrix:
    result = identity()
    for _ in range(power):
        result = matmul(result, matrix)
    return result


def wedge2(matrix: Matrix) -> Matrix:
    """Exterior-square matrix in the ordered basis e01,e02,e12.

    Matrix columns act on input basis vectors.  The output coefficient on
    e_p wedge e_q is the 2x2 minor with rows p,q and columns i,j.
    """

    result: Matrix = []
    for p, q in PAIRS:
        row: list[complex] = []
        for i, j in PAIRS:
            row.append(matrix[p][i] * matrix[q][j] - matrix[p][j] * matrix[q][i])
        result.append(row)
    return result


def hodge_transport_wedge2_to_dual() -> Matrix:
    """Hodge identification wedge2(C^3) -> (C^3)^* in the same orientation.

    With basis e01,e02,e12 this sends:
        e01 -> e2^*, e02 -> -e1^*, e12 -> e0^*.

    The resulting matrix is signed-permutation/monomial, so it cannot be
    converted into the dense Fourier matrix by rephasing or relabeling.
    """

    return [
        [0j, 0j, 1 + 0j],
        [0j, -1 + 0j, 0j],
        [1 + 0j, 0j, 0j],
    ]


def support_count(matrix: Matrix) -> int:
    return sum(1 for row in matrix for entry in row if abs(entry) > TOL)


def row_support_counts(matrix: Matrix) -> list[int]:
    return [sum(1 for entry in row if abs(entry) > TOL) for row in matrix]


def col_support_counts(matrix: Matrix) -> list[int]:
    return [sum(1 for row in range(3) if abs(matrix[row][col]) > TOL) for col in range(3)]


def is_monomial(matrix: Matrix) -> bool:
    return all(count == 1 for count in row_support_counts(matrix)) and all(
        count == 1 for count in col_support_counts(matrix)
    )


def has_same_zero_pattern_invariants(left: Matrix, right: Matrix) -> bool:
    """Support counts preserved by diagonal phases and row/column permutations."""

    return (
        sorted(row_support_counts(left)) == sorted(row_support_counts(right))
        and sorted(col_support_counts(left)) == sorted(col_support_counts(right))
        and support_count(left) == support_count(right)
    )


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


def selected_basis_template_status() -> dict[str, Any]:
    template = load_json("selected_su5_qutrit_polarization_data.template.json")
    sectors = template.get("sector_basis_data", {})
    supplied = bool(sectors) and all(
        sectors.get(name, {}).get(field) is not None
        for name, field in (("10_M", "basis_matrix_U10"), ("bar5_M", "basis_matrix_Ubar5"))
    )
    return {
        "template_present": bool(template),
        "template_status": template.get("status"),
        "selected_sector_basis_matrices_supplied": supplied,
        "required_acceptance_test": template.get("acceptance_tests", {}).get(
            "relative_transport_equals_F_mod_rephase_permutation"
        ),
    }


def analyze() -> dict[str, Any]:
    qutrit = load_json("qutrit_polarization_transport_lemma_certificate.json")
    selector = load_json("su5_qutrit_transport_selector_hunt_certificate.json")
    typed = load_json("iwasawa_typed_monad_section_recovery_certificate.json")
    monad = load_json("iwasawa_monad_map_data_gate_certificate.json")
    projective = load_json("iwasawa_projective_twist_source_hunt_certificate.json")
    zero_mode = load_json("selected_zero_mode_basis_dotd_interface_certificate.json")

    z = clock()
    x = shift()
    f = fourier()
    w2_z = wedge2(z)
    w2_x = wedge2(x)
    hodge = hodge_transport_wedge2_to_dual()

    zero_mode_slots = zero_mode.get("basis_slots", {})
    selected_zero_mode_values_supplied = bool(zero_mode_slots) and all(
        slot.get("ordered_zero_mode_basis") is not None
        for key, slot in zero_mode_slots.items()
        if key in {"Q", "u", "d", "L", "e", "N"}
    )

    support_invariants_match_f = has_same_zero_pattern_invariants(hodge, f)
    exterior_square_shortcut_rejected = (
        is_monomial(w2_z)
        and is_monomial(w2_x)
        and is_monomial(hodge)
        and support_count(hodge) == 3
        and support_count(f) == 9
        and not support_invariants_match_f
    )

    finite_transport_proved = (
        qutrit.get("verdict", {}).get("finite_transport_lemma_proved") is True
    )
    existing_selector_found = (
        selector.get("verdict", {}).get("selected_B10_Bbar5_transport_found") is True
    )
    typed_monad_can_close_now = (
        typed.get("route_decision", {}).get("typed_monad_cech_can_close_now") is True
    )
    monad_can_compute_h1 = (
        monad.get("consequence_for_sm_closure", {}).get("can_compute_H1_X_E_from_current_monad_data")
        is True
    )
    projective_twist_selected = (
        projective.get("verdict", {}).get("selected_projective_twist_source_found") is True
    )
    selected_basis = selected_basis_template_status()

    source_can_close_selection_now = (
        existing_selector_found
        or typed_monad_can_close_now
        or monad_can_compute_h1
        or projective_twist_selected
        or selected_zero_mode_values_supplied
        or selected_basis["selected_sector_basis_matrices_supplied"]
    )

    return {
        "calculation": "SU5QutritPolarizationSelectionGate",
        "source_status": {
            "finite_transport_lemma_proved": finite_transport_proved,
            "existing_direct_selector_found": existing_selector_found,
            "typed_monad_cech_can_close_now": typed_monad_can_close_now,
            "monad_can_compute_H1_now": monad_can_compute_h1,
            "selected_projective_twist_source_found": projective_twist_selected,
            "selected_zero_mode_sector_values_supplied": selected_zero_mode_values_supplied,
            "selected_basis_template": selected_basis,
        },
        "finite_exterior_square_shortcut_test": {
            "setup": "wedge2(C^3) ~= (C^3)^* is tested as a possible source of the 10_M/bar5_M split",
            "Z_cubed_identity": approx_equal(matrix_power(z, 3), identity()),
            "X_cubed_identity": approx_equal(matrix_power(x, 3), identity()),
            "wedge2_Z": w2_z,
            "wedge2_X": w2_x,
            "wedge2_Z_is_monomial": is_monomial(w2_z),
            "wedge2_X_is_monomial": is_monomial(w2_x),
            "hodge_transport_wedge2_to_dual": hodge,
            "hodge_transport_is_monomial": is_monomial(hodge),
            "hodge_support_count": support_count(hodge),
            "fourier_support_count": support_count(f),
            "hodge_can_equal_F_mod_rephase_permutation": support_invariants_match_f,
            "exterior_square_shortcut_rejected": exterior_square_shortcut_rejected,
            "interpretation": (
                "The SU(3) exterior-square/dual relation supports the representation "
                "dictionary but does not select the dense Fourier transport."
            ),
        },
        "closed_now": {
            "finite_qutrit_transport_core": finite_transport_proved,
            "corpus_selector_absence_checked": not existing_selector_found,
            "monad_zero_mode_data_absence_checked": not typed_monad_can_close_now
            and not monad_can_compute_h1
            and not selected_zero_mode_values_supplied,
            "exterior_square_shortcut_rejected": exterior_square_shortcut_rejected,
            "minimal_remaining_finite_packet_identified": True,
        },
        "remaining_finite_packet": {
            "required_source": "selected monad/Cech cohomology, spectral Galerkin/Riesz data, or selected gerbe/twisted-bundle data",
            "required_matrices": ["U_10", "U_bar5"],
            "required_sector_statements": {
                "10_M": "clock-polarized qutrit basis, or explicit U_10",
                "bar5_M": "shift-polarized qutrit basis, or explicit U_bar5",
            },
            "finite_acceptance_tests": [
                "U_10 and U_bar5 are unitary in the selected L2 metrics",
                "U_10^dagger U_bar5 equals F or F^* modulo diagonal phases and family permutations",
                "orientation convention selects F for q=79 rather than F^*",
                "the result is derived before using observed masses or CKM data",
            ],
            "target_template": "certificates/selected_su5_qutrit_polarization_data.template.json",
        },
        "verdict": {
            "sector_polarization_selection_proved_from_current_data": source_can_close_selection_now,
            "can_promote_su5_qutrit_heavy_link_candidate_to_selected_input": source_can_close_selection_now,
            "current_best_status": "gate closed; selected sector-basis data still open",
            "next_required_input": (
                "fill the selected_su5_qutrit_polarization_data packet with actual "
                "U_10 and U_bar5 from selected zero-mode data, then rerun the finite "
                "transport acceptance test"
            ),
        },
        "guardrails": {
            "claims_full_polarization_selection": source_can_close_selection_now,
            "promotes_candidate_without_selected_U10_Ubar5": False,
            "uses_wedge2_duality_as_fourier_transport": False,
            "uses_observed_masses_or_ckm_inputs": False,
            "claims_full_sm_closure": False,
        },
    }


def main() -> int:
    print(json.dumps(encode(analyze()), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
