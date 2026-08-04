from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp, smith_normal_form


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_q79genus2handleandlerayperiodexecution"
OUTPUT_DIR = ROOT / "candidate_data" / SLUG
FACTORIZATION = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2distinguishedcutsystemandglobalrelation"
    / "global_integral_gauss_manin_factorization.packet.json"
)
PRIMITIVE_THIMBLES = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2thimbleperiodexecution"
    / "primitive_thimble_period_candidate_table.packet.json"
)
THIMBLE_CONVERGENCE = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2thimbleperiodexecution"
    / "full_90_column_convergence_audit.packet.json"
)
THIMBLE_DIR = ROOT / "candidate_data" / "selected_q79genus2thimbleperiodexecution"
HANDLE_PRODUCTION = OUTPUT_DIR / "primitive_handle_periods.production.packet.json"
HANDLE_TIGHT = OUTPUT_DIR / "primitive_handle_periods.tight.packet.json"
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
RESIDUES = (
    ROOT
    / "candidate_data"
    / "selected_q79genus2lefschetzperiodreduction"
    / "explicit_prym_residues_and_delta_normal_function.packet.json"
)
NOTE = (
    ROOT
    / "proof_corpus"
    / "MTT_Selected_q79GenusTwoHandleAndLerayPeriodExecution_v1.md"
)
ORIENTATION = OUTPUT_DIR / "oriented_thimble_alignment.packet.json"
PRESENTATION = OUTPUT_DIR / "coupled_integral_H2_chain_presentation.packet.json"
LERAY = OUTPUT_DIR / "explicit_Leray_edge_periods.packet.json"
CONVERGENCE = OUTPUT_DIR / "full_integral_basis_convergence.packet.json"
PERIOD_TABLE = OUTPUT_DIR / "full_integral_basis_period_table.packet.json"
FRONTIER = OUTPUT_DIR / "U6_frontier_after_A119.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERTIFICATE = ROOT / "certificates" / f"{SLUG}_certificate.json"
STATUS = (
    "MTT_U6_Q79_COUPLED_INTEGRAL_H2_BASIS_AND_FLOATING_8X92_PERIOD_"
    "TABLE_CLOSED_INTERVAL_BETA_BRANCH_OPEN"
)
NEXT = "MTT_Selected_q79GenusTwoNormalFunctionBetaAndIntegralBranchExecution_v1"
EXPECTED_ORIENTATION = (
    "--++++-++--+-+-------+--++-+-++-++---+--+---++-------+-+---+-----+"
    "--++++--+---++--+++-++++"
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


def integer_rows(matrix: sp.Matrix) -> list[list[int]]:
    return [
        [int(matrix[row, column]) for column in range(matrix.cols)]
        for row in range(matrix.rows)
    ]


def complex_value(value: dict) -> complex:
    return complex(float(value["real"]), float(value["imaginary"]))


def complex_table(values: list[list[dict]]) -> np.ndarray:
    return np.asarray(
        [[complex_value(value) for value in row] for row in values],
        dtype=np.complex128,
    )


def complex_pair(value: complex) -> dict[str, str]:
    return {
        "real": format(float(value.real), ".17g"),
        "imaginary": format(float(value.imag), ".17g"),
    }


def complex_rows(matrix: np.ndarray) -> list[list[dict[str, str]]]:
    return [
        [complex_pair(complex(matrix[row, column])) for column in range(matrix.shape[1])]
        for row in range(matrix.shape[0])
    ]


def diagonal(matrix: sp.Matrix) -> list[int]:
    return [abs(int(matrix[index, index])) for index in range(min(matrix.shape))]


def first_unimodular_columns(matrix: sp.Matrix) -> tuple[tuple[int, ...], int]:
    for indices in itertools.combinations(range(matrix.cols), matrix.rows):
        determinant = int(matrix[:, indices].det())
        if abs(determinant) == 1:
            return indices, determinant
    raise AssertionError("no unimodular four-column block")


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
        raise AssertionError("kernel boundary")
    if kernel[nonpivots, :] != sp.eye(len(nonpivots)):
        raise AssertionError("kernel saturation witness")
    return kernel, pivots, nonpivots, determinant


def oriented_vanishing_cycles(
    factorization: dict, handle_packet: dict
) -> tuple[sp.Matrix, list[int], list[dict], float]:
    factors = factorization["factors"]
    base_periods = complex_table(
        handle_packet["marking"]["base_holomorphic_period_matrix"]
    )
    if base_periods.shape != (2, 4):
        raise AssertionError("base holomorphic period matrix shape")
    signs: list[int] = []
    rows: list[dict] = []
    maximum_error = 0.0
    for index, factor in enumerate(factors, start=1):
        packet_path = THIMBLE_DIR / (
            f"d{index:03d}_{factor['root_id']}.thimble_period.candidate.json"
        )
        packet = load(packet_path)
        observed = np.asarray(
            [
                complex_value(value)
                for value in packet["execution"][
                    "base_fiber_holomorphic_periods_dt_over_u_and_t_dt_over_u"
                ]
            ],
            dtype=np.complex128,
        )
        unoriented = np.asarray(
            factor["positive_vanishing_cycle_up_to_sign"], dtype=np.int64
        )
        predicted = base_periods @ unoriented
        scale = max(
            float(np.linalg.norm(observed)),
            float(np.linalg.norm(predicted)),
            np.finfo(float).tiny,
        )
        positive_error = float(np.linalg.norm(observed - predicted) / scale)
        negative_error = float(np.linalg.norm(observed + predicted) / scale)
        sign = 1 if positive_error <= negative_error else -1
        selected_error = min(positive_error, negative_error)
        signs.append(sign)
        maximum_error = max(maximum_error, selected_error)
        rows.append(
            {
                "distinguished_index": index,
                "root_id": factor["root_id"],
                "orientation_sign": sign,
                "positive_scaled_residual": format(positive_error, ".17g"),
                "negative_scaled_residual": format(negative_error, ".17g"),
                "selected_scaled_residual": format(selected_error, ".17g"),
            }
        )
    sign_string = "".join("+" if sign == 1 else "-" for sign in signs)
    if sign_string != EXPECTED_ORIENTATION:
        raise AssertionError(f"orientation string changed: {sign_string}")
    if maximum_error >= 2.0e-8:
        raise AssertionError("thimble orientation alignment residual")
    unoriented_matrix = sp.Matrix.hstack(
        *[
            sp.Matrix(factor["positive_vanishing_cycle_up_to_sign"])
            for factor in factors
        ]
    )
    oriented = unoriented_matrix * sp.diag(*signs)
    return oriented, signs, rows, maximum_error


def local_extension(
    factors: list[dict], oriented: sp.Matrix, endpoint: sp.Matrix
) -> sp.Matrix:
    identity = sp.eye(4)
    current = identity
    rows: list[sp.Matrix] = []
    for index, factor in enumerate(factors):
        action = sp.Matrix(factor["positive_picard_lefschetz_matrix"])
        increment = (action - identity) * current
        cycle = oriented[:, index]
        pivot = next(row for row in range(4) if cycle[row] != 0)
        coefficient = increment[pivot, :] / cycle[pivot]
        if increment != cycle * coefficient:
            raise AssertionError(f"local extension rank-one factor {index + 1}")
        rows.append(coefficient)
        current = action * current
    if current != endpoint:
        raise AssertionError("local extension endpoint action")
    extension = sp.Matrix.vstack(*rows)
    if oriented * extension != endpoint - identity:
        raise AssertionError("local extension telescoping identity")
    return extension


def main() -> int:
    inputs = (
        FACTORIZATION,
        PRIMITIVE_THIMBLES,
        THIMBLE_CONVERGENCE,
        HANDLE_PRODUCTION,
        HANDLE_TIGHT,
        SPECTRAL_INVARIANTS,
        MARKED_LATTICE,
        RESIDUES,
        NOTE,
    )
    for path in inputs:
        if not path.exists():
            raise FileNotFoundError(path)

    factorization = load(FACTORIZATION)
    primitive_packet = load(PRIMITIVE_THIMBLES)
    thimble_convergence = load(THIMBLE_CONVERGENCE)
    production_packet = load(HANDLE_PRODUCTION)
    tight_packet = load(HANDLE_TIGHT)
    invariants = load(SPECTRAL_INVARIANTS)
    marked_lattice = load(MARKED_LATTICE)
    residues = load(RESIDUES)

    factors = factorization["factors"]
    if len(factors) != 90:
        raise AssertionError("factor count")
    if invariants["Lefschetz_and_Hodge"]["betti"] != [1, 2, 92, 2, 1]:
        raise AssertionError("surface Betti numbers")
    if invariants["Lefschetz_and_Hodge"]["p_g"] != 9:
        raise AssertionError("surface geometric genus")
    if residues["residue_forms"]["exact_linear_rank"] != 8:
        raise AssertionError("primitive residue rank")
    if marked_lattice["primitivity"]["span_H_delta_primitive"] is not True:
        raise AssertionError("primitive K3 polarization marking")

    oriented, signs, orientation_rows, orientation_error = oriented_vanishing_cycles(
        factorization, production_packet
    )
    kernel, pivots, nonpivots, pivot_determinant = saturated_kernel_basis(
        oriented
    )
    if kernel.shape != (90, 86):
        raise AssertionError("oriented thimble kernel shape")

    identity = sp.eye(4)
    lift_a = int(production_packet["central_lift_result"]["A"])
    lift_b = int(production_packet["central_lift_result"]["B"])
    if (lift_a, lift_b) != (1, -1):
        raise AssertionError("selected central handle lifts")
    action_a = lift_a * sp.Matrix(factorization["handle_actions"]["A"])
    action_b = lift_b * sp.Matrix(factorization["handle_actions"]["B"])
    local_product = sp.Matrix(
        factorization["surface_relation"][
            "ordered_distinguished_action_product"
        ]
    )
    handle_boundary_action = action_b.inv() * action_a.inv() * action_b * action_a
    if handle_boundary_action != local_product:
        raise AssertionError("central-lift commutator")

    handle_boundary = (action_a - identity).row_join(action_b - identity)
    fox = (
        identity - action_a.inv() * action_b * action_a
    ).col_join(action_a - handle_boundary_action)
    if handle_boundary * fox != handle_boundary_action - identity:
        raise AssertionError("Fox boundary identity")
    fox_snf = smith_normal_form(fox, domain=sp.ZZ)
    if diagonal(fox_snf)[:4] != [1, 1, 1, 3]:
        raise AssertionError("selected-lift handle-only Smith diagonal")

    extension = local_extension(factors, oriented, handle_boundary_action)
    full_relation = extension.col_join(fox)
    full_boundary = (-oriented).row_join(handle_boundary)
    if full_boundary * full_relation != sp.zeros(4, 4):
        raise AssertionError("full relation is not a cycle")

    pivot_inverse = oriented[:, pivots].inv()
    handle_lifts = sp.zeros(90, 8)
    pivot_handle_lifts = pivot_inverse * handle_boundary
    for row, pivot_index in enumerate(pivots):
        for column in range(8):
            handle_lifts[pivot_index, column] = pivot_handle_lifts[row, column]
    if oriented * handle_lifts != handle_boundary:
        raise AssertionError("handle boundary lift")
    kernel_cycles = kernel.row_join(handle_lifts).col_join(
        sp.zeros(8, 86).row_join(sp.eye(8))
    )
    if kernel_cycles.shape != (98, 94):
        raise AssertionError("full kernel basis shape")
    if full_boundary * kernel_cycles != sp.zeros(4, 94):
        raise AssertionError("full kernel basis boundary")

    residual_extension = extension - handle_lifts * fox
    thimble_relation_coordinates = residual_extension[nonpivots, :]
    if kernel * thimble_relation_coordinates != residual_extension:
        raise AssertionError("relation coordinates in thimble kernel")
    relation_coordinates = thimble_relation_coordinates.col_join(fox)
    if kernel_cycles * relation_coordinates != full_relation:
        raise AssertionError("full relation coordinate replay")

    relation_snf, relation_left, relation_right = smith_normal_decomp(
        relation_coordinates, domain=sp.ZZ
    )
    if relation_snf != relation_left * relation_coordinates * relation_right:
        raise AssertionError("full relation Smith decomposition")
    if diagonal(relation_snf)[:4] != [1, 1, 1, 1]:
        raise AssertionError("full relation is not primitive")
    complement = relation_left.inv()[:, 4:94]
    completion = relation_coordinates.row_join(complement)
    completion_determinant = int(completion.det())
    if abs(completion_determinant) != 1:
        raise AssertionError("primary quotient completion")
    primary_basis = kernel_cycles * complement
    if primary_basis.shape != (98, 90):
        raise AssertionError("primary basis shape")
    if full_boundary * primary_basis != sp.zeros(4, 90):
        raise AssertionError("primary basis boundary")
    pure_thimble_columns = sum(
        primary_basis[90:98, column] == sp.zeros(8, 1)
        for column in range(primary_basis.cols)
    )
    if pure_thimble_columns != 82:
        raise AssertionError("pure-thimble column count")
    handle_supported_columns = primary_basis.cols - pure_thimble_columns
    maximum_coefficient = max(abs(int(value)) for value in primary_basis)

    orientation_packet = {
        "schema": "MTTQ79OrientedThimbleAlignment.v1",
        "status": "ALL_90_THIMBLE_ORIENTATIONS_ALIGNED_TO_THE_MARKED_BASE_FIBER",
        "orientation_sign_string": EXPECTED_ORIENTATION,
        "positive_sign_count": signs.count(1),
        "negative_sign_count": signs.count(-1),
        "maximum_selected_scaled_residual": format(orientation_error, ".17g"),
        "oriented_vanishing_boundary_matrix_rows": integer_rows(oriented),
        "columns": orientation_rows,
        "correction": {
            "A118_primitive_thimble_integrals_remain_valid": True,
            "A118_old_TK_table_is_a_basis_diagnostic_only": True,
            "reason": "The endpoint chord orientations differ from the up-to-sign PL representatives in 52 of 90 columns; the final closed assembly must use the oriented boundary matrix and the coupled handle tails.",
        },
    }
    dump(ORIENTATION, orientation_packet)

    presentation = {
        "schema": "MTTQ79CoupledIntegralH2ChainPresentation.v1",
        "status": "SATURATED_RANK_90_PRIMARY_H2_LATTICE_CLOSED",
        "chain_complex": {
            "relative_chain_module": "Z^90_thimbles direct_sum Z^8_handle_cylinders",
            "relative_chain_rank": 98,
            "boundary_matrix_shape": [4, 98],
            "boundary_formula": "[-W | (A-I) | (B-I)]",
            "boundary_matrix_rows": integer_rows(full_boundary),
            "boundary_rank": full_boundary.rank(),
            "kernel_rank": kernel_cycles.cols,
            "four_full_surface_relations_shape": [98, 4],
            "four_full_surface_relations_columns": integer_rows(full_relation),
        },
        "selected_central_lifts": {
            "A": lift_a,
            "B": lift_b,
            "A_action": integer_rows(action_a),
            "B_action": integer_rows(action_b),
            "commutator_action": integer_rows(handle_boundary_action),
            "handle_only_Fox_smith_diagonal": diagonal(fox_snf)[:4],
            "handle_only_index_three_is_not_surface_torsion": True,
        },
        "coupled_extension": {
            "local_thimble_extension_L_shape": [90, 4],
            "local_thimble_extension_L_rows": integer_rows(extension),
            "Fox_handle_extension_F_shape": [8, 4],
            "Fox_handle_extension_F_rows": integer_rows(fox),
            "identity_WL_equals_P_minus_I": True,
            "identity_DF_equals_P_minus_I": True,
            "identity_boundary_of_LF_is_zero": True,
        },
        "saturated_kernel_and_quotient": {
            "oriented_kernel_pivot_indices_one_based": [index + 1 for index in pivots],
            "oriented_kernel_pivot_determinant": pivot_determinant,
            "kernel_basis_Z_shape": [98, 94],
            "kernel_basis_Z_columns": integer_rows(kernel_cycles),
            "relation_coordinates_X_shape": [94, 4],
            "relation_coordinates_X_columns": integer_rows(relation_coordinates),
            "full_relation_smith_diagonal": diagonal(relation_snf)[:4],
            "full_relation_primitive": True,
            "quotient_completion_determinant": completion_determinant,
            "primary_integral_basis_shape": [98, 90],
            "primary_integral_basis_columns": integer_rows(primary_basis),
            "pure_thimble_columns": pure_thimble_columns,
            "handle_supported_columns": handle_supported_columns,
            "maximum_absolute_basis_coefficient": maximum_coefficient,
            "primary_lattice_torsion_free": True,
        },
        "correction_to_A117": {
            "rank_90_primary_plus_rank_2_edge_count_remains_valid": True,
            "old_86_plus_4_primitive_direct_sum_superseded": True,
            "correct_integral_split": "82 pure-thimble basis columns plus 8 coupled thimble/handle basis columns",
            "index_three_defect_removed_by_full_thimble_tail": True,
        },
        "theorem": {
            "name": "Q79CoupledIntegralPrimaryH2BasisTheorem",
            "proved": True,
            "statement": "With the period-selected central lifts +A and -B and the 90 chord-oriented thimbles, the full 98-chain boundary kernel has rank 94. The four coupled thimble/Fox surface relations form a primitive sublattice with Smith diagonal (1,1,1,1), so their quotient is a torsion-free rank-90 primary H2 lattice with the emitted integral basis.",
        },
    }
    dump(PRESENTATION, presentation)

    leray = {
        "schema": "MTTQ79ExplicitLerayEdgePeriods.v1",
        "status": "TWO_PRIMITIVE_AMBIENT_LERAY_EDGE_LIFTS_AND_EIGHT_ZERO_PERIOD_COLUMNS_CLOSED",
        "ambient_geometry": {
            "threefold": "J=K3 x E_i",
            "surface_divisor": "[C]=p_K3^*H+3*p_E^*[point]",
            "K3_lattice": "H2(K3,Z) is even unimodular",
            "polarization": "H is primitive and H^2=2",
            "dual_class_existence": "Unimodularity and primitivity give d in H2(K3,Z) with H.d=1.",
        },
        "edge_basis": {
            "F": "fiber C intersect (K3 x {e0})",
            "Gamma_d": "PD_C(i^*p_K3^*PD_K3(d))",
            "F_squared": 0,
            "F_dot_Gamma_d": 1,
            "Gamma_d_squared": "3*d^2, an even integer",
            "isotropic_horizontal_adjustment": "Gamma_0=Gamma_d-(3*d^2/2)F",
            "intersection_matrix_F_Gamma0": [[0, 1], [1, 0]],
            "both_classes_primitive": True,
            "no_holomorphic_section_assumed": True,
        },
        "primitive_residue_argument": {
            "p_g_C": 9,
            "ambient_h20_dimension": 1,
            "section_space_dimension": 9,
            "defining_scalar_line_dimension": 1,
            "traceless_residue_dimension": 8,
            "A111_exact_residue_rank": residues["residue_forms"]["exact_linear_rank"],
            "conclusion": "The eight sl3 residue forms span H20_prim(C), hence pair trivially with every cycle Poincare dual to an ambient restriction.",
        },
        "period_column_order": ["F", "Gamma_0"],
        "period_matrix_shape": [8, 2],
        "period_matrix_exact": [[0, 0] for _ in range(8)],
        "theorem": {
            "name": "Q79PrimitiveResidueLerayEdgeZeroPeriodTheorem",
            "proved": True,
            "statement": "The fiber F and an ambient horizontal lift Gamma_0 form a primitive hyperbolic Leray-edge pair. The eight traceless incidence residues are primitive holomorphic two-forms, so both edge columns vanish exactly. This uses a topological K3 dual class and does not assert an algebraic or holomorphic section.",
        },
    }
    dump(LERAY, leray)

    thimble_periods = complex_table(primitive_packet["period_rows"])
    production_handles = complex_table(
        production_packet["primitive_handle_period_matrix"]
    )
    tight_handles = complex_table(tight_packet["primitive_handle_period_matrix"])
    if thimble_periods.shape != (8, 90):
        raise AssertionError("primitive thimble period shape")
    if production_handles.shape != tight_handles.shape or production_handles.shape != (8, 8):
        raise AssertionError("primitive handle period shape")
    primitive_periods = np.hstack([thimble_periods, production_handles])
    primary_integer = np.asarray(primary_basis.tolist(), dtype=np.float64)
    primary_periods = primitive_periods @ primary_integer
    final_periods = np.hstack([primary_periods, np.zeros((8, 2), dtype=np.complex128)])
    if final_periods.shape != (8, 92):
        raise AssertionError("final period shape")

    delta_thimble = np.zeros((8, 90), dtype=np.float64)
    convergence_rows = {
        int(row["distinguished_index"]): row
        for row in thimble_convergence[
            "columns_by_decreasing_scale_normalized_difference"
        ]
    }
    if set(convergence_rows) != set(range(1, 91)):
        raise AssertionError("thimble convergence column inventory")
    for index in range(1, 91):
        delta_thimble[:, index - 1] = np.asarray(
            [float(value) for value in convergence_rows[index]["rowwise_absolute_differences"]],
            dtype=np.float64,
        )
    delta_handle = np.abs(production_handles - tight_handles)
    primary_difference_envelope = (
        delta_thimble @ np.abs(primary_integer[:90, :])
        + delta_handle @ np.abs(primary_integer[90:98, :])
    )
    maximum_envelope = float(np.max(primary_difference_envelope))
    column_scaled_envelopes = []
    for column in range(90):
        scale = max(float(np.max(np.abs(primary_periods[:, column]))), np.finfo(float).tiny)
        column_scaled_envelopes.append(
            float(np.max(primary_difference_envelope[:, column]) / scale)
        )
    maximum_scaled_envelope = max(column_scaled_envelopes)
    maximum_handle_difference = float(np.max(delta_handle))
    maximum_handle_scale = max(
        float(np.max(np.abs(production_handles))), np.finfo(float).tiny
    )
    convergence = {
        "schema": "MTTQ79FullIntegralBasisFloatingConvergence.v1",
        "status": "TWO_RUN_DIFFERENCE_ENVELOPE_PROPAGATED_TO_ALL_90_PRIMARY_COLUMNS",
        "primitive_handle_production_parameters": production_packet["execution"],
        "primitive_handle_tight_parameters": tight_packet["execution"],
        "maximum_primitive_handle_absolute_difference": format(maximum_handle_difference, ".17g"),
        "maximum_primitive_handle_scale_normalized_difference": format(
            maximum_handle_difference / maximum_handle_scale, ".17g"
        ),
        "propagation_formula": "DeltaPi <= DeltaT*abs(B_thimble)+DeltaH*abs(B_handle)",
        "primary_entrywise_absolute_difference_envelope_rows": [
            [format(float(value), ".17g") for value in row]
            for row in primary_difference_envelope
        ],
        "maximum_primary_absolute_difference_envelope": format(maximum_envelope, ".17g"),
        "maximum_primary_column_scale_normalized_difference_envelope": format(
            maximum_scaled_envelope, ".17g"
        ),
        "edge_columns_are_exact_zero": True,
        "strict_scope": {
            "all_90_primary_columns_covered": True,
            "all_2_edge_columns_exact": True,
            "floating_two_run_convergence_only": True,
            "interval_enclosure": False,
            "rigorous_truncation_error_bound": False,
        },
    }
    dump(CONVERGENCE, convergence)

    period_table = {
        "schema": "MTTQ79FullIntegralBasisPeriodTable.v1",
        "status": "FULL_FLOATING_8X92_PERIOD_TABLE_ASSEMBLED_ON_EXACT_INTEGRAL_BASIS",
        "form_order": primitive_packet["form_names"],
        "column_order": [
            *[f"primary_{index:02d}" for index in range(1, 91)],
            "Leray_F",
            "Leray_Gamma0",
        ],
        "period_matrix_shape": [8, 92],
        "period_rows": complex_rows(final_periods),
        "assembly": {
            "primitive_period_matrix_shape": [8, 98],
            "primary_integral_basis_shape": [98, 90],
            "primary_formula": "[T_8x90 | H_8x8] B_98x90",
            "edge_formula": "append exact zero columns for F and Gamma_0",
        },
        "strict_scope": {
            "exact_integral_basis": True,
            "floating_period_values": True,
            "interval_certified_entries": 0,
            "normal_function_beta_rows_emitted": 0,
            "integral_branch_selected": False,
            "gerbe_zero_or_no_go": False,
            "target_fitting_used": False,
        },
    }
    dump(PERIOD_TABLE, period_table)

    frontier = {
        "schema": "MTTU6FrontierAfterA119.v1",
        "status": STATUS,
        "global_integral_H1_surface_relation_closed": True,
        "selected_central_handle_lifts_closed": True,
        "oriented_thimble_columns": 90,
        "exact_primary_integral_basis_columns": 90,
        "exact_Leray_edge_basis_columns": 2,
        "exact_integral_H2_basis_columns": 92,
        "floating_period_table_shape": [8, 92],
        "floating_period_columns_executed": 92,
        "interval_period_columns_certified": 0,
        "beta_C_period_rows_emitted": 0,
        "integral_period_branch_selected": False,
        "gerbe_zero_or_no_go_executed": False,
        "strict_MTT_source_moduli_removed": 0,
        "U6_strong_CP_closed": False,
        "next_required_artifact": NEXT,
    }
    dump(FRONTIER, frontier)

    authority_paths = [
        *inputs,
        Path(__file__),
        ORIENTATION,
        PRESENTATION,
        LERAY,
        CONVERGENCE,
        PERIOD_TABLE,
        FRONTIER,
    ]
    candidate = {
        "schema": "MTTSelectedQ79GenusTwoHandleAndLerayPeriodExecution.v1",
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
            "orientation": str(ORIENTATION.relative_to(ROOT)).replace("\\", "/"),
            "coupled_integral_presentation": str(PRESENTATION.relative_to(ROOT)).replace("\\", "/"),
            "Leray_edge_periods": str(LERAY.relative_to(ROOT)).replace("\\", "/"),
            "convergence": str(CONVERGENCE.relative_to(ROOT)).replace("\\", "/"),
            "period_table": str(PERIOD_TABLE.relative_to(ROOT)).replace("\\", "/"),
            "frontier": str(FRONTIER.relative_to(ROOT)).replace("\\", "/"),
        },
        "checks": {
            "all_90_orientations_selected": len(signs) == 90,
            "orientation_alignment_below_2e_8": orientation_error < 2.0e-8,
            "central_lifts_are_plusA_minusB": (lift_a, lift_b) == (1, -1),
            "handle_only_index_three_detected": diagonal(fox_snf)[:4] == [1, 1, 1, 3],
            "full_relation_is_primitive": diagonal(relation_snf)[:4] == [1, 1, 1, 1],
            "primary_integral_basis_has_90_columns": primary_basis.cols == 90,
            "full_integral_basis_has_92_columns": final_periods.shape[1] == 92,
            "Leray_edge_periods_are_exact_zero": leray["period_matrix_exact"] == [[0, 0] for _ in range(8)],
            "floating_8x92_table_assembled": final_periods.shape == (8, 92),
            "interval_promotion_not_invented": frontier["interval_period_columns_certified"] == 0,
            "integral_branch_not_invented": not frontier["integral_period_branch_selected"],
            "gerbe_decision_not_invented": not frontier["gerbe_zero_or_no_go_executed"],
        },
        "results": frontier,
        "next_required_artifact": NEXT,
    }
    dump(CANDIDATE, candidate)
    certificate = {
        "certificate": "MTTSelectedQ79GenusTwoHandleAndLerayPeriodExecution",
        "status": STATUS,
        "candidate_path": str(CANDIDATE.relative_to(ROOT)).replace("\\", "/"),
        "candidate_sha256": sha256(CANDIDATE),
        "closure_claimed": False,
        "exact_integral_H2_basis_closed": True,
        "floating_8x92_period_table_closed": True,
        "interval_period_enclosure_closed": False,
        "normal_function_beta_closed": False,
        "integral_branch_selected": False,
        "full_U6_closed": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }
    dump(CERTIFICATE, certificate)
    print(json.dumps(candidate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
