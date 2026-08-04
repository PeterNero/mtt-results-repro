from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_REPO = TEXPAPERS / "mtt-sm-parity-closure"

SQUARE_SPECTRAL_SURFACE = (
    SM_REPO
    / "candidate_data"
    / "selected_q79explicitmodelrelativedelignegerbezeroornogoexecution"
    / "square_elliptic_identity_alignment_spectral_surface.packet.json"
)
SPECTRAL_SYMBOL = (
    ROOT / "certificates" / "q79_spectral_hym_strain_symbol_bridge_certificate.json"
)
QUARTERTURN_HESSIAN = (
    ROOT
    / "certificates"
    / "q79_complement_quarterturn_hessian_scalarization_certificate.json"
)
PARENT_DESCENT = (
    ROOT
    / "certificates"
    / "q79_shared_z64_fuyau_parent_quarterturn_descent_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_square_theta_quarterturn_strain_nogo_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Square_Theta_QuarterTurn_to_Strain_DirectFunctor_NoGo_v1.md"
)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def hermitian_basis() -> tuple[list[str], list[sp.Matrix]]:
    names: list[str] = []
    basis: list[sp.Matrix] = []
    for index in range(3):
        atom = sp.zeros(3)
        atom[index, index] = 1
        names.append(f"D{index + 1}")
        basis.append(atom)

    # Opposite-edge order (23),(13),(12), matching the q79 complement theorem.
    pairs = [(1, 2), (0, 2), (0, 1)]
    for first, second in pairs:
        atom = sp.zeros(3)
        atom[first, second] = atom[second, first] = 1 / sp.sqrt(2)
        names.append(f"S{first + 1}{second + 1}")
        basis.append(atom)
    for first, second in pairs:
        atom = sp.zeros(3)
        atom[first, second] = sp.I / sp.sqrt(2)
        atom[second, first] = -sp.I / sp.sqrt(2)
        names.append(f"K{first + 1}{second + 1}")
        basis.append(atom)
    return names, basis


def adjoint_real_matrix(unitary: sp.Matrix, basis: list[sp.Matrix]) -> sp.Matrix:
    columns = []
    for atom in basis:
        transformed = sp.simplify(unitary * atom * unitary.conjugate().T)
        coordinates = [
            sp.simplify(sp.trace(reference.conjugate().T * transformed))
            for reference in basis
        ]
        columns.append(sp.Matrix(coordinates))
    return sp.simplify(sp.Matrix.hstack(*columns))


def main() -> None:
    square_surface = load(SQUARE_SPECTRAL_SURFACE)
    spectral_symbol = load(SPECTRAL_SYMBOL)
    quarterturn_hessian = load(QUARTERTURN_HESSIAN)
    parent_descent = load(PARENT_DESCENT)

    a, b, c = sp.symbols("a b c")
    cubic = -a**3 + a * c**2 + b**2 * c
    transformed_cubic = sp.expand(cubic.subs({a: -a, b: sp.I * b}, simultaneous=True))

    # On H^0(E,O(3*0)) with the packet's basis (a,b,c), multiplication by i
    # on the square elliptic curve acts projectively by diag(-1,i,1).
    theta_action = sp.diag(-1, sp.I, 1)
    names, basis = hermitian_basis()
    adjoint = adjoint_real_matrix(theta_action, basis)

    strain_indices = list(range(6))
    orientation_indices = list(range(6, 9))
    strain_to_orientation = adjoint.extract(orientation_indices, strain_indices)
    strain_preserved = strain_to_orientation == sp.zeros(3, 6)

    square_minus_identity_kernel_dimension = 9 - (adjoint**2 + sp.eye(9)).rank()
    fixed_dimension = 9 - (adjoint - sp.eye(9)).rank()
    minus_dimension = 9 - (adjoint + sp.eye(9)).rank()
    trace_adjoint = sp.trace(adjoint)

    checks = {
        "packet_is_exact_square_elliptic_trial": (
            square_surface["elliptic_curve"]["analytic_modulus_up_to_SL2Z"]
            == "tau=i"
            and square_surface["elliptic_curve"]["degree_three_basis"]
            == ["a", "b", "c"]
            and square_surface["elliptic_curve"]["plane_cubic"]
            == "-a**3 + a*c**2 + b**2*c"
        ),
        "theta_quarterturn_preserves_cubic_projectively": transformed_cubic == -cubic,
        "theta_quarterturn_has_order4": theta_action**4 == sp.eye(3)
        and theta_action**2 != sp.eye(3),
        "Hermitian_basis_is_trace_orthonormal": all(
            sp.simplify(sp.trace(left.conjugate().T * right))
            == (1 if row == column else 0)
            for row, left in enumerate(basis)
            for column, right in enumerate(basis)
        ),
        "adjoint_action_is_real_orthogonal_order4": (
            all(value.is_real is not False for value in adjoint)
            and adjoint.T * adjoint == sp.eye(9)
            and adjoint**4 == sp.eye(9)
        ),
        "direct_theta_adjoint_does_not_preserve_q79_real_strain": not strain_preserved,
        "order4_rotation_sector_has_dimension4_not6": (
            square_minus_identity_kernel_dimension == 4
        ),
        "adjoint_real_eigenspace_inventory_is_3_plus2_plus4": (
            fixed_dimension == 3
            and minus_dimension == 2
            and square_minus_identity_kernel_dimension == 4
        ),
        "direct_theta_adjoint_cannot_restrict_to_JDE_on_six_dimensions": (
            square_minus_identity_kernel_dimension == 4
            and square_minus_identity_kernel_dimension < 6
        ),
        "spectral_symbol_DSK_split_is_available": spectral_symbol["theorem"][
            "spectral_endomorphism_decomposition"
        ]["hermitian_endomorphisms"]
        == "Herm(V)=D direct_sum S direct_sum K with real dimensions 3+3+3",
        "parent_theorem_did_not_claim_same_branch_invariance": parent_descent[
            "claim_tiers"
        ]["free_orbit_covariance_implies_single_branch_Hessian_invariance"]
        == "CLOSED_NO_GO",
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"failed checks: {failed}")

    certificate = {
        "certificate": "q79_square_theta_quarterturn_strain_nogo",
        "date": "2026-07-15",
        "program": "MTT protospinor GR response proof",
        "status": "Q79_SQUARE_THETA_DIRECT_ADJOINT_TO_STRAIN_QUARTERTURN_CLOSED_NOGO_NONTRIVIAL_INVERSE_FOURIER_MUKAI_FUNCTOR_OR_DIRECT_HYM_REQUIRED",
        "inputs": {
            "square_spectral_surface": str(SQUARE_SPECTRAL_SURFACE),
            "spectral_symbol_bridge": str(SPECTRAL_SYMBOL),
            "quarterturn_Hessian_scalarization": str(QUARTERTURN_HESSIAN),
            "shared_Z64_FuYau_parent_descent": str(PARENT_DESCENT),
        },
        "checks": checks,
        "finite_data": {
            "theta_basis": names[:3],
            "theta_quarterturn": [
                [str(sp.simplify(value)) for value in row]
                for row in theta_action.tolist()
            ],
            "Hermitian_basis_order": names,
            "adjoint_real_matrix": [
                [int(value) for value in row] for row in adjoint.tolist()
            ],
            "adjoint_trace": int(trace_adjoint),
            "adjoint_plus1_eigenspace_dimension": fixed_dimension,
            "adjoint_minus1_eigenspace_dimension": minus_dimension,
            "adjoint_J2_minus1_sector_dimension": square_minus_identity_kernel_dimension,
            "desired_JDE_sector_dimension": 6,
            "strain_to_orientation_block_rank": int(strain_to_orientation.rank()),
        },
        "theorem": {
            "name": "SquareThetaQuarterTurnToStrainDirectFunctorNoGo",
            "geometric_action": {
                "elliptic_curve": "b^2*c=a^3-a*c^2",
                "automorphism": "(a,b,c)->(-a,i*b,c)",
                "projective_residual": "P transforms to -P",
                "degree_three_matrix": "diag(-1,i,1)",
            },
            "adjoint_result": {
                "statement": (
                    "On Herm(3), the direct degree-three theta adjoint has real "
                    "eigenspace inventory +1:3, -1:2, and J^2=-1 rotation sector:4."
                ),
                "strain_failure": (
                    "It fixes D, flips one S/K edge plane by pi, and rotates two "
                    "S/K edge planes by quarter turns. Therefore D direct-sum S is "
                    "not invariant."
                ),
                "basis_independent_no_go": (
                    "The kernel of Ad(U)^2+I has dimension four. Hence no change of "
                    "basis can produce a six-dimensional invariant subspace on which "
                    "the direct adjoint acts as J_DE."
                ),
            },
            "consequence": {
                "retired_shortcut": (
                    "The Fu-Yau elliptic order-four automorphism cannot simply be "
                    "identified with the diagonal/edge strain quarter-turn through "
                    "its direct action on the degree-three theta space."
                ),
                "remaining_routes": [
                    "construct a nontrivial typed inverse-Fourier-Mukai functor and prove its induced action on the sheet-symbol carrier is J_DE",
                    "or compute the actual projected HYM Hessian block directly",
                ],
            },
        },
        "claim_tiers": {
            "square_elliptic_degree_three_quarterturn": "CLOSED_EXACT",
            "direct_theta_adjoint_on_Herm3": "CLOSED_EXACT",
            "direct_theta_adjoint_preserves_q79_D_plus_S_strain": "CLOSED_NO_GO",
            "direct_theta_adjoint_realizes_six_dimensional_JDE": "CLOSED_NO_GO",
            "abstract_C4_matrix_match_is_sufficient_same_carrier_functor": "CLOSED_NO_GO",
            "nontrivial_inverse_Fourier_Mukai_induced_JDE_functor": "OPEN",
            "actual_projected_HYM_Hessian": "OPEN",
        },
        "guardrails": {
            "claims_trial_tau_i_or_identity_alignment_is_MTT_selected": False,
            "claims_no_possible_nontrivial_Fourier_Mukai_functor_exists": False,
            "claims_actual_HYM_Hessian_computed": False,
            "uses_observed_physics_data": False,
            "adds_fitted_numeric_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# q79 Square-Theta Quarter-Turn to Strain Direct-Functor No-Go v1

Status:
`Q79_SQUARE_THETA_DIRECT_ADJOINT_TO_STRAIN_QUARTERTURN_CLOSED_NOGO_NONTRIVIAL_INVERSE_FOURIER_MUKAI_FUNCTOR_OR_DIRECT_HYM_REQUIRED`

## Exact geometric action

The constructive square elliptic packet uses

```text
E: b^2*c=a^3-a*c^2,
H^0(E,O(3*0))=<a,b,c>.
```

The origin-preserving elliptic quarter-turn is

```text
(a,b,c)->(-a,i*b,c),
U_theta=diag(-1,i,1).
```

Direct substitution sends the cubic polynomial to its negative, so the same
projective cubic is preserved, and `U_theta^4=I` exactly.

## Induced action on Herm(3)

Use the trace-orthonormal basis

```text
D1,D2,D3,
S23,S13,S12,
K23,K13,K12.
```

The exact real adjoint action `X->U_theta X U_theta^*` has

```text
dim ker(Ad(U)-I)   =3,
dim ker(Ad(U)+I)   =2,
dim ker(Ad(U)^2+I)=4.
```

It fixes the three diagonal modes. One off-diagonal Hermitian plane is rotated
by `pi`, while the other two `(S_ij,K_ij)` planes are rotated by quarter turns.
Consequently

```text
Ad(U_theta)(D direct-sum S) is not contained in D direct-sum S.
```

## Basis-independent no-go

The desired lane quarter-turn `J_DE` obeys `J_DE^2=-I` on a real
six-dimensional carrier. The direct theta adjoint has only a four-dimensional
`J^2=-I` sector. Kernel dimension is invariant under change of basis, so no
conjugation can turn this direct adjoint into `J_DE` on six dimensions.

Therefore the exact abstract equality of the two `2x2` quarter-turn matrices
does not supply the same-carrier functor. In particular, the geometric
elliptic automorphism cannot simply be attached to the spectral strain symbol
by its direct degree-three theta action.

## What remains viable

This is a targeted no-go, not a no-go for Fourier-Mukai geometry. Two routes
remain:

```text
1. construct a genuinely nontrivial inverse-Fourier-Mukai functor and prove
   that its induced action on the sheet-symbol multiplicity plane is J_DE;
2. construct the actual balanced-HYM operator and compute H_std directly.
```

The packet's `tau=i` and identity alignment remain constructive trial data,
not primitive MTT selections. No observed datum or fitted parameter is used.
"""

    OUT_CERT.parent.mkdir(parents=True, exist_ok=True)
    OUT_NOTE.parent.mkdir(parents=True, exist_ok=True)
    OUT_CERT.write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {certificate['status']}")


if __name__ == "__main__":
    main()
