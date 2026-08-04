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
import q79_covariant_parameter_continued_thimble as continued


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
    parser.add_argument("--scale", type=float, required=True)
    parser.add_argument("--index", type=int, required=True)
    parser.add_argument("--substeps", type=int, default=16)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def scale_tag(value: float) -> str:
    return format(value, ".3e").replace("+", "p").replace("-", "m").replace(".", "d")


def segment_coordinates(path: np.ndarray, point: complex) -> dict:
    if len(path) != 2:
        raise ValueError("radial path must be one segment")
    start, end = path
    vector = end - start
    squared_length = vector.real**2 + vector.imag**2
    if squared_length == 0:
        raise ValueError("radial path has zero length")
    best: dict | None = None
    for real_shift in range(-2, 3):
        for imaginary_shift in range(-2, 3):
            lifted = point + real_shift + 1j * imaginary_shift
            offset = lifted - start
            parameter = (
                offset.real * vector.real + offset.imag * vector.imag
            ) / squared_length
            clamped = min(1.0, max(0.0, parameter))
            closest = start + clamped * vector
            clearance = float(abs(closest - lifted))
            signed_transverse = float(
                (vector.real * offset.imag - vector.imag * offset.real)
                / abs(vector)
            )
            row = {
                "radial_path_clearance": clearance,
                "longitudinal_parameter": float(parameter),
                "clamped_longitudinal_parameter": float(clamped),
                "signed_transverse_coordinate": signed_transverse,
                "deck_shift": [real_shift, imaginary_shift],
            }
            if best is None or clearance < best["radial_path_clearance"]:
                best = row
    if best is None:
        raise AssertionError("segment coordinate search returned no lift")
    return best


def main() -> int:
    arguments = parse_args()
    if not 0 < arguments.scale <= 1:
        raise ValueError("scale must lie in (0,1]")
    if arguments.substeps < 1:
        raise ValueError("substeps must be positive")
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
    tag = (
        f"pcdiag_r{arguments.rank}_s{scale_tag(arguments.scale)}_"
        f"d{arguments.index:03d}_n{arguments.substeps:03d}"
    )
    output_directory = probe.PROBE_DIRECTORY / tag
    output = output_directory / "diagnostic.packet.json"
    if output.exists() and not arguments.force:
        print(f"cached {relative(output)}")
        print(json.dumps(load(output)["summary"], indent=2))
        return 0

    base_alignment = probe.central_alignment()
    y_fibrations = []
    z_fibrations = []
    endpoint_alignment = None
    for substep in range(1, arguments.substeps + 1):
        fraction = arguments.scale * substep / arguments.substeps
        alignment = base_alignment @ expm(fraction * tangent)
        endpoint_alignment = alignment
        directory = output_directory / "homotopy" / f"s{substep:03d}"
        y_path = directory / "fy.packet.json"
        z_path = directory / "fz.packet.json"
        dump(y_path, probe.build_point_fibration(alignment, "y"))
        dump(z_path, probe.build_point_fibration(alignment, "z"))
        y_fibrations.append(str(y_path))
        z_fibrations.append(str(z_path))
    if endpoint_alignment is None:
        raise AssertionError("endpoint alignment was not constructed")
    centers, critical_diagnostics = probe.continued_critical_centers(
        endpoint_alignment
    )
    fan_row = next(
        row
        for row in load(probe.FAN)["distinguished_positive_meridians"]
        if int(row["distinguished_index"]) == arguments.index
    )
    central_packet = load(
        probe.central_period_path(arguments.index, fan_row["root_id"])
    )
    line_chart = central_packet.get("line_chart", "y")
    endpoint_fibration = Path(
        y_fibrations[-1] if line_chart == "y" else z_fibrations[-1]
    )
    endpoint_transport = probe.Q79SelectedAlignmentPeriodRootTransport(
        endpoint_fibration,
        load(probe.HOMOLOGY)["homology_convention"],
        omitted=probe.OMITTED,
        dps=70,
    )
    actual_radial_path = np.asarray(
        [endpoint_transport.base, centers[fan_row["root_id"]]],
        dtype=np.complex128,
    )
    critical_path_clearances = sorted(
        (
            {"root_id": root_id, **segment_coordinates(actual_radial_path, center)}
            for root_id, center in centers.items()
            if root_id != fan_row["root_id"]
        ),
        key=lambda row: row["radial_path_clearance"],
    )
    task = {
        "distinguished_index": arguments.index,
        "root_id": fan_row["root_id"],
        "central_packet_path": str(
            probe.central_period_path(arguments.index, fan_row["root_id"])
        ),
        "critical_center": [
            centers[fan_row["root_id"]].real,
            centers[fan_row["root_id"]].imag,
        ],
        "y_homotopy_fibrations": y_fibrations,
        "z_homotopy_fibrations": z_fibrations,
    }
    execution = continued.execute(task)
    chosen_residual = min(
        execution["positive_continuity_residual"],
        execution["negative_continuity_residual"],
    )
    packet = {
        "schema": "MTTQ79CovariantParameterContinuedThimbleDiagnostic.v1",
        "status": "PARAMETER_CONTINUED_THIMBLE_EXECUTED",
        "candidate_rank": arguments.rank,
        "scale": arguments.scale,
        "distinguished_index": arguments.index,
        "root_id": fan_row["root_id"],
        "parameter_substeps": arguments.substeps,
        "critical_continuation": critical_diagnostics,
        "actual_radial_path_other_critical_clearances": critical_path_clearances,
        "execution": execution,
        "summary": {
            "candidate_rank": arguments.rank,
            "scale": arguments.scale,
            "distinguished_index": arguments.index,
            "root_id": fan_row["root_id"],
            "parameter_substeps": arguments.substeps,
            "chosen_continuity_residual": chosen_residual,
            "sequential_to_direct_maximum_root_difference": execution[
                "approach_root_rebase"
            ]["sequential_to_direct_maximum_root_difference"],
            "nearest_other_critical_root_to_actual_radial_path": (
                critical_path_clearances[0]["root_id"]
            ),
            "nearest_other_critical_clearance_to_actual_radial_path": (
                critical_path_clearances[0]["radial_path_clearance"]
            ),
            "nearest_other_critical_signed_transverse_coordinate": (
                critical_path_clearances[0]["signed_transverse_coordinate"]
            ),
            "nearest_other_critical_longitudinal_parameter": (
                critical_path_clearances[0]["longitudinal_parameter"]
            ),
            "elapsed_seconds": time.perf_counter() - started,
        },
        "authority": {
            "Jacobian": relative(JACOBIAN),
            "Jacobian_sha256": sha256(JACOBIAN),
            "probe_engine_source": relative(Path(probe.__file__).resolve()),
            "probe_engine_source_sha256": sha256(Path(probe.__file__).resolve()),
            "parameter_continuation_source": relative(Path(continued.__file__).resolve()),
            "parameter_continuation_source_sha256": sha256(
                Path(continued.__file__).resolve()
            ),
            "source": relative(Path(__file__)),
            "source_sha256": sha256(Path(__file__)),
        },
        "strict_scope": {
            "single_thimble_diagnostic": True,
            "parameter_continued_root_labels": True,
            "full_candidate_residual_executed": False,
            "interval_certificate": False,
            "floating_only": True,
            "covariant_zero_proved": False,
        },
    }
    dump(output, packet)
    print(f"wrote {relative(output)}")
    print(json.dumps(packet["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
