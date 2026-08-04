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
FAR_SOURCE = VALIDATED / "far_source" / "d057.1em03.json"
CANONICAL = VALIDATED / "d057.n3.full8.refined.json"
THIMBLE = (
    VALIDATED.parent / "cplx" / "n3ud" / "thimbles" / "t057.json"
)
DIRECTORY = VALIDATED / "far_residue"
MAIN = DIRECTORY / "d057.main.a397.json"
CHECKPOINT = DIRECTORY / "d057.main.a397.ckpt.json"
TAIL = DIRECTORY / "d057.tail_frobenius.a397f.json"
PACKET = DIRECTORY / "d057.full.a397.json"


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
    source = load(FAR_SOURCE)
    canonical = load(CANONICAL)
    main_packet = load(MAIN)
    checkpoint = load(CHECKPOINT)
    tail = load(TAIL)
    thimble = load(THIMBLE)
    require(packet["artifact"] == "A397", "A397 artifact label changed")
    require(
        packet["schema"] == "MTTQ79HeightFourD057FarCutFullResidueInterval.v1",
        "A397 schema changed",
    )
    target = packet["selected_target"]
    require(int(target["distinguished_index"]) == 57, "A397 target changed")
    require(target["root_id"] == "selected_008", "A397 root changed")
    require(int(target["signed_chain_coefficient"]) == 4, "A397 coefficient changed")
    require(float(target["endpoint_cutoff_epsilon"]) == 1.0e-3, "A397 cutoff changed")
    require(int(target["orientation_sign"]) == -1, "A397 orientation changed")
    require(
        source["artifact"] == "A380FS"
        and int(source["selected_target"]["distinguished_index"]) == 57,
        "A397 far source changed",
    )

    execution = main_packet["validated_main_transport"]
    require(
        int(execution["accepted_step_count"]) == len(execution["steps"]),
        "A397 accepted-step count changed",
    )
    require(execution["accepted_step_count"] > 0, "A397 main transport is empty")
    require(
        math.isclose(
            float(execution["steps"][-1]["end_arclength"]),
            float(execution["path_length"]),
            rel_tol=2.0e-15,
            abs_tol=1.0e-15,
        ),
        "A397 main transport did not reach the base",
    )
    maximum_correction = float(main_packet["numerics"]["maximum_lift_correction"])
    require(
        all(
            float(step["maximum_transformed_lift_correction"]) <= maximum_correction
            for step in execution["steps"]
        ),
        "A397 main step exceeded its correction budget",
    )
    require(checkpoint["complete"], "A397 checkpoint is not complete")
    require(
        checkpoint["A397_far_source_sha256"] == sha256(FAR_SOURCE),
        "A397 checkpoint far-source authority changed",
    )
    require(
        checkpoint["A397_builder_sha256"]
        == sha256(ROOT / "scripts" / "run_q79_d057_far_cut_full_residue.py"),
        "A397 checkpoint builder authority changed",
    )
    require(
        int(checkpoint["A397_main_dps"]) == int(main_packet["numerics"]["main_dps"]),
        "A397 checkpoint precision changed",
    )
    require(
        int(main_packet["orientation"]["selected_sign"])
        == int(target["orientation_sign"]),
        "A397 main/full orientation mismatch",
    )
    require(
        tail["artifact"] == "A397F"
        and tail["schema"]
        == "MTTQ79HeightFourD057FarCutFrobeniusTailInterval.v1"
        and float(tail["selected_target"]["endpoint_cutoff_epsilon"]) == 1.0e-3,
        "A397F tail identity changed",
    )
    require(
        tail["strict_scope"]["quantitative_Hensel_factor_disk_closed"]
        and tail["strict_scope"]["finite_Frobenius_period_series_with_Cauchy_tail_used"]
        and tail["strict_scope"]["full_precision_interval_round_trip_used"]
        and not tail["strict_scope"]["segmented_tail_used_as_bound"],
        "A397 lost its strict Frobenius-tail source",
    )

    main_centers = np.asarray(
        [
            complex_value(value)
            for value in main_packet["all_eight_main_residue_rows"]["interval_centers"]
        ],
        dtype=np.complex128,
    )
    tail_centers = np.asarray(
        [complex_value(value) for value in tail["all_eight_endpoint_tails"]["interval_centers"]],
        dtype=np.complex128,
    )
    main_radii = np.asarray(
        execution["residue_coordinate_radius_uppers"], dtype=np.float64
    )
    tail_radii = np.asarray(
        tail["all_eight_endpoint_tails"]["interval_radius_uppers"],
        dtype=np.float64,
    )
    expected_centers = main_centers + int(target["orientation_sign"]) * tail_centers
    expected_radii = main_radii + tail_radii
    floating = np.asarray(
        [complex_value(value) for value in thimble["period_values"]],
        dtype=np.complex128,
    )
    differences = abs(floating - expected_centers)
    require(bool(np.all(differences <= expected_radii)), "A397 floating values escaped")
    rows = packet["residue_rows"]
    require(len(rows) == 8, "A397 row count changed")
    for index, row in enumerate(rows):
        require(int(row["residue_index_zero_based"]) == index, "A397 rows reordered")
        center = complex_value(row["full_interval_center"])
        radius = float(row["full_interval_radius_upper"])
        require(abs(center - expected_centers[index]) < 2.0e-14, "A397 center does not splice")
        require(
            math.isclose(radius, float(expected_radii[index]), rel_tol=2.0e-15, abs_tol=1.0e-300),
            "A397 radius does not splice",
        )
        require(
            math.isclose(
                float(row["selected_chain_contribution_radius_upper"]),
                4.0 * radius,
                rel_tol=2.0e-15,
                abs_tol=1.0e-300,
            ),
            "A397 chain multiplier changed",
        )
        require(row["floating_value_contained"], "A397 containment flag is false")

    summary = packet["summary"]
    chain_radii = 4.0 * expected_radii
    canonical_maximum = float(canonical["summary"]["maximum_full_interval_radius_upper"])
    new_maximum = float(np.max(expected_radii))
    scalar_replay = {
        "maximum_full_interval_radius_upper": new_maximum,
        "maximum_chain_coordinate_radius_upper": float(np.max(chain_radii)),
        "selected_chain_product_disk_l2_radius_upper": float(np.linalg.norm(chain_radii)),
        "maximum_floating_center_difference": float(np.max(differences)),
        "minimum_floating_containment_margin": float(np.min(expected_radii - differences)),
        "canonical_A246_maximum_full_interval_radius_upper": canonical_maximum,
        "A246_to_A397_maximum_radius_tightening_factor": canonical_maximum / new_maximum,
    }
    for key, expected in scalar_replay.items():
        require(
            math.isclose(float(summary[key]), expected, rel_tol=2.0e-14, abs_tol=1.0e-300),
            f"A397 summary does not replay {key}",
        )
    require(new_maximum < canonical_maximum, "A397 does not tighten canonical A246")
    for label, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.exists(), f"A397 authority missing: {label}")
        require(sha256(path) == entry["sha256"], f"A397 authority stale: {label}")
    for source_packet in (main_packet, tail):
        for label, entry in source_packet["authority"].items():
            path = ROOT / entry["path"]
            require(path.exists(), f"A397 source authority missing: {label}")
            require(sha256(path) == entry["sha256"], f"A397 source authority stale: {label}")
    scope = packet["strict_scope"]
    require(scope["full_period_vector_interval_closed"], "A397 full interval is open")
    require(scope["strictly_tighter_than_canonical_A246"], "A397 tightening gate is false")
    require(not scope["floating_values_used_as_bounds"], "A397 uses diagnostics as bounds")
    require(not scope["full_76_target_chain_recomposition_updated"], "A397 overclaims chain update")
    require(not scope["coupled_beta_period_residual_transport_closed"], "A397 overclaims coupling")
    require(not scope["interval_Newton_existence_and_uniqueness_closed"], "A397 overclaims Newton")
    require(not scope["covariant_zero_proved"], "A397 overclaims a covariant zero")
    require(not scope["full_SM_closure_proved"], "A397 overclaims SM closure")
    require(not scope["observed_SM_values_used"], "observed SM data entered A397")
    print(
        "PASS: A397 independently replays the d057 far-cut main/Frobenius-tail splice and "
        f"tightens A246 by {canonical_maximum / new_maximum:.6g}x"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
