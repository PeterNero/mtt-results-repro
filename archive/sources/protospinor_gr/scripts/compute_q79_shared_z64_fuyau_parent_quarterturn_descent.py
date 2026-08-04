from __future__ import annotations

import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
TEXPAPERS = ROOT.parent
SM_REPO = TEXPAPERS / "mtt-sm-parity-closure"

SAME_CIRCLE = (
    ROOT / "certificates" / "same_circle_weight2_bundle_obstruction_certificate.json"
)
QUARTERTURN_HESSIAN = (
    ROOT
    / "certificates"
    / "q79_complement_quarterturn_hessian_scalarization_certificate.json"
)
FUYAU_TOPOLOGY = (
    SM_REPO
    / "candidate_data"
    / "selected_q79nonpullbackchiralvisiblebundleandfullsu9holonomyselection"
    / "rank_one_fuyau_shared_circle_clutching.packet.json"
)
FUYAU_SOURCE_GATE = (
    SM_REPO
    / "candidate_data"
    / "selected_q79hiddenbundleexistencebianchiallocationandspectrumexecution"
    / "rank_one_fuyau_k3_lattice_and_bianchi_allocation.packet.json"
)
CHERN_ORBIT = (
    SM_REPO
    / "candidate_data"
    / "selected_q79markedk3ellipticperiodsourceandgerbezeroexecution"
    / "Z4_Chern_orbit_superset.packet.json"
)
COMPLEX_NESTING_GATE = (
    SM_REPO
    / "candidate_data"
    / "selected_q79markedk3ellipticperiodsourceandgerbezeroexecution"
    / "complex_nesting_and_retarded_bridge_gate.packet.json"
)
FOUNDATION_V8 = (
    TEXPAPERS
    / "3 Core Foundations"
    / "revised_tex_vnext"
    / "Modal_Triplet_Theory__Foundation_v8"
    / "main.tex"
)

OUT_CERT = (
    ROOT
    / "certificates"
    / "q79_shared_z64_fuyau_parent_quarterturn_descent_certificate.json"
)
OUT_NOTE = (
    ROOT
    / "proof_corpus"
    / "q79_Shared_Z64_FuYau_Parent_QuarterTurn_and_Descent_Dichotomy_v1.md"
)


def load(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def order_mod_n(element: int, modulus: int) -> int:
    return modulus // math.gcd(element, modulus)


def generated_subgroup(element: int, modulus: int) -> tuple[int, ...]:
    return tuple(sorted({(power * element) % modulus for power in range(modulus)}))


def character_restriction_exponents(
    character_label: int, subgroup_generator: int, modulus: int
) -> list[int]:
    """Return exponents r with chi(g^m)=i^r for the order-four subgroup."""
    return [
        ((character_label * subgroup_generator * power) % modulus) // 16
        for power in range(4)
    ]


def symbolic_chern_orbit(generator: sp.Matrix) -> list[list[int]]:
    vector = sp.Matrix([1, 0])
    orbit = []
    for _ in range(4):
        orbit.append([int(vector[0]), int(vector[1])])
        vector = generator * vector
    return orbit


def packet_orbit_to_coefficients(orbit: list[list[object]]) -> list[list[int]]:
    coefficients = []
    for first, second in orbit:
        row = []
        for value in (first, second):
            if value == "delta":
                row.append(1)
            elif value == "-delta":
                row.append(-1)
            elif value == 0:
                row.append(0)
            else:
                raise ValueError(f"unexpected Chern-orbit value: {value}")
        coefficients.append(row)
    return coefficients


def main() -> None:
    same_circle = load(SAME_CIRCLE)
    quarterturn_hessian = load(QUARTERTURN_HESSIAN)
    fuyau_topology = load(FUYAU_TOPOLOGY)
    fuyau_source_gate = load(FUYAU_SOURCE_GATE)
    chern_orbit = load(CHERN_ORBIT)
    complex_gate = load(COMPLEX_NESTING_GATE)
    foundation_text = FOUNDATION_V8.read_text(encoding="utf-8", errors="replace")

    modulus = 64
    order_four_elements = [
        element for element in range(modulus) if order_mod_n(element, modulus) == 4
    ]
    order_four_subgroups = {
        generated_subgroup(element, modulus) for element in order_four_elements
    }
    subgroup = tuple(sorted(next(iter(order_four_subgroups))))
    positive_generator = 16
    negative_generator = 48

    root_labels = same_circle["finite_Z64_result"]["square_root_character_labels"]
    root_restrictions = {
        str(label): character_restriction_exponents(
            label, positive_generator, modulus
        )
        for label in root_labels
    }
    tt_label = same_circle["finite_Z64_result"]["TT_character_label"]
    tt_restriction = character_restriction_exponents(
        tt_label, positive_generator, modulus
    )

    j2 = sp.Matrix([[0, -1], [1, 0]])
    j6 = sp.kronecker_product(j2, sp.eye(3))
    packet_j2 = sp.Matrix(chern_orbit["generator"]["J"])
    computed_orbit = symbolic_chern_orbit(j2)
    packet_orbit = packet_orbit_to_coefficients(chern_orbit["orbit"])

    # A free C4 orbit constrains a family only by conjugacy.  This explicit
    # anisotropic branch Hessian extends covariantly around the whole orbit.
    h0 = sp.diag(1, 1, 1, 2, 2, 2)
    orbit_hessians = [
        sp.simplify((j6**power) * h0 * (j6 ** (-power)))
        for power in range(4)
    ]
    covariance_residuals = [
        sp.simplify(
            orbit_hessians[(power + 1) % 4]
            - j6 * orbit_hessians[power] * j6.inv()
        )
        for power in range(4)
    ]
    branch_commutator = sp.simplify(h0 * j6 - j6 * h0)

    # If the four branch labels are instead reduced as Lens redundancy and the
    # operator descends to one branch-independent representative, covariance
    # becomes H=JHJ^{-1}, exactly the internal quarter-turn condition.
    h00, h01, h11 = sp.symbols("h00 h01 h11", real=True)
    physical_block = sp.Matrix([[h00, h01], [h01, h11]])
    descent_equations = list(sp.simplify(physical_block * j2 - j2 * physical_block))
    coefficient_matrix, _ = sp.linear_eq_to_matrix(
        descent_equations, [h00, h01, h11]
    )
    descent_nullspace = coefficient_matrix.nullspace()

    source_guard = fuyau_source_gate["source_guard"]
    checks = {
        "Z64_has_unique_order4_subgroup": len(order_four_subgroups) == 1
        and subgroup == (0, 16, 32, 48),
        "order4_generators_are_plusminus16": order_four_elements == [16, 48],
        "both_weight1_roots_restrict_to_same_plus_i_character": (
            root_restrictions == {"1": [0, 1, 2, 3], "33": [0, 1, 2, 3]}
        ),
        "root_ratio_is_trivial_on_order4_subgroup": (33 - 1) % 4 == 0,
        "TT_weight2_restricts_to_sign_character": tt_restriction == [0, 2, 0, 2],
        "realified_order4_character_is_integral_quarterturn": (
            j2**2 == -sp.eye(2)
            and j2**4 == sp.eye(2)
            and j2.det() == 1
            and packet_j2 == j2
        ),
        "integral_quarterturn_generates_exact_A107_Chern_orbit": (
            computed_orbit == packet_orbit
        ),
        "active_rank_one_topology_contains_shared_untwisted_circle": (
            fuyau_topology["rank_one_FuYau_topology"]["space"]
            == "X=P_delta x S1_shared"
            and fuyau_topology["rank_one_FuYau_topology"]["reason"]
            .startswith("The second Fu-Yau circle has zero Chern class")
        ),
        "primitive_shared_circle_to_FuYau_source_is_still_open": (
            source_guard["corpus_identifies_it_with_the_untwisted_FuYau_circle"]
            is False
        ),
        "A107_parent_cost_and_gerbe_data_are_C4_covariant": (
            chern_orbit["Bianchi_and_cost"]["continuous_parameter_added"] == 0
            and chern_orbit["Bianchi_and_cost"]["each_curvature_norm_cost"] == 4
            and chern_orbit["gerbe_execution_covariance"]["zero_invariant"]
            is True
            and chern_orbit["gerbe_execution_covariance"][
                "transversality_invariant"
            ]
            is True
        ),
        "free_orbit_covariance_counterexample_is_exact": (
            all(residual == sp.zeros(6) for residual in covariance_residuals)
            and branch_commutator != sp.zeros(6)
            and all(matrix == matrix.T for matrix in orbit_hessians)
        ),
        "free_orbit_covariance_preserves_all_six_branch_coefficients": (
            quarterturn_hessian["finite_data"][
                "single_branch_self_adjoint_S3_commutant_dimension"
            ]
            == 6
        ),
        "autonomous_descent_forces_scalar_physical_block": (
            len(descent_nullspace) == 1
            and descent_nullspace[0] == sp.Matrix([1, 0, 1])
        ),
        "internal_quarterturn_scalarization_was_already_closed": (
            quarterturn_hessian["claim_tiers"][
                "self_adjoint_S3_quarterturn_Hessian_scalarization"
            ]
            == "CLOSED_EXACT"
        ),
        "Foundation_v8_supplies_exact_autonomous_descent_criterion": (
            "Autonomous descent criterion" in foundation_text
            and "r(\\Phi x)=r(\\Phi x')" in foundation_text
        ),
        "retarded_representative_selector_is_not_cross_promoted": (
            complex_gate["U9_retarded_import"]["typed_map_to_Z4_Chern_orbit"]
            is False
        ),
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"failed checks: {failed}")

    certificate = {
        "certificate": "q79_shared_z64_fuyau_parent_quarterturn_descent",
        "date": "2026-07-15",
        "program": "MTT protospinor GR response proof",
        "status": "Q79_SHARED_Z64_FUYAU_PARENT_QUARTERTURN_CLOSED_CONDITIONAL_FREE_ORBIT_HESSIAN_INFERENCE_NOGO_LENS_DESCENT_OR_DIRECT_HYM_OPEN",
        "inputs": {
            "same_circle_weight2": str(SAME_CIRCLE),
            "quarterturn_Hessian_scalarization": str(QUARTERTURN_HESSIAN),
            "rank_one_FuYau_topology": str(FUYAU_TOPOLOGY),
            "rank_one_FuYau_source_gate": str(FUYAU_SOURCE_GATE),
            "A107_Chern_orbit": str(CHERN_ORBIT),
            "complex_nesting_gate": str(COMPLEX_NESTING_GATE),
            "Foundation_v8": str(FOUNDATION_V8),
        },
        "checks": checks,
        "finite_data": {
            "Z64_order4_subgroup": list(subgroup),
            "Z64_order4_generators": order_four_elements,
            "weight1_root_restriction_i_exponents": root_restrictions,
            "weight2_restriction_i_exponents": tt_restriction,
            "integral_quarterturn": [[int(value) for value in row] for row in j2.tolist()],
            "Chern_orbit_coefficients_of_delta": computed_orbit,
            "free_orbit_covariant_H0": [[int(value) for value in row] for row in h0.tolist()],
            "free_orbit_H0_commutator_rank": int(branch_commutator.rank()),
            "single_branch_equivariant_Hessian_dimension": 6,
            "free_orbit_covariant_Hessian_family_dimension": 6,
            "Lens_descent_physical_block_dimension": 1,
            "Lens_descent_physical_block": "H_std=kappa_standard*I2",
        },
        "theorem": {
            "name": "SharedZ64FuYauParentQuarterTurnAndDescentDichotomy",
            "part_A_root_independent_finite_source": {
                "statement": (
                    "The unique C4 subgroup <16> of Z64 is seen identically by "
                    "chi_1 and chi_33. Its realification is the integral quarter-turn "
                    "J=[[0,-1],[1,0]], so no odd-root choice is required."
                ),
                "parameter_count": 0,
            },
            "part_B_active_FuYau_parent": {
                "statement": (
                    "Conditional on the active topology X=P_delta x S1_shared, J "
                    "acts on the vertical integral T2 lattice and transports the Chern "
                    "pair around the exact minimal four-branch A107 orbit. It is an "
                    "automorphism of the parent family, not of one rank-one branch."
                ),
                "primitive_source_boundary": (
                    "The older A102 source gate still does not derive from primitive "
                    "MTT that S1_shared is the untwisted Fu-Yau factor."
                ),
            },
            "part_C_covariance_no_go": {
                "statement": (
                    "C4 covariance on a free four-branch orbit does not imply that the "
                    "Hessian at one selected branch commutes with J. Evaluation at one "
                    "branch is a bijection from covariant families to arbitrary branch "
                    "Hessians, so all six self-adjoint S3 coefficients survive."
                ),
                "counterexample": (
                    "H0=diag(I3,2I3) does not commute with J_DE, while "
                    "Hm=J_DE^m H0 J_DE^-m is an exact C4-covariant family."
                ),
            },
            "part_D_Lens_descent_exit": {
                "statement": (
                    "If the four Chern orientations are typed as Lens redundancy and "
                    "the selected HYM operator descends autonomously to the quotient, "
                    "branch-independence plus covariance gives [H,J_DE]=0. The prior "
                    "commutant theorem then forces H_std=kappa_standard I2."
                ),
                "alternative": (
                    "If the four orientations are physical retarded/superselection "
                    "branches, quotient descent is unavailable and the actual projected "
                    "HYM block must be computed directly."
                ),
            },
        },
        "claim_tiers": {
            "shared_Z64_unique_order4_subgroup": "CLOSED_EXACT",
            "odd_root_restriction_to_order4_subgroup": "CLOSED_EXACT_ROOT_INDEPENDENT",
            "active_rank_one_FuYau_parent_integral_C4_action": "CLOSED_CONDITIONAL_ON_ACTIVE_TOPOLOGY_TYPING",
            "minimal_four_branch_FuYau_parent": "CLOSED_EXACT",
            "parent_orbit_cost_Bianchi_gerbe_covariance": "CLOSED_CONDITIONAL_ON_SELECTED_PARENT",
            "free_orbit_covariance_implies_single_branch_Hessian_invariance": "CLOSED_NO_GO",
            "autonomous_Lens_quotient_descent_implies_quarterturn_invariance": "CLOSED_EXACT_CONDITIONAL",
            "physical_TT_scalarization_under_Lens_descent": "CLOSED_EXACT_CONDITIONAL",
            "primitive_MTT_shared_circle_to_FuYau_source": "OPEN",
            "MTT_types_C4_as_Lens_redundancy_not_physical_superselection": "OPEN",
            "typed_retarded_representative_selector": "OPEN",
            "actual_inverse_Fourier_Mukai_HYM_operator": "OPEN",
        },
        "guardrails": {
            "claims_active_rank_one_topology_is_primitive_MTT_selected": False,
            "claims_free_orbit_covariance_scalarizes_one_branch": False,
            "claims_C4_parent_action_is_single_branch_automorphism": False,
            "claims_odd_root_or_retarded_orientation_selected": False,
            "claims_actual_HYM_operator_computed": False,
            "uses_observed_physics_data": False,
            "adds_fitted_numeric_parameter": False,
        },
        "note_written": str(OUT_NOTE),
    }

    note = r"""# q79 Shared-Z64 Fu-Yau Parent Quarter-Turn and Descent Dichotomy v1

Status:
`Q79_SHARED_Z64_FUYAU_PARENT_QUARTERTURN_CLOSED_CONDITIONAL_FREE_ORBIT_HESSIAN_INFERENCE_NOGO_LENS_DESCENT_OR_DIRECT_HYM_OPEN`

## Exact finite source

The selected shared finite carrier already contains a canonical order-four
sector. The cyclic group `Z64` has one and only one subgroup of order four:

```text
C4=<16>={0,16,32,48}.
```

The two still-possible odd character roots are `chi_1` and `chi_33`. On this
subgroup they agree exactly:

```text
chi_1(16m)=chi_33(16m)=i^m.
```

Their ratio `chi_32` is trivial there. The realification of this character on
the oriented integral rank-two lattice is

```text
J=[[0,-1],[1,0]],
J^2=-I,
J^4=I.
```

Thus the order-four source is root-independent and introduces no numerical
parameter. Reversing the generator replaces `J` by `-J` and reverses the orbit;
it does not change the parent set or the Hessian commutant.

## Fu-Yau parent action

At the active rank-one topology tier,

```text
X=P_delta x S1_shared,
```

the two vertical circle directions form an integral `T2` lattice with Chern
pair `(delta,0)`. Acting by `J` gives

```text
(delta,0) -> (0,delta) -> (-delta,0) -> (0,-delta).
```

This is exactly the A107 minimal Chern orbit. It closes the integral lattice
action on the four-branch parent and explains the square-fiber `tau=i`
candidate without choosing between `chi_1` and `chi_33`.

The scope is conditional. The A102 source guard still says that primitive MTT
has not selected the identification of `S1_shared` with the untwisted Fu-Yau
circle. The action above is an automorphism of the four-branch parent family,
not of the single branch `(delta,0)`.

## New no-go: covariance is not invariance

This distinction matters for the HYM Hessian. Let `J_DE` be the canonical
quarter-turn on the diagonal/edge strain multiplicity plane. A covariant
operator family on the four branches obeys

```text
H_{m+1}=J_DE H_m J_DE^{-1}.
```

Every self-adjoint `S3`-equivariant `H_0` extends uniquely by this formula.
Therefore free-orbit covariance retains all six branch Hessian coefficients;
it does not imply `[H_0,J_DE]=0`. The exact counterexample is

```text
H_0=diag(I3,2I3),
H_m=J_DE^m H_0 J_DE^{-m}.
```

The family is perfectly `C4`-covariant, but `H_0` is anisotropic and does not
commute with `J_DE`. Consequently the Fu-Yau parent orbit by itself cannot be
used to claim `H_std=kappa_standard I2` on our observed branch.

## The exact dichotomy

There are now two mathematically distinct exits.

### Lens-redundancy exit

If the four Chern orientations are alternative representatives of one reduced
state, the quarter-turn is genuinely Lens-type redundancy. Foundation v8's
autonomous-descent criterion then requires the HYM operator to be constant on
the reduction fibers. Combining branch-independence with covariance gives

```text
[H,J_DE]=0.
```

The complement-quarterturn theorem then closes

```text
H_std=kappa_standard I2,
h_DE=0,
h_DD=h_EE=kappa_standard>0.
```

### Physical-branch exit

If the four orientations are physical retarded or superselection branches,
they are not quotient redundancy. Covariance relates their Hessians but does
not scalarize any one of them. The selected inverse-Fourier-Mukai/HYM operator
must then be constructed and its `2x2` block computed directly.

## Remaining decision

The old broad source theorem has been replaced by a sharper binary theorem:

```text
prove the C4 parent is Lens redundancy with autonomous HYM descent,
or treat it as physical branch data and calculate H_std directly.
```

Primitive shared-circle/Fu-Yau selection, the typed retarded representative,
and the actual balanced-HYM operator remain open. No observed datum and no
fitted parameter enters this result.
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
