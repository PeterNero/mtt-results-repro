"""Audit terminal source switch or operator Pic0/gerbe D_E bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_terminalsourceswitch_or_operatorpic0gerbede"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
TERMINAL_SWITCH = PACKET_DIR / "terminal_source_switch_assessment.packet.json"
GERBE_ROUTE = PACKET_DIR / "operator_pic0_gerbe_de_replacement.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_terminal_or_gerbe.packet.json"
CUTSET = PACKET_DIR / "visible_operator_payload_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_TerminalSourceSwitch_or_OperatorPic0GerbeDE_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_TERMINALSOURCESWITCH_OR_OPERATORPIC0GERBEDE_BUILT_GERBE_ROUTE_PRIMARY_OPERATOR_PAYLOAD_OPEN"
NEXT = "MTT_Selected_VisibleOperatorPayload_or_RouteCHYMResidual_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    terminal = load(TERMINAL_SWITCH)
    gerbe = load(GERBE_ROUTE)
    promotion = load(PROMOTION)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    require(terminal["terminal_source_switch_closed_conditionally"] is True, "terminal route should be conditionally closed")
    require(terminal["terminal_source_switch_unconditional"] is False, "terminal route overpromoted")
    require(terminal["actual_terminal_source_promoted_in_current_chain"] is False, "actual terminal source overpromoted")
    require(
        terminal["conditional_source_closure"]["selected_source_label"] == "g3 / L3-K2",
        "terminal selected label mismatch",
    )
    require(
        terminal["conditional_source_closure"]["selected_L"] == [1, -2, 0]
        and terminal["conditional_source_closure"]["selected_L2"] == [2, -4, 0],
        "terminal L/L2 mismatch",
    )

    require(gerbe["direct_pic0_invariance_status"] == "RETIRED_FOR_NOW", "direct Pic0 not retired")
    require(gerbe["neutral_pic0_selection_status"] == "ABSENT", "neutral Pic0 unexpectedly selected")
    require(gerbe["primary_execution_route"] == "PRIMARY_EXECUTION_ROUTE", "gerbe route not primary")
    require(gerbe["source_level_gerbe_rhoe_promoted"] is True, "source-level gerbe rhoE missing")
    require(gerbe["operator_level_projective_rhoe_promoted"] is False, "operator rhoE overpromoted")
    require(gerbe["operator_pic0_replaced_for_next_attempt"] is True, "operator Pic0 replacement not selected")
    require(gerbe["actual_DE_payload_emitted"] is False, "D_E payload overemitted")
    require(gerbe["accepted_as_actual_QaSU3_packet"] is False, "Qa/SU3 packet overaccepted")
    require(gerbe["accepted_for_true_SM_equivalence"] is False, "true SM equivalence overaccepted")

    closed = gerbe["closed_at_source_or_restriction_level"]
    for key in [
        "selected_S3_flat_Deligne_class",
        "selected_S3_pullback_table",
        "smooth_Freed_Witten_cancellation",
        "block_projector_retention",
        "map_to_qutrit_central_cocycle",
        "visible_Green_Schwarz_curvature",
    ]:
        require(closed[key] is True, f"source/restriction support missing: {key}")

    open_ops = gerbe["still_open_at_operator_level"]
    for key in [
        "selected_visible_operator_source_constructed",
        "selected_D_E_dotD_Riesz_Green_constructed",
        "coherent_spectral_zero_mode_projectors_constructed",
        "selected_hym_or_route_c_residual_closed",
    ]:
        require(open_ops[key] is False, f"operator gate overclosed: {key}")

    require(
        promotion["route_A_terminal_source_switch"]["unconditional_terminal_source_switch_closed"] is False,
        "promotion overclosed terminal route",
    )
    require(
        promotion["route_B_operator_pic0_gerbe_de"]["selected_s3_gerbe_source_certified"] is True,
        "promotion missing selected S3 route",
    )
    require(
        promotion["route_B_operator_pic0_gerbe_de"]["actual_DE_payload_emitted"] is False,
        "promotion overemitted D_E",
    )
    require(promotion["true_SM_equivalence_closed"] is False, "promotion true equivalence overclosed")
    require(promotion["no_knob_closed"] is False, "promotion no-knob overclosed")

    require(cutset["recommended_next_artifact"] == NEXT, "cutset next artifact mismatch")
    for required in [
        "selected visible SM bundle/sheaf or Route-C source on q79/F,m=1",
        "Chern-Weil derivation of Tr_F_visible^2 from that same source",
        "HYM/Strominger or Route-C residual with selected_source_verified true",
        "sector D_E action matrices for Q,u,d,L,e,N,H with selected-source proof",
        "Riesz projector, complement gap, reduced Green, and truncation data",
        "same-branch dotD_alpha1 and horizontal responses",
    ]:
        require(required in cutset["remaining_minimal_payloads"], f"cutset missing: {required}")

    require(data["closure_decision"]["terminal_source_switch_conditionally_closed"] is True, "candidate missing conditional terminal route")
    require(data["closure_decision"]["unconditional_terminal_source_switch_closed"] is False, "candidate terminal overclosed")
    require(data["closure_decision"]["operator_pic0_replaced_by_gerbe_route"] is True, "candidate missing gerbe replacement")
    require(data["closure_decision"]["actual_DE_payload_emitted"] is False, "candidate D_E overemitted")
    require(data["closure_decision"]["actual_QaSU3_packet_promoted"] is False, "candidate Qa/SU3 overpromoted")
    require(cert["operator_pic0_replaced_by_gerbe_route"] is True, "certificate missing gerbe route")
    require(cert["actual_QaSU3_packet_promoted"] is False, "certificate Qa/SU3 overpromoted")
    require("This is a real narrowing" in note, "note missing narrowing statement")

    for packet in [terminal, gerbe, promotion, cutset, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
