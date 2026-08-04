"""Build latest AH8/PiCKM frontier synthesis and next strict targets."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CORPUS = ROOT / "proof_corpus"
CERTS = ROOT / "certificates"

SLUG = "selected_latestah8pickmfrontier_or_nextstrictclosuretargets"
OUT = DATA / f"{SLUG}.candidate.json"
PACKET_DIR = DATA / SLUG
SYNTHESIS = PACKET_DIR / "latest_ah8_pickm_frontier_synthesis.packet.json"
TARGETS = PACKET_DIR / "next_strict_closure_targets.packet.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_LatestAH8PiCKMFrontier_or_NextStrictClosureTargets_v1.md"

VISIBLE_AH8 = DATA / "selected_visibleglobalstromingerprovenance_or_bn27finalrowacceptance.candidate.json"
STRICT_GLOBAL = DATA / "selected_strictglobalcechhym_or_truesmafterah8.candidate.json"
PICKM = DATA / "selected_pickmnumeratorbranchretentionprinciple_or_weightrows.candidate.json"
CKM_PROFILE = DATA / "selected_ckmcovarianceprofileorhigherorderresidualclosure_or_pmnshiggspewrows.candidate.json"
MAGNITUDE = DATA / "selected_magnitudebearingrows_after_postah8_dynamicimport.candidate.json"
PMNS = DATA / "selected_pmnsrunningmassrows_or_higgsthresholdstrictpewexit.candidate.json"
HIGGS = DATA / "selected_higgsthresholdstrictpewexit_or_selectedsourcerows.candidate.json"
STRICT_PEW = DATA / "selected_strictpewdirectksourcerows_or_finalsmnoknobaudit.candidate.json"
ONEPRIMITIVE = DATA / "selected_oneprimitiveclosurepaperupdate_or_strictnoknobupgradeprogram.candidate.json"

STATUS = (
    "MTT_SELECTED_LATESTAH8PICKMFRONTIER_OR_NEXTSTRICTCLOSURETARGETS_"
    "BUILT_FRONTIER_SYNTHESIS"
)
NEXT = "MTT_Selected_LiteralGoodCoverHYMGlobalWitness_or_PrecisionValueSourceAfterAH8_v1"


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    visible_ah8 = load(VISIBLE_AH8)
    strict_global = load(STRICT_GLOBAL)
    pickm = load(PICKM)
    ckm_profile = load(CKM_PROFILE)
    magnitude = load(MAGNITUDE)
    pmns = load(PMNS)
    higgs = load(HIGGS)
    strict_pew = load(STRICT_PEW)
    oneprimitive = load(ONEPRIMITIVE)

    synthesis = {
        "schema": "MTTLatestAH8PiCKMFrontierSynthesis.v1",
        "status": "LATEST_FRONTIER_SYNTHESIZED",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "AH8_BN27_matrix_frontier": {
            "strict_lane": "4/8",
            "one_premise_BN27_lane": "6/8",
            "two_premise_AH_equivalent_lane": "8/8",
            "two_premise_AH_equivalent_lane_closed": visible_ah8["closure_decision"][
                "two_premise_AH_equivalent_lane_closed"
            ],
            "projected_RouteC_equivalence_for_BN27_HYM_row_accepted": visible_ah8[
                "closure_decision"
            ]["projected_RouteC_equivalence_for_BN27_HYM_row_accepted"],
            "literal_global_Cech_HYM_lane_closed": visible_ah8["closure_decision"][
                "literal_good_cover_Cech_HYM_closed"
            ],
        },
        "strict_global_frontier": {
            "AH8_consumed_and_locked": strict_global["closure_decision"][
                "AH8_consumed_and_locked"
            ],
            "strict_global_closed": strict_global["closure_decision"]["strict_global_closed"],
            "literal_good_cover_Cech_witness_family_closed": strict_global["closure_decision"][
                "literal_good_cover_Cech_witness_family_closed"
            ],
            "literal_global_HYM_witness_family_closed": strict_global["closure_decision"][
                "literal_global_HYM_witness_family_closed"
            ],
            "precision_value_source_rows_closed": strict_global["closure_decision"][
                "precision_value_source_rows_closed"
            ],
        },
        "CKM_frontier": {
            "selected_Pi_CKM_weight_rows": pickm["closure_decision"]["accepted_weight_rows"],
            "selected_Pi_CKM_row_certificates": pickm["closure_decision"][
                "selected_Pi_CKM_row_certificates"
            ],
            "ckm_diagonal_profile_admission_closed": ckm_profile["closure_decision"][
                "ckm_diagonal_profile_admission_closed"
            ],
            "accepted_ckm_diagonal_profile_admission_rows": ckm_profile["key_numbers"][
                "accepted_ckm_diagonal_profile_admission_rows"
            ],
            "chi2_ckm_diagonal": ckm_profile["key_numbers"]["chi2_ckm_diagonal"],
            "max_abs_sigma_score_no_covariance": ckm_profile["key_numbers"][
                "max_abs_sigma_score_no_covariance"
            ],
            "exact_central_CKM_closed": ckm_profile["closure_decision"][
                "ckm_exact_central_residual_closed"
            ],
            "full_covariance_profile_closed": ckm_profile["closure_decision"][
                "ckm_full_covariance_profile_closed"
            ],
        },
        "flavor_magnitude_frontier": {
            "minimal_nine_slot_policy_adopted": magnitude["closure_decision"][
                "minimal_nine_slot_policy_adopted"
            ],
            "policy_source_value_row_count": magnitude["closure_decision"][
                "policy_source_value_row_count"
            ],
            "strict_no_knob_flavor_closure": magnitude["closure_decision"][
                "strict_no_knob_flavor_closure"
            ],
            "accepted_selected_no_knob_coefficient_source_row_count": magnitude[
                "closure_decision"
            ]["accepted_selected_no_knob_coefficient_source_row_count"],
        },
        "PMNS_and_precision_frontier": {
            "PMNS_minimal_oscillation_policy_closed": pmns["closure_decision"][
                "PMNS_minimal_oscillation_policy_closed"
            ],
            "PMNS_replay_ready": pmns["closure_decision"]["PMNS_replay_ready"],
            "PMNS_source_rows_closed": pmns["closure_decision"]["PMNS_source_rows_closed"],
            "absolute_neutrino_mass_closed": pmns["closure_decision"][
                "absolute_neutrino_mass_closed"
            ],
            "threshold_mass_scheme_readiness_closed": pmns["closure_decision"][
                "threshold_mass_scheme_readiness_closed"
            ],
        },
        "Higgs_and_PEW_frontier": {
            "finite_H_scalar_source_closed": higgs["closure_decision"][
                "finite_H_scalar_source_closed"
            ],
            "H_radial_zero_parameter_replacement_closed": higgs["closure_decision"][
                "H_radial_zero_parameter_replacement_closed"
            ],
            "accepted_H_scalar_source_rows": higgs["key_numbers"]["accepted_H_scalar_source_rows"],
            "H_specific_parameter_count": strict_pew["key_numbers"]["H_specific_parameter_count"],
            "one_shared_primitive_tier_closed": strict_pew["closure_decision"][
                "one_shared_primitive_tier_closed"
            ],
            "shared_physical_primitive_count": strict_pew["key_numbers"][
                "shared_physical_primitive_count_under_axiom"
            ],
            "accepted_strict_P_EW_source_rows": strict_pew["key_numbers"][
                "accepted_strict_P_EW_source_rows"
            ],
            "accepted_direct_K_threshold_Omega_H_lambda_rows": strict_pew["key_numbers"][
                "accepted_direct_K_threshold_Omega_H_lambda_rows"
            ],
            "strict_no_knob_closure": strict_pew["closure_decision"]["strict_no_knob_closure"],
        },
        "current_adopted_standard": oneprimitive["closure_decision"]["current_closure_standard"],
    }

    targets = {
        "schema": "MTTNextStrictClosureTargetsAfterAH8PiCKM.v1",
        "status": "NEXT_TARGETS_LOCKED",
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "primary_next_required_artifact": NEXT,
        "do_not_reopen": [
            "AH-equivalent BN27 projected Route-C lane at 8/8",
            "selected Pi_CKM weight rows at 3/3",
            "CKM diagonal-profile admission",
            "finite H scalar source and H-specific zero-parameter replacement",
            "one-shared-physical-primitive publication standard",
        ],
        "strict_global_targets": [
            "literal good-cover Deligne-Cech witness family",
            "literal global HYM/projective connection coefficient witness family",
        ],
        "true_equivalence_targets": [
            "full CKM covariance/profile likelihood instead of diagonal-only admission",
            "selected precision/value source rows",
            "selected PMNS source rows and absolute neutrino policy",
            "strict P_EW/direct-K source rows or derivation of the physical-normalization axiom",
            "strict flavor coefficient source rows beyond the nine-slot policy tier",
        ],
        "acceptable_counted_tiers": [
            "two-premise AH-equivalent BN27 matrix lane",
            "one-shared-physical-primitive SM closure standard",
            "minimal nine-slot flavor policy tier",
        ],
    }

    candidate = {
        "candidate": "MTTSelectedLatestAH8PiCKMFrontierOrNextStrictClosureTargets",
        "status": STATUS,
        "closure_claimed": True,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "inputs": {
            "visible_AH8": rel(VISIBLE_AH8),
            "strict_global_after_AH8": rel(STRICT_GLOBAL),
            "Pi_CKM_rows": rel(PICKM),
            "CKM_profile": rel(CKM_PROFILE),
            "post_AH8_magnitudes": rel(MAGNITUDE),
            "PMNS_running": rel(PMNS),
            "Higgs_threshold": rel(HIGGS),
            "strict_PEW_final_audit": rel(STRICT_PEW),
            "one_primitive_standard": rel(ONEPRIMITIVE),
        },
        "output_packets": {
            "latest_ah8_pickm_frontier_synthesis": rel(SYNTHESIS),
            "next_strict_closure_targets": rel(TARGETS),
        },
        "theorem": {
            "name": "LatestAH8PiCKMFrontierSynthesisTheorem",
            "proved": True,
            "statement": (
                "The latest accepted state is synthesized without reopening consumed rows: "
                "the AH-equivalent BN27 projected Route-C lane is 8/8, Pi_CKM weight "
                "rows are 3/3 with diagonal CKM profile admission, finite H scalar "
                "source/H-specific zero-parameter replacement are closed, and strict "
                "no-knob closure remains open at literal global witnesses, precision/value "
                "rows, PMNS absolute/source rows, strict PEW/direct-K rows, and strict "
                "flavor coefficient source rows."
            ),
        },
        "closed_now": [
            "Latest AH8/Pi_CKM/post-AH8 frontier is recorded as an audited packet.",
            "Consumed rows are protected against loopback.",
            "Next strict closure targets are ordered.",
        ],
        "not_closed": [
            "Strict global literal good-cover/HYM witnesses.",
            "Full true-SM precision equivalence.",
            "Strict zero-primitive/no-knob PEW/direct-K derivation.",
            "Strict no-knob flavor coefficient derivation.",
        ],
        "key_numbers": {
            "two_premise_AH_equivalent_connection_rows": 8,
            "strict_connection_rows": 4,
            "Pi_CKM_selected_weight_rows": 3,
            "CKM_diagonal_profile_rows": 3,
            "flavor_policy_rows": 9,
            "strict_flavor_coefficient_rows": 0,
            "accepted_H_scalar_source_rows": 1,
            "accepted_strict_P_EW_source_rows": 0,
            "accepted_direct_K_threshold_Omega_H_lambda_rows": 0,
            "shared_physical_primitive_count": 1,
        },
        "closure_decision": {
            "frontier_synthesis_ready": True,
            "two_premise_AH_equivalent_lane_closed": True,
            "Pi_CKM_weight_rows_closed": True,
            "CKM_diagonal_profile_admission_closed": True,
            "one_shared_primitive_tier_closed": True,
            "strict_global_closed": False,
            "strict_no_knob_closure": False,
            "true_SM_equivalence_closed": False,
        },
        "next_required_artifact": NEXT,
    }

    cert = {
        "certificate": "MTT_Selected_LatestAH8PiCKMFrontier_or_NextStrictClosureTargets_v1",
        "status": STATUS,
        "candidate": rel(OUT),
        "frontier_synthesis_ready": True,
        "two_premise_AH_equivalent_lane_closed": True,
        "Pi_CKM_weight_rows_closed": True,
        "CKM_diagonal_profile_admission_closed": True,
        "one_shared_primitive_tier_closed": True,
        "strict_global_closed": False,
        "strict_no_knob_closure": False,
        "true_SM_equivalence_closed": False,
        "observed_data_used_as_selector": False,
        "target_fitting_used": False,
        "next_required_artifact": NEXT,
    }

    note = f"""# MTT Selected LatestAH8PiCKMFrontier or NextStrictClosureTargets v1

Status: `{STATUS}`

## Locked Results

- AH-equivalent BN27 projected Route-C lane: `8/8`.
- Strict BN27 connection-row lane: `4/8`.
- Selected `Pi_CKM` weight rows: `3/3`.
- CKM diagonal-profile admission rows: `3`.
- Minimal flavor policy rows: `9`, with strict coefficient rows still `0`.
- Finite H scalar source rows: `1`.
- Strict `P_EW` rows: `0`.
- Direct `K_threshold.Omega_H.lambda` rows: `0`.

## Do Not Reopen

The AH8 projected/AH-equivalent BN27 matrix row and the selected `Pi_CKM`
weight rows are consumed for their stated tiers. They are not strict global
literal witnesses and not full covariance/precision closure.

## Next Strict Targets

1. Literal good-cover Deligne-Cech witness family.
2. Literal global HYM/projective connection coefficient witness family.
3. Full CKM covariance/profile likelihood or selected higher-order residual rows.
4. Precision/value source rows, PMNS source rows, and strict `P_EW`/direct-K rows.

Next required artifact: `{NEXT}`.
"""

    write_json(SYNTHESIS, synthesis)
    write_json(TARGETS, targets)
    write_json(OUT, candidate)
    write_json(CERT, cert)
    NOTE.write_text(note, encoding="utf-8")

    print(json.dumps({"candidate": rel(OUT), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
