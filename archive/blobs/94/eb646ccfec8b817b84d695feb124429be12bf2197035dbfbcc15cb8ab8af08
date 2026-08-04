"""Audit post-AH8 flavor-operator policy use and CKM/PMNS bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
BUILDER = ROOT / "scripts" / "build_selected_flavoroperatorpolicyuse_afterah8_or_ckmpmnsbridge.py"

SLUG = "selected_flavoroperatorpolicyuse_afterah8_or_ckmpmnsbridge"
PACKET_DIR = DATA / SLUG
CANDIDATE = DATA / f"{SLUG}.candidate.json"
CERT = CERTS / f"{SLUG}_certificate.json"
NOTE = CORPUS / "MTT_Selected_FlavorOperatorPolicyUseAfterAH8_or_CKMPMNSOrientationBridge_v1.md"
ORIENTATION_IMPORT = PACKET_DIR / "post_ah8_policy_operator_ckm_pmns_bridge_import.packet.json"
Q79_IMPORT = PACKET_DIR / "post_ah8_q79_ckm_phase_contact_import.packet.json"
HEAVY_TARGET = PACKET_DIR / "post_ah8_heavy_link_orientation_target.packet.json"
NEXT_PACKET = PACKET_DIR / "next_heavy_link_vector_values_after_policy_bridge.packet.json"

STATUS = "MTT_SELECTED_FLAVOROPERATORPOLICYUSE_AFTERAH8_CKMPMNS_BRIDGE_Q79_CONTACT_HEAVYLINK_OPEN"
NEXT = "MTT_Selected_HeavyLinkVectorValuesAfterPolicyBridge_or_CKMHigherBreakdownLaw_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    candidate = load(CANDIDATE)
    cert = load(CERT)
    orientation = load(ORIENTATION_IMPORT)
    q79 = load(Q79_IMPORT)
    heavy = load(HEAVY_TARGET)
    next_packet = load(NEXT_PACKET)
    note = NOTE.read_text(encoding="utf-8")

    require(candidate["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(candidate["next_required_artifact"] == NEXT, "candidate next mismatch")
    require(cert["next_required_artifact"] == NEXT, "certificate next mismatch")
    require(next_packet["next_required_artifact"] == NEXT, "next packet mismatch")
    require(candidate["theorem"]["proved"] is True, "candidate theorem not proved")
    require(cert["theorem_proved"] is True, "cert theorem not proved")

    for payload in [candidate, cert, orientation, q79, heavy, next_packet]:
        require(payload["closure_claimed"] is True, "closure boundary missing")
        require(payload["observed_data_used_as_selector"] is False, "observed selector used")
        require(payload["target_fitting_used"] is False, "target fitting used")

    decision = candidate["closure_decision"]
    require(decision["policy_operator_CKM_PMNS_bridge_imported"] is True, "bridge not imported")
    require(decision["policy_csk_source_value_row_count"] == 9, "policy rows")
    require(decision["strict_csk_source_row_count"] == 0, "strict rows overaccepted")
    require(decision["qualitative_CP_bridge_closed"] is True, "CP bridge")
    require(decision["q79_CKM_CP_phase_contact_imported"] is True, "q79 contact")
    require(decision["q_mod_448"] == 79, "q value")
    require(2.0 < decision["q79_phase_residual_deg"] < 2.3, "q79 phase residual changed")
    require(0.018 < decision["q79_jarlskog_relative_residual"] < 0.019, "J residual changed")
    require(decision["selected_heavy_link_values_emitted"] is False, "heavy link overemitted")
    require(decision["selected_CKM_PMNS_orientation_source_closed"] is False, "orientation source overclosed")
    require(decision["CKM_angles_derived"] is False, "CKM angles overderived")
    require(decision["full_no_knob_closed"] is False, "no-knob overclosed")
    require(decision["true_SM_equivalence_closed"] is False, "true SM overclosed")

    require(orientation["CKM_PMNS_orientation_bridge_executable"] is True, "orientation executable")
    require(orientation["flavor_operator_policy_value_use_closed"] is True, "policy use")
    require(orientation["policy_csk_source_value_row_count"] == 9, "orientation policy rows")
    require(orientation["strict_csk_source_row_count"] == 0, "orientation strict rows")
    require(orientation["selected_CKM_PMNS_orientation_source_closed"] is False, "orientation overclosed")

    require(q79["selected_CKM_CP_phase_contact_imported"] is True, "q79 packet contact")
    require(q79["q_mod_448"] == 79, "q79 packet q")
    require(q79["CKM_angle_magnitudes_derived"] is False, "q79 angle overderived")
    require(q79["full_CKM_orientation_values_derived"] is False, "q79 orientation overderived")
    require(q79["observed_CKM_used_as_selector"] is False, "CKM selector used")

    require(heavy["CKM_heavy_link_calculator_ready"] is True, "heavy calculator")
    require(heavy["leading_noncommutation_closed"] is True, "heavy noncommutation")
    require(heavy["selected_packet_values_open"] is True, "heavy packet not open")
    require(heavy["selected_heavy_link_values_emitted"] is False, "heavy values overemitted")
    for field in ["t_u13", "t_u23", "t_d13", "t_d23", "c_u13", "c_u23", "c_d13", "c_d23"]:
        require(field in heavy["required_packet_entries"], f"heavy field missing: {field}")

    for item in [
        "AH-equivalent BN27 8/8 matrix row",
        "minimal nine-slot flavor policy value table",
        "CKM/PMNS policy-tier bridge",
        "q79 CKM CP phase contact",
    ]:
        require(item in next_packet["do_not_reopen"], f"non-reopen missing: {item}")
    for item in [
        "selected heavy-link vector values t_u,t_d,c_u,c_d",
        "selected CKM angle magnitudes",
        "selected CKM/PMNS orientation source theorem",
        "strict csk/flavor source rows replacing policy values",
    ]:
        require(item in next_packet["remaining_orientation_targets"], f"target missing: {item}")

    require(cert["policy_operator_CKM_PMNS_bridge_imported"] is True, "cert bridge")
    require(cert["q79_CKM_CP_phase_contact_imported"] is True, "cert q79")
    require(cert["selected_heavy_link_values_emitted"] is False, "cert heavy")
    require(cert["selected_CKM_PMNS_orientation_source_closed"] is False, "cert orientation")
    require(cert["true_SM_equivalence_closed"] is False, "cert true SM")

    require("q79 CKM CP phase contact" in note, "note q79")
    require("heavy-link vector values" in note, "note heavy")
    require(NEXT in note, "note next")

    print("Post-AH8 CKM/PMNS bridge audit passed")
    print(json.dumps({"candidate": str(CANDIDATE.relative_to(ROOT)), "status": STATUS}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
