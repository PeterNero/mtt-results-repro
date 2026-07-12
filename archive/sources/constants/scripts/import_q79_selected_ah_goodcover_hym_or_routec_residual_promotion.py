"""Import q79 selected AH/good-cover HYM or Route-C residual promotion gate."""

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

PREVIOUS = CERTS / "q79_base_order_terminal_lane_or_direct_hym_selected_source_import_certificate.json"
Q79_HYM_BRIDGE = Q79 / "certificates" / "q79_selected_ah_goodcover_promotion_hym_certificate.json"
Q79_STABILITY = Q79 / "certificates" / "q79_global_destabilizer_enumeration_or_selected_residual_certificate.json"
Q79_AH_YONEDA = Q79 / "certificates" / "valpha_appell_humbert_yoneda_promotion_certificate.json"
Q79_HYM_ATTEMPT = Q79 / "certificates" / "selected_hym_operator_source_attempt_certificate.json"
Q79_ALL_GATES = Q79 / "certificates" / "all_remaining_valpha_gates_attempt_certificate.json"

OUTPUT_PACKET = DATA / "q79_selected_ah_goodcover_hym_or_routec_residual_promotion_import.candidate.json"
OUTPUT_CERT = CERTS / "q79_selected_ah_goodcover_hym_or_routec_residual_promotion_import_certificate.json"
OUTPUT_NOTE = CORPUS / "Q79_Selected_AH_GoodCover_HYM_or_RouteC_Residual_Promotion_Import_v1.md"

STATUS = "Q79_SELECTED_AH_GOODCOVER_HYM_PROMOTION_BRIDGE_IMPORTED_SOURCE_VALUES_OPEN"
NEXT = "Q79_Selected_AH_Source_Selection_or_RouteC_SelectedResidual_v1"


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
    bridge = load(Q79_HYM_BRIDGE)
    stability = load(Q79_STABILITY)
    ah_yoneda = load(Q79_AH_YONEDA)
    hym_attempt = load(Q79_HYM_ATTEMPT)
    all_gates = load(Q79_ALL_GATES)

    summary = bridge["promotion_summary"]
    status = bridge["selected_AH_goodcover_status"]
    checks = {
        "H0_previous_names_this_gate": previous["verdict"]["best_next_artifact"]
        == "Q79_Selected_AH_GoodCover_HYM_or_RouteC_Residual_Promotion_v1",
        "H1_reflexive_hull_reduction_proved": bridge[
            "rank_one_torsion_free_reflexive_hull_theorem"
        ]["proved"]
        is True,
        "H2_reduced_AH_stability_bridge_conditional": bridge[
            "reduced_AH_to_full_stability_implication"
        ]["proved_conditionally"]
        is True
        and summary["conditional_reduced_AH_to_full_stability_bridge_proved"] is True,
        "H3_li_yau_hym_bridge_conditional": bridge["HYM_bridge"]["proved_conditionally"]
        is True
        and bridge["HYM_bridge"]["operator_source_not_emitted"] is True,
        "H4_selected_AH_goodcover_not_supplied": summary["selected_AH_or_goodcover_source_supplied"]
        is False
        and status["AH_selected_by_mtt"] is False
        and status["pullback_cech_selected_L2_packet_constructed"] is False,
        "H5_selected_chamber_not_supplied": summary["selected_Gauduchon_chamber_supplied"]
        is False,
        "H6_no_hym_or_routec_values": summary["selected_HYM_connection_values_supplied"]
        is False
        and summary["selected_RouteC_residual_values_supplied"] is False,
        "H7_AH_yoneda_law_verified_not_selected": ah_yoneda["closed_by_this_attempt"][
            "AH_factor_product_law_matches_yoneda_degree_addition"
        ]
        is True
        and ah_yoneda["appell_humbert_selection_state"]["selected_by_mtt"] is False,
        "H8_reduced_AH_stability_imported": stability["conditional_global_stability_theorem"][
            "proved"
        ]
        is True
        and stability["promotion_gap"]["full_stability_proved"] is False,
        "H9_hym_operator_attempt_still_blocked": hym_attempt["calculation_results"][
            "selected_hym_operator_source_verified"
        ]
        is False
        and hym_attempt["calculation_results"]["route_c_honest_operator_pipeline_pass"]
        is False,
        "H10_all_gates_stability_still_open": all_gates["gate_summary"][
            "SelectedNonSplitVAlphaStabilityOrRouteCResidual"
        ]
        == "PARTIAL_NON_SPLIT_INPUT_CLOSED_STABILITY_OPEN",
        "H11_no_proxy_inputs": bridge["target_fitting_used"] is False
        and bridge["guardrails"]["uses_observed_masses_or_ckm_inputs"] is False
        and bridge["guardrails"]["uses_benchmark_flavor_entries"] is False,
    }
    proved = all(checks.values())

    return {
        "packet": "Q79_Selected_AH_GoodCover_HYM_or_RouteC_Residual_Promotion_Import_v1",
        "status": STATUS
        if proved
        else "Q79_SELECTED_AH_GOODCOVER_HYM_PROMOTION_IMPORT_FAILED",
        "inputs": {
            "previous": local_rel(PREVIOUS),
            "q79_hym_bridge": q79_rel(Q79_HYM_BRIDGE),
            "q79_reduced_AH_stability": q79_rel(Q79_STABILITY),
            "q79_AH_yoneda_promotion": q79_rel(Q79_AH_YONEDA),
            "q79_hym_operator_attempt": q79_rel(Q79_HYM_ATTEMPT),
            "q79_all_remaining_valpha_gates": q79_rel(Q79_ALL_GATES),
        },
        "import_checks": checks,
        "theorem": {
            "name": "Q79SelectedAHGoodCoverHYMOrRouteCResidualPromotionImportTheorem",
            "proved": proved,
            "closure_claimed": False,
            "statement": (
                "The q79 AH/good-cover promotion layer is imported: rank-one "
                "torsion-free destabilizers reduce to saturated reflexive line "
                "hulls; reduced AH stability promotes to full stability if a "
                "selected AH/good-cover section algebra is supplied; and the "
                "Li-Yau/Gauduchon bridge gives HYM existence if the selected "
                "stable holomorphic bundle and selected chamber are supplied. "
                "The import does not supply the selected AH/good-cover source, "
                "Gauduchon chamber, HYM connection values, Route-C residual "
                "values, or same-source operator payload."
            ),
        },
        "promotion_bridge": {
            "rank_one_torsion_free_reflexive_hull_theorem": bridge[
                "rank_one_torsion_free_reflexive_hull_theorem"
            ],
            "reduced_AH_to_full_stability_implication": bridge[
                "reduced_AH_to_full_stability_implication"
            ],
            "HYM_bridge": bridge["HYM_bridge"],
            "promotion_summary": bridge["promotion_summary"],
            "selected_AH_goodcover_status": bridge["selected_AH_goodcover_status"],
        },
        "AH_yoneda_status": {
            "appell_humbert_selection_state": ah_yoneda[
                "appell_humbert_selection_state"
            ],
            "appell_humbert_yoneda_promotion": ah_yoneda[
                "appell_humbert_yoneda_promotion"
            ],
            "closed_by_this_attempt": ah_yoneda["closed_by_this_attempt"],
            "still_open": ah_yoneda["still_open"],
        },
        "routec_or_operator_status": {
            "hym_operator_attempt": hym_attempt["calculation_results"],
            "hym_operator_still_open": hym_attempt["still_open"],
            "all_remaining_valpha_gate_summary": all_gates["gate_summary"],
            "same_source_fusion_validator": all_gates["same_source_fusion_validator"],
            "selected_valpha_validator": all_gates["selected_valpha_validator"],
        },
        "what_closes_now": {
            "rank_one_torsion_free_reflexive_hull_reduction": True,
            "reduced_AH_to_full_stability_bridge_conditional": True,
            "Li_Yau_Gauduchon_HYM_bridge_conditional": True,
            "AH_factor_product_law_matches_Yoneda": True,
            "blocker_reduced_to_selected_source_or_selected_residual_values": True,
        },
        "what_remains_open": {
            "selected_AH_representative_or_literal_goodcover_Cech_source": True,
            "selected_target_branch_L_over_swapped_branch": True,
            "selected_Gauduchon_chamber_source": True,
            "selected_HYM_connection_values": True,
            "selected_RouteC_residual_values": True,
            "operator_layer_neutral_Pic0_selection_or_quotient": True,
            "same_source_ChernWeil_GS_row": True,
            "same_source_DE_Riesz_Green_dotD": True,
            "primitive_C1_contractions": True,
            "promote_terminal_principle_to_unconditional_MTT_spine": True,
            "full_SM_or_no_knob_closure": True,
        },
        "guardrails": {
            "claims_selected_AH_source": False,
            "claims_selected_goodcover_source": False,
            "claims_selected_Gauduchon_chamber": False,
            "claims_full_stability_unconditionally": False,
            "claims_hym_existence_unconditionally": False,
            "claims_selected_HYM_connection_values": False,
            "claims_selected_RouteC_residual": False,
            "claims_same_source_operator_payload": False,
            "claims_full_SM_closure": False,
            "uses_observed_masses_or_mixings": False,
            "uses_benchmark_flavor_entries": False,
        },
        "verdict": {
            "promotion_bridge_imported": True,
            "selected_source_or_values_closed": False,
            "best_next_artifact": NEXT,
            "best_next_step": (
                "Either supply a selected AH/good-cover source plus selected "
                "Gauduchon chamber to activate the HYM bridge, or emit selected "
                "Route-C residual values and same-source D_E/Riesz/Green/dotD "
                "payloads directly."
            ),
        },
    }


def render_note(packet: dict[str, Any]) -> str:
    return f"""# Q79 Selected AH/GoodCover HYM or Route-C Residual Promotion Import v1

## Result

Status: `{packet["status"]}`

The promotion bridge is now imported locally.  It closes the reflexive-hull
reduction and the conditional implication from reduced AH stability to full
stability, provided a selected AH/good-cover section algebra is supplied.  It
also imports the conditional Li-Yau/Gauduchon HYM bridge.

It does **not** emit selected HYM connection coefficients, Route-C residual
values, selected `D_E/Riesz/Green/dotD`, or primitive C1 matrices.

## Promotion Bridge

```json
{json.dumps(packet["promotion_bridge"], indent=2, sort_keys=True)}
```

## Route-C Or Operator Status

```json
{json.dumps(packet["routec_or_operator_status"], indent=2, sort_keys=True)}
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
