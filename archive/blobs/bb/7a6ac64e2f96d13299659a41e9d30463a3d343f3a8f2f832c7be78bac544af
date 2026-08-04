from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2integralsurfacecyclepresentation"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}_certificate.json"
PRESENTATION = ROOT / "candidate_data" / SLUG / "integral_surface_cycle_presentation.packet.json"
CONTRACT = ROOT / "candidate_data" / SLUG / "corrected_prym_period_execution_contract.packet.json"
FRONTIER = ROOT / "candidate_data" / SLUG / "U6_frontier_after_A117.packet.json"
FACTORIZATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedcutsystemandglobalrelation"
    / "global_integral_gauss_manin_factorization.packet.json"
)
NOTE = ROOT / "proof_corpus" / "MTT_Selected_q79GenusTwoIntegralSurfaceCyclePresentation_v1.md"
STATUS = (
    "MTT_U6_Q79_INTEGRAL_SURFACE_CYCLE_PRESENTATION_CLOSED_"
    "THIMBLE_PERIOD_EXECUTION_OPEN"
)
NEXT = "MTT_Selected_q79GenusTwoCertifiedThimblePeriodExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def diagonal(matrix: sp.Matrix) -> list[int]:
    return [int(matrix[index, index]) for index in range(min(matrix.shape))]


def main() -> int:
    subprocess.run(
        [
            sys.executable,
            str(
                ROOT
                / "scripts"
                / "build_selected_q79genus2integralsurfacecyclepresentation.py"
            ),
        ],
        cwd=ROOT,
        check=True,
    )

    candidate = load(CANDIDATE)
    certificate = load(CERTIFICATE)
    presentation = load(PRESENTATION)
    contract = load(CONTRACT)
    frontier = load(FRONTIER)
    factorization = load(FACTORIZATION)

    require(candidate["status"] == certificate["status"] == STATUS, "status")
    require(candidate["next_required_artifact"] == NEXT, "candidate next")
    require(certificate["next_required_artifact"] == NEXT, "certificate next")
    require(certificate["candidate_sha256"] == sha256(CANDIDATE), "candidate hash")
    require(all(candidate["checks"].values()), "candidate check")
    require(candidate["supersession"]["rank_count_retained"], "rank retention")
    require(candidate["supersession"]["primitive_86_plus_4_direct_sum_retired"], "old direct sum not retired")
    require(certificate["superseded_by_A119_coupled_integral_presentation"], "A119 supersession")

    thimble = presentation["thimble_boundary_lattice"]
    vanishing = sp.Matrix(thimble["matrix_rows"])
    kernel = sp.Matrix(thimble["closed_thimble_kernel_basis_columns"])
    require(vanishing.shape == (4, 90), "vanishing shape")
    require(kernel.shape == (90, 86), "kernel shape")
    require(vanishing * kernel == sp.zeros(4, 86), "kernel boundary")
    require(kernel.rank() == 86, "kernel rank")
    require(
        diagonal(smith_normal_form(vanishing, domain=sp.ZZ))[:4]
        == [1, 1, 1, 1],
        "vanishing Smith diagonal",
    )
    pivot_indices = [
        value - 1
        for value in thimble[
            "lexicographically_first_unimodular_pivot_indices_one_based"
        ]
    ]
    require(int(vanishing[:, pivot_indices].det()) == 1, "pivot determinant")
    nonpivots = [index for index in range(90) if index not in pivot_indices]
    require(kernel[nonpivots, :] == sp.eye(86), "kernel saturation witness")

    handles = presentation["punctured_torus_handle_lattice"]
    fox = sp.Matrix(handles["fox_boundary_matrix_rows_A_then_B"])
    complement = sp.Matrix(handles["handle_quotient_complement_columns"])
    require(fox.shape == (8, 4), "Fox shape")
    require(complement.shape == (8, 4), "handle complement shape")
    require(fox.rank() == 4, "Fox rank")
    require(
        diagonal(smith_normal_form(fox, domain=sp.ZZ))[:4]
        == [1, 1, 1, 1],
        "Fox Smith diagonal",
    )
    require(abs(int(fox.row_join(complement).det())) == 1, "handle completion")

    action_a = sp.Matrix(factorization["handle_actions"]["A"])
    action_b = sp.Matrix(factorization["handle_actions"]["B"])
    rho_a = action_a.inv()
    rho_b = action_b.inv()
    rho_boundary = rho_a * rho_b * rho_a.inv() * rho_b.inv()
    expected_fox = (
        sp.eye(4) - rho_a * rho_b * rho_a.inv()
    ).col_join(rho_a - rho_boundary)
    require(fox == expected_fox, "Fox replay")
    local_product = sp.Matrix(
        factorization["surface_relation"][
            "ordered_distinguished_action_product"
        ]
    )
    require(rho_boundary == local_product.inv(), "boundary action")

    decomposition = presentation["surface_h2_decomposition"]
    require(decomposition["closed_thimble_rank"] == 86, "thimble rank")
    require(decomposition["punctured_torus_handle_rank"] == 4, "handle rank")
    require(decomposition["Leray_edge_rank"] == 2, "edge rank")
    require(decomposition["known_integral_H2_rank"] == 92, "H2 rank")
    require(decomposition["primary_extension_rank"] == 90, "primary rank")

    assembly = contract["period_assembly"]
    require(assembly["primitive_thimble_integrals_shape"] == [8, 90], "T shape")
    require(assembly["primitive_handle_cylinder_integrals_shape"] == [8, 8], "H shape")
    require(assembly["Leray_edge_periods_shape"] == [8, 2], "E shape")
    require(assembly["final_integral_period_table_shape"] == [8, 92], "Pi shape")
    require(contract["closed"]["integral_column_count_and_ownership"], "ownership")
    require(contract["open"]["primitive_thimble_numerical_values"] == 0, "period invented")
    require(not contract["open"]["integral_branch"], "branch invented")
    require(not contract["open"]["gerbe_zero_or_no_go"], "gerbe invented")

    require(frontier["integral_surface_cycle_presentation_closed"], "frontier presentation")
    require(frontier["surface_H2_rank"] == 92, "frontier rank")
    require(frontier["beta_C_period_rows_emitted"] == 0, "beta rows")
    require(not frontier["integral_period_branch_selected"], "frontier branch")
    require(not frontier["gerbe_zero_or_no_go_executed"], "frontier gerbe")
    require(not frontier["U6_strong_CP_closed"], "U6 overclosed")

    for item in candidate["authority_hashes"]:
        path = ROOT / item["path"]
        require(path.exists(), f"missing authority: {path}")
        require(sha256(path) == item["sha256"], f"authority hash: {path}")

    note = NOTE.read_text(encoding="utf-8")
    for phrase in (
        "into 92 closed\nsurface cycles",
        "diag(1,1,1,1)",
        "86 closed thimble classes",
        "4 punctured-torus handle classes",
        "2 Leray edge classes",
        "8x92",
        "Supersession notice",
        "coupled `82+8` basis",
    ):
        require(phrase in note, f"note phrase: {phrase}")

    print("A117 q79 integral surface-cycle presentation audit: PASS")
    print(f"status={STATUS}")
    print("retained: saturated thimble rank and preliminary 86+4+2 rank reconciliation")
    print("superseded: primitive 86+4 direct sum; A119 supplies the coupled integral basis")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
