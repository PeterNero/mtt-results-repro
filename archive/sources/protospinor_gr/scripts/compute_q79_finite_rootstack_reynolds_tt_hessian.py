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
SPECTRAL_SYMBOL = (
    ROOT / "certificates" / "q79_spectral_hym_strain_symbol_bridge_certificate.json"
)
ROOTPLANE_JDE = (
    ROOT
    / "certificates"
    / "q79_shared_rootplane_twisted_exterior_jde_functor_certificate.json"
)
FINITE_SOURCE = (
    SM_REPO
    / "candidate_data"
    / "selected_finiteprojectedhymsourceprinciple_or_bandlimitexactnessproof.candidate.json"
)
RANK2_ROW_MODEL = (
    ROOT / "candidate_data" / "selected_scalar_exps_to_full_hym_row_model_lift.packet.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_finite_rootstack_reynolds_tt_hessian_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Finite_RootStack_Reynolds_TT_Hessian_and_Direct_Operator_Exit_v1.md"
)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def permutation_matrix(permutation: tuple[int, int, int]) -> sp.Matrix:
    matrix = sp.zeros(3)
    for source, target in enumerate(permutation):
        matrix[target, source] = 1
    return matrix


def as_strings(matrix: sp.Matrix) -> list[list[str]]:
    return [
        [str(sp.simplify(matrix[row, column])) for column in range(matrix.cols)]
        for row in range(matrix.rows)
    ]


def main() -> None:
    rootstack = load(ROOTSTACK)
    spectral_symbol = load(SPECTRAL_SYMBOL)
    rootplane_jde = load(ROOTPLANE_JDE)
    finite_source = load(FINITE_SOURCE)
    rank2_row_model = load(RANK2_ROW_MODEL)

    permutations = list(itertools.permutations(range(3)))
    sheet_actions = [permutation_matrix(permutation) for permutation in permutations]
    strain_actions = [sp.diag(action, action) for action in sheet_actions]

    reynolds = sp.simplify(sum(strain_actions, sp.zeros(6)) / len(strain_actions))
    complement = sp.eye(6) - reynolds

    mismatch_hessian = sp.simplify(
        sum(
            ((sp.eye(6) - action).T * (sp.eye(6) - action) for action in strain_actions),
            sp.zeros(6),
        )
        / (2 * len(strain_actions))
    )

    identity3 = sp.eye(3)
    zero3 = sp.zeros(3)
    jde = sp.BlockMatrix([[zero3, -identity3], [identity3, zero3]]).as_explicit()

    # One orthonormal standard vector in each lane reads off the multiplicity block.
    standard_atom = sp.Matrix([1, -1, 0]) / sp.sqrt(2)
    multiplicity_embedding = sp.Matrix.hstack(
        sp.Matrix.vstack(standard_atom, sp.zeros(3, 1)),
        sp.Matrix.vstack(sp.zeros(3, 1), standard_atom),
    )
    tt_block = sp.simplify(multiplicity_embedding.T * mismatch_hessian * multiplicity_embedding)

    trace_d = sp.Matrix([1, 1, 1, 0, 0, 0])
    trace_e = sp.Matrix([0, 0, 0, 1, 1, 1])
    eigenvalues = mismatch_hessian.eigenvals()

    # The finite action is
    #   S_fin(w)=kappa/(4|S3|) sum_g ||w-rho(g)w||^2.
    # Its Hessian is kappa*Q.  The displayed matrix is the kappa=1 shape.
    checks = {
        "q79_minimal_full_monodromy_group_is_S3": rootstack["claim_tiers"][
            "full_S3_cusp_monodromy"
        ]
        == "CLOSED_EXACT_2_3_2_1"
        and rootstack["claim_tiers"]["minimal_full_monodromy_rootstack"]
        == "CLOSED_UNIQUE_MINIMAL",
        "q79_spectral_symbol_has_two_permutation_copies": spectral_symbol["finite_data"][
            "S3_irrep_multiplicities"
        ]["strain_modes"]
        == {"sign": 0, "standard": 2, "trivial": 2},
        "flat_symbol_JDE_is_root_independent": rootplane_jde["claim_tiers"][
            "shared_root_C4_realification"
        ]
        == "CLOSED_EXACT_ROOT_INDEPENDENT"
        and rootplane_jde["claim_tiers"][
            "typed_shared_C4_to_rootstack_strain_JDE_functor"
        ]
        == "CLOSED_EXACT_ON_FLAT_SHEET_SYMBOL",
        "finite_projected_source_exactness_is_available": finite_source["closure_decision"][
            "finite_projected_HYM_source_principle_closed"
        ]
        is True,
        "six_group_elements_used_once": len(strain_actions) == 6
        and len({tuple(action) for action in strain_actions}) == 6,
        "reynolds_is_symmetric": reynolds.T == reynolds,
        "reynolds_is_idempotent": reynolds**2 == reynolds,
        "reynolds_rank_is_two": reynolds.rank() == 2,
        "reynolds_is_the_two_lane_trivial_projector": reynolds
        == sp.diag(sp.ones(3, 3) / 3, sp.ones(3, 3) / 3),
        "mismatch_hessian_equals_reynolds_complement": mismatch_hessian == complement,
        "hessian_is_positive_semidefinite": eigenvalues == {sp.Integer(0): 2, sp.Integer(1): 4},
        "kernel_is_exactly_two_trace_modes": 6 - mismatch_hessian.rank() == 2
        and mismatch_hessian * trace_d == sp.zeros(6, 1)
        and mismatch_hessian * trace_e == sp.zeros(6, 1)
        and sp.Matrix.hstack(trace_d, trace_e).rank() == 2,
        "JDE_commutes_with_reynolds": jde * reynolds == reynolds * jde,
        "JDE_commutes_with_hessian": jde * mismatch_hessian == mismatch_hessian * jde,
        "projected_TT_block_is_identity": tt_block == sp.eye(2),
        "TT_offdiagonal_is_zero": tt_block[0, 1] == 0,
        "TT_diagonal_entries_are_equal_positive": tt_block[0, 0]
        == tt_block[1, 1]
        == 1,
        "rank2_row_model_is_not_rank3_spectral_bundle": rank2_row_model[
            "proof_reduction"
        ]["selected_holomorphic_structure"]["triangular_extension_form"].startswith(
            "barpartial_V = [["
        )
        and "rank-2" in rank2_row_model["theorem"]["statement"]
        and spectral_symbol["finite_data"][
            "S3_characters_by_identity_transposition_three_cycle"
        ]["diagonal_sheet_modes"]["identity"]
        == 3,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed checks: {failed}")

    certificate = {
        "certificate": "q79_finite_rootstack_reynolds_tt_hessian",
        "date": "2026-07-15",
        "program": "MTT protospinor GR response proof",
        "status": "Q79_FINITE_ROOTSTACK_REYNOLDS_TT_HESSIAN_CLOSED_EXACT_ONE_SCALE_CONTINUUM_BALANCED_HYM_NOT_CLAIMED",
        "inputs": {
            "q79_full_monodromy_rootstack": str(ROOTSTACK),
            "q79_spectral_strain_symbol": str(SPECTRAL_SYMBOL),
            "q79_flat_symbol_JDE": str(ROOTPLANE_JDE),
            "finite_projected_source_principle": str(FINITE_SOURCE),
            "rank2_row_model_type_guard": str(RANK2_ROW_MODEL),
        },
        "theorem": {
            "name": "q79FiniteRootStackReynoldsTTHessianTheorem",
            "source_carrier": "W_fin=R3_D direct_sum R3_E with diagonal S3 sheet action",
            "normalized_action": (
                "S_fin(w)=kappa_fin/(4|S3|) sum_{g in S3} "
                "||w-rho(g)w||^2"
            ),
            "hessian": "H_fin=kappa_fin*(I-P_Haar)",
            "Haar_projector": "P_Haar=|S3|^-1 sum_g rho(g)",
            "TT_conclusion": (
                "On standard_D direct_sum standard_E, the multiplicity block is "
                "H_std=kappa_fin I2, so h_DE=0 and h_DD=h_EE=kappa_fin>0."
            ),
            "selection_scope": (
                "The normalized group average is the unique S3-invariant probability "
                "trace on the finite orbit. The only unfixed coefficient is the one "
                "overall action normalization kappa_fin."
            ),
            "continuum_boundary": (
                "This is the direct finite projected root-stack operator exit. It does "
                "not construct the nonzero-Chern inverse-Fourier-Mukai visible bundle "
                "or its balanced continuum HYM Hessian."
            ),
        },
        "finite_data": {
            "group": "S3",
            "group_order": len(strain_actions),
            "carrier_dimension": 6,
            "reynolds_projector": as_strings(reynolds),
            "normalized_hessian_shape": as_strings(mismatch_hessian),
            "normalized_hessian_spectrum": {"0": 2, "1": 4},
            "normalized_hessian_rank": mismatch_hessian.rank(),
            "kernel": ["trace_D=(1,1,1;0,0,0)", "trace_E=(0,0,0;1,1,1)"],
            "J_DE": as_strings(jde),
            "TT_multiplicity_block": as_strings(tt_block),
            "dimensionless_fitted_parameters": 0,
            "overall_action_normalizations": 1,
        },
        "claim_tiers": {
            "normalized_S3_Haar_trace": "CLOSED_EXACT_UNIQUE",
            "finite_rootstack_group_mismatch_action": "CLOSED_EXACT_CONSTRUCTED",
            "finite_rootstack_projected_Hessian": "CLOSED_EXACT",
            "finite_rootstack_TT_2x2_block": "CLOSED_EXACT_IDENTITY_SHAPE",
            "finite_rootstack_JDE_invariance": "CLOSED_EXACT_ROOT_INDEPENDENT",
            "dimensionless_TT_Hessian_parameters": "CLOSED_ZERO",
            "physical_TT_action_normalization": "OPEN_ONE_EFFECTIVE_SCALE",
            "rank2_row_model_directly_equals_rank3_q79_spectral_bundle": "CLOSED_NO_GO_TYPE_MISMATCH",
            "actual_q79_inverse_Fourier_Mukai_visible_bundle": "OPEN",
            "actual_q79_balanced_continuum_HYM_Hessian": "OPEN",
            "finite_source_exit_requires_continuum_HYM_for_its_own_exactness": "CLOSED_NO",
        },
        "guardrails": {
            "claims_actual_continuum_HYM_Hessian_computed": False,
            "claims_rank2_HYM_row_model_is_rank3_spectral_bundle": False,
            "claims_overall_Newton_or_action_scale_derived": False,
            "claims_unique_physical_choice_of_finite_over_continuum_exit": False,
            "uses_observed_physics_values": False,
            "adds_dimensionless_fit": False,
        },
        "checks": checks,
        "next_required_artifact": "MTT_q79_FiniteSource_TEGR_ClassicalClosure_and_ParameterLedger_v1",
        "note_written": str(OUT_NOTE),
    }

    note = """# q79 Finite Root-Stack Reynolds TT Hessian and Direct Operator Exit v1

Date: 2026-07-15

Status:
`Q79_FINITE_ROOTSTACK_REYNOLDS_TT_HESSIAN_CLOSED_EXACT_ONE_SCALE_CONTINUUM_BALANCED_HYM_NOT_CLAIMED`

## Theorem

Use the already selected finite q79 full-monodromy symbol

```text
W_fin = R^3_D direct-sum R^3_E
```

with the diagonal sheet action of `S3`. Let

```text
P_Haar = (1/6) sum_{g in S3} rho(g).
```

The exact group average is

```text
P_Haar = diag((1/3) 11^T, (1/3) 11^T).
```

It is symmetric, idempotent, and rank two. Its image is exactly the two
trivial sheet/edge trace modes.

Define the normalized finite closure-defect action

```text
S_fin(w) = kappa_fin/(4|S3|) sum_g ||w-rho(g)w||^2.
```

Direct differentiation gives

```text
H_fin = kappa_fin (I-P_Haar).
```

Thus the normalized shape has spectrum

```text
0 with multiplicity 2,
1 with multiplicity 4.
```

The four positive directions are the two copies of the standard `S3`
representation. In an orthonormal standard vector in each lane, the physical
multiplicity block is exactly

```text
H_std = kappa_fin I2,
h_DE = 0,
h_DD = h_EE = kappa_fin > 0.
```

The previously constructed root-independent `J_DE` commutes with both
`P_Haar` and `H_fin`. No dimensionless coefficient is fitted. Only the single
overall action normalization `kappa_fin` remains.

## Why this is selected rather than guessed

The q79 cusp/root-stack theorem supplies the full `S3` sheet monodromy. The
spectral-symbol theorem supplies the two permutation copies `D` and `E`. On a
finite group orbit, normalized Haar counting is the unique invariant
probability trace. The displayed action is the corresponding mean squared
failure of global sheet closure, so its Hessian is an exact finite-source
object, not a continuum quadrature approximation.

This uses the same finite-projected-source standard already proved for the MTT
HYM program: finite trace and projected operations are exact on the selected
finite algebra.

## Type guard

The existing nonlinear one-row HYM replay is a genuine rank-2 extension
calculation. The q79 spectral visible carrier is rank 3. Therefore the rank-2
solution cannot simply be relabeled as the missing rank-3 Fu-Yau HYM block.
This theorem avoids that type error by calculating directly on the selected
finite root-stack symbol.

## Exact scope

Closed now:

```text
finite q79 direct-operator Hessian,
the projected 2x2 TT block,
J_DE invariance at the finite source tier,
zero dimensionless Hessian fits,
one and only one overall action normalization.
```

Not claimed:

```text
construction of the nonzero-Chern inverse Fourier-Mukai visible bundle,
the balanced continuum Fu-Yau HYM connection or Hessian,
selection of the finite exit over every continuum completion,
the numerical Newton scale.
```

The old `2/11` Fourier-Mukai count therefore remains correct for the continuum
route, but it no longer blocks the finite projected q79 operator exit.
"""

    OUT_CERT.write_text(json.dumps(certificate, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {certificate['status']}")


if __name__ == "__main__":
    main()
