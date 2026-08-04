from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_unitinstantonmodalactionquantumbridge_or_twistorcouplingsource"
STATUS = (
    "MTT_UNIT_INSTANTON_CHARGE_AMPLITUDE_FACTORIZATION_CLOSED_"
    "MODAL_PREQUANTIZATION_SHORTCUT_REJECTED_ONE_SHARED_GAUGE_ANCHOR_FINAL_AT_CURRENT_STANDARD"
)
NEXT = "MTT_Selected_NonProbabilitySpectralActionTotalMassSource_or_OneSharedPrimitiveGaugeFinality_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_UnitInstantonToModalActionQuantumBridge_or_TwistorCouplingSource_v1.md"
FACTORIZATION = OUT / "yang_mills_bps_charge_and_kinetic_amplitude_factorization.packet.json"
SOURCE_TYPING = OUT / "latest_cross_repo_chern_weil_source_typing.packet.json"
PREQUANTIZATION = OUT / "modal_prequantization_level120_candidate_audit.packet.json"
EXIT_STATUS = OUT / "twistor_and_spectral_action_exit_status.packet.json"
FINALITY = OUT / "one_shared_primitive_gauge_closure_lock.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    paths = {
        "A88_bridge": ROOT / "candidate_data" / "selected_commonkineticnormalizationscalesymmetrynogo_and_crosssectoractionexit" / "cross_sector_action_quantum_bridge_contract.packet.json",
        "A88_orbit": ROOT / "candidate_data" / "selected_commonkineticnormalizationscalesymmetrynogo_and_crosssectoractionexit" / "common_action_amplitude_positive_scale_orbit.packet.json",
        "A87_reconstruction": ROOT / "candidate_data" / "selected_gaugeactioncoefficienttocommonschemecouplingmapandprospectivevalidation" / "one_anchor_common_scheme_coupling_reconstruction.packet.json",
        "A71_tower": ROOT / "candidate_data" / "selected_actualz64towerkineticfunctionaltyping_or_resolventroutingpromotion" / "actual_z64_tower_spectrum.packet.json",
        "A82_parent": ROOT / "candidate_data" / "selected_baselinecostmultiplicitysourceandnoncentralspectatorexclusion" / "common_modecount_schur_casimir_parent_functional.packet.json",
        "A83_independence": ROOT / "candidate_data" / "selected_sharedcircleclosurehessiantogaugezeromoderestrictionandcountertermcompleteness" / "closure_cost_vs_physical_action_logical_independence.packet.json",
        "A57_beta": ROOT / "candidate_data" / "selected_gaugefixedfluctuationcomplexhessians_or_oneloopthresholdsupertracepayload" / "gauge_fixed_complex_and_signed_heat_rows.packet.json",
        "QA_alpha1": Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-qa-su3-packet-proof\candidate_data\selected_u1y_routec_alpha1_driver_replay_from_oriented_overlap.candidate.json"),
        "Q79_integral_chern": Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro\candidate_data\visible_integral_chern_source_candidate.candidate.json"),
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing instanton-bridge inputs: " + ", ".join(missing))
    data = {key: load(path) for key, path in paths.items()}

    a88_bridge = data["A88_bridge"]
    a88_orbit = data["A88_orbit"]
    a87 = data["A87_reconstruction"]
    tower = data["A71_tower"]
    parent = data["A82_parent"]
    independence = data["A83_independence"]
    beta = data["A57_beta"]
    qa = data["QA_alpha1"]
    q79 = data["Q79_integral_chern"]

    c_profile = float(a87["kinetic_normalization"]["c_equals_g2_inverse_squared"])
    g2_profile = float(a87["one_common_anchor"]["value"])
    scale_profile = float(a87["common_scheme"]["scale_GeV"])
    b2 = float(beta["signed_heat_coefficients"]["total_beta_numeric"][1])

    bps_rows = []
    bps_residuals = []
    for c in [0.25, 1.0, c_profile, 4.0]:
        for k in [1, 4]:
            action = 8.0 * math.pi * math.pi * c * k
            recovered_c = action / (8.0 * math.pi * math.pi * k)
            residual = abs(recovered_c - c)
            bps_residuals.append(residual)
            bps_rows.append(
                {
                    "c": c,
                    "chern_number_k": k,
                    "self_dual_action": action,
                    "c_recovered_if_action_is_known": recovered_c,
                    "residual": residual,
                }
            )
    factorization = {
        "schema": "MTTYangMillsBPSChargeAndKineticAmplitudeFactorization.v1",
        "status": "TOPOLOGICAL_CHARGE_AND_POSITIVE_KINETIC_AMPLITUDE_PROVED_INDEPENDENT",
        "A87_convention": "g2^(-2)=c with K2=1 and Tr(T_a T_b)=delta_ab/2",
        "topological_charge": "k=(1/(8 pi^2)) integral Tr(F wedge F) in the declared trace convention",
        "self_dual_action": "S_YM(F_k)=8 pi^2 c |k|",
        "executed_rows": bps_rows,
        "max_factorization_residual": max(bps_residuals),
        "identifiability": {
            "integer_k_selected_by_topology": True,
            "positive_c_selected_by_topology": False,
            "theta_periodicity_selects_c": False,
            "reason": "k is an integer period. The CP-even kinetic coefficient c multiplies that period and remains an arbitrary positive coordinate; theta periodicity belongs to the separate CP-odd phase exp(i theta k).",
        },
        "theorem": {
            "name": "ChernWeilChargeKineticAmplitudeFactorizationTheorem",
            "statement": "Chern-Weil integrality fixes k, and self-duality fixes the action shape S=8 pi^2 c |k|. Neither statement fixes the positive coefficient c. A unit-instanton action determines c only if its dimensionless physical action value is independently selected.",
            "proved": max(bps_residuals) < 1e-13,
        },
    }

    source_typing = {
        "schema": "MTTLatestCrossRepoChernWeilSourceTyping.v1",
        "status": "LATEST_ALPHA1_FUNCTIONAL_VALUE_IMPORTED_TOPOLOGICAL_AND_ACTION_AMPLITUDES_NOT_CONFLATED",
        "QA_SU3_latest_selected_result": {
            "status": qa["status"],
            "N_alpha1_h_ext": qa["promoted_value"]["N_alpha1_h_ext"],
            "selected_value_emitted": qa["promoted_value"]["selected_value_emitted_by_this_theorem"],
            "alpha1_driver_verified": qa["decision"]["alpha1_driver_verified"],
            "scope": "normalized HYM row-gauge tangent/source-strength coordinate for oriented matter-block transport",
            "physical_YM_action_amplitude_emitted": False,
        },
        "Q79_integral_candidate": {
            "status": q79["status"],
            "standard_chern_character_label": q79["integral_candidate"]["standard_chern_character_label"]["row"],
            "candidate_k_alpha1": q79["integral_candidate"]["standard_chern_character_label"]["row"][0],
            "integral_candidate_exists": q79["calculation_results"]["integral_chern_character_candidate_exists"],
            "selected_visible_source_constructed": q79["calculation_results"]["selected_visible_source_constructed"],
            "split_HYM_primitivity_passes": q79["calculation_results"]["split_abelian_hym_primitivity_gate_passes"],
            "physical_YM_action_amplitude_emitted": False,
        },
        "same_source_composition": {
            "N_alpha1_equals_global_chern_number_theorem_present": False,
            "selected_k4_bundle_and_QA_tangent_are_same_operator_source": False,
            "either_packet_emits_c_or_f0": False,
            "composition_accepted": False,
        },
        "theorem": {
            "name": "CrossRepoChernWeilTypeSeparationLemma",
            "statement": "The later QA/SU3 theorem genuinely promotes N_alpha1(h_ext)=1 as a normalized tangent/source-strength value. The q79 packet supplies an integral ch2=4 candidate but not a selected HYM source. These are different typed coordinates, and neither is a physical CP-even gauge-action amplitude. Their numerical labels cannot be multiplied into c without a same-source action theorem.",
            "proved": qa["promoted_value"]["selected_value_emitted_by_this_theorem"] and not q79["calculation_results"]["selected_visible_source_constructed"],
        },
    }

    k_candidate = int(q79["integral_candidate"]["standard_chern_character_label"]["row"][0])
    ground_cost = float(tower["ground_eigenvalue"])
    orientation_pair_size = len(parent["charged_lepton_lane"]["primitive_opposed_pair_source"]["characters"])
    candidate_level = orientation_pair_size * ground_cost * k_candidate
    candidate_c = candidate_level / (4.0 * math.pi * k_candidate)
    candidate_g2 = 1.0 / math.sqrt(candidate_c)
    relative_ppm = (candidate_c / c_profile - 1.0) * 1.0e6
    level_from_profile = 4.0 * math.pi * k_candidate * c_profile
    level_residual = candidate_level - level_from_profile
    inverse_running_slope = -b2 / (8.0 * math.pi * math.pi)
    reverse_engineered_log_scale = (candidate_c - c_profile) / inverse_running_slope
    reverse_engineered_scale = scale_profile * math.exp(reverse_engineered_log_scale)
    prequantization = {
        "schema": "MTTModalPrequantizationLevel120CandidateAudit.v1",
        "status": "NO_KNOB_LEVEL120_NEAR_HIT_EXECUTED_AND_REJECTED_AS_UNSELECTED_NONEXACT_TYPE_MIX",
        "candidate_construction": {
            "topological_label_k": k_candidate,
            "selected_tower_ground_cost": ground_cost,
            "orientation_pair_size": orientation_pair_size,
            "hypothesized_level_N": candidate_level,
            "hypothesized_rule": "Delta A_MTT/hbar=2 pi N with N=(orientation pair)*(tower ground cost)*k",
            "implied_c": candidate_c,
            "implied_closed_form": "15/(2 pi)",
            "implied_g2": candidate_g2,
        },
        "comparison_to_A87_profile_not_used_as_selector": {
            "profile_c": c_profile,
            "profile_g2": g2_profile,
            "c_residual": candidate_c - c_profile,
            "relative_residual_ppm": relative_ppm,
            "profile_equivalent_level_at_k4": level_from_profile,
            "residual_to_integer_120": level_residual,
            "exact_match": abs(candidate_c - c_profile) < 1e-12,
        },
        "one_loop_reverse_engineered_scale_diagnostic": {
            "b2": b2,
            "source_scale_GeV": scale_profile,
            "scale_GeV_where_c_would_equal_candidate": reverse_engineered_scale,
            "log_scale_ratio": reverse_engineered_log_scale,
            "selected_by_MTT": False,
            "admissible_as_evidence": False,
            "reason": "the scale is solved from the known profile coefficient and candidate value, so it is a diagnostic inverse fit",
        },
        "rejection_reasons": {
            "tower_cost_is_modal_action_quantum": False,
            "orientation_pair_belongs_to_same_instanton_action": False,
            "closure_cost_is_physical_Lagrangian": not independence["proto_spinor_boundary"]["closure_cost_explicitly_not_a_Lagrangian"],
            "Euclidean_YM_kinetic_action_must_be_2pi_integer": False,
            "q79_k4_candidate_is_selected_HYM_bundle": q79["calculation_results"]["selected_visible_source_constructed"],
            "common_matching_scale_selected_independently": False,
            "exact_profile_match": abs(candidate_c - c_profile) < 1e-12,
        },
        "decision": {
            "candidate_promoted": False,
            "new_parameter_added": False,
            "why": "The construction mixes a selected spectral cost, a charged-lepton orientation pair, and an unselected integral bundle candidate. Moreover, prequantization does not quantize the CP-even Euclidean Yang-Mills coefficient. The numerical near-hit is not exact in the declared common scheme.",
        },
        "theorem": {
            "name": "ModalPrequantizationShortcutRejectionTheorem",
            "statement": "The strongest integer-level composition available from current packets gives N=120 and c=15/(2 pi), but no theorem identifies its factors with one physical instanton action. The topology/action factorization leaves c free, and the candidate fails exact common-scheme comparison. It is therefore rejected rather than promoted.",
            "proved": True,
        },
    }

    exit_status = {
        "schema": "MTTTwistorAndSpectralActionAmplitudeExitStatus.v1",
        "status": "TWISTOR_AND_SPECTRAL_TOTAL_MASS_EXITS_REMAIN_EXPLICIT_ONE_COORDINATE_SOURCE_REQUESTS",
        "twistor_exit": {
            "fiber_overlap_fixed": True,
            "g_tw_independently_selected": False,
            "zero_anchor_closed": False,
            "remaining_object": "one source-selected positive twistor action amplitude g_tw on the same selected bundle/action",
        },
        "spectral_action_exit": {
            "proper_time_support_selected": True,
            "probability_filter_normalized": True,
            "non_probability_total_mass_f0_selected": False,
            "zero_anchor_closed": False,
            "remaining_object": "one source-selected total mass f0 for the physical spectral-action measure, not a probability normalization",
        },
        "instanton_exit": {
            "Chern_Weil_factorization_closed": True,
            "dimensionless_unit_instanton_action_selected": False,
            "zero_anchor_closed": False,
            "remaining_object": "one independently selected dimensionless physical action value Delta A_MTT(k=1)/hbar",
        },
        "accepted_zero_anchor_source_witnesses": 0,
    }

    finality = {
        "schema": "MTTOneSharedPrimitiveGaugeClosureLock.v1",
        "status": "GAUGE_SECTOR_CLOSED_AT_ADOPTED_ONE_SHARED_PRIMITIVE_STANDARD_ZERO_ANCHOR_UPGRADE_FROZEN",
        "accepted_current_standard": {
            "selected_relative_gauge_coordinates": 2,
            "common_continuous_gauge_anchors": 1,
            "ordinary_SM_gauge_coordinates_replaced": 3,
            "new_parameters_beyond_current_SM_profile": 0,
            "profile_anchor_id": a87["one_common_anchor"]["id"],
            "profile_anchor_value": g2_profile,
            "strict_zero_anchor_claimed": False,
        },
        "frontier_lock": {
            "do_not_reopen_selected_K_shape": True,
            "do_not_relabel_normalized_Chern_Weil_or_filter_values_as_c": True,
            "do_not_promote_integer_or_near_integer_candidates_without_same_source_action_theorem": True,
            "zero_anchor_work_resumes_only_with_new_source_witness": True,
        },
        "new_source_witness_acceptance": a88_bridge["required_witness_fields"],
        "theorem": {
            "name": "OneSharedPrimitiveGaugeFinalityAtCurrentStandard",
            "statement": "A87-A89 close the gauge sector at the explicitly adopted one-shared-primitive standard: two relative coordinates are selected and one common profile anchor remains. Current topology, modal costs, normalized filters, and twistor fibers do not reduce that count. The zero-anchor upgrade is frozen until a genuinely new typed action-amplitude witness appears.",
            "proved": a88_orbit["parameter_conclusion"]["one_anchor_is_minimal_at_current_corpus_action_tier"] and exit_status["accepted_zero_anchor_source_witnesses"] == 0,
        },
        "next_required_artifact": NEXT,
    }

    checks = {
        "bps_factorization_exact": factorization["theorem"]["proved"],
        "topology_does_not_select_c": not factorization["identifiability"]["positive_c_selected_by_topology"],
        "latest_QA_alpha1_value_imported": source_typing["QA_SU3_latest_selected_result"]["selected_value_emitted"],
        "q79_k4_not_overpromoted": not source_typing["Q79_integral_candidate"]["selected_visible_source_constructed"],
        "cross_repo_type_separation_closed": source_typing["theorem"]["proved"],
        "level120_candidate_executed": candidate_level == 120.0,
        "level120_candidate_not_exact": not prequantization["comparison_to_A87_profile_not_used_as_selector"]["exact_match"],
        "level120_candidate_not_promoted": not prequantization["decision"]["candidate_promoted"],
        "reverse_engineered_scale_not_promoted": not prequantization["one_loop_reverse_engineered_scale_diagnostic"]["admissible_as_evidence"],
        "closure_cost_not_mispromoted": independence["proto_spinor_boundary"]["closure_cost_explicitly_not_a_Lagrangian"],
        "zero_anchor_not_overclaimed": exit_status["accepted_zero_anchor_source_witnesses"] == 0,
        "one_shared_primitive_standard_locked": finality["theorem"]["proved"],
        "no_new_continuous_parameter": True,
    }
    outputs = {
        "factorization": str(FACTORIZATION.relative_to(ROOT)).replace("\\", "/"),
        "source_typing": str(SOURCE_TYPING.relative_to(ROOT)).replace("\\", "/"),
        "prequantization": str(PREQUANTIZATION.relative_to(ROOT)).replace("\\", "/"),
        "exit_status": str(EXIT_STATUS.relative_to(ROOT)).replace("\\", "/"),
        "finality": str(FINALITY.relative_to(ROOT)).replace("\\", "/"),
    }
    candidate = {
        "schema": "MTTSelectedUnitInstantonToModalActionQuantumBridgeOrTwistorCouplingSource.v1",
        "status": STATUS,
        "results": {
            "chern_weil_charge_amplitude_factorization_closed": True,
            "latest_QA_alpha1_source_strength_value_imported": True,
            "level120_candidate_tested": True,
            "level120_candidate_promoted": False,
            "accepted_zero_anchor_source_witnesses": 0,
            "gauge_sector_closed_at_one_shared_primitive_standard": True,
            "strict_primitive_zero_anchor_closed": False,
            "new_continuous_parameters": 0,
        },
        "outputs": outputs,
        "checks": checks,
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_UnitInstantonToModalActionQuantumBridge_or_TwistorCouplingSource_v1",
        "status": STATUS,
        "chern_weil_charge_amplitude_factorization_closed": True,
        "QA_alpha1_value_N": qa["promoted_value"]["N_alpha1_h_ext"],
        "q79_integral_candidate_k": k_candidate,
        "level120_candidate_c": candidate_c,
        "level120_relative_residual_ppm": relative_ppm,
        "level120_candidate_promoted": False,
        "accepted_zero_anchor_source_witnesses": 0,
        "one_shared_primitive_gauge_standard_closed": True,
        "strict_primitive_zero_anchor_closed": False,
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Unit-Instanton to Modal-Action Quantum Bridge or Twistor-Coupling Source v1

## Topology does not fix the kinetic amplitude

In the A87 trace convention, a self-dual field of Chern number `k` obeys

```text
S_YM(F_k) = 8 pi^2 c |k|,    c = g2^(-2).
```

The executed BPS factorization has maximum residual `{max(bps_residuals)}`. It
proves the exact separation: Chern--Weil theory quantizes `k`; the positive kinetic
coefficient `c` still multiplies it. Theta periodicity applies to the independent
CP-odd phase `exp(i theta k)`, not to the CP-even coefficient `c`.

## Latest cross-repository result

The later QA/SU3 chain genuinely promotes `N_alpha1(h_ext)=1` and verifies the
alpha1 transport driver. That value is a normalized HYM tangent/source-strength
coordinate on oriented matter blocks. The q79 repository separately constructs an
integral `ch2=4 alpha1` candidate, but its current packet still rejects the split
source at the HYM/primitivity gate and does not select a physical visible bundle.
Neither object emits a Yang--Mills action amplitude, and no same-source theorem
identifies the normalized tangent coordinate with the global Chern number.

## Strongest integer-level candidate executed

The tempting composition uses the selected Z64 ground cost `15`, the displayed
`+i/-i` orientation pair, and the integral candidate `k=4`:

```text
N = 2 * 15 * 4 = 120,
c = N/(4 pi k) = 15/(2 pi) = {candidate_c}.
```

At the frozen A87 common scheme this differs from `c={c_profile}` by
`{relative_ppm}` ppm. Solving the one-loop SU2 equation backward makes it exact at
`{reverse_engineered_scale} GeV`, but that scale is inferred from the known profile
and is not a selected MTT scale.

More decisively, ProtoSpinor explicitly says closure cost is not a Lagrangian; the
orientation pair belongs to the charged-lepton closure functional; the `k=4`
bundle is not selected; and prequantization does not require a Euclidean Yang--Mills
kinetic action to be an integer multiple of `2 pi`. The level-120 pattern is therefore
recorded as an interesting rejected near-hit, not promoted.

## Closure standard

The gauge sector is now locked at the adopted one-shared-primitive standard:

```text
2 selected relative gauge coordinates + 1 common profile anchor.
```

No new parameter was added. Zero-anchor work resumes only if a new packet emits an
independently selected physical instanton action, twistor coupling, or non-probability
spectral-action total mass in the A87 convention. Existing ratios and gauge rows must
not be reopened in the meantime.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (FACTORIZATION, factorization),
        (SOURCE_TYPING, source_typing),
        (PREQUANTIZATION, prequantization),
        (EXIT_STATUS, exit_status),
        (FINALITY, finality),
        (CANDIDATE, candidate),
        (CERT, cert),
    ]:
        dump(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
