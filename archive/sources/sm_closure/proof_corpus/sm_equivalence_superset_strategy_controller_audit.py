"""Audit the SM-equivalence superset strategy controller."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data" / "sm_equivalence_superset_strategy_controller.candidate.json"
CERT = ROOT / "certificates" / "sm_equivalence_superset_strategy_controller_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_SM_Equivalence_Superset_Strategy_Controller_v1.md"
BUILDER = ROOT / "scripts" / "build_sm_equivalence_superset_strategy_controller.py"

STATUS = "MTT_SM_EQUIVALENCE_SUPERSET_STRATEGY_CONTROLLER_BUILT_SOURCE_FIRST_MEASURED_DOWNSTREAM"
NEXT = "MTT_Selected_PrimitiveC1Contractions_or_DynamicOverlapTensor_SourceEmission_v1"


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

    goal = data["branch_goal"]
    require(goal["primary_goal"] == "SM-equivalence / SM-parity closure", "wrong primary goal")
    require(goal["secondary_goal"] == "no-knob derivation as upgrade path", "wrong secondary goal")

    source = data["selected_source_before_measurement"]
    require(source["sm_sector_interface_ready"] is True, "SM sector interface not ready")
    require(source["static_sm_slot_functor_routing_closed"] is True, "static routing not closed")
    require(source["dynamic_operator_payload_open"] is True, "dynamic boundary not open")
    require(source["actual_selected_sm_packet_closed"] is False, "selected SM packet overclaimed")
    require(source["qa_su3_color_operator_packet_supplied"] is False, "Qa/SU3 overclaimed")

    program = data["superset_program"]
    require(program["mode"] == "SM_EQUIVALENCE_FIRST_NO_KNOB_LATER", "wrong strategy mode")
    require(program["locked_target"] == NEXT, "locked target mismatch")
    require("Yukawa" in " ".join(program["allowed_measured_inputs_after_target"]), "Yukawa input missing")
    forbidden = " ".join(program["forbidden_uses"])
    require("source selection" in forbidden and "measured" in forbidden, "source-selection guard missing")
    require("A_selected" in forbidden and "b_selected" in forbidden, "dynamic guard missing")

    gates = data["acceptance_gates"]
    require(gates["G0_branch_policy"]["closed"] is True, "branch policy not closed")
    require(gates["G1_measured_parameter_policy"]["closed"] is True, "measured policy not closed")
    require(gates["G2_static_sm_source_structure"]["closed_for_interface"] is True, "static interface not ready")
    require(gates["G2_static_sm_source_structure"]["closed_for_full_packet"] is False, "full packet overclaimed")
    require(gates["G3_static_weyl_sector_routing"]["closed"] is True, "static routing gate not closed")
    require(gates["G4_dynamic_operator_boundary"]["closed"] is False, "dynamic boundary overclosed")
    require(gates["G4_dynamic_operator_boundary"]["next_required_artifact"] == NEXT, "G4 next mismatch")
    require(gates["G5_measured_sm_replay"]["closed"] is False, "measured replay overclosed")

    require(data["closure_claimed"] is False, "closure overclaimed")
    require(data["sm_equivalence_claimed"] is False, "SM equivalence overclaimed")
    require(data["no_knob_closure_claimed"] is False, "no-knob overclaimed")
    require(data["observed_data_used_as_selector"] is False, "observed data used as selector")
    require(data["target_fitting_used"] is False, "target fitting used")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(cert["theorem_proved"] is True, "certificate theorem missing")

    closes = data["what_closes_now"]
    require(closes["branch_policy_set_to_SM_equivalence_first"] is True, "branch policy not closed")
    require(closes["measured_inputs_allowed_only_downstream"] is True, "downstream policy missing")
    require(closes["no_knob_kept_as_upgrade_not_prerequisite"] is True, "no-knob policy missing")

    remains = data["what_remains_open"]
    for key in [
        "selected_dynamic_overlap_tensor_or_primitive_C1_contractions",
        "selected_A_selected",
        "selected_b_selected",
        "measured_SM_replay_after_source_boundary",
        "full_SM_equivalence_closure",
        "no_knob_constants_derivation",
    ]:
        require(remains[key] is True, f"remaining blocker missing: {key}")

    require("SM-equivalence" in note and "Measured SM constants are allowed only after" in note, "note policy missing")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
