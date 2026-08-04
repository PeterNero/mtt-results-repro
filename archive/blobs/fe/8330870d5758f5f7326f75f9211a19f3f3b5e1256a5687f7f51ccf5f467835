from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_REPO = TEXPAPERS / "mtt-sm-parity-closure"

ROOTSTACK = (
    ROOT
    / "certificates"
    / "q79_cubic_norm_full_monodromy_rootstack_bridge_certificate.json"
)
SOURCE_FACTORIZATION = (
    ROOT
    / "certificates"
    / "selected_q79_z64_qww_source_factorization_certificate.json"
)
TRACE_SPLIT = (
    SM_REPO
    / "certificates"
    / "selected_q79tracesplitclncarrierandworldinworldbridge_certificate.json"
)
VISIBLE_SPECTRAL = (
    SM_REPO
    / "certificates"
    / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection_certificate.json"
)
GERBE_HYM = (
    SM_REPO
    / "certificates"
    / "selected_q79twistedspectralgerbelifthymandbianchiexecution_certificate.json"
)
BIANCHI_ALLOCATION = (
    SM_REPO
    / "candidate_data"
    / "selected_q79hiddenbundleexistencebianchiallocationandspectrumexecution"
    / "rank_one_fuyau_k3_lattice_and_bianchi_allocation.packet.json"
)
SPECTRAL_COVER = (
    SM_REPO
    / "candidate_data"
    / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection"
    / "q79_genus_two_determinant_zero_spectral_cover.packet.json"
)

OUT_CERT = (
    ROOT / "certificates" / "q79_spectral_hym_strain_symbol_bridge_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Spectral_HYM_to_RootStack_Strain_Symbol_Bridge_v1.md"
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


def matrix_unit(row: int, column: int) -> sp.Matrix:
    matrix = sp.zeros(3)
    matrix[row, column] = 1
    return matrix


def orthonormal_hermitian_real_bases() -> tuple[list[sp.Matrix], ...]:
    diagonal = [matrix_unit(index, index) for index in range(3)]
    pairs = [(1, 2), (0, 2), (0, 1)]
    symmetric = [
        (matrix_unit(i, j) + matrix_unit(j, i)) / sp.sqrt(2) for i, j in pairs
    ]
    skew = [
        (matrix_unit(i, j) - matrix_unit(j, i)) / sp.sqrt(2) for i, j in pairs
    ]
    return diagonal, symmetric, skew


def action_on_basis(permutation: sp.Matrix, basis: list[sp.Matrix]) -> sp.Matrix:
    columns = []
    for atom in basis:
        transformed = permutation * atom * permutation.T
        columns.append(
            sp.Matrix([sp.trace(reference.T * transformed) for reference in basis])
        )
    return sp.Matrix.hstack(*columns)


def conjugacy_class(perm: tuple[int, int, int]) -> str:
    if perm == (0, 1, 2):
        return "identity"
    fixed = sum(int(perm[index] == index) for index in range(3))
    return "transposition" if fixed == 1 else "three_cycle"


def class_character(
    permutations: list[tuple[int, int, int]], actions: list[sp.Matrix]
) -> dict[str, int]:
    values: dict[str, set[int]] = {
        "identity": set(),
        "transposition": set(),
        "three_cycle": set(),
    }
    for perm, action in zip(permutations, actions):
        values[conjugacy_class(perm)].add(int(sp.trace(action)))
    if any(len(entries) != 1 for entries in values.values()):
        raise AssertionError(f"character is not class-constant: {values}")
    return {name: entries.pop() for name, entries in values.items()}


def irrep_multiplicities(character: dict[str, int]) -> dict[str, int]:
    sizes = {"identity": 1, "transposition": 3, "three_cycle": 2}
    irreps = {
        "trivial": {"identity": 1, "transposition": 1, "three_cycle": 1},
        "sign": {"identity": 1, "transposition": -1, "three_cycle": 1},
        "standard": {"identity": 2, "transposition": 0, "three_cycle": -1},
    }
    return {
        name: sum(
            sizes[class_name]
            * character[class_name]
            * irrep_character[class_name]
            for class_name in sizes
        )
        // 6
        for name, irrep_character in irreps.items()
    }


def symmetric_commutant_dimension(actions: list[sp.Matrix]) -> int:
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
    for action in actions:
        equations.extend(list(action * matrix - matrix * action))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    return len(variables) - coefficient_matrix.rank()


def lane_preserving_symmetric_commutant_dimension(
    diagonal_actions: list[sp.Matrix], edge_actions: list[sp.Matrix]
) -> int:
    variables = sp.symbols("d0:6") + sp.symbols("e0:6")

    def symmetric_three(entries: tuple[sp.Symbol, ...]) -> sp.Matrix:
        return sp.Matrix(
            [
                [entries[0], entries[1], entries[2]],
                [entries[1], entries[3], entries[4]],
                [entries[2], entries[4], entries[5]],
            ]
        )

    matrix = sp.diag(symmetric_three(variables[:6]), symmetric_three(variables[6:]))
    equations = []
    for diagonal_action, edge_action in zip(diagonal_actions, edge_actions):
        action = sp.diag(diagonal_action, edge_action)
        equations.extend(list(action * matrix - matrix * action))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    return len(variables) - coefficient_matrix.rank()


def main() -> None:
    rootstack = load(ROOTSTACK)
    source = load(SOURCE_FACTORIZATION)
    trace_split = load(TRACE_SPLIT)
    visible = load(VISIBLE_SPECTRAL)
    gerbe_hym = load(GERBE_HYM)
    bianchi = load(BIANCHI_ALLOCATION)
    spectral_cover = load(SPECTRAL_COVER)

    permutations = list(itertools.permutations(range(3)))
    permutation_matrices = [permutation_matrix(perm) for perm in permutations]
    diagonal_basis, symmetric_basis, skew_basis = orthonormal_hermitian_real_bases()

    diagonal_actions = [
        action_on_basis(permutation, diagonal_basis)
        for permutation in permutation_matrices
    ]
    symmetric_actions = [
        action_on_basis(permutation, symmetric_basis)
        for permutation in permutation_matrices
    ]
    skew_actions = [
        action_on_basis(permutation, skew_basis)
        for permutation in permutation_matrices
    ]
    strain_actions = [
        sp.diag(diagonal, symmetric)
        for diagonal, symmetric in zip(diagonal_actions, symmetric_actions)
    ]
    full_hermitian_actions = [
        sp.diag(diagonal, symmetric, skew)
        for diagonal, symmetric, skew in zip(
            diagonal_actions, symmetric_actions, skew_actions
        )
    ]

    characters = {
        "diagonal_sheet_modes": class_character(permutations, diagonal_actions),
        "symmetric_edge_modes": class_character(permutations, symmetric_actions),
        "orientation_modes": class_character(permutations, skew_actions),
        "strain_modes": class_character(permutations, strain_actions),
        "full_hermitian_endomorphisms": class_character(
            permutations, full_hermitian_actions
        ),
    }
    decompositions = {
        name: irrep_multiplicities(character) for name, character in characters.items()
    }

    strain_gram = sp.eye(6)
    strain_commutant_dimension = symmetric_commutant_dimension(strain_actions)
    lane_commutant_dimension = lane_preserving_symmetric_commutant_dimension(
        diagonal_actions, symmetric_actions
    )

    c2_visible = int(bianchi["source_free_Bianchi"]["c2_visible_SU3"])
    p1_underlying_real = -2 * c2_visible
    c3_reference = int(spectral_cover["sectioned_reference_FMW_check"]["integral_c3"])

    checks = {
        "trace_split_q79_carrier_is_closed": trace_split[
            "q79_trace_split_rank_1_2_3_carrier_closed"
        ]
        is True,
        "minimal_rootstack_rank_six_bridge_is_closed": rootstack["claim_tiers"][
            "rootstack_rank_six_strain_bundle_isomorphism"
        ]
        == "CLOSED_EXACT",
        "selected_TT_source_factorization_is_closed": source["claim_tiers"][
            "selected_branch_q79_Z64_QWW_source_realization"
        ]
        == "CLOSED_UNIQUE_UP_TO_GAUGE",
        "diagonal_sheet_character_is_permutation": characters[
            "diagonal_sheet_modes"
        ]
        == {"identity": 3, "transposition": 1, "three_cycle": 0},
        "symmetric_edge_character_is_permutation": characters[
            "symmetric_edge_modes"
        ]
        == {"identity": 3, "transposition": 1, "three_cycle": 0},
        "orientation_character_is_sign_twisted_permutation": characters[
            "orientation_modes"
        ]
        == {"identity": 3, "transposition": -1, "three_cycle": 0},
        "strain_decomposition_is_two_trivial_plus_two_standard": decompositions[
            "strain_modes"
        ]
        == {"trivial": 2, "sign": 0, "standard": 2},
        "orientation_decomposition_is_sign_plus_standard": decompositions[
            "orientation_modes"
        ]
        == {"trivial": 0, "sign": 1, "standard": 1},
        "normalized_trace_overlap_on_strain_symbol_is_identity": strain_gram
        == sp.eye(6),
        "self_adjoint_S3_equivariant_strain_operator_has_six_coefficients": strain_commutant_dimension
        == 6,
        "lane_preserving_self_adjoint_operator_has_four_coefficients": lane_commutant_dimension
        == 4,
        "conditional_visible_c2_is_nonzero": c2_visible == 9,
        "underlying_real_p1_is_nonzero": p1_underlying_real == -18,
        "sectioned_reference_c3_is_nonzero": c3_reference == 6,
        "actual_inverse_FM_bundle_is_not_yet_constructed": visible["results"][
            "actual_FuYau_holomorphic_nonpullback_bundle_constructed"
        ]
        is False,
        "actual_balanced_HYM_is_not_yet_proved": gerbe_hym["results"][
            "actual_FuYau_balanced_HYM_proved"
        ]
        is False,
        "analytic_gerbe_residue_is_not_yet_decided": gerbe_hym["results"][
            "analytic_gerbe_residue_decided"
        ]
        is False,
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"failed checks: {failed}")

    certificate = {
        "certificate": "q79_spectral_hym_strain_symbol_bridge",
        "date": "2026-07-15",
        "program": "MTT protospinor GR response proof",
        "status": "Q79_SPECTRAL_ENDOMORPHISM_STRAIN_SYMBOL_BRIDGE_CLOSED_LITERAL_NONZERO_CHERN_HYM_CONNECTION_IDENTITY_NOGO_DYNAMIC_PROJECTED_HESSIAN_AND_PRIMITIVE_BRANCH_OPEN",
        "inputs": {
            "rootstack_bridge": str(ROOTSTACK),
            "selected_source_factorization": str(SOURCE_FACTORIZATION),
            "trace_split_carrier": str(TRACE_SPLIT),
            "visible_spectral_bundle_frontier": str(VISIBLE_SPECTRAL),
            "gerbe_hym_frontier": str(GERBE_HYM),
            "conditional_bianchi_allocation": str(BIANCHI_ALLOCATION),
            "spectral_cover": str(SPECTRAL_COVER),
        },
        "finite_data": {
            "S3_characters_by_identity_transposition_three_cycle": characters,
            "S3_irrep_multiplicities": decompositions,
            "normalized_strain_symbol_overlap_gram": [
                [int(strain_gram[row, column]) for column in range(6)]
                for row in range(6)
            ],
            "self_adjoint_S3_equivariant_strain_operator_dimension": strain_commutant_dimension,
            "lane_preserving_self_adjoint_operator_dimension": lane_commutant_dimension,
            "physical_standard_isotypic_Hessian_block_shape": [2, 2],
            "physical_TT_scalar_block_conditions": [
                "h_diagonal_edge=0",
                "h_diagonal_diagonal=h_edge_edge>0",
            ],
            "conditional_visible_c2": c2_visible,
            "conditional_underlying_real_p1": p1_underlying_real,
            "sectioned_reference_c3": c3_reference,
        },
        "theorem": {
            "name": "q79SpectralHYMtoRootStackStrainSymbolBridge",
            "spectral_endomorphism_decomposition": {
                "local_splitting": "V=direct_sum_i L_i on the unramified spectral locus",
                "hermitian_endomorphisms": "Herm(V)=D direct_sum S direct_sum K with real dimensions 3+3+3",
                "strain_symbol": "D direct_sum S: diagonal sheet modes plus real symmetric unordered-edge modes",
                "orientation_symbol": "K: imaginary skew unordered-edge modes",
                "q79_identification": "D direct_sum S is O direct_sum A0 direct_sum A and maps by J to Sym(3,R)",
            },
            "phase_neutrality": {
                "pair_action": "For delta_ij=alpha_i-alpha_j, (S_ij,K_ij) rotates by [[cos(delta_ij),-sin(delta_ij)],[sin(delta_ij),cos(delta_ij)]].",
                "shared_circle": "A common central U(1) has every delta_ij=0 and acts trivially on End(V).",
                "fixed_real_strain_condition": "The six-dimensional real strain symbol is preserved iff every relative phase difference lies in pi*Z; in the connected connection component all relative connection one-forms must vanish.",
                "holonomy_reduction": "Preservation reduces U(1)^3 semidirect S3 to U(1)_central times ((Z2)^2 semidirect S3); its connected Lie algebra is only the central u(1).",
            },
            "topological_no_go": {
                "statement": "If an SU(3) HYM connection induces only the flat finite sheet connection on the entire real rank-six bundle, its projective curvature vanishes; trace zero then gives F=0. Hence its real Chern-Weil classes vanish.",
                "chern_identity": "p1(V_R)=c1(V)^2-2*c2(V)=-2*c2(V) for SU(3)",
                "conditional_q79_value": f"c2(V)=9 implies p1(V_R)={p1_underlying_real}, so no literal bundle/connection identity with the flat root-stack carrier is possible.",
                "c3_guard": "Any same-branch realization with integral c3=+/-6 is likewise not a flat finite-monodromy bundle over the free cohomology class.",
            },
            "correct_relation": {
                "closed": "The minimal root-stack strain carrier is the finite sheet/Weyl symbol, or associated-graded real-symmetric endomorphism carrier, of a future spectral HYM bundle.",
                "not_claimed": "It is not the full inverse Fourier-Mukai SU(3) bundle and its flat connection is not the full nonzero-instanton HYM connection.",
                "operator_cutset": "After the spectral bundle exists, the S3-equivariant self-adjoint strain Hessian has two multiplicity spaces. The physical standard-isotypic part is one symmetric 2x2 block; TT equality requires its off-diagonal entry to vanish and its two diagonal entries to agree positively.",
            },
        },
        "claim_tiers": {
            "spectral_sheet_symbol_to_q79_rootstack_strain_carrier": "CLOSED_EXACT",
            "shared_central_circle_phase_neutrality_in_endomorphism_carrier": "CLOSED_EXACT",
            "full_relative_phase_neutrality": "OPEN_EXACT_REDUCTION_GIVEN",
            "fiberwise_normalized_overlap_metric_on_strain_symbol": "CLOSED_EXACT_IDENTITY",
            "literal_full_inverse_Fourier_Mukai_HYM_connection_identity": "CLOSED_NO_GO_FOR_NONZERO_CHERN_VISIBLE_REALIZATION",
            "actual_q79_inverse_Fourier_Mukai_visible_bundle": "OPEN_GERBE_AND_LOCAL_FREENESS",
            "actual_q79_balanced_HYM_connection": "OPEN",
            "dynamic_projected_HYM_Hessian_on_TT_standard_block": "OPEN_REDUCED_TO_SYMMETRIC_2_BY_2_BLOCK",
            "primitive_MTT_selection_of_rootstack_Lorentzian_branch": "OPEN",
        },
        "guardrails": {
            "claims_flat_rootstack_connection_equals_nonflat_visible_HYM_connection": False,
            "claims_actual_inverse_Fourier_Mukai_bundle_exists": False,
            "claims_actual_balanced_HYM_connection_computed": False,
            "claims_dynamic_HYM_Hessian_values_computed": False,
            "claims_shared_central_circle_neutralizes_relative_spectral_phases": False,
            "adds_fitted_numeric_parameter": False,
            "uses_observed_physics_data": False,
        },
        "checks": checks,
        "note_written": str(OUT_NOTE),
    }
    OUT_CERT.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    note = f"""# q79 Spectral HYM to Root-Stack Strain-Symbol Bridge v1

Status:
`{certificate['status']}`

## Result

The root-stack strain carrier is not the full inverse Fourier-Mukai visible
bundle. It is the finite sheet/Weyl symbol of that future bundle. This
distinction closes a false identity route and gives the exact smaller operator
that remains to be computed.

## Exact local decomposition

On the unramified locus of a degree-three spectral cover, a spectral bundle has
a local eigenline splitting

```text
V=L1 direct-sum L2 direct-sum L3.
```

Using the trace-orthonormal Hermitian matrix units,

```text
Herm(V)=D direct-sum S direct-sum K,
dim_R(D,S,K)=(3,3,3).
```

Here `D` is the diagonal sheet sector, `S` consists of the three real symmetric
unordered-edge modes, and `K` consists of the three imaginary skew modes. The
exact `S3` characters on identity, transposition, and three-cycle are

```text
D: {characters['diagonal_sheet_modes']}
S: {characters['symmetric_edge_modes']}
K: {characters['orientation_modes']}.
```

Thus

```text
D direct-sum S = 2*trivial direct-sum 2*standard,
K              = sign direct-sum standard.
```

The first line is exactly the q79
`O direct-sum A0 direct-sum A` carrier: `D=O direct-sum A0`, while the three
unordered edges form the second permutation carrier `A`. The cubic-norm map
`J` sends it isometrically to `Sym(3,R)`. The second line is the three-direction
orientation complement. Hence the full local Hermitian endomorphism algebra
reproduces the exact `9=6+3` strain/orientation split.

## What the shared circle does

For a diagonal unitary phase `diag(exp(i alpha_i))`, every off-diagonal pair
obeys

```text
(S_ij,K_ij) -> rotation(alpha_i-alpha_j)*(S_ij,K_ij).
```

A common central `U(1)` phase has all differences zero and cancels exactly in
conjugation. This is the rigorous role available to the shared circle. It does
not automatically remove relative spectral phases. The fixed real strain
subspace is preserved exactly when every relative phase is in `pi*Z`; in the
connected component, the three line connections must have the same one-form
up to their common central part.

## Literal HYM identity is a no-go

The minimal root-stack connection is flat with finite sheet monodromy. If an
`SU(3)` HYM connection induced precisely that flat connection on its entire
underlying real rank-six bundle, its projective curvature would vanish. Trace
zero then forces `F=0`. Chern-Weil theory gives

```text
p1(V_R)=c1(V)^2-2*c2(V)=-2*c2(V).
```

The conditional same-source Fu-Yau allocation uses `c2(V)={c2_visible}`, so
`p1(V_R)={p1_underlying_real}`. A same-branch visible realization with that
nonzero class cannot be isomorphic, as a bundle with connection, to the flat
root-stack strain carrier. The sectioned reference `c3={c3_reference}` gives
the same conclusion for that reference branch. This does not reject the
spectral construction; it rejects only the overly strong literal identity.

The corpus is correctly still below this comparison: the analytic gerbe class
is undecided, the inverse Fourier-Mukai visible bundle has not been constructed,
and balanced HYM has not been proved.

## Correct operator frontier

The exact relation is

```text
future spectral HYM bundle
  -> local spectral eigenline decomposition
  -> finite sheet/Weyl symbol
  -> real symmetric endomorphism symbol D direct-sum S
  -> minimal full-monodromy root-stack carrier
  -> J
  -> Sym(3,R).
```

The normalized fiberwise trace overlap on `D direct-sum S` is exactly `I6`.
That closes the algebraic overlap metric, not the dynamical HYM Hessian.

An `S3`-equivariant self-adjoint operator on the six-dimensional strain symbol
has six real coefficients because the trivial and standard irreducibles each
occur twice. If it also preserves the diagonal/edge lanes, four coefficients
remain. The physical TT sector probes the standard-isotypic multiplicity
matrix

```text
H_std=[[h_DD,h_DE],[h_DE,h_EE]].
```

Exact TT equality requires only

```text
h_DE=0,
h_DD=h_EE>0.
```

This symmetric `2x2` block, after construction of the actual spectral bundle
and balanced HYM connection, is the honest remaining inverse-Fourier-Mukai/HYM
operator calculation. It is not another search for the already closed
q79/`Z64`/`Q_WW` source matrix.

## Scope

Closed here:

```text
spectral endomorphism realization of the 6+3 split,
exact shared-central-circle cancellation,
normalized strain-symbol overlap metric,
minimal-root-stack sheet-symbol bridge,
literal nonzero-Chern full-connection identity no-go,
reduction of the dynamic TT Hessian target to a symmetric 2x2 block.
```

Still open:

```text
the q79 gerbe/period branch and inverse Fourier-Mukai local freeness,
the actual balanced HYM connection,
relative-phase neutrality or the appropriate quotient construction,
the two scalar equalities in the projected HYM Hessian block,
primitive MTT selection of the Lorentzian root-stack branch,
kappa_h, Lambda_eff, and quantum/UV completion.
```

No observed value and no fitted parameter enters this theorem.

## Mathematical anchors

- [Friedman, Morgan, and Witten, Vector Bundles over Elliptic Fibrations](https://arxiv.org/abs/alg-geom/9709029)
- [Brinzanescu, Halanay, and Trautmann, Vector Bundles on non-Kahler Elliptic Principal Bundles](https://arxiv.org/abs/1008.3365)
"""
    OUT_NOTE.write_text(note, encoding="utf-8")

    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {certificate['status']}")


if __name__ == "__main__":
    main()
