from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

import certify_q79_height4_d087_full_residue_main_interval as main_certificate


ROOT = main_certificate.ROOT
DIRECTORY = main_certificate.PROBE_DIRECTORY / "validated_transport"
MAIN = DIRECTORY / "d087.n3.main8.c1e10.json"
TAIL = DIRECTORY / "d087.n3.tail8.r9600.json"
COARSE = DIRECTORY / "d087.n3.full8.interval.json"
THIMBLE = main_certificate.THIMBLE
COMPLETION = (
    main_certificate.PROBE_DIRECTORY
    / "rank3_complex_PGL3_completion.packet.json"
)
BOUNDARY = (
    main_certificate.PROBE_DIRECTORY
    / "rank3_complex_PGL3_floating_boundary.packet.json"
)
OUTPUT = DIRECTORY / "d087.n3.full8.refined.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_q79HeightFourD087RefinedFullResidueInterval_A225_v1.md"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_matrix(values: list[list[dict[str, str]]]) -> np.ndarray:
    return np.asarray(
        [[complex_value(value) for value in row] for row in values],
        dtype=np.complex128,
    )


def minimum(values: list[float]) -> float:
    if not values:
        raise AssertionError("expected a nonempty clearance profile")
    return float(min(values))


def main() -> int:
    main_packet = load(MAIN)
    tail_packet = load(TAIL)
    coarse_packet = load(COARSE)
    thimble = load(THIMBLE)
    completion = load(COMPLETION)
    boundary = load(BOUNDARY)

    orientation = int(main_packet["orientation"]["selected_sign"])
    if orientation not in {-1, 1}:
        raise AssertionError("refined main orientation is not integral")
    dominant = boundary["difference_decomposition"]["dominant_thimble"]
    if int(dominant["distinguished_index"]) != 87:
        raise AssertionError("A219 dominant thimble is not d087")
    chain_coefficient = int(dominant["signed_coefficient"])
    if chain_coefficient != -1:
        raise AssertionError("A219 d087 signed chain coefficient changed")

    main_centers = np.asarray(
        [
            complex_value(value)
            for value in main_packet["all_eight_main_residue_rows"][
                "interval_centers"
            ]
        ],
        dtype=np.complex128,
    )
    tail_centers = np.asarray(
        [
            complex_value(value)
            for value in tail_packet["all_eight_endpoint_tails"][
                "interval_centers"
            ]
        ],
        dtype=np.complex128,
    )
    floating = np.asarray(
        [complex_value(value) for value in thimble["period_values"]],
        dtype=np.complex128,
    )
    main_radii = np.asarray(
        main_packet["validated_main_transport"][
            "residue_coordinate_radius_uppers"
        ],
        dtype=np.float64,
    )
    tail_radii = np.asarray(
        tail_packet["all_eight_endpoint_tails"]["interval_radius_uppers"],
        dtype=np.float64,
    )
    if not all(
        len(value) == 8
        for value in (
            main_centers,
            tail_centers,
            floating,
            main_radii,
            tail_radii,
        )
    ):
        raise AssertionError("refined d087 source vectors are not eight-dimensional")

    full_centers = main_centers + orientation * tail_centers
    full_radii = main_radii + tail_radii
    floating_differences = abs(floating - full_centers)
    contained = floating_differences <= full_radii
    if not bool(np.all(contained)):
        raise AssertionError(
            "n3 floating d087 vector left the refined full interval: "
            f"{np.flatnonzero(~contained).tolist()}"
        )

    chain_centers = chain_coefficient * full_centers
    chain_radii = abs(chain_coefficient) * full_radii
    product_disk_l2_radius = float(np.linalg.norm(chain_radii))

    jacobian = complex_matrix(completion["complex_Jacobian"])
    if jacobian.shape != (8, 8):
        raise AssertionError("A215 complex Jacobian is not 8 by 8")
    singular_values = np.linalg.svd(jacobian, compute_uv=False)
    minimum_singular_value = float(singular_values[-1])
    if minimum_singular_value <= 0.0:
        raise AssertionError("A215 point Jacobian is singular")
    inverse_jacobian = np.linalg.inv(jacobian)
    spectral_inverse_norm = 1.0 / minimum_singular_value
    linearized_l2_radius = spectral_inverse_norm * product_disk_l2_radius
    linearized_coordinate_radii = abs(inverse_jacobian) @ chain_radii

    chamber_samples = completion["chamber_profile"]["samples"]
    if len(chamber_samples) != 17:
        raise AssertionError("A215 chamber profile no longer has 17 samples")
    sampled_crossings = completion["chamber_profile"]["crossings"]
    clearance_summary = {
        "sample_count": len(chamber_samples),
        "crossing_count": len(sampled_crossings),
        "minimum_A_handle_clearance": minimum(
            [float(sample["minimum_A_handle_clearance"]) for sample in chamber_samples]
        ),
        "minimum_B_handle_clearance": minimum(
            [float(sample["minimum_B_handle_clearance"]) for sample in chamber_samples]
        ),
        "minimum_nearest_radial_pair_clearance": minimum(
            [
                float(sample["nearest_radial_pair"]["clearance"])
                for sample in chamber_samples
            ]
        ),
    }

    coarse_radius = float(
        coarse_packet["summary"]["maximum_full_interval_radius_upper"]
    )
    refined_radius = float(np.max(full_radii))
    rows = []
    for index in range(8):
        rows.append(
            {
                "residue_index_zero_based": index,
                "main_center": main_certificate.encoded_complex(main_centers[index]),
                "main_radius_upper": float(main_radii[index]),
                "oriented_tail_center": main_certificate.encoded_complex(
                    orientation * tail_centers[index]
                ),
                "tail_radius_upper": float(tail_radii[index]),
                "full_interval_center": main_certificate.encoded_complex(
                    full_centers[index]
                ),
                "full_interval_radius_upper": float(full_radii[index]),
                "selected_chain_contribution_center": main_certificate.encoded_complex(
                    chain_centers[index]
                ),
                "selected_chain_contribution_radius_upper": float(
                    chain_radii[index]
                ),
                "floating_value_diagnostic_only": main_certificate.encoded_complex(
                    floating[index]
                ),
                "floating_to_interval_center_distance": float(
                    floating_differences[index]
                ),
                "floating_value_contained": bool(contained[index]),
                "containment_margin": float(
                    full_radii[index] - floating_differences[index]
                ),
            }
        )

    payload = {
        "schema": "MTTQ79HeightFourD087RefinedFullResidueInterval.v1",
        "status": "D087_N3_REFINED_FULL_EIGHT_ROW_CHAIN_CONTRIBUTION_INTERVAL_CERTIFIED",
        "selected_target": {
            "distinguished_index": 87,
            "root_id": "selected_085",
            "line_chart": "y",
            "orientation_sign": orientation,
            "selected_chain_coefficient": chain_coefficient,
            "endpoint_cutoff_epsilon": main_packet["selected_target"][
                "endpoint_cutoff_epsilon"
            ],
        },
        "splice_identity": (
            "full residue vector = refined validated main vector + selected "
            "orientation sign times refined validated node-to-cutoff tail vector"
        ),
        "residue_rows": rows,
        "refined_interval_summary": {
            "certified_rows": 8,
            "maximum_full_interval_radius_upper": refined_radius,
            "selected_chain_product_disk_l2_radius_upper": product_disk_l2_radius,
            "maximum_floating_center_difference": float(
                np.max(floating_differences)
            ),
            "minimum_floating_containment_margin": float(
                np.min(full_radii - floating_differences)
            ),
            "all_floating_values_contained": bool(np.all(contained)),
            "coarse_maximum_radius_upper": coarse_radius,
            "coarse_to_refined_maximum_radius_improvement_factor": float(
                coarse_radius / refined_radius
            ),
        },
        "point_Jacobian_conditioning_diagnostic": {
            "source": "A215 stored complex point Jacobian",
            "minimum_singular_value": minimum_singular_value,
            "spectral_inverse_norm": spectral_inverse_norm,
            "linearized_correction_l2_radius_upper": linearized_l2_radius,
            "linearized_coordinate_disk_radius_uppers": [
                float(value) for value in linearized_coordinate_radii
            ],
            "maximum_linearized_coordinate_disk_radius_upper": float(
                np.max(linearized_coordinate_radii)
            ),
            "is_interval_Newton_certificate": False,
            "reason_not_interval_Newton": (
                "A215 supplies a full-rank point Jacobian but no interval "
                "Jacobian enclosure or derivative-Lipschitz bound on this ball"
            ),
        },
        "sampled_chamber_profile_diagnostic": {
            **clearance_summary,
            "compatible_norm_comparison_to_linearized_ball_available": False,
            "reason_no_chamber_ball_claim": (
                "the A215 clearances are geometric transverse/root clearances "
                "sampled on one Newton ray, not an all-directions Lipschitz "
                "bound in the eight complex deformation coordinates"
            ),
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "A223_refined_tail": TAIL,
                "A224_refined_main": MAIN,
                "A222_coarse_full_comparator": COARSE,
                "n3_d087_floating_cache": THIMBLE,
                "A215_complex_point_Jacobian": COMPLETION,
                "A219_floating_boundary_and_chain_coefficient": BOUNDARY,
                "source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "target_node_interval_Newton_closed": True,
            "all_eight_main_rows_interval_closed": True,
            "all_eight_tail_rows_interval_closed": True,
            "orientation_splice_closed": True,
            "full_d087_period_vector_interval_closed": True,
            "selected_d087_chain_contribution_interval_closed": True,
            "floating_values_used_as_bounds": False,
            "point_Jacobian_linearized_conditioning_executed": True,
            "interval_Jacobian_certificate": False,
            "nonlinear_interval_Newton_closed": False,
            "all_direction_chamber_containment_closed": False,
            "covariant_zero_proved": False,
        },
        "next_required_artifact": (
            "apply the same refined full-vector interval construction to "
            "d034, d041, d030, and d062, recompose the selected rank-3 chain, "
            "then enclose the complex Jacobian and its derivative variation "
            "for chamber-aware interval Newton"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four d087 Refined Full-Residue Interval (A225) v1\n\n"
        "A223 and A224 are spliced with the selected orientation and A219 "
        "chain coefficient. This certifies all eight rows of the complete "
        "d087 contribution without using the floating cache as an error bound.\n\n"
        f"The maximum row radius is `{refined_radius:.12g}` and the product-disk "
        f"L2 radius is `{product_disk_l2_radius:.12g}`. This is a "
        f"`{coarse_radius / refined_radius:.6g}`-fold improvement over A222's "
        "maximum row radius. The independent floating cache remains inside "
        f"all eight balls with minimum margin "
        f"`{np.min(full_radii - floating_differences):.12g}`.\n\n"
        "Applying the stored A215 point inverse gives a linearized L2 "
        f"correction-radius diagnostic of `{linearized_l2_radius:.12g}`. This "
        "is not an interval Newton or chamber-containment theorem: A215 has no "
        "interval Jacobian enclosure, and its sampled wall clearances are not "
        "an all-directions bound in the deformation-coordinate norm.\n\n"
        "The next proof work is the same certificate for d034, d041, d030, "
        "and d062, exact selected-chain recomposition, and an interval "
        "Jacobian/derivative enclosure. No covariant zero or full SM closure "
        "is claimed here.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["refined_interval_summary"], indent=2))
    print(json.dumps(payload["point_Jacobian_conditioning_diagnostic"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
