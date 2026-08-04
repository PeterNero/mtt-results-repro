"""Audit Qa/SU3 candidate payload fill or profile source acquisition."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_qasu3candidatepayloadfill_or_profilesourceacquisition"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
PAYLOAD_FILL = PACKET_DIR / "qasu3_candidate_payload_fill_attempt.packet.json"
PROFILE_ACQ = PACKET_DIR / "profile_source_acquisition_attempt.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_payload_fill.packet.json"
CUTSET = PACKET_DIR / "ordered_source_or_profile_workspace_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_QaSU3CandidatePayloadFill_or_ProfileSourceAcquisition_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_QASU3CANDIDATEPAYLOADFILL_OR_PROFILESOURCEACQUISITION_BUILT_PARTIAL_PAYLOAD_TRUE_EQ_OPEN"
NEXT = "MTT_Selected_OrderedVAlphaPic0Source_or_ProfileWorkspaceImport_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    payload = load(PAYLOAD_FILL)
    profile = load(PROFILE_ACQ)
    promotion = load(PROMOTION)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(payload["best_lane"] == "local_same_source_visible_color_attempt", "wrong best lane")
    require(payload["best_lane_present"] is True, "best lane support missing")
    require(payload["partial_payload_emitted"] is True, "partial payload not emitted")
    require(payload["partial_payload_fields"]["ordered_difference"] == "L3_minus_K2", "ordered difference mismatch")
    require(payload["partial_payload_fields"]["line_bundle_value"] == [1, -2, 0], "line-bundle value mismatch")
    require(payload["partial_payload_fields"]["doubled_c2_value"] == [2, -4, 0], "doubled value mismatch")
    require(payload["partial_payload_fields"]["unique_ordered_difference"] is True, "unique ordered difference missing")
    require(payload["partial_payload_fields"]["visible_gs_bianchi_residual_zero"] is True, "GS residual not closed")
    require(payload["actual_selected_operator_payload_filled"] is False, "actual operator payload overfilled")
    require(payload["accepted_as_actual_QaSU3_packet"] is False, "Qa/SU3 packet overaccepted")
    require(payload["accepted_for_true_SM_equivalence"] is False, "true equivalence overaccepted")
    require(payload["accepted_for_no_knob"] is False, "no-knob overaccepted")
    require(payload["filled_operator_slot_count"] < payload["required_operator_slot_count"], "operator slots unexpectedly complete")

    required_open_slots = [
        "selected_source_status_for_L3_minus_K2_or_enlarged_visible_source",
        "Pic0_selection_or_physical_quotient_theorem",
        "transition_rhoE_or_Cech_Dolbeault_DE_data",
        "selected_HYM_or_RouteC_residual",
        "Riesz_Green_dotD_projector_retention",
    ]
    for slot in required_open_slots:
        require(payload["operator_payload_slots"][slot] is False, f"slot overclosed: {slot}")

    require("superset path" in payload["superset_strategy_used"], "superset strategy not recorded")
    require("no observed SM constants select the lane" in payload["superset_strategy_used"], "selector guardrail missing")

    require(profile["local_profile_source_imported_now"] is False, "profile source overimported")
    require(profile["surrogate_profile_remains_diagnostic_only"] is True, "surrogate guardrail missing")
    require(profile["route_A_can_close_true_SM_equivalence_now"] is False, "route A overclosed")
    require(len(profile["required_profile_workspace_payload"]) >= 5, "profile workspace payload underspecified")

    require(promotion["route_B_qasu3_payload_fill"]["partial_payload_emitted"] is True, "promotion missing partial payload")
    require(
        promotion["route_B_qasu3_payload_fill"]["actual_selected_operator_payload_filled"] is False,
        "promotion overfilled actual operator payload",
    )
    require(promotion["route_B_qasu3_payload_fill"]["can_close_true_SM_equivalence_now"] is False, "route B overcloses")
    require(promotion["true_SM_equivalence_closed"] is False, "promotion true equivalence overclosed")
    require(promotion["no_knob_closed"] is False, "promotion no-knob overclosed")

    require(cutset["recommended_next_artifact"] == NEXT, "cutset next artifact mismatch")
    for required in [
        "source-select the ordered V_alpha/L3-K2 lane or an enlarged visible source",
        "prove Pic0 selection or a physical quotient theorem removing Pic0",
        "emit selected transition/rho_E or Cech-Dolbeault/D_E data",
        "prove selected HYM/Route-C residual and Riesz/Green/dotD/projector retention",
    ]:
        require(required in cutset["remaining_minimal_payloads"], f"cutset missing: {required}")

    require(data["source_presence_checked"]["all_mined_candidates_present"] is True, "mined candidates not present")
    require(data["source_presence_checked"]["same_source_packet_present"] is True, "same-source packet not present")
    require(data["source_presence_checked"]["parity_interface_support_present"] is True, "parity support not present")
    require(data["closure_decision"]["partial_QaSU3_payload_filled"] is True, "candidate partial payload missing")
    require(data["closure_decision"]["actual_QaSU3_packet_promoted"] is False, "candidate Qa/SU3 overpromoted")
    require(data["closure_decision"]["profile_workspace_imported"] is False, "candidate profile overimported")
    require(data["closure_decision"]["true_SM_equivalence_closed"] is False, "candidate true equivalence overclosed")
    require(cert["partial_QaSU3_payload_filled"] is True, "certificate partial payload missing")
    require(cert["actual_QaSU3_packet_promoted"] is False, "certificate overpromoted")
    require("This is progress, but not closure" in note, "note missing closure guardrail")

    for packet in [payload, profile, promotion, cutset, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
