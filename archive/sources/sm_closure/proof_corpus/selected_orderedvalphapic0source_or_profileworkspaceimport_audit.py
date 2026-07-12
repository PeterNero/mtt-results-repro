"""Audit ordered V_alpha/Pic0 source or profile workspace import bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SLUG = "selected_orderedvalphapic0source_or_profileworkspaceimport"
DATA = ROOT / "candidate_data" / f"{SLUG}.candidate.json"
PACKET_DIR = ROOT / "candidate_data" / SLUG
ORDERED_BRIDGE = PACKET_DIR / "ordered_valpha_pic0_bridge.packet.json"
PROFILE_WORKSPACE = PACKET_DIR / "profile_workspace_import_attempt.packet.json"
PROMOTION = PACKET_DIR / "promotion_decision_after_ordered_bridge.packet.json"
CUTSET = PACKET_DIR / "terminal_source_or_operator_workspace_cutset.packet.json"
CERT = ROOT / "certificates" / f"{SLUG}_certificate.json"
NOTE = ROOT / "proof_corpus" / "MTT_Selected_OrderedVAlphaPic0Source_or_ProfileWorkspaceImport_v1.md"
BUILDER = ROOT / "scripts" / f"build_{SLUG}.py"

STATUS = "MTT_SELECTED_ORDEREDVALPHAPIC0SOURCE_OR_PROFILEWORKSPACEIMPORT_BUILT_ORDERED_LAYER_BRIDGE_OPERATOR_OPEN"
NEXT = "MTT_Selected_TerminalSourceSwitch_or_OperatorPic0GerbeDE_v1"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    subprocess.run([sys.executable, str(BUILDER)], cwd=ROOT, check=True)

    data = load(DATA)
    bridge = load(ORDERED_BRIDGE)
    profile = load(PROFILE_WORKSPACE)
    promotion = load(PROMOTION)
    cutset = load(CUTSET)
    cert = load(CERT)
    note = NOTE.read_text(encoding="utf-8")

    require(data["status"] == STATUS, "candidate status mismatch")
    require(cert["status"] == STATUS, "certificate status mismatch")
    require(data["theorem"]["proved"] is True and cert["theorem_proved"] is True, "theorem flag missing")
    require(data["next_required_artifact"] == NEXT and cert["next_required_artifact"] == NEXT, "next artifact mismatch")

    target = bridge["ordered_target"]
    require(target["selected_ordered_difference"] == "L3-K2", "ordered target mismatch")
    require(target["L"] == [1, -2, 0], "L mismatch")
    require(target["L2"] == [2, -4, 0], "L2 mismatch")
    require(target["conditional_unique_target_inside_lane"] is True, "conditional target not retained")
    require(target["strict_ordered_validator_would_pass_after_source_and_pic0"] is True, "validator condition missing")

    pic0 = bridge["ordered_layer_pic0_accounting"]
    require(pic0["ordered_layer_pic0_closed"] is True, "ordered layer Pic0 not closed")
    require(pic0["ordered_pic0_removed_as_ordered_source_blocker"] is True, "ordered Pic0 blocker not removed")
    require(pic0["operator_layer_pic0_closed"] is False, "operator Pic0 overclosed")
    require("must recheck Pic0" in pic0["operator_layer_reopen_condition"], "operator Pic0 reopen guardrail missing")

    source_switch = bridge["source_switch_status"]
    require(source_switch["central_neutral_member_closed"] is True, "central neutral member missing")
    require(source_switch["monad_orientation_closed_as_candidate"] is True, "orientation candidate missing")
    for key in [
        "terminal_monad_lane_selection_closed",
        "standard_lattice_or_equivalent_closed",
        "base_factor_order_closed",
        "AH_or_Cech_binding_closed",
    ]:
        require(source_switch[key] is False, f"source switch overclosed: {key}")

    require(bridge["actual_ordered_source_promoted"] is False, "actual ordered source overpromoted")
    require(bridge["actual_operator_layer_pic0_resolved"] is False, "operator Pic0 overresolved")
    require(bridge["actual_QaSU3_packet_promoted"] is False, "Qa/SU3 packet overpromoted")
    require(bridge["accepted_for_true_SM_equivalence"] is False, "true SM equivalence overaccepted")
    require(len(bridge["operator_layer_still_requires"]) >= 8, "operator-layer requirements underspecified")
    require(bridge["superset_strategy_used"]["using_one_straight_path"] is False, "superset mode not recorded")
    require("no measured constants" in bridge["superset_strategy_used"]["locked_target"], "selector guardrail missing")

    require(profile["profile_workspace_imported"] is False, "profile workspace overimported")
    require(profile["surrogate_profile_remains_diagnostic_only"] is True, "surrogate guardrail missing")
    require(profile["can_close_true_SM_equivalence_now"] is False, "profile route overclosed")

    require(promotion["route_B_ordered_valpha_pic0_source"]["ordered_layer_pic0_closed"] is True, "promotion missing ordered Pic0")
    require(
        promotion["route_B_ordered_valpha_pic0_source"]["actual_ordered_source_promoted"] is False,
        "promotion overpromoted source",
    )
    require(
        promotion["route_B_ordered_valpha_pic0_source"]["operator_layer_pic0_resolved"] is False,
        "promotion overresolved operator Pic0",
    )
    require(promotion["route_B_ordered_valpha_pic0_source"]["actual_QaSU3_packet_promoted"] is False, "promotion overpromoted Qa/SU3")
    require(promotion["true_SM_equivalence_closed"] is False, "promotion true equivalence overclosed")
    require(promotion["no_knob_closed"] is False, "promotion no-knob overclosed")

    require(cutset["recommended_next_artifact"] == NEXT, "cutset next artifact mismatch")
    for required in [
        "promote terminal monad lane selection as MTT-selected source data",
        "select standard lattice or equivalent source and base-factor order",
        "bind L3-K2 to AH/Cech transition data from the same source",
        "resolve operator-layer Pic0 by same-source operator invariance or gerbe/twisted D_E replacement",
        "emit same-source D_E/rho_E, Riesz, Green, dotD, and projector retention",
    ]:
        require(required in cutset["remaining_minimal_payloads"], f"cutset missing: {required}")

    require(data["closure_decision"]["ordered_layer_pic0_bridged"] is True, "candidate bridge missing")
    require(data["closure_decision"]["actual_ordered_source_promoted"] is False, "candidate source overpromoted")
    require(data["closure_decision"]["actual_QaSU3_packet_promoted"] is False, "candidate Qa/SU3 overpromoted")
    require(data["closure_decision"]["profile_workspace_imported"] is False, "candidate profile overimported")
    require(cert["ordered_layer_pic0_bridged"] is True, "certificate bridge missing")
    require(cert["actual_QaSU3_packet_promoted"] is False, "certificate Qa/SU3 overpromoted")
    require("What does not close is the physical operator packet" in note, "note missing operator guardrail")

    for packet in [bridge, profile, promotion, cutset, data, cert]:
        require(packet.get("observed_data_used_as_selector") is False, "observed selector violation")
        require(packet.get("target_fitting_used") is False, "target fitting violation")

    print(json.dumps({"candidate": str(DATA.relative_to(ROOT)), "status": STATUS}, indent=2))
    print(f"PASS {DATA.name}: {STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
