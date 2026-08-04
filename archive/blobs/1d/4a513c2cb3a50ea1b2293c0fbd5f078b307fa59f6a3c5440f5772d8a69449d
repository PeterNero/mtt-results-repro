from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import certify_q79_height4_far_cut_target_hessian_interval as far


SELECTED = far.paths(46)
MAIN = SELECTED["main"]
TAIL = SELECTED["tail"]
FULL = SELECTED["full"]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def matrix(packet: dict, key: str) -> tuple[np.ndarray, np.ndarray]:
    rows = packet[key]
    require(len(rows) == 8 and all(len(row) == 8 for row in rows), f"{key} shape")
    centers = np.asarray(
        [[complex_value(entry["interval_center"]) for entry in row] for row in rows],
        dtype=np.complex128,
    )
    radii = np.asarray(
        [[float(entry["component_radius_upper"]) for entry in row] for row in rows],
        dtype=np.float64,
    )
    require(bool(np.all(np.isfinite(centers))), f"{key} nonfinite center")
    require(bool(np.all(np.isfinite(radii))), f"{key} nonfinite radius")
    require(bool(np.all(radii >= 0.0)), f"{key} negative radius")
    return centers, radii


def check_authority(packet: dict, label: str) -> None:
    for name, row in packet["authority"].items():
        path = ROOT / row["path"]
        require(path.exists(), f"{label} authority missing: {name}")
        require(sha256(path) == row["sha256"], f"{label} authority stale: {name}")


def main() -> int:
    main_packet = load(MAIN)
    tail_packet = load(TAIL)
    full_packet = load(FULL)
    require(main_packet["artifact"] == "A380F", "d046 far main artifact changed")
    require(tail_packet["artifact"] == "A381QF", "d046 far tail artifact changed")
    require(full_packet["artifact"] == "A382F", "d046 far full artifact changed")
    require(
        full_packet["schema"] == "MTTQ79HeightFourTargetFullHessianInterval.v1",
        "d046 far full schema changed",
    )
    target = full_packet["selected_target"]
    require(int(target["distinguished_index"]) == 46, "d046 far target changed")
    require(target["line_chart"] == "z", "d046 far chart changed")
    require(
        float(main_packet["selected_target"]["endpoint_cutoff_epsilon"])
        == float(tail_packet["selected_target"]["endpoint_cutoff_epsilon"])
        == 1.0e-3,
        "d046 far cutoff changed",
    )
    orientation = int(target["orientation_sign"])
    coefficient = int(target["signed_chain_coefficient"])
    require(orientation in {-1, 1}, "d046 far orientation is not a sign")

    main_centers, main_radii = matrix(
        main_packet, "complex_main_Hessian_8_by_8"
    )
    tail_centers, tail_radii = matrix(
        tail_packet, "complex_tail_Hessian_8_by_8"
    )
    full_centers, full_radii = matrix(
        full_packet, "complex_full_Hessian_8_by_8"
    )
    require(
        float(np.max(abs(full_centers - (main_centers + orientation * tail_centers))))
        < 1.0e-14,
        "d046 far Hessian splice centers do not replay",
    )
    require(
        bool(np.allclose(full_radii, main_radii + tail_radii, rtol=2.0e-15)),
        "d046 far Hessian splice radii do not replay",
    )
    for row_index, row in enumerate(full_packet["complex_full_Hessian_8_by_8"]):
        for column_index, entry in enumerate(row):
            require(
                abs(
                    complex_value(entry["selected_chain_contribution_center"])
                    - coefficient * full_centers[row_index, column_index]
                )
                < 1.0e-14,
                "d046 selected-chain Hessian center does not replay",
            )
            require(
                math.isclose(
                    float(entry["selected_chain_contribution_radius_upper"]),
                    abs(coefficient) * full_radii[row_index, column_index],
                    rel_tol=2.0e-15,
                ),
                "d046 selected-chain Hessian radius does not replay",
            )

    summary = full_packet["summary"]
    require(int(summary["certified_full_Hessian_entries"]) == 64, "d046 lost entries")
    require(summary["all_canonical_full_intervals_overlap"] is True, "d046 full overlap lost")
    require(
        math.isclose(
            float(summary["full_Hessian_product_box_frobenius_radius_upper"]),
            float(np.linalg.norm(full_radii)),
            rel_tol=2.0e-15,
        ),
        "d046 far full Frobenius radius does not replay",
    )
    source = main_packet["initial_period_source"]
    require(
        source["canonical_display_intervals_overlap_all_five"] is True,
        "d046 far full-precision initializer lost ordinary overlap",
    )
    require(
        float(source["maximum_full_precision_period_radius_upper"]) < 1.0e-35,
        "d046 far initializer is too wide",
    )
    require(
        full_packet["strict_scope"]["target_full_Hessian_interval_closed"] is True,
        "d046 far full Hessian is open",
    )
    require(
        full_packet["strict_scope"]["observed_SM_values_used"] is False,
        "observed values entered d046 far Hessian",
    )
    check_authority(main_packet, "A380F")
    check_authority(tail_packet, "A381QF")
    check_authority(full_packet, "A382F")
    print(
        "PASS: d046 far-cut main/tail/full 8x8 Hessians replay with current "
        f"authorities and chain Frobenius radius "
        f"{summary['selected_chain_Hessian_product_box_frobenius_radius_upper']:.6e}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
