"""Import q79 global destabilizer, AH promotion, and monad-source chain."""

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

PREVIOUS = DATA / "q79_weylpair_sector_charge_samesource_nogo_chain_import.candidate.json"
GLOBAL_DESTAB = Q79 / "certificates" / "q79_global_destabilizer_enumeration_or_selected_residual_certificate.json"
AH_HYM = Q79 / "certificates" / "q79_selected_ah_goodcover_promotion_hym_certificate.json"
AH_SOURCE = Q79 / "certificates" / "q79_ah_source_selection_or_routec_residual_reduction_certificate.json"
MONAD_L2 = Q79 / "certificates" / "q79_selected_monad_l2_source_and_operatorpic0_or_routec_residual_certificate.json"

OUTPUT_PACKET = DATA / "q79_global_destabilizer_ah_monad_source_chain_import.candidate.json"
OUTPUT_CERT = CERTS / "q79_global_destabilizer_ah_monad_source_chain_import_certificate.json"
OUTPUT_NOTE = CORPUS / "Q79_Global_Destabilizer_AH_Monad_Source_Chain_Import_v1.md"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_packet() -> dict[str, Any]:
    previous = load_json(PREVIOUS)
    global_destab = load_json(GLOBAL_DESTAB)
    ah_hym = load_json(AH_HYM)
    ah_source = load_json(AH_SOURCE)
    monad_l2 = load_json(MONAD_L2)

    chain = {
        "previous_chain": {
            "status": previous["status"],
            "next_required_artifact": previous["verdict"]["next_required_artifact"],
        },
        "global_destabilizer_enumeration": {
            "status": global_destab["status"],
            "closure_claimed": global_destab["closure_claimed"],
            "reduced_AH_model_stability_proved": global_destab["what_closes_now"][
                "reduced_AH_model_stability_proved_from_prior_yoneda_obstructions"
            ],
            "unbounded_reduced_AH_rank_one_line_enumeration": global_destab[
                "what_closes_now"
            ]["unbounded_reduced_AH_rank_one_line_enumeration"],
            "claims_full_stability": global_destab["guardrails"][
                "claims_full_stability"
            ],
            "selected_AH_or_goodcover_open": global_destab["what_remains_open"][
                "selected_AH_representative_or_literal_good_cover_table"
            ],
            "selected_RouteC_residual_values_open": global_destab[
                "what_remains_open"
            ]["selected_RouteC_residual_values"],
            "next_required_artifact": global_destab["next_required_artifact"],
        },
        "ah_goodcover_promotion_hym_bridge": {
            "status": ah_hym["status"],
            "closure_claimed": ah_hym["closure_claimed"],
            "reflexive_hull_reduction_proved": ah_hym["what_closes_now"][
                "rank_one_torsion_free_destabilizer_reduces_to_saturated_reflexive_line_hull"
            ],
            "conditional_HYM_bridge_ready": ah_hym["what_closes_now"][
                "Li_Yau_Gauduchon_HYM_bridge_ready_if_selected_stability_and_chamber_supplied"
            ],
            "claims_hym_unconditionally": ah_hym["guardrails"][
                "claims_hym_existence_unconditionally"
            ],
            "selected_AH_source_open": ah_hym["what_remains_open"][
                "selected_AH_representative_or_literal_goodcover_Cech_source"
            ],
            "selected_Gauduchon_chamber_open": ah_hym["what_remains_open"][
                "selected_Gauduchon_chamber_source"
            ],
            "next_required_artifact": ah_hym["next_required_artifact"],
        },
        "ah_source_or_routec_residual_reduction": {
            "status": ah_source["status"],
            "closure_claimed": ah_source["closure_claimed"],
            "ah_goodcover_equivalence_closed": ah_source["what_closes_now"][
                "AH_or_goodcover_selection_reduced_to_single_source_class_selection"
            ],
            "selected_AH_reduced_to_terminal_lane": ah_source["what_closes_now"][
                "selected_AH_source_reduced_to_terminal_lane_selector_plus_operator_pic0_recheck"
            ],
            "terminal_lane_selector_open": ah_source["what_remains_open"][
                "selected_terminal_monad_lane_L3_minus_K2_source_selector"
            ],
            "operator_pic0_open": ah_source["what_remains_open"][
                "operator_layer_Pic0_selection_or_quotient"
            ],
            "selected_RouteC_residual_values_open": ah_source["what_remains_open"][
                "selected_RouteC_residual_values"
            ],
            "next_required_artifact": ah_source["next_required_artifact"],
        },
        "selected_monad_l2_source_operatorpic0_or_routec_residual": {
            "status": monad_l2["status"],
            "closure_claimed": monad_l2["closure_claimed"],
            "selected_monad_L2_source_closed_under_explicit_principle": monad_l2[
                "what_closes_now"
            ][
                "selected_monad_difference_L2_source_under_explicit_terminal_section_principle"
            ],
            "selected_h1_8_nonzero_Ext_input": monad_l2["what_closes_now"][
                "selected_h1_8_nonzero_Ext_input"
            ],
            "operator_arithmetic_reduced_to_source_provenance_flags": monad_l2[
                "what_closes_now"
            ]["routec_operator_arithmetic_reduced_to_selected_source_provenance_flags"],
            "claims_unconditional_terminal_section_principle": monad_l2[
                "guardrails"
            ]["claims_unconditional_terminal_section_principle_in_current_corpus"],
            "operator_layer_pic0_open": monad_l2["what_remains_open"][
                "operator_layer_Pic0_selection_or_quotient_for_holonomy_sensitive_data"
            ],
            "same_source_operator_provenance_open": monad_l2["what_remains_open"][
                "same_source_operator_provenance_for_routec_residual_DE_Riesz_Green_dotD"
            ],
            "next_required_artifact": monad_l2["next_required_artifact"],
        },
    }

    checks = {
        "G0_previous_next_matches_global_destab": chain["previous_chain"][
            "next_required_artifact"
        ]
        == "Q79_Selected_RouteC_Global_Destabilizer_Enumeration_or_Selected_Residual_v1",
        "G1_reduced_AH_stability_proved_but_not_full": chain[
            "global_destabilizer_enumeration"
        ]["reduced_AH_model_stability_proved"]
        and chain["global_destabilizer_enumeration"]["claims_full_stability"] is False,
        "G2_reflexive_hull_and_conditional_HYM_bridge_proved": chain[
            "ah_goodcover_promotion_hym_bridge"
        ]["reflexive_hull_reduction_proved"]
        and chain["ah_goodcover_promotion_hym_bridge"]["conditional_HYM_bridge_ready"]
        and chain["ah_goodcover_promotion_hym_bridge"]["claims_hym_unconditionally"]
        is False,
        "G3_AH_goodcover_reduced_to_source_class": chain[
            "ah_source_or_routec_residual_reduction"
        ]["ah_goodcover_equivalence_closed"]
        and chain["ah_source_or_routec_residual_reduction"][
            "selected_AH_reduced_to_terminal_lane"
        ],
        "G4_monad_L2_source_closed_under_explicit_principle": chain[
            "selected_monad_l2_source_operatorpic0_or_routec_residual"
        ]["selected_monad_L2_source_closed_under_explicit_principle"]
        and chain["selected_monad_l2_source_operatorpic0_or_routec_residual"][
            "claims_unconditional_terminal_section_principle"
        ]
        is False,
        "G5_operator_provenance_still_open": chain[
            "selected_monad_l2_source_operatorpic0_or_routec_residual"
        ]["operator_layer_pic0_open"]
        and chain["selected_monad_l2_source_operatorpic0_or_routec_residual"][
            "same_source_operator_provenance_open"
        ],
    }

    proved = all(checks.values())
    return {
        "packet": "Q79_Global_Destabilizer_AH_Monad_Source_Chain_Import_v1",
        "status": (
            "Q79_GLOBAL_DESTABILIZER_AH_MONAD_SOURCE_CHAIN_IMPORTED"
            if proved
            else "Q79_GLOBAL_DESTABILIZER_AH_MONAD_SOURCE_CHAIN_IMPORT_FAILED"
        ),
        "inputs": {
            "previous": str(PREVIOUS.relative_to(ROOT)),
            "global_destabilizer": str(GLOBAL_DESTAB),
            "ah_hym_bridge": str(AH_HYM),
            "ah_source_reduction": str(AH_SOURCE),
            "monad_l2": str(MONAD_L2),
        },
        "theorem": {
            "name": "Q79GlobalDestabilizerAHMonadSourceChainImport",
            "proved": proved,
            "statement": (
                "The q79 global-destabilizer branch is imported through the "
                "reduced AH stability theorem, conditional HYM/reflexive-hull "
                "promotion bridge, AH/good-cover source-class reduction, and "
                "selected monad L2 source closure under the explicit terminal "
                "admissible-section principle. The remaining local frontier is "
                "same-source operator provenance or a selected Route-C solve."
            ),
        },
        "import_checks": checks,
        "chain": chain,
        "decision": {
            "reduced_AH_stability_closed": True,
            "full_HYM_stability_unconditional": False,
            "selected_monad_L2_source_conditionally_closed": True,
            "operator_layer_pic0_or_routec_residual_open": True,
            "next_required_artifact": "Q79_SameSource_Operator_Provenance_or_Selected_RouteC_Solve_v1",
        },
        "guardrails": {
            "does_not_claim_full_stability_or_HYM": True,
            "does_not_claim_selected_RouteC_residual": True,
            "does_not_claim_operator_layer_Pic0_closed": True,
            "does_not_claim_A_selected_or_b_selected": True,
            "does_not_claim_selected_DE_dotD_Riesz_Green": True,
            "does_not_claim_Yukawa_or_SM_closure": True,
            "does_not_use_observed_or_benchmark_inputs": True,
        },
        "verdict": {
            "what_closes_now": (
                "Reduced AH stability and the AH/good-cover promotion logic are "
                "imported; the terminal monad L2 source closes only under the "
                "explicit admissible-section principle."
            ),
            "what_remains": (
                "Prove same-source operator provenance, including operator-layer "
                "Pic0 behavior for D_E/Riesz/Green/dotD, or supply a selected "
                "Route-C residual solve."
            ),
            "next_required_artifact": "Q79_SameSource_Operator_Provenance_or_Selected_RouteC_Solve_v1",
        },
    }


def build_certificate(packet: dict[str, Any]) -> dict[str, Any]:
    return {
        "certificate": "Q79GlobalDestabilizerAHMonadSourceChainImport",
        "status": packet["status"],
        "packet_path": str(OUTPUT_PACKET.relative_to(ROOT)),
        "note_path": str(OUTPUT_NOTE.relative_to(ROOT)),
        "theorem": packet["theorem"],
        "import_checks": packet["import_checks"],
        "decision": packet["decision"],
        "guardrails": packet["guardrails"],
        "verdict": packet["verdict"],
    }


def render_note(cert: dict[str, Any], packet: dict[str, Any]) -> str:
    return f"""# Q79 Global Destabilizer AH Monad Source Chain Import v1

## Result

Status: `{cert["status"]}`

The reduced Appell-Humbert stability lane is strong: the unbounded rank-one
line enumeration closes inside the reduced model, and the reflexive-hull/HYM
bridge is ready conditionally.  The selected monad-difference L2 source also
closes under the explicit terminal admissible-section principle.  The remaining
obstruction is operator provenance: operator-layer `Pic0` and same-source
`D_E`/Riesz/Green/`dotD`, or an honest selected Route-C residual solve.

## Import Checks

```json
{json.dumps(packet["import_checks"], indent=2, sort_keys=True)}
```

## Chain

```json
{json.dumps(packet["chain"], indent=2, sort_keys=True)}
```

## Decision

```json
{json.dumps(packet["decision"], indent=2, sort_keys=True)}
```
"""


def main() -> int:
    packet = build_packet()
    cert = build_certificate(packet)
    if "--write" in sys.argv:
        OUTPUT_PACKET.write_text(
            json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_CERT.write_text(
            json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        OUTPUT_NOTE.write_text(render_note(cert, packet), encoding="utf-8")
    print(json.dumps(cert, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
