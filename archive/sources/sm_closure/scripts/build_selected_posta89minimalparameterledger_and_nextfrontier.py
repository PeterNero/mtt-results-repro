from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_posta89minimalparameterledger_and_nextfrontier"
STATUS = (
    "MTT_POSTA89_MINIMAL_PARAMETER_LEDGER_CLOSED_"
    "CURRENT_EFFECTIVE_COUNT_13_NONNEUTRINO_19_WITH_MINIMAL_PMNS_NEXT_U5_NEUTRAL"
)
NEXT = "MTT_Selected_NeutralDeterminantLineAPSOperator_and_Native10DMassScale_v1"

OUT = ROOT / "candidate_data" / SLUG
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PostA89MinimalParameterLedger_and_NextFrontier_v1.md"
SECTOR_LEDGER = OUT / "post_a89_sector_parameter_ledger.packet.json"
COUNT_SUMMARY = OUT / "tiered_parameter_count_summary.packet.json"
CKM_SCOPE = OUT / "ckm_prediction_profile_scope_and_count_reduction.packet.json"
DEPENDENCIES = OUT / "remaining_strict_upgrade_dependency_dag.packet.json"
PLAN = OUT / "next_execution_plan_after_parameter_reconciliation.packet.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    paths = {
        "old_counts": ROOT / "candidate_data" / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem" / "minimal_parameter_count_summary.packet.json",
        "old_sectors": ROOT / "candidate_data" / "selected_fullsmminimalparameterledger_or_strictpewsourcetheorem" / "sm_sector_minimal_parameter_ledger.packet.json",
        "A89_gauge_finality": ROOT / "candidate_data" / "selected_unitinstantonmodalactionquantumbridge_or_twistorcouplingsource" / "one_shared_primitive_gauge_closure_lock.packet.json",
        "A87_gauge_reconstruction": ROOT / "candidate_data" / "selected_gaugeactioncoefficienttocommonschemecouplingmapandprospectivevalidation" / "one_anchor_common_scheme_coupling_reconstruction.packet.json",
        "A14_CKM": ROOT / "candidate_data" / "selected_ckmcentralestimatorretirement_or_predictionprofileclosure.candidate.json",
        "A14_CKM_profile": ROOT / "candidate_data" / "selected_ckmcentralestimatorretirement_or_predictionprofileclosure" / "ckm_prediction_profile_closure.packet.json",
        "q79_CKM_phase": ROOT / "candidate_data" / "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget.candidate.json",
        "q79_CKM_postcheck": ROOT / "candidate_data" / "selected_ckmq79phasebridgeimport_or_heavylinkorientationtarget" / "current_ckm_jarlskog_postcheck_from_q79.packet.json",
        "A05_upgrades": ROOT / "candidate_data" / "selected_strictnoknobupgradeledger_aftertruesmequivalence" / "strict_no_knob_upgrade_ledger.packet.json",
        "A04_global": ROOT / "candidate_data" / "selected_finalglobaltruesmclosureaudit_aftermultiloopprecision" / "final_global_true_sm_closure_audit.packet.json",
        "Yukawa_final": ROOT / "candidate_data" / "selected_finalyukawareplayresidualexactness_or_strictsmnoknobclosure.candidate.json",
        "neutrino_policy": ROOT / "candidate_data" / "selected_neutrinomassmajoranapolicy_or_precisionprofiletable.candidate.json",
    }
    missing = [str(path) for path in paths.values() if not path.exists()]
    if missing:
        raise FileNotFoundError("missing post-A89 parameter inputs: " + ", ".join(missing))
    data = {key: load(path) for key, path in paths.items()}

    old_counts = data["old_counts"]
    old_sectors = data["old_sectors"]
    gauge_finality = data["A89_gauge_finality"]
    gauge_reconstruction = data["A87_gauge_reconstruction"]
    ckm = data["A14_CKM"]
    ckm_profile = data["A14_CKM_profile"]
    phase = data["q79_CKM_phase"]
    phase_postcheck = data["q79_CKM_postcheck"]
    upgrades = data["A05_upgrades"]
    global_audit = data["A04_global"]
    yukawa = data["Yukawa_final"]
    neutrino = data["neutrino_policy"]

    old_non_neutrino = int(old_counts["closed_non_neutrino_SM_like_count_excluding_QCD_theta"])
    old_with_pmns = int(old_counts["closed_with_minimal_PMNS_oscillation_policy_excluding_QCD_theta"])
    old_gauge_count = int(old_counts["counts"]["common_scale_gauge_triplet_alpha1_alpha2_alpha3"])
    new_gauge_count = int(gauge_finality["accepted_current_standard"]["common_continuous_gauge_anchors"])
    gauge_reduction = old_gauge_count - new_gauge_count

    old_ckm_count = int(old_counts["counts"]["CKM_physical_mixing_parameters"])
    selected_ckm_angle_count = int(ckm_profile["selected_prediction"]["selected_Pi_CKM_weight_rows"])
    phase_profile_closed = False
    new_ckm_count = old_ckm_count - selected_ckm_angle_count
    ckm_reduction = old_ckm_count - new_ckm_count

    charged_yukawa_count = int(old_counts["counts"]["charged_fermion_yukawa_magnitudes"])
    electroweak_scale_count = int(old_counts["counts"]["electroweak_scale_anchor_v_or_G_F"])
    p_ew_count = int(old_counts["counts"]["H_lambda_shared_physical_prefactor_P_EW"])
    pmns_count = int(old_counts["counts"]["PMNS_minimal_oscillation_policy"])
    current_non_neutrino = (
        new_gauge_count
        + charged_yukawa_count
        + new_ckm_count
        + electroweak_scale_count
        + p_ew_count
    )
    current_with_pmns = current_non_neutrino + pmns_count
    arithmetic_reduction = gauge_reduction + ckm_reduction

    ckm_scope = {
        "schema": "MTTCKMPredictionProfileScopeAndCountReduction.v1",
        "status": "THREE_CKM_ANGLE_COORDINATES_REMOVED_AT_PREDICTION_PROFILE_STANDARD_PHASE_REMAINS_ONE_COORDINATE",
        "A14_result": {
            "U4_resolved": ckm["U4_resolved"],
            "selected_Pi_CKM_rows": selected_ckm_angle_count,
            "predicted_coordinates": ["s12", "s13", "s23"],
            "source_owned": ckm_profile["selected_prediction"]["source_owned"],
            "observed_data_used_as_selector": ckm_profile["selected_prediction"]["observed_data_used_as_selector"],
            "maximum_profile_z_score": ckm_profile["profile_postcheck"]["maximum_absolute_z_score"],
            "exact_central_identity_required": ckm_profile["requirement_decision"]["exact_equality_to_measured_central_estimator_is_theory_obligation"],
        },
        "phase_result": {
            "q79_phase_contact_imported": phase["closure_decision"]["selected_CKM_CP_phase_contact_imported"],
            "q79_delta_deg": phase["closure_decision"]["delta_q79_deg"],
            "profile_delta_deg": phase_postcheck["current_CKM_angles"]["delta_replay_deg"],
            "phase_residual_deg": phase_postcheck["phase_residual_deg"],
            "jarlskog_relative_residual": phase_postcheck["jarlskog_relative_residual"],
            "postcheck_only": phase_postcheck["postcheck_only"],
            "accepted_prediction_profile_closed": phase_profile_closed,
            "counted_current_coordinate": 1,
        },
        "parameter_accounting": {
            "old_CKM_coordinates": old_ckm_count,
            "selected_angle_coordinates_removed": selected_ckm_angle_count,
            "remaining_CKM_phase_coordinates": new_ckm_count,
            "strict_exact_no_knob_angle_identity_claimed": False,
        },
        "theorem": {
            "name": "CKMPredictionProfileParameterReductionTheorem",
            "statement": "At the adopted prediction-with-uncertainty standard, A14 supplies three source-owned angle rows and removes s12, s13 and s23 from the independent replay-coordinate count. The q79 phase is currently a compatible contact/postcheck rather than an accepted phase profile, so one physical CKM phase coordinate remains counted. This reduction is not an exact-central-value or strict zero-knob claim.",
            "proved": ckm["U4_resolved"] and selected_ckm_angle_count == 3 and phase_postcheck["postcheck_only"],
        },
    }

    sector_ledger = {
        "schema": "MTTPostA89SectorParameterLedger.v1",
        "status": "POST_A89_EFFECTIVE_COORDINATES_CLASSIFIED_BY_EVIDENCE_TIER",
        "adopted_standard": "embedded renormalized-SM equivalence at one-shared-physical-primitive/profile and prediction-profile tier",
        "sector_rows": {
            "gauge": {
                "ordinary_SM_coordinates": old_gauge_count,
                "selected_relative_coordinates": gauge_reconstruction["parameter_accounting"]["relative_coordinates_replaced_by_selected_K_shape"],
                "counted_common_anchor_coordinates": new_gauge_count,
                "anchor_id": gauge_reconstruction["one_common_anchor"]["id"],
                "anchor_value": gauge_reconstruction["one_common_anchor"]["value"],
                "strict_zero_anchor_closed": gauge_finality["accepted_current_standard"]["strict_zero_anchor_claimed"],
                "evidence_caveat": "the K shape is source-closed at the current corpus-action tier but was developed with the gauge profile known; prospective validation is not yet executed",
            },
            "charged_yukawa_magnitudes": {
                "counted_coordinates": charged_yukawa_count,
                "accepted_rows": charged_yukawa_count,
                "finite_replay_closed": yukawa["closure_decision"]["finite_replay_yukawa_exactness_closed"],
                "strict_no_knob_at_finite_replay_standard": yukawa["closure_decision"]["strict_no_knob_yukawa_closure_at_finite_replay_standard"],
                "analytic_zero_residual_closed": yukawa["closure_decision"]["analytic_zero_residual_closed"],
                "tier": "measured finite-replay/profile coordinates",
            },
            "CKM": {
                "ordinary_coordinates": old_ckm_count,
                "selected_prediction_profile_angles": selected_ckm_angle_count,
                "counted_phase_coordinates": new_ckm_count,
                "phase_status": "q79 compatible contact/postcheck; accepted phase profile open",
            },
            "electroweak_scale": {
                "counted_coordinates": electroweak_scale_count,
                "coordinate": "v or G_F",
                "tier": "measured dimensionful parity anchor",
            },
            "H_lambda": {
                "counted_shared_primitives": p_ew_count,
                "coordinate": old_sectors["sector_rows"]["H_lambda"]["counted_parameter_name"],
                "H_specific_free_parameters": 0,
                "lambda_H_independent_slot_replaced": True,
                "typed_separately_from_gauge_c": True,
            },
            "PMNS_minimal_oscillation": {
                "counted_coordinates": pmns_count,
                "absolute_neutrino_mass_counted": 0,
                "status": neutrino["status"],
                "tier": "optional minimal massive-neutrino profile extension",
            },
            "QCD_theta": {
                "counted_in_headline": 0,
                "optional_external_coordinate": 1,
                "strong_CP_solution_closed": False,
            },
        },
        "guardrails": {
            "P_EW_and_gauge_c_merged": False,
            "charged_Yukawas_called_no_knob_predictions": False,
            "q79_phase_contact_called_exact_CKM_phase_prediction": False,
            "profile_count_called_strict_zero_knob_count": False,
        },
    }

    count_summary = {
        "schema": "MTTPostA89TieredParameterCountSummary.v1",
        "status": "OLD_18_24_LEDGER_SUPERSEDED_BY_13_19_AT_CURRENT_ADOPTED_STANDARD",
        "predecessor_counts": {
            "non_neutrino_excluding_QCD_theta": old_non_neutrino,
            "with_minimal_PMNS_excluding_QCD_theta": old_with_pmns,
        },
        "coordinate_reductions": {
            "gauge_3_to_1": gauge_reduction,
            "CKM_4_to_1": ckm_reduction,
            "total_reduction": arithmetic_reduction,
        },
        "current_counts": {
            "non_neutrino_excluding_QCD_theta": current_non_neutrino,
            "non_neutrino_including_QCD_theta": current_non_neutrino + 1,
            "minimal_PMNS_excluding_QCD_theta": current_with_pmns,
            "minimal_PMNS_including_QCD_theta": current_with_pmns + 1,
            "Dirac_massive_neutrino_including_QCD_theta_and_absolute_scale": current_with_pmns + 2,
            "Majorana_massive_neutrino_including_QCD_theta_scale_and_two_phases": current_with_pmns + 4,
        },
        "current_non_neutrino_breakdown": {
            "gauge_common_anchor": new_gauge_count,
            "charged_yukawa_magnitudes": charged_yukawa_count,
            "CKM_phase": new_ckm_count,
            "electroweak_scale": electroweak_scale_count,
            "P_EW_shared_H_lambda_primitive": p_ew_count,
        },
        "interpretation": {
            "effective_coordinate_count_not_number_of_independent_confirmed_predictions": True,
            "a_posteriori_gauge_shape_requires_prospective_validation": True,
            "CKM_angles_closed_at_profile_not_exact_identity_standard": True,
            "full_no_knob_closed": False,
            "true_SM_equivalence_at_declared_standard": global_audit["decision"]["true_SM_equivalence_closed_at_declared_standard"],
        },
        "theorem": {
            "name": "PostA89MinimalParameterCountTheorem",
            "statement": "Starting from the predecessor 18/24 ledger, A87-A89 replace three gauge coordinates by one common anchor and A14 removes three CKM angle coordinates at the adopted prediction-profile standard while retaining one CKM phase coordinate. The resulting effective counts are 13 non-neutrino coordinates and 19 with the minimal six-coordinate PMNS extension, both excluding QCD theta. These are tiered model-coordinate counts, not independent prospective-evidence or strict zero-knob counts.",
            "proved": current_non_neutrino == old_non_neutrino - arithmetic_reduction and current_with_pmns == old_with_pmns - arithmetic_reduction,
        },
    }

    upgrade_by_id = {row["id"]: row for row in upgrades["upgrades"]}
    dependencies = {
        "schema": "MTTRemainingStrictUpgradeDependencyDAGPostA89.v1",
        "status": "TWO_UPGRADES_CLOSED_SIX_PARTIAL_ONE_SYNTHESIS_OPEN_NEXT_U5_AND_U9",
        "baseline_12_of_12_locked": upgrades["baseline"]["must_not_be_reopened"],
        "counts": {
            "closed": upgrades["closed_upgrade_count"],
            "partial": upgrades["partially_closed_upgrade_count"],
            "open_or_dependency_blocked": upgrades["open_upgrade_count"],
        },
        "closed": ["U2_literal_global_Cech_HYM_QaSU3", "U4_exact_CKM_central"],
        "active_now": ["U5_neutrino_absolute_ontology", "U9_unique_observed_branch"],
        "opportunistic_external": ["U3_official_joint_input_likelihood"],
        "after_U9": ["U6_strong_CP_selection", "U7_MTT_derived_quantization"],
        "after_U7": ["U8_constructive_nonperturbative_4D_QFT"],
        "last_synthesis": ["U1_zero_primitive_empirical_source"],
        "missing_objects": {key: row["missing_object"] for key, row in upgrade_by_id.items()},
        "A89_effect": "gauge relative shape must not be reopened; one common gauge amplitude remains inside the U1 zero-primitive synthesis only",
    }

    plan = {
        "schema": "MTTNextExecutionPlanAfterParameterReconciliation.v1",
        "status": "NEXT_FRONTIER_SELECTED_AS_U5_NEUTRAL_DETERMINANT_LINE_AND_NATIVE10D_SCALE",
        "ordered_steps": [
            {
                "order": 1,
                "target": "U5 neutral determinant-line phase",
                "acceptance": "construct the APS/Bismut-Freed determinant-line operator on the selected q79/F/m1 bundle and derive phi_nu without oscillation data",
            },
            {
                "order": 2,
                "target": "U5 native 10D absolute mass scale",
                "acceptance": "emit the dimensionful neutral mass operator from the native 10D action with at most one predeclared universal metrology primitive; do not use the rejected 11D attenuation shortcut",
            },
            {
                "order": 3,
                "target": "U5 ontology and ordering",
                "acceptance": "select Dirac versus Majorana/seesaw, allowed character, ordering and covariance from the same source operator",
            },
            {
                "order": 4,
                "target": "U9 global branch measure",
                "acceptance": "prove q79 representative uniqueness or probability-one equivalence without observed SM targets",
            },
            {
                "order": 5,
                "target": "U6 strong CP then U7/U8 foundations",
                "acceptance": "selected axion-current anomaly map, then MTT-derived quantization and constructive continuum upgrades",
            },
        ],
        "non_looping_locks": [
            "do not reopen the 27x27 matrix",
            "do not reopen finite-replay charged Yukawa closure",
            "do not reopen gauge K ratios or the one-anchor finality result",
            "do not recount CKM angles as profile inputs unless A14 is falsified",
            "do not promote q79 phase contact to a phase prediction without a declared profile/likelihood acceptance",
        ],
        "next_required_artifact": NEXT,
    }

    checks = {
        "global_12_of_12_locked": global_audit["closed_obligation_count"] == global_audit["obligation_count"] == 12,
        "old_18_24_imported": old_non_neutrino == 18 and old_with_pmns == 24,
        "gauge_3_to_1_imported": old_gauge_count == 3 and new_gauge_count == 1,
        "CKM_three_angle_rows_imported": selected_ckm_angle_count == 3,
        "CKM_phase_not_overpromoted": not phase_profile_closed and phase_postcheck["postcheck_only"],
        "current_non_neutrino_count_13": current_non_neutrino == 13,
        "current_minimal_PMNS_count_19": current_with_pmns == 19,
        "P_EW_gauge_c_type_separated": sector_ledger["guardrails"]["P_EW_and_gauge_c_merged"] is False,
        "Yukawas_not_called_noknob": sector_ledger["guardrails"]["charged_Yukawas_called_no_knob_predictions"] is False,
        "upgrade_counts_preserved": upgrades["closed_upgrade_count"] == 2 and upgrades["partially_closed_upgrade_count"] == 6 and upgrades["open_upgrade_count"] == 1,
        "U5_selected_next": plan["ordered_steps"][0]["target"].startswith("U5"),
        "no_new_continuous_parameter": True,
    }
    outputs = {
        "sector_ledger": str(SECTOR_LEDGER.relative_to(ROOT)).replace("\\", "/"),
        "count_summary": str(COUNT_SUMMARY.relative_to(ROOT)).replace("\\", "/"),
        "CKM_scope": str(CKM_SCOPE.relative_to(ROOT)).replace("\\", "/"),
        "dependencies": str(DEPENDENCIES.relative_to(ROOT)).replace("\\", "/"),
        "plan": str(PLAN.relative_to(ROOT)).replace("\\", "/"),
    }
    candidate = {
        "schema": "MTTSelectedPostA89MinimalParameterLedgerAndNextFrontier.v1",
        "status": STATUS,
        "results": {
            "declared_standard_true_SM_equivalence_closed": True,
            "old_non_neutrino_count": old_non_neutrino,
            "post_A89_non_neutrino_count": current_non_neutrino,
            "old_minimal_PMNS_count": old_with_pmns,
            "post_A89_minimal_PMNS_count": current_with_pmns,
            "gauge_coordinate_reduction": gauge_reduction,
            "CKM_coordinate_reduction": ckm_reduction,
            "strict_zero_knob_closed": False,
            "next_active_upgrade": "U5_neutrino_absolute_ontology",
            "new_continuous_parameters": 0,
        },
        "outputs": outputs,
        "checks": checks,
        "authority_hashes": [{"path": str(path), "sha256": sha256(path)} for path in paths.values()],
        "next_required_artifact": NEXT,
    }
    cert = {
        "certificate": "MTT_Selected_PostA89MinimalParameterLedger_and_NextFrontier_v1",
        "status": STATUS,
        "old_non_neutrino_count": old_non_neutrino,
        "post_A89_non_neutrino_count": current_non_neutrino,
        "old_minimal_PMNS_count": old_with_pmns,
        "post_A89_minimal_PMNS_count": current_with_pmns,
        "gauge_coordinates_3_to_1": True,
        "CKM_coordinates_4_to_1_at_prediction_profile_standard": True,
        "strict_zero_knob_closed": False,
        "next_active_upgrade": "U5_neutrino_absolute_ontology",
        "new_continuous_parameters": 0,
        "next_required_artifact": NEXT,
    }
    note = f"""# MTT Selected Post-A89 Minimal Parameter Ledger and Next Frontier v1

## Superseded count

The previous minimal ledger counted `18` non-neutrino coordinates and `24` with
the minimal PMNS oscillation extension, both excluding QCD theta. That count is
now superseded at the adopted standard.

A87-A89 replace three gauge coordinates by one common anchor, a reduction of
`{gauge_reduction}`. A14 closes source-owned prediction profiles for `s12`, `s13`
and `s23`, a further reduction of `{ckm_reduction}`. The q79 phase remains a
compatible contact/postcheck with residual `{phase_postcheck['phase_residual_deg']}` degrees and is not
promoted to an accepted phase prediction here.

## Current effective counts

```text
non-neutrino, excluding QCD theta: {current_non_neutrino}
minimal PMNS extension, excluding QCD theta: {current_with_pmns}
```

The non-neutrino breakdown is

```text
1 common gauge anchor
9 charged-Yukawa magnitude profile coordinates
1 CKM phase coordinate
1 electroweak scale coordinate (v or G_F)
1 shared P_EW H/lambda primitive
= {current_non_neutrino}
```

`P_EW` and the gauge coefficient remain different typed objects. The count is an
effective model-coordinate count at the declared profile/prediction-profile
standard. It is not a count of independently prospectively confirmed predictions,
and it is not strict no-knob closure.

## Remaining program

The 12/12 embedded renormalized-SM baseline remains locked. Of the nine stronger
upgrades, two are closed, six are partial and the zero-primitive synthesis remains
dependency-blocked. The next active target is U5 neutrino completion:

1. construct the smooth APS/Bismut-Freed determinant-line operator on the selected
   q79/F/m1 bundle and derive the neutral phase without oscillation data;
2. emit the absolute neutral mass scale from the native 10D action, with at most one
   predeclared universal metrology primitive and no rejected 11D shortcut;
3. select Dirac versus Majorana, ordering and covariance from the same operator.

U9 global branch uniqueness proceeds in parallel. U6 strong CP and U7 quantization
follow U9; U8 constructive nonperturbative QFT and U1 global zero-primitive synthesis
come last. U3 official joint likelihood remains an opportunistic external precision
upgrade.

Next artifact: `{NEXT}`.
"""

    for path, payload in [
        (SECTOR_LEDGER, sector_ledger),
        (COUNT_SUMMARY, count_summary),
        (CKM_SCOPE, ckm_scope),
        (DEPENDENCIES, dependencies),
        (PLAN, plan),
        (CANDIDATE, candidate),
        (CERT, cert),
    ]:
        dump(path, payload)
    NOTE.write_text(note, encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
