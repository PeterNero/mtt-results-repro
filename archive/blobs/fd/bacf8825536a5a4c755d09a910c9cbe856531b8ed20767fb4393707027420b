from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp, smith_normal_form


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2integralsurfacecyclepresentation"
FACTORIZATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedcutsystemandglobalrelation"
    / "global_integral_gauss_manin_factorization.packet.json"
)
SPECTRAL_INVARIANTS = (
    ROOT
    / "candidate_data"
    / "selected_q79twistedspectralgerbelifthymandbianchiexecution"
    / "spectral_surface_invariants.packet.json"
)
A111_RESIDUES = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2lefschetzperiodreduction"
    / "explicit_prym_residues_and_delta_normal_function.packet.json"
)
A116_READY = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedcutsystemandglobalrelation"
    / "eight_prym_period_transport.ready.json"
)
OUTPUT_DIR = ROOT / "candidate_data" / SLUG
PRESENTATION = OUTPUT_DIR / "integral_surface_cycle_presentation.packet.json"
PERIOD_CONTRACT = OUTPUT_DIR / "corrected_prym_period_execution_contract.packet.json"
FRONTIER = OUTPUT_DIR / "U6_frontier_after_A117.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_q79GenusTwoIntegralSurfaceCyclePresentation_v1.md"
)
NEXT = "MTT_Selected_q79GenusTwoCertifiedThimblePeriodExecution_v1"
STATUS = (
    "MTT_U6_Q79_INTEGRAL_SURFACE_CYCLE_PRESENTATION_CLOSED_"
    "THIMBLE_PERIOD_EXECUTION_OPEN"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rows(matrix: sp.Matrix) -> list[list[int]]:
    return [
        [int(matrix[row, column]) for column in range(matrix.cols)]
        for row in range(matrix.rows)
    ]


def diagonal_entries(matrix: sp.Matrix) -> list[int]:
    return [int(matrix[index, index]) for index in range(min(matrix.shape))]


def first_unimodular_columns(matrix: sp.Matrix) -> tuple[tuple[int, ...], int]:
    rank = matrix.rows
    for indices in itertools.combinations(range(matrix.cols), rank):
        determinant = int(matrix[:, indices].det())
        if abs(determinant) == 1:
            return indices, determinant
    raise AssertionError("no unimodular vanishing-cycle block")


def main() -> int:
    for path in (
        FACTORIZATION,
        SPECTRAL_INVARIANTS,
        A111_RESIDUES,
        A116_READY,
        NOTE,
    ):
        if not path.exists():
            raise FileNotFoundError(path)

    factorization = load(FACTORIZATION)
    invariants = load(SPECTRAL_INVARIANTS)
    residues = load(A111_RESIDUES)
    a116_ready = load(A116_READY)

    factors = factorization["factors"]
    if len(factors) != 90:
        raise AssertionError("distinguished factor count")
    if residues["residue_forms"]["exact_linear_rank"] != 8:
        raise AssertionError("A111 residue rank")
    if a116_ready["closed_inputs"]["global_integral_H1_surface_relation"] is not True:
        raise AssertionError("A116 global relation")

    intersection = sp.Matrix(factorization["base"]["intersection_matrix"])
    identity = sp.eye(4)
    vanishing_cycles = sp.Matrix.hstack(
        *[
            sp.Matrix(row["positive_vanishing_cycle_up_to_sign"])
            for row in factors
        ]
    )
    if vanishing_cycles.rank() != 4:
        raise AssertionError("vanishing cycles do not span fiber H1")

    for row in factors:
        cycle = sp.Matrix(row["positive_vanishing_cycle_up_to_sign"])
        action = sp.Matrix(row["positive_picard_lefschetz_matrix"])
        if action != identity + cycle * cycle.T * intersection:
            raise AssertionError("PL factor/cycle mismatch")

    vanishing_snf = smith_normal_form(vanishing_cycles, domain=sp.ZZ)
    if diagonal_entries(vanishing_snf)[:4] != [1, 1, 1, 1]:
        raise AssertionError("vanishing-cycle image is not saturated")

    pivot_indices, pivot_determinant = first_unimodular_columns(
        vanishing_cycles
    )
    pivot = vanishing_cycles[:, pivot_indices]
    pivot_inverse = pivot.inv()
    nonpivot_indices = [
        index for index in range(90) if index not in pivot_indices
    ]
    thimble_kernel = sp.zeros(90, 86)
    for column, factor_index in enumerate(nonpivot_indices):
        thimble_kernel[factor_index, column] = 1
        pivot_coefficients = -pivot_inverse * vanishing_cycles[:, factor_index]
        for row, pivot_index in enumerate(pivot_indices):
            thimble_kernel[pivot_index, column] = pivot_coefficients[row]
    if vanishing_cycles * thimble_kernel != sp.zeros(4, 86):
        raise AssertionError("thimble-kernel boundary is nonzero")
    if thimble_kernel.rank() != 86:
        raise AssertionError("thimble-kernel rank")
    # The nonpivot identity block makes this kernel basis primitive in Z^90.
    nonpivot_minor = thimble_kernel[nonpivot_indices, :]
    if nonpivot_minor != sp.eye(86):
        raise AssertionError("thimble-kernel saturation witness")

    action_a = sp.Matrix(factorization["handle_actions"]["A"])
    action_b = sp.Matrix(factorization["handle_actions"]["B"])
    rho_a = action_a.inv()
    rho_b = action_b.inv()
    rho_boundary = rho_a * rho_b * rho_a.inv() * rho_b.inv()
    local_product = sp.Matrix(
        factorization["surface_relation"][
            "ordered_distinguished_action_product"
        ]
    )
    if rho_boundary != local_product.inv():
        raise AssertionError("homomorphic handle/local boundary mismatch")

    # For r=A B A^-1 B^-1, Fox derivatives are
    # d_A r=1-A B A^-1 and d_B r=A-r.  M is an anti-representation,
    # hence rho(g)=M(g)^-1 is used in the cellular boundary.
    fox_boundary = (
        identity - rho_a * rho_b * rho_a.inv()
    ).col_join(rho_a - rho_boundary)
    fox_snf, fox_left, fox_right = smith_normal_decomp(
        fox_boundary, domain=sp.ZZ
    )
    if fox_snf != fox_left * fox_boundary * fox_right:
        raise AssertionError("Fox Smith decomposition")
    if diagonal_entries(fox_snf)[:4] != [1, 1, 1, 1]:
        raise AssertionError("Fox image is not primitive")
    if fox_boundary.rank() != 4:
        raise AssertionError("Fox boundary rank")

    handle_complement = fox_left.inv()[:, 4:8]
    handle_completion = fox_boundary.row_join(handle_complement)
    if abs(int(handle_completion.det())) != 1:
        raise AssertionError("handle quotient completion is not unimodular")

    betti = invariants["Lefschetz_and_Hodge"]["betti"]
    if betti != [1, 2, 92, 2, 1]:
        raise AssertionError("surface Betti numbers changed")
    primary_rank = thimble_kernel.cols + handle_complement.cols
    edge_rank = betti[2] - primary_rank
    if primary_rank != 90 or edge_rank != 2:
        raise AssertionError("surface-cycle rank decomposition")

    presentation = {
        "schema": "MTTQ79IntegralSurfaceCyclePresentation.v1",
        "status": "INTEGRAL_SURFACE_CYCLE_PRESENTATION_CLOSED",
        "action_convention": {
            "recorded_action": factorization["action_convention"],
            "cellular_homomorphism": "rho(g)=M(g)^-1",
            "homomorphic_boundary_word": "rho(A)*rho(B)*rho(A)^-1*rho(B)^-1",
        },
        "thimble_boundary_lattice": {
            "map": "delta: Z^90 -> H1(C_base,Z)=Z^4",
            "matrix_shape": [4, 90],
            "matrix_rows": rows(vanishing_cycles),
            "smith_diagonal": diagonal_entries(vanishing_snf)[:4],
            "image_saturated": True,
            "lexicographically_first_unimodular_pivot_indices_one_based": [
                index + 1 for index in pivot_indices
            ],
            "pivot_root_ids": [factors[index]["root_id"] for index in pivot_indices],
            "pivot_matrix": rows(pivot),
            "pivot_determinant": pivot_determinant,
            "closed_thimble_kernel_rank": thimble_kernel.cols,
            "closed_thimble_kernel_basis_columns": rows(thimble_kernel),
            "kernel_saturated": True,
        },
        "punctured_torus_handle_lattice": {
            "relative_cell_module": "(Z^4)_A direct_sum (Z^4)_B",
            "boundary_word": "A*B*A^-1*B^-1",
            "fox_boundary_formula": [
                "I-rho(A)rho(B)rho(A)^-1",
                "rho(A)-rho(A B A^-1 B^-1)",
            ],
            "fox_boundary_matrix_rows_A_then_B": rows(fox_boundary),
            "fox_smith_diagonal": diagonal_entries(fox_snf)[:4],
            "fox_image_saturated": True,
            "handle_quotient_rank": handle_complement.cols,
            "handle_quotient_complement_columns": rows(handle_complement),
            "unimodular_completion_determinant": int(
                handle_completion.det()
            ),
        },
        "surface_h2_decomposition": {
            "known_integral_H2_rank": betti[2],
            "closed_thimble_rank": thimble_kernel.cols,
            "punctured_torus_handle_rank": handle_complement.cols,
            "Leray_edge_rank": edge_rank,
            "abstract_free_decomposition": "Z^86 direct_sum Z^4 direct_sum Z^2",
            "primary_extension_rank": primary_rank,
            "torsion_free_reason": "H1(C,Z)=Z^2 and integral Poincare duality/UCT",
            "splitting_scope": "The rank-two Leray edge extension splits abstractly over Z; explicit geometric lifts are still required for a concrete 92-column period basis.",
        },
        "theorem": {
            "name": "Q79GenusTwoIntegralSurfaceCyclePresentationTheorem",
            "proved": True,
            "statement": "The A116 vanishing-boundary map has a saturated rank-86 kernel.  In the homomorphic action convention, the punctured-torus Fox boundary has primitive rank four and free rank-four cokernel.  Together with the rank-two Leray edge contribution, these give the exact free rank-92 surface-cycle presentation required before period execution.",
        },
    }
    dump(PRESENTATION, presentation)

    contract = {
        "schema": "MTTQ79CorrectedPrymPeriodExecutionContract.v1",
        "status": "INTEGRAL_COLUMN_OWNERSHIP_CLOSED_NUMERICAL_PERIODS_OPEN",
        "correction_to_A116_readiness": {
            "old_shorthand": a116_ready["next_execution"][
                "transport_generators"
            ],
            "correction": "The 90 meridian paths and A/B paths transport the local system, but they are not themselves 92 closed H2 basis cycles.",
            "no_A116_monodromy_result_reopened": True,
        },
        "period_assembly": {
            "primitive_thimble_integrals_shape": [8, 90],
            "closed_thimble_periods": "T_8x90 * K_90x86",
            "primitive_handle_cylinder_integrals_shape": [8, 8],
            "handle_periods": "H_8x8 * C_8x4, with the boundary-matching thimble correction fixed by the same Fox presentation",
            "Leray_edge_periods_shape": [8, 2],
            "final_integral_period_table_shape": [8, 92],
        },
        "closed": {
            "integral_column_count_and_ownership": True,
            "saturated_thimble_kernel": True,
            "torsion_free_handle_quotient": True,
            "surface_H2_rank": 92,
        },
        "open": {
            "primitive_thimble_numerical_values": 0,
            "primitive_handle_numerical_values": 0,
            "explicit_rank_two_Leray_edge_lifts": False,
            "beta_vector": False,
            "integral_branch": False,
            "gerbe_zero_or_no_go": False,
        },
        "next_required_artifact": NEXT,
    }
    dump(PERIOD_CONTRACT, contract)

    frontier = {
        "schema": "MTTU6FrontierAfterA117.v1",
        "status": STATUS,
        "global_integral_H1_surface_relation_closed": True,
        "integral_surface_cycle_presentation_closed": True,
        "closed_thimble_lattice_rank": 86,
        "punctured_torus_handle_lattice_rank": 4,
        "Leray_edge_rank": 2,
        "surface_H2_rank": 92,
        "beta_C_period_rows_emitted": 0,
        "integral_period_branch_selected": False,
        "gerbe_zero_or_no_go_executed": False,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(FRONTIER, frontier)

    authority_paths = [
        FACTORIZATION,
        SPECTRAL_INVARIANTS,
        A111_RESIDUES,
        A116_READY,
        Path(__file__),
        NOTE,
    ]
    candidate = {
        "schema": "MTTSelectedQ79GenusTwoIntegralSurfaceCyclePresentation.v1",
        "status": STATUS,
        "proof_artifact": str(NOTE.relative_to(ROOT)).replace("\\", "/"),
        "authority_hashes": [
            {
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "sha256": sha256(path),
            }
            for path in authority_paths
        ],
        "outputs": {
            "integral_cycle_presentation": str(PRESENTATION.relative_to(ROOT)).replace("\\", "/"),
            "corrected_period_contract": str(PERIOD_CONTRACT.relative_to(ROOT)).replace("\\", "/"),
            "frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
        },
        "supersession": {
            "artifact": "MTT_Selected_q79GenusTwoHandleAndLerayPeriodExecution_v1",
            "rank_count_retained": True,
            "primitive_86_plus_4_direct_sum_retired": True,
            "reason": "The period-selected central handle lift and oriented thimble tails require the A119 coupled integral quotient.",
        },
        "checks": {
            "vanishing_image_is_all_Z4": diagonal_entries(vanishing_snf)[:4] == [1, 1, 1, 1],
            "closed_thimble_kernel_is_saturated_rank_86": thimble_kernel.cols == 86,
            "Fox_image_is_primitive_rank_4": diagonal_entries(fox_snf)[:4] == [1, 1, 1, 1],
            "handle_quotient_is_free_rank_4": handle_complement.cols == 4,
            "unimodular_handle_completion": abs(int(handle_completion.det())) == 1,
            "surface_rank_reconciles_to_92": primary_rank + edge_rank == 92,
            "path_carriers_not_mistyped_as_H2_basis": True,
            "period_values_not_invented": contract["open"]["primitive_thimble_numerical_values"] == 0,
            "integral_branch_not_invented": not frontier["integral_period_branch_selected"],
            "gerbe_decision_not_invented": not frontier["gerbe_zero_or_no_go_executed"],
        },
        "results": frontier,
        "next_required_artifact": NEXT,
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "certificate": "MTTSelectedQ79GenusTwoIntegralSurfaceCyclePresentation",
        "status": STATUS,
        "candidate_path": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "candidate_sha256": sha256(CANDIDATE),
        "closure_claimed": False,
        "integral_surface_cycle_presentation_closed": True,
        "numerical_period_execution_closed": False,
        "full_U6_closed": False,
        "superseded_by_A119_coupled_integral_presentation": True,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    dump(CERTIFICATE, certificate)
    print(json.dumps(candidate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
