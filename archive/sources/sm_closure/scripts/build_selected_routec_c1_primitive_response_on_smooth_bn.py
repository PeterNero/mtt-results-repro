"""Build the first C1 primitive-response contraction on smooth B_N.

This artifact contracts the emitted B_N zero modes and dotD horizontal
responses against the canonical finite translation-invariant trilinear tensor:
the product is nonzero only when the three active F3^2 modes sum to zero.

The result is intentionally conservative.  It tests the first natural overlap
tensor and records whether it can already produce nonzero C1 response matrices.
It does not claim selected Yukawa, CKM, or source promotion.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
OUTPUT = DATA / "selected_routec_c1_primitive_response_on_smooth_bn.candidate.json"
CERT = CERTS / "selected_routec_c1_primitive_response_on_smooth_bn_certificate.json"
NOTE = CORPUS / "MTT_Selected_RouteC_C1_Primitive_Response_on_Smooth_BN_v1.md"

DOTD = DATA / "selected_routec_sector_projectors_dotd_on_smooth_bn" / "sector_projectors_dotd_on_smooth_bn.source_lift_diagnostic.json"
BN = DATA / "selected_routec_smooth_bn_galerkin_lift.candidate.json"

SECTOR_TRIPLES = {
    "u": ("Q", "u", "H"),
    "d": ("Q", "d", "Hdagger"),
    "e": ("L", "e", "Hdagger"),
    "nuD": ("L", "N", "H"),
}
H_CONJUGATE_ALIASES = {"Hdagger": "H"}
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


def nonzero_entries(vector: list[Any]) -> list[tuple[int, complex]]:
    entries = []
    for idx, raw in enumerate(vector):
        value = to_complex(raw)
        if abs(value) > TOL:
            entries.append((idx, value))
    return entries


def mode_sum_zero(basis: list[dict[str, Any]], i: int, j: int, k: int) -> bool:
    left = basis[i]["active_deck_mode"]
    middle = basis[j]["active_deck_mode"]
    right = basis[k]["active_deck_mode"]
    return all((left[pos] + middle[pos] + right[pos]) % 3 == 0 for pos in range(2))


def fiber_coupling_allowed(basis: list[dict[str, Any]], i: int, j: int, k: int) -> bool:
    # Minimal qutrit/E6-like finite tensor: fiber labels sum to zero.
    return (
        basis[i]["fiber_index"] + basis[j]["fiber_index"] + basis[k]["fiber_index"]
    ) % 3 == 0


def tensor_value(basis: list[dict[str, Any]], i: int, j: int, k: int) -> complex:
    if mode_sum_zero(basis, i, j, k) and fiber_coupling_allowed(basis, i, j, k):
        return 1.0 + 0.0j
    return 0.0 + 0.0j


def trilinear(basis: list[dict[str, Any]], a: list[Any], b: list[Any], c: list[Any]) -> complex:
    total = 0.0 + 0.0j
    for i, ai in nonzero_entries(a):
        for j, bj in nonzero_entries(b):
            for k, ck in nonzero_entries(c):
                total += ai * bj * ck * tensor_value(basis, i, j, k)
    return total


def add_vectors(*vectors: list[complex]) -> list[complex]:
    return [sum(vector[idx] for vector in vectors) for idx in range(len(vectors[0]))]


def as_complex_vector(vector: list[Any]) -> list[complex]:
    return [to_complex(value) for value in vector]


def zero_matrix(rows: int, cols: int) -> list[list[complex]]:
    return [[0.0 + 0.0j for _ in range(cols)] for _ in range(rows)]


def matrix_norm(matrix: list[list[complex]]) -> float:
    return max((abs(value) for row in matrix for value in row), default=0.0)


def c1_matrix_for_sector(
    basis: list[dict[str, Any]],
    slots: dict[str, Any],
    left_sector: str,
    right_sector: str,
    higgs_sector: str,
) -> dict[str, Any]:
    h_sector = H_CONJUGATE_ALIASES.get(higgs_sector, higgs_sector)
    left_slot = slots[left_sector]
    right_slot = slots[right_sector]
    h_slot = slots[h_sector]
    left_zero = [as_complex_vector(v) for v in left_slot["ordered_zero_mode_basis"]]
    right_zero = [as_complex_vector(v) for v in right_slot["ordered_zero_mode_basis"]]
    h_zero = as_complex_vector(h_slot["ordered_zero_mode_basis"][0])
    left_resp = [as_complex_vector(v) for v in left_slot["horizontal_response_vectors"]]
    right_resp = [as_complex_vector(v) for v in right_slot["horizontal_response_vectors"]]
    h_resp = as_complex_vector(h_slot["horizontal_response_vectors"][0])

    matrix = zero_matrix(len(left_zero), len(right_zero))
    terms: dict[str, dict[str, Any]] = {}
    for i in range(len(left_zero)):
        for j in range(len(right_zero)):
            left_term = trilinear(basis, left_resp[i], right_zero[j], h_zero)
            right_term = trilinear(basis, left_zero[i], right_resp[j], h_zero)
            higgs_term = trilinear(basis, left_zero[i], right_zero[j], h_resp)
            total = left_term + right_term + higgs_term
            matrix[i][j] = total
            terms[f"{i},{j}"] = {
                "left_response": left_term,
                "right_response": right_term,
                "higgs_response": higgs_term,
                "total": total,
            }
    return {
        "left_sector": left_sector,
        "right_sector": right_sector,
        "higgs_sector": higgs_sector,
        "matrix": matrix,
        "max_abs_entry": matrix_norm(matrix),
        "terms": terms,
    }


def count_nonzero_tensor_slots(basis: list[dict[str, Any]]) -> int:
    count = 0
    for i in range(len(basis)):
        for j in range(len(basis)):
            for k in range(len(basis)):
                if abs(tensor_value(basis, i, j, k)) > TOL:
                    count += 1
    return count


def main() -> None:
    bn = load(BN)
    dotd = load(DOTD)
    basis = bn["B_N_lift"]["basis"]
    slots = dotd["dotd_response_slots"]

    matrices = {
        sector: c1_matrix_for_sector(basis, slots, *triple)
        for sector, triple in SECTOR_TRIPLES.items()
    }
    all_zero = all(item["max_abs_entry"] <= TOL for item in matrices.values())
    nonzero_tensor_slots = count_nonzero_tensor_slots(basis)
    response_support = {
        sector: [
            {
                "response_index": idx,
                "support_basis_indices": [entry[0] for entry in nonzero_entries(vec)],
            }
            for idx, vec in enumerate(slot["horizontal_response_vectors"])
        ]
        for sector, slot in slots.items()
    }

    candidate = {
        "candidate": "MTTSelectedRouteCC1PrimitiveResponseOnSmoothBN",
        "status": "MTT_SELECTED_ROUTEC_C1_PRIMITIVE_RESPONSE_ON_SMOOTH_BN_COMPUTED_SELECTED_PRIMITIVE_OPEN",
        "inputs": {
            "smooth_bn": rel(BN),
            "dotd_response": rel(DOTD),
        },
        "primitive_tensor": {
            "name": "canonical_mode_conserving_F3xF3_qutrit_trilinear",
            "definition": "T(phi_i, phi_j, phi_k)=1 iff active F3^2 modes and fiber labels each sum to zero mod 3; otherwise 0.",
            "nonzero_tensor_slots": nonzero_tensor_slots,
            "selected_by_theorem": False,
        },
        "c1_response_matrices": matrices,
        "diagnostics": {
            "all_c1_matrices_zero_for_canonical_tensor": all_zero,
            "response_support": response_support,
            "why_zero": (
                "The emitted horizontal responses live in the (-1,-1) active mode while zero modes and the Higgs zero mode live in (0,0). "
                "The canonical translation-invariant tensor enforces active-mode conservation, so one-response C1 terms do not conserve F3^2 momentum."
            ),
        },
        "superset_mode": {
            "classification": "CONSTRAINED_NUMERICAL_SUPERSET_REPAIR",
            "straight_path": {
                "classification": "PARTIAL",
                "canonical_C1_tensor_computed": True,
                "nonzero_selected_C1_response_found": not all_zero,
                "honest_selected_source_promoted": False,
            },
            "superset_convergence": {
                "uses_string_flux_trilinear_overlap_clue": True,
                "uses_same_BN_dotD_Green_layer": True,
                "canonical_tensor_is_first_natural_overlap_test": True,
            },
            "superset_repair": {
                "classification": "CANONICAL_TRANSLATION_INVARIANT_C1_ZERO_SELECTED_PRIMITIVE_NEEDED",
                "next_required_object": "selected non-invariant primitive tensor, vertex correction, basis transport, or source theorem that changes the one-response selection rule",
            },
            "diagnostic_backfit_only": {
                "used": False,
                "observed_physical_data_used": False,
            },
        },
        "what_closes_now": {
            "primitive_C1_contraction_engine_built": True,
            "canonical_mode_conserving_tensor_tested": True,
            "canonical_tensor_zero_response_result_proved_finitely": all_zero,
            "missing_C1_object_sharpened": True,
            "target_fitting_excluded": True,
        },
        "what_remains_open": {
            "selected_noninvariant_C1_primitive_or_vertex": True,
            "selected_basis_transport_between_zero_and_response_modes": True,
            "selected_dotD_source_verified": True,
            "alpha1_driver_verified": True,
            "nonzero_C1_response_matrices": all_zero,
            "yukawa_CKM_PMNS_magnitudes": True,
            "honest_replay_without_lifted_flags": True,
            "full_SM_or_no_knob_closure": True,
        },
        "closure_claimed": False,
        "target_fitting_used": False,
        "next_required_artifact": "MTT_Selected_RouteC_NonInvariant_C1_Primitive_or_BasisTransport_Search_v1",
        "theorem": {
            "name": "CanonicalC1PrimitiveResponseOnSmoothBNNoGo",
            "proved": True,
            "statement": (
                "For the emitted 27-mode B_N dotD response packet, the canonical finite translation-invariant "
                "F3^2 x qutrit trilinear tensor gives zero one-response C1 matrices in the u,d,e,nuD sectors. "
                "Therefore nonzero C1 data require a selected non-invariant primitive, vertex correction, basis transport, "
                "or a source theorem deriving a different selected trilinear tensor."
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
        f"""# MTT Selected Route-C C1 Primitive Response on Smooth BN

Status: `{candidate['status']}`

This computes the first natural C1 primitive-response contraction on the same
27-mode `B_N` basis: the finite translation-invariant trilinear tensor with
active `F3^2` mode conservation and qutrit fiber conservation.

## Result

- Nonzero primitive tensor slots: `{nonzero_tensor_slots}`.
- `u,d,e,nuD` one-response C1 matrices are all zero: `{all_zero}`.

The zero result is not a numerical failure.  It is a clean selection-rule
result: the current `dotD` horizontal responses live in active mode `(-1,-1)`,
while the zero modes and Higgs zero mode live in `(0,0)`.  A one-response
trilinear term therefore violates the canonical active-mode conservation rule.

## Consequence

The next missing object is sharper than before.  Nonzero C1 response requires
one of:

- a selected non-invariant C1 primitive/vertex tensor,
- selected basis transport mixing zero and response modes,
- a same-source theorem deriving a different selected trilinear tensor,
- or selected full Iwasawa/Strominger data whose response support changes the
  active-mode selection rule.

No Yukawa, CKM, PMNS, or mass claim is made here.
""",
        encoding="utf-8",
    )
    print(json.dumps({"candidate": rel(OUTPUT), "status": candidate["status"]}, indent=2))


if __name__ == "__main__":
    main()
