"""Derive finite orientation parity from the q79/q369 antiunitary pair."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

ANTIUNITARY_CERT = CERTS / "orientation_branch_antiunitary_equivalence_certificate.json"
Q79 = CANDIDATES / "iwasawa_route_c_branch_smoke" / "current_q79_orientation"
Q369 = CANDIDATES / "iwasawa_route_c_branch_smoke" / "conjugate_q369_orientation"
OUT_CANDIDATE = CANDIDATES / "orientation_observable_parity.candidate.json"
OUT_CERT = CERTS / "orientation_observable_parity_certificate.json"

TOL = 1e-9

FILE_SPECS = {
    "de_action.candidate.json": {
        "slot_key": "operator_slots",
        "matrix_keys": ["domain_gram", "range_gram", "D_E_matrix", "stiffness_matrix"],
        "vector_list_keys": ["ordered_zero_mode_basis"],
    },
    "reduced_green.candidate.json": {
        "slot_key": "green_slots",
        "matrix_keys": [
            "gram_matrix",
            "stiffness_matrix",
            "riesz_projector",
            "complement_projector",
            "reduced_green_operator",
        ],
        "vector_list_keys": [],
    },
    "dotd_response.candidate.json": {
        "slot_key": "dotd_response_slots",
        "matrix_keys": [
            "gram_matrix",
            "stiffness_matrix",
            "riesz_projector",
            "complement_projector",
            "reduced_green_operator",
            "dotD_alpha1_matrix",
        ],
        "vector_list_keys": [
            "ordered_zero_mode_basis",
            "source_vectors",
            "horizontal_response_vectors",
        ],
    },
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def parse_complex(value: Any) -> complex:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return complex(float(value), 0.0)
    if (
        isinstance(value, list)
        and len(value) == 2
        and all(isinstance(part, (int, float)) and not isinstance(part, bool) for part in value)
    ):
        return complex(float(value[0]), float(value[1]))
    raise ValueError(f"invalid complex entry {value!r}")


def parse_matrix(entry: Any) -> list[list[complex]]:
    matrix_data = entry.get("matrix") if isinstance(entry, dict) else entry
    return [[parse_complex(value) for value in row] for row in matrix_data]


def parse_vector_list(entry: Any) -> list[list[complex]]:
    return [[parse_complex(value) for value in vector] for vector in entry]


def sum_abs_sq_matrix(matrix: list[list[complex]]) -> float:
    return sum(abs(value) ** 2 for row in matrix for value in row)


def sum_abs_sq_vectors(vectors: list[list[complex]]) -> float:
    return sum(abs(value) ** 2 for vector in vectors for value in vector)


def sum_matrix(matrix: list[list[complex]]) -> complex:
    return sum((value for row in matrix for value in row), 0.0 + 0.0j)


def sum_vectors(vectors: list[list[complex]]) -> complex:
    return sum((value for vector in vectors for value in vector), 0.0 + 0.0j)


def is_square(matrix: list[list[complex]]) -> bool:
    return bool(matrix) and len(matrix) == len(matrix[0])


def trace(matrix: list[list[complex]]) -> complex:
    return sum(matrix[idx][idx] for idx in range(len(matrix)))


def determinant(matrix: list[list[complex]]) -> complex:
    if not is_square(matrix):
        raise ValueError("determinant needs a square matrix")
    size = len(matrix)
    work = [row[:] for row in matrix]
    det = 1.0 + 0.0j
    for col in range(size):
        pivot = None
        for row in range(col, size):
            if abs(work[row][col]) > TOL:
                pivot = row
                break
        if pivot is None:
            return 0.0 + 0.0j
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            det *= -1.0
        pivot_value = work[col][col]
        det *= pivot_value
        for row in range(col + 1, size):
            factor = work[row][col] / pivot_value
            for idx in range(col, size):
                work[row][idx] -= factor * work[col][idx]
    return det


def update_even(counter: dict[str, Any], left: float, right: float) -> None:
    diff = abs(left - right)
    counter["checks"] += 1
    counter["max_abs_error"] = max(counter["max_abs_error"], diff)
    if diff > TOL:
        counter["failures"] += 1


def update_conjugate(counter: dict[str, Any], left: complex, right: complex) -> None:
    diff = abs(right - left.conjugate())
    counter["checks"] += 1
    counter["max_abs_error"] = max(counter["max_abs_error"], diff)
    if diff > TOL:
        counter["failures"] += 1
    if abs(left.imag) > TOL and abs(right.imag) > TOL and left.imag * right.imag < 0:
        counter["nonzero_imaginary_sign_flips"] += 1


def analyze() -> dict[str, Any]:
    antiunitary = load(ANTIUNITARY_CERT)
    even = {"checks": 0, "failures": 0, "max_abs_error": 0.0}
    odd = {
        "checks": 0,
        "failures": 0,
        "max_abs_error": 0.0,
        "nonzero_imaginary_sign_flips": 0,
    }
    files: dict[str, Any] = {}

    for filename, spec in FILE_SPECS.items():
        q79_data = load(Q79 / filename)
        q369_data = load(Q369 / filename)
        slot_key = spec["slot_key"]
        file_even_start = even["checks"]
        file_odd_start = odd["checks"]
        for sector in sorted(q79_data[slot_key]):
            left_slot = q79_data[slot_key][sector]
            right_slot = q369_data[slot_key][sector]
            for key in spec["matrix_keys"]:
                left = parse_matrix(left_slot[key])
                right = parse_matrix(right_slot[key])
                update_even(even, sum_abs_sq_matrix(left), sum_abs_sq_matrix(right))
                update_conjugate(odd, sum_matrix(left), sum_matrix(right))
                if is_square(left) and is_square(right):
                    update_conjugate(odd, trace(left), trace(right))
                    update_conjugate(odd, determinant(left), determinant(right))
            for key in spec["vector_list_keys"]:
                left_vectors = parse_vector_list(left_slot[key])
                right_vectors = parse_vector_list(right_slot[key])
                update_even(
                    even,
                    sum_abs_sq_vectors(left_vectors),
                    sum_abs_sq_vectors(right_vectors),
                )
                update_conjugate(odd, sum_vectors(left_vectors), sum_vectors(right_vectors))
        files[filename] = {
            "cp_even_norm_checks": even["checks"] - file_even_start,
            "complex_conjugation_checks": odd["checks"] - file_odd_start,
        }

    closed = (
        antiunitary.get("summary", {}).get("antiunitary_equivalence_closed") is True
        and even["failures"] == 0
        and odd["failures"] == 0
    )

    report = {
        "calculation": "OrientationObservableParity",
        "status": "ORIENTATION_OBSERVABLE_PARITY_CLOSED_YUKAWA_VALUES_OPEN",
        "depends_on": [str(ANTIUNITARY_CERT.relative_to(ROOT))],
        "finite_operator_parity": {
            "files": files,
            "cp_even_norm_invariants": even,
            "complex_conjugation_invariants": odd,
            "finite_parity_closed": closed,
        },
        "conditional_yukawa_extension": {
            "if_selected_yukawa_pair_is_antiunitary_conjugate": {
                "singular_values_equal": True,
                "mass_ratios_equal": True,
                "ckm_angle_magnitudes_equal": True,
                "jarlskog_and_other_cp_odd_signs_reverse": True,
            },
            "current_selected_yukawa_matrices_absent": True,
            "not_a_mass_or_ckm_magnitude_calculation": True,
        },
        "what_this_closes": {
            "finite_operator_cp_even_parity": closed,
            "finite_operator_cp_odd_conjugation_parity": closed,
            "q79_q369_are_one_antiunitary_pair_at_current_finite_layer": closed,
        },
        "what_this_does_not_close": {
            "unique_m1_vs_m2_selection": False,
            "selected_source_origin": False,
            "selected_yukawa_matrices": False,
            "ckm_angles_or_mass_ratios": False,
            "jarlskog_value": False,
            "full_SM_closure": False,
        },
        "guardrails": {
            "claims_observed_cp_sign_selects_branch": False,
            "uses_observed_masses_or_mixings": False,
            "uses_benchmark_flavor_entries": False,
            "claims_selected_yukawas_computed": False,
            "claims_full_sm_closure": False,
        },
        "verdict": {
            "honest_answer": (
                "At the current finite operator layer, q79 and q369 have identical "
                "CP-even norm data and conjugate CP-odd orientation data.  Thus "
                "the branch pair can only be split by a selected source/retarded "
                "orientation theorem; masses and mixing magnitudes cannot select "
                "between exact antiunitary conjugates."
            ),
            "next_step": (
                "Either prove the retarded/source theorem selecting one orientation, "
                "or carry this parity rule forward to the future selected Yukawa "
                "matrices and compute CP-even values plus the CP-odd sign from the "
                "selected branch."
            ),
        },
    }
    return report


def main() -> int:
    report = analyze()
    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "OrientationObservableParity",
        "status": report["status"],
        "analysis_script": "scripts/derive_orientation_observable_parity.py",
        "candidate_data": str(OUT_CANDIDATE.relative_to(ROOT)),
        "finite_operator_parity": report["finite_operator_parity"],
        "conditional_yukawa_extension": report["conditional_yukawa_extension"],
        "what_this_closes": report["what_this_closes"],
        "what_this_does_not_close": report["what_this_does_not_close"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["finite_operator_parity"]["finite_parity_closed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
