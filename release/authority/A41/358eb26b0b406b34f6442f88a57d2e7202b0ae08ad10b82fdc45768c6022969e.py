"""Build the Lens/Dedekind neutral-phase candidate and one-scale profile."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
GR = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof")
SLUG = "selected_neutrallensdedekindtransgression_or_oneprimitiveprofile"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "neutral_lens_dedekind_transgression.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralLensDedekindTransgression_or_OnePrimitiveProfile_v1.md"
STATUS = "MTT_SELECTED_NEUTRAL_LENS_DEDEKIND_IDENTITY_CLOSED_PHASE_SOURCE_NORMALIZATION_OPEN_ONE_SCALE_PROFILE_READY"
NEXT = "MTT_Selected_NeutralAPSDeterminantLineIdentificationAndCountertermNormalization_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sawtooth(n: int, k: int) -> Fraction:
    residue = n % k
    if residue == 0:
        return Fraction(0)
    return Fraction(residue, k) - Fraction(1, 2)


def dedekind_sum(h: int, k: int) -> Fraction:
    return sum((sawtooth(n, k) * sawtooth(h * n, k) for n in range(1, k)), Fraction(0))


def main() -> int:
    z64 = load(Q79 / "certificates" / "z64_exact_branch_certificate.json")
    a38 = load(ROOT / "certificates" / "selected_neutralcommoncirclefactorizationandholonomyscalarreduction_certificate.json")
    a39 = load(ROOT / "certificates" / "selected_neutralfiniteheisenbergdeterminantnogoandsmoothlifttarget_certificate.json")
    a40 = load(ROOT / "certificates" / "selected_neutraltwoprimitiveprofilevalueclosure_certificate.json")
    pmns = load(ROOT / "candidate_data" / "sm_equivalence_ckm_gauge_pmns_convention_fill.candidate.json")["PMNS_packet"]
    metrology = load(GR / "certificates" / "dimensional_metrology_no_go_and_relative_closure_theorem_certificate.json")

    selected_cost = int(z64["hessian_block"]["selected_value"])
    quarter_turn = 16
    selected_lag = z64["retarded_kernel"]["selected_lag"]
    s_15_16 = dedekind_sum(selected_cost, quarter_turn)
    s_16_15 = dedekind_sum(quarter_turn, selected_cost)
    reciprocity_rhs = -Fraction(1, 4) + Fraction(1, 12) * (
        Fraction(selected_cost, quarter_turn)
        + Fraction(quarter_turn, selected_cost)
        + Fraction(1, selected_cost * quarter_turn)
    )
    mixed_residue = (
        12 * (s_15_16 + s_16_15)
        + 3
        - Fraction(selected_cost, quarter_turn)
        - Fraction(quarter_turn, selected_cost)
    )
    expected_residue = Fraction(1, selected_cost * quarter_turn)
    phi_candidate = 2.0 * math.pi * float(mixed_residue)
    phi_profile = float(a40["phi_nu_rad"])

    cosine = [math.cos(phi_candidate + 2.0 * math.pi * k / 3.0) for k in range(3)]
    ordered = sorted(range(3), key=lambda k: cosine[k])
    c_min, c_mid, c_max = (cosine[k] for k in ordered)
    ratio_candidate = (c_mid - c_min) / (c_max - c_min)

    inputs = pmns["input_values"]
    dm21 = float(inputs["Delta_m21_sq_eV2"]["central_value"])
    dm21_sigma = float(inputs["Delta_m21_sq_eV2"]["uncertainty"])
    dm31 = float(inputs["Delta_m3l_sq_eV2"]["central_value"])
    dm31_sigma_plus = float(inputs["Delta_m3l_sq_eV2"]["uncertainty_plus"])
    dm31_sigma_minus = float(inputs["Delta_m3l_sq_eV2"]["uncertainty_minus"])
    dm31_sigma_sym = 0.5 * (dm31_sigma_plus + dm31_sigma_minus)
    dm21_prediction = ratio_candidate * dm31
    prediction_sigma_from_scale = ratio_candidate * dm31_sigma_sym
    comparison_sigma = math.hypot(dm21_sigma, prediction_sigma_from_scale)
    residual = dm21_prediction - dm21
    pull = residual / comparison_sigma

    amplitude = dm31 / (c_max - c_min)
    offset = -amplitude * c_min
    mass_sq_by_k = [offset + amplitude * value for value in cosine]
    mass_sq = [mass_sq_by_k[k] for k in ordered]
    masses = [math.sqrt(max(0.0, value)) for value in mass_sq]

    checks = {
        "selected_Z64_exact_branch_closed": z64["status"] == "CLOSED_EXACT_CENTRAL_CIRCLE_BRANCH",
        "retarded_unit_lag_is_16_to_15": selected_lag == "16 -> 15 = S^-1",
        "selected_hessian_cost_is_15": selected_cost == 15,
        "common_circle_factorization_closed": a38["theorem_proved"],
        "finite_SU3_determinant_no_go_closed": a39["theorem_proved"],
        "A40_profile_target_available": a40["theorem_proved"],
        "dedekind_reciprocity_exact": s_15_16 + s_16_15 == reciprocity_rhs,
        "mixed_reciprocity_residue_exact": mixed_residue == expected_residue == Fraction(1, 240),
        "candidate_phase_is_pi_over_120": abs(phi_candidate - math.pi / 120.0) < 1e-16,
        "candidate_ratio_within_declared_diagonal_uncertainty": abs(pull) < 1.0,
        "absolute_metrology_no_go_imported": metrology["no_go"]["status"] == "PROVED_IN_CURRENT_FORMALIZATION",
        "one_absolute_metrology_primitive_is_minimal": metrology["no_go"]["free_parameter_count_for_absolute_units"] == 1,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    theorem_proved = all(checks.values())

    exact = lambda value: {"numerator": value.numerator, "denominator": value.denominator, "text": str(value)}
    packet = {
        "schema": "MTTSelectedNeutralLensDedekindTransgressionOrOnePrimitiveProfile.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralTwoPrimitiveProfileValueClosure_v1",
        "theorem": {
            "name": "NeutralLensDedekindMixedResidueAndConditionalOnePrimitiveProfileTheorem",
            "proved": theorem_proved,
            "statement": "For the independently selected retarded Z64 pair 16->15, classical Dedekind reciprocity gives the exact renormalized mixed residue R_15,16=12[s(15,16)+s(16,15)]+3-15/16-16/15=1/240. If the physical neutral Bismut-Freed/APS determinant-line connection is proved to retain this mixed Lens term after the MTT shared-circle cancellation of local self terms, then phi_nu=2pi R_15,16=pi/120. That phase predicts the oscillation ratio and reduces the A40 neutral mass-splitting profile from two measured scale coordinates to one. The arithmetic identity and conditional implication are proved; the determinant-family/operator, spin structure, orientation and counterterm-normalization identification are not yet proved.",
        },
        "source_checks": checks,
        "selected_arithmetic": {
            "Z64_selected_cost": selected_cost,
            "quarter_turn_anchor": quarter_turn,
            "retarded_lag": selected_lag,
            "dedekind_s_15_16": exact(s_15_16),
            "dedekind_s_16_15": exact(s_16_15),
            "reciprocity_sum": exact(s_15_16 + s_16_15),
            "renormalized_mixed_residue": exact(mixed_residue),
            "identity": "12*(s(15,16)+s(16,15))+3-15/16-16/15=1/240",
        },
        "determinant_line_candidate": {
            "candidate_holonomy": "exp(2*pi*i*R_15_16)",
            "candidate_phi_nu_rad": phi_candidate,
            "candidate_phi_nu_exact": "pi/120",
            "A40_calibrated_phi_nu_rad": phi_profile,
            "absolute_phase_residual_rad": phi_candidate - phi_profile,
            "relative_phase_residual": phi_candidate / phi_profile - 1.0,
            "canonical_external_framework": "Bismut-Freed/Dai-Freed determinant-line holonomy from exponentiated eta invariants; APS lens-space eta/signature defects are expressed by Dedekind sums",
            "references": [
                "https://arxiv.org/abs/hep-th/9405012",
                "https://arxiv.org/abs/dg-ga/9505002",
                "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4BC45AB3FD65076115A82564AAAB23E0/S0013091522000153a.pdf/atiyahpatodisinger_rho_invariant_and_signatures_of_links.pdf",
            ],
            "physical_identification_closed": False,
            "missing_identification_fields": [
                "selected neutral family of Dirac/signature operators",
                "Lens-space or equivalent boundary/mapping-torus identification for the ordered 15/16 pair",
                "spin or spinC structure and orientation",
                "Bismut-Freed/APS normalization relating the eta/rho invariant to arg det H_nu",
                "MTT cancellation theorem subtracting the two local self terms while retaining the mixed reciprocity residue",
            ],
        },
        "conditional_one_scale_profile": {
            "mass_scale_input": "Delta_m3l_sq_eV2",
            "continuous_neutral_mass_splitting_inputs": 1,
            "candidate_ratio": ratio_candidate,
            "observed_ratio": dm21 / dm31,
            "predicted_Delta_m21_sq_eV2": dm21_prediction,
            "observed_Delta_m21_sq_eV2": dm21,
            "residual_eV2": residual,
            "comparison_sigma_eV2_diagonal_approximation": comparison_sigma,
            "pull_sigma_diagonal_approximation": pull,
            "A_nu_eV2_from_one_scale": amplitude,
            "mass_squared_eV2": mass_sq,
            "masses_eV": masses,
            "sum_masses_eV": sum(masses),
            "classification": "CONDITIONAL_ONE_MEASURED_SCALE_PROFILE_COMPATIBLE_NOT_A_PRE_REGISTERED_PREDICTION",
        },
        "absolute_scale_boundary": {
            "imported_no_go": metrology["no_go"],
            "strict_absolute_neutral_scale_selected": False,
            "minimal_current_executable_extension": "one measured neutral mass-squared scale",
            "stronger_shared_primitive_route": "one universal E0/L0/Omega0 metrology primitive plus a source-derived dimensionless neutral response coefficient",
            "source_derived_dimensionless_neutral_response_coefficient_available": False,
        },
        "closure_decision": {
            "exact_Dedekind_reciprocity_identity_closed": theorem_proved,
            "canonical_Lens_eta_framework_identified": True,
            "candidate_phase_matches_profile_within_uncertainty": abs(pull) < 1.0,
            "conditional_two_to_one_neutral_scale_reduction_ready": theorem_proved,
            "strict_determinant_line_phase_source_closed": False,
            "strict_absolute_scale_source_closed": False,
            "strict_neutral_no_knob_closed": False,
        },
        "epistemic_policy": {
            "observed_data_used_as_geometry_or_branch_selector": False,
            "target_used_to_rank_this_hypothesis": True,
            "target_fitting_used": True,
            "pre_registered_prediction": False,
            "future_oscillation_updates_can_be_held_out_tests": True,
            "forbidden_claim": "Do not call pi/120 an MTT prediction until the APS determinant-line identification and cancellation normalization are independently proved.",
        },
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralLensDedekindTransgression_or_OnePrimitiveProfile_v1",
        "candidate": f"candidate_data/{SLUG}.candidate.json",
        "status": STATUS,
        "theorem_proved": theorem_proved,
        "mixed_reciprocity_residue": exact(mixed_residue),
        "candidate_phi_nu_rad": phi_candidate,
        "candidate_phi_nu_exact": "pi/120",
        "candidate_ratio": ratio_candidate,
        "pull_sigma_diagonal_approximation": pull,
        "conditional_continuous_neutral_mass_splitting_inputs": 1,
        "strict_determinant_line_phase_source_closed": False,
        "strict_absolute_scale_source_closed": False,
        "target_fitting_used": True,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Neutral Lens-Dedekind Transgression or One-Primitive Profile v1

## Exact result

The selected exact `Z64` branch supplies the ordered retarded pair `16 -> 15`.
For the classical Dedekind sum, exact rational arithmetic gives

```text
s(15,16) = {s_15_16}
s(16,15) = {s_16_15}
12[s(15,16)+s(16,15)] + 3 - 15/16 - 16/15 = {mixed_residue}
```

Thus the renormalized mixed reciprocity residue is exactly `1/240`. If the
physical neutral determinant-line connection is the corresponding mixed
Lens/APS transgression after shared-circle cancellation of the local self
terms, then

```text
phi_nu = 2*pi/240 = pi/120 = {phi_candidate} rad.
```

This gives the mass-splitting ratio `{ratio_candidate}`. Using only the locked
`Delta m3l^2` as a scale predicts `Delta m21^2={dm21_prediction} eV^2`, a
diagonal-profile pull of `{pull}` sigma from the locked central value.

## Boundary

The Dedekind identity is proved, but the physical identification is not. It
still requires the selected neutral operator family, Lens/mapping-torus
identification, spin structure, orientation, Bismut-Freed/APS normalization,
and the MTT cancellation theorem that removes the local terms and retains the
mixed residue. The hypothesis was found while inspecting the target, so this
is not a pre-registered prediction.

Absolute scale remains protected by the proved one-dimensional metrology
symmetry. Current execution needs one scale primitive; strict closure needs a
universal metrology source plus the neutral response coefficient.

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
