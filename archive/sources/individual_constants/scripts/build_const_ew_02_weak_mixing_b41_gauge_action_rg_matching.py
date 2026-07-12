"""Build CONST-EW-02 B41 gauge-action and RG/matching frontier packet."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"

SM_PARITY = ROOT.parent / "mtt-sm-parity-closure"
THETA_CORPUS = ROOT.parent / "18 Theta-Closure & Execution Program" / "_md_v3_corrected"

SLUG = "const_ew_02_weak_mixing_b41_gauge_action_rg_matching"
BASE = DATA / SLUG
OUTPUT = DATA / f"{SLUG}.candidate.json"
GAUGE_ANCHOR = BASE / "gauge_action_anchor_status.packet.json"
RG_MATCHING = BASE / "rg_matching_threshold_scheme_status.packet.json"
THETA_CLASS = BASE / "theta_v_prediction_classification.packet.json"
BOUNDARY = BASE / "weak_mixing_b41_boundary.packet.json"
NEXT_WORK = BASE / "next_labeled_workorder.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_CONST_EW_02_WeakMixing_B41_GaugeAction_RGMatching_v1.md"

STATUS = "MTT_CONST_EW_02_B41_GAUGE_ACTION_RG_MATCHING_BUILT_ANCHOR_VALUES_OPEN"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def maybe_load(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"missing": True, "path": rel(path)}
    return load(path)


def main() -> int:
    BASE.mkdir(parents=True, exist_ok=True)

    b40_path = DATA / "const_ew_02_weak_mixing_b40_local_kernel_to_profile.candidate.json"
    b40_gate_path = DATA / "const_ew_02_weak_mixing_b40_local_kernel_to_profile" / "physical_weak_angle_gate_after_local_kernel.packet.json"
    b26_contract_path = DATA / "const_ew_02_weak_mixing_b26_two_edge_promotion_contract" / "gaugekinetic_rg_source_contract.packet.json"

    a5_path = DATA / "const_em_01_alpha1_kphys_source_hunt.candidate.json"
    a6_path = DATA / "const_em_01_alpha1_dimensional_anchor_packet_gate.candidate.json"
    a10_path = DATA / "const_em_01_alpha1_universal_primitive_or_nogo.candidate.json"

    sm_rg_policy_path = SM_PARITY / "candidate_data" / "sm_equivalence_rgpolicy_covariance_and_observable_suite.candidate.json"
    sm_rg_engine_path = SM_PARITY / "candidate_data" / "selected_rgengineexecution_or_selectedsmpacketcertificateintegration.candidate.json"
    sm_rg_accept_path = SM_PARITY / "candidate_data" / "selected_acceptedrgtransportvalues_or_qasu3sourcepacket.candidate.json"

    theta_i_path = THETA_CORPUS / "Theta_Closure_in_Modal_Triplet_Theory_I__Gauge_Couplings_from_Internal_Geometry.md"
    theta_iii_path = THETA_CORPUS / "Theta_Closure_in_Modal_Triplet_Theory_III__Twistor_Action_Matching_and_Independent_Normalization.md"
    theta_v_path = THETA_CORPUS / "Theta_Closure_in_Modal_Triplet_Theory_V__Redundant_Determination_from_Gauge_Couplings_and_the_Weak_Mixing_Angle.md"

    b40 = load(b40_path)
    b40_gate = load(b40_gate_path)
    b26_contract = load(b26_contract_path)
    a5 = load(a5_path)
    a6 = load(a6_path)
    a10 = load(a10_path)
    sm_rg_policy = maybe_load(sm_rg_policy_path)
    sm_rg_engine = maybe_load(sm_rg_engine_path)
    sm_rg_accept = maybe_load(sm_rg_accept_path)

    gauge_anchor = {
        "schema": "MTTConstEW02B41GaugeActionAnchorStatus.v1",
        "status": "GAUGE_ACTION_NORMALIZATION_REDUCED_TO_ALPHA_PHYS_OR_ONE_PRIMITIVE_SOURCE_UNIT",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B41-GAUGE-ACTION-NORMALIZATION-ANCHOR",
        "inputs": {
            "B40_candidate": rel(b40_path),
            "B40_physical_gate": rel(b40_gate_path),
            "alpha_A5_K_phys_hunt": rel(a5_path),
            "alpha_A6_dimensional_anchor_gate": rel(a6_path),
            "alpha_A10_universal_primitive_or_nogo": rel(a10_path),
            "theta_III_twistor_action_normalization": rel(theta_iii_path),
        },
        "superset_path_use": {
            "straight_MTT_path": "Gauge-action normalization is treated as the same physical action/unit anchor isolated by alpha1/K_phys.",
            "theta_twistor_path": "Twistor-action normalization supports internal overlap normalization and same functional object, but does not emit the physical dimensionful action unit.",
            "locked_target": "A selected physical gauge/action normalization in the same trace convention as the weak-split profile.",
        },
        "imported_facts": {
            "B40_moved_active_blocker_to_physical_gate": b40["physical_gate_reduced_to_gauge_action_RG_matching"],
            "A5_K_phys_reduced_to_alpha_phys_or_action_unit": a5["what_closes_now"]["K_phys_reduced_to_alpha_phys_or_action_unit"],
            "A6_selected_dimensional_anchor_gate_built": a6["what_closes_now"]["acceptance_gate"],
            "A10_current_corpus_strict_no_knob_alpha_nogo": a10["what_closes_now"]["strict_current_corpus_nogo"],
            "A10_one_universal_primitive_extension_ready": a10["what_closes_now"]["one_universal_primitive_extension"],
        },
        "decision": {
            "strict_no_knob_physical_action_anchor_closed": False,
            "one_universal_primitive_extension_ready": True,
            "twistor_action_internal_overlap_normalization_support": True,
            "physical_alpha_or_metrology_anchor_closed": False,
            "K_phys_or_f_ab_closed": False,
        },
        "required_to_promote": {
            "strict_tier": "Emit a same-branch target-independent physical action/unit value: alpha_phys, Omega0, ell_p/kappa11/modal gap, or an equivalent K_phys/f_ab anchor.",
            "one_primitive_tier": "Declare one universal metrological primitive once, then reuse it unchanged across alpha1 and weak mixing. This is not strict no-knob closure.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    rg_matching = {
        "schema": "MTTConstEW02B41RGMatchingThresholdSchemeStatus.v1",
        "status": "RG_MATCHING_POLICY_SCAFFOLD_AVAILABLE_VALUES_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B41-RG-MATCHING-THRESHOLD-SCHEME",
        "inputs": {
            "B26_gaugekinetic_RG_contract": rel(b26_contract_path),
            "SM_parity_RG_policy": rel(sm_rg_policy_path),
            "SM_parity_RG_engine": rel(sm_rg_engine_path),
            "SM_parity_accepted_RG_transport": rel(sm_rg_accept_path),
            "theta_I_gauge_couplings": rel(theta_i_path),
            "theta_V_weak_mixing": rel(theta_v_path),
        },
        "external_methodology_constraints": [
            {
                "role": "precision_weak_angle_scheme_and_scale_guardrail",
                "source": "Particle Data Group, 2025 Electroweak Model and Constraints on New Physics review",
                "url": "https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf",
                "imported_use": "Weak mixing angle values depend on renormalization prescription, scale, and effective-angle convention; therefore B41 must declare the scheme before any physical comparison.",
                "value_imported": False,
            },
            {
                "role": "precision_SM_gauge_beta_function_benchmark",
                "source": "Mihaila, Salomon, Steinhauser, Gauge Coupling Beta Functions in the Standard Model to Three Loops, arXiv:1201.5868",
                "url": "https://arxiv.org/abs/1201.5868",
                "imported_use": "Precision physical comparison needs a declared loop order and benchmarkable beta-function convention.",
                "value_imported": False,
            },
            {
                "role": "weak_angle_running_hadronic_threshold_guardrail",
                "source": "Erler, Ferro-Hernandez, Kuberski, Theory Driven Evolution of the Weak Mixing Angle, CERN-TH-2024-071",
                "url": "https://cds.cern.ch/record/2902222/files/2406.16691.pdf",
                "imported_use": "Low-energy weak-angle running involves scheme-dependent higher-order and hadronic vacuum-polarization inputs; these cannot be replaced by an internal ratio alone.",
                "value_imported": False,
            },
        ],
        "policy_scaffold": {
            "reference_scheme_from_sm_parity": sm_rg_policy.get("rg_policy", {}).get("scheme", "UNKNOWN"),
            "reference_scale_from_sm_parity": sm_rg_policy.get("rg_policy", {}).get("reference_scale", "UNKNOWN"),
            "gauge_normalization_from_sm_parity": sm_rg_policy.get("rg_policy", {}).get("gauge_normalization", {}),
            "diagnostic_rg_engine_exists": sm_rg_engine.get("what_closes_now", {}).get("one_loop_RG_engine_contract_built", False),
            "firstpass_RG_acceptance_tier_exists": sm_rg_accept.get("what_closes_now", {}).get("firstpass_RG_acceptance_convention_declared", False),
            "B26_required_source_packet": b26_contract["required_source_packet"],
        },
        "decision": {
            "RG_policy_scaffold_declared": True,
            "one_loop_diagnostic_engine_available": bool(sm_rg_engine.get("what_closes_now", {}).get("one_loop_RG_engine_contract_built", False)),
            "precision_benchmark_values_imported_as_selectors": False,
            "source_selected_mu_match_closed": False,
            "source_selected_threshold_vector_closed": False,
            "precision_RG_threshold_values_closed": False,
            "physical_weak_angle_profile_closed": False,
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    theta_class = {
        "schema": "MTTConstEW02B41ThetaVPredictionClassification.v1",
        "status": "THETA_V_WEAK_ANGLE_VALUES_CLASSIFIED_AS_DIAGNOSTIC_OR_ONE_ANCHOR_REPLAY_NOT_SOURCE_CLOSURE",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B41-THETA-V-CLASSIFICATION",
        "inputs": {
            "theta_V_weak_mixing_paper": rel(theta_v_path),
            "theta_I_gauge_coupling_targets": rel(theta_i_path),
            "theta_III_twistor_action": rel(theta_iii_path),
        },
        "theta_V_reported_values": {
            "tree_level_matching_sin2_MZ_approx": 0.23120,
            "threshold_scan_sin2_MZ_approx_range": [0.23157, 0.23214],
            "delta_r_eff_scan": [0.02, 0.05],
            "imported_as_source_value": False,
        },
        "classification": {
            "round_trip_consistency": True,
            "non_circular_test_template": True,
            "strict_no_knob_physical_weak_angle_closure": False,
            "reason_strict_not_closed": [
                "Theta I/V use measured gauge/electroweak information in target or normalization slots.",
                "The physical gauge/action normalization is not source-selected in the current strict branch.",
                "Threshold matching and mu_match are not independently selected by the current source packet.",
            ],
            "allowed_use": "Use as a benchmarked replay/profile template once the physical anchor and RG/matching policy are selected.",
            "forbidden_use": "Do not promote the reported numeric weak-angle values as selected source closure.",
        },
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    boundary = {
        "schema": "MTTConstEW02B41Boundary.v1",
        "status": "B41_PHYSICAL_GATE_FRONTIER_LOCKED_STRICT_ANCHOR_AND_RG_VALUES_OPEN",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B41-BOUNDARY",
        "previous_B40_status": b40["status"],
        "closed_or_decided_now": {
            "C1_local_source_kernel_remains_retired_as_active_local_blocker": True,
            "gauge_action_anchor_reduced_to_alpha_phys_or_universal_action_unit": True,
            "one_universal_primitive_tier_identified_and_guardrailed": True,
            "RG_matching_policy_scaffold_declared": True,
            "Theta_V_values_classified_without_promotion": True,
            "external_precision_constraints_imported_as_methodology_not_selectors": True,
        },
        "still_open": {
            "strict_no_knob_physical_action_anchor": True,
            "physical_alpha_or_metrology_anchor": True,
            "K_phys_or_f_ab_value": True,
            "source_selected_mu_match": True,
            "source_selected_threshold_vector": True,
            "precision_RG_threshold_values": True,
            "physical_weak_angle_numerical_closure": True,
            "strict_full_no_knob_closure": True,
        },
        "anti_cycle_delta_from_B40": {
            "B40": "moved the active local-tier blocker from dynamic C1 source ownership to physical gauge/action/RG matching",
            "B41": "locks the physical gate into two named lanes: action-unit anchoring and RG/matching execution",
            "not_repeated": [
                "not re-opening C1 source-kernel ownership",
                "not treating Theta V reported values as source-selected closure",
                "not using observed weak angle, alpha, or benchmark values as source selectors",
            ],
        },
        "allowed_claim": "B41 gives a machine-checkable physical-frontier contract and a legal one-primitive bridge option.",
        "forbidden_claim": "strict no-knob physical weak-angle prediction or precision SM weak-angle closure",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    next_work = {
        "schema": "MTTConstEW02B41NextWork.v1",
        "status": "NEXT_WORKORDER_B42_ONE_ANCHOR_OR_STRICT_SOURCE_UNIT_THEN_RG_EXECUTION",
        "active_label": "CONST-EW-02 / WEAK-MIXING / B42-PHYSICAL-NORMALIZATION-OR-RG-ENGINE-EXECUTION",
        "primary": {
            "label": "CONST-EW-02 / WEAK-MIXING / B42-SELECTED-ACTION-UNIT-OR-ONE-PRIMITIVE-BRIDGE",
            "task": "Either derive a selected physical action/unit anchor from corpus sources, or explicitly enter the one-universal-primitive tier and reuse that primitive unchanged from alpha1 into weak mixing.",
        },
        "parallel": {
            "label": "CONST-EW-02 / WEAK-MIXING / B42-RG-ENGINE-EXECUTION-WITH-LOCKED-SCHEME",
            "task": "Run the selected weak profile through a declared MSbar/GUT-normalized RG/matching policy with source-tagged mu_match and thresholds, classifying any observed inputs as replay checks only.",
        },
        "success_condition": {
            "strict_tier": "selected physical action unit + selected mu_match + selected threshold vector + RG convention, all source-tagged before observed comparison",
            "one_primitive_tier": "one primitive declared once, alpha1 and weak mixing both replayed from it without per-observable retuning",
        },
    }

    candidate = {
        "candidate": "MTTConstEW02WeakMixingB41GaugeActionRGMatching",
        "status": STATUS,
        "active_label": "CONST-EW-02 / WEAK-MIXING / B41-GAUGE-ACTION-RG-MATCHING",
        "output_packets": {
            "gauge_action_anchor_status": rel(GAUGE_ANCHOR),
            "rg_matching_threshold_scheme_status": rel(RG_MATCHING),
            "theta_v_prediction_classification": rel(THETA_CLASS),
            "weak_mixing_b41_boundary": rel(BOUNDARY),
            "next_labeled_workorder": rel(NEXT_WORK),
        },
        "theorem": {
            "name": "CONSTEW02B41GaugeActionRGMatchingFrontierTheorem",
            "proved": True,
            "statement": (
                "After the B40 local source-kernel handoff, physical weak-angle closure is equivalent to supplying a selected physical gauge/action normalization together with a selected matching scale, RG scheme, and threshold vector. Current corpus, repo, and external benchmark imports close the contract and classify the Theta weak-angle replay as diagnostic or one-anchor replay, but they do not supply strict no-knob physical normalization or source-selected RG threshold values."
            ),
        },
        "gauge_action_anchor_reduced": True,
        "one_universal_primitive_extension_ready": True,
        "RG_matching_policy_scaffold_declared": True,
        "theta_V_values_classified_not_promoted": True,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
    }

    cert = {
        "certificate": "MTT_CONST_EW_02_WeakMixing_B41_GaugeAction_RGMatching_v1",
        "status": STATUS,
        "candidate_path": rel(OUTPUT),
        "note_path": rel(NOTE),
        "gauge_action_anchor_reduced": True,
        "one_universal_primitive_extension_ready": True,
        "RG_matching_policy_scaffold_declared": True,
        "theta_V_values_classified_not_promoted": True,
        "physical_weak_angle_closure": False,
        "strict_full_no_knob_closure": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "closure_claimed": False,
        "next_primary": next_work["primary"]["label"],
        "next_parallel": next_work["parallel"]["label"],
    }

    note = f"""# MTT CONST EW 02 Weak Mixing B41 Gauge Action RG Matching v1

Status: `{STATUS}`

Label: `CONST-EW-02 / WEAK-MIXING / B41-GAUGE-ACTION-RG-MATCHING`

## Result

```text
C1 local source-kernel remains retired       True
gauge/action anchor reduced                  True
one-universal-primitive bridge ready         True
RG/matching scaffold declared                True
Theta V numeric replay promoted as source    False
physical weak-angle numerical closure        False
```

B41 stops the physical branch from looping back into C1.  In the current
local-principle tier, the remaining weak-mixing problem is exactly the physical
action-unit plus RG/matching problem.

## Superset Use

- Straight MTT/source path: physical gauge/action normalization must be emitted
  as `K_phys`, `f_ab`, `alpha_phys`, or an equivalent action-unit anchor.
- Theta path: Papers I/III/V provide overlap, twistor-action, and one-loop
  weak-angle replay structure, but their reported numeric weak-angle values are
  not promoted as selected source closure.
- External QFT/PDG path: precision literature is used only to constrain the
  required scheme, scale, loop order, and threshold policy.

## Next

`CONST-EW-02 / WEAK-MIXING / B42-PHYSICAL-NORMALIZATION-OR-RG-ENGINE-EXECUTION`
"""

    for path, payload in [
        (GAUGE_ANCHOR, gauge_anchor),
        (RG_MATCHING, rg_matching),
        (THETA_CLASS, theta_class),
        (BOUNDARY, boundary),
        (NEXT_WORK, next_work),
        (OUTPUT, candidate),
        (CERT, cert),
    ]:
        write_json(path, payload)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUTPUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
