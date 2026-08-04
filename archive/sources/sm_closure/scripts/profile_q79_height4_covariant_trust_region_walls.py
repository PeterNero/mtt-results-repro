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


def signed_handle_coordinate(name: str, value: complex) -> float:
    coordinate = value.imag - 0.25 if name == "A" else value.real - 0.25
    return float(coordinate - round(coordinate))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--rank", type=int, choices=(2, 3, 4, 5), required=True)
    parser.add_argument("--samples", type=int, default=17)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> int:
    arguments = parse_args()
    if arguments.samples < 2:
        raise ValueError("samples must be at least two")
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
    fan = load(probe.FAN)["distinguished_positive_meridians"]
    central_centers = {
        row["root_id"]: probe.complex_value(row["canonical_lift"])
        for row in fan
    }
    scales = np.linspace(0.0, 1.0, arguments.samples)
    output = (
        probe.PROBE_DIRECTORY
        / f"rank{arguments.rank}_full_step_wall_profile_{arguments.samples:03d}.packet.json"
    )
    if output.exists() and not arguments.force:
        print(f"cached {relative(output)}")
        print(json.dumps(load(output)["summary"], indent=2))
        return 0

    samples = []
    previous_signed: dict[str, dict[str, float]] | None = None
    bracketed_crossings = []
    base_alignment = probe.central_alignment()
    for sample_index, scale in enumerate(scales):
        if sample_index == 0:
            centers = central_centers
            diagnostics = {
                "isolated_roots": 90,
                "matching_method": "selected central fan representatives",
                "maximum_a_root_shift": 0.0,
                "maximum_torus_lift_shift": 0.0,
            }
        else:
            alignment = base_alignment @ expm(float(scale) * tangent)
            centers, diagnostics = probe.continued_critical_centers(alignment)
        signed = {
            name: {
                root_id: signed_handle_coordinate(name, value)
                for root_id, value in centers.items()
            }
            for name in ("A", "B")
        }
        nearest = {
            name: min(values.items(), key=lambda row: abs(row[1]))
            for name, values in signed.items()
        }
        crossings_from_previous = []
        if previous_signed is not None:
            for name in ("A", "B"):
                for root_id, value in signed[name].items():
                    old_value = previous_signed[name][root_id]
                    if old_value * value < 0:
                        crossing = {
                            "handle": name,
                            "root_id": root_id,
                            "lower_scale": float(scales[sample_index - 1]),
                            "upper_scale": float(scale),
                            "lower_signed_coordinate": old_value,
                            "upper_signed_coordinate": value,
                        }
                        crossings_from_previous.append(crossing)
                        bracketed_crossings.append(crossing)
        sample = {
            "sample_index": sample_index,
            "scale": float(scale),
            "nearest_A_root_id": nearest["A"][0],
            "nearest_A_signed_coordinate": nearest["A"][1],
            "nearest_B_root_id": nearest["B"][0],
            "nearest_B_signed_coordinate": nearest["B"][1],
            "selected_090_A_signed_coordinate": signed["A"]["selected_090"],
            "selected_090_B_signed_coordinate": signed["B"]["selected_090"],
            "crossings_from_previous_sample": crossings_from_previous,
            "critical_continuation": diagnostics,
        }
        samples.append(sample)
        previous_signed = signed
        print(
            f"[{sample_index + 1}/{len(scales)}] scale={scale:.6f} "
            f"B-nearest={nearest['B'][0]}:{nearest['B'][1]:+.6e} "
            f"crossings={len(crossings_from_previous)}",
            flush=True,
        )

    packet = {
        "schema": "MTTQ79HeightFourCovariantTrustRegionWallProfile.v1",
        "status": "FLOATING_WALL_PROFILE_EXECUTED",
        "candidate_rank": arguments.rank,
        "full_least_squares_step": [float(value) for value in full_step],
        "sample_count": len(samples),
        "samples": samples,
        "bracketed_crossings": bracketed_crossings,
        "summary": {
            "candidate_rank": arguments.rank,
            "sample_count": len(samples),
            "bracketed_crossing_count": len(bracketed_crossings),
            "minimum_sampled_A_clearance": min(
                abs(row["nearest_A_signed_coordinate"]) for row in samples
            ),
            "minimum_sampled_B_clearance": min(
                abs(row["nearest_B_signed_coordinate"]) for row in samples
            ),
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
            "all_ninety_critical_values_continued_at_each_noncentral_sample": True,
            "sampled_path_profile_only": True,
            "complete_no_crossing_certificate": False,
            "floating_only": True,
            "covariant_zero_proved": False,
            "observed_SM_values_used": False,
        },
    }
    dump(output, packet)
    print(f"wrote {relative(output)}")
    print(json.dumps(packet["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
