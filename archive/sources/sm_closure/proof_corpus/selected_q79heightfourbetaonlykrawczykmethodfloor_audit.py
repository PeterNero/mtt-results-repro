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
PACKET = VALIDATED / "n3.beta_floor.a396.json"
PREFIX = VALIDATED / "n3.certified76.recomposition.json"
A383 = VALIDATED / "n3.rank3.handle_hessian.interval.json"
A384 = VALIDATED / "n3.rank3.residual_jacobian.interval.json"
A385S = VALIDATED / "n3.pgl3.polydisk_chart_source.json"
D065 = VALIDATED / "d065.n3.full8.refined.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def upper(value: float) -> float:
    return math.nextafter(float(value), math.inf)


def positive_matvec_upper(matrix: np.ndarray, vector: np.ndarray) -> np.ndarray:
    result = np.zeros(matrix.shape[0], dtype=np.float64)
    for row in range(matrix.shape[0]):
        total = 0.0
        for column in range(matrix.shape[1]):
            total = upper(total + upper(matrix[row, column] * vector[column]))
        result[row] = total
    return result


def post_fixed_point_upper(constant: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    require(
        float(np.max(abs(np.linalg.eigvals(matrix)))) < 1.0,
        "A396 defect matrix is not contractive",
    )
    candidate = np.nextafter(
        np.maximum(np.linalg.solve(np.eye(matrix.shape[0]) - matrix, constant), 0.0),
        math.inf,
    )
    for _ in range(128):
        image = np.nextafter(constant + positive_matvec_upper(matrix, candidate), math.inf)
        if bool(np.all(image <= candidate)):
            return candidate
        candidate = np.nextafter(np.maximum(candidate, image) * (1.0 + 1.0e-12), math.inf)
    raise AssertionError("A396 post-fixed point did not replay")


def close_array(actual: np.ndarray, expected: np.ndarray, message: str) -> None:
    require(
        bool(np.allclose(actual, expected, rtol=2.0e-14, atol=1.0e-300)),
        message,
    )


def main() -> int:
    packet = load(PACKET)
    prefix = load(PREFIX)
    handle = load(A383)
    jacobian = load(A384)
    chart = load(A385S)
    wall = load(D065)
    require(packet["artifact"] == "A396", "A396 artifact label changed")
    require(
        packet["schema"] == "MTTQ79HeightFourBetaOnlyKrawczykMethodFloor.v1",
        "A396 schema changed",
    )
    handle_rows = {
        int(row["residue_index_zero_based"]): row for row in handle["handle_rows"]
    }
    require(set(handle_rows) == set(range(8)), "A396 handle rows changed")
    chain_radii = np.asarray(
        [float(row["certified_prefix_interval_radius_upper"]) for row in prefix["residue_rows"]],
        dtype=np.float64,
    )
    handle_radii = np.asarray(
        [float(handle_rows[index]["component_radius_upper"]) for index in range(8)],
        dtype=np.float64,
    )
    wall_radii = np.asarray(
        [3.0 * float(wall["residue_rows"][index]["full_interval_radius_upper"]) for index in range(8)],
        dtype=np.float64,
    )
    period_radii = chain_radii + handle_radii + wall_radii
    close_array(
        np.asarray(packet["period_component_radius_uppers"], dtype=np.float64),
        period_radii,
        "A396 period radii do not replay",
    )
    inverse = np.asarray(
        [[complex_value(value) for value in row] for row in jacobian["center_inverse_8_by_8"]],
        dtype=np.complex128,
    )
    defect = np.nextafter(
        np.asarray(
            jacobian["verified_interval_nonsingularity"][
                "componentwise_preconditioned_defect_upper_8_by_8"
            ],
            dtype=np.float64,
        ),
        math.inf,
    )
    correction = positive_matvec_upper(abs(inverse), np.nextafter(period_radii, math.inf))
    method_radii = post_fixed_point_upper(np.nextafter(correction, math.inf), defect)
    close_array(
        np.asarray(packet["A384_preconditioned_period_uncertainty_uppers"]),
        correction,
        "A396 preconditioned uncertainty does not replay",
    )
    close_array(
        np.asarray(packet["method_floor_coordinate_disk_radii"]),
        method_radii,
        "A396 method-floor radii do not replay",
    )
    chart_radii = {
        float(row["coordinate_complex_box"]["real_radius_requested"])
        for row in chart["charts"]
    }
    require(len(chart_radii) == 1, "A396 chart radii changed")
    chart_square = chart_radii.pop()
    disk = float(np.max(method_radii))
    square = disk / math.sqrt(2.0)
    gap = square / chart_square
    summary = packet["summary"]
    scalar_replay = {
        "period_product_box_l2_radius_upper": float(np.linalg.norm(period_radii)),
        "maximum_period_component_radius_upper": float(np.max(period_radii)),
        "optimistic_method_floor_maximum_complex_disk_radius": disk,
        "optimistic_method_floor_equivalent_real_imaginary_square_radius": square,
        "A385S_real_imaginary_square_radius": chart_square,
        "A385S_complex_disk_radius": math.sqrt(2.0) * chart_square,
        "method_floor_to_A385S_square_gap_factor": gap,
    }
    for key, expected in scalar_replay.items():
        require(
            math.isclose(float(summary[key]), expected, rel_tol=2.0e-14, abs_tol=1.0e-300),
            f"A396 summary does not replay {key}",
        )
    require(
        int(summary["dominant_period_residue_index_zero_based"]) == int(np.argmax(period_radii)),
        "A396 dominant residue changed",
    )
    require(gap > 1.0, "A396 beta-only method floor unexpectedly fits A385S")
    for name, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.exists(), f"missing A396 authority {name}")
        require(sha256(path) == entry["sha256"], f"stale A396 authority {name}")
    scope = packet["strict_scope"]
    require(scope["monotone_limit_of_current_independent_box_point_test_computed"], "A396 method gate false")
    require(not scope["beta_only_tightening_sufficient_for_current_A385S_test"], "A396 decision changed")
    require(not scope["lower_bound_on_true_residual_uncertainty_proved"], "A396 overclaims a true lower bound")
    require(not scope["all_possible_correlation_preserving_enclosures_excluded"], "A396 excludes correlations")
    require(not scope["absence_of_a_covariant_zero_proved"], "A396 overclaims nonexistence")
    require(not scope["interval_Newton_existence_and_uniqueness_closed"], "A396 overclaims interval Newton")
    require(not scope["covariant_zero_proved"], "A396 overclaims a covariant zero")
    require(not scope["full_SM_closure_proved"], "A396 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "observed SM data entered A396")
    print(
        "PASS: A396 independently replays the beta-zero independent-box method "
        f"limit and its {gap:.6g}x gap to A385S"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
