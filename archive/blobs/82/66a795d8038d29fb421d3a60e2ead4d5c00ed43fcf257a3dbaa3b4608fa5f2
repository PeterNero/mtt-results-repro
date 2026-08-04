from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
DISCRIMINANT = DIRECTORY / "selected_alignment_dual_discriminant.interval.packet.json"
FAN = DIRECTORY / "selected_alignment_distinguished_radial_fan.interval.packet.json"
OUTPUT = DIRECTORY / "selected_alignment_torus_handle_paths.interval.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def encode(value: complex) -> dict[str, str]:
    return {"real": format(value.real, ".17g"), "imaginary": format(value.imag, ".17g")}


def decode(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def segment_distance(start: complex, end: complex, point: complex) -> float:
    direction = end - start
    parameter = ((point - start).conjugate() * direction).real / abs(direction) ** 2
    parameter = min(1.0, max(0.0, parameter))
    return abs(point - (start + parameter * direction))


def main() -> int:
    discriminant = load(DISCRIMINANT)
    fan = load(FAN)
    critical = [
        (
            decode(point["canonical_uniformizing_lift"]),
            float(point["canonical_uniformizing_lift"]["radius_upper"]),
        )
        for point in discriminant["critical_points_on_E"]["points"]
    ]
    chart_zeros = [
        (
            decode(point["canonical_uniformizing_lift"]),
            float(point["canonical_uniformizing_lift"]["radius_upper"]),
        )
        for point in discriminant["selected_y_line_chart_zeros"]["points"]
    ]
    if len(critical) != 90 or len(chart_zeros) != 3:
        raise AssertionError("selected obstruction inventory changed")

    base = 0.25 + 0.25j
    handles: list[dict] = []
    for name, period in (("A", 1 + 0j), ("B", 1j)):
        endpoint = base + period
        critical_clearance = min(
            segment_distance(base, endpoint, center + horizontal + 1j * vertical)
            - radius
            for center, radius in critical
            for horizontal in range(-2, 4)
            for vertical in range(-2, 4)
        ) - 1e-14
        chart_clearance = min(
            segment_distance(base, endpoint, center + horizontal + 1j * vertical)
            - radius
            for center, radius in chart_zeros
            for horizontal in range(-2, 4)
            for vertical in range(-2, 4)
        ) - 1e-14
        pole_clearance = min(
            segment_distance(base, endpoint, horizontal + 1j * vertical)
            for horizontal in range(-2, 4)
            for vertical in range(-2, 4)
        ) - 1e-14
        if min(critical_clearance, chart_clearance, pole_clearance) <= 0:
            raise AssertionError(
                f"selected handle {name} crosses an obstruction: "
                f"critical={critical_clearance} chart={chart_clearance} pole={pole_clearance}"
            )
        handles.append(
            {
                "name": name,
                "universal_cover_start": encode(base),
                "universal_cover_end": encode(endpoint),
                "period_class": "1" if name == "A" else "i",
                "critical_ball_clearance_lower": format(critical_clearance, ".17g"),
                "selected_y_chart_zero_clearance_lower": format(chart_clearance, ".17g"),
                "elliptic_pole_clearance_lower": format(pole_clearance, ".17g"),
            }
        )

    payload = {
        "schema": "MTTQ79SelectedAlignmentTorusHandlePathsInterval.v1",
        "status": "SELECTED_ALIGNMENT_A_AND_B_TORUS_HANDLE_CARRIERS_CERTIFIED",
        "authority": {
            "selected_discriminant_sha256": sha256(DISCRIMINANT),
            "selected_fan_sha256": sha256(FAN),
        },
        "base": {
            "normalized_torus": "C/(Z+iZ)",
            "point": encode(base),
            "fiber": "(a,b)=(-i,1+i)",
        },
        "handles": handles,
        "minimums": {
            "critical_ball_clearance_lower": format(
                min(float(row["critical_ball_clearance_lower"]) for row in handles), ".17g"
            ),
            "selected_y_chart_zero_clearance_lower": format(
                min(float(row["selected_y_chart_zero_clearance_lower"]) for row in handles), ".17g"
            ),
            "elliptic_pole_clearance_lower": format(
                min(float(row["elliptic_pole_clearance_lower"]) for row in handles), ".17g"
            ),
        },
        "topology": {
            "A_period_class": "1",
            "B_period_class": "i",
            "common_basepoint": True,
            "endpoint_fibers_identified_by_square_torus_periodicity": True,
        },
        "strict_scope": {
            "selected_handle_path_carriers_certified": 2,
            "selected_handle_monodromies_computed": 0,
            "selected_handle_root_tubes_certified": 0,
            "observed_SM_values_used": False,
        },
    }
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUTPUT.relative_to(ROOT)}")
    print(json.dumps(payload["minimums"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
