from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

from q79_selected_alignment_period_transport import (
    Q79SelectedAlignmentGaussManin,
    Q79SelectedAlignmentPeriodRootTransport,
)
from select_q79_selected_alignment_period_atlas import reduction_conditions


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
Y_FIBRATION = DIRECTORY / "selected_alignment_genus2_fibration_seed.interval.packet.json"
Z_FIBRATION = DIRECTORY / "selected_alignment_zchart_genus2_fibration_seed.interval.packet.json"
HANDLE_DIRECTORY = DIRECTORY / "selected_alignment_handle_monodromy"
HOMOLOGY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)
OUTPUT = DIRECTORY / "selected_alignment_handle_period_atlas.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    homology = load(HOMOLOGY)["homology_convention"]
    engines: dict[str, Q79SelectedAlignmentGaussManin] = {}
    for chart, path in (("y", Y_FIBRATION), ("z", Z_FIBRATION)):
        transport = Q79SelectedAlignmentPeriodRootTransport(
            path, homology, omitted=2 + 3j, dps=70
        )
        engines[chart] = Q79SelectedAlignmentGaussManin(
            path,
            transport,
            coordinate="t",
            omitted=2 + 3j,
        )

    rows: list[dict] = []
    for handle in ("A", "B"):
        packet_path = HANDLE_DIRECTORY / f"handle_{handle}.packet.json"
        packet = load(packet_path)
        trajectory_path = ROOT / packet["trajectory"]["path"]
        if sha256(trajectory_path) != packet["trajectory"]["sha256"]:
            raise AssertionError(f"selected handle {handle} trajectory hash")
        with np.load(trajectory_path) as saved:
            path = np.asarray(saved["w"], dtype=np.complex128)
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
                "handle": handle,
                "trajectory_nodes": int(len(path)),
                "trajectory_path": str(trajectory_path.relative_to(ROOT)).replace(
                    "\\", "/"
                ),
                "trajectory_sha256": sha256(trajectory_path),
                "selected_line_chart": selected,
                "rejected_to_selected_maximum_condition_ratio": format(
                    ratio, ".17g"
                ),
                "charts": chart_rows,
            }
        )

    payload = {
        "schema": "MTTQ79SelectedAlignmentHandlePeriodAtlas.v1",
        "status": "SELECTED_ALIGNMENT_HANDLE_PERIOD_ATLAS_SELECTED_BY_GEOMETRIC_CONDITION",
        "selection_rule": "For each certified handle trajectory, select y or z by the smaller maximum equilibrated Gauss-Manin reduction condition over every certified trajectory node. Period values are never evaluated.",
        "rows": rows,
        "authority": {
            "y_fibration_sha256": sha256(Y_FIBRATION),
            "z_fibration_sha256": sha256(Z_FIBRATION),
            "homology_convention_sha256": sha256(HOMOLOGY),
            "reduction_condition_source_sha256": sha256(
                ROOT / "scripts" / "select_q79_selected_alignment_period_atlas.py"
            ),
            "selector_source_sha256": sha256(Path(__file__).resolve()),
        },
        "strict_scope": {
            "all_certified_handle_trajectory_nodes_scanned": True,
            "period_values_evaluated_for_selection": False,
            "observed_SM_values_used": False,
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
