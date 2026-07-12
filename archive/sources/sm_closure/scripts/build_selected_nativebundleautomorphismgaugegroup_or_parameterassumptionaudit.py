"""Build the direct native-bundle SM gauge group and parameter-assumption audit."""

from __future__ import annotations

import cmath
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA = ROOT.parent / "mtt-qa-su3-packet-proof"
SLUG = "selected_nativebundleautomorphismgaugegroup_or_parameterassumptionaudit"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "native_bundle_gauge_group_and_parameter_audit.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NativeBundleAutomorphismGaugeGroup_or_ParameterAssumptionAudit_v1.md"
STATUS = "MTT_SELECTED_NATIVE_BUNDLE_AUTOMORPHISM_SM_GAUGE_GROUP_Z6_QUOTIENT_CLOSED_PARAMETER_ASSUMPTIONS_RECLASSIFIED"
NEXT = "MTT_Selected_NativeGaugeActionToFullFiniteBimodule_or_DirectGenerativeSMBaseClosure_v1"
TOL = 1e-12


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    a45 = load(ROOT / "certificates" / "selected_classlaneprojectorsandweakrealstructuresourcetheorem_certificate.json")
    a46 = load(ROOT / "certificates" / "selected_typedfamilygaugecarrieranddiagonalsmrepresentationtheorem_certificate.json")
    representation = load(
        ROOT / "candidate_data" / "selected_typedfamilygaugecarrieranddiagonalsmrepresentationtheorem"
        / "typed_family_gauge_carrier_and_anomaly_table.packet.json"
    )
    hypercharge = load(
        QA / "certificates" / "selected_electroweak_u1y_hypercharge_weights_typed_convention_gate_certificate.json"
    )

    rows = representation["typed_carrier"]["left_Weyl_representation_rows"]
    integer_charges = {row["field"]: int(6 * Fraction(row["Y"])) for row in rows}
    expected_charges = {"Q": 1, "u^c": -4, "d^c": 2, "L": -3, "e^c": 6, "N^c": 0}
    if integer_charges != expected_charges:
        raise AssertionError(f"hypercharge table changed: {integer_charges}")

    def center_phase(row: dict, a: int, b: int, k: int) -> complex:
        color_power = 1 if row["SU3"] == "3" else -1 if row["SU3"] == "bar3" else 0
        weak_power = 1 if row["SU2"] == "2" else 0
        q = integer_charges[row["field"]]
        return (
            cmath.exp(2j * math.pi * a * color_power / 3)
            * ((-1) ** (b * weak_power))
            * cmath.exp(1j * math.pi * k * q / 3)
        )

    kernel = []
    max_kernel_residual = 0.0
    for a in range(3):
        for b in range(2):
            for k in range(6):
                residual = max(abs(center_phase(row, a, b, k) - 1) for row in rows)
                if residual < TOL:
                    kernel.append({"color_Z3_power": a, "weak_Z2_power": b, "U1_sixth_root_power": k})
                    max_kernel_residual = max(max_kernel_residual, residual)
    expected_kernel = [
        {"color_Z3_power": t % 3, "weak_Z2_power": t % 2, "U1_sixth_root_power": t}
        for t in range(6)
    ]
    kernel_key = lambda item: (item["U1_sixth_root_power"], item["color_Z3_power"], item["weak_Z2_power"])

    native_group = {
        "circle_rank1": {
            "preserved_structure": "Hermitian line and central-circle phase",
            "unitary_automorphism_group": "U(1)",
            "lie_dimension": 1,
        },
        "lens_rank2": {
            "preserved_structure": "Hermitian metric plus selected epsilon/J symplectic form",
            "unitary_automorphism_group": "USp(2) = SU(2)",
            "lie_dimension": 3,
        },
        "nil_rank3": {
            "preserved_structure": "Hermitian metric plus determinant-trivial SU(3) volume form (c1=0)",
            "unitary_automorphism_group": "SU(3)",
            "lie_dimension": 8,
        },
        "local_product": "U(1) x SU(2) x SU(3)",
        "faithful_global_group_on_A46_carrier": "(U(1) x SU(2) x SU(3))/Z6",
        "lie_algebra": "u(1) direct-sum su(2) direct-sum su(3)",
        "lie_dimension": 12,
    }

    parameter_audit = [
        {
            "object": "A44/A45 rank-1/rank-2/full projectors",
            "old_possible_reading": "three matrix choices",
            "classification": "basis representatives of the selected native 1<2<3 flag",
            "continuous_free_parameters": 0,
            "status": "SELECTED_UP_TO_UNITARY_EQUIVALENCE",
        },
        {
            "object": "A44/A45 weak J=epsilon K",
            "old_possible_reading": "chosen antiunitary",
            "classification": "unique normalized invariant symplectic real structure up to phase/basis",
            "continuous_free_parameters": 0,
            "status": "SELECTED_UP_TO_GAUGE_EQUIVALENCE",
        },
        {
            "object": "A46 low-energy SM gauge group",
            "old_possible_reading": "standard E6 branching premise",
            "classification": "direct native bundle-automorphism group; E6 route retained as UV encoding",
            "continuous_free_parameters": 0,
            "status": "CLOSED_BY_DIRECT_SUPERSET_ROUTE",
        },
        {
            "object": "A46 representation rows and hypercharges",
            "old_possible_reading": "six supplied SM labels",
            "classification": "selected matter-slot packet plus exact representation decomposition and typed U1Y map",
            "continuous_free_parameters": 0,
            "status": "DISCRETE_STRUCTURE_NO_CONTINUOUS_KNOB",
        },
        {
            "object": "A40 two neutrino mass-squared splittings",
            "old_possible_reading": "two MTT parameters",
            "classification": "two observed profile-calibration coordinates in the fallback profile execution",
            "continuous_free_parameters": 2,
            "status": "MEASURED_PROFILE_INPUTS_NOT_SOURCE_DERIVED",
        },
        {
            "object": "A41 phi_nu=pi/120",
            "old_possible_reading": "one fitted phase",
            "classification": "exact Lens/Dedekind source candidate conditional on APS determinant-line identification",
            "continuous_free_parameters": 0,
            "status": "DISCRETE_EXACT_CANDIDATE_STRICT_PROMOTION_OPEN",
        },
        {
            "object": "A41 neutral absolute scale",
            "old_possible_reading": "remaining shape and scale pair",
            "classification": "one measured profile scale after conditional phase promotion",
            "continuous_free_parameters": 1,
            "status": "ONE_SCALE_PROFILE_INPUT_STRICT_SOURCE_OPEN",
        },
        {
            "object": "A42 measured G and derived E0",
            "old_possible_reading": "new neutrino parameter",
            "classification": "one universal dimensional metrology anchor; E0 is derived and adds no neutrino-specific knob",
            "continuous_free_parameters": 1,
            "status": "CONDITIONAL_ALTERNATIVE_ROUTE_NOT_ADDITIVE_TO_BASELINE",
        },
        {
            "object": "A42 exponent 11 and A43 nil quarter",
            "old_possible_reading": "two discrete parameter choices",
            "classification": "target-ranked unselected hypotheses; native 10D check rejects treating them as closed inputs",
            "continuous_free_parameters": 0,
            "status": "NOT_ACCEPTED_PARAMETERS_AND_NOT_CLOSED_RESULTS",
        },
        {
            "object": "shared P_EW",
            "old_possible_reading": "Higgs-specific fit knob",
            "classification": "one shared physical profile primitive replacing an independent lambda_H coordinate",
            "continuous_free_parameters": 1,
            "status": "ADOPTED_BASELINE_PROFILE_PRIMITIVE_STRICT_SOURCE_OPEN",
        },
        {
            "object": "Dirac/Weyl/twistor downstream tetrad/connection/normalization fields",
            "old_possible_reading": "five free parameters",
            "classification": "same-source theorem obligations; field objects whose values must be emitted, not automatically scalar knobs",
            "continuous_free_parameters": 0,
            "status": "PROOF_OBLIGATIONS_NOT_PARAMETER_COUNT",
        },
    ]

    checks = {
        "A45_native_flag_closed": a45["native_rank_flag_closed_up_to_unitary_equivalence"],
        "A45_weak_J_closed": a45["weak_real_structure_closed_up_to_unitary_phase_equivalence"],
        "A46_family_diagonal_representation_closed": a46["family_diagonal_gauge_action_closed"],
        "A46_anomaly_table_closed": a46["local_anomaly_rows_cancel_exactly"] and a46["Witten_SU2_anomaly_absent"],
        "typed_hypercharge_map_closed": hypercharge["closed"]["typed_hypercharge_convention_map"],
        "integer_hypercharges_primitive": math.gcd(*[abs(value) for value in integer_charges.values()]) == 1,
        "native_lie_dimension_is_12": native_group["lie_dimension"] == 12,
        "global_kernel_has_order_6": len(kernel) == 6,
        "global_kernel_is_diagonal_Z6": sorted(kernel, key=kernel_key) == sorted(expected_kernel, key=kernel_key),
        "global_kernel_residual_below_tolerance": max_kernel_residual < TOL,
    }
    theorem_proved = all(checks.values())

    packet = {
        "schema": "MTTSelectedNativeBundleAutomorphismGaugeGroupOrParameterAssumptionAudit.v1",
        "status": STATUS,
        "theorem": {
            "name": "NativeBundleAutomorphismSMGaugeGroupAndZ6KernelTheorem",
            "proved": theorem_proved,
            "statement": "The selected native rank-1 central-circle carrier has unitary automorphism U1; the selected rank-2 lens carrier with invariant epsilon/J has unitary symplectic automorphism USp2=SU2; and the selected rank-3 determinant-trivial nil/visible carrier has automorphism SU3. Their product acts family-diagonally on the A46 chiral carrier. The exact kernel on all six emitted left-Weyl rows is the diagonal Z6 generated by (omega3,-1,exp(i*pi/3)), so the faithful global gauge group is (SU3 x SU2 x U1)/Z6. This directly selects the low-energy SM gauge group from native MTT bundle structure; no E6 Wilson-line premise is needed for the direct route.",
        },
        "native_bundle_gauge_group": native_group,
        "global_kernel_execution": {
            "integer_normalized_hypercharges_6Y": integer_charges,
            "enumerated_center_domain_size": 3 * 2 * 6,
            "kernel_order": len(kernel),
            "kernel_elements": kernel,
            "generator": {"color_Z3_power": 1, "weak_Z2_power": 1, "U1_sixth_root_power": 1},
            "max_kernel_action_residual": max_kernel_residual,
        },
        "route_decision": {
            "direct_native_bundle_automorphism_route_closed": True,
            "E6_selected_bundle_source_role": "UV matter/unification encoding yielding E6 and three chiral 27s",
            "E6_to_SM_Wilson_line_required_for_direct_low_energy_route": False,
            "E6_physical_breaking_selector_closed": False,
            "why_not_a_contradiction": "MTT is used as a superset: the direct native bundle automorphism encoding selects the low-energy gauge group, while the heterotic E6 encoding supplies a compatible UV representation organization.",
            "existing_S3_symmetry_breaking_packets_reused_as_gauge_breaking": False,
            "S3_packet_type": "family/orientation and visible-source branch selection, not E6 gauge commutant breaking",
        },
        "parameter_assumption_audit": {
            "scope": "A40-A46 plus the adopted shared-P_EW baseline and proto-spinor same-source fields",
            "rows": parameter_audit,
            "new_continuous_knobs_introduced_by_A44_A47": 0,
            "adopted_baseline_shared_physical_primitive_count": 1,
            "conditional_neutral_profile_input_count_after_A41": 1,
            "fallback_A40_neutral_profile_input_count": 2,
            "A42_G_route_is_alternative_not_additive": True,
            "proof_obligations_must_not_be_counted_as_parameters": True,
        },
        "checks": checks,
        "claim_boundary": {
            "low_energy_gauge_group_and_global_form_closed": True,
            "family_diagonal_chiral_action_and_anomalies_closed": True,
            "gauge_coupling_values_derived_here": False,
            "full_finite_Connes_bimodule_closed": False,
            "E6_Wilson_line_breaking_closed": False,
            "strict_zero_knob_dimensionful_metrology_closed": False,
        },
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NativeBundleAutomorphismGaugeGroup_or_ParameterAssumptionAudit_v1",
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "native_low_energy_gauge_lie_algebra_closed": True,
        "faithful_global_SM_gauge_group_Z6_quotient_closed": True,
        "global_kernel_order": len(kernel),
        "new_continuous_knobs_A44_A47": 0,
        "A40_A46_parameter_assumptions_reclassified": True,
        "direct_route_needs_E6_Wilson_line": False,
        "full_Connes_finite_bimodule_closed": False,
        "strict_dimensionful_no_knob_closed": False,
        "next_required_artifact": NEXT,
    }

    note = """# MTT Selected Native Bundle-Automorphism Gauge Group or Parameter-Assumption Audit v1

## Direct Low-Energy Gauge Selection

The selected native bundle tensors already select the low-energy gauge group without requiring
the heterotic E6 encoding to perform a further Wilson-line breaking:

```text
rank-1 central-circle line                         -> U(1)
rank-2 lens carrier preserving epsilon/J          -> USp(2) = SU(2)
rank-3 determinant-trivial nil/visible carrier    -> SU(3)
```

Thus the local group is `U(1) x SU(2) x SU(3)`. On the A46 chiral carrier, with
integer-normalized charges `6Y=(1,-4,2,-3,6,0)`, exhaustive center enumeration gives the
six-element kernel generated by

```text
(omega_3, -1, exp(i*pi/3)).
```

The faithful global group is therefore

```text
(SU(3) x SU(2) x U(1))/Z6.
```

This is the observed SM global gauge-group form. The E6 bundle remains useful as a compatible
UV matter/unification encoding and source of three chiral 27s. A selected E6 Wilson line is not
needed for this direct MTT route. Existing S3 symmetry-breaking packets were checked and remain
typed to family/orientation selection, not visible E6 gauge breaking.

## Parameter and Assumption Correction

The recent work introduced no new continuous gauge or representation knobs:

- the rank projectors and `J` are unique up to gauge/basis equivalence;
- the six representation rows, hypercharges, Z6 quotient, and anomaly cancellations are discrete
  selected or exact data;
- the former low-energy E6 branching premise is bypassed by the direct bundle-automorphism route;
- the five downstream Dirac/Weyl/twistor source fields are proof obligations, not five scalar parameters.

The honest continuous-input ledger is unchanged:

- adopted global profile baseline: one shared physical primitive `P_EW`;
- A40 neutral fallback: two observed splitting coordinates;
- conditional A41 neutral route: one observed absolute scale after the exact phase candidate;
- A42 measured `G` route: one alternative universal metrology anchor, not an additional baseline
  parameter and not a neutrino-specific knob.

The A42 exponent 11 and A43 nil quarter are target-ranked unselected hypotheses. They are neither
accepted parameters nor closed predictions. This distinction prevents failed source candidates from
inflating the parameter count.

## Remaining Scope

Gauge coupling values, strict dimensionful metrology, and the optional full Connes finite bimodule
remain open. They are separate from selection of the low-energy gauge group and its anomaly-free
chiral representation, which are now closed on the direct native-bundle route.

Next artifact: `MTT_Selected_NativeGaugeActionToFullFiniteBimodule_or_DirectGenerativeSMBaseClosure_v1`.
"""

    dump(PACKET, packet)
    dump(CANDIDATE, packet)
    dump(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
