from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

import certify_q79_height4_d087_full_residue_main_interval as main_certificate


ROOT = main_certificate.ROOT
DIRECTORY = main_certificate.PROBE_DIRECTORY / "validated_transport"
MAIN = DIRECTORY / "d087.n3.main8.interval.json"
TAIL = DIRECTORY / "d087.n3.tail8.interval.json"
THIMBLE = main_certificate.THIMBLE
OUTPUT = DIRECTORY / "d087.n3.full8.interval.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79HeightFourD087FullResidueInterval_A222_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def main() -> int:
    main_packet = load(MAIN)
    tail_packet = load(TAIL)
    thimble = load(THIMBLE)
    orientation = int(main_packet["orientation"]["selected_sign"])
    if orientation not in {-1, 1}:
        raise AssertionError("A220 orientation is not integral")
    main_rows = main_packet["all_eight_main_residue_rows"]
    tail_rows = tail_packet["all_eight_endpoint_tails"]
    main_centers = np.asarray(
        [complex_value(value) for value in main_rows["interval_centers"]],
        dtype=np.complex128,
    )
    tail_centers = np.asarray(
        [complex_value(value) for value in tail_rows["interval_centers"]],
        dtype=np.complex128,
    )
    floating = np.asarray(
        [complex_value(value) for value in thimble["period_values"]],
        dtype=np.complex128,
    )
    main_radii = np.asarray(
        main_packet["validated_main_transport"][
            "residue_coordinate_radius_uppers"
        ],
        dtype=np.float64,
    )
    tail_radii = np.asarray(
        tail_rows["interval_radius_uppers"], dtype=np.float64
    )
    if not all(len(value) == 8 for value in (main_centers, tail_centers, floating)):
        raise AssertionError("A222 source vectors are not eight-dimensional")
    full_centers = main_centers + orientation * tail_centers
    full_radii = main_radii + tail_radii
    differences = abs(floating - full_centers)
    contained = differences <= full_radii
    if not bool(np.all(contained)):
        raise AssertionError(
            "n3 floating d087 vector left the validated full interval: "
            f"{np.flatnonzero(~contained).tolist()}"
        )
    rows = []
    for index in range(8):
        rows.append(
            {
                "residue_index_zero_based": index,
                "main_center": main_certificate.encoded_complex(
                    main_centers[index]
                ),
                "main_radius_upper": float(main_radii[index]),
                "oriented_tail_center": main_certificate.encoded_complex(
                    orientation * tail_centers[index]
                ),
                "tail_radius_upper": float(tail_radii[index]),
                "full_interval_center": main_certificate.encoded_complex(
                    full_centers[index]
                ),
                "full_interval_radius_upper": float(full_radii[index]),
                "floating_value_diagnostic_only": main_certificate.encoded_complex(
                    floating[index]
                ),
                "floating_to_interval_center_distance": float(
                    differences[index]
                ),
                "floating_value_contained": bool(contained[index]),
                "containment_margin": float(
                    full_radii[index] - differences[index]
                ),
            }
        )
    payload = {
        "schema": "MTTQ79HeightFourD087FullResidueInterval.v1",
        "status": "D087_N3_FULL_EIGHT_ROW_PERIOD_VECTOR_INTERVAL_CERTIFIED",
        "selected_target": {
            "distinguished_index": 87,
            "root_id": "selected_085",
            "line_chart": "y",
            "orientation_sign": orientation,
            "endpoint_cutoff_epsilon": main_packet["selected_target"][
                "endpoint_cutoff_epsilon"
            ],
        },
        "splice_identity": (
            "full residue vector = validated main vector + selected orientation "
            "sign times validated node-to-cutoff tail vector"
        ),
        "residue_rows": rows,
        "summary": {
            "certified_rows": 8,
            "maximum_full_interval_radius_upper": float(np.max(full_radii)),
            "maximum_floating_center_difference": float(np.max(differences)),
            "minimum_floating_containment_margin": float(
                np.min(full_radii - differences)
            ),
            "all_floating_values_contained": bool(np.all(contained)),
        },
        "authority": {
            name: {"path": relative(path), "sha256": sha256(path)}
            for name, path in {
                "A220_main": MAIN,
                "A221_tail": TAIL,
                "n3_d087_floating_cache": THIMBLE,
                "source": Path(__file__).resolve(),
            }.items()
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "target_node_interval_Newton_closed": True,
            "all_eight_main_rows_interval_closed": True,
            "all_eight_tail_rows_interval_closed": True,
            "orientation_splice_closed": True,
            "full_d087_period_vector_interval_closed": True,
            "floating_values_used_as_bounds": False,
            "covariant_zero_proved": False,
        },
        "next_required_artifact": (
            "repeat the target-alignment full-vector interval certificate for "
            "d034, d041, d030, and d062, then recompose the rank-3 chain"
        ),
    }
    dump(OUTPUT, payload)
    NOTE.write_text(
        "# MTT q79 Height-Four d087 Full-Residue Interval (A222) v1\n\n"
        "A220 certifies all eight correlated main rows at the n3 alignment. "
        "A221 certifies all eight desingularized node-to-cutoff tails on the "
        "same branch. Their orientation-synchronized ball sum therefore "
        "encloses the complete d087 PGL(3) residue-period vector.\n\n"
        f"The maximum full-row radius is `{np.max(full_radii):.12g}`. The "
        f"independent n3 floating cache lies inside all eight balls, with "
        f"minimum containment margin `{np.min(full_radii - differences):.12g}`. "
        "The floating cache is a diagnostic only and was not used as an error "
        "bound.\n\n"
        "This closes the dominant A219 thimble d087. The next interval targets "
        "are d034, d041, d030, and d062, followed by exact chain recomposition. "
        "No covariant zero or full SM closure is claimed here.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    print(json.dumps(payload["summary"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
