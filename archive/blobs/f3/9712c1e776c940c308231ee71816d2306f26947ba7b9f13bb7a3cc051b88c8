from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np
from flint import ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_selected_side_beta_defect_transport as validated


VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
PACKET = VALIDATED / "far_residue" / "d027.tail_segmented.a406r.json"
SOURCE = VALIDATED / "far_source" / "d027.1em03.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    packet = load(PACKET)
    source = load(SOURCE)
    require(packet["artifact"] == "A406R", "A406R artifact label changed")
    require(
        packet["schema"] == "MTTQ79HeightFourTargetFullResidueTailInterval.v1",
        "A406R schema changed",
    )
    require(
        packet["status"] == "D027_FAR_CUT_SEGMENTED_TAIL_BRANCH_REFERENCE_CERTIFIED",
        "A406R status changed",
    )
    target = packet["selected_target"]
    require(int(target["distinguished_index"]) == 27, "A406R target changed")
    require(target["root_id"] == "selected_011", "A406R root changed")
    require(list(target["cutoff_pair_zero_based"]) == [1, 2], "A406R pair changed")
    epsilon = float(target["endpoint_cutoff_epsilon"])
    require(epsilon == 1.0e-3, "A406R cutoff changed")
    require(source["artifact"] == "A380FS", "A406R source changed")
    numerics = packet["numerics"]
    ctx.dps = int(numerics["dps"])
    require(ctx.dps >= 90, "A406R precision gate failed")
    expected_segments = int(numerics["outer_segments"])
    require(expected_segments == 9600, "A406R segment count changed")
    rows = packet["regular_segments"]
    require(len(rows) == expected_segments, "A406R regular cover is incomplete")
    ordered = sorted(rows, key=lambda row: float(row["x_interval"]["lower"]))
    node_upper = float(packet["node_segment"]["x_interval"]["upper"])
    require(
        math.isclose(float(ordered[0]["x_interval"]["lower"]), node_upper, rel_tol=2.0e-13, abs_tol=2.0e-18),
        "A406R regular cover misses the node segment",
    )
    require(
        math.isclose(float(ordered[-1]["x_interval"]["upper"]), epsilon, rel_tol=2.0e-15, abs_tol=2.0e-18),
        "A406R regular cover misses the cutoff",
    )
    covered_width = node_upper
    for index, row in enumerate(ordered):
        lower = float(row["x_interval"]["lower"])
        upper = float(row["x_interval"]["upper"])
        require(lower < upper, f"A406R segment {index} has nonpositive width")
        covered_width += upper - lower
        if index:
            previous = float(ordered[index - 1]["x_interval"]["upper"])
            require(
                math.isclose(previous, lower, rel_tol=2.0e-13, abs_tol=2.0e-18),
                f"A406R cover has a gap at segment {index}",
            )
        require(row["factor_overlap_with_node_side_neighbor"], f"A406R factor chain breaks at segment {index}")
        require(float(row["quadratic_discriminant_absolute_lower"]) > 0.0, f"A406R discriminant meets zero at segment {index}")
        require(float(row["minimum_quartic_half_plane_margin"]) > 0.0, f"A406R quartic half-plane margin fails at segment {index}")
        require(float(row["minimum_square_root_sign_margin"]) > 0.0, f"A406R square-root sign fails at segment {index}")
        require(int(row["selected_period_sign"]) in {-1, 1}, f"A406R sign invalid at segment {index}")
        require(
            float(row["opposite_orientation_difference_lower"])
            > float(row["selected_orientation_difference_upper"]),
            f"A406R orientation is not separated at segment {index}",
        )
        require(len(row["row_integrals"]) == 8, f"A406R row count changed at segment {index}")
    require(math.isclose(covered_width, epsilon, rel_tol=2.0e-13, abs_tol=2.0e-16), "A406R cover width does not replay")

    hensel = packet["quantitative_Hensel_disk"]
    require(hensel["quantitative_Hensel_disk_closed"], "A406R Hensel disk open")
    require(float(hensel["self_map_bound_upper"]) <= float(hensel["uniform_factor_correction_radius"]), "A406R Hensel self-map failed")
    require(float(hensel["contraction_bound_upper"]) < 1.0, "A406R Hensel contraction failed")

    endpoint = packet["all_eight_endpoint_tails"]
    balls = [validated.interval_from_bounds(value) for value in endpoint["intervals"]]
    centers = np.asarray([validated.midpoint(value) for value in balls], dtype=np.complex128)
    radii = np.asarray([validated.radius_upper(value) for value in balls], dtype=np.float64)
    stored_centers = np.asarray(
        [complex_value(value) for value in endpoint["interval_centers"]],
        dtype=np.complex128,
    )
    stored_radii = np.asarray(endpoint["interval_radius_uppers"], dtype=np.float64)
    require(centers.shape == radii.shape == (8,), "A406R endpoint dimension changed")
    require(bool(np.array_equal(centers, stored_centers)), "A406R endpoint centers do not round-trip")
    require(bool(np.array_equal(radii, stored_radii)), "A406R endpoint radii do not round-trip")
    require(
        math.isclose(float(endpoint["maximum_interval_radius_upper"]), float(np.max(radii)), rel_tol=2.0e-15, abs_tol=1.0e-300),
        "A406R maximum endpoint radius does not replay",
    )

    for label, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.is_file(), f"A406R authority missing: {label}")
        require(sha256(path) == entry["sha256"], f"A406R authority stale: {label}")
    scope = packet["strict_scope"]
    require(scope["all_eight_node_to_cutoff_tail_intervals_closed"], "A406R tail cover flag false")
    require(scope["full_precision_interval_round_trip_used"], "A406R serialized bounds were not replayed")
    require(scope["branch_overlap_reference_only"], "A406R role changed")
    require(not scope["accepted_as_final_d027_tail_bound"], "A406R coarse radii were promoted")
    require(not scope["full_d027_period_vector_interval_closed"], "A406R overclaims full d027")
    require(not scope["covariant_zero_proved"], "A406R overclaims a covariant zero")
    require(not scope["full_SM_closure_proved"], "A406R overclaims SM closure")
    require(not scope["observed_SM_values_used"], "observed SM data entered A406R")
    print(
        "PASS: A406R independently replays the 9,600-segment d027 branch "
        f"reference with maximum coarse radius {np.max(radii):.6g}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
