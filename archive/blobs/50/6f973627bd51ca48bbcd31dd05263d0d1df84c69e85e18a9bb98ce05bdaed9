from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from q79_selected_alignment_period_transport import (
    Q79SelectedAlignmentGaussManin,
    Q79SelectedAlignmentPeriodRootTransport,
)


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
Y_FIBRATION = DIRECTORY / "selected_alignment_genus2_fibration_seed.interval.packet.json"
Z_FIBRATION = DIRECTORY / "selected_alignment_zchart_genus2_fibration_seed.interval.packet.json"
FAN = DIRECTORY / "selected_alignment_distinguished_radial_fan.interval.packet.json"
HOMOLOGY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
OUTPUT = DIRECTORY / "selected_alignment_period_atlas.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decode_complex(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def reduction_conditions(
    gauss_manin: Q79SelectedAlignmentGaussManin, w_value: complex
) -> tuple[float, float, float, float]:
    a_value, b_value, coefficients, _derivative = gauss_manin.fiber_data(
        w_value
    )
    polynomial_derivative = np.asarray(
        [index * coefficients[index] for index in range(1, 7)],
        dtype=np.complex128,
    )
    columns: list[np.ndarray] = []
    for power in range(6):
        column = np.zeros(11, dtype=np.complex128)
        if power:
            column += power * gauss_manin.shift(coefficients, power - 1)
        column -= 0.5 * gauss_manin.shift(polynomial_derivative, power)
        columns.append(column)
    for power in range(5):
        columns.append(gauss_manin.shift(coefficients, power))
    reduction = np.column_stack(columns)
    raw = float(np.linalg.cond(reduction))
    equilibrated = reduction.copy()
    for _ in range(4):
        row_norms = np.max(np.abs(equilibrated), axis=1)
        if np.any(row_norms == 0):
            return raw, float("inf"), 0.0, 0.0
        equilibrated /= row_norms[:, None]
        column_norms = np.max(np.abs(equilibrated), axis=0)
        if np.any(column_norms == 0):
            return raw, float("inf"), 0.0, 0.0
        equilibrated /= column_norms[None, :]
    line = gauss_manin.alignment @ np.asarray(
        [a_value, b_value, 1 + 0j], dtype=np.complex128
    )
    denominator_index = 1 if gauss_manin.line_chart == "y" else 2
    return (
        raw,
        float(np.linalg.cond(equilibrated)),
        float(abs(coefficients[-1])),
        float(abs(line[denominator_index])),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=257)
    parser.add_argument("--epsilon", type=float, default=3.0e-6)
    return parser.parse_args()


def main() -> int:
    arguments = parse_args()
    if arguments.samples < 33 or not 0 < arguments.epsilon < 0.01:
        raise ValueError("invalid atlas scan resolution")
    fan = load(FAN)
    homology = load(HOMOLOGY)["homology_convention"]
    engines: dict[str, Q79SelectedAlignmentGaussManin] = {}
    for chart, path in (("y", Y_FIBRATION), ("z", Z_FIBRATION)):
        transport = Q79SelectedAlignmentPeriodRootTransport(
            path,
            homology,
            omitted=2 + 3j,
            dps=70,
        )
        engines[chart] = Q79SelectedAlignmentGaussManin(
            path,
            transport,
            coordinate="t",
            omitted=2 + 3j,
        )

    sample_index = np.arange(arguments.samples, dtype=np.float64)
    parameters = (
        0.5
        * (1 - np.cos(np.pi * sample_index / (arguments.samples - 1)))
        * (1 - arguments.epsilon)
    )
    base = 0.25 + 0.25j
    rows: list[dict] = []
    for fan_row in fan["distinguished_positive_meridians"]:
        critical = decode_complex(fan_row["canonical_lift"])
        path = base + parameters * (critical - base)
        chart_rows: dict[str, dict] = {}
        for chart, gauss_manin in engines.items():
            values = [
                reduction_conditions(gauss_manin, complex(w_value))
                for w_value in path
            ]
            chart_rows[chart] = {
                "line_chart": chart,
                "maximum_raw_reduction_condition": format(
                    max(value[0] for value in values), ".17g"
                ),
                "maximum_equilibrated_reduction_condition": format(
                    max(value[1] for value in values), ".17g"
                ),
                "minimum_t6_coefficient_absolute": format(
                    min(value[2] for value in values), ".17g"
                ),
                "minimum_line_chart_denominator_absolute": format(
                    min(value[3] for value in values), ".17g"
                ),
            }
        selected = min(
            ("y", "z"),
            key=lambda chart: float(
                chart_rows[chart][
                    "maximum_equilibrated_reduction_condition"
                ]
            ),
        )
        rejected = "z" if selected == "y" else "y"
        ratio = float(
            chart_rows[rejected][
                "maximum_equilibrated_reduction_condition"
            ]
        ) / max(
            float(
                chart_rows[selected][
                    "maximum_equilibrated_reduction_condition"
                ]
            ),
            np.finfo(float).tiny,
        )
        rows.append(
            {
                "distinguished_index": fan_row["distinguished_index"],
                "root_id": fan_row["root_id"],
                "selected_line_chart": selected,
                "rejected_to_selected_maximum_condition_ratio": format(
                    ratio, ".17g"
                ),
                "charts": chart_rows,
            }
        )

    payload = {
        "schema": "MTTQ79SelectedAlignmentPeriodAtlas.v1",
        "status": "SELECTED_ALIGNMENT_TWO_CHART_PERIOD_ATLAS_SELECTED_BY_GEOMETRIC_CONDITION",
        "selection_rule": "For each distinguished radial path, select y or z by the smaller maximum equilibrated Gauss-Manin reduction condition on the fixed 257-point Chebyshev endpoint-clustered grid. Ties select y. Period values are never evaluated.",
        "sample_grid": {
            "kind": "Chebyshev endpoint-clustered radial parameters",
            "sample_count": arguments.samples,
            "endpoint_cutoff_epsilon": format(arguments.epsilon, ".17g"),
        },
        "counts": {
            "selected_y": sum(
                row["selected_line_chart"] == "y" for row in rows
            ),
            "selected_z": sum(
                row["selected_line_chart"] == "z" for row in rows
            ),
        },
        "rows": rows,
        "authority": {
            "y_fibration_sha256": sha256(Y_FIBRATION),
            "z_fibration_sha256": sha256(Z_FIBRATION),
            "distinguished_fan_sha256": sha256(FAN),
            "homology_convention_sha256": sha256(HOMOLOGY),
            "selector_source_sha256": sha256(Path(__file__).resolve()),
        },
        "strict_scope": {
            "period_values_evaluated_for_selection": False,
            "observed_SM_values_used": False,
            "finite_sample_condition_selection": True,
            "continuous_chart_nonvanishing_certificate": False,
        },
    }
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
