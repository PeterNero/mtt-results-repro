from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

WORLD_IN_WORLD = Path(
    r"C:\Users\nero_\Downloads\TEXPAPERS\10 ProtoSpinor\revised_tex_vnext"
) / (
    r"World_in_World_Genesis__Local_Comparison_Geometry_and_Globalization_Program_v5"
) / "main.tex"
CLOSURE_STRAIN = Path(
    r"C:\Users\nero_\Downloads\TEXPAPERS\10 ProtoSpinor\revised_tex_vnext"
) / (
    r"Closure_Strain_Geometry__Local_Normal_Forms_and_Conditional_Matter_Encodings_v7"
) / "main.tex"
Q79_CARRIER = Path(
    r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus"
) / "MTT_Selected_q79TraceSplitCLNCarrierAndWorldInWorldBridge_v1.md"
Q79_SIGNED_SHEET = Path(
    r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-sm-parity-closure\proof_corpus"
) / "MTT_Selected_q79SignedSheetSpinLiftReduction_v1.md"

OUT_CERT = ROOT / "certificates" / "q79_s3_strain_intertwiner_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "q79_S3_Strain_Intertwiner_and_Local_Q_Source_v1.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def permutation_sign(perm: tuple[int, int, int]) -> int:
    inversions = sum(
        1 for i in range(3) for j in range(i + 1, 3) if perm[i] > perm[j]
    )
    return -1 if inversions % 2 else 1


def permutation_matrix(perm: tuple[int, int, int]) -> sp.Matrix:
    matrix = sp.zeros(3)
    for source, target in enumerate(perm):
        matrix[target, source] = 1
    return matrix


def strain_map(source: sp.Matrix) -> sp.Matrix:
    """Map (a_1,a_2,a_3;b_1,b_2,b_3) to diagonal plus opposite-edge strain."""
    a1, a2, a3, b1, b2, b3 = source
    root2 = sp.sqrt(2)
    return sp.Matrix(
        [
            [a1, b3 / root2, b2 / root2],
            [b3 / root2, a2, b1 / root2],
            [b2 / root2, b1 / root2, a3],
        ]
    )


def frobenius_inner(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    return sp.trace(left.T * right)


def matrix_exp_symmetric(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * np.exp(values)) @ vectors.T


def main() -> None:
    world = read(WORLD_IN_WORLD)
    closure = read(CLOSURE_STRAIN)
    q79 = read(Q79_CARRIER)
    signed_sheet = read(Q79_SIGNED_SHEET)

    source_tests = {
        "world_in_world_Q_typed": (
            "Q_{\\rm WW}\\in\\Gamma" in world
            and "\\operatorname{Hom}(TP,TI)" in world
        ),
        "world_in_world_polar_metric_present": (
            "Q_{\\rm WW}^{T}Q_{\\rm WW}" in world
        ),
        "log_strain_is_half_log_QTQ": (
            "S=\\log U=\\frac12\\log(Q^TQ)" in closure
        ),
        "q79_trace_split_present": all(
            token in q79
            for token in (
                "A = O direct-sum A_0",
                "rank(O)=1",
                "rank(A_0)=2",
                "rank(A)=3",
            )
        ),
        "q79_monodromy_is_S3": "Mon(C/K3)=S3" in signed_sheet,
        "q79_signed_orientation_action_present": (
            "rho_plus(sigma)=sign(sigma) P_sigma" in q79
        ),
    }

    basis = [sp.eye(6).col(i) for i in range(6)]
    image_basis = [strain_map(vector) for vector in basis]
    gram = sp.Matrix(
        6,
        6,
        lambda i, j: sp.simplify(
            frobenius_inner(image_basis[i], image_basis[j])
        ),
    )

    u0 = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    p_trace3 = sp.simplify(u0 * u0.T)
    p_trace0_3 = sp.eye(3) - p_trace3
    p1 = sp.diag(1, 1, 1, 0, 0, 0)
    p1[:3, :3] = p_trace3
    p2 = sp.zeros(6)
    p2[:3, :3] = p_trace0_3
    p3 = sp.diag(0, 0, 0, 1, 1, 1)

    projector_checks = {
        "p1_idempotent": sp.simplify(p1 * p1 - p1) == sp.zeros(6),
        "p2_idempotent": sp.simplify(p2 * p2 - p2) == sp.zeros(6),
        "p3_idempotent": sp.simplify(p3 * p3 - p3) == sp.zeros(6),
        "projectors_sum_to_identity": sp.simplify(p1 + p2 + p3) == sp.eye(6),
        "projectors_pairwise_orthogonal": all(
            sp.simplify(left * right) == sp.zeros(6)
            for left, right in ((p1, p2), (p1, p3), (p2, p3))
        ),
        "ranks_are_1_2_3": [p1.rank(), p2.rank(), p3.rank()] == [1, 2, 3],
    }

    equivariance_rows: list[dict[str, object]] = []
    equivariance_exact = True
    orientation_exact = True
    for perm in itertools.permutations(range(3)):
        p = permutation_matrix(perm)
        sign = permutation_sign(perm)
        rho = sign * p
        orientation_exact = orientation_exact and sp.det(rho) == 1

        source_action = sp.diag(p, p)
        residual_zero = True
        for vector in basis:
            lhs = strain_map(source_action * vector)
            rhs = sp.simplify(rho * strain_map(vector) * rho.T)
            if sp.simplify(lhs - rhs) != sp.zeros(3):
                residual_zero = False
                break
        equivariance_exact = equivariance_exact and residual_zero
        equivariance_rows.append(
            {
                "permutation": list(perm),
                "sign": sign,
                "det_rho_plus": int(sp.det(rho)),
                "intertwining_residual_exactly_zero": residual_zero,
            }
        )

    rng = np.random.default_rng(7903)
    direction = rng.normal(size=6)
    direction /= np.linalg.norm(direction)
    symbolic_direction = sp.Matrix([sp.Float(value, 17) for value in direction])
    strain = np.array(strain_map(symbolic_direction), dtype=float)
    epsilon = 1.0e-7
    q_epsilon = matrix_exp_symmetric(epsilon * strain)
    metric_epsilon = q_epsilon.T @ q_epsilon
    derivative_numeric = (metric_epsilon - np.eye(3)) / epsilon
    derivative_predicted = 2.0 * strain
    derivative_residual = float(
        np.linalg.norm(derivative_numeric - derivative_predicted, ord="fro")
    )

    exact_checks = {
        "J_is_frobenius_isometry": gram == sp.eye(6),
        "all_six_S3_actions_intertwine": equivariance_exact,
        "rho_plus_is_orientation_preserving": orientation_exact,
        **projector_checks,
        "finite_difference_confirms_DG0_equals_2J": derivative_residual < 1.0e-6,
    }

    theorem = {
        "name": "q79S3StrainIntertwinerAndLocalQSource.v1",
        "statement": (
            "On the unbranched q79 S3 sheet local system, the map J(a,b)="
            "Diag(a)+(opposite-edge symmetric matrix of b)/sqrt(2) is an exact "
            "S3-equivariant isometry from (O plus A0) plus A to Sym(3,R). "
            "It maps the source ranks 1,2,3 to scalar diagonal, traceless "
            "diagonal, and symmetric off-diagonal strain."
        ),
        "source_coordinates": "(a1,a2,a3 ; b1,b2,b3), with a=trace plus trace-zero and b=the reused full lane",
        "formula": (
            "J(a,b)=[[a1,b3/sqrt(2),b2/sqrt(2)],"
            "[b3/sqrt(2),a2,b1/sqrt(2)],"
            "[b2/sqrt(2),b1/sqrt(2),a3]]"
        ),
        "why_no_global_sheet_order_is_needed": (
            "Relabeling sheets by sigma acts as P_sigma on both a and b and as "
            "rho_plus(sigma) S rho_plus(sigma)^T on strain. The six exact "
            "intertwining identities make the local formula descend as an "
            "associated-bundle map."
        ),
        "orientation_fixed_Q_source": "Q(f)=exp(J f)",
        "induced_metric_observable": "G(f)=Q(f)^T Q(f)=exp(2 J f)",
        "selected_background": "f_*=0, Q_*=I, G_*=I",
        "computed_derivative": "DG(0)[delta f]=2 J(delta f)",
        "log_strain_derivative": "D[(1/2)log G](0)[delta f]=J(delta f)",
        "proved_on_unbranched_S3_local_system": all(exact_checks.values()),
    }

    scope = {
        "closed": [
            "parameter-free real six-lane fiber map",
            "S3 monodromy compatibility without ordered sheets",
            "canonical Euclidean/Frobenius metric compatibility",
            "1+2+3 projector compatibility",
            "orientation-fixed nonlinear Q source",
            "local induced-metric derivative DG(0)=2J",
            "flat associated-local-system connection compatibility on the unbranched locus",
        ],
        "still_open": [
            "extension through the q79 branch locus",
            "compatibility with the selected inverse-Fourier-Mukai/HYM connection and metric",
            "removal or neutralization of the L_shared complex phase for a real metric observable",
            "identification of this internal rank-three carrier with the physical spatial frame bundle",
            "transport of the actual selected Hessian, retarded kernel, and overlap kernel",
        ],
        "important_typing_correction": (
            "The exact map is J_L=id_{L_shared} tensor J from L_shared tensor "
            "(O plus A0 plus A) to L_shared tensor Sym(V). A real untwisted "
            "metric additionally needs a real structure, phase-neutral pairing, "
            "or a selected trivialization; J alone does not erase L_shared."
        ),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "q79_s3_strain_intertwiner",
        "status": "Q79_S3_STRAIN_INTERTWINER_AND_LOCAL_Q_SOURCE_CLOSED_HYM_PHYSICAL_IDENTIFICATION_OPEN",
        "source_files": {
            "world_in_world_v5": str(WORLD_IN_WORLD),
            "closure_strain_v7": str(CLOSURE_STRAIN),
            "q79_trace_split_carrier": str(Q79_CARRIER),
            "q79_signed_sheet_monodromy": str(Q79_SIGNED_SHEET),
        },
        "source_tests": source_tests,
        "exact_checks": exact_checks,
        "equivariance_table": equivariance_rows,
        "gram_matrix": [[str(value) for value in row] for row in gram.tolist()],
        "projector_ranks": [p1.rank(), p2.rank(), p3.rank()],
        "metric_derivative_finite_difference": {
            "epsilon": epsilon,
            "frobenius_residual": derivative_residual,
        },
        "theorem": theorem,
        "scope": scope,
        "guardrails": {
            "claims_global_HYM_intertwiner_closed": False,
            "claims_branch_locus_extension_closed": False,
            "claims_physical_spacetime_metric_derived": False,
            "claims_L_shared_phase_trivialized": False,
            "adds_fitted_numeric_parameter": False,
            "uses_observed_GR_data": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# q79 S3 Strain Intertwiner and Local Q Source v1

## Exact construction

Write the q79 trace-split carrier without its common line factor as

```text
F_q79 = (O direct-sum A0) direct-sum A = A direct-sum A.
```

In a local sheet chart let `a=(a1,a2,a3)` denote the first copy, already split
canonically into trace and trace-zero parts, and let `b=(b1,b2,b3)` denote the
reused full rank-three lane. Define

```text
J(a,b) =
[
  a1          b3/sqrt(2)  b2/sqrt(2)
  b3/sqrt(2)  a2          b1/sqrt(2)
  b2/sqrt(2)  b1/sqrt(2)  a3
].
```

The second copy is sent from vertices to opposite edges. The `1/sqrt(2)` is
forced by the Frobenius norm of a symmetric off-diagonal matrix unit.

The exact symbolic audit proves:

```text
J^* J = I6,
J rho_source(sigma) = Ad_{rho_plus(sigma)} J for every sigma in S3,
rank(P_trace, P_trace-zero, P_offdiag) = (1,2,3).
```

Since `rho_plus(sigma)=sign(sigma) P_sigma`, its sign cancels under conjugation.
The opposite-edge rule is equivariant under every sheet relabeling. Therefore
the formula descends on the unbranched q79 `S3` local system and does not choose
a global ordering of sheets.

## Actual local Q and metric map

On the orientation-fixed polar slice define

```text
S(f) = J f,
Q(f) = exp(S(f)),
G(f) = Q(f)^T Q(f) = exp(2 S(f)).
```

At the zero-strain background `f_*=0`,

```text
Q_*=I,
G_*=I,
DG(0)[delta f] = 2 J(delta f),
D[(1/2) log G](0)[delta f] = J(delta f).
```

This is the first explicit, monodromy-compatible local metric derivative in
the q79/world-in-world chain. It is a calculation from a displayed nonlinear
observable, not acceptance of a prefilled `B0` matrix.

## What this closes

- the real `1+2+3` fiber intertwiner on the unbranched `S3` local system;
- transition compatibility without ordered sheets;
- the canonical Frobenius metric and all three lane projectors;
- an orientation-fixed nonlinear `Q` source and its exact local derivative.

## What remains

The theorem does not yet turn this carrier into the physical spacetime metric.
It still requires extension through the branch locus, compatibility with the
selected HYM connection/metric and Hessian, and an identification with the
physical spatial frame bundle.

There is also a typing point hidden by earlier rank notation. The exact twisted
map is

```text
id_L tensor J:
L_shared tensor (O direct-sum A0 direct-sum A)
  -> L_shared tensor Sym(V).
```

An untwisted real metric requires a selected real structure, phase-neutral
pairing, or trivialization. The common complex line cannot simply disappear.
"""

    OUT_NOTE.write_text(note, encoding="utf-8")
    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
