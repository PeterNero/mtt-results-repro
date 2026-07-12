"""Audit post-source-promotion full-SM gap audit / dotD alpha1 closure."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_postsourcepromotionfullsmgapaudit_or_dotdalpha1matterroutingclosure"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ALPHA1_RESULT = PACKET_DIR / "alpha1_dotd_driver_validator_result.packet.json"
MATTER_RESULT = PACKET_DIR / "same_source_dynamic_matter_overlap_validator_result.packet.json"
MATRIX = PACKET_DIR / "postsource_fullsm_gap_matrix.packet.json"
NEXT_CUTSET = PACKET_DIR / "next_cutset_after_postsource_gap_audit.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PostSourcePromotionFullSMGapAudit_or_DotDAlpha1MatterRoutingClosure_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = (
    "MTT_SELECTED_POSTSOURCEPROMOTIONFULLSMGAPAUDIT_OR_DOTDALPHA1MATTERROUTINGCLOSURE_"
    "BUILT_ALPHA1_CLOSED_STATIC_MATTER_CLOSED_DYNAMIC_FULLSM_OPEN"
)
NEXT = "MTT_Selected_SameSourceDynamicMatterOverlapOperatorPacket_or_PrimitiveC1ValueClosure_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    cert = load(CERT)
    alpha1 = load(ALPHA1_RESULT)
    matter = load(MATTER_RESULT)
    matrix = load(MATRIX)
    cutset = load(NEXT_CUTSET)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(data["observed_data_used_as_selector"] is False, "observed selector used")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(alpha1["returncode"] == 0, "alpha1 validator should pass")
    require(any('"ok": true' in line for line in alpha1["stdout"]), "alpha1 ok missing")
    require(matter["returncode"] == 1, "dynamic matter validator should reject")
    require(any('"ok": false' in line for line in matter["stdout"]), "matter rejection missing")

    require(matrix["alpha1_dotd"]["closed"] is True, "alpha1 not closed in matrix")
    require(matrix["matter_slot_routing"]["static_readout_closed"] is True, "static matter not closed")
    require(matrix["matter_slot_routing"]["dynamic_same_source_packet_closed"] is False, "dynamic matter overclosed")
    require(matrix["full_SM"]["SM_parity_remains_closed"] is True, "SM parity not preserved")
    require(matrix["full_SM"]["true_SM_equivalence_closed"] is False, "true SM overclosed")
    require(matrix["full_SM"]["no_knob_closed"] is False, "no-knob overclosed")

    require(data["what_closes_now"]["alpha1_driver_verified"] is True, "alpha1 driver not promoted")
    require(data["what_closes_now"]["selected_dotD_source_verified"] is True, "dotD source not promoted")
    require(data["what_closes_now"]["static_matter_slot_readout_closed"] is True, "static matter not promoted")
    require(data["what_remains_open"]["same_source_dynamic_matter_overlap_operator_packet"] is True, "dynamic matter gap missing")
    require(data["promotion_decision"]["true_SM_equivalence_closed"] is False, "true SM overclosed in candidate")
    require(data["promotion_decision"]["full_SM_no_knob_closed"] is False, "full SM overclosed in candidate")
    require(cutset["recommended_next"]["artifact"] == NEXT, "cutset next mismatch")
    normalized_note = " ".join(note.split())
    require("full SM/no-knob closure is still not claimed" in normalized_note, "note missing guardrail")

    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
