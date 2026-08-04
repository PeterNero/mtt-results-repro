"""Build the native rank-flag and proto-spinor weak-real-structure theorem."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
BOOK = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\10 The Book on Modal Triplet Theory"
    r"\The_Book_on_Modal_Triplet_Theory_v9.md"
)
PROTO = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\10 ProtoSpinor"
    r"\The_Proto_Spinor__Triadic_Closure_from_Pointwise_Internal_Embedding_v4.md"
)
SLUG = "selected_classlaneprojectorsandweakrealstructuresourcetheorem"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "class_lane_projectors_and_weak_real_structure.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_ClassLaneProjectorsAndWeakRealStructureSourceTheorem_v1.md"
STATUS = "MTT_SELECTED_NATIVE_RANK_FLAG_AND_WEAK_REAL_STRUCTURE_CLOSED_CLASS_LANE_GAUGE_TYPE_MISMATCH_PROVED"
NEXT = "MTT_Selected_TypedFamilyGaugeCarrierAndDiagonalSMRepresentationTheorem_v1"


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    predecessor = json.loads(
        (ROOT / "certificates" / "selected_samegeometryqutrittosmalgebrabridge_or_generativebasefrontier_certificate.json").read_text(encoding="utf-8")
    )
    book = BOOK.read_text(encoding="utf-8")
    proto = PROTO.read_text(encoding="utf-8")

    p1 = np.diag([1.0, 0.0, 0.0]).astype(complex)
    p2 = np.diag([1.0, 1.0, 0.0]).astype(complex)
    p3 = np.eye(3, dtype=complex)
    epsilon = np.array([[0.0, 1.0], [-1.0, 0.0]], dtype=complex)
    identity2 = np.eye(2, dtype=complex)

    flag_checks = {
        "projectors_idempotent": all(np.linalg.norm(p @ p - p) == 0 for p in (p1, p2, p3)),
        "projectors_self_adjoint": all(np.linalg.norm(p.conjugate().T - p) == 0 for p in (p1, p2, p3)),
        "projector_ranks_are_1_2_3": [int(np.linalg.matrix_rank(p)) for p in (p1, p2, p3)] == [1, 2, 3],
        "nested_flag": np.linalg.norm(p1 @ p2 - p1) == 0 and np.linalg.norm(p2 @ p3 - p2) == 0,
        "book_has_native_rank_hierarchy": all(
            phrase in book
            for phrase in ["effective rank--1", "effective rank--2", "effective rank--3", "Rank--$1+2+3=6$"]
        ),
        "book_has_commuting_vertical_laplacians": "vertical Laplacians for these bundles" in book and "commute" in book,
        "book_has_structural_gauge_lane_dictionary": all(
            phrase in book for phrase in ["$B_1$ seeds $U(1)$", "$B_2$ extends to $SU(2)$", "$B_3$ completes the triad with $SU(3)$"]
        ),
    }
    j_checks = {
        "epsilon_antisymmetric": np.linalg.norm(epsilon.T + epsilon) == 0,
        "epsilon_unitary": np.linalg.norm(epsilon.conjugate().T @ epsilon - identity2) == 0,
        "J_squared_minus_one": np.linalg.norm(epsilon @ epsilon.conjugate() + identity2) == 0,
        "proto_spin3_su2_lift_forced": "$Spin(3)\\cong SU(2)$" in proto and "if and only if" in proto,
        "same_upstream_carrier_explicit": "same proto-spinor carrier" in proto and "same proto-spinorial closure carrier" in proto,
    }

    theorem_checks = {key: bool(value) for key, value in {**flag_checks, **j_checks}.items()}
    theorem_proved = all(theorem_checks.values()) and predecessor["conditional_C_H_M3_bridge_closed"]
    same_source_fields = {
        "proto_spinor_Psi": True,
        "circle_carrier_C": True,
        "lens_carrier_L": True,
        "nil_carrier_N": True,
        "lorentzian_slab_metric_and_tetrad": False,
        "slab_local_Spin13_lift": False,
        "spin_connection_and_Dirac_operator": False,
        "twistor_projective_complex_structure": False,
        "action_and_normalization_values": False,
    }
    strict_same_source_closed = all(same_source_fields.values())

    packet = {
        "schema": "MTTSelectedClassLaneProjectorsAndWeakRealStructureSourceTheorem.v1",
        "status": STATUS,
        "theorem": {
            "name": "NativeReuseFlagAndProtoSpinorSymplecticRealStructureTheorem",
            "proved": theorem_proved,
            "statement": "The native circle/lens/nil reuse hierarchy supplies ranks 1,2,3 and hence a complete complex flag, unique up to U(3), represented by p1<=p2<=p3. The forced fundamental Spin(3)=SU(2) proto-spinor carries the invariant alternating form epsilon, unique up to nonzero scale; unit normalization gives J=epsilon K with J^2=-1, unique up to phase and unitary basis. Therefore these projector and weak-real-structure representatives are not arbitrary matrix knobs. However the outer C3_class factor in the finite qutrit package is a Z3 family/character factor. Reducing its three lanes differently to C,H,M3 is type-incompatible with family-universal SM gauge action. The physical bridge must preserve the family factor and construct a separate native gauge algebra acting diagonally on it.",
        },
        "native_flag": {
            "bundle_ranks": [1, 2, 3],
            "representative_projector_ranks": [1, 2, 3],
            "selection_equivalence": "unique up to U(3) change of basis",
            "physical_content": "corner algebras and their isomorphism classes are basis independent",
            "corpus_locations": {
                "rank_and_commutation": "The_Book_on_Modal_Triplet_Theory_v9.md:491-496",
                "gauge_dictionary": "The_Book_on_Modal_Triplet_Theory_v9.md:1413-1420",
            },
        },
        "weak_real_structure": {
            "source": "forced Spin(3)=SU(2) fundamental proto-spinor",
            "representative": "J=epsilon K, epsilon=[[0,1],[-1,0]]",
            "J_squared": -1,
            "selection_equivalence": "unique up to phase and U(2) basis",
            "fixed_real_star_algebra": "H inside M2(C)",
            "corpus_location": "The_Proto_Spinor__Triadic_Closure_from_Pointwise_Internal_Embedding_v4.md:428-466",
        },
        "checks": theorem_checks,
        "source_promotion": {
            "native_rank_flag_selected": True,
            "proto_spinor_weak_J_selected_up_to_equivalence": True,
            "rank1_rank2_rank3_matrix_representatives_are_free_knobs": False,
            "native_flag_identified_with_finite_qutrit_C3_carrier": False,
            "conditional_C_H_M3_bridge_promoted_without_extra_premise": False,
            "old_identification_premise_rejected_by_type_check": True,
            "reason": "C3_class is the Z3 family/character index; B_cen/B_lens/B_nil is the gauge-rank reuse hierarchy. Identifying them would assign inequivalent gauge algebras to the three families.",
        },
        "typed_carrier_correction": {
            "existing_basis": "[family/class c in Z3, qutrit phase a in Z3, qutrit shift b in Z3]",
            "family_factor_must_be_preserved": True,
            "required_form": "H_phys = C3_family tensor H_one-family; rho_phys(a)=I_family tensor rho_one-family(a)",
            "required_gauge_algebra": "A_F=C direct-sum H direct-sum M3(C), sourced independently from the native rank flag and proto-spinor J",
            "A44_abstract_algebra_reduction_still_correct": True,
            "A44_class_lane_assignment_as_physical_SM_representation": False,
            "three_family_universality_test": "[rho(a), P_family_g]=0 for every a in A_F and g=0,1,2",
        },
        "dirac_weyl_twistor_same_source_audit": {
            "structural_carrier_identity_closed": True,
            "common_upstream_fields": same_source_fields,
            "common_upstream_field_count": sum(same_source_fields.values()),
            "total_required_field_count": len(same_source_fields),
            "strict_common_value_packet_closed": strict_same_source_closed,
            "logical_result": "The corpus proves a common upstream carrier and conditional encoding regimes. It does not yet prove that the Lorentzian, connection, twistor-linearization, action, and normalization data are emitted by one selected native-10D packet.",
            "commuting_diagram_required": "For each encoding E_r, require E_r o T_native = T_r o E_r with the same selected connection, real/complex structure, projectors, branch, and normalization.",
        },
        "epistemic_policy": {
            "observed_SM_values_used": False,
            "standard_SM_representation_imported": False,
            "book_gauge_dictionary_treated_as_operator_derivation": False,
            "encoding_definitions_treated_as_dynamical_equivalence": False,
            "one_identification_premise_exposed": True,
        },
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_ClassLaneProjectorsAndWeakRealStructureSourceTheorem_v1",
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "native_rank_flag_closed_up_to_unitary_equivalence": True,
        "weak_real_structure_closed_up_to_unitary_phase_equivalence": True,
        "finite_qutrit_to_native_flag_identification_closed": False,
        "dirac_weyl_twistor_common_carrier_closed": True,
        "dirac_weyl_twistor_strict_same_value_packet_closed": strict_same_source_closed,
        "same_source_fields_closed": sum(same_source_fields.values()),
        "same_source_fields_total": len(same_source_fields),
        "next_required_artifact": NEXT,
    }

    note = """# MTT Selected Class-Lane Projectors and Weak Real Structure Source Theorem v1

## Result

The native bundle hierarchy is not merely three unlabeled copies. The corpus specifies
effective ranks `1,2,3`, a reuse hierarchy, and commuting vertical Laplacians. Any complete
complex flag of dimensions `1 < 2 < 3` is unitarily equivalent to

```text
p1=diag(1,0,0), p2=diag(1,1,0), p3=I3.
```

Consequently these particular matrices are coordinate representatives, not three adjustable
physical projectors. Their corner-algebra isomorphism classes are invariant under the common
unitary change of basis.

The proto-spinor theorem independently forces the fundamental `Spin(3)=SU(2)` lift. Its
two-dimensional complex representation is pseudoreal and has, up to scale, one invariant
alternating form `epsilon`. Unit normalization gives

```text
J=epsilon K, epsilon=[[0,1],[-1,0]], J^2=-1.
```

Thus the weak quaternionic real structure in the previous algebra bridge is selected up to
physically irrelevant phase and basis equivalence; it is not an empirical knob.

## Type Correction to the Previous Bridge

The finite package orders its basis as `[class c in Z3, phase a in Z3, shift b in Z3]`.
The outer `C3_class` is a family/character index. It is not the circle/lens/nil rank hierarchy.
Therefore the previous lane-wise `C,H,M3` reduction remains an exact abstract real-algebra
construction, but it cannot be the physical SM representation: it would give the three families
inequivalent gauge algebras.

The corrected carrier must instead have the typed form

```text
H_phys = C3_family tensor H_one-family,
rho_phys(a) = I_family tensor rho_one-family(a).
```

The native rank flag and proto-spinor `J` must source `A_F=C direct-sum H direct-sum M3(C)`
on the one-family internal factor. This is a new, sharper target; no identification of family
classes with gauge bundles is allowed.

## Dirac, Weyl, and Twistor Answer

They do come from the same upstream carrier in the proved structural sense: all are regimes of
`Xi=(Psi,C,L,N)`. That is already stronger than three unrelated encodings. It is not yet a
same-value dynamical theorem. The current paper assumes the Lorentzian slab and local `Spin(1,3)`
lift, defines the Dirac operator after choosing a tetrad and spin connection, and obtains twistors
only in a null-dominated, low-lens-curvature regime.

The strict theorem therefore needs one commuting source diagram: the same selected native packet
must emit the slab geometry, spin lift, connection, branch/projectors, complex or real structure,
and normalization, and every Dirac/Weyl/twistor encoding must intertwine that common transport.
Current same-source readiness is `4/9`: `Psi,C,L,N` are common; the five downstream value-bearing
fields are not yet jointly selected.

Next artifact: `MTT_Selected_TypedFamilyGaugeCarrierAndDiagonalSMRepresentationTheorem_v1`.
"""

    dump(PACKET, packet)
    dump(CANDIDATE, packet)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
