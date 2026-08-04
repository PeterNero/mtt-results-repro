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
NODE = VALIDATED / "d034.n3.node.refined.json"
MAIN = VALIDATED / "d034.n3.main8.refined.json"
TAIL = VALIDATED / "d034.n3.tail8.refined.json"
FULL = VALIDATED / "d034.n3.full8.refined.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD034RefinedFullResidueInterval_A226_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_vector(values: list[dict[str, str]]) -> np.ndarray:
    return np.asarray([complex_value(value) for value in values], dtype=np.complex128)


def verify_authority(rows: dict[str, dict], label: str) -> None:
    for name, row in rows.items():
        path = ROOT / row["path"]
        require(path.exists(), f"missing {label} authority {name}: {path}")
        require(sha256(path) == row["sha256"], f"stale {label} authority {name}: {path}")


def close(left: float, right: float, tolerance: float = 1.0e-14) -> bool:
    return abs(float(left) - float(right)) <= tolerance * max(
        1.0, abs(float(left)), abs(float(right))
    )


def main() -> int:
    for path in (NODE, MAIN, TAIL, FULL, NOTE):
        require(path.exists(), f"missing A226 artifact: {path}")
    node = load(NODE)
    main_packet = load(MAIN)
    tail_packet = load(TAIL)
    full = load(FULL)
    for label, packet in (
        ("node", node),
        ("main", main_packet),
        ("tail", tail_packet),
        ("full", full),
    ):
        selected = packet["selected_target"]
        require(int(selected["distinguished_index"]) == 34, f"A226 {label} index changed")
        require(selected["root_id"] == "selected_007", f"A226 {label} root changed")
        require(selected["line_chart"] == "y", f"A226 {label} chart changed")
        verify_authority(packet["authority"], f"A226 {label}")

    require(
        node["status"] == "N3_TARGET_NODE_AND_LOCAL_FACTOR_INTERVAL_CERTIFIED",
        "A226 node status changed",
    )
    require(
        main_packet["status"]
        == "N3_NODE_AND_ALL_EIGHT_MAIN_RESIDUE_ROWS_INTERVAL_CERTIFIED_TAIL_OPEN",
        "A226 main status changed",
    )
    require(
        tail_packet["status"]
        == "N3_ALL_EIGHT_NODE_TO_CUTOFF_RESIDUE_TAILS_INTERVAL_CERTIFIED",
        "A226 tail status changed",
    )
    require(
        full["status"]
        == "N3_REFINED_FULL_EIGHT_ROW_CHAIN_CONTRIBUTION_INTERVAL_CERTIFIED",
        "A226 full status changed",
    )
    require(full["artifact"] == "A226", "A226 artifact label changed")
    require(
        float(node["certified_node"]["parameter_radius_upper"]) < 1.0e-50,
        "A226 node parameter radius regressed",
    )
    require(
        float(node["certified_node"]["double_root_radius_upper"]) < 1.0e-50,
        "A226 node root radius regressed",
    )
    main_radii = np.asarray(
        main_packet["validated_main_transport"]["residue_coordinate_radius_uppers"],
        dtype=np.float64,
    )
    tail_radii = np.asarray(
        tail_packet["all_eight_endpoint_tails"]["interval_radius_uppers"],
        dtype=np.float64,
    )
    require(len(main_radii) == len(tail_radii) == 8, "A226 does not have eight rows")
    require(np.all(np.isfinite(main_radii)) and np.all(main_radii > 0), "A226 main radii invalid")
    require(np.all(np.isfinite(tail_radii)) and np.all(tail_radii > 0), "A226 tail radii invalid")
    require(np.max(main_radii) < 1.0e-4, "A226 main radius exceeded production gate")
    require(len(tail_packet["regular_segments"]) == 9600, "A226 tail partition changed")
    require(
        all(row["factor_overlap_with_node_side_neighbor"] for row in tail_packet["regular_segments"]),
        "A226 tail factor chain lost overlap",
    )

    orientation = int(main_packet["orientation"]["selected_sign"])
    coefficient = int(full["selected_target"]["selected_chain_coefficient"])
    require(orientation in {-1, 1}, "A226 orientation is not integral")
    require(coefficient == 3, "A226 A219 chain coefficient changed")
    main_centers = complex_vector(
        main_packet["all_eight_main_residue_rows"]["interval_centers"]
    )
    tail_centers = complex_vector(
        tail_packet["all_eight_endpoint_tails"]["interval_centers"]
    )
    expected_centers = main_centers + orientation * tail_centers
    expected_radii = main_radii + tail_radii
    rows = full["residue_rows"]
    require(len(rows) == 8, "A226 full packet does not emit eight rows")
    stored_centers = complex_vector([row["full_interval_center"] for row in rows])
    stored_radii = np.asarray(
        [row["full_interval_radius_upper"] for row in rows], dtype=np.float64
    )
    require(np.max(abs(stored_centers - expected_centers)) < 1.0e-14, "A226 center splice mismatch")
    require(np.max(abs(stored_radii - expected_radii)) < 1.0e-14, "A226 radius splice mismatch")
    require(all(row["floating_value_contained"] for row in rows), "A226 floating containment failed")
    require(all(float(row["containment_margin"]) > 0 for row in rows), "A226 containment margin failed")
    summary = full["summary"]
    require(close(summary["maximum_full_interval_radius_upper"], np.max(expected_radii)), "A226 maximum radius mismatch")
    require(
        close(
            summary["selected_chain_product_disk_l2_radius_upper"],
            np.linalg.norm(abs(coefficient) * expected_radii),
        ),
        "A226 chain L2 radius mismatch",
    )
    scope = full["strict_scope"]
    require(scope["full_period_vector_interval_closed"], "A226 period vector reopened")
    require(scope["selected_chain_contribution_interval_closed"], "A226 chain contribution reopened")
    require(not scope["rank3_selected_chain_recomposition_closed"], "A226 overclaims chain recomposition")
    require(not scope["interval_Jacobian_certificate"], "A226 overclaims interval Jacobian")
    require(not scope["covariant_zero_proved"], "A226 overclaims covariant zero")
    require(not scope["observed_SM_values_used"], "A226 consumed observed SM values")

    print("q79 A226 d034 refined full-residue interval audit: PASS")
    print(
        "closed: d034 node, eight-row main/tail splice, and coefficient-three "
        f"chain ball; max row radius={np.max(expected_radii):.6e}"
    )
    print("open: remaining selected-chain rows, interval Jacobian, and covariant zero")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
