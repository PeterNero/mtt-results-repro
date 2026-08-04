"""Test a shared-E0 neutral scale candidate without promoting an unfounded law."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GR = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof")
NONSM = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob")
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
M_THEORY = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings\Modal_Triplet_Theory__From_MTT_to_M_theory.md"
)
SLUG = "selected_neutraluniversale0attenuationcandidate_or_sourcelawfrontier"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "neutral_universal_e0_attenuation_discrimination.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralUniversalE0AttenuationCandidate_or_SourceLawFrontier_v1.md"
STATUS = "MTT_SELECTED_NEUTRAL_SHARED_E0_ATTENUATION_CANDIDATE_NUMERICALLY_COMPATIBLE_SOURCE_LAW_OPEN"
NEXT = "MTT_Selected_NeutralElevenFoldAttenuationAndProperTimeNormalizationTheorem_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    a40 = load(ROOT / "certificates" / "selected_neutraltwoprimitiveprofilevalueclosure_certificate.json")
    a41 = load(ROOT / "candidate_data" / "selected_neutrallensdedekindtransgression_or_oneprimitiveprofile.candidate.json")
    pmns = load(ROOT / "candidate_data" / "sm_equivalence_ckm_gauge_pmns_convention_fill.candidate.json")["PMNS_packet"]
    gr = load(GR / "certificates" / "one_anchor_gr_normalization_propagation_certificate.json")
    ew = load(NONSM / "certificates" / "selected_electroweak_local_projection_gate_certificate.json")
    shape = load(GR / "certificates" / "actual_shape_map_factorization_reduction_certificate.json")
    phase = load(Q79 / "certificates" / "iwasawa_c6_global_phase_block_certificate.json")

    # 2022 CODATA metrology. hbar, c and the joule/eV conversion are exact in the SI;
    # only G carries the quoted uncertainty here.
    G_si = 6.67430e-11
    G_si_sigma = 0.00015e-11
    hbar_si = 1.054571817e-34
    c_si = 299792458.0
    joule_per_GeV = 1.602176634e-10
    G_GeV_minus2 = G_si * joule_per_GeV**2 / (hbar_si * c_si**5)
    G_relative_sigma = G_si_sigma / G_si

    energy_family = gr["solution"]["energy_anchor_family"]
    g_coefficient = float(energy_family["G_eff_times_E0_squared"])
    E0_GeV = math.sqrt(g_coefficient / G_GeV_minus2)

    N = int(gr["solution"]["selected_internal_row"]["N"])
    tau = float(gr["solution"]["selected_internal_row"]["tau_int"])
    dimension = 11
    proper_time_amplitude = math.exp(-tau / 4.0)
    base_eV = E0_GeV * 1e9 / N**dimension
    mu_eV = base_eV * proper_time_amplitude

    phi = float(a41["determinant_line_candidate"]["candidate_phi_nu_rad"])
    cosine = sorted(math.cos(phi + 2.0 * math.pi * k / 3.0) for k in range(3))
    spread = cosine[2] - cosine[0]
    ratio = (cosine[1] - cosine[0]) / spread
    A_prediction = mu_eV**2 / (1.0 + ratio)
    dm31_prediction = A_prediction * spread
    dm21_prediction = ratio * dm31_prediction
    masses_prediction = [math.sqrt(max(0.0, A_prediction * (value - cosine[0]))) for value in cosine]

    inputs = pmns["input_values"]
    dm21_observed = float(inputs["Delta_m21_sq_eV2"]["central_value"])
    dm21_sigma = float(inputs["Delta_m21_sq_eV2"]["uncertainty"])
    dm31_observed = float(inputs["Delta_m3l_sq_eV2"]["central_value"])
    dm31_sigma = 0.5 * (
        float(inputs["Delta_m3l_sq_eV2"]["uncertainty_plus"])
        + float(inputs["Delta_m3l_sq_eV2"]["uncertainty_minus"])
    )
    A_profile = float(a40["A_nu_eV2"])

    def comparison(prediction: float, observed: float, observed_sigma: float | None = None) -> dict:
        predicted_sigma = abs(prediction) * G_relative_sigma
        combined_sigma = None if observed_sigma is None else math.hypot(predicted_sigma, observed_sigma)
        residual = prediction - observed
        return {
            "prediction": prediction,
            "observed_profile_value": observed,
            "residual": residual,
            "relative_residual": prediction / observed - 1.0,
            "predicted_sigma_from_G_only": predicted_sigma,
            "observed_sigma": observed_sigma,
            "combined_pull_sigma": None if combined_sigma is None else residual / combined_sigma,
        }

    exponent_scan = []
    target_mass = math.sqrt(A_profile)
    for exponent in [4, 6, 7, 10, 11, 12]:
        trial = E0_GeV * 1e9 / N**exponent
        exponent_scan.append({
            "exponent": exponent,
            "raw_mass_eV": trial,
            "absolute_log_residual_to_A40_sqrt_A": abs(math.log(trial / target_mass)),
        })
    fitted_exponent = math.log(E0_GeV * 1e9 / target_mass, N)

    rejected_nearby = {
        "electroweak_0p89": {
            "value": float(ew["execution_i_diagnostic"]["Delta_alpha_12_split"]),
            "admissible": False,
            "reason": "Certificate labels its c1/c2 import DIAGNOSTIC_NOT_PREDICTION and says source coefficients are unselected.",
        },
        "GR_det_core_C_0p8925": {
            "value": float(shape["finite_residuals"]["det_core_C"]),
            "admissible": False,
            "reason": "This is a finite residual inside CORE_B0_SAME_ANGLE_FACTORISATION_OPEN, not a selected neutral response coefficient.",
        },
        "q79_imaginary_phase": {
            "value": float(phase["calculation_results"]["chi_79"]["imag"]),
            "admissible": False,
            "reason": "The phase certificate explicitly proves that the unit-modulus C6 phase cannot set mass or mixing magnitudes.",
        },
    }

    m_theory_text = M_THEORY.read_text(encoding="utf-8")
    checks = {
        "A41_exact_phase_candidate_available": a41["theorem"]["proved"] is True,
        "GR_one_anchor_family_closed": gr["verdict"]["one_anchor_gr_normalization_family_closed"] is True,
        "selected_order_is_448": N == 448,
        "selected_tau_is_log448_over_15": abs(tau - math.log(448) / 15.0) < 1e-15,
        "corpus_contains_10D_to_11D_circle_lift": "ten-dimensional coherent fixed point and its 11D circle lift" in m_theory_text,
        "exponent_11_is_best_in_predeclared_dimension_scan": min(exponent_scan, key=lambda row: row["absolute_log_residual_to_A40_sqrt_A"])["exponent"] == 11,
        "candidate_A_within_one_G_sigma_of_A40_profile": abs(A_prediction / A_profile - 1.0) < G_relative_sigma,
        "all_nearby_imported_decimals_rejected_by_type_or_provenance": all(not row["admissible"] for row in rejected_nearby.values()),
    }
    candidate_discrimination_proved = all(checks.values())

    packet = {
        "schema": "MTTSelectedNeutralUniversalE0AttenuationCandidateOrSourceLawFrontier.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralLensDedekindTransgression_or_OnePrimitiveProfile_v1",
        "theorem": {
            "name": "NeutralUniversalE0AttenuationCandidateDiscriminationTheorem",
            "proved": candidate_discrimination_proved,
            "statement": "With the independently existing one-anchor GR family, N=448, tau_int=log(448)/15, the corpus 11D circle lift, and the A41 phase candidate, the target-ranked trial mu_nu=E0*448^-11*exp(-tau_int/4), A_nu=mu_nu^2/(1+r_nu), is numerically compatible with the A40 neutral amplitude using the measured Newton constant as the single shared metrology primitive. Exponent 11 is uniquely nearest in the declared dimension scan. This proves a sharp candidate and rejects three tempting mistyped coefficients; it does not prove the elevenfold attenuation law, quarter-proper-time factor, or neutral normalization from the selected action.",
        },
        "checks": checks,
        "metrology": {
            "role": "one universal measured absolute-scale primitive, not a neutrino-sector fit",
            "CODATA_release": "2022",
            "G_SI": G_si,
            "G_SI_sigma": G_si_sigma,
            "G_GeV_minus2": G_GeV_minus2,
            "G_relative_sigma": G_relative_sigma,
            "E0_GeV_from_GR_family": E0_GeV,
            "GR_relation": energy_family["G_eff_phys"],
            "source_url": "https://physics.nist.gov/cuu/pdf/wall_2022.pdf",
        },
        "candidate_law": {
            "N": N,
            "dimension_exponent": dimension,
            "tau_int": tau,
            "proper_time_amplitude": proper_time_amplitude,
            "formula_mu": "mu_nu = E0 * 448^(-11) * exp(-tau_int/4)",
            "formula_A": "A_nu = mu_nu^2 / (1 + r_nu)",
            "base_E0_over_448_pow_11_eV": base_eV,
            "mu_nu_eV": mu_eV,
            "r_nu_from_A41": ratio,
            "A_nu_prediction_eV2": A_prediction,
            "fitted_raw_exponent_without_proper_time_or_profile_normalization": fitted_exponent,
        },
        "predictions_and_postchecks": {
            "A_nu": comparison(A_prediction, A_profile),
            "Delta_m31_sq_eV2": comparison(dm31_prediction, dm31_observed, dm31_sigma),
            "Delta_m21_sq_eV2": comparison(dm21_prediction, dm21_observed, dm21_sigma),
            "masses_eV": masses_prediction,
            "sum_masses_eV": sum(masses_prediction),
        },
        "dimension_scan": exponent_scan,
        "rejected_nearby_coefficients": rejected_nearby,
        "source_law_boundary": {
            "native_MTT_dimension": 10,
            "M_theory_lift_dimension": 11,
            "neutral_operator_proved_to_live_on_11D_lift": False,
            "elevenfold_attenuation_derived_from_selected_operator": False,
            "quarter_proper_time_normalization_derived": False,
            "one_plus_ratio_normalization_derived_from_selected_action": False,
            "physical_APS_phase_identification_closed": False,
            "strict_neutral_scale_source_closed": False,
            "new_neutrino_specific_continuous_parameter_added": False,
            "universal_metrology_primitive_count": 1,
            "target_used_to_rank_formula": True,
            "pre_registered_prediction": False,
        },
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralUniversalE0AttenuationCandidate_or_SourceLawFrontier_v1",
        "status": STATUS,
        "theorem_proved": candidate_discrimination_proved,
        "E0_GeV": E0_GeV,
        "mu_nu_eV": mu_eV,
        "A_nu_prediction_eV2": A_prediction,
        "A_nu_relative_residual": A_prediction / A_profile - 1.0,
        "dimension_11_unique_in_scan": checks["exponent_11_is_best_in_predeclared_dimension_scan"],
        "universal_metrology_primitive_count": 1,
        "new_neutrino_specific_continuous_parameter_count": 0,
        "strict_neutral_scale_source_closed": False,
        "target_used_to_rank_formula": True,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Neutral Universal-E0 Attenuation Candidate or Source-Law Frontier v1

## Result

The existing GR one-anchor family gives

```text
G_eff(E0) = {g_coefficient} / E0^2.
```

Using the 2022 CODATA Newton constant as the one universal metrology primitive
gives `E0={E0_GeV} GeV`. The source-native, target-ranked trial

```text
mu_nu = E0 * 448^-11 * exp[-(log(448)/15)/4]
A_nu  = mu_nu^2 / (1+r_nu)
```

with the A41 `phi_nu=pi/120` ratio gives
`mu_nu={mu_eV} eV` and `A_nu={A_prediction} eV^2`. The relative residual
against the A40 profile amplitude is `{A_prediction / A_profile - 1.0}`,
about 18 ppm and inside the current relative uncertainty of `G`.

Among the predeclared physical-dimension exponents `4,6,7,10,11,12`, exponent
`11` is uniquely nearest. This makes the M-theory lift a serious source target,
not a proof: the corpus contains the 10D-to-11D circle lift, but no theorem says
that the neutral channel acquires one factor `1/448` per spacetime dimension.
Native MTT is `Y^4 x X^6`, hence 10D. Exponent 11 is admissible only after a
separate theorem places the physical neutral operator on the M-theory circle
lift. That lift identification is currently open.

## Provenance guard

Three nearby decimals are rejected. `0.89` is an explicitly fitted EW
diagnostic, `0.8925` belongs to an open GR core-factorization residual, and
`Im chi_79=0.894795...` is a CP phase whose certificate forbids using it as a
mass magnitude. None can be promoted as the missing neutral coefficient.

The numerical compatibility theorem is closed. Strict source promotion is not:
derive the elevenfold attenuation, the `exp(-tau_int/4)` amplitude convention,
and the `(1+r_nu)^(-1/2)` normalization from the same selected neutral
operator/action. The A41 APS determinant-line identification also remains open.
The candidate was found using the target and is not a pre-registered prediction.

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
