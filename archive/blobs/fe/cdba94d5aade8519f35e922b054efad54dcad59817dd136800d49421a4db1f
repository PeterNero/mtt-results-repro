"""Audit latest AH8/PiCKM frontier synthesis and next strict targets."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_latestah8pickmfrontier_or_nextstrictclosuretargets"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"
CANDIDATE = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
SYNTHESIS = PACKET_DIR / "latest_ah8_pickm_frontier_synthesis.packet.json"
TARGETS = PACKET_DIR / "next_strict_closure_targets.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_LatestAH8PiCKMFrontier_or_NextStrictClosureTargets_v1.md"

STATUS = (
    "MTT_SELECTED_LATESTAH8PICKMFRONTIER_OR_NEXTSTRICTCLOSURETARGETS_"
    "BUILT_FRONTIER_SYNTHESIS"
)
NEXT = "MTT_Selected_LiteralGoodCoverHYMGlobalWitness_or_PrecisionValueSourceAfterAH8_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(CANDIDATE)
    synthesis = load(SYNTHESIS)
    targets = load(TARGETS)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status")
    require(cert["status"] == STATUS, "cert status")
    require(data["closure_claimed"] is True, "candidate closes synthesis packet")
    require(data["observed_data_used_as_selector"] is False, "candidate observed selector")
    require(data["target_fitting_used"] is False, "candidate target fitting")
    require(data["next_required_artifact"] == NEXT, "candidate next")
    require(cert["next_required_artifact"] == NEXT, "cert next")

    require(synthesis["status"] == "LATEST_FRONTIER_SYNTHESIZED", "synthesis status")
    require(synthesis["observed_data_used_as_selector"] is False, "synthesis observed")
    require(synthesis["target_fitting_used"] is False, "synthesis target fit")
    ah8 = synthesis["AH8_BN27_matrix_frontier"]
    require(ah8["strict_lane"] == "4/8", "strict lane")
    require(ah8["one_premise_BN27_lane"] == "6/8", "one premise lane")
    require(ah8["two_premise_AH_equivalent_lane"] == "8/8", "two premise lane")
    require(ah8["two_premise_AH_equivalent_lane_closed"] is True, "AH8 closed")
    require(ah8["literal_global_Cech_HYM_lane_closed"] is False, "literal not closed")

    sg = synthesis["strict_global_frontier"]
    require(sg["AH8_consumed_and_locked"] is True, "AH8 lock")
    require(sg["strict_global_closed"] is False, "strict global")
    require(sg["literal_good_cover_Cech_witness_family_closed"] is False, "Cech witness")
    require(sg["literal_global_HYM_witness_family_closed"] is False, "HYM witness")
    require(sg["precision_value_source_rows_closed"] is False, "precision")

    ckm = synthesis["CKM_frontier"]
    require(ckm["selected_Pi_CKM_weight_rows"] == 3, "Pi rows")
    require(ckm["selected_Pi_CKM_row_certificates"] == 3, "Pi certs")
    require(ckm["ckm_diagonal_profile_admission_closed"] is True, "CKM diag")
    require(ckm["accepted_ckm_diagonal_profile_admission_rows"] == 3, "CKM diag rows")
    require(ckm["chi2_ckm_diagonal"] < 1e-6, "CKM chi2")
    require(ckm["exact_central_CKM_closed"] is False, "exact CKM")
    require(ckm["full_covariance_profile_closed"] is False, "covariance")

    flavor = synthesis["flavor_magnitude_frontier"]
    require(flavor["minimal_nine_slot_policy_adopted"] is True, "policy")
    require(flavor["policy_source_value_row_count"] == 9, "policy rows")
    require(flavor["strict_no_knob_flavor_closure"] is False, "strict flavor")
    require(flavor["accepted_selected_no_knob_coefficient_source_row_count"] == 0, "strict coeff")

    pmns = synthesis["PMNS_and_precision_frontier"]
    require(pmns["PMNS_minimal_oscillation_policy_closed"] is True, "PMNS policy")
    require(pmns["PMNS_replay_ready"] is True, "PMNS replay")
    require(pmns["PMNS_source_rows_closed"] is False, "PMNS source")
    require(pmns["absolute_neutrino_mass_closed"] is False, "neutrino mass")

    higgs = synthesis["Higgs_and_PEW_frontier"]
    require(higgs["finite_H_scalar_source_closed"] is True, "H scalar")
    require(higgs["H_radial_zero_parameter_replacement_closed"] is True, "H zero")
    require(higgs["accepted_H_scalar_source_rows"] == 1, "H rows")
    require(higgs["H_specific_parameter_count"] == 0, "H parameters")
    require(higgs["one_shared_primitive_tier_closed"] is True, "one primitive")
    require(higgs["shared_physical_primitive_count"] == 1, "primitive count")
    require(higgs["accepted_strict_P_EW_source_rows"] == 0, "PEW rows")
    require(higgs["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "direct K rows")
    require(higgs["strict_no_knob_closure"] is False, "strict no knob")

    require(targets["status"] == "NEXT_TARGETS_LOCKED", "target status")
    require(targets["primary_next_required_artifact"] == NEXT, "target next")
    require(len(targets["do_not_reopen"]) == 5, "do not reopen")
    require(len(targets["strict_global_targets"]) == 2, "strict targets")
    require(len(targets["true_equivalence_targets"]) == 5, "equivalence targets")

    require(data["theorem"]["proved"] is True, "theorem proved")
    require(len(data["closed_now"]) == 3, "closed now")
    require(len(data["not_closed"]) == 4, "not closed")
    key = data["key_numbers"]
    require(key["two_premise_AH_equivalent_connection_rows"] == 8, "key AH8")
    require(key["strict_connection_rows"] == 4, "key strict rows")
    require(key["Pi_CKM_selected_weight_rows"] == 3, "key Pi")
    require(key["CKM_diagonal_profile_rows"] == 3, "key CKM")
    require(key["flavor_policy_rows"] == 9, "key flavor")
    require(key["strict_flavor_coefficient_rows"] == 0, "key strict flavor")
    require(key["accepted_H_scalar_source_rows"] == 1, "key H")
    require(key["accepted_strict_P_EW_source_rows"] == 0, "key PEW")
    require(key["accepted_direct_K_threshold_Omega_H_lambda_rows"] == 0, "key K")
    require(key["shared_physical_primitive_count"] == 1, "key primitive")

    decision = data["closure_decision"]
    require(decision["frontier_synthesis_ready"] is True, "decision ready")
    require(decision["two_premise_AH_equivalent_lane_closed"] is True, "decision AH8")
    require(decision["Pi_CKM_weight_rows_closed"] is True, "decision Pi")
    require(decision["CKM_diagonal_profile_admission_closed"] is True, "decision CKM")
    require(decision["one_shared_primitive_tier_closed"] is True, "decision primitive")
    require(decision["strict_global_closed"] is False, "decision strict global")
    require(decision["strict_no_knob_closure"] is False, "decision strict")
    require(decision["true_SM_equivalence_closed"] is False, "decision true SM")

    for phrase in [
        "AH-equivalent BN27 projected Route-C lane: `8/8`",
        "Selected `Pi_CKM` weight rows: `3/3`",
        "Strict `P_EW` rows: `0`",
        "Next Strict Targets",
        NEXT,
    ]:
        require(phrase in note, f"note missing {phrase}")

    print(f"PASS {CANDIDATE.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
