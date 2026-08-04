from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79alignmenteightbyninetytwoperiodexecution"
DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
)
PERIOD_DIRECTORY = DIRECTORY / "selected_alignment_thimble_periods"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
PRIMITIVE = PERIOD_DIRECTORY / "selected_alignment_primitive_thimble_period_table.packet.json"
ORIENTATION = PERIOD_DIRECTORY / "selected_alignment_thimble_orientation_synchronization.packet.json"
HANDLES = PERIOD_DIRECTORY / "selected_alignment_primitive_handle_periods.packet.json"
BASIS = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmentintegralh2presentation"
    / "selected_alignment_exact_integral_H2_basis.packet.json"
)
LERAY = PERIOD_DIRECTORY / "selected_alignment_explicit_Leray_edge_periods.packet.json"
CONVERGENCE = PERIOD_DIRECTORY / "selected_alignment_full_integral_basis_convergence.packet.json"
PERIODS = PERIOD_DIRECTORY / "selected_alignment_full_integral_basis_period_table.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def complex_value(value: dict[str, str]) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_table(rows: list[list[dict[str, str]]]) -> np.ndarray:
    return np.asarray(
        [[complex_value(value) for value in row] for row in rows],
        dtype=np.complex128,
    )


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    primitive = load(PRIMITIVE)
    orientation = load(ORIENTATION)
    handles = load(HANDLES)
    basis = load(BASIS)
    leray = load(LERAY)
    convergence = load(CONVERGENCE)
    periods = load(PERIODS)
    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash")
    for authority in candidate["authority_hashes"]:
        path = ROOT / authority["path"]
        require(path.exists(), f"missing authority {path}")
        require(sha256(path) == authority["sha256"], f"authority hash {path}")

    thimbles = complex_table(primitive["period_rows"])
    signs = np.asarray(orientation["column_signs"], dtype=np.int64)
    handle_matrix = complex_table(handles["primitive_handle_period_matrix"])
    primary_basis = np.asarray(
        basis["primary_basis"]["basis_columns"], dtype=np.int64
    )
    emitted = complex_table(periods["period_matrix_rows"])
    require(thimbles.shape == (8, 90), "thimble shape")
    require(signs.shape == (90,), "orientation shape")
    require(handle_matrix.shape == (8, 8), "handle shape")
    require(primary_basis.shape == (98, 90), "basis shape")
    replay = np.hstack(
        [
            np.hstack([thimbles * signs[np.newaxis, :], handle_matrix])
            @ primary_basis,
            np.zeros((8, 2), dtype=np.complex128),
        ]
    )
    require(emitted.shape == (8, 92), "period shape")
    require(np.max(np.abs(replay - emitted)) < 1.0e-13, "period assembly replay")
    require(periods["column_order"] == basis["column_order"], "column order")
    require(leray["period_matrix_exact"] == [[0, 0] for _ in range(8)], "Leray zeros")
    require(np.array_equal(emitted[:, 90:92], np.zeros((8, 2))), "emitted edge zeros")
    require(
        float(
            orientation["checks"][
                "maximum_scaled_holomorphic_linearity_residual"
            ]
        )
        < 1.0e-8,
        "orientation residual",
    )
    require(
        handles["central_lift_result"]["independent_period_continuation_agrees"],
        "handle lift replay",
    )
    require(
        float(
            convergence[
                "maximum_primary_column_scale_normalized_difference_envelope"
            ]
        )
        < 1.0e-8,
        "full convergence envelope",
    )
    require(not certificate["integral_branch_selected"], "branch guard")
    require(not periods["strict_scope"]["integral_period_branch_selected"], "period branch guard")

    print("q79 A131 selected-alignment 8x92 period execution audit: PASS")
    print("closed: 90 thimbles, 8 handles, exact 2-column Leray zero")
    print("closed: floating 8x92 table on the exact A130 integral basis")
    print("open: interval nonzero periods and exact beta-lattice branch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
