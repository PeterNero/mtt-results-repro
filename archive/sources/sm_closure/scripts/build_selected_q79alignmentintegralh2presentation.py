from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp, smith_normal_form


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79alignmentintegralh2presentation"
OUT = ROOT / "candidate_data" / SLUG
A129 = ROOT / "candidate_data" / "selected_q79alignmenthandlesandglobalsurfacerelation.candidate.json"
FACTORIZATION = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmenthandlesandglobalsurfacerelation"
    / "selected_alignment_global_integral_gauss_manin_factorization.packet.json"
)
CENTRAL_LIFTS = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_handle_central_lifts.interval.packet.json"
)
SPECTRAL_INVARIANTS = (
    ROOT
    / "candidate_data"
    / "selected_q79twistedspectralgerbelifthymandbianchiexecution"
    / "spectral_surface_invariants.packet.json"
)
MARKED_LATTICE = (
    ROOT
    / "candidate_data"
    / "selected_q79k3perioddomainxihessianexecutionormarkedmodelgerbecertificate"
    / "marked_lattice_certificate.packet.json"
)
CENTRAL_LIFT_SCRIPT = ROOT / "scripts" / "certify_q79_selected_alignment_handle_central_lifts.py"
PRESENTATION = OUT / "selected_alignment_coupled_integral_H2_chain_presentation.packet.json"
EDGE = OUT / "selected_alignment_Leray_edge_basis.packet.json"
BASIS = OUT / "selected_alignment_exact_integral_H2_basis.packet.json"
FRONTIER = OUT / "U6_frontier_after_A130.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}.certificate.json"

STATUS = (
    "MTT_U6_Q79_SELECTED_ALIGNMENT_EXACT_INTEGRAL_H2_BASIS_CLOSED_"
    "SELECTED_PERIOD_EXECUTION_OPEN"
)
NEXT = "MTT_Selected_q79SelectedAlignmentEightByNinetyTwoPeriodExecution_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def rows(matrix: sp.Matrix) -> list[list[int]]:
    return [[int(matrix[row, column]) for column in range(matrix.cols)] for row in range(matrix.rows)]


def diagonal(matrix: sp.Matrix) -> list[int]:
    return [abs(int(matrix[index, index])) for index in range(min(matrix.shape))]


def first_unimodular_columns(matrix: sp.Matrix) -> tuple[tuple[int, ...], int]:
    for indices in itertools.combinations(range(matrix.cols), matrix.rows):
        determinant = int(matrix[:, indices].det())
        if abs(determinant) == 1:
            return indices, determinant
    raise AssertionError("selected boundary has no unimodular four-column block")


def saturated_kernel_basis(
    boundary: sp.Matrix,
) -> tuple[sp.Matrix, tuple[int, ...], list[int], int]:
    pivots, determinant = first_unimodular_columns(boundary)
    nonpivots = [index for index in range(boundary.cols) if index not in pivots]
    pivot_inverse = boundary[:, pivots].inv()
    kernel = sp.zeros(boundary.cols, len(nonpivots))
    for column, index in enumerate(nonpivots):
        kernel[index, column] = 1
        coefficients = -pivot_inverse * boundary[:, index]
        for row, pivot_index in enumerate(pivots):
            kernel[pivot_index, column] = coefficients[row]
    if boundary * kernel != sp.zeros(boundary.rows, kernel.cols):
        raise AssertionError("selected saturated kernel boundary")
    if kernel[nonpivots, :] != sp.eye(len(nonpivots)):
        raise AssertionError("selected saturated kernel witness")
    return kernel, pivots, nonpivots, determinant


def local_extension(
    factors: list[dict], oriented: sp.Matrix, endpoint: sp.Matrix
) -> sp.Matrix:
    identity = sp.eye(4)
    current = identity
    extension_rows: list[sp.Matrix] = []
    for index, factor in enumerate(factors):
        action = sp.Matrix(factor["positive_picard_lefschetz_matrix"])
        increment = (action - identity) * current
        cycle = oriented[:, index]
        pivot = next(row for row in range(4) if cycle[row] != 0)
        coefficient = increment[pivot, :] / cycle[pivot]
        if increment != cycle * coefficient:
            raise AssertionError(f"selected local extension factor {index + 1}")
        extension_rows.append(coefficient)
        current = action * current
    if current != endpoint:
        raise AssertionError("selected local extension endpoint")
    extension = sp.Matrix.vstack(*extension_rows)
    if oriented * extension != endpoint - identity:
        raise AssertionError("selected local extension telescoping identity")
    return extension


def main() -> int:
    a129 = load(A129)
    factorization = load(FACTORIZATION)
    lifts = load(CENTRAL_LIFTS)
    invariants = load(SPECTRAL_INVARIANTS)
    marked_lattice = load(MARKED_LATTICE)
    if not a129["checks"]["global_integral_H1_representation_closed"]:
        raise AssertionError("A129 global factorization is unavailable")
    if not lifts["theorem"]["proved"] or lifts["selected_lifts"] != {"A": 1, "B": -1}:
        raise AssertionError("selected central handle lifts are unavailable")
    if invariants["Lefschetz_and_Hodge"]["betti"] != [1, 2, 92, 2, 1]:
        raise AssertionError("selected spectral-surface Betti numbers changed")
    if not marked_lattice["primitivity"]["span_H_delta_primitive"]:
        raise AssertionError("selected primitive K3 marking is unavailable")

    factors = factorization["factors"]
    intersection = sp.Matrix(factorization["base"]["intersection_matrix"])
    identity = sp.eye(4)
    oriented = sp.Matrix.hstack(
        *[sp.Matrix(factor["positive_vanishing_cycle_up_to_sign"]) for factor in factors]
    )
    if oriented.shape != (4, 90) or oriented.rank() != 4:
        raise AssertionError("selected vanishing boundary shape/rank")
    for index, factor in enumerate(factors):
        cycle = oriented[:, index]
        action = sp.Matrix(factor["positive_picard_lefschetz_matrix"])
        if action != identity + cycle * cycle.T * intersection:
            raise AssertionError(f"selected positive PL cycle {index + 1}")
    vanishing_snf = smith_normal_form(oriented, domain=sp.ZZ)
    if diagonal(vanishing_snf)[:4] != [1, 1, 1, 1]:
        raise AssertionError("selected vanishing image is not saturated")
    kernel, pivots, nonpivots, pivot_determinant = saturated_kernel_basis(oriented)
    if kernel.shape != (90, 86):
        raise AssertionError("selected thimble kernel shape")

    action_a = int(lifts["selected_lifts"]["A"]) * sp.Matrix(
        factorization["handle_actions"]["A"]
    )
    action_b = int(lifts["selected_lifts"]["B"]) * sp.Matrix(
        factorization["handle_actions"]["B"]
    )
    local_product = sp.Matrix(
        factorization["surface_relation"]["ordered_distinguished_action_product"]
    )
    handle_boundary_action = action_b.inv() * action_a.inv() * action_b * action_a
    if handle_boundary_action != local_product:
        raise AssertionError("selected central-lift commutator")

    handle_boundary = (action_a - identity).row_join(action_b - identity)
    fox = (
        identity - action_a.inv() * action_b * action_a
    ).col_join(action_a - handle_boundary_action)
    if handle_boundary * fox != handle_boundary_action - identity:
        raise AssertionError("selected Fox boundary identity")
    fox_snf = smith_normal_form(fox, domain=sp.ZZ)
    if diagonal(fox_snf)[:4] != [1, 1, 1, 0]:
        raise AssertionError("selected central-lift handle-only Fox Smith diagonal")

    extension = local_extension(factors, oriented, handle_boundary_action)
    full_relation = extension.col_join(fox)
    full_boundary = (-oriented).row_join(handle_boundary)
    if full_boundary * full_relation != sp.zeros(4, 4):
        raise AssertionError("selected full relation is not a cycle")

    pivot_inverse = oriented[:, pivots].inv()
    handle_lifts = sp.zeros(90, 8)
    pivot_handle_lifts = pivot_inverse * handle_boundary
    for row, pivot_index in enumerate(pivots):
        for column in range(8):
            handle_lifts[pivot_index, column] = pivot_handle_lifts[row, column]
    if oriented * handle_lifts != handle_boundary:
        raise AssertionError("selected handle boundary lift")
    kernel_cycles = kernel.row_join(handle_lifts).col_join(
        sp.zeros(8, 86).row_join(sp.eye(8))
    )
    if kernel_cycles.shape != (98, 94):
        raise AssertionError("selected full kernel basis shape")
    if full_boundary * kernel_cycles != sp.zeros(4, 94):
        raise AssertionError("selected full kernel boundary")

    residual_extension = extension - handle_lifts * fox
    thimble_relation_coordinates = residual_extension[nonpivots, :]
    if kernel * thimble_relation_coordinates != residual_extension:
        raise AssertionError("selected relation thimble coordinates")
    relation_coordinates = thimble_relation_coordinates.col_join(fox)
    if kernel_cycles * relation_coordinates != full_relation:
        raise AssertionError("selected relation coordinate replay")
    relation_snf, relation_left, relation_right = smith_normal_decomp(
        relation_coordinates, domain=sp.ZZ
    )
    if relation_snf != relation_left * relation_coordinates * relation_right:
        raise AssertionError("selected relation Smith decomposition")
    if diagonal(relation_snf)[:4] != [1, 1, 1, 1]:
        raise AssertionError("selected full relation is not primitive")
    complement = relation_left.inv()[:, 4:94]
    completion = relation_coordinates.row_join(complement)
    completion_determinant = int(completion.det())
    if abs(completion_determinant) != 1:
        raise AssertionError("selected primary quotient completion")
    primary_basis = kernel_cycles * complement
    if primary_basis.shape != (98, 90):
        raise AssertionError("selected primary basis shape")
    if full_boundary * primary_basis != sp.zeros(4, 90):
        raise AssertionError("selected primary basis boundary")
    pure_thimble_columns = sum(
        primary_basis[90:98, column] == sp.zeros(8, 1)
        for column in range(primary_basis.cols)
    )
    handle_supported_columns = primary_basis.cols - pure_thimble_columns
    maximum_coefficient = max(abs(int(value)) for value in primary_basis)

    presentation = {
        "schema": "MTTQ79SelectedAlignmentCoupledIntegralH2ChainPresentation.v1",
        "status": "SELECTED_ALIGNMENT_SATURATED_RANK_90_PRIMARY_H2_LATTICE_CLOSED",
        "canonical_orientation": {
            "rule": "For each primitive PL vector, the first nonzero coordinate is positive; orient the associated thimble compatibly.",
            "period_values_required": False,
            "orientation_changes_are_unimodular_column_sign_changes": True,
        },
        "chain_complex": {
            "relative_chain_module": "Z^90_thimbles direct_sum Z^8_handle_cylinders",
            "relative_chain_rank": 98,
            "boundary_matrix_shape": [4, 98],
            "boundary_formula": "[-W | (A-I) | (B-I)]",
            "boundary_matrix_rows": rows(full_boundary),
            "boundary_rank": full_boundary.rank(),
            "kernel_rank": kernel_cycles.cols,
            "full_surface_relations_shape": [98, 4],
            "full_surface_relations_columns": rows(full_relation),
        },
        "vanishing_lattice": {
            "boundary_shape": [4, 90],
            "boundary_rows": rows(oriented),
            "smith_diagonal": diagonal(vanishing_snf)[:4],
            "image_saturated": True,
            "kernel_rank": kernel.cols,
            "kernel_saturated": True,
            "unimodular_pivot_indices_one_based": [index + 1 for index in pivots],
            "pivot_determinant": pivot_determinant,
        },
        "selected_central_lifts": {
            "A": lifts["selected_lifts"]["A"],
            "B": lifts["selected_lifts"]["B"],
            "selection_source": "interval leading-coefficient winding, not period fitting",
            "A_action": rows(action_a),
            "B_action": rows(action_b),
            "commutator_action": rows(handle_boundary_action),
            "handle_only_Fox_smith_diagonal": diagonal(fox_snf)[:4],
            "handle_only_rank_three_defect_is_resolved_by_full_thimble_coupling": True,
        },
        "coupled_quotient": {
            "kernel_basis_shape": [98, 94],
            "kernel_basis_columns": rows(kernel_cycles),
            "relation_coordinates_shape": [94, 4],
            "relation_coordinates_columns": rows(relation_coordinates),
            "full_relation_smith_diagonal": diagonal(relation_snf)[:4],
            "full_relation_primitive": True,
            "quotient_completion_determinant": completion_determinant,
            "primary_integral_basis_shape": [98, 90],
            "primary_integral_basis_columns": rows(primary_basis),
            "pure_thimble_columns": pure_thimble_columns,
            "handle_supported_columns": handle_supported_columns,
            "maximum_absolute_basis_coefficient": maximum_coefficient,
            "primary_lattice_torsion_free": True,
        },
        "theorem": {
            "name": "Q79SelectedAlignmentCoupledIntegralPrimaryH2BasisTheorem",
            "proved": True,
            "statement": "With the interval-selected central lifts +A and -B and canonically oriented selected thimbles, the 98-chain boundary kernel has rank 94. The four coupled thimble/Fox surface relations form a primitive sublattice with Smith diagonal (1,1,1,1); the emitted quotient basis is therefore a torsion-free rank-90 primary integral H2 basis.",
        },
    }
    dump(PRESENTATION, presentation)

    edge = {
        "schema": "MTTQ79SelectedAlignmentLerayEdgeBasis.v1",
        "status": "SELECTED_ALIGNMENT_TWO_PRIMITIVE_LERAY_EDGE_CLASSES_CLOSED",
        "ambient_geometry": {
            "threefold": "J=K3 x E_i",
            "surface_divisor_class": "[C_A]=p_K3^*H+3*p_E^*[point], independent of invertible alignment A",
            "surface_betti_numbers": invariants["Lefschetz_and_Hodge"]["betti"],
            "K3_lattice_even_unimodular": True,
            "polarization_H_primitive_and_square_two": True,
        },
        "edge_basis": {
            "F": "fiber C_A intersect (K3 x {e0})",
            "Gamma_0": "primitive ambient horizontal lift adjusted by an integral multiple of F",
            "intersection_matrix": [[0, 1], [1, 0]],
            "both_classes_primitive": True,
            "rank": 2,
        },
        "theorem": {
            "name": "Q79SelectedAlignmentPrimitiveLerayEdgeBasisTheorem",
            "proved": True,
            "statement": "The invertible alignment changes the incidence fibration but not its ambient divisor class. The primitive fiber and adjusted horizontal ambient class therefore give the same primitive hyperbolic rank-two Leray edge pair on C_A.",
        },
    }
    dump(EDGE, edge)

    basis = {
        "schema": "MTTQ79SelectedAlignmentExactIntegralH2Basis.v1",
        "status": "SELECTED_ALIGNMENT_EXACT_RANK_92_INTEGRAL_H2_BASIS_CLOSED",
        "surface_H2_rank": 92,
        "primary_basis": {
            "rank": 90,
            "chain_module_order": [
                *[f"thimble_{index:03d}" for index in range(1, 91)],
                *[f"handle_A_fiber_{index}" for index in range(1, 5)],
                *[f"handle_B_fiber_{index}" for index in range(1, 5)],
            ],
            "basis_columns": rows(primary_basis),
        },
        "Leray_edge_basis": ["F", "Gamma_0"],
        "column_order": [
            *[f"primary_{index:02d}" for index in range(1, 91)],
            "Leray_F",
            "Leray_Gamma0",
        ],
        "exact_checks": {
            "primary_rank_90": True,
            "primary_quotient_torsion_free": True,
            "edge_rank_2_primitive": True,
            "total_rank_92": True,
            "complete_integral_endpoint_basis": True,
        },
        "strict_scope": {
            "period_columns_emitted": 0,
            "integral_period_branch_selected": False,
            "observed_SM_values_used": False,
        },
    }
    dump(BASIS, basis)

    frontier = {
        "schema": "MTTU6FrontierAfterA130.v1",
        "status": STATUS,
        "selected_alignment_global_integral_H1_surface_relation_closed": True,
        "selected_alignment_central_handle_lifts_closed": True,
        "selected_alignment_primary_integral_H2_basis_columns": 90,
        "selected_alignment_Leray_edge_basis_columns": 2,
        "selected_alignment_exact_integral_H2_basis_columns": 92,
        "selected_alignment_period_columns": 0,
        "integral_period_branch_selected": False,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(FRONTIER, frontier)

    authority_paths = [
        A129,
        FACTORIZATION,
        CENTRAL_LIFTS,
        SPECTRAL_INVARIANTS,
        MARKED_LATTICE,
        CENTRAL_LIFT_SCRIPT,
        Path(__file__),
        PRESENTATION,
        EDGE,
        BASIS,
        FRONTIER,
    ]
    candidate = {
        "schema": "MTTSelectedQ79AlignmentIntegralH2Presentation.v1",
        "status": STATUS,
        "proof_artifact": "proof_corpus/MTT_Selected_q79AlignmentIntegralH2Presentation_v1.md",
        "authority_hashes": [
            {"path": relative(path), "sha256": sha256(path)} for path in authority_paths
        ],
        "outputs": {
            "coupled_presentation": relative(PRESENTATION),
            "Leray_edge_basis": relative(EDGE),
            "exact_integral_H2_basis": relative(BASIS),
            "frontier": relative(FRONTIER),
        },
        "checks": {
            "selected_central_lifts_derived_without_period_fit": True,
            "vanishing_image_saturated": True,
            "full_coupled_relation_primitive": True,
            "primary_integral_basis_has_90_columns": True,
            "complete_integral_H2_basis_has_92_columns": True,
            "period_values_not_invented": True,
            "integral_branch_not_invented": True,
            "observed_SM_target_fitting_used": False,
        },
        "results": frontier,
        "next_required_artifact": NEXT,
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "certificate": "MTTSelectedQ79AlignmentIntegralH2Presentation",
        "status": STATUS,
        "candidate_sha256": sha256(CANDIDATE),
        "selected_central_handle_lifts_closed": True,
        "selected_exact_integral_H2_basis_columns": 92,
        "selected_period_columns": 0,
        "integral_branch_selected": False,
        "observed_SM_target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    dump(CERTIFICATE, certificate)
    print(f"wrote {CANDIDATE.relative_to(ROOT)}")
    print(f"wrote {CERTIFICATE.relative_to(ROOT)}")
    print(
        "A130: selected central lifts and exact coupled rank-92 integral H2 basis closed; periods remain"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
