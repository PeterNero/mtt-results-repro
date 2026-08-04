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
CANONICAL_MAIN = VALIDATED / "d027.n3.main8.refined.json"
THIMBLE = VALIDATED.parent / "cplx" / "n3ud" / "thimbles" / "t027.json"
DIRECTORY = VALIDATED / "far_residue"
PACKET = DIRECTORY / "d027.main.a406m.json"
CHECKPOINT = DIRECTORY / "d027.main.a406m.ckpt.json"
BUILDER = ROOT / "scripts" / "run_q79_d027_far_cut_main_residue.py"


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
    canonical = load(CANONICAL_MAIN)
    thimble = load(THIMBLE)
    checkpoint = load(CHECKPOINT)
    require(packet["artifact"] == "A406M", "A406M artifact label changed")
    require(
        packet["schema"] == "MTTQ79HeightFourD027FarCutResidueMainInterval.v1",
        "A406M schema changed",
    )
    require(
        packet["status"]
        == "D027_FAR_CUT_ALL_EIGHT_MAIN_RESIDUE_ROWS_INTERVAL_CERTIFIED",
        "A406M status changed",
    )
    target = packet["selected_target"]
    require(int(target["distinguished_index"]) == 27, "A406M target changed")
    require(target["root_id"] == "selected_011", "A406M root changed")
    require(int(target["A219_contribution_rank"]) == 15, "A406M rank changed")
    require(int(target["signed_chain_coefficient"]) == -2, "A406M coefficient changed")
    require(float(target["endpoint_cutoff_epsilon"]) == 1.0e-3, "A406M cutoff changed")
    require(
        set(int(value) for value in target["near_node_colliding_pair_zero_based"])
        == {1, 2},
        "A406M colliding pair changed",
    )
    require(
        source["artifact"] == "A380FS"
        and int(source["selected_target"]["distinguished_index"]) == 27,
        "A406M source identity changed",
    )

    execution = packet["validated_main_transport"]
    steps = execution["steps"]
    require(int(execution["accepted_step_count"]) == len(steps), "A406M step count changed")
    require(len(steps) > 0, "A406M main transport is empty")
    require(
        math.isclose(
            float(steps[-1]["end_arclength"]),
            float(execution["path_length"]),
            rel_tol=2.0e-15,
            abs_tol=1.0e-15,
        ),
        "A406M main transport did not reach the base",
    )
    maximum_correction = float(packet["numerics"]["maximum_lift_correction"])
    require(
        all(float(step["maximum_transformed_lift_correction"]) <= maximum_correction for step in steps),
        "A406M main step exceeded its correction budget",
    )
    require(checkpoint["complete"], "A406M checkpoint is incomplete")
    expected_checkpoint = {
        "A406M_builder_sha256": sha256(BUILDER),
        "A406M_far_source_sha256": sha256(SOURCE),
        "A406M_main_dps": int(packet["numerics"]["main_dps"]),
    }
    for key, expected in expected_checkpoint.items():
        require(checkpoint[key] == expected, f"A406M checkpoint changed: {key}")

    base_center = np.asarray(
        [complex_value(value) for value in execution["center"][:5]],
        dtype=np.complex128,
    )
    floating_base = np.asarray(
        [complex_value(value) for value in thimble["base_fiber_propagated_periods"]],
        dtype=np.complex128,
    )
    plus = float(np.max(abs(base_center - floating_base)))
    minus = float(np.max(abs(-base_center - floating_base)))
    orientation = 1 if plus <= minus else -1
    stored_orientation = int(packet["orientation"]["selected_sign"])
    require(stored_orientation == orientation, "A406M orientation does not replay")
    require(
        stored_orientation == int(canonical["orientation"]["selected_sign"]),
        "A406M orientation differs from canonical d027",
    )
    require(max(plus, minus) > 1000.0 * max(min(plus, minus), 1.0e-15), "A406M orientation not separated")
    transported = np.asarray(
        [complex_value(value) for value in execution["center"][5:]],
        dtype=np.complex128,
    )
    expected_centers = -orientation * transported
    stored_centers = np.asarray(
        [complex_value(value) for value in packet["all_eight_main_residue_rows"]["interval_centers"]],
        dtype=np.complex128,
    )
    require(bool(np.all(abs(stored_centers - expected_centers) < 2.0e-14)), "A406M residue centers changed")
    radii = np.asarray(execution["residue_coordinate_radius_uppers"], dtype=np.float64)
    require(radii.shape == (8,), "A406M did not emit eight residue radii")
    require(bool(np.all(np.isfinite(radii))) and bool(np.all(radii >= 0.0)), "A406M residue radii invalid")
    require(
        math.isclose(
            float(packet["all_eight_main_residue_rows"]["maximum_radius_upper"]),
            float(np.max(radii)),
            rel_tol=2.0e-14,
            abs_tol=1.0e-300,
        ),
        "A406M maximum residue radius does not replay",
    )

    for label, entry in packet["authority"].items():
        path = ROOT / entry["path"]
        require(path.is_file(), f"A406M authority missing: {label}")
        require(sha256(path) == entry["sha256"], f"A406M authority stale: {label}")
    for label, entry in source["authority"].items():
        path = ROOT / entry["path"]
        require(path.is_file(), f"A406M source authority missing: {label}")
        require(sha256(path) == entry["sha256"], f"A406M source authority stale: {label}")
    scope = packet["strict_scope"]
    require(scope["far_cut_period_source_consumed"], "A406M source gate false")
    require(scope["all_eight_far_cut_main_rows_interval_closed"], "A406M main gate false")
    require(not scope["matching_far_cut_tail_interval_closed"], "A406M overclaims its tail")
    require(not scope["full_d027_period_vector_interval_closed"], "A406M overclaims full d027")
    require(not scope["covariant_zero_proved"], "A406M overclaims a covariant zero")
    require(not scope["full_SM_closure_proved"], "A406M overclaims SM closure")
    require(not scope["observed_SM_values_used"], "observed SM data entered A406M")
    print(
        "PASS: A406M independently replays the complete d027 far-cut main "
        f"transport with maximum residue radius {np.max(radii):.6g}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
