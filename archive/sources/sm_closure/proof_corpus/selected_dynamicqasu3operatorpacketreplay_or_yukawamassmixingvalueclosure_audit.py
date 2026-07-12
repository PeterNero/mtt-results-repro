"""Audit dynamic Qa/SU3 replay or Yukawa/mass/mixing value closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_dynamicqasu3operatorpacketreplay_or_yukawamassmixingvalueclosure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
QASU3_REPLAY = PACKET_DIR / "dynamic_qasu3_operator_packet_replay.packet.json"
YUKAWA_ATTEMPT = PACKET_DIR / "yukawa_mass_mixing_value_closure_attempt.packet.json"
TRUE_EQ_GATE = PACKET_DIR / "true_equivalence_gate_after_dynamic_qasu3_replay.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_dynamic_qasu3_replay.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_DynamicQaSU3OperatorPacketReplay_or_YukawaMassMixingValueClosure_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_DYNAMICQASU3OPERATORPACKETREPLAY_OR_YUKAWAMASSMIXINGVALUECLOSURE_"
    "BUILT_DYNAMIC_PACKET_REPLAYED_VALUE_CLOSURE_OPEN"
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
    qasu3 = load(QASU3_REPLAY)
    yukawa = load(YUKAWA_ATTEMPT)
    true_gate = load(TRUE_EQ_GATE)
    cutset = load(NEXT_CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(qasu3["dynamic_matter_overlap_packet_closed"] is True, "dynamic packet not imported")
    require(qasu3["actual_QaSU3_operator_packet_first_response_layer_closed"] is True, "Qa/SU3 first response not closed")
    require(qasu3["not_a_precision_value_packet"] is True, "precision value overclaim missing")
    for key in [
        "mass_split_positive",
        "ckm_commutator_positive",
        "pmns_commutator_positive",
        "cp_odd_invariant_nonzero",
    ]:
        require(qasu3["qualitative_flavor_response"][key] is True, f"qualitative test missing {key}")

    decision = yukawa["closure_decision"]
    for key in [
        "Yukawa_magnitudes_closed",
        "running_mass_ratios_closed",
        "CKM_PMNS_measured_angles_phase_closed",
        "Higgs_RG_precision_closed",
        "true_SM_equivalence_closed",
        "full_SM_no_knob_closed",
    ]:
        require(decision[key] is False, f"value closure overclaimed: {key}")
    require(true_gate["actual_QaSU3_operator_packet_status"]["first_response_layer_now_closed"] is True, "true gate did not import first response")
    require(true_gate["actual_QaSU3_operator_packet_status"]["full_precision_packet_closed"] is False, "full precision overclosed")
    require(true_gate["true_equivalence"]["true_SM_equivalence_closed"] is False, "true equivalence overclosed")
    require(data["promotion_decision"]["dynamic_QaSU3_first_response_layer_closed"] is True, "candidate did not promote first response")
    require(data["promotion_decision"]["accepted_Yukawa_magnitudes_closed"] is False, "candidate overclosed Yukawa")
    require(data["promotion_decision"]["true_SM_equivalence_closed"] is False, "candidate overclosed true SM")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    require("does not close accepted Yukawa magnitudes" in " ".join(note.split()), "note missing value guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
