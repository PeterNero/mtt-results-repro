"""Analyze SU(5)-split qutrit basis transport for CKM heavy links.

The pure qutrit/C6 support calculation shows that the conjugate finite
pairings have diagonal invariant support, hence zero (1,3) and (2,3) heavy
links in one common family basis.  This script tests the next possible source:
relative basis transport between the SU(5) matter slots used by the E6 Yukawa
dictionary.

The key distinction is gauge versus sector-relative transport:

* a common unitary on all family slots cancels in B_left^* I B_right;
* a representation split, for example B_10 = I and B_bar5 = F, does not cancel
  in the down channel 10_M x bar5_M while it still cancels in the up channel
  10_M x 10_M.

This is a no-observed-data candidate direction, not a selected MTT fill.  It
only becomes selected if a later zero-mode/monad/Galerkin theorem derives the
representation-dependent transport from the same branch.
"""

from __future__ import annotations

import json
import math
from typing import Any


TOL = 1e-10
HEAVY_LINKS = ((0, 2), (1, 2))
OMEGA = complex(-0.5, math.sqrt(3) / 2.0)


Matrix = list[list[complex]]


def identity() -> Matrix:
    return [[1.0 + 0j if row == col else 0j for col in range(3)] for row in range(3)]


def fourier(conjugate: bool = False) -> Matrix:
    omega = OMEGA.conjugate() if conjugate else OMEGA
    scale = 1.0 / math.sqrt(3)
    return [[(omega ** (row * col)) * scale for col in range(3)] for row in range(3)]


def dagger(matrix: Matrix) -> Matrix:
    return [[matrix[col][row].conjugate() for col in range(3)] for row in range(3)]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [sum(left[row][mid] * right[mid][col] for mid in range(3)) for col in range(3)]
        for row in range(3)
    ]


def max_abs(matrix: Matrix) -> float:
    return max(abs(entry) for row in matrix for entry in row)


def matrix_sub(left: Matrix, right: Matrix) -> Matrix:
    return [[left[row][col] - right[row][col] for col in range(3)] for row in range(3)]


def is_unitary(matrix: Matrix) -> bool:
    return max_abs(matrix_sub(matmul(dagger(matrix), matrix), identity())) < TOL


def support(left_basis: Matrix, right_basis: Matrix) -> Matrix:
    """Transport diagonal invariant support I into the sector bases."""

    return matmul(dagger(left_basis), right_basis)


def heavy_vector(matrix: Matrix) -> list[complex]:
    return [matrix[row][col] for row, col in HEAVY_LINKS]


def vector_sub(left: list[complex], right: list[complex]) -> list[complex]:
    return [a - b for a, b in zip(left, right)]


def nonzero(vector: list[complex]) -> bool:
    return any(abs(entry) > TOL for entry in vector)


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


def symbolic_fourier_entry(row: int, col: int, conjugate: bool = False) -> str:
    exponent = (row * col) % 3
    if conjugate and exponent != 0:
        exponent = (-exponent) % 3
    if exponent == 0:
        return "1/sqrt(3)"
    return f"omega^{exponent}/sqrt(3)"


def analyze_case(name: str, b_10: Matrix, b_bar5: Matrix, b_u: Matrix | None = None) -> dict[str, Any]:
    b_u = b_10 if b_u is None else b_u
    up = support(b_10, b_u)
    down = support(b_10, b_bar5)
    up_heavy = heavy_vector(up)
    down_heavy = heavy_vector(down)
    delta = vector_sub(down_heavy, up_heavy)

    return {
        "name": name,
        "up_pair": "10_M x 10_M",
        "down_pair": "10_M x bar5_M",
        "up_support": up,
        "down_support": down,
        "up_heavy_links_13_23": up_heavy,
        "down_heavy_links_13_23": down_heavy,
        "Delta_t_candidate": delta,
        "leading_heavy_link_gate_if_selected": nonzero(delta),
    }


def zero_c1_packet_from_candidate(delta: list[complex]) -> dict[str, Any]:
    terms = (
        "theta_overlap_variation",
        "left_zero_mode_response",
        "right_zero_mode_response",
        "higgs_zero_mode_response",
        "explicit_vertex",
        "basis_connection",
    )
    sectors: dict[str, dict[str, list[complex]]] = {
        "u": {term: [0j, 0j] for term in terms},
        "d": {term: [0j, 0j] for term in terms},
    }
    sectors["d"]["basis_connection"] = delta
    return {
        "status": "NONSELECTED_CANDIDATE_FIXTURE",
        "description": (
            "C1 heavy-link primitive fixture using only the SU5 qutrit basis "
            "transport candidate in the down-sector basis_connection term."
        ),
        "sectors": sectors,
        "guardrails": {
            "selected_by_MTT": False,
            "uses_observed_flavor_data": False,
            "claims_selected_C1_response": False,
        },
    }


def ckm_packet_from_candidate(delta: list[complex]) -> dict[str, Any]:
    return {
        "status": "NONSELECTED_CANDIDATE_FIXTURE",
        "description": (
            "Leading CKM heavy-link fixture using the SU5 qutrit basis "
            "transport candidate for Delta_t and the proved pure-C6 "
            "Delta_c=(0,0)."
        ),
        "phase_branch": {
            "modulus": 448,
            "selected_label": 79,
        },
        "inputs": {
            "character_trivial_heavy_link": {
                "u": {"entries": [0j, 0j]},
                "d": {"entries": delta},
            },
            "c6_heavy_link": {
                "u": {"entries": [0j, 0j]},
                "d": {"entries": [0j, 0j]},
            },
        },
        "guardrails": {
            "selected_by_MTT": False,
            "uses_observed_flavor_data": False,
            "claims_selected_Delta_v": False,
        },
    }


def analyze() -> dict[str, Any]:
    i3 = identity()
    f = fourier()
    f_conj = fourier(conjugate=True)

    aligned = analyze_case("aligned_identity", i3, i3)
    common_fourier = analyze_case("common_fourier_gauge", f, f)
    split_bar5_fourier = analyze_case("su5_split_B10_identity_Bbar5_fourier", i3, f)
    split_bar5_inverse = analyze_case("su5_split_B10_identity_Bbar5_inverse_fourier", i3, f_conj)
    split_10_fourier = analyze_case("su5_split_B10_fourier_Bbar5_identity", f, i3)

    cases = [
        aligned,
        common_fourier,
        split_bar5_fourier,
        split_bar5_inverse,
        split_10_fourier,
    ]
    selected_candidate = split_bar5_fourier

    return {
        "calculation": "SU5QutritBasisTransportHeavyLinks",
        "setup": {
            "finite_support_input": "pure qutrit invariant support I_3",
            "transport_formula": "M(left,right)=B_left^dagger I_3 B_right",
            "fourier_matrix": "F_jk=omega^(j*k)/sqrt(3), j,k=0,1,2",
            "omega": "exp(2*pi*i/3)",
            "heavy_link_entries": "matrix entries (1,3) and (2,3)",
            "e6_su5_channel_split": {
                "up": "10_M x 10_M",
                "down": "10_M x bar5_M",
            },
        },
        "unitarity_checks": {
            "I3_unitary": is_unitary(i3),
            "F_unitary": is_unitary(f),
            "F_conjugate_unitary": is_unitary(f_conj),
        },
        "cases": cases,
        "gauge_cancellation": {
            "aligned_identity_delta_zero": not nonzero(aligned["Delta_t_candidate"]),
            "common_fourier_delta_zero": not nonzero(common_fourier["Delta_t_candidate"]),
            "common_transport_interpreted_as_gauge": True,
        },
        "best_candidate": {
            "name": selected_candidate["name"],
            "sector_transport_rule": "B_10=I_3, B_bar5=F",
            "why_this_is_not_common_gauge": (
                "up uses 10_M x 10_M and cancels; down uses 10_M x bar5_M "
                "and sees the relative 10/bar5 transport"
            ),
            "Delta_t_candidate_symbolic": [
                symbolic_fourier_entry(0, 2),
                symbolic_fourier_entry(1, 2),
            ],
            "Delta_t_candidate_numeric": selected_candidate["Delta_t_candidate"],
            "magnitudes": [abs(entry) for entry in selected_candidate["Delta_t_candidate"]],
            "candidate_c1_heavy_link_primitives_packet": zero_c1_packet_from_candidate(
                selected_candidate["Delta_t_candidate"]
            ),
            "candidate_ckm_heavy_link_packet": ckm_packet_from_candidate(
                selected_candidate["Delta_t_candidate"]
            ),
        },
        "inverse_candidate": {
            "name": split_bar5_inverse["name"],
            "sector_transport_rule": "B_10=I_3, B_bar5=F^*",
            "Delta_t_candidate_symbolic": [
                symbolic_fourier_entry(0, 2, conjugate=True),
                symbolic_fourier_entry(1, 2, conjugate=True),
            ],
            "Delta_t_candidate_numeric": split_bar5_inverse["Delta_t_candidate"],
        },
        "what_this_would_close_if_selected": {
            "nonzero_character_trivial_heavy_link_direction": True,
            "basis_connection_entries_for_reduced_C1_packet": True,
            "leading_CKM_noncommutation_gate": True,
        },
        "still_open": {
            "MTT_selection_of_B10_Bbar5_transport": True,
            "whether_transport_is_finite_basis_change_or_C1_linear_response": True,
            "normalization_prefactor_from_selected_overlap_kernel": True,
            "canonical_kinetic_metric_and_full_Yukawa_matrices": True,
            "Jarlskog_and_CKM_angle_magnitudes": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "selected_by_MTT": False,
            "uses_benchmark_or_observed_flavor_data": False,
            "claims_selected_C1_response": False,
            "claims_selected_C6_support": False,
            "claims_CKM_angles_or_Jarlskog": False,
            "claims_full_SM_closure": False,
        },
        "verdict": {
            "representation_split_fourier_transport_is_a_viable_exact_candidate": True,
            "common_fourier_transport_is_not_viable_because_it_cancels": True,
            "candidate_promotes_missing_numbers_only_after_selection_theorem": True,
            "next_required_lemma": (
                "derive the 10_M/bar5_M relative qutrit Fourier transport from "
                "selected monad/Cech/Galerkin zero-mode data"
            ),
        },
    }


def main() -> int:
    print(json.dumps(encode(analyze()), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
