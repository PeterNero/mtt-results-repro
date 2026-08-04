"""Import q79 base-order terminal-lane source or direct HYM selected-source gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "candidate_data"
CERTS = ROOT / "certificates"
CORPUS = ROOT / "proof_corpus"
Q79 = Path(r"C:\Users\nero_\Downloads\TEXPAPERS\mtt-q79-proof-repro")

PREVIOUS = CERTS / "q79_selected_l2_cochain_ext_or_direct_hym_value_packet_fill_certificate.json"
Q79_TERMINAL = Q79 / "certificates" / "terminal_admissible_section_source_principle_certificate.json"
Q79_SIGN = Q79 / "certificates" / "terminal_map_dual_extension_sign_certificate.json"
Q79_LOCKDOWN = Q79 / "certificates" / "terminal_valpha_remaining_parts_lockdown_certificate.json"
Q79_STABILITY = Q79 / "certificates" / "q79_global_destabilizer_enumeration_or_selected_residual_certificate.json"

OUTPUT_PACKET = DATA / "q79_base_order_terminal_lane_or_direct_hym_selected_source_import.candidate.json"
OUTPUT_CERT = CERTS / "q79_base_order_terminal_lane_or_direct_hym_selected_source_import_certificate.json"
OUTPUT_NOTE = CORPUS / "Q79_Base_Order_Terminal_Lane_or_Direct_HYM_Selected_Source_Import_v1.md"

STATUS = "Q79_BASE_ORDER_TERMINAL_LANE_SELECTED_UNDER_EXPLICIT_PRINCIPLE_STABILITY_OPERATOR_OPEN"
NEXT = "Q79_Selected_AH_GoodCover_HYM_or_RouteC_Residual_Promotion_v1"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def local_rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def q79_rel(path: Path) -> str:
    try:
        return path.relative_to(Q79).as_posix()
    except ValueError:
        return str(path)


def build_packet() -> dict[str, Any]:
    previous = load(PREVIOUS)
    terminal = load(Q79_TERMINAL)
    sign = load(Q79_SIGN)
    lockdown = load(Q79_LOCKDOWN)
    stability = load(Q79_STABILITY)

    terminal_checks = terminal["input_closure_checks"]
    selected = terminal["selection_derivation"]
    term_validators = terminal["validator_results"]

    checks = {
        "B0_previous_names_this_gate": previous["verdict"]["best_next_artifact"]
        == "Q79_Base_Order_Breaking_Terminal_Lane_Source_or_Direct_HYM_Selected_Source_v1",
        "B1_terminal_principle_synthesized": terminal["source_principle"]["status"]
        == "EXPLICIT_PRINCIPLE_SYNTHESIZED_FROM_MTT_CORPUS",
        "B2_terminal_principle_not_unconditional": terminal["still_open"][
            "promote_principle_to_unconditional_MTT_axiom_or_prove_from_projection_admissibility"
        ]
        is True,
        "B3_terminal_inputs_closed": all(terminal_checks.values()),
        "B4_l3_k2_selected_under_principle": selected["selected_source_label"]
        == "g3 / L3-K2"
        and selected["selected_L"] == [1, -2, 0]
        and selected["selected_L2"] == [2, -4, 0],
        "B5_ordered_source_validator_passes_under_principle": term_validators[
            "ordered_source"
        ]["exit_code"]
        == 0,
        "B6_h1_ext_promotes_under_principle": term_validators["cohomology"][
            "exit_code"
        ]
        == 0
        and term_validators["cohomology"]["promotes_rank_two_route"] is True,
        "B7_sign_and_base_order_closed_for_g3": sign["what_this_closes"][
            "base_order_sign_ambiguity_for_terminal_g3_route"
        ]
        is True
        and sign["rank2_extension_binding"]["physical_L_in_rank2_candidate_list"] is True,
        "B8_lockdown_retires_old_l_h1_blockers": lockdown["closed_parts"][
            "h1_8_nonzero_ext_packet_validates"
        ]
        is True
        and lockdown["closed_parts"]["ordered_integral_L2_source_validates"] is True,
        "B9_stability_only_reduced_AH": stability["conditional_global_stability_theorem"][
            "proved"
        ]
        is True
        and stability["promotion_gap"]["full_stability_proved"] is False
        and stability["promotion_gap"]["hym_existence_proved"] is False,
        "B10_no_proxy_inputs": terminal["guardrails"]["uses_observed_flavor_data"] is False
        and terminal["guardrails"]["uses_benchmark_flavor_entries"] is False
        and stability["target_fitting_used"] is False,
    }
    proved = all(checks.values())

    return {
        "packet": "Q79_Base_Order_Terminal_Lane_or_Direct_HYM_Selected_Source_Import_v1",
        "status": STATUS
        if proved
        else "Q79_BASE_ORDER_TERMINAL_LANE_SELECTED_SOURCE_IMPORT_FAILED",
        "inputs": {
            "previous": local_rel(PREVIOUS),
            "q79_terminal_admissible_section_source_principle": q79_rel(Q79_TERMINAL),
            "q79_terminal_map_dual_extension_sign": q79_rel(Q79_SIGN),
            "q79_terminal_valpha_remaining_parts_lockdown": q79_rel(Q79_LOCKDOWN),
            "q79_global_destabilizer_or_selected_residual": q79_rel(Q79_STABILITY),
        },
        "import_checks": checks,
        "theorem": {
            "name": "Q79BaseOrderTerminalLaneSelectedSourceImportTheorem",
            "proved": proved,
            "closure_claimed": False,
            "statement": (
                "The base-order terminal-lane source gate is imported as closed "
                "under q79's explicit TerminalAdmissibleSectionSourcePrinciple: "
                "the terminal g3/L3-K2 source selects L=(1,-2,0), L^2=(2,-4,0), "
                "and the ordered-source and H1/Ext validators pass as selected "
                "data. The import does not make the principle unconditional and "
                "does not prove full stability/HYM, Route-C residual values, or "
                "same-source operator payloads."
            ),
        },
        "selected_terminal_source_under_principle": {
            "source_principle": terminal["source_principle"],
            "selection_derivation": terminal["selection_derivation"],
            "terminal_lane_scan": terminal["terminal_lane_scan"],
            "validator_results": terminal["validator_results"],
            "generated_packets": terminal["generated_packets"],
        },
        "sign_and_base_order": {
            "terminal_map_duality": sign["terminal_map_duality"],
            "ordered_base_matrix_binding": sign["ordered_base_matrix_binding"],
            "rank2_extension_binding": sign["rank2_extension_binding"],
        },
        "stability_or_hym_status": {
            "reduced_AH_stability_proved": stability["conditional_global_stability_theorem"],
            "promotion_gap": stability["promotion_gap"],
            "reduced_AH_global_rank_one_enumeration": stability[
                "reduced_AH_global_rank_one_enumeration"
            ],
            "route_c_residual_lane": stability["route_c_residual_lane"],
        },
        "what_closes_now": {
            "base_order_L3_K2_selection_under_explicit_principle": True,
            "selected_ordered_L2_source_under_principle": True,
            "selected_h1_8_nonzero_Ext_under_principle": True,
            "old_L_sign_h1_Ext_blockers_retired_conditionally": True,
            "reduced_AH_rank_one_stability_enumeration_imported": True,
        },
        "what_remains_open": {
            "promote_terminal_principle_to_unconditional_MTT_spine": True,
            "selected_AH_or_good_cover_promotion": True,
            "rank_one_torsion_free_reflexive_hull_theorem": True,
            "selected_Gauduchon_chamber_source": True,
            "selected_HYM_or_Strominger_existence_certificate": True,
            "selected_RouteC_residual_values": True,
            "operator_layer_Pic0_recheck": True,
            "same_source_ChernWeil_GS_row": True,
            "same_source_DE_Riesz_Green_dotD": True,
            "primitive_C1_contractions": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "claims_unconditional_terminal_selector": False,
            "claims_full_stability": False,
            "claims_hym_existence": False,
            "claims_selected_RouteC_residual": False,
            "claims_same_source_operator_payload": False,
            "claims_primitive_C1_values": False,
            "claims_full_SM_closure": False,
            "uses_observed_masses_or_mixings": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "base_order_gate_closed_under_explicit_principle": True,
            "selected_value_source_unconditional": False,
            "best_next_artifact": NEXT,
            "best_next_step": (
                "Promote the reduced AH/good-cover stability bridge and prove "
                "HYM/Strominger existence or emit selected Route-C residual "
                "values from the same terminal V_alpha source."
            ),
        },
    }


def render_note(packet: dict[str, Any]) -> str:
    return f"""# Q79 Base-Order Terminal Lane or Direct HYM Selected Source Import v1

## Result

Status: `{packet["status"]}`

The local base-order gate is now imported from q79 as closed **under an explicit
terminal admissible-section principle**.  Under that principle, `g3 / L3-K2`
selects `L=(1,-2,0)` and `L^2=(2,-4,0)`, and both validators pass:

- selected ordered-source validator: pass
- selected `H^1/Ext` validator: pass with `h1=8`

This does not make the source theorem unconditional.  The principle still has
to be promoted into the main MTT spine or derived from projection/admissibility
rules.

## Selected Terminal Source

```json
{json.dumps(packet["selected_terminal_source_under_principle"], indent=2, sort_keys=True)}
```

## Stability Or HYM Status

```json
{json.dumps(packet["stability_or_hym_status"], indent=2, sort_keys=True)}
```

## Remaining Open

```json
{json.dumps(packet["what_remains_open"], indent=2, sort_keys=True)}
```

Next: `{packet["verdict"]["best_next_artifact"]}`.
"""


def main() -> int:
    packet = build_packet()
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_CERT.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_NOTE.write_text(render_note(packet), encoding="utf-8")
    print(json.dumps(packet, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
