"""Attempt Selected_Terminal_Monad_Lane_Source_Selector_v1."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CERTS = ROOT / "certificates"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

Q79_PACKET = Q79 / "candidate_data" / "visible_rank2_l2_ordered_source.monad_difference_candidate.json"
Q79_VALIDATOR = Q79 / "scripts" / "validate_visible_rank2_l2_ordered_source_packet.py"
Q79_PROOF = Q79 / "certificates" / "selected_monad_difference_l2_source_proof_attempt_certificate.json"
Q79_OBSTRUCTION = Q79 / "certificates" / "visible_rank2_l2_selector_obstruction_certificate.json"

TERMINAL = CERTS / "selected_qa_su3_terminal_monad_lane_selector_attempt_certificate.json"
PIC0 = CERTS / "selected_monad_difference_l2_source_and_pic0_quotient_attempt_certificate.json"
H1 = CERTS / "selected_qa_su3_m1_rank2_ext_h1_source_data_attempt_certificate.json"

OUTPUT_CERT = CERTS / "selected_terminal_monad_lane_source_selector_attempt_certificate.json"
OUTPUT_PACKET = CERTS / "selected_terminal_monad_lane_source_selector.if_axiom_packet.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(packet: dict[str, Any], name: str) -> dict[str, Any]:
    tmp = CERTS / f"_tmp_{name}.json"
    tmp.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    try:
        proc = subprocess.run(
            [sys.executable, str(Q79_VALIDATOR), str(tmp)],
            cwd=Q79,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
    finally:
        try:
            tmp.unlink()
        except OSError:
            pass

    report = None
    for line in proc.stdout.splitlines():
        if line.startswith("visible_rank2_l2_ordered_source_validation_report="):
            report = json.loads(line.split("=", 1)[1])
    return {"exit_code": proc.returncode, "stdout": proc.stdout, "parsed_report": report}


def apply_pic0_quotient(packet: dict[str, Any]) -> None:
    packet["pic0_resolution"] = {
        "resolution": "pic0_quotient_rule",
        "source_selected_or_quotiented": True,
        "scope": "ordered Chern-Weil/H1 source gate only",
        "not_global_holonomy_claim": True,
    }


def apply_terminal_source_axiom(packet: dict[str, Any]) -> None:
    packet["candidate_role"] = "SELECTED_DATA"
    packet["status"] = "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED"
    packet["source"]["fixture_only"] = False
    packet["source"]["selected_by_mtt"] = True
    packet["source"]["source_certificate"] = "Selected_Terminal_Monad_Lane_Source_Selector.v1"
    packet["source"]["source_status"] = "VISIBLE_RANK2_L2_ORDERED_SOURCE_SELECTED_PIC0_QUOTIENTED"
    packet["selection_evidence"]["standard_lattice_or_equivalent_selected"] = True
    packet["selection_evidence"]["base_factor_order_selected"] = True
    packet["selection_evidence"]["base_swap_broken_by_source"] = True


def main() -> None:
    terminal = load(TERMINAL)
    pic0 = load(PIC0)
    h1 = load(H1)
    proof = load(Q79_PROOF)
    obstruction = load(Q79_OBSTRUCTION)
    base = load(Q79_PACKET)

    pic0_only = copy.deepcopy(base)
    apply_pic0_quotient(pic0_only)
    pic0_validation = validate(pic0_only, "terminal_selector_pic0_only")

    if_axiom = copy.deepcopy(pic0_only)
    apply_terminal_source_axiom(if_axiom)
    axiom_validation = validate(if_axiom, "terminal_selector_if_axiom")

    terminal_scan = proof["terminal_monad_difference_scan"]
    selected_candidate = terminal_scan["selected_candidate_inside_lane"]
    obstruction_theorem = obstruction["obstruction_theorem"]

    base_swap_obstruction_survives = (
        obstruction["no_breaking_source_available"] is True
        and obstruction["attempt_to_prove_target_selector"]["proved_unique_target_selection"] is False
        and obstruction["current_breaking_sources"]["selected_D_E_dotD_Hessian_orders_base_factors"] is False
        and obstruction["current_breaking_sources"]["selected_ordered_integral_source_for_L2"] is False
    )

    candidate_routes = {
        "R1_current_closed_invariants": {
            "status": "REFUTED_BY_BASE_SWAP_OBSTRUCTION",
            "can_select_terminal_lane": False,
            "reason": obstruction_theorem["theorem"],
        },
        "R2_local_pic0_quotient_plus_terminal_arithmetic": {
            "status": "SUFFICIENT_IF_SOURCE_AXIOM_SUPPLIED",
            "can_select_terminal_lane": False,
            "validator_if_axiom": {
                "exit_code": axiom_validation["exit_code"],
                "status": (axiom_validation["parsed_report"] or {}).get("status"),
                "open_items": (axiom_validation["parsed_report"] or {}).get("open_items"),
            },
            "reason": (
                "Pic0 is no longer a local ordered-gate blocker, and terminal "
                "arithmetic forces L3-K2 inside the terminal lane; however the "
                "choice of the terminal lane itself is not derived."
            ),
        },
        "R3_selected_wall_or_base_order_source": {
            "status": "OPEN_REQUIRED_BREAKING_SOURCE",
            "can_select_terminal_lane": False,
            "must_supply": [
                "selected target Gauduchon wall r1:r2=sqrt(2):1",
                "or an equivalent source that orders the two base elliptic factors",
            ],
        },
        "R4_same_source_DE_dotD_Riesz_Green": {
            "status": "OPEN_REQUIRED_BREAKING_SOURCE",
            "can_select_terminal_lane": False,
            "must_supply": [
                "selected D_E on the same V_alpha/L3-K2 source",
                "dotD_alpha1 primitive response",
                "Riesz projector and reduced Green operator",
                "proof the operator response breaks base-swap in the target direction",
            ],
        },
        "R5_typed_transition_or_rhoE_data": {
            "status": "OPEN_REQUIRED_SOURCE_DATA",
            "can_select_terminal_lane": False,
            "must_supply": terminal["minimal_next_object"]["two_allowed_routes"][0]["must_supply"],
        },
    }

    output = {
        "certificate": "SelectedTerminalMonadLaneSourceSelectorAttempt",
        "status": "TERMINAL_MONAD_LANE_SOURCE_SELECTOR_REDUCED_TO_BASE_ORDER_BREAKING_SOURCE_OPEN",
        "inputs": {
            "terminal_lane_attempt": str(TERMINAL.relative_to(ROOT)),
            "local_pic0_quotient": str(PIC0.relative_to(ROOT)),
            "h1_packet": str(H1.relative_to(ROOT)),
            "q79_selected_monad_difference_proof": str(Q79_PROOF),
            "q79_selector_obstruction": str(Q79_OBSTRUCTION),
            "q79_unselected_packet": str(Q79_PACKET),
        },
        "selected_candidate_if_terminal_lane_selected": {
            "label": selected_candidate["label"],
            "value": selected_candidate["value"],
            "double_value": selected_candidate["double_value"],
            "central_degree": selected_candidate["central_degree"],
            "dual_label": selected_candidate["dual_label"],
            "dual_printed_g_type_matches": selected_candidate["dual_matches_printed_g_type"],
        },
        "closed_now": {
            "pic0_removed_as_local_ordered_gate_blocker": pic0["closed_now"][
                "pic0_quotient_admissible_for_ordered_CW_H1_gate"
            ],
            "terminal_lane_conditional_uniqueness_imported": terminal["closed_now"][
                "conditional_uniqueness_inside_terminal_lane"
            ],
            "L3_minus_K2_forced_if_terminal_lane_selected": terminal_scan["target_matches"] == ["L3-K2"],
            "validator_passes_if_exact_source_axiom_added": axiom_validation["exit_code"] == 0
            and (axiom_validation["parsed_report"] or {}).get("status") == "PASS",
            "h1_ext_packet_ready_after_source_selection": h1["imported_h1_packet"]["h1"] == 8
            and h1["imported_h1_packet"]["nonzero_ext_class"] is True,
        },
        "not_closed": {
            "derived_terminal_monad_lane_selector": True,
            "base_order_breaking_source": base_swap_obstruction_survives,
            "typed_transition_or_rhoE_data": True,
            "same_source_D_E_dotD_Riesz_Green": True,
            "non_split_stability_or_HYM": True,
            "global_holonomy_sensitive_Pic0": True,
            "full_SM_closure": True,
        },
        "validator_tests": {
            "pic0_quotient_without_source_axiom": {
                "exit_code": pic0_validation["exit_code"],
                "status": (pic0_validation["parsed_report"] or {}).get("status"),
                "open_items": (pic0_validation["parsed_report"] or {}).get("open_items"),
            },
            "pic0_quotient_plus_terminal_source_axiom": candidate_routes[
                "R2_local_pic0_quotient_plus_terminal_arithmetic"
            ]["validator_if_axiom"],
        },
        "candidate_routes": candidate_routes,
        "minimal_remaining_source_theorem": {
            "name": "Base_Order_Breaking_Terminal_Lane_Source_v1",
            "must_prove": [
                "MTT supplies a source that selects terminal monad differences L_i-K2 as the visible ordered L lane",
                "the same source orders the base factors/sign convention so L3-K2, not its swapped/dual orbit, is selected",
                "typed transition/rhoE data or a same-source D_E/dotD/Riesz/Green packet binds the lane to physical operators",
            ],
            "after_success": [
                "rerun ordered-source validator as selected data",
                "promote h1=8 nonzero Ext packet",
                "continue to stability/HYM or Route-C and same-source response matrices",
            ],
        },
        "guardrails": {
            "claims_terminal_lane_selector_proved": False,
            "claims_base_order_source_proved": False,
            "claims_typed_transition_data_supplied": False,
            "claims_same_source_operator_packet_constructed": False,
            "claims_global_pic0_holonomy_resolved": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "honest_answer": (
            "After the local Pic0 quotient, the ordered-source gate is reduced to "
            "one exact missing theorem: a base-order-breaking source selecting the "
            "terminal monad lane. Current closed invariants cannot provide it, by "
            "the existing base-swap obstruction. If that source theorem is supplied, "
            "the strict ordered-source validator passes immediately."
        ),
    }

    if "--write-certificate" in sys.argv:
        OUTPUT_CERT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        OUTPUT_PACKET.write_text(json.dumps(if_axiom, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
