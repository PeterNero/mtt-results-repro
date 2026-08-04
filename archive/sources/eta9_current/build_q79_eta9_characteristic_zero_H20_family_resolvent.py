from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from scipy import sparse

import assemble_q79_eta9_full_recursive_H20_source_block as source_block
import bind_q79_eta9_original_jacobian_coordinate_factorization as factor_io
import build_q79_eta9_gauss_manin_block_chunk as polynomial_io
import build_q79_eta9_graph_cayley_block_compiler as cayley
import build_q79_eta9_number_field_smooth_lift as number_field
import build_q79_eta9_original_jacobian_macaulay as macaulay
import build_q79_eta9_smooth_graph_slice_witness as residue
import verify_q79_eta9_original_jacobian_coordinate_solver as coordinate_io


ROOT = Path(__file__).resolve().parent
BASE = residue.BASE
GLOBAL_F0 = ROOT / "q79_eta9_global_f0_lift.packet.json"
NUMBER_FIELD = ROOT / "q79_eta9_number_field_smooth_lift.packet.json"
B89 = ROOT / "q79_eta9_concrete_pencil_seed.packet.json"
B103 = ROOT / "q79_eta9_full_vanishing_residue_basis.packet.json"
MACAULAY = ROOT / "q79_eta9_original_jacobian_macaulay_H20.packet.json"
CSC = ROOT / "q79_eta9_original_jacobian_macaulay_H20_csc.packet.json"
FACTORIZATION = ROOT / "q79_eta9_original_jacobian_coordinate_factorization_H20.packet.json"
FAMILY_UPDATE = ROOT / "q79_eta9_family_macaulay_update_H20.packet.json"
FAMILY_UPDATE_NPZ = ROOT / "q79_eta9_family_macaulay_update_H20.npz"
FAMILY_COORDINATES = ROOT / "q79_eta9_family_macaulay_update_H20.coordinates.cscbin"
GF11_RESOLVENT = ROOT / "q79_eta9_family_resolvent_H20.packet.json"
OUT = ROOT / "q79_eta9_characteristic_zero_H20_family_resolvent.packet.json"

PRIME = 11
RESIDUE_GAMMA = 3


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(label)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while block := handle.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def record(path: Path, packet: dict | None = None) -> dict[str, object]:
    result: dict[str, object] = {
        "path": str(path),
        "sha256": sha256(path),
        "bytes": path.stat().st_size,
    }
    if packet is not None:
        result["schema_or_certificate"] = packet.get(
            "schema", packet.get("certificate", "UNSCHEMATIZED")
        )
        result["status"] = packet.get("status", "NO_STATUS_FIELD")
    return result


def evaluate_mod11(coefficients: list[int], gamma: int = RESIDUE_GAMMA) -> int:
    return sum(
        (coefficient % PRIME) * pow(gamma, exponent, PRIME)
        for exponent, coefficient in enumerate(coefficients)
    ) % PRIME


def primitive_integer_vector(vector: sp.Matrix) -> list[int]:
    denominator = sp.ilcm(*[entry.q for entry in vector])
    values = [int(entry * denominator) for entry in vector]
    divisor = math.gcd(*[abs(value) for value in values if value])
    values = [value // divisor for value in values]
    first = next(value for value in values if value)
    return [-value for value in values] if first < 0 else values


def base_equation_terms(base: dict) -> dict[tuple[int, ...], int]:
    x, y, z = sp.symbols("x y z")
    f6 = sp.Poly(
        sp.sympify(base["explicit_K3"]["F6_equals_G3_squared_plus_Q2_H4"]),
        x,
        y,
        z,
        domain=sp.ZZ,
    )
    terms: dict[tuple[int, ...], int] = {
        (0, 0, 0, 2, 0, 0, 0, 0, 0, 0): 1
    }
    for powers, coefficient in f6.terms():
        exponent = tuple(int(value) for value in powers) + (0, 0, 0, 0, 0, 0, 0)
        terms[exponent] = -int(coefficient)
    return terms


def k3_image_matrix(
    target_lookup: dict[tuple[int, ...], int], base: dict
) -> sp.Matrix:
    multipliers = macaulay.monomials_of_cox_degree((3, 1, 0))
    require(len(multipliers) == 33, "33 H20 K3 multipliers")
    terms = base_equation_terms(base)
    matrix = sp.zeros(len(target_lookup), len(multipliers))
    for column, multiplier in enumerate(multipliers):
        for exponent, coefficient in terms.items():
            product = tuple(
                multiplier[index] + exponent[index] for index in range(10)
            )
            row = target_lookup.get(product)
            require(row is not None, "K3 multiplier product lies in H20 ambient basis")
            matrix[row, column] += coefficient
    return matrix


def exact_f0_vector(
    target_lookup: dict[tuple[int, ...], int], global_f0: dict
) -> list[list[int]]:
    adapter = residue.extension_adapter()
    coefficients = residue.f0_coefficients(global_f0)
    result = [[0] * 6 for _ in range(len(target_lookup))]
    for theta in range(3):
        for offset, monomials, w_exponent in (
            (0, cayley.monomials(9), 0),
            (55, cayley.monomials(6), 1),
        ):
            for local_index, powers in enumerate(monomials):
                exponent = tuple(powers) + (w_exponent,) + tuple(
                    1 if theta == index else 0 for index in range(3)
                ) + (0, 0, 0)
                row = target_lookup.get(exponent)
                require(row is not None, "F0 term lies in H20 ambient basis")
                result[row] = [
                    int(value)
                    for value in residue.gamma_coordinates(
                        coefficients[theta * 83 + offset + local_index], adapter
                    )
                ]
    return result


def exact_f1_vector(
    target_lookup: dict[tuple[int, ...], int], b89: dict
) -> list[int]:
    result = [0] * len(target_lookup)
    for theta, row_text in enumerate(b89["pencil"]["F1_coefficient_rows"]):
        for exponent, coefficient in polynomial_io.parse_normal_form(row_text).items():
            lifted = list(exponent)
            lifted[4 + theta] += 1
            row = target_lookup.get(tuple(lifted))
            require(row is not None, "F1 term lies in H20 ambient basis")
            result[row] += int(coefficient)
    return result


def main() -> None:
    paths = {
        "K3_base": BASE,
        "global_F0": GLOBAL_F0,
        "number_field_lift": NUMBER_FIELD,
        "B89_pencil": B89,
        "B103_basis": B103,
        "H20_Macaulay": MACAULAY,
        "H20_CSC": CSC,
        "H20_factorization": FACTORIZATION,
        "H20_family_update": FAMILY_UPDATE,
        "H20_GF11_resolvent": GF11_RESOLVENT,
    }
    packets = {name: load(path) for name, path in paths.items()}
    for name, packet in packets.items():
        if "checks" in packet:
            require(all(packet["checks"].values()), f"{name} checks")

    base = packets["K3_base"]
    b89 = packets["B89_pencil"]
    macaulay_packet = packets["H20_Macaulay"]
    csc = packets["H20_CSC"]
    factor = packets["H20_factorization"]
    update = packets["H20_family_update"]
    gf11_resolvent = packets["H20_GF11_resolvent"]
    number_field_packet = packets["number_field_lift"]

    require(
        number_field_packet["number_field"][
            "minimal_polynomial_coefficients_ascending"
        ]
        == number_field.MINPOLY,
        "same selected sextic number field",
    )
    require(b89["pencil"]["field"] == "Q(gamma)", "B89 number field")
    require(
        b89["pencil"]["members"] == "F_lambda=F0+lambda*F1",
        "affine B89 pencil",
    )
    require(
        factor["exact_coordinate_identity"]["selected_original_Jacobian_columns"]
        == list(range(34)),
        "all 34 H20 image columns selected in their source order",
    )
    blocks = macaulay_packet["column_blocks"]
    require(blocks[7]["generator_name"] == "dPhi/du", "K3 image block")
    require(
        (blocks[7]["first_column"], blocks[7]["past_last_column"]) == (0, 33),
        "33 K3 image columns",
    )
    require(blocks[9]["generator_name"] == "dPhi/ds", "F0 image block")
    require(
        (blocks[9]["first_column"], blocks[9]["past_last_column"]) == (33, 34),
        "one F0 image column",
    )

    target = [
        tuple(int(value) for value in exponent)
        for exponent in macaulay_packet["target_monomial_basis"]["exponent_vectors"]
    ]
    require(len(target) == 282 and len(set(target)) == 282, "H20 ambient basis")
    target_lookup = {exponent: index for index, exponent in enumerate(target)}
    quotient_rows = [int(value) for value in csc["binary"]["quotient_unit_rows"]]
    require(len(quotient_rows) == 248, "248 H20 quotient-unit rows")
    quotient_row_set = set(quotient_rows)
    residual_rows = [row for row in range(282) if row not in quotient_row_set]
    require(len(residual_rows) == 34, "34 H20 complement rows")

    k3_matrix = k3_image_matrix(target_lookup, base)
    residual_k3 = k3_matrix.extract(residual_rows, range(33))
    require(residual_k3.rank() == 33, "K3 image has complement rank 33")
    nullspace = residual_k3.T.nullspace()
    require(len(nullspace) == 1, "unique H20 complement left-null covector")
    left_covector = primitive_integer_vector(nullspace[0])
    require(
        left_covector
        == [16] + [0] * 20 + [12] + [0] * 5 + [-24, 0, 0, 1, 0, 0, 0],
        "frozen primitive H20 quotient covector",
    )

    f0 = exact_f0_vector(target_lookup, packets["global_F0"])
    f1 = exact_f1_vector(target_lookup, b89)
    alpha_numerator = sum(
        left_covector[index] * f1[row]
        for index, row in enumerate(residual_rows)
    )
    alpha_denominator = [
        sum(
            left_covector[index] * f0[row][power]
            for index, row in enumerate(residual_rows)
        )
        for power in range(6)
    ]
    require(alpha_numerator == 133, "exact H20 alpha numerator")
    require(
        alpha_denominator == [-335, 547, 1304, 627, 443, -407],
        "exact H20 alpha denominator",
    )
    require(any(alpha_denominator), "nonzero alpha denominator in Q(gamma)")

    residual_numerator = sp.Matrix(
        [
            [
                alpha_denominator[power] * f1[row]
                - alpha_numerator * f0[row][power]
                for power in range(6)
            ]
            for row in residual_rows
        ]
    )
    _, pivot_rows_tuple = residual_k3.T.rref()
    pivot_rows = [int(value) for value in pivot_rows_tuple]
    require(len(pivot_rows) == 33, "33 independent K3 complement rows")
    square_k3 = residual_k3.extract(pivot_rows, range(33))
    k3_coordinate_numerators = square_k3.inv() * residual_numerator.extract(
        pivot_rows, range(6)
    )
    require(
        residual_k3 * k3_coordinate_numerators == residual_numerator,
        "all 34 complement equations hold",
    )

    unscaled_coordinate_numerators = sp.zeros(282, 6)
    for column in range(33):
        for power in range(6):
            unscaled_coordinate_numerators[248 + column, power] = (
                k3_coordinate_numerators[column, power]
            )
    unscaled_coordinate_numerators[281, 0] = alpha_numerator
    quotient_k3 = k3_matrix.extract(quotient_rows, range(33))
    for quotient_index, ambient_row in enumerate(quotient_rows):
        for power in range(6):
            unscaled_coordinate_numerators[quotient_index, power] = (
                alpha_denominator[power] * f1[ambient_row]
                - sum(
                    quotient_k3[quotient_index, column]
                    * k3_coordinate_numerators[column, power]
                    for column in range(33)
                )
                - alpha_numerator * f0[ambient_row][power]
            )

    rational_scale = int(
        sp.ilcm(*[entry.q for entry in unscaled_coordinate_numerators])
    )
    require(rational_scale == 256, "frozen common rational denominator")
    coordinate_numerators = [
        [
            int(unscaled_coordinate_numerators[row, power] * rational_scale)
            for power in range(6)
        ]
        for row in range(282)
    ]
    coordinate_denominator = [
        rational_scale * coefficient for coefficient in alpha_denominator
    ]

    # Verify C0*x=F1 by clearing the one common Q(gamma) denominator.
    cross_multiplication_residuals = 0
    for ambient_row in range(282):
        quotient_index = (
            quotient_rows.index(ambient_row) if ambient_row in quotient_row_set else None
        )
        for power in range(6):
            left = (
                coordinate_numerators[quotient_index][power]
                if quotient_index is not None
                else 0
            )
            left += sum(
                int(k3_matrix[ambient_row, column])
                * coordinate_numerators[248 + column][power]
                for column in range(33)
            )
            left += f0[ambient_row][power] * coordinate_numerators[281][0]
            right = coordinate_denominator[power] * f1[ambient_row]
            if left != right:
                cross_multiplication_residuals += 1
    require(cross_multiplication_residuals == 0, "exact C0*x=F1 identity")

    selected_source_mod11, _ = source_block.selected_source_matrix("H20")
    exact_source_mod11 = np.zeros((282, 282), dtype=np.uint8)
    for column, row in enumerate(quotient_rows):
        exact_source_mod11[row, column] = 1
    for row in range(282):
        for column in range(33):
            exact_source_mod11[row, 248 + column] = int(k3_matrix[row, column]) % PRIME
        exact_source_mod11[row, 281] = evaluate_mod11(f0[row])
    source_residual = (
        sparse.csc_matrix(exact_source_mod11.astype(np.int32))
        - selected_source_mod11.astype(np.int32)
    ).tocsc()
    source_residual.data %= PRIME
    source_residual.eliminate_zeros()
    require(source_residual.nnz == 0, "characteristic-zero C0 reduces to selected GF11 C0")

    family_update = sparse.load_npz(FAMILY_UPDATE_NPZ).tocsc()
    require(family_update.shape == (282, 34), "GF11 family-update shape")
    require(
        [column for column in range(34) if family_update.indptr[column + 1] > family_update.indptr[column]]
        == [33],
        "only dPhi/ds changes in H20",
    )
    exact_f1_mod11 = np.asarray([value % PRIME for value in f1], dtype=np.uint8)
    require(
        np.array_equal(family_update[:, 33].toarray().ravel(), exact_f1_mod11),
        "characteristic-zero C1 reduces to selected GF11 C1",
    )

    denominator_mod11 = evaluate_mod11(coordinate_denominator)
    require(denominator_mod11 != 0, "coordinate denominator is a unit at (11,gamma-3)")
    coordinate_reduction = np.asarray(
        [
            evaluate_mod11(numerator) * pow(denominator_mod11, -1, PRIME) % PRIME
            for numerator in coordinate_numerators
        ],
        dtype=np.uint8,
    )
    gf11_coordinates, quotient_count, image_rank = coordinate_io.read_coordinates(
        FAMILY_COORDINATES
    )
    require(
        gf11_coordinates.shape == (282, 34)
        and (quotient_count, image_rank) == (248, 34),
        "GF11 coordinate dimensions",
    )
    active_columns = [
        column
        for column in range(34)
        if gf11_coordinates.indptr[column + 1] > gf11_coordinates.indptr[column]
    ]
    require(active_columns == [33], "one active GF11 coordinate column")
    require(
        np.array_equal(
            coordinate_reduction,
            gf11_coordinates[:, 33].toarray().ravel().astype(np.uint8),
        ),
        "all 282 exact coordinates reduce to the frozen GF11 result",
    )
    alpha_mod11 = (
        evaluate_mod11([rational_scale * alpha_numerator])
        * pow(denominator_mod11, -1, PRIME)
        % PRIME
    )
    require(
        alpha_mod11
        == gf11_resolvent["resolvent"]["alpha_mod11"]
        == 7,
        "characteristic-zero alpha reduces to the GF11 alpha",
    )

    checks = {
        "the_selected_sextic_number_field_and_B89_affine_pencil_are_hash_bound": True,
        "the_H20_augmented_chart_is_exactly_248_quotient_units_plus33_K3_columns_plus_F0": True,
        "the33_K3_columns_have_rank33_on_the34_row_complement": True,
        "the_primitive_integral_left_null_covector_is_unique_up_to_sign": True,
        "the_exact_alpha_numerator133_and_degree5_denominator_are_computed_from_F1_and_F0": True,
        "the_alpha_denominator_is_nonzero_in_the_degree6_number_field": True,
        "all282_characteristic_zero_coordinates_are_emitted_over_one_common_denominator": True,
        "the_cross_multiplied_identity_C0_times_x_equals_F1_has_zero_residual": True,
        "the_exact_C0_and_C1_reduce_to_the_frozen_GF11_selected_chart": True,
        "all282_exact_coordinates_reduce_to_the_existing_GF11_coordinate_solution": True,
        "the_characteristic_zero_alpha_reduces_to_alpha7_mod11": True,
        "the_H20_family_resolvent_is_exactly_rank_one_over_Q_gamma": True,
        "no_H11_H02_global_connection_monodromy_period_or_betaC_is_inferred": True,
    }
    require(all(checks.values()), "characteristic-zero H20 checks")

    packet = {
        "schema": "MTTQ79Eta9CharacteristicZeroH20FamilyResolvent.v1",
        "date": "2026-08-03",
        "status": (
            "Q79_ETA9_SELECTED_H20_AFFINE_FAMILY_CHART_AND_RANK_ONE_RESOLVENT_"
            "CLOSED_EXACT_OVER_Q_GAMMA_WITH_COMPLETE282_COORDINATE_VECTOR_AND_"
            "GF11_REDUCTION_BRIDGE"
        ),
        "controlling_blocker": "B.ETA9.01",
        "inputs": {
            name: record(path, packets[name]) for name, path in paths.items()
        }
        | {
            "H20_family_update_NPZ": record(FAMILY_UPDATE_NPZ),
            "H20_family_coordinates_GF11": record(FAMILY_COORDINATES),
        },
        "coefficient_field": {
            "field": "Q(gamma)",
            "minimal_polynomial_coefficients_ascending": number_field.MINPOLY,
            "minimal_polynomial": (
                "gamma^6+24*gamma^5+89*gamma^4+44*gamma^3+"
                "33*gamma^2+16*gamma+64"
            ),
            "irreducibility_certificate": number_field_packet["number_field"][
                "irreducible_over_Q_reason"
            ],
            "good_reduction_prime_ideal": "(11,gamma-3)",
        },
        "selected_H20_chart": {
            "ambient_dimension": 282,
            "coordinate_order": (
                "248 B103 quotient-unit columns, 33 multiplier-times-K columns, F0"
            ),
            "quotient_unit_ambient_rows_zero_based": quotient_rows,
            "complement_ambient_rows_zero_based": residual_rows,
            "K3_multiplier_count": 33,
            "K3_complement_rank": 33,
            "primitive_left_null_covector_on_complement": left_covector,
            "left_null_support_local_zero_based": [
                index for index, value in enumerate(left_covector) if value
            ],
            "left_null_support_ambient_zero_based": [
                residual_rows[index]
                for index, value in enumerate(left_covector)
                if value
            ],
            "selected_square_K3_rows_local_zero_based": pivot_rows,
            "selected_square_K3_determinant": str(int(square_k3.det())),
        },
        "rank_one_update": {
            "definition": "K_H20=C0^{-1}*C1=x*e_F0^T",
            "active_augmented_column_zero_based": 281,
            "coordinate_vector_length": 282,
            "coordinate_vector_nonzero_entries_over_Q_gamma": sum(
                any(value for value in row) for row in coordinate_numerators
            ),
            "common_denominator_coefficients_ascending": coordinate_denominator,
            "coordinate_numerator_coefficients_ascending": coordinate_numerators,
            "cross_multiplication_identity": (
                "C0*coordinate_numerators=coordinate_denominator*F1 coefficientwise in Q[gamma]"
            ),
            "cross_multiplication_residual_nonzeros": cross_multiplication_residuals,
            "alpha_primitive_fraction": {
                "numerator": alpha_numerator,
                "denominator_coefficients_ascending": alpha_denominator,
                "formula": (
                    "133/(-335+547*gamma+1304*gamma^2+627*gamma^3+"
                    "443*gamma^4-407*gamma^5)"
                ),
            },
            "quadratic_identity": "K_H20^2=alpha*K_H20",
            "rank_over_Q_gamma": 1,
        },
        "chart_determinant_ratio": {
            "formula": "det(C(lambda))/det(C0)=1+alpha*lambda=(D+133*lambda)/D",
            "D_coefficients_ascending": alpha_denominator,
            "unique_chart_pole": "lambda=-D(gamma)/133",
        },
        "good_reduction_replay": {
            "prime": PRIME,
            "gamma_residue": RESIDUE_GAMMA,
            "common_denominator_mod11": denominator_mod11,
            "alpha_mod11": alpha_mod11,
            "coordinate_entries_compared": 282,
            "coordinate_mismatches": 0,
            "C0_matrix_mismatches": int(source_residual.nnz),
            "C1_vector_mismatches": 0,
        },
        "checks": checks,
        "theorem": {
            "name": "q79Eta9CharacteristicZeroH20FamilyResolventTheorem",
            "statement": (
                "For the selected B89 pencil over Q(gamma), the frozen H20 augmented "
                "Macaulay chart consists of 248 monomial quotient units, 33 multiples "
                "of the K3 equation, and F0. The K3 columns have a one-dimensional "
                "integral left annihilator. Applying it to F1 and F0 gives the exact "
                "displayed alpha. The emitted 282-coordinate vector satisfies "
                "C0*x=F1 identically after clearing its nonzero common denominator. "
                "Consequently K=C0^{-1}C1=x e_F0^T has rank one, obeys K^2=alpha K, "
                "and has determinant ratio 1+alpha lambda. Reduction at "
                "(11,gamma-3) reproduces every entry of the prior GF(11) solution."
            ),
            "tier": "CLOSED_EXACT_CHARACTERISTIC_ZERO_LOCAL_H20_FAMILY_RESOLVENT",
        },
        "guardrails": [
            "This closes the selected H20 local affine chart over Q(gamma), not H11 or H02.",
            "The unique zero of the H20 chart determinant is a coordinate-chart pole; it is not identified with a physical discriminant value.",
            "The packet does not emit a characteristic-zero Gauss-Manin path evaluator, integral meridian matrix, periods, 248 readouts or beta_C.",
            "The selected F0 integer-representative lift and hash-selected integral F1 are fixed source data; no observed value or fitted parameter is introduced here.",
        ],
        "next_required_object": (
            "Construct the analogous characteristic-zero implicit K=C0^{-1}C1 actions "
            "on the selected H11 and H02 reachable source blocks, then combine them with "
            "the canonical A1 Frobenius recurrence in a certified path evaluator."
        ),
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print("Q79_ETA9_CHARACTERISTIC_ZERO_H20_FAMILY_RESOLVENT_BUILD_PASS")
    print(
        f"alpha=133/D(gamma) coordinates=282 scale={rational_scale} "
        f"alpha_mod11={alpha_mod11} packet_sha256={sha256(OUT)}"
    )


if __name__ == "__main__":
    main()
