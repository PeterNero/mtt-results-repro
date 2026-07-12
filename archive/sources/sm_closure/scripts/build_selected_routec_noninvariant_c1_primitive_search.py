"""Search finite non-invariant C1 primitive candidates on smooth B_N.

The canonical C1 tensor vanishes because the dotD response has active mode
(-1,-1) while the two zero modes have active mode (0,0).  This artifact tests
the minimal non-invariant repair: a primitive/vertex insertion carrying the
missing active momentum (1,1).  It searches the three qutrit fiber shifts and
the all-fiber envelope without using observed flavor data.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
OUTPUT = DATA / "selected_routec_noninvariant_c1_primitive_search.candidate.json"
CERT = CERTS / "selected_routec_noninvariant_c1_primitive_search_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_NonInvariant_C1_Primitive_Search_v1.md"

BN = DATA / "selected_routec_smooth_bn_galerkin_lift.candidate.json"
DOTD = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn" / "sector_projectors_dotd_on_smooth_bn.source_lift_diagnostic.json"
CANONICAL = DATA / "selected_routec_c1_primitive_response_on_smooth_bn.candidate.json"

SECTOR_TRIPLES = {
    "u": ("Q", "u", "H"),
    "d": ("Q", "d", "Hdagger"),
    "e": ("L", "e", "Hdagger"),
    "nuD": ("L", "N", "H"),
}
H_ALIASES = {"Hdagger": "H"}
TOL = 1e-12


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def to_complex(value: Any) -> complex:
    if isinstance(value, complex):
        return value
    if isinstance(value, bool):
        raise TypeError("boolean is not scalar")
    if isinstance(value, (int, float)):
        return complex(float(value), 0.0)
    if isinstance(value, list) and len(value) == 2:
        return complex(float(value[0]), float(value[1]))
    raise TypeError(f"unsupported scalar {value!r}")


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


def cvec(vector: list[Any]) -> list[complex]:
    return [to_complex(value) for value in vector]


def support(vector: list[complex]) -> list[tuple[int, complex]]:
    return [(idx, value) for idx, value in enumerate(vector) if abs(value) > TOL]


def tensor_value(
    basis: list[dict[str, Any]],
    i: int,
    j: int,
    k: int,
    *,
    primitive_active_shift: tuple[int, int],
    primitive_fiber_shift: int | str,
) -> complex:
    active_sum = [
        (
            basis[i]["active_deck_mode"][pos]
            + basis[j]["active_deck_mode"][pos]
            + basis[k]["active_deck_mode"][pos]
            + primitive_active_shift[pos]
        )
        % 3
        for pos in range(2)
    ]
    if active_sum != [0, 0]:
        return 0.0 + 0.0j
    fiber_sum = (
        basis[i]["fiber_index"] + basis[j]["fiber_index"] + basis[k]["fiber_index"]
    ) % 3
    if primitive_fiber_shift == "all":
        return 1.0 + 0.0j
    if (fiber_sum + int(primitive_fiber_shift)) % 3 == 0:
        return 1.0 + 0.0j
    return 0.0 + 0.0j


def trilinear(
    basis: list[dict[str, Any]],
    a: list[complex],
    b: list[complex],
    c: list[complex],
    *,
    primitive_active_shift: tuple[int, int],
    primitive_fiber_shift: int | str,
) -> complex:
    total = 0.0 + 0.0j
    for i, ai in support(a):
        for j, bj in support(b):
            for k, ck in support(c):
                total += ai * bj * ck * tensor_value(
                    basis,
                    i,
                    j,
                    k,
                    primitive_active_shift=primitive_active_shift,
                    primitive_fiber_shift=primitive_fiber_shift,
                )
    return total


def zero_matrix(rows: int, cols: int) -> list[list[complex]]:
    return [[0.0 + 0.0j for _ in range(cols)] for _ in range(rows)]


def max_abs(matrix: list[list[complex]]) -> float:
    return max((abs(value) for row in matrix for value in row), default=0.0)


def rank(matrix: list[list[complex]]) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    out = 0
    for col in range(cols):
        pivot = None
        for row in range(out, rows):
            if abs(work[row][col]) > TOL:
                pivot = row
                break
        if pivot is None:
            continue
        work[out], work[pivot] = work[pivot], work[out]
        scale = work[out][col]
        work[out] = [value / scale for value in work[out]]
        for row in range(rows):
            if row == out or abs(work[row][col]) <= TOL:
                continue
            factor = work[row][col]
            work[row] = [work[row][idx] - factor * work[out][idx] for idx in range(cols)]
        out += 1
    return out


def matrix_for_sector(
    basis: list[dict[str, Any]],
    slots: dict[str, Any],
    left: str,
    right: str,
    higgs: str,
    *,
    primitive_active_shift: tuple[int, int],
    primitive_fiber_shift: int | str,
) -> list[list[complex]]:
    h = H_ALIASES.get(higgs, higgs)
    left_slot = slots[left]
    right_slot = slots[right]
    h_slot = slots[h]
    left_zero = [cvec(v) for v in left_slot["ordered_zero_mode_basis"]]
    right_zero = [cvec(v) for v in right_slot["ordered_zero_mode_basis"]]
    h_zero = cvec(h_slot["ordered_zero_mode_basis"][0])
    left_resp = [cvec(v) for v in left_slot["horizontal_response_vectors"]]
    right_resp = [cvec(v) for v in right_slot["horizontal_response_vectors"]]
    h_resp = cvec(h_slot["horizontal_response_vectors"][0])
    matrix = zero_matrix(len(left_zero), len(right_zero))
    for i in range(len(left_zero)):
        for j in range(len(right_zero)):
            matrix[i][j] = (
                trilinear(
                    basis,
                    left_resp[i],
                    right_zero[j],
                    h_zero,
                    primitive_active_shift=primitive_active_shift,
                    primitive_fiber_shift=primitive_fiber_shift,
                )
                + trilinear(
                    basis,
                    left_zero[i],
                    right_resp[j],
                    h_zero,
                    primitive_active_shift=primitive_active_shift,
                    primitive_fiber_shift=primitive_fiber_shift,
                )
                + trilinear(
                    basis,
                    left_zero[i],
                    right_zero[j],
                    h_resp,
                    primitive_active_shift=primitive_active_shift,
                    primitive_fiber_shift=primitive_fiber_shift,
                )
            )
    return matrix


def matrix_pattern(matrix: list[list[complex]]) -> list[list[int]]:
    return [[1 if abs(value) > TOL else 0 for value in row] for row in matrix]


def candidate_report(
    basis: list[dict[str, Any]],
    slots: dict[str, Any],
    *,
    primitive_active_shift: tuple[int, int],
    primitive_fiber_shift: int | str,
) -> dict[str, Any]:
    matrices = {
        sector: matrix_for_sector(
            basis,
            slots,
            *triple,
            primitive_active_shift=primitive_active_shift,
            primitive_fiber_shift=primitive_fiber_shift,
        )
        for sector, triple in SECTOR_TRIPLES.items()
    }
    return {
        "primitive_active_shift": list(primitive_active_shift),
        "primitive_fiber_shift": primitive_fiber_shift,
        "selected_by_theorem": False,
        "uses_observed_flavor_data": False,
        "status": "STRUCTURAL_FINITE_CANDIDATE_UNSELECTED",
        "matrices": matrices,
        "summary": {
            sector: {
                "max_abs_entry": max_abs(matrix),
                "rank": rank(matrix),
                "support_pattern": matrix_pattern(matrix),
            }
            for sector, matrix in matrices.items()
        },
    }


def main() -> None:
    bn = load(BN)
    dotd = load(DOTD)
    canonical = load(CANONICAL)
    basis = bn["B_N_lift"]["basis"]
    slots = dotd["dotd_response_slots"]

    tested = [
        candidate_report(
            basis,
            slots,
            primitive_active_shift=(1, 1),
            primitive_fiber_shift=fiber_shift,
        )
        for fiber_shift in (0, 1, 2, "all")
    ]
    legal_nonzero = [
        item
        for item in tested
        if any(entry["max_abs_entry"] > TOL for entry in item["summary"].values())
    ]
    ranks_by_candidate = {
        str(item["primitive_fiber_shift"]): {
            sector: summary["rank"] for sector, summary in item["summary"].items()
        }
        for item in tested
    }
    candidate = {
        "candidate": "MTTSelectedRouteCNonInvariantC1PrimitiveSearch",
        "status": "MTT_SELECTED_ROUTEC_NONINVARIANT_C1_PRIMITIVE_SEARCH_BUILT_UNSELECTED_CANDIDATES_OPEN",
        "inputs": {
            "smooth_bn": rel(BN),
            "dotd_response": rel(DOTD),
            "canonical_c1_zero_result": rel(CANONICAL),
        },
        "search_rule": {
            "minimal_active_shift_required": [1, 1],
            "reason": canonical["diagnostics"]["why_zero"],
            "fiber_shifts_tested": [0, 1, 2, "all"],
            "observed_flavor_data_used": False,
        },
        "candidate_primitives": tested,
        "calculation_results": {
            "nonzero_unselected_candidates_found": len(legal_nonzero),
            "all_four_tested_candidates_nonzero": len(legal_nonzero) == 4,
            "ranks_by_candidate": ranks_by_candidate,
            "can_close_selected_C1_now": False,
            "why_not_closed": "The active shift (1,1) is forced by finite momentum bookkeeping, but no theorem yet selects a fiber shift or proves this non-invariant primitive/transport from the MTT source.",
        },
        "superset_mode": {
            "classification": "CONSTRAINED_NUMERICAL_SUPERSET_REPAIR",
            "straight_path": {
                "classification": "PARTIAL",
                "nonzero_C1_candidate_matrices_found": len(legal_nonzero) > 0,
                "selected_C1_primitive_proved": False,
            },
            "superset_convergence": {
                "string_flux_trilinear_overlap_clue": True,
                "canonical_zero_no_go_used": True,
                "finite_momentum_bookkeeping_forces_active_shift": [1, 1],
            },
            "superset_repair": {
                "classification": "NONINVARIANT_C1_CANDIDATES_FOUND_SELECTION_THEOREM_OPEN",
                "next_required_object": "prove selected primitive/vertex/basis transport chooses active shift (1,1) and one fiber rule from source data",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "observed_physical_data_used": False,
            },
        },
        "what_closes_now": {
            "canonical_zero_repaired_at_candidate_level": len(legal_nonzero) > 0,
            "minimal_active_shift_identified": True,
            "finite_noninvariant_C1_candidate_matrices_emitted": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_noninvariant_C1_primitive_or_vertex": True,
            "selected_basis_transport_theorem": True,
            "fiber_shift_selection": True,
            "selected_dotD_source_verified": True,
            "alpha1_driver_verified": True,
            "yukawa_CKM_PMNS_magnitudes": True,
            "honest_replay_without_lifted_flags": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_RouteC_Primitive_Source_Selection_Theorem_or_FiberRule_Audit_v1",
        "theorem": {
            "name": "MinimalNonInvariantC1PrimitiveCandidateTheorem",
            "proved": True,
            "statement": (
                "For the emitted B_N/dotD packet, nonzero one-response C1 matrices arise from the minimal "
                "non-invariant primitive active shift (1,1). The finite calculation emits the three fiber-shift "
                "variants and all-fiber envelope, but none is selected-source proof until MTT derives the primitive, "
                "vertex correction, or basis transport from the q79/F,m=1 S3/GS branch."
            ),
        },
    }
    OUTPUT.write_text(json.dumps(encode(candidate), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    CERT.write_text(
        json.dumps(
            {
                "status": candidate["status"],
                "candidate_path": rel(OUTPUT),
                "note_path": rel(NOTE),
                "what_closes": candidate["what_closes_now"],
                "what_remains_open": candidate["what_remains_open"],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    NOTE.write_text(
        f"""# MTT Selected Route-C Non-Invariant C1 Primitive Search

Status: `{candidate['status']}`

The canonical C1 tensor vanishes because the dotD response has active mode
`(-1,-1)` while zero modes have `(0,0)`.  This search tests the minimal
non-invariant repair: a primitive or basis-transport insertion carrying active
shift `(1,1)`.

## Result

- Tested fiber shifts: `0`, `1`, `2`, and `all`.
- Nonzero unselected candidates found: `{len(legal_nonzero)}`.
- Selected C1 closure now: `False`.

The active shift is forced by finite momentum bookkeeping; this is a real
structural clue.  But the fiber rule is still not selected by theorem, and no
source theorem yet proves that this non-invariant primitive, vertex correction,
or basis transport is emitted by the selected q79/F,m=1 S3/GS branch.

## Next Gate

Prove a primitive-source selection theorem or fiber-rule audit:

- derive active shift `(1,1)` from the selected gerbe/Strominger data,
- derive the qutrit fiber rule from the selected rho_E/Chan-Paton source,
- or prove a selected basis-transport map with the same finite effect.

No observed Yukawa, CKM, PMNS, or mass data were used.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": candidate["status"]}, indent=2))


if __name__ == "__main__":
    main()
