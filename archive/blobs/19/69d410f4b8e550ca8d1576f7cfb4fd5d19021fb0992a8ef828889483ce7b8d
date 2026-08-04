"""Build the exact qutrit-to-SM finite-algebra bridge and source-selection gate."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
PROTO = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory\10 ProtoSpinor"
    r"\Closure_Strain_Geometry_and_the_Structure_of_the_Standard_Model_v5.md"
)
SLUG = "selected_samegeometryqutrittosmalgebrabridge_or_generativebasefrontier"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "same_geometry_qutrit_to_sm_algebra_bridge.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_SameGeometryQutritToSMAlgebraBridge_or_GenerativeBaseFrontier_v1.md"
STATUS = "MTT_SELECTED_SAME_GEOMETRY_QUTRIT_TO_SM_ALGEBRA_CONDITIONAL_BRIDGE_CLOSED_SOURCE_SELECTION_OPEN"
NEXT = "MTT_Selected_ClassLaneProjectorsAndWeakRealStructureSourceTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def matrix_payload(matrix: np.ndarray) -> list[list[list[float]]]:
    return [[[float(z.real), float(z.imag)] for z in row] for row in matrix]


def main() -> int:
    package = load(ROOT / "certificates" / "selected_hymoverlapvaluesource_or_qutritspectraltriplepackaging_certificate.json")
    package_detail = load(ROOT / "candidate_data" / "selected_hymoverlapvaluesource_or_qutritspectraltriplepackaging" / "finite_spectral_triple_packaging.packet.json")
    qutrit = load(ROOT / "candidate_data" / "selected_hymoverlapvaluesource_or_qutritspectraltriplepackaging" / "qutrit_weyl_27x27_matrix_realization.packet.json")
    qft = load(ROOT / "certificates" / "selected_renormalizedsmobservablefunctor_fromcommonschemeaction_certificate.json")
    final = load(ROOT / "certificates" / "selected_finalglobaltruesmclosureaudit_aftermultiloopprecision_certificate.json")
    branch = load(ROOT / "certificates" / "selected_branchorbitandretardedrepresentative_or_globalmeasureuniqueness_certificate.json")
    packet_audit = load(ROOT / "certificates" / "actual_selected_sm_packet_anomaly_audit_certificate.json")
    proto_text = PROTO.read_text(encoding="utf-8")

    # The closed qutrit package has three class lanes, each carrying M3(C).
    aq_real_dimension = 3 * 2 * 3 * 3
    aq_center_real_dimension = 3 * 2
    af_real_dimension = 2 + 4 + 2 * 3 * 3
    af_center_real_dimension = 2 + 1 + 2

    p1 = np.diag([1.0, 0.0, 0.0]).astype(complex)
    p2 = np.diag([1.0, 1.0, 0.0]).astype(complex)
    identity2 = np.eye(2, dtype=complex)
    qi = np.array([[1j, 0], [0, -1j]], dtype=complex)
    qj = np.array([[0, 1], [-1, 0]], dtype=complex)
    qk = np.array([[0, 1j], [1j, 0]], dtype=complex)
    quaternion_basis = [identity2, qi, qj, qk]

    expected_products = {
        (1, 1): (-1, 0),
        (2, 2): (-1, 0),
        (3, 3): (-1, 0),
        (1, 2): (1, 3),
        (2, 3): (1, 1),
        (3, 1): (1, 2),
        (2, 1): (-1, 3),
        (3, 2): (-1, 1),
        (1, 3): (-1, 2),
    }
    multiplication_residuals = []
    for (left, right), (sign, target) in expected_products.items():
        residual = np.linalg.norm(quaternion_basis[left] @ quaternion_basis[right] - sign * quaternion_basis[target])
        multiplication_residuals.append(float(residual))

    real_columns = []
    for value in quaternion_basis:
        real_columns.append(np.concatenate([value.real.ravel(), value.imag.ravel()]))
    quaternion_real_rank = int(np.linalg.matrix_rank(np.column_stack(real_columns), tol=1e-12))

    # J=epsilon K. Commutation M epsilon = epsilon conjugate(M) characterizes H in M2(C).
    epsilon = qj
    antiunitary_residuals = [float(np.linalg.norm(value @ epsilon - epsilon @ value.conjugate())) for value in quaternion_basis]
    adjoint_span_residuals = []
    basis_matrix = np.column_stack(real_columns)
    for value in quaternion_basis:
        adjoint = value.conjugate().T
        target = np.concatenate([adjoint.real.ravel(), adjoint.imag.ravel()])
        coeff, *_ = np.linalg.lstsq(basis_matrix, target, rcond=None)
        adjoint_span_residuals.append(float(np.linalg.norm(basis_matrix @ coeff - target)))

    checks = {
        "embedded_renormalized_SM_QFT_recovery_closed": qft["actual_local_QFT_observable_functor_at_parity_profile_standard"],
        "standard_quantization_is_imported_not_MTT_derived": qft["standard_SM_quantization_imported_as_parity_structure"] and not qft["standard_SM_quantization_derived_from_MTT"],
        "declared_standard_true_SM_equivalence_closed": final["true_SM_equivalence_closed_at_declared_standard"],
        "qutrit_finite_spectral_package_closed": package["finite_qutrit_spectral_package_closed"],
        "qutrit_algebra_is_three_M3C_lanes": package_detail["finite_algebra"] == "A_Q = C^3_class tensor M_3(C)_qutrit-left",
        "qutrit_carrier_dimension_is_27": qutrit["carrier_dimension"] == 27,
        "proto_corpus_contains_SM_finite_algebra_as_assumption": "A_F=\\mathbb{C}\\oplus\\mathbb{H}\\oplus M_3(\\mathbb{C})" in proto_text,
        "direct_algebra_isomorphism_rejected_by_real_dimension": aq_real_dimension != af_real_dimension,
        "direct_algebra_isomorphism_rejected_by_center_dimension": aq_center_real_dimension != af_center_real_dimension,
        "rank_one_corner_projector_exact": np.linalg.norm(p1 @ p1 - p1) == 0 and int(np.linalg.matrix_rank(p1)) == 1,
        "rank_two_corner_projector_exact": np.linalg.norm(p2 @ p2 - p2) == 0 and int(np.linalg.matrix_rank(p2)) == 2,
        "quaternion_basis_real_rank_four": quaternion_real_rank == 4,
        "quaternion_multiplication_exact": max(multiplication_residuals) < 1e-15,
        "quaternion_real_structure_exact": max(antiunitary_residuals) < 1e-15,
        "quaternion_adjoint_closure_exact": max(adjoint_span_residuals) < 1e-15,
        "candidate_reduced_algebra_real_dimension_24": 2 + quaternion_real_rank + 18 == 24,
    }
    theorem_proved = all(checks.values())

    source_selection = {
        "three_qutrit_class_lanes_selected": package["finite_qutrit_spectral_package_closed"],
        "rank1_rank2_full_lane_assignment_selected_as_U1_SU2_SU3": False,
        "weak_lane_antiunitary_J_with_J_squared_minus_one_selected": False,
        "existing_antiunitary_q79_orbit_is_sufficient_weak_real_structure": False,
        "SM_finite_algebra_derived_rather_than_assumed": False,
        "chiral_SM_representation_table_emitted_from_bridge": False,
        "anomaly_table_recomputed_on_emitted_representation": False,
        "same_geometry_HYM_overlap_values_bound_to_representation": False,
    }

    packet = {
        "schema": "MTTSelectedSameGeometryQutritToSMAlgebraBridgeOrGenerativeBaseFrontier.v1",
        "status": STATUS,
        "predecessors": [
            "MTT_Selected_HYMOverlapValueSourceTheorem_or_QutritSpectralTriplePackaging_v1",
            "MTT_Selected_RenormalizedSMObservableFunctor_FromCommonSchemeAction_v1",
            "MTT_Selected_FinalGlobalTrueSMClosureAudit_AfterMultiLoopPrecision_v1",
        ],
        "theorem": {
            "name": "QutritClassLaneToSMFiniteAlgebraConditionalReductionAndNoDirectIdentificationTheorem",
            "proved": theorem_proved,
            "statement": "The closed MTT qutrit package A_Q=C^3 tensor M3(C)=M3(C)^3 cannot be identified directly with the Standard-Model finite algebra A_F=C direct-sum H direct-sum M3(C): their real dimensions and center dimensions differ. Nevertheless, a mathematically exact real *-algebra reduction exists across the three class lanes. A rank-one corner of lane 0 gives C; a rank-two corner of lane 1, fixed by the antiunitary symplectic real structure J=epsilon K, gives H; and the full lane 2 gives M3(C). The resulting real algebra has dimension 24 and is isomorphic to A_F. This closes the conditional algebra bridge, not its MTT source selection, representation action, anomaly table, or HYM value map.",
        },
        "already_closed_recovery_scope": {
            "embedded_local_renormalized_QFT_functor": True,
            "functor": "Readout o LSZ o Green o Q_SM o E_SM",
            "perturbative_observable_equivalence": True,
            "unitarity_locality_renormalization_role": "inherited from the imported standard gauge-fixed renormalized SM QFT on the embedded branch",
            "anomaly_free_role": "required/admitted at parity interface; actual no-knob selected representation/anomaly packet remains open",
            "standard_BRST_path_integral_derived_from_MTT": False,
            "constructive_nonperturbative_4D_QFT_closed": False,
        },
        "direct_identification_no_go": {
            "source_algebra": "A_Q = M3(C) direct-sum M3(C) direct-sum M3(C)",
            "target_algebra": "A_F = C direct-sum H direct-sum M3(C)",
            "A_Q_real_dimension": aq_real_dimension,
            "A_F_real_dimension": af_real_dimension,
            "A_Q_center_real_dimension": aq_center_real_dimension,
            "A_F_center_real_dimension": af_center_real_dimension,
            "direct_real_star_algebra_isomorphism_possible": False,
            "reason": "Both total real dimension and center real dimension are invariants and disagree.",
        },
        "conditional_same_geometry_bridge": {
            "lane_0": "p1 M3(C) p1 ~= C with p1=diag(1,0,0)",
            "lane_1": "(p2 M3(C) p2)^J ~= H with p2=diag(1,1,0), J=epsilon K, epsilon=[[0,1],[-1,0]]",
            "lane_2": "M3(C) retained as the color algebra",
            "result": "A_SM^cand = C direct-sum H direct-sum M3(C)",
            "result_real_dimension": 24,
            "p1": matrix_payload(p1),
            "p2": matrix_payload(p2),
            "quaternion_basis": [matrix_payload(value) for value in quaternion_basis],
            "quaternion_real_rank": quaternion_real_rank,
            "max_quaternion_multiplication_residual": max(multiplication_residuals),
            "max_antiunitary_fixed_residual": max(antiunitary_residuals),
            "max_adjoint_span_residual": max(adjoint_span_residuals),
            "mathematical_bridge_closed": theorem_proved,
            "selected_as_physical_MTT_SM_algebra": False,
        },
        "source_checks": checks,
        "source_selection_frontier": source_selection,
        "old_packet_audit_context": {
            "actual_selected_representation_packet_was_open": packet_audit["what_remains_open"]["actual_selected_representation_packet"],
            "actual_anomaly_table_was_open": packet_audit["what_remains_open"]["actual_anomaly_table_on_selected_packet"],
            "antiunitary_branch_orbit_members": branch["selected_antiunitary_orbit_members"],
            "why_existing_antiunitary_is_not_enough": "The q79 antiunitary orbit selects retarded/conjugate orientation; it is not yet a weak-lane real structure satisfying the finite spectral-triple representation axioms.",
        },
        "generative_base_acceptance_test": {
            "required_next_fields": [
                "select the class-lane assignment and p1/p2/full projectors from native 10D geometry before SM labels enter",
                "derive a weak-lane antiunitary J with J^2=-1 and prove its fixed algebra is the physical H lane",
                "construct the chiral Hilbert representation of C direct-sum H direct-sum M3(C)",
                "derive hypercharge/unimodularity and three-family multiplicity from the same packet",
                "machine-check local, mixed, gravitational and Witten anomalies on that emitted representation",
                "bind the selected HYM overlap operator to the same representation and emit held-out values",
            ],
            "same_geometry_generative_base_closed": False,
            "next_single_target": NEXT,
        },
        "epistemic_policy": {
            "observed_SM_values_used": False,
            "SM_representation_table_imported_into_bridge": False,
            "proto_SM_algebra_treated_as_derived": False,
            "direct_27_equals_SM_claim_rejected": True,
            "embedded_QFT_recovery_reopened": False,
        },
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_SameGeometryQutritToSMAlgebraBridge_or_GenerativeBaseFrontier_v1",
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "embedded_local_QFT_recovery_closed": True,
        "standard_quantization_imported": True,
        "direct_qutrit_equals_SM_algebra_rejected": True,
        "conditional_C_H_M3_bridge_closed": theorem_proved,
        "candidate_SM_algebra_real_dimension": 24,
        "class_lane_assignment_selected": source_selection["rank1_rank2_full_lane_assignment_selected_as_U1_SU2_SU3"],
        "weak_real_structure_selected": source_selection["weak_lane_antiunitary_J_with_J_squared_minus_one_selected"],
        "representation_and_anomaly_packet_closed": False,
        "same_geometry_generative_base_closed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Same-Geometry Qutrit-to-SM Algebra Bridge or Generative-Base Frontier v1

## Recovery Already Closed

The low-energy local-QFT statement is already closed at the declared standard:

```text
Obs_SM^MTT = Readout o LSZ o Green o Q_SM o E_SM.
```

On the embedded branch, `E_SM` gives the same gauge-fixed renormalized SM
action and parameter point, and `Q_SM` imports standard BRST/Faddeev-Popov
quantization. Perturbative observables therefore agree order by order. This is
an embedding/recovery theorem. It does not derive standard quantization or the
SM action from native MTT geometry.

## Exact New Bridge

The closed finite MTT package is

```text
A_Q = C^3_class tensor M3(C) = M3(C) direct-sum M3(C) direct-sum M3(C),
dim_R(A_Q)=54, dim_R(Z(A_Q))=6.
```

The proto-spinor SM encoding assumes

```text
A_F = C direct-sum H direct-sum M3(C),
dim_R(A_F)=24, dim_R(Z(A_F))=5.
```

The unequal invariants prove that `A_Q` cannot simply be renamed `A_F`.
However the three class lanes admit the exact real-star-algebra reduction

```text
lane 0: p1 M3(C) p1 ~= C,                 rank(p1)=1,
lane 1: (p2 M3(C) p2)^J ~= H,             rank(p2)=2,
lane 2: M3(C),
J = epsilon K, epsilon=[[0,1],[-1,0]].
```

The quaternion basis has real rank `{quaternion_real_rank}`; multiplication,
antiunitary-fixed and adjoint-closure residuals are respectively
`{max(multiplication_residuals)}`, `{max(antiunitary_residuals)}` and
`{max(adjoint_span_residuals)}`. Thus the conditional reduced algebra is
exactly `C direct-sum H direct-sum M3(C)`.

## Frontier

MTT has not yet selected the rank-1/rank-2/full lane assignment as the physical
U(1)/SU(2)/SU(3) packet, nor selected the weak-lane antiunitary `J`. The existing
q79 antiunitary theorem concerns retarded/conjugate branch orientation and
cannot be silently reused as the quaternionic weak real structure.

The next theorem must select those projectors and `J` from native 10D geometry
before SM labels or measured values enter. It must then emit the chiral
representation and anomaly table. This is the shortest current path from the
closed embedding theorem to a genuinely generative MTT base.

Next artifact: `{NEXT}`.
"""

    dump(PACKET, packet)
    dump(CANDIDATE, packet)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
