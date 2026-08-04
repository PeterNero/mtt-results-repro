from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2handleandlerayperiodexecution"
OUTPUT_DIR = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}_certificate.json"
ORIENTATION = OUTPUT_DIR / "oriented_thimble_alignment.packet.json"
PRESENTATION = OUTPUT_DIR / "coupled_integral_H2_chain_presentation.packet.json"
LERAY = OUTPUT_DIR / "explicit_Leray_edge_periods.packet.json"
CONVERGENCE = OUTPUT_DIR / "full_integral_basis_convergence.packet.json"
PERIOD_TABLE = OUTPUT_DIR / "full_integral_basis_period_table.packet.json"
FRONTIER = OUTPUT_DIR / "U6_frontier_after_A119.packet.json"
PRIMITIVE_THIMBLES = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2thimbleperiodexecution"
    / "primitive_thimble_period_candidate_table.packet.json"
)
HANDLE_PRODUCTION = OUTPUT_DIR / "primitive_handle_periods.production.packet.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_q79GenusTwoHandleAndLerayPeriodExecution_v1.md"
)
STATUS = (
    "MTT_U6_Q79_COUPLED_INTEGRAL_H2_BASIS_AND_FLOATING_8X92_PERIOD_"
    "TABLE_CLOSED_INTERVAL_BETA_BRANCH_OPEN"
)
NEXT = "MTT_Selected_q79GenusTwoNormalFunctionBetaAndIntegralBranchExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def parse_complex(value: dict) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_table(values: list[list[dict]]) -> np.ndarray:
    return np.asarray(
        [[parse_complex(value) for value in row] for row in values],
        dtype=np.complex128,
    )


def diagonal(matrix: sp.Matrix) -> list[int]:
    return [abs(int(matrix[index, index])) for index in range(min(matrix.shape))]


def main() -> int:
    subprocess.run(
        [
            sys.executable,
            str(
                ROOT
                / "scripts"
                / "build_selected_q79genus2handleandlerayperiodexecution.py"
            ),
        ],
        cwd=ROOT,
        check=True,
    )

    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    orientation = load(ORIENTATION)
    presentation = load(PRESENTATION)
    leray = load(LERAY)
    convergence = load(CONVERGENCE)
    period_table = load(PERIOD_TABLE)
    frontier = load(FRONTIER)
    primitive_packet = load(PRIMITIVE_THIMBLES)
    handle_packet = load(HANDLE_PRODUCTION)

    require(candidate["status"] == certificate["status"] == STATUS, "status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(certificate["next_required_artifact"] == NEXT, "certificate next")
    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash")
    require(all(candidate["checks"].values()), "candidate checks")

    require(orientation["positive_sign_count"] == 38, "positive signs")
    require(orientation["negative_sign_count"] == 52, "negative signs")
    require(len(orientation["orientation_sign_string"]) == 90, "sign string")
    require(
        float(orientation["maximum_selected_scaled_residual"]) < 2.0e-8,
        "orientation residual",
    )
    oriented = sp.Matrix(orientation["oriented_vanishing_boundary_matrix_rows"])
    require(oriented.shape == (4, 90), "oriented boundary shape")
    require(diagonal(smith_normal_form(oriented, domain=sp.ZZ))[:4] == [1, 1, 1, 1], "oriented boundary Smith form")

    chain = presentation["chain_complex"]
    quotient = presentation["saturated_kernel_and_quotient"]
    boundary = sp.Matrix(chain["boundary_matrix_rows"])
    relations = sp.Matrix(chain["four_full_surface_relations_columns"])
    kernel = sp.Matrix(quotient["kernel_basis_Z_columns"])
    coordinates = sp.Matrix(quotient["relation_coordinates_X_columns"])
    basis = sp.Matrix(quotient["primary_integral_basis_columns"])
    require(boundary.shape == (4, 98), "boundary shape")
    require(relations.shape == (98, 4), "relations shape")
    require(kernel.shape == (98, 94), "kernel shape")
    require(coordinates.shape == (94, 4), "relation coordinate shape")
    require(basis.shape == (98, 90), "primary basis shape")
    require(boundary.rank() == 4, "boundary rank")
    require(boundary * kernel == sp.zeros(4, 94), "kernel boundary")
    require(boundary * relations == sp.zeros(4, 4), "relation boundary")
    require(kernel * coordinates == relations, "relation coordinate replay")
    require(boundary * basis == sp.zeros(4, 90), "basis boundary")
    require(
        presentation["selected_central_lifts"]["handle_only_Fox_smith_diagonal"]
        == [1, 1, 1, 3],
        "handle-only Smith form",
    )
    require(diagonal(smith_normal_form(coordinates, domain=sp.ZZ))[:4] == [1, 1, 1, 1], "full relation Smith form")
    require(abs(quotient["quotient_completion_determinant"]) == 1, "unimodular completion")
    require(quotient["pure_thimble_columns"] == 82, "pure thimble count")
    require(quotient["handle_supported_columns"] == 8, "handle-supported count")
    require(quotient["maximum_absolute_basis_coefficient"] == 10, "basis coefficient bound")

    require(leray["edge_basis"]["intersection_matrix_F_Gamma0"] == [[0, 1], [1, 0]], "Leray U pair")
    require(leray["edge_basis"]["both_classes_primitive"], "Leray primitivity")
    require(leray["edge_basis"]["no_holomorphic_section_assumed"], "section overclaim")
    require(leray["primitive_residue_argument"]["p_g_C"] == 9, "p_g")
    require(leray["primitive_residue_argument"]["A111_exact_residue_rank"] == 8, "residue rank")
    require(leray["period_matrix_exact"] == [[0, 0] for _ in range(8)], "edge periods")

    thimbles = complex_table(primitive_packet["period_rows"])
    handles = complex_table(handle_packet["primitive_handle_period_matrix"])
    periods = complex_table(period_table["period_rows"])
    require(thimbles.shape == (8, 90), "thimble period shape")
    require(handles.shape == (8, 8), "handle period shape")
    require(periods.shape == (8, 92), "full period shape")
    replay = np.hstack([thimbles, handles]) @ np.asarray(basis.tolist(), dtype=np.float64)
    require(np.allclose(periods[:, :90], replay, rtol=0.0, atol=2.0e-13), "primary period assembly")
    require(np.array_equal(periods[:, 90:92], np.zeros((8, 2), dtype=np.complex128)), "exact edge zeros")
    require(float(convergence["maximum_primitive_handle_scale_normalized_difference"]) < 2.0e-8, "handle convergence")
    require(float(convergence["maximum_primary_column_scale_normalized_difference_envelope"]) < 1.0e-7, "full-table convergence envelope")
    require(not convergence["strict_scope"]["interval_enclosure"], "interval overclaim")
    require(not convergence["strict_scope"]["rigorous_truncation_error_bound"], "error-bound overclaim")

    require(frontier["exact_integral_H2_basis_columns"] == 92, "H2 basis count")
    require(frontier["floating_period_columns_executed"] == 92, "period column count")
    require(frontier["interval_period_columns_certified"] == 0, "interval count")
    require(frontier["beta_C_period_rows_emitted"] == 0, "beta overclaim")
    require(not frontier["integral_period_branch_selected"], "branch overclaim")
    require(not frontier["gerbe_zero_or_no_go_executed"], "gerbe overclaim")
    require(not frontier["U6_strong_CP_closed"], "U6 overclaim")

    for item in candidate["authority_hashes"]:
        path = ROOT / item["path"]
        require(path.exists(), f"missing authority: {path}")
        require(sha256(path) == item["sha256"], f"authority hash: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "A_period = +A_braid",
        "B_period = -B_braid",
        "Smith diagonal `(1,1,1,3)`",
        "Smith diagonal `(1,1,1,1)`",
        "82 pure-thimble columns",
        "8 thimble/handle-supported columns",
        "intersection matrix `U`",
        "complete floating `8x92` table",
        "not an interval enclosure",
    ):
        require(phrase in note, f"note phrase: {phrase}")

    print("A119 q79 handle/Leray period execution audit: PASS")
    print(f"status={STATUS}")
    print("closed: exact coupled rank-92 H2 basis and floating 8x92 period table")
    print("open: interval enclosure, beta vector, integral branch, gerbe zero/no-go")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
