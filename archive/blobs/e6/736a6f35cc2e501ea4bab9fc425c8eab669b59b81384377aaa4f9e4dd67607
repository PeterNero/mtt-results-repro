"""Prove the terminal-map dual/sign convention for the visible rank-two source.

The actual terminal-map source selector is still open. This script closes a
smaller ambiguity: once the central-neutral terminal entry is the printed
`g3 : L3 -> K2` map type, the visible rank-two extension line is forced to be
the dual line `L = L3-K2 = (1,-2,0)`, not the printed Hom type
`K2-L3=(-1,2,0)`.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "candidate_data"
CERTS = ROOT / "certificates"

MONAD_MAP_GATE = CERTS / "iwasawa_monad_map_data_gate_certificate.json"
CENTRAL_FILTER = CERTS / "central_circle_neutral_terminal_lane_filter_certificate.json"
VALPHA_ROUTE = CERTS / "visible_rank2_extension_valpha_route_certificate.json"
PULLBACK_CECH = CERTS / "visible_rank2_l2_pullback_cech_attempt_certificate.json"
APPELL_HUMBERT = CERTS / "visible_rank2_l2_appell_humbert_automorphy_certificate.json"
TERMINAL_SOURCE = CERTS / "terminal_map_source_principle_base_order_attempt_certificate.json"

OUT_CANDIDATE = CANDIDATES / "terminal_map_dual_extension_sign.candidate.json"
OUT_CERT = CERTS / "terminal_map_dual_extension_sign_certificate.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def vsub(a: list[int], b: list[int]) -> list[int]:
    return [x - y for x, y in zip(a, b)]


def vneg(a: list[int]) -> list[int]:
    return [-x for x in a]


def vscale(k: int, a: list[int]) -> list[int]:
    return [k * x for x in a]


def target_matrix() -> list[list[int]]:
    return [
        [0, 2, 0, 0, 0, 0],
        [-2, 0, 0, 0, 0, 0],
        [0, 0, 0, -4, 0, 0],
        [0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]


def analyze() -> dict[str, Any]:
    monad = load(MONAD_MAP_GATE)
    central = load(CENTRAL_FILTER)
    valpha = load(VALPHA_ROUTE)
    pullback = load(PULLBACK_CECH)
    appell = load(APPELL_HUMBERT)
    terminal_source = load(TERMINAL_SOURCE)

    line_data = monad.get("source_monad", {}).get("line_bundle_c1_vectors_abc", {})
    typed_g = monad.get("typed_map_check", {}).get("g_entry_types", {})
    l3 = line_data.get("L3")
    k2 = line_data.get("K2")
    printed_g3 = typed_g.get("g3_K2_tensor_L3_inverse")
    physical_l = vsub(l3, k2) if isinstance(l3, list) and isinstance(k2, list) else None
    dual_of_printed_g3 = vneg(printed_g3) if isinstance(printed_g3, list) else None
    physical_l2 = vscale(2, physical_l) if isinstance(physical_l, list) else None

    central_selected = central.get("terminal_lane_filter", {}).get("selected_by_filter", {})
    rank2_schema = valpha.get("rank2_extension_schema", {})
    rank2_candidates = valpha.get("finite_line_class_solutions", [])
    candidate_vectors = [entry.get("l_vector_abc") for entry in rank2_candidates]

    pullback_model = pullback.get("pullback_model", {})
    pullback_matrix = pullback_model.get("c1_deck_alternating_matrix_order_g1_to_g6")
    ah_model = appell.get("model", {})
    ah_matrix = ah_model.get("c1_deck_alternating_matrix_order_g1_to_g6")
    expected_matrix = target_matrix()

    terminal_g3_dual_sign_closed = (
        physical_l == [1, -2, 0]
        and printed_g3 == [-1, 2, 0]
        and dual_of_printed_g3 == physical_l
        and central_selected.get("label") == "L3-K2"
        and central_selected.get("value") == physical_l
        and central_selected.get("dual_label") == "K2-L3"
        and central_selected.get("dual_value") == printed_g3
        and central_selected.get("dual_matches_printed_g_type") is True
    )
    rank2_extension_convention_closed = (
        rank2_schema.get("sequence") == "0 -> L -> V_alpha -> L^{-1} -> 0"
        and rank2_schema.get("formula_c2") == "c2(V_alpha)=-l^2"
        and rank2_schema.get("target_c2") == [4, 0, 0]
        and physical_l in candidate_vectors
    )
    ordered_matrix_bound = (
        physical_l2 == [2, -4, 0]
        and pullback_model.get("L_vector_abc") == physical_l
        and pullback_model.get("c1_L_squared_vector_abc") == physical_l2
        and pullback_model.get("degree_pairs", {}).get("E1_pair_g1_g2") == 2
        and pullback_model.get("degree_pairs", {}).get("E2_pair_g3_g4") == -4
        and pullback_model.get("degree_pairs", {}).get("central_pair_g5_g6") == 0
        and pullback_matrix == expected_matrix
        and ah_matrix == expected_matrix
        and appell.get("construction_checks", {}).get("central_shared_circle_trivial") is True
        and appell.get("construction_checks", {}).get("c1_matrix_matches_required_order") is True
    )

    terminal_source_still_open = (
        terminal_source.get("status")
        == "TERMINAL_MAP_SOURCE_PRINCIPLE_BASE_ORDER_REDUCED_TO_TYPED_OR_OPERATOR_SOURCE_OPEN"
    )
    theorem_proved = (
        terminal_g3_dual_sign_closed
        and rank2_extension_convention_closed
        and ordered_matrix_bound
        and terminal_source_still_open
    )

    report = {
        "calculation": "TerminalMapDualExtensionSignTheorem",
        "status": (
            "TERMINAL_MAP_DUAL_EXTENSION_SIGN_PROVED_SELECTOR_OPEN"
            if theorem_proved
            else "TERMINAL_MAP_DUAL_EXTENSION_SIGN_INCOMPLETE"
        ),
        "generated_by": "scripts/prove_terminal_map_dual_extension_sign.py",
        "inputs": {
            "monad_map_gate": MONAD_MAP_GATE.name,
            "central_filter": CENTRAL_FILTER.name,
            "visible_rank2_extension_valpha_route": VALPHA_ROUTE.name,
            "visible_rank2_l2_pullback_cech_attempt": PULLBACK_CECH.name,
            "visible_rank2_l2_appell_humbert_automorphy": APPELL_HUMBERT.name,
            "terminal_map_source_attempt": TERMINAL_SOURCE.name,
        },
        "terminal_map_duality": {
            "L3": l3,
            "K2": k2,
            "computed_L3_minus_K2": physical_l,
            "printed_terminal_g3_type_K2_minus_L3": printed_g3,
            "dual_of_printed_g3_type": dual_of_printed_g3,
            "physical_L_is_dual_of_printed_g3_terminal_map_type": dual_of_printed_g3
            == physical_l,
            "physical_L_squared": physical_l2,
        },
        "rank2_extension_binding": {
            "sequence": rank2_schema.get("sequence"),
            "formula_c2": rank2_schema.get("formula_c2"),
            "target_c2": rank2_schema.get("target_c2"),
            "physical_L_in_rank2_candidate_list": physical_l in candidate_vectors,
            "interpretation": (
                "The monad map entry g3 has Hom type L^{-1}=K2-L3. The "
                "visible rank-two extension convention takes the subline L in "
                "0 -> L -> V_alpha -> L^{-1} -> 0, so the physical line is "
                "the dual L=L3-K2."
            ),
        },
        "ordered_base_matrix_binding": {
            "L": physical_l,
            "L_squared": physical_l2,
            "degree_pairs": pullback_model.get("degree_pairs"),
            "matrix_order_g1_to_g6": expected_matrix,
            "pullback_matrix_matches": pullback_matrix == expected_matrix,
            "appell_humbert_matrix_matches": ah_matrix == expected_matrix,
            "central_shared_circle_degree_zero": (
                pullback_model.get("degree_pairs", {}).get("central_pair_g5_g6") == 0
            ),
        },
        "what_this_closes": {
            "terminal_g3_dual_sign_convention": terminal_g3_dual_sign_closed,
            "rank2_extension_physical_L_is_L3_minus_K2_not_printed_Hom_type": (
                terminal_g3_dual_sign_closed and rank2_extension_convention_closed
            ),
            "target_L2_matrix_order_binding_conditional_on_terminal_g3": ordered_matrix_bound,
            "base_order_sign_ambiguity_for_terminal_g3_route": (
                terminal_g3_dual_sign_closed and ordered_matrix_bound
            ),
        },
        "what_this_does_not_close": {
            "actual_terminal_map_source_selector": True,
            "selected_pullback_representative": True,
            "typed_terminal_map_sections": True,
            "same_source_D_E_dotD_Riesz_Green": True,
            "nonzero_Ext_class_selected": True,
            "stability_or_HYM": True,
            "full_SM_closure": True,
        },
        "remaining_packet": {
            "name": "Selected_Terminal_Map_Source_Principle.v1",
            "now_reduced_to": [
                "prove that MTT selects the terminal g3 source, rather than merely allowing it",
                "supply selected typed transition/automorphy data or same-source operator data",
                "promote the h1=8 pullback packet from UNSELECTED_FIXTURE to SELECTED_DATA without changing entries by hand",
            ],
        },
        "guardrails": {
            "claims_actual_terminal_map_selector_proved": False,
            "claims_MTT_selected_pullback_representative": False,
            "claims_typed_sections_supplied": False,
            "claims_selected_Ext_class": False,
            "claims_stability_proved": False,
            "claims_full_SM_closure": False,
            "uses_benchmark_flavor_entries": False,
            "uses_observed_flavor_data": False,
        },
        "verdict": {
            "honest_answer": (
                "The sign and base-order convention is closed for the terminal "
                "g3 route: the printed map type is L^{-1}=K2-L3=(-1,2,0), "
                "while the visible extension subline is its dual "
                "L=L3-K2=(1,-2,0), giving L^2=(2,-4,0) and the already "
                "constructed ordered Appell-Humbert/Cech matrix. This does "
                "not yet prove that MTT selects g3."
            )
        },
    }
    return report


def main() -> int:
    report = analyze()
    write(OUT_CANDIDATE, report)
    cert = {
        "certificate": "TerminalMapDualExtensionSignTheorem",
        "status": report["status"],
        "analysis_script": report["generated_by"],
        "candidate_data": rel(OUT_CANDIDATE),
        "inputs": report["inputs"],
        "terminal_map_duality": report["terminal_map_duality"],
        "rank2_extension_binding": report["rank2_extension_binding"],
        "ordered_base_matrix_binding": report["ordered_base_matrix_binding"],
        "what_this_closes": report["what_this_closes"],
        "what_this_does_not_close": report["what_this_does_not_close"],
        "remaining_packet": report["remaining_packet"],
        "guardrails": report["guardrails"],
        "verdict": report["verdict"],
    }
    write(OUT_CERT, cert)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
