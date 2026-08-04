"""Audit measured-SM replay admission for SM-equivalence."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "sm_equivalence_measured_replay_admission.candidate.json"
CERT = ROOT / "certificates" / "sm_equivalence_measured_replay_admission_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SM_Equivalence_Measured_Replay_Admission_v1.md"
BUILDER = ROOT / "scripts" / "build_sm_equivalence_measured_replay_admission.py"

STATUS = "MTT_SM_EQUIVALENCE_MEASURED_REPLAY_ADMISSION_BUILT_DYNAMIC_OVERLAP_AS_NO_KNOB_UPGRADE"
NEXT = "MTT_SM_Equivalence_Measured_Parameter_Replay_Manifest_v1"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "next artifact mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next artifact mismatch")
    require(NEXT in note, "note missing next artifact")

    policy = data["branch_policy_update"]
    require(policy["corrected_for_SM_equivalence"] is True, "SM-equivalence correction missing")
    require(policy["previous_controller_locked_G4_before_measured_replay"] is True, "prior G4 state not recorded")
    require("no-knob upgrade target" in policy["new_rule"], "new rule does not mention no-knob upgrade")

    source = data["static_source_boundary"]
    for key in [
        "sm_sector_packet_schema_declared",
        "measured_slot_boundary_declared",
        "measured_values_do_not_select_packet",
        "all_six_sm_slot_functor_arrows_emitted_static",
        "static_sector_route_Z_to_u_e_X_to_d_nuD",
        "finite_trace_transfer_normalization_static",
        "oneM_Dirac_neutrino_rule_static",
    ]:
        require(source[key] is True, f"static source boundary not closed: {key}")

    dynamic = data["dynamic_upgrade_boundary"]
    require(dynamic["dynamic_overlap_tensor_emitted"] is False, "dynamic overlap overclaimed")
    require(dynamic["selected_C1_primitive_emitted"] is False, "primitive C1 overclaimed")
    require(dynamic["A_selected_claimed"] is False, "A_selected overclaimed")
    require(dynamic["b_selected_claimed"] is False, "b_selected overclaimed")
    require(dynamic["parity_role"] == "NO_KNOB_UPGRADE_TARGET_NOT_PARITY_PREREQUISITE", "wrong dynamic role")

    slots = data["measured_replay_slots"]
    for key in ["gauge_couplings", "yukawa_matrices", "CKM_PMNS_CP", "Higgs_parameters"]:
        require(slots[key]["admitted_for_SM_equivalence"] is True, f"slot not admitted: {key}")
        require(slots[key]["blocked_as_source_selector"] is True, f"slot selector guard missing: {key}")
        require(slots[key]["required_conventions"], f"slot conventions missing: {key}")
        require(slots[key]["no_knob_upgrade"], f"slot no-knob target missing: {key}")

    manifest = data["replay_manifest_requirements"]
    require(manifest["measured_slot_table"] is True, "measured slot table missing")
    require(manifest["SM_reference_conventions"] is True, "SM conventions missing")
    forbidden = " ".join(manifest["forbidden_replay_behaviors"])
    require("source packet" in forbidden and "no-knob derivation" in forbidden, "forbidden replay guard missing")

    require(data["empirical_ledger_ready"] is True, "empirical ledger not ready")
    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["sm_equivalence_claimed"] is False, "SM equivalence overclaimed")
    require(data["no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used as selector")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    closes = data["what_closes_now"]
    require(closes["SM_equivalence_measured_replay_admission_policy"] is True, "admission not closed")
    require(closes["dynamic_overlap_reclassified_as_no_knob_upgrade_not_parity_prerequisite"] is True, "dynamic not reclassified")
    require(closes["measured_Yukawa_CKM_PMNS_Higgs_slots_admitted_downstream"] is True, "measured slots not admitted")

    remains = data["what_remains_open"]
    for key in [
        "measured_parameter_replay_manifest",
        "actual_numeric_SM_equivalence_replay",
        "empirical_equivalence_audit_run",
        "selected_dynamic_overlap_tensor_or_primitive_C1_contractions_for_no_knob_upgrade",
        "full_SM_equivalence_closure",
        "full_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    require("dynamic overlap tensor / A_selected / b_selected = no-knob upgrade target" in note, "note missing reclassification")
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
