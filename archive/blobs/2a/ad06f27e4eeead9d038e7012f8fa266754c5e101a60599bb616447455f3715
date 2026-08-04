from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np

import build_q79_height4_krawczyk_feasibility_seed as seed


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
A387 = VALIDATED / "n3.rank3.krawczyk.seed.a387.json"
A394 = VALIDATED / "n3.rank3.residual.a394.json"
OUTPUT = VALIDATED / "n3.rank3.krawczyk.seed.a395.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourAugmentedBetaKrawczykSeed_A395_v1.md"
ARTIFACT = "A395"


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


def authorities_current(packet: dict) -> bool:
    for row in packet.get("authority", {}).values():
        path = ROOT / row["path"]
        if not path.exists() or sha256(path) != row["sha256"]:
            return False
    return True


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def encoded_complex(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def main() -> int:
    jacobian = load(A384)
    chart = load(A385S)
    affine_source = load(A385A)
    old_seed = load(A387)
    residual = load(A394)
    if jacobian.get("artifact") != "A384" or not authorities_current(jacobian):
        raise AssertionError("A395 requires a current A384 Jacobian packet")
    if (
        chart.get("artifact") != "A385S"
        or affine_source.get("artifact") != "A385A"
        or not authorities_current(chart)
        or not authorities_current(affine_source)
    ):
        raise AssertionError("A395 requires current A385 chart and affine packets")
    if old_seed.get("artifact") != "A387" or not authorities_current(old_seed):
        raise AssertionError("A395 requires the current A387 comparison packet")
    if (
        residual.get("artifact") != "A394"
        or not residual["strict_scope"]["residual_interval_strictly_tighter_than_A386"]
        or not authorities_current(residual)
    ):
        raise AssertionError("A395 requires a current, tightened A394 residual")

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
    floating_recentered_radii = np.nextafter(
        residual_radii + abs(residual_centers - floating_residual), math.inf
    )
    correction_error_bounds = seed.positive_matvec_upper(
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
    floating_nominal_radii = seed.scaled_point_radius(
        floating_correction_bounds, correction_error_bounds, defect, 0.0
    )
    rigorous_point_radii = seed.scaled_point_radius(
        floating_correction_bounds, correction_error_bounds, defect, 1.0
    )

    requested_radii = {
        float(row["coordinate_complex_box"]["real_radius_requested"])
        for row in chart["charts"]
    }
    if len(requested_radii) != 1:
        raise AssertionError("A385S y/z coordinate radii differ")
    requested_radius = requested_radii.pop()
    selected_disk_radius = math.sqrt(2.0) * requested_radius
    nominal_required_disk = float(np.max(floating_nominal_radii))
    rigorous_required_disk = float(np.max(rigorous_point_radii))
    nominal_required_square = nominal_required_disk / math.sqrt(2.0)
    rigorous_required_square = rigorous_required_disk / math.sqrt(2.0)
    old_required_disk = float(
        old_seed["minimal_point_Krawczyk_product_disks"][
            "full_A386_maximum_complex_disk_radius"
        ]
    )
    if not rigorous_required_disk < old_required_disk:
        raise AssertionError("A394 did not improve the A387 point-Krawczyk scale")

    radius_trials = sorted(
        {
            requested_radius,
            seed.upper(nominal_required_square),
            1.0e-6,
            2.0e-6,
            1.0e-5,
            1.0e-4,
            1.0e-3,
            seed.upper(rigorous_required_square),
        }
    )
    trials = []
    for square_radius in radius_trials:
        disk_radius = math.sqrt(2.0) * square_radius
        residual_scale = seed.maximum_residual_scale_for_radius(
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
                "full_A394_point_Krawczyk_image_fits": rigorous_required_disk <= disk_radius,
                "maximum_uniform_A394_residual_radius_scale_for_point_test": residual_scale,
                "required_uniform_residual_tightening_factor_if_finite": (
                    1.0 / residual_scale if residual_scale > 0.0 else None
                ),
                "whole_polydisk_Jacobian_transport_included": False,
            }
        )

    point_fits = rigorous_required_disk <= selected_disk_radius
    payload = {
        "schema": "MTTQ79HeightFourAugmentedBetaKrawczykFeasibilitySeed.v1",
        "status": "A384_A394_POINT_KRAWCZYK_SCALE_DIAGNOSTIC_EXECUTED",
        "artifact": ARTIFACT,
        "point_model": (
            "Y is the A384 serialized center inverse; the numerical seed uses the "
            "independent floating residual; the rigorous disk is the full A394 "
            "enclosure recentered on that diagnostic; B is the certified A384 "
            "point-Jacobian defect"
        ),
        "interval_box_midpoint_preconditioned_correction_diagnostic": [
            encoded_complex(value) for value in midpoint_correction
        ],
        "floating_residual_newton_seed": [
            encoded_complex(value) for value in floating_correction
        ],
        "floating_residual_l2_norm": float(np.linalg.norm(floating_residual)),
        "floating_newton_seed_absolute_uppers": floating_correction_bounds.tolist(),
        "A394_rigorous_radii_recentered_on_floating_diagnostic": (
            floating_recentered_radii.tolist()
        ),
        "A394_residual_uncertainty_correction_uppers": correction_error_bounds.tolist(),
        "point_preconditioned_defect": {
            "componentwise_upper_8_by_8": defect.tolist(),
            "spectral_radius_diagnostic": spectral_radius,
            "A384_weighted_infinity_contraction_upper": float(
                jacobian["summary"]["preconditioned_weighted_infinity_contraction_upper"]
            ),
        },
        "minimal_point_Krawczyk_product_disks": {
            "floating_seed_only_coordinate_radii": floating_nominal_radii.tolist(),
            "full_A394_residual_interval_coordinate_radii": rigorous_point_radii.tolist(),
            "floating_seed_maximum_complex_disk_radius": nominal_required_disk,
            "full_A394_maximum_complex_disk_radius": rigorous_required_disk,
            "floating_seed_equivalent_real_imaginary_square_radius": nominal_required_square,
            "full_A394_equivalent_real_imaginary_square_radius": rigorous_required_square,
            "A387_full_A386_maximum_complex_disk_radius": old_required_disk,
            "A387_to_A395_required_disk_reduction_factor": (
                old_required_disk / rigorous_required_disk
            ),
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
            "full_A394_point_Krawczyk_image_fits": point_fits,
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
            "A387_prior_point_Krawczyk_seed": authority(A387),
            "A394_augmented_beta_residual": authority(A394),
            "A387_numerical_algorithm_source": authority(Path(seed.__file__).resolve()),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "floating_residual_Newton_seed_computed": True,
            "interval_box_midpoint_not_treated_as_true_residual": True,
            "A394_residual_uncertainty_propagated": True,
            "A384_point_Jacobian_defect_propagated": True,
            "strictly_tighter_point_test_than_A387": True,
            "current_A385S_sufficient_point_Krawczyk_test_passed": point_fits,
            "failure_of_sufficient_test_promoted_to_nonexistence": False,
            "Jacobian_polydisk_extension_closed": False,
            "wall_free_polydisk_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "transport the A384 Jacobian over the existing wall-free A385S box"
            if point_fits
            else "tighten the dominant A394 width or construct a coupled beta-period "
            "residual enclosure before the whole-polydisk Jacobian transport"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Augmented-Beta Krawczyk Seed (A395) v1\n\n"
        "A395 propagates the A394 residual through the certified A384 point "
        "Jacobian and keeps the floating Newton seed separate from the rigorous "
        "interval uncertainty.\n\n"
        f"The full point-test disk falls from `{old_required_disk:.12g}` in A387 "
        f"to `{rigorous_required_disk:.12g}`, a factor "
        f"`{old_required_disk / rigorous_required_disk:.12g}`. The current A385S "
        f"disk is `{selected_disk_radius:.12g}`, so the sufficient point test is "
        f"`{point_fits}`.\n\n"
        "This remains a point-Jacobian feasibility calculation. It is not a "
        "whole-polydisk Krawczyk theorem and does not prove a covariant zero.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["minimal_point_Krawczyk_product_disks"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
