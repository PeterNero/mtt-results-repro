from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from flint import acb, acb_mat, arb, ctx


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_height4_target_full_residue_interval as generic
import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_selected_alignment_single_E32_thimble_main_interval as pilot
import certify_q79_selected_side_beta_defect_transport as validated
import q79_fast_taylor_runtime as fast


PACKET = main_hessian.VALIDATED / "far_source" / "ranked.first_step.a399.json"
EXPECTED_INDICES = (57, 27, 82, 17, 4)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def initial_state(system, periods: list[acb]):
    center = [system.midpoint_acb(value) for value in periods]
    centers = [center + [acb(0)] for _ in range(8)]
    frames = []
    for _row in range(8):
        identity = acb_mat(6, 6)
        for coordinate in range(6):
            identity[coordinate, coordinate] = acb(1)
        frames.append(
            pilot.E32LiftErrorFrame(
                fundamental=identity,
                coordinate_radii=[value.rad().upper() for value in periods]
                + [arb(0)],
            )
        )
    return centers, frames


def replay(row: dict, *, dps: int, order: int, step: float) -> float:
    index = int(row["distinguished_index"])
    source_path = main_hessian.VALIDATED / "far_source" / f"d{index:03d}.1em03.json"
    source = load(source_path)
    system, rank, target = main_hessian.selected_system(index, dps)
    require(rank == int(row["A219_contribution_rank"]), f"d{index:03d} rank changed")
    require(target["root_id"] == row["root_id"], f"d{index:03d} root changed")
    require(system.line_chart == row["line_chart"], f"d{index:03d} chart changed")
    require(
        int(target["signed_coefficient"]) == int(row["signed_chain_coefficient"]),
        f"d{index:03d} coefficient changed",
    )
    periods = [
        validated.decoded_acb(value)
        for value in source["far_cut_source"]["full_precision_period_balls"]
    ]
    start_packet = source["far_cut_source"]["cutoff_start_binary64"]
    start = complex(float(start_packet["real"]), float(start_packet["imaginary"]))
    direction = -start / abs(start)
    require(
        float(direction.real).hex() == row["direction_binary64"]["real_hex"],
        f"d{index:03d} direction real part changed",
    )
    require(
        float(direction.imag).hex() == row["direction_binary64"]["imaginary_hex"],
        f"d{index:03d} direction imaginary part changed",
    )
    centers, frames = initial_state(system, periods)
    replay_centers, replay_frames, diagnostics = (
        generic.main_engine.validated_all_residue_rows_step(
            system,
            start,
            direction,
            step,
            centers,
            frames,
            order=order,
        )
    )
    stored_centers = [
        [validated.decoded_acb(value) for value in values]
        for values in row["output_centers"]
    ]
    require(
        all(
            replay_value.overlaps(stored_value)
            for replay_values, stored_values in zip(replay_centers, stored_centers)
            for replay_value, stored_value in zip(replay_values, stored_values)
        ),
        f"d{index:03d} output-center replay lost overlap",
    )
    stored_frames = [generic.decoded_frame(value) for value in row["output_frames"]]
    for frame_index, (replay_frame, stored_frame) in enumerate(
        zip(replay_frames, stored_frames)
    ):
        require(
            all(
                replay_frame.fundamental[left, right].overlaps(
                    stored_frame.fundamental[left, right]
                )
                for left in range(6)
                for right in range(6)
            ),
            f"d{index:03d} frame {frame_index} replay lost overlap",
        )
        require(
            all(
                replay_radius.overlaps(stored_radius)
                for replay_radius, stored_radius in zip(
                    replay_frame.coordinate_radii, stored_frame.coordinate_radii
                )
            ),
            f"d{index:03d} frame {frame_index} radii changed",
        )
    radius = float(diagnostics["maximum_residue_coordinate_radius_upper"])
    stored_radius = float(
        row["diagnostics"]["maximum_residue_coordinate_radius_upper"]
    )
    require(
        abs(radius - stored_radius) <= 1.0e-12 * max(radius, stored_radius, 1.0e-300),
        f"d{index:03d} first-step radius changed",
    )
    require(radius < 1.0e-12, f"d{index:03d} first-step radius is too wide")
    return radius


def main() -> int:
    packet = load(PACKET)
    require(
        packet["schema"] == "MTTQ79HeightFourRankedFarCutFirstStep.v1",
        "A399 schema changed",
    )
    require(packet["artifact"] == "A399", "A399 artifact changed")
    rows = packet["targets"]
    require(
        tuple(int(row["distinguished_index"]) for row in rows) == EXPECTED_INDICES,
        "A399 ranked target set changed",
    )
    dps = int(packet["method"]["dps"])
    order = int(packet["method"]["Taylor_order"])
    step = float(packet["method"]["step"])
    ctx.dps = dps
    fast.install()
    try:
        radii = [replay(row, dps=dps, order=order, step=step) for row in rows]
    finally:
        fast.uninstall()
    maximum = max(radii)
    require(
        maximum
        == float(packet["summary"]["maximum_first_step_residue_radius_upper"]),
        "A399 maximum radius summary changed",
    )
    for label, authority in packet["authority"].items():
        path = ROOT / authority["path"]
        require(path.exists(), f"A399 authority missing: {label}")
        require(sha256(path) == authority["sha256"], f"A399 authority stale: {label}")
    scope = packet["strict_scope"]
    require(scope["one_local_step_per_target_interval_closed"], "A399 local steps open")
    require(not scope["complete_main_transports_closed"], "A399 overclaims main transport")
    require(not scope["full_chain_recomposition_closed"], "A399 overclaims chain")
    require(
        not scope["interval_Newton_existence_and_uniqueness_closed"],
        "A399 overclaims Newton",
    )
    print(
        "PASS: A399 independently replays five rigorous far-cut first steps; "
        f"maximum radius {maximum:.6e}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
