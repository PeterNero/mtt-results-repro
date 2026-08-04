from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
from flint import ctx
from scipy.linalg import expm

import explore_q79_height4_covariant_floating_probe as probe
from diagnose_q79_covariant_parameter_continued_thimble import segment_coordinates


ROOT = probe.ROOT
JACOBIAN = (
    probe.PROBE_DIRECTORY / "height4_covariant_floating_jacobian.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rank", type=int, choices=(2, 3, 4, 5), required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--other", required=True)
    parser.add_argument("--lower", type=float, required=True)
    parser.add_argument("--upper", type=float, required=True)
    parser.add_argument("--iterations", type=int, default=30)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> int:
    arguments = parse_args()
    if not 0 <= arguments.lower < arguments.upper <= 1:
        raise ValueError("wall bracket must satisfy 0 <= lower < upper <= 1")
    if arguments.iterations < 1:
        raise ValueError("iterations must be positive")
    ctx.dps = 100
    started = time.perf_counter()
    jacobian_packet = load(JACOBIAN)
    selected = next(
        row
        for row in jacobian_packet["candidate_Jacobians"]
        if int(row["A132_objective_rank"]) == arguments.rank
    )
    full_step = np.asarray(
        selected["local_least_squares_step_on_available_directions"],
        dtype=np.float64,
    )
    evaluator = probe.PGL3BetaEvaluator()
    tangent = sum(
        (
            full_step[index] * evaluator.generators[index]
            for index in range(8)
        ),
        np.zeros((3, 3), dtype=np.complex128),
    )
    base_alignment = probe.central_alignment()
    base_point = 0.25 + 0.25j

    evaluations: dict[str, dict] = {}

    def evaluate(scale: float) -> dict:
        key = format(scale, ".17g")
        if key in evaluations:
            return evaluations[key]
        alignment = base_alignment @ expm(scale * tangent)
        centers, diagnostics = probe.continued_critical_centers(alignment)
        coordinates = segment_coordinates(
            np.asarray([base_point, centers[arguments.target]], dtype=np.complex128),
            centers[arguments.other],
        )
        row = {
            "scale": scale,
            **coordinates,
            "critical_continuation": diagnostics,
        }
        evaluations[key] = row
        return row

    lower = arguments.lower
    upper = arguments.upper
    lower_row = evaluate(lower)
    upper_row = evaluate(upper)
    lower_sign = lower_row["signed_transverse_coordinate"]
    upper_sign = upper_row["signed_transverse_coordinate"]
    if lower_sign * upper_sign >= 0:
        raise AssertionError("supplied radial-wall bracket has no sign change")
    for iteration in range(arguments.iterations):
        midpoint = (lower + upper) / 2
        midpoint_row = evaluate(midpoint)
        midpoint_sign = midpoint_row["signed_transverse_coordinate"]
        print(
            f"[{iteration + 1}/{arguments.iterations}] "
            f"scale={midpoint:.12f} transverse={midpoint_sign:+.6e}",
            flush=True,
        )
        if lower_sign * midpoint_sign <= 0:
            upper = midpoint
            upper_row = midpoint_row
            upper_sign = midpoint_sign
        else:
            lower = midpoint
            lower_row = midpoint_row
            lower_sign = midpoint_sign

    output = (
        probe.PROBE_DIRECTORY
        / (
            f"rank{arguments.rank}_{arguments.target}_{arguments.other}_"
            "radial_wall.packet.json"
        )
    )
    packet = {
        "schema": "MTTQ79CovariantRadialWallLocation.v1",
        "status": "FLOATING_RADIAL_WALL_BRACKETED",
        "candidate_rank": arguments.rank,
        "target_root_id": arguments.target,
        "crossing_root_id": arguments.other,
        "lower_endpoint": lower_row,
        "upper_endpoint": upper_row,
        "evaluations": sorted(evaluations.values(), key=lambda row: row["scale"]),
        "summary": {
            "candidate_rank": arguments.rank,
            "target_root_id": arguments.target,
            "crossing_root_id": arguments.other,
            "wall_scale_midpoint": (lower + upper) / 2,
            "wall_scale_bracket_width": upper - lower,
            "lower_signed_transverse_coordinate": lower_sign,
            "upper_signed_transverse_coordinate": upper_sign,
            "longitudinal_parameter_at_lower_endpoint": lower_row[
                "longitudinal_parameter"
            ],
            "longitudinal_parameter_at_upper_endpoint": upper_row[
                "longitudinal_parameter"
            ],
            "elapsed_seconds": time.perf_counter() - started,
        },
        "authority": {
            "Jacobian": relative(JACOBIAN),
            "Jacobian_sha256": sha256(JACOBIAN),
            "probe_engine_source": relative(Path(probe.__file__).resolve()),
            "probe_engine_source_sha256": sha256(Path(probe.__file__).resolve()),
            "source": relative(Path(__file__)),
            "source_sha256": sha256(Path(__file__)),
        },
        "strict_scope": {
            "all_ninety_critical_values_continued_per_evaluation": True,
            "oriented_radial_wall_bracket": True,
            "floating_only": True,
            "interval_wall_certificate": False,
            "Picard_Lefschetz_jump_applied": False,
            "covariant_zero_proved": False,
        },
    }
    dump(output, packet)
    print(f"wrote {relative(output)}")
    print(json.dumps(packet["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
