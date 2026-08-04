from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_REPO = TEXPAPERS / "mtt-sm-parity-closure"

SPECTRAL_SYMBOL = (
    ROOT / "certificates" / "q79_spectral_hym_strain_symbol_bridge_certificate.json"
)
ROOTSTACK = (
    ROOT
    / "certificates"
    / "q79_cubic_norm_full_monodromy_rootstack_bridge_certificate.json"
)
A107 = (
    SM_REPO
    / "certificates"
    / "selected_q79markedk3ellipticperiodsourceandgerbezeroexecution_certificate.json"
)
CHERN_ORBIT = (
    SM_REPO
    / "candidate_data"
    / "selected_q79markedk3ellipticperiodsourceandgerbezeroexecution"
    / "Z4_Chern_orbit_superset.packet.json"
)
SINGLE_BRANCH_NOGO = (
    SM_REPO
    / "candidate_data"
    / "selected_q79markedk3ellipticperiodsourceandgerbezeroexecution"
    / "single_branch_order4_stabilizer_nogo.packet.json"
)
COMPLEX_NESTING_GATE = (
    SM_REPO
    / "candidate_data"
    / "selected_q79markedk3ellipticperiodsourceandgerbezeroexecution"
    / "complex_nesting_and_retarded_bridge_gate.packet.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_complement_quarterturn_hessian_scalarization_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Complement_QuarterTurn_Hessian_Scalarization_Theorem_v1.md"
)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def permutation_matrix(perm: tuple[int, int, int]) -> sp.Matrix:
    matrix = sp.zeros(3)
    for source, target in enumerate(perm):
        matrix[target, source] = 1
    return matrix


def edge_action(permutation: sp.Matrix) -> sp.Matrix:
    # Edge order (23),(13),(12) is complementary to vertex order 1,2,3.
    units = []
    for row, column in [(1, 2), (0, 2), (0, 1)]:
        atom = sp.zeros(3)
        atom[row, column] = atom[column, row] = 1 / sp.sqrt(2)
        units.append(atom)
    columns = []
    for atom in units:
        transformed = permutation * atom * permutation.T
        columns.append(
            sp.Matrix([sp.trace(reference.T * transformed) for reference in units])
        )
    return sp.Matrix.hstack(*columns)


def symmetric_commutant_basis(
    actions: list[sp.Matrix], extra_commutants: list[sp.Matrix]
) -> list[sp.Matrix]:
    dimension = actions[0].rows
    variables = sp.symbols(f"h0:{dimension * (dimension + 1) // 2}")
    matrix = sp.zeros(dimension)
    cursor = 0
    for row in range(dimension):
        for column in range(row, dimension):
            matrix[row, column] = variables[cursor]
            matrix[column, row] = variables[cursor]
            cursor += 1

    equations = []
    for action in actions + extra_commutants:
        equations.extend(list(action * matrix - matrix * action))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    nullspace = coefficient_matrix.nullspace()
    return [sp.simplify(matrix.subs(dict(zip(variables, vector)))) for vector in nullspace]


def matrix_span_rank(matrices: list[sp.Matrix]) -> int:
    return sp.Matrix.hstack(*[matrix.reshape(matrix.rows * matrix.cols, 1) for matrix in matrices]).rank()


def main() -> None:
    spectral_symbol = load(SPECTRAL_SYMBOL)
    rootstack = load(ROOTSTACK)
    a107 = load(A107)
    chern_orbit = load(CHERN_ORBIT)
    single_branch = load(SINGLE_BRANCH_NOGO)
    complex_gate = load(COMPLEX_NESTING_GATE)

    permutations = list(itertools.permutations(range(3)))
    vertex_actions = [permutation_matrix(perm) for perm in permutations]
    edge_actions = [edge_action(action) for action in vertex_actions]
    complement_intertwines = all(
        vertex == edge for vertex, edge in zip(vertex_actions, edge_actions)
    )

    strain_actions = [sp.diag(vertex, edge) for vertex, edge in zip(vertex_actions, edge_actions)]
    identity3 = sp.eye(3)
    zero3 = sp.zeros(3)
    quarter_turn = sp.BlockMatrix(
        [[zero3, -identity3], [identity3, zero3]]
    ).as_explicit()
    exchange = sp.BlockMatrix(
        [[zero3, identity3], [identity3, zero3]]
    ).as_explicit()

    no_extra_basis = symmetric_commutant_basis(strain_actions, [])
    exchange_basis = symmetric_commutant_basis(strain_actions, [exchange])
    quarter_turn_basis = symmetric_commutant_basis(strain_actions, [quarter_turn])

    ones = sp.ones(3, 3)
    projector_trivial = ones / 3
    projector_standard = identity3 - projector_trivial
    expected_quarter_turn_basis = [
        sp.diag(projector_trivial, projector_trivial),
        sp.diag(projector_standard, projector_standard),
    ]
    combined_rank = matrix_span_rank(quarter_turn_basis + expected_quarter_turn_basis)

    kappa_trivial, kappa_standard = sp.symbols(
        "kappa_trivial kappa_standard", real=True
    )
    scalarized_hessian = (
        kappa_trivial * expected_quarter_turn_basis[0]
        + kappa_standard * expected_quarter_turn_basis[1]
    )
    off_diagonal_lane_block = scalarized_hessian[:3, 3:]
    diagonal_lane_difference = sp.simplify(
        scalarized_hessian[:3, :3] - scalarized_hessian[3:, 3:]
    )

    cern_j = sp.Matrix(chern_orbit["generator"]["J"])
    cern_j6 = sp.kronecker_product(cern_j, identity3)

    checks = {
        "spectral_sheet_symbol_bridge_is_available": spectral_symbol["claim_tiers"][
            "spectral_sheet_symbol_to_q79_rootstack_strain_carrier"
        ]
        == "CLOSED_EXACT",
        "unique_positive_complement_map_is_available": rootstack["finite_data"][
            "equivariant_atom_bijection_count"
        ]
        == 1,
        "complement_edge_action_equals_sheet_action": complement_intertwines,
        "lane_quarterturn_is_orthogonal": quarter_turn.T * quarter_turn == sp.eye(6),
        "lane_quarterturn_squares_to_minus_identity": quarter_turn**2 == -sp.eye(6),
        "lane_quarterturn_commutes_with_S3": all(
            action * quarter_turn == quarter_turn * action for action in strain_actions
        ),
        "unconstrained_self_adjoint_S3_commutant_dimension_is_6": len(no_extra_basis)
        == 6,
        "exchange_only_commutant_dimension_is_4": len(exchange_basis) == 4,
        "quarterturn_invariant_commutant_dimension_is_2": len(quarter_turn_basis)
        == 2,
        "quarterturn_commutant_is_exactly_trivial_and_standard_scalars": combined_rank
        == 2,
        "quarterturn_forces_zero_lane_mixing": off_diagonal_lane_block == sp.zeros(3),
        "quarterturn_forces_equal_lane_blocks": diagonal_lane_difference == sp.zeros(3),
        "FuYau_Chern_orbit_uses_same_abstract_quarterturn_matrix": cern_j6
        == quarter_turn,
        "single_FuYau_branch_has_order4_no_go": single_branch["theorem"]["proved"]
        is True
        and single_branch["status"]
        == "EXACT_SINGLE_BRANCH_ORDER4_STABILIZER_NOGO_CLOSED",
        "minimal_FuYau_parent_orbit_has_length_4": chern_orbit["orbit_length"] == 4
        and chern_orbit["generator"]["order"] == 4,
        "A107_does_not_strictly_select_tau_i": a107["results"][
            "tau_i_strictly_selected"
        ]
        is False,
        "typed_lane_to_FuYau_source_bridge_is_open": complex_gate[
            "corpus_support"
        ]["global_FuYau_Chern_orbit_action_derived"]
        is False
        and complex_gate["U9_retarded_import"]["typed_map_to_Z4_Chern_orbit"]
        is False,
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"failed checks: {failed}")

    certificate = {
        "certificate": "q79_complement_quarterturn_hessian_scalarization",
        "date": "2026-07-15",
        "program": "MTT protospinor GR response proof",
        "status": "Q79_COMPLEMENT_QUARTERTURN_HESSIAN_SCALARIZATION_CLOSED_CONDITIONAL_LANE_TO_FUYAU_Z4_SOURCE_FUNCTOR_AND_ACTUAL_HYM_EXISTENCE_OPEN",
        "inputs": {
            "spectral_symbol_bridge": str(SPECTRAL_SYMBOL),
            "rootstack_bridge": str(ROOTSTACK),
            "A107": str(A107),
            "FuYau_Z4_Chern_orbit": str(CHERN_ORBIT),
            "single_branch_order4_no_go": str(SINGLE_BRANCH_NOGO),
            "complex_nesting_source_gate": str(COMPLEX_NESTING_GATE),
        },
        "finite_data": {
            "lane_quarterturn": [[int(value) for value in row] for row in quarter_turn.tolist()],
            "FuYau_Chern_pair_quarterturn": chern_orbit["generator"]["J"],
            "single_branch_self_adjoint_S3_commutant_dimension": len(no_extra_basis),
            "exchange_invariant_self_adjoint_commutant_dimension": len(exchange_basis),
            "quarterturn_invariant_self_adjoint_commutant_dimension": len(
                quarter_turn_basis
            ),
            "scalarized_Hessian_formula": "H=kappa_trivial*(P1 direct_sum P1)+kappa_standard*(Pstd direct_sum Pstd)",
            "physical_TT_block": "H_std=kappa_standard*I2",
            "physical_TT_conditions": [
                "h_DE=0",
                "h_DD=h_EE=kappa_standard",
                "kappa_standard>0 under strict HYM stability",
            ],
            "minimal_FuYau_Chern_orbit": chern_orbit["orbit"],
        },
        "theorem": {
            "name": "q79ComplementQuarterTurnHessianScalarization",
            "canonical_complex_structure": {
                "complement_map": "The unique S3-equivariant positive sheet-to-opposite-edge isometry C identifies the two permutation carriers.",
                "definition": "J_DE(d,e)=(-C^{-1}e,Cd)",
                "properties": "J_DE is orthogonal, J_DE^2=-I, and it commutes with S3.",
                "parameter_count": 0,
            },
            "scalarization": {
                "hypotheses": "H is real self-adjoint, S3-equivariant, and commutes with J_DE.",
                "conclusion": "H=kappa_trivial on both trivial copies and kappa_standard on both standard copies, with no diagonal-edge mixing.",
                "TT_conclusion": "On the physical standard multiplicity plane H_std=kappa_standard I2, so h_DE=0 and h_DD=h_EE; positivity gives kappa_standard>0.",
                "exchange_only_is_insufficient": "Commutation with the lane exchange alone leaves four coefficients and allows a nonzero mixing entry. The order-four complex structure is the sharp symmetry.",
            },
            "FuYau_relation": {
                "representation_level": "The A107 Fu-Yau Chern-pair generator is the same abstract order-four matrix [[0,-1],[1,0]] on a two-copy multiplicity space.",
                "single_branch": "A single rank-one Chern pair has no order-four stabilizer, so it cannot supply this symmetry.",
                "minimal_parent": "The exact minimal parent is the four-element Chern orbit (delta,0),(0,delta),(-delta,0),(0,-delta).",
                "open_functor": "The current corpus does not identify the Chern-pair multiplicity plane with the diagonal/edge strain multiplicity plane on the same carrier, nor prove the selected HYM action commutes with that quarter-turn.",
            },
            "closing_routes": [
                "Prove LensQuarterTurnToFuYauChernOrbitSourceTheorem together with its induced action on the spectral sheet-symbol multiplicity plane and HYM functional.",
                "Or compute the actual projected HYM 2x2 block directly and verify the two scalarization equations without quarter-turn selection.",
            ],
        },
        "claim_tiers": {
            "canonical_q79_complement_lane_complex_structure": "CLOSED_EXACT",
            "self_adjoint_S3_quarterturn_Hessian_scalarization": "CLOSED_EXACT",
            "physical_TT_block_scalarization": "CLOSED_CONDITIONAL_ON_SELECTED_QUARTERTURN_INVARIANCE",
            "single_rank_one_FuYau_branch_supplies_order4_symmetry": "CLOSED_NO_GO",
            "minimal_four_branch_FuYau_Chern_orbit": "CLOSED_EXACT",
            "abstract_Z4_representation_match": "CLOSED_EXACT",
            "typed_lane_quarterturn_to_FuYau_Chern_orbit_source_functor": "OPEN",
            "selected_HYM_action_is_quarterturn_invariant": "OPEN",
            "actual_inverse_Fourier_Mukai_HYM_bundle": "OPEN",
            "numeric_kappa_standard": "OPEN",
        },
        "guardrails": {
            "claims_abstract_Z4_match_is_same_carrier_source_theorem": False,
            "claims_single_FuYau_branch_has_quarterturn_symmetry": False,
            "claims_shared_central_U1_is_lane_quarterturn": False,
            "claims_actual_HYM_Hessian_computed": False,
            "adds_fitted_numeric_parameter": False,
            "uses_observed_physics_data": False,
        },
        "checks": checks,
        "note_written": str(OUT_NOTE),
    }
    OUT_CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# q79 Complement Quarter-Turn Hessian Scalarization Theorem v1

Status:
`{certificate['status']}`

## Result

The two still-free equalities in the projected HYM/TT block have an exact
symmetry solution. It is conditional on one sharply identified same-carrier
source theorem, not on a numerical fit.

## Canonical lane quarter-turn

The unique positive `S3`-equivariant complement map sends each sheet atom to
its opposite unordered edge. In the ordered bases

```text
vertices: (1,2,3),
edges:    (23,13,12),
```

its matrix is the identity. On the two-copy strain carrier define

```text
J_DE(d,e)=(-e,d),
J_DE=[[0,-I3],[I3,0]].
```

The exact calculation gives

```text
J_DE^T J_DE=I6,
J_DE^2=-I6,
[J_DE,rho(sigma)]=0 for every sigma in S3.
```

This is a parameter-free orthogonal complex structure on the diagonal/edge
multiplicity plane. It is not automatically the common central circle: that
central phase cancels in endomorphism conjugation, whereas `J_DE` exchanges
the two strain copies.

## Hessian scalarization

Before the quarter-turn is imposed, a self-adjoint `S3`-equivariant operator on

```text
W=2*trivial direct-sum 2*standard
```

has six real coefficients. Lane exchange alone leaves four and still permits
diagonal-edge mixing. Requiring commutation with `J_DE` leaves exactly two:

```text
H=kappa_trivial*(P1 direct-sum P1)
 +kappa_standard*(Pstd direct-sum Pstd).
```

Therefore the physical standard-isotypic multiplicity block is

```text
H_std=kappa_standard*I2,
h_DE=0,
h_DD=h_EE=kappa_standard.
```

Strict stability gives `kappa_standard>0`. Thus quarter-turn invariance proves
exactly the two equations isolated by the spectral sheet-symbol theorem. The
numerical value of `kappa_standard` remains the one action normalization, not a
new dimensionless matrix parameter.

## Fu-Yau comparison

A107 independently computes the same abstract order-four matrix on the Fu-Yau
Chern pair:

```text
J_T2=[[0,-1],[1,0]].
```

It also proves a decisive global distinction. The single branch `(delta,0)`
has a parabolic stabilizer and no order-four symmetry. Its unique minimal
quarter-turn completion is

```text
(delta,0) -> (0,delta) -> (-delta,0) -> (0,-delta).
```

The four branches have equal curvature cost and Bianchi allocation, and the
square-fiber quarter-turn conditionally selects `tau=i`. This is the correct
superset lane.

The representation-level matrices now agree exactly, but the same-carrier
functor is still open. The corpus has not proved that the Fu-Yau Chern-pair
multiplicity plane acts as `J_DE` on the diagonal/edge spectral strain symbol,
nor that the selected HYM functional is invariant under it. Calling the two
quarter-turns identical before that theorem would be a cross-source shortcut.

## Sharp closing theorem

The remaining symmetry route is:

```text
LensQuarterTurnToFuYauChernOrbitSourceTheorem
  + induced action on the spectral sheet-symbol multiplicity plane
  + invariance of the selected HYM functional
  => [H_std,J_DE]=0
  => H_std=kappa_standard I2.
```

The direct alternative is to construct the actual inverse Fourier-Mukai/HYM
bundle and calculate the `2x2` block, then verify the same two equations.

## Scope

Closed here:

```text
canonical complement lane complex structure,
exact S3 plus quarter-turn Hessian commutant,
conditional TT block scalarization,
single-branch order-four no-go,
minimal four-branch Fu-Yau parent,
abstract Z4 representation match.
```

Still open:

```text
typed lane-quarter-turn/Fu-Yau same-carrier functor,
selected HYM action invariance under that quarter-turn,
gerbe branch and inverse Fourier-Mukai/HYM existence,
numeric kappa_standard and primitive Lorentzian branch selection.
```

No observed value and no fitted parameter enters this theorem.
"""
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {certificate['status']}")


if __name__ == "__main__":
    main()
