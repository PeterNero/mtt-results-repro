"""Audit VSD-01 dynamic operator back-import or Yukawa value frontier."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_vsd01_dynamicoperatorbackimport_or_yukawavaluefrontier"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
DYNAMIC_IMPORT = PACKET_DIR / "selected_dynamic_overlap_tensor_backimport.packet.json"
QASU3_REPLAY = PACKET_DIR / "qasu3_first_response_backimport.packet.json"
VSD01_DECISION = PACKET_DIR / "vsd01_dynamic_tensor_subgate_decision.packet.json"
CUTSET = PACKET_DIR / "next_cutset_after_vsd01_dynamic_backimport.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_VSD01_DynamicOperatorBackimport_or_YukawaValueFrontier_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_VSD01_DYNAMICOPERATORBACKIMPORT_OR_YUKAWAVALUEFRONTIER_"
    "BUILT_DYNAMIC_TENSOR_SUBGATE_CLOSED_VALUE_LAYER_OPEN"
)
NEXT = "MTT_Selected_YukawaMagnitudeRGClosure_or_FinalTrueSMEquivalenceAudit_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    dynamic_import = load(DYNAMIC_IMPORT)
    qasu3 = load(QASU3_REPLAY)
    decision = load(VSD01_DECISION)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["closure_claimed"] is False, "candidate full closure overclaimed")
    require(data["unpatched_theorem_closure_claimed"] is True, "dynamic theorem should be imported")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(dynamic_import["target_obligation"] == "VSD-01-selected-overlap-value-kernel", "wrong target")
    require(dynamic_import["selected_dynamic_overlap_tensor_promoted"] is True, "dynamic tensor not promoted")
    require(dynamic_import["dynamic_matter_overlap_operator_packet_closed"] is True, "matter overlap not closed")
    require(dynamic_import["same_source_validator_passes"] is True, "same-source validator failed")
    require(dynamic_import["selected_by_MTT"] is True, "dynamic values not selected")
    require(dynamic_import["sector_response_coverage"]["sector_first_response_keys"] == ["d", "e", "nuD", "u"], "sector coverage mismatch")
    require(dynamic_import["sector_response_coverage"]["matter_sector_matrix_layer_closed"] is True, "matter matrix layer not closed")
    require(dynamic_import["sector_response_coverage"]["accepted_running_yukawa_values_closed"] is False, "Yukawa values overclosed")
    require(dynamic_import["qualitative_tests"]["current_layer_flavor_tests_pass_conditionally"] is True, "qualitative tests missing")
    require(dynamic_import["observed_data_used_as_selector"] is False, "dynamic import observed selector")
    require(dynamic_import["closure_claimed"] is True, "dynamic import should close subgate")

    require(qasu3["dynamic_QaSU3_first_response_layer_closed"] is True, "Qa/SU3 first response not closed")
    require(qasu3["actual_QaSU3_operator_packet_first_response_layer_closed"] is True, "actual packet not closed")
    require(qasu3["selected_dynamic_overlap_tensor_promoted"] is True, "Qa/SU3 tensor not promoted")
    require(qasu3["dynamic_matter_overlap_packet_closed"] is True, "Qa/SU3 matter packet not closed")
    require(qasu3["not_a_precision_value_packet"] is True, "precision guard missing")
    for key in [
        "mass_split_positive",
        "ckm_commutator_positive",
        "pmns_commutator_positive",
        "cp_odd_invariant_nonzero",
    ]:
        require(qasu3["qualitative_flavor_response"][key] is True, f"qualitative response missing: {key}")
    require(qasu3["closure_claimed"] is True, "Qa/SU3 subgate should close")

    closed = decision["closed_for_VSD01_now"]
    for key in [
        "selected_dynamic_overlap_threshold_tensor_T_selected_first_response_layer",
        "dynamic_matter_overlap_operator_packet",
        "dynamic_QaSU3_first_response_operator_layer",
        "sector_matrix_rows_for_matter_families_first_response_layer",
        "same_branch_linking_tensor_rows_to_versioned_value_packet",
        "no_observed_data_selector_guard",
    ]:
        require(closed[key] is True, f"VSD-01 dynamic close flag missing: {key}")
    open_items = decision["still_open_for_true_SM_value_equivalence"]
    for key in [
        "accepted_Y_u_MZ_Y_d_MZ_Y_e_MZ_values",
        "accepted_lambda_H_MZ_value",
        "threshold_matching_values",
        "mass_scheme_conversion",
        "covariance_profile_likelihood_execution",
        "published_or_reconstructed_profile_likelihood",
        "CKM_PMNS_measured_angles_phase",
        "running_mass_ratios",
        "true_SM_equivalence",
        "full_SM_no_knob",
    ]:
        require(open_items[key] is True, f"value frontier missing: {key}")
    require(decision["VSD01_dynamic_tensor_subgate_closed"] is True, "dynamic subgate not closed")
    require(decision["VSD01_full_value_obligation_closed"] is False, "full value obligation overclosed")
    require(decision["closure_claimed"] is False, "decision overclaimed")

    final = data["closure_decision"]
    require(final["VSD01_source_assembly_subgate_closed"] is True, "source assembly regressed")
    require(final["VSD01_dynamic_tensor_subgate_closed"] is True, "dynamic subgate not closed in candidate")
    require(final["VSD01_full_value_obligation_closed"] is False, "VSD-01 full value overclosed")
    require(final["accepted_Yukawa_Higgs_RG_value_layer_closed"] is False, "accepted value layer overclosed")
    require(final["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(final["full_no_knob_closed"] is False, "no-knob overclosed")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("prevents wheel-spinning" in note, "note missing wheel-spinning guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
