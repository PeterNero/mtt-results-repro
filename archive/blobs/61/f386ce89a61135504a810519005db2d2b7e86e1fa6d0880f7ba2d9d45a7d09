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
SOURCE = VALIDATED / "far_source" / "d027.1em03.json"
CANONICAL = VALIDATED / "d027.n3.full8.refined.json"
CANONICAL_MAIN = VALIDATED / "d027.n3.main8.refined.json"
THIMBLE = VALIDATED.parent / "cplx" / "n3ud" / "thimbles" / "t027.json"
DIRECTORY = VALIDATED / "far_residue"
MAIN = DIRECTORY / "d027.main.a406m.json"
CHECKPOINT = DIRECTORY / "d027.main.a406m.ckpt.json"
TAIL = DIRECTORY / "d027.tail_frobenius.a406f.json"
PACKET = DIRECTORY / "d027.full.a406.json"


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
    canonical = load(CANONICAL)
    canonical_main = load(CANONICAL_MAIN)
    main_packet = load(MAIN)
    checkpoint = load(CHECKPOINT)
    tail = load(TAIL)
    thimble = load(THIMBLE)
    require(packet["artifact"] == "A406", "A406 artifact label changed")
    require(packet["schema"] == "MTTQ79HeightFourD027FarCutFullResidueInterval.v1", "A406 schema changed")
    require(packet["status"] == "D027_FAR_CUT_FROBENIUS_FULL_EIGHT_ROW_CHAIN_INTERVAL_CERTIFIED", "A406 status changed")
    target = packet["selected_target"]
    require(int(target["distinguished_index"]) == 27, "A406 target changed")
    require(target["root_id"] == "selected_011", "A406 root changed")
    require(int(target["A219_contribution_rank"]) == 15, "A406 rank changed")
    coefficient = int(target["signed_chain_coefficient"])
    require(coefficient == -2, "A406 coefficient changed")
    require(float(target["endpoint_cutoff_epsilon"]) == 1.0e-3, "A406 cutoff changed")
    require(source["artifact"] == "A380FS", "A406 far source changed")

    execution = main_packet["validated_main_transport"]
    steps = execution["steps"]
    require(int(execution["accepted_step_count"]) == len(steps) and len(steps) > 0, "A406 main execution invalid")
    require(math.isclose(float(steps[-1]["end_arclength"]), float(execution["path_length"]), rel_tol=2.0e-15, abs_tol=1.0e-15), "A406 main path incomplete")
    require(checkpoint["complete"], "A406 checkpoint is incomplete")
    require(checkpoint["A406M_far_source_sha256"] == sha256(SOURCE), "A406 source checkpoint changed")
    require(checkpoint["A406M_builder_sha256"] == sha256(ROOT / "scripts" / "run_q79_d027_far_cut_main_residue.py"), "A406 main builder checkpoint changed")
    orientation = int(target["orientation_sign"])
    require(orientation == int(main_packet["orientation"]["selected_sign"]), "A406 orientation mismatch")
    require(orientation == int(canonical_main["orientation"]["selected_sign"]), "A406 canonical orientation mismatch")
    require(tail["artifact"] == "A406F", "A406 tail source changed")
    tail_scope = tail["strict_scope"]
    require(tail_scope["quantitative_Hensel_factor_disk_closed"], "A406 lost the Hensel disk")
    require(tail_scope["finite_Frobenius_period_series_with_Cauchy_tail_used"], "A406 lost the Cauchy tail")
    require(tail_scope["full_precision_interval_round_trip_used"], "A406 lost interval round-trip")
    require(not tail_scope["A406R_segmented_reference_used_as_bound"], "A406 uses A406R as a bound")

    main_centers = np.asarray(
        [complex_value(value) for value in main_packet["all_eight_main_residue_rows"]["interval_centers"]],
        dtype=np.complex128,
    )
    main_radii = np.asarray(execution["residue_coordinate_radius_uppers"], dtype=np.float64)
    tail_centers = np.asarray(
        [complex_value(value) for value in tail["all_eight_endpoint_tails"]["interval_centers"]],
        dtype=np.complex128,
    )
    tail_radii = np.asarray(tail["all_eight_endpoint_tails"]["interval_radius_uppers"], dtype=np.float64)
    expected_centers = main_centers + orientation * tail_centers
    expected_radii = main_radii + tail_radii
    floating = np.asarray([complex_value(value) for value in thimble["period_values"]], dtype=np.complex128)
    differences = abs(floating - expected_centers)
    require(bool(np.all(differences <= expected_radii)), "A406 floating diagnostics escaped")

    rows = packet["residue_rows"]
    require(len(rows) == 8, "A406 row count changed")
    for index, row in enumerate(rows):
        require(int(row["residue_index_zero_based"]) == index, "A406 rows reordered")
        center = complex_value(row["full_interval_center"])
        radius = float(row["full_interval_radius_upper"])
        require(abs(center - expected_centers[index]) < 2.0e-14, f"A406 row {index} center does not splice")
        require(math.isclose(radius, float(expected_radii[index]), rel_tol=2.0e-15, abs_tol=1.0e-300), f"A406 row {index} radius does not splice")
        require(abs(complex_value(row["selected_chain_contribution_center"]) - coefficient * center) < 2.0e-14, f"A406 row {index} chain center changed")
        require(math.isclose(float(row["selected_chain_contribution_radius_upper"]), abs(coefficient) * radius, rel_tol=2.0e-15), f"A406 row {index} chain radius changed")
        require(row["floating_value_contained"], f"A406 row {index} containment flag false")

    canonical_maximum = float(canonical["summary"]["maximum_full_interval_radius_upper"])
    new_maximum = float(np.max(expected_radii))
    chain_radii = abs(coefficient) * expected_radii
    expected_summary = {
        "maximum_full_interval_radius_upper": new_maximum,
        "maximum_chain_coordinate_radius_upper": float(np.max(chain_radii)),
        "selected_chain_product_disk_l2_radius_upper": float(np.linalg.norm(chain_radii)),
        "maximum_floating_center_difference": float(np.max(differences)),
        "minimum_floating_containment_margin": float(np.min(expected_radii - differences)),
        "canonical_d027_maximum_full_interval_radius_upper": canonical_maximum,
        "canonical_to_A406_maximum_radius_tightening_factor": canonical_maximum / new_maximum,
    }
    for key, expected in expected_summary.items():
        require(math.isclose(float(packet["summary"][key]), expected, rel_tol=2.0e-14, abs_tol=1.0e-300), f"A406 summary changed: {key}")
    require(new_maximum < canonical_maximum, "A406 does not tighten canonical d027")

    for source_packet in (packet, main_packet, tail):
        for label, entry in source_packet["authority"].items():
            path = ROOT / entry["path"]
            require(path.is_file(), f"A406 authority missing: {label}")
            require(sha256(path) == entry["sha256"], f"A406 authority stale: {label}")
    scope = packet["strict_scope"]
    for key in (
        "all_eight_far_cut_main_rows_interval_closed",
        "all_eight_Frobenius_tail_rows_interval_closed",
        "orientation_splice_closed",
        "full_period_vector_interval_closed",
        "selected_chain_contribution_interval_closed",
        "strictly_tighter_than_canonical_d027",
    ):
        require(scope[key], f"A406 strict gate false: {key}")
    require(not scope["floating_values_used_as_bounds"], "A406 uses floating values as bounds")
    require(not scope["full_76_target_chain_recomposition_updated"], "A406 overclaims chain recomposition")
    require(not scope["coupled_beta_period_residual_transport_closed"], "A406 overclaims coupling")
    require(not scope["interval_Newton_existence_and_uniqueness_closed"], "A406 overclaims Newton")
    require(not scope["covariant_zero_proved"], "A406 overclaims a zero")
    require(not scope["full_SM_closure_proved"], "A406 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "observed SM data entered A406")
    print(
        "PASS: A406 independently replays the d027 main/Frobenius splice and "
        f"tightens the canonical interval by {canonical_maximum / new_maximum:.6g}x"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
