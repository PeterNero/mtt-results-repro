from __future__ import annotations

import hashlib
import json
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


def close(left: float, right: float, tolerance: float = 1.0e-14) -> bool:
    return abs(float(left) - float(right)) <= tolerance * max(
        1.0, abs(float(left)), abs(float(right))
    )


def verify_authority(rows: dict[str, dict], label: str) -> None:
    for name, row in rows.items():
        path = ROOT / row["path"]
        require(path.exists(), f"missing {label} authority {name}: {path}")
        require(sha256(path) == row["sha256"], f"stale {label} authority {name}: {path}")


def audit_target(
    *,
    index: int,
    root_id: str,
    coefficient: int,
    artifact: str,
    line_chart: str = "y",
) -> dict:
    stem = f"d{index:03d}.n3"
    node_path = VALIDATED / f"{stem}.node.refined.json"
    main_path = VALIDATED / f"{stem}.main8.refined.json"
    checkpoint_path = VALIDATED / f"{stem}.main8.refined.checkpoint.json"
    tail_path = VALIDATED / f"{stem}.tail8.refined.json"
    full_path = VALIDATED / f"{stem}.full8.refined.json"
    note_path = (
        ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{index:03d}RefinedFullResidueInterval_{artifact}_v1.md"
    )
    for path in (
        node_path,
        main_path,
        checkpoint_path,
        tail_path,
        full_path,
        note_path,
    ):
        require(path.exists(), f"missing {artifact} artifact: {path}")
    node = load(node_path)
    main_packet = load(main_path)
    checkpoint = load(checkpoint_path)
    tail_packet = load(tail_path)
    full = load(full_path)
    for label, packet in (
        ("node", node),
        ("main", main_packet),
        ("tail", tail_packet),
        ("full", full),
    ):
        selected = packet["selected_target"]
        require(int(selected["distinguished_index"]) == index, f"{artifact} {label} index changed")
        require(selected["root_id"] == root_id, f"{artifact} {label} root changed")
        require(
            selected["line_chart"] == line_chart,
            f"{artifact} {label} chart changed",
        )
        verify_authority(packet["authority"], f"{artifact} {label}")
    require(checkpoint["complete"], f"{artifact} transport checkpoint is incomplete")
    require(
        len(checkpoint["accepted_steps"])
        == int(main_packet["validated_main_transport"]["accepted_step_count"]),
        f"{artifact} checkpoint/main step count mismatch",
    )
    require(
        node["status"] == "N3_TARGET_NODE_AND_LOCAL_FACTOR_INTERVAL_CERTIFIED",
        f"{artifact} node status changed",
    )
    require(
        main_packet["status"]
        == "N3_NODE_AND_ALL_EIGHT_MAIN_RESIDUE_ROWS_INTERVAL_CERTIFIED_TAIL_OPEN",
        f"{artifact} main status changed",
    )
    require(
        tail_packet["status"]
        == "N3_ALL_EIGHT_NODE_TO_CUTOFF_RESIDUE_TAILS_INTERVAL_CERTIFIED",
        f"{artifact} tail status changed",
    )
    require(
        full["status"]
        == "N3_REFINED_FULL_EIGHT_ROW_CHAIN_CONTRIBUTION_INTERVAL_CERTIFIED",
        f"{artifact} full status changed",
    )
    require(full["artifact"] == artifact, f"{artifact} artifact label changed")
    require(
        float(node["certified_node"]["parameter_radius_upper"]) < 1.0e-50,
        f"{artifact} node parameter radius regressed",
    )
    require(
        float(node["certified_node"]["double_root_radius_upper"]) < 1.0e-50,
        f"{artifact} node root radius regressed",
    )
    main_radii = np.asarray(
        main_packet["validated_main_transport"]["residue_coordinate_radius_uppers"],
        dtype=np.float64,
    )
    tail_radii = np.asarray(
        tail_packet["all_eight_endpoint_tails"]["interval_radius_uppers"],
        dtype=np.float64,
    )
    require(len(main_radii) == len(tail_radii) == 8, f"{artifact} row count changed")
    require(np.all(np.isfinite(main_radii)) and np.all(main_radii > 0), f"{artifact} main radii invalid")
    require(np.all(np.isfinite(tail_radii)) and np.all(tail_radii > 0), f"{artifact} tail radii invalid")
    require(np.max(main_radii) < 1.0e-4, f"{artifact} main radius exceeded production gate")
    require(len(tail_packet["regular_segments"]) == 9600, f"{artifact} tail partition changed")
    require(
        all(row["factor_overlap_with_node_side_neighbor"] for row in tail_packet["regular_segments"]),
        f"{artifact} tail factor chain lost overlap",
    )
    orientation = int(main_packet["orientation"]["selected_sign"])
    require(orientation in {-1, 1}, f"{artifact} orientation is not integral")
    require(
        int(full["selected_target"]["selected_chain_coefficient"]) == coefficient,
        f"{artifact} A219 chain coefficient changed",
    )
    main_centers = complex_vector(
        main_packet["all_eight_main_residue_rows"]["interval_centers"]
    )
    tail_centers = complex_vector(
        tail_packet["all_eight_endpoint_tails"]["interval_centers"]
    )
    expected_centers = main_centers + orientation * tail_centers
    expected_radii = main_radii + tail_radii
    rows = full["residue_rows"]
    require(len(rows) == 8, f"{artifact} full row count changed")
    stored_centers = complex_vector([row["full_interval_center"] for row in rows])
    stored_radii = np.asarray(
        [row["full_interval_radius_upper"] for row in rows], dtype=np.float64
    )
    require(np.max(abs(stored_centers - expected_centers)) < 1.0e-14, f"{artifact} center splice mismatch")
    require(np.max(abs(stored_radii - expected_radii)) < 1.0e-14, f"{artifact} radius splice mismatch")
    require(all(row["floating_value_contained"] for row in rows), f"{artifact} floating containment failed")
    require(all(float(row["containment_margin"]) > 0 for row in rows), f"{artifact} containment margin failed")
    summary = full["summary"]
    require(close(summary["maximum_full_interval_radius_upper"], np.max(expected_radii)), f"{artifact} maximum radius mismatch")
    require(
        close(
            summary["selected_chain_product_disk_l2_radius_upper"],
            np.linalg.norm(abs(coefficient) * expected_radii),
        ),
        f"{artifact} chain L2 radius mismatch",
    )
    scope = full["strict_scope"]
    require(scope["full_period_vector_interval_closed"], f"{artifact} period vector reopened")
    require(scope["selected_chain_contribution_interval_closed"], f"{artifact} chain contribution reopened")
    require(not scope["rank3_selected_chain_recomposition_closed"], f"{artifact} overclaims chain recomposition")
    require(not scope["interval_Jacobian_certificate"], f"{artifact} overclaims interval Jacobian")
    require(not scope["covariant_zero_proved"], f"{artifact} overclaims covariant zero")
    require(not scope["observed_SM_values_used"], f"{artifact} consumed observed SM values")
    return {
        "maximum_full_radius": float(np.max(expected_radii)),
        "chain_l2_radius": float(np.linalg.norm(abs(coefficient) * expected_radii)),
        "accepted_steps": int(main_packet["validated_main_transport"]["accepted_step_count"]),
        "orientation": orientation,
    }
