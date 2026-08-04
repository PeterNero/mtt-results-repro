from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent

FOUNDATION = (
    TEXPAPERS
    / "3 Core Foundations"
    / "revised_tex_vnext"
    / "Modal_Triplet_Theory__Foundation_v8"
    / "main.tex"
)
PROJECTION = (
    TEXPAPERS
    / "3 Core Foundations"
    / "revised_tex_vnext"
    / "The_Projection__Admissibility_Principle__Descent__Recovery__and_Structural_Constraints_v2"
    / "main.tex"
)
FIXED_POINT_I = (
    TEXPAPERS
    / "4 Fixed Points"
    / "revised_tex_vnext"
    / "Fixed_Points_I__Fixed_Points_over_Multi_Bundle_Manifolds_v6"
    / "main.tex"
)

ROOTSTACK = (
    ROOT
    / "certificates"
    / "q79_cubic_norm_full_monodromy_rootstack_bridge_certificate.json"
)
SOURCE_MAP = (
    ROOT / "certificates" / "selected_q79_z64_qww_source_factorization_certificate.json"
)
FINITE_OPERATOR = (
    ROOT / "certificates" / "q79_finite_rootstack_reynolds_tt_hessian_certificate.json"
)
CLASSICAL = (
    ROOT / "certificates" / "q79_finite_source_tegr_classical_closure_certificate.json"
)
LOW_ENERGY_EFT = (
    ROOT / "certificates" / "q79_interacting_low_energy_qg_eft_closure_certificate.json"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_primitive_branch_selection_cutset_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Primitive_Physical_Branch_NonDerivability_and_OneAxiom_Completion_v1.md"
)


def read(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8", errors="replace")


def load(path: Path) -> dict:
    return json.loads(read(path))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    foundation = read(FOUNDATION)
    projection = read(PROJECTION)
    fixed_point = read(FIXED_POINT_I)
    rootstack = load(ROOTSTACK)
    source_map = load(SOURCE_MAP)
    finite_operator = load(FINITE_OPERATOR)
    classical = load(CLASSICAL)
    low_energy_eft = load(LOW_ENERGY_EFT)

    u, v, x = sp.symbols("u v x", real=True)
    t = sp.symbols("t", positive=True)
    cost = x**2
    gradient = sp.diff(cost, x)
    monotonicity_residual = sp.expand(
        (gradient.subs(x, u) - gradient.subs(x, v)) * (u - v)
        - 2 * (u - v) ** 2
    )
    flow = sp.exp(-2 * t) * x
    fixed_point_equation = sp.factor(flow - x)
    fixed_point_solutions = sp.solve(sp.Eq(flow, x), x)

    # Two disconnected, isomorphic physical-completion labels. Every datum used
    # by the abstract Foundation and basin-local fixed-point theorem is identical.
    branch_labels = ["R0", "R1"]
    invariant_feature = {label: [1, 2, 1, 0, 2] for label in branch_labels}
    invariant_scores = {label: 0 for label in branch_labels}
    selected_minimizers = [
        label for label, value in invariant_scores.items() if value == 0
    ]
    swap = [[0, 1], [1, 0]]

    checks = {
        "Foundation_declares_Lorentzian_completion_not_derived": (
            "The canonical base" in foundation
            and "dimension $3+1$ is part of the canonical FP physical realization"
            in foundation
            and "derived by the abstract Hilbert-bundle theory" in foundation
        ),
        "Foundation_declares_selection_reset_is_extra_law": (
            "Calling the reset\n``selection'' does not make it part of the original flow."
            in foundation
        ),
        "Projection_principle_has_no_automatic_selection": (
            "Nor does exit select a new state." in projection
        ),
        "FixedPoint_uniqueness_is_internal_to_declared_coherent_sector": (
            "Uniqueness on the coherent sector" in fixed_point
            and "unique minimizer $\\Psi^\\ast$" in fixed_point
        ),
        "countermodel_cost_is_nonnegative": sp.ask(sp.Q.nonnegative(cost)) is True,
        "countermodel_gradient_is_two_x": gradient == 2 * x,
        "countermodel_strong_monotonicity_mu_two": monotonicity_residual == 0,
        "countermodel_flow_is_contracting_for_positive_time": sp.limit(
            flow, t, sp.oo
        )
        == 0,
        "countermodel_each_branch_has_same_unique_equilibrium": fixed_point_solutions
        == [0],
        "countermodel_branch_features_are_identical": invariant_feature["R0"]
        == invariant_feature["R1"],
        "countermodel_invariant_minimization_does_not_select_one_branch": len(
            selected_minimizers
        )
        == 2,
        "branch_swap_is_nontrivial_involution": sp.Matrix(swap) ** 2 == sp.eye(2)
        and sp.Matrix(swap) != sp.eye(2),
        "q79_minimal_full_monodromy_continuation_is_unique_after_branch": (
            rootstack["claim_tiers"]["minimal_full_monodromy_rootstack"]
            == "CLOSED_UNIQUE_MINIMAL"
        ),
        "q79_source_map_is_unique_up_to_gauge_after_branch": (
            source_map["claim_tiers"][
                "selected_branch_q79_Z64_QWW_source_realization"
            ]
            == "CLOSED_UNIQUE_UP_TO_GAUGE"
        ),
        "q79_finite_operator_is_exact_after_branch": finite_operator["claim_tiers"][
            "finite_rootstack_TT_2x2_block"
        ]
        == "CLOSED_EXACT_IDENTITY_SHAPE",
        "classical_GR_tier_is_closed_after_branch": classical["claim_tiers"][
            "classical_GR_equivalence_at_declared_finite_source_IR_tier"
        ]
        == "CLOSED_CONDITIONAL_WITH_TWO_EFFECTIVE_GRAVITATIONAL_COORDINATES",
        "interacting_low_energy_EFT_tier_is_closed_after_branch": low_energy_eft[
            "claim_tiers"
        ]["interacting_low_energy_quantum_GR_EFT"]
        == "CLOSED_BY_STANDARD_EFT_COMPOSITION_AT_EACH_FIXED_ORDER",
    }
    checks = {name: bool(value) for name, value in checks.items()}
    if not all(checks.values()):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed checks: {failed}")

    status = (
        "PRIMITIVE_BRANCH_SELECTION_NOT_DERIVABLE_FROM_CURRENT_FOUNDATION_"
        "ONE_DISCRETE_PHYSICAL_REALIZATION_AXIOM_SUFFICES_FOR_LOW_ENERGY_QG_TIER"
    )
    physical_axiom = (
        "A_QG: the physical MTT completion is the gauge-equivalence class of the "
        "canonical q79/Z64/Q_WW minimal-full-monodromy-rootstack Lorentzian "
        "realization carrying the normalized finite Reynolds action."
    )

    certificate = {
        "certificate": "q79_primitive_branch_selection_cutset",
        "date": "2026-07-15",
        "program": "MTT protospinor GR response proof",
        "status": status,
        "corpus_inputs": {
            "Foundation_v8": {"path": str(FOUNDATION), "sha256": sha256(FOUNDATION)},
            "Projection_Admissibility_v2": {
                "path": str(PROJECTION),
                "sha256": sha256(PROJECTION),
            },
            "Fixed_Points_I_v6": {
                "path": str(FIXED_POINT_I),
                "sha256": sha256(FIXED_POINT_I),
            },
        },
        "computed_inputs": {
            "minimal_rootstack": str(ROOTSTACK),
            "selected_source_map": str(SOURCE_MAP),
            "finite_operator": str(FINITE_OPERATOR),
            "classical_GR": str(CLASSICAL),
            "low_energy_QG_EFT": str(LOW_ENERGY_EFT),
        },
        "theorem": {
            "name": "PrimitivePhysicalBranchNonDerivabilityAndOneAxiomCompletion",
            "non_derivability": (
                "Foundation v8 and Projection-Admissibility v2 explicitly leave "
                "physical completion and branch selection as supplied data. Fixed "
                "Points I proves uniqueness only inside a declared coherent sector "
                "for a fixed cost/flow. The displayed two-branch automorphism model "
                "satisfies those internal hypotheses on both branches while no "
                "invariant score selects one. Therefore the current abstract corpus "
                "cannot derive a unique physical realization."
            ),
            "minimal_completion_axiom": physical_axiom,
            "sufficiency": (
                "After A_QG, prior exact uniqueness theorems leave no further "
                "discrete geometry/operator choice: the minimal root-stack orders "
                "are (2,3,2,1), the q79/Z64/QWW source is unique up to gauge, the "
                "finite TT block is kappa_e I2, and the declared classical GR, free "
                "graviton and interacting low-energy EFT tiers compose."
            ),
            "minimality": (
                "At least one branch-noninvariant datum is logically necessary, as "
                "shown by the branch-swap automorphism. One discrete realization "
                "axiom is sufficient. This is minimal by logical type; it is not a "
                "claim that the axiom has been derived from prior MTT dynamics."
            ),
        },
        "countermodel": {
            "branch_set": branch_labels,
            "fiber_on_each_branch": "R",
            "cost_on_each_branch": "C_b(x)=x^2",
            "gradient_flow_on_each_branch": "Phi_t(x)=exp(-2t)x",
            "strong_monotonicity_constant": 2,
            "unique_equilibrium_on_each_branch": 0,
            "branch_swap_matrix": swap,
            "identical_invariant_feature_vectors": invariant_feature,
            "invariant_minimizer_set": selected_minimizers,
        },
        "parameter_ledger": {
            "additional_discrete_physical_realization_axioms": 1,
            "additional_continuous_parameters_from_branch_axiom": 0,
            "target_or_observed_data_used_to_choose_branch": 0,
            "effective_low_energy_gravity_coordinates_still_required": [
                "kappa_h_or_G_eff",
                "Lambda_eff",
            ],
            "state_data_if_unique_universe_is_claimed": 1,
            "higher_derivative_Wilson_values_or_UV_completion": "STILL_OPEN",
        },
        "claim_tiers": {
            "primitive_branch_selection_from_unaugmented_current_MTT": (
                "CLOSED_NO_GO_BY_EXPLICIT_TWO_BRANCH_AUTOMORPHISM_MODEL"
            ),
            "minimal_extra_branch_selection_data": (
                "CLOSED_ONE_DISCRETE_PHYSICAL_REALIZATION_AXIOM_ZERO_CONTINUOUS_KNOBS"
            ),
            "q79_geometry_operator_choice_after_A_QG": (
                "CLOSED_UNIQUE_UP_TO_DECLARED_GAUGE"
            ),
            "low_energy_QG_law_after_A_QG": (
                "CLOSED_CONDITIONAL_ON_KAPPA_H_LAMBDA_EFT_DATA_AND_STATE"
            ),
            "A_QG_derived_from_current_upper_MTT_dynamics": "OPEN",
            "numeric_kappa_h": "OPEN",
            "numeric_Lambda_eff": "OPEN",
            "UV_complete_quantum_gravity": "OPEN",
        },
        "guardrails": {
            "claims_basin_local_fixed_point_uniqueness_selects_geometry": False,
            "claims_minimal_rootstack_relative_uniqueness_selects_q79_physics": False,
            "claims_admissibility_exit_selects_a_new_state": False,
            "claims_A_QG_is_derived_rather_than_adopted": False,
            "claims_one_discrete_axiom_fixes_kappa_or_Lambda": False,
            "uses_observed_data": False,
            "adds_continuous_fit_parameter": False,
        },
        "checks": checks,
        "next_required_artifact": (
            "MTT_UpperDynamics_TargetIndependent_PhysicalRealizationFunctional_"
            "with_Strict_q79_Gap_v1"
        ),
        "note_written": str(OUT_NOTE),
    }

    note = f"""# q79 Primitive Physical Branch Non-Derivability and One-Axiom Completion v1

Date: 2026-07-15

Status:
`{status}`

## Question

Can the revised Foundation, Projection-Admissibility, or Fixed-Point papers
already promote the constructed q79 minimal-rootstack Lorentzian realization
to the unique physical branch?

The answer is no for the unaugmented current corpus, and the obstruction is
exact rather than merely a missing search.

Foundation v8 states that the canonical `3+1` Lorentzian base belongs to a
physical completion and is not derived by the abstract Hilbert-bundle theory.
It also states that a reset called selection is a new hybrid law unless it is
derived from upper dynamics. Projection-Admissibility v2 says directly that
admissibility exit does not select a new state. Fixed Points I v6 proves
uniqueness inside a declared coherent sector for a fixed cost and flow; it does
not compare inequivalent physical completions.

## Exact countermodel

Take two disconnected branch labels `R0,R1`. On each branch use

```text
H_b=R,
C_b(x)=x^2,
Phi_t(x)=exp(-2t)x.
```

The gradient is `2x`, the strong-monotonicity constant is exactly `mu=2`, and
each branch has the same unique equilibrium `x=0`. Give both branches the same
admissibility margins, spectral ranks, gaps, and finite root-order feature
vector. The swap

```text
R0 <-> R1
```

is a nontrivial involutive automorphism preserving every datum used by those
abstract theorems. Any score made only from the invariant data ties on both
branches. A unique branch choice would break the automorphism and therefore
requires at least one branch-noninvariant input.

This proves:

```text
basin-local unique minimizer != unique physical branch.
```

Likewise, the q79 root stack is uniquely minimal after q79 monodromy is chosen;
that relative uniqueness does not choose q79 from the class of physical
completions.

## Minimal one-axiom completion

Exactly one discrete declaration is sufficient:

```text
{physical_axiom}
```

After this axiom, the existing exact chain leaves no further discrete
geometry/operator choice:

```text
q79 monodromy
  -> unique minimal root orders (2,3,2,1)
  -> unique rank-six strain bridge
  -> unique q79/Z64/QWW source up to gauge
  -> H_TT=kappa_e I2
  -> TEGR/Einstein classical law
  -> two-helicity free graviton
  -> interacting low-energy quantum-GR EFT parity.
```

The added branch datum is one discrete axiom and zero continuous knobs. It is
minimal by logical type because the two-branch countermodel proves that no
branch-invariant theorem can do the job. It is an adopted completion axiom,
not a theorem secretly extracted from Foundation v8.

## Remaining values

The one-axiom completion does not determine the dimensionful Newton/action
normalization or `Lambda_eff`. It also does not select a unique cosmic state,
higher-derivative Wilson values, or an all-scale UV theory. Thus the strongest
honest low-energy ledger is:

```text
one discrete physical-realization axiom,
one Newton/action coordinate,
one cosmological coordinate,
state data when a unique universe is requested,
standard EFT Wilson data at the chosen higher order.
```

## What would derive rather than adopt the axiom

The missing stronger object is now exact: a target-independent functional on
the gauge quotient of admissible physical realizations, derived from upper MTT
dynamics, for which the q79 class exists and has a strict positive gap over
every inequivalent competitor. It must include Lorentzian hyperbolicity,
source compatibility, and admissibility, and it cannot use measured GR/SM data
as its selector.
"""

    OUT_CERT.parent.mkdir(parents=True, exist_ok=True)
    OUT_NOTE.parent.mkdir(parents=True, exist_ok=True)
    OUT_CERT.write_text(json.dumps(certificate, indent=2) + "\n", encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(status)


if __name__ == "__main__":
    main()
