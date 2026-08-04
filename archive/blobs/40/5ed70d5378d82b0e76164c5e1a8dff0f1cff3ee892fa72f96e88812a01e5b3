from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import subprocess
import sys
from pathlib import Path

import build_q79_height4_target_full_hessian_interval as full_hessian
import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_height4_target_tail_hessian_interval as tail_hessian


ROOT = Path(__file__).resolve().parents[1]
VALIDATED = main_hessian.VALIDATED
HESSIAN = main_hessian.OUTPUT_DIRECTORY
PREFIX = VALIDATED / "n3.certified76.recomposition.json"
A231 = VALIDATED / "n3.chain.frontier.json"
FAST_MAIN = ROOT / "scripts" / "run_q79_height4_stable_fast_target_main_hessian.py"
SOURCE_CUT_MAIN = (
    ROOT / "scripts" / "run_q79_height4_stable_fast_source_derived_cut_main_hessian.py"
)
SOURCE_CUT_ADAPTER = (
    ROOT / "scripts" / "certify_q79_height4_source_derived_far_cut_hessian_interval.py"
)
TAIL = ROOT / "scripts" / "certify_q79_height4_target_tail_hessian_quadrature_interval.py"
MANIFEST = HESSIAN / "precision.manifest.json"
TARGET_CHAIN_FROBENIUS_BUDGET = 0.6
TARGET_COUNT = 76
WALL_INDEX = 65
WALL_EXTRA_WEIGHT = 3
SOURCE_DERIVED_CUT_EPSILONS = {
    30: 1.0e-3,
    62: 1.0e-3,
    82: 1.0e-3,
    87: 1.0e-3,
}
SOURCE_DERIVED_CUT_INDICES = set(SOURCE_DERIVED_CUT_EPSILONS)
SOURCE_DERIVED_TAIL_ORDERS = {
    30: 24,
    62: 24,
    82: 24,
    87: 24,
}
DETOUR_SOURCE_CUT_EPSILONS = {34: 1.0e-10}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f"{path.name}.{os.getpid()}.tmp")
    temporary.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authorities_current(packet: dict) -> bool:
    authority = packet.get("authority", {})
    if not authority:
        return False
    for row in authority.values():
        path_value = row.get("path")
        expected = row.get("sha256")
        if not path_value or not expected:
            return False
        path = ROOT / path_value
        if not path.exists() or sha256(path) != expected:
            return False
    return True


def packet(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        return load(path)
    except (OSError, json.JSONDecodeError):
        return None


def finite_nonnegative(value: object) -> bool:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return False
    return math.isfinite(number) and number >= 0.0


def effective_weight(index: int, coefficient: int) -> int:
    return abs(coefficient) + (WALL_EXTRA_WEIGHT if index == WALL_INDEX else 0)


def full_budget(index: int, coefficient: int) -> float:
    return TARGET_CHAIN_FROBENIUS_BUDGET / (
        TARGET_COUNT * effective_weight(index, coefficient)
    )


def standard_paths(index: int) -> dict[str, Path]:
    selected = full_hessian.paths(index)
    return {
        "route": Path("standard"),
        "main": selected["main"],
        "tail": selected["tail"],
        "full": selected["output"],
    }


def detour_paths(index: int) -> dict[str, Path]:
    return {
        "route": Path("detour"),
        "main": HESSIAN / "detour" / f"d{index:03d}.mainH.json",
        "tail": (
            HESSIAN / "far2" / f"d{index:03d}.tailH.json"
            if index in DETOUR_SOURCE_CUT_EPSILONS
            else tail_hessian.output_paths(index)["output"]
        ),
        "full": HESSIAN / "detour" / f"d{index:03d}.fullH.json",
    }


def source_derived_cut_paths(index: int) -> dict[str, Path]:
    return {
        "route": Path("source_derived_cut"),
        "main": HESSIAN / "far2" / f"d{index:03d}.mainH.json",
        "tail": HESSIAN / "far2" / f"d{index:03d}.tailH.json",
        "full": HESSIAN / "far2" / f"d{index:03d}.fullH.json",
    }


def source_route_component_current(index: int, selected: dict[str, Path]) -> bool:
    expected_epsilon = SOURCE_DERIVED_CUT_EPSILONS[index]
    for part, quality in (
        ("main", main_certificate_quality),
        ("tail", tail_certificate_quality),
    ):
        value = packet(selected[part])
        if value is None or not quality(selected)[0]:
            continue
        recorded = value.get("selected_target", {}).get("endpoint_cutoff_epsilon")
        if recorded is not None and float(recorded) == expected_epsilon:
            return True
    return False


def main_certificate_quality(selected: dict[str, Path]) -> tuple[bool, float]:
    value = packet(selected["main"])
    if value is None:
        return False, math.inf
    radius = value.get("summary", {}).get(
        "main_Hessian_product_box_frobenius_radius_upper", math.inf
    )
    valid = bool(
        value.get("schema") == "MTTQ79HeightFourTargetMainHessianInterval.v1"
        and value.get("strict_scope", {}).get(
            "target_main_Hessian_interval_closed", False
        )
        is True
        and authorities_current(value)
        and finite_nonnegative(radius)
    )
    return valid, float(radius)


def main_quality(selected: dict[str, Path], budget: float) -> tuple[bool, float]:
    certified, radius = main_certificate_quality(selected)
    return certified and radius <= budget / 2.0, radius


def tail_certificate_quality(selected: dict[str, Path]) -> tuple[bool, float]:
    value = packet(selected["tail"])
    if value is None:
        return False, math.inf
    radius = value.get("summary", {}).get(
        "tail_Hessian_product_box_frobenius_radius_upper", math.inf
    )
    strict_scope = value.get("strict_scope", {})
    tail_closed = bool(
        strict_scope.get("target_tail_Hessian_interval_closed", False)
        or strict_scope.get("target_Frobenius_tail_Hessian_interval_closed", False)
    )
    valid = bool(
        value.get("schema")
        in {
            "MTTQ79HeightFourTargetTailHessianInterval.v1",
            "MTTQ79HeightFourTargetTailHessianQuadratureInterval.v1",
        }
        and tail_closed
        and authorities_current(value)
        and finite_nonnegative(radius)
    )
    return valid, float(radius)


def tail_quality(selected: dict[str, Path], budget: float) -> tuple[bool, float]:
    certified, radius = tail_certificate_quality(selected)
    return certified and radius <= budget / 2.0, radius


def full_quality(selected: dict[str, Path], budget: float) -> tuple[bool, float]:
    value = packet(selected["full"])
    if (
        value is None
        or not selected["main"].exists()
        or not selected["tail"].exists()
    ):
        return False, math.inf
    radius = value.get("summary", {}).get(
        "full_Hessian_product_box_frobenius_radius_upper", math.inf
    )
    authority = value.get("authority", {})
    valid = bool(
        value.get("schema") == "MTTQ79HeightFourTargetFullHessianInterval.v1"
        and value.get("strict_scope", {}).get(
            "target_full_Hessian_interval_closed", False
        )
        is True
        and authorities_current(value)
        and authority.get("A380_main_Hessian", {}).get("sha256")
        == sha256(selected["main"])
        and authority.get("A381_tail_Hessian", {}).get("sha256")
        == sha256(selected["tail"])
        and finite_nonnegative(radius)
        and float(radius) <= budget
    )
    return valid, float(radius)


def selected_route(index: int, budget: float) -> dict[str, Path]:
    routes = [standard_paths(index), detour_paths(index)]
    if index in SOURCE_DERIVED_CUT_INDICES:
        routes.append(source_derived_cut_paths(index))
    completed = [
        (full_quality(route, budget)[1], route)
        for route in routes
        if full_quality(route, budget)[0]
    ]
    if completed:
        return min(completed, key=lambda row: row[0])[1]
    if detour_paths(index)["main"].exists():
        return detour_paths(index)
    if index in SOURCE_DERIVED_CUT_INDICES:
        source_route = source_derived_cut_paths(index)
        if source_route_component_current(index, source_route):
            return source_route
    return standard_paths(index)


def inventory() -> tuple[list[dict], dict[int, int]]:
    prefix = load(PREFIX)
    rows = prefix["certified_targets_in_A219_priority_order"]
    if len(rows) != TARGET_COUNT:
        raise AssertionError("A373 target inventory changed")
    a231 = load(A231)
    coefficients = {
        int(row["distinguished_index"]): int(row["raw_signed_coefficient"])
        for row in a231["exact_floating_decomposition"]["thimble_rows"]
    }
    if len(coefficients) != TARGET_COUNT:
        raise AssertionError("A231 coefficient inventory changed")
    return rows, coefficients


def write_manifest(rows: list[dict], coefficients: dict[int, int], arguments) -> dict:
    targets = []
    for row in rows:
        index = int(row["distinguished_index"])
        coefficient = coefficients[index]
        budget = full_budget(index, coefficient)
        selected = selected_route(index, budget)
        main_certified, _ = main_certificate_quality(selected)
        tail_certified, _ = tail_certificate_quality(selected)
        main_valid, main_radius = main_quality(selected, budget)
        tail_valid, tail_radius = tail_quality(selected, budget)
        full_valid, full_radius = full_quality(selected, budget)
        targets.append(
            {
                "A219_profile_priority_rank": int(row["A219_profile_priority_rank"]),
                "distinguished_index": index,
                "signed_chain_coefficient": coefficient,
                "effective_absolute_weight_including_wall": effective_weight(
                    index, coefficient
                ),
                "selected_route": str(selected["route"]),
                "full_Frobenius_radius_budget": budget,
                "main_certificate_current": main_certified,
                "tail_certificate_current": tail_certified,
                "main_half_budget_pass": main_valid,
                "tail_half_budget_pass": tail_valid,
                "full_budget_pass": full_valid,
                "main_Frobenius_radius": main_radius,
                "tail_Frobenius_radius": tail_radius,
                "full_Frobenius_radius": full_radius,
                "main_path": relative(selected["main"]),
                "tail_path": relative(selected["tail"]),
                "full_path": relative(selected["full"]),
                "main_sha256": (
                    sha256(selected["main"]) if selected["main"].exists() else None
                ),
                "tail_sha256": (
                    sha256(selected["tail"]) if selected["tail"].exists() else None
                ),
                "full_sha256": (
                    sha256(selected["full"]) if selected["full"].exists() else None
                ),
            }
        )
    counts = {
        "main_certificates_current": sum(
            row["main_certificate_current"] for row in targets
        ),
        "tail_certificates_current": sum(
            row["tail_certificate_current"] for row in targets
        ),
        "main_half_budget": sum(row["main_half_budget_pass"] for row in targets),
        "tail_half_budget": sum(row["tail_half_budget_pass"] for row in targets),
        "full_budget": sum(row["full_budget_pass"] for row in targets),
    }
    value = {
        "schema": "MTTQ79HeightFourPrecisionHessianQueueManifest.v1",
        "status": (
            "ALL_76_COEFFICIENT_WEIGHTED_HESSIAN_BUDGETS_CLOSED"
            if counts["full_budget"] == TARGET_COUNT
            else "PRECISION_HESSIAN_QUEUE_IN_PROGRESS"
        ),
        "budget": {
            "total_target_chain_and_wall_Frobenius_budget": TARGET_CHAIN_FROBENIUS_BUDGET,
            "allocation": (
                "equal contribution budget per target, divided by the exact absolute "
                "chain coefficient and by the extra d065 wall weight"
            ),
            "component_split_rule": (
                "main/tail half budgets are sufficient diagnostics only; the certified "
                "spliced full product-box Frobenius radius is the necessary acceptance gate"
            ),
            "target_count": TARGET_COUNT,
            "wall_index": WALL_INDEX,
            "wall_extra_weight": WALL_EXTRA_WEIGHT,
        },
        "configuration": {
            "main_order": arguments.main_order,
            "tail_order": arguments.tail_order,
            "dps": arguments.dps,
            "maximum_step": arguments.maximum_step,
            "maximum_lift_correction": arguments.maximum_lift_correction,
            "maximum_output_increment": arguments.maximum_output_increment,
            "maximum_output_radius": arguments.maximum_output_radius,
            "tail_outer_segments": arguments.tail_outer_segments,
            "tail_theta_segments": arguments.tail_theta_segments,
            "tail_node_width": arguments.tail_node_width,
            "tail_series_terms": arguments.tail_series_terms,
        },
        "counts": counts,
        "remaining_full_budget_count": TARGET_COUNT - counts["full_budget"],
        "targets": targets,
        "strict_scope": {
            "observed_SM_values_used": False,
            "exact_A231_integer_coefficients_used": True,
            "d065_extra_PL_wall_weight_included": True,
            "all_76_component_certificates_current": (
                counts["main_certificates_current"] == TARGET_COUNT
                and counts["tail_certificates_current"] == TARGET_COUNT
            ),
            "main_tail_half_split_is_diagnostic_not_required": True,
            "all_76_main_half_budgets_closed": counts["main_half_budget"] == TARGET_COUNT,
            "all_76_tail_half_budgets_closed": counts["tail_half_budget"] == TARGET_COUNT,
            "all_76_full_Hessian_budgets_closed": counts["full_budget"] == TARGET_COUNT,
            "A384_point_Jacobian_nonsingularity_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "full_SM_closure_proved": False,
        },
        "authority": {
            "A373_inventory": {"path": relative(PREFIX), "sha256": sha256(PREFIX)},
            "A231_coefficients": {"path": relative(A231), "sha256": sha256(A231)},
            "fast_main_runner": {"path": relative(FAST_MAIN), "sha256": sha256(FAST_MAIN)},
            "source_cut_main_runner": {
                "path": relative(SOURCE_CUT_MAIN),
                "sha256": sha256(SOURCE_CUT_MAIN),
            },
            "source_cut_adapter": {
                "path": relative(SOURCE_CUT_ADAPTER),
                "sha256": sha256(SOURCE_CUT_ADAPTER),
            },
            "tail_builder": {"path": relative(TAIL), "sha256": sha256(TAIL)},
            "full_builder": {
                "path": relative(Path(full_hessian.__file__).resolve()),
                "sha256": sha256(Path(full_hessian.__file__).resolve()),
            },
            "queue_source": {
                "path": relative(Path(__file__).resolve()),
                "sha256": sha256(Path(__file__).resolve()),
            },
        },
    }
    dump(MANIFEST, value)
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-rank", type=int, default=1)
    parser.add_argument("--end-rank", type=int, default=76)
    parser.add_argument("--dps", type=int, default=100)
    parser.add_argument("--main-order", type=int, default=48)
    parser.add_argument("--tail-order", type=int, default=48)
    parser.add_argument("--maximum-step", type=float, default=0.02)
    parser.add_argument("--minimum-step", type=float, default=1.0e-12)
    parser.add_argument("--maximum-steps", type=int, default=50000)
    parser.add_argument("--maximum-lift-correction", type=float, default=1.0e-7)
    parser.add_argument("--maximum-output-increment", type=float, default=1.0e-5)
    parser.add_argument("--maximum-output-radius", type=float, default=0.005)
    parser.add_argument("--tail-outer-segments", type=int, default=256)
    parser.add_argument("--tail-theta-segments", type=int, default=64)
    parser.add_argument("--tail-node-width", type=float, default=1.0e-12)
    parser.add_argument("--tail-series-terms", type=int, default=14)
    parser.add_argument("--main-only", action="store_true")
    parser.add_argument("--tail-only", action="store_true")
    parser.add_argument("--full-only", action="store_true")
    parser.add_argument("--manifest-only", action="store_true")
    arguments = parser.parse_args()
    if not 1 <= arguments.start_rank <= arguments.end_rank <= TARGET_COUNT:
        raise ValueError("require 1 <= start rank <= end rank <= 76")
    selected_modes = sum(
        int(value)
        for value in (arguments.main_only, arguments.tail_only, arguments.full_only)
    )
    if selected_modes > 1:
        raise ValueError("main-only, tail-only, and full-only are mutually exclusive")

    rows, coefficients = inventory()
    write_manifest(rows, coefficients, arguments)
    if arguments.manifest_only:
        print(f"wrote {relative(MANIFEST)}")
        return 0

    selected_rows = [
        row
        for row in rows
        if arguments.start_rank
        <= int(row["A219_profile_priority_rank"])
        <= arguments.end_rank
    ]
    for row in selected_rows:
        rank = int(row["A219_profile_priority_rank"])
        index = int(row["distinguished_index"])
        coefficient = coefficients[index]
        budget = full_budget(index, coefficient)
        selected = selected_route(index, budget)
        full_valid, full_radius = full_quality(selected, budget)
        if full_valid:
            print(
                f"precision rank={rank}/76 d{index:03d} full=True "
                f"radius={full_radius:.6e} budget={budget:.6e}",
                flush=True,
            )
            continue
        if str(selected["route"]) == "detour":
            print(
                f"precision rank={rank}/76 d{index:03d} detour "
                f"full=False radius={full_radius:.6e} budget={budget:.6e}",
                flush=True,
            )
            continue

        main_certified, _ = main_certificate_quality(selected)
        tail_certified, _ = tail_certificate_quality(selected)
        if (
            main_certified
            and tail_certified
            and not arguments.main_only
            and not arguments.tail_only
        ):
            print(
                f"precision rank={rank}/76 d{index:03d} asymmetric splice starting",
                flush=True,
            )
            if str(selected["route"]) == "source_derived_cut":
                full_command = [
                    sys.executable,
                    str(SOURCE_CUT_ADAPTER),
                    "--index", str(index),
                    "--phase", "full",
                    "--epsilon", str(SOURCE_DERIVED_CUT_EPSILONS[index]),
                ]
            else:
                full_command = [
                    sys.executable,
                    str(Path(full_hessian.__file__).resolve()),
                    "--index", str(index),
                ]
            subprocess.run(full_command, cwd=ROOT, check=True)
            full_valid, full_radius = full_quality(selected, budget)
            print(
                f"precision d{index:03d} asymmetric full={full_valid} "
                f"radius={full_radius:.6e} budget={budget:.6e}",
                flush=True,
            )
            write_manifest(rows, coefficients, arguments)
            if full_valid:
                continue

        main_valid, _main_radius = main_quality(selected, budget)
        if not arguments.tail_only and not arguments.full_only and not main_valid:
            tail_certified, current_tail_radius = tail_certificate_quality(selected)
            component_budget = (
                budget - current_tail_radius
                if tail_certified and current_tail_radius < budget
                else budget / 2.0
            )
            maximum_radius = min(arguments.maximum_output_radius, component_budget)
            increment = min(arguments.maximum_output_increment, component_budget / 100.0)
            print(
                f"precision rank={rank}/76 d{index:03d} main starting "
                f"remaining-after-tail-budget={component_budget:.6e}",
                flush=True,
            )
            source_route = str(selected["route"]) == "source_derived_cut"
            main_command = [
                sys.executable,
                str(SOURCE_CUT_MAIN if source_route else FAST_MAIN),
                "--index",
                str(index),
            ]
            if source_route:
                main_command.extend(
                    ["--epsilon", str(SOURCE_DERIVED_CUT_EPSILONS[index])]
                )
            main_command.extend(
                [
                    "--dps", str(arguments.dps),
                    "--order", str(arguments.main_order),
                    "--maximum-step", str(arguments.maximum_step),
                    "--minimum-step", str(arguments.minimum_step),
                    "--maximum-steps", str(arguments.maximum_steps),
                    "--maximum-lift-correction", str(arguments.maximum_lift_correction),
                    "--maximum-output-increment", str(increment),
                    "--maximum-output-radius", str(maximum_radius),
                ]
            )
            result = subprocess.run(
                main_command,
                cwd=ROOT,
                check=False,
            )
            if result.returncode != 0:
                print(f"precision d{index:03d} main execution failed", flush=True)
            write_manifest(rows, coefficients, arguments)
        if arguments.main_only:
            continue

        tail_valid, _tail_radius = tail_quality(selected, budget)
        if not arguments.full_only and not tail_valid:
            print(
                f"precision rank={rank}/76 d{index:03d} tail starting "
                f"budget={budget / 2.0:.6e}",
                flush=True,
            )
            if str(selected["route"]) == "source_derived_cut":
                tail_command = [
                    sys.executable,
                    str(SOURCE_CUT_ADAPTER),
                    "--index", str(index),
                    "--phase", "tail-hessian",
                    "--epsilon", str(SOURCE_DERIVED_CUT_EPSILONS[index]),
                    "--dps", str(arguments.dps),
                    "--tail-order", str(
                        SOURCE_DERIVED_TAIL_ORDERS.get(index, arguments.tail_order)
                    ),
                    "--tail-seed-segments", str(arguments.tail_outer_segments),
                    "--theta-segments", str(arguments.tail_theta_segments),
                    "--node-width", str(arguments.tail_node_width),
                    "--series-terms", str(arguments.tail_series_terms),
                ]
            else:
                tail_command = [
                    sys.executable,
                    str(TAIL),
                    "--index", str(index),
                    "--dps", str(arguments.dps),
                    "--order", str(arguments.tail_order),
                    "--outer-segments", str(arguments.tail_outer_segments),
                    "--theta-segments", str(arguments.tail_theta_segments),
                    "--node-width", str(arguments.tail_node_width),
                    "--series-terms", str(arguments.tail_series_terms),
                ]
            result = subprocess.run(
                tail_command,
                cwd=ROOT,
                check=False,
            )
            if result.returncode != 0:
                print(f"precision d{index:03d} tail execution failed", flush=True)
            write_manifest(rows, coefficients, arguments)
        if arguments.tail_only:
            continue

        main_certified, _ = main_certificate_quality(selected)
        tail_certified, _ = tail_certificate_quality(selected)
        if main_certified and tail_certified:
            full_valid, _ = full_quality(selected, budget)
            if not full_valid:
                print(f"precision rank={rank}/76 d{index:03d} splice starting", flush=True)
                if str(selected["route"]) == "source_derived_cut":
                    full_command = [
                        sys.executable,
                        str(SOURCE_CUT_ADAPTER),
                        "--index", str(index),
                        "--phase", "full",
                        "--epsilon", str(SOURCE_DERIVED_CUT_EPSILONS[index]),
                    ]
                else:
                    full_command = [
                        sys.executable,
                        str(Path(full_hessian.__file__).resolve()),
                        "--index", str(index),
                    ]
                subprocess.run(
                    full_command,
                    cwd=ROOT,
                    check=True,
                )
                full_valid, radius = full_quality(selected, budget)
                print(
                    f"precision d{index:03d} full={full_valid} "
                    f"radius={radius:.6e} budget={budget:.6e}",
                    flush=True,
                )
                write_manifest(rows, coefficients, arguments)
        else:
            print(
                f"precision d{index:03d} awaits tighter component packet(s)",
                flush=True,
            )

    manifest = write_manifest(rows, coefficients, arguments)
    counts = manifest["counts"]
    print(
        f"precision queue main={counts['main_half_budget']}/76 "
        f"tail={counts['tail_half_budget']}/76 full={counts['full_budget']}/76",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
