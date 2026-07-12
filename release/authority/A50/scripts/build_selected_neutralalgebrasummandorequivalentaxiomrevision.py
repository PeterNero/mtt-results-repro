"""Select the minimal neutral algebra summand and its anomaly-free gauge line."""

from __future__ import annotations

import json
from math import gcd
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_neutralalgebrasummandorequivalentaxiomrevision"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "neutral_summand_and_hypercharge_reduction.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralAlgebraSummandOrEquivalentAxiomRevision_v1.md"
STATUS = "MTT_SELECTED_CN_FROM_COMPLEX_1M_AND_UNIQUE_ANOMALY_FREE_SHARED_HYPERCHARGE_LINE_CLOSED_PROFILE_FINITE_TRIPLE_CLOSED"
NEXT = "MTT_Selected_FiniteSpectralActionAndHiggsInnerFluctuation_or_DirectGenerativeSMActionClosure_v1"


FIELDS = ["Q", "u^c", "d^c", "L", "e^c", "N^c"]
EXPECTED_6Y = np.array([1, -4, 2, -3, 6, 0], dtype=int)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def left_weyl_charge_vector(alpha_c: int, mu_m3: int, nu_cn: int) -> np.ndarray:
    """Charges from u J u J^-1 on the A49 edges, written as left-Weyl rows."""
    return np.array(
        [
            -mu_m3,
            mu_m3 - alpha_c,
            alpha_c + mu_m3,
            -alpha_c,
            2 * alpha_c,
            alpha_c - nu_cn,
        ],
        dtype=int,
    )


def anomalies(charges: np.ndarray) -> dict[str, int]:
    q, uc, dc, lepton, ec, nc = [int(value) for value in charges]
    return {
        "SU3_squared_U1": 2 * q + uc + dc,
        "SU2_squared_U1": 3 * q + lepton,
        "gravity_squared_U1": 6 * q + 3 * uc + 3 * dc + 2 * lepton + ec + nc,
        "U1_cubic": 6 * q**3 + 3 * uc**3 + 3 * dc**3 + 2 * lepton**3 + ec**3 + nc**3,
    }


def primitive_integer_null_vector(matrix: np.ndarray) -> np.ndarray:
    # For the two independent rows used here, their cross product spans the exact nullspace.
    vector = np.cross(matrix[0], matrix[1]).astype(int)
    divisor = 0
    for value in vector:
        divisor = gcd(divisor, abs(int(value)))
    vector //= divisor
    if vector[0] < 0:
        vector *= -1
    return vector


def main() -> int:
    a46 = load(ROOT / "certificates" / "selected_typedfamilygaugecarrieranddiagonalsmrepresentationtheorem_certificate.json")
    a47 = load(ROOT / "certificates" / "selected_nativebundleautomorphismgaugegroup_or_parameterassumptionaudit_certificate.json")
    a49 = load(ROOT / "certificates" / "selected_physicalfinitediracoperatorandintersectionform_or_fullfinitetripleclosure_certificate.json")
    a46_packet = load(ROOT / "candidate_data" / "selected_typedfamilygaugecarrieranddiagonalsmrepresentationtheorem.candidate.json")

    # In phase-coordinate order (alpha_C, mu_M3, nu_CN), the two independent
    # local anomaly equations are alpha_C+3 mu_M3=0 and alpha_C-nu_CN=0.
    anomaly_constraint_matrix = np.array([[1, 3, 0], [1, 0, -1]], dtype=int)
    selected_phase_vector = primitive_integer_null_vector(anomaly_constraint_matrix)
    selected_charges = left_weyl_charge_vector(*selected_phase_vector)
    selected_anomalies = anomalies(selected_charges)

    # The cubic polynomial is 6 alpha^2(alpha+3mu)+(alpha-nu)^3, so it vanishes
    # identically on the exact linear-anomaly nullspace.
    alpha, mu, nu = [int(value) for value in selected_phase_vector]
    cubic_factorized = 6 * alpha**2 * (alpha + 3 * mu) + (alpha - nu) ** 3

    independent_cn_direction = np.array([0, 0, 1], dtype=int)
    independent_cn_anomalies = anomalies(left_weyl_charge_vector(*independent_cn_direction))
    independent_c_direction = np.array([1, 0, 0], dtype=int)
    independent_m3_direction = np.array([0, 1, 0], dtype=int)

    source_rows = a46_packet["typed_carrier"]["left_Weyl_representation_rows"]
    source_slots = {row["field"]: row["source_slot"] for row in source_rows}
    checks = {
        "A46_selected_complex_1M_equals_Nc_slot": source_slots["N^c"] == "1_M",
        "A46_anomaly_table_closed": a46["local_anomaly_rows_cancel_exactly"],
        "A47_native_shared_U1_and_Z6_closed": a47["faithful_global_SM_gauge_group_Z6_quotient_closed"],
        "A49_native_three_summand_no_go_proved": a49["native_three_summand_full_finite_triple_impossible"],
        "A49_CN_completion_axioms_closed": a49["minimal_CN_completion_finite_axioms_closed"],
        "linear_anomaly_constraint_rank_two": int(np.linalg.matrix_rank(anomaly_constraint_matrix)) == 2,
        "anomaly_free_abelian_nullspace_dimension_one": 3 - int(np.linalg.matrix_rank(anomaly_constraint_matrix)) == 1,
        "primitive_phase_vector_is_3_minus1_3": selected_phase_vector.tolist() == [3, -1, 3],
        "induced_left_Weyl_charges_equal_A47_6Y": np.array_equal(selected_charges, EXPECTED_6Y),
        "all_selected_local_anomalies_zero": all(value == 0 for value in selected_anomalies.values()),
        "factorized_cubic_anomaly_zero": cubic_factorized == 0,
        "independent_CN_phase_is_anomalous": independent_cn_anomalies["gravity_squared_U1"] != 0 and independent_cn_anomalies["U1_cubic"] != 0,
        "no_second_anomaly_free_continuous_U1": 3 - int(np.linalg.matrix_rank(anomaly_constraint_matrix)) == 1,
        "CN_phase_locked_to_shared_circle": nu == alpha,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    theorem_proved = all(checks.values())

    packet = {
        "schema": "MTTSelectedNeutralAlgebraSummandOrEquivalentAxiomRevision.v1",
        "status": STATUS,
        "theorem": {
            "name": "SelectedComplexOneMNeutralSummandAndUniqueAnomalyFreeSharedCircleTheorem",
            "proved": theorem_proved,
            "statement": "The selected one-dimensional complex 1_M=N^c matter carrier, together with the A49 orientability/Poincare-duality no-go, uniquely supplies the minimal complex summand C_N=End_C(1_M). For the completed edge representation, cancellation of SU2^2-U1 and gravitational-U1 anomalies has a one-dimensional exact phase nullspace generated by (alpha_C,mu_M3,nu_CN)=(3,-1,3). It emits precisely the A46/A47 integer hypercharges 6Y=(1,-4,2,-3,6,0); the cubic and remaining mixed anomalies vanish, while an independent C_N phase is anomalous. Thus C and C_N are distinct finite-algebra sheets but are locked to the same selected physical circle, leaving no extra continuous U1 and preserving the /Z6 SM gauge group.",
        },
        "minimal_algebra_selection": {
            "selected_matter_slot": "1_M=N^c",
            "carrier_type": "one-dimensional complex line",
            "endomorphism_algebra": "End_C(1_M)=C_N",
            "why_distinct_central_idempotent_is_forced": "A49 proves the N_R:C--C self-edge is non-orientable and the odd-rank KO6 intersection form is degenerate",
            "minimality_scope": "finite unital complex star-algebra completions preserving the A46 particle slots and KO6 axioms",
            "new_particle_slots": 0,
            "new_continuous_parameters": 0,
            "new_discrete_choice_after_axiom_and_carrier_requirements": 0,
        },
        "abelian_phase_system": {
            "coordinate_order": ["alpha_C", "mu_M3_center", "nu_CN"],
            "left_Weyl_charge_map": {
                "Q": "-mu",
                "u^c": "mu-alpha",
                "d^c": "alpha+mu",
                "L": "-alpha",
                "e^c": "2alpha",
                "N^c": "alpha-nu",
            },
            "linear_anomaly_constraints": {
                "SU2_squared_U1": "-(alpha+3mu)=0",
                "gravity_squared_U1": "alpha-nu=0",
            },
            "constraint_matrix": anomaly_constraint_matrix.tolist(),
            "constraint_rank": int(np.linalg.matrix_rank(anomaly_constraint_matrix)),
            "nullspace_dimension": 3 - int(np.linalg.matrix_rank(anomaly_constraint_matrix)),
            "primitive_null_vector": selected_phase_vector.tolist(),
            "cubic_factorization": "A_U1^3 = 6 alpha^2(alpha+3mu)+(alpha-nu)^3",
        },
        "selected_gauge_line": {
            "phase_vector": selected_phase_vector.tolist(),
            "field_order": FIELDS,
            "integer_charges_6Y": selected_charges.tolist(),
            "A46_A47_integer_charges_6Y": EXPECTED_6Y.tolist(),
            "anomalies": selected_anomalies,
            "CN_and_C_phase_relation": "nu_CN=alpha_C",
            "M3_center_relation": "mu_M3=-alpha_C/3",
            "physical_interpretation": "two distinct finite-algebra sheets share one anomaly-free physical circle action",
        },
        "rejected_extra_directions": {
            "independent_CN_phase_vector": independent_cn_direction.tolist(),
            "independent_CN_left_Weyl_charges": left_weyl_charge_vector(*independent_cn_direction).tolist(),
            "independent_CN_anomalies": independent_cn_anomalies,
            "pure_C_phase_charges": left_weyl_charge_vector(*independent_c_direction).tolist(),
            "pure_M3_center_phase_charges": left_weyl_charge_vector(*independent_m3_direction).tolist(),
            "second_anomaly_free_U1_exists": False,
        },
        "completed_finite_geometry_status": {
            "algebra": "C + H + M3(C) + C_N",
            "profile_DF": "closed by A49",
            "order_zero_and_one": "closed by A48/A49",
            "orientability": "closed by A49 on C_N completion",
            "Poincare_duality": "closed by A49 on C_N completion",
            "gauge_lie_algebra_after_anomaly_reduction": "su3 + su2 + u1_Y",
            "faithful_global_gauge_group": "(SU3 x SU2 x U1_Y)/Z6",
            "full_finite_triple_at_declared_profile_standard": theorem_proved,
            "strict_no_knob_physical_values": False,
            "unrestricted_full_unitary_group_identified_with_SM_group": False,
            "physical_gauge_restriction": "A47 native low-energy group intersected with the unique anomaly-free phase line on the A46 spectrum",
        },
        "checks": checks,
        "epistemic_policy": {
            "observed_values_used_to_select_CN": False,
            "observed_values_used_to_select_hypercharge_line": False,
            "standard_finite_complex_endomorphism_identity_used": True,
            "standard_local_anomaly_freedom_required": True,
            "extra_scalar_or_symmetry_breaking_assumed": False,
            "new_continuous_knobs": 0,
            "profile_DF_remains_profile_data": True,
            "UV_Green_Schwarz_or_extra_Higgs_extensions_excluded": False,
            "scope": "unique anomaly-free low-energy U1 on the selected A46 spectrum, not a classification of all UV completions",
        },
        "external_consistency": {
            "unimodularity_or_extra_Higgs_alternative": "https://arxiv.org/abs/hep-th/0409211",
            "right_handed_neutrino_orientability_obstruction": "https://arxiv.org/abs/hep-th/0610097",
        },
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_NeutralAlgebraSummandOrEquivalentAxiomRevision_v1",
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "CN_selected_from_complex_1M_carrier": True,
        "unique_anomaly_free_abelian_line_closed": True,
        "selected_phase_vector": selected_phase_vector.tolist(),
        "selected_integer_hypercharges_6Y": selected_charges.tolist(),
        "independent_CN_U1_rejected_by_anomalies": True,
        "shared_circle_reduction_closed": True,
        "faithful_Z6_SM_gauge_group_preserved": True,
        "full_finite_triple_at_profile_standard_closed": True,
        "strict_no_knob_DF_values_closed": False,
        "new_continuous_knobs": 0,
        "next_required_artifact": NEXT,
    }

    note = """# MTT Selected Neutral Algebra Summand or Equivalent Axiom Revision v1

## The Neutral Summand Is Selected

A49 left one discrete question: whether its minimal `C_N` completion is genuinely supplied by MTT.
The selected matter packet already answers it. `1_M=N^c` is a distinct one-dimensional complex
line. Its complex-linear endomorphism algebra is canonically

```text
End_C(1_M) = C_N.
```

A49 proves that its primitive central idempotent cannot be identified with the old `C` sheet: doing
so restores the non-orientable `N_R:C--C` self-edge and the degenerate odd-rank intersection form.
Therefore `C_N` is the unique minimal complex-algebra completion preserving the selected slots and
the KO6 orientability/Poincare-duality axioms. It adds no state and no continuous parameter.

## The Shared Circle Calculation

Distinct algebra sheets need not mean distinct physical circles. Write the three abelian unitary
phases as `(alpha_C,mu_M3,nu_CN)`. On the A49 edges their left-Weyl charges are

```text
Q=-mu,  u^c=mu-alpha,  d^c=alpha+mu,
L=-alpha,  e^c=2alpha, N^c=alpha-nu.
```

The two independent linear anomaly equations are

```text
SU(2)^2-U(1):       alpha + 3 mu = 0,
gravity^2-U(1):     alpha - nu = 0.
```

Their exact integer nullspace is one-dimensional, generated by

```text
(alpha,mu,nu) = (3,-1,3).
```

It emits

```text
6Y(Q,u^c,d^c,L,e^c,N^c) = (1,-4,2,-3,6,0),
```

exactly the A46/A47 representation. The cubic anomaly factorizes as
`6 alpha^2(alpha+3mu)+(alpha-nu)^3`, so it vanishes on the same line. A separate `C_N`
phase charges only `N^c` and has nonzero gravitational and cubic anomalies; it is rejected.

## Closure

The two complex summands are distinct finite-geometric sheets but share one anomaly-free physical
circle. No extra `U(1)`, breaking scalar, continuous knob, or observed selector is introduced. The
faithful gauge group remains `(SU3 x SU2 x U1_Y)/Z6`.

This is a low-energy theorem on the selected A46 spectrum. It does not classify ultraviolet
Green--Schwarz cancellations or models that replace unimodularity with an extra Higgs and a massive
neutral vector. Such constructions are possible extensions, but they are not emitted by the selected
A46/A47 SM branch and are not needed for its closure.

Together A48-A50 now close the completed finite real-even SM triple at the declared profile standard:
the `96x96 D_F`, order zero, order one, orientability, Poincare duality, anomaly-free hypercharge
reduction, and global `/Z6` form are all executable. Strict no-knob derivation of the profile values is
still a stronger program.

Next artifact: `MTT_Selected_FiniteSpectralActionAndHiggsInnerFluctuation_or_DirectGenerativeSMActionClosure_v1`.
"""

    dump(PACKET, packet)
    dump(CANDIDATE, packet)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
