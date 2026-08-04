from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79alignmentcontinuousrootmonodromypromotion"
OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
PROMOTED = OUT / "ninety_promoted_selected_alignment_picard_lefschetz_monodromies.packet.json"
FRONTIER = OUT / "U6_frontier_after_A128.packet.json"
TUBE_BATCH = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_continuous_root_tube_batch.packet.json"
)
BRAID_BATCH = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_interval_braid_and_global_relation.packet.json"
)
HOMOLOGY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2picardlefschetzmonodromyexecution"
    / "numerical_monodromy_exploration.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    promoted = load(PROMOTED)
    frontier = load(FRONTIER)
    tubes = load(TUBE_BATCH)
    braids = load(BRAID_BATCH)
    homology = load(HOMOLOGY)["homology_convention"]

    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash")
    for authority in candidate["authority_hashes"]:
        path = ROOT / authority["path"]
        require(path.exists(), f"missing authority {path}")
        require(sha256(path) == authority["sha256"], f"authority hash {path}")

    require(
        tubes["status"] == "ALL_90_SELECTED_ALIGNMENT_CONTINUOUS_ROOT_TUBES_CLOSED",
        "root-tube batch status",
    )
    require(tubes["counts"]["continuous_root_tube_certificates"] == 90, "tube count")
    require(tubes["counts"]["segments_certified"] > 1_000_000, "segment count")
    require(float(tubes["minimums"]["Rouche_relative_margin"]) > 0, "Rouche margin")
    require(float(tubes["minimums"]["pairwise_tube_separation"]) > 0, "tube separation")
    require(braids["counts"]["selected_local_braids_certified"] == 90, "braid count")
    require(braids["counts"]["interval_certified_crossings"] >= 3797, "crossing count")
    require(float(braids["minimums"]["projected_endpoint_pair_difference_lower"]) > 0, "projection gap")
    require(float(braids["minimums"]["crossing_height_lower"]) > 0, "crossing height")

    intersection = sp.Matrix(homology["intersection_matrix"])
    image_blocks: list[sp.Matrix] = []
    require(len(promoted["rows"]) == 90, "promoted row count")
    for row in promoted["rows"]:
        packet_path = ROOT / row["monodromy_packet_path"]
        tube_path = ROOT / row["root_tube_certificate_path"]
        require(sha256(packet_path) == row["monodromy_packet_sha256"], "monodromy hash")
        require(sha256(tube_path) == row["root_tube_certificate_sha256"], "tube hash")
        tube = load(tube_path)
        braid_path = ROOT / row["interval_braid_certificate_path"]
        require(sha256(braid_path) == row["interval_braid_certificate_sha256"], "braid hash")
        braid = load(braid_path)
        require(tube["acceptance"]["promotion_ready"], "tube promotion")
        require(
            tube["certificate"]["segments_certified"]
            == row["certified_path_segments"],
            "tube segment agreement",
        )
        require(float(row["minimum_Rouche_relative_margin"]) > 0, "row margin")
        require(float(row["minimum_pairwise_tube_separation"]) > 0, "row separation")
        matrix = sp.Matrix(row["integral_picard_lefschetz_matrix"])
        delta = matrix - sp.eye(4)
        require(matrix.det() == 1, "PL determinant")
        require(matrix.T * intersection * matrix == intersection, "PL symplectic")
        require(delta.rank() == 1 and delta * delta == sp.zeros(4), "PL rank one")
        permutation = row["endpoint_root_permutation"]
        require(
            sum(value != index for index, value in enumerate(permutation)) == 2,
            "PL transposition",
        )
        require(row["promotion_accepted"], "PL promotion accepted")
        require(all(braid["acceptance"].values()), "braid promotion")
        require(
            sp.Matrix(braid["certificate"]["integral_symplectic_matrix"]) == matrix,
            "braid matrix replay",
        )
        image_blocks.append(delta)

    image_rank = sp.Matrix.hstack(*image_blocks).rank()
    require(image_rank == 4, "vanishing image span")
    aggregate = promoted["aggregate"]
    require(aggregate["promoted_local_matrix_count"] == 90, "aggregate promoted count")
    require(aggregate["vanishing_image_span_rank"] == image_rank, "aggregate image rank")
    require(promoted["strict_scope"]["selected_handle_monodromies_promoted"] == 0, "handle guard")
    require(not promoted["strict_scope"]["selected_global_surface_relation_checked"], "relation guard")
    require(promoted["strict_scope"]["endpoint_integral_H2_basis_columns"] == 0, "basis guard")
    require(promoted["strict_scope"]["endpoint_period_columns"] == 0, "period guard")
    require(frontier["selected_alignment_certified_continuous_root_tubes"] == 90, "frontier tubes")
    require(frontier["selected_alignment_promoted_local_PL_monodromies"] == 90, "frontier PL")
    require(not frontier["integral_period_branch_selected"], "branch guard")
    require(certificate["selected_endpoint_period_columns"] == 0, "certificate period guard")

    print("q79 A128 selected-alignment continuous root monodromy audit: PASS")
    print(
        f"certified: 90 paths, {tubes['counts']['segments_certified']} segments, "
        f"min Rouche margin {tubes['minimums']['Rouche_relative_margin']}"
    )
    print("promoted: 90 integral PL matrices, vanishing-image span rank 4")
    print("open: selected A/B handles, global surface relation, endpoint H2 basis and periods")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
