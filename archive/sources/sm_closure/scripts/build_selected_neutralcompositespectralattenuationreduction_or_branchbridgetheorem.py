"""Compress the A42 attenuation to one spectrum and audit its source premises."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")
GR = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-protospinor-gr-response-proof")
M_THEORY = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\16 Strings, Flux, & M-Theory Encodings\Modal_Triplet_Theory__From_MTT_to_M_theory.md"
)
BOOK = Path(
    r"C:\ObsidianVault\BrainOfNerodes\Papers\Modal Triplet Theory"
    r"\10 The Book on Modal Triplet Theory\The_Book_on_Modal_Triplet_Theory_v9.md"
)
SLUG = "selected_neutralcompositespectralattenuationreduction_or_branchbridgetheorem"
OUT = ROOT / "candidate_data" / SLUG
PACKET = OUT / "neutral_composite_spectral_attenuation.packet.json"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_NeutralCompositeSpectralAttenuationReduction_or_BranchBridgeTheorem_v1.md"
STATUS = "MTT_SELECTED_NEUTRAL_ATTENUATION_COMPRESSED_TO_COMPOSITE_SPECTRUM_BRANCH_BRIDGE_OPEN"
NEXT = "MTT_Selected_NeutralNative10D_or_MTheoryLiftOperatorSelectionAndBranchBridge_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    a41 = load(ROOT / "candidate_data" / "selected_neutrallensdedekindtransgression_or_oneprimitiveprofile.candidate.json")
    a42 = load(ROOT / "candidate_data" / "selected_neutraluniversale0attenuationcandidate_or_sourcelawfrontier.candidate.json")
    z64 = load(Q79 / "certificates" / "z64_exact_branch_certificate.json")
    gap = load(GR / "certificates" / "dimensionless_modal_gap_operator_reduction_certificate.json")
    branch = load(GR / "certificates" / "selected_aint_packet_branch_bridge_audit_certificate.json")
    m_theory_text = M_THEORY.read_text(encoding="utf-8")
    book_text = BOOK.read_text(encoding="utf-8")

    N = int(a42["candidate_law"]["N"])
    tau = float(a42["candidate_law"]["tau_int"])
    circle_cost = int(z64["hessian_block"]["selected_value"])
    dimension_count = int(a42["candidate_law"]["dimension_exponent"])
    nil_floor = Fraction(1, 4)
    composite_eigenvalue = dimension_count * Fraction(circle_cost) + nil_floor

    circle_heat_factor = math.exp(-tau * circle_cost)
    direct_factor = N ** (-dimension_count) * math.exp(-tau * float(nil_floor))
    compressed_factor = math.exp(-tau * float(composite_eigenvalue))
    native_dimension_count = 10
    native_composite_eigenvalue = native_dimension_count * Fraction(circle_cost) + nil_floor
    native_factor = math.exp(-tau * float(native_composite_eigenvalue))
    native_mu_eV = float(a42["metrology"]["E0_GeV_from_GR_family"]) * 1e9 * native_factor
    native_A_eV2 = native_mu_eV**2 / (1.0 + float(a41["conditional_one_scale_profile"]["candidate_ratio"]))

    phi = float(a41["determinant_line_candidate"]["candidate_phi_nu_rad"])
    cosine = sorted(math.cos(phi + 2.0 * math.pi * k / 3.0) for k in range(3))
    spread = cosine[2] - cosine[0]
    ratio = (cosine[1] - cosine[0]) / spread
    shifted = [value - cosine[0] for value in cosine]
    normalized_shape = [value / spread for value in shifted]
    trace_shifted = sum(shifted)
    trace_normalized = sum(normalized_shape)

    profile_identities = {
        "sum_cosine_zero": abs(sum(cosine)) < 1e-15,
        "trace_shifted_equals_minus_3_cmin": abs(trace_shifted + 3.0 * cosine[0]) < 1e-15,
        "trace_shifted_equals_spread_times_one_plus_r": abs(trace_shifted - spread * (1.0 + ratio)) < 1e-15,
        "normalized_shape_is_0_r_1": max(abs(a - b) for a, b in zip(normalized_shape, [0.0, ratio, 1.0])) < 1e-15,
        "trace_normalized_equals_one_plus_r": abs(trace_normalized - (1.0 + ratio)) < 1e-15,
    }

    source_premises = {
        "circle_cost_15_selected_in_exact_Z64_branch": circle_cost == 15,
        "tau_equals_log_N_over_circle_cost": abs(tau - math.log(N) / circle_cost) < 1e-15,
        "M_theory_corpus_has_11D_circle_lift": "ten-dimensional coherent fixed point and its 11D circle lift" in m_theory_text,
        "recursive_dimension_census_4_plus_1_plus_2_plus_3_plus_1_is_11": (
            "Rank--$1+2+3=6$" in book_text
            and "3{+}1" in book_text
            and "11D circle lift" in m_theory_text
            and 4 + 1 + 2 + 3 + 1 == 11
        ),
        "eleven_Z64_cost_blocks_selected_in_one_neutral_operator": False,
        "physical_neutral_operator_selected_on_M_theory_11D_lift": False,
        "nil_floor_one_quarter_selected_as_global_Aint_saturation": branch["import_decisions"]["can_import_theta_nil_floor_as_selected_global_saturation"],
        "Z64_and_nil_values_bridged_in_same_operator_convention": branch["verdict"]["selected_global_Aint_packet_closed"],
        "neutral_semigroup_identified_with_composite_operator": False,
        "profile_trace_over_spread_normalization_selected_by_action": False,
    }

    exact_checks = {
        "circle_heat_factor_is_one_over_448": abs(circle_heat_factor - 1.0 / N) < 1e-15,
        "attenuation_compression_identity": abs(direct_factor - compressed_factor) < 1e-40,
        "composite_eigenvalue_is_661_over_4": composite_eigenvalue == Fraction(661, 4),
        "A42_factor_reproduced": abs(direct_factor - a42["candidate_law"]["proper_time_amplitude"] / N**dimension_count) < 1e-40,
        "all_profile_identities": all(profile_identities.values()),
    }
    reduction_theorem_proved = all(exact_checks.values())

    required_promotion = [
        "Construct one selected neutral Hilbert/operator packet carrying eleven common-circle cost-15 contributions; 11D spacetime dimension alone is insufficient.",
        "Prove the nil contribution is an exact selected eigenvalue 1/4 in that same packet; the current corpus permits only a benchmark saturation/universal lower bound.",
        "Prove the Z64 and nil terms share one A_int convention and commute or otherwise establish the sum-spectrum 661/4.",
        "Identify the physical neutral attenuation with exp(-tau_int A_nu_comp) on the selected neutral state.",
        "Derive the trace-over-spectral-spread normalization from the neutral action, rather than from the successful A42 postcheck.",
    ]

    packet = {
        "schema": "MTTSelectedNeutralCompositeSpectralAttenuationReductionOrBranchBridgeTheorem.v1",
        "status": STATUS,
        "predecessor": "MTT_Selected_NeutralUniversalE0AttenuationCandidate_or_SourceLawFrontier_v1",
        "theorem": {
            "name": "NeutralCompositeSpectralAttenuationReductionAndSourceNoGoTheorem",
            "proved": reduction_theorem_proved,
            "statement": "Conditionally on the M-theory lift, the A42 attenuation is exactly one heat-semigroup factor: because tau_int=log(448)/15 and the selected exact Z64 cost is 15, 448^-11 exp(-tau_int/4)=exp[-tau_int(11*15+1/4)]=exp(-tau_int*661/4). Native MTT is 10D, and no theorem currently places the physical neutral operator on the 11D lift. The A41 three-basin normalization obeys Tr(C-c_min I)=Delta_c(1+r), so 1/(1+r) is the unit-trace normalization of the spectral-diameter-normalized shape. These algebraic reductions are proved. Source promotion is not: the corpus does not select eleven Z64 blocks in one neutral operator, does not promote the nil 1/4 benchmark to the selected global A_int spectrum, explicitly lacks the Z64/nil branch bridge, and does not derive the trace-over-spread normalization from the action.",
        },
        "exact_spectral_compression": {
            "N": N,
            "tau_int": tau,
            "selected_circle_cost": circle_cost,
            "dimension_count": dimension_count,
            "nil_floor_candidate": {"numerator": 1, "denominator": 4, "status": "BENCHMARK_SATURATION_NOT_SELECTED_GLOBAL_AINT_EIGENVALUE"},
            "composite_eigenvalue": {"numerator": composite_eigenvalue.numerator, "denominator": composite_eigenvalue.denominator, "text": str(composite_eigenvalue)},
            "identity": "448^-11*exp(-tau_int/4)=exp[-tau_int*(11*15+1/4)]=exp(-tau_int*661/4)",
            "direct_factor": direct_factor,
            "compressed_factor": compressed_factor,
            "checks": exact_checks,
        },
        "conditional_closing_operator": {
            "native_dimension_census": "Y^4 + circle rank 1 + lens-added rank 2 + nil-added rank 3 = 10",
            "conditional_lifted_dimension_census": "native MTT 10D + M-theory lift circle rank 1 = 11",
            "dimension_census_closed_from_corpus": source_premises["recursive_dimension_census_4_plus_1_plus_2_plus_3_plus_1_is_11"],
            "physical_neutral_operator_lifted_to_11D": False,
            "Hilbert_space": "H_nu^comp = (tensor product over a=1..11 of H_64^(a)) tensor H_nil",
            "operator": "A_nu^comp = sum_a A_64^(a) + A_nil",
            "selected_state_condition": "A_64^(a) psi_a=15 psi_a for all a; A_nil psi_nil=(1/4) psi_nil",
            "semigroup_consequence": "exp(-tau_int A_nu^comp) psi = exp(-tau_int*661/4) psi",
            "mathematical_implication_proved": True,
            "operator_selected_by_MTT": False,
            "shared_circle_requirement": "The eleven factors must be functorial contributions of the recursive Y4/circle/lens/nil/lift geometry through one shared central-circle bundle, not eleven independent circles.",
        },
        "native_10D_counterfactual": {
            "purpose": "Show that the successful exponent is not the native MTT dimension by default.",
            "composite_eigenvalue": str(native_composite_eigenvalue),
            "attenuation_factor": native_factor,
            "mu_nu_eV": native_mu_eV,
            "A_nu_eV2": native_A_eV2,
            "ratio_to_A40_A_nu": native_A_eV2 / float(a42["predictions_and_postchecks"]["A_nu"]["observed_profile_value"]),
            "native_10D_matches_neutral_profile": False,
        },
        "profile_normalization_reduction": {
            "cosine_eigenvalues_ordered": cosine,
            "spectral_spread": spread,
            "ratio_r_nu": ratio,
            "diameter_normalized_shape_eigenvalues": normalized_shape,
            "trace_of_normalized_shape": trace_normalized,
            "identity": "Q=(C-c_min I)/Delta_c has spectrum [0,r,1] and Tr(Q)=1+r",
            "A42_normalization_interpretation": "division by 1+r is unit-trace normalization of Q",
            "identities": profile_identities,
            "selected_action_uses_this_normalization": False,
        },
        "source_premise_audit": source_premises,
        "source_no_go": {
            "current_strict_source_promotion_possible": False,
            "reason": "At least four indispensable premises are absent, and the GR branch audit explicitly forbids cross-branch substitution of the Z64 cost and nil benchmark without a selected A_int bridge.",
            "candidate_numerically_refuted": False,
            "candidate_structurally_sharpened": True,
            "required_promotion_clauses": required_promotion,
        },
        "epistemic_policy": {
            "new_target_fit_performed": False,
            "inherits_A42_target_ranked_discovery": True,
            "claims_physical_prediction": False,
            "claims_11D_dimension_implies_tensor_multiplicity": False,
            "claims_nil_floor_is_selected_saturation": False,
            "claims_cross_branch_bridge": False,
        },
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_NeutralCompositeSpectralAttenuationReduction_or_BranchBridgeTheorem_v1",
        "status": STATUS,
        "theorem_proved": reduction_theorem_proved,
        "composite_eigenvalue_exact": str(composite_eigenvalue),
        "attenuation_compression_identity_closed": exact_checks["attenuation_compression_identity"],
        "profile_normalization_identity_closed": exact_checks["all_profile_identities"],
        "elevenfold_multiplicity_selected": source_premises["eleven_Z64_cost_blocks_selected_in_one_neutral_operator"],
        "neutral_operator_selected_on_11D_lift": source_premises["physical_neutral_operator_selected_on_M_theory_11D_lift"],
        "nil_quarter_saturation_selected": source_premises["nil_floor_one_quarter_selected_as_global_Aint_saturation"],
        "same_operator_branch_bridge_closed": source_premises["Z64_and_nil_values_bridged_in_same_operator_convention"],
        "selected_action_normalization_closed": source_premises["profile_trace_over_spread_normalization_selected_by_action"],
        "strict_source_promotion_closed": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected Neutral Composite Spectral Attenuation Reduction or Branch-Bridge Theorem v1

## Exact reduction

The selected exact central-circle block has cost `15`, and the shared internal
proper time is `tau_int=log(448)/15`. Therefore

```text
exp(-15 tau_int) = 1/448,
448^-11 exp(-tau_int/4)
  = exp[-tau_int(11*15+1/4)]
  = exp[-tau_int*(661/4)].
```

Thus A42 does not need two unrelated numerical corrections. It asks for one
selected neutral eigenvalue `661/4` of a composite heat-kernel generator.

The A41 profile normalization also has an exact interpretation. For ordered
cosine eigenvalues and `Delta_c=c_max-c_min`,

```text
Q=(C-c_min I)/Delta_c,
spec(Q)=[0,r_nu,1],
Tr(Q)=1+r_nu.
```

Hence division by `1+r_nu` is precisely unit-trace normalization of the
spectral-diameter-normalized three-basin shape.

The corpus does close the dimensional census behind the exponent: the external
base contributes `4`, the recursive circle/lens/nil hierarchy contributes
`1+2+3=6`, and the M-theory circle lift contributes `1`, totaling `11`.
But native MTT stops at the first two terms and is 10D. The final `+1` belongs
to the conditional M-theory lift. No current theorem places the physical
neutral operator on that lift, and the native 10D version misses the A40 scale
by a factor of `{native_A_eV2 / float(a42["predictions_and_postchecks"]["A_nu"]["observed_profile_value"])}` in `A_nu`.
The dimension census also does not replicate the same cost-15 operator on every
direction.

## Source decision

The formula is structurally sharper but is not yet promoted. The current
M-theory corpus supplies an 11D circle lift, not eleven selected `Z64` heat
blocks. The exact cost `15` and the nil value `1/4` also come from different
source statuses: `15` is selected on the exact central-circle branch, while
`1/4` is a benchmark saturation/universal lower bound and is explicitly not a
selected global `A_int` eigenvalue. The GR branch audit forbids combining them
without a same-operator bridge. Finally, no selected neutral action currently
chooses the trace-over-spread normalization.

A sufficient closing construction is

```text
H_nu^comp = (tensor product_a=1^11 H_64^(a)) tensor H_nil,
A_nu^comp = sum_a A_64^(a) + A_nil,
spec_selected(A_nu^comp) = 11*15 + 1/4 = 661/4,
```

with all eleven contributions proved to arise functorially from the recursive
`4+(1+2+3)+1` geometry through one shared central-circle bundle rather than
eleven independent circles. This conditional
operator implication is exact. Selection of that operator is the remaining
theorem.

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
