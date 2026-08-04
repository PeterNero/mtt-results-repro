from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from flint import acb, ctx

import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_selected_alignment_E32_handle_combination_interval as handle
import certify_q79_selected_alignment_single_E32_thimble_main_interval as pilot
import certify_q79_selected_side_beta_defect_transport as validated


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIRECTORY = main_hessian.VALIDATED / "far_source"
ARTIFACT = "A380FS"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
        "real_binary64_hex": float(value.real).hex(),
        "imaginary_binary64_hex": float(value.imag).hex(),
    }


def paths(index: int, epsilon: float) -> tuple[Path, Path]:
    epsilon_label = format(epsilon, ".0e").replace("-", "m").replace("+", "p")
    stem = f"d{index:03d}.{epsilon_label}"
    return (
        OUTPUT_DIRECTORY / f"{stem}.json",
        ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{index:03d}SelectedFarCutPeriodSource_A380FS_v1.md",
    )


def execute(arguments: argparse.Namespace) -> dict:
    canonical_path = main_hessian.target_paths(arguments.index)["canonical_main"]
    canonical = load(canonical_path)
    system, rank, row = main_hessian.selected_system(arguments.index, arguments.dps)
    node_parameter = validated.decoded_acb(
        canonical["certified_node"]["parameter_ball"]
    )
    node_center = handle.midpoint(node_parameter)
    start = handle.midpoint(
        node_center * acb(format(1.0 - arguments.epsilon, ".17g"))
    )
    roots, leading = pilot.roots_at(system, start)
    cut_pair = tuple(
        int(value)
        for value in canonical["selected_target"][
            "near_node_colliding_pair_zero_based"
        ]
    )
    if len(cut_pair) != 2 or not 0 <= cut_pair[0] < cut_pair[1] < len(roots):
        raise AssertionError("preselected cutoff pair is malformed")
    minimum_root_separation = min(
        validated.lower(abs(roots[left] - roots[right]))
        for left in range(len(roots))
        for right in range(left)
    )
    if minimum_root_separation <= 0.0:
        raise AssertionError("far-cut root balls are not pairwise separated")
    periods, diagnostics = handle.direct_cut_periods(
        roots,
        leading,
        cut_pair,
        segments=arguments.cut_segments,
        tolerance=arguments.cut_tolerance,
    )
    encoded_periods = [validated.encoded_acb(value) for value in periods]
    serialized_periods = [validated.decoded_acb(value) for value in encoded_periods]
    raw_maximum_radius = max(validated.radius_upper(value) for value in periods)
    maximum_radius = max(
        raw_maximum_radius,
        max(validated.radius_upper(value) for value in serialized_periods),
    )
    if not 0.0 < maximum_radius < arguments.maximum_period_radius:
        raise ArithmeticError(
            f"far-cut period radius {maximum_radius:.6e} exceeds source budget"
        )

    output, note = paths(arguments.index, arguments.epsilon)
    packet = {
        "schema": "MTTQ79HeightFourSelectedFarCutPeriodSource.v1",
        "status": "SELECTED_NODE_FAR_CUT_FIVE_PERIOD_ARBITRARY_PRECISION_SOURCE_CERTIFIED",
        "artifact": ARTIFACT,
        "selected_target": {
            "distinguished_index": arguments.index,
            "A219_contribution_rank": rank,
            "root_id": row["root_id"],
            "line_chart": system.line_chart,
            "signed_chain_coefficient": int(row["signed_coefficient"]),
            "canonical_cutoff_epsilon": float(
                canonical["selected_target"]["endpoint_cutoff_epsilon"]
            ),
            "selected_far_cut_epsilon": arguments.epsilon,
            "preselected_pair_zero_based": list(cut_pair),
        },
        "far_cut_source": {
            "node_parameter_ball": canonical["certified_node"]["parameter_ball"],
            "node_root_ball": canonical["certified_node"]["double_root_ball"],
            "node_center_binary64": pair(node_center),
            "cutoff_start_binary64": pair(start),
            "full_precision_period_balls": encoded_periods,
            "raw_quadrature_maximum_period_radius_upper": raw_maximum_radius,
            "serialized_source_maximum_period_radius_upper": max(
                validated.radius_upper(value) for value in serialized_periods
            ),
            "maximum_period_radius_upper": maximum_radius,
            "minimum_root_ball_separation_lower": minimum_root_separation,
            "direct_cut_diagnostics": diagnostics,
        },
        "numerics": {
            "dps": arguments.dps,
            "cut_segments": arguments.cut_segments,
            "cut_tolerance": arguments.cut_tolerance,
            "maximum_period_radius": arguments.maximum_period_radius,
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "canonical_ordinary_main": canonical_path,
                "selected_fibration": main_hessian.main_engine.FIBRATION,
                "direct_cut_period_engine": Path(handle.__file__).resolve(),
                "cutoff_root_engine": Path(pilot.__file__).resolve(),
                "builder_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "canonical_certified_node_reused": True,
            "A219_preselected_vanishing_pair_reused": True,
            "far_cut_period_source_interval_closed": True,
            "far_cut_main_Hessian_interval_closed": False,
            "far_cut_tail_Hessian_interval_closed": False,
            "far_cut_full_Hessian_interval_closed": False,
            "full_76_target_chain_Hessian_interval_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "transport the A378 main Hessian from this source and splice the "
            "matching differentiated A135 tail, then replay the canonical full row"
        ),
    }
    dump(output, packet)
    note.write_text(
        f"# MTT q79 Height-Four d{arguments.index:03d} Selected Far-Cut Period Source (A380FS) v1\n\n"
        f"The certified node and A219-selected vanishing pair define a direct-cycle "
        f"source at `epsilon={arguments.epsilon:.12g}`. All five period balls are "
        f"stored as full Arb intervals; their maximum radius is "
        f"`{maximum_radius:.12g}`. No observed Standard Model datum enters.\n\n"
        "This packet closes the reusable far-cut initializer only. Main transport, "
        "the matching endpoint tail, and the full-row replay remain explicit next steps.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(output)}")
    print(f"wrote {relative(note)}")
    print(
        json.dumps(
            {
                "index": arguments.index,
                "epsilon": arguments.epsilon,
                "line_chart": system.line_chart,
                "maximum_period_radius_upper": maximum_radius,
                "minimum_root_ball_separation_lower": minimum_root_separation,
            },
            indent=2,
        )
    )
    return packet


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("--index", type=int, required=True)
    value.add_argument("--epsilon", type=float, default=1.0e-3)
    value.add_argument("--dps", type=int, default=100)
    value.add_argument("--cut-segments", type=int, default=40)
    value.add_argument("--cut-tolerance", type=float, default=1.0e-50)
    value.add_argument("--maximum-period-radius", type=float, default=1.0e-35)
    return value


def main() -> int:
    arguments = parser().parse_args()
    if not 1 <= arguments.index <= 90:
        raise ValueError("index must lie in [1,90]")
    if not 0.0 < arguments.epsilon < 0.01:
        raise ValueError("far-cut epsilon must lie in (0,0.01)")
    ctx.dps = arguments.dps
    execute(arguments)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
