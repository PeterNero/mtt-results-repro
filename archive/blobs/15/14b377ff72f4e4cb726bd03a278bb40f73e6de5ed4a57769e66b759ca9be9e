from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PERIOD_DIRECTORY = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
)
VALIDATED = PERIOD_DIRECTORY / "covariant_floating_probe" / "validated_transport"
PACKET = VALIDATED / "n3.relative_chain_identity.a400.json"
PRESENTATION = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmentintegralh2presentation"
    / "selected_alignment_coupled_integral_H2_chain_presentation.packet.json"
)
BASIS = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmentintegralh2presentation"
    / "selected_alignment_exact_integral_H2_basis.packet.json"
)
A208 = PERIOD_DIRECTORY / "selected_alignment_height4_survivor_queue_and_E32_priority.packet.json"
A231 = VALIDATED / "n3.chain.frontier.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def matrix_vector(matrix: list[list[int]], vector: list[int]) -> list[int]:
    require(bool(matrix), "empty integer matrix")
    require(all(len(row) == len(vector) for row in matrix), "matrix dimensions changed")
    return [
        sum(int(value) * int(vector[index]) for index, value in enumerate(row))
        for row in matrix
    ]


def main() -> int:
    packet = load(PACKET)
    presentation = load(PRESENTATION)
    basis = load(BASIS)
    a208 = load(A208)
    a231 = load(A231)
    require(
        packet["schema"] == "MTTQ79HeightFourSelectedRelativeChainIdentity.v1",
        "A400 schema changed",
    )
    require(packet["artifact"] == "A400", "A400 artifact changed")
    require(packet["theorem"]["proved"], "A400 theorem is not marked proved")

    candidates = [
        row
        for row in a208["height_four_candidates"]
        if int(row["A132_objective_rank"]) == 3
    ]
    require(len(candidates) == 1, "A208 rank-3 branch count changed")
    candidate = candidates[0]
    ell = [int(value) for value in candidate["effective_coordinates_Z90"]]
    basis_columns = [
        [int(value) for value in row]
        for row in basis["primary_basis"]["basis_columns"]
    ]
    primitive = matrix_vector(basis_columns, ell)
    boundary = [
        [int(value) for value in row]
        for row in presentation["chain_complex"]["boundary_matrix_rows"]
    ]
    boundary_image = matrix_vector(boundary, primitive)
    require(boundary_image == [0, 0, 0, 0], "A400 selected cycle has a boundary")
    selected = packet["selected_branch"]
    require(
        [int(value) for value in selected["effective_integral_coordinates_Z90"]] == ell,
        "A400 effective coordinates changed",
    )
    require(
        [int(value) for value in selected["primitive_chain_coordinates_Z98"]]
        == primitive,
        "A400 primitive coordinates changed",
    )
    require(
        [int(value) for value in selected["A130_boundary_image_Z4"]]
        == boundary_image,
        "A400 boundary image changed",
    )

    expected_manifest = [
        {"distinguished_index": index + 1, "coefficient": int(value)}
        for index, value in enumerate(primitive[:90])
        if int(value) != 0
    ]
    require(
        expected_manifest == candidate["primitive_thimble_chain"],
        "A208 primitive manifest no longer replays A130",
    )
    require(
        [int(value) for value in candidate["primitive_handle_coordinates"]]
        == primitive[90:],
        "A208 handle coordinates no longer replay A130",
    )
    replay_manifest = [
        {
            "distinguished_index": int(row["distinguished_index"]),
            "coefficient": int(row["chain_coefficient"]),
        }
        for row in a231["exact_floating_decomposition"]["thimble_rows"]
    ]
    require(replay_manifest == expected_manifest, "A231 chain replay changed")
    require(
        int(packet["picard_lefschetz_transport"]["integral_wall_weight"])
        == int(a231["exact_floating_decomposition"]["PL_wall_weight"]),
        "A400 PL wall weight changed",
    )

    for label, authority in packet["authority"].items():
        path = ROOT / authority["path"]
        require(path.exists(), f"A400 authority missing: {label}")
        require(sha256(path) == authority["sha256"], f"A400 authority stale: {label}")
    scope = packet["strict_scope"]
    require(scope["rank3_primitive_cycle_closed_exactly"], "A400 cycle closure open")
    require(scope["same_carrier_relative_period_identity_closed"], "A400 identity open")
    require(
        not scope["correlation_preserving_path_execution_closed"],
        "A400 overclaims correlated execution",
    )
    require(
        not scope["existing_independent_endpoint_boxes_may_be_correlated_retroactively"],
        "A400 permits invalid retrospective correlation",
    )
    require(
        not scope["integral_branch_selected_by_a_zero_theorem"],
        "A400 overclaims branch selection",
    )
    require(not scope["covariant_zero_proved"], "A400 overclaims a covariant zero")
    print(
        "PASS: A400 independently verifies the exact closed rank-3 cycle and "
        "keeps joint interval transport open"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
