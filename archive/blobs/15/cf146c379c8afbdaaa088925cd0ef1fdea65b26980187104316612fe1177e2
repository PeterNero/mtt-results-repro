"""Audit Phi_fin alpha1 payload values or typed B_N retarded derivative execution."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_phifinalpha1payloadvalues_or_typedbnretardedderivativeexecution"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
EXECUTION = PACKET_DIR / "alpha1_derivative_dotd_execution_packet.packet.json"
TYPED = PACKET_DIR / "typed_bn_retarded_execution_status.packet.json"
GATE = PACKET_DIR / "dynamic_phifin_c1_payload_gate.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PhiFinAlpha1PayloadValues_or_TypedBNRetardedDerivativeExecution_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_PHIFINALPHA1PAYLOADVALUES_OR_TYPEDBNRETARDEDEXECUTION_BUILT_ALPHA1_RETIRED_DYNAMIC_PAYLOAD_OPEN"
NEXT = "MTT_Selected_PrimitiveC1Contractions_or_DynamicPhiFinC1Payload_ValueEmission_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    execution = load(EXECUTION)
    typed = load(TYPED)
    gate = load(GATE)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem not proved")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    lane_a = execution["lane_A_visible_routec_source_identity"]
    require(lane_a["source_identity"]["selected_emitted"] is True, "source identity regressed")
    require(lane_a["visible_routec_operator_source"]["selected_emitted"] is True, "visible source regressed")
    require(lane_a["same_branch_alpha1_derivative"]["selected_emitted"] is True, "alpha1 derivative not filled")
    require(lane_a["same_branch_alpha1_derivative"]["theorem_derived"] is True, "alpha1 derivative not theorem-derived")
    require(lane_a["dotd_validator_replay"]["selected_emitted"] is True, "dotD replay not filled")
    require(lane_a["dotd_validator_replay"]["honest_validator_exit_code"] == 0, "honest dotD replay not closed")
    require(lane_a["dotd_validator_replay"]["alpha1_driver_verified"] is True, "alpha1 driver not verified")
    require(lane_a["phi_fin_payload"]["selected_emitted"] is False, "dynamic payload overfilled")
    require(lane_a["phi_fin_payload"]["dynamic_C1_payload_selected"] is False, "dynamic C1 payload overselected")
    require(execution["validation"]["ok"] is False, "full lane unexpectedly validated")
    require("lane_A.phi_fin_payload: selected_emitted is not true" in execution["validation"]["errors"], "payload failure missing")

    require(typed["typed_retarded_derivative_emitted"] is False, "typed retarded derivative overemitted")
    require(typed["primitive_response_candidate_values_emitted"] is True, "primitive support candidate missing")
    require(typed["accepted_as_lane_B_validation"] is False, "Lane B overvalidated")

    require(gate["alpha1_derivative_retired"] is True, "alpha1 not retired")
    require(gate["honest_dotD_replay_retired"] is True, "dotD not retired")
    require(gate["visible_routec_contract_lane_A_fully_validates_now"] is False, "full Lane A overvalidated")
    require("selected dynamic Phi_fin C1 payload" in gate["remaining_primary_payloads"], "dynamic payload missing")
    require(gate["next_required_artifact"] == NEXT, "gate next mismatch")

    require(data["closure_decision"]["same_branch_alpha1_derivative_closed"] is True, "candidate alpha1 not closed")
    require(data["closure_decision"]["honest_dotd_validator_replay_closed"] is True, "candidate dotD not closed")
    require(data["closure_decision"]["phi_fin_dynamic_c1_payload_closed"] is False, "candidate dynamic payload overclosed")
    require(data["closure_decision"]["typed_bn_retarded_derivative_closed"] is False, "candidate typed retarded overclosed")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(cert["validator_ok"] is False, "certificate validator overpassed")

    for packet in [execution, typed, gate, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    require("retires alpha1 as the active blocker" in note, "note missing alpha1 retirement")
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
