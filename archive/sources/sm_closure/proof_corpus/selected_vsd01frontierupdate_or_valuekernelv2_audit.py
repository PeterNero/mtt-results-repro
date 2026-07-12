"""Audit VSD-01 frontier update / value-source kernel v2."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_vsd01frontierupdate_or_valuekernelv2"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
VSD01_UPDATE = PACKET_DIR / "vsd01_updated_obligation_status.packet.json"
KERNEL_DELTA = PACKET_DIR / "value_source_kernel_delta_v2.packet.json"
NO_WHEELTRACK = PACKET_DIR / "no_old_wheeltrack_frontier_guard.packet.json"
CUTSET = PACKET_DIR / "next_atomic_value_source_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_VSD01FrontierUpdate_or_ValueKernelV2_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_VSD01FRONTIERUPDATE_OR_VALUEKERNELV2_BUILT_VSD01_PROGRESS_RECONCILED_TRUE_EQUIVALENCE_OPEN"
NEXT = "MTT_Selected_VSD02ThresholdResponseRule_or_ExternalLikelihoodImport_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    update = load(VSD01_UPDATE)
    delta = load(KERNEL_DELTA)
    guard = load(NO_WHEELTRACK)
    cutset = load(CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["closure_claimed"] is False, "candidate overclaimed closure")
    require(data["unpatched_theorem_closure_claimed"] is False, "unpatched closure overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(update["row_id"] == "VSD-01-selected-overlap-value-kernel", "wrong row")
    require(update["old_kernel_status"]["closed"] is False, "old kernel unexpectedly closed")
    closed = update["newly_closed_subgates"]
    for key in [
        "physical_source_assembly_subgate",
        "selected_dynamic_tensor_first_response_subgate",
        "same_branch_linking_to_versioned_packet",
        "versioned_common_scale_profile_input_values",
        "diagonal_profile_execution_layer",
    ]:
        require(closed[key] is True, f"new closed subgate missing: {key}")
    values = update["value_packet_summary"]
    require(values["accepted_as_versioned_common_scale_candidate_values"] is True, "versioned values missing")
    require(values["accepted_for_SM_parity"] is True, "SM parity value support missing")
    require(values["accepted_for_true_precision_equivalence"] is False, "true precision overaccepted")
    require(values["accepted_as_no_knob_MTT_prediction"] is False, "no-knob prediction overaccepted")
    still_open = update["still_open_for_full_VSD01_and_true_equivalence"]
    for key in [
        "accepted_threshold_matching_values",
        "accepted_mass_scheme_conversion_values",
        "multi_loop_threshold_convention_source_rows",
        "external_threshold_or_likelihood_source_import",
        "no_knob_Yukawa_Higgs_value_source_derivation",
        "true_SM_equivalence_closure",
    ]:
        require(still_open[key] is True, f"open item missing: {key}")
    require(update["VSD01_legacy_open_label_retired"] is True, "legacy VSD01 label not retired")
    require(update["VSD01_full_obligation_closed"] is False, "VSD01 full closure overclaimed")

    require(delta["old_closed_row_count"] == 0, "old closed count should remain historical")
    vsd_delta = delta["delta"]["VSD-01-selected-overlap-value-kernel"]
    require(vsd_delta["old_status"] == "open_static_only", "wrong old status")
    require(
        vsd_delta["new_status"]
        == "source_assembly_and_dynamic_first_response_closed_value_precision_open",
        "wrong new status",
    )
    require(delta["closure_claimed"] is False, "kernel delta overclaimed")

    require(guard["status"] == "OLD_VSD01_DYNAMIC_TENSOR_BLOCKER_RETIRED", "guard status mismatch")
    for item in [
        "re-proving source promotion for A_selected/b_selected/deltaTheta_C1",
        "re-proving physical Phi_fin C1 action-source certificate",
        "re-proving selected dynamic matter/overlap first-response packet",
        "treating first-pass common-scale values as true precision or no-knob closure",
    ]:
        require(item in guard["old_track_to_avoid"], f"missing old-track guard: {item}")
    require(guard["closure_claimed"] is False, "guard overclaimed")

    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require(cutset["closure_claimed"] is False, "cutset overclaimed")
    final = data["closure_decision"]
    require(final["VSD01_legacy_dynamic_absence_blocker_retired"] is True, "legacy blocker not retired")
    require(final["VSD01_full_obligation_closed"] is False, "VSD01 overclosed")
    require(final["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(final["full_no_knob_closed"] is False, "no-knob overclosed")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("we do not fall back into old work" in note, "note missing wheeltrack guard")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
