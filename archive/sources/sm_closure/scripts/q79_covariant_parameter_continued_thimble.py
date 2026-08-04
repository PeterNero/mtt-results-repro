from __future__ import annotations

import hashlib
import tempfile
from pathlib import Path

import numpy as np

import explore_q79_height4_covariant_floating_probe as probe


CACHE_ALGORITHM = "parameter_continued_approach_root_rebase_v1"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def execute(task: dict) -> dict:
    index = int(task["distinguished_index"])
    root_id = task["root_id"]
    central_packet_path = Path(task["central_packet_path"])
    central_packet = probe.load(central_packet_path)
    line_chart = central_packet.get("line_chart", "y")
    fibration_paths = [
        Path(path) for path in task[f"{line_chart}_homotopy_fibrations"]
    ]
    if not fibration_paths:
        raise AssertionError("parameter homotopy has no noncentral fibration")
    endpoint_fibration = fibration_paths[-1]
    stem = f"d{index:03d}_{root_id}"
    trajectory_packet_path = probe.TRAJECTORY_DIRECTORY / f"{stem}.packet.json"
    trajectory_packet = probe.load(trajectory_packet_path)
    if line_chart == "y":
        trajectory_path = probe.ROOT / trajectory_packet["trajectory"]["path"]
    else:
        trajectory_path = (
            probe.PERIOD_DIRECTORY
            / "adapted_line_chart_approaches"
            / f"{stem}.y_to_z_approach.trajectory.npz"
        )
    homology = probe.load(probe.HOMOLOGY)["homology_convention"]
    critical_center = complex(*task["critical_center"])
    with np.load(trajectory_path) as saved:
        saved_w = np.asarray(saved["w"], dtype=np.complex128)
        saved_roots = np.asarray(saved["roots"], dtype=np.complex128)
        saved_radii = np.asarray(saved["root_radius_uppers"], dtype=np.float64)
    saved_distances = np.abs(saved_w - critical_center)
    saved_minimum = float(np.min(saved_distances))
    approach_indices = np.flatnonzero(saved_distances <= saved_minimum * 1.001)
    if not len(approach_indices):
        raise AssertionError("saved trajectory has no perturbed approach point")
    approach_index = int(approach_indices[0])
    approach = complex(saved_w[approach_index])

    labelled_roots = saved_roots[approach_index]
    labelled_radii = saved_radii[approach_index]
    matching_ratios = []
    endpoint_transport = None
    for fibration in fibration_paths:
        transport = probe.Q79SelectedAlignmentPeriodRootTransport(
            fibration, homology, omitted=probe.OMITTED, dps=70
        )
        unordered, unordered_radii = transport.roots_at(approach)
        labelled_roots, labelled_radii, ratio = transport.match(
            labelled_roots, unordered, unordered_radii
        )
        matching_ratios.append(float(ratio))
        endpoint_transport = transport
    if endpoint_transport is None:
        raise AssertionError("endpoint root transport was not constructed")

    endpoint_unordered, endpoint_unordered_radii = endpoint_transport.roots_at(approach)
    direct_roots, _, direct_ratio = endpoint_transport.match(
        saved_roots[approach_index],
        endpoint_unordered,
        endpoint_unordered_radii,
    )
    sequential_to_direct_difference = float(
        np.max(abs(labelled_roots - direct_roots))
    )
    rebased_roots = saved_roots.copy()
    rebased_root_radii = saved_radii.copy()
    rebased_roots[approach_index] = labelled_roots
    rebased_root_radii[approach_index] = labelled_radii
    with tempfile.TemporaryDirectory(prefix=f"q79-pc-rebase-{index:03d}-") as directory:
        rebased_path = Path(directory) / "trajectory.npz"
        np.savez_compressed(
            rebased_path,
            w=saved_w,
            roots=rebased_roots,
            root_radius_uppers=rebased_root_radii,
        )
        execution = probe.execute_selected_alignment_thimble_period(
            fibration_path=endpoint_fibration,
            homology_convention=homology,
            trajectory_path=rebased_path,
            trajectory_packet=trajectory_packet,
            critical_center=critical_center,
            omitted=probe.OMITTED,
            epsilon=1.0e-5,
            inner_order=160,
            dps=70,
            root_step_ratio=0.12,
            rtol=2.0e-10,
            atol=2.0e-13,
            gauss_manin_chart="t",
            local_direct_cutoff=0.0,
            local_outer_order=32,
            tail_outer_order=24,
        )
    period = probe.complex_vector(execution["period_values"])
    base = probe.complex_vector(
        [row["value"] for row in execution["base_fiber_propagated_periods"]]
    )
    central_period = probe.complex_vector(central_packet["execution"]["period_values"])
    positive = float(np.linalg.norm(period - central_period))
    negative = float(np.linalg.norm(period + central_period))
    continuity_sign = 1 if positive <= negative else -1
    period *= continuity_sign
    base *= continuity_sign
    return {
        "schema": "MTTQ79CovariantParameterContinuedThimbleCache.v1",
        "cache_algorithm": CACHE_ALGORITHM,
        "distinguished_index": index,
        "root_id": root_id,
        "line_chart": line_chart,
        "critical_center": probe.complex_pair(critical_center),
        "period_values": probe.encoded_complex_vector(period),
        "base_fiber_propagated_periods": probe.encoded_complex_vector(base),
        "continuity_sign_relative_to_selected_packet": continuity_sign,
        "positive_continuity_residual": positive,
        "negative_continuity_residual": negative,
        "approach_root_rebase": {
            "algorithm": CACHE_ALGORITHM,
            "approach_index": approach_index,
            "approach_parameter": probe.complex_pair(approach),
            "parameter_substeps": len(fibration_paths),
            "matching_ratios": matching_ratios,
            "maximum_matching_ratio": max(matching_ratios),
            "direct_endpoint_matching_ratio": float(direct_ratio),
            "sequential_to_direct_maximum_root_difference": (
                sequential_to_direct_difference
            ),
            "endpoint_maximum_root_displacement_from_central": float(
                np.max(abs(labelled_roots - saved_roots[approach_index]))
            ),
        },
        "runner_source": probe.relative(Path(__file__).resolve()),
        "runner_source_sha256": sha256(Path(__file__).resolve()),
        "numerics": execution["numerics"],
    }
