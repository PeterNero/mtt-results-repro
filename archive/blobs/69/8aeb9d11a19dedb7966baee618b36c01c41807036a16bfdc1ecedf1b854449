from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79alignmentintegralh2presentation"
OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"
PRESENTATION = OUT / "selected_alignment_coupled_integral_H2_chain_presentation.packet.json"
EDGE = OUT / "selected_alignment_Leray_edge_basis.packet.json"
BASIS = OUT / "selected_alignment_exact_integral_H2_basis.packet.json"
FRONTIER = OUT / "U6_frontier_after_A130.packet.json"
CENTRAL_LIFTS = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_handle_central_lifts.interval.packet.json"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def diagonal(matrix: sp.Matrix) -> list[int]:
    return [abs(int(matrix[index, index])) for index in range(min(matrix.shape))]


def main() -> int:
    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    presentation = load(PRESENTATION)
    edge = load(EDGE)
    basis = load(BASIS)
    frontier = load(FRONTIER)
    lifts = load(CENTRAL_LIFTS)
    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash")
    for authority in candidate["authority_hashes"]:
        path = ROOT / authority["path"]
        require(path.exists(), f"missing authority {path}")
        require(sha256(path) == authority["sha256"], f"authority hash {path}")

    require(lifts["selected_lifts"] == {"A": 1, "B": -1}, "central lifts")
    require(lifts["strict_scope"]["period_values_used"] == 0, "central-lift period guard")
    for row in lifts["handles"]:
        require(float(row["minimum_leading_coefficient_absolute_lower"]) > 0, "leading coefficient")
        require(
            row["hyperelliptic_central_lift"]
            == (1 if row["leading_coefficient_winding_number"] % 2 == 0 else -1),
            "winding parity",
        )

    vanishing = sp.Matrix(presentation["vanishing_lattice"]["boundary_rows"])
    require(vanishing.shape == (4, 90), "vanishing shape")
    require(vanishing.rank() == 4, "vanishing rank")
    require(diagonal(smith_normal_form(vanishing, domain=sp.ZZ))[:4] == [1, 1, 1, 1], "vanishing SNF")

    chain = presentation["chain_complex"]
    boundary = sp.Matrix(chain["boundary_matrix_rows"])
    relations = sp.Matrix(chain["full_surface_relations_columns"])
    require(boundary.shape == (4, 98), "boundary shape")
    require(relations.shape == (98, 4), "relations shape")
    require(boundary * relations == sp.zeros(4, 4), "relation cycles")
    quotient = presentation["coupled_quotient"]
    coordinates = sp.Matrix(quotient["relation_coordinates_columns"])
    require(coordinates.shape == (94, 4), "relation-coordinate shape")
    require(diagonal(smith_normal_form(coordinates, domain=sp.ZZ))[:4] == [1, 1, 1, 1], "relation SNF")
    require(abs(int(quotient["quotient_completion_determinant"])) == 1, "completion determinant")
    primary = sp.Matrix(quotient["primary_integral_basis_columns"])
    require(primary.shape == (98, 90), "primary shape")
    require(primary.rank() == 90, "primary rank")
    require(boundary * primary == sp.zeros(4, 90), "primary cycles")
    require(quotient["pure_thimble_columns"] == 82, "pure thimble count")
    require(quotient["handle_supported_columns"] == 8, "handle count")
    require(quotient["maximum_absolute_basis_coefficient"] == 3, "basis coefficient bound")

    require(edge["edge_basis"]["rank"] == 2, "edge rank")
    require(edge["edge_basis"]["intersection_matrix"] == [[0, 1], [1, 0]], "edge pairing")
    require(edge["edge_basis"]["both_classes_primitive"], "edge primitivity")
    require(basis["surface_H2_rank"] == 92, "H2 rank")
    require(len(basis["column_order"]) == 92, "basis column count")
    require(all(basis["exact_checks"].values()), "basis exact checks")
    require(basis["strict_scope"]["period_columns_emitted"] == 0, "period guard")
    require(frontier["selected_alignment_exact_integral_H2_basis_columns"] == 92, "frontier basis")
    require(frontier["selected_alignment_period_columns"] == 0, "frontier periods")
    require(not certificate["integral_branch_selected"], "branch guard")

    print("q79 A130 selected-alignment integral H2 presentation audit: PASS")
    print("central lifts: A=+1, B=-1 from certified q6 windings 6 and -5")
    print("closed: primitive coupled 90-column primary basis plus 2 Leray columns")
    print("open: selected 8x92 period execution and exact integral-branch decision")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
