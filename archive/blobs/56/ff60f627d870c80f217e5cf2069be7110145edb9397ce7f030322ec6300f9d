from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
H2 = (
    ROOT
    / "candidate_data"
    / "selected_q79alignmentintegralh2presentation"
    / "selected_alignment_coupled_integral_H2_chain_presentation.packet.json"
)
A231 = (
    ROOT
    / "candidate_data"
    / "selected_q79covariantperiodbranchcutsetandtightbetatransport"
    / "selected_alignment_thimble_periods"
    / "covariant_floating_probe"
    / "validated_transport"
    / "n3.chain.frontier.json"
)
OUTPUT = A231.parent / "n3.chain.relation_l1.a393.json"
NOTE = ROOT / "proof_corpus" / "MTT_q79Rank3ChainRelationL1Optimality_A393_v1.md"
ARTIFACT = "A393"
ZERO_DUAL_VALUES = {
    6: Fraction(0),
    7: Fraction(-1),
    8: Fraction(-1),
    9: Fraction(1),
    16: Fraction(1),
    38: Fraction(-1, 5),
    39: Fraction(-1),
    45: Fraction(1),
    56: Fraction(2, 5),
    58: Fraction(1),
    63: Fraction(1),
    69: Fraction(-1),
    72: Fraction(1),
    75: Fraction(4, 5),
    96: Fraction(-1),
    97: Fraction(-1),
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def authority(path: Path) -> dict[str, str]:
    return {"path": relative(path), "sha256": sha256(path)}


def dot(left: list[int | Fraction], right: list[int | Fraction]) -> Fraction:
    return sum((Fraction(a) * Fraction(b) for a, b in zip(left, right)), Fraction(0))


def matrix_vector(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def transpose_vector(matrix: list[list[int]], vector: list[int | Fraction]) -> list[Fraction]:
    return [
        sum((Fraction(matrix[row][column]) * Fraction(vector[row]) for row in range(len(matrix))), Fraction(0))
        for column in range(len(matrix[0]))
    ]


def encode_fraction(value: Fraction) -> dict[str, int]:
    return {"numerator": value.numerator, "denominator": value.denominator}


def main() -> int:
    h2 = load(H2)
    a231 = load(A231)
    if h2.get("status") != "SELECTED_ALIGNMENT_SATURATED_RANK_90_PRIMARY_H2_LATTICE_CLOSED":
        raise AssertionError("selected integral H2 presentation changed")
    relations = [
        [int(value) for value in row]
        for row in h2["chain_complex"]["full_surface_relations_columns"]
    ]
    boundary = [
        [int(value) for value in row]
        for row in h2["chain_complex"]["boundary_matrix_rows"]
    ]
    if len(relations) != 98 or any(len(row) != 4 for row in relations):
        raise AssertionError("surface relation matrix is not 98 by 4")
    if len(boundary) != 4 or any(len(row) != 98 for row in boundary):
        raise AssertionError("boundary matrix is not 4 by 98")
    for column in range(4):
        relation = [relations[row][column] for row in range(98)]
        if matrix_vector(boundary, relation) != [0, 0, 0, 0]:
            raise AssertionError("surface relation is not in the boundary kernel")

    chain = [0 for _ in range(98)]
    rows = a231["exact_floating_decomposition"]["thimble_rows"]
    for row in rows:
        index = int(row["distinguished_index"])
        chain[index - 1] = int(row["PL_corrected_effective_signed_coefficient"])
    handles = [int(value) for value in a231["selected_candidate"]["primitive_handle_coordinates"]]
    if len(handles) != 8:
        raise AssertionError("rank-3 handle coordinate count changed")
    chain[90:] = handles
    if len(rows) != 76 or sum(value != 0 for value in chain[:90]) != 76:
        raise AssertionError("rank-3 thimble support changed")
    if chain[64] != 4:
        raise AssertionError("Picard-Lefschetz corrected d065 coefficient changed")

    dual = []
    for one_based, coefficient in enumerate(chain, start=1):
        if coefficient > 0:
            dual.append(Fraction(1))
        elif coefficient < 0:
            dual.append(Fraction(-1))
        else:
            if one_based not in ZERO_DUAL_VALUES:
                raise AssertionError(f"dual witness lacks zero coordinate {one_based}")
            dual.append(ZERO_DUAL_VALUES[one_based])
    if set(ZERO_DUAL_VALUES) != {
        index for index, value in enumerate(chain, start=1) if value == 0
    }:
        raise AssertionError("dual zero-coordinate inventory changed")
    relation_annihilation = transpose_vector(relations, dual)
    if relation_annihilation != [Fraction(0) for _ in range(4)]:
        raise AssertionError("dual witness does not annihilate the relation lattice")
    if max(abs(value) for value in dual) > 1:
        raise AssertionError("dual witness leaves the l-infinity unit ball")
    l1 = sum(abs(value) for value in chain)
    dual_pairing = dot(dual, chain)
    if l1 != 174 or dual_pairing != 174:
        raise AssertionError("rank-3 L1 certificate changed")

    payload = {
        "artifact": ARTIFACT,
        "schema": "MTTQ79Rank3ChainRelationL1Optimality.v1",
        "status": "PL_CORRECTED_RANK3_CHAIN_L1_MINIMAL_MODULO_SURFACE_RELATIONS_PROVED",
        "chain_module": "Z^90_thimbles direct_sum Z^8_handle_cylinders",
        "PL_corrected_chain_coordinates": chain,
        "surface_relation_matrix_98_by_4": relations,
        "boundary_vector": matrix_vector(boundary, chain),
        "dual_witness": [encode_fraction(value) for value in dual],
        "exact_replay": {
            "chain_support": sum(value != 0 for value in chain),
            "thimble_support": sum(value != 0 for value in chain[:90]),
            "handle_support": sum(value != 0 for value in chain[90:]),
            "chain_l1_norm": l1,
            "dual_l_infinity_norm": encode_fraction(max(abs(value) for value in dual)),
            "relation_transpose_times_dual": [
                encode_fraction(value) for value in relation_annihilation
            ],
            "dual_pairing_with_chain": encode_fraction(dual_pairing),
            "all_four_relations_have_zero_boundary": True,
        },
        "theorem": {
            "statement": (
                "For every k in Z^4, ||c+Rk||_1 >= y.(c+Rk) = y.c = 174 = ||c||_1. "
                "Hence the PL-corrected rank-3 chain c is globally L1-minimal in its "
                "class modulo the four selected primitive surface relations."
            ),
            "proof_ingredients": [
                "||y||_infinity <= 1",
                "R^T y = 0 exactly over Q",
                "y.c = ||c||_1 = 174",
            ],
            "global_integer_relation_shift_optimality": True,
            "global_real_relation_shift_optimality": True,
        },
        "authority": {
            "selected_integral_H2_presentation": authority(H2),
            "A231_rank3_chain_and_PL_identity": authority(A231),
            "builder_source": authority(Path(__file__).resolve()),
        },
        "strict_scope": {
            "observed_SM_values_used": False,
            "PL_corrected_chain_used": True,
            "four_exact_primitive_surface_relations_used": True,
            "unweighted_L1_relation_compression_closed_by_optimality": True,
            "weighted_interval_radius_optimality_proved": False,
            "minimum_support_L0_optimality_proved": False,
            "coupled_chain_period_transport_closed": False,
            "interval_Newton_existence_and_uniqueness_closed": False,
            "covariant_zero_proved": False,
            "full_SM_closure_proved": False,
        },
        "next_required_artifact": (
            "tighten the existing representative by correlated period transport; "
            "surface-relation L1 compression cannot lower its coefficient burden"
        ),
    }
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    NOTE.write_text(
        "# MTT q79 Rank-3 Chain Relation L1 Optimality (A393) v1\n\n"
        "A393 includes the Picard-Lefschetz correction in the 98-coordinate "
        "thimble/handle chain and tests all shifts by the four exact primitive "
        "surface relations.\n\n"
        "A rational dual witness has infinity norm one, annihilates all four "
        "relations exactly, and pairs with the chain to `174`, equal to its "
        "L1 norm. Therefore the current chain is globally L1-minimal in this "
        "relation class.\n\n"
        "This does not prove weighted interval-radius or minimum-support "
        "optimality. It does rule out unweighted relation compression as the "
        "missing Krawczyk-width mechanism.\n",
        encoding="utf-8",
    )
    print(f"wrote {relative(OUTPUT)}")
    print(f"wrote {relative(NOTE)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
