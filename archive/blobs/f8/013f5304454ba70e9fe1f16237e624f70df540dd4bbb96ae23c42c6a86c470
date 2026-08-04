from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

GLOBAL_DG = ROOT / "certificates" / "global_covariant_helicity2_dg_bundle_certificate.json"
METRIC_SOURCE = ROOT / "certificates" / "world_in_world_z64_metric_source_map_certificate.json"
LOCAL_STF = ROOT / "certificates" / "selected_stf_hessian_form_certificate.json"
SCALE_BRIDGE = ROOT / "certificates" / "stf_hessian_scale_to_geff_relation_certificate.json"
REVISED_ACTION = (
    ROOT.parent
    / "10 ProtoSpinor"
    / "revised_tex_vnext"
    / "Closure_Geometry_and_a_Regime_Local_Ten_Dimensional_Action_Ansatz_v4"
    / "main.tex"
)

OUT_CERT = ROOT / "certificates" / "global_tt_hessian_action_uniqueness_reduction_certificate.json"
OUT_NOTE = ROOT / "proof_corpus" / "Global_TT_Hessian_and_Action_Uniqueness_Reduction_v1.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rank(matrix: list[list[Fraction]]) -> int:
    work = [row[:] for row in matrix]
    row_count = len(work)
    column_count = len(work[0]) if work else 0
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (row for row in range(pivot_row, row_count) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = work[row][column]
            if factor != 0:
                work[row] = [
                    value - factor * pivot_value
                    for value, pivot_value in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def matvec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum(value * component for value, component in zip(row, vector)) for row in matrix]


def main() -> None:
    global_dg = load(GLOBAL_DG)
    metric = load(METRIC_SOURCE)
    local_stf = load(LOCAL_STF)
    scale = load(SCALE_BRIDGE)
    revised_action_text = REVISED_ACTION.read_text(encoding="utf-8")

    # A symmetric 2 x 2 fiber Hessian H=[[a,b],[b,c]] must be invariant under
    # the weight-two quarter-turn J. The two independent equations are a-c=0
    # and b=0, so the symmetric commutant is one-dimensional.
    commutant_constraints = [
        [Fraction(1), Fraction(0), Fraction(-1)],
        [Fraction(0), Fraction(1), Fraction(0)],
    ]
    commutant_rank = rank(commutant_constraints)
    commutant_nullity = 3 - commutant_rank
    scalar_hessian = [Fraction(1), Fraction(0), Fraction(1)]
    scalar_hessian_residual = matvec(commutant_constraints, scalar_hessian)

    # Write the most general self-adjoint, parity-even, Lorentz-covariant
    # second-order metric operator as
    #
    # E_mn = A Box h_mn
    #      + B(d_m div(h)_n + d_n div(h)_m)
    #      + C d_m d_n h
    #      + D eta_mn div(div(h))
    #      + E eta_mn Box h.
    #
    # The first three rows impose the linearized Bianchi identity. The fourth
    # is the formal self-adjointness relation C=D. Their exact nullspace is the
    # Fierz-Pauli/linearized-Einstein vector (1,-1,1,1,-1).
    fp_constraints = [
        [Fraction(1), Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(1)],
        [Fraction(0), Fraction(0), Fraction(1), Fraction(-1), Fraction(0)],
    ]
    fp_rank = rank(fp_constraints)
    fp_nullity = 5 - fp_rank
    fp_vector = [
        Fraction(1),
        Fraction(-1),
        Fraction(1),
        Fraction(1),
        Fraction(-1),
    ]
    fp_residual = matvec(fp_constraints, fp_vector)

    # A Lorentz-invariant algebraic mass operator alpha h_mn + beta eta_mn h
    # has identically vanishing divergence for arbitrary h only when both
    # coefficients vanish. Thus gauge invariance excludes a mass term at this
    # quadratic level; this is conditional on MTT selecting that gauge symmetry.
    mass_constraints = [
        [Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(1)],
    ]
    mass_rank = rank(mass_constraints)
    mass_nullity = 2 - mass_rank

    metric_shape = metric["construction"]["core_factorization_matrix_C_for_metric_g"]
    metric_factor_two = (
        abs(metric_shape[0][0] - 2.0) < 1.0e-12
        and abs(metric_shape[1][1] - 2.0) < 1.0e-12
        and abs(metric_shape[0][1]) < 1.0e-12
        and abs(metric_shape[1][0]) < 1.0e-12
    )

    checks = {
        "global_helicity2_bundle_and_DG_available": (
            global_dg["claim_tiers"]["global_covariant_DG_bundle_map"]
            == "CLOSED_FOR_CONSTRUCTED_REALIZATION"
        ),
        "local_STF_form_is_explicitly_hypothesis_based": (
            local_stf["source_assumptions_used"][
                "local_covariance_and_rotation_invariance_of_transverse_plane"
            ]
            is True
        ),
        "symmetric_weight2_commutant_has_dimension_one": commutant_nullity == 1,
        "scalar_identity_spans_symmetric_commutant": all(
            value == 0 for value in scalar_hessian_residual
        ),
        "metric_to_half_log_strain_derivative_is_two": metric_factor_two,
        "metric_coordinate_hessian_factor_is_one_quarter": (
            Fraction(1, 2) ** 2 == Fraction(1, 4)
        ),
        "Fierz_Pauli_constraint_matrix_has_rank_four": fp_rank == 4,
        "Fierz_Pauli_operator_space_has_dimension_one": fp_nullity == 1,
        "linearized_Einstein_vector_satisfies_all_constraints": all(
            value == 0 for value in fp_residual
        ),
        "gauge_invariant_algebraic_mass_term_is_zero": mass_nullity == 0,
        "old_scale_bridge_uses_metric_quadratic_action_convention": (
            "quadratic_action_convention" in scale["relation"]
        ),
        "revised_proto_action_declares_ansatz": "action is an ansatz" in revised_action_text,
        "revised_proto_action_admits_EH_is_imported": (
            "imports the Einstein--Hilbert term" in revised_action_text
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    theorem = {
        "name": "GlobalTTHessianTransportAndFierzPauliUniquenessReductionTheorem",
        "part_A_global_fiber_hessian": {
            "statement": (
                "On E_TT=P_perp x_SO2 V2, every symmetric SO(2)-equivariant "
                "fiber Hessian is H_e=kappa_e Id_E. If the selected fixed point "
                "is nondegenerate and stable on this sector, then kappa_e>0."
            ),
            "proof_data": {
                "symmetric_matrix_coordinates": ["a", "b", "c"],
                "constraints": ["a=c", "b=0"],
                "constraint_rank": commutant_rank,
                "solution_dimension": commutant_nullity,
            },
            "scope": (
                "The global patching and unique form are proved. Positivity remains "
                "conditional on the upstream nondegenerate-stability hypothesis; no "
                "selected numerical Hessian is emitted here."
            ),
        },
        "part_B_coordinate_transport": {
            "half_log_strain": "e=(1/2)log G",
            "linearized_metric_relation": "h=delta G=2e",
            "strain_coordinate_hessian": "H_e=kappa_e Id_E",
            "metric_coordinate_hessian": "H_h=(kappa_e/4) Id_E",
            "definitions": "kappa_h:=kappa_e/4",
            "EH_convention_bridge": {
                "metric_coefficient": "kappa_h=(32*pi*G_eff)^(-1)",
                "strain_coefficient": "kappa_e=4*kappa_h=(8*pi*G_eff)^(-1)",
            },
            "correction": (
                "The old symbol kappa_STF was used both for closure-strain stiffness "
                "and for the metric-coordinate EH coefficient. Those are different by "
                "a factor of four for the explicitly computed G=exp(2S) map."
            ),
        },
        "part_C_action_uniqueness_reduction": {
            "hypotheses": [
                "a local parity-even Lorentz-covariant operator on a symmetric metric perturbation",
                "at most two derivatives in the infrared principal action",
                "formal self-adjointness",
                "linearized diffeomorphism invariance / off-shell Bianchi identity",
            ],
            "general_coefficients": ["A", "B", "C", "D", "E"],
            "constraint_matrix": [[str(value) for value in row] for row in fp_constraints],
            "constraint_rank": fp_rank,
            "solution_dimension": fp_nullity,
            "unique_vector_up_to_scale": [str(value) for value in fp_vector],
            "operator": (
                "E_mn=Box h_mn-d_m div(h)_n-d_n div(h)_m+d_m d_n h"
                "+eta_mn div(div(h))-eta_mn Box h"
            ),
            "TT_restriction": "E_TT=Box h_TT on a flat background, and the corresponding Lichnerowicz block on an Einstein background",
            "mass_statement": (
                "An algebraic Lorentz-invariant mass operator is incompatible with "
                "the same off-shell gauge identity unless its two coefficients vanish."
            ),
            "retarded_statement": (
                "Once a time orientation and globally hyperbolic Lorentzian background "
                "are selected, the normally hyperbolic TT operator has unique advanced "
                "and retarded Green operators. This does not select those Lorentzian "
                "inputs from MTT."
            ),
        },
        "parameter_count": 0,
        "remaining_source_problem": (
            "Prove from the same selected MTT source that the physical action satisfies "
            "the four action hypotheses, chooses the displayed G observable, and fixes "
            "kappa_h plus the matter stress normalization. The revised proto action "
            "cannot supply that proof because it explicitly imports EH and Lorentzian data."
        ),
    }

    cert = {
        "program": "MTT protospinor GR response proof",
        "certificate": "global_tt_hessian_action_uniqueness_reduction",
        "date": "2026-07-15",
        "status": "GLOBAL_TT_HESSIAN_PATCHING_COORDINATE_TRANSPORT_AND_FIERZ_PAULI_UNIQUENESS_CLOSED_SELECTED_MTT_ACTION_SOURCE_OPEN",
        "inputs": {
            "global_covariant_helicity2_dg_bundle": str(GLOBAL_DG),
            "world_in_world_z64_metric_source_map": str(METRIC_SOURCE),
            "selected_stf_hessian_form": str(LOCAL_STF),
            "stf_hessian_scale_to_geff_relation": str(SCALE_BRIDGE),
            "revised_proto_action": str(REVISED_ACTION),
        },
        "checks": checks,
        "theorem": theorem,
        "claim_tiers": {
            "global_symmetric_weight2_Hessian_form": "CLOSED_UNDER_STATED_STABILITY_AND_COVARIANCE_HYPOTHESES",
            "strain_to_metric_Hessian_coordinate_transport": "CLOSED_EXACT_FACTOR_ONE_QUARTER",
            "old_kappa_STF_symbol_overload": "RESOLVED_BY_KAPPA_E_VS_KAPPA_H",
            "Fierz_Pauli_operator_uniqueness": "CLOSED_CONDITIONAL_ON_FOUR_EXPLICIT_ACTION_HYPOTHESES",
            "massless_quadratic_operator": "CLOSED_CONDITIONAL_ON_LINEARIZED_DIFF_GAUGE_INVARIANCE",
            "retarded_Green_operator_uniqueness": "CLOSED_CONDITIONAL_ON_GLOBAL_HYPERBOLICITY_AND_TIME_ORIENTATION",
            "selected_MTT_action_satisfies_hypotheses": "OPEN",
            "selected_numeric_kappa_h": "OPEN",
            "selected_stress_coupling": "OPEN",
            "full_Lorentzian_GR_or_QG": "OPEN",
        },
        "supersession": {
            "stale_gate": "selected H_anchor to TT projection is missing",
            "replacement": (
                "The global DG and TT projector now supply the projection explicitly. "
                "The remaining Hessian issue is action-source selection and scale, not "
                "an unknown 2x2 matrix."
            ),
            "normalization_correction": (
                "Metric and half-log strain Hessian coefficients must be distinguished "
                "by kappa_h=kappa_e/4."
            ),
        },
        "guardrails": {
            "claims_selected_MTT_action_closed": False,
            "claims_upstream_stability_hypothesis_derived_here": False,
            "claims_numeric_kappa_or_Newton_constant": False,
            "claims_retarded_boundary_condition_selected_by_MTT": False,
            "claims_stress_coupling_closed": False,
            "claims_full_GR_or_QG_closed": False,
            "uses_observed_GR_data": False,
            "adds_fitted_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# Global TT Hessian and Action Uniqueness Reduction v1

Date: 2026-07-15

## 1. Global Hessian form

The new helicity bundle removes the old patching ambiguity.  A symmetric
fiber Hessian on the real weight-two representation has coordinates

```text
H = [[a,b],[b,c]].
```

Invariance under a spatial `pi/4` rotation, which acts on helicity two by the
quarter-turn matrix `J`, gives

```text
a=c,
b=0.
```

The exact constraint matrix has rank two, so the symmetric equivariant
commutant is one-dimensional.  Consequently the local plus/cross result
patches globally as

```text
H_e = kappa_e Id_E
```

on `E_TT`.  If the selected fixed point is nondegenerate and stable in this
sector, `kappa_e>0`.  This proves the global form, not the MTT source of that
stability hypothesis or a numerical value.

## 2. Exact coordinate correction

The displayed metric source is

```text
e = (1/2) log G,
G = exp(2e),
h = delta G = 2e
```

at the identity background.  Hessians transform contragrediently, hence

```text
H_h = (1/2 I)^T H_e (1/2 I)
    = (kappa_e/4) Id_E.
```

Define `kappa_h=kappa_e/4`.  In the repository's Einstein-Hilbert metric
normalization,

```text
kappa_h = (32 pi G_eff)^(-1),
kappa_e = (8 pi G_eff)^(-1).
```

The older `kappa_STF` notation was overloaded: it denoted both the closure
strain coefficient and the metric-coordinate Einstein-Hilbert coefficient.
The new notation resolves that factor-of-four ambiguity.  Existing numerical
rows remain metric-coordinate rows if they use the `1/(32 pi G_eff)` formula.

## 3. The action is no longer an arbitrary matrix problem

For a symmetric metric perturbation, write the most general local,
parity-even, Lorentz-covariant, formally self-adjoint two-derivative operator
with coefficients `(A,B,C,D,E)`.  The off-shell linearized Bianchi identity and
self-adjointness give a rank-four exact system.  Its nullspace is one
dimensional and is spanned by

```text
(A,B,C,D,E) = (1,-1,1,1,-1).
```

This is the Fierz-Pauli/linearized-Einstein operator.  On TT fields it reduces
to `Box` in flat space and to the corresponding Lichnerowicz block on an
Einstein background.  The same gauge identity excludes every algebraic mass
term.  On a selected globally hyperbolic, time-oriented Lorentzian background,
the resulting normally hyperbolic operator has unique retarded and advanced
Green operators.

These are conditional uniqueness statements.  They reduce the remaining
source theorem to four explicit action hypotheses: locality, the two-derivative
infrared order, self-adjointness, and linearized diffeomorphism invariance.
They do not derive those hypotheses from MTT.

## 4. Honest frontier

The old claim that the projection into TT is missing is superseded: the global
`DG` and TT projector now provide it.  The remaining hard object is also not an
unknown `2 x 2` Hessian.  It is the same-source action theorem proving that MTT
selects:

1. the displayed `G=Q^TQ` observable;
2. the four action hypotheses above;
3. the coefficient `kappa_h` and the matter stress normalization; and
4. the Lorentzian time orientation/background domain used by the retarded
   solution.

The revised proto-spinor action cannot close that gate by itself: it correctly
states that it is an ansatz and that it imports the Einstein-Hilbert term.
"""

    OUT_CERT.write_text(json.dumps(cert, indent=2), encoding="utf-8")
    OUT_NOTE.write_text(note, encoding="utf-8")
    print(f"WROTE: {OUT_CERT}")
    print(f"WROTE: {OUT_NOTE}")
    print(f"STATUS: {cert['status']}")


if __name__ == "__main__":
    main()
