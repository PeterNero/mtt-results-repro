"""Attempt the remaining terminal-map source principle and base-order theorem.

This collects the now-closed local pieces and asks whether the actual selector
can be promoted from them.  The answer is intentionally strict: central
neutrality and local Pic0 are closed, but the terminal map source principle and
physical base-order binding still require typed transition/rhoE data or a
same-source operator response.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

CENTRAL_FILTER = CERTS / "central_circle_neutral_terminal_lane_filter_certificate.json"
ORDERED_REDUCTION = CERTS / "ordered_layer_terminal_lane_selector_reduction_certificate.json"
PIC0_QUOTIENT = CERTS / "ordered_layer_pic0_quotient_certificate.json"
MONAD_MAP_GATE = CERTS / "iwasawa_monad_map_data_gate_certificate.json"
MONAD_ROLE = CERTS / "iwasawa_monad_visible_source_role_certificate.json"
TYPED_MONAD = CERTS / "iwasawa_typed_monad_section_recovery_certificate.json"
RHOE_RECOVERY = CERTS / "iwasawa_rhoE_source_recovery_certificate.json"
RHOE_SEARCH = CERTS / "visible_rhoE_source_ansatz_search_certificate.json"
GAUDUCHON_WALL = CERTS / "selected_gauduchon_wall_radius_gate_certificate.json"
INTEGRAL_LIFT = CERTS / "visible_rank2_l2_integral_lift_source_gap_certificate.json"
SELECTOR_OBSTRUCTION = CERTS / "visible_rank2_l2_selector_obstruction_certificate.json"

CONSTANTS_SELECTOR = Path(
    r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-nonsm-constants-no-knob"
    r"\certificates\selected_terminal_monad_lane_source_selector_attempt_certificate.json"
)

OUT_CANDIDATE = CANDIDATES / "terminal_map_source_principle_base_order_attempt.candidate.json"
OUT_CERT = CERTS / "terminal_map_source_principle_base_order_attempt_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def analyze() -> dict[str, Any]:
    central = load(CENTRAL_FILTER)
    reduction = load(ORDERED_REDUCTION)
    pic0 = load(PIC0_QUOTIENT)
    monad_map = load(MONAD_MAP_GATE)
    monad_role = load(MONAD_ROLE)
    typed = load(TYPED_MONAD)
    rhoe = load(RHOE_RECOVERY)
    rhoe_search = load(RHOE_SEARCH)
    wall = load(GAUDUCHON_WALL)
    integral = load(INTEGRAL_LIFT)
    obstruction = load(SELECTOR_OBSTRUCTION)
    constants = load(CONSTANTS_SELECTOR)

    central_filter_closed = (
        central.get("status")
        == "CENTRAL_CIRCLE_NEUTRAL_TERMINAL_LANE_FILTER_PROVED_SELECTOR_OPEN"
        and central.get("what_this_closes", {}).get(
            "unique_zero_central_terminal_difference_is_L3_minus_K2"
        )
        is True
    )
    pic0_closed = (
        pic0.get("what_this_closes", {}).get(
            "pic0_quotient_for_ordered_chern_h1_curvature_layer"
        )
        is True
    )
    terminal_reduced = (
        reduction.get("status") == "ORDERED_LAYER_REDUCED_TO_TERMINAL_MONAD_LANE_SELECTOR"
    )
    monad_in_corpus = "0 -> K1" in monad_map.get("source_monad", {}).get("sequence", "")
    monad_typed_missing = typed.get("route_decision", {}).get("typed_monad_cech_can_close_now") is False
    rhoe_missing = rhoe.get("verdict", {}).get("rho_E_recovered_from_current_corpus") is False
    monad_not_visible_c2_source = (
        monad_role.get("what_this_closes", {}).get(
            "do_not_reuse_c2_zero_monad_as_c2_4_alpha1_source"
        )
        is True
    )
    current_invariants_no_go = obstruction.get("no_breaking_source_available") is True
    wall_open = (
        wall.get("status") == "GAUDUCHON_WALL_REDUCED_TO_RADIUS_RATIO_SOURCE_OPEN"
        and wall.get("still_open", {}).get("source_certified_r1_over_r2_sqrt2_wall")
        is True
    )
    integral_open = (
        integral.get("status") == "VISIBLE_RANK2_L2_INTEGRAL_LIFT_REDUCED_TO_SOURCE_CERTIFICATE"
        and integral.get("still_open", {}).get(
            "selected_ordered_integral_Cech_or_automorphy_source_for_L2_2_minus4_0"
        )
        is True
    )
    selected_response_primary = (
        rhoe_search.get("surviving_routes", {}).get("primary")
        == "selected D_E/dotD de_response promotion on the q79/F branch"
    )
    constants_agrees = (
        constants.get("status")
        == "TERMINAL_MONAD_LANE_SOURCE_SELECTOR_REDUCED_TO_BASE_ORDER_BREAKING_SOURCE_OPEN"
    )

    actual_selector_proved = (
        central_filter_closed
        and pic0_closed
        and terminal_reduced
        and monad_in_corpus
        and not monad_typed_missing
        and not rhoe_missing
        and not current_invariants_no_go
    )

    routes = {
        "R1_central_circle_filter": {
            "status": "CLOSED_SUBFILTER",
            "closes": "central-neutral terminal lane member is uniquely L3-K2",
            "can_prove_actual_selector": False,
        },
        "R2_local_pic0_quotient": {
            "status": "CLOSED_ORDERED_LAYER_ONLY",
            "closes": "Pic0 is quotient-equivalent for ordered Chern/H1/ordinary-curvature layer",
            "can_prove_actual_selector": False,
        },
        "R3_literal_terminal_monad_map": {
            "status": "BLOCKED_TYPED_MAPS_AND_VISIBLE_ROLE",
            "terminal_map_in_corpus": monad_in_corpus,
            "typed_sections_missing": monad_typed_missing,
            "monad_alone_wrong_visible_c2_role": monad_not_visible_c2_source,
            "can_prove_actual_selector": False,
        },
        "R4_current_closed_invariants": {
            "status": "REFUTED_BY_BASE_SWAP_OBSTRUCTION",
            "no_breaking_source_available": current_invariants_no_go,
            "can_prove_actual_selector": False,
        },
        "R5_selected_wall_base_order": {
            "status": "LIVE_SOURCE_RATIO_OPEN",
            "source_certified_target_wall_open": wall_open,
            "needed": "derive r1:r2=sqrt(2):1 or equivalent p1:p2=1:2 from selected source geometry",
            "can_prove_actual_selector": False,
        },
        "R6_integral_cech_or_de_lift": {
            "status": "LIVE_SOURCE_CERTIFICATE_ONLY_GAP",
            "ordered_integral_lift_open": integral_open,
            "needed": "selected ordered integral Cech/automorphy/D_E source for L^2=(2,-4,0)",
            "can_prove_actual_selector": False,
        },
        "R7_same_source_operator_response": {
            "status": "PRIMARY_OPEN_SELECTED_RESPONSE",
            "rhoE_recovered": not rhoe_missing,
            "selected_response_route_primary": selected_response_primary,
            "needed": "selected D_E/dotD/Riesz/Green packet that carries the same terminal-map/base-order source",
            "can_prove_actual_selector": False,
        },
        "R8_constants_repo_cross_check": {
            "status": "AGREES_BASE_ORDER_SOURCE_OPEN" if constants_agrees else "MISSING_OR_CHANGED",
            "can_prove_actual_selector": False,
        },
    }

    report = {
        "calculation": "TerminalMapSourcePrincipleBaseOrderAttempt",
        "status": (
            "TERMINAL_MAP_SOURCE_PRINCIPLE_BASE_ORDER_PROVED"
            if actual_selector_proved
            else "TERMINAL_MAP_SOURCE_PRINCIPLE_BASE_ORDER_REDUCED_TO_TYPED_OR_OPERATOR_SOURCE_OPEN"
        ),
        "generated_by": "scripts/attempt_terminal_map_source_principle_base_order.py",
        "inputs": {
            "central_filter": CENTRAL_FILTER.name,
            "ordered_reduction": ORDERED_REDUCTION.name,
            "pic0_quotient": PIC0_QUOTIENT.name,
            "monad_map_gate": MONAD_MAP_GATE.name,
            "monad_visible_role": MONAD_ROLE.name,
            "typed_monad_recovery": TYPED_MONAD.name,
            "rhoE_recovery": RHOE_RECOVERY.name,
            "rhoE_search": RHOE_SEARCH.name,
            "gauduchon_wall": GAUDUCHON_WALL.name,
            "integral_lift": INTEGRAL_LIFT.name,
            "selector_obstruction": SELECTOR_OBSTRUCTION.name,
            "constants_selector_attempt": str(CONSTANTS_SELECTOR),
        },
        "closed_now": {
            "central_filter_inside_terminal_lane": central_filter_closed,
            "ordered_layer_Pic0_quotient": pic0_closed,
            "ordered_layer_reduced_to_terminal_selector": terminal_reduced,
            "terminal_monad_sequence_present_in_corpus": monad_in_corpus,
            "constants_repo_agrees_base_order_source_open": constants_agrees,
        },
        "not_closed": {
            "terminal_map_source_principle": True,
            "physical_base_order_binding": True,
            "typed_terminal_map_sections": monad_typed_missing,
            "selected_rhoE_or_transition_data": rhoe_missing,
            "selected_wall_ratio_source": wall_open,
            "selected_integral_Cech_or_DE_lift": integral_open,
            "same_source_operator_response": True,
            "full_SM_closure": True,
        },
        "route_evaluation": routes,
        "minimal_remaining_packet": {
            "name": "Selected_Terminal_Map_Base_Order_Source_Packet.v1",
            "must_supply": [
                "source principle selecting the terminal monad map lane L_i-K2 as the visible ordered L source",
                "physical binding of monad base labels to Appell-Humbert/Cech order E1 positive and E2 negative",
                "typed transition/rhoE data or selected D_E/dotD/Riesz/Green response from the same source",
                "proof that the route is not merely the c2=0 matter monad reused as the visible c2=4 alpha1 source",
            ],
            "after_success": [
                "the central filter forces L3-K2=(1,-2,0)",
                "the already-generated terminal-lane selected packet passes the strict ordered-source validator",
                "the h1=8 Ext packet can be promoted and rerun as selected data",
            ],
        },
        "guardrails": {
            "claims_actual_terminal_map_selector_proved": actual_selector_proved,
            "claims_typed_sections_supplied": False,
            "claims_selected_rhoE_supplied": False,
            "claims_same_source_operator_response_constructed": False,
            "claims_full_SM_closure": False,
            "uses_observed_flavor_data": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "honest_answer": (
                "We have not proved the actual terminal-map selector.  What is "
                "newly sharp is the cutset: central neutrality and ordered-layer "
                "Pic0 are closed; the remaining selector requires a typed "
                "terminal-map/transition source or a same-source operator response "
                "that also binds the physical base order."
            )
        },
    }
    return report


def main() -> int:
    report = analyze()
    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "TerminalMapSourcePrincipleBaseOrderAttempt",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": rel(OUT_CANDIDATE),
        "inputs": report["inputs"],
        "closed_now": report["closed_now"],
        "not_closed": report["not_closed"],
        "route_evaluation": report["route_evaluation"],
        "minimal_remaining_packet": report["minimal_remaining_packet"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
