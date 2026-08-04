from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79alignmenthandlesandglobalsurfacerelation"
OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
FACTORIZATION = OUT / "selected_alignment_global_integral_gauss_manin_factorization.packet.json"
FRONTIER = OUT / "U6_frontier_after_A129.packet.json"
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
    factorization = load(FACTORIZATION)
    frontier = load(FRONTIER)
    homology = load(HOMOLOGY)["homology_convention"]
    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash")
    for authority in candidate["authority_hashes"]:
        path = ROOT / authority["path"]
        require(path.exists(), f"missing authority {path}")
        require(sha256(path) == authority["sha256"], f"authority hash {path}")

    intersection = sp.Matrix(homology["intersection_matrix"])
    identity = sp.eye(4)
    product = identity
    vectors: list[list[int]] = []
    require(len(factorization["factors"]) == 90, "factor count")
    for expected_index, row in enumerate(factorization["factors"], 1):
        require(row["distinguished_index"] == expected_index, "factor order")
        matrix = sp.Matrix(row["positive_picard_lefschetz_matrix"])
        vector = sp.Matrix(row["positive_vanishing_cycle_up_to_sign"])
        delta = matrix - identity
        require(matrix.det() == 1, "factor determinant")
        require(matrix.T * intersection * matrix == intersection, "factor symplectic")
        require(delta.rank() == 1 and delta * delta == sp.zeros(4), "factor PL")
        require(matrix == identity + vector * vector.T * intersection, "positive PL replay")
        product = matrix * product
        vectors.append([int(value) for value in vector])
    require(sp.Matrix(vectors).rank() == 4, "vanishing span")

    handle_a = sp.Matrix(factorization["handle_actions"]["A"])
    handle_b = sp.Matrix(factorization["handle_actions"]["B"])
    for matrix in (handle_a, handle_b):
        require(matrix.det() == 1, "handle determinant")
        require(matrix.T * intersection * matrix == intersection, "handle symplectic")
    boundary = handle_b.inv() * handle_a.inv() * handle_b * handle_a
    require(product == boundary, "global surface relation")
    require(
        product
        == sp.Matrix(
            factorization["surface_relation"]["ordered_distinguished_action_product"]
        ),
        "stored relation product",
    )
    for row in factorization["handle_promotions"]:
        require(row["promotion_accepted"], "handle promotion")
        tube_path = ROOT / row["root_tube_certificate_path"]
        braid_path = ROOT / row["interval_braid_certificate_path"]
        require(sha256(tube_path) == row["root_tube_certificate_sha256"], "handle tube hash")
        require(sha256(braid_path) == row["interval_braid_certificate_sha256"], "handle braid hash")
        tube = load(tube_path)
        braid = load(braid_path)
        require(float(tube["certificate"]["minimum_Rouche_relative_margin"]) > 0, "handle Rouche")
        require(float(tube["certificate"]["minimum_pairwise_tube_separation"]) > 0, "handle separation")
        require(all(braid["acceptance"].values()), "handle braid certificate")

    require(factorization["exact_checks"]["global_integral_H1_representation_closed"], "H1 closure")
    require(frontier["selected_alignment_torus_handle_monodromies_promoted"] == 2, "frontier handles")
    require(frontier["selected_alignment_global_integral_H1_surface_relation_closed"], "frontier relation")
    require(frontier["selected_alignment_integral_H2_basis_columns"] == 0, "basis guard")
    require(frontier["selected_alignment_period_columns"] == 0, "period guard")
    require(not certificate["integral_branch_selected"], "branch guard")

    print("q79 A129 selected-alignment handle/global relation audit: PASS")
    print("promoted: 90 positive local PL factors plus selected A/B handles")
    print("closed exactly: M90...M1 = B^-1 A^-1 B A")
    print("open: endpoint integral H2 presentation and selected period execution")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
