from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import math
from pathlib import Path

from flint import ctx

import certify_q79_full_lower_contour_homotopy as contour
from certify_q79_selected_side_beta_defect_transport import A124, SOURCE, WALL


ROOT = contour.ROOT
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2delignebetaperiodandintegralbranchexecution"
)
OUTPUT = DIRECTORY / "pgl3_left_upper_0p05_homotopy.a390h.interval.json"
CHECKPOINT = DIRECTORY / "pgl3_left_upper_0p05_homotopy.a390h.checkpoint.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79LeftUpperContourHomotopy_A390H_v1.md"
A379 = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
    / "n3.beta_hessian.interval.json"
)
ARTIFACT = "A390H"
NAMES = [
    "reduction_determinant",
    "y_chart_scale",
    "q_leading_coefficient",
    "q_discriminant",
    "g_on_q_norm",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def atomic_dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def pair(value: complex) -> dict[str, str]:
    return {
        "real": format(value.real, ".17g"),
        "imaginary": format(value.imag, ".17g"),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--checkpoint", type=Path, default=CHECKPOINT)
    parser.add_argument("--dps", type=int, default=90)
    parser.add_argument("--maximum-depth", type=int, default=30)
    parser.add_argument("--relative-radius-gate", type=float, default=0.5)
    parser.add_argument("--taylor-order", type=int, default=10)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--initial-subdivisions", type=int, default=16)
    parser.add_argument("--checkpoint-batch", type=int, default=8)
    parser.add_argument("--real-right", type=float, default=0.65)
    parser.add_argument("--imaginary-top", type=float, default=0.05)
    parser.add_argument("--allow-obstructed", action="store_true")
    parser.add_argument("--restart", action="store_true")
    arguments = parser.parse_args()
    ctx.dps = arguments.dps
    if not arguments.real_right > 0:
        raise ValueError("real-right must be positive")
    if not arguments.imaginary_top > 0:
        raise ValueError("imaginary-top must be positive")

    right = arguments.real_right
    top = arguments.imaginary_top
    # Clockwise boundary of [0,right] x [0,top].
    corners = [0 + 0j, top * 1j, right + top * 1j, right + 0j, 0 + 0j]
    tasks = []
    for left, endpoint in zip(corners, corners[1:]):
        for index in range(arguments.initial_subdivisions):
            chunk_left = left + (endpoint - left) * (
                index / arguments.initial_subdivisions
            )
            chunk_right = left + (endpoint - left) * (
                (index + 1) / arguments.initial_subdivisions
            )
            tasks.append(
                (
                    chunk_left,
                    chunk_right,
                    arguments.maximum_depth,
                    arguments.relative_radius_gate,
                    arguments.taylor_order,
                )
            )
    configuration = {
        "dps": arguments.dps,
        "maximum_depth": arguments.maximum_depth,
        "relative_radius_gate": arguments.relative_radius_gate,
        "taylor_order": arguments.taylor_order,
        "initial_subdivisions_per_side": arguments.initial_subdivisions,
        "real_right": format(right, ".17g"),
        "imaginary_top": format(top, ".17g"),
        "task_count": len(tasks),
        "A124_sha256": sha256(A124),
        "wall_sha256": sha256(WALL),
        "alignment_sha256": sha256(SOURCE),
        "A379_sha256": sha256(A379),
        "obstruction_model_source_sha256": sha256(Path(contour.__file__).resolve()),
        "builder_source_sha256": sha256(Path(__file__).resolve()),
    }
    chunks: list[list[dict]] = []
    if arguments.checkpoint.exists() and not arguments.restart:
        checkpoint = json.loads(arguments.checkpoint.read_text(encoding="utf-8"))
        if checkpoint.get("configuration") != configuration:
            raise ValueError("A390H checkpoint configuration or authority is stale")
        chunks = checkpoint["chunks"]
        if len(chunks) > len(tasks):
            raise ValueError("A390H checkpoint contains excess tasks")
        print(f"resuming A390H after {len(chunks)}/{len(tasks)} boundary tasks", flush=True)
    batch_size = max(1, arguments.checkpoint_batch)
    with concurrent.futures.ProcessPoolExecutor(
        max_workers=arguments.workers,
        initializer=contour.initialize_worker,
        initargs=(arguments.dps,),
    ) as executor:
        while len(chunks) < len(tasks):
            stop = min(len(tasks), len(chunks) + batch_size)
            batch = list(executor.map(contour.certify_boundary_chunk, tasks[len(chunks):stop]))
            chunks.extend(batch)
            atomic_dump(
                arguments.checkpoint,
                {
                    "schema": "MTTQ79LeftUpperContourHomotopyCheckpoint.v1",
                    "configuration": configuration,
                    "completed_chunk_count": len(chunks),
                    "chunks": chunks,
                },
            )
            print(f"A390H boundary progress {len(chunks)}/{len(tasks)}", flush=True)
    leaves = [leaf for chunk in chunks for leaf in chunk]
    windings = {name: contour.winding_certificate(leaves, name) for name in NAMES}
    family_regular = all(
        windings[name]["winding_number"] == 0
        for name in ("reduction_determinant", "y_chart_scale")
    )
    finite_flat_regular = all(
        windings[name]["winding_number"] == 0
        for name in ("q_leading_coefficient", "g_on_q_norm")
    )
    q_winding = int(windings["q_discriminant"]["winding_number"])
    if q_winding > 0:
        raise ArithmeticError("clockwise q-discriminant boundary has positive winding")
    q_collision_count = -q_winding
    homotopy_certified = family_regular and finite_flat_regular
    selected_domain = abs(right - 0.65) < 1.0e-15 and abs(top - 0.05) < 1.0e-15
    candidate_waypoints = [
        0 + 0j,
        top * 1j,
        right + top * 1j,
        right - 0.1j,
        0.82 - 0.1j,
        0.82 + 0j,
        1 + 0j,
    ]
    packet = {
        "artifact": ARTIFACT,
        "schema": "MTTQ79LeftUpperContourHomotopyIntervalCertificate.v1",
        "status": (
            "LEFT_UPPER_CONTOUR_HOMOTOPY_INTERVAL_CERTIFIED"
            if homotopy_certified
            else "LEFT_UPPER_CONTOUR_HOMOTOPY_OBSTRUCTED"
        ),
        "domain": {
            "real_interval": ["0", format(right, ".17g")],
            "imaginary_interval": ["0", format(top, ".17g")],
            "boundary_orientation": "clockwise",
            "corners": [pair(value) for value in corners],
            "elliptic_pole_exclusion": (
                "For lambda=x+iy in this rectangle, "
                "w=1/4+i/4+i*lambda has Re(w)=1/4-y in [0.20,0.25] "
                "and hence cannot meet the Z+iZ pole lattice."
            ),
        },
        "route_replacement": {
            "selected_A379_initial_segment": [pair(0 + 0j), pair(right + 0j)],
            "replacement_initial_segment": [
                pair(0 + 0j),
                pair(top * 1j),
                pair(right + top * 1j),
                pair(right + 0j),
            ],
            "candidate_beta_Hessian_waypoints": [
                pair(value) for value in candidate_waypoints
            ],
            "remaining_A379_segments_unchanged": True,
        },
        "boundary_cover": {
            "leaf_count": len(leaves),
            "maximum_depth": max(leaf["depth"] for leaf in leaves),
            "relative_radius_gate": arguments.relative_radius_gate,
            "taylor_order": arguments.taylor_order,
            "worker_count": arguments.workers,
            "initial_subdivisions_per_side": arguments.initial_subdivisions,
            "minimum_absolute_lower_bounds": {
                name: min(leaf["absolute_lower_bounds"][name] for leaf in leaves)
                for name in NAMES
            },
            "leaves": leaves,
        },
        "argument_principle": windings,
        "execution": {
            "configuration": configuration,
            "checkpoint": relative(arguments.checkpoint),
            "checkpoint_sha256": sha256(arguments.checkpoint),
            "completed_chunk_count": len(chunks),
        },
        "finite_flat_divisor_theorem": {
            "applies": finite_flat_regular,
            "q_discriminant_zero_count_with_multiplicity": q_collision_count,
            "individual_q_roots_globally_labelled": q_collision_count == 0,
            "symmetric_divisor_and_quotient_trace_extend": finite_flat_regular,
        },
        "decision": {
            "smooth_genus_two_family_on_closed_upper_left_rectangle": family_regular,
            "finite_flat_symmetric_divisor_preserved": finite_flat_regular,
            "A379_to_left_upper_route_homotopy_certified": homotopy_certified,
            "normal_function_endpoint_branch_preserved": homotopy_certified,
            "selected_domain_parameters_used": selected_domain,
        },
        "authority": {
            "A124_transport_source": authority(A124),
            "selected_wall_source": authority(WALL),
            "selected_alignment_source": authority(SOURCE),
            "A379_selected_beta_Hessian_route": authority(A379),
            "obstruction_model_source": authority(Path(contour.__file__).resolve()),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "closed_rectangle_argument_principle_executed": True,
            "A379_route_replacement_homotopy_interval_certified": homotopy_certified,
            "candidate_route_beta_Hessian_transport_executed": False,
            "candidate_route_tighter_than_A379_certified": False,
            "observed_SM_values_used": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "execute the A379 beta/Hessian system on the certified left-upper route "
            "and compare all 72 endpoint enclosure radii"
            if homotopy_certified
            else "choose a smaller upper-left rectangle or another admissible route"
        ),
    }
    dump(arguments.output, packet)
    if selected_domain:
        NOTE.write_text(
            "# MTT q79 Left-Upper Contour Homotopy (A390H) v1\n\n"
            f"The rectangle `[0,{right:.17g}] x [0,{top:.17g}]` has "
            f"{len(leaves)} validated boundary leaves. The smooth-family gate is "
            f"`{family_regular}` and the finite-flat symmetric-divisor gate is "
            f"`{finite_flat_regular}`. Therefore the proposed replacement of the "
            "first A379 segment is interval-homotopic exactly when both gates pass.\n\n"
            "This certificate does not execute the beta/Hessian transport and does "
            "not prove an interval-Newton zero.\n",
            encoding="utf-8",
        )
    print(
        json.dumps(
            {
                "artifact": ARTIFACT,
                "homotopy_certified": homotopy_certified,
                "leaf_count": len(leaves),
                "maximum_depth": packet["boundary_cover"]["maximum_depth"],
                "windings": {
                    name: value["winding_number"] for name, value in windings.items()
                },
            },
            indent=2,
            sort_keys=True,
        ),
        flush=True,
    )
    if not homotopy_certified and not arguments.allow_obstructed:
        raise AssertionError("the left-upper rectangle contains an obstruction")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
