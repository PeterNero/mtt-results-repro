from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
)
VALIDATED = DIRECTORY / "validated_transport"
MAIN = VALIDATED / "d087.n3.main8.c1e10.json"
TAIL = VALIDATED / "d087.n3.tail8.r9600.json"
COARSE = VALIDATED / "d087.n3.full8.interval.json"
REFINED = VALIDATED / "d087.n3.full8.refined.json"
TAIL_NOTE = (
    ROOT / "proof_corpus" / "MTT_q79HeightFourD087RefinedTailInterval_A223_v1.md"
)
MAIN_NOTE = (
    ROOT / "proof_corpus" / "MTT_q79HeightFourD087RefinedMainInterval_A224_v1.md"
)
FULL_NOTE = (
    ROOT / "proof_corpus" / "MTT_q79HeightFourD087RefinedFullResidueInterval_A225_v1.md"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def close(left: float, right: float, tolerance: float = 1.0e-14) -> bool:
    return abs(float(left) - float(right)) <= tolerance * max(
        1.0, abs(float(left)), abs(float(right))
    )


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_vector(values: list[dict[str, str]]) -> np.ndarray:
    return np.asarray([complex_value(value) for value in values], dtype=np.complex128)


def complex_matrix(values: list[list[dict[str, str]]]) -> np.ndarray:
    return np.asarray(
        [[complex_value(value) for value in row] for row in values],
        dtype=np.complex128,
    )


def verify_authority(rows: dict[str, dict]) -> None:
    for name, row in rows.items():
        path = ROOT / row["path"]
        require(path.exists(), f"missing A225 authority {name}: {path}")
        require(sha256(path) == row["sha256"], f"stale A225 authority {name}: {path}")


def main() -> int:
    for path in (MAIN, TAIL, COARSE, REFINED, TAIL_NOTE, MAIN_NOTE, FULL_NOTE):
        require(path.exists(), f"missing A223-A225 artifact: {path}")
    require(
        TAIL_NOTE.read_text(encoding="utf-8").startswith(
            "# MTT q79 Height-Four d087 Refined Full-Residue Tail Interval (A223) v1"
        ),
        "A223 note title regressed",
    )
    require(
        MAIN_NOTE.read_text(encoding="utf-8").startswith(
            "# MTT q79 Height-Four d087 Refined Full-Residue Main Interval (A224) v1"
        ),
        "A224 note title regressed",
    )

    main_packet = load(MAIN)
    tail_packet = load(TAIL)
    coarse = load(COARSE)
    refined = load(REFINED)
    require(
        refined["schema"] == "MTTQ79HeightFourD087RefinedFullResidueInterval.v1",
        "A225 schema changed",
    )
    require(
        refined["status"]
        == "D087_N3_REFINED_FULL_EIGHT_ROW_CHAIN_CONTRIBUTION_INTERVAL_CERTIFIED",
        "A225 status changed",
    )
    verify_authority(refined["authority"])
    require(len(tail_packet["regular_segments"]) == 9600, "A223 partition changed")
    require(
        max(tail_packet["all_eight_endpoint_tails"]["interval_radius_uppers"])
        < 5.0e-7,
        "A223 tail radius regressed above 5e-7",
    )
    require(
        max(
            main_packet["validated_main_transport"][
                "residue_coordinate_radius_uppers"
            ]
        )
        < 8.0e-7,
        "A224 main radius regressed above 8e-7",
    )

    orientation = int(main_packet["orientation"]["selected_sign"])
    coefficient = int(refined["selected_target"]["selected_chain_coefficient"])
    require(orientation == -1, "A224 orientation changed")
    require(coefficient == -1, "A219 d087 chain coefficient changed")
    main_centers = complex_vector(
        main_packet["all_eight_main_residue_rows"]["interval_centers"]
    )
    tail_centers = complex_vector(
        tail_packet["all_eight_endpoint_tails"]["interval_centers"]
    )
    main_radii = np.asarray(
        main_packet["validated_main_transport"]["residue_coordinate_radius_uppers"],
        dtype=np.float64,
    )
    tail_radii = np.asarray(
        tail_packet["all_eight_endpoint_tails"]["interval_radius_uppers"],
        dtype=np.float64,
    )
    expected_centers = main_centers + orientation * tail_centers
    expected_radii = main_radii + tail_radii
    rows = refined["residue_rows"]
    require(len(rows) == 8, "A225 does not emit eight rows")
    stored_centers = complex_vector([row["full_interval_center"] for row in rows])
    stored_radii = np.asarray(
        [row["full_interval_radius_upper"] for row in rows], dtype=np.float64
    )
    require(np.max(abs(stored_centers - expected_centers)) < 1.0e-14, "A225 center splice mismatch")
    require(np.max(abs(stored_radii - expected_radii)) < 1.0e-14, "A225 radius splice mismatch")
    require(
        all(row["floating_value_contained"] for row in rows),
        "A225 floating diagnostic escaped a row",
    )
    require(
        all(float(row["containment_margin"]) > 0.0 for row in rows),
        "A225 has a nonpositive containment margin",
    )

    summary = refined["refined_interval_summary"]
    max_radius = float(np.max(expected_radii))
    l2_radius = float(np.linalg.norm(abs(coefficient) * expected_radii))
    require(close(summary["maximum_full_interval_radius_upper"], max_radius), "A225 maximum radius mismatch")
    require(close(summary["selected_chain_product_disk_l2_radius_upper"], l2_radius), "A225 L2 radius mismatch")
    require(max_radius < 1.2e-6, "A225 maximum radius regressed above 1.2e-6")
    coarse_radius = float(coarse["summary"]["maximum_full_interval_radius_upper"])
    improvement = coarse_radius / max_radius
    require(close(summary["coarse_to_refined_maximum_radius_improvement_factor"], improvement), "A225 improvement factor mismatch")
    require(improvement > 650.0, "A225 tightening fell below 650-fold")

    completion = load(
        ROOT / refined["authority"]["A215_complex_point_Jacobian"]["path"]
    )
    jacobian = complex_matrix(completion["complex_Jacobian"])
    require(np.linalg.matrix_rank(jacobian) == 8, "A215 point Jacobian lost rank")
    singular_minimum = float(np.linalg.svd(jacobian, compute_uv=False)[-1])
    correction_bound = l2_radius / singular_minimum
    diagnostic = refined["point_Jacobian_conditioning_diagnostic"]
    require(close(diagnostic["minimum_singular_value"], singular_minimum), "A225 singular value mismatch")
    require(close(diagnostic["linearized_correction_l2_radius_upper"], correction_bound), "A225 point-Jacobian correction bound mismatch")
    require(correction_bound < 8.0e-7, "A225 point-Jacobian diagnostic regressed")
    require(not diagnostic["is_interval_Newton_certificate"], "A225 overclaims interval Newton")

    chamber = refined["sampled_chamber_profile_diagnostic"]
    samples = completion["chamber_profile"]["samples"]
    require(chamber["sample_count"] == len(samples) == 17, "A225 chamber sample count changed")
    require(chamber["crossing_count"] == 0, "A225 sampled path acquired a crossing")
    require(
        not chamber["compatible_norm_comparison_to_linearized_ball_available"],
        "A225 incorrectly promotes sampled clearances to a chamber ball",
    )

    scope = refined["strict_scope"]
    require(scope["full_d087_period_vector_interval_closed"], "A225 d087 vector reopened")
    require(scope["selected_d087_chain_contribution_interval_closed"], "A225 chain contribution reopened")
    require(not scope["interval_Jacobian_certificate"], "A225 fabricates an interval Jacobian")
    require(not scope["nonlinear_interval_Newton_closed"], "A225 fabricates interval Newton")
    require(not scope["covariant_zero_proved"], "A225 overclaims the covariant zero")
    require(not scope["observed_SM_values_used"], "A225 consumed observed SM values")

    print("q79 A223-A225 refined d087 full-residue interval audit: PASS")
    print(
        f"closed: eight-row d087 chain ball, max radius={max_radius:.6e}, "
        f"tightening={improvement:.3f}x"
    )
    print(
        f"diagnostic only: point-Jacobian correction L2 radius={correction_bound:.6e}"
    )
    print("open: remaining chain rows, interval Jacobian, and chamber-safe interval Newton")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
