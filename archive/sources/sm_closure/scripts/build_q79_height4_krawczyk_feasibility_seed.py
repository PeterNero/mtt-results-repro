from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A384 = VALIDATED / "n3.rank3.residual_jacobian.interval.json"
A385S = VALIDATED / "n3.pgl3.polydisk_chart_source.json"
A385A = VALIDATED / "n3.pgl3.centered_affine_hessian_source.json"
A386 = VALIDATED / "n3.rank3.residual.a386.json"
OUTPUT = VALIDATED / "n3.rank3.krawczyk.seed.a387.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourKrawczykFeasibilitySeed_A387_v1.md"
ARTIFACT = "A387"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def encoded_complex(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def upper(value: float) -> float:
    return math.nextafter(float(value), math.inf)


def positive_matvec_upper(matrix: np.ndarray, vector: np.ndarray) -> np.ndarray:
    result = np.zeros(matrix.shape[0], dtype=np.float64)
    for row in range(matrix.shape[0]):
        total = 0.0
        for column in range(matrix.shape[1]):
            product = upper(matrix[row, column] * vector[column])
            total = upper(total + product)
        result[row] = total
    return result


def post_fixed_point_upper(constant: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    spectral_radius = float(np.max(abs(np.linalg.eigvals(matrix))))
    if not spectral_radius < 1.0:
        raise ArithmeticError("positive Krawczyk defect matrix is not contractive")
    candidate = np.linalg.solve(np.eye(matrix.shape[0]) - matrix, constant)
    candidate = np.nextafter(np.maximum(candidate, 0.0), math.inf)
    for _ in range(128):
        image = np.nextafter(constant + positive_matvec_upper(matrix, candidate), math.inf)
        if bool(np.all(image <= candidate)):
            return candidate
        candidate = np.nextafter(np.maximum(candidate, image) * (1.0 + 1.0e-12), math.inf)
    raise ArithmeticError("failed to construct a positive post-fixed point")


def scaled_point_radius(
    center_correction: np.ndarray,
    error_correction: np.ndarray,
    defect: np.ndarray,
    scale: float,
) -> np.ndarray:
    constant = np.nextafter(center_correction + scale * error_correction, math.inf)
    return post_fixed_point_upper(constant, defect)


def maximum_residual_scale_for_radius(
    center_correction: np.ndarray,
    error_correction: np.ndarray,
    defect: np.ndarray,
    coordinate_disk_radius: float,
) -> float:
    if float(np.max(scaled_point_radius(center_correction, error_correction, defect, 0.0))) > coordinate_disk_radius:
        return 0.0
    if float(np.max(scaled_point_radius(center_correction, error_correction, defect, 1.0))) <= coordinate_disk_radius:
        return 1.0
    low = 0.0
    high = 1.0
    for _ in range(80):
        middle = (low + high) / 2.0
        if float(np.max(scaled_point_radius(center_correction, error_correction, defect, middle))) <= coordinate_disk_radius:
            low = middle
        else:
            high = middle
    return low


def main() -> int:
    jacobian = load(A384)
    chart = load(A385S)
    affine_source = load(A385A)
    residual = load(A386)
    if jacobian.get("artifact") != "A384":
        raise AssertionError("A387 requires A384")
    if chart.get("artifact") != "A385S" or affine_source.get("artifact") != "A385A":
        raise AssertionError("A387 requires the A385 chart and affine source")
    if residual.get("artifact") != "A386":
        raise AssertionError("A387 requires the Hessian-aligned A386 residual")

    residual_centers = np.asarray(
        [complex_value(row["residual_interval_center"]) for row in residual["residue_rows"]],
        dtype=np.complex128,
    )
    residual_radii = np.asarray(
        [float(row["residual_component_radius_upper"]) for row in residual["residue_rows"]],
        dtype=np.float64,
    )
    floating_residual = np.asarray(
        [complex_value(row["floating_residual_diagnostic_only"]) for row in residual["residue_rows"]],
        dtype=np.complex128,
    )
    inverse = np.asarray(
        [[complex_value(value) for value in row] for row in jacobian["center_inverse_8_by_8"]],
        dtype=np.complex128,
    )
    midpoint_correction = -(inverse @ residual_centers)
    floating_correction = -(inverse @ floating_residual)
    floating_correction_bounds = np.nextafter(abs(floating_correction), math.inf)
    # Recenter the rigorous A386 disks on the independent floating diagnostic.
    # This does not make the diagnostic a bound: the added center displacement
    # preserves the complete A386 enclosure.
    floating_recentered_radii = np.nextafter(
        residual_radii + abs(residual_centers - floating_residual), math.inf
    )
    correction_error_bounds = positive_matvec_upper(
        abs(inverse), floating_recentered_radii
    )
    defect = np.asarray(
        jacobian["verified_interval_nonsingularity"][
            "componentwise_preconditioned_defect_upper_8_by_8"
        ],
        dtype=np.float64,
    )
    defect = np.nextafter(defect, math.inf)
    spectral_radius = float(np.max(abs(np.linalg.eigvals(defect))))
    floating_nominal_radii = scaled_point_radius(
        floating_correction_bounds, correction_error_bounds, defect, 0.0
    )
    rigorous_point_radii = scaled_point_radius(
        floating_correction_bounds, correction_error_bounds, defect, 1.0
    )

    chart_rows = chart["charts"]
    requested_radii = {
        float(row["coordinate_complex_box"]["real_radius_requested"])
        for row in chart_rows
    }
    if len(requested_radii) != 1:
        raise AssertionError("A385S y/z coordinate radii differ")
    requested_radius = requested_radii.pop()
    selected_disk_radius = math.sqrt(2.0) * requested_radius
    nominal_required_disk = float(np.max(floating_nominal_radii))
    rigorous_required_disk = float(np.max(rigorous_point_radii))
    nominal_required_square = nominal_required_disk / math.sqrt(2.0)
    rigorous_required_square = rigorous_required_disk / math.sqrt(2.0)

    radius_trials = sorted(
        {
            requested_radius,
            upper(nominal_required_square),
            1.0e-6,
            2.0e-6,
            1.0e-5,
            1.0e-4,
            1.0e-3,
            upper(rigorous_required_square),
        }
    )
    trials = []
    for square_radius in radius_trials:
        disk_radius = math.sqrt(2.0) * square_radius
        residual_scale = maximum_residual_scale_for_radius(
            floating_correction_bounds,
            correction_error_bounds,
            defect,
            disk_radius,
        )
        trials.append(
            {
                "real_and_imaginary_coordinate_radius": square_radius,
                "enclosing_complex_disk_radius": disk_radius,
                "floating_seed_point_Krawczyk_image_fits": nominal_required_disk <= disk_radius,
                "full_A386_point_Krawczyk_image_fits": rigorous_required_disk <= disk_radius,
                "maximum_uniform_A386_residual_radius_scale_for_point_test": residual_scale,
                "required_uniform_residual_tightening_factor_if_finite": (
                    1.0 / residual_scale if residual_scale > 0.0 else None
                ),
                "whole_polydisk_Jacobian_transport_included": False,
            }
        )

    payload = {
        "schema": "MTTQ79HeightFourKrawczykFeasibilitySeed.v1",
        "status": "A384_A386_POINT_KRAWCZYK_SCALE_DIAGNOSTIC_EXECUTED",
        "artifact": ARTIFACT,
        "point_model": (
            "Y=A384 serialized center inverse; the numerical seed uses the "
            "independent A386 floating residual, while the rigorous residual "
            "disk is recentered on that diagnostic with its full enclosure "
            "retained; B is the A384 certified point-Jacobian defect"
        ),
        "interval_box_midpoint_preconditioned_correction_diagnostic": [
            encoded_complex(value) for value in midpoint_correction
        ],
        "floating_residual_newton_seed": [
            encoded_complex(value) for value in floating_correction
        ],
        "floating_residual_l2_norm": float(np.linalg.norm(floating_residual)),
        "floating_newton_seed_absolute_uppers": floating_correction_bounds.tolist(),
        "A386_rigorous_radii_recentered_on_floating_diagnostic": (
            floating_recentered_radii.tolist()
        ),
        "A386_residual_uncertainty_correction_uppers": correction_error_bounds.tolist(),
        "point_preconditioned_defect": {
            "componentwise_upper_8_by_8": defect.tolist(),
            "spectral_radius_diagnostic": spectral_radius,
            "A384_weighted_infinity_contraction_upper": float(
                jacobian["summary"]["preconditioned_weighted_infinity_contraction_upper"]
            ),
        },
        "minimal_point_Krawczyk_product_disks": {
            "floating_seed_only_coordinate_radii": floating_nominal_radii.tolist(),
            "full_A386_residual_interval_coordinate_radii": rigorous_point_radii.tolist(),
            "floating_seed_maximum_complex_disk_radius": nominal_required_disk,
            "full_A386_maximum_complex_disk_radius": rigorous_required_disk,
            "floating_seed_equivalent_real_imaginary_square_radius": nominal_required_square,
            "full_A386_equivalent_real_imaginary_square_radius": rigorous_required_square,
        },
        "selected_A385S_chart_test": {
            "real_and_imaginary_coordinate_radius": requested_radius,
            "enclosing_complex_disk_radius": selected_disk_radius,
            "floating_residual_newton_seed_maximum_absolute": float(
                np.max(abs(floating_correction))
            ),
            "floating_seed_point_Krawczyk_image_fits": (
                nominal_required_disk <= selected_disk_radius
            ),
            "full_A386_point_Krawczyk_image_fits": rigorous_required_disk <= selected_disk_radius,
            "failed_sufficient_test_does_not_prove_absence_of_a_zero": True,
        },
        "radius_and_residual_precision_trials": trials,
        "A385A_current_local_source": {
            "real_and_imaginary_coordinate_radius": requested_radius,
            "maximum_covariant_centered_disk_radius_upper": float(
                affine_source["summary"]["maximum_covariant_centered_disk_radius_upper"]
            ),
            "maximum_beta_forcing_centered_disk_radius_upper": float(
                affine_source["summary"]["maximum_beta_forcing_centered_disk_radius_upper"]
            ),
            "maximum_affine_reduction_weighted_contraction_upper": float(
                affine_source["summary"]["maximum_affine_reduction_weighted_contraction_upper"]
            ),
            "larger_radius_extrapolation_permitted": False,
        },
        "authority": {
            "A384_point_residual_Jacobian": authority(A384),
            "A385S_selected_polydisk_chart": authority(A385S),
            "A385A_centered_affine_source": authority(A385A),
            "A386_Hessian_aligned_residual": authority(A386),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "floating_residual_Newton_seed_computed": True,
            "interval_box_midpoint_not_treated_as_true_residual": True,
            "A386_residual_uncertainty_propagated": True,
            "A384_point_Jacobian_defect_propagated": True,
            "current_A385S_sufficient_point_Krawczyk_test_passed": (
                rigorous_required_disk <= selected_disk_radius
            ),
            "failure_of_sufficient_test_promoted_to_nonexistence": False,
            "Jacobian_polydisk_extension_closed": False,
            "wall_free_polydisk_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "retain the existing A385 chart and replace independently added A386 "
            "source radii by a coupled/correlation-preserving residual enclosure; "
            "then transport the Jacobian over that wall-free box"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Krawczyk Feasibility Seed (A387) v1\n\n"
        "A387 combines the tightened A386 value enclosure with the certified A384 "
        "point Jacobian. It separates the floating Newton seed from the midpoint "
        "of the much wider rigorous residual box and executes a componentwise "
        "positive Krawczyk scale diagnostic.\n\n"
        f"The independent floating residual norm is `{np.linalg.norm(floating_residual):.12g}` "
        f"and its Newton seed has maximum absolute value "
        f"`{np.max(abs(floating_correction)):.12g}`. Including the A384 point-Jacobian "
        f"defect, its product-disk radius is `{nominal_required_disk:.12g}`. "
        f"Including the dependency-forgetting A386 residual widths raises that "
        f"point-test radius to `{rigorous_required_disk:.12g}`.\n\n"
        f"The current A385S complex disk radius is `{selected_disk_radius:.12g}`, "
        "which contains the floating seed, but the full A386 sufficient point "
        "test does not pass. This is not a "
        "nonexistence result: the whole-polydisk Jacobian is not yet transported, "
        "and the A386 residual still loses beta-period cancellation. The packet "
        "fixes the numerical scales for those two remaining constructions.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["minimal_point_Krawczyk_product_disks"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
