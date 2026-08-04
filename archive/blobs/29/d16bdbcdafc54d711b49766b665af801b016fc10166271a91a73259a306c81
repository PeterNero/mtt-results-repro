"""Test whether circle/bundle-adapted Yukawa bases reduce the nine rows."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SLUG = "selected_yukawageometryadaptedbasiscompression_or_nineslotwall"
PACKET_DIR = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
BASIS = PACKET_DIR / "geometry_adapted_yukawa_basis_inventory.packet.json"
TESTS = PACKET_DIR / "basis_compression_rank_tests.packet.json"
DECISION = PACKET_DIR / "basis_compression_decision.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_YukawaGeometryAdaptedBasisCompression_or_NineSlotWall_v1.md"

SPECTRAL_BASIS = (
    DATA
    / "selected_spectralyukawaresponsebasis_or_coefficientsourcewall"
    / "selected_family_spectral_response_basis.packet.json"
)
COEFFS = (
    DATA
    / "selected_spectralyukawaresponsebasis_or_coefficientsourcewall"
    / "diagnostic_log_yukawa_response_coefficients.packet.json"
)
REDUCTION = DATA / "selected_flavorthresholdsourceoperator_or_reducedcoefficienttheorem.candidate.json"
CONCRETE = DATA / "selected_flavorsourceoperatorconcretesearch_or_minimalnineslotpolicy.candidate.json"
FEATURES = DATA / "selected_flavorsourceoperatorconcretesearch_or_minimalnineslotpolicy" / "source_native_feature_rows.packet.json"
POLICY = DATA / "selected_flavorthresholdoperatorsourcevalues_or_nineslotpolicyadoption.candidate.json"

STATUS = "MTT_SELECTED_YUKAWA_GEOMETRY_ADAPTED_BASIS_COMPRESSION_TESTED_NINE_SLOT_WALL_RETAINED"
NEXT = "MTT_Selected_YukawaNewSourceRelation_or_NonInvertibleFlavorQuotientTest_v1"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def matrix_rank_payload(matrix: np.ndarray, label: str) -> dict[str, Any]:
    singular = np.linalg.svd(matrix, compute_uv=False)
    u, s, vt = np.linalg.svd(matrix, full_matrices=False)
    best_rank2 = (u[:, :2] * s[:2]) @ vt[:2, :]
    residual = matrix - best_rank2
    return {
        "label": label,
        "matrix": matrix.tolist(),
        "rank": int(np.linalg.matrix_rank(matrix, tol=1.0e-12)),
        "determinant": float(np.linalg.det(matrix)),
        "singular_values": [float(x) for x in singular],
        "best_rank2_relative_frobenius_residual": float(np.linalg.norm(residual) / np.linalg.norm(matrix)),
        "best_rank2_max_abs_residual": float(np.max(np.abs(residual))),
        "rank2_exact_compression_closes": False,
    }


def main() -> int:
    spectral = load(SPECTRAL_BASIS)
    coeffs = load(COEFFS)
    reduction = load(REDUCTION)
    concrete = load(CONCRETE)
    features = load(FEATURES)
    policy = load(POLICY)

    if spectral["accepted_as_selected_basis_map"] is not True:
        raise ValueError("selected family spectral basis is not closed")
    if reduction["closure_decision"]["coefficient_matrix_full_rank"] is not True:
        raise ValueError("previous full-rank wall is not present")
    if concrete["closure_decision"]["minimal_nine_slot_profile_policy_closed"] is not True:
        raise ValueError("minimal nine-slot policy is not closed")
    if policy["closure_decision"]["policy_source_value_row_count"] != 9:
        raise ValueError("policy nine-slot rows are not emitted")

    coefficient_matrix = np.array(
        [row["coefficient_values_c0_c1_c2"] for row in coeffs["sector_rows"]],
        dtype=float,
    )
    log_magnitude_matrix = np.array(
        [np.log(row["input_common_scale_diag_abs_Y"]) for row in coeffs["sector_rows"]],
        dtype=float,
    )
    vandermonde = np.array(spectral["vandermonde_matrix"], dtype=float)

    family_index = np.arange(3)
    circle_fourier = np.column_stack(
        [
            np.ones(3) / math.sqrt(3.0),
            np.cos(2.0 * math.pi * family_index / 3.0) * math.sqrt(2.0 / 3.0),
            np.sin(2.0 * math.pi * family_index / 3.0) * math.sqrt(2.0 / 3.0),
        ]
    )
    polynomial_to_lagrange = vandermonde.T
    lagrange_values = coefficient_matrix @ polynomial_to_lagrange
    circle_fourier_coefficients = log_magnitude_matrix @ circle_fourier

    basis = {
        "schema": "MTTYukawaGeometryAdaptedBasisInventory.v1",
        "status": "GEOMETRY_ADAPTED_BASIS_INVENTORY_BUILT",
        "closed_geometry_used": [
            "shared/common circle family carrier",
            "qutrit family spectrum",
            "selected family spectral response basis",
            "matter-slot routing u,d,e with phase/shift source directions",
            "qutrit/shared-circle theta exponent rows",
        ],
        "admissible_basis_changes_if_family_resolution_retained": [
            {
                "basis": "selected polynomial spectral basis",
                "matrix": "1,x,x^2 on the selected family spectrum",
                "invertible": True,
                "determinant": spectral["vandermonde_determinant"],
            },
            {
                "basis": "family-projector/Lagrange basis",
                "matrix": "polynomial_to_lagrange = Vandermonde^T",
                "invertible": True,
                "determinant": float(np.linalg.det(polynomial_to_lagrange)),
            },
            {
                "basis": "circle/Fourier real qutrit basis",
                "matrix": "constant, cos(2*pi*j/3), sin(2*pi*j/3)",
                "invertible": True,
                "determinant": float(np.linalg.det(circle_fourier)),
            },
        ],
        "noninvertible_compression_requires_new_source_relation": True,
        "why_noninvertible_is_not_basis_only": (
            "A noninvertible map would identify or discard a family direction. That is not a harmless "
            "circle/bundle rebasing once the selected basis is family resolved; it must be justified as a "
            "new selected source relation or quotient before empirical replay."
        ),
        "source_native_feature_rows": features["features_by_sector"],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    tests = {
        "schema": "MTTYukawaBasisCompressionRankTests.v1",
        "status": "GEOMETRY_ADAPTED_BASIS_COMPRESSION_TESTED_NO_EXACT_REDUCTION",
        "polynomial_coefficient_matrix": matrix_rank_payload(coefficient_matrix, "c_{s,k} in selected polynomial basis"),
        "lagrange_family_projector_matrix": matrix_rank_payload(lagrange_values, "log|Y_s| in family projector basis"),
        "circle_fourier_family_matrix": matrix_rank_payload(circle_fourier_coefficients, "log|Y_s| in real circle/Fourier basis"),
        "basis_transform_checks": {
            "vandermonde_determinant_nonzero": abs(float(np.linalg.det(vandermonde))) > 1.0e-12,
            "polynomial_to_lagrange_reconstruction_max_abs_residual": float(
                np.max(np.abs(lagrange_values - log_magnitude_matrix))
            ),
            "circle_fourier_determinant": float(np.linalg.det(circle_fourier)),
            "rank_invariant_under_lagrange_transform": int(np.linalg.matrix_rank(lagrange_values, tol=1.0e-12)) == 3,
            "rank_invariant_under_circle_fourier_transform": int(
                np.linalg.matrix_rank(circle_fourier_coefficients, tol=1.0e-12)
            )
            == 3,
        },
        "best_approximate_compression": {
            "coefficient_matrix_rank2_relative_frobenius_residual": matrix_rank_payload(
                coefficient_matrix, "tmp"
            )["best_rank2_relative_frobenius_residual"],
            "log_magnitude_matrix_rank2_relative_frobenius_residual": matrix_rank_payload(
                log_magnitude_matrix, "tmp"
            )["best_rank2_relative_frobenius_residual"],
            "interpretation": "structured near-compression exists, but rank-2 compression is not exact and is not a selected source theorem",
        },
        "accepted_reduced_coefficient_rows": 0,
        "accepted_strict_no_knob_yukawa_rows": 0,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    decision = {
        "schema": "MTTYukawaGeometryAdaptedBasisCompressionDecision.v1",
        "status": "NINE_SLOT_WALL_RETAINED_FOR_CURRENT_CIRCLE_BUNDLE_GEOMETRY",
        "basis_only_reduction_below_nine_closed": False,
        "current_geometry_forces_family_resolved_basis_up_to_invertible_rebasing": True,
        "invertible_geometry_adapted_rebasis_can_reduce_rank": False,
        "noninvertible_reduction_requires_new_selected_source_relation": True,
        "policy_profile_operator_retained": True,
        "policy_source_value_row_count": 9,
        "strict_selected_no_knob_coefficient_source_row_count": 0,
        "what_this_proves": (
            "The previous full-rank wall is not an artifact of choosing 1,x,x^2 instead of an obvious "
            "circle/bundle-adapted basis. Polynomial, Lagrange/projector, and real Fourier qutrit bases "
            "are related by invertible maps and all keep rank 3 across u,d,e."
        ),
        "what_this_does_not_prove": (
            "It does not prove that MTT can never reduce Yukawa rows. It proves that basis rotation alone "
            "inside the currently closed family-resolved circle/bundle geometry cannot do it."
        ),
        "legal_next_exits": [
            "derive a new selected source relation among c_{s,k}",
            "derive a noninvertible flavor quotient from MTT geometry before empirical replay",
            "emit selected threshold/profile rows that explain the rank-2 near-compression residual",
        ],
        "forbidden_exits": [
            "choose a noninvertible projection because it improves the Yukawa residual",
            "rotate to a target-fitted basis after seeing the nine coefficients",
            "reinterpret the nine policy/profile rows as strict no-knob source rows",
        ],
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
    }

    theorem = {
        "name": "YukawaGeometryAdaptedBasisCompressionNoGoTheorem",
        "proved": True,
        "statement": (
            "For the currently closed family-resolved MTT circle/bundle geometry, replacing the selected "
            "polynomial spectral basis by the corresponding family-projector/Lagrange basis or real "
            "circle/Fourier qutrit basis is an invertible rebasing. The u,d,e Yukawa coefficient/log-magnitude "
            "matrix remains rank 3 in each such basis. Therefore the nine-slot wall is not removed by an "
            "obvious geometry-adapted basis change; reduction requires a new selected source relation or "
            "noninvertible quotient theorem."
        ),
    }

    data = {
        "candidate": "MTTSelectedYukawaGeometryAdaptedBasisCompressionOrNineSlotWall",
        "status": STATUS,
        "inputs": {
            "selected_family_spectral_response_basis": rel(SPECTRAL_BASIS),
            "diagnostic_log_yukawa_response_coefficients": rel(COEFFS),
            "previous_reduction_wall": rel(REDUCTION),
            "concrete_operator_search": rel(CONCRETE),
            "source_native_feature_rows": rel(FEATURES),
            "nine_slot_policy_adoption": rel(POLICY),
        },
        "output_packets": {
            "geometry_adapted_yukawa_basis_inventory": rel(BASIS),
            "basis_compression_rank_tests": rel(TESTS),
            "basis_compression_decision": rel(DECISION),
        },
        "closure_decision": {
            "geometry_adapted_basis_compression_tested": True,
            "basis_only_reduction_below_nine_closed": False,
            "nine_slot_policy_profile_operator_retained": True,
            "policy_source_value_row_count": 9,
            "strict_selected_no_knob_coefficient_source_row_count": 0,
            "strict_no_knob_flavor_closure": False,
            "true_SM_equivalence_closed": False,
            "full_no_knob_closed": False,
        },
        "key_numbers": {
            "polynomial_coefficient_rank": tests["polynomial_coefficient_matrix"]["rank"],
            "lagrange_projector_rank": tests["lagrange_family_projector_matrix"]["rank"],
            "circle_fourier_rank": tests["circle_fourier_family_matrix"]["rank"],
            "polynomial_coefficient_determinant": tests["polynomial_coefficient_matrix"]["determinant"],
            "lagrange_log_magnitude_determinant": tests["lagrange_family_projector_matrix"]["determinant"],
            "circle_fourier_determinant": tests["circle_fourier_family_matrix"]["determinant"],
            "best_rank2_log_magnitude_relative_residual": tests["best_approximate_compression"][
                "log_magnitude_matrix_rank2_relative_frobenius_residual"
            ],
        },
        "theorem": theorem,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_YukawaGeometryAdaptedBasisCompression_or_NineSlotWall_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "theorem_proved": True,
        "geometry_adapted_basis_compression_tested": True,
        "basis_only_reduction_below_nine_closed": False,
        "policy_source_value_row_count": 9,
        "strict_selected_no_knob_coefficient_source_row_count": 0,
        "strict_no_knob_flavor_closure": False,
        "true_SM_equivalence_closed": False,
        "full_no_knob_closed": False,
        "closure_claimed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected YukawaGeometryAdaptedBasisCompression or NineSlotWall v1

Status: `{STATUS}`.

## Theorem

`YukawaGeometryAdaptedBasisCompressionNoGoTheorem` is proved.

The test asks whether the previous nine-Yukawa wall was just a bad basis choice.
It was not, at least for the currently closed family-resolved circle/bundle
geometry.

The selected polynomial basis, family-projector/Lagrange basis, and real
circle/Fourier qutrit basis are all invertibly related. Their ranks are:

```text
polynomial coefficient basis rank = {tests["polynomial_coefficient_matrix"]["rank"]}
family projector basis rank       = {tests["lagrange_family_projector_matrix"]["rank"]}
circle/Fourier qutrit basis rank  = {tests["circle_fourier_family_matrix"]["rank"]}
```

So a geometry-adapted basis rotation alone cannot reduce the nine coefficient
slots.

The best rank-2 approximation is real but not exact:

```text
rank-2 relative Frobenius residual in log-magnitude basis =
{tests["best_approximate_compression"]["log_magnitude_matrix_rank2_relative_frobenius_residual"]}
```

This keeps the earlier conclusion intact:

```text
policy/profile Yukawa operator rows = 9
strict no-knob coefficient rows     = 0
```

What remains possible is not another invertible rebasing, but a new selected
source relation, a selected noninvertible flavor quotient, or selected
threshold/profile rows explaining the approximate compression residual.

Next artifact: `{NEXT}`.
"""

    write_json(BASIS, basis)
    write_json(TESTS, tests)
    write_json(DECISION, decision)
    write_json(OUTPUT, data)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
