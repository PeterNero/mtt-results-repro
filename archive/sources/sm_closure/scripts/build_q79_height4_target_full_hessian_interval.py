from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

import certify_q79_height4_target_main_hessian_interval as main_hessian
import certify_q79_height4_target_tail_hessian_interval as tail_hessian
import certify_q79_height4_tight_target_full_residue_interval as tight


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = "A382"


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
    }


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def matrix(packet: dict, key: str) -> tuple[np.ndarray, np.ndarray]:
    centers = np.empty((8, 8), dtype=np.complex128)
    radii = np.empty((8, 8), dtype=np.float64)
    for row in range(8):
        for column in range(8):
            entry = packet[key][row][column]
            centers[row, column] = complex_value(entry["interval_center"])
            radii[row, column] = float(entry["component_radius_upper"])
    return centers, radii


def paths(index: int) -> dict[str, Path]:
    return {
        "main": main_hessian.target_paths(index)["output"],
        "tail": tail_hessian.output_paths(index)["output"],
        "canonical_full": tight.canonical_paths(index)["full"],
        "output": main_hessian.OUTPUT_DIRECTORY / f"d{index:03d}.fullH.interval.json",
        "note": ROOT
        / "proof_corpus"
        / f"MTT_q79HeightFourD{index:03d}FullHessianInterval_A382_v1.md",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=int, required=True)
    arguments = parser.parse_args()
    if not 1 <= arguments.index <= 90:
        raise ValueError("index must lie in [1,90]")
    selected = paths(arguments.index)
    for name in ("main", "tail", "canonical_full"):
        if not selected[name].exists():
            raise FileNotFoundError(f"missing {name} input for d{arguments.index:03d}")
    main_packet = load(selected["main"])
    tail_packet = load(selected["tail"])
    canonical = load(selected["canonical_full"])
    if not main_packet["strict_scope"]["target_main_Hessian_interval_closed"]:
        raise AssertionError("A382 requires the A380 main Hessian")
    tail_scope = tail_packet["strict_scope"]
    if not (
        tail_scope.get("target_tail_Hessian_interval_closed", False)
        or tail_scope.get("target_Frobenius_tail_Hessian_interval_closed", False)
    ):
        raise AssertionError("A382 requires an independently certified tail Hessian")
    frobenius_tail = bool(
        tail_scope.get("target_Frobenius_tail_Hessian_interval_closed", False)
    )
    quadrature_tail = bool(
        tail_scope.get(
            "A135_dual_quadrature_tail_Hessian_interval_closed", False
        )
    )
    if frobenius_tail == quadrature_tail:
        raise AssertionError(
            "A382 requires exactly one certified tail-Hessian method"
        )
    tail_method = "log-free Frobenius-Cauchy" if frobenius_tail else (
        "differentiated A135 radial/theta interval quadrature"
    )
    main_target = main_packet["selected_target"]
    tail_target = tail_packet["selected_target"]
    if (
        int(main_target["distinguished_index"]) != arguments.index
        or int(tail_target["distinguished_index"]) != arguments.index
        or main_target["root_id"] != tail_target["root_id"]
        or main_target["line_chart"] != tail_target["line_chart"]
    ):
        raise AssertionError("main and tail Hessian target identities differ")
    orientation = int(main_target["orientation_sign"])
    if orientation not in {-1, 1}:
        raise AssertionError("main thimble orientation is not a sign")

    main_rows = main_packet["main_residue_rows"]
    tail_rows = tail_packet["tail_residue_rows"]
    main_centers = np.asarray(
        [complex_value(value["interval_center"]) for value in main_rows],
        dtype=np.complex128,
    )
    tail_centers = np.asarray(
        [complex_value(value["interval_center"]) for value in tail_rows],
        dtype=np.complex128,
    )
    main_radii = np.asarray(
        [float(value["component_radius_upper"]) for value in main_rows],
        dtype=np.float64,
    )
    tail_radii = np.asarray(
        [float(value["component_radius_upper"]) for value in tail_rows],
        dtype=np.float64,
    )
    full_centers = main_centers + orientation * tail_centers
    full_radii = main_radii + tail_radii

    canonical_centers = np.asarray(
        [
            complex_value(value["full_interval_center"])
            for value in canonical["residue_rows"]
        ],
        dtype=np.complex128,
    )
    canonical_radii = np.asarray(
        [
            float(value["full_interval_radius_upper"])
            for value in canonical["residue_rows"]
        ],
        dtype=np.float64,
    )
    differences = abs(full_centers - canonical_centers)
    overlap = differences <= full_radii + canonical_radii
    if not bool(np.all(overlap)):
        raise AssertionError("A382 full rows do not overlap the canonical full target")

    main_matrix, main_matrix_radii = matrix(
        main_packet, "complex_main_Hessian_8_by_8"
    )
    tail_matrix, tail_matrix_radii = matrix(
        tail_packet, "complex_tail_Hessian_8_by_8"
    )
    full_matrix = main_matrix + orientation * tail_matrix
    full_matrix_radii = main_matrix_radii + tail_matrix_radii
    coefficient = int(main_target["signed_chain_coefficient"])
    payload = {
        "schema": "MTTQ79HeightFourTargetFullHessianInterval.v1",
        "status": "TARGET_FULL_COMPLEX_8_BY_8_HESSIAN_INTERVAL_SPLICED",
        "artifact": ARTIFACT,
        "selected_target": {
            "distinguished_index": arguments.index,
            "A219_contribution_rank": int(main_target["A219_contribution_rank"]),
            "root_id": main_target["root_id"],
            "line_chart": main_target["line_chart"],
            "orientation_sign": orientation,
            "signed_chain_coefficient": coefficient,
            "full_identity": "Pi_full=Pi_main+orientation*Pi_tail",
            "Hessian_identity": "D Pi_full=D Pi_main+orientation*D Pi_tail",
            "certified_tail_Hessian_method": tail_method,
        },
        "full_residue_rows": [
            {
                "residue_index_zero_based": index,
                "interval_center": pair(full_centers[index]),
                "component_radius_upper": float(full_radii[index]),
                "canonical_center_difference": float(differences[index]),
                "canonical_intervals_overlap": bool(overlap[index]),
            }
            for index in range(8)
        ],
        "complex_full_Hessian_8_by_8": [
            [
                {
                    "row_zero_based": row,
                    "column_zero_based": column,
                    "interval_center": pair(full_matrix[row, column]),
                    "component_radius_upper": float(full_matrix_radii[row, column]),
                    "selected_chain_contribution_center": pair(
                        coefficient * full_matrix[row, column]
                    ),
                    "selected_chain_contribution_radius_upper": float(
                        abs(coefficient) * full_matrix_radii[row, column]
                    ),
                }
                for column in range(8)
            ]
            for row in range(8)
        ],
        "summary": {
            "certified_full_rows": 8,
            "certified_full_Hessian_entries": 64,
            "maximum_full_row_component_radius_upper": float(np.max(full_radii)),
            "maximum_full_Hessian_component_radius_upper": float(
                np.max(full_matrix_radii)
            ),
            "full_Hessian_product_box_frobenius_radius_upper": float(
                np.linalg.norm(full_matrix_radii)
            ),
            "selected_chain_Hessian_product_box_frobenius_radius_upper": float(
                abs(coefficient) * np.linalg.norm(full_matrix_radii)
            ),
            "all_canonical_full_intervals_overlap": bool(np.all(overlap)),
            "maximum_canonical_full_center_difference": float(np.max(differences)),
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "A380_main_Hessian": selected["main"],
                "A381_tail_Hessian": selected["tail"],
                "canonical_full_target_interval": selected["canonical_full"],
                "builder_source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "target_main_Hessian_interval_closed": True,
            "target_tail_Hessian_interval_closed": True,
            "target_Frobenius_tail_Hessian_interval_closed": frobenius_tail,
            "A135_dual_quadrature_tail_Hessian_interval_closed": quadrature_tail,
            "target_full_Hessian_interval_closed": True,
            "selected_chain_coefficient_applied": True,
            "full_76_target_chain_Hessian_interval_closed": False,
            "rank3_handle_Hessian_interval_closed": False,
            "full_residual_interval_Jacobian_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "repeat A380-A382 over the remaining selected thimbles and sum their "
            "preselected signed chain contributions"
        ),
    }
    dump(selected["output"], payload)
    selected["note"].write_text(
        f"# MTT q79 Height-Four d{arguments.index:03d} Full Hessian Interval (A382) v1\n\n"
        "A382 splices the independently certified main-path and tail Hessians "
        "with the preselected thimble orientation. The tail method is "
        f"`{tail_method}`. "
        "The ordinary rows overlap the canonical full interval target.\n\n"
        f"The maximum full-Hessian component radius is "
        f"`{np.max(full_matrix_radii):.12g}`. The selected chain coefficient is "
        f"`{coefficient}` and is recorded without changing target selection.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(selected['output'])}")
    print(f"wrote {relative(selected['note'])}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
