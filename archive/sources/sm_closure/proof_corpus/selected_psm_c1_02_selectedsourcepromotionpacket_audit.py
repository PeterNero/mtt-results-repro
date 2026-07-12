"""Audit selected PSM-C1-02 source-promotion packet."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_psm_c1_02_selectedsourcepromotionpacket"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
CURRENT = PACKET_DIR / "current_unpatched_selected_source_promotion_packet.packet.json"
PATCHED = PACKET_DIR / "patched_local_axiom_source_promotion_packet.packet.json"
CONDITIONAL = PACKET_DIR / "conditional_unpatched_selected_source_promotion_packet.packet.json"
CURRENT_RESULT = PACKET_DIR / "current_unpatched_source_promotion_validator_result.packet.json"
PATCHED_RESULT = PACKET_DIR / "patched_local_axiom_source_promotion_validator_result.packet.json"
CONDITIONAL_RESULT = PACKET_DIR / "conditional_unpatched_source_promotion_validator_result.packet.json"
ROUTEB_CONDITIONAL_RESULT = PACKET_DIR / "conditional_routeb_strict_payload_validator_result.packet.json"
PROMOTION_MATRIX = PACKET_DIR / "psm_c1_02_source_promotion_matrix.packet.json"
NEXT = PACKET_DIR / "next_labeled_workorder.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_PSM_C1_02_SelectedSourcePromotionPacket_v1.md"
VALIDATOR = ROOT / "scripts" / "validate_selected_psm_c1_02_source_promotion_packet.py"

STATUS = "MTT_SELECTED_PSM_C1_02_SELECTEDSOURCEPROMOTIONPACKET_BUILT_UNPATCHED_SOURCE_OPEN"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validator_returncode(path: Path) -> int:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return proc.returncode


def closed_field_count(packet: dict) -> int:
    return sum(
        1
        for item in packet["source_fields"].values()
        if item["selected_emitted"] is True
        and item["theorem_derived"] is True
        and item["source_owner_verified"] is True
        and item["same_branch"] is True
    )


def main() -> int:
    data = load(DATA)
    current = load(CURRENT)
    patched = load(PATCHED)
    conditional = load(CONDITIONAL)
    current_result = load(CURRENT_RESULT)
    patched_result = load(PATCHED_RESULT)
    conditional_result = load(CONDITIONAL_RESULT)
    routeb_result = load(ROUTEB_CONDITIONAL_RESULT)
    matrix = load(PROMOTION_MATRIX)
    next_work = load(NEXT)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "status mismatch")
    require(data["active_post_sm_parity_label"] == "PSM-C1-02", "active label mismatch")
    require(data["post_sm_parity_label_context"]["closed_boundary"] == "DONE-PARITY-00", "closed boundary missing")
    require(data["theorem"]["proved"] is True, "theorem not proved")
    require(data["closure_claimed"] is False, "candidate overclaimed closure")
    require(data["observed_data_used_as_selector"] is False, "observed data used as selector")
    require(data["target_fitting_used"] is False, "target fitting used")

    require(current["mode"] == "current_unpatched", "current mode mismatch")
    require(current["free_axiom_patch_used"] is False, "current must be unpatched")
    require(closed_field_count(current) == 3, "current closed field count should be 3")
    require(current_result["passes"] is False, "current packet should fail")
    require(validator_returncode(CURRENT) == 1, "current validator return changed")

    require(patched["mode"] == "patched_local_axiom", "patched mode mismatch")
    require(patched["free_axiom_patch_used"] is True, "patched packet must disclose patch")
    require(patched_result["passes"] is False, "patched packet must fail unpatched validator")
    require(validator_returncode(PATCHED) == 1, "patched validator return changed")

    require(conditional["mode"] == "conditional_unpatched", "conditional mode mismatch")
    require(conditional["conditional_only"] is True, "conditional packet must be conditional")
    require(conditional["free_axiom_patch_used"] is False, "conditional must be unpatched")
    require(closed_field_count(conditional) == 9, "conditional must close all nine fields")
    require(conditional_result["passes"] is True, "conditional packet should pass")
    require(validator_returncode(CONDITIONAL) == 0, "conditional validator return changed")

    require(routeb_result["passes"] is True, "strict Route-B conditional payload should pass")
    require(matrix["current_packet_passes"] is False, "matrix overclaims current pass")
    require(matrix["patched_packet_passes_unpatched_validator"] is False, "matrix should reject patch")
    require(matrix["conditional_packet_passes"] is True, "matrix missing conditional pass")
    require(matrix["closed_current_fields"] == 3, "matrix closed count mismatch")
    require(matrix["open_current_fields"] == 4, "matrix open count mismatch")
    require(matrix["dynamic_values_ready"] is True, "dynamic values should be ready")
    require(matrix["unpatched_source_rule_proved"] is False, "unpatched source rule overclaimed")
    require(matrix["honest_galerkin_table_exported"] is False, "honest Galerkin export overclaimed")

    require(next_work["active_label"] == "PSM-C1-02", "next active label mismatch")
    require(next_work["next_required_artifact"] == data["next_required_artifact"], "next artifact mismatch")
    require(cert["closure_claimed"] is False, "certificate overclaimed closure")
    require(cert["current_unpatched_packet_passes"] is False, "certificate overclaims current")
    require(cert["patched_packet_passes_unpatched_validator"] is False, "certificate overclaims patch")
    require(cert["conditional_unpatched_packet_passes"] is True, "certificate missing conditional")
    require("post-SM-parity frontier" in note, "note missing frontier language")
    require("not an SM-parity blocker" in note, "note missing boundary guardrail")
    require("Patched local-axiom mode" in note, "note missing patch separation")

    print(f"PASS {DATA.name}: {data['status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
