from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from pathlib import Path

from flint import acb, acb_mat, arb, ctx

import certify_q79_height4_d087_full_residue_main_interval as n3_engine
import certify_q79_selected_side_base_lift_interval as serializer
import certify_q79_selected_side_beta_defect_transport as validated
import q79_fast_taylor_runtime as fast
import run_q79_augmented_beta_transport as augmented
import run_q79_height4_junction_operator_sweeps as junction


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
)
A383 = VALIDATED / "n3.rank3.handle_hessian.interval.json"
A383_A_CHECKPOINT = VALIDATED / "n3.handleA.hessian.checkpoint.json"
A404 = VALIDATED / "n3.junction_operator_sweep.a404.json"
A411 = VALIDATED / "jop" / "trunk.a411.json"
DIRECTORY = VALIDATED / "ol"
SOURCE = DIRECTORY / "ha.src.a418.json"
CHECKPOINT = DIRECTORY / "ha.a418.ckpt.json"
OUTPUT = DIRECTORY / "ha.a418.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourAHandleOuterHubAffine_A418_v1.md"
FAST_AUDIT = ROOT / "proof_corpus" / "selected_q79fasttaylorruntime_equivalence_audit.py"
HUB = 0.1 + 0.0j
ENTRY = 0.0 - 0.1j
ENDPOINT = 0.0 - 1.0j


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def interval_entry(value: dict) -> acb:
    center = value["center"]
    radius = float(value["component_radius_upper"])
    real = float(center["real"])
    imaginary = float(center["imaginary"])
    serialization = max(math.ulp(real), math.ulp(imaginary), 1.0e-300)
    outward = math.nextafter(radius + serialization, math.inf)
    return acb(
        arb(format(real, ".17g"), format(outward, ".17g")),
        arb(format(imaginary, ".17g"), format(outward, ".17g")),
    )


def interval_matrix(rows: list[list[dict]]) -> acb_mat:
    return acb_mat([[interval_entry(value) for value in row] for row in rows])


def column(values: list[acb]) -> acb_mat:
    result = acb_mat(len(values), 1)
    for row, value in enumerate(values):
        result[row, 0] = value
    return result


def encoded_ball(value: acb) -> dict:
    bounds = serializer.complex_interval(value)
    persisted = validated.interval_from_bounds(bounds)
    center = validated.midpoint(persisted)
    return {
        "interval_bounds": bounds,
        "interval_center": {
            "real": format(center.real, ".17g"),
            "imaginary": format(center.imag, ".17g"),
        },
        "interval_radius_upper": validated.radius_upper(persisted),
    }


def encoded_matrix(matrix: acb_mat) -> list[list[dict]]:
    return [
        [encoded_ball(matrix[row, col]) for col in range(matrix.ncols())]
        for row in range(matrix.nrows())
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--order", type=int, default=32)
    parser.add_argument("--initial-step", type=float, default=0.003)
    parser.add_argument("--minimum-step", type=float, default=1.0e-12)
    parser.add_argument("--maximum-steps", type=int, default=100000)
    parser.add_argument("--restart", action="store_true")
    arguments = parser.parse_args()
    if arguments.dps < 90 or arguments.order < 24:
        raise ValueError("A418 requires at least 90 digits and Taylor order 24")
    ctx.dps = arguments.dps
    started = time.perf_counter()

    handle = load(A383)
    handle_checkpoint = load(A383_A_CHECKPOINT)
    manifest = load(A404)
    trunk = load(A411)
    if handle.get("artifact") != "A383" or not handle["strict_scope"]["rank3_handle_Hessian_interval_closed"]:
        raise AssertionError("A418 requires A383")
    if handle["authority"]["A_path_checkpoint"]["sha256"] != sha256(A383_A_CHECKPOINT):
        raise AssertionError("A418 A383 A-handle checkpoint is stale")
    if trunk.get("artifact") != "A411" or not trunk["strict_scope"]["common_hub_to_canonical_base_operator_closed"]:
        raise AssertionError("A418 requires A411")
    handle_entry = next(
        row for row in manifest["ordered_entry_rows"]
        if row.get("kind") == "selected_A_handle_entry"
    )
    entry = complex(
        float(handle_entry["point"]["real"]),
        float(handle_entry["point"]["imaginary"]),
    )
    hub = complex(
        float(manifest["operational_disk"]["hub"]["real"]),
        float(manifest["operational_disk"]["hub"]["imaginary"]),
    )
    if abs(hub - HUB) > 1.0e-16 or abs(entry - ENTRY) > 1.0e-16:
        raise AssertionError("A418 operational handle path changed")

    base_periods = [
        validated.decoded_acb(value)
        for value in handle_checkpoint["configuration"]["initial_periods"]
    ]
    if len(base_periods) != 5:
        raise AssertionError("A418 A383 base period dimension changed")
    trunk_period = interval_matrix(trunk["period_transport_5_by_5"])
    trunk_residue = interval_matrix(trunk["integrated_residue_operator_8_by_5"])
    if validated.lower(abs(trunk_period.det())) <= 0.0:
        raise AssertionError("A418 A411 period operator is singular")
    hub_period_column = trunk_period.inv() * column(base_periods)
    hub_periods = [hub_period_column[row, 0] for row in range(5)]
    replay = trunk_period * hub_period_column
    if any(not replay[row, 0].overlaps(base_periods[row]) for row in range(5)):
        raise AssertionError("A418 hub period source does not replay A383 base periods")

    source = {
        "schema": "MTTQ79HeightFourAHandleHubSource.v1",
        "status": "SELECTED_A_HANDLE_HUB_PERIOD_BALLS_DERIVED",
        "artifact": "A418S",
        "y_chart_base_lift": [serializer.complex_interval(value) for value in hub_periods],
        "source_identity": "p_hub=U_A411^-1*p_base_A383",
        "authority": {
            "A383_selected_A_handle": authority(A383),
            "A383_A_path_checkpoint": authority(A383_A_CHECKPOINT),
            "A404_operational_path": authority(A404),
            "A411_terminal_trunk": authority(A411),
            "builder_source": authority(Path(__file__).resolve()),
        },
    }
    dump(SOURCE, source)
    source_hash = sha256(SOURCE)
    builder_hash = sha256(Path(__file__).resolve())
    path_name = (
        f"A418 selected A-handle hub-to-endpoint dps={arguments.dps} "
        f"source={source_hash[:16]} builder={builder_hash[:16]}"
    )
    if arguments.restart and CHECKPOINT.exists():
        CHECKPOINT.unlink()
    if CHECKPOINT.exists():
        checkpoint = load(CHECKPOINT)
        if checkpoint.get("A418_source_sha256") != source_hash or checkpoint.get(
            "A418_builder_sha256"
        ) != builder_hash:
            raise ValueError("A418 checkpoint authority changed")

    original_dump = validated.atomic_dump

    def stamped_dump(path: Path, value: dict) -> None:
        payload = dict(value)
        if path == CHECKPOINT:
            payload["A418_source_sha256"] = source_hash
            payload["A418_builder_sha256"] = builder_hash
        original_dump(path, payload)

    system = n3_engine.exact_target_system(arguments.dps)
    originals = junction.install_augmented_homogeneous_engine()
    validated.BASE_LIFT = SOURCE
    validated.atomic_dump = stamped_dump
    fast.install()
    try:
        transport = validated.execute_validated_path(
            system,
            waypoints=[HUB, ENTRY, ENDPOINT],
            path_name=path_name,
            order=arguments.order,
            initial_step=arguments.initial_step,
            minimum_step=arguments.minimum_step,
            maximum_steps=arguments.maximum_steps,
            checkpoint_path=CHECKPOINT,
            resume=CHECKPOINT.exists(),
        )
    finally:
        fast.uninstall()
        validated.atomic_dump = original_dump
        junction.restore_engine(originals)

    completed = load(CHECKPOINT)
    center = [validated.decoded_acb(value) for value in completed["center"]]
    frame = validated.LiftErrorFrame(
        fundamental=validated.decoded_matrix(completed["lift_fundamental"]),
        coordinate_radii=[arb(value) for value in completed["coordinate_radii"]],
    )
    generator = augmented.dynamic_generator_matrix(frame)
    if len(center) != 13 or generator.nrows() != 13 or generator.ncols() != 13:
        raise AssertionError("A418 final affine state dimension changed")

    hub_outer_center = hub_periods + center[5:13]
    hub_outer_generator = acb_mat(13, 13)
    for row in range(5):
        hub_outer_generator[row, row] = acb(hub_periods[row].rad())
    for row in range(5, 13):
        for col in range(13):
            hub_outer_generator[row, col] = generator[row, col]
    component_radii = [
        validated.radius_upper(hub_outer_center[row])
        + validated.upper(
            sum((abs(hub_outer_generator[row, col]) for col in range(13)), arb(0))
        )
        for row in range(13)
    ]

    base_to_hub_residue = -(trunk_residue * hub_period_column)
    a383_full_centers = [
        validated.decoded_acb(value) for value in handle_checkpoint["center"][5:13]
    ]
    a383_full_radii = [
        validated.upper(arb(value)) for value in handle_checkpoint["output_radii"][:8]
    ]
    recomposition_differences = []
    recomposition_margins = []
    for row in range(8):
        recomposed = center[5 + row] + base_to_hub_residue[row, 0]
        difference = abs(validated.midpoint(recomposed) - validated.midpoint(a383_full_centers[row]))
        outer_radius = component_radii[5 + row]
        base_hub_radius = validated.radius_upper(base_to_hub_residue[row, 0])
        margin = outer_radius + base_hub_radius + a383_full_radii[row] - difference
        if margin < 0.0:
            raise AssertionError(f"A418 row {row} misses the independent A383 A-handle")
        recomposition_differences.append(difference)
        recomposition_margins.append(margin)

    payload = {
        "schema": "MTTQ79HeightFourAHandleOuterHubAffine.v1",
        "status": "SELECTED_A_HANDLE_HUB_TO_ENDPOINT_13_STATE_AFFINE_PATH_CERTIFIED",
        "artifact": "A418",
        "path": {
            "waypoints": [
                {"real": format(value.real, ".17g"), "imaginary": format(value.imag, ".17g")}
                for value in (HUB, ENTRY, ENDPOINT)
            ],
            "identity": "base_to_endpoint=(base_to_hub)+(hub_to_entry)+(entry_to_A_endpoint)",
            "base_to_hub_augmented_residue_rule": "q_BH=-V_0*U_0^-1*p_base",
        },
        "hub_outer_affine_center_13": [encoded_ball(value) for value in hub_outer_center],
        "hub_outer_affine_generator_13_by_13": encoded_matrix(hub_outer_generator),
        "hub_outer_component_total_radius_uppers": component_radii,
        "A383_A_handle_crosscheck": {
            "maximum_center_difference": max(recomposition_differences),
            "minimum_overlap_margin": min(recomposition_margins),
            "all_eight_rows_overlap": True,
        },
        "validated_transport": transport,
        "summary": {
            "accepted_steps": transport["execution"]["accepted_step_count"],
            "rejected_steps": transport["execution"]["rejected_step_count"],
            "maximum_hub_period_radius_upper": max(component_radii[:5]),
            "maximum_outer_residue_radius_upper": max(component_radii[5:]),
            "maximum_A383_center_difference": max(recomposition_differences),
            "minimum_A383_overlap_margin": min(recomposition_margins),
        },
        "authority": {
            "A383_selected_handle_execution": authority(A383),
            "A383_A_path_checkpoint": authority(A383_A_CHECKPOINT),
            "A404_operational_handle_path": authority(A404),
            "A411_terminal_trunk": authority(A411),
            "A418_hub_source": authority(SOURCE),
            "completed_affine_checkpoint": authority(CHECKPOINT),
            "homogeneous_system": authority(Path(n3_engine.__file__).resolve()),
            "augmented_transport": authority(Path(augmented.__file__).resolve()),
            "C_backed_Taylor_runtime": authority(Path(fast.__file__).resolve()),
            "C_backed_Taylor_equivalence_audit": authority(FAST_AUDIT),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "selected_A_handle_hub_period_source_derived": True,
            "selected_hub_entry_endpoint_path_executed": True,
            "full_13_state_affine_frame_retained": True,
            "independent_A383_full_A_handle_crosscheck_closed": True,
            "attached_to_all_76_thimble_hub_sum": False,
            "exact_period_boundary_zero_applied": False,
            "beta_minus_B_block_attached": False,
            "full_common_relative_chain_transport_executed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "attach A418 to A417, use A403 to remove the exact zero common-trunk "
            "period block, and splice the resulting chain-plus-A-handle residues "
            "to the correlated A402 beta-minus-B block"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four A-Handle Outer Hub Affine Path (A418) v1\n\n"
        "A418 derives the selected A-handle period balls at the operational hub "
        "from A383 and A411, then validates the selected path through the A404 "
        "handle entry to `-i` in one 13-state affine frame.\n\n"
        f"All eight recomposed rows overlap the independent A383 A-handle; minimum "
        f"margin `{min(recomposition_margins):.12g}`. Attachment to A417, exact "
        "period cancellation, the A402 splice, Newton inclusion, covariant zero, "
        "and full SM closure remain open.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}", flush=True)
    print(f"wrote {relative(NOTE)}", flush=True)
    print(json.dumps(payload["summary"], indent=2), flush=True)
    print(f"elapsed_seconds={time.perf_counter() - started:.6g}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
