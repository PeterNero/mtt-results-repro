"""Reduce the V_alpha source path after the terminal g3 sign theorem.

The older branch-orientation gates treated a source-certified Gauduchon wall or
an integral lift as the first way to distinguish L=(1,-2,0) from the swapped
branch.  The terminal-map dual theorem changes the critical path for the
terminal-g3 route: conditional on selecting the terminal g3 source, the sign and
ordered L^2 matrix are already fixed.  The remaining problem is the selected
source itself, plus Ext/stability/operator data from that same source.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

TERMINAL_SIGN = CERTS / "terminal_map_dual_extension_sign_certificate.json"
BRANCH_GATE = CERTS / "selected_pullback_l2_branch_orientation_source_gate_certificate.json"
WALL_GATE = CERTS / "selected_gauduchon_wall_radius_gate_certificate.json"
VALPHA_LEDGER = CERTS / "visible_valpha_chern_bianchi_source_packet_candidates_certificate.json"
TERMINAL_SOURCE = CERTS / "terminal_map_source_principle_base_order_attempt_certificate.json"
VALPHA_SUFFICIENCY = CERTS / "selected_valpha_operator_source_sufficiency_certificate.json"

OUT_CANDIDATE = CANDIDATES / "terminal_g3_valpha_source_path_reduction.candidate.json"
OUT_CERT = CERTS / "terminal_g3_valpha_source_path_reduction_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def analyze() -> dict[str, Any]:
    terminal_sign = load(TERMINAL_SIGN)
    branch = load(BRANCH_GATE)
    wall = load(WALL_GATE)
    ledger = load(VALPHA_LEDGER)
    terminal_source = load(TERMINAL_SOURCE)
    sufficiency = load(VALPHA_SUFFICIENCY)

    terminal_closes = terminal_sign.get("what_this_closes", {})
    branch_gate = branch.get("finite_qutrit_gate", {})
    wall_status = wall.get("status")
    ledger_best = ledger.get("best_current_route", {})
    ledger_calc = ledger.get("calculation_results", {})
    suff_closes = sufficiency.get("what_this_closes", {})

    terminal_g3_fixes_l = (
        terminal_sign.get("status") == "TERMINAL_MAP_DUAL_EXTENSION_SIGN_PROVED_SELECTOR_OPEN"
        and terminal_closes.get("terminal_g3_dual_sign_convention") is True
        and terminal_closes.get("target_L2_matrix_order_binding_conditional_on_terminal_g3")
        is True
    )
    finite_only_ambiguous = (
        branch.get("status") == "PULLBACK_L2_BRANCH_ORIENTATION_GATE_REDUCED_TO_WALL_OR_INTEGRAL_LIFT"
        and branch_gate.get("target_and_swapped_same_finite_signature") is True
        and branch_gate.get("distinguishes_target_from_swapped") is False
    )
    wall_was_open_selector = wall_status == "GAUDUCHON_WALL_REDUCED_TO_RADIUS_RATIO_SOURCE_OPEN"
    terminal_source_open = (
        terminal_source.get("status")
        == "TERMINAL_MAP_SOURCE_PRINCIPLE_BASE_ORDER_REDUCED_TO_TYPED_OR_OPERATOR_SOURCE_OPEN"
    )
    valpha_primary_is_terminal_l = (
        ledger.get("status") == "VISIBLE_VALPHA_CHERN_BIANCHI_SOURCE_PACKET_CANDIDATES_BUILT_SOURCE_OPEN"
        and ledger_best.get("candidate_id") == "rank2_non_split_extension_preferred_L_1_-2_0"
        and ledger_calc.get("terminal_g3_sign_order_closed_before_source_selection") is True
    )
    downstream_sufficient = (
        sufficiency.get("status")
        == "SELECTED_VALPHA_OPERATOR_SOURCE_CONDITIONAL_SUFFICIENCY_PROVED_SOURCE_OPEN"
        and suff_closes.get("selected_valpha_source_packet_sufficiency_condition") is True
        and suff_closes.get("downstream_validator_stack_has_no_hidden_matrix_defect") is True
    )

    reduction_valid = (
        terminal_g3_fixes_l
        and finite_only_ambiguous
        and wall_was_open_selector
        and terminal_source_open
        and valpha_primary_is_terminal_l
        and downstream_sufficient
    )

    report = {
        "calculation": "TerminalG3VAlphaSourcePathReduction",
        "status": (
            "TERMINAL_G3_VALPHA_SOURCE_PATH_REDUCED_TO_SELECTED_SOURCE_PACKET_OPEN"
            if reduction_valid
            else "TERMINAL_G3_VALPHA_SOURCE_PATH_REDUCTION_INCOMPLETE"
        ),
        "generated_by": "scripts/reduce_terminal_g3_valpha_source_path.py",
        "inputs": {
            "terminal_map_dual_extension_sign": TERMINAL_SIGN.name,
            "selected_pullback_l2_branch_orientation_source_gate": BRANCH_GATE.name,
            "selected_gauduchon_wall_radius_gate": WALL_GATE.name,
            "visible_valpha_chern_bianchi_source_packet_candidates": VALPHA_LEDGER.name,
            "terminal_map_source_principle_base_order_attempt": TERMINAL_SOURCE.name,
            "selected_valpha_operator_source_sufficiency": VALPHA_SUFFICIENCY.name,
        },
        "route_reclassification": {
            "finite_qutrit_route": {
                "still_ambiguous_for_finite_only_selection": finite_only_ambiguous,
                "reason": "mod 3 both target and swapped branches have image (1,1)",
            },
            "terminal_g3_route": {
                "branch_sign_and_order_fixed": terminal_g3_fixes_l,
                "selected_L": [1, -2, 0],
                "selected_L2": [2, -4, 0],
                "reason": "the printed g3 Hom type is K2-L3, so the rank-two extension line is the dual L3-K2",
            },
            "gauduchon_wall_route": {
                "old_role": "candidate branch selector p1:p2=1:2",
                "new_role": "stability/HYM chamber witness after terminal g3 fixes L",
                "wall_search_no_longer_primary_for_sign": terminal_g3_fixes_l
                and wall_was_open_selector,
                "target_wall_p": [1, 2, 1],
                "target_radius_ratio": "r1:r2=sqrt(2):1",
            },
        },
        "critical_path_now": {
            "name": "Selected_Terminal_G3_VAlpha_Source.v1",
            "must_supply": [
                "MTT source principle selecting the terminal g3 source rather than merely allowing it",
                "selected typed Cech/Appell-Humbert or equivalent operator source for L=(1,-2,0)",
                "Pic0 rule: neutral character selected, specific flat character selected, or Pic0 quotient proved valid for the operator layer",
                "selected h1=8 L^2 cohomology packet with closed non-exact Ext vector",
                "non-split stability/HYM or Route-C residual from the same source",
                "same-source visible Chern-Weil/Green-Schwarz row, D_E, Riesz/Green, dotD, and primitive C1 contractions",
            ],
            "can_reuse": [
                "terminal g3 dual sign/order theorem",
                "pullback Cech h1=8 fixture as arithmetic template",
                "Appell-Humbert L^2 matrix",
                "selected V_alpha operator-source sufficiency validator stack",
            ],
            "cannot_reuse_as_proof": [
                "finite qutrit orientation alone",
                "equal-radius Iwasawa specialization",
                "split abelian row as selected HYM source",
                "hypothetical selected flags from sufficiency tests",
            ],
        },
        "calculation_results": {
            "branch_sign_ambiguity_closed_for_terminal_g3_route": terminal_g3_fixes_l,
            "finite_qutrit_route_remains_ambiguous_if_used_alone": finite_only_ambiguous,
            "gauduchon_wall_reclassified_as_stability_chamber_witness": terminal_g3_fixes_l
            and wall_was_open_selector,
            "sqrt2_radius_wall_no_longer_required_to_choose_sign_on_terminal_g3_path": (
                terminal_g3_fixes_l and wall_was_open_selector
            ),
            "actual_terminal_g3_source_selection_still_open": terminal_source_open,
            "selected_valpha_downstream_stack_conditionally_sufficient": downstream_sufficient,
        },
        "what_this_closes": {
            "do_not_search_for_gauduchon_wall_as_primary_sign_selector_on_terminal_g3_path": reduction_valid,
            "terminal_g3_path_now_has_single_named_source_packet": reduction_valid,
            "old_branch_orientation_gate_reconciled_with_new_terminal_sign_theorem": reduction_valid,
            "wall_route_retained_only_for_stability_or_nonterminal_finite_lift_paths": reduction_valid,
        },
        "still_open": {
            "actual_terminal_g3_source_selector": True,
            "selected_L2_cohomology_packet": True,
            "selected_nonzero_Ext_class": True,
            "operator_layer_Pic0_rule": True,
            "non_split_stability_or_HYM": True,
            "same_source_Chern_Weil_GS_DE_Riesz_Green_dotD": True,
            "primitive_C1_contractions": True,
            "full_SM_closure": True,
        },
        "guardrails": {
            "claims_actual_terminal_g3_source_selected": False,
            "claims_selected_L2_cohomology_packet": False,
            "claims_nonzero_Ext_selected": False,
            "claims_stability_or_HYM_proved": False,
            "claims_selected_D_E_dotD_constructed": False,
            "claims_full_SM_closure": False,
            "uses_benchmark_flavor_entries": False,
            "uses_observed_flavor_data": False,
        },
        "verdict": {
            "honest_answer": (
                "The solution path is now cleaner: for the terminal-g3 route, "
                "branch sign/order is already fixed by the dual-extension theorem. "
                "The sqrt(2) Gauduchon wall should no longer be treated as the "
                "primary sign selector; it is a stability/HYM chamber witness or a "
                "fallback for nonterminal finite-lift routes. The hard remaining "
                "object is one selected terminal-g3 V_alpha source packet."
            )
        },
    }
    return report


def main() -> int:
    report = analyze()
    write(OUT_CANDIDATE, report)
    certificate = {
        "certificate": "TerminalG3VAlphaSourcePathReduction",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": rel(OUT_CANDIDATE),
        "inputs": report["inputs"],
        "route_reclassification": report["route_reclassification"],
        "critical_path_now": report["critical_path_now"],
        "calculation_results": report["calculation_results"],
        "what_this_closes": report["what_this_closes"],
        "still_open": report["still_open"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, certificate)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"].endswith("_OPEN") else 1


if __name__ == "__main__":
    raise SystemExit(main())
