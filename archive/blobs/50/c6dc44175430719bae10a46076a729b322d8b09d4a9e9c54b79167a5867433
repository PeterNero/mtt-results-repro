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
PACKET = VALIDATED / "n3.chain.d057far.a398.json"
A373 = VALIDATED / "n3.certified76.recomposition.json"
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
        "A398 defect matrix is not contractive",
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
    raise AssertionError("A398 post-fixed point did not replay")


def close_array(actual: np.ndarray, expected: np.ndarray, message: str) -> None:
    require(
        bool(np.allclose(actual, expected, rtol=2.0e-14, atol=1.0e-300)),
        message,
    )


def main() -> int:
    packet = load(PACKET)
    old_chain = load(A373)
    handle = load(A383)
    jacobian = load(A384)
    chart = load(A385S)
    wall = load(D065)
    require(packet["artifact"] == "A398", "A398 artifact label changed")
    require(
        packet["schema"] == "MTTQ79HeightFourD057FarCutChainRecomposition.v1",
        "A398 schema changed",
    )
    manifest = packet["component_authority_manifest"]
    require(len(manifest) == 76, "A398 component count changed")
    require(
        [int(row["A219_profile_priority_rank"]) for row in manifest] == list(range(1, 77)),
        "A398 component order changed",
    )
    require(
        [int(row["distinguished_index"]) for row in manifest].count(57) == 1,
        "A398 d057 multiplicity changed",
    )
    centers = np.zeros(8, dtype=np.complex128)
    radii = np.zeros(8, dtype=np.float64)
    ranking = []
    replaced = 0
    for entry in manifest:
        path = ROOT / entry["selected_packet_path"]
        require(path.exists(), "A398 selected component packet is missing")
        require(
            sha256(path) == entry["selected_packet_sha256"],
            "A398 selected component authority is stale",
        )
        target = load(path)
        index = int(entry["distinguished_index"])
        require(
            int(target["selected_target"]["distinguished_index"]) == index,
            "A398 target identity changed",
        )
        rows = {
            int(row["residue_index_zero_based"]): row for row in target["residue_rows"]
        }
        require(set(rows) == set(range(8)), "A398 target rows changed")
        component_radii = np.zeros(8, dtype=np.float64)
        for residue_index in range(8):
            row = rows[residue_index]
            centers[residue_index] += complex_value(
                row["selected_chain_contribution_center"]
            )
            radius = float(row["selected_chain_contribution_radius_upper"])
            radii[residue_index] += radius
            component_radii[residue_index] = radius
        is_replacement = bool(entry["canonical_packet_replaced"])
        replaced += int(is_replacement)
        require(is_replacement == (index == 57), "A398 replacement flag changed")
        ranking.append(
            {
                "distinguished_index": index,
                "l2": float(np.linalg.norm(component_radii)),
            }
        )
    require(replaced == 1, "A398 did not replace exactly one packet")

    packet_rows = packet["residue_rows"]
    require(len(packet_rows) == 8, "A398 row count changed")
    for index, row in enumerate(packet_rows):
        require(int(row["residue_index_zero_based"]) == index, "A398 rows reordered")
        require(
            abs(complex_value(row["recomposed_chain_interval_center"]) - centers[index])
            < 2.0e-14,
            "A398 chain center does not replay",
        )
        require(
            math.isclose(
                float(row["recomposed_chain_interval_radius_upper"]),
                float(radii[index]),
                rel_tol=2.0e-14,
                abs_tol=1.0e-300,
            ),
            "A398 chain radius does not replay",
        )
        floating = complex_value(row["floating_chain_diagnostic_only"])
        require(abs(floating - centers[index]) <= radii[index], "A398 floating chain escaped")

    handle_rows = {
        int(row["residue_index_zero_based"]): row for row in handle["handle_rows"]
    }
    handle_radii = np.asarray(
        [float(handle_rows[index]["component_radius_upper"]) for index in range(8)],
        dtype=np.float64,
    )
    wall_radii = np.asarray(
        [3.0 * float(wall["residue_rows"][index]["full_interval_radius_upper"]) for index in range(8)],
        dtype=np.float64,
    )
    period_radii = radii + handle_radii + wall_radii
    close_array(
        np.asarray(packet["period_component_radius_uppers_after_A397"]),
        period_radii,
        "A398 period radii do not replay",
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
        np.asarray(packet["optimistic_beta_zero_method_coordinate_disk_radii"]),
        method_radii,
        "A398 method radii do not replay",
    )
    old_radii = np.asarray(
        [float(row["certified_prefix_interval_radius_upper"]) for row in old_chain["residue_rows"]],
        dtype=np.float64,
    )
    old_l2 = float(np.linalg.norm(old_radii))
    new_l2 = float(np.linalg.norm(radii))
    require(new_l2 < old_l2, "A398 does not tighten A373")
    chart_radii = {
        float(row["coordinate_complex_box"]["real_radius_requested"])
        for row in chart["charts"]
    }
    require(len(chart_radii) == 1, "A398 chart radii changed")
    chart_square = chart_radii.pop()
    method_disk = float(np.max(method_radii))
    method_square = method_disk / math.sqrt(2.0)
    ranking.sort(key=lambda row: row["l2"], reverse=True)
    summary = packet["summary"]
    scalar_replay = {
        "A373_chain_product_box_l2_radius_upper": old_l2,
        "A398_chain_product_box_l2_radius_upper": new_l2,
        "A373_to_A398_chain_radius_tightening_factor": old_l2 / new_l2,
        "A373_maximum_chain_component_radius_upper": float(np.max(old_radii)),
        "A398_maximum_chain_component_radius_upper": float(np.max(radii)),
        "optimistic_beta_zero_method_maximum_complex_disk_radius": method_disk,
        "optimistic_beta_zero_method_equivalent_square_radius": method_square,
        "A385S_square_radius": chart_square,
        "optimistic_method_to_A385S_gap_factor": method_square / chart_square,
    }
    for key, expected in scalar_replay.items():
        require(
            math.isclose(float(summary[key]), expected, rel_tol=2.0e-14, abs_tol=1.0e-300),
            f"A398 summary does not replay {key}",
        )
    require(
        int(summary["next_dominant_target_by_selected_l2_width"])
        == int(ranking[0]["distinguished_index"]),
        "A398 next dominant target changed",
    )
    for label, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.exists(), f"A398 authority missing: {label}")
        require(sha256(path) == entry["sha256"], f"A398 authority stale: {label}")
    scope = packet["strict_scope"]
    require(scope["same_76_selected_chain_coefficients_used"], "A398 changed the chain")
    require(scope["only_d057_interval_certificate_replaced"], "A398 replacement scope changed")
    require(scope["full_76_target_chain_recomposition_updated"], "A398 chain update is false")
    require(scope["strictly_tighter_than_A373"], "A398 tightening gate is false")
    require(not scope["beta_period_cross_correlation_preserved"], "A398 overclaims correlation")
    require(not scope["lower_bound_on_true_residual_uncertainty_proved"], "A398 overclaims a lower bound")
    require(not scope["interval_Newton_existence_and_uniqueness_closed"], "A398 overclaims Newton")
    require(not scope["covariant_zero_proved"], "A398 overclaims a covariant zero")
    require(not scope["full_SM_closure_proved"], "A398 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "observed SM data entered A398")
    print(
        "PASS: A398 independently rebuilds all 76 target rows with only d057 "
        f"replaced and tightens A373 by {old_l2 / new_l2:.6g}x"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
