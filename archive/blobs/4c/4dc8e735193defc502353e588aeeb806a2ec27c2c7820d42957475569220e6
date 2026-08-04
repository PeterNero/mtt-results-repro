from __future__ import annotations

import hashlib
import json
from pathlib import Path

from flint import acb, acb_mat, arb, ctx

import certify_q79_height4_target_full_residue_interval as generic
import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_selected_alignment_single_E32_thimble_main_interval as pilot
import certify_q79_selected_side_beta_defect_transport as validated
import q79_fast_taylor_runtime as fast


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = main_hessian.VALIDATED
SOURCE_DIRECTORY = VALIDATED / "far_source"
OUTPUT = SOURCE_DIRECTORY / "ranked.first_step.a399.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourRankedFarCutFirstStep_A399_v1.md"
FAST_AUDIT = ROOT / "proof_corpus" / "selected_q79fasttaylorruntime_equivalence_audit.py"
ARTIFACT = "A399"
INDICES = (57, 27, 82, 17, 4)
STEP = 1.0e-4
ORDER = 24
DPS = 90


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


def execute_target(index: int) -> dict:
    source_path = SOURCE_DIRECTORY / f"d{index:03d}.1em03.json"
    source = load(source_path)
    target = source["selected_target"]
    if int(target["distinguished_index"]) != index:
        raise AssertionError(f"d{index:03d} far-cut source identity changed")
    system, rank, row = main_hessian.selected_system(index, DPS)
    if rank != int(target["A219_contribution_rank"]):
        raise AssertionError(f"d{index:03d} contribution rank changed")
    if row["root_id"] != target["root_id"] or system.line_chart != target["line_chart"]:
        raise AssertionError(f"d{index:03d} source geometry changed")

    periods = [
        validated.decoded_acb(value)
        for value in source["far_cut_source"]["full_precision_period_balls"]
    ]
    start_packet = source["far_cut_source"]["cutoff_start_binary64"]
    start = complex(float(start_packet["real"]), float(start_packet["imaginary"]))
    direction = -start / abs(start)
    centers, frames = initial_state(system, periods)
    output_centers, output_frames, diagnostics = (
        generic.main_engine.validated_all_residue_rows_step(
            system,
            start,
            direction,
            STEP,
            centers,
            frames,
            order=ORDER,
        )
    )
    maximum_radius = float(diagnostics["maximum_residue_coordinate_radius_upper"])
    if maximum_radius >= 1.0e-12:
        raise ArithmeticError(
            f"d{index:03d} far-cut first-step residue radius is unexpectedly wide: "
            f"{maximum_radius:.6e}"
        )
    return {
        "distinguished_index": index,
        "A219_contribution_rank": rank,
        "root_id": row["root_id"],
        "line_chart": system.line_chart,
        "signed_chain_coefficient": int(row["signed_coefficient"]),
        "start_binary64": start_packet,
        "direction_binary64": {
            "real": format(direction.real, ".17g"),
            "imaginary": format(direction.imag, ".17g"),
            "real_hex": float(direction.real).hex(),
            "imaginary_hex": float(direction.imag).hex(),
        },
        "step": STEP,
        "initial_period_maximum_radius_upper": max(
            validated.radius_upper(value) for value in periods
        ),
        "output_centers": [
            [validated.encoded_acb(value) for value in row_values]
            for row_values in output_centers
        ],
        "output_frames": [generic.encoded_frame(frame) for frame in output_frames],
        "diagnostics": diagnostics,
        "selected_chain_first_step_radius_upper": (
            abs(int(row["signed_coefficient"])) * maximum_radius
        ),
        "source_authority": authority(source_path),
        "canonical_main_authority": authority(
            main_hessian.target_paths(index)["canonical_main"]
        ),
    }


def main() -> int:
    ctx.dps = DPS
    fast.install()
    try:
        rows = [execute_target(index) for index in INDICES]
    finally:
        fast.uninstall()

    maximum_radius = max(
        float(row["diagnostics"]["maximum_residue_coordinate_radius_upper"])
        for row in rows
    )
    payload = {
        "schema": "MTTQ79HeightFourRankedFarCutFirstStep.v1",
        "status": "RANKED_DOMINANT_FIVE_FAR_CUT_LOCAL_TRANSPORT_FEASIBILITY_CERTIFIED",
        "artifact": ARTIFACT,
        "method": {
            "description": (
                "one rigorous homogeneous all-eight residue step from each audited "
                "epsilon=1e-3 direct-cycle source toward the common basepoint"
            ),
            "dps": DPS,
            "Taylor_order": ORDER,
            "step": STEP,
            "ranked_indices": list(INDICES),
        },
        "targets": rows,
        "summary": {
            "target_count": len(rows),
            "maximum_first_step_residue_radius_upper": maximum_radius,
            "all_first_steps_below_1e_minus_12": maximum_radius < 1.0e-12,
        },
        "authority": {
            "all_row_main_engine": authority(Path(generic.main_engine.__file__).resolve()),
            "selected_system_engine": authority(Path(main_hessian.__file__).resolve()),
            "C_backed_Taylor_runtime": authority(Path(fast.__file__).resolve()),
            "C_backed_Taylor_equivalence_audit": authority(FAST_AUDIT),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "ranked_far_cut_sources_consumed": True,
            "one_local_step_per_target_interval_closed": True,
            "complete_main_transports_closed": False,
            "matching_tail_intervals_closed": False,
            "full_target_period_intervals_closed": False,
            "full_chain_recomposition_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "complete A397 for d057, replay A398, then promote the same far-cut "
            "transport pattern in descending weighted interval contribution order"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four Ranked Far-Cut First Step (A399) v1\n\n"
        "A399 executes one rigorous all-eight homogeneous residue step from each "
        "audited `epsilon=1e-3` source for `d057`, `d027`, `d082`, `d017`, and "
        "`d004`. These are the five largest weighted source-width contributions "
        "in the current 76-thimble chain.\n\n"
        f"The largest first-step residue-coordinate radius is "
        f"`{maximum_radius:.12g}`. This certifies local feasibility of the far-cut "
        "route for all five targets; it does not replace any complete main or tail "
        "transport and does not certify the full chain or a Krawczyk inclusion.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
