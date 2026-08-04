from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import sympy as sp

from q79_selected_alignment_genus2_root_transport import (
    Q79SelectedAlignmentRootTransport,
    load,
)
from q79genus2_root_transport import free_reduce, matrix_rows


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
FIBRATION = DIRECTORY / "selected_alignment_genus2_fibration_seed.interval.packet.json"
PATHS = DIRECTORY / "selected_alignment_torus_handle_paths.interval.packet.json"
HOMOLOGY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
OUTPUT = DIRECTORY / "selected_alignment_handle_monodromy"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--handle", choices=("A", "B"), required=True)
    parser.add_argument("--step-ratio", type=float, default=0.14)
    parser.add_argument("--coarse-steps", type=int, default=128)
    arguments = parser.parse_args()
    started = time.perf_counter()

    path_packet = load(PATHS)
    path = next(row for row in path_packet["handles"] if row["name"] == arguments.handle)
    homology_packet = load(HOMOLOGY)
    transport = Q79SelectedAlignmentRootTransport(
        FIBRATION,
        homology_packet["homology_convention"],
        omitted=2 + 3j,
        dps=70,
    )
    start = decode(path["universal_cover_start"])
    endpoint = decode(path["universal_cover_end"])
    if abs(start - transport.base) > 1e-15:
        raise AssertionError("selected handle basepoint changed")

    points: list[complex] = [start]
    roots: list[np.ndarray] = [transport.base_roots.copy()]
    radii: list[list[float]] = [transport.base_radii.copy()]
    ratio_state = [0.0]
    previous = transport.base_roots
    coarse = np.linspace(start, endpoint, arguments.coarse_steps + 1)
    for left, right in zip(coarse, coarse[1:]):
        previous = transport.advance(
            complex(left),
            complex(right),
            previous,
            points,
            roots,
            radii,
            arguments.step_ratio,
            ratio_state,
        )

    word, final_order, minimum_event_gap = transport.braid_word(roots)
    reduced = free_reduce(word)
    action = sp.Matrix(transport.action(word).tolist())
    intersection = sp.Matrix(homology_packet["homology_convention"]["intersection_matrix"])
    if action.det() != 1 or action.T * intersection * action != intersection:
        raise AssertionError("selected handle matrix is not integral symplectic")
    final_permutation = transport.endpoint_permutation(roots[-1])
    if sorted(final_permutation) != list(range(6)):
        raise AssertionError("selected handle endpoint is not a root permutation")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    trajectory_path = OUTPUT / f"handle_{arguments.handle}.trajectory.npz"
    np.savez_compressed(
        trajectory_path,
        w=np.asarray(points, dtype=np.complex128),
        roots=np.asarray(roots, dtype=np.complex128),
        root_radius_uppers=np.asarray(radii, dtype=np.float64),
    )
    packet = {
        "schema": "MTTQ79SelectedAlignmentHandleMonodromy.v1",
        "status": "SELECTED_ALIGNMENT_HANDLE_POINTWISE_MONODROMY_COMPUTED",
        "handle": arguments.handle,
        "authority": {
            "fibration_sha256": sha256(FIBRATION),
            "handle_paths_sha256": sha256(PATHS),
            "homology_convention_sha256": sha256(HOMOLOGY),
        },
        "path": path,
        "branch_chart": {
            "coordinate": "s=1/(t-(2+3i))",
            "projection_angle": "pi/7",
        },
        "transport": {
            "step_to_root_separation_threshold": format(arguments.step_ratio, ".17g"),
            "maximum_step_to_root_separation_ratio": format(ratio_state[0], ".17g"),
            "root_solve_count": transport.root_solve_count,
            "saved_sample_count": len(points),
            "coarse_segment_count": arguments.coarse_steps,
        },
        "braid": {
            "raw_word": [[generator, sign] for generator, sign in word],
            "raw_length": len(word),
            "free_reduced_word": [[generator, sign] for generator, sign in reduced],
            "free_reduced_length": len(reduced),
            "minimum_projected_event_parameter_separation": format(minimum_event_gap, ".17g"),
            "final_order": final_order,
            "final_root_permutation": final_permutation,
        },
        "homology": {
            "integral_symplectic_matrix": matrix_rows(action),
            "determinant": int(action.det()),
        },
        "trajectory": {
            "path": str(trajectory_path.relative_to(ROOT)).replace("\\", "/"),
            "sha256": sha256(trajectory_path),
            "array_schema": {
                "w": [len(points)],
                "roots": [len(points), 6],
                "root_radius_uppers": [len(points), 6],
            },
        },
        "strict_scope": {
            "pointwise_root_balls_certified": True,
            "continuous_root_tubes_certified": False,
            "handle_monodromy_promoted": False,
            "observed_SM_values_used": False,
        },
    }
    packet_path = OUTPUT / f"handle_{arguments.handle}.packet.json"
    packet_path.write_text(
        json.dumps(packet, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {packet_path.relative_to(ROOT)}")
    print(
        f"handle {arguments.handle}: samples={len(points)} word={len(word)} "
        f"permutation={final_permutation} matrix={matrix_rows(action)}"
    )
    print(f"elapsed_seconds={time.perf_counter() - started:.8g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
