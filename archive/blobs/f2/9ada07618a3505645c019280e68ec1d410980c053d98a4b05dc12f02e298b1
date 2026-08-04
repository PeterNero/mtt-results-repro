"""Audit the measured-parameter replay manifest for SM-equivalence."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "sm_equivalence_measured_parameter_replay_manifest.candidate.json"
CERT = ROOT / "certificates" / "sm_equivalence_measured_parameter_replay_manifest_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SM_Equivalence_Measured_Parameter_Replay_Manifest_v1.md"
BUILDER = ROOT / "scripts" / "build_sm_equivalence_measured_parameter_replay_manifest.py"

STATUS = "MTT_SM_EQUIVALENCE_MEASURED_PARAMETER_REPLAY_MANIFEST_BUILT_VALUES_OPEN"
NEXT = "MTT_SM_Equivalence_Reference_Data_Packet_v1"


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

    strategy = data["superset_strategy_use"]
    require(
        strategy["mode"] == "SUPERSET_TO_LOCKED_SOURCE_THEN_STRAIGHT_MEASURED_REPLAY",
        "wrong superset strategy mode",
    )
    require(strategy["measured_targets_used_to_lock_source"] is False, "measured targets select source")
    require("straight SM-standard downstream computation" in strategy["explanation"], "strategy not explained")

    preconditions = data["preconditions"]
    for key in [
        "measured_admission_closed",
        "static_source_boundary_closed",
        "measured_inputs_do_not_select_sources",
        "empirical_interfaces_ready",
        "all_six_static_sm_slot_arrows_closed",
    ]:
        require(preconditions[key] is True, f"precondition not closed: {key}")

    slots = data["slot_manifest"]
    slot_ids = {slot["slot_id"] for slot in slots}
    required_ids = {
        "gauge.alpha_1_alpha_2_alpha_3",
        "yukawa.Y_u_Y_d_Y_e",
        "mixing.CKM",
        "mixing.PMNS",
        "higgs.v_mh_lambda_or_potential",
        "neutrino.yukawa_or_mass_splittings",
    }
    require(required_ids <= slot_ids, "required measured slots missing")
    for slot in slots:
        require(slot["parameter_class"] == "MEASURED_PARITY_INPUT", f"wrong class: {slot['slot_id']}")
        require(slot["value_status"] == "MEASURED_VALUE_NOT_FILLED_IN_THIS_MANIFEST", "value filled too early")
        require(slot["required_reference_fields"], f"reference schema missing: {slot['slot_id']}")
        require(slot["required_conventions"], f"conventions missing: {slot['slot_id']}")
        require(slot["allowed_replay_targets"], f"replay target missing: {slot['slot_id']}")
        require("source selection" in slot["forbidden_uses"], f"source guard missing: {slot['slot_id']}")
        require(slot["no_knob_upgrade_target"], f"no-knob target missing: {slot['slot_id']}")

    pipeline = {step["step"]: step for step in data["replay_pipeline"]}
    require(pipeline["freeze_selected_source_boundary"]["status"] == "READY", "source freeze not ready")
    require(pipeline["load_reference_data_packet"]["status"] == "OPEN_NEXT", "next packet not open next")
    require(pipeline["empirical_equivalence_audit"]["status"] == "OPEN", "empirical audit not open")
    require("cannot promote a no-knob selector" in pipeline["empirical_equivalence_audit"]["rule"], "audit guard missing")

    policy = data["reference_data_policy"]
    require(policy["values_filled_here"] is False, "values filled in manifest")
    require(policy["next_packet_must_freeze_values_before_replay"] is True, "next packet freeze not required")
    require(any("PDG" in source for source in policy["preferred_sources"]), "PDG-like source not requested")
    require("basis and phase convention" in policy["must_record"], "basis/phase record missing")

    forbidden = " ".join(data["forbidden_promotions"])
    for phrase in ["Yukawa", "CKM", "gauge couplings", "masses", "no-knob proof"]:
        require(phrase in forbidden, f"forbidden promotion missing: {phrase}")

    closes = data["what_closes_now"]
    for key in [
        "measured_slot_manifest_built",
        "SM_equivalence_replay_pipeline_declared",
        "reference_data_packet_schema_declared",
        "superset_use_limited_to_source_boundary",
        "source_selection_guardrails_preserved",
    ]:
        require(closes[key] is True, f"close flag missing: {key}")

    remains = data["what_remains_open"]
    for key in [
        "reference_data_packet_values",
        "actual_numeric_tree_level_replay",
        "RG_scheme_transport_replay",
        "empirical_equivalence_audit_run",
        "full_SM_equivalence_closure",
        "full_no_knob_closure",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["sm_equivalence_claimed"] is False, "SM equivalence overclaimed")
    require(data["no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used as selector")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")
    require("successful replay is evidence for SM-equivalence only" in note, "note guardrail missing")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
