from __future__ import annotations

import argparse
import json
import math

import certify_q79_selected_alignment_E32_thimble_polygonal_main_interval as polygonal


def parse_grid(value: str) -> list[float]:
    return [float(item) for item in value.split(",") if item.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--distinguished-index", type=int, required=True)
    parser.add_argument("--epsilon", type=float, default=1.0e-5)
    parser.add_argument(
        "--detour-fractions",
        default="0.2,0.25,0.3,0.32,0.35,0.385,0.4,0.45,0.5,0.55,0.6",
    )
    parser.add_argument(
        "--detour-offsets",
        default="-0.12,-0.1,-0.08,-0.06,-0.04,-0.03,-0.02,-0.01,0,0.01,0.02,0.03,0.04,0.06,0.08,0.1,0.12",
    )
    parser.add_argument(
        "--return-fractions", default="0.65,0.7,0.74,0.78,0.82,0.86"
    )
    parser.add_argument("--limit", type=int, default=20)
    arguments = parser.parse_args()

    source = polygonal.load(
        polygonal.pilot.candidate_path(arguments.distinguished_index)
    )
    critical = polygonal.handle.complex_value(source["critical_center"])
    dual = polygonal.load(polygonal.DUAL)
    z_wall = (
        polygonal.load(polygonal.Z_WALL)
        if source["line_chart"] == "z"
        else None
    )
    rows = []
    rejected = 0
    for fraction in parse_grid(arguments.detour_fractions):
        for offset in parse_grid(arguments.detour_offsets):
            for return_fraction in parse_grid(arguments.return_fractions):
                if not 0 < fraction < return_fraction < 1:
                    continue
                path, design = polygonal.build_detour(
                    critical,
                    epsilon=arguments.epsilon,
                    detour_fraction=fraction,
                    detour_offset=offset,
                    return_fraction=return_fraction,
                )
                try:
                    geometry = polygonal.certify_detour(
                        path,
                        dual,
                        source["root_id"],
                        line_chart=source["line_chart"],
                        z_wall=z_wall,
                    )
                except (AssertionError, ArithmeticError, ZeroDivisionError):
                    rejected += 1
                    continue
                clearances = [
                    geometry["other_critical_ball_clearance_lower"],
                    geometry[
                        f"selected_{source['line_chart']}_chart_zero_clearance_lower"
                    ],
                    geometry["elliptic_infinity_clearance_lower"],
                ]
                rows.append(
                    {
                        "detour_fraction": fraction,
                        "detour_offset": offset,
                        "return_fraction": return_fraction,
                        "minimum_clearance_lower": min(clearances),
                        "other_critical_clearance_lower": clearances[0],
                        "chart_zero_clearance_lower": clearances[1],
                        "elliptic_infinity_clearance_lower": clearances[2],
                        "path_length": sum(
                            abs(right - left)
                            for left, right in zip(path[:-1], path[1:])
                        ),
                        "maximum_winding_residual": geometry[
                            "maximum_integer_winding_residual"
                        ],
                        "path": design["points_in_base_to_node_order"],
                    }
                )
    rows.sort(
        key=lambda row: (
            -row["minimum_clearance_lower"],
            row["path_length"],
            abs(row["detour_offset"]),
        )
    )
    result = {
        "distinguished_index": arguments.distinguished_index,
        "root_id": source["root_id"],
        "line_chart": source["line_chart"],
        "tested": len(rows) + rejected,
        "accepted_null_homotopic": len(rows),
        "rejected": rejected,
        "ranked_routes": rows[: arguments.limit],
    }
    print(json.dumps(result, indent=2))
    if not rows or not math.isfinite(rows[0]["minimum_clearance_lower"]):
        raise ArithmeticError("no certified null-homotopic detour was found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
